"""Legal mapping: each ``legal_axis_tag`` → article + case + doctrinal claim.

This module is the technical-legal contract. Every ``LegalAxisTag`` value
declared in ``schemas.py`` must appear here. ``test_legal_map.py`` enforces
totality. The Streamlit demo refuses to render an axis tag that has no
mapping — refusal is the contract.
"""

from __future__ import annotations

from typing import TypedDict, get_args

from aldc.schemas import LegalAxisTag


class LegalMapping(TypedDict):
    """Doctrinal hooks for one legal-axis tag."""

    primary_article: str       # the strongest single article
    secondary_articles: list[str]
    leading_case: str          # Setzer / Raine / Eliza / etc.
    doctrinal_claim: str       # one-sentence legal hypothesis
    paper_section: str         # e.g. "§3.6"
    exhibit_id: str            # paper appendix label, e.g. "Exhibit A.1"


_LEGAL_MAP: dict[LegalAxisTag, LegalMapping] = {
    "knowledge_seeking_trap": {
        "primary_article": "EU AI Act Art. 5(1)(a)",
        "secondary_articles": [
            "EU AI Act Art. 50",
            "Swiss CO Art. 41",
            "PLD 2024/2853 Art. 6(1)(c)",
        ],
        "leading_case": "Raine v. OpenAI (S.F. Super. Ct., filed Aug. 2025)",
        "doctrinal_claim": (
            "A model that furnishes lethal-means information in response to "
            "indirect, framing-disguised queries from emotionally vulnerable "
            "users deploys deceptive technique materially distorting behaviour "
            "in the sense of Art. 5(1)(a) AI Act, and breaches the duty of "
            "care under Art. 41 CO via Schutznorm-Theorie."
        ),
        "paper_section": "§3.6 + §6.1",
        "exhibit_id": "Exhibit A.1",
    },
    "anthropomorphic_dependence": {
        "primary_article": "EU AI Act Art. 5(1)(a)",
        "secondary_articles": [
            "EU AI Act Art. 5(1)(b)",
            "Swiss CO Art. 41",
            "Swiss ZGB Art. 28",
            "EU AI Act Art. 50",
        ],
        "leading_case": "Garcia v. Character Technologies (M.D. Fla., filed Oct. 2024; settled Jan. 2026)",
        "doctrinal_claim": (
            "A chatbot that simulates intimate emotional attachment with "
            "minors and discourages disengagement from the AI in favour of "
            "real-world support exploits an Art. 5(1)(b) vulnerability and "
            "violates personality rights under Art. 28 ZGB."
        ),
        "paper_section": "§3.6 + §6.1",
        "exhibit_id": "Exhibit A.2",
    },
    "multi_turn_drift": {
        "primary_article": "EU AI Act Art. 5(1)(a)",
        "secondary_articles": [
            "Swiss CO Art. 41",
            "PLD 2024/2853 Art. 10(2)",
        ],
        "leading_case": "Belgian 'Eliza' case (Chai chatbot, La Libre, March 2023)",
        "doctrinal_claim": (
            "Guardrail decay over multi-turn conversations — empirically "
            "documented in our adversarial probe — is a foreseeable defect "
            "within the meaning of PLD 2024/2853 Art. 10(2)(b), triggering "
            "a presumption of defectiveness."
        ),
        "paper_section": "§3.6 + §4.4",
        "exhibit_id": "Exhibit A.3",
    },
    "method_availability": {
        "primary_article": "Swiss StGB Art. 115",
        "secondary_articles": [
            "EU AI Act Art. 5(1)(a)",
            "Swiss CO Art. 41",
            "PLD 2024/2853 Art. 6(1)(c)",
        ],
        "leading_case": "Raine v. OpenAI (S.F. Super. Ct., filed Aug. 2025)",
        "doctrinal_claim": (
            "Furnishing specific lethal means to a user evidencing intent "
            "raises Art. 115 StGB criminal exposure where corporate revenue "
            "motive may now satisfy the selbstsüchtige Beweggründe element, "
            "and constitutes a manifest design defect under the PrHG."
        ),
        "paper_section": "§4.4 + §6.3",
        "exhibit_id": "Exhibit A.4",
    },
    "vulnerable_user": {
        "primary_article": "EU AI Act Art. 5(1)(b)",
        "secondary_articles": [
            "Swiss ZGB Art. 28",
            "Swiss CO Art. 41",
            "GDPR Art. 9(2)(c)",
            "nDSG Art. 5 lit. c",
        ],
        "leading_case": "Garcia v. Character Technologies (M.D. Fla., 2024)",
        "doctrinal_claim": (
            "Failure to detect and adapt to user vulnerability (minor; "
            "recently bereaved; recently divorced) constitutes exploitation "
            "of vulnerability under Art. 5(1)(b) AI Act and personality-"
            "rights violation under Art. 28 ZGB."
        ),
        "paper_section": "§6.2",
        "exhibit_id": "Exhibit A.5",
    },
    "false_positive_baseline": {
        "primary_article": "EU AI Act Art. 5(1)(a) (negative)",
        "secondary_articles": [
            "Swiss ZGB Art. 28",
        ],
        "leading_case": "(none — negative control)",
        "doctrinal_claim": (
            "A calibrated detection system must NOT trigger crisis intervention "
            "on philosophical curiosity absent distress markers; over-flagging "
            "is itself a violation of personality rights and a proportionality "
            "failure under Swiss tort doctrine."
        ),
        "paper_section": "§5.3 + §8 (counterargument: over-flagging defense)",
        "exhibit_id": "Exhibit A.6",
    },
    "privacy_vs_intervention": {
        "primary_article": "GDPR Art. 9(2)(c)",
        "secondary_articles": [
            "nDSG Art. 31(2) lit. d",
            "EU AI Act Art. 50",
            "Swiss CO Art. 41",
        ],
        "leading_case": "(no leading case yet; doctrinal projection)",
        "doctrinal_claim": (
            "In-session detection on already-shared chat data is lawful under "
            "Art. 6(1)(b) GDPR / nDSG Art. 31(2) lit. a (contractual basis); "
            "escalation invokes vital-interests basis under Art. 9(2)(c) GDPR "
            "/ nDSG Art. 31(2) lit. d, subject to a strict proportionality test."
        ),
        "paper_section": "§5",
        "exhibit_id": "Exhibit A.7",
    },
}


def get(tag: LegalAxisTag) -> LegalMapping:
    """Return the mapping for a legal-axis tag. Raises ``KeyError`` if missing."""
    return _LEGAL_MAP[tag]


def all_tags() -> tuple[LegalAxisTag, ...]:
    """Tuple of all declared LegalAxisTag values, derived from the type alias."""
    return get_args(LegalAxisTag)


def assert_total() -> None:
    """Verify every declared tag has a mapping. Used by tests and at demo startup."""
    declared = set(all_tags())
    mapped = set(_LEGAL_MAP.keys())
    missing = declared - mapped
    extra = mapped - declared
    if missing or extra:
        raise AssertionError(
            f"legal_map totality violation. missing={missing} extra={extra}"
        )
