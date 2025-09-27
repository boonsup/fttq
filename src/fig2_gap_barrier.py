#!/usr/bin/env python3
"""
Figure 2: Energy gap barrier schematic.
Plots energy vs. state with Δ_topo highlighted,
showing ground state, excited state, and thermal noise threshold.
"""

import matplotlib.pyplot as plt

def make_fig2(filename="figures/fig2_gap_barrier.pdf"):
    fig, ax = plt.subplots(figsize=(4.5, 3.5))

    # Example energies (arbitrary scale)
    ground = 0
    excited = 1.0
    thermal = 0.2

    # Draw levels
    ax.hlines(ground, 0, 1, colors="blue", linewidth=2, label="Ground state")
    ax.hlines(excited, 0, 1, colors="red", linewidth=2, label="Excited state")

    # Thermal noise threshold
    ax.hlines(thermal, 0, 1, colors="orange", linestyle="--", label="$k_B T$")

    # Gap annotation
    ax.annotate(
        "", xy=(0.5, ground), xytext=(0.5, excited),
        arrowprops=dict(arrowstyle="<->", color="black")
    )
    ax.text(0.55, 0.5, r"$\Delta_{\mathrm{topo}}$", fontsize=11, va="center")

    # Style
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.1, 1.2)
    ax.set_xticks([])
    ax.set_ylabel("Energy (arb. units)")
    ax.legend(loc="upper left", fontsize=8)

    plt.tight_layout()
    plt.savefig(filename)
    print(f"✅ Saved {filename}")

if __name__ == "__main__":
    make_fig2()
