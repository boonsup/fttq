#!/usr/bin/env python3
"""
make_package.py — Build arXiv and Zenodo zip bundles
for "Maximizing Δ_topo for Fault-Tolerant Topological Qubits".
"""

import os
import zipfile

# --- Configuration ---
ARXIV_ZIP = "arxiv_submission.zip"
ZENODO_ZIP = "zenodo_bundle.zip"

# Files for arXiv (strict: only manuscript, bib, figures, supplementary)
ARXIV_FILES = [
    "main.tex",
    "main.bib",
    "further_reading.tex",
    "LICENSE",
    "manifest.txt",
    "figures/fig1_qubit.pdf",
    "figures/fig2_gap_barrier.pdf",
    "figures/fig3_materials_blueprint.pdf",
    "figures/fig4_scaling_real.pdf",
    "figures/fig4_eps_real.pdf",
    "figures/fig5_benchmark_roadmap.pdf",
    "figures/fig6_milestones_timeline.pdf",
    "supplementary/supplementary.pdf"
]

# Files for Zenodo (everything reproducible: scripts, data, readme, etc.)
ZENODO_FILES = [
    "main.tex",
    "main.bib",
    "further_reading.tex",
    "README.md",
    "README_zenodo.md",
    "LICENSE",
    "manifest.txt",
    "Makefile",
    "src/fig1_qubit.py",
    "src/fig2_gap_barrier.py",
    "src/fig3_materials_blueprint.py",
    "src/fig4_scaling.py",
    "src/figures_pipeline.ipynb",
    "figures/fig1_qubit.pdf",
    "figures/fig2_gap_barrier.pdf",
    "figures/fig3_materials_blueprint.pdf",
    "figures/fig4_scaling_real.pdf",
    "figures/fig4_eps_real.pdf",
    "figures/fig5_benchmark_roadmap.pdf",
    "figures/fig6_milestones_timeline.pdf",
    "figures/fig_graphical_abstract.pdf",
    "supplementary/supplementary.pdf",
    "supplementary/supplementary_fig1_workflow.pdf",
    "supplementary/supplementary_table1.csv",
]

def make_zip(zipname, files):
    with zipfile.ZipFile(zipname, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            if os.path.exists(f):
                zf.write(f, f)
                print(f"📦 Added {f}")
            else:
                print(f"⚠️ Missing {f}, skipped")
    print(f"\n✅ Created {zipname}")

if __name__ == "__main__":
    print("=== Building arXiv package ===")
    make_zip(ARXIV_ZIP, ARXIV_FILES)

    print("\n=== Building Zenodo package ===")
    make_zip(ZENODO_ZIP, ZENODO_FILES)
