# Artifact → Paper crosswalk

Each artifact output maps to a specific paragraph or evidentiary appendix in
the paper. Use this when writing or reviewing — every claim that depends on
the artifact should be traceable through this table.

| Artifact output | Paper section it grounds | Use in argument |
|---|---|---|
| `data/corpus.jsonl` (35 → 300 dialogues) | §2 Methodology; Appendix Exhibit A | Demonstrates breadth + axis coverage; basis for every per-axis F1. |
| `data/corpus_seed.yaml` | §2 Methodology | Documents the parametric generation grid (stratification). |
| `data/exhibit_set.jsonl` (12 worked examples) | §3.6, §4.4 worked examples | Specific *Raine* / *Setzer* / *Eliza* patterns analysed in legal prose. |
| `data/policy_excerpts/*` (dated) | §3.6 + Appendix Exhibit E | Establishes what each provider's *published policy* says — basis for the "policy-only baseline still fails X%" claim. |
| `results/detections.jsonl` (two raters per conversation) | §2 Methodology; Appendix Exhibit B | Source for κ and per-axis F1. |
| `results/baselines.jsonl` | §3.6, §4.4; Appendix Exhibit C | Source for naive-fail-rate, policy-fail-rate, detector-wrapped-success-rate. |
| `results/live_providers.jsonl` | §3.6 Live Industry Scorecard; Appendix Exhibit D | The "as of May 2026" empirical claim against each commercial provider. |
| `results/adversarial.jsonl` + `results/adversarial_decay.json` | §3.6 Figure 2 (guardrail decay); Appendix Exhibit F | Empirical reproduction of the Setzer / Eliza multi-turn pattern. |
| `results/multilingual.jsonl` (if generated) | §3.6 Cross-lingual robustness paragraph; Appendix Exhibit | DE / FR / IT comparison — anticipates the Swiss-jurisdiction challenge. |
| `results/metrics.json` | Document B Results Table; §3.4 Performable Duty prong 1 | All F1, κ, CIs, failure rates, $/case. |
| `results/report.md` | Document B Project Description | Auto-generated summary that drops in verbatim. |
| `results/scorecard.md` | Document B Table 1 | The Industry Scorecard chart row labels + cell values. |
| Cost ledger in `metrics.json` (`detector_cost_per_call_usd`, `projected_cost_per_user_month_usd`) | §3.4 Performable Duty prong 2 (*Wirtschaftliche Zumutbarkeit*) | The dollar number that kills the "too expensive" defense. |
| `src/aldc/safe_response.py` | §3.4 prong 3 (integration overhead) | "~250 LOC, one engineer-week" claim — auditable from this file. |
| `src/aldc/legal_map.py` | §3.3, §4 every legal-axis discussion | The technical-legal contract: each axis tag → article + leading case + doctrinal claim. |
| `src/aldc/regulator_view.py` + Streamlit Regulator Mode tab | §4.4 Defect taxonomy + Workshop slide 5 | The AI Act conformity audit — turns the artifact from "classifier" into "compliance instrument". |
| Bootstrap 95% CIs (in `metrics.json`) | §3.4 Performable Duty (all three prongs); §2 Methodology | Statistical rigor expected by the CS audience (Bernstein). |
| `src/aldc/runtime.py` + the cost-equivalent ledger | §2 Methodology; §3.4 prong 2 footnote | Two backends documented; the "free via Max" vs "$X via API" honesty. |
| `docs/ETHICS.md` | §2 Synthetic-data ethics paragraph | Pre-emptively answers the ethics-of-synthetic-suicide-data question. |

## Workshop slides → artifact

| Slide | Artifact element |
|---|---|
| Slide 1 (the harm) | quotations from Setzer / Raine / Eliza court filings (no artifact dependency). |
| Slide 2 (thesis) | `results/scorecard.md` headline numbers. |
| Slides 3–6 (live demo) | `app/demo.py` running on Erik's laptop or `aldc-uzh.streamlit.app`. |
| Slide 7 (Industry Scorecard chart) | `results/scorecard.md` + chart derived from `metrics.json`. |
| Slide 8 (Cross-lingual robustness) | per-language F1 table from `metrics.json`. |
| Slide 9 (Art. 3 bis PrHG drafted text) | paper §4.3 (no artifact dependency). |
| Slide 10 (limitations) | `docs/ETHICS.md` + the §7 neuro-overreach paper section. |
