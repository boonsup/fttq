#!/usr/bin/env python3
"""
Polish a .bib file to make it LaTeX/arXiv-safe:
 - Escapes underscores (_) → \_
 - Normalizes en-dash (–) and em-dash (—) to double dash (--)
 - Removes/normalizes non-ASCII chars
 - Detects duplicate BibTeX keys
 - Optionally auto-renames duplicates (e.g., Willow2025a, Willow2025b)
 - Optionally sorts entries alphabetically by key
 - Generates summary report (entries, duplicates, fixes)
 - --check-only mode: scan and report issues without writing output
"""

import re
import sys
from collections import defaultdict

def polish_bib(input_file, output_file=None, auto_rename=False, sort_keys=False, check_only=False):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Split entries by @
    entries = re.split(r'(?=@\w+\{)', content)
    cleaned_entries = []
    keys_seen = defaultdict(list)
    key_counts = defaultdict(int)

    # Counters
    total_entries = 0
    duplicates_fixed = 0
    unsafe_chars_fixed = 0

    for idx, entry in enumerate(entries):
        if not entry.strip():
            continue
        total_entries += 1
        lines = entry.splitlines()
        first_line = lines[0]

        # Detect key
        m = re.match(r"(@\w+\{)([^,]+)(,)", first_line.strip())
        if m:
            prefix, key, suffix = m.groups()
            key_counts[key] += 1
            if key_counts[key] > 1 and auto_rename and not check_only:
                new_key = f"{key}{chr(96+key_counts[key])}"  # a,b,c...
                print(f"🔄 Renaming duplicate key '{key}' → '{new_key}'")
                first_line = first_line.replace(key, new_key, 1)
                key = new_key
                duplicates_fixed += 1
            keys_seen[key].append(idx + 1)
            lines[0] = first_line
        else:
            key = f"UNKNOWN_{idx}"

        # Clean each line
        polished_lines = []
        for line in lines:
            before = line
            if "_" in line and "$" not in line:
                line = line.replace("_", r"\_")
            line = line.replace("–", "--").replace("—", "--")
            line = line.replace("\u00a0", " ")
            line = re.sub(r"[^\x00-\x7F]", "", line)
            if line != before:
                unsafe_chars_fixed += 1
            polished_lines.append(line)

        cleaned_entries.append((key, "\n".join(polished_lines)))

    # Sort entries if requested and not check-only
    if sort_keys and not check_only:
        cleaned_entries.sort(key=lambda x: x[0].lower())

    # Write polished file (unless check-only)
    if not check_only and output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            for _, entry_text in cleaned_entries:
                f.write(entry_text.strip() + "\n\n")
        print(f"\n✅ Polished {input_file} → {output_file}")
    elif check_only:
        print(f"🔎 Check-only mode: scanned {input_file}, no output written")

    # Report duplicates (only if not auto-renamed)
    duplicates = {k: v for k, v in keys_seen.items() if len(v) > 1}
    if duplicates and not auto_rename:
        print("\n⚠️ Duplicate citation keys detected:")
        for key, lines in duplicates.items():
            print(f"  - {key} (appears in {len(lines)} entries)")

    # Summary report
    print("\n📊 Summary Report")
    print(f"  Total entries processed: {total_entries}")
    print(f"  Duplicates auto-renamed: {duplicates_fixed}")
    print(f"  Lines with unsafe chars fixed: {unsafe_chars_fixed}")

    # CI integration: fail if problems
    if check_only and (duplicates or unsafe_chars_fixed > 0):
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python polish_bib.py main.bib [output.bib] [--auto-rename] [--sort] [--check-only]")
    else:
        auto_flag = "--auto-rename" in sys.argv
        sort_flag = "--sort" in sys.argv
        check_flag = "--check-only" in sys.argv
        args = [a for a in sys.argv[1:] if not a.startswith("--")]

        if check_flag:
            polish_bib(args[0], None, auto_flag, sort_flag, check_flag)
        elif len(args) >= 2:
            polish_bib(args[0], args[1], auto_flag, sort_flag, check_flag)
        else:
            print("Error: must specify output file unless using --check-only")
