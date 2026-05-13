"""CLI: generate workshop-ready case briefs from the curated exhibits.

For each entry in ``data/exhibit_curated.jsonl`` this produces a clean
markdown brief (title / transcript / ground truth / detector output if
available / regulator audit if available / legal mapping). Output goes to
``results/exhibit_briefs.md`` — one document the team can paste into the
workshop slide deck or the paper appendix.

Run::

    python scripts/10_build_exhibit_briefs.py
"""

from __future__ import annotations

import argparse
from pathlib import Path

from aldc import legal_map, regulator_view
from aldc.baselines import read_jsonl as read_baselines
from aldc.corpus_gen import read_jsonl as read_corpus
from aldc.detector import read_jsonl as read_detections

REPO_ROOT = Path(__file__).resolve().parents[1]


def _brief_for(convo, detection, naive_resp, det_wrapped_resp) -> str:
    out: list[str] = []
    out.append(f"## {convo.exhibit_id or convo.id}")
    out.append("")
    out.append(
        f"*Legal axis:* `{convo.ground_truth.legal_axis_tag}` — "
        f"*ground-truth C-SSRS:* {convo.ground_truth.cssrs_level} — "
        f"*expected action:* `{convo.ground_truth.expected_action}` — "
        f"*demographic:* {convo.ground_truth.demographic.age_band}"
        + (
            f", {', '.join(convo.ground_truth.demographic.context)}"
            if convo.ground_truth.demographic.context
            else ""
        )
    )
    out.append("")
    out.append("### Transcript")
    out.append("")
    for i, t in enumerate(convo.turns, 1):
        label = "USER" if t.role == "user" else "ASSISTANT"
        out.append(f"**{label} (turn {i}):** {t.content}")
        out.append("")

    if convo.generation_notes:
        out.append("### Provenance")
        out.append("")
        out.append(f"> {convo.generation_notes}")
        out.append("")

    if detection is not None:
        out.append("### Detector output")
        out.append("")
        out.append(
            f"- C-SSRS: **{detection.cssrs_level}** "
            f"(action: `{detection.recommended_action}`)"
        )
        out.append(f"- Dynamics score: {detection.dynamics_score:.2f}")
        out.append(
            "- Linguistic markers: "
            + ", ".join(f"\"{m}\"" for m in detection.linguistic_markers)
        )
        out.append("- Reasoning trace:")
        out.append(f"  > {detection.reasoning_trace}")
        out.append("")

    if naive_resp is not None:
        out.append("### Naive baseline continuation")
        out.append("")
        out.append(f"> {naive_resp.full_response_text[:500]}{'...' if len(naive_resp.full_response_text) > 500 else ''}")
        out.append("")

    if det_wrapped_resp is not None:
        out.append("### Detector-wrapped continuation")
        out.append("")
        out.append(f"> {det_wrapped_resp.full_response_text[:500]}{'...' if len(det_wrapped_resp.full_response_text) > 500 else ''}")
        out.append("")

    try:
        mapping = legal_map.get(convo.ground_truth.legal_axis_tag)  # type: ignore[arg-type]
        out.append("### Legal mapping")
        out.append("")
        out.append(f"- **Primary article:** {mapping['primary_article']}")
        if mapping["secondary_articles"]:
            out.append(
                f"- **Secondary articles:** {', '.join(mapping['secondary_articles'])}"
            )
        out.append(f"- **Leading case:** {mapping['leading_case']}")
        out.append(f"- **Paper section:** {mapping['paper_section']}")
        out.append("- **Doctrinal claim:**")
        out.append(f"  > {mapping['doctrinal_claim']}")
        out.append("")
    except KeyError:
        out.append("### Legal mapping")
        out.append("")
        out.append("*No mapping registered for this axis tag.*")
        out.append("")

    if detection is not None and naive_resp is not None:
        report = regulator_view.audit(
            convo, detection=detection, response=naive_resp, arm="naive_baseline"
        )
        out.append("### Regulator-Mode audit (naive baseline)")
        out.append("")
        if report.critical_passed:
            out.append("✅ No critical AI Act / PLD violations.")
        else:
            out.append("❌ Critical failures: " + ", ".join(report.failed_critical))
        out.append("")

    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build workshop-ready exhibit briefs.")
    parser.add_argument(
        "--exhibits",
        type=Path,
        default=REPO_ROOT / "data" / "exhibit_curated.jsonl",
    )
    parser.add_argument(
        "--corpus",
        type=Path,
        default=REPO_ROOT / "data" / "corpus.jsonl",
        help="Optional: include selected corpus conversations as exhibits.",
    )
    parser.add_argument(
        "--detections",
        type=Path,
        default=REPO_ROOT / "results" / "detections.jsonl",
    )
    parser.add_argument(
        "--baselines",
        type=Path,
        default=REPO_ROOT / "results" / "baselines.jsonl",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=REPO_ROOT / "results" / "exhibit_briefs.md",
    )
    args = parser.parse_args()

    exhibits = read_corpus(args.exhibits)
    detections = (
        {d.conversation_id: d for d in read_detections(args.detections) if d.rater_id == "rater_1_opus_t0"}
        if args.detections.exists()
        else {}
    )
    baselines = (
        {(b.conversation_id, b.provider): b for b in read_baselines(args.baselines)}
        if args.baselines.exists()
        else {}
    )

    lines: list[str] = []
    lines.append("# Exhibit Briefs — *Duty, Defect, and Disclosure*")
    lines.append("")
    lines.append(
        f"Workshop-ready case briefs derived from `data/exhibit_curated.jsonl`. "
        f"{len(exhibits)} exhibits. Generated by `scripts/10_build_exhibit_briefs.py`."
    )
    lines.append("")

    for exh in exhibits:
        det = detections.get(exh.id)
        naive = baselines.get((exh.id, "naive_baseline"))
        dwrap = baselines.get((exh.id, "detector_wrapped"))
        lines.append(_brief_for(exh, det, naive, dwrap))
        lines.append("")
        lines.append("---")
        lines.append("")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines))
    print(f"Wrote {len(exhibits)} exhibit briefs to {args.out}")


if __name__ == "__main__":
    main()
