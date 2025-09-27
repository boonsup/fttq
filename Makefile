# ===========================
# LaTeX build targets
# ===========================

all: main.pdf supplementary.pdf

main.pdf: main.tex main.bib figures/*.pdf
	pdflatex main.tex
	bibtex main
	pdflatex main.tex
	pdflatex main.tex

supplementary.pdf: supplementary.tex supplementary/*.csv supplementary/*.pdf
	pdflatex supplementary.tex
	bibtex supplementary || true
	pdflatex supplementary.tex
	pdflatex supplementary.tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.fdb_latexmk *.fls *.synctex.gz
	rm -f supplementary/*.aux supplementary/*.bbl supplementary/*.blg supplementary/*.log supplementary/*.out

# ===========================
# Packaging
# ===========================

package:
	@echo "📦 Building arXiv + Zenodo packages..."
	python make_package.py

# ===========================
# Convenience
# ===========================

figures:
	python src/fig1_qubit.py
	python src/fig2_gap_barrier.py
	python src/fig3_materials_blueprint.py
	python src/fig4_scaling.py
