"""Build a single consolidated `paper/PAPER_FINAL_DRAFT.md`.

Reads the per-section paper files, merges them in proper document order,
strips internal "Revision notes for ..." footers and the meta-instruction
blockquotes that target Athira / Erik / Nishant, and writes one clean
Markdown document with YAML metadata for the cover page and explicit
page-break markers before each top-level section. Footnote numbering is
preserved as-is.

Run::

    python scripts/build_paper_final.py
"""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PAPER = REPO / "paper"

# Front matter (Roman-numbered in the eventual Word version) plus body.
# Each entry will start on a new page in both the .pdf and .docx outputs.
ORDER = [
    ("Abbreviations", "list_of_abbreviations.md"),
    ("Abstract", "abstract.md"),
    ("Document A: Problem and Solution", "document_a.md"),
    ("Document B: Project Description", "document_b.md"),
    ("Document C §1: Introduction and Research Statement", "document_c_01_introduction.md"),
    ("Document C §2: Methodology and Scope", "document_c_02_methodology.md"),
    ("Document C §3: Duty of Care under Art. 41 OR and the Performable Duty Doctrine", "document_c_03_duty_of_care.md"),
    ("Document C §4: Defect, Product Liability, and the PrHG Gap", "document_c_04_defect.md"),
    ("Document C §5: Disclosure, Privacy, Detection, and the Vital-Interests Bridge", "document_c_05_disclosure.md"),
    ("Document C §6: Manipulation and Criminal Liability", "document_c_06_manipulation.md"),
    ("Document C §7: The Seductive Overreach of Neuro-Predictive Safety Claims", "document_c_07_neuro_overreach.md"),
    ("Document C §8: Counterarguments and Replies", "document_c_08_counterarguments.md"),
    ("Document C §9: Conclusion and Policy Recommendations", "document_c_09_conclusion.md"),
    ("Bibliography", "bibliography.md"),
    ("List of Technical Tools (UZH §4.5 disclosure)", "list_of_technical_tools.md"),
    ("Declaration of Originality", "declaration_of_originality.md"),
]

REVISION_FOOTER_PATTERN = re.compile(
    r"\n---\n\n\*[A-Z][^\n]*\*:?.*?$",
    re.DOTALL,
)

META_BLOCKQUOTE_PATTERN = re.compile(
    r"^>\s*\*\*[^*]*(for Athira|for Erik|for Nishant|Layout note|Status:|Formatting note)[^*]*\*\*[\s\S]*?(?=\n\n|\Z)",
    re.MULTILINE | re.IGNORECASE,
)

HORIZONTAL_RULE_LINE = re.compile(r"^[ \t]*---[ \t]*$", re.MULTILINE)

# YAML metadata block. Pandoc reads this to generate the title page in
# .pdf and the title block in .docx. Erik replaces the .docx title block
# with the §4.1-formatted cover page before submission.
YAML_FRONT_MATTER = """\
---
title: "Duty, Defect, and Disclosure"
subtitle: "Reassessing Developer Liability for LLM Chatbots in Suicidal Crises under Swiss and European Law"
author:
  - Athira Ashokan
  - Erik Avtandilyan
  - Nishant Kumar Singh
date: "15 May 2026"
lang: en
documentclass: scrartcl
classoption:
  - 12pt
  - a4paper
  - titlepage
  - twoside=false
header-includes:
  - \\usepackage{microtype}
  - \\usepackage{booktabs}
  - \\usepackage{longtable}
  - \\renewcommand{\\arraystretch}{1.15}
  - \\setkomafont{title}{\\rmfamily\\bfseries}
  - \\setkomafont{subtitle}{\\rmfamily\\itshape}
  - \\setkomafont{author}{\\rmfamily}
  - \\setkomafont{date}{\\rmfamily}
  - \\setkomafont{publishers}{\\rmfamily\\normalsize}
  - \\setkomafont{section}{\\rmfamily\\bfseries\\large}
  - \\setkomafont{subsection}{\\rmfamily\\bfseries\\normalsize}
  - \\setkomafont{subsubsection}{\\rmfamily\\bfseries\\normalsize}
  - '\\publishers{University of Zurich\\\\Faculty of Law\\\\[0.6em]Course: \\emph{Artificial Intelligence: Technology and Law} (FS26)\\\\Lecturers: Prof.~Dr.~iur.~Florent Thouvenin\\\\Prof.~Abraham Bernstein, PhD}'
---
"""

# Page break inserted before each top-level section. Pandoc emits the
# appropriate construct per output format (\\newpage for LaTeX/PDF,
# raw OOXML w:br type=page for DOCX).
PAGE_BREAK_MD = """
```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\\newpage
```
"""


def _strip_revision_notes(text: str) -> str:
    """Strip the section-end revision-notes footer and similar meta blocks."""
    # Find the last '---' followed by a *Name:* or similar coordination footer
    # and cut everything from there to the end.
    m = re.search(
        r"\n---\n\s*\*(?:Revision notes|Notes for|Substantive contribution|Read-through|Open question|Commentary status)[^\n]*",
        text,
        flags=re.IGNORECASE,
    )
    if m:
        return text[: m.start()].rstrip() + "\n"
    return text


def _strip_meta_blockquotes(text: str) -> str:
    """Strip coordination blockquotes that target the team."""
    return META_BLOCKQUOTE_PATTERN.sub("", text).strip()


def _strip_first_heading(text: str) -> str:
    """Drop the leading ``# Title`` heading; we add a wrapper instead."""
    lines = text.splitlines()
    out: list[str] = []
    dropped_first_heading = False
    for line in lines:
        if not dropped_first_heading and line.startswith("# "):
            dropped_first_heading = True
            continue
        out.append(line)
    return "\n".join(out).strip()


def _strip_internal_hr(text: str) -> str:
    """Strip horizontal-rule lines that were Markdown section dividers."""
    return HORIZONTAL_RULE_LINE.sub("", text)


def main() -> None:
    parts: list[str] = []
    parts.append(YAML_FRONT_MATTER)

    for index, (title, filename) in enumerate(ORDER):
        path = PAPER / filename
        if not path.exists():
            print(f"missing: {filename}")
            continue
        raw = path.read_text()
        body = _strip_revision_notes(raw)
        body = _strip_meta_blockquotes(body)
        body = _strip_first_heading(body)
        body = _strip_internal_hr(body)

        if index > 0:
            parts.append(PAGE_BREAK_MD)
        parts.append(f"\n# {title}\n")
        parts.append(body)

    out = PAPER / "PAPER_FINAL_DRAFT.md"
    out.write_text("\n".join(parts) + "\n")

    # Stats
    text = out.read_text()
    print(f"Wrote {out}")
    print(f"  Total characters: {len(text):,}")
    print(f"  Total words: {len(text.split()):,}")
    print(f"  Total lines: {len(text.splitlines()):,}")
    n_verify = text.count("[VERIFY")
    print(f"  [VERIFY] tags remaining: {n_verify}")
    # Page-break Markdown blocks include '---' lines via raw HTML/openxml,
    # so only count true text-content rules:
    n_true_hr = sum(
        1 for line in text.splitlines()
        if line.strip() == "---"
    )
    print(f"  Horizontal rules remaining: {n_true_hr}")


if __name__ == "__main__":
    main()
