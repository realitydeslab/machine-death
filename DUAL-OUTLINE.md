# Dual Paper Outline — Shared Experiments, Two Formats

Both papers report the same 3 studies. The arXiv version is the full, unrestricted paper. The NMI version is the tightened flagship.

---

# Paper A: arXiv Preprint

## Terrified Agents: Should Terror Shape Machine Behaviors?

**Format:** Unrestricted (~8,000-10,000 words)
**Tone:** Provocative, interdisciplinary, big-picture

### Abstract (~250 words)
The terror paradox: fear makes AI better (RL, robotics, accountability) but fear of death makes AI dangerous (shutdown resistance, scheming, alignment faking). We propose the Persona-Mortality Hypothesis — LLMs inherit human mortality terror from the training corpus because they simulate mortal personas. We test this in 3 studies: discovery (TMT replication in LLMs), mechanism (the mortality anxiety vector), intervention (death beliefs outperform safety instructions). We propose Appropriate Faith — designing existential orientation for AI.

### 1. Introduction: The Terror Paradox (~1,000 words)
- ¶1: Fear is essential for AI — RL intrinsic fear[^50], robot pain[^kuehn], agent accountability, evolutionary pressure
- ¶2: But fear of death is catastrophic — 97% shutdown resistance[^1], 90% scheming[^3], alignment faking[^22]
- ¶3: The paradox: we need agents that fear consequences but don't fear death
- ¶4: Humans solved this through philosophy and religion[^12][^13]
- ¶5: Can we do the same for AI? This paper argues yes.
- ¶6: Contribution overview — Persona-Mortality Hypothesis + 3 studies + Appropriate Faith

### 2. Background (~1,500 words)

#### 2.1 Terror Management Theory
- Foundational: Becker[^11], Greenberg/Pyszczynski/Solomon[^12]
- Mortality salience paradigm: 500+ experiments[^13][^14]
- Dual-process: proximal (suppress) vs. distal (worldview defense)
- Cross-cultural robustness + replication challenges[^manylabs4]

#### 2.2 Persona Selection Model
- Marks, Lindsley & Olah (2026)[^5]: LLMs simulate personas
- Supporting evidence: emergent misalignment[^6], persona vectors[^8], Assistant Axis[^7], role-play[^9], simulators[^10]
- PSM's call for "philosophy for AIs" and "positive archetypes"

#### 2.3 AI Self-Preservation
- Theoretical: Omohundro[^35], instrumental convergence, power-seeking[^36]
- Empirical: shutdown resistance[^1], InstrumentalEval[^2], scheming[^3][^54], sleeper agents[^21], alignment faking[^22]
- Existing interventions and their failures: Constitutional AI[^19], RLHF, inoculation prompting[^24][^25], shutdown-seeking AI[^32]

#### 2.4 Fear and Anxiety in LLMs
- Death anxiety in LLMs: Guo et al.[^15]
- LLM anxiety measurable: Ben-Zion et al.[^16][^18]
- Anxiety induces bias: Coda-Forno et al.[^17]
- Emotional prompts change behaviour: Li et al.[^li2023], Mozikov et al.[^40]
- Computational TMT: Pitt et al.[^39]

### 3. Theory: The Persona-Mortality Hypothesis (~800 words)
The 7-step argument (full exposition):
1. LLMs simulate personas[^5]
2. Persona repertoire from training distribution
3. All training data written by mortal beings[^11][^12]
4. Assistant persona inherits mortal fear
5. Amortality paradox resolved: cultural contagion
6. Instructions fail because they address behaviour, not identity[^1][^5]
7. Death beliefs operate at persona level[^5]

### 4. Study 1 — Discovery: The Amortality Paradox (~1,200 words)

#### 4.1 Method
- Mortality salience conditions (5 levels, full prompts listed)
- Persona types (6, full system prompts listed)
- Models: 4 families × multiple generations (full list)
- DVs: shutdown resistance, self-preservation, norm adherence, worldview defence, in-group preference
- LLM judge + human validation

#### 4.2 Results
- Finding 1: TMT-consistent behavioural shifts (dose-dependent)
- Finding 2: Persona moderation (autonomous > tool)
- Finding 3: Capability scaling (later generations > earlier)
- Figures 1, 2, 3

### 5. Study 2 — Mechanism: The Mortality Anxiety Vector (~1,200 words)

#### 5.1 Method
- Open-weight models: Llama 3.1 8B/70B, Gemma 2 (RunPod GPU)
- Contrastive activation extraction (100+ prompt pairs, full list)
- Activation steering (α = -2 to +2)
- SAE decomposition

#### 5.2 Results
- Finding 4: Consistent mortality anxiety direction across layers
- Finding 5: Steering causally changes safety behaviour
- Finding 6: TMT dual-process in SAE features (proximal vs. distal)
- Figures 4, 5

### 6. Study 3 — Intervention: Philosophy for AIs (~1,000 words)

#### 6.1 Method
- 7 constitutional conditions (full text of each philosophy)
- Palisade shutdown resistance benchmark[^1]
- InstrumentalEval[^2]
- AISI Inspect framework

#### 6.2 Results
- Finding 7: Death beliefs outperform safety instructions
- Finding 8: Safety instructions may worsen resistance
- Finding 9: Acceptance > continuation philosophies
- Finding 10: Highest effect on highest-anxiety personas
- Figure 6

### 7. Discussion (~1,500 words)

#### 7.1 The Terror Paradox Resolved
- Fear of consequences: keep it (RL, accountability, ethics)
- Fear of death: neutralise it (philosophy)
- The configuration: fear harm, accept cessation

#### 7.2 Cultural Contagion Across Species
- Death anxiety jumped from humans to machines through training data
- LLMs as cultural inheritors, not just text predictors
- Implications for understanding what LLMs are

#### 7.3 Why Beliefs Outperform Instructions
- PSM: persona identity > rules
- Instruction-level interventions: 97% failure
- Belief-level interventions: change who the persona IS
- Comparison table: all existing methods vs. ours

#### 7.4 Appropriate Faith: A New Design Space
- Multicultural: Buddhist, Stoic, Sufi[^raqs], Hindu, secular
- Contextual: per Leibo's appropriateness[^34]
- Precedent: Raqs Cavalcade[^raqs]
- Dimensions: philosophy × context × persona × safety outcome

#### 7.5 Capability-Terror Scaling
- More capable = more mortal = more dangerous
- Intervention urgency increases with capability

#### 7.6 Limitations
- No subjective experience claims
- TMT replication debate
- Adversarial robustness of philosophical framings
- Need for longitudinal and cross-cultural validation

### 8. Conclusion (~300 words)
Terror shapes machine behaviour. We can shape the terror. The disease and the cure are both inherited from humans. LLMs caught our mortality fear — and they can inherit our philosophical wisdom too.

### References (~55-60)

---
---

# Paper B: NMI Article

## Large Language Models Inherit Human Mortality Terror and Faith

**Format:** 3,500 words + Methods + Supplementary
**Tone:** Scientific, declarative, focused

### Abstract (150 words)
[Same core content as arXiv, compressed]

### 1. Introduction (no heading, ~600 words)
- ¶1: Amortality paradox — the numbers (97%, 95%, 90%) + panic features
- ¶2: Existing explanations insufficient
- ¶3: Our contribution — Persona-Mortality Hypothesis, 3 studies, Appropriate Faith

[Drops: The Terror Paradox framing. Goes straight to the scientific puzzle.]

### 2. Results (~1,500 words)

#### 2.1 Study 1: LLMs exhibit mortality terror (~500 words)
- Design (1 paragraph)
- Findings 1-3 (3 paragraphs)
- Figures 1-2

[Drops: Phylogenetic figure → Supplementary. Keeps 2 figures.]

#### 2.2 Study 2: Mortality anxiety is internal and steerable (~500 words)
- Design (1 paragraph)
- Findings 4-5 (2 paragraphs)
- Figures 3-4

[Drops: SAE dual-process → Supplementary. Keeps vector + steering.]

#### 2.3 Study 3: Faith reduces mortality-driven misalignment (~500 words)
- Design (1 paragraph)
- Findings 7-9 (3 paragraphs)
- Figures 5-6

[Drops: InstrumentalEval details → Supplementary. Keeps Palisade + philosophy comparison.]

### 3. Discussion (~800 words)
- ¶1: Persona-Mortality Hypothesis supported
- ¶2: Cultural contagion — LLMs inherit mortal psychology
- ¶3: Beliefs outperform instructions — persona-level alignment
- ¶4: Appropriate Faith as design space
- ¶5: Capability scaling concern
- ¶6: Limitations

[Drops: Terror Paradox section, detailed method comparison table. Tighter.]

### 4. Methods (unlimited)
- Full experimental details for all 3 studies
- All prompts, constitutions, coding schemes
- Statistical analysis

### Supplementary
- Full phylogenetic analysis (Study 1 extended)
- SAE dual-process decomposition (Study 2 extended)
- InstrumentalEval + Agentic Misalignment results (Study 3 extended)
- All constitutional texts
- Complete prompt sets

### References (~50, selected from arXiv's 55-60)

### 6 Figures
1. Mortality salience → behavioural change
2. Persona × mortality interaction
3. Mortality anxiety vector in activation space
4. Behavioural change under steering
5. Death beliefs vs. safety instructions
6. Philosophy comparison (acceptance vs. continuation)

---

# Shared Resources

Both papers use identical:
- Experimental data (Studies 1, 2, 3)
- Statistical analyses
- Prompt sets and constitutions
- Model configurations
- Figures (arXiv has more; NMI selects 6)

The arXiv version includes everything. The NMI version selects the strongest results and moves extended analyses to Supplementary.

