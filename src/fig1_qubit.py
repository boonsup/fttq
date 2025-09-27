#!/usr/bin/env python3
"""
Figure 1: Conceptual schematic of a topological exciton qubit.
- Two localized quasiparticles (blue/red)
- Braiding path (dashed curve)
- Poisoning event (star marker)
"""

import matplotlib.pyplot as plt

def make_fig1(filename="figures/fig1_qubit.pdf"):
    fig, ax = plt.subplots(figsize=(4, 4))

    # Qubit sites
    ax.scatter([0, 1], [0, 0], s=200, c=["blue", "red"], zorder=3)
    ax.text(0, -0.15, "Qubit site A", ha="center", fontsize=9)
    ax.text(1, -0.15, "Qubit site B", ha="center", fontsize=9)

    # Braiding path
    t = [i/100 for i in range(101)]
    x = [0.5 + 0.4 * (2*u-1) for u in t]
    y = [0.4*(1-(2*u-1)**2) for u in t]
    ax.plot(x, y, "--", c="black", lw=1.5, label="Braiding path")

    # Poisoning event
    ax.scatter([0.5], [0.25], marker="*", s=150, c="orange", edgecolor="k", zorder=4)
    ax.text(0.55, 0.35, "Quasiparticle\npoisoning", fontsize=9)

    # Style
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")
    ax.legend(loc="upper right", fontsize=8)

    plt.tight_layout()
    plt.savefig(filename)
    print(f"✅ Saved {filename}")

if __name__ == "__main__":
    make_fig1()
