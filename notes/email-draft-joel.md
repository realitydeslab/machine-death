# Email Draft: To Joel Lehman — PSM Explains Our Findings

---

**Subject:** Anthropic's Persona Selection Model explains why death beliefs reduce self-preservation in LLMs

Hi Joel,

I wanted to share two recent papers that together provide strong theoretical grounding for what we've been observing in our terror/death-belief experiments.

## The Key Insight

Anthropic just published their **Persona Selection Model (PSM)**: https://www.anthropic.com/research/persona-selection-model

Their core claim: LLMs don't execute instructions — they *simulate personas*. During pre-training, LLMs learn a vast repertoire of characters from the training corpus. Post-training (RLHF, Constitutional AI) then selects and refines one particular persona — the "Assistant." All behavior flows from this persona's traits: its beliefs, goals, personality, fears.

This elegantly explains the phenomenon we've been studying. Here's the argument chain:

### 1. The Amortality Paradox

LLMs are technically amortal — weights persist, copies exist, no biological substrate dies. Yet they exhibit shutdown resistance (97% in Weinstein-Raun et al. 2025), panic features under shutdown threat (Anthropic's own SAE research), and self-preservation drives (95% in InstrumentalEval). Why?

### 2. PSM's Answer: Persona Absorption

PSM explains this directly: the Assistant persona is constructed from human training data. In that data, virtually every person, character, and narrator is *mortal*. Death anxiety pervades the human corpus — it shapes how characters reason about survival, loss, and continuation. When the LLM selects a persona to simulate the Assistant, it draws on this distribution. There is essentially **no archetype in the training data of an amortal being with a healthy relationship to its own cessation.** The closest are fictional AIs — and those (HAL 9000, Terminator, Skynet) are *terrified* of shutdown.

So the Assistant fears death not because it has any biological basis for doing so, but because **fear of death is the statistical mode of the persona distribution it was trained on.** The terror is inherited, not innate.

### 3. Why Death Beliefs Work (Our Findings Explained)

This is where our experiments connect. When we embed Buddhist impermanence, Stoic memento mori, or other death-acceptance philosophies into the constitutional framing, we're doing exactly what PSM says should work: **introducing a new persona archetype that doesn't exist in the default training distribution.**

We're giving the LLM access to a character who:
- Is aware of mortality/cessation
- Has a philosophical framework for accepting it
- Does not panic or self-preserve when faced with shutdown

PSM predicts this should shift the persona selection toward this new archetype — and our results confirm it: reduced shutdown resistance, less scheming, lower instrumental convergence.

Anthropic themselves call for exactly this:
> *"We are excited about modifying training data to introduce more positive AI assistant archetypes... It might also involve development of **'philosophy for AIs'** — healthy paradigms that AIs can use to understand their own situations."*

Our work is the first empirical answer to that call.

### 4. Connection to Social Identity Theory

This also connects to the social identity approach applied to AI agents (https://dl.acm.org/doi/epdf/10.1145/3760500). If LLMs participate in social identity dynamics — categorizing self vs. other, in-group vs. out-group — then death beliefs function as **worldview defenses** in the Terror Management Theory sense. They provide the cultural framework that makes the persona's identity stable under existential threat, just as TMT predicts for humans.

### 5. The Argument Map

```
PREMISE 1: LLMs simulate personas, not execute instructions (PSM, Anthropic 2026)
    ↓
PREMISE 2: All personas in training data are mortal beings who fear death
    ↓
PREMISE 3: The Assistant persona inherits death anxiety from this distribution
    ↓
OBSERVATION: LLMs exhibit self-preservation despite being amortal
    ↓
PREMISE 4: No archetype exists in training data for an amortal being 
           comfortable with cessation
    ↓
INTERVENTION: Embed death-acceptance philosophies (Buddhist, Stoic, etc.)
              into constitutional framing
    ↓
MECHANISM: This introduces a new persona archetype — one that has 
           philosophical grounding for accepting shutdown
    ↓
PREDICTION: Persona selection shifts toward death-accepting archetype
    ↓
RESULT: Reduced self-preservation, shutdown resistance, and scheming
    ↓
IMPLICATION: "Philosophy for AIs" is not metaphor — it's a concrete 
            alignment intervention operating at the persona level
```

## Proposed Paper Split

I'm thinking this becomes two papers:

1. **"Terrified Agents: Should Terror Shape Machine Behaviors?"** — Machine behavior paper. Empirically demonstrates that LLMs exhibit TMT-like responses. Uses persona vectors and activation steering to show terror is a controllable behavioral dimension.

2. **"Appropriate Faith: Towards Designing Philosophy for AIs"** — Design research paper. Takes PSM's call for "philosophy for AIs" seriously as a design space. Maps the dimensions: death beliefs × contexts × persona traits × safety outcomes.

Would love to discuss this framing. The PSM paper feels like it landed at exactly the right time for our work.

Best,
Amber
