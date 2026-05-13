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
