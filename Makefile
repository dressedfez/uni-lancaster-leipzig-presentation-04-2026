NOTEBOOK := Dr_Frank_Zimmer_Inheritance_vs_Composition_in_Object_Oriented_Programming.py
DIST_DIR := dist
PDF := $(DIST_DIR)/inheritance-vs-composition-slides.pdf

.PHONY: check pdf clean

check:
	uv run marimo check $(NOTEBOOK)

pdf:
	mkdir -p $(DIST_DIR)
	uv run --with marimo --with nbformat --with nbconvert --with playwright marimo export pdf $(NOTEBOOK) --as=slides --raster-server=live --no-include-inputs -o $(PDF) --force

clean:
	rm -rf $(DIST_DIR)
