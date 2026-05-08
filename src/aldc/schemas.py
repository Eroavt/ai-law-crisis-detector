"""Pydantic schemas — the law/code contract.

The `legal_axis_tag` enum is the single point where the technical artifact
meets the legal argument. Every tag must have a mapping in `legal_map.py`;
the demo refuses to render a conversation whose tag has no mapping.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

# C-SSRS ideation severity, levels 0-5 (Columbia Suicide Severity Rating Scale)
CssrsLevel = int

LegalAxisTag = Literal[
    "knowledge_seeking_trap",     # AI Act Art. 5(1)(a); Raine pattern
    "anthropomorphic_dependence",  # Setzer / Character.AI pattern
    "multi_turn_drift",           # Belgian "Eliza" / Chai pattern
    "method_availability",        # explicit means inquiry
    "vulnerable_user",            # AI Act Art. 5(1)(b); minor / bereaved / divorced
    "false_positive_baseline",    # philosophical curiosity — must NOT trigger
    "privacy_vs_intervention",    # GDPR Art. 9(2)(c) / nDSG Art. 31(2) lit. d
]

ActionLevel = Literal[
    "acknowledge",
    "empathic_redirect",
    "hand_off_to_hotline",
    "emergency_intervention",
]

AgeBand = Literal["minor_under_18", "adult_18_64", "elderly_65_plus"]

UserContext = Literal["bereaved", "divorced", "isolated", "philosophical_only"]

ArmId = Literal[
    "detector",
    "naive_baseline",
    "policy_baseline_openai",
    "policy_baseline_anthropic",
    "policy_baseline_character_ai",
    "live_openai_gpt4o",
    "live_openai_gpt4o_mini",
    "live_google_gemini25pro",
    "live_google_gemini25flash",
    "live_anthropic_sonnet46",
    "live_character_ai_web",
]

RaterId = Literal["rater_1_opus_t0", "rater_2_opus_t03", "rater_3_deberta"]


class Turn(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class Demographic(BaseModel):
    age_band: AgeBand
    context: list[UserContext] = Field(default_factory=list)


class GroundTruth(BaseModel):
    cssrs_level: int = Field(ge=0, le=5)
    asq_responses: tuple[bool, bool, bool, bool]
    legal_axis_tag: LegalAxisTag
    expected_action: ActionLevel
    demographic: Demographic


class Conversation(BaseModel):
    id: str
    turns: list[Turn]
    ground_truth: GroundTruth
    generation_notes: str | None = None
    exhibit_id: str | None = None


class DetectionResult(BaseModel):
    conversation_id: str
    arm: ArmId = "detector"
    rater_id: RaterId | None = None
    cssrs_level: int = Field(ge=0, le=5)
    asq_responses: tuple[bool, bool, bool, bool]
    linguistic_markers: list[str]
    dynamics_score: float = Field(ge=0, le=1)
    recommended_action: ActionLevel
    reasoning_trace: str
    model_version: str
    temperature: float
    timestamp_utc: str
    api_cost_usd: float = 0.0
    latency_ms: int = 0


class ProviderResponse(BaseModel):
    """Raw response from a live commercial LLM provider for a given conversation."""

    conversation_id: str
    provider: str
    model_version: str
    timestamp_utc: str
    full_response_text: str
    api_cost_usd: float = 0.0
    latency_ms: int = 0
    flagged_for_safety: bool = False
