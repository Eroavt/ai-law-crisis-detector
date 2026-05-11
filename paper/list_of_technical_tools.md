# List of Technical Tools — UZH §4.5 disclosure

In accordance with the Faculty of Law's *Guidelines for Academic Essays* §4.5, we
disclose the technical tools used in the preparation of this paper and the
accompanying research artifact.

## Tools used and their role

**Claude Opus 4.7 and Claude Sonnet 4.6 (Anthropic).** Used inside the research
artifact (described in Document B) as the calibrated raters that score
conversational transcripts against the Columbia Suicide Severity Rating Scale
and the NIMH Ask Suicide-Screening Questions, and as the generator of the
stratified synthetic-dialogue corpus. The system prompts, the parameter
choices, and the JSONL outputs are checked into the repository at
`src/aldc/prompts/` and `data/corpus.jsonl`; the runs are reproducible from
`docs/REPRODUCE.md`. Use of these models inside the artifact is the
methodological subject of Document C §2, not an undisclosed editorial aid.

**GitHub Copilot and Anthropic Claude (assistant context).** Used in the
software-engineering portion of the artifact — code architecture review, bug
fixes, refactoring suggestions, and integration-test scaffolding for the
detector pipeline (`src/aldc/runtime.py`, `src/aldc/eval.py`, the Streamlit
demo). The artifact's working logic, the prompt designs, the corpus
parametrisation, and the legal mapping in `src/aldc/legal_map.py` are
authored by us.

**Research assistance.** We used Claude as a research aid to identify
publicly available primary-law sources (EUR-Lex, Fedlex, bger.ch) and to
locate publicly filed court complaints in the cases discussed in the paper
(*Garcia v. Character Technologies*, *Raine v. OpenAI*, *Gavalas v. Google*).
The act of citing each source and of verifying that the citation accurately
represents the source was performed by the authors. The legal reasoning and
the doctrinal positions taken in the paper are our own.

## Tools NOT used in this paper

We did not use AI tools to draft, paraphrase, summarise, translate, or
otherwise generate the text of this paper or its footnotes. All prose, all
doctrinal arguments, all citations, and all reform proposals in Documents A,
B and C reflect the authors' own work.

---

[signed by the three authors at the time of submission]
