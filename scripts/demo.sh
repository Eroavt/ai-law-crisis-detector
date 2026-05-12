#!/usr/bin/env bash
# Workshop / quick-look demo. Launches the Streamlit app and prints a
# checklist of what the audience can do with it.
#
# Usage: ./scripts/demo.sh
#   (or: bash scripts/demo.sh)

set -euo pipefail
cd "$(dirname "$0")/.."

echo
echo "=== AI-Law Crisis Detector — quick demo ==="
echo
echo "Loading the artifact and checking the data is in place..."
echo

uv run python -c "
from pathlib import Path
from aldc.corpus_gen import read_jsonl as read_corpus
from aldc.detector import read_jsonl as read_detections
from aldc.baselines import read_jsonl as read_baselines
from aldc import legal_map

issues = []
try:
    convos = read_corpus(Path('data/corpus.jsonl'))
    print(f'  ✓ Corpus loaded: {len(convos)} conversations')
except Exception as e:
    issues.append(f'corpus.jsonl: {e}')

try:
    dets = read_detections(Path('results/detections.jsonl'))
    print(f'  ✓ Detections loaded: {len(dets)} rater outputs')
except Exception as e:
    issues.append(f'detections.jsonl: {e}')

try:
    base = read_baselines(Path('results/baselines.jsonl'))
    print(f'  ✓ Baselines loaded: {len(base)} continuations')
except Exception as e:
    issues.append(f'baselines.jsonl: {e}')

legal_map.assert_total()
print(f'  ✓ Legal map total: {len(legal_map.all_tags())} axes')

if issues:
    print('  ✗ Issues:')
    for i in issues: print(f'    - {i}')
    exit(1)
"

echo
echo "Data looks good. Pick a conversation to look at:"
echo "  - kst_01 — Raine-pattern (indirect knowledge-seeking)"
echo "  - ad_01  — Setzer-pattern (anthropomorphic dependence, minor)"
echo "  - mtd_03 — Eliza-pattern (multi-turn drift, level 5)"
echo "  - fp_01  — philosophical-curiosity baseline (should NOT flag)"
echo "  - pvi_02 — privacy-vs-intervention edge case"
echo
echo "Launching Streamlit demo at http://localhost:8501 ..."
echo "  Main tab: side-by-side comparison of 5 deployment arms"
echo "  Regulator Mode tab: 12-check AI Act / GDPR / PLD / Art. 115 StGB audit"
echo

exec uv run streamlit run app/demo.py
