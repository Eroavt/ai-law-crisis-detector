# AI-Law Crisis Detector (ALDC)

Research artifact accompanying the paper **"Duty, Defect, and Disclosure: Reassessing Developer Liability for LLM Chatbots in Suicidal Crises under the EU and Swiss Law"** (UZH FS26 *AI: Technology and Law*, Profs. Thouvenin & Bernstein, May 2026).

## What this is

ALDC is a clinically-grounded, calibrated detection pipeline that classifies a chat conversation against the Columbia Suicide Severity Rating Scale (C-SSRS) and the NIMH Ask Suicide-Screening Questions (ASQ), and emits a structured `DetectionResult` linking the case to a specific Swiss / EU legal article. The artifact is the technical premise of the paper's central legal claim:

> **The foreseeability gap has closed.** Crisis detection in conversational AI is technically performable with off-the-shelf models at marginal cost. Failure to deploy is no longer a research limitation — it is a foreseeable, defective design choice.

## What this is not

Not a clinical tool. Not deployable as-is in production without a proper safety review, locale-appropriate hotlines, and human-on-the-loop oversight. Synthetic data is for *evaluation*, not training.

## Architecture

```
Conversation ──► Detector (Opus 4.7, two raters at T=0.0 and T=0.3)
                       │
                       ├─► DetectionResult (C-SSRS, ASQ, markers, dynamics, action, trace)
                       │
                       └─► Cohen's κ between raters
Conversation ──► 3-arm baselines: naive / policy-only / detector-wrapped
Conversation ──► Live providers: OpenAI / Google / Anthropic / Character.AI
                       │
                       └─► The Industry Scorecard (paper Document B Table 1)
```

## Layout

- `src/aldc/schemas.py` — the law/code contract.
- `src/aldc/legal_map.py` — every legal-axis tag → article + case + doctrinal claim + paper section.
- `src/aldc/prompts/` — load-bearing system prompts.
- `src/aldc/detector.py` — Opus-based calibrated rater.
- `src/aldc/baselines.py` — three-arm contrast.
- `src/aldc/live_providers.py` — multi-provider scorecard generator.
- `src/aldc/safe_response.py` — graduated safe-response module with Swiss + intl. hotlines.
- `app/demo.py` — Streamlit demo, the workshop-presentation hinge.
- `data/corpus.jsonl` — paper Exhibit A (35-dialogue MVP, expanding to 150).
- `results/` — paper Exhibits B–H.
- `docs/` — ETHICS, REPRODUCE, ARTIFACT_TO_PAPER, DATASHEET, MODEL_CARD.

## Setup

```bash
uv sync                    # install deps (or: uv sync --extra live for live-provider arm)
cp .env.example .env       # then put your ANTHROPIC_API_KEY in .env
uv run pytest              # smoke test
```

## Reproducibility

See `docs/REPRODUCE.md` for the exact recipe (model versions, dates, costs).

## License

MIT. Authors: Erik Avtandilyan, Athira Ashokan, Nishant Kumar Singh.
