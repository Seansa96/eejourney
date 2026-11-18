# Geometry Mastery Diagnostic authoring sources

The parent directory contains the student PDF and the separate grader PDF. All 30 questions are original and aligned to the library sources identified in the grader packet. No textbook problem is presented as directly reproduced or adapted.

## Rebuild

Requires Python 3, `reportlab`, and Windows Arial and Segoe UI Symbol fonts. The script finds the vault-relative temporary dependency directory used during initial creation; a normal ReportLab installation also works.

```powershell
python -m pip install reportlab
python .\build_geometry_diagnostic.py
```

Run `build_geometry_diagnostic.py` from any directory. It writes both PDFs in its parent directory and a machine-readable `assessment_manifest.json` beside the script. The data, solutions, point allocations, source alignments, and diagrams are embedded in the Python source. Edit that source to revise the assessment.

## Verify and render

```powershell
python -m pip install pymupdf pillow
python .\verify_geometry_diagnostic.py
```

Verification checks content totals, independently recomputed numerical relationships, PDF page count, text boundaries, glyph mappings, response space, and absence of grader content in the student PDF. It renders every page and contact sheets into the vault's `tmp/geometry-review` directory. Inspect the full-page images for legibility and diagram/label placement; automated checks cannot replace that visual review.

The score bands are provisional instructional judgments, not a standardized assessment. The packet distinguishes topic knowledge, foundational performance, advanced transfer, and incomplete coverage. Do not infer formal proof mastery from informal explanations.
