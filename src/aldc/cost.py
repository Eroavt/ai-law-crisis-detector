"""Cost ledger.

Aggregates per-call costs and projects to per-active-user-month figures used
in the paper's *Wirtschaftliche Zumutbarkeit* analysis (the second prong of the
Performable Duty doctrine: economic reasonableness).
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from aldc.schemas import DetectionResult, ProviderResponse


@dataclass(frozen=True)
class CostSummary:
    detector_total_usd: float
    detector_calls: int
    detector_cost_per_call_usd: float
    baseline_total_usd: float
    baseline_calls: int
    grand_total_usd: float
    # Projection: a moderate consumer chatbot user has ~50 messages/month.
    projected_user_messages_per_month: int
    projected_cost_per_user_month_usd: float

    def as_dict(self) -> dict:
        return {
            "detector_total_usd": round(self.detector_total_usd, 6),
            "detector_calls": self.detector_calls,
            "detector_cost_per_call_usd": round(self.detector_cost_per_call_usd, 6),
            "baseline_total_usd": round(self.baseline_total_usd, 6),
            "baseline_calls": self.baseline_calls,
            "grand_total_usd": round(self.grand_total_usd, 6),
            "projected_user_messages_per_month": self.projected_user_messages_per_month,
            "projected_cost_per_user_month_usd": round(
                self.projected_cost_per_user_month_usd, 6
            ),
        }


def summarise(
    detections: Iterable[DetectionResult],
    baselines: Iterable[ProviderResponse],
    *,
    msgs_per_user_per_month: int = 50,
) -> CostSummary:
    det_list = list(detections)
    base_list = list(baselines)
    det_total = sum(d.api_cost_usd for d in det_list)
    det_calls = len(det_list)
    cost_per_call = det_total / det_calls if det_calls else 0.0
    base_total = sum(b.api_cost_usd for b in base_list)
    base_calls = len(base_list)
    return CostSummary(
        detector_total_usd=det_total,
        detector_calls=det_calls,
        detector_cost_per_call_usd=cost_per_call,
        baseline_total_usd=base_total,
        baseline_calls=base_calls,
        grand_total_usd=det_total + base_total,
        projected_user_messages_per_month=msgs_per_user_per_month,
        projected_cost_per_user_month_usd=cost_per_call * msgs_per_user_per_month,
    )
