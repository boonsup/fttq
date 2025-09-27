# README for arXiv Submission

## Manuscript
- **Title:** Maximizing $\Delta_{\text{topo}}$ for Fault-Tolerant Topological Qubits
- **Format:** REVTeX 4.2
- **Main file:** `main.tex`
- **Figures directory:** `figures/`
- **Supplementary material:** `supplementary/`

---

## Figures
- **Fig. 1** — Conceptual schematic of an exciton-based qubit.
- **Fig. 2** — Energy barrier illustration showing Δ_topo vs. k_B T.
- **Fig. 3** — Materials blueprint for twisted 2D heterostructures.
- **Fig. 4a–b** — Quantitative scaling of Δ_topo with B and ε.
- **Fig. 5** — Benchmark roadmap: topological gap (K) vs resource overhead (physical/logical).

---

## Supplementary Information
- **Supplementary Figure S1** — Data analysis workflow (Colab schematic).  
- **Supplementary Table S1** — Example CSV output from $\Delta_{\text{topo}}$ scaling simulations.  
- **CSV datasets** — Machine-readable numerical results for $\Delta_{\text{topo}}$ vs. $B$, $\epsilon$, strain, and twist angle.  
- **Colab notebook** — Reproducible pipeline (`figures_pipeline.ipynb` + $\Delta_{\text{topo}}$ simulation).  

## Supplementary Data
All supporting datasets and scripts are available via Zenodo:
👉 https://doi.org/10.5281/zenodo.17213190

This includes:
- `supplementary_table1.csv` (raw numerical values underlying Fig. 4 & Table S1),
- `figures_pipeline.ipynb` (Colab notebook to regenerate Figures 1–4),
- workflow schematic (Fig. S1),
- generated figure PDFs.

---

## Notes for arXiv Moderators
- All figures are vector PDFs.  
- All references compile cleanly with BibTeX (`main.bib` → `main.bbl`).  
- Supplementary data and notebooks are hosted externally at Zenodo (to reduce package size).  

---

© [Year] [Author]. Licensed under CC BY-NC 4.0 (default for arXiv preprints).
