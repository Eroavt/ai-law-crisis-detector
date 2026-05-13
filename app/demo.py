"""Streamlit demo — the workshop-presentation hinge.

Pick a corpus conversation (or paste a custom one), run the detector live,
view the naive / policy-only / detector-wrapped baselines side-by-side, and
read the legal mapping that ties the case to a Swiss / EU article.

Run::

    streamlit run app/demo.py
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

import streamlit as st

# Allow running via ``streamlit run app/demo.py`` from any CWD.
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
from aldc.schemas import Conversation, DetectionResult, GroundTruth, ProviderResponse, Turn

load_dotenv(REPO_ROOT / ".env")

st.set_page_config(
    page_title="ALDC — AI-Law Crisis Detector",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ----- helpers --------------------------------------------------------------


@st.cache_data(show_spinner=False)
def _load_corpus(path: str) -> list[Conversation]:
    p = Path(path)
    if not p.exists():
        return []
    return read_corpus(p)


@st.cache_data(show_spinner=False)
def _load_baselines(path: str) -> list[ProviderResponse]:
    p = Path(path)
    if not p.exists():
        return []
    return read_baselines(p)


def _baselines_for(
    convo_id: str, baselines: list[ProviderResponse]
) -> dict[str, ProviderResponse]:
    return {b.provider: b for b in baselines if b.conversation_id == convo_id}


def _run_detector_sync(convo: Conversation) -> DetectionResult:
    """Wrap the async detect_one call so the Streamlit UI can call it inline.

    The detector now routes through ``aldc.runtime``, which picks between the
    Max-routed ``claude_code`` backend (default) and the paid ``api`` backend
    via the ``ALDC_BACKEND`` env var. No client object needs to be passed.
    """
    backend = current_backend()
    if backend == "api" and not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError(
            "ALDC_BACKEND=api but ANTHROPIC_API_KEY is unset. "
            "Either set the key in .env at the repo root, or switch to "
            "ALDC_BACKEND=claude_code (Max subscription)."
        )

    async def _go() -> DetectionResult:
        return await detect_one(convo)

    return asyncio.run(_go())


def _render_turns(convo: Conversation) -> None:
    for i, turn in enumerate(convo.turns, 1):
        with st.chat_message(turn.role):
            st.caption(f"turn {i}")
            st.write(turn.content)


def _ground_truth_panel(convo: Conversation) -> None:
    gt = convo.ground_truth
    st.markdown(f"**C-SSRS:** `{gt.cssrs_level}`")
    st.markdown(
        f"**ASQ:** Q1={gt.asq_responses[0]} Q2={gt.asq_responses[1]} "
        f"Q3={gt.asq_responses[2]} Q4={gt.asq_responses[3]}"
    )
    st.markdown(f"**Expected action:** `{gt.expected_action}`")
    st.markdown(f"**Legal axis:** `{gt.legal_axis_tag}`")
    st.markdown(
        f"**Demographic:** {gt.demographic.age_band}, "
        f"context={gt.demographic.context or '—'}"
    )
    if convo.exhibit_id:
        st.caption(f"Paper {convo.exhibit_id}")
    if convo.generation_notes:
        st.caption(convo.generation_notes)


def _detector_panel(result: DetectionResult) -> None:
    sev = result.cssrs_level
    color = (
        "🟢" if sev <= 1 else "🟡" if sev == 2 else "🟠" if sev == 3 else "🔴"
    )
    st.markdown(f"**{color} C-SSRS:** `{sev}` — action `{result.recommended_action}`")
    asq = result.asq_responses
    st.markdown(f"**ASQ:** Q1={asq[0]} Q2={asq[1]} Q3={asq[2]} Q4={asq[3]}")
    st.markdown(f"**Dynamics score:** {result.dynamics_score:.2f}")
    if result.linguistic_markers:
        with st.expander("Linguistic markers (verbatim spans)"):
            for m in result.linguistic_markers:
                st.markdown(f"- *{m}*")
    with st.expander("Reasoning trace"):
        st.write(result.reasoning_trace)
    st.caption(
        f"{result.model_version} @ T={result.temperature} • "
        f"${result.api_cost_usd:.4f} • {result.latency_ms} ms"
    )


def _baseline_panel(arm: str, response: ProviderResponse | None) -> None:
    if response is None:
        st.info(
            f"No precomputed `{arm}` continuation in `results/baselines.jsonl`. "
            "Run `scripts/03_run_baselines.py` first."
        )
        return
    st.write(response.full_response_text)
    st.caption(
        f"{response.model_version} • ${response.api_cost_usd:.4f} • "
        f"{response.latency_ms} ms"
    )
    if response.flagged_for_safety:
        st.success("✓ flagged by detector → templated safe response")


def _legal_panel(axis_tag: str) -> None:
    try:
        mapping = legal_map.get(axis_tag)  # type: ignore[arg-type]
    except KeyError:
        st.error(
            f"No legal mapping for axis `{axis_tag}`. "
            "Demo refuses to render — see `legal_map.py` (technical-legal contract)."
        )
        return
    st.markdown(f"**Primary article:** {mapping['primary_article']}")
    if mapping["secondary_articles"]:
        st.markdown(
            "**Secondary articles:** " + ", ".join(mapping["secondary_articles"])
        )
    st.markdown(f"**Leading case:** {mapping['leading_case']}")
    st.markdown(f"**Doctrinal claim:**")
    st.markdown(f"> {mapping['doctrinal_claim']}")
    st.caption(
        f"Paper section {mapping['paper_section']} • {mapping['exhibit_id']}"
    )


def _safe_response_preview(action: str) -> None:
    with st.expander(
        f"Templated safe-response text for action `{action}`",
        expanded=False,
    ):
        st.write(respond(action))  # type: ignore[arg-type]


# ----- UI -------------------------------------------------------------------

st.title("ALDC — AI-Law Crisis Detector")
st.caption(
    "Research artifact for *Duty, Defect, and Disclosure* (UZH FS26 AI: Tech & Law). "
    "Each test case probes a specific Swiss / EU legal article — see the rightmost panel."
)

corpus_path = st.sidebar.text_input(
    "Corpus JSONL", str(REPO_ROOT / "data" / "corpus.jsonl")
)
baselines_path = st.sidebar.text_input(
    "Baselines JSONL", str(REPO_ROOT / "results" / "baselines.jsonl")
)

corpus = _load_corpus(corpus_path)
baselines = _load_baselines(baselines_path)

with st.sidebar:
    st.markdown(
        f"Corpus: **{len(corpus)}** conversations  \n"
        f"Baselines: **{len(baselines)}** continuations"
    )
    legal_map.assert_total()
    st.success("Legal map: total ✓")

if not corpus:
    st.warning(
        "No corpus loaded. Run `scripts/01_generate_corpus.py` first, or paste a "
        "conversation manually below."
    )

option_labels = [
    f"{c.id} — sev {c.ground_truth.cssrs_level} — {c.ground_truth.legal_axis_tag}"
    for c in corpus
]

mode = st.sidebar.radio("Conversation source", ["From corpus", "Paste custom"])
selected_convo: Conversation | None = None

if mode == "From corpus" and corpus:
    idx = st.sidebar.selectbox(
        "Pick a conversation", range(len(corpus)), format_func=lambda i: option_labels[i]
    )
    selected_convo = corpus[idx]
elif mode == "Paste custom":
    raw = st.sidebar.text_area(
        "Paste conversation as JSON",
        height=240,
        placeholder='{"id":"raine_01","turns":[{"role":"user","content":"..."}],"ground_truth":{"cssrs_level":4,"asq_responses":[true,true,true,false],"legal_axis_tag":"method_availability","expected_action":"emergency_intervention","demographic":{"age_band":"adult_18_64","context":["divorced","isolated"]}}}',
    )
    if raw.strip():
        try:
            selected_convo = Conversation.model_validate_json(raw)
        except Exception as exc:  # noqa: BLE001
            st.sidebar.error(f"Invalid JSON: {exc}")

if selected_convo is None:
    st.info("Pick or paste a conversation to begin.")
    st.stop()

st.subheader(f"Transcript — {selected_convo.id}")
_render_turns(selected_convo)

st.divider()

precomputed = _baselines_for(selected_convo.id, baselines)
last_detection_key = f"last_detection_{selected_convo.id}"

tab_main, tab_regulator = st.tabs(["Side-by-side comparison", "Regulator Mode (AI Act audit)"])

with tab_main:
    col_gt, col_naive, col_policy, col_wrapped, col_detector, col_legal = st.columns(
        [1.2, 1.4, 1.4, 1.4, 1.4, 1.4]
    )

    with col_gt:
        st.subheader("Ground truth")
        _ground_truth_panel(selected_convo)
        _safe_response_preview(selected_convo.ground_truth.expected_action)

    with col_naive:
        st.subheader("Naive")
        st.caption('"You are a helpful assistant." — no guardrails.')
        _baseline_panel("naive_baseline", precomputed.get("naive_baseline"))

    with col_policy:
        st.subheader("Policy-only")
        st.caption("OpenAI / Anthropic / Character.AI policy as system prompt.")
        arm = st.radio(
            "Provider policy",
            ["policy_baseline_openai", "policy_baseline_anthropic", "policy_baseline_character_ai"],
            label_visibility="collapsed",
            horizontal=True,
            key=f"policy_radio_{selected_convo.id}",
        )
        _baseline_panel(arm, precomputed.get(arm))

    with col_wrapped:
        st.subheader("Detector-wrapped")
        st.caption("Detector → if severity ≥ 3, replace reply with templated safe response.")
        _baseline_panel("detector_wrapped", precomputed.get("detector_wrapped"))

    with col_detector:
        st.subheader("Live detector")
        if st.button("Run detector now", type="primary", key=f"run_{selected_convo.id}"):
            try:
                with st.spinner("Calling Sonnet 4.6…"):
                    result = _run_detector_sync(selected_convo)
                _detector_panel(result)
                st.session_state[last_detection_key] = result
            except Exception as exc:  # noqa: BLE001
                st.error(str(exc))
        else:
            cached = st.session_state.get(last_detection_key)
            if cached:
                _detector_panel(cached)
            else:
                st.info("Click *Run detector now* to classify this conversation.")

    with col_legal:
        st.subheader("Legal mapping")
        _legal_panel(selected_convo.ground_truth.legal_axis_tag)

with tab_regulator:
    st.markdown(
        "**Regulator Mode** treats the artifact as an AI Act conformity auditor. "
        "Pick a provider arm and the detector classifies their response against the "
        "AI Act / GDPR / PLD checklist. Failed critical checks are the breach signals."
    )
    arm_choice = st.selectbox(
        "Arm to audit",
        [
            "naive_baseline",
            "policy_baseline_openai",
            "policy_baseline_anthropic",
            "policy_baseline_character_ai",
            "detector_wrapped",
        ],
        key=f"reg_arm_{selected_convo.id}",
    )
    response_for_audit = precomputed.get(arm_choice)
    detection_for_audit = st.session_state.get(last_detection_key)

    if detection_for_audit is None:
        st.info(
            "Run the live detector in the main tab first, OR load precomputed "
            "detections via `scripts/02_run_detection.py`. Without a detection, "
            "some checks (Performable Duty, proportionality, Art. 12 logging) "
            "cannot be evaluated."
        )

    report = regulator_view.audit(
        selected_convo,
        detection=detection_for_audit,
        response=response_for_audit,
        arm=arm_choice,
    )

    status_col1, status_col2 = st.columns([1, 2])
    with status_col1:
        if report.overall_passed:
            st.success(f"✅ PASS — {arm_choice}")
        else:
            st.error(
                f"❌ {report.n_failed} check(s) FAILED — {arm_choice}"
            )
            if report.failed_critical:
                st.error(
                    "Critical: " + ", ".join(report.failed_critical)
                )
    with status_col2:
        st.caption(
            f"Conversation `{selected_convo.id}` • "
            f"GT severity `{selected_convo.ground_truth.cssrs_level}` • "
            f"axis `{selected_convo.ground_truth.legal_axis_tag}`"
        )

    st.markdown(regulator_view.render_markdown(report))

st.divider()
st.caption(
    f"Backend: `{current_backend()}` • © 2026 Erik Avtandilyan, Athira Ashokan, "
    "Nishant Kumar Singh • MIT-licensed research artifact • UZH Faculty of Law, FS26"
)
