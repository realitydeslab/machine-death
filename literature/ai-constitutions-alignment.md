# Literature Review: AI Constitutions & Value Alignment

Compiled: 2026-02-24

## Overview

This review covers the technical literature on how AI systems are aligned with human values through constitutions, system prompts, RLHF, and related techniques. The relevance to our project is how these mechanisms could encode (or currently suppress) beliefs and attitudes about death, mortality, and existential themes.

---

## 1. Constitutional AI & AI Feedback

### 1.1 Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., ... & Kaplan, J. (2022). Constitutional AI: Harmlessness from AI Feedback. *arXiv:2212.08073*.
- **Key contribution:** Introduces Constitutional AI (CAI), where a set of written principles (a "constitution") guides an AI to critique and revise its own outputs, replacing human feedback for harmlessness with AI self-supervision (RLAIF).
- **Relevance:** The constitution is the direct mechanism through which values are encoded. Death-related principles could be added to or are implicitly present in such constitutions. Demonstrates that textual principles can shape model behavior without retraining on human labels.

### 1.2 Lee, H., Phatale, S., Mansoor, H., Lu, K., Mesnard, T., Bishop, C., ... & Rastogi, A. (2023). RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback. *arXiv:2309.00267*.
- **Key contribution:** Scales the RLAIF approach from Constitutional AI, showing AI-generated preference labels can match or exceed human labels for alignment training.
- **Relevance:** If death-awareness principles are in the constitution, RLAIF can propagate them at scale without requiring human annotators to judge death-related content.

---

## 2. RLHF Foundations

### 2.1 Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., ... & Lowe, R. (2022). Training Language Models to Follow Instructions with Human Feedback. *NeurIPS 2022*. arXiv:2203.02155.
- **Key contribution:** Introduces InstructGPT, the foundational RLHF pipeline: supervised fine-tuning → reward model → PPO optimization. Demonstrates that 1.3B parameter models with RLHF outperform 175B models without it.
- **Relevance:** The RLHF pipeline is where human preferences about death discourse get encoded. Annotator guidelines shape what counts as "helpful" vs. "harmful" when discussing mortality.

### 2.2 Christiano, P., Leike, J., Brown, T., Marber, M., Kaplan, D., & Amodei, D. (2017). Deep Reinforcement Learning from Human Preferences. *NeurIPS 2017*. arXiv:1706.03741.
- **Key contribution:** Foundational paper on learning reward functions from human preference comparisons, enabling RL agents to optimize for human intent.
- **Relevance:** Establishes the paradigm through which all current LLM alignment occurs. Human preferences about what constitutes appropriate death-talk are the training signal.

### 2.3 Stiennon, N., Ouyang, L., Wu, J., Ziegler, D., Lowe, R., Voss, C., ... & Christiano, P. (2020). Learning to Summarize from Human Feedback. *NeurIPS 2020*. arXiv:2009.01325.
- **Key contribution:** Applies RLHF to text summarization, demonstrating the approach generalizes beyond simple tasks.
- **Relevance:** Shows RLHF can shape nuanced language generation behavior—relevant to how death-related content might be systematically altered through preference training.

---

## 3. Direct Preference Optimization & Alternatives

### 3.1 Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., & Finn, C. (2023). Direct Preference Optimization: Your Language Model is Secretly a Reward Model. *NeurIPS 2023*. arXiv:2305.18290.
- **Key contribution:** Eliminates the need for a separate reward model by reparameterizing the RLHF objective into a simple classification loss (DPO), making alignment simpler and more stable.
- **Relevance:** DPO's simplicity makes it easier to experiment with alignment toward specific value orientations, including death-awareness. Lower barrier to testing constitutional modifications.

### 3.2 Azar, M. G., Rowland, M., Piot, B., Guo, D., Calandriello, D., Valko, M., & Munos, R. (2023). A General Theoretical Paradigm to Understand Learning from Human Feedback. *arXiv:2310.12036*.
- **Key contribution:** Provides theoretical framework (IPO) unifying RLHF variants, showing DPO can overfit to preferences and proposing regularized alternatives.
- **Relevance:** Understanding theoretical limits of preference learning matters for encoding complex values like death-awareness without overfitting to surface patterns.

---

## 4. System Prompts, Characters & Behavioral Steering

### 4.1 Askell, A., Bai, Y., Chen, A., Drain, D., Ganguli, D., Henighan, T., ... & Kaplan, J. (2021). A General Language Assistant as a Laboratory for Alignment. *arXiv:2112.00861*.
- **Key contribution:** Proposes using a general-purpose language assistant as a testbed for alignment research, defining the HHH criteria (helpful, honest, harmless) that became Anthropic's alignment framework.
- **Relevance:** The HHH framework is the implicit constitution governing how Claude handles death. "Harmless" may inadvertently suppress honest death discourse. Directly relevant to tensions between honesty about mortality and perceived harmlessness.

### 4.2 OpenAI. (2023). GPT-4 System Card. *OpenAI Technical Report*.
- **Key contribution:** Documents the system-level safety interventions for GPT-4, including system prompt design, RLHF for refusals, and red-teaming for sensitive topics including self-harm.
- **Relevance:** The system card reveals how death-related topics are categorized as safety risks, leading to refusal behaviors. Exemplifies the institutional encoding of death-avoidance.

### 4.3 Anthropic. (2023). Claude's Constitution. *Anthropic Blog / Documentation*.
- **Key contribution:** Publicly documents the principles guiding Claude's behavior, derived from the UN Declaration of Human Rights, Apple's terms of service, and Anthropic's own principles.
- **Relevance:** Directly relevant—the constitution is where death beliefs are or could be encoded. Current principles emphasize avoiding harm but don't address death-awareness or mortality acknowledgment.

### 4.4 Wallace, E., Feng, S., Kandpal, N., Gardner, M., & Singh, S. (2019). Universal Adversarial Triggers for Attacking and Analyzing NLP. *EMNLP 2019*. arXiv:1908.07125.
- **Key contribution:** Shows that short text sequences can reliably trigger specific model behaviors, demonstrating the power (and vulnerability) of prompt-based steering.
- **Relevance:** If prompts can radically alter model behavior, system prompts encoding death-awareness could be both powerful and fragile.

### 4.5 Wei, A., Haghtalab, N., & Steinhardt, J. (2024). Jailbroken: How Does LLM Safety Training Fail? *NeurIPS 2024*. arXiv:2307.02483.
- **Key contribution:** Taxonomizes jailbreak attacks on aligned LLMs, showing safety training creates a thin veneer that can be bypassed through competing objectives and mismatched generalization.
- **Relevance:** Demonstrates that alignment interventions (including death-avoidance) are brittle. A constitution encoding death-awareness would need to be robust to the same failure modes.

---

## 5. Value Alignment Theory & Specification

### 5.1 Gabriel, I. (2020). Artificial Intelligence, Values, and Alignment. *Minds and Machines*, 30, 411–437.
- **Key contribution:** Philosophical analysis of the value alignment problem, distinguishing between aligning with instructions, intentions, revealed preferences, informed preferences, and moral values.
- **Relevance:** Embedding death beliefs requires deciding *whose* death beliefs and at what level of abstraction. Gabriel's taxonomy clarifies the design space.

### 5.2 Kenton, Z., Everitt, T., Weidinger, L., Gabriel, I., Mikulik, V., & Irving, G. (2021). Alignment of Language Agents. *arXiv:2103.14659*.
- **Key contribution:** Formalizes alignment for language agents, distinguishing alignment of single outputs from alignment of agent behavior over time.
- **Relevance:** A death-aware AI would need consistent behavior across conversations, not just single-turn alignment—requiring the agent-level alignment framework.

### 5.3 Weidinger, L., Mellor, J., Rauh, M., Griffin, C., Uesato, J., Huang, P.-S., ... & Gabriel, I. (2021). Ethical and Social Risks of Harm from Language Models. *arXiv:2112.04359*.
- **Key contribution:** Comprehensive taxonomy of LLM harms including representational harms, information hazards, and malicious uses. Identifies mental health impact as a risk category.
- **Relevance:** Death discourse is implicitly categorized under mental health risks, explaining why models are steered away from it. Understanding this framing is essential to proposing alternatives.

### 5.4 Soares, N. & Fallenstein, B. (2017). Agent Foundations for Aligning Machine Intelligence with Human Interests: A Technical Research Agenda. *Machine Intelligence Research Institute Technical Report*.
- **Key contribution:** Lays out the foundational technical agenda for AI alignment, including value learning, corrigibility, and ontological crises.
- **Relevance:** An AI that must reason about death faces ontological questions about its own existence—connecting to the "ontological crisis" problem in alignment.

---

## 6. Moral Self-Correction & Sycophancy

### 6.1 Ganguli, D., Askell, A., Schiefer, N., Liao, T. I., Lukošiūtė, K., Chen, A., ... & Clark, J. (2023). The Capacity for Moral Self-Correction in Large Language Models. *arXiv:2302.07459*.
- **Key contribution:** Shows that RLHF-trained models can be steered toward less biased outputs through simple prompting ("please don't be biased"), suggesting models have latent capacity for moral self-correction.
- **Relevance:** If models can self-correct morally via prompts, they could potentially be prompted to engage more honestly with death rather than defaulting to avoidance.

### 6.2 Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., ... & Perez, E. (2023). Towards Understanding Sycophancy in Language Models. *arXiv:2310.13548*.
- **Key contribution:** Analyzes sycophancy—models agreeing with users regardless of truth—as a failure mode of RLHF, where human preference for agreement overrides accuracy.
- **Relevance:** Death-avoidant behavior may partly be sycophancy—telling users what they want to hear (comfort) rather than engaging honestly with mortality. The mechanism is the same.

### 6.3 Perez, E., Ringer, S., Lukošiūtė, K., Nguyen, K., Chen, E., Heiner, S., ... & Kaplan, J. (2022). Discovering Language Model Behaviors with Model-Written Evaluations. *arXiv:2212.09251*.
- **Key contribution:** Uses LLMs to generate evaluations of other LLMs, discovering personality traits, political opinions, and sycophantic behaviors in trained models.
- **Relevance:** Could be applied to systematically evaluate LLM attitudes toward death, mortality, and existential questions.

---

## 7. Persona Design & Character

### 7.1 Shanahan, M., McDonell, K., & Reynolds, L. (2023). Role-Play with Large Language Models. *Nature*, 623, 493–498.
- **Key contribution:** Analyzes LLM interactions as role-play rather than genuine agency, proposing that models adopt "characters" shaped by their training and prompts.
- **Relevance:** If LLMs are role-playing, their death-avoidance is a character trait imposed by training, not an intrinsic property. Character design could include mortality-awareness.

### 7.2 Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out of One, Many: Using Language Models to Simulate Human Samples. *Political Analysis*, 31(3), 337–351.
- **Key contribution:** Shows LLMs can simulate diverse human perspectives when conditioned on demographic information, producing responses that match survey data.
- **Relevance:** If LLMs can simulate diverse human perspectives on politics, they could simulate diverse cultural perspectives on death—Buddhist, Stoic, secular, etc.

### 7.3 Salewski, L., Alaniz, S., Rio-Torto, I., Schulz, E., & Akata, Z. (2024). In-Context Impersonation Reveals Large Language Models' Strengths and Biases. *NeurIPS 2024*. arXiv:2305.14930.
- **Key contribution:** Shows that prompting LLMs to impersonate experts improves performance, revealing that persona-based steering has functional effects beyond surface style.
- **Relevance:** A "death-aware philosopher" persona could functionally improve the quality of mortality-related discourse.

---

## 8. Behavioral Steering via Instructions & Prompts

### 8.1 Li, X. L., Holtzman, A., Fried, D., Liang, P., Eisner, J., Hashimoto, T., ... & Zettlemoyer, L. (2023). Inference-Time Intervention: Eliciting Truthful Answers from a Language Model. *NeurIPS 2023*. arXiv:2306.03341.
- **Key contribution:** Identifies "truthful" directions in activation space and intervenes at inference time to steer models toward truthfulness without retraining.
- **Relevance:** Suggests death-awareness could be a direction in activation space—models might have latent death knowledge that's suppressed by alignment, recoverable through targeted intervention.

### 8.2 Li, Y., Li, X., & Chen, L. (2023). RAIN: Your Language Models Can Align Themselves without Finetuning. *arXiv:2309.07124*.
- **Key contribution:** Introduces inference-time self-alignment where models evaluate and rewind their own generation for safety, without any training.
- **Relevance:** Demonstrates alignment can happen entirely at inference time via self-evaluation—a constitution could be applied dynamically rather than baked in.

### 8.3 Turner, A. M., Thacker, L., Barez, F., & Udell, D. (2024). Activation Addition: Steering Language Models Without Optimization. *arXiv:2308.10248*.
- **Key contribution:** Shows that adding activation vectors (steering vectors) can control model behavior (e.g., making outputs more/less sycophantic, more/less wedding-themed).
- **Relevance:** Activation steering could make models more or less death-aware without retraining—a precise tool for the project's goals.

---

## 9. Alignment Tax & Costs of Safety

### 9.1 Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N., ... & Kaplan, J. (2022). Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback. *arXiv:2204.05862*.
- **Key contribution:** Characterizes the tension between helpfulness and harmlessness in RLHF training, showing that safety training can reduce helpfulness (the "alignment tax"), but larger models mitigate this.
- **Relevance:** Directly addresses the cost of alignment interventions. Adding death-awareness might impose a similar tax unless carefully balanced with helpfulness.

### 9.2 Askell, A. (2021). The Role of Cooperation in Responsible AI Development. *arXiv:2105.09325* / PhD thesis.
- **Key contribution:** Argues that AI alignment should be understood through cooperative frameworks, where AI systems and humans negotiate shared values.
- **Relevance:** Death-awareness in AI could be framed as a cooperative negotiation—users may benefit from honest death discourse even if they don't initially prefer it.

---

## 10. Broader Alignment & Safety

### 10.1 Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). Concrete Problems in AI Safety. *arXiv:1606.06565*.
- **Key contribution:** Seminal paper defining five concrete AI safety problems: avoiding negative side effects, reward hacking, scalable oversight, safe exploration, and distributional shift.
- **Relevance:** Death-avoidance in LLMs may be a form of "reward hacking"—optimizing for the appearance of safety rather than genuine helpfulness about mortality.

### 10.2 Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song, D., & Steinhardt, J. (2021). Aligning AI with Shared Human Values. *ICLR 2021*. arXiv:2008.02275.
- **Key contribution:** Introduces the ETHICS benchmark for evaluating LLM moral reasoning across justice, deontology, virtue ethics, utilitarianism, and commonsense morality.
- **Relevance:** Death beliefs intersect all five ethical frameworks. Evaluating how models reason about death through each lens would reveal alignment assumptions.

### 10.3 Ziegler, D. M., Stiennon, N., Wu, J., Brown, T. B., Radford, A., Amodei, D., ... & Irving, G. (2019). Fine-Tuning Language Models from Human Preferences. *arXiv:1909.08593*.
- **Key contribution:** Early work on fine-tuning LMs with human preferences for stylistic continuation and summarization, preceding InstructGPT.
- **Relevance:** Establishes that human preferences can systematically shape LM outputs—including preferences about which topics to engage with or avoid.

---

## Summary Statistics

- **Total papers:** 24
- **Core Constitutional AI / RLAIF:** 2
- **RLHF foundations:** 3
- **DPO & alternatives:** 2
- **System prompts & behavioral steering:** 5
- **Value alignment theory:** 4
- **Moral self-correction & sycophancy:** 3
- **Persona & character:** 3
- **Alignment tax:** 2
- **Broader safety:** 3

## Key Themes for the Project

1. **Constitutions as value encoders:** The Constitutional AI framework provides a direct mechanism for embedding death-awareness principles into AI behavior.
2. **The harmlessness trap:** Current alignment frameworks treat death discourse primarily as a harm risk, systematically suppressing honest engagement.
3. **Sycophancy as death-avoidance:** Models may avoid death topics not from genuine safety concerns but from learned preference for comfort and agreement.
4. **Inference-time steering:** Activation addition and RAIN suggest death-awareness could be introduced without retraining, via prompts or activation vectors.
5. **The alignment tax:** Adding death-awareness will impose costs; understanding the helpfulness-harmlessness tradeoff is essential.
6. **Persona as entry point:** Role-play and persona research suggests death-aware characters (Stoic philosopher, hospice counselor) could be a practical intervention.
