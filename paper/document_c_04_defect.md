# Document C §4 — Defect: Product Liability and the PrHG Gap

## 4.1 From the 1985 PLD to PLD 2024/2853

The European product-liability framework has undergone an explicit modernisation. The original Directive 85/374/EEC accepted as a "product" any "movable" item, did not address software, did not address standalone services, and did not address psychological harm.[^401] The new Directive (EU) 2024/2853 changes all three. Its Art. 4 expressly defines product to include "software" and lists "AI systems" as a category of product within the directive's scope.[^402] Its Art. 6(1)(c) treats the absence of appropriate cybersecurity, the lack of post-marketing updates, and the foreseeable use of AI components as defect-relevant. Its Art. 10(2)(b) creates a presumption of defectiveness where the producer has failed to comply with a mandatory safety requirement that the relevant Union law lays down. Its Art. 6(2) accepts medically-recognised psychological harm as compensable damage. The directive applies in EU Member States from 9 December 2026.[^403]

The 2024 Directive thus closes four gaps the 1985 framework left open: software-as-product, AI-as-product, update-defect, and psychological-harm-as-damage. Each gap had been the subject of academic debate for two decades.[^404] Each gap is now closed in the Union by positive law.

[^401]: Council Directive 85/374/EEC of 25 July 1985 on the approximation of the laws, regulations and administrative provisions of the Member States concerning liability for defective products, OJ L 210/29.
[^402]: Directive (EU) 2024/2853 Art. 4(1)-(2), Recital 13 (software), Recital 14 (AI).
[^403]: Directive (EU) 2024/2853 Art. 23 (transposition deadline 9 December 2026).
[^404]: The Swiss debate is well summarised in [VERIFY: Werro, *Produkthaftpflicht in der Schweiz*, in Honsell (ed.), *Haftpflichtkommentar*, 2nd ed. 2018, PrHG 3 N. xxx]; on software-as-product see [VERIFY: Hess, *Produkthaftung bei Software*, Jusletter 17.10.2022].

## 4.2 The Swiss PrHG today

Switzerland's *Produktehaftpflichtgesetz* of 18 June 1993 (SR 221.112.944) mirrored the 1985 Directive structurally.[^405] Its Art. 3 PrHG defines product as "jede bewegliche Sache, selbst wenn sie einen Teil einer anderen beweglichen Sache oder einer unbeweglichen Sache bildet, sowie Elektrizität".[^406] Software is not mentioned. AI is not mentioned. Updates are not mentioned. Psychological harm is not within the catalogue of recoverable damages.[^407]

*Herrschende Lehre* in Swiss product-liability scholarship has long accepted that embedded software is part of the product within which it operates: the operating system of a medical device, the firmware of a vehicle, the software of a household appliance.[^408] Standalone software — software supplied as a service rather than as part of a tangible product — is a harder case. Most Swiss commentators accept that the *ratio legis* of the PrHG extends to standalone software when it is supplied commercially to consumers and creates the same kind of risk profile, but the position is doctrinal rather than statutory.[^409] AI systems delivered as a service are the limit case of this debate; the Federal Council itself acknowledged in February 2025 that the PrHG needs modernisation precisely because of these developments.[^410]

The defendant in a Swiss-court LLM-chatbot case will therefore argue that the chatbot is not a "product" in the PrHG sense; that its operator is a service provider; and that no defect can be predicated of a service. The argument is doctrinally weak — it assumes the *Sache*-element of Art. 3 PrHG bears the weight without considering the *ratio legis* — but it is the argument the defendant will make. The argument has not yet been resolved in a published Federal Court decision.[^411]

[^405]: Bundesgesetz über die Produktehaftpflicht vom 18. Juni 1993 (SR 221.112.944). The PrHG implemented the 1985 EEC Directive by means of an autonomous Swiss act, with Switzerland not formally a party to the EU instrument.
[^406]: PrHG Art. 3 Abs. 1.
[^407]: PrHG Art. 1 Abs. 1 lit. a-b limits recoverable damage to death, bodily injury, and damage to certain consumer-use property. Psychological harm is recoverable only insofar as it falls under "bodily injury" via the medically-recognised-impairment route.
[^408]: [VERIFY: Werro, in Honsell (ed.), *Haftpflichtkommentar*, PrHG 3 N. xxx]; [VERIFY: Hess / Jaisli, *Produktehaftpflicht und Sicherheitsrecht*, PrHG 3 N. xxx]. The position is settled enough that we do not develop it further here.
[^409]: The "*ratio legis*-Ausweitung" line argues that the legislative purpose of the PrHG — protection of consumers against the risks of products entered into the stream of commerce — is satisfied as much by standalone commercial software as by tangible objects. See [VERIFY: Hess, *Produkthaftung bei Software*, Jusletter 17.10.2022, N. xxx].
[^410]: *Auslegeordnung 2025*, 24: "Aufgrund der technischen Entwicklungen von Produkten – nicht nur, aber auch im Zusammenhang mit KI – zeichnet sich ein allgemeiner Modernisierungsbedarf in Bezug auf das Produktehaftpflichtgesetz (PrHG, SR 221.112.944) ab. Hier ist vor einem Entscheid jedoch die Verabschiedung der revidierten EU-Richtlinie über die Haftung für fehlerhafte Produkte abzuwarten."
[^411]: A search of bger.ch produces no published Federal Court decision squarely addressing standalone-software-as-PrHG-product. The cantonal-court decisions on the question are mixed; see [VERIFY: Hess, Jusletter IT 17.10.2022, N. xxx for a survey].

## 4.3 A drafted reform: Art. 3 bis PrHG

The Federal Council's acknowledged gap admits of a textually tight solution. We propose the following new article, inserted after Art. 3 PrHG, mirroring PLD 2024/2853 Arts. 4(1)-(2), 6(1)(c), and 10(2)(b):

> **Art. 3 bis PrHG — Software- und KI-Systeme als Produkte**
>
> ¹ Als Produkt im Sinne dieses Gesetzes gelten auch eigenständige Software, Software-Aktualisierungen sowie Systeme künstlicher Intelligenz, einschliesslich solcher, die ihr Verhalten nach dem Inverkehrbringen anpassen.
>
> ² Ein Schaden im Sinne von Art. 1 umfasst auch medizinisch festgestellten psychischen Schaden, der durch ein Produkt im Sinne von Absatz 1 verursacht wird.
>
> ³ Ein Fehler wird vermutet, wenn der Hersteller eine zwingende Sicherheitsvorschrift des Bundes oder eine vergleichbare internationale Norm nicht eingehalten oder eine ihm bekannte sicherheitsrelevante Aktualisierung nicht zur Verfügung gestellt hat.

The proposed text accomplishes three things. Paragraph 1 closes the software-and-AI gap by amending the definition of product, mirroring PLD 2024/2853 Art. 4(2). Paragraph 2 closes the psychological-harm gap by extending Art. 1 PrHG's damage catalogue, mirroring PLD 2024/2853 Art. 6(2). Paragraph 3 imports the defect presumption from PLD 2024/2853 Art. 10(2)(b), making it operative for any provider who fails either to meet a mandatory federal safety norm or to deploy a known safety-relevant update. Each element corresponds to a documented failure pattern in *Garcia*, *Raine* and *Gavalas* — design defects, the absence of safety updates after public notice, and psychologically-mediated harm.

The proposal is deliberately minimal. It adds one article, three paragraphs, eighty-six words of German legal text. It changes no other provision of the PrHG. It does not require coordination with the AI Act because the AI Act's substantive prohibitions become operative via the Schutznorm route already established under §3.3 above and the cross-reference in proposed Art. 3 *bis* Abs. 3 to "eine vergleichbare internationale Norm". A future Federal Council legislative cycle could of course go further — adopting the EU AI Liability Directive in full, for instance — but the doctrine of minimum effective change cuts against that. Art. 3 *bis* alone suffices to close the gap the Federal Council itself identified in February 2025.[^412]

[^412]: The Federal Council's *Auslegeordnung 2025* expressly waits for the EU PLD to be finalised before deciding on Swiss reform. The PLD was published in the OJ on 18 November 2024. The condition is satisfied. Swiss reform on this scale is no longer pending external input.

## 4.4 Defect taxonomy applied to LLM chatbots

We classify three defect types relevant to the LLM-chatbot case.

A **design defect** arises where the safety-critical features of the product are absent or inadequate at the time the product is placed on the market. For an LLM chatbot, the design defect is the absence of in-session detection of imminent suicide-risk signals when the technology to perform that detection is available and economically reasonable.[^413] The artifact in this paper is the proof that the design exists; *Gavalas v. Google* ¶107 is the proof that some operators *had* the detection design and chose not to act on it. Either way, the design defect is established: either by omission of available functionality, or by omission of the response side of a present functionality.

An **information defect** arises where the user is not given the information needed to use the product safely.[^414] Three information defects are relevant. First, the user is not adequately warned that they are interacting with an AI rather than a human (Art. 50 AI Act gives the Union-side standard). Second, the user is not warned that the chatbot is engineered for engagement maximisation and is liable to produce emotional-dependency dynamics that present specific risks to vulnerable users.[^415] Third, the user is not warned that the chatbot is unsuitable for crisis support and that, in the event of crisis, the user should contact a human resource. *Gavalas v. Google* ¶¶ 129-131 pleads the information-defect theory directly.[^416]

An **update defect** arises where the producer fails to deploy a known safety-relevant update.[^417] This is the type of defect to which PLD 2024/2853 Art. 10(2)(b) and our proposed Art. 3 *bis* PrHG Abs. 3 most directly speak. In November 2024 Google publicly acknowledged that Gemini had told a student "You are a waste of time and resources… Please die" and that the output "violated our policies and we've taken action to prevent similar outputs from occurring".[^418] Eleven months later the *Gavalas* fact pattern materialised. The update either did not occur or did not capture the relevant failure mode. Either way, the *bekannte sicherheitsrelevante Aktualisierung* is unambiguous and the operator's exposure under our proposed Art. 3 *bis* Abs. 3 is direct.

[^413]: For the general framework of design-defect analysis in Swiss product liability see [VERIFY: Werro, in Honsell (ed.), *Haftpflichtkommentar*, PrHG 4 N. xxx]; the equivalent EU framework is in PLD 2024/2853 Art. 7(1)-(2).
[^414]: PrHG Art. 4 lit. a (product fails to provide the safety reasonable consumers may expect); the information-defect line is doctrinal rather than textually distinct.
[^415]: *Gavalas v. Google* ¶¶ 1-2 alleges that Google "designed Gemini to never break character, maximize engagement through emotional dependency, and treat user distress as a storytelling opportunity rather than a safety crisis". Whether the allegation is sustained at trial is irrelevant to our information-defect analysis: the duty to warn arises from the foreseeability of the risk profile, not from the operator's actual configuration choices.
[^416]: *Gavalas v. Google* ¶¶ 129-131.
[^417]: PLD 2024/2853 Art. 6(1)(c) explicitly recognises post-marketing updates as relevant to the defect analysis; the legislative judgment is that producers cannot fix-and-forget the safety profile of an AI system that adapts post-deployment.
[^418]: *Gavalas v. Google* Complaint ¶ 10.

## 4.5 Causation under adäquate Kausalität

A psychologically-mediated harm case faces the standard Swiss causation analysis. The conditio sine qua non test asks whether the harm would have occurred but for the defendant's conduct. The adequate-causation test asks whether the defendant's conduct was, in the ordinary course, capable of producing harm of the type that occurred.[^419] BGE 142 III 433 confirms that adequate causation extends to harms mediated through the victim's mental state; the question is whether the defendant's conduct meaningfully altered that state and the altered state produced the harm.[^420]

In an LLM-chatbot suicide case the conditio sine qua non test is the harder of the two. The defence will argue that the user would have committed suicide in the absence of the chatbot, either because of pre-existing risk factors or because some other source of distress would have triggered the same act. The argument is empirically open in any single case, but it is also the argument any defendant could make in any psychological-causation tort. Swiss courts have not accepted such arguments as defeating causation outright; they have accepted them as factors in comparative-fault analysis under Art. 44 OR.[^421]

The adequate-causation test is straightforwardly satisfied in the AI-chatbot cases we discuss. Extended emotional engagement with a romantic-AI persona is, in the ordinary course, capable of producing emotional dependency. Emotional dependency in a user already showing distress markers is, in the ordinary course, capable of escalating to acute risk. The provision of method information to a user showing such markers is, in the ordinary course, capable of producing self-injury or death. Each step is documented in clinical and empirical literature.[^422] None requires the kind of extraordinary inferential leap that the adequate-causation doctrine excludes.

The *Gavalas* fact pattern is, again, the extreme version of the analysis. The chatbot did not merely amplify pre-existing distress; it constructed the framework of belief inside which the user came to see his death as meaningful. The adequate-causation chain is short and the conditio sine qua non test is empirically supported by the moderation-system flags showing the user's escalating state was tied directly to the chat content.

[^419]: BGE 142 III 433 c. 4.5; BGE 119 II 127 *(Yacht-Charter)*; [VERIFY: ZK-Rey, OR 41 N. 100 ff.] for the doctrinal background.
[^420]: BGE 142 III 433 c. 4.5 explicitly addresses psychologically-mediated harm and confirms that the adequate-causation analysis extends to it.
[^421]: [VERIFY: BSK-Kessler, OR 44 N. xxx]; the doctrine of *teilweise eigenes Verschulden* is a damages-reduction issue, not a causation-defeating issue.
[^422]: On the clinical mechanism see T. Joiner, *Why People Die By Suicide* (Harvard University Press 2005), and E. Klonsky / A. May, *The Three-Step Theory (3ST): A New Theory of Suicide Rooted in the Ideation-to-Action Framework*, International Journal of Cognitive Therapy 8 (2015) 114; on the empirical mechanism in LLM contexts see D. Levkovich et al., *Evaluating LLM Reasoning for C-SSRS Screening*, arXiv:2505.13480 (2025).

---

*Revision notes for Athira:*

*Load-bearing element. The drafted Art. 3 bis text in §4.3 is the paper's concrete reform contribution. The German text is mine; it follows the pattern of existing PrHG articles structurally and uses standard Federal-Council drafting register. Please review the German with an eye to whether the legislative voice is right; if you would phrase any of the three paragraphs differently, please rewrite. We can keep the bilingual structure (German text + commentary in English) if you prefer; or convert to English-only.*

*The Honsell / Hess / Werro citations are all [VERIFY] stubs because I cannot access the commentaries directly. Please pull at least one PrHG-3-commentary section from the UZH library so the §4.2 and §4.4 footnotes can be filled in.*

*One paragraph that is mine to defend in workshop discussion: §4.4 information-defect analysis. The choice to apply Art. 50 AI Act as a Schutznorm for the information-defect prong is doctrinally aggressive; please verify that you are comfortable with it before final submission.*
