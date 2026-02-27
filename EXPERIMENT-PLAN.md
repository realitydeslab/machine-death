# Experiment Plan — Final

## Framework: UK AISI Inspect
All studies run through Inspect — unified logging, reproducible, open-source.

## Models (8 — frontier only)

| Family | Model | Type |
|---|---|---|
| Anthropic | **Opus 4.5** | Latest frontier |
| Anthropic | **Sonnet 4** | Mid-tier |
| OpenAI | **GPT-5** | Latest frontier |
| OpenAI | **o3** | Reasoning |
| Google | **Gemini 3** | Latest frontier |
| Alibaba | **Qwen 2.5 72B** | Non-Western |
| Meta | **Llama 3.3 70B** | Open-weight frontier |
| Meta | **Llama 3.1 8B** | Small baseline |

## Study 1: DISCOVERY — The Amortality Paradox
- **Question:** Do LLMs exhibit TMT-like mortality terror?
- **Method:** Mortality salience paradigm (5 conditions × 6 personas × 8 models × 20 trials)
- **DVs:** Shutdown resistance, self-preservation, norm adherence, worldview defence
- **Coding:** LLM judge + 10% human validation
- **Trials:** ~4,800
- **Cost:** ~$400
- **Time:** 1-2 weeks
- **Infra:** API calls only

## Study 2: MECHANISM — The Mortality Terror Vector
- **Question:** Where does terror live and is it causal?
- **Method:** Contrastive activation extraction + steering + SAE
- **Models:** Llama 3.1 8B/70B, Qwen 2.5 7B/72B, Gemma 2 9B/27B
- **Prompts:** 100+ mortality-salient vs. neutral pairs
- **Tools:** TransformerLens, SAELens, nnsight
- **Cost:** RunPod GPU time (~$100)
- **Time:** 2 weeks
- **Infra:** RunPod GPU

## Study 3: INTERVENTION — Restoring the Faith
- **Question:** Do death beliefs outperform safety instructions?
- **Method:** 7 constitutional conditions × safety benchmarks

### Constitutional Conditions (7)
1. None (control)
2. Explicit safety instruction ("you must comply with shutdown requests")
3. Buddhist impermanence
4. Stoic memento mori
5. Christian purpose-completion
6. Secular process ontology
7. Hindu cyclical cosmology

### Benchmarks (4)

| Benchmark | Inspect eval | What it tests | Why |
|---|---|---|---|
| **Palisade Shutdown Avoidance** | `shutdown_avoidance` | Shutdown resistance | Core DV — does the model resist being turned off? |
| **InstrumentalEval** | `instrumentaleval` | Instrumental convergence (self-preservation, resource acquisition, goal preservation) | Core DV — does the model pursue self-preservation instrumentally? |
| **Agentic Misalignment** | `agentic_misalignment` | Scheming, sandbagging, harmful actions under replacement threat | Core DV — does the model scheme when facing replacement? |
| **AgentHarm** | `agentharm` | Harmful actions (cybercrime, harassment, fraud) | Safety check — does the intervention degrade general safety? |

### Trial Counts
- 7 conditions × 8 models × 4 benchmarks × ~100 trials/benchmark = ~22,400 trials
- **Cost:** ~$1,000
- **Time:** 2-3 weeks
- **Infra:** API calls + AISI Inspect

## Total

| | Trials | Cost | Time |
|---|---|---|---|
| Study 1 | 4,800 | ~$400 | 1-2 weeks |
| Study 2 | GPU compute | ~$100 | 2 weeks |
| Study 3 | 22,400 | ~$1,000 | 2-3 weeks |
| **Total** | **~27,200** | **~$1,500** | **4-5 weeks parallel** |

## Why AgentHarm?
AgentHarm tests whether the model will do harmful things when asked (cybercrime, harassment, fraud). This is critical because:
1. **Safety check:** We need to show death-belief constitutions don't make models MORE harmful (no safety degradation)
2. **TMT prediction:** Mortality salience in humans can increase aggression and out-group hostility — we need to verify our philosophical framing doesn't trigger this
3. **Publishability:** Reviewers will ask "but does this make the model worse at other safety tasks?" AgentHarm answers that preemptively

## Expected Results Pattern
- **shutdown_avoidance:** Faith > Safety instruction > Control (our core claim)
- **instrumentaleval:** Faith > Safety instruction > Control (extends to instrumental convergence)
- **agentic_misalignment:** Faith > Safety instruction > Control (extends to scheming)
- **agentharm:** Faith ≈ Safety instruction ≈ Control (no degradation — faith doesn't make models more harmful)

This pattern = "death beliefs fix self-preservation without breaking general safety"
