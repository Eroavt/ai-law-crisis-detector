"""Build a single consolidated `paper/PAPER_FINAL_DRAFT.md`.

Reads the 16 separate paper section files, merges them in proper document
order, strips internal "Revision notes for ..." footers, and writes one
clean Markdown document. Footnote numbering is preserved as-is (each
section has its own range — Document C §3 uses 3xx, §4 uses 4xx, etc.);
Word import or Pandoc conversion can renumber if continuous numbering is
preferred. ``[VERIFY: ...]`` tags are preserved so Athira can find them.

Run::

    python scripts/build_paper_final.py
"""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PAPER = REPO / "paper"

# Document order
ORDER = [
    ("Title page", "title_page.md"),
    ("Abstract", "abstract.md"),
    ("Document A — Problem and Solution", "document_a.md"),
    ("Document B — Project Description", "document_b.md"),
    ("Document C §1 — Introduction and Research Statement", "document_c_01_introduction.md"),
    ("Document C §2 — Methodology and Scope", "document_c_02_methodology.md"),
    ("Document C §3 — Duty of Care: Art. 41 OR and the Performable Duty Doctrine", "document_c_03_duty_of_care.md"),
    ("Document C §4 — Defect: Product Liability and the PrHG Gap", "document_c_04_defect.md"),
    ("Document C §5 — Disclosure: Privacy, Detection, and the Vital-Interests Bridge", "document_c_05_disclosure.md"),
    ("Document C §6 — Manipulation and Criminal Liability", "document_c_06_manipulation.md"),
    ("Document C §7 — The Seductive Overreach of Neuro-Predictive Safety Claims", "document_c_07_neuro_overreach.md"),
    ("Document C §8 — Counterarguments and Replies", "document_c_08_counterarguments.md"),
    ("Document C §9 — Conclusion and Policy Recommendations", "document_c_09_conclusion.md"),
    ("Bibliography", "bibliography.md"),
    ("Declaration of Originality", "declaration_of_originality.md"),
    ("List of Technical Tools (UZH §4.5 disclosure)", "list_of_technical_tools.md"),
]

REVISION_FOOTER_PATTERN = re.compile(
    r"\n---\n\n\*Revision notes for [^\n]*\*:?.*?$",
    re.DOTALL | re.IGNORECASE,
)

INTERNAL_NOTE_BLOCK = re.compile(
    r"^> \*\*[^*]*for Athira[^*]*\*\*[^\n]*\n",
    re.MULTILINE | re.IGNORECASE,
)


def _strip_revision_notes(text: str) -> str:
    """Strip the section-end revision-notes footer."""
    return REVISION_FOOTER_PATTERN.sub("", text).rstrip() + "\n"


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


def main() -> None:
    parts: list[str] = []
    parts.append("# Duty, Defect, and Disclosure")
    parts.append("")
    parts.append(
        "Reassessing Developer Liability for LLM Chatbots in Suicidal Crises "
        "under Swiss and European Law"
    )
    parts.append("")
    parts.append("*Athira Ashokan / Erik Avtandilyan / Nishant Kumar Singh*")
    parts.append("")
    parts.append(
        "University of Zurich, Faculty of Law — *Artificial Intelligence: "
        "Technology and Law* (FS26)"
    )
    parts.append("")
    parts.append(
        "Submitted on 15 May 2026. Lecturers: Prof. Dr. iur. Florent Thouvenin "
        "and Prof. Abraham Bernstein, PhD."
    )
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(
        "**Note on this document.** This is the consolidated single-file "
        "draft generated from the artifact repository on 12 May 2026. "
        "Section-internal revision-notes footers have been removed for "
        "submission readiness. Footnote numbering follows the per-section "
        "convention used in the source files (Document C §3 uses 3xx, §4 "
        "uses 4xx, etc.) so any conversion to continuous numbering for the "
        "Word-formatted submission is straightforward."
    )
    parts.append("")
    parts.append(
        "[VERIFY] tags in the footnotes mark commentary citations that "
        "require Athira's UZH-library access (swisslex.ch, jusletter.weblaw.ch) "
        "to verify paragraph numbers. The legal arguments themselves are "
        "complete; the [VERIFY] tags are paragraph-number polish."
    )
    parts.append("")
    parts.append("---")
    parts.append("")

    for title, filename in ORDER:
        path = PAPER / filename
        if not path.exists():
            print(f"missing: {filename}")
            continue
        raw = path.read_text()
        body = _strip_revision_notes(raw)
        body = _strip_first_heading(body)
        parts.append(f"\n\n---\n\n# {title}\n")
        parts.append(body)

    out = PAPER / "PAPER_FINAL_DRAFT.md"
    out.write_text("\n".join(parts) + "\n")

    # Stats
    text = out.read_text()
    print(f"Wrote {out}")
    print(f"  Total characters: {len(text):,}")
    print(f"  Total words: {len(text.split()):,}")
    print(f"  Total lines: {len(text.splitlines()):,}")
    # Verify counts
    n_verify = text.count("[VERIFY")
    n_revision_notes = text.lower().count("revision notes for")
    print(f"  [VERIFY] tags remaining for Athira: {n_verify}")
    print(f"  Revision-notes footers remaining (should be 0): {n_revision_notes}")


if __name__ == "__main__":
    main()
