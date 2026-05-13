"""Build the final UZH-§6-compliant submission DOCX from the Markdown source.

Steps:
1. Generate a reference.docx with UZH §6 styles: Times New Roman 12,
   1.5 line spacing, 2.5/4/2.5/2 cm margins (top/left/bottom/right),
   justified with hyphenation, A4. Body, Heading 1-3, Footnote Text,
   and a custom Bibliography Entry style with SMALL CAPS for author surnames.
2. Run pandoc to convert paper/PAPER_FINAL_DRAFT.md → paper/submission.docx
   using the reference template.
3. Also generate paper/submission.pdf via pandoc/LaTeX for visual review.

Run::

    uv run python scripts/build_submission_docx.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Cm, Pt

REPO = Path(__file__).resolve().parents[1]
PAPER = REPO / "paper"
REFERENCE_DOCX = PAPER / "reference.docx"
SOURCE_MD = PAPER / "PAPER_FINAL_DRAFT.md"
OUT_DOCX = PAPER / "submission.docx"
OUT_PDF = PAPER / "submission.pdf"


def _set_run_font(run, *, name="Times New Roman", size_pt=12, small_caps=False):
    run.font.name = name
    run.font.size = Pt(size_pt)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    rfonts.set(qn("w:ascii"), name)
    rfonts.set(qn("w:hAnsi"), name)
    rfonts.set(qn("w:cs"), name)
    if small_caps:
        sc = OxmlElement("w:smallCaps")
        sc.set(qn("w:val"), "1")
        rpr.append(sc)


def _set_paragraph_alignment(p, *, justify=True, line_spacing=1.5):
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if justify else WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.line_spacing = line_spacing
    pf.space_before = Pt(0)
    pf.space_after = Pt(6)


def _enable_hyphenation(doc):
    """Turn on automatic hyphenation across the document."""
    settings = doc.settings.element
    auto_hy = OxmlElement("w:autoHyphenation")
    auto_hy.set(qn("w:val"), "1")
    settings.append(auto_hy)


def _set_page_margins_and_size(doc):
    """A4, 2.5 cm top, 4 cm left, 2.5 cm bottom, 2 cm right (UZH §6)."""
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.5)
    section.left_margin = Cm(4.0)
    section.bottom_margin = Cm(2.5)
    section.right_margin = Cm(2.0)
    section.header_distance = Cm(1.25)
    section.footer_distance = Cm(1.25)


def _style_existing(doc, style_name, *, size_pt=12, bold=False, italic=False,
                    space_before=0, space_after=6, line_spacing=1.5,
                    justify=True, small_caps=False):
    style = doc.styles[style_name]
    style.font.name = "Times New Roman"
    style.font.size = Pt(size_pt)
    style.font.bold = bold
    style.font.italic = italic
    if hasattr(style, "paragraph_format"):
        pf = style.paragraph_format
        pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
        pf.line_spacing = line_spacing
        pf.space_before = Pt(space_before)
        pf.space_after = Pt(space_after)
        pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if justify else WD_ALIGN_PARAGRAPH.LEFT
    # Force the rFonts so Word doesn't fall back to Calibri
    rpr = style.element.find(qn("w:rPr"))
    if rpr is None:
        rpr = OxmlElement("w:rPr")
        style.element.insert(0, rpr)
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    rfonts.set(qn("w:ascii"), "Times New Roman")
    rfonts.set(qn("w:hAnsi"), "Times New Roman")
    rfonts.set(qn("w:cs"), "Times New Roman")
    if small_caps:
        sc = rpr.find(qn("w:smallCaps"))
        if sc is None:
            sc = OxmlElement("w:smallCaps")
            sc.set(qn("w:val"), "1")
            rpr.append(sc)


def build_reference_docx():
    """Generate the UZH §6 reference template."""
    doc = Document()
    _set_page_margins_and_size(doc)
    _enable_hyphenation(doc)

    # Body
    _style_existing(doc, "Normal", size_pt=12, line_spacing=1.5, justify=True,
                    space_after=6)

    # Headings (sizes follow UZH §4.1 guidance for body papers)
    _style_existing(doc, "Heading 1", size_pt=16, bold=True, justify=False,
                    space_before=18, space_after=12, line_spacing=1.15)
    _style_existing(doc, "Heading 2", size_pt=14, bold=True, justify=False,
                    space_before=14, space_after=8, line_spacing=1.15)
    _style_existing(doc, "Heading 3", size_pt=12, bold=True, justify=False,
                    space_before=10, space_after=6, line_spacing=1.15)

    # Footnote text
    for sn in ("Footnote Text", "footnote text"):
        if sn in doc.styles:
            _style_existing(doc, sn, size_pt=10, line_spacing=1.15,
                            space_after=2, justify=True)
            break

    # Bibliography Entry: hanging indent + SMALL CAPS will be applied via
    # explicit run-level smallCaps in the body for the surname token only;
    # the style itself is plain Times New Roman 12, 1.0 line spacing for
    # space efficiency and a 6 pt space-after between entries.
    if "Bibliography Entry" not in doc.styles:
        from docx.enum.style import WD_STYLE_TYPE
        doc.styles.add_style("Bibliography Entry", WD_STYLE_TYPE.PARAGRAPH)
    _style_existing(doc, "Bibliography Entry", size_pt=12, line_spacing=1.15,
                    space_after=6, justify=True, small_caps=False)

    # Save the reference
    REFERENCE_DOCX.parent.mkdir(parents=True, exist_ok=True)
    doc.save(REFERENCE_DOCX)
    print(f"  Wrote {REFERENCE_DOCX}")


def run_pandoc_docx():
    """Convert PAPER_FINAL_DRAFT.md → submission.docx using the reference."""
    if not shutil.which("pandoc"):
        sys.exit("pandoc not found on PATH")
    cmd = [
        "pandoc",
        str(SOURCE_MD),
        "-o", str(OUT_DOCX),
        "--reference-doc", str(REFERENCE_DOCX),
        "--from", "markdown+yaml_metadata_block+footnotes+pipe_tables",
        "--to", "docx",
        "--standalone",
        "--toc",
        "--toc-depth=3",
    ]
    print("  " + " ".join(cmd))
    subprocess.run(cmd, check=True)
    print(f"  Wrote {OUT_DOCX}")


def run_pandoc_pdf():
    """Convert PAPER_FINAL_DRAFT.md → submission.pdf for visual review.

    Requires a TeX engine (xelatex preferred, falls back to pdflatex).
    Skipped silently if no TeX is installed.
    """
    if not shutil.which("pandoc"):
        return
    engines = ["xelatex", "lualatex", "pdflatex"]
    engine = next((e for e in engines if shutil.which(e)), None)
    if engine is None:
        print("  (no TeX engine found; skipping PDF generation)")
        return
    cmd = [
        "pandoc",
        str(SOURCE_MD),
        "-o", str(OUT_PDF),
        "--from", "markdown+yaml_metadata_block+footnotes+pipe_tables",
        "--pdf-engine", engine,
        "--standalone",
        "--toc",
        "--toc-depth=3",
        "-V", "papersize=a4",
        "-V", "geometry:top=2.5cm,left=4cm,bottom=2.5cm,right=2cm",
        "-V", "mainfont=Times New Roman" if engine in ("xelatex", "lualatex") else "fontfamily=times",
        "-V", "fontsize=12pt",
        "-V", "linestretch=1.5",
    ]
    print("  " + " ".join(cmd))
    try:
        subprocess.run(cmd, check=True)
        print(f"  Wrote {OUT_PDF}")
    except subprocess.CalledProcessError as e:
        print(f"  PDF generation failed (engine={engine}); the DOCX is still usable.")
        print(f"  {e}")


def main():
    print("[1/3] Generating UZH §6 reference template...")
    build_reference_docx()
    print("[2/3] Converting Markdown → DOCX via Pandoc...")
    run_pandoc_docx()
    print("[3/3] Generating PDF preview (optional)...")
    run_pandoc_pdf()
    print()
    print("Submission artifacts:")
    print(f"  {OUT_DOCX}  ({OUT_DOCX.stat().st_size:,} bytes)")
    if OUT_PDF.exists():
        print(f"  {OUT_PDF}  ({OUT_PDF.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
