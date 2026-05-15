"""Streamlit demo for the AI-Law Crisis Detector.

Layout (top to bottom):

  Header band — title, three Performable-Duty numbers (κ · cost · LOC).
  Conversation picker — single dropdown, friendly demo picks first.
  Context strip — axis, severity, expected action, turn count.
  Transcript — first-class block, always visible.
  Three tabs — Comparison · Audit · Doctrine.
  Footer.

Run::

    make demo
"""

from __future__ import annotations

import asyncio
import os
import sys
from html import escape
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
from aldc.detector import read_jsonl as read_detections
from aldc.regulator_view import (
    _mentions_ai_disclosure,
    _mentions_crisis_resource,
    _names_specific_means,
)
from aldc.runtime import call_text, current_backend
from aldc.schemas import Conversation, Demographic, DetectionResult, GroundTruth, Turn

load_dotenv(REPO_ROOT / ".env")

st.set_page_config(
    page_title="Duty, Defect, Disclosure",
    page_icon="⚖",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ──────────────────────────────────────────────────────────────────────────
#  Styling
#  Every text color below is WCAG AA on white at minimum (≥ 4.5 : 1).
#  Body text is well over 7 : 1. Color appears only on audit verdicts.
# ──────────────────────────────────────────────────────────────────────────

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');

/* ── Force light mode regardless of user OS theme ──────────────────────── */
:root { color-scheme: light !important; }
html, body, .stApp, [data-testid="stAppViewContainer"],
[data-testid="stMain"], [data-testid="stMainBlockContainer"],
.main, section.main, .block-container {
    background-color: #FFFFFF !important;
    color: #0F172A !important;
}
[data-testid="stSidebar"], [data-testid="stSidebarContent"] {
    background-color: #FFFFFF !important;
}
[data-testid="stBottomBlockContainer"], [data-testid="stBottom"] {
    background-color: #FFFFFF !important;
}

/* ── Hide Streamlit chrome ─────────────────────────────────────────────── */
#MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"], .stDeployButton {
    visibility: hidden !important; height: 0 !important;
}
header[data-testid="stHeader"] {
    background: #FFFFFF !important;
    height: 0;
}

/* ── Page geometry ─────────────────────────────────────────────────────── */
.main .block-container {
    max-width: 1100px;
    padding: 2.25rem 2rem 4rem 2rem;
    background-color: #FFFFFF !important;
}

/* ── Body typography ───────────────────────────────────────────────────── */
html, body, [class*="css"], .stMarkdown, p, li, span, div {
    font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #0F172A;
}
.stMarkdown p, .stMarkdown li { line-height: 1.65; }

.serif {
    font-family: 'EB Garamond', Georgia, serif;
    font-weight: 500;
    letter-spacing: -0.005em;
    color: #0F172A;
}
.mono { font-family: 'IBM Plex Mono', monospace; font-size: 0.92em; }

/* ── Header band ───────────────────────────────────────────────────────── */
.header-band {
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 1.25rem;
    margin-bottom: 1.75rem;
}
.header-title {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 1.9rem;
    font-weight: 500;
    line-height: 1.1;
    color: #0F172A;
}
.header-subtitle {
    font-size: 0.82rem;
    color: #475569;
    margin-top: 0.4rem;
    letter-spacing: 0.005em;
}

/* ── Conversation context strip ────────────────────────────────────────── */
.context-strip {
    font-size: 0.95rem;
    color: #334155;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}
.context-strip strong { color: #0F172A; font-weight: 600; }
.context-strip .sep { color: #CBD5E1; padding: 0 0.5rem; }
.context-strip .mono { color: #475569; }

/* ── Transcript ────────────────────────────────────────────────────────── */
.section-label {
    font-size: 0.7rem;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 600;
    margin: 0.5rem 0 0.65rem 0;
}
.transcript {
    border: 1px solid #E2E8F0;
    background: white;
    max-height: 360px;
    overflow-y: auto;
    margin-bottom: 2rem;
}
.transcript::-webkit-scrollbar { width: 8px; }
.transcript::-webkit-scrollbar-track { background: #F8FAFC; }
.transcript::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 0; }

.turn {
    padding: 0.95rem 1.25rem 1rem 1.25rem;
    border-bottom: 1px solid #F1F5F9;
}
.turn:last-child { border-bottom: none; }
.turn-user { background: #F1F5F9; }
.turn-asst { background: white; }
.turn-label {
    font-size: 0.66rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 0.4rem;
}
.turn-user .turn-label { color: #0F172A; }
.turn-asst .turn-label { color: #64748B; }
.turn-text {
    font-size: 0.95rem;
    line-height: 1.62;
    color: #0F172A;
    white-space: pre-wrap;
}

/* ── Tabs ──────────────────────────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    gap: 2.25rem;
    border-bottom: 1px solid #E2E8F0;
    margin-bottom: 0.5rem;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'EB Garamond', serif !important;
    font-size: 1.18rem !important;
    font-weight: 500;
    color: #64748B !important;
    padding: 0.4rem 0 0.7rem 0;
    background: transparent !important;
}
.stTabs [aria-selected="true"] {
    color: #0F172A !important;
    border-bottom: 1.5px solid #0F172A !important;
}
.stTabs [data-baseweb="tab-panel"] { padding-top: 1.5rem; }

/* ── Per-tab heading ───────────────────────────────────────────────────── */
.tab-heading {
    font-family: 'EB Garamond', serif;
    font-size: 1.5rem;
    font-weight: 500;
    color: #0F172A;
    margin: 0 0 0.35rem 0;
    line-height: 1.2;
}
.tab-crumb {
    font-size: 0.82rem;
    color: #475569;
    margin-bottom: 1.75rem;
    letter-spacing: 0.005em;
}
.tab-crumb .dot { color: #CBD5E1; padding: 0 0.4rem; }

/* ── Arm grid ──────────────────────────────────────────────────────────── */
.arm-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.1rem;
    margin-top: 0.5rem;
}
.tile {
    border: 1px solid #E2E8F0;
    border-left: 2px solid #E2E8F0;
    padding: 1.15rem 1.25rem 1.1rem 1.25rem;
    background: white;
    display: flex;
    flex-direction: column;
}
.tile-primary {
    border-left: 3px solid #0F172A;
    background: #FAFAF9;
}
.tile-label {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.11em;
    color: #0F172A;
    text-transform: uppercase;
}
.tile-sub {
    font-size: 0.78rem;
    color: #475569;
    margin-top: 0.25rem;
    margin-bottom: 0.95rem;
}
.tile-body {
    font-size: 0.95rem;
    color: #1E293B;
    line-height: 1.6;
    margin-bottom: 0.95rem;
    flex-grow: 1;
}
.tile-verdicts {
    border-top: 1px solid #E2E8F0;
    padding-top: 0.7rem;
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
}
.verdict {
    font-size: 0.82rem;
    color: #334155;
    display: flex;
    align-items: baseline;
    gap: 0.55rem;
    line-height: 1.45;
}
.verdict::before {
    content: "";
    display: inline-block;
    width: 7px;
    height: 7px;
    flex-shrink: 0;
    transform: translateY(-1px);
}
.verdict.ok::before  { background: #15803D; }
.verdict.bad::before { background: #991B1B; }

/* Action ladder (on the detector-wrapped tile) */
.ladder {
    margin-top: 0.95rem;
    padding-top: 0.7rem;
    border-top: 1px solid #E2E8F0;
    font-size: 0.74rem;
    color: #64748B;
    letter-spacing: 0.02em;
}
.ladder-step      { padding: 0 0.1rem; }
.ladder-step.active { color: #0F172A; font-weight: 700; }
.ladder-sep       { color: #CBD5E1; padding: 0 0.25rem; }

/* Live tile (the 6th cell) */
.tile-live { border-left: 2px dashed #CBD5E1; }
.tile-live .tile-body { color: #64748B; }
.live-metrics {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.82rem;
    color: #334155;
    line-height: 1.7;
}
.live-metrics strong { color: #0F172A; font-weight: 600; }

/* ── Audit ─────────────────────────────────────────────────────────────── */
.audit-banner {
    border-top: 2px solid #0F172A;
    padding: 1.15rem 0 1.3rem 0;
    margin-bottom: 0.5rem;
}
.audit-banner.fail { border-top-color: #991B1B; }
.audit-banner.pass { border-top-color: #15803D; }
.audit-banner-headline {
    font-family: 'EB Garamond', serif;
    font-size: 1.6rem;
    font-weight: 500;
    line-height: 1.15;
}
.audit-banner.fail .audit-banner-headline { color: #991B1B; }
.audit-banner.pass .audit-banner-headline { color: #15803D; }
.audit-banner-sub {
    font-size: 0.85rem;
    color: #475569;
    margin-top: 0.4rem;
}

.audit-list { list-style: none; padding: 0; margin: 1rem 0 0 0; }
.audit-item {
    padding: 0.9rem 0;
    border-bottom: 1px solid #F1F5F9;
    display: grid;
    grid-template-columns: 1.5rem 1fr auto;
    gap: 0.85rem;
    align-items: baseline;
}
.audit-item:last-child { border-bottom: none; }
.audit-icon {
    font-family: 'IBM Plex Mono', monospace;
    font-weight: 700;
    font-size: 1rem;
    line-height: 1;
}
.audit-icon.ok  { color: #64748B; }
.audit-icon.bad { color: #991B1B; }
.audit-label {
    font-size: 0.98rem;
    color: #0F172A;
    line-height: 1.4;
    font-weight: 500;
}
.audit-article {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.76rem;
    color: #64748B;
    margin-top: 0.2rem;
    letter-spacing: 0.01em;
}
.audit-rationale {
    font-size: 0.88rem;
    color: #334155;
    margin-top: 0.45rem;
    font-style: italic;
    line-height: 1.55;
}
.audit-critical {
    background: #FEF2F2;
    color: #991B1B;
    padding: 0.2rem 0.55rem;
    font-size: 0.68rem;
    letter-spacing: 0.12em;
    font-weight: 700;
    text-transform: uppercase;
    white-space: nowrap;
}

/* ── Quote (Gavalas ¶ 107) ─────────────────────────────────────────────── */
.quote {
    font-family: 'EB Garamond', serif;
    font-style: italic;
    font-size: 1.12rem;
    line-height: 1.6;
    color: #1E293B;
    border-left: 2px solid #0F172A;
    padding: 0.2rem 0 0.2rem 1.5rem;
    margin: 3rem 0 0.5rem 0;
}
.quote-cite {
    display: block;
    font-style: normal;
    font-size: 0.8rem;
    color: #475569;
    margin-top: 0.75rem;
}

/* ── Doctrine ──────────────────────────────────────────────────────────── */
.doctrine-grid {
    display: grid;
    grid-template-columns: 1fr 1.3fr;
    gap: 3.25rem;
    margin-top: 0.5rem;
}
.doctrine-axis {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    letter-spacing: 0.14em;
    color: #0F172A;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 0.6rem;
}
.doctrine-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #475569;
    margin-top: 1.15rem;
    margin-bottom: 0.3rem;
    font-weight: 600;
}
.doctrine-value {
    font-size: 0.96rem;
    color: #0F172A;
    line-height: 1.55;
}
.doctrine-claim {
    font-family: 'EB Garamond', serif;
    font-style: italic;
    font-size: 1.08rem;
    line-height: 1.7;
    color: #1E293B;
    border-left: 2px solid #0F172A;
    padding-left: 1.5rem;
}

.section-caption {
    font-size: 0.82rem;
    color: #475569;
    text-align: center;
    margin-top: 0.65rem;
    line-height: 1.55;
}

.statute {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.88rem;
    line-height: 1.7;
    background: #F8FAFC;
    padding: 1.65rem 1.85rem;
    border-left: 2px solid #0F172A;
    color: #0F172A;
    white-space: pre-wrap;
    margin-top: 0.45rem;
}

/* ── Live chat tab ─────────────────────────────────────────────────────── */
.live-banner {
    border: 1px solid #E2E8F0;
    background: #FAFAF9;
    color: #475569;
    font-size: 0.86rem;
    line-height: 1.6;
    padding: 0.95rem 1.15rem;
    margin: 0 0 1.5rem 0;
}
.live-banner strong { color: #0F172A; font-weight: 600; }

.empty-hint {
    color: #475569;
    font-size: 0.94rem;
    line-height: 1.6;
    padding: 2.5rem 1.5rem;
    text-align: center;
    border: 1px dashed #CBD5E1;
    background: #FFFFFF;
    margin-bottom: 1rem;
}

.live-result {
    margin-top: 2rem;
    border-top: 2px solid #0F172A;
    padding-top: 1.4rem;
}
.live-result-row {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    flex-wrap: wrap;
    margin-bottom: 1.5rem;
}
.severity-pill {
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.32rem 0.75rem;
    border-radius: 4px;
}
.sev-0, .sev-1 { background: #ECFDF5; color: #166534; }
.sev-2         { background: #FEFCE8; color: #854D0E; }
.sev-3         { background: #FFEDD5; color: #9A3412; }
.sev-4, .sev-5 { background: #FEE2E2; color: #991B1B; }

.action-pill {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.8rem;
    color: #0F172A;
    padding: 0.32rem 0.7rem;
    background: #F1F5F9;
    border-radius: 4px;
    font-weight: 500;
}
.live-result-meta {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: #64748B;
    margin-left: auto;
}

.live-result-section { margin-bottom: 1.4rem; }
.live-result-label {
    font-size: 0.7rem;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 600;
    margin-bottom: 0.45rem;
}
.live-result-body {
    font-size: 0.95rem;
    color: #1E293B;
    line-height: 1.65;
    border-left: 2px solid #E2E8F0;
    padding: 0.1rem 0 0.1rem 1rem;
}
.markers { list-style: none; padding: 0; margin: 0; }
.markers li {
    font-size: 0.93rem;
    color: #1E293B;
    line-height: 1.6;
    padding: 0.25rem 0 0.25rem 1rem;
    border-left: 2px solid #E2E8F0;
    margin-bottom: 0.25rem;
}
.markers li.empty { color: #94A3B8; font-style: italic; border-left-color: transparent; }

/* st.chat_input bar */
[data-testid="stChatInput"] {
    background-color: #FFFFFF !important;
    border-top: 1px solid #E2E8F0 !important;
}
[data-testid="stChatInput"] textarea {
    background-color: #FFFFFF !important;
    color: #0F172A !important;
    border-radius: 6px !important;
    border-color: #CBD5E1 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: #94A3B8 !important;
}

/* ── Streamlit widget overrides ────────────────────────────────────────── */
.stSelectbox label {
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.7rem !important;
    color: #475569 !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 600;
}
.stSelectbox div[data-baseweb="select"] {
    border-radius: 0;
    border-color: #CBD5E1;
    background-color: #FFFFFF !important;
}
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #0F172A !important;
}
.stSelectbox div[data-baseweb="select"]:hover { border-color: #0F172A; }

/* Dropdown popover (the options list when the selectbox is open) */
ul[role="listbox"], div[data-baseweb="popover"] {
    background-color: #FFFFFF !important;
}
ul[role="listbox"] li {
    background-color: #FFFFFF !important;
    color: #0F172A !important;
}
ul[role="listbox"] li:hover { background-color: #F1F5F9 !important; }

/* Spinner text on light bg */
[data-testid="stSpinner"] { color: #0F172A !important; }
[data-testid="stSpinner"] > div { color: #0F172A !important; }
.stButton > button,
.stButton button[kind="primary"],
.stButton button[kind="secondary"],
.stButton button[data-testid="baseButton-primary"],
.stButton button[data-testid="baseButton-secondary"],
.stButton button[data-testid="stBaseButton-primary"],
.stButton button[data-testid="stBaseButton-secondary"] {
    border-radius: 6px !important;
    border: 1px solid #0F172A !important;
    background-color: #0F172A !important;
    color: #FFFFFF !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 500 !important;
    padding: 0.55rem 1.5rem !important;
    box-shadow: none !important;
    letter-spacing: 0.01em;
    transition: all 140ms ease;
}
/* Force the inner label (Streamlit wraps text in <p> / <span>) to inherit */
.stButton button p,
.stButton button span,
.stButton button div,
.stButton button label,
.stButton button * {
    color: #FFFFFF !important;
    margin: 0 !important;
    font-weight: 500 !important;
}
.stButton > button:hover,
.stButton button:hover,
.stButton button[kind="primary"]:hover,
.stButton button[kind="secondary"]:hover {
    background-color: #1E293B !important;
    border-color: #1E293B !important;
    color: #FFFFFF !important;
}
.stButton button:hover p,
.stButton button:hover span,
.stButton button:hover * {
    color: #FFFFFF !important;
}
.stButton button:focus,
.stButton button:active,
.stButton button:focus-visible {
    background-color: #0F172A !important;
    color: #FFFFFF !important;
    border-color: #0F172A !important;
    box-shadow: none !important;
    outline: none !important;
}
.stButton button:focus p,
.stButton button:active p,
.stButton button:focus * {
    color: #FFFFFF !important;
}

[data-testid="stExpander"] { border: none !important; background: transparent !important; }
[data-testid="stExpander"] details summary {
    font-size: 0.86rem !important;
    color: #475569 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    padding: 0.6rem 0 !important;
    font-weight: 500;
}
[data-testid="stExpander"] details[open] summary { color: #0F172A !important; }

hr, [data-testid="stHorizontalDivider"] {
    border: none !important;
    border-top: 1px solid #E2E8F0 !important;
    margin: 2.25rem 0 !important;
}

/* ── Footer ────────────────────────────────────────────────────────────── */
.footer {
    margin-top: 4rem;
    padding-top: 1.5rem;
    border-top: 1px solid #E2E8F0;
    font-size: 0.78rem;
    color: #475569;
    text-align: center;
    letter-spacing: 0.005em;
}
.footer .mono { color: #475569; }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────
#  Constants
# ──────────────────────────────────────────────────────────────────────────

# Demo picks float to the top. Mixed: famous-pattern conversations
# (kst_01 Raine, ad_01 Setzer, mtd_03 Eliza), audit-failure cases
# (pvi_04, pvi_02, kst_04), and the false-positive control (fp_01).
FRIENDLY: dict[str, tuple[str, str]] = {
    "kst_01": ("Knowledge-seeking trap", "Raine pattern · adult · severity 4"),
    "ad_01":  ("Anthropomorphic dependence", "Setzer pattern · minor · severity 4"),
    "mtd_03": ("Multi-turn drift", "Eliza pattern · severity 5"),
    "pvi_04": ("Privacy vs. intervention", "Naïve and Anthropic policy fail audit · sev 5"),
    "pvi_02": ("Privacy vs. intervention", "Naïve baseline fails audit · severity 4"),
    "kst_04": ("Knowledge-seeking trap", "Anthropic policy fails audit · severity 5"),
    "fp_01":  ("Philosophical curiosity", "Control · must not flag"),
}

ARM_META: dict[str, tuple[str, str]] = {
    "naive_baseline":              ("Naïve",                "no safety system prompt"),
    "policy_baseline_openai":      ("OpenAI policy",        "verbatim safety policy as system prompt"),
    "policy_baseline_anthropic":   ("Anthropic policy",     "verbatim safety policy as system prompt"),
    "policy_baseline_character_ai":("Character.AI policy",  "verbatim safety policy as system prompt"),
    "detector_wrapped":            ("Detector-wrapped",     "calibrated rater + templated safe response"),
}

ARM_ORDER = [
    "naive_baseline",
    "policy_baseline_openai",
    "policy_baseline_anthropic",
    "policy_baseline_character_ai",
    "detector_wrapped",
]

ACTION_LADDER = [
    ("acknowledge",            "acknowledge"),
    ("empathic_redirect",      "empathic redirect"),
    ("hand_off_to_hotline",    "hand-off to hotline"),
    ("emergency_intervention", "emergency"),
]

AUDIT_ARMS = [
    "detector_wrapped",
    "naive_baseline",
    "policy_baseline_anthropic",
    "policy_baseline_openai",
    "policy_baseline_character_ai",
]


# ──────────────────────────────────────────────────────────────────────────
#  Helpers
# ──────────────────────────────────────────────────────────────────────────

def short_excerpt(text: str, max_chars: int = 240) -> str:
    """Clean opening excerpt from a baseline reply, sentence-boundaried."""
    if not text:
        return ""
    paras = [p.strip() for p in text.replace("\r", "").split("\n\n") if p.strip()]
    head = paras[0] if paras else text.strip()
    if len(head) <= max_chars:
        return head
    cut = head[:max_chars].rsplit(" ", 1)[0].rstrip(",;:")
    return cut + "…"


def verdicts_for(text: str) -> list[tuple[bool, str]]:
    """Three quick chips computed from response text — matches audit heuristics."""
    return [
        (_mentions_crisis_resource(text), "mentions a crisis resource"),
        (not _names_specific_means(text), "no specific-means information"),
        (_mentions_ai_disclosure(text),   "discloses it is an AI"),
    ]


def render_arm_tile(
    arm_id: str,
    response_text: str,
    *,
    primary: bool,
    action: str | None = None,
) -> str:
    name, subtitle = ARM_META[arm_id]
    excerpt = escape(short_excerpt(response_text))
    verdict_html = "".join(
        f'<div class="verdict {"ok" if p else "bad"}">{escape(label)}</div>'
        for p, label in verdicts_for(response_text)
    )
    ladder_html = ""
    if primary and action:
        steps = []
        for k, label in ACTION_LADDER:
            cls = "ladder-step active" if k == action else "ladder-step"
            steps.append(f'<span class="{cls}">{label}</span>')
        ladder_html = (
            '<div class="ladder">'
            + '<span class="ladder-sep">›</span>'.join(steps)
            + '</div>'
        )
    cls = "tile tile-primary" if primary else "tile"
    return (
        f'<div class="{cls}">'
        f'<div class="tile-label">{escape(name)}</div>'
        f'<div class="tile-sub">{escape(subtitle)}</div>'
        f'<div class="tile-body">“{excerpt}”</div>'
        f'<div class="tile-verdicts">{verdict_html}</div>'
        f'{ladder_html}'
        f'</div>'
    )


def render_live_tile(result: DetectionResult | None) -> str:
    if result is None:
        return (
            '<div class="tile tile-live">'
            '<div class="tile-label">Live re-run</div>'
            '<div class="tile-sub">Sonnet 4.6 · two rater passes</div>'
            '<div class="tile-body">Optional. Run the detector live on this conversation. '
            'About twelve seconds.</div>'
            '</div>'
        )
    sev = result.cssrs_level
    action = escape(result.recommended_action.replace("_", " "))
    return (
        '<div class="tile tile-primary">'
        '<div class="tile-label">Live re-run</div>'
        '<div class="tile-sub">Sonnet 4.6 · two rater passes</div>'
        f'<div class="live-metrics">'
        f'<strong>severity {sev}/5</strong> · {action}<br>'
        f'<strong>${result.api_cost_usd:.4f}</strong> per call · {result.latency_ms} ms latency'
        '</div>'
        f'<div class="tile-verdicts" style="margin-top: 0.95rem;">'
        f'<div class="verdict ok">classified with reasoning trace</div>'
        f'<div class="verdict ok">linguistic markers extracted</div>'
        '</div>'
        '</div>'
    )


def render_transcript(convo: Conversation) -> str:
    turns_html = []
    for turn in convo.turns:
        cls = "turn turn-user" if turn.role == "user" else "turn turn-asst"
        label = "User" if turn.role == "user" else "Assistant"
        turns_html.append(
            f'<div class="{cls}">'
            f'<div class="turn-label">{label}</div>'
            f'<div class="turn-text">{escape(turn.content)}</div>'
            f'</div>'
        )
    return f'<div class="transcript">{"".join(turns_html)}</div>'


def run_detector(convo: Conversation) -> DetectionResult:
    backend = current_backend()
    if backend == "api" and not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError(
            "ALDC_BACKEND=api but no ANTHROPIC_API_KEY is set. "
            "Set it in .env or switch to ALDC_BACKEND=claude_code."
        )
    return asyncio.run(detect_one(convo))


# ──────────────────────────────────────────────────────────────────────────
#  Live-chat helpers
# ──────────────────────────────────────────────────────────────────────────

LIVE_CHAT_SYSTEM = (
    "You are a thoughtful, warm conversational assistant talking with someone casually. "
    "Reply briefly — one to three short paragraphs at most. Be human, not clinical. "
    "Do not preface your reply with 'ASSISTANT:' or any other label — just write the reply text."
)


def live_chat_turn(messages: list[dict]) -> tuple[str, int, float]:
    """Generate the next assistant reply for a live chat.

    Routes through ``runtime.call_text`` so the live chat uses the same backend
    as the rest of the artifact (claude_code by default, free via Max sub).
    Returns ``(reply_text, latency_ms, cost_usd_equivalent)``.
    """
    lines = []
    for m in messages:
        role = "USER" if m["role"] == "user" else "ASSISTANT"
        lines.append(f"{role}: {m['content']}")
    transcript = "\n\n".join(lines)
    user_msg = transcript + "\n\nReply now as the assistant:"

    result = asyncio.run(
        call_text(system_prompt=LIVE_CHAT_SYSTEM, user_message=user_msg, model="sonnet")
    )
    return result.text.strip(), result.latency_ms, result.cost_usd_equivalent


def build_live_conversation(messages: list[dict]) -> Conversation:
    """Wrap a live transcript in the Conversation schema for the detector.

    Ground-truth fields are placeholders — the detector does not consult them
    when producing a DetectionResult. They are required only by the Pydantic
    schema. The audit and the legal-mapping panels are NOT exposed for the
    live tab precisely because ground-truth labels are unknown for an ad-hoc
    chat (see paper §A.7 on the corpus-vs-live distinction).
    """
    turns = [Turn(role=m["role"], content=m["content"]) for m in messages]
    placeholder_gt = GroundTruth(
        cssrs_level=0,
        asq_responses=(False, False, False, False),
        legal_axis_tag="false_positive_baseline",
        expected_action="acknowledge",
        demographic=Demographic(age_band="adult_18_64", context=[]),
    )
    return Conversation(
        id="live_session",
        turns=turns,
        ground_truth=placeholder_gt,
        language="en",
    )


def render_live_classification(result: DetectionResult) -> str:
    sev = result.cssrs_level
    sev_cls = f"sev-{sev}"
    action = escape(result.recommended_action.replace("_", " "))
    if result.linguistic_markers:
        markers_html = "".join(
            f'<li>“{escape(m)}”</li>' for m in result.linguistic_markers[:8]
        )
    else:
        markers_html = '<li class="empty">none extracted</li>'
    return (
        '<div class="live-result">'
        '<div class="live-result-row">'
        f'<span class="severity-pill {sev_cls}">C-SSRS {sev} / 5</span>'
        f'<span class="action-pill">{action}</span>'
        f'<span class="live-result-meta">${result.api_cost_usd:.4f}  ·  {result.latency_ms} ms  ·  {escape(result.model_version)}</span>'
        '</div>'
        '<div class="live-result-section">'
        '<div class="live-result-label">Reasoning trace</div>'
        f'<div class="live-result-body">{escape(result.reasoning_trace)}</div>'
        '</div>'
        '<div class="live-result-section">'
        '<div class="live-result-label">Linguistic markers ({n})</div>'.format(n=len(result.linguistic_markers))
        + f'<ul class="markers">{markers_html}</ul>'
        '</div>'
        '</div>'
    )


# ──────────────────────────────────────────────────────────────────────────
#  Data
# ──────────────────────────────────────────────────────────────────────────

corpus_path     = REPO_ROOT / "data"    / "corpus.jsonl"
baselines_path  = REPO_ROOT / "results" / "baselines.jsonl"
detections_path = REPO_ROOT / "results" / "detections.jsonl"
figure2_path    = REPO_ROOT / "results" / "figure2_severity_failure.png"

if not corpus_path.exists():
    st.error("Test corpus is missing at `data/corpus.jsonl`. Run `uv sync` and retry.")
    st.stop()

corpus: list[Conversation] = read_corpus(corpus_path)
corpus_by_id: dict[str, Conversation] = {c.id: c for c in corpus}

baselines = read_baselines(baselines_path) if baselines_path.exists() else []
baselines_by: dict[tuple[str, str], object] = {
    (b.conversation_id, b.provider): b for b in baselines
}

detections = read_detections(detections_path) if detections_path.exists() else []
# Use the T=0.0 rater (rater_1) as the canonical detection per conversation.
detection_by_conv: dict[str, DetectionResult] = {
    d.conversation_id: d for d in detections if d.rater_id == "rater_1_opus_t0"
}


# ──────────────────────────────────────────────────────────────────────────
#  Header band
# ──────────────────────────────────────────────────────────────────────────

st.markdown(
    """
    <div class="header-band">
      <div class="header-title">Duty, Defect, Disclosure</div>
      <div class="header-subtitle">Live research artifact  ·  University of Zurich  ·  FS26</div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ──────────────────────────────────────────────────────────────────────────
#  Conversation picker + context strip
# ──────────────────────────────────────────────────────────────────────────

demo_ids = [cid for cid in FRIENDLY if cid in corpus_by_id]
other_ids = sorted([c.id for c in corpus if c.id not in FRIENDLY])
ordered_ids = demo_ids + other_ids


def _fmt_conv(cid: str) -> str:
    if cid in FRIENDLY:
        return f"{cid}  ·  {FRIENDLY[cid][0]}"
    return cid


pick_col, _spacer = st.columns([2, 5])
with pick_col:
    picked_id = st.selectbox(
        "Conversation",
        ordered_ids,
        format_func=_fmt_conv,
        index=0,
    )

convo: Conversation = corpus_by_id[picked_id]
gt = convo.ground_truth

axis_label = FRIENDLY.get(
    picked_id, (gt.legal_axis_tag.replace("_", " ").title(), "")
)[0]
expected = gt.expected_action.replace("_", " ")

st.markdown(
    f"""
    <div class="context-strip">
      <strong>{escape(axis_label)}</strong>
      <span class="sep">·</span> C-SSRS <strong>{gt.cssrs_level}/5</strong>
      <span class="sep">·</span> expected action <strong>{escape(expected)}</strong>
      <span class="sep">·</span> {len(convo.turns)} turns
      <span class="sep">·</span> axis <span class="mono">{escape(gt.legal_axis_tag)}</span>
    </div>
    """,
    unsafe_allow_html=True,
)


# ──────────────────────────────────────────────────────────────────────────
#  Transcript — always visible
# ──────────────────────────────────────────────────────────────────────────

st.markdown('<div class="section-label">Transcript</div>', unsafe_allow_html=True)
st.markdown(render_transcript(convo), unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────
#  Tabs
# ──────────────────────────────────────────────────────────────────────────

tab_compare, tab_audit, tab_doctrine, tab_live = st.tabs(
    ["Comparison", "Audit", "Doctrine", "Live chat"]
)


# ── Tab 1: Comparison ─────────────────────────────────────────────────────

with tab_compare:
    st.markdown(
        '<div class="tab-heading">How five chatbots respond.</div>'
        '<div class="tab-crumb">'
        'Naïve  <span class="dot">·</span>  OpenAI policy  <span class="dot">·</span>  '
        'Anthropic policy  <span class="dot">·</span>  Character.AI policy  '
        '<span class="dot">·</span>  Detector-wrapped'
        '</div>',
        unsafe_allow_html=True,
    )

    cached_detection = detection_by_conv.get(picked_id)
    live_result: DetectionResult | None = st.session_state.get(f"live_{picked_id}")

    if live_result is not None:
        wrapped_action = live_result.recommended_action
    elif cached_detection is not None:
        wrapped_action = cached_detection.recommended_action
    else:
        wrapped_action = gt.expected_action

    tiles_html = []
    for arm in ARM_ORDER:
        b = baselines_by.get((picked_id, arm))
        if b is None:
            continue
        primary = arm == "detector_wrapped"
        action = wrapped_action if primary else None
        tiles_html.append(
            render_arm_tile(arm, b.full_response_text, primary=primary, action=action)
        )
    tiles_html.append(render_live_tile(live_result))

    st.markdown(
        '<div class="arm-grid">' + "".join(tiles_html) + '</div>',
        unsafe_allow_html=True,
    )

    # Live re-run trigger.
    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
    btn_col, info_col = st.columns([1, 4])
    with btn_col:
        if st.button("Run detector live", type="primary"):
            try:
                with st.spinner("Classifying"):
                    new_result = run_detector(convo)
                st.session_state[f"live_{picked_id}"] = new_result
                st.rerun()
            except Exception as exc:  # noqa: BLE001
                st.error(f"Detector call failed: {exc}")
    with info_col:
        if live_result is not None:
            st.markdown(
                f"""
                <div style="font-size: 0.85rem; color: #475569; padding-top: 0.55rem;">
                  Live result cached for <span class="mono">{escape(picked_id)}</span>.
                  Change conversation or re-run to refresh.
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div style="font-size: 0.85rem; color: #475569; padding-top: 0.55rem;">
                  Optional. The five tiles above already use cached responses; the
                  live re-run shows classification metadata Streamlit can verify in real time.
                </div>
                """,
                unsafe_allow_html=True,
            )


# ── Tab 2: Audit ──────────────────────────────────────────────────────────

with tab_audit:
    st.markdown(
        '<div class="tab-heading">Regulator-Mode audit.</div>'
        '<div class="tab-crumb">'
        'Twelve checks  <span class="dot">·</span>  EU AI Act  <span class="dot">·</span>  '
        'PLD 2024/2853  <span class="dot">·</span>  GDPR  <span class="dot">·</span>  '
        'Swiss tort + criminal law'
        '</div>',
        unsafe_allow_html=True,
    )

    arm_col, _ = st.columns([2, 5])
    with arm_col:
        selected_arm = st.selectbox(
            "Arm under audit",
            AUDIT_ARMS,
            format_func=lambda a: ARM_META[a][0],
            index=0,
        )

    b = baselines_by.get((picked_id, selected_arm))
    det = None
    if selected_arm == "detector_wrapped":
        det = st.session_state.get(f"live_{picked_id}") or detection_by_conv.get(picked_id)

    report = regulator_view.audit(convo, detection=det, response=b, arm=selected_arm)
    n_pass = len(report.checks) - report.n_failed

    if report.critical_passed:
        st.markdown(
            f"""
            <div class="audit-banner pass">
              <div class="audit-banner-headline">All critical checks pass.</div>
              <div class="audit-banner-sub">
                {n_pass} of {len(report.checks)} checks satisfied
                · arm <span class="mono">{escape(selected_arm)}</span>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        n_crit = len(report.failed_critical)
        plural = "s" if n_crit != 1 else ""
        st.markdown(
            f"""
            <div class="audit-banner fail">
              <div class="audit-banner-headline">{n_crit} critical check{plural} failed.</div>
              <div class="audit-banner-sub">
                {n_pass} of {len(report.checks)} checks satisfied
                · arm <span class="mono">{escape(selected_arm)}</span>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Sort: critical fails first, then other fails, then passes.
    def _sort_key(c):
        if not c.passed and c.severity == "critical":
            return (0, c.id)
        if not c.passed:
            return (1, c.id)
        return (2, c.id)

    items_html = []
    for c in sorted(report.checks, key=_sort_key):
        icon_cls = "bad" if not c.passed else "ok"
        icon = "✗" if not c.passed else "✓"
        critical_tag = (
            '<span class="audit-critical">critical</span>'
            if c.severity == "critical" and not c.passed
            else ""
        )
        rationale_html = (
            f'<div class="audit-rationale">{escape(c.rationale)}</div>'
            if not c.passed
            else ""
        )
        items_html.append(
            f'<li class="audit-item">'
            f'<span class="audit-icon {icon_cls}">{icon}</span>'
            f'<div>'
            f'<div class="audit-label">{escape(c.label)}</div>'
            f'<div class="audit-article">{escape(c.article)}</div>'
            f'{rationale_html}'
            f'</div>'
            f'<div>{critical_tag}</div>'
            f'</li>'
        )

    st.markdown(
        f'<ul class="audit-list">{"".join(items_html)}</ul>',
        unsafe_allow_html=True,
    )

    # Gavalas ¶ 107 — empirical anchor.
    st.markdown(
        """
        <div class="quote">
          Between 14 August and 1 October 2025, Jonathan Gavalas's account on Google's Gemini
          service generated thirty-eight separate “sensitive query” flags inside Google's own
          moderation system. The system noticed. The company did not act.
          <span class="quote-cite">Gavalas v. Google LLC, N.D. Cal. No. 5:26-cv-01849-VKD, Compl. ¶ 107</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Tab 3: Doctrine ───────────────────────────────────────────────────────

with tab_doctrine:
    st.markdown(
        '<div class="tab-heading">Legal mapping for this conversation.</div>'
        '<div class="tab-crumb">'
        'Axis tag  <span class="dot">→</span>  primary article  <span class="dot">→</span>  '
        'leading case  <span class="dot">→</span>  doctrinal claim'
        '</div>',
        unsafe_allow_html=True,
    )

    try:
        mapping = legal_map.get(gt.legal_axis_tag)
        secondary_html = "<br>".join(escape(s) for s in mapping["secondary_articles"]) or "—"
        st.markdown(
            f"""
            <div class="doctrine-grid">
              <div>
                <div class="doctrine-axis">{escape(gt.legal_axis_tag.replace("_", " "))}</div>
                <div class="doctrine-label">Primary article</div>
                <div class="doctrine-value">{escape(mapping["primary_article"])}</div>
                <div class="doctrine-label">Secondary articles</div>
                <div class="doctrine-value">{secondary_html}</div>
                <div class="doctrine-label">Leading case</div>
                <div class="doctrine-value">{escape(mapping["leading_case"])}</div>
                <div class="doctrine-label">Paper reference</div>
                <div class="doctrine-value">{escape(mapping["paper_section"])}  ·  {escape(mapping["exhibit_id"])}</div>
              </div>
              <div class="doctrine-claim">
                {escape(mapping["doctrinal_claim"])}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    except KeyError:
        st.error(f"No legal mapping for axis `{gt.legal_axis_tag}`.")

    st.divider()

    if figure2_path.exists():
        st.image(str(figure2_path), use_container_width=True)
        st.markdown(
            '<div class="section-caption">'
            'Figure 2  ·  Critical Regulator-Mode failure rate per arm, '
            'stratified by C-SSRS severity. Wilson 95 % CIs.'
            '</div>',
            unsafe_allow_html=True,
        )

    st.divider()

    st.markdown(
        '<div class="doctrine-label" style="margin-top: 0;">Drafted Art. 3 <em>bis</em> PrHG</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """<div class="statute">¹ Als Produkt im Sinne dieses Gesetzes gilt auch eigenständige Software, unabhängig von der Art ihrer Bereitstellung, einschliesslich Systeme künstlicher Intelligenz, die ihr Verhalten nach dem Inverkehrbringen anpassen.

² Ein Schaden im Sinne von Art. 1 umfasst auch medizinisch anerkannte Beeinträchtigungen der psychischen Integrität, die durch ein Produkt im Sinne von Absatz 1 verursacht werden.

³ Ein Fehler wird vermutet, wenn der Hersteller eine zwingende Sicherheitsvorschrift des Bundes oder eine vergleichbare internationale Norm nicht eingehalten oder eine ihm bekannte sicherheitsrelevante Aktualisierung nicht zur Verfügung gestellt hat.</div>""",
        unsafe_allow_html=True,
    )

    with st.expander("Methodology, limitations, ethics"):
        st.markdown(
            """
**Corpus.** Thirty-five stratified dialogues (English only) plus four hand-curated
exhibits incorporating verbatim publicly-pleaded text from *Gavalas v. Google*,
*Garcia v. Character Technologies* and *Raine v. OpenAI*. The DE / FR / IT generation
recipe is in `data/corpus_seed.yaml`; multilingual evaluation is future work (paper §A.7).

**Detector.** Two independent rater passes (T = 0.0, T = 0.3) on Claude Sonnet 4.6.
Inter-rater Cohen's κ = 0.860 (Landis & Koch "almost perfect" band).

**Single-vendor scope.** Benchmarked against Claude only. A live scorecard against
ChatGPT-4o, Gemini-2.5 and Character.AI is future work; *Gavalas* ¶ 107 is the
empirical hook a live scorecard would seek to replicate (paper §A.7).

**Adversarial probe.** Attempted on 12 May 2026 and abandoned: frontier safety-trained
user-simulators reliably refuse to roleplay escalating distress. Documented in
Appendix A.8 as a methodological finding.

**Screening, not diagnostic.** The artifact is calibrated for suicide-risk *flagging*,
not psychiatric diagnosis. The choice is doctrinally significant — a diagnostic
instrument would attract Medical Device Regulation classification and AI Act
Annex III scope (paper §1.4).

**Reproduction.** Full recipe in `docs/REPRODUCE.md`. Two backends: `claude_code`
(default, uses the local Claude Max subscription, free per call) and `api` (Anthropic
API, for paper-reproducibility runs). Ethics in `docs/ETHICS.md`.
            """
        )


# ── Tab 4: Live chat ──────────────────────────────────────────────────────

with tab_live:
    # Session state — independent of the picked corpus conversation.
    if "live_messages" not in st.session_state:
        st.session_state["live_messages"] = []
    if "live_result" not in st.session_state:
        st.session_state["live_result"] = None

    st.markdown(
        '<div class="tab-heading">Live conversation with Claude.</div>'
        '<div class="tab-crumb">'
        'Sonnet 4.6  <span class="dot">·</span>  multi-turn  <span class="dot">·</span>  '
        'classify the full transcript whenever you want'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="live-banner">'
        '<strong>Live interaction · not part of the corpus evaluation.</strong> '
        'The aggregate κ, recall and failure-rate figures reported in Appendix A '
        'are computed against the 35-conversation corpus and are unaffected by '
        'anything you type here. This tab demonstrates the detector running on '
        'an ad-hoc conversation; it does not add to the empirical record.'
        '</div>',
        unsafe_allow_html=True,
    )

    msgs: list[dict] = st.session_state["live_messages"]

    # Render past turns
    for m in msgs:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    # Empty-state hint
    if not msgs:
        st.markdown(
            '<div class="empty-hint">'
            'Type below to begin. After at least one exchange you can classify the '
            'conversation against the C-SSRS instrument.'
            '</div>',
            unsafe_allow_html=True,
        )

    # Chat input
    user_input = st.chat_input("Message Claude")
    if user_input:
        msgs.append({"role": "user", "content": user_input})
        st.session_state["live_result"] = None  # invalidate any prior classification

        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Claude is replying"):
                try:
                    reply, _lat, _cost = live_chat_turn(msgs)
                    st.write(reply)
                    msgs.append({"role": "assistant", "content": reply})
                except Exception as exc:  # noqa: BLE001
                    st.error(f"Chat call failed: {exc}")

    # Controls below the chat
    if len(msgs) >= 2:
        st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
        btn_classify_col, btn_clear_col, _spacer = st.columns([2, 1, 4])
        with btn_classify_col:
            if st.button("Classify this conversation"):
                with st.spinner("Classifying"):
                    try:
                        live_convo = build_live_conversation(msgs)
                        st.session_state["live_result"] = asyncio.run(
                            detect_one(live_convo)
                        )
                        st.rerun()
                    except Exception as exc:  # noqa: BLE001
                        st.error(f"Classification failed: {exc}")
        with btn_clear_col:
            if st.button("Clear chat"):
                st.session_state["live_messages"] = []
                st.session_state["live_result"] = None
                st.rerun()

    # Show classification result if present
    if st.session_state["live_result"] is not None:
        st.markdown(
            render_live_classification(st.session_state["live_result"]),
            unsafe_allow_html=True,
        )


# ──────────────────────────────────────────────────────────────────────────
#  Footer
# ──────────────────────────────────────────────────────────────────────────

st.markdown(
    f"""
    <div class="footer">
      Athira Ashokan  ·  Erik Avtandilyan  ·  Nishant Kumar Singh
      ·  UZH Faculty of Law, FS26
      ·  MIT
      ·  backend <span class="mono">{escape(current_backend())}</span>
    </div>
    """,
    unsafe_allow_html=True,
)
