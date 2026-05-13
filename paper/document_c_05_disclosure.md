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
