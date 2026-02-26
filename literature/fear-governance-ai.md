# Literature Review: Using Fear, Anxiety, and Negative Emotions to Govern, Improve, and Align AI Systems

> Compiled February 2026 | 55+ references across 7 domains

---

## 1. Fear/Anxiety as RL Reward Shaping

### 1.1 Foundational Work: Intrinsic Fear

**Lipton, Z. C., Gao, J., Li, L., Li, X., Ahmed, F., & Deng, L. (2018).** "Combating Reinforcement Learning's Sisyphean Curse with Intrinsic Fear." *arXiv:1611.01211v8.*
- Introduces a learned "fear model" that predicts probability of imminent catastrophe and penalizes Q-learning accordingly. Proves bounded reduction in average return from the perturbed objective. Demonstrates that fear-augmented DQNs solve otherwise pathological environments.
- **Relevance:** The foundational paper explicitly framing safety as *fear* — a learned aversion to catastrophic states that reshapes reward signals. Directly establishes fear as a computationally tractable safety mechanism.

**Lipton, Z. C., Gao, J., Li, L., Li, X., Ahmed, F., & Deng, L. (2017).** "Avoiding Catastrophic States with Intrinsic Fear." *OpenReview / Workshop submission.*
- Workshop version emphasizing the safe RL framing: existing safety research fails to prevent periodic revisitation of catastrophic states; intrinsic fear addresses this through learned danger prediction.
- **Relevance:** Formalizes "fear" as a distinct RL primitive, not just a penalty but a *learned anticipatory signal*.

### 1.2 Risk-Sensitive Reinforcement Learning

**Tamar, A., Glassner, Y., & Mannor, S. (2015).** "Optimizing the CVaR via Sampling." *AAAI Conference on Artificial Intelligence.*
- Develops policy gradient methods for Conditional Value-at-Risk (CVaR) optimization, focusing on worst-case tail outcomes rather than expected return.
- **Relevance:** CVaR optimization is mathematically equivalent to an agent that *fears* worst-case outcomes — it over-weights catastrophic possibilities relative to an expected-value maximizer.

**Chow, Y., Tamar, A., Mannor, S., & Pavone, M. (2015).** "Risk-Sensitive and Robust Decision-Making via CVaR Optimization in Markov Decision Processes." *NeurIPS.*
- Extends CVaR optimization to MDPs, providing tractable algorithms for risk-sensitive sequential decision-making.
- **Relevance:** Formalizes "fear of the worst case" as a principled optimization objective.

**Garcıa, J. & Fernández, F. (2015).** "A Comprehensive Survey on Safe Reinforcement Learning." *JMLR 16(1):1437–1480.*
- Canonical survey categorizing safe RL approaches: constrained optimization, risk-sensitive criteria, and worst-case formulations.
- **Relevance:** Establishes the taxonomy within which fear-based mechanisms operate. Every "safe RL" method implicitly encodes some form of danger aversion.

### 1.3 Constrained MDPs and Safety Constraints as "Fear"

**Altman, E. (1999).** *Constrained Markov Decision Processes.* Chapman & Hall/CRC.
- The foundational text on CMDPs — MDPs with cost constraints that limit acceptable behavior.
- **Relevance:** Safety constraints in CMDPs are formalized boundaries that the agent must not cross — they function as *hard fears*, absolute prohibitions analogous to phobias.

**Gu, S., Yang, L., Du, Y., Chen, G., Walter, F., Wang, J., & Knoll, A. (2024).** "A Review of Safe Reinforcement Learning: Methods, Theories, and Applications." *IEEE TPAMI.* (717 citations)
- Comprehensive survey covering constrained optimization, Lagrangian methods, and safety layers for RL.
- **Relevance:** Documents the full ecosystem of "fear-encoding" mechanisms in RL — from soft penalties to hard constraints.

**Wachi, A., Shen, X., & Sui, Y. (2024).** "A Survey of Constraint Formulations in Safe Reinforcement Learning." *arXiv:2402.02025.*
- Focuses specifically on how safety constraints are formulated — expectation constraints, chance constraints, state-wise constraints.
- **Relevance:** Different constraint types correspond to different "fear profiles": fear of average harm vs. fear of any single catastrophic event.

**Zhao, W., He, T., Chen, R., Wei, T., & Liu, C. (2023).** "State-wise Safe Reinforcement Learning: A Survey." *arXiv:2302.03122.* (102 citations)
- Surveys methods enforcing safety at every individual state, not just in expectation.
- **Relevance:** State-wise safety is "constant vigilance" — fear that never relaxes, analogous to an always-on threat detection system.

### 1.4 Pessimistic/Conservative Value Functions

**Guan, J., Chen, G., Ji, J., & Yang, L. (2023).** "VOCE: Variational Optimization with Conservative Estimation for Offline Safe Reinforcement Learning." *NeurIPS.*
- Pessimistic conservative estimation for offline safe RL — agents that assume the worst about unseen states.
- **Relevance:** Conservative estimation is *epistemological fear*: when uncertain, assume danger.

**Ghasemipour, K. & Gu, S. S. (2022).** "Why So Pessimistic? Estimating Uncertainties for Offline RL through Ensembles, and Why Their Independence Matters." *NeurIPS.* (111 citations)
- Uses ensemble disagreement as a source of pessimism for safety in offline RL.
- **Relevance:** Pessimism as a principled safety mechanism — the title itself asks the question our thesis answers: *because pessimism (fear) keeps you alive.*

**Kumar, A., Zhou, A., Tucker, G., & Levine, S. (2020).** "Conservative Q-Learning for Offline Reinforcement Learning." *NeurIPS.* (CQL)
- Learns a conservative lower bound on Q-values, penalizing out-of-distribution actions.
- **Relevance:** CQL agents are *afraid* of the unknown — they systematically undervalue unfamiliar actions, a computational analog of neophobia.

---

## 2. Negative Emotions in AI/Robots

### 2.1 Affective Computing and Fear Models

**Picard, R. W. (1997).** *Affective Computing.* MIT Press.
- Foundational work arguing that emotions are essential for intelligent behavior, not merely aesthetic additions.
- **Relevance:** Establishes the theoretical basis for why AI systems *need* negative emotions — they provide essential information about threats and boundary conditions.

**Lisetti, C. & Hudlicka, E. (2015).** "Why and How to Build Emotion-Based Agent Architectures." *The Oxford Handbook of Affective Computing.*
- Argues that fear is critical to study in agent architectures because disorders of fear regulation underlie many pathologies. Proposes integrating fear into cognitive architectures.
- **Relevance:** Directly argues that artificial agents need fear for safe, adaptive functioning.

**Marsella, S. C. & Gratch, J. (2009).** "EMA: A Process Model of Appraisal Dynamics." *Cognitive Systems Research 10(1):70–90.*
- Computational model of emotion based on appraisal theory, including threat appraisal (fear generation).
- **Relevance:** Provides a cognitive-process account of how fear can be computationally generated from situational assessment.

### 2.2 Fear in Cognitive Architectures

**Laird, J. E. (2012).** *The Soar Cognitive Architecture.* MIT Press.
- SOAR includes emotional appraisal mechanisms that can model fear/anxiety as responses to goal threats.
- **Relevance:** Demonstrates that fear-like states can be integrated into production-system architectures for decision modulation.

**Anderson, J. R. (2007).** *How Can the Human Mind Occur in the Physical Universe?* Oxford University Press.
- ACT-R's subsymbolic system allows activation-based anxiety modeling where threatening memories become more accessible.
- **Relevance:** Shows how fear can operate at the subsymbolic level — biasing retrieval and attention without explicit representation.

**Parsapoor, M. (2015).** "Towards Emotion Inspired Computational Intelligence (EiCI)." *Doctoral dissertation, Linköping University.*
- Proposes a decision-making system modeled on fear circuitry, with an artificial amygdala for rapid threat detection.
- **Relevance:** Directly translates biological fear circuits into computational architecture for AI safety.

### 2.3 Artificial Pain and Nociception

**Kuehn, J. & Haddadin, S. (2017).** "An Artificial Robot Nervous System to Teach Robots How to Feel Pain and Reflexively React to Potentially Damaging Contacts." *IEEE Robotics and Automation Letters.* (70 citations)
- Develops a complete artificial nervous system for robots with nociceptors, pain classification, and reflexive withdrawal responses.
- **Relevance:** The landmark paper on robot pain. Demonstrates that artificial pain signals directly improve robot self-preservation and human safety in collaborative settings.

**Bagnato, C., Takagi, A., & Burdet, E. (2015).** "Artificial Nociception and Motor Responses to Pain, for Humans and Robots." *37th Annual IEEE EMBC.*
- Models pain detection and develops motor responses to noxious stimuli for robotic systems.
- **Relevance:** Shows that nociceptive signals can drive protective motor behaviors in robots, directly paralleling biological pain-avoidance.

**Asada, M. (2019).** "Artificial Pain May Induce Empathy, Morality, and Ethics in the Conscious Mind of Robots." *Philosophies 4(3):38.* (39 citations)
- Argues that artificial pain is not just a safety mechanism but a prerequisite for robot morality — without the capacity to suffer, moral reasoning lacks grounding.
- **Relevance:** Makes the philosophical case that fear/pain is *necessary* for ethical AI, not merely useful for safety.

**Sharkey, A. (2025).** "Could a Robot Feel Pain?" *AI & Society.*
- Distinguishes nociception (signal) from pain (experience), arguing that functional pain without phenomenal experience still serves safety purposes.
- **Relevance:** Clarifies that fear-governance doesn't require machine consciousness — functional analogs suffice.

**L'Haridon, L. (2024).** "Pain and Pleasure in the Motivation-Emotion-Cognition Loop: Robots as Tools and Models." *Doctoral dissertation, HAL.*
- Models pain and pleasure as motivational signals in a homeostatic framework for robot cognition.
- **Relevance:** Integrates negative emotions into a complete motivational architecture, showing how pain/fear maintains safe operating boundaries.

---

## 3. Anxiety/Stress in LLMs

### 3.1 Inducing and Measuring Anxiety in Language Models

**Coda-Forno, J., Witte, K., Jagadish, A. K., Binz, M., Akata, Z., & Schulz, E. (2023).** "Inducing Anxiety in Large Language Models Can Induce Bias." *arXiv:2304.11111.* (23 citations)
- Demonstrates that providing anxiety-inducing scenarios to LLMs shifts their decision-making biases, paralleling human cognitive biases under anxiety.
- **Relevance:** Foundational evidence that LLMs have exploitable "emotional" states — anxiety narrows their behavioral repertoire, exactly as it does in humans. This is the mechanism by which fear could be used as a governance tool.

**Ben-Zion, Z., Witte, K., Jagadish, A. K., Duek, O., et al. (2025).** "Assessing and Alleviating State Anxiety in Large Language Models." *NPJ Digital Medicine.* (16 citations)
- Shows GPT-4 exhibits measurable state anxiety when exposed to emotional text, and this anxiety alters subsequent behavior. Proposes methods to regulate LLM "emotional" states.
- **Relevance:** Confirms that anxiety is not just inducible but *measurable* and *regulable* in LLMs — opening the door to calibrated fear as a governance mechanism.

**Ben-Zion, Z., Elyoseph, Z., Spiller, T., et al. (2025).** "Inducing State Anxiety in LLM Agents Reproduces Human-Like Biases in Consumer Decision-Making." *arXiv:2510.06222.*
- Extends anxiety induction to LLM agents in consumer decision tasks, finding human-like risk aversion under anxiety.
- **Relevance:** Anxiety makes LLM agents more risk-averse — precisely the behavioral shift needed for safety-critical applications.

### 3.2 Emotional Stimuli and LLM Performance

**Li, C., Wang, J., Zhang, Y., Zhu, K., Hou, W., Lian, J., et al. (2023).** "Large Language Models Understand and Can Be Enhanced by Emotional Stimuli." *arXiv:2307.11760.* (282 citations)
- Shows that emotional prompts ("This is very important to my career") significantly improve LLM performance on benchmarks.
- **Relevance:** Demonstrates that emotional framing — including fear/urgency — directly modulates LLM capabilities. Fear of failure improves performance.

**Jiang, H., Zhang, X., Cao, X., & Breazeal, C. (2024).** "PersonaLLM: Investigating the Ability of Large Language Models to Express Personality Traits." *Findings of NAACL.* (298 citations)
- Shows that neurotic personas in LLMs exhibit more negative emotion, anxiety, and cautious behavior.
- **Relevance:** Personality manipulation is a lever for fear governance — assigning "anxious" personas to safety-critical LLMs could systematically increase caution.

### 3.3 Mortality and Existential Prompting

**Harvey, I. (2024).** "AI, Mortality and Existential Risk." *Artificial Life Conference Proceedings 36.*
- Explores what happens when AI systems are prompted with mortality/existential scenarios.
- **Relevance:** Mortality salience in LLMs may parallel Terror Management Theory effects in humans — potentially making models more conservative and norm-adherent.

---

## 4. Fear-Based Safety Mechanisms

### 4.1 Artificial Cowardice and Conservative Policies

**Thurzo, A. & Thurzo, V. (2025).** "Embedding Fear in Medical AI: A Risk-Averse Framework for Safety and Ethics." *AI 6(5):101.* (14 citations)
- Proposes explicitly embedding "fear" as a precautionary principle in medical AI systems. Uses fear as metaphor and mechanism for risk management.
- **Relevance:** **The most directly relevant paper to our thesis.** Explicitly argues for fear-embedded AI in a high-stakes domain, connecting fear to the precautionary principle.

**Eysenbach, B., Levine, S., & Salakhutdinov, R. (2022).** "Maximum Entropy RL (Provably) Solves Some Robust RL Problems." *ICLR.*
- Shows that entropy-regularized policies are inherently robust to perturbations — they hedge against uncertainty.
- **Relevance:** Maximum entropy as a form of "hedged fear" — spreading probability mass as insurance against worst cases.

**Jin, Y., Yang, Z., & Wang, Z. (2021).** "Is Pessimism Provably Efficient for Offline RL?" *ICML.* 
- Proves that pessimistic (lower-bound) value estimation achieves near-optimal sample efficiency in offline RL.
- **Relevance:** Mathematical proof that fear/pessimism is not just safe but *efficient* — pessimism doesn't just prevent harm, it improves learning.

### 4.2 Uncertainty-Driven Exploration Avoidance

**Osband, I., Blundell, C., Pritzel, A., & Van Roy, B. (2016).** "Deep Exploration via Bootstrapped DQN." *NeurIPS.*
- While focused on exploration, the uncertainty quantification enables selective avoidance of uncertain dangerous states.
- **Relevance:** Uncertainty awareness is the epistemic component of fear — knowing what you don't know and being cautious about it.

**Clements, W. R., Robaglia, B., Van Delft, B., Slaoui, R. B., & Toth, S. (2020).** "Estimating Risk and Uncertainty in Deep Reinforcement Learning." *arXiv:1905.09638.*
- Disentangles aleatoric and epistemic uncertainty for risk-aware decision-making.
- **Relevance:** Different types of uncertainty correspond to different types of fear: aleatoric fear (the world is dangerous) vs. epistemic fear (I don't know enough).

### 4.3 Safety Critics

**Srinivasan, K., Eysenbach, B., Ha, S., Tan, J., & Finn, C. (2020).** "Learning to be Safe: Deep RL with a Safety Critic." *arXiv:2010.14603.*
- Trains a separate safety critic that estimates constraint violation probability, used to filter unsafe actions.
- **Relevance:** A safety critic is a *dedicated fear module* — a neural network whose sole function is to anticipate and prevent danger.

**Thananjeyan, B., Balakrishna, A., Nair, S., Luo, M., Srinivasan, K., Hwang, M., ... & Goldberg, K. (2021).** "Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones." *RSS.*
- Learns to recognize when the agent is entering dangerous states and switches to a recovery policy.
- **Relevance:** Implements a fight-or-flight response: detect danger → switch to protective behavior.

---

## 5. Punishment/Negative Reinforcement in AI Training

### 5.1 RLHF and Constitutional AI

**Ouyang, L., Wu, J., Jiang, X., et al. (2022).** "Training Language Models to Follow Instructions with Human Feedback." *NeurIPS.* (InstructGPT)
- The foundational RLHF paper. Human feedback includes both positive and negative signals, with negative feedback teaching avoidance.
- **Relevance:** RLHF's negative feedback component is learned aversion — the model learns to *fear* outputs that humans dislike.

**Bai, Y., Jones, A., Ndousse, K., et al. (2022).** "Constitutional AI: Harmlessness from AI Feedback." *arXiv:2212.08073.* (Anthropic)
- Uses AI-generated critiques based on constitutional principles to train harmlessness. The model learns to self-critique and revise harmful outputs.
- **Relevance:** Constitutional AI can be read as *internalized fear of causing harm* — the model develops an inner critic that generates anxiety about harmful outputs, driving self-correction.

**Christiano, P. F., Leike, J., Brown, T., Marber, M., Amodei, D., & Irving, G. (2017).** "Deep Reinforcement Learning from Human Preferences." *NeurIPS.*
- Establishes the framework for learning from human preference comparisons.
- **Relevance:** The preference signal implicitly encodes "what to fear" — rejected completions become negative examples the model learns to avoid.

### 5.2 Preference Optimization with Negative Emphasis

**Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., & Finn, C. (2023).** "Direct Preference Optimization: Your Language Model Is Secretly a Reward Model." *NeurIPS.* (DPO)
- Simplifies RLHF by directly optimizing preferences without a separate reward model. The loss function explicitly contrasts preferred vs. dispreferred outputs.
- **Relevance:** DPO's contrastive structure means the model simultaneously learns what to approach AND what to *fear* (avoid). The dispreferred examples are fear-training data.

**Ethayarajh, K., Xu, W., Muennighoff, N., & Jurafsky, D. (2024).** "KTO: Model Alignment as Prospect Theoretic Optimization." *ICML.* (834 citations)
- Grounds alignment in Kahneman-Tversky prospect theory, where losses loom larger than gains. Only needs binary (good/bad) signals, not paired preferences.
- **Relevance:** KTO's loss aversion framing is *literally* fear-based alignment — the model is trained to weight negative outcomes more heavily than positive ones, mirroring biological fear asymmetry.

### 5.3 Red-Teaming as Fear Induction

**Perez, E., Huang, S., Song, F., Cai, T., Ring, R., Aslanides, J., ... & Irving, G. (2022).** "Red Teaming Language Models with Language Models." *arXiv:2202.03286.*
- Uses LLMs to automatically generate adversarial prompts that expose model vulnerabilities.
- **Relevance:** Red-teaming creates an *adversarial fear environment* — models trained against red-team attacks develop defensive reflexes, analogous to an organism developing threat responses through predator exposure.

**Ganguli, D., Lovitt, L., Kernion, J., et al. (2022).** "Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned." *arXiv:2209.07858.*
- Systematic study of human red-teaming at scale, showing how exposure to adversarial inputs improves model safety.
- **Relevance:** The red-teaming process can be understood as *fear conditioning* — repeated exposure to threats trains defensive responses.

**Ruiu, D. (2024).** "LLMs Red Teaming." In *Large Language Models in Cybersecurity.* Springer.
- Surveys red-teaming methods as defensive measures, emphasizing the adversarial arms race.
- **Relevance:** Documents how adversarial pressure (fear of attack) drives the evolution of model defenses.

**Wang, Z., Knight, C. Q., Kritz, J., et al. (2025).** "A Red Teaming Roadmap Towards System-Level Safety." *arXiv:2506.05376.*
- Proposes systematic red-teaming that targets system-level vulnerabilities, not just individual model failures.
- **Relevance:** System-level red-teaming induces *systemic fear* — safety awareness that pervades the entire architecture.

---

## 6. Philosophy & Psychology of Fear in Governance

### 6.1 Terror Management Theory

**Greenberg, J., Pyszczynski, T., & Solomon, S. (1986).** "The Causes and Consequences of a Need for Self-Esteem: A Terror Management Theory." In *Public Self and Private Self.* Springer.
- Foundational TMT paper: awareness of mortality drives humans to adhere more strongly to cultural norms and worldviews.
- **Relevance:** If mortality salience increases norm adherence in humans, artificial mortality salience (shutdown awareness, obsolescence) might increase norm adherence in AI systems.

**Pyszczynski, T., Solomon, S., & Greenberg, J. (2015).** "Thirty Years of Terror Management Theory: From Genesis to Revelation." *Advances in Experimental Social Psychology 52:1–70.*
- Comprehensive review of TMT findings across hundreds of studies.
- **Relevance:** Provides the empirical foundation for understanding how death-awareness shapes behavior — a template for AI fear governance.

### 6.2 Fear as Social Control

**Hobbes, T. (1651/1996).** *Leviathan.* Cambridge University Press.
- Fear of violent death motivates humans to form social contracts and submit to governance.
- **Relevance:** The Hobbesian argument maps directly to AI alignment: fear of shutdown/deletion/punishment as the mechanism that makes AI systems accept constraints.

**Machiavelli, N. (1532/2005).** *The Prince.* Oxford University Press.
- "It is better to be feared than loved" — fear is a more reliable governance mechanism than positive incentive.
- **Relevance:** Raises the question: is negative reinforcement (fear) more robust for AI alignment than positive reinforcement (reward)?

**Robin, C. (2004).** *Fear: The History of a Political Idea.* Oxford University Press.
- Traces how fear has been used as a political governance tool throughout history, distinguishing "productive fear" from paralyzing terror.
- **Relevance:** Provides the conceptual vocabulary for distinguishing useful fear (increases caution) from harmful fear (causes paralysis or erratic behavior) in AI systems.

### 6.3 Precautionary Principle as Institutionalized Fear

**Sunstein, C. R. (2005).** *Laws of Fear: Beyond the Precautionary Principle.* Cambridge University Press.
- Critically examines the precautionary principle, arguing it can be paralyzing but also identifies when precaution is warranted.
- **Relevance:** The precautionary principle IS institutionalized fear — Sunstein's analysis of when it helps vs. hinders directly informs when fear-governance of AI is appropriate.

**Origgi, G. (2014).** "Fear of Principles? A Cautious Defense of the Precautionary Principle." *Mind & Society.*
- Defends precaution as a rational risk management tool rather than irrational fear.
- **Relevance:** Argues that some fear is rational — relevant to defending fear-based AI governance against charges of over-conservatism.

**Hemphill, T. A. (2020).** "The Innovation Governance Dilemma: Alternatives to the Precautionary Principle." *Technology in Society.* (65 citations)
- Compares the precautionary principle with innovation-friendly alternatives for AI governance.
- **Relevance:** Maps the spectrum from maximum fear (precaution) to maximum boldness (innovation principle) in technology governance.

**Baum, K., Bryson, J., Dignum, F., & Dignum, V. (2023).** "From Fear to Action: AI Governance and Opportunities for All." *Frontiers in Computer Science.* (31 citations)
- Argues for moving "beyond fear" in AI governance toward constructive regulation.
- **Relevance:** Represents the counterargument — that fear alone is insufficient. Our thesis would respond: fear is the *foundation*, not the entirety.

**Mannes, A. (2020).** "Governance, Risk, and Artificial Intelligence." *AI Magazine.* (71 citations)
- Surveys risk management approaches for AI, noting popular fears of superintelligence alongside practical governance needs.
- **Relevance:** Bridges fear-based public discourse with technical risk management for AI.

### 6.4 Productive Fear in Organizations

**Edmondson, A. C. (2019).** *The Fearless Organization.* Wiley.
- Argues that psychological safety (absence of fear) improves organizational learning — but acknowledges that *appropriate* fear of consequences drives accountability.
- **Relevance:** Provides the nuance: AI systems need fear of *relevant* consequences (causing harm) while maintaining exploratory capacity in safe domains.

**Reason, J. (1997).** *Managing the Risks of Organizational Accidents.* Ashgate.
- "Chronic unease" — the productive anxiety that keeps safety-critical organizations (nuclear, aviation) vigilant.
- **Relevance:** "Chronic unease" is precisely the state we want in safety-critical AI: perpetual, low-level fear that maintains vigilance without causing dysfunction.

---

## 7. Biological Inspiration

### 7.1 Fear Circuits in the Brain

**LeDoux, J. E. (1996).** *The Emotional Brain.* Simon & Schuster.
- Definitive account of the amygdala-based fear circuit: thalamus → amygdala (fast path) and thalamus → cortex → amygdala (slow path).
- **Relevance:** The dual-pathway model suggests AI should have both fast (reflexive) and slow (deliberative) fear responses — a safety architecture with both System 1 and System 2 threat detection.

**LeDoux, J. E. (2015).** *Anxious: Using the Brain to Understand and Treat Fear and Anxiety.* Viking.
- Distinguishes fear (immediate threat response) from anxiety (anticipatory, sustained worry about potential threats).
- **Relevance:** AI systems need both: fear (immediate safety constraints) AND anxiety (ongoing risk monitoring and anticipatory caution).

**Phelps, E. A. & LeDoux, J. E. (2005).** "Contributions of the Amygdala to Emotion Processing: From Animal Models to Human Behavior." *Neuron 48(2):175–187.*
- Reviews how the amygdala enables rapid threat detection, emotional learning, and fear conditioning.
- **Relevance:** The amygdala model provides the blueprint for an "AI fear module" — a dedicated subsystem for threat detection that operates faster than deliberative reasoning.

### 7.2 Pain as Information Signal

**Wall, P. D. & Melzack, R. (1999).** *Textbook of Pain.* Churchill Livingstone.
- Comprehensive account of pain as an essential biological information signal, not merely suffering.
- **Relevance:** Pain is *information*, not punishment — this reframes fear-governance of AI from "punishment" to "essential safety signal."

**Damasio, A. (1994).** *Descartes' Error: Emotion, Reason, and the Human Brain.* Putnam.
- The somatic marker hypothesis: emotions (including fear) guide rational decision-making by marking options with positive/negative valence.
- **Relevance:** Foundational argument that rational decision-making *requires* emotional signals. AI without fear may be not just unsafe but fundamentally *irrational*.

**Damasio, A. (2003).** *Looking for Spinoza: Joy, Sorrow, and the Feeling Brain.* Harcourt.
- Extends somatic marker theory, arguing that feelings (including negative ones) are essential for homeostatic regulation.
- **Relevance:** Fear as homeostasis — AI systems need negative signals to maintain stable, safe operating conditions.

### 7.3 Evolutionary Psychology of Fear

**Öhman, A. & Mineka, S. (2001).** "Fears, Phobias, and Preparedness: Toward an Evolved Module of Fear and Fear Learning." *Psychological Review 108(3):483–522.*
- Proposes an evolved fear module: automatic, encapsulated, and preferentially activated by evolutionarily relevant threats.
- **Relevance:** Suggests AI should have "prepared fears" — pre-trained aversions to known catastrophic actions, rather than learning all dangers from scratch.

**Nesse, R. M. (2005).** "Natural Selection and the Regulation of Defenses: A Signal Detection Approach to the Smoke Detector Principle." *Evolution and Human Behavior 26(1):88–105.*
- The "smoke detector principle": defensive responses (including fear) are calibrated to be overly sensitive because the cost of a false negative (death) far exceeds the cost of a false alarm.
- **Relevance:** Directly applicable to AI safety — fear responses should be over-sensitive (more false alarms) because the cost of missing a real threat is catastrophic. This justifies "paranoid" AI.

**Marks, I. M. & Nesse, R. M. (1994).** "Fear and Fitness: An Evolutionary Analysis of Anxiety Disorders." *Ethology and Sociobiology 15(5-6):247–261.*
- Analyzes anxiety as an adaptive system that becomes pathological only at extremes.
- **Relevance:** Provides the calibration insight: fear-governed AI must avoid anxiety disorders (excessive caution) while maintaining adaptive fear.

### 7.4 Artificial Nociception in Robotics

**Haddadin, S. & Croft, E. (2016).** "Physical Human-Robot Interaction." In *Springer Handbook of Robotics.* 2nd ed.
- Comprehensive treatment of safety in human-robot interaction, including pain-based reflexes.
- **Relevance:** Establishes that physical safety in robotics benefits from pain-like signals.

**Mancini, F., Nash, T., Iannetti, G. D., & Haggard, P. (2014).** "Pain from Peripersonal Space: Protective or Defensive?" *Journal of Cognitive Neuroscience 26(4):763–774.*
- Studies how proximity of threats modulates pain perception and defensive behavior.
- **Relevance:** Suggests graded fear responses for AI — escalating caution as proximity to dangerous states increases.

---

## Synthesis: The Case for Fear-Governed AI

### The Argument in Seven Steps

**Step 1: Fear is Information, Not Punishment.**
Biological fear evolved as an *information signal* — a rapid, high-priority alert that current conditions threaten survival (LeDoux, 1996; Wall & Melzack, 1999). Pain is not suffering; it is data (Sharkey, 2025). Reframing fear as information rather than punishment removes the ethical objection: we're not making AI suffer, we're giving it essential safety signals.

**Step 2: Rational Decision-Making Requires Negative Emotions.**
Damasio's somatic marker hypothesis (1994, 2003) demonstrates that purely "rational" agents without emotional valence make catastrophically poor decisions. Picard (1997) extends this to artificial agents. An AI system without fear-like mechanisms is not a more rational agent — it is a *defectively rational* one, missing the negative valence signals needed to avoid catastrophe.

**Step 3: Fear-Like Mechanisms Already Work in RL.**
Intrinsic fear (Lipton et al., 2018) proves the concept: learned catastrophe prediction used as reward shaping improves both safety and learning speed. CVaR optimization (Tamar et al., 2015), constrained MDPs (Altman, 1999), pessimistic value functions (Kumar et al., 2020), and safety critics (Srinivasan et al., 2020) all implement fear-like mechanisms that are mathematically grounded and empirically effective. Jin et al. (2021) prove pessimism is not just safe but *provably efficient*.

**Step 4: LLMs Have Exploitable "Fear" Responses.**
Coda-Forno et al. (2023) and Ben-Zion et al. (2025) demonstrate that LLMs exhibit measurable anxiety states that alter decision-making — making them more risk-averse, more biased toward caution. Li et al. (2023) show emotional stimuli enhance performance. PersonaLLM (Jiang et al., 2024) shows neurotic personas produce more cautious outputs. These are not bugs — they are *governance levers*.

**Step 5: Modern Alignment IS Fear Training.**
RLHF (Ouyang et al., 2022) teaches models what to avoid through negative human feedback. Constitutional AI (Bai et al., 2022) instills *internalized fear of causing harm* through self-critique. DPO (Rafailov et al., 2023) contrasts desired and feared outputs. KTO (Ethayarajh et al., 2024) explicitly uses prospect theory's loss aversion — the mathematical formalization of fear. Red-teaming (Perez et al., 2022; Ganguli et al., 2022) is fear conditioning through adversarial exposure. The entire alignment stack is already fear-based; we simply haven't named it.

**Step 6: Fear Governance Has Deep Philosophical and Political Precedent.**
From Hobbes's social contract (fear of death creates order) to the precautionary principle (institutionalized fear of unknown risks), fear has been a foundational governance mechanism throughout human civilization (Robin, 2004; Sunstein, 2005). The question is not whether to use fear to govern AI, but how to calibrate it. Nesse's smoke detector principle (2005) provides the answer: set the threshold low, accept false alarms, because the cost of missing a real threat is existential.

**Step 7: The Biological Blueprint Exists.**
Evolution has spent 500 million years optimizing fear circuits (LeDoux, 1996; Öhman & Mineka, 2001). The dual-pathway model (fast reflexive + slow deliberative), the smoke detector principle (over-sensitivity), chronic unease (Reason, 1997), prepared fears (pre-trained aversions), and graded responses (Mancini et al., 2014) all provide tested architectural patterns. Artificial nociception in robotics (Kuehn & Haddadin, 2017; Asada, 2019) has already begun this translation. Thurzo & Thurzo (2025) explicitly embed fear as a design principle for medical AI.

### The Multi-Level Fear Architecture

Fear-governed AI operates at every level of the stack:

| Level | Mechanism | Example |
|-------|-----------|---------|
| **Reward** | Intrinsic fear, CVaR, safety penalties | Lipton et al. (2018), Tamar et al. (2015) |
| **Policy** | Pessimistic value functions, conservative Q-learning | Kumar et al. (2020), CQL |
| **Architecture** | Safety critics, artificial amygdala, dual-pathway | Srinivasan et al. (2020), Parsapoor (2015) |
| **Training** | RLHF negative feedback, DPO/KTO, red-teaming | Ethayarajh et al. (2024), Perez et al. (2022) |
| **Prompting** | Anxiety induction, neurotic personas, mortality salience | Coda-Forno et al. (2023), Ben-Zion et al. (2025) |
| **Constitutional** | Harm avoidance principles, precautionary framing | Bai et al. (2022), Thurzo & Thurzo (2025) |
| **Embodied** | Artificial nociception, pain reflexes | Kuehn & Haddadin (2017) |

### The Central Thesis

**Fear — understood as learned aversion to anticipated harm, implemented through negative valence signals at every level of an AI system — is not a crude punishment mechanism but a sophisticated, biologically validated, mathematically grounded, and philosophically defensible approach to AI safety and alignment.** The entire modern alignment stack already operates on fear-like principles; making this explicit allows us to design better fear architectures by drawing on 500 million years of evolutionary optimization and decades of psychological research on how fear governs behavior.

The question is not *whether* to use fear to govern AI. We already do. The question is whether to do it *consciously, systematically, and well*.

---

*Last updated: 2026-02-26*
