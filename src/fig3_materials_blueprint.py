#!/usr/bin/env python3
"""
Figure 3: Materials blueprint schematic
- Twisted bilayer TMDs
- Strain arrows
- Perpendicular magnetic field
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def make_fig3(filename="figures/fig3_materials_blueprint.pdf"):
    fig, ax = plt.subplots(figsize=(4.5, 4.5))

    # Two stacked layers
    rect1 = patches.Rectangle((-0.5, -0.2), 2, 0.3, angle=2, fc="lightblue", alpha=0.7, label="MoSe2 layer")
    rect2 = patches.Rectangle((-0.6, 0.1), 2, 0.3, angle=-2, fc="lightgreen", alpha=0.7, label="WSe2 layer")
    ax.add_patch(rect1)
    ax.add_patch(rect2)

    # Strain arrows
    ax.arrow(0.5, 0.5, 0.3, 0.0, head_width=0.05, head_length=0.05, fc="red", ec="red")
    ax.arrow(0.5, 0.5, -0.3, 0.0, head_width=0.05, head_length=0.05, fc="red", ec="red")
    ax.text(0.5, 0.55, "Strain", color="red", fontsize=9, ha="center")

    # Magnetic field arrow
    ax.arrow(1.2, -0.1, 0, 0.6, head_width=0.05, head_length=0.05, fc="purple", ec="purple")
    ax.text(1.25, 0.2, "B-field", color="purple", fontsize=9, rotation=90)

    # Style
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")
    ax.legend(loc="lower right", fontsize=8)

    plt.tight_layout()
    plt.savefig(filename)
    print(f"✅ Saved {filename}")

if __name__ == "__main__":
    make_fig3()
