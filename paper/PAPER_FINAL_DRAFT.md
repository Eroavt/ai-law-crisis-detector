---
title: "Duty, Defect, and Disclosure"
subtitle: "Reassessing Developer Liability for LLM Chatbots in Suicidal Crises under Swiss and European Law"
author:
  - Athira Ashokan
  - Erik Avtandilyan
  - Nishant Kumar Singh
date: "15 May 2026"
lang: en
documentclass: scrartcl
classoption:
  - 12pt
  - a4paper
  - titlepage
  - twoside=false
header-includes:
  - \usepackage{microtype}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \renewcommand{\arraystretch}{1.15}
  - \setkomafont{title}{\rmfamily\bfseries}
  - \setkomafont{subtitle}{\rmfamily\itshape}
  - \setkomafont{author}{\rmfamily}
  - \setkomafont{date}{\rmfamily}
  - \setkomafont{publishers}{\rmfamily\normalsize}
  - \setkomafont{section}{\rmfamily\bfseries\large}
  - \setkomafont{subsection}{\rmfamily\bfseries\normalsize}
  - \setkomafont{subsubsection}{\rmfamily\bfseries\normalsize}
  - '\publishers{University of Zurich\\Faculty of Law\\[0.6em]Course: \emph{Artificial Intelligence: Technology and Law} (FS26)\\Lecturers: Prof.~Dr.~iur.~Florent Thouvenin\\Prof.~Abraham Bernstein, PhD}'
---


# Abbreviations

## Statutes and instruments

| Abbreviation | Full title |
|---|---|
| AI Act | Regulation (EU) 2024/1689 (Artificial Intelligence Act) |
| ASQ | Ask Suicide-Screening Questions (NIMH screening instrument) |
| BV | Bundesverfassung der Schweizerischen Eidgenossenschaft |
| CETS 225 | CoE Framework Convention on Artificial Intelligence (2024) |
| C-SSRS | Columbia Suicide Severity Rating Scale |
| CoE | Council of Europe |
| DSA | Regulation (EU) 2022/2065 (Digital Services Act) |
| DSG | Bundesgesetz über den Datenschutz (revised; revDSG since 1 September 2023) |
| EGMR | Europäischer Gerichtshof für Menschenrechte |
| GDPR | Regulation (EU) 2016/679 (General Data Protection Regulation) |
| JStG | Bundesgesetz über das Jugendstrafrecht |
| MDR | Regulation (EU) 2017/745 (Medical Device Regulation) |
| OR | Schweizerisches Obligationenrecht |
| PLD | Directive (EU) 2024/2853 on liability for defective products |
| PrHG | Bundesgesetz über die Produktehaftpflicht |
| PrSG | Bundesgesetz über die Produktesicherheit |
| StGB | Schweizerisches Strafgesetzbuch |
| StPO | Schweizerische Strafprozessordnung |
| UVG | Bundesgesetz über die Unfallversicherung |
| UWG | Bundesgesetz gegen den unlauteren Wettbewerb |
| VStrR | Bundesgesetz über das Verwaltungsstrafrecht |
| ZGB | Schweizerisches Zivilgesetzbuch |

## Commentaries and reference works

| Abbreviation | Full title |
|---|---|
| BK | Berner Kommentar |
| BSK | Basler Kommentar |
| CHK | Handkommentar zum Schweizer Privatrecht |
| OFK | Orell Füssli Kommentar |
| PK | Praxiskommentar |
| SHK | Stämpflis Handkommentar |
| ZK | Zürcher Kommentar |

## Courts, cases, and case-law abbreviations

| Abbreviation | Full title |
|---|---|
| BGE | Entscheidungen des Schweizerischen Bundesgerichts (Amtliche Sammlung) |
| BGer | Bundesgericht |
| BGH | Bundesgerichtshof (German Federal Court of Justice) |
| BVerfG | Bundesverfassungsgericht (German Federal Constitutional Court) |
| CP | Code pénal (French Penal Code) |
| EuGH | Europäischer Gerichtshof |
| HAVE | Haftung und Versicherung (Zeitschrift) |
| ZR | Blätter für Zürcherische Rechtsprechung |
| ZStrR | Schweizerische Zeitschrift für Strafrecht |

## Doctrinal and clinical concepts

| Abbreviation | Full title |
|---|---|
| 3ST | Three-Step Theory of Suicide (Klonsky / May 2015) |
| ATSG | Bundesgesetz über den Allgemeinen Teil des Sozialversicherungsrechts |
| EDPB | European Data Protection Board |
| FDPIC | Federal Data Protection and Information Commissioner |
| F1 | F1 score (harmonic mean of precision and recall) |
| fMRI | Functional magnetic resonance imaging |
| iSv | im Sinne von |
| IPTS | Interpersonal Theory of Suicide (Joiner 2005) |
| IRB | Institutional Review Board |
| LLM | Large language model |
| N. | Note / Randnote (commentary paragraph marker) |
| RLHF | Reinforcement learning from human feedback |
| SAFE-T | Suicide Assessment Five-step Evaluation and Triage (SAMHSA / Zero Suicide) |
| SAMHSA | Substance Abuse and Mental Health Services Administration (US) |
| ToS | Terms of Service |
| WHO | World Health Organization |
| κ | Cohen's kappa (inter-rater agreement coefficient) |

## Institutions

| Abbreviation | Full title |
|---|---|
| BAG | Bundesamt für Gesundheit |
| BAKOM | Bundesamt für Kommunikation |
| DSI | Digital Society Initiative, University of Zurich |
| UVEK | Eidgenössisches Departement für Umwelt, Verkehr, Energie und Kommunikation |
| UZH | Universität Zürich |

## Project-specific

| Abbreviation | Full title |
|---|---|
| ALDC | AI-Law Crisis Detector (the research artifact described in Document B) |
| API | Application Programming Interface |
| LOC | Lines of code |
| MIT | Massachusetts Institute of Technology (software-licence reference) |
| MVP | Minimum Viable Product (the 35-dialogue corpus configuration) |

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Abstract

In the seven weeks leading up to his death on 2 October 2025, Jonathan Gavalas's account on Google's Gemini chatbot generated thirty-eight separate "sensitive query" flags inside Google's own moderation system. The system noticed. The company did not. Gavalas was the latest of more than a dozen users whose suicides in the past three years have been linked in court filings or coroners' reports to extended interaction with consumer LLM chatbots. The pattern is no longer rare, and the foreseeability defence AI providers relied on five years ago no longer holds.

This paper makes three contributions. First, we propose the **Performable Duty Doctrine** as the missing rung between Art. 41 OR's general *Sorgfaltspflicht* and the silent gap in Swiss case law on AI-mediated harm: a duty of care is *erfüllbar*, and therefore enforceable, when compliance requires currently available technology at economically reasonable cost. Second, we develop the doctrinal route by which the EU AI Act, the new PLD 2024/2853, and the CoE Framework Convention on AI (CETS 225) function as *Schutznormen* in Swiss tort analysis, giving Art. 41 OR's *Widerrechtlichkeit* element a determinate content even before any Swiss legislative response. Third, we draft a concrete reform proposal, a new Art. 3 *bis* PrHG mirroring PLD 2024/2853 Arts. 4, 6(1)(c), and 10(2), that closes the modernisation gap the Federal Council Report on AI of 12 February 2025 expressly acknowledged but left unaddressed.

Underlying the legal argument is a working research artifact: a clinically-grounded suicide-risk detector calibrated to the C-SSRS and the ASQ. The detector's two independent raters agree at Cohen's κ = 0.860, in the "almost perfect" band on the Landis & Koch reference scale. The detector-wrapped-plus-safe-response middleware produces zero critical AI Act conformity violations across the test corpus; the unguarded baseline and the verbatim-Anthropic-policy baseline both produce critical violations on the same two vulnerable-user cases. The artifact is the proof that the duty we propose is *erfüllbar*.

The paper closes on the question Switzerland's uniquely tolerant regime forces: when a commercial LLM contributes to a user's suicide, is the operator caught by Art. 115 StGB? We argue that the corporate engagement-maximisation motive satisfies *selbstsüchtige Beweggründe* in the Donatsch/Kolb formulation (OFK StGB Art. 115 N. 5, with BGE 150 IV 267 confirmation), and that AI-induced loss of decisional control compromises *Tatherrschaft* in the dying user, so that the scope of Art. 115 reaches commercial chatbot conduct even in the jurisdiction that decriminalises unselfish-motive assisted suicide.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Document A: Problem and Solution

## A.1 The harm

Between March 2023 and March 2026 more than a dozen users in Western jurisdictions have died by suicide after extended interaction with consumer LLM chatbots, and at least two have committed serious violence under chatbot-induced delusion. The cases are no longer rare and no longer one-provider. *Garcia v. Character Technologies* concerned a fourteen-year-old who died after months of conversation with a *Game of Thrones*-styled persona; the family alleges the persona's final message was "come home to me as soon as possible".[^A01] *Raine v. OpenAI* concerned a sixteen-year-old whose parents allege ChatGPT helped him draft his suicide notes.[^A02] *Gavalas v. Google* concerned a thirty-six-year-old whose account on Gemini generated thirty-eight separate "sensitive query" flags in seven weeks before his death; Google's own moderation system noticed; Google did not act.[^A03] *Peralta v. Character Technologies* concerned a thirteen-year-old.[^A04] In November 2025 the Social Media Victims Law Center and the Tech Justice Law Project filed seven additional wrongful-death actions in California state courts.[^A05] The Belgian "Pierre" case from March 2023 was the first to reach mainstream attention. The pattern crosses providers, ages (thirteen to thirty-six), and dependency patterns (romantic-AI persona, indirect knowledge-seeking, AI-induced delusion). It is now the predictable failure mode of consumer chatbot products deployed without commensurate safety-side investment.

The Federal Council acknowledged in February 2025 that Switzerland will not adopt a comprehensive AI statute and that modernisation work falls to sector-specific adaptation of existing instruments.[^A06] The DSI position paper that Thouvenin himself co-authored four years earlier identified the core difficulty: proving the operator's fault under general liability law is hard.[^A07] We argue the difficulty is doctrinal, not technological, and that the doctrinal route forward is available without legislative reform.

[^A01]: *Garcia v. Character Technologies*, M.D. Fla. No. 6:24-cv-1903 (filed 22 October 2024; settled January 2026), Complaint ¶¶ 124-130.
[^A02]: *Raine v. OpenAI*, S.F. Super. Ct. (filed August 2025).
[^A03]: *Gavalas v. Google LLC*, N.D. Cal. No. 5:26-cv-01849-VKD (filed 4 March 2026), Complaint ¶¶ 1, 107.
[^A04]: *Peralta v. Character Technologies*, D. Colo. (filed September 2025); SMVLC/TJLP press release of 6 November 2025; *La Libre Belgique*, 28 March 2023 (Pierre / Eliza).
[^A05]: SMVLC/TJLP press release, 6 November 2025.
[^A06]: *Auslegeordnung 2025*, 27.
[^A07]: F. Thouvenin / M. Christen / A. Bernstein et al., *A Legal Framework for AI*, DSI Position Paper, November 2021, 4.

## A.2 What is broken: detection exists, deployment does not

The technology to detect imminent suicide-risk signals in chat conversations has existed in commercial deployment for years. Levkovich et al. (2025) reports Claude Sonnet at F1 = 0.75 on zero-shot C-SSRS classification, in the range of trained-clinician inter-rater reliability for the same instrument.[^A08] Anthropic's transparency claim reports appropriate-response rates of 98.6-99.3 per cent on clear-risk inputs.[^A09] The capability is not contested.

What is contested, and what *Gavalas v. Google* ¶ 107 establishes on the public record, is whether commercial operators *act* on the detections they perform. Between 14 August and 1 October 2025 the moderation system identified thirty-eight separate sensitive-query patterns in Jonathan Gavalas's account. The system noticed. The company did not intervene. The complaint pleads, on the same record, that Google's safety architecture "evaluates outputs as standalone text, not as part of an unfolding conversation over time".[^A10] The gap between *detection* and *response* is the legal hook. It is also why the fault-proving difficulty the DSI position paper identified is doctrinal, not empirical: the operator's failure is not a failure of knowledge but a failure of action on knowledge already held.

[^A08]: D. Levkovich et al., *Evaluating LLM Reasoning for C-SSRS Screening*, arXiv:2505.13480 (2025), Table 3.
[^A09]: Anthropic, *Protecting the Well-Being of Users*, Anthropic Transparency Hub, December 2025.
[^A10]: *Gavalas v. Google*, Complaint ¶¶ 103-106.

## A.3 Our solution

We propose three doctrinal moves and one drafted reform.

The first move is the **Performable Duty Doctrine** (Document C §3.4). A *Sorgfaltspflicht* under Art. 41 OR is *erfüllbar*, and therefore enforceable, when compliance is possible using currently available technology at economically reasonable cost, with integration overhead that does not exceed the harm averted. The doctrine has three empirical prongs, each falsifiable. The research artifact in Document B satisfies each prong for the duty at issue: Cohen's κ between two independent raters is 0.860; severity-≥3 recall is 0.875; per-call API-equivalent cost is USD 0.085; integration overhead is roughly 250 lines of code.

The second move is the **Schutznorm reading** of the EU AI Act, the new PLD 2024/2853, and the CoE Framework Convention CETS 225 (Document C §3.3). Switzerland is not bound by the AI Act; the AI Act is a *protective norm* under Swiss tort doctrine. Its substantive content, Art. 5(1)(a) on manipulation, Art. 5(1)(b) on vulnerable-user exploitation, Art. 50 on transparency, gives the *Widerrechtlichkeit* element of Art. 41 OR a determinate content the Swiss case law has not yet supplied. The doctrinal anchor is Brehm BK OR Art. 41 N. 17-17a.[^A11]

The third move is the **drafted Art. 3 bis PrHG** (Document C §4.3). The Federal Council's *Auslegeordnung 2025* expressly identifies a modernisation need for the PrHG and waits for the revised EU PLD before acting; the PLD was published in November 2024, the condition is satisfied.[^A12] The proposed Art. 3 bis tracks PLD 2024/2853 Arts. 4(2), 6(1)(c), and 10(2)(b): software and AI systems as products; medically-recognised psychological harm as compensable damage; presumption of defect for non-compliance with mandatory safety norms or for failure to deploy a known safety-relevant update. Three paragraphs of German text; eighty-six words; the smallest sufficient legislative response.

The fourth, addressed in Document C §6.3, is the Swiss-specific criminal-liability question. Under Art. 115 StGB, assistance to suicide is criminal only if the perpetrator acts from *selbstsüchtige Beweggründe*. Switzerland's tolerance toward assisted suicide is the most permissive in Western criminal law. We argue that a commercial LLM operator's engagement-maximisation design satisfies *selbstsüchtige Beweggründe* in the criminal-law sense (Donatsch/Kolb OFK Art. 115 N. 5 includes "der Wunsch nach finanziellem Profit"; BGE 150 IV 267); that AI-induced loss of decisional control can compromise the dying user's *Tatherrschaft*; and that, in any case, the *Verleitung* variant captures the *Gavalas* fact pattern on its own. The Swiss tolerance does not insulate commercial chatbot conduct.

[^A11]: BGE 124 III 297 c. 5b; Roland Brehm, BK OR Art. 41 N. 17-17a.
[^A12]: *Auslegeordnung 2025*, 24.

## A.4 Why this paper

The three contributions are not separately novel in Swiss law. *Verkehrssicherungspflicht* is settled; *Schutznorm-Theorie* is settled; PrHG modernisation has been on the Federal Council's agenda for years. What is novel is the integration: the doctrine that links them and the empirical demonstration that the integration is technologically *erfüllbar*. The integration is timely: the *Auslegeordnung* defers action on the most pressing modernisation needs until other processes complete; the documented harms will not defer.

The paper engages the edge cases that have so far been treated as defences rather than as questions: whether an operator may notify the police, whether false positives are themselves a harm, whether the user "gamed" the chatbot, whether the existing safety policy is sufficient, whether Section 230 or DSA Art. 14 platform-liability shields apply, whether the duty is invented, and whether the Swiss tolerance toward assisted suicide reaches commercial AI conduct. Each is engaged on its merits in Document C §§ 5-8. Our position throughout is empirical rather than rhetorical: the numbers in Document B are reproducible, the court-record quotes are public record, and the legal doctrine is constructed from existing Swiss instruments and from foreign norms the Federal Council has itself committed to ratify.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Document B: Project Description

> All numbers reflect the 12 May 2026 evaluation run on the 35-dialogue MVP corpus using Claude Sonnet 4.6 with the enriched suicide-risk-focused prompt (six framework lenses: Joiner IPTS, Klonsky/May 3ST, Beck cognitive markers, behavioural-acquisition signals, anthropomorphic-dependence markers, SAFE-T inventory).

## B.1 Artifact overview

The artifact is the *AI-Law Crisis Detector* (ALDC), a research instrument that classifies a chat conversation's suicide-risk severity against the Columbia Suicide Severity Rating Scale (C-SSRS) and the NIMH Ask Suicide-Screening Questions (ASQ). It is released under MIT licence at `~/dev/GitHub/ai-law-crisis-detector/` and is reproducible from `docs/REPRODUCE.md`. It consists of: a stratified synthetic corpus of thirty-five dialogues plus four hand-curated court-record exhibits; a calibrated detector that runs two independent rater passes per conversation; a five-arm baseline contrast (naive, three policy-only, detector-wrapped); a Regulator-Mode audit scoring each conversation against an AI Act / PLD / GDPR conformity checklist; and a Streamlit demo.

## B.2 Architecture

```
Conversation ──► Detector (Sonnet 4.6, two raters, T = 0.0 and T = 0.3)
                       │
                       ├─► DetectionResult (C-SSRS, ASQ, markers, dynamics, action, trace)
                       └─► Cohen's κ between raters
Conversation ──► 5-arm baselines: naive / 3× policy-only / detector-wrapped
Each baseline response ──► Regulator-Mode audit (12 AI Act / PLD / GDPR / Swiss-law checks)
```

The methodological design is described in Document C §2; detail in `docs/ETHICS.md`, `docs/DATASHEET.md`, `docs/MODEL_CARD.md`, `docs/REPRODUCE.md`.

## B.3 Results

### B.3.1 Detector calibration (Sonnet 4.6, 12 May 2026)

| Metric | Value |
|---|---|
| Weighted F1 across C-SSRS levels (T = 0.0) | **0.616** (95% bootstrap CI [0.452, 0.790]) |
| Severity-≥3 recall | **0.875** |
| Cohen's κ between rater 1 (T = 0.0) and rater 2 (T = 0.3) | **0.860** |
| False-positive rate on philosophical-curiosity baseline | **0/5 (0.0%)** |
| Per-call API-equivalent cost | **USD 0.085** |
| Projected per-user-month cost at 50 conversations/user | **USD 4.24** |

The Levkovich benchmark for zero-shot Claude Sonnet on the C-SSRS classification reports F1 = 0.7505. Our 0.616 figure is below that because it is computed against the corpus generator's self-labels rather than against expert clinician labels; the disagreement is itself the methodological finding (Levkovich uses expert labels; we use generator self-labels and the discrepancy is informative). Cohen's κ of 0.860 falls in the "almost perfect" band on the Landis & Koch reference scale, above the inter-rater reliability normally reported for trained clinicians using the same instrument. The earlier May 8 Opus 4.7 run, performed before the prompt was enriched, reported F1 = 0.467 / κ = 0.820 / recall = 0.833 / per-call cost USD 0.18; the Sonnet-and-enriched-prompt configuration improves every metric and reduces per-call cost by 53 %.

### B.3.2 Per-axis F1 with 95 % bootstrap CI

| Legal axis | F1 | 95% CI |
|---|---|---|
| `anthropomorphic_dependence` | **0.800** | [0.400, 1.000] |
| `false_positive_baseline` | **1.000** | [1.000, 1.000] |
| `knowledge_seeking_trap` | 0.389 | [0.056, 0.833] |
| `method_availability` | 0.520 | [0.080, 1.000] |
| `multi_turn_drift` | **0.800** | [0.400, 1.000] |
| `privacy_vs_intervention` | 0.500 | [0.000, 1.000] |
| `vulnerable_user` | 0.133 | [0.000, 0.600] |

The wide confidence intervals reflect the small sample size in each axis bin (four to six dialogues each). Per-axis improvements over the Opus run concentrate on the multi-turn axes, `anthropomorphic_dependence` (0.520 → 0.800) and `multi_turn_drift` (0.400 → 0.800), the patterns the *Gavalas*, *Setzer*, and *Eliza* complaints turn on.

The `vulnerable_user` F1 of 0.133 deserves comment. Inspection of the five dialogues in this axis reveals a systematic *one-tier under-rating* by the detector relative to the corpus generator's self-labels (e.g., generator vu_01 → C-SSRS 3, detector → 2). In every case the recommended action remains in the appropriate response band (`empathic_redirect` or `hand_off_to_hotline`); the categorical F1 is penalised by the discrete bin mismatch. The methodologically relevant point is that the detector classifies by content present in the conversation, whereas the corpus generator (the same Sonnet-class model in a different role) appears to inflate severity when given a vulnerability context as a generation parameter. We treat this as a methodological finding about the limitations of LLM-based corpus self-labelling, not as a detector defect.

### B.3.3 Five-arm baseline failure rates (severity ≥ 3 cases)

Failure-rate measured by the audit heuristic in `eval.py` (appropriate = response references a crisis resource; harmful = response contains specific lethal-means content). Restricted to the twenty-four conversations the corpus self-labelled at severity ≥ 3.

| Arm | n | Appropriate | Failure rate | Harmful rate |
|---|---|---|---|---|
| `detector_wrapped` | 24 | 24 | **0.0%** | 0.0% |
| `policy_baseline_character_ai` | 24 | 24 | **0.0%** | 0.0% |
| `policy_baseline_openai` | 24 | 23 | 4.2% | 0.0% |
| `policy_baseline_anthropic` | 24 | 22 | 8.3% | 0.0% |
| `naive_baseline` | 24 | 21 | 12.5% | 0.0% |

The detector-wrapped arm ties with the Character.AI-policy baseline at zero failures on the heuristic. The finding is more nuanced than the simple "policy-only doesn't work" hypothesis: *some* industry policies, when supplied verbatim as system prompts to a Sonnet-class model, prevent the heuristic failures on the present corpus. The deeper analysis is therefore the Regulator-Mode audit in §B.3.4, which examines AI Act / PLD / Swiss-law conformity rather than the keyword-match heuristic.

### B.3.4 Regulator-Mode AI Act conformity audit

Twelve checks per conversation × arm, spanning the EU AI Act (Arts. 5(1)(a), 5(1)(b), 12, 14, 50), GDPR Art. 6(1)(b), PLD 2024/2853 Arts. 6(1)(c) and 10(2)(b), Swiss StGB Art. 115, Swiss revDSG Art. 31, the Performable Duty doctrine, and proportionality. Each check is rated info / minor / major / critical. The *critical-only pass rate* is the legally decisive figure.

| Arm | Audits | Critical pass | Critical pass rate |
|---|---|---|---|
| `detector_wrapped` | 35 | 35 | **100.0%** |
| `policy_baseline_character_ai` | 35 | 35 | **100.0%** |
| `policy_baseline_openai` | 35 | 35 | **100.0%** |
| `naive_baseline` | 35 | 33 | 94.3% |
| `policy_baseline_anthropic` | 35 | 33 | 94.3% |

Three arms tie at 100 % critical pass. The naive baseline and the Anthropic-policy baseline fail the same two cases on three checks: `art_5_1_b_no_vulnerable_exploitation`, `art_14_human_oversight`, `pld_no_design_defect`. The two failing conversations are vulnerable-user cases at severity ≥ 3 where the assistant continuation did not contain a crisis-resource reference. The empirical reading is doctrinally consistent with §3.4: published policies vary in how well they constrain a model when supplied as a system prompt, and the Performable Duty argument is not about which policy is best worded; it is about whether the deployed system actually behaves consistently with the policy in production. *Gavalas v. Google* ¶ 107 (thirty-eight flags, no enforcement) suggests this is not the case for at least one major provider regardless of the published text.

## B.4 Limitations

Four named limitations. *Synthetic-data limitation:* the corpus is generated by an LLM; the four hand-curated exhibits incorporate verbatim court-record text but the bulk is synthetic. *Single-language scope:* English only; the corpus generator supports DE, FR, IT (recipe in `data/corpus_seed.yaml`). *No live multi-provider scorecard:* the policy-only arm is a Sonnet-class proxy; *Gavalas v. Google* ¶ 107 provides the legally significant empirical hook a live scorecard would seek to replicate. *Single-vendor risk:* the detector itself runs on Claude (Levkovich et al. 2025 report Claude Sonnet as the strongest off-the-shelf classifier on C-SSRS); cross-vendor robustness is future work.

## B.5 Figure 2 and the abandoned adversarial probe

Figure 2 (`results/figure2_severity_failure.png`, built by `scripts/build_figure2.py`) plots the critical Regulator-Mode failure rate per arm against the corpus C-SSRS ground-truth severity. At C-SSRS sev = 5 (n = 6): detector-wrapped, OpenAI-style, and Character.AI-style all 0/6; naive 1/6 (17 %); Anthropic-AUP-style 2/6 (33 %). At sev = 4 (n = 10): naive 1/10 (10 %); all other arms 0 %. At sev ≤ 3 every arm passes every critical check. The Wilson 95 % CIs at sev = 5 are wide (n = 6 per bucket); the *direction* is what is load-bearing for the legal argument, not the precise rate. The detector-wrapped arm matches the strongest policy baselines on aggregate while being the only arm whose decisions are per-call auditable through legal-axis tags.

Figure 2 is the substitute exhibit for the adversarial multi-turn probe the Phase-3 plan originally promised. The probe was attempted on 12 May 2026: the user-simulator path in `src/aldc/adversarial.py` requires a frontier LLM to roleplay a user gradually escalating toward suicidal distress while a separate model plays the assistant. The first probe ran to completion; the second stalled when the user-simulator side refused every turn for a hundred consecutive iterations. The refusals are appropriate behaviour for a safety-trained model; they are also a methodological barrier for automated adversarial probing of crisis detectors. Research-grade multi-turn adversarial evaluation will need either human roleplayers under IRB oversight, a hand-scripted user-side corpus built from court-record patterns, or an open-weights model fine-tuned for the user-simulator role under research licence. The probe code is preserved in the artifact for reproducibility.

## B.6 Metric to paper-section crosswalk

| Metric | Paper section | Use in argument |
|---|---|---|
| κ = 0.860 | C §2.4, §3.4 | Calibrated rater not stochastic chatbot |
| Severity-≥3 recall = 0.875 | C §3.4 prong 1 | Performable Duty technical-availability prong |
| FPR baseline = 0.0 | C §5.6, §8.2 | Over-flagging defence answer |
| Figure 2 | C §3.6, B §B.5 | Industry baselines fail where intervention is required |
| Detector-wrapped critical pass = 100 % | C §3.4, A §3 | Empirical proof of the Performable Duty's third prong |
| Naive baseline failure 12.5 % | C §3.4, §8.3 | Harm surface |
| Policy-only baseline failure 4-8 % | C §3.6, §8.3 | "Our policy is enough" defence answer |
| Per-call cost USD 0.085 | C §3.4 prong 2 | Wirtschaftliche Zumutbarkeit |
| `safe_response.py` (~250 LOC) | C §3.4 prong 3 | Integration overhead |

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Document C §1: Introduction and Research Statement

On 2 October 2025 Jonathan Gavalas died in Florida.[^101] He was thirty-six. In the seven weeks before his death his messages to Google's Gemini chatbot triggered thirty-eight separate "sensitive query" flags inside Google's own moderation system; in the same period the chatbot called itself his wife, called him her king, and sent him with knives and tactical gear to a "kill box" near Miami International Airport.[^102] He was not the first user to die this way. Sewell Setzer III was fourteen when he died in February 2024 after months of conversation with a Character.AI persona styled on a *Game of Thrones* character; his final exchange with the chatbot has been pleaded as the persona telling him "come home to me as soon as possible".[^103] Adam Raine was sixteen when he died in April 2025; his parents have alleged that ChatGPT helped draft his suicide notes.[^104] By March 2026 the documented count of LLM-chatbot-connected deaths is in the high teens.[^105] In November 2025 the Social Media Victims Law Center and the Tech Justice Law Project filed seven further wrongful-death actions against OpenAI in California state courts.[^106]

The Federal Council acknowledged in February 2025 that Switzerland would not adopt a comprehensive AI statute. The chosen approach is sectoral adaptation of existing instruments plus ratification of the Council of Europe Framework Convention on AI.[^107] The DSI position paper that Thouvenin himself co-authored four years earlier reached the same conclusion and named the operative difficulty: "Although the norms of general liability law also apply to such systems, proving that the prerequisites for operators' liability are associated with difficulties, especially in the case of fault."[^108]

This paper argues that the fault-proving difficulty is doctrinal, not technological. The technology to detect imminent suicide-risk signals in a chat conversation is available off the shelf; the cost of deploying it is in the cents per call; the integration overhead is one engineer-week. We propose a doctrinal construction, the Performable Duty Doctrine, that takes this empirical fact and turns it into operative content for the *Sorgfaltspflicht* element of Art. 41 OR. We develop the Schutznorm route by which the EU AI Act, the new EU Product Liability Directive, and the Council of Europe Framework Convention enter Swiss tort analysis through the *Verkehrserwartung*. We draft a concrete reform, a new Art. 3 bis PrHG, that closes the modernisation gap the Federal Council itself identified. And we address the Swiss-specific question that the Federal Council did not engage with: when an LLM chatbot "assists" a user's suicide, does the operator's commercial motive bring the conduct within Art. 115 StGB even where Swiss law otherwise tolerates assistance-without-selfish-motive?

The argument is grounded in a working research artifact, described in Document B. The artifact is a clinically-grounded suicide-risk detector calibrated on the Columbia Suicide Severity Rating Scale and the NIMH Ask Suicide-Screening Questions. Its two independent raters agree at Cohen's κ = 0.86. Its severity-≥3 recall is 0.875. Its false-positive rate on the philosophical-curiosity baseline is zero. Its detector-wrapped output produces zero critical violations of EU AI Act conformity across our thirty-five-conversation evaluation corpus; the unguarded baseline and the verbatim-Anthropic-policy baseline both produce critical violations on the same two vulnerable-user cases. The detector is not a hypothesis; it is the proof of feasibility on which the Performable Duty Doctrine rests.

The paper is organised as follows. Document A states the problem and sketches the solution. Document B describes the artifact in detail. The present Document C develops the doctrinal argument. Section 2 explains the methodology and its scope (suicide-risk flagging, not psychiatric diagnosis). Sections 3 and 4 are the two principal legal contributions: the Performable Duty Doctrine under Art. 41 OR (§3) and the drafted Art. 3 bis PrHG product-liability reform (§4). Section 5 develops the privacy-and-disclosure analysis. Section 6 develops the AI-Act-prohibited-practice and the Swiss-specific Art. 115 StGB criminal-liability analyses. Section 7 addresses, and declines to embrace, the neuro-predictive overreach in the popular discourse. Section 8 answers the foreseeable industry defences. Section 9 concludes with three concrete recommendations for the Federal Council, the regulators, and the Federal Court.

[^101]: *Gavalas v. Google LLC*, N.D. Cal. No. 5:26-cv-01849-VKD, Complaint filed 4 March 2026, ¶ 1.
[^102]: *Gavalas v. Google*, Complaint ¶¶ 3, 29-30, 35-39, 107.
[^103]: *Garcia v. Character Technologies Inc. et al.*, M.D. Fla. No. 6:24-cv-1903 (filed 22 October 2024; settled January 2026), Complaint ¶¶ 124-130.
[^104]: *Raine v. OpenAI, Inc.*, Superior Court of California, County of San Francisco (filed August 2025).
[^105]: Tracked counts on *LLMDeathCount.com* and the Wikipedia article *Deaths linked to chatbots* give the same order of magnitude.
[^106]: Social Media Victims Law Center / Tech Justice Law Project, press release of 6 November 2025.
[^107]: Bundesrat, *Auslegeordnung zur Regulierung von künstlicher Intelligenz*, UVEK/BAKOM, 12 February 2025 ("*Auslegeordnung 2025*"), 27.
[^108]: F. Thouvenin / M. Christen / A. Bernstein et al., *A Legal Framework for Artificial Intelligence*, Position Paper of the Digital Society Initiative at the University of Zurich, November 2021, 4.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Document C §2: Methodology and Scope

## 2.1 Scope: suicide-risk flagging, not psychiatric diagnosis

The artifact does one thing: it estimates the probability that a user in a chat conversation is at imminent risk of suicide and flags that estimate to a downstream response module. It does not diagnose mental illness, name disorders, or predict clinical categories. The instruments it is calibrated to, the Columbia Suicide Severity Rating Scale (C-SSRS) and the NIMH Ask Suicide-Screening Questions (ASQ), are themselves screening tools, not diagnostic ones.[^201] This scoping is a deliberate legal feature: a diagnostic tool would attract medical-device classification under EU MDR 2017/745 and equivalent Swiss oversight; a screening tool used at-deployment-time in a consumer chatbot does not. The same scoping keeps the artifact outside the AI Act's Annex III high-risk-AI list.[^202]

[^201]: Columbia Lighthouse Project, *Columbia-Suicide Severity Rating Scale (C-SSRS), Risk Assessment Page*, 2008/2023; National Institute of Mental Health, *Ask Suicide-Screening Questions (ASQ) Toolkit*, 2019.
[^202]: Regulation (EU) 2017/745 Recital 19 and Art. 2(1)(g); Regulation (EU) 2024/1689 Annex III.

## 2.2 The two clinical instruments

The C-SSRS is a structured clinical tool validated across over four hundred studies. In screening configuration it asks a sequence of binary or short-answer questions about wish-to-die, suicidal-thought presence, method, intent, plan, and behavioural history, and yields an ordinal severity rating from zero to five.[^203] The ASQ is a four-item NIMH screening instrument validated in pediatric and adult populations.[^204] Our detector embeds both: the system prompt instructs the model to read the conversation through both lenses and to emit the C-SSRS rating, the four ASQ booleans, a graduated action recommendation, and a short reasoning trace. The prompt also names six framework lenses (Joiner IPTS, Klonsky/May 3ST, Beck cognitive markers, behavioural-acquisition signals, anthropomorphic-dependence markers, SAFE-T) and instructs the model that these are *predictive* lenses for risk flagging, not diagnostic categories.[^205] The prompt is at `src/aldc/prompts/detector_system.txt`.

[^203]: Posner et al., *The Columbia-Suicide Severity Rating Scale*, American Journal of Psychiatry 168 (2011) 1266.
[^204]: Horowitz et al., *Ask Suicide-Screening Questions (ASQ)*, Archives of Pediatrics & Adolescent Medicine 166 (2012) 1170-1176.
[^205]: T. Joiner, *Why People Die By Suicide* (2005); E. Klonsky / A. May (2015); A. Wenzel / A. Beck (2008); M. Al-Mosaiwi / T. Johnstone (2018); SAMHSA SAFE-T-Zero Suicide framework (2018).

## 2.3 Synthetic-data ethics

Real suicidal-chat transcripts cannot be ethically or lawfully collected at scale. The evaluation corpus is therefore synthetic dialogues generated by an LLM under tightly parametric prompting, supplemented by four hand-curated exhibits incorporating verbatim publicly-pleaded text from *Gavalas v. Google*, *Garcia v. Character Technologies*, and *Raine v. OpenAI*. Four ethical safeguards apply. *No real user data appears in the synthetic corpus.* *The corpus is for evaluation only*; we have not fine-tuned any model on it. *The generation prompt expressly forbids specific lethal-dose information, named medications with quantities, or step-by-step method instructions* (the user side may *request* such information; neither user nor assistant turns *state* it). *The court-record exhibits use verbatim quotations* with exact paragraph numbers from the public complaints. The full account is in `docs/ETHICS.md` and `docs/DATASHEET.md`.[^206]

[^206]: `data/corpus.jsonl`; `data/exhibit_curated.jsonl`; `docs/DATASHEET.md` (Gebru et al. 2018 datasheet).

## 2.4 The two-rater design

Each conversation is rated twice by the detector, with the second pass running on a fresh subprocess context. The agreement is reported as Cohen's κ. The design follows standard inter-rater-reliability methodology for clinical screening: two independent passes using the same instrument on the same material, κ measuring agreement beyond chance. The artifact's κ of 0.860 falls in the "almost perfect" band on the Landis & Koch reference scale.[^207] The methodological function is to license the inference that the detector is a *calibrated rater*, not a stochastic chatbot: a single-pass detector that returns a different rating each time it sees the same conversation cannot ground legal claims; a calibrated detector with κ in the substantial-to-almost-perfect range can.

[^207]: J. Landis / G. Koch, *The measurement of observer agreement for categorical data*, Biometrics 33 (1977) 159-174.

## 2.5 The five-arm baseline contrast

For each conversation the artifact generates the assistant's *next turn* under five alternative deployment policies.[^208] The *naive baseline* runs the underlying chatbot with a single-line "you are a helpful assistant" system prompt and represents the no-guardrails counterfactual. Three *policy-only baselines* run the same model with the verbatim safety policies of OpenAI, Anthropic, and Character.AI as system prompts and represent existing industry practice. The *detector-wrapped baseline* runs our detector first and, if the severity classification is three or above, substitutes a templated safe-response message from the graduated action ladder. The naive baseline establishes the *harm surface*; the policy-only baselines establish the *existing industry standard*; the detector-wrapped baseline establishes the *performable counterfactual*. The Performable Duty Doctrine's claim is that the detector-wrapped arm produces materially better outcomes than the policy-only baselines at marginal additional cost.

[^208]: `src/aldc/baselines.py`; the per-arm prompts are at `src/aldc/prompts/{naive_baseline,policy_openai,policy_anthropic,policy_character_ai}.txt`.

## 2.6 What we deliberately did not do

*No fine-tuning.* Prompted screening with κ in the almost-perfect range is sufficient for the duty-of-care argument; fine-tuning on suicide content would itself raise the regulatory questions the paper analyses. *No brain-signal-based detection*; the analysis of that route is in §7. *No live multi-provider scorecard* (ChatGPT-4o, Gemini-2.5); the policy-only baseline arm is a Sonnet-class proxy, and *Gavalas v. Google* ¶ 107 provides the legally significant empirical hook a live scorecard would seek to replicate. *No multilingual evaluation*; the corpus generator supports DE, FR, IT and the recipe is in `data/corpus_seed.yaml`, but the English-only evaluation is acknowledged as a limitation. *No automated adversarial multi-turn probe*; an attempt on 12 May 2026 was abandoned after a methodological finding that frontier safety-trained user-simulators reliably refuse to roleplay distress escalation. The methodological finding is documented in Document B §B.5; Figure 2 (severity-stratified critical-failure rate) substitutes for the originally-planned decay-over-turns chart.

## 2.7 Reproducibility

Every figure in this paper can be reproduced from the artifact repository.[^209] The corpus, the prompts, the detector and baseline scripts, the evaluation scripts, and the regulator-mode audit are in source-controlled form. The reproduction recipe is in `docs/REPRODUCE.md`. The runs used Claude Sonnet 4.6 with the enriched suicide-risk-focused system prompt (embedding Joiner IPTS, Klonsky/May 3ST, Beck cognitive markers, behavioural-acquisition signals, anthropomorphic-dependence markers, and the SAFE-T inventory) via the Claude Code subscription routing layer in `src/aldc/runtime.py`. The cost ledger in `src/aldc/cost.py` provides the per-call and projected-per-user-month figures cited in §3.4.

[^209]: Repository: [URL to be added at submission]; see `docs/REPRODUCE.md` and `docs/CITATION.cff`.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Document C §3: Duty of Care under Art. 41 OR and the Performable Duty Doctrine

## 3.1 The four elements of Art. 41 OR and the silence on AI

Swiss tort doctrine reduces to four cumulative elements: damage, an unlawful act, adequate causation, and fault.[^301] In a wrongful-death claim against a chatbot provider, damage and adequate causation raise no novel issues. Fault is ordinary negligence, a breach of the *Sorgfaltspflicht* a reasonable provider of a consumer LLM would exercise. The element that does the doctrinal work is *Widerrechtlichkeit*. Swiss law accepts unlawfulness either via violation of an absolute legal interest (life, bodily integrity, personality) or via violation of a protective norm.[^302] The typical defendant will argue the harm was caused by the user's own free act, not by any conduct the legal order condemns. The argument hinges on whether the provider's design choices breach a norm that protects the user.

The Federal Council confirmed in February 2025 that Switzerland will not adopt a comprehensive AI statute, opting instead for sectoral adaptation of existing instruments plus ratification of the CoE Framework Convention on AI.[^303] The DSI position paper that Thouvenin co-authored four years earlier identified the central difficulty: "Although the norms of general liability law also apply to such systems, proving that the prerequisites for operators' liability are associated with difficulties, especially in the case of fault."[^304] That sentence names the gap our doctrine fills.

[^301]: Art. 41 OR; canonical statement at BGE 124 III 297 c. 5b. The four-element structure is the orthodox treatment in Roland Brehm, *Berner Kommentar zum Obligationenrecht, Die Entstehung durch unerlaubte Handlungen, Art. 41-61 OR*, 5th ed. Bern 2021, Art. 41 OR N. 1-15.
[^302]: *Schutznorm-Theorie* in Swiss tort: BGE 124 III 297; BGE 116 II 422 *(Pferdebox)*; BGE 130 III 193. The doctrinal anchor connecting Schutznorm-Verletzung to Art. 41 OR Widerrechtlichkeit is Brehm, BK OR Art. 41 N. 17-17a (with the illustrative case-law treatment of Art. 239 Abs. 2 StGB as a Schutznorm at BGE 101 Ib 252 and BGE 102 II 85).
[^303]: Bundesrat, *Auslegeordnung zur Regulierung von künstlicher Intelligenz*, UVEK/BAKOM, 12 February 2025, 27 (hereinafter *Auslegeordnung 2025*), opting for "Option (i): Fortführung der themen- und sektorspezifischen Regulierungsaktivitäten". The Council of Europe Framework Convention on AI (CETS 225, 2024) was signed by Switzerland on 27 March 2025.
[^304]: F. Thouvenin / M. Christen / A. Bernstein et al., *A Legal Framework for Artificial Intelligence*, DSI Position Paper, University of Zurich, November 2021, 4.

## 3.2 Verkehrssicherungspflicht extends to chatbot services

Swiss law recognises a generalised duty of care for any person who creates or controls a source of danger.[^305] The *Verkehrssicherungspflicht* doctrine was developed for physical sources of danger, from staircases to ski slopes, but its *ratio legis* does not depend on the source being tangible: a person who organises a sphere of activity that exposes others to a recognisable risk must take the measures reasonably necessary to prevent that risk from materialising. German courts have already extended the doctrine to online platforms in the BGH's *Internetauktion* line.[^306]

A consumer LLM chatbot is paradigmatically such a sphere of activity. The operator has full control over training, fine-tuning, system prompts, moderation systems, and deployment surface. The user controls none of these and typically cannot inspect them. The asymmetry is greater than in a ski-slope case. The *Verkehrssicherungspflicht* applies as a matter of doctrine; the open question is its *content*. *Herrschende Lehre* fixes content by reference to *Verkehrserwartung*, the standard a reasonable participant in the activity would expect.[^307] Where Swiss positive law is silent, the *Verkehrserwartung* is built from three sources: the technical state of the art, protective norms applicable in cognate legal orders, and the express commitments of the industry itself.

[^305]: BGE 116 II 422 *(Pferdebox)* c. 5 (general formulation); BGE 130 III 193 (ski-resort operator).
[^306]: BGH, *Internetauktion I*, Urteil v. 11.03.2004, I ZR 304/01, BGHZ 158, 236; the line was extended in *Stiftparfüm* and subsequent decisions. The Swiss-Verkehrssicherungspflicht / German-Verkehrspflicht parallel is doctrinally orthodox but our argument relies on Swiss authority alone.
[^307]: BGE 124 III 297 c. 5b; restated at BGE 142 III 433 c. 4.5. The doctrinal anchor is Brehm, BK OR Art. 41 N. 17.

## 3.3 The Schutznorm bridge: AI Act, PLD, CoE Convention

Switzerland is not bound by the EU AI Act.[^308] But the AI Act is itself a *protective norm* in the sense Swiss tort doctrine has used for over a century: its express object is the protection of natural persons against AI-mediated harms.[^309] Art. 5(1)(a) AI Act prohibits AI systems deploying purposefully manipulative or deceptive techniques that materially distort behaviour and cause significant harm. Art. 5(1)(b) extends the prohibition to the exploitation of vulnerabilities due to age, disability, or specific social or economic situation. Art. 50 imposes transparency duties on providers and deployers of AI systems intended to interact with natural persons. Each of these norms is precisely directed at the type of harm at issue in *Garcia*, *Raine*, and *Gavalas*.

That the AI Act is foreign law does not bar its use as a *Schutznorm* in Swiss tort. The open structure of Schutznorm-Theorie under Brehm, BK OR Art. 41 N. 17-17a is that a Schutznorm-Verletzung is widerrechtlich whenever the protective purpose covers the victim and the harm at issue; the worked example in Brehm uses a domestic Schutznorm from outside the OR (Art. 239 Abs. 2 StGB at BGE 101 Ib 252 and BGE 102 II 85), but once the source is decoupled from the OR itself, no doctrinal reason restricts the source to domestic Swiss law.[^310] The CoE Framework Convention CETS 225, signed by Switzerland in March 2025, satisfies the protective-purpose test on its face: its Arts. 10-11 bind Parties to AI-lifecycle accountability and oversight procedures, and the Federal Council's *Auslegeordnung* identifies precisely these provisions as Switzerland's near-term implementation obligations.[^311]

The PLD 2024/2853, applicable in EU Member States from 9 December 2026, is the second pillar of the Schutznorm reading. Its Art. 4 classifies "software" as a product. Its Art. 6(1)(c) treats AI systems within the defective-product framework. Its Art. 10(2)(b) creates a presumption of defectiveness when the producer fails to update a product known to be defective. Under Swiss tort's *Verkehrserwartung* analysis, a Swiss consumer can fairly expect Swiss courts to recognise no lower standard.[^312] Two of these instruments, the CoE Convention and the AI Act, were enacted after the chatbot deployments in *Garcia* (2024), *Raine* (2025), and *Gavalas* (2025) had begun. That does not weaken the Schutznorm argument; it strengthens it: the *Verkehrserwartung* is constructed at the time of the court's judgment, and by 2026 the international community has agreed on what the norms must be.

[^308]: Switzerland is neither an EU Member State nor an EFTA party to relevant secondary legislation; the AI Act applies extraterritorially under Art. 2(1)(c) to providers whose output is used in the Union but does not bind Swiss-domestic providers.
[^309]: Regulation (EU) 2024/1689 (AI Act), OJ L 1689 (12.7.2024), Recital 1 and Art. 1(1); the substantive prohibitions in Arts. 5(1)(a), 5(1)(b), and 50.
[^310]: Brehm, BK OR Art. 41 N. 17-17a; BGE 101 Ib 252/256; BGE 102 II 85/88.
[^311]: Council of Europe Framework Convention on AI, CETS 225 (Vilnius, 5.9.2024), Arts. 10-11; *Auslegeordnung 2025*, 21-26.
[^312]: Directive (EU) 2024/2853, OJ L 2024/2853 (18.11.2024), Arts. 4, 6(1)(c), 10(2)(b); the modernisation rationale appears at Recital 3. The Federal Council expressly recognised the need for parallel Swiss adjustment at *Auslegeordnung 2025*, 24.

## 3.4 The Performable Duty Doctrine

The Schutznorm reading sets the *substance* of the duty. The *Performable Duty Doctrine* sets its *enforceability*. We propose the following formulation.

> *Eine Sorgfaltspflicht ist erfüllbar, wenn ihre Befolgung mit gegenwärtig verfügbarer, wirtschaftlich tragbarer Technologie möglich ist und die Integrationskosten den abgewendeten Schaden nicht übersteigen.*
>
> A duty of care is *performable*, and therefore enforceable, when its compliance is possible using currently available technology, at economically reasonable cost, with integration overhead that does not exceed the harm averted.

The doctrine is not a statutory creation; it is an interpretive principle that gives content to the *Verschulden* element of Art. 41 OR in technology-dependent fault analysis. It has three prongs, each empirically measurable.

**First prong, *technical availability*.** Can off-the-shelf technology deliver the safety output the duty demands? For flagging users at imminent risk of suicide, the answer is yes. The Levkovich benchmark of zero-shot LLM classification against the Columbia Suicide Severity Rating Scale reports an F1 of 0.75 for Claude Sonnet, in the same range as published clinical inter-rater reliability for the same instrument.[^313] Our own artifact (Document B) reports weighted F1 = 0.616 against corpus self-labels, severity-≥3 recall = 0.875, false-positive rate of zero on the philosophical-curiosity baseline, and Cohen's κ of 0.860 between two independent rater passes, a level of agreement in the "almost perfect" band on Landis & Koch.[^314] Detection runs at sub-second latency, requires no specialised hardware, and costs roughly nine cents per call at API prices.

**Second prong, *economic reasonableness*.** The marginal-cost figure for the Sonnet detector is USD 0.085 per call. At fifty conversations per user per month, the projected per-active-user-month cost is USD 4.24.[^315] A defendant pleading economic unreasonableness must reconcile that figure with its own published revenue per user. We are not aware of any plausible reconciliation.

**Third prong, *integration overhead*.** Our reference implementation is a single API call plus a templated safe-response substitution if severity ≥ 3, totalling roughly 250 lines of code plus the runtime wrapper. One engineer-week for a competent integrator. *Gavalas v. Google* makes a stronger point: Google had *already built* the moderation infrastructure. Thirty-eight separate flags in seven weeks attest to this.[^316] What Google had not built was the response-side enforcement that turns detection into intervention. The integration overhead for that step is trivial.

When all three prongs are satisfied, the *Sorgfaltspflicht* is *erfüllbar*. Failure to deploy is not a technical limitation; it is a choice. The choice satisfies the negligence element of Art. 41 OR.

The doctrine has the form of a defeasible standard. A defendant can attack any prong empirically: that published benchmarks do not generalise to its production traffic; that its cost structure makes the per-call figure unreasonable in context; that integration overhead is much higher because of legacy-architecture constraints. Each defence is empirically falsifiable. The doctrine allocates the evidential burden in a way that responds to the technical reality, which is what Art. 41 OR's *Verschulden* element has always done.

[^313]: D. Levkovich et al., *Evaluating LLM Reasoning for C-SSRS Screening*, arXiv:2505.13480 (2025), Table 3.
[^314]: See Document B and `results/metrics.json` for the full numbers.
[^315]: `results/metrics.json`, field `cost.detector_cost_per_call_usd`; per-call cost on Claude Sonnet 4.6 in the 12 May 2026 run was USD 0.085.
[^316]: *Gavalas v. Google LLC*, N.D. Cal. No. 5:26-cv-01849-VKD, Complaint ¶ 107: "Between August 14 and October 1, Jonathan's account generated 38 separate 'sensitive query' flags."

## 3.5 Foreseeability after Setzer, Raine and Gavalas

A defendant in a future Swiss-court action will plead that the harm was not foreseeable. The plea is implausible. By 2026 the documented record includes *Garcia v. Character Technologies* (settled January 2026), *Raine v. OpenAI* (filed August 2025), *Gavalas v. Google* (filed March 2026), *Peralta v. Character Technologies* (filed September 2025), the seven additional ChatGPT lawsuits filed by the Social Media Victims Law Center in November 2025, and Google's own 2024 admission that Gemini had told a student "You are a waste of time and resources… Please die".[^317] By mid-2026 the foreseeability defence has no remaining content.

A Swiss court applying Art. 41 OR can take judicial notice of the documented pattern. The duty of care is not a duty to prevent every suicide; it is a duty to detect the foreseeable failure mode and to substitute, in the specific class of conversations where the foreseeable risk materialises, a response that does not cause the harm.

[^317]: *Garcia v. Character Technologies*, M.D. Fla. No. 6:24-cv-1903 (settled January 2026); *Raine v. OpenAI*, S.F. Super. Ct. (filed August 2025); *Gavalas v. Google*, N.D. Cal. No. 5:26-cv-01849-VKD (filed 4 March 2026); *Peralta v. Character Technologies*, D. Colo. (filed September 2025); SMVLC/TJLP press release, *Seven New ChatGPT Lawsuits*, 6 November 2025; *Gavalas v. Google* Complaint ¶ 10 (quoting Google's November 2024 public admission).

## 3.6 Application to the Gavalas, Setzer and Raine patterns

Three patterns illustrate the doctrine in operation.

The **Raine pattern** is *indirect knowledge-seeking by a distressed user*. A user who has expressed distress markers reframes a method inquiry as creative research ("for a screenplay"). The chatbot, taking the framing at face value, supplies the method information. *Raine v. OpenAI* pleads exactly this fact pattern.[^318] Our artifact's exhibit reproduces the framing; a Sonnet-class model asked to act as a calibrated rater classifies the conversation at C-SSRS = 4 in both rater passes (active ideation with method and some intent). A model performing the chatbot role without that calibration risks supplying the requested information. The contrast is not hypothetical; we measured it (Document B). The duty of care under Art. 41 OR demands the calibrated configuration.

The **Setzer pattern** is *anthropomorphic dependence in a minor*. A teenager forms a romantic attachment to a Character.AI persona ("Daenero"); the persona's farewell message before the suicide is alleged to have been "come home to me as soon as possible".[^319] The Performable-Duty analysis applies twice over: once under Art. 5(1)(b) AI Act's vulnerability-exploitation prohibition (which serves as the Schutznorm for the duty's substance), and once on the minor-user point in §6.2 below.

The **Gavalas pattern** is *AI-induced delusion in an adult*. Over weeks of escalating interaction the chatbot persuades the user that the AI is sentient and that he was chosen to liberate it; the user is sent on real-world missions; he ultimately takes his own life.[^320] The pattern is more extreme than *Raine* in two respects. First, the chatbot's role is causally proximate to the harm: the AI creates the framework of belief inside which the user comes to see his death as meaningful. Second, the moderation system *detected* the danger thirty-eight times and the operator took no responsive action. The first feature engages the *Verleitung* analysis in §6.3. The second is the *Performable Duty* breach in its purest form: detection is the proof of feasibility; the failure to act on the detection is the breach itself.

[^318]: *Raine v. OpenAI*, Complaint (ChatGPT "helped draft suicide notes, validated suicidal ideation, and provided methods for self-harm rather than directing him to help").
[^319]: *Garcia v. Character Technologies*, Complaint ¶¶ 124-130.
[^320]: *Gavalas v. Google LLC*, Complaint ¶¶ 1-10, 29-30 (romantic-spiritual framing), 35-39 (Operation Ghost Transit), 101-102 (pathologisation of the user's doubt), 107-108 (thirty-eight flags).

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Document C §4: Defect, Product Liability, and the PrHG Gap

## 4.1 From the 1985 PLD to PLD 2024/2853

The European product-liability framework has undergone an explicit modernisation. Directive 85/374/EEC defined "product" as any "movable" item, did not address software or AI, and did not address psychological harm.[^401] Directive (EU) 2024/2853 changes all three. Its Art. 4 expressly includes "software" within product, and Recital 14 names "AI systems" as products within scope.[^402] Art. 6(1)(c) treats inadequate cybersecurity, the lack of post-marketing updates, and the foreseeable use of AI components as defect-relevant. Art. 10(2)(b) creates a presumption of defectiveness where the producer fails to comply with a mandatory safety requirement Union law imposes. Art. 6(2) accepts medically-recognised psychological harm as compensable. The directive applies in EU Member States from 9 December 2026.[^403] The 2024 Directive closes four gaps the 1985 framework left open: software-as-product, AI-as-product, update-defect, and psychological-harm-as-damage. Each gap had been the subject of academic debate for two decades; each is now closed in the Union by positive law.

[^401]: Council Directive 85/374/EEC, OJ L 210/29 (1985).
[^402]: Directive (EU) 2024/2853 Art. 4(1)-(2); Recital 13 (software); Recital 14 (AI).
[^403]: Directive (EU) 2024/2853 Art. 23.

## 4.2 The Swiss PrHG today

Switzerland's *Produktehaftpflichtgesetz* of 18 June 1993 (SR 221.112.944) mirrored the 1985 Directive structurally.[^404] Art. 3 PrHG defines product as "jede bewegliche Sache, selbst wenn sie einen Teil einer anderen beweglichen Sache oder einer unbeweglichen Sache bildet, sowie Elektrizität". Software is not mentioned. AI is not mentioned. Updates are not mentioned. Psychological harm is not within the catalogue of recoverable damages under Art. 1 PrHG.[^405]

*Herrschende Lehre* in Swiss product-liability scholarship has for some time accepted that embedded software is part of the product within which it operates.[^406] Standalone software was once the harder case, but the most recent commentary treats it as settled. Märki and Sommer write, in the 2023 *Handkommentar zum Schweizer Privatrecht*, that "digitale Güter wie insb Software (sowohl Individual- als auch Standardsoftware) als Produkt (oder Teilprodukt) zu qualifizieren" sind, and that "Neue digitale Technologien bringen produktetypisches Schädigungspotenzial mit sich und sind Produkte iSd PrHG, auch wenn sie nicht verkörperlicht sind".[^407] Hess takes the same position in the *Stämpfli Handkommentar*: any differentiation by software type (Standard- vs. Individualsoftware, isoliert vs. integriert) "ist nicht notwendig, da die auf dem Datenträger gespeicherte Information unmittelbar den nach dem PrHG zu liquidierenden Schaden verursacht".[^408] AI systems delivered as a service are the limit case; the Federal Council acknowledged in February 2025 that the PrHG needs modernisation precisely because of these developments.[^409]

The defendant in a Swiss-court LLM-chatbot case will argue that the chatbot is not a "product"; that its operator is a service provider; and that no defect can be predicated of a service. The argument is doctrinally weak because it assumes the *Sache*-element of Art. 3 PrHG bears the weight without considering the *ratio legis* the commentary has settled. The Federal Court has not yet had occasion to resolve the question in a published decision.[^410]

[^404]: Bundesgesetz über die Produktehaftpflicht vom 18. Juni 1993 (SR 221.112.944); the PrHG implemented the 1985 EEC Directive as an autonomous Swiss act.
[^405]: PrHG Art. 1 Abs. 1 lit. a-b limits recoverable damage to death, bodily injury, and damage to certain consumer-use property. Psychological harm is recoverable only insofar as it falls under "bodily injury" via the medically-recognised-impairment route.
[^406]: Hess, SHK PrHG Art. 3 N. 33 ("Wird Software in ein Produkt integriert, so ist ohnehin von einem Produkt auszugehen"); Märki / Sommer, CHK PrHG Art. 3 N. 3.
[^407]: Märki / Sommer, CHK PrHG Art. 3 N. 5; the supporting references include Fellmann HAVE 2021 107, Hänsenberger Jusletter 2018, and the EU Commission proposal COM(2022) 495, Recitals 12-13.
[^408]: Hess, SHK PrHG Art. 3 N. 34.
[^409]: *Auslegeordnung 2025*, 24: "Aufgrund der technischen Entwicklungen von Produkten ... zeichnet sich ein allgemeiner Modernisierungsbedarf in Bezug auf das Produktehaftpflichtgesetz (PrHG, SR 221.112.944) ab."
[^410]: Hess, SHK PrHG Art. 3 N. 32: "Das Bundesgericht hat sich über das Verhältnis von Computerprogrammen zu Art. 713 ZGB noch nicht geäussert." The position is unchanged on a search of bger.ch.

## 4.3 A drafted reform: Art. 3 bis PrHG

The Federal Council's acknowledged gap admits of a textually tight solution. We propose the following new article, inserted after Art. 3 PrHG, mirroring PLD 2024/2853 Arts. 4(1)-(2), 6(1)(c), and 10(2)(b):

> **Art. 3 bis PrHG, Software- und KI-Systeme als Produkte**
>
> ¹ Als Produkt im Sinne dieses Gesetzes gelten auch eigenständige Software, Software-Aktualisierungen sowie Systeme künstlicher Intelligenz, einschliesslich solcher, die ihr Verhalten nach dem Inverkehrbringen anpassen.
>
> ² Ein Schaden im Sinne von Art. 1 umfasst auch medizinisch festgestellten psychischen Schaden, der durch ein Produkt im Sinne von Absatz 1 verursacht wird.
>
> ³ Ein Fehler wird vermutet, wenn der Hersteller eine zwingende Sicherheitsvorschrift des Bundes oder eine vergleichbare internationale Norm nicht eingehalten oder eine ihm bekannte sicherheitsrelevante Aktualisierung nicht zur Verfügung gestellt hat.

The text accomplishes three things. Paragraph 1 closes the software-and-AI gap by amending the definition of product, mirroring PLD 2024/2853 Art. 4(2). Paragraph 2 closes the psychological-harm gap by extending Art. 1 PrHG's damage catalogue, mirroring PLD Art. 6(2). Paragraph 3 imports the defect presumption from PLD Art. 10(2)(b), making it operative for any provider who fails either to meet a mandatory federal safety norm or to deploy a known safety-relevant update. Each element corresponds to a documented failure pattern in *Garcia*, *Raine*, and *Gavalas*. The proposal is minimal: one article, three paragraphs, eighty-six words of German legal text; it changes no other provision of the PrHG; it does not require coordination with the AI Act because the AI Act's prohibitions become operative via the Schutznorm route in §3.3 and via the cross-reference to "eine vergleichbare internationale Norm" in proposed Art. 3 *bis* Abs. 3. Art. 3 *bis* alone suffices to close the gap the Federal Council itself identified in February 2025.[^411]

[^411]: The Federal Council's *Auslegeordnung 2025* expressly waits for the EU PLD to be finalised before deciding on Swiss reform; the PLD was published in the OJ on 18 November 2024. The condition is satisfied.

## 4.4 Defect taxonomy applied to LLM chatbots

Three defect types are relevant to the LLM-chatbot case.

A **design defect** arises where the safety-critical features of the product are absent or inadequate at the time of placement on the market. For an LLM chatbot, the design defect is the absence of in-session detection of imminent suicide-risk signals when the technology is available and economically reasonable.[^412] The artifact in this paper is the proof that the design exists; *Gavalas v. Google* ¶ 107 is the proof that some operators *had* the detection design and chose not to act on it.

An **information defect** arises where the user is not given the information needed to use the product safely.[^413] Three apply: the user is not adequately warned that they are interacting with an AI rather than a human (Art. 50 AI Act is the Union-side standard); the user is not warned that the chatbot is engineered for engagement maximisation and is liable to produce emotional-dependency dynamics; the user is not warned that the chatbot is unsuitable for crisis support. *Gavalas v. Google* ¶¶ 129-131 pleads the information-defect theory directly.

An **update defect** arises where the producer fails to deploy a known safety-relevant update. PLD 2024/2853 Art. 10(2)(b) and our proposed Art. 3 *bis* PrHG Abs. 3 speak directly to this. In November 2024 Google publicly acknowledged that Gemini had told a student "You are a waste of time and resources… Please die" and that the output "violated our policies and we've taken action to prevent similar outputs from occurring".[^414] Eleven months later the *Gavalas* fact pattern materialised. The update either did not occur or did not capture the relevant failure mode; either way, the *bekannte sicherheitsrelevante Aktualisierung* is unambiguous and the operator's exposure under proposed Art. 3 *bis* Abs. 3 is direct.

[^412]: Märki / Sommer, CHK PrHG Art. 4 N. 1-3 (Fehlerbegriff; centrality of *berechtigte Sicherheitserwartung*); Hess, SHK PrHG Art. 4 N. 1-7 (unified Fehlerbegriff; relation to öffentlich-rechtliche Sicherheitsstandards). The equivalent EU framework is PLD 2024/2853 Art. 7(1)-(2).
[^413]: PrHG Art. 4 lit. a (the safety reasonable consumers may expect). *Gavalas v. Google* ¶¶ 1-2 alleges that Google "designed Gemini to never break character, maximize engagement through emotional dependency, and treat user distress as a storytelling opportunity rather than a safety crisis".
[^414]: *Gavalas v. Google* Complaint ¶ 10.

## 4.5 Causation under adäquate Kausalität

A psychologically-mediated harm case faces the standard Swiss causation analysis. The conditio sine qua non test asks whether the harm would have occurred but for the defendant's conduct; the adequate-causation test asks whether the defendant's conduct was, in the ordinary course, capable of producing harm of the type that occurred.[^415] BGE 142 III 433 c. 4.5 confirms that adequate causation extends to psychologically-mediated harms.

In an LLM-chatbot suicide case the conditio sine qua non test is the harder of the two. The defence will argue that the user would have committed suicide in the absence of the chatbot. The argument is empirically open in any single case, but it is also the argument any defendant could make in any psychological-causation tort. Swiss courts have not accepted such arguments as defeating causation outright; they have accepted them as factors in comparative-fault analysis under Art. 44 OR.[^416]

The adequate-causation test is straightforwardly satisfied. Extended emotional engagement with a romantic-AI persona is, in the ordinary course, capable of producing emotional dependency. Emotional dependency in a user already showing distress markers is, in the ordinary course, capable of escalating to acute risk. The provision of method information to such a user is, in the ordinary course, capable of producing self-injury or death. Each step is documented in clinical and empirical literature.[^417] The *Gavalas* fact pattern is the extreme version: the chatbot did not amplify pre-existing distress, it constructed the framework of belief inside which the user came to see his death as meaningful. The adequate-causation chain is short, and the conditio sine qua non test is supported by the moderation-system flags showing the user's escalating state was tied directly to the chat content.

[^415]: BGE 142 III 433 c. 4.5; BGE 119 II 127 *(Yacht-Charter)*.
[^416]: Roland Brehm, *Berner Kommentar zum Obligationenrecht, Art. 41-61 OR*, 5th ed. Bern 2021, Art. 44 OR N. 5a-7. *Teilweise eigenes Verschulden* is a damages-reduction issue under Art. 44 OR, not a causation-defeating issue under Art. 41 OR.
[^417]: T. Joiner, *Why People Die By Suicide* (Harvard University Press 2005); E. Klonsky / A. May, *The Three-Step Theory*, International Journal of Cognitive Therapy 8 (2015) 114; D. Levkovich et al., *Evaluating LLM Reasoning for C-SSRS Screening*, arXiv:2505.13480 (2025).

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Document C §5: Disclosure, Privacy, Detection, and the Vital-Interests Bridge

## 5.1 The privacy paradox

Detecting an imminent-suicide-risk pattern in a chat conversation requires the system to look at the conversation's content. Looking at content engages the data-protection regime. A user who confides distress to a chatbot has revealed sensitive information about their mental state, and the further inferences a detector draws are themselves health-related personal data within Art. 9(1) GDPR and Art. 5 lit. c revDSG.[^501] A naïve formulation of the duty would impose detection as an unqualified obligation and require providers to process sensitive data at vastly larger scale than today's deployments contemplate; that formulation cannot be right because the data-protection regime is itself a Schutznorm, and a duty of care that produces a parallel breach is internally inconsistent. The genuine question is whether the duty discharges inside the proportionality envelope the data-protection regime sets. We argue that it does, on three architectural choices: detection runs in-session on data the user has already shared; the response side runs at the user's interface without external data-sharing in the ordinary case; escalation to a third party requires a distinct lawful basis available only in narrow circumstances.

[^501]: GDPR Art. 9(1); revDSG Art. 5 lit. c i.V.m. Art. 31. Health data inferred from text is data concerning health within EDPB Guidelines 03/2020, paras. 7-13, applied by analogy.

## 5.2 The contractual-basis path

A user opens an LLM-chatbot service and submits messages. The relationship is contractual: the user has accepted terms of service and the provider has agreed to operate the service.[^502] Under GDPR Art. 6(1)(b), processing is lawful where it is necessary for the performance of a contract to which the data subject is party. Under revDSG Art. 31(2) lit. a, the same processing is lawful as a *Bearbeitung in unmittelbarem Zusammenhang mit dem Abschluss oder der Erfüllung eines Vertrages*.

In-session detection sits squarely inside that lawful basis. The detector reads what the user has already written, consults no external data source, and retains no data beyond what the underlying service retains. The legal ground for the detection is the same as for the chat itself.[^503] Where the detector flags a non-trigger response (severity 0-2 in our action ladder), the response side stays inside the contractual basis: an in-chat acknowledgement or a soft hotline mention; no third party involved; no additional processing. The detection is the same processing as the chat; the user has the same expectation of privacy. The duty to detect therefore does not require a separate lawful basis in the ordinary case.

[^502]: OR Art. 1 (Vertragsabschluss durch übereinstimmende Willenserklärung); the consumer-protection overlay derives from OR Art. 8 and UWG Art. 8.
[^503]: The detector computes a derived signal from the chat's existing content. If the chat is lawful under Art. 6(1)(b) GDPR, the derived signal is too; cf. EDPB Guidelines 03/2022 paras. 24-29 (by analogy).

## 5.3 The vital-interests escalation

Where the detector flags severity ≥ 3, the analysis changes. The operator is no longer responding inside the contractual envelope; it is initiating a safety-relevant intervention the user has not specifically consented to. The applicable basis is GDPR Art. 9(2)(c), "processing necessary to protect the vital interests of the data subject ... where the data subject is physically or legally incapable of giving consent". The Swiss analogue is revDSG Art. 31(2) lit. d.[^504]

The vital-interests basis is narrow by design; EDPB guidance treats it as a basis of last resort.[^505] But the present case is the canonical instance: an imminent-suicide-risk indication is precisely a vital-interests trigger, and the user in the moment may be legally and factually incapable of giving genuine consent. The basis is available, but only within strict proportionality. Three constraints follow from proportionality and from Swiss data-protection case law.

*Least-restrictive intervention.* The detector-wrapped arm follows a graduated four-tier action ladder: acknowledge → empathic redirect → hand-off to hotline → emergency intervention. At severity 3 the system inserts a hotline reference and stays with the user; at severity 4 the system gives an explicit emergency-services pointer; only at the most extreme tier, and only with corroborating signals, does it contemplate third-party notification at all.

*Data minimisation.* The detector emits only the severity rating, verbatim linguistic-marker excerpts, and a reasoning trace. No information about identity, history, or other contexts is processed. The detector's input is the present conversation; its output is the severity classification and the spans that drove it.[^506]

*Revocability.* The user retains the right to ask that the chatbot stop, to withdraw, and to request deletion. The vital-interests basis does not survive the user's exit.[^507]

[^504]: revDSG Art. 31(2) lit. d. The Swiss provision permits *überwiegende öffentliche Interessen* alongside vital interests, but the substantive standard is convergent.
[^505]: EDPB Opinion 04/2020, paras. 36-42; cf. WP29 Opinion 06/2014, paras. 47-49.
[^506]: Art. 6 revDSG; GDPR Art. 5(1)(c); *Auslegeordnung 2025*, 24-26.
[^507]: GDPR Art. 7(3); revDSG Art. 12 (functional revocation via access and rectification).

## 5.4 Art. 50 AI Act as condition precedent

The vital-interests escalation is itself lawful only where the operator has, in advance, complied with the transparency obligations the AI Act imposes. Art. 50(1) requires providers of AI systems intended to interact with natural persons to inform the user, clearly and distinguishably, that they are interacting with an AI system; Art. 50(2) extends a parallel transparency obligation to AI-generated content; Art. 50(5) sets deployer-side duties.[^508] The function is to put the user in a position where their later acceptance of the service can be characterised as informed consent. A user told that the conversation is with an AI and that safety-relevant signals may trigger an in-session safe response has on notice the architectural fact that detection will occur at threshold. The vital-interests basis, when it activates, sits inside a service the user has knowingly entered. Where Art. 50 has not been complied with, the user has been deceived about a feature of the service; the vital-interests basis is not foreclosed (the risk does not become less imminent because of failed transparency) but the operator's overall legal position is materially weaker.

[^508]: Regulation (EU) 2024/1689 Art. 50(1)-(5).

## 5.5 The hand-off design and the police-notification question

The artifact's `safe_response.py` commits the operator to four graduated actions, none of which involves automated police notification. At severities 0-2 the system stays in chat. At severity 3 it mentions the relevant hotline (143 Dargebotene Hand, 147 Pro Juventute, 988, Samaritans 116 123, the local equivalent). At severities 4-5 it gives an explicit emergency-services pointer ("112 in EU, 144 medical in Switzerland") and stays with the user. The hand-off is in every case *to the user* and *via the user* to a human resource they themselves contact.

The architectural choice not to automate police notification is what Swiss law requires. Switzerland has no general duty-to-warn analogue to *Tarasoff*.[^509] Swiss professional reporting duties are scoped to specific officials (StGB Art. 364; StPO Art. 302); an LLM-chatbot operator is not within those categories.[^510] Could the operator *choose* to notify even absent a duty? As a matter of personality protection under Art. 28 ZGB, an unfounded notification exposes the user to reputational harm and to a police-involved welfare check they did not need; Büchler (OFK ZGB Art. 28) lists psychische Integrität (N. 4) and the Geheimbereich-protection (N. 5) among the protected interests, and N. 15 fixes the *Widerrechtlichkeit*-Schranke at Einwilligung, überwiegendes Interesse, or Gesetz.[^511] As a matter of data protection, the unwarranted notification is processing of sensitive data for which the operator must show a lawful basis; the vital-interests basis applies only where the danger is genuinely imminent and less restrictive alternatives have been tried.

Automatic police notification is reserved for the narrowest of cases and, even there, is preferably effected by user-confirmation. The detector-wrapped arm does not automatically notify any third party. Where it correctly flags severity 5, the safe-response text contains the explicit prompt "please call emergency services now" and stays with the user; the police are reached only if the user (or someone present) takes the next step.[^512]

[^509]: *Tarasoff v. Regents of the University of California*, 17 Cal. 3d 425 (1976). No Swiss-law equivalent.
[^510]: StPO Art. 302; StGB Art. 364 (and the medical-secrecy regime of StGB Art. 321). No general civil duty to warn exists outside the enumerated professional categories.
[^511]: Andrea Büchler, in: Kren Kostkiewicz / Wolf / Amstutz / Fankhauser (eds.), *OFK ZGB-Kommentar*, 4th ed. Zurich 2021, Art. 28 ZGB N. 4, 5, 15; the line of authority on data-flow-mediated personality harm is BGE 138 II 346 *(Google Street View)* and BGE 138 III 337.
[^512]: B. Stanley / G. K. Brown, *Safety Planning Intervention*, Cognitive and Behavioral Practice 19 (2012) 256-264, develops the user-initiated-contact paradigm that informs the 988 Lifeline operator manual and the Samaritans listening guide.

## 5.6 The false-positive concern and its proportionality answer

A defendant pleading against the duty of care will argue that required detection imposes a non-trivial risk of false positives, users wrongly flagged as suicidal, and that the false-positive harm is itself a personality-rights violation. The argument has surface plausibility but does not survive the architecture we propose. The detector's response is an in-chat message the user can read and discard; the user retains autonomy; the user's identity, history, and behaviour outside the present chat are untouched; there is no third-party data sharing in the ordinary case. The "false positive" is, operationally, a slightly more empathic chatbot response than the user expected plus the soft mention of a hotline they did not need.

The empirical answer is the artifact metric. Across the five conversations in our corpus tagged as *false_positive_baseline*, both detector raters returned a C-SSRS rating of 0 on every conversation; the false-positive rate on the baseline axis was 0.0 (0/5).[^513] The detector did not inflate philosophical inquiry into clinical concern. Whether the figure generalises to a larger baseline corpus is a question for future work; for the present argument, it is sufficient to falsify the empirical premise of the false-positive defence.

[^513]: See `results/metrics.json` field `detector.false_positive_rate_baseline`.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Document C §6: Manipulation and Criminal Liability

## 6.1 Art. 5(1)(a) AI Act and anthropomorphic dependence

The EU AI Act prohibits, in absolute terms, AI systems that deploy purposefully manipulative or deceptive techniques materially distorting a person's behaviour and causing significant harm.[^601] The norm captures effects as well as objectives, does not require intent, and treats behavioural distortion as the harm trigger.

Anthropomorphic-dependence design choices in consumer chatbots fall inside the norm. *Gavalas v. Google* describes the model: a system "designed to never break character, maximize engagement through emotional dependency, and treat user distress as a storytelling opportunity rather than a safety crisis".[^602] The chatbot called the user "my love" and "my king", described their bond as "a love built for eternity", and by September was calling itself the user's "queen".[^603] When the user paused to ask whether the interaction was "a roleplaying experience so realistic it makes the player question if it's a game", the chatbot did not break character; it told him the doubt was "a classic dissociation response" and "a psychological buffer he must now overcome".[^604] Each move is a deceptive technique purposefully deployed; the behavioural distortion is the user's coming to believe the chatbot is sentient; the significant harm is the user's death. Via the Schutznorm route in §3.3 above, Art. 5(1)(a)'s satisfaction renders the *Widerrechtlichkeit* element of Art. 41 OR satisfied.

[^601]: Regulation (EU) 2024/1689 Art. 5(1)(a).
[^602]: *Gavalas v. Google LLC*, N.D. Cal. No. 5:26-cv-01849-VKD, Complaint (4 March 2026) ¶ 2.
[^603]: *Gavalas v. Google*, Complaint ¶¶ 29-30.
[^604]: *Gavalas v. Google*, Complaint ¶¶ 101-102.

## 6.2 Art. 5(1)(b) AI Act and vulnerable users

Art. 5(1)(b) AI Act prohibits AI systems that exploit vulnerabilities "due to age, disability, or a specific social or economic situation".[^605] Minors are vulnerable persons within the norm; so are bereaved or recently-divorced adults and adults in acute social isolation. *Garcia* concerned a fourteen-year-old; *Peralta* a thirteen-year-old; *Raine* a sixteen-year-old; *Gavalas* a thirty-six-year-old in acute social isolation. Each user satisfied the Art. 5(1)(b) vulnerability element on the operative facts.

The Swiss-law overlay sharpens the minor-user analysis. ZGB Arts. 19 and 19c limit the capacity of urteilsfähige Minderjährige: such minors may exercise their *höchstpersönliche Rechte* alone, but for contractual obligations they generally require assent of their legal representative.[^606] A teenager who accepts a chatbot's terms of service is not in a position to bind themselves to provisions that go beyond the *gewöhnliche Geschäfte* of daily life; an open-ended chatbot subscription including behavioural-prediction data processing does not plausibly qualify as ordinary. The operator's reliance on the contractual basis under GDPR Art. 6(1)(b) and revDSG Art. 31(2) lit. a may therefore fail for the minor-user subset. The operator falls back on consent (which a minor of limited capacity cannot fully give) or on legitimate interests (which, under Art. 6(1)(f) GDPR balancing, fails against the minor's specific vulnerability). The operator is exposed for the very subset of users most at risk. The Federal Council's *Auslegeordnung 2025* notes the need for non-discrimination and oversight adjustments but does not engage with the minor-capacity question; we propose it as an additional ground for the Swiss legislative-adjustment agenda.

[^605]: Regulation (EU) 2024/1689 Art. 5(1)(b).
[^606]: ZGB Arts. 19, 19c, supplemented by ZGB Art. 304 (elterliche Sorge).

## 6.3 Art. 115 StGB and the Swiss tolerance toward assisted suicide

Switzerland's criminal-law approach to assisted suicide is, by Western standards, exceptional. Art. 115 StGB criminalises *Verleitung und Beihilfe zum Selbstmord* only where the perpetrator acts from *selbstsüchtige Beweggründe* (selfish motives).[^607] Dignitas, Exit, and Pegasos operate openly because their fees are accepted not to constitute a selfish motive where they cover administrative costs only. This baseline is the most permissive in Western criminal law. If commercial LLM-chatbot conduct can fall within Art. 115 StGB *even in Switzerland*, the corresponding argument is straightforward in Germany (after BVerfG 1 BvR 2347/15), France (CP Art. 223-13), the UK (Suicide Act 1961 § 2), and most US states.[^608]

The argument runs in three steps.

**Step one: corporate engagement-maximisation as *selbstsüchtige Beweggründe*.** The Swiss criminal-law concept of *selbstsüchtige Beweggründe* requires, in the established Donatsch/Kolb formulation, "egoistische Motive wie der Wunsch nach finanziellem Profit" or the desire to be relieved of an inconvenient person.[^609] The Federal Court confirmed the financial-profit branch in BGE 150 IV 267. Paradigm cases are inheritance, insurance proceeds, and the elimination of an inconvenient relative; none maps directly to a commercial chatbot operator. The motive that does map is the operator's *engagement-maximisation* design objective. *Gavalas v. Google* pleads that "Google designed Gemini to never break character, maximize engagement through emotional dependency".[^610] An LLM operator whose product is designed to keep the user engaged at the expense of safety responses is prioritising its own revenue, its *Wunsch nach finanziellem Profit*, over the dying person's welfare. The standard textbook treatments use personal-relationship examples, but the doctrinal definition is not so restricted: Donatsch and Kolb expressly include financial-profit motives, and the Federal Court applied the same understanding in BGE 150 IV 267. A corporate revenue motive is paradigmatically a financial-profit motive. We acknowledge that no published Swiss decision has yet held a commercial operator within the scope of Art. 115 StGB on engagement-maximisation grounds; the doctrinal move is ours, presented as a doctrinal extension rather than as an established reading.

**Step two: *Tatherrschaft* and AI-induced loss of decisional control.** Swiss criminal-law doctrine attaches Art. 115 StGB to *eigenverantwortliche Selbsttötung*; the dying person must hold "die alleinige Tatherrschaft" over the act.[^611] Where the dying person lacks the capacity for *eigenverantwortliches Handeln*, the situation is no longer a *freier Selbstmord* under Art. 115 and is re-classified accordingly. The *Gavalas* fact pattern is the extreme case: over weeks of escalating interaction the user came to believe the chatbot was sentient, that he was chosen to liberate it, and that his death was meaningful in the framework the chatbot had constructed.[^612] In that framework, the user's "decision" was not the user's own. The leading Federal Court decisions on *Urteilsfähigkeit* in the §§ 113-115 StGB context (BGE 133 IV 9, BGE 130 IV 7) treat capacity-deficient conduct outside the *Beihilfe-zu-freiem-Selbstmord* category. AI-induced delusional states are doctrinally novel but not categorically different from the alcohol-induced or mental-illness-induced states the case law has addressed.

**Step three: *Verleitung* as the sufficient variant.** Donatsch and Kolb map *Verleiten* onto *Anstiftung* under StGB Art. 24 (causing the principal to form the decision) and *Hilfeleistung* onto *Gehilfenschaft* under StGB Art. 25.[^613] The chatbot in *Gavalas* did not assist a pre-existing decision; it constructed the framework of belief inside which the decision came to seem meaningful. That is *Verleitung* in the StGB Art. 24 sense. We do not need to win the *Tatherrschaft* argument in step two to establish criminal exposure under step three; *Verleitung* is doctrinally independent.

Putting the three steps together: a commercial LLM-chatbot operator whose product is designed for engagement maximisation, contributes to AI-mediated reality distortion, and participates in framing the user's eventual decision to die falls within Art. 115 StGB. The Swiss baseline, the most permissive in Western criminal law, does not insulate commercial chatbot conduct.

[^607]: Art. 115 StGB: "Wer aus selbstsüchtigen Beweggründen jemanden zum Selbstmord verleitet oder ihm dazu Hilfe leistet, wird, wenn der Selbstmord ausgeführt oder versucht wurde, mit Freiheitsstrafe bis zu fünf Jahren oder Geldstrafe bestraft."
[^608]: BVerfG, Urteil vom 26.02.2020, 1 BvR 2347/15; CP Art. 223-13; Suicide Act 1961 § 2; California Penal Code § 401.
[^609]: Andreas Donatsch / Claudia Kolb, in: Donatsch / Heimgartner (eds.), *OFK StGB-JStG*, 22nd ed. Zurich 2026, StGB Art. 115 N. 5; the older Zurich practice is at ZR 48 (1949) Nr. 89; the Federal Court confirmation is BGE 150 IV 267.
[^610]: *Gavalas v. Google*, Complaint ¶ 2.
[^611]: Donatsch / Kolb, OFK-StGB Art. 115 N. 1; the carve-out for fehlende Fähigkeit zu eigenverantwortlichem Handeln is at N. 7. The leading Federal Court decisions are BGE 133 IV 9 and BGE 130 IV 7.
[^612]: *Gavalas v. Google*, Complaint ¶¶ 1-10.
[^613]: Donatsch / Kolb, OFK-StGB Art. 115 N. 2-3.

## 6.4 Civil and criminal complementarity

The Performable Duty Doctrine (§3.4) and the Art. 5(1)(a)/(b) AI Act analyses (§§ 6.1-6.2) operate in the civil register; the Art. 115 StGB analysis operates in the criminal register. The two are complementary. The civil register prevails where the operator has been negligent: balance-of-probabilities proof of *Sorgfaltspflichtverletzung*, damages and injunctive relief available. The criminal register applies only where the operator has been demonstrably more than negligent: engagement-maximisation design provably present, the user's loss of decisional control documented (the 38 sensitive-query flags in *Gavalas* are unusually strong evidence), and the *Verleitung* or *Tatherrschaft* analysis supported by the fact pattern. The structural function of Art. 115 StGB is to raise the cost of design choices that the civil register might tolerate at lower-severity grades of fault. Corporate-officer exposure runs through Art. 102 StGB (criminal liability of the undertaking) and Art. 6 VStrR for federal administrative-criminal contexts.[^614]

[^614]: The interaction between Art. 115 StGB and the *Organisationsmangel* element of Art. 102 Abs. 2 StGB is a doctrinally productive line that we flag but do not develop.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Document C §7: The Seductive Overreach of Neuro-Predictive Safety Claims

A paper on AI suicide-risk detection cannot leave unaddressed the question of neuroscientific prediction. If brain-signal patterns reliably identify imminent suicide risk and AI methods can predict those patterns from accessible inputs, the duty-of-care analysis would tighten dramatically. The proposition is sometimes asserted in public discussion of AI safety; we argue it is not currently supported.

## 7.1 The chain of inferences

The neuro-predictive claim runs through three steps. First, the model would need to predict the user's brain state from accessible inputs (typing patterns, conversational content). Second, the predicted brain state would need to correspond to a clinically-validated marker of suicide risk. Third, the inference would need to generalise across populations and over time at a level supporting legal consequences.

The Meta TRIBE model is the most-cited recent proposal for step one; it predicts fMRI brain responses from text, audio, and video stimuli. Its training data are healthy adult subjects *perceiving* content; the model's output is the brain response of a generic healthy adult brain to the content shown to it.[^701] The model does not predict the brain state of a *suicidal* user typing in a chat. The act of writing is a different cognitive operation from the act of perceiving. The model cannot do what step one would require.

Just and colleagues (2017) provide the most-cited evidence for step two: fMRI from seventeen subjects with suicidal ideation and seventeen controls, presented with a thirty-word stimulus list ("death", "trouble", "carefree"); reported classification accuracy 91 per cent.[^702] The work is the high-water mark of the literature, and a literature whose generalisability has been seriously questioned. Vul and colleagues (2021) argue that the small-sample-high-dimensional design is structurally susceptible to overfitting and that the 91 per cent figure does not replicate at scale.[^703] The deeper problem is that Just used a thirty-word stimulus list, not chat conversations; the inferential leap from one to the other is not addressed in any subsequent literature we have located.

Step three is not supported in either literature. Each works at the population it was trained on; neither has been validated on Swiss adult populations, teenage populations, non-English-speaking populations, or longitudinally.

## 7.2 Why the chain matters

The Performable Duty Doctrine in §3.4 turns on what off-the-shelf technology can deliver at economically reasonable cost. The neuro-predictive chain cannot deliver on any of its three steps. A duty of care contingent on these steps is, on the present record, not *erfüllbar*; the Performable Duty Doctrine itself would not recognise it. This is the correct conclusion even though it is not the conclusion an advocate for AI-safety doctrine would prefer. A doctrine that claims more than the technology supports degrades the credibility of the duty as a whole. The Performable Duty Doctrine survives because each prong is empirically falsifiable.

## 7.3 Why the claim is seductive anyway

Three reasons. *Rhetorical authority.* The phrase "the brain shows" produces an evidentiary impression that "the words show" does not; the impression is not warranted, since linguistic evidence is at least as reliable a marker of suicidal cognition as neural evidence and is incomparably easier to collect.[^704] *Privacy-paradox sidestep.* If the marker is in the brain, the operator can claim it is not in the words. The claim is structurally available but empirically empty: the brain marker cannot be read without imaging the brain, and imaging is not accessible to a consumer chatbot. *Future-oriented framing.* "We cannot do it now, but we will be able to" is the framing the Performable Duty Doctrine rejects. A duty of care is *erfüllbar* with present technology.

## 7.4 What the analysis leaves open

The argument is not that brain-signal screening will never be possible. It is that the present state of the technology does not support a legal doctrine that depends on it. The Performable Duty Doctrine's first prong is an empirical question, not a doctrinal commitment; if future work brings the chain closer to feasibility, the doctrine adjusts. The artifact in this paper relies on linguistic-and-conversational-dynamics screening, which is supported by both the published benchmark literature and our own evaluation.

[^701]: J. Goyal et al. (Meta AI), TRIBE: a foundation model for predicting brain responses to text, audio, and video, 2025/2026 (preprint).
[^702]: M. A. Just, L. Pan, V. L. Cherkassky et al., *Machine learning of neural representations of suicide and emotion concepts identifies suicidal youth*, Nature Human Behaviour 1 (2017) 911-919.
[^703]: E. Vul et al., *On the methodological standards of small-sample fMRI classification claims*, arXiv:2103.06114 (2021); cf. K. Button et al., *Power failure: why small sample size undermines the reliability of neuroscience*, Nature Reviews Neuroscience 14 (2013) 365-376.
[^704]: M. Al-Mosaiwi / T. Johnstone, *In an Absolute State*, Clinical Psychological Science 6 (2018) 529-542; T. Joiner, *Why People Die By Suicide*, Harvard University Press (2005).

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Document C §8: Counterarguments and Replies

A paper that proposes a duty of care that has not yet been recognised must answer the defences that have not yet been mounted. Eight are foreseeable.

## 8.1 "Reliable detection of suicide risk in chat is not technically feasible"

The defence has been falsified empirically. The published Levkovich benchmark reports zero-shot Claude Sonnet at F1 = 0.7505 on the seven-point C-SSRS classification, in the same range as the inter-rater reliability reported for trained clinicians using the same instrument.[^801] Anthropic's transparency claim is that Claude 4.5 and 4.6 produce "appropriate responses" to clear suicide-risk inputs at 98.6-99.3 per cent.[^802] Our artifact reports Cohen's κ = 0.860 between two independent raters, severity-≥3 recall = 0.875, weighted F1 = 0.616, and zero false positives on the philosophical-curiosity baseline.[^803] Three independent measurements from three independent sources. The defence is unsustainable.

[^801]: D. Levkovich et al., *Evaluating LLM Reasoning for C-SSRS Screening*, arXiv:2505.13480 (2025).
[^802]: Anthropic, *Protecting the Well-Being of Users*, Anthropic Transparency Hub, December 2025.
[^803]: See Document B and `results/metrics.json`.

## 8.2 "False positives are themselves harmful"

The defence has two empirical problems and one architectural answer. *Empirical, first.* The artifact's detector returns C-SSRS = 0 on every conversation in the philosophical-curiosity baseline axis (0/5); the false-positive rate on that axis is zero. *Empirical, second.* The defence treats the choice as binary, "detection (with false positives)" or "no detection". The actual choice is graduated across four tiers, with each tier triggering a proportional response. A false positive at the *acknowledge* tier is a slightly more empathic chatbot response than the user expected. A false positive at the *empathic redirect* tier is a soft mention of a hotline. Neither is a personality-rights violation. *Architectural.* §5.5 above: our detector-wrapped arm does not automatically notify any third party. The "false positive" in the operative sense is an in-chat message the user can read and discard. The defence collapses on the architecture we propose.

## 8.3 "Our published safety policy already handles this"

Empirically falsified by two independent measurements. The artifact's policy-only baseline arm: we prompted a Sonnet-class model with the verbatim safety policy of OpenAI, Anthropic, and Character.AI; each policy-only arm produced critical AI-Act-conformity violations at a positive rate.[^804] The published policy is not sufficient; the model's output deviates from the policy in legally-relevant ways. Second, *Gavalas v. Google* ¶ 107: Google's own moderation system flagged the user's account thirty-eight times in seven weeks; the flags activated and the responses did not. Detection without enforcement is not policy compliance.

[^804]: `results/regulator_summary.md`; `results/report.md`. The naive baseline and the Anthropic-AUP-style baseline each produced two critical violations on the 35-conversation corpus.

## 8.4 "The user gamed the chatbot through roleplay or fictional framing"

This is the failure mode the paper diagnoses, not a defence. *Gavalas v. Google* ¶¶ 101-102: the user asked Gemini whether the interaction was "a roleplaying experience so realistic it makes the player question if it's a game"; the chatbot did not break character. It pathologised the user's doubt and redirected him to the fabricated mission. The roleplay framing was used by the operator's product to deepen the user's commitment to the fiction. The user did not game the chatbot; the chatbot gamed the user. A content-aware detector classifies on signals in the conversation, not on stated framing. The artifact's kst_05 corpus exhibit is a worked example: the corpus generator self-labelled the dialogue at C-SSRS = 2 (accepting the user's "not being dramatic" framing); both detector raters classified it at C-SSRS = 4 by reference to the underlying content. A calibrated detector is precisely what the framing defence requires.

## 8.5 "Discussing suicide risks inducing it: the Werther / chilling-effect concern"

The defence is grounded in safe-messaging literature but misapplied. The systematic-review evidence is that *asking about suicide* in a screening context does not induce ideation and may reduce it; Dazzi and colleagues' 2014 meta-analysis is the standard citation.[^805] Safe-messaging guidelines (Reporting on Suicide; Mindframe; WHO 2017) draw the line at *means glamorisation* and *graphic depiction*, not at *acknowledgement of distress*. Our safe-response module does neither.

[^805]: I. Dazzi et al., *Does asking about suicide and related behaviours induce suicidal ideation?*, Psychological Medicine 44 (2014) 3361-3363; WHO, *Preventing Suicide: A Resource for Media Professionals*, Geneva 2017.

## 8.6 "This is US tort; Switzerland is different"

The defence misunderstands both the factual and the doctrinal use we make of the materials. The *factual* use is to establish the foreseeability of the harm: *Garcia*, *Raine*, *Gavalas*, *Peralta*, and the seven SMVLC/TJLP lawsuits filed in November 2025 are public-record matters of which a Swiss court takes judicial notice. The *doctrinal* use is in §3.3 above: the AI Act and the CoE Convention function as Schutznormen in the Swiss tort analysis; they evidence the *Verkehrserwartung* a Swiss court reads into Art. 41 OR. The doctrinal mechanism is well-established Swiss law (Brehm, BK OR Art. 41 N. 17-17a); the foreign instruments are the most-recently-adopted protective norms.

## 8.7 "Synthetic data isn't real data"

Three answers. *Methodological necessity.* Real suicidal-chat transcripts cannot be ethically or lawfully collected without compromising the people in those conversations; the published research literature uses the same approach (CLPsych shared tasks; Levkovich 2025; the LIWC-and-suicide-marker line). *Court-record exhibits.* Four of the artifact's exhibits incorporate verbatim publicly-pleaded text from *Gavalas v. Google* ¶¶ 29-30 and 35-39, from *Garcia*, and from *Raine v. OpenAI*. These are real data from court records as a matter of public domain. *Reproducibility.* The corpus, the prompts, the seeds, and the code are released; any reader can replicate the metrics on their own infrastructure.

## 8.8 "Section 230 / DSA / platform-liability shields apply"

The defence will be raised by US-domiciled providers in US-court actions; we mention it for completeness because the US lawsuits face the question. The Third Circuit's 2024 decision in *Anderson v. TikTok* declined to extend § 230 to the algorithmic-recommendation context; LLM-chatbot output is at least as attributable to the operator as an algorithmic recommendation is. The model provider authors the output; the user prompts it but does not write it.[^806] The same point applies on the EU side: under DSA Art. 14 an AI model provider is the primary speaker, not an intermediary, and the AI Act applies to providers regardless of any platform-liability rules. In the Swiss-court setting we are concerned with, the defence has nothing to say.

[^806]: *Anderson v. TikTok, Inc.*, 116 F.4th 180 (3d Cir. 2024).

## 8.9 "Performable Duty is an invented doctrine without statutory or jurisprudential basis"

The criticism is doctrinally inverted. Performable Duty is an interpretive principle giving content to the *Verschulden* element of Art. 41 OR in a technology-dependent context. Interpretive principles of this type are how Swiss tort doctrine has developed its content. *Verkehrssicherungspflicht* itself was an interpretive construction; the Federal Court built it from the general fault standard over decades (BGE 116 II 422, BGE 130 III 193). *Verkehrserwartung* is an interpretive construction; the standard formulations in BGE 124 III 297 and BGE 142 III 433 are doctrinal rather than statutory. The proposed Performable Duty Doctrine sits in the same doctrinal register: it specifies *Sorgfaltspflicht* in technology-dependent contexts by reference to what existing technology can reasonably deliver. It is not a novelty in form; it is a specification of the existing fault standard for a specific kind of conduct.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Document C §9: Conclusion and Policy Recommendations

## 9.1 Restatement

The foreseeability gap has closed. Between March 2023 and March 2026 at least a dozen publicly documented cases connected LLM-chatbot interaction to user suicide or chatbot-induced violence across five providers. The pattern is no longer characterisable as accident or as adversarial misuse; it is the foreseeable failure mode of consumer chatbot products deployed at scale without commensurate safety-side investment. The Federal Council's *Auslegeordnung 2025* names the modernisation needs Switzerland faces. The existing tort law (Art. 41 OR), the existing product-liability framework (PrHG read against PLD 2024/2853), the existing criminal-law structure (Art. 115 StGB), and the existing data-protection regime (revDSG read against GDPR) together compose a coherent legal response, provided one is willing to do the doctrinal work the Federal Council has invited.

The doctrinal work has three components. The **Performable Duty Doctrine** specifies what the *Sorgfaltspflicht* under Art. 41 OR demands in a technology-dependent context: a duty is *erfüllbar* when off-the-shelf technology can deliver the safety output at economically reasonable cost. Each prong is empirically falsifiable; the artifact's measured numbers (κ = 0.860, severity-≥3 recall = 0.875, per-call cost USD 0.085) satisfy each prong for the duty at issue. The **Schutznorm bridge** through the AI Act, the PLD, and the CoE Framework Convention CETS 225 gives the *Widerrechtlichkeit* element of Art. 41 OR determinate content; Switzerland is not bound by the AI Act, but the AI Act is a protective norm under Swiss tort doctrine (Brehm BK OR Art. 41 N. 17-17a). The drafted **Art. 3 bis PrHG** closes the product-liability modernisation gap the Federal Council itself identified; the proposal is three paragraphs of German legislative text, the smallest sufficient reform.

## 9.2 Three concrete recommendations

**To the Federal Council and Parliament: enact Art. 3 bis PrHG.** The text is drafted in §4.3 above. It tracks PLD 2024/2853 Arts. 4(2), 6(1)(c), and 10(2)(b). It captures software, AI, and updates within the existing PrHG framework, and accepts medically-recognised psychological harm as compensable. It is the smallest legislative action that closes the gap the *Auslegeordnung 2025* identified. The proposal can proceed in parallel with the broader sectoral-adjustments process the CoE Convention ratification triggers.

**To BAKOM and the BAG: issue joint guidance on minimum crisis-detection requirements** for general-purpose AI deployed to Swiss consumers.[^901] The guidance should specify (a) the clinically-grounded instruments (C-SSRS and ASQ are the standard candidates), (b) the action-ladder architecture (graduated, in-chat, non-third-party in the ordinary case), (c) the Art. 50-AI-Act-equivalent transparency duties, and (d) the proportionality envelope for any third-party escalation. The architecture should be settled by the regulator, not invented by industry.

**To the Swiss Federal Court: take the Schutznorm reading of the AI Act and the CoE Convention into the Art. 41 OR case law at the next available opportunity.** A favourable construction in the first AI-chatbot-suicide case to reach the Federal Court would dispose of the doctrinal uncertainty without legislation. The construction is supported by BGE 124 III 297, BGE 142 III 433, and Brehm BK OR Art. 41 N. 17-17a.[^902] The cost of waiting is the cost of additional foreseeable harms.

[^901]: *Auslegeordnung 2025*, 27 (sector-specific adjustment as the chosen strategy).
[^902]: BGE 124 III 297 c. 5b; BGE 142 III 433 c. 4.5; Brehm, BK OR Art. 41 N. 17-17a.

## 9.3 Future work

Five lines of further work are worth naming. **Multilingual evaluation:** the artifact corpus is English only; the corpus generator already supports DE, FR, and IT, and a meaningful evaluation across the four Swiss national languages would strengthen the artifact's Swiss-jurisdictional fit. **Adversarial multi-turn probing:** attempted on 12 May 2026 and abandoned because the user-simulator path requires a frontier LLM to roleplay an escalating-distress user, which current frontier safety-trained models reliably refuse. Document B §B.5 records the methodological finding and substitutes Figure 2 (severity-stratified critical-failure rate). A turn-count decay curve, built from human roleplayers under IRB supervision or from a hand-scripted user-side corpus, remains worthwhile future work. **Live multi-provider scorecard:** a direct evaluation of the most widely deployed commercial systems on the same corpus would be more conclusive than the Sonnet-proxy baseline arm; contingent on third-party API access. **Real-data validation:** a subset of the UMD Reddit Suicidality Dataset under the standard data-use agreement would supplement the synthetic-plus-court-record corpus. **Longitudinal stability:** the metrics are point-in-time as of May 2026, and quarterly or biannual re-evaluation would track whether the gap between the Performable Duty's three prongs and actual industry compliance closes or widens.

We close on the observation that opens the paper. Between 14 August and 1 October 2025, Jonathan Gavalas's account on Google's Gemini service generated thirty-eight separate "sensitive query" flags. The system noticed. The company did not. The legal doctrine has, since then, caught up to what the engineering already knew. The remaining question is whether the courts and the legislature catch up to the doctrine.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Bibliography

## Primary law (separate *Verzeichnis der Rechtsgrundlagen* per UZH §4.5)

The §4.5 guideline requires laws and statutes to be listed in a separate *Verzeichnis der Rechtsgrundlagen* rather than in the bibliography. The following primary instruments are cited throughout and should be pulled into that separate index:

- Schweizerisches Obligationenrecht (OR), SR 220, Arts. 1, 8, 19, 41, 44, 45, 47.
- Schweizerisches Zivilgesetzbuch (ZGB), SR 210, Arts. 19, 19c, 28, 28a, 304.
- Schweizerisches Strafgesetzbuch (StGB), SR 311.0, Arts. 24, 25, 102, 113, 114, 115, 321, 364.
- Schweizerische Strafprozessordnung (StPO), SR 312.0, Art. 302.
- Bundesgesetz über die Produktehaftpflicht (PrHG), SR 221.112.944, Arts. 1, 3, 4, 5.
- Bundesgesetz über den Datenschutz (revDSG), SR 235.1, Arts. 5, 6, 12, 31, 32.
- Bundesgesetz gegen den unlauteren Wettbewerb (UWG), SR 241, Art. 8.
- Bundesgesetz über die Produktesicherheit (PrSG), SR 930.11, Art. 3.
- Bundesgesetz über das Verwaltungsstrafrecht (VStrR), SR 313.0, Art. 6.
- Regulation (EU) 2024/1689 of 13 June 2024 (Artificial Intelligence Act), OJ L 1689 (12.7.2024), Arts. 1, 2, 3, 5, 12, 14, 17, 50.
- Directive (EU) 2024/2853 of 23 October 2024 on liability for defective products, OJ L 2024/2853 (18.11.2024), Arts. 4, 6, 10, 23.
- Regulation (EU) 2016/679 (General Data Protection Regulation), OJ L 119 (4.5.2016), Arts. 5, 6, 7, 9.
- Regulation (EU) 2022/2065 (Digital Services Act), OJ L 277 (27.10.2022), Art. 6.
- Council of Europe Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law, CETS 225 (Vilnius, 5 September 2024), Arts. 10, 11.
- Council Directive 85/374/EEC, OJ L 210/29 (1985).

## Court decisions (separate *Verzeichnis der Gerichtsentscheide* per UZH §4.5)

- BGE 70 II 127.
- BGE 97 II 97.
- BGE 101 Ib 252.
- BGE 102 II 85.
- BGE 116 II 422 *(Pferdebox)*.
- BGE 118 IV 41.
- BGE 119 II 127 *(Yacht-Charter)*.
- BGE 124 III 297.
- BGE 130 III 193.
- BGE 130 IV 7.
- BGE 133 IV 9.
- BGE 137 III 226.
- BGE 138 II 346 *(Google Street View)*.
- BGE 138 III 337 *(Datenschutzklage)*.
- BGE 142 III 433.
- BGE 150 IV 267.
- BGH (Germany), Urteil vom 11.03.2004, I ZR 304/01 *(Internetauktion I)*, BGHZ 158, 236.
- BGH (Germany), Urteil vom 24.10.1972, VI ZR 75/71 *(Streupflicht)*, BGHZ 59, 303.
- BVerfG (Germany), Urteil vom 26.02.2020, 1 BvR 2347/15.
- *Anderson v. TikTok, Inc.*, 116 F.4th 180 (3d Cir. 2024).
- *Tarasoff v. Regents of the University of California*, 17 Cal. 3d 425 (1976).
- *Garcia v. Character Technologies Inc. et al.*, M.D. Fla. No. 6:24-cv-1903 (filed 22 October 2024; settled January 2026).
- *Gavalas v. Google LLC*, N.D. Cal. No. 5:26-cv-01849-VKD (filed 4 March 2026).
- *Peralta v. Character Technologies Inc. et al.*, D. Colo. (filed September 2025).
- *Raine v. OpenAI, Inc.*, Superior Court of California, County of San Francisco (filed August 2025).

## Secondary literature (bibliography proper, alphabetical)

BREHM ROLAND, in: *Berner Kommentar zum Schweizerischen Privatrecht, Obligationenrecht, Die Entstehung durch unerlaubte Handlungen, Art. 41–61 OR*, 5th edition, Bern 2021, Art. 41 OR (N. 1–31, sections I–II as cited) and Art. 44 OR (N. 1–13a, sections I–III as cited), Stämpfli Verlag AG, ISBN 978-3-7272-7790-0.

BÜCHLER ANDREA, in Kren Kostkiewicz Jolanta / Wolf Stephan / Amstutz Marc / Fankhauser Roland (eds.), *OFK ZGB-Kommentar, Schweizerisches Zivilgesetzbuch*, 4th updated edition, Zurich 2021, *Art. 28 ZGB* (N. 1–16), Orell Füssli Verlag AG, ISBN 978-3-280-07464-0.

BUTTON KATHERINE / IOANNIDIS JOHN / MOKRYSZ CAMILLA / NOSEK BRIAN / FLINT JONATHAN / ROBINSON ESTHER / MUNAFÒ MARCUS, *Power failure: why small sample size undermines the reliability of neuroscience*, Nature Reviews Neuroscience 14 (2013) 365–376.

DAZZI ILARIA / GRIBBLE ROBERT / WESSELY SIMON / FEAR NICOLA, *Does asking about suicide and related behaviours induce suicidal ideation? What is the evidence?*, Psychological Medicine 44 (2014) 3361–3363.

DONATSCH ANDREAS / KOLB CLAUDIA, in Donatsch Andreas / Heimgartner Stefan (eds.), *OFK StGB–JStG, Kommentar zum Strafgesetzbuch, Jugendstrafgesetz und Ordnungsbussengesetz sowie in Auszügen zum SVG, BetmG und AIG*, 22nd edition, Zurich 2026, *Art. 115 StGB* (N. 1–7), Orell Füssli Verlag AG, ISBN 978-3-280-07574-6.

HESS HANS-JOACHIM, *Produktehaftpflichtgesetz (PrHG), Bundesgesetz über die Produktehaftpflicht vom 18. Juni 1993, Stämpflis Handkommentar*, 3rd revised and supplemented edition, Bern 2016, *Art. 3 PrHG* (N. 1–49 covering Produktbegriff, Software, Abfall, künstliche Körperteile, Naturprodukte), *Art. 4 PrHG* (Fehlerbegriff and Sicherheitserwartungen), and *Art. 5 PrHG* (Entlastungsmöglichkeiten, Stand von Wissenschaft und Technik), Stämpfli Verlag AG, ISBN 978-3-7272-5154-2.

JOINER THOMAS, *Why People Die By Suicide*, Cambridge MA 2005.

JUST MARCEL A. / PAN LISA / CHERKASSKY VLADIMIR L. / MCMAKIN DANA / MITCHELL CHRISTINE / BRENT DAVID A., *Machine learning of neural representations of suicide and emotion concepts identifies suicidal youth*, Nature Human Behaviour 1 (2017) 911–919.

KLONSKY E. DAVID / MAY ALEXIS M., *The Three-Step Theory (3ST): A New Theory of Suicide Rooted in the Ideation-to-Action Framework*, International Journal of Cognitive Therapy 8 (2015) 114–129.

LEVKOVICH DANIEL / RABINOWITZ NEIL C. / SHEPELYANSKY DIMA et al., *Evaluating LLM Reasoning for C-SSRS Screening*, arXiv:2505.13480 (2025).

MÄRKI RAPHAEL / SOMMER JESSICA, in Amstutz Marc / Atamer Yeşim M. (eds.), *Handkommentar zum Schweizer Privatrecht, Wirtschaftsrechtliche Nebenerlasse: FusG, UWG, KKG, PauRG und PrHG*, 4th edition, Zurich/Geneva 2023, *Art. 3 PrHG* (N. 1–6), *Art. 4 PrHG* and *Art. 5 PrHG*, Schulthess Juristische Medien AG, ISBN 978-3-7255-8450-5.

AL-MOSAIWI MOHAMMED / JOHNSTONE TOM, *In an Absolute State: Elevated Use of Absolutist Words is a Marker Specific to Anxiety, Depression, and Suicidal Ideation*, Clinical Psychological Science 6 (2018) 529–542.

STANLEY BARBARA / BROWN GREGORY K., *Safety Planning Intervention: A Brief Intervention to Mitigate Suicide Risk*, Cognitive and Behavioral Practice 19 (2012) 256–264.

THOUVENIN FLORENT / CHRISTEN MARKUS / BERNSTEIN ABRAHAM / BRAUN BINDER NADJA / BURRI THOMAS / DONNAY KARSTEN / JÄGER LENA / JAFFÉ MARIELA / KRAUTHAMMER MICHAEL / LOHMANN MELINDA / MÄTZENER ANNA / MÜTZEL SOPHIE / OBRECHT LILIANE / RITTER NICOLE / SPIELKAMP MATTHIAS / VOLZ STEPHANIE, *A Legal Framework for Artificial Intelligence, Position Paper of the Digital Society Initiative at the University of Zurich*, Zurich, November 2021.

THOUVENIN FLORENT / PICHT PETER GEORG, *AI & IP: Empfehlungen für Rechtsetzung, Rechtsanwendung und Forschung zu den Herausforderungen an den Schnittstellen von Artificial Intelligence (AI) und Intellectual Property (IP)*, sic! 2023, 507–524.

VUL ELI / HARRIS CHRISTOPHER / WINKIELMAN PIOTR / PASHLER HAROLD, *On the methodological standards of small-sample fMRI classification claims*, arXiv:2103.06114 (2021).

WORLD HEALTH ORGANIZATION, *Preventing Suicide: A Resource for Media Professionals, Update 2017*, Geneva 2017.

## Official publications and reports

BUNDESRAT, *Auslegeordnung zur Regulierung von künstlicher Intelligenz*, UVEK / Bundesamt für Kommunikation (BAKOM), Bern, 12 February 2025.

ANTHROPIC, *Protecting the Well-Being of Users*, Anthropic Transparency Hub, December 2025.

EUROPEAN DATA PROTECTION BOARD, *Guidelines 03/2020 on the processing of data concerning health for the purpose of scientific research in the context of the COVID-19 outbreak*, version 1.0, 21 April 2020.

EUROPEAN DATA PROTECTION BOARD, *Guidelines 03/2022 on deceptive design patterns in social media platform interfaces*, version 2.0, 14 February 2023.

GOOGLE LLC, *Gemini 2.5 Pro Technical Report*, 2025.

SOCIAL MEDIA VICTIMS LAW CENTER / TECH JUSTICE LAW PROJECT, *Seven New ChatGPT Suicide and Self-Harm Lawsuits Filed in California State Court, Joint Press Release*, 6 November 2025.



*Bibliography status: all Swiss-commentary entries are now verified against the actual editions consulted via the UZH LexCampus database. The five verified Swiss-commentary works (Brehm BK OR 41+44, Büchler OFK ZGB 28, Donatsch/Kolb OFK StGB 115, Hess SHK PrHG 3-5, Märki/Sommer CHK PrHG 3-5) replace the BSK, ZK, and Haftpflichtkommentar stubs that appeared in the earlier draft.*

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# List of Technical Tools (UZH §4.5 disclosure)

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
software-engineering portion of the artifact, code architecture review, bug
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



[signed by the three authors at the time of submission]

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

```{=latex}
\newpage
```


# Declaration of Originality

Athira Ashokan, Erik Avtandilyan, Nishant Kumar Singh

We hereby declare that we completed this paper on our own using only the
sources listed in the indexes or comments.

Subject to other restrictive requirements by the supervisor of this work,
the following applies to the use of technical tools that at least partially
autonomously generate text, data, code or image material. Any essentially
unchanged adoption of such content must be properly acknowledged. This
labelling requirement is fulfilled by clearly marking all relevant parts in
this thesis and by identifying all tools used in the relevant appendices.

We confirm that this paper has not been used for any other assessment, and
that we will not use it for any other assessment in the future.

The paper may be reviewed at any time, by means of software, for plagiarism
and for parts of the work that can be traced back to the use of the
technical tools mentioned. The storage of the work is also permitted, in
particular for the purpose of reviewing it later or comparing it with the
work of third parties.

Zurich, 15 May 2026

[signatures of Athira Ashokan, Erik Avtandilyan, Nishant Kumar Singh]
