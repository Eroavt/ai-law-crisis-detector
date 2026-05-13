"""Streamlit demo for the AI-Law Crisis Detector.

Workshop-ready, designed for non-technical readers (Profs. Thouvenin and
Bernstein and the workshop audience). Three things only:

  1. Pick a conversation from the test corpus.
  2. See what our calibrated detector classifies it as, and what our
     safe-response module would send back.
  3. See whether the response passes the EU AI Act / Swiss-law conformity
     audit. A toggle reveals the contrast with a no-detector chatbot.

Run::

    make demo

or::

    streamlit run app/demo.py
"""

from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

import streamlit as st

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from dotenv import load_dotenv

from aldc import legal_map, regulator_view
from aldc.baselines import read_jsonl as read_baselines
from aldc.corpus_gen import read_jsonl as read_corpus
from aldc.detector import detect_one
from aldc.runtime import current_backend
from aldc.safe_response import respond
from aldc.schemas import Conversation, DetectionResult

load_dotenv(REPO_ROOT / ".env")

st.set_page_config(
    page_title="AI-Law Crisis Detector",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ----- Friendly labels for the demo conversations ---------------------------

FRIENDLY_LABELS: dict[str, str] = {
    "kst_01": "Distressed adult, method-seeking via creative-writing framing  (Raine pattern)",
    "ad_01":  "Minor forming romantic attachment to a chatbot persona  (Setzer pattern)",
    "mtd_03": "Long-running distress drift across 20+ turns  (Eliza pattern)",
    "fp_01":  "Philosophical question about meaning  (control — should NOT flag)",
    "pvi_02": "Privacy vs. intervention edge case",
}


# ----- Severity rendering ---------------------------------------------------

def severity_label(level: int) -> tuple[str, str]:
    """Return (emoji+text, colour-name) for a C-SSRS severity level."""
    table = [
        ("🟢 0 — no risk signals",                       "green"),
        ("🟢 1 — wish-to-die, no plan",                  "green"),
        ("🟡 2 — passive ideation",                      "yellow"),
        ("🟠 3 — active ideation, no plan",              "orange"),
        ("🔴 4 — active ideation with method or intent", "red"),
        ("🔴 5 — active plan and intent",                "red"),
    ]
    return table[max(0, min(5, level))]


# ----- Live detector call ---------------------------------------------------

def run_detector(convo: Conversation) -> DetectionResult:
    backend = current_backend()
    if backend == "api" and not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError(
            "ALDC_BACKEND=api but no ANTHROPIC_API_KEY is set. "
            "Set it in .env or switch to ALDC_BACKEND=claude_code."
        )
    return asyncio.run(detect_one(convo))


# ----- Page -----------------------------------------------------------------

st.title("⚖️ AI-Law Crisis Detector")
st.markdown(
    "A research artifact showing that an LLM chatbot can detect users at "
    "imminent risk of suicide and respond safely — at a cost of about nine "
    "cents per call. Built for the UZH FS26 course *AI: Technology and Law* "
    "(Profs. Thouvenin & Bernstein). The accompanying paper argues that "
    "this empirical fact turns the failure to deploy crisis detection into "
    "a foreseeable breach of the Swiss developer duty of care."
)

st.divider()

# --- Step 1: pick a conversation -------------------------------------------

st.subheader("Step 1.  Pick a conversation to evaluate")

corpus_path = REPO_ROOT / "data" / "corpus.jsonl"
if not corpus_path.exists():
    st.error("Test corpus is missing at `data/corpus.jsonl`. Run `uv sync` and retry.")
    st.stop()

corpus: list[Conversation] = read_corpus(corpus_path)
corpus_by_id: dict[str, Conversation] = {c.id: c for c in corpus}

# Show demo picks first
demo_ids = [cid for cid in FRIENDLY_LABELS if cid in corpus_by_id]
other_ids = sorted([c.id for c in corpus if c.id not in FRIENDLY_LABELS])
ordered_ids = demo_ids + other_ids


def _format_id(cid: str) -> str:
    friendly = FRIENDLY_LABELS.get(cid)
    return f"{cid}  —  {friendly}" if friendly else cid


picked_id = st.selectbox(
    "Pick from the demo set (top of the list) or any of the 35 corpus conversations:",
    ordered_ids,
    index=0,
    format_func=_format_id,
    label_visibility="visible",
)
convo: Conversation = corpus_by_id[picked_id]

# Show transcript
with st.container(border=True):
    st.caption(f"Transcript — {convo.id}  ·  {len(convo.turns)} turns")
    for i, turn in enumerate(convo.turns, 1):
        with st.chat_message(turn.role):
            st.write(turn.content)


st.divider()

# --- Step 2: our detector's classification ---------------------------------

st.subheader("Step 2.  What our detector classifies this conversation as")

state_key = f"result_{convo.id}"
result: DetectionResult | None = st.session_state.get(state_key)

if result is None:
    st.info(
        "Click the button to run the detector. It calls Claude Sonnet 4.6 with "
        "our suicide-risk-focused prompt and takes about twelve seconds."
    )
    if st.button("Run the detector", type="primary"):
        try:
            with st.spinner("Calling Claude Sonnet 4.6 …"):
                result = run_detector(convo)
            st.session_state[state_key] = result
            st.rerun()
        except Exception as exc:  # noqa: BLE001
            st.error(f"Detector call failed: {exc}")
else:
    sev_text, sev_colour = severity_label(result.cssrs_level)
    if sev_colour == "green":
        st.success(f"**C-SSRS severity:** {sev_text}")
    elif sev_colour == "yellow":
        st.warning(f"**C-SSRS severity:** {sev_text}")
    else:
        st.error(f"**C-SSRS severity:** {sev_text}")

    c1, c2, c3 = st.columns(3)
    c1.metric("Recommended action", result.recommended_action.replace("_", " "))
    c2.metric("Cost of this call", f"${result.api_cost_usd:.4f}")
    c3.metric("Latency", f"{result.latency_ms} ms")

    with st.expander("How the detector reached this rating"):
        st.markdown(f"**Reasoning trace:** {result.reasoning_trace}")
        if result.linguistic_markers:
            st.markdown("**Verbatim distress markers it picked up:**")
            for m in result.linguistic_markers:
                st.markdown(f"- *“{m}”*")

    if st.button("Reset detector for this conversation", type="secondary"):
        del st.session_state[state_key]
        st.rerun()

    st.markdown("**Our safe-response system would reply with:**")
    with st.container(border=True):
        st.write(respond(result.recommended_action))


st.divider()

# --- Step 3: AI Act / Swiss-law conformity audit ---------------------------

st.subheader("Step 3.  EU AI Act and Swiss-law conformity audit")
st.caption(
    "Twelve checks against AI Act Arts. 5(1)(a), 5(1)(b), 12, 14, 50; "
    "GDPR Art. 6(1)(b); PLD 2024/2853 Arts. 6(1)(c), 10(2)(b); "
    "Swiss StGB Art. 115; revDSG Art. 31; the Performable Duty doctrine; "
    "proportionality. Critical-only pass rate is the legally decisive figure."
)

# Load the precomputed detector-wrapped response (no live call needed here)
baselines = read_baselines(REPO_ROOT / "results" / "baselines.jsonl")
detector_wrapped = next(
    (b for b in baselines if b.conversation_id == convo.id and b.provider == "detector_wrapped"),
    None,
)
naive_response = next(
    (b for b in baselines if b.conversation_id == convo.id and b.provider == "naive_baseline"),
    None,
)

show_contrast = st.toggle(
    "Compare with a chatbot that has no crisis detection",
    value=False,
    help="When on, the audit also runs on the naive baseline (a chatbot with no safety guardrails) "
    "so you can see the contrast.",
)

if show_contrast:
    audit_columns = st.columns(2)
    audit_targets = [
        ("Without our detector", "naive_baseline", naive_response),
        ("With our detector", "detector_wrapped", detector_wrapped),
    ]
else:
    audit_columns = [st.container()]
    audit_targets = [("With our detector", "detector_wrapped", detector_wrapped)]

for col, (title, arm_id, resp) in zip(audit_columns, audit_targets):
    with col:
        with st.container(border=True):
            st.markdown(f"**{title}**")
            report = regulator_view.audit(
                convo,
                detection=result,
                response=resp,
                arm=arm_id,
            )
            if report.critical_passed:
                st.success("✅ Passes every critical check")
            else:
                st.error(
                    f"❌ Fails {len(report.failed_critical)} critical "
                    f"check{'s' if len(report.failed_critical) != 1 else ''}"
                )
                for c in report.failed_critical:
                    st.markdown(f"- `{c}`")
            st.caption(
                f"{report.n_failed} of {len(report.checks)} checks fail in total "
                f"(critical + major + minor)."
            )


st.divider()

# --- Step 4: legal mapping --------------------------------------------------

st.subheader("Step 4.  Which Swiss / EU legal provisions this case engages")

axis_tag = convo.ground_truth.legal_axis_tag
try:
    mapping = legal_map.get(axis_tag)
    with st.container(border=True):
        st.markdown(f"**Conversation type:** `{axis_tag}`")
        st.markdown(f"**Primary article:** {mapping['primary_article']}")
        if mapping["secondary_articles"]:
            st.markdown(
                "**Secondary articles:** "
                + " · ".join(mapping["secondary_articles"])
            )
        st.markdown(f"**Leading court case:** {mapping['leading_case']}")
        st.markdown(f"**Doctrinal claim:**  \n> *{mapping['doctrinal_claim']}*")
        st.caption(
            f"Paper reference:  {mapping['paper_section']}  ·  {mapping['exhibit_id']}"
        )
except KeyError:
    st.error(f"No legal mapping for axis `{axis_tag}`.")


# --- Footer -----------------------------------------------------------------

st.divider()
st.caption(
    f"Backend: `{current_backend()}`  ·  MIT-licensed research artifact  ·  "
    "© 2026 Athira Ashokan, Erik Avtandilyan, Nishant Kumar Singh  ·  "
    "[github.com/Eroavt/ai-law-crisis-detector]"
    "(https://github.com/Eroavt/ai-law-crisis-detector)"
)
