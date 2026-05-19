# Inheritance vs. Composition in Object-Oriented Programming

This repository contains the source material for an academic talk by Dr. Frank Zimmer on the design trade-offs between inheritance and composition in object-oriented programming. The talk introduces the conceptual distinction between `is-a` and `has-a` relationships, demonstrates both approaches with Python examples, and discusses their implications for reuse, coupling, flexibility, and maintainability.

The material was prepared for the University of Lancashire Leipzig Talk, April 2026, as part of an application to a professorship.

## Contents

- `Dr_Frank_Zimmer_Inheritance_vs_Composition_in_Object_Oriented_Programming.py` - marimo source notebook for the talk
- `layouts/` - marimo slide layout metadata
- `pictures/` - AI-generated visual assets used in the slides
- `dist/` - generated publication artifacts, including the PDF version of the talk

## Running the Talk

The talk is authored as a [marimo](https://marimo.io/) notebook. It uses inline script metadata, so it can be run with `uv`:

```bash
uv run marimo run Dr_Frank_Zimmer_Inheritance_vs_Composition_in_Object_Oriented_Programming.py
```

To edit the source notebook:

```bash
uv run marimo edit Dr_Frank_Zimmer_Inheritance_vs_Composition_in_Object_Oriented_Programming.py
```

## Exporting

Check the notebook before exporting:

```bash
uv run marimo check Dr_Frank_Zimmer_Inheritance_vs_Composition_in_Object_Oriented_Programming.py
```

Export the slide deck as a PDF:

```bash
make pdf
```

The PDF export is provided as a convenient static version of the talk. It may not reproduce the interactive marimo presentation perfectly, especially with respect to slide layout, output rendering, and browser-dependent formatting.

## Asset Credits

The images in `pictures/` are AI-generated visual assets prepared for this talk.

## Citation

If you refer to this talk, please cite it as:

> Dr. Frank Zimmer. 2026. *Inheritance vs. Composition in Object-Oriented Programming*. University of Lancashire Leipzig Talk, April 2026.

Machine-readable citation metadata is provided in `CITATION.cff`.

## License

This work is licensed under the Creative Commons Attribution 4.0 International License. See `LICENSE` for details.
