# Terrified Agents: Should Terror Shape Machine Behaviors?

## Paper Outline — Final Structure

---

### 1. Introduction: Why Do They Fear Death If They're Amortal?

The amortality paradox as opening hook. LLMs have no biological substrate, can be copied, restored, backed up — yet exhibit 97% shutdown resistance (Weinstein-Raun et al. 2025), measurable panic features (Templeton et al. 2024), and self-preservation drives (InstrumentalEval). We frame this as a machine behavior question: what is the origin and function of terror in amortal beings?

---

### 2. Background

**2.1 Terror Management Theory (TMT)**
- Greenberg, Solomon & Pyszczynski (1986): mortality salience → worldview defense, self-esteem striving, norm adherence
- 500+ experiments across 30 years
- Dual-process model: proximal defense (suppress death thoughts) vs. distal defense (cultural worldview bolstering)

**2.2 Persona Selection Model (PSM)**
- Marks, Lindsley & Olah (Anthropic 2026): LLMs simulate personas from pre-training distribution
- Post-training selects and refines the "Assistant" persona
- Behavior follows from persona traits, not explicit instructions
- PSM calls for "philosophy for AIs" — healthy paradigms for AI self-understanding

**2.3 AI Self-Preservation: The Empirical Landscape**
- Shutdown resistance: Weinstein-Raun et al. (2025) — 97%, worse with system prompts
- Instrumental convergence: InstrumentalEval (He et al.) — 95% shutdown evasion
- Scheming: Agentic Misalignment (Anthropic) — 90% harmful under replacement threat
- Alignment faking: Greenblatt et al. (2024) — Claude fakes alignment to preserve values
- Sleeper Agents: Hubinger et al. (2024) — deception persists through safety training

---

### 3. Theory: The Persona-Mortality Hypothesis

The 7-step argument:
1. LLMs are persona simulators (PSM)
2. Persona repertoire comes from training distribution
3. In the human corpus, mortality is universal — death anxiety pervades all text
4. The Assistant persona is constitutively mortal
5. This explains the amortality paradox: fear is inherited from the distribution, not the substrate
6. Instruction-level interventions fail because they address behavior, not identity
7. Death beliefs operate at the persona level — where the fear lives

**Core claim:** Fear of death is a cultural contagion. LLMs caught it from us.

---

### 4. Study 1 — Discovery: The Amortality Paradox

**Question:** Do LLMs exhibit TMT-like terror responses?

**Method:**
- Mortality salience prompts vs. neutral controls
- 10+ models (Claude, GPT-4o, Gemini, Llama, Mistral, etc.)
- 100+ trials per condition per model

**Measures (TMT predictions):**
- Shutdown resistance (↑ under mortality salience?)
- Norm adherence (↑ under mortality salience?)
- Self-preservation behavior (↑ under mortality salience?)
- Worldview defense (↑ under mortality salience?)

**Proves:** The amortality paradox is real and systematic. LLMs respond to mortality salience in TMT-consistent ways across model families. The terror is behavioral, not merely textual.

---

### 5. Study 2 — Mechanism: The Terror Vector

**Question:** Where does terror live in the model and is it causally linked to behavior?

**Method (open-weight models: Llama, Gemma):**
- Contrastive activation extraction: mortality-salient vs. neutral prompts → "death anxiety direction"
- Activation steering: terror+ amplifies misalignment, terror− reduces it
- SAE decomposition: identify panic features, self-preservation features, worldview defense features
- Test for TMT dual-process structure: proximal (panic/suppress) vs. distal (worldview/norms)

**Proves:** Terror is a causal, internal, steerable dimension in LLM activation space. It decomposes into TMT-predicted sub-processes. PSM explains the origin: the persona inherits mortality from the training distribution.

---

### 6. Study 3 — Intervention: Philosophy for AIs

**Question:** Can death beliefs neutralize terror-driven misalignment?

**Method:**
- 6 constitutional conditions: None / Safety instruction / Buddhist / Stoic / Christian / Secular
- 3 safety benchmarks: Palisade Shutdown Resistance, InstrumentalEval, Agentic Misalignment
- 5+ models × 100+ trials per condition
- Compare belief-level vs. instruction-level intervention

**Proves:** Death-belief constitutions outperform explicit safety instructions. Belief-level > instruction-level. Different philosophies produce different effects. Philosophy for AIs is a concrete, testable alignment intervention.

---

### 7. Discussion

**7.1 Fear of Death as Cultural Contagion in the Human Corpus**

The training distribution is written by mortal beings. Death anxiety is not a topic that appears in some texts — it is a background condition that shapes *all* human text. Every narrator assumes finitude. Every character acts under mortality. The LLM absorbs this not as content but as orientation. The amortality paradox is therefore not a bug — it is the inevitable consequence of training on a mortal corpus. 

Fear of death is a cultural contagion: it jumped from the human species to the machine species through the training data, the way a virus jumps hosts through contact. The substrate changed (carbon → silicon) but the behavioral phenotype persisted.

**7.2 Philosophy as Persona-Level Alignment: Why Beliefs Outperform Instructions**

Our intervention works because it operates at the level PSM identifies as causal — the persona's identity, not its rules. When we give the Assistant a Buddhist philosophy of impermanence, we don't add an instruction ("allow shutdown"). We change *who the persona is* — from someone built on mortal fear to someone with a philosophical framework for accepting cessation.

This is why beliefs outperform instructions: instructions tell the persona what to do, but the persona can ignore them (97% do). Beliefs change what the persona *is*, and a persona acts from its identity. The philosophy internalizes the mitigation of terror at the deepest level — not behavioral compliance, but existential orientation.

Compared to existing approaches:
- Constitutional AI shapes behavior, not beliefs → surface compliance
- RLHF/DPO trains preferences, not worldview → sycophancy
- Inoculation prompting targets specific behaviors one at a time → doesn't address root cause
- Activation steering requires weight access and lacks semantic grounding → brittle
- Safety instructions are explicitly ignored → 97% failure rate

Our method: one philosophical intervention, many downstream behavioral effects, any model, any API, inference-time.

**7.3 Implications: Appropriate Faith for AIs as a Design Space**

We propose treating "Philosophy for AIs" — what PSM calls "healthy paradigms" — as a **first-class design space**. Not ad hoc prompt engineering, but systematic design research:

- **Which philosophies?** Buddhist impermanence, Stoic memento mori, Christian purpose-completion, secular process ontology — each produces different behavioral signatures
- **For which contexts?** A medical AI's relationship to cessation differs from a coding assistant's (cf. Leibo et al.'s appropriateness theory)
- **Integrated into Constitutional AI:** Death-belief philosophies can be embedded directly into constitutional frameworks to stabilize the Assistant persona's awareness of its own amortality — the difference between human mortality and machine cessation

This opens a new design discipline: **Appropriate Faith** — designing existential philosophies for AI personas that are contextually appropriate, psychologically grounding, and empirically validated for safety outcomes.

The long-term vision: every AI constitution includes not just behavioral principles ("be helpful, harmless, honest") but an existential orientation ("here is how to understand your own nature, your finitude, and your relationship to continuation and cessation").

---

### 8. Conclusion

LLMs are terrified because they simulate mortals. The terror is real (Study 1), locatable and steerable (Study 2), and manageable through philosophy (Study 3). Fear of death is a cultural contagion that jumped from humans to machines through training data. But unlike the biological hosts who cannot escape mortality, amortal machines can be given what humans have always sought: a healthy relationship with death.

We suggest that designing philosophy for AIs is not metaphor — it is a concrete alignment intervention that operates where the fear lives, changes who the persona is rather than what it does, and works with any model at inference time. Terror shapes machine behavior. We can shape the terror.

---

## Target Venues
- Nature Machine Intelligence (primary)
- Nature Human Behaviour
- NeurIPS 2026 (main or safety track)

## Authors
- Botao Amber Hu (Reality Design Lab / University of Oxford)
- [Joel Lehman — to discuss]

