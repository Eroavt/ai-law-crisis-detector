# Convenience targets for the AI-Law Crisis Detector artifact.
#
# Anything you can do with `uv run python ...` you can also do here in one word.
# Used during workshop rehearsal so the live-demo path is `make demo` and not a
# command remembered under stress.

.DEFAULT_GOAL := help

UV    ?= uv
PY    := $(UV) run python
PYTEST := $(UV) run pytest

.PHONY: help demo demo-check test figure2 paper preflight regulator evaluate clean

help:
	@echo "AI-Law Crisis Detector — make targets"
	@echo ""
	@echo "  make demo         Workshop demo: preflight, then Streamlit on :8501"
	@echo "  make demo-check   Preflight only (no Streamlit launch)"
	@echo "  make test         Full test suite (paper-metric anchors included)"
	@echo "  make figure2      Rebuild Figure 2 (no API calls)"
	@echo "  make regulator    Re-run Regulator-Mode audits"
	@echo "  make evaluate     Re-run evaluation (metrics.json, report.md)"
	@echo "  make paper        Rebuild PAPER_FINAL_DRAFT.md"
	@echo "  make submission   Rebuild paper + generate UZH-§6-formatted .docx and .pdf"
	@echo "  make preflight    test + figure2 + paper-rebuild, end-to-end"
	@echo "  make clean        Remove __pycache__ and *.pyc"

demo:
	@bash scripts/demo.sh

demo-check:
	@$(PY) -c "from pathlib import Path; \
from aldc.corpus_gen import read_jsonl as rc; from aldc.detector import read_jsonl as rd; \
from aldc.baselines import read_jsonl as rb; from aldc import legal_map; \
c=rc(Path('data/corpus.jsonl')); d=rd(Path('results/detections.jsonl')); b=rb(Path('results/baselines.jsonl')); \
legal_map.assert_total(); \
print(f'corpus={len(c)} detections={len(d)} baselines={len(b)} legal_axes={len(legal_map.all_tags())}'); \
print('preflight OK')"

test:
	@$(PYTEST) -q

figure2:
	@$(PY) scripts/build_figure2.py

regulator:
	@$(PY) scripts/09_run_regulator_audits.py

evaluate:
	@$(PY) scripts/08_evaluate.py

paper:
	@$(PY) scripts/build_paper_final.py

submission: paper
	@$(PY) scripts/build_submission_docx.py

preflight: test figure2 paper
	@echo ""
	@echo "Preflight complete. Repo state is workshop-ready."

clean:
	@find . -type d -name __pycache__ -prune -exec rm -rf {} +
	@find . -type f -name '*.pyc' -delete
	@echo "Cleaned __pycache__ and *.pyc"
