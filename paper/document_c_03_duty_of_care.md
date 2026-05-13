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
