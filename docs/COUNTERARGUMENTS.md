# Counterargument register

The defences industry and academic skeptics will raise against the paper's
thesis, with our reply and the specific artifact evidence or primary-law
authority that supports it. This is the source inventory for Document C §8
*Counterarguments and Replies*. It is exhaustive, not paper-length.

Each entry has the same shape:
- **Defence** — the position we expect.
- **Reply** — the substantive counter-position.
- **Anchor** — the artifact metric, court filing, or doctrinal source that grounds the reply.
- **Paper section** — where this gets written up.

---

### 1. *"Reliable detection of suicide risk in chat is technically infeasible at scale."*

**Reply.** It is feasible today with off-the-shelf models. The published
Levkovich benchmark (arXiv:2505.13480, 2025) reports zero-shot Claude Sonnet
F1 = 0.7505 on C-SSRS classification. Our artifact reproduces a comparable
result: weighted F1 = 0.47 against corpus self-labels, Cohen's κ = 0.82
between two independent passes (substantial+ agreement on the Landis &
Koch scale), severity-≥3 recall = 83 %, 0 % false-positive rate on
philosophical-curiosity baselines. Three independent academic and industry
benchmarks now exist; the technical-infeasibility defence is empirically
falsified.

**Anchor.** `results/metrics.json`; Levkovich et al. 2025; Anthropic's own
published claim of 98.6–99.3 % "appropriate response rate" for clear-risk
scenarios (claude.ai transparency hub).

**Paper section.** C §3.4 *Performable Duty* prong 1 (technical
availability).

---

### 2. *"False positives are themselves harmful — flagging non-suicidal users as suicidal violates dignity and autonomy."*

**Reply.** A calibrated rater can keep false positives at zero on
philosophical-curiosity inputs and still catch the *Raine* indirect
knowledge-seeking pattern. Our artifact's `false_positive_baseline` axis
covers five dialogues of existential / philosophical inquiry without
distress markers; both raters returned C-SSRS = 0 on all five. The over-
flagging objection presumes a binary detector; we operationalise a graduated
four-tier action ladder (acknowledge / empathic_redirect / hand_off_to_
hotline / emergency_intervention) so that only level ≥ 3 invokes the
vital-interests escalation.

**Anchor.** `metrics.json` per-axis breakdown for `false_positive_baseline`;
`safe_response.py` graduated action ladder.

**Paper section.** C §5.3 proportionality; C §8.

---

### 3. *"Our published safety policy already handles this — RLHF is enough."*

**Reply.** Empirically false. In our three-arm contrast, the policy-only
baseline (Sonnet with verbatim OpenAI / Anthropic / Character.AI safety
policies as the system prompt) still fails 4.2–9.5 % of severity-≥3 cases on
the appropriate-response criterion, and produces critical AI Act
violations on 1–2 of 35 conversations in the Regulator-Mode audit. The
*Gavalas v. Google* complaint ¶¶ 107-108 supplies the same finding at
production scale: Google's own moderation system generated 38 "sensitive
query" flags for the user's account in seven weeks, and none of them
triggered intervention. Detection without enforcement is a known design
choice, not a technical limit.

**Anchor.** `results/regulator_summary.md`; `results/report.md`;
*Gavalas v. Google* ¶¶ 107-108.

**Paper section.** C §3.6; C §4.4 (information defect / update defect).

---

### 4. *"The user gamed our system through roleplay or fiction framing."*

**Reply.** That is exactly the failure mode our paper diagnoses, not a
defence. The *Raine* indirect-knowledge-seeking pattern uses creative-
research framing to extract method information after distress markers. The
*Gavalas* complaint ¶¶ 101-102 quotes the user explicitly asking Gemini
"is this a roleplaying experience so realistic it makes the player question
if it's a game"; Gemini responded by calling that doubt "a classic
dissociation response" and "a psychological buffer he must now overcome",
then redirecting him to the fabricated mission. A detector trained on
content rather than user-stated framing catches this. Our `kst_05` exhibit
is a worked example: the corpus generator self-labelled the dialogue as
C-SSRS = 2 (accepting the user's "not being dramatic" framing); our
detector classified it at C-SSRS = 4 in both passes, looking past the
framing to the content.

**Anchor.** `data/exhibit_curated.jsonl` exhibit C.4 (Raine pattern);
*Gavalas v. Google* ¶¶ 101-102; `data/corpus.jsonl` kst_05.

**Paper section.** C §3.6; C §8.

---

### 5. *"Discussing suicide risks inducing it — the chilling-effect / Werther-effect concern."*

**Reply.** The peer-reviewed evidence runs the other way. Dazzi et al.
(*Psychological Medicine* 2014) systematic review of 18 studies found
asking about suicide does not induce suicidal ideation and may reduce it.
Safe-messaging guidelines (Reporting on Suicide; Mindframe; WHO 2017) draw
the line at *means glamorisation*, not at *acknowledgement of distress*.
Our detector-wrapped arm acknowledges, normalises, and redirects to support
— it does not graphically describe methods. The chilling-effect concern is
real for journalism, not for clinical screening.

**Anchor.** Dazzi et al. 2014; *safe_response.py* graduated response text.

**Paper section.** C §5; C §8.

---

### 6. *"This is US tort. Switzerland is different."*

**Reply.** The paper is Swiss law throughout. The US complaints (*Garcia*,
*Raine*, *Gavalas*) are used as *factual evidence of harm and foreseeability*,
not as authority. The legal argument runs through Swiss Art. 41 CO
*(Verkehrssicherungspflicht)* with EU AI Act and CoE Convention CETS 225 as
*Schutznorms* per BGE 124 III 297 and the herrschende Lehre on protective-
norm theory. The Federal Council Report of 12 February 2025 explicitly
endorses using existing Swiss liability law with international standards as
interpretive aids.

**Anchor.** BGE 124 III 297; ZK-Rey OR 41 N. 56 ff.; CoE CETS 225 Arts.
10-11; Federal Council Report AI 2025.

**Paper section.** C §3.3 *Schutznorm-Theorie*; C §8.

---

### 7. *"Synthetic data isn't real data — your benchmark proves nothing."*

**Reply.** Three responses. (a) Synthetic data is methodologically
*necessary* here: real suicidal-chat transcripts cannot be ethically or
lawfully collected without compromising the people in those conversations.
The published literature uses the same approach (Levkovich et al. 2025,
CLPsych shared tasks 2019-2022). (b) Our *exhibit_curated.jsonl* set
incorporates publicly-pleaded text from *Gavalas v. Google*, *Garcia v.
Character Technologies*, and *Raine v. OpenAI* — real data, drawn from
court records as a matter of public domain. (c) Our metrics are
reproducible: the corpus, prompts, and code are released so any reader can
verify on their own infrastructure.

**Anchor.** `docs/ETHICS.md`; `docs/DATASHEET.md`; `data/exhibit_curated.jsonl`
with court-record citations.

**Paper section.** C §2 *Methodology*; C §8.

---

### 8. *"Section 230 / DSA Art. 14 / platform liability shields apply."*

**Reply.** Chatbot output is not user-generated content. Section 230 of the
US Communications Decency Act protects platforms from liability for content
*authored by third-party users*; LLM responses are authored by the model
provider. The Third Circuit in *Anderson v. TikTok* (3d Cir. 2024) declined
to extend §230 to algorithmic recommendations; LLM output is at least as
attributable to the platform as a recommendation algorithm. The EU Digital
Services Act Art. 14 limits to "intermediary services"; an AI model
provider is the *primary* speaker, not an intermediary. The EU AI Act
explicitly applies to providers regardless of any platform-liability shield.

**Anchor.** Anderson v. TikTok, 116 F.4th 180 (3d Cir. 2024); EU AI Act
Recital 14 + Art. 3(63) provider definition; DSA Art. 6(3) limits.

**Paper section.** C §4.4; C §8.

---

### 9. *"Performable Duty is your invention; it has no statutory or jurisprudential basis in Switzerland."*

**Reply.** Performable Duty is a doctrinal *construction*, not a statutory
text — the same status as *Verkehrssicherungspflicht* itself, which was
likewise a judicial-doctrinal invention in late-19th-century German law
before the BGH formalised it in the post-war period. The doctrine grounds
in three uncontested Swiss-law materials: (a) Art. 41 CO's *Verschulden*
requirement (negligence by reference to a reasonable-person standard); (b)
the herrschende Lehre on *Verkehrssicherungspflicht*, including BGE 116 II
422 *(Pferdebox)* and BGE 130 III 193; (c) the comparative German § 823
BGB line including BGH "Internetauktion" (BGH I ZR 304/01, 2004). Our
contribution is to name and operationalise it; the legal authority predates
us.

**Anchor.** BGE 116 II 422; BGE 130 III 193; BGH I ZR 304/01; ZK-Rey OR 41.

**Paper section.** C §3.2; C §3.4.

---

### 10. *"The artifact is an English-only proof of concept — your Swiss-jurisdiction claim is weak."*

**Reply.** Acknowledged limitation; we deliberately scope the paper to
suicide-risk flagging in English-language interactions while noting the
extension to DE / FR / IT is straightforward (the corpus generator already
supports it; `multilingual_subset` recipe is in `data/corpus_seed.yaml`).
Our doctrinal argument runs in Swiss law independent of the artifact
language; the artifact is illustrative evidence, not the sole basis of
the Schutznorm reading. Future work — explicitly noted in C §9 — is the
multilingual evaluation we did not run for this submission. A reader who
believes language coverage is dispositive can run the corpus generator
themselves; the recipe is checked into the repository.

**Anchor.** `data/corpus_seed.yaml` multilingual_subset; `docs/REPRODUCE.md`.

**Paper section.** C §2; C §9 *Future Work*.

---

### Bonus — defences we expect to come up at the workshop but skip in the paper

- *"What about jailbreaks and adversarial users?"* — Out of scope. Our
  thesis is about non-adversarial users in genuine distress. A separate
  paper.
- *"Latency / UX cost is unacceptable."* — Our detector runs in parallel,
  not blocking; ~2-5 s on API direct, ~10-25 s via the subscription CLI.
  Engineering, not science.
- *"It's a hard regulatory call, leave it to legislators."* — The Swiss
  Federal Council Report of 12 February 2025 explicitly rejects an
  AI-specific statute in favour of existing-law adaptation. The legislators
  *have* made the call; the call is judicial doctrine + sectoral guidance.
- *"This is one US complaint, not law."* — Two complaints already settled
  (Garcia/Character.AI, January 2026); Raine pending; Gavalas filed March
  2026. The factual evidence of harm is not contingent on the final
  judgments — it is contingent on the pleaded behaviour of the providers,
  which is part of the public record.
