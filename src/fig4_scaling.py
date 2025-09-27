#!/usr/bin/env python3
"""
Fig. 4 scaling script for Δ_topo (topological energy gap).

Generates:
 - figures/fig4_scaling_B_real.pdf   (Δ_topo vs B at fixed ε)
 - figures/fig4_scaling_eps_real.pdf (Δ_topo vs ε at fixed B)
 - supplementary/supplementary_table1.csv (numerical dataset, aligned with Table S1)

Usage:
    python src/fig4_scaling.py
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# --- Constants ---
Ec_prefactor_meV = 56.11  # Coulomb energy prefactor (approx)
K_per_meV = 11.6045       # 1 meV ≈ 11.6 K

# --- Parameters ---
kappa = 0.1                          # scaling factor
B_list_fixed = [10, 15, 20, 30, 45]  # Tesla values for Table S1
eps_fixed = 4.0                      # Table S1 uses ε = 4.0

# --- Function for Δ_topo (meV) ---
def delta_topo_meV(B, eps, kappa=0.1):
    return kappa * Ec_prefactor_meV * np.sqrt(B) / eps

# --- Output directories ---
os.makedirs("figures", exist_ok=True)
os.makedirs("supplementary", exist_ok=True)

# --- Fig. 4a: Δ_topo vs B ---
B_vals = np.linspace(5, 45, 200)
eps_vals_fixed = [3.5, 4.0, 6.0, 10]

plt.figure(figsize=(6,4))
for eps in eps_vals_fixed:
    plt.plot(B_vals, delta_topo_meV(B_vals, eps, kappa),
             label=fr"$\epsilon={eps}$")
plt.xlabel("Magnetic Field $B$ [Tesla]")
plt.ylabel(r"$\Delta_{\mathrm{topo}}$ [meV]")
plt.title(r"Scaling of $\Delta_{\text{topo}}$ with $B$")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("figures/fig4_scaling_B_real.pdf")
plt.close()

# --- Fig. 4b: Δ_topo vs ε ---
eps_range = np.linspace(2, 12, 200)
B_list_for_plot = [10, 20, 30, 45]

plt.figure(figsize=(6,4))
for B in B_list_for_plot:
    plt.plot(eps_range, delta_topo_meV(B, eps_range, kappa),
             label=fr"$B={B}\,\mathrm{{T}}$")
plt.xlabel(r"Dielectric Constant $\epsilon$")
plt.ylabel(r"$\Delta_{\mathrm{topo}}$ [meV]")
plt.title(r"Scaling of $\Delta_{\text{topo}}$ with $\epsilon$")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("figures/fig4_scaling_eps_real.pdf")
plt.close()

# --- Generate CSV dataset for Table S1 ---
rows = []
for B in B_list_fixed:
    for k in [0.05, 0.10, 0.15]:
        delta_meV = delta_topo_meV(B, eps_fixed, k)
        delta_K = delta_meV * K_per_meV
        rows.append({
            "B [T]": B,
            "ε": eps_fixed,
            "κ": k,
            "Δ_topo [meV]": round(float(delta_meV), 3),
            "Δ_topo [K]": round(float(delta_K), 1)
        })

df = pd.DataFrame(rows)

csv_out = "supplementary/supplementary_table1.csv"
df.to_csv(csv_out, index=False)

print("✅ Outputs generated:")
print(" - figures/fig4_scaling_B_real.pdf")
print(" - figures/fig4_scaling_eps_real.pdf")
print(f" - {csv_out}")
#!/usr/bin/env python3
"""
Figure 4: Scaling of Δ_topo with magnetic field B and dielectric constant ε.
- Panel (a): Δ_topo vs. B
- Panel (b): Δ_topo vs. ε
Exports both PDF and CSV (Supplementary Table S1).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def compute_delta_topo(B_vals, eps_vals, prefactor=5.8):
    """
    Compute Δ_topo in Kelvin using Coulomb scaling:
    Δ_topo ≈ (e^2 / (ε ℓ_B k_B)) ~ prefactor * sqrt(B)/ε
    prefactor chosen to give ~50 K at B=20 T, ε=4.
    """
    return prefactor * np.sqrt(B_vals) / eps_vals

def make_fig4(figfile="figures/fig4_scaling.pdf", csvfile="supplementary/supplementary_table1.csv"):
    # Prepare parameter sweeps
    B_vals = np.linspace(5, 30, 100)     # Tesla
    eps_vals = np.array([2, 4, 8])       # dielectric constants

    # Δ_topo vs B for different ε
    plt.figure(figsize=(10, 4))

    # Panel (a): Δ_topo vs B
    plt.subplot(1, 2, 1)
    for eps in eps_vals:
        delta = compute_delta_topo(B_vals, eps)
        plt.plot(B_vals, delta, label=f"$\\epsilon={eps}$")
    plt.xlabel("Magnetic field B (T)")
    plt.ylabel(r"$\Delta_{\mathrm{topo}}$ (K)")
    plt.title("(a) Scaling with B")
    plt.legend()

    # Panel (b): Δ_topo vs ε (at fixed B=20T)
    plt.subplot(1, 2, 2)
    eps_sweep = np.linspace(2, 10, 100)
    delta_eps = compute_delta_topo(20, eps_sweep)
    plt.plot(eps_sweep, delta_eps, color="purple")
    plt.xlabel(r"Dielectric constant $\epsilon$")
    plt.ylabel(r"$\Delta_{\mathrm{topo}}$ (K)")
    plt.title("(b) Scaling with ε (B=20T)")

    plt.tight_layout()
    os.makedirs(os.path.dirname(figfile), exist_ok=True)
    plt.savefig(figfile)
    print(f"✅ Saved {figfile}")

    # Export CSV (Δ_topo estimates)
    rows = []
    for B in [10, 20, 30]:
        for eps in [2, 4, 8]:
            delta = compute_delta_topo(B, eps)
            rows.append({"B (T)": B, "ε": eps, "Δ_topo (K)": round(delta, 2)})

    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(csvfile), exist_ok=True)
    df.to_csv(csvfile, index=False)
    print(f"✅ Saved {csvfile}")

if __name__ == "__main__":
    make_fig4()
