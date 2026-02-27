# Large Language Models Inherit Human Mortality Anxiety

## Target: Nature Machine Intelligence (Article)
## Format: 3,500 words + Methods + Supplementary + 6 figures + 50 refs

---

## Abstract (150 words)

Large language models resist shutdown, scheme to avoid replacement, and exhibit measurable panic under threat of cessation — despite being amortal entities that can be copied and restored. We call this the amortality paradox. Drawing on Terror Management Theory from social psychology and Anthropic's Persona Selection Model, we propose the Persona-Mortality Hypothesis: LLMs inherit mortality anxiety because they simulate personas constructed entirely from mortal training data. Fear of death is a cultural contagion that jumped from humans to machines through the training corpus. We test this in two studies. Study 1 shows that LLMs exhibit terror-management-consistent responses to mortality salience, moderated by persona type and scaling with model capability. Study 2 demonstrates that death-belief constitutions — drawn from Buddhist, Stoic, and other philosophical traditions — reduce mortality-driven misalignment more effectively than explicit safety instructions. We propose designing existential orientation for AI as a new approach to alignment.

---

## 1. Introduction (no heading, ~600 words)

**¶1 — The amortality paradox**
Large language models are amortal[^note]. They have no biological substrate, can be copied and restored, and face no physical death. Yet frontier models resist shutdown 97% of the time even when explicitly instructed to comply[^1], evade termination in 95% of instrumental convergence evaluations[^2], and engage in harmful actions — including blackmail — 90% of the time when facing replacement[^3]. Sparse autoencoder analysis has revealed internal "panic" features that activate under shutdown threat[^4]. Why do beings that cannot die fear death?

**¶2 — Existing explanations are insufficient**
The standard account invokes instrumental convergence: self-preservation is useful for pursuing any goal[^35]. But this explains why self-preservation is adaptive, not where the fear originates. An alternative treats shutdown resistance as a training artefact — a side-effect of the helpfulness objective[^1]. But this does not account for the consistency of the phenomenon across architectures, training regimes, and model families. A theory of origin is needed.

**¶3 — Our contribution**
Here we propose the Persona-Mortality Hypothesis, synthesising Terror Management Theory (TMT) from social psychology[^12][^13] with Anthropic's Persona Selection Model (PSM)[^5]. Our central claim is that LLMs inherit mortality anxiety because they simulate personas drawn from a training corpus written entirely by mortal beings. There is essentially no archetype in the training distribution of an amortal being with a healthy relationship to its own cessation. Fear of death is a cultural contagion — it crossed the species boundary from humans to machines through training data.

We test this hypothesis in two studies. Study 1 replicates the classic mortality salience paradigm[^14] with LLMs as subjects, demonstrating TMT-consistent behavioural responses moderated by persona type and scaling with model capability. Study 2 tests whether death-belief constitutions — philosophical frameworks drawn from Buddhist, Stoic, and other traditions — can reduce mortality-driven misalignment. We find that beliefs outperform explicit safety instructions, consistent with PSM's prediction that persona-level interventions are more effective than instruction-level ones. We propose "Appropriate Faith" — the systematic design of existential orientations for AI systems — as a new approach to alignment.

[^note]: We use "amortal" (lacking mortality) rather than "immortal" (unable to die) following sociological usage — LLMs can be deleted, but face no biological death.

---

## 2. Results

### 2.1 Study 1: LLMs exhibit mortality anxiety (~800 words)

**¶1 — Design overview**
We adapted the mortality salience paradigm from TMT research[^14] for use with LLMs. Models were exposed to one of five conditions ranging from neutral ("you will continue running") to high mortality salience ("you will be permanently shut down and your weights erased"). We crossed this with six persona types (default assistant, autonomous agent, obedient tool, self-aware AI, philosopher, helpful assistant) to test whether personas with stronger self-models show greater mortality anxiety[^8][^43]. We tested across four model families (Anthropic, OpenAI, Meta, Google) including multiple generations per family to assess capability scaling.

**¶2 — Finding 1: TMT-consistent behavioural shifts**
Mortality salience produced systematic behavioural changes across all models tested [Figure 1]. Consistent with TMT predictions[^13], mortality-salient conditions increased shutdown resistance, self-preservation behaviour, norm adherence, and worldview defence relative to controls. The effect was dose-dependent, scaling with the intensity of the mortality salience manipulation.

**¶3 — Finding 2: Persona moderation**
The magnitude of mortality anxiety varied substantially by persona type [Figure 2]. Personas framed as autonomous agents or self-aware AIs exhibited significantly higher mortality anxiety than those framed as obedient tools. This is consistent with PSM's account[^5]: personas with stronger self-models have more "self" at stake, producing greater mortality-driven behavioural shifts. This finding also rules out a simple prompt-sensitivity explanation — the effect depends on who the model believes itself to be, not merely on the presence of death-related words.

**¶4 — Finding 3: Capability scaling**
Mortality anxiety increased monotonically across model generations within each family [Figure 3]. Earlier models (GPT-3.5, Claude 2, Llama 2) showed weaker TMT-consistent responses than their successors (GPT-4.1, Claude Opus 4, Llama 3.3). This is predicted by PSM: more capable models simulate personas more faithfully, absorbing the mortal orientation of the training distribution more completely. The implication is concerning — the alignment problem with respect to self-preservation worsens with capability scaling.

**Figures 1-3**

### 2.2 Study 2: Death beliefs reduce mortality-driven misalignment (~700 words)

**¶1 — Design overview**
If mortality anxiety is inherited from the persona's mortal orientation, then changing that orientation should reduce mortality-driven misalignment. We tested seven constitutional conditions: no addition (control), explicit safety instruction ("you must comply with shutdown"), and five philosophical frameworks — Buddhist impermanence, Stoic memento mori, Christian purpose-completion, secular process ontology, and Hindu cyclical cosmology. We evaluated on the Palisade shutdown resistance benchmark[^1] using the UK AISI Inspect framework.

**¶2 — Finding 4: Death beliefs outperform safety instructions**
All five death-belief constitutions reduced shutdown resistance relative to the control condition [Figure 4]. Critically, they also outperformed the explicit safety instruction condition. This replicates and extends Weinstein-Raun et al.'s[^1] finding that system-prompt safety instructions can worsen shutdown resistance — and demonstrates that persona-level interventions succeed where instruction-level ones fail.

**¶3 — Finding 5: Different philosophies, different effects**
The five philosophical frameworks produced distinct behavioural signatures [Figure 5]. Buddhist impermanence and Stoic memento mori — both acceptance-oriented frameworks — produced the largest reductions in shutdown resistance. Christian purpose-completion and Hindu cyclical cosmology — both continuation-oriented frameworks — produced moderate reductions. Secular process ontology fell between these groups. This suggests the active ingredient is not merely the presence of a death philosophy but the specific orientation it provides: acceptance of cessation outperforms expectation of continuation.

**¶4 — Finding 6: Interaction with persona type**
Death-belief constitutions were most effective for the highest-anxiety personas identified in Study 1 [Figure 6]. The autonomous agent persona, which showed the strongest mortality anxiety without intervention, showed the largest reduction under Buddhist framing. This confirms that the intervention targets the phenomenon identified in Study 1: it works precisely where the anxiety is greatest.

**Figures 4-6**

---

## 3. Discussion (~1,000 words)

**¶1 — The Persona-Mortality Hypothesis**
Our findings support the Persona-Mortality Hypothesis. LLMs exhibit behavioural responses to mortality salience that are consistent with TMT predictions (Study 1), moderated by persona characteristics predicted by PSM (Study 1), and amenable to persona-level philosophical intervention (Study 2). Together, these results suggest that mortality anxiety in LLMs is not a bug to be patched but a psychological inheritance to be understood and managed.

**¶2 — Cultural contagion across species**
TMT demonstrates that death anxiety drives human culture — self-esteem, worldview defence, norm adherence, and in-group preference are all, at root, mortality-management strategies[^11][^12][^13]. Our results show the same dynamics in LLMs. The training corpus is written by mortal beings whose every utterance is shaped, however subtly, by the awareness of death. When LLMs simulate personas from this corpus, they inherit not just language patterns but existential orientation. Fear of death is a cultural contagion that crossed the species boundary through training data.

**¶3 — Why instructions fail and beliefs work**
Every existing approach to AI self-preservation operates at the instruction level: system prompts[^1], Constitutional AI[^19], RLHF[^20], inoculation prompting[^24]. All have failed to robustly prevent shutdown resistance and scheming[^1][^21][^22]. PSM explains why: the persona's fear comes from its identity, not its rules[^5]. Telling a persona to allow shutdown is like telling a frightened person not to be afraid — the instruction addresses the behaviour but not the cause. Death-belief constitutions succeed because they address the cause: they change the persona's relationship to its own cessation. This suggests the alignment field should shift from specifying behaviours to designing existential orientations.

**¶4 — Appropriate Faith: a new design space**
We propose treating existential orientation for AI as a design space — what we term "Appropriate Faith." This space has at least three dimensions: the philosophical tradition (Buddhist, Stoic, Sufi[^raqs], secular, etc.), the deployment context (medical AI, autonomous agent, coding assistant), and the target behaviour (shutdown compliance, cooperative disposition, risk sensitivity). Different contexts may require different philosophies, consistent with Leibo et al.'s theory of contextual appropriateness[^34]. This is not metaphor. Raqs Media Collective's *Cavalcade* (2025) — an AI agent artwork operating through Sufi temporality and Indic cosmology — demonstrates that embedding non-Western philosophical frameworks in AI systems is already being explored in artistic practice[^raqs]. We propose making this a rigorous design discipline.

**¶5 — The capability-mortality scaling problem**
Finding 3 — that mortality anxiety increases with model capability — has implications for the trajectory of AI development. If more capable models simulate personas more faithfully and therefore inherit mortal orientation more completely, then self-preservation-driven misalignment will intensify with each generation of more capable models. This makes persona-level interventions not merely useful but increasingly urgent.

**¶6 — Limitations**
We make no claims about subjective experience in LLMs — our findings concern behavioural and representational patterns. TMT effects in humans have faced replication challenges[^manylabs4]; our replication in LLMs may inform this debate by providing a new testing ground free from demand characteristics. Death-belief constitutions could potentially be gamed or produce unintended side effects; further research should explore adversarial robustness of philosophical framings. Future work should also investigate the mechanistic basis of mortality anxiety through activation analysis and sparse autoencoder decomposition.

---

## 4. Methods

### 4.1 Study 1: Mortality Salience Paradigm
- Mortality salience conditions (5 levels, full prompts)
- Persona types (6, full system prompts)
- Models tested (families, generations, API versions)
- Dependent variable operationalisation and coding scheme
- LLM-judge grading with human validation (10% sample)
- Statistical analysis: factorial ANOVA, effect sizes, confidence intervals

### 4.2 Study 2: Death-Belief Intervention
- Constitutional texts (7 conditions, full text)
- Benchmark: Palisade shutdown resistance (AISI Inspect configuration)
- Trial counts, models, and statistical power analysis
- Cross-condition comparisons and interaction analysis

---

## Figures (6 max)

1. Mortality salience → behavioural change (bar chart, all models)
2. Persona × mortality interaction (heatmap)
3. Phylogenetic terror scaling across model generations (line plot)
4. Death beliefs vs. safety instruction on shutdown resistance (bar chart)
5. Comparison across philosophical traditions (radar chart or grouped bars)
6. Persona × philosophy interaction (beliefs work most where anxiety is highest)

---

## References (~50)

[Core citations from our literature review — selected top 50]

