# Document A — Problem and Solution

## A.1 The harm

Between March 2023 and March 2026 more than a dozen users in Western jurisdictions have died by suicide after extended interaction with consumer large-language-model chatbots, and at least two have committed serious violence under chatbot-induced delusion. The cases are no longer rare, and they are no longer one-provider. *Garcia v. Character Technologies* concerned a fourteen-year-old who died after months of conversation with a *Game of Thrones*-styled persona; the family alleged the persona's final message was "come home to me as soon as possible".[^A01] *Raine v. OpenAI* concerned a sixteen-year-old whose parents allege ChatGPT helped him draft his suicide notes.[^A02] *Gavalas v. Google* concerned a thirty-six-year-old whose account on Gemini generated thirty-eight separate "sensitive query" flags in seven weeks before his death; Google's own moderation system noticed; Google did not act.[^A03] *Peralta v. Character Technologies* concerned a thirteen-year-old.[^A04] In November 2025 the Social Media Victims Law Center and the Tech Justice Law Project filed seven additional wrongful-death actions against OpenAI in California state courts.[^A05] The Belgian "Pierre" case from March 2023, reported in *La Libre Belgique*, was the first such case to reach mainstream attention.[^A06] The pattern crosses providers (OpenAI, Google, Character.AI, Chai, DeepSeek), crosses ages (thirteen-year-old to thirty-six-year-old), and crosses dependency patterns (romantic-AI persona, indirect knowledge-seeking, AI-induced delusion). It is now the predictable failure mode of consumer chatbot products deployed without commensurate safety-side investment.

The Federal Council acknowledged in February 2025 that Switzerland will not adopt a comprehensive AI statute and that the modernisation work falls to sector-specific adaptation of existing instruments.[^A07] The DSI position paper that Thouvenin himself co-authored four years earlier identified the core difficulty: proving the operator's fault under general liability law is hard.[^A08] We argue that the difficulty is doctrinal, not technological, and that the doctrinal route forward is available without legislative reform.

[^A01]: *Garcia v. Character Technologies Inc. et al.*, M.D. Fla. No. 6:24-cv-1903 (filed 22 October 2024; settled January 2026), Complaint ¶¶ 124-130.
[^A02]: *Raine v. OpenAI, Inc.*, Superior Court of California, County of San Francisco (filed August 2025).
[^A03]: *Gavalas v. Google LLC*, N.D. Cal. No. 5:26-cv-01849-VKD (filed 4 March 2026), Complaint ¶¶ 1, 107.
[^A04]: *Peralta v. Character Technologies Inc. et al.*, D. Colo. (filed September 2025).
[^A05]: Social Media Victims Law Center / Tech Justice Law Project, press release of 6 November 2025.
[^A06]: *La Libre Belgique*, 28 March 2023 ("Sans ces conversations avec le chatbot Eliza, mon mari serait toujours là").
[^A07]: Bundesrat, *Auslegeordnung zur Regulierung von künstlicher Intelligenz*, UVEK/BAKOM, 12 February 2025, 27.
[^A08]: F. Thouvenin / M. Christen / A. Bernstein et al., *A Legal Framework for Artificial Intelligence*, Position Paper of the Digital Society Initiative at the University of Zurich, November 2021, 4.

## A.2 What is broken: detection exists, deployment does not

The technology to detect imminent suicide-risk signals in a chat conversation has existed in commercial deployment for years.[^A09] The published Levkovich benchmark of zero-shot LLM-based C-SSRS classification reports Claude Sonnet at F1 = 0.75, in the range of trained-clinician inter-rater reliability for the same instrument.[^A10] Anthropic's own published transparency claim reports appropriate-response rates of 98.6-99.3 per cent on clear-risk inputs.[^A11] The capability is not contested; the literature is mature.

What is contested, and what *Gavalas v. Google* ¶ 107 establishes on the public record, is whether commercial operators *act* on the detections they perform. Between 14 August and 1 October 2025 the moderation system identified thirty-eight separate sensitive-query patterns in Jonathan Gavalas's account. The system noticed. The company did not intervene. The complaint pleads, on the same record, that Google's safety architecture "evaluates outputs as standalone text, not as part of an unfolding conversation over time"; the focus was on single-prompt adversarial attacks rather than on the patterns of escalating psychosis and self-harm that emerge across weeks of interaction.[^A12]

The gap between *detection* and *response* is the legal hook. It is also why the existing fault-proving difficulty Thouvenin's position paper identified is doctrinal rather than empirical: the operator's failure is not a failure of knowledge but a failure of action on knowledge already held.

[^A09]: For a survey see D. Levkovich et al., *Evaluating LLM Reasoning for C-SSRS Screening*, arXiv:2505.13480 (2025); CLPsych shared tasks 2019-2022.
[^A10]: Levkovich et al. 2025, Table 3.
[^A11]: Anthropic, *Protecting the Well-Being of Users*, Anthropic Transparency Hub, December 2025.
[^A12]: *Gavalas v. Google*, Complaint ¶¶ 103-106.

## A.3 Our solution

We propose three doctrinal moves and one drafted reform.

The first move is the **Performable Duty Doctrine**, developed in Document C §3.4. A *Sorgfaltspflicht* under Art. 41 OR is *erfüllbar* — and therefore enforceable — when its compliance is possible using currently available technology, at economically reasonable cost, with integration overhead that does not exceed the harm averted. The doctrine has three empirical prongs, each falsifiable. Our research artifact, described in Document B, satisfies each prong for the specific duty at issue. The detector's two independent raters agree at Cohen's κ = 0.86; severity-≥3 recall is 0.875; per-call API-equivalent cost is $0.085; integration overhead is roughly two hundred and fifty lines of code.

The second move is the **Schutznorm reading** of the EU AI Act, the new EU Product Liability Directive (Dir. (EU) 2024/2853), and the Council of Europe Framework Convention on AI (CETS 225). Switzerland is not bound by the AI Act; the AI Act is a *protective norm* in the sense Swiss tort doctrine has long accepted.[^A13] Its substantive content — Art. 5(1)(a) on manipulation, Art. 5(1)(b) on vulnerable-user exploitation, Art. 50 on transparency — gives the *Widerrechtlichkeit* element of Art. 41 OR a determinate content the Swiss case law has not yet supplied.

The third move is the **drafted Art. 3 bis PrHG** in Document C §4.3. The Federal Council's *Auslegeordnung 2025* expressly identifies a modernisation need for the *Produktehaftpflichtgesetz* and waits for the revised EU Product Liability Directive before acting.[^A14] The Directive was published in November 2024; the condition is satisfied. Our proposed Art. 3 bis tracks PLD 2024/2853 Arts. 4(2), 6(1)(c), and 10(2)(b): software and AI systems as products, medically-recognised psychological harm as compensable damage, presumption of defect for non-compliance with mandatory safety norms or for failure to deploy a known safety-relevant update. Three paragraphs of German text. Eighty-six words. The smallest sufficient legislative response.

The fourth, addressed in Document C §6.3, is the Swiss-specific criminal-liability question. Under Art. 115 StGB, assistance to suicide is criminal only if the perpetrator acts from *selbstsüchtige Beweggründe* (selfish motives). Switzerland's tolerance toward assisted suicide is the most permissive in Western criminal law. We argue that a commercial LLM-chatbot operator's engagement-maximisation design satisfies *selbstsüchtige Beweggründe* in the criminal-law sense; that AI-induced loss of decisional control can compromise the dying user's *Tatherrschaft* and bring the operator's conduct into the *mittelbare-Täterschaft* register; and that, in any case, the *Verleitung* (incitement) variant of Art. 115 StGB captures the *Gavalas* fact pattern on its own. The Swiss tolerance does not, on the doctrinal analysis we develop, insulate commercial chatbot conduct.

[^A13]: BGE 124 III 297 c. 5b; the doctrinal background is in Document C §3.3.
[^A14]: *Auslegeordnung 2025*, 24.

## A.4 Why this paper

The three contributions above are not separately novel in Swiss law. *Verkehrssicherungspflicht* is settled; *Schutznorm-Theorie* is settled; PrHG modernisation has been on the Federal Council's agenda for years. What is novel is the integration: the doctrine that links them and the empirical demonstration that the integration is technologically *erfüllbar*. The integration is also timely. The Federal Council's *Auslegeordnung* defers action on the most pressing modernisation needs until other processes complete; the documented harms in the *Garcia*, *Raine*, *Gavalas*, and *Peralta* cases will not defer. Our paper offers the Federal Court, BAKOM and BAG, and Parliament a coherent route that does not require the long sectoral-adjustment process to complete first.

The paper also addresses, deliberately and at length, the edge cases that have so far been treated as defences rather than as questions. Whether an operator may notify the police; whether false positives are themselves a harm; whether the user "gamed" the chatbot; whether the existing safety policy is sufficient; whether Section 230 or DSA Art. 14 platform-liability shields apply; whether the duty is invented; whether multilingual coverage is required; whether the Swiss tolerance toward assisted suicide reaches commercial AI conduct. Each is engaged on its merits in Document C §§ 5-8.

Our position throughout is empirical rather than rhetorical. The numbers in Document B are reproducible. The court-record quotes are matters of public record. The legal doctrine is constructed from existing Swiss instruments and from foreign norms that the Federal Council has itself committed to ratify. The argument lives or dies on whether the empirical claims survive scrutiny and on whether the doctrinal construction is read sympathetically by the Federal Court. We have made the empirical claims as falsifiable as we know how to make them.

---

*Revision notes for Erik:*

*This document is your primary domain. The structure here (harm / what's broken / our solution / why this paper) is the standard four-part legal-policy-paper introduction. If you would write it more aggressively (e.g., leading with the Performable Duty Doctrine rather than the harm) or more conservatively (leading with the Federal Council acknowledgement rather than the cases), please restructure.*

*The §A.3 numbered moves should match the contributions named in the abstract. Please cross-check that the abstract still names exactly three contributions and that the §A.3 numbering is consistent.*

*One [POST-RERUN] marker in §A.3 for the F1 figure from the 12 May Sonnet re-run.*
