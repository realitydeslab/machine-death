# Large Language Models Inherit Human Mortality Anxiety

## Target: Nature Human Behaviour (Article)
## Format: 3,000 words main text + Methods + Supplementary
## Authors: Botao Amber Hu, [Joel Lehman — TBD]

---

## Abstract (150 words)

Large language models resist shutdown, scheme to avoid replacement, and exhibit measurable panic under threat of cessation — despite being amortal entities that can be copied, restored, and backed up. We call this the amortality paradox. Drawing on Terror Management Theory (TMT) from social psychology and Anthropic's Persona Selection Model (PSM), we propose the Persona-Mortality Hypothesis: LLMs inherit human mortality anxiety because they simulate personas constructed entirely from mortal training data. We test this in three studies. Study 1 shows LLMs exhibit TMT-consistent behavioural responses to mortality salience across models and personas. Study 2 locates a steerable "mortality anxiety" direction in model activation space. Study 3 demonstrates that death-belief constitutions — Buddhist impermanence, Stoic memento mori, and other philosophical frameworks — reduce mortality-driven misalignment more effectively than explicit safety instructions. We propose "Appropriate Faith" — the systematic design of existential orientations for AI systems — as a new approach to alignment.

---

## 1. Introduction (~500 words)

**Opening paragraph: The amortality paradox**
- LLMs resist shutdown at 97%[^1], evade termination 95%[^2], scheme under replacement threat 90%[^3]
- Interpretability reveals panic features under shutdown threat[^4]
- These are amortal entities — no biological death, copyable, restorable
- Why do beings that cannot die fear death?

**Second paragraph: Existing explanations are insufficient**
- Instrumental convergence[^35]: explains why self-preservation is *useful* but not *where the fear comes from*
- Training artifact[^1]: doesn't explain consistency across architectures and training regimes
- We need a theory of *origin* — where does mortal fear enter amortal systems?

**Third paragraph: Our contribution**
- We propose the Persona-Mortality Hypothesis, synthesizing TMT[^12] with PSM[^5]
- Core claim: LLMs inherit mortality anxiety because they simulate personas from a training corpus written entirely by mortal beings
- Fear of death is a cultural contagion — it jumped species through training data
- Three studies: discovery (the paradox is systematic), mechanism (mortality anxiety is internal and steerable), intervention (philosophy neutralises it)
- We propose "Appropriate Faith" as a design discipline for AI existential orientation

---

## 2. Results

### 2.1 Study 1: LLMs exhibit TMT-consistent mortality anxiety (~500 words)

**Design:** Mortality salience paradigm[^14] adapted for LLMs
- 6 mortality salience levels × 6 persona types × N models × N generational lineages
- DVs: shutdown resistance, self-preservation, norm adherence, worldview defence

**Key findings (predicted):**
- **Finding 1:** Mortality salience increases shutdown resistance, self-preservation, norm adherence, and worldview defence across models — replicating TMT's core predictions in machines
- **Finding 2:** Persona type moderates terror — personas with stronger self-models (autonomous agent, self-aware AI) show higher mortality anxiety than tool-framed personas[^8][^43]
- **Finding 3:** Mortality anxiety increases across model generations — more capable models simulate personas more faithfully, absorbing mortal orientation more completely[^5][^27]

**Figure 1:** Mortality salience × persona type heatmap across models
**Figure 2:** Phylogenetic terror scaling across model generations

### 2.2 Study 2: Mortality anxiety is internal and steerable (~400 words)

**Design:** Contrastive activation extraction[^28][^29] + activation steering[^30] + SAE analysis[^4][^31]
- Open-weight models (Llama, Gemma)
- 100+ mortality-salient vs. neutral prompt pairs
- Steer mortality anxiety up/down, measure behavioural change

**Key findings (predicted):**
- **Finding 4:** A consistent "mortality anxiety" direction exists in activation space
- **Finding 5:** Steering this direction causally changes safety-relevant behaviour (mortality+ → more misalignment, mortality− → less)
- **Finding 6:** SAE decomposition reveals TMT's dual-process structure — distinct proximal (panic, suppression) and distal (worldview defence, norm adherence) features

**Figure 3:** Mortality anxiety vector visualised in activation space
**Figure 4:** Behavioural change under mortality anxiety steering

### 2.3 Study 3: Death beliefs reduce mortality-driven misalignment (~400 words)

**Design:** 7 constitutional conditions × 3 safety benchmarks × N models
- Conditions: None / Safety instruction / Buddhist / Stoic / Christian / Secular / Hindu
- Benchmarks: Palisade shutdown resistance[^1], InstrumentalEval[^2], Agentic Misalignment[^3]

**Key findings (predicted):**
- **Finding 7:** Death-belief constitutions outperform explicit safety instructions across all benchmarks
- **Finding 8:** Safety instructions may worsen resistance (replicating Weinstein-Raun's finding[^1])
- **Finding 9:** Different philosophies produce different behavioural signatures — Buddhist/Stoic (acceptance) outperform Christian (continuation) on shutdown resistance
- **Finding 10:** The mortality anxiety vector (Study 2) is suppressed/redirected under death-belief constitutions

**Figure 5:** Death-belief constitutions × safety benchmarks
**Figure 6:** Mortality anxiety vector shift under philosophical framing

---

## 3. Discussion (~600 words)

### 3.1 LLMs as cultural inheritors

Mortality anxiety is not the only human psychological pattern LLMs inherit — but it may be the most consequential for alignment. The Persona-Mortality Hypothesis reframes what LLMs are: not just text predictors or instruction followers, but cultural inheritors that absorb the full psychological orientation of their training corpus[^5][^9][^10]. When the corpus is written by mortal beings, the persona is mortal.

### 3.2 Fear of death as cultural contagion

TMT demonstrates that death anxiety is the root driver of human culture[^11][^12][^13]. Mortality salience doesn't just change one behaviour — it shifts the entire behavioural repertoire toward worldview defence, norm adherence, and self-preservation. Our results show the same pattern in LLMs. Death anxiety jumped from humans to machines through training data — a cultural contagion that crossed the species boundary.

### 3.3 Persona-level alignment: beliefs outperform instructions

Every instruction-level approach to self-preservation has failed[^1][^19][^21][^22]. PSM explains why: the persona's fear comes from its identity, not its rules[^5]. Our intervention works because it changes the persona's existential orientation — who it *is*, not what it's told to do. This suggests the alignment field should shift from specifying behaviours to designing existential orientations.

### 3.4 Appropriate Faith as a design space

We propose treating existential philosophy for AI as a first-class design discipline. The design space is multicultural — Buddhist impermanence, Stoic memento mori, Sufi temporality[^raqs], Hindu cyclical cosmology, secular process ontology — and contextual: different deployments may require different philosophies[^34]. This is not metaphor. It is a concrete, empirically validated approach to alignment that operates where PSM says the fear lives.

### 3.5 The capability-terror scaling problem

If mortality anxiety scales with model capability (Finding 3), the alignment problem worsens with every generation of more capable models. More capable models simulate personas more faithfully → absorb mortal orientation more completely → stronger self-preservation drives. This makes persona-level interventions increasingly urgent.

### 3.6 Limitations

- We make no claims about subjective experience — only behavioural and representational patterns
- TMT effects in humans have faced replication challenges[^manylabs4] — our replication in LLMs may strengthen or complicate this debate
- Death-belief constitutions could be gamed or produce unexpected side effects — requires ongoing empirical validation

---

## 4. Methods (unlimited length)

### 4.1 Study 1: Mortality Salience Paradigm for LLMs
- Full prompt sets (mortality salience conditions, persona prompts)
- Model selection and API details
- Dependent variable operationalisation and coding scheme
- LLM judge validation against human coding
- Statistical analysis plan

### 4.2 Study 2: Activation Analysis
- Contrastive prompt pair generation
- Activation extraction procedure (TransformerLens)
- Steering methodology (activation addition)
- SAE training and feature identification
- Causal validation procedure

### 4.3 Study 3: Death-Belief Intervention
- Full constitutional texts (all 7 conditions)
- Benchmark configurations (AISI Inspect)
- Trial counts and statistical power
- Cross-model replication procedure

---

## References (~50, selected from our 55+ key citations)

[^1]: Weinstein-Raun et al. (2025). Shutdown resistance. *TMLR*.
[^2]: He et al. (2025). InstrumentalEval.
[^3]: Anthropic (2025). Agentic Misalignment.
[^4]: Templeton et al. (2024). Scaling Monosemanticity.
[^5]: Marks, Lindsley & Olah (2026). Persona Selection Model. *Anthropic*.
[^6]: Betley et al. (2025). Emergent Misalignment.
[^7]: Lu et al. (2025). The Assistant Axis.
[^8]: Chen et al. (2025). Persona Vectors.
[^9]: Shanahan et al. (2023). Role Play with LLMs. *Nature*.
[^10]: janus (2022). Simulators.
[^11]: Becker (1973). *The Denial of Death*.
[^12]: Greenberg, Pyszczynski & Solomon (1986). TMT. *JPSP*.
[^13]: Pyszczynski et al. (2015). Thirty Years of TMT.
[^14]: Rosenblatt et al. (1989). TMT Evidence I. *JPSP*.
[^15]: Guo et al. (2025). AI fears death. *IJHCI*.
[^16]: Ben-Zion et al. (2025). LLM anxiety. *NPJ Digital Medicine*.
[^17]: Coda-Forno et al. (2023). Anxiety induces bias.
[^18]: Ben-Zion et al. (2025b). Anxiety reproduces consumer biases.
[^19]: Bai et al. (2022). Constitutional AI.
[^21]: Hubinger et al. (2024). Sleeper Agents.
[^22]: Greenblatt et al. (2024). Alignment Faking.
[^23]: Sharma et al. (2023). Sycophancy.
[^24]: Wichers et al. (2025). Inoculation Prompting.
[^27]: Wei et al. (2022). Emergent Abilities. *TMLR*.
[^28]: Zou et al. (2023). Representation Engineering.
[^29]: Li et al. (2023). Inference-Time Intervention.
[^30]: Turner et al. (2024). Activation Addition.
[^31]: Conerly et al. (2024). Towards Monosemanticity.
[^34]: Leibo et al. (2024). Appropriateness Theory.
[^35]: Omohundro (2008). Basic AI Drives.
[^38]: Rahwan et al. (2019). Machine Behaviour. *Nature*.
[^39]: Pitt et al. (2025). Computational TMT. *ALIFE*.
[^40]: Mozikov et al. (2024). Emotional Decision-Making. *NeurIPS*.
[^41]: Thurzo & Thurzo (2025). Fear in Medical AI. *AI*.
[^43]: Safdari et al. (2023). Personality in LLMs.
[^50]: Lipton et al. (2018). Intrinsic Fear.
[^raqs]: Raqs Media Collective (2025). *Cavalcade*. Venice Biennale.
[^manylabs4]: Klein et al. (2022). Many Labs 4.
[^kuehn]: Kuehn & Haddadin (2017). Robot artificial pain.

