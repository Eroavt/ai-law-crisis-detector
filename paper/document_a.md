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
