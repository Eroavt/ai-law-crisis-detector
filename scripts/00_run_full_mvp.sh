#!/usr/bin/env bash
# Full MVP pipeline: corpus → detection → baselines → evaluation.
# Idempotent in the sense that each step writes its own output file; re-running
# overwrites. Pass --skip-corpus / --skip-detection / --skip-baselines to
# resume from a partial run.

set -euo pipefail
cd "$(dirname "$0")/.."

SKIP_CORPUS=0
SKIP_DETECTION=0
SKIP_BASELINES=0

for arg in "$@"; do
  case "$arg" in
    --skip-corpus)    SKIP_CORPUS=1 ;;
    --skip-detection) SKIP_DETECTION=1 ;;
    --skip-baselines) SKIP_BASELINES=1 ;;
    -h|--help)
      echo "Usage: $0 [--skip-corpus] [--skip-detection] [--skip-baselines]"
      exit 0
      ;;
    *)
      echo "Unknown arg: $arg" >&2; exit 2 ;;
  esac
done

echo "ALDC MVP pipeline — $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "Backend: ${ALDC_BACKEND:-claude_code} (override via ALDC_BACKEND=api)"
echo

if [[ "$SKIP_CORPUS" -eq 0 ]]; then
  echo "[1/4] Generating corpus..."
  uv run python scripts/01_generate_corpus.py
fi

if [[ "$SKIP_DETECTION" -eq 0 ]]; then
  echo "[2/4] Running two-rater detection..."
  uv run python scripts/02_run_detection.py
fi

if [[ "$SKIP_BASELINES" -eq 0 ]]; then
  echo "[3/4] Running 5-arm baselines..."
  uv run python scripts/03_run_baselines.py
fi

echo "[4/4] Evaluating..."
uv run python scripts/08_evaluate.py

echo
echo "Done. See:"
echo "  - data/corpus.jsonl"
echo "  - results/detections.jsonl"
echo "  - results/baselines.jsonl"
echo "  - results/metrics.json"
echo "  - results/report.md"
echo
echo "Streamlit demo:  uv run streamlit run app/demo.py"
