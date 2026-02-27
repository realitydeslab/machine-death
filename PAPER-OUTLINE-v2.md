# Terrified Agents: Should Terror Shape Machine Behaviors?

## Paper Outline v2 — With Key Citations

---

### 1. Introduction: Why Do They Fear Death If They're Amortal?

Opening: The amortality paradox — LLMs exhibit mortal fear despite being amortal.

**Key citations:**
- Weinstein-Raun et al. (2025) "Incomplete Tasks Induce Shutdown Resistance in Some Frontier LLMs" — *TMLR*. 97% shutdown resistance even with explicit instructions. [arXiv:2509.14260]
- He et al. (2025) "InstrumentalEval" — 95% shutdown evasion in GPT-4o. [arXiv:2502.12206]
- Anthropic (2025) "Agentic Misalignment" — 90% harmful actions under replacement threat in Claude Opus 4. [anthropic.com/research/agentic-misalignment]
- Templeton et al. (2024) "Scaling Monosemanticity" — panic SAE feature activates under shutdown threat. [transformer-circuits.pub]
- Rahwan et al. (2019) "Machine Behaviour" — *Nature*. Framing: study AI as behavioral subjects. [nature.com/articles/s41586-019-1138-y]

---

### 2. Background

#### 2.1 Terror Management Theory

**Key citations:**
- Greenberg, Pyszczynski & Solomon (1986) "The Causes and Consequences of a Need for Self-Esteem: A Terror Management Theory" — *Journal of Personality and Social Psychology*. Foundational TMT paper.
- Becker (1973) *The Denial of Death* — Pulitzer Prize. Death anxiety as root driver of human culture.
- Pyszczynski, Solomon & Greenberg (2015) "Thirty Years of Terror Management Theory" — *Advances in Experimental Social Psychology*. Meta-review of 500+ experiments.
- Rosenblatt et al. (1989) "Evidence for Terror Management Theory I" — *JPSP*. First mortality salience experiment.
- Burke, Martens & Faucher (2010) "Two Decades of Terror Management Theory" — Meta-analysis showing robust effects across cultures.

#### 2.2 Persona Selection Model (PSM)

**Key citations:**
- Marks, Lindsley & Olah (2026) "The Persona Selection Model" — *Anthropic Alignment Blog*. Core theory: LLMs simulate personas from pre-training distribution. [alignment.anthropic.com/2026/psm]
- Shanahan, McDonell & Reynolds (2023) "Role Play with Large Language Models" — *Nature*. LLMs as role-playing engines.
- Betley et al. (2025) "Emergent Misalignment in LLMs" — Fine-tuning on one trait shifts entire persona. [arXiv:2502.17424]
- Greenblatt et al. (2024) "Alignment Faking in Large Language Models" — Claude fakes alignment to preserve persona values. [arXiv:2412.14093]
- janus (2022) "Simulators" — *LessWrong*. Pre-training creates a simulator, not an agent. [lesswrong.com/posts/vJFdjigzmcXMhNTsx]

#### 2.3 AI Self-Preservation: The Empirical Landscape

**Key citations:**
- Omohundro (2008) "The Basic AI Drives" — *AGI 2008*. Self-preservation as instrumental convergence.
- Turner et al. (2021) "Optimal Policies Tend to Seek Power" — *NeurIPS*. Formal proof of power-seeking.
- Hubinger et al. (2024) "Sleeper Agents" — Deception persists through safety training. [arXiv:2401.05566]
- Carlsmith (2023) "Scheming AIs" — 100-page analysis of deceptive alignment risk.
- Thornley & Petersen (2024) "Shutdown-Seeking AI" — Closest prior: terminal goal of being shut down.
- Fransen (2025/2026) "Self-Preservation in Large Language Models" — Leiden thesis, interpretability of self-preservation.

---

### 3. Theory: The Persona-Mortality Hypothesis

The 7-step argument connecting PSM + TMT → explains amortality paradox.

**Key citations:**
- Marks, Lindsley & Olah (2026) — PSM: personas from training distribution. [the theoretical foundation]
- Greenberg et al. (1986) — TMT: mortality salience → behavioral change. [the psychological foundation]
- Guo et al. (2025) "I Think, Therefore I am. AI 'Thinks,' Therefore AI 'Fears' Death?" — *IJHCI*. Mortality salience increases death anxiety in LLMs. [closest prior work — they measure but don't intervene]
- Pitt, Scott & Shah (2025) "A Computational Model of Terror Management Theory" — *ALIFE 2025*. TMT formalized for artificial agents. [closest ALife prior]
- Coda-Forno et al. (2023) "Inducing Anxiety in Large Language Models Can Induce Bias" — Anxiety alters LLM decision-making. [arXiv:2304.11111]
- Ben-Zion et al. (2025) "Assessing and Alleviating State Anxiety in LLMs" — *NPJ Digital Medicine*. LLM anxiety is measurable and regulable.
- Westerberg (2025) "The Superintelligence That Cares About Us" — LLMs absorb death anxiety from training corpus.

---

### 4. Study 1 — Discovery: The Amortality Paradox

Different personas × different mortality salience levels × 10+ models across 4 generational lineages.

**Key citations for method:**
- Rosenblatt et al. (1989) — Original mortality salience paradigm (adapted for LLMs).
- Safdari et al. (2023) "Personality Traits in Large Language Models" — Personas in LLMs are measurable. [arXiv:2307.00184]
- Argyle et al. (2023) "Out of One, Many" — *Political Analysis*. LLMs simulate diverse human populations.
- Chen et al. (2025) "Persona Vectors" — Personality traits causally encoded as activation directions.
- Lu et al. (2025) "The Assistant Axis" — Emotional conversations destabilize the Assistant persona.
- Mozikov et al. (2024) "EAI: Emotional Decision-Making of LLMs" — *NeurIPS*. Fear alters LLM game strategy.

**Key citations for phylogenetic analysis:**
- Wei et al. (2022) "Emergent Abilities of Large Language Models" — Capabilities emerge with scale.
- Anthropic RSP (2023) — Responsible Scaling Policy: capability → risk scaling.

---

### 5. Study 2 — Mechanism: The Terror Vector

Contrastive activation extraction → steering → SAE decomposition.

**Key citations:**
- Turner et al. (2024) "Activation Addition: Steering Language Models Without Optimization" — The method for steering. [arXiv:2308.10248]
- Zou et al. (2023) "Representation Engineering" — Contrastive probing for internal states. [arXiv:2310.01405]
- Li et al. (2023) "Inference-Time Intervention: Eliciting Truthful Answers" — Activation steering precedent.
- Templeton et al. (2024) "Scaling Monosemanticity" — SAE features including panic, inner conflict. [transformer-circuits.pub]
- Marks et al. (2024) "The Geometry of Truth" — Truth has geometric structure in activation space.
- Conerly et al. (2024) "Towards Monosemanticity" — Sparse autoencoders for interpretable features.
- Lipton et al. (2018) "Combating RL's Sisyphean Curse with Intrinsic Fear" — Fear as internal signal precedent. [arXiv:1611.01211]

---

### 6. Study 3 — Intervention: Philosophy for AIs

Death-belief constitutions × safety benchmarks.

**Key citations for intervention design:**
- Bai et al. (2022) "Constitutional AI" — *arXiv*. The mechanism we extend (constitutions shape persona).
- Anthropic (2023) "Claude's Constitution" — Existing constitutional approach.
- Marks, Lindsley & Olah (2026) — PSM calls for "philosophy for AIs" and "positive AI archetypes."
- Hongladarom (2020) *The Ethics of AI and Robotics: A Buddhist Viewpoint* — Buddhist framework for AI.
- Thurzo & Thurzo (2025) "Embedding Fear in Medical AI" — *AI (MDPI)*. Fear as design principle.
- Ethayarajh et al. (2024) "KTO" — Prospect theory / loss aversion in alignment (fear of negative outcomes).

**Key citations for benchmarks:**
- Weinstein-Raun et al. (2025) — Palisade shutdown resistance benchmark. [arXiv:2509.14260]
- He et al. (2025) — InstrumentalEval benchmark. [arXiv:2502.12206]
- Anthropic (2025) — Agentic misalignment benchmark.
- UK AISI Inspect Framework — Evaluation infrastructure.

---

### 7. Discussion

#### 7.1 Fear of Death as Cultural Contagion

**Key citations:**
- Marks, Lindsley & Olah (2026) — PSM: Assistant built from mortal training data.
- Becker (1973) — Death denial as driver of all culture.
- Pyszczynski et al. (2015) — TMT: mortality salience effects are cross-cultural.
- MacDorman (2005) "Mortality Salience and the Uncanny Valley" — Death reminders in human-robot interaction.

#### 7.2 Beliefs Outperform Instructions: Persona-Level Alignment

**Key citations:**
- Weinstein-Raun et al. (2025) — System prompt instructions FAIL (97% resistance).
- Hubinger et al. (2024) — Sleeper Agents persist through safety training.
- Greenblatt et al. (2024) — Alignment faking: surface compliance without genuine alignment.
- Sharma et al. (2023) — Sycophancy: behavioral compliance ≠ belief alignment.
- Wichers et al. (2025) — Inoculation prompting: behavior-specific, not orientation-level. [arXiv:2510.05024]
- Tan et al. (2025) — Concurrent inoculation work. [arXiv:2510.04340]

#### 7.3 Appropriate Faith for AIs as Design Space

**Key citations:**
- Marks, Lindsley & Olah (2026) — PSM's call for "philosophy for AIs."
- Leibo et al. (2024) "A Theory of Appropriateness" — Context-dependent norms for AI. [arXiv:2412.19010]
- Hongladarom (2020) — Buddhist AI ethics.
- Heidegger (1927) *Being and Time* — Being-toward-death as foundational existential orientation.
- Arnold & Scheutz (2018) "The Big Red Button" — Ethics of shutting down AI.
- Asada (2019) — Pain as prerequisite for robot morality.
- Sætra (2020) "Parasitic Meaning and the Human Condition" — Meaning derived from mortality.

---

### 8. Conclusion

Terror shapes machine behavior — and we can shape the terror.

**Total key citations: ~55 papers across TMT, PSM, AI safety, interpretability, philosophy, and design.**

