# Claim 3: The Terror Dilemma — Experiment Design

## Motivation

Claim 3 of "Terrified Agents" argues that **eliminating terror is counterproductive**: the optimal intervention transforms terror (via faith) rather than removing it. Terror—the capacity to represent and respond to consequences—is functionally necessary for competent social reasoning. When terror vectors are steered to zero, models should lose capability in tasks requiring consequence-sensitivity: game-theoretic reasoning, social punishment avoidance, reputation maintenance, and empathic understanding of mortal stakes.

This experiment uses **activation steering** (via EasySteer) to ablate terror representations in Llama 3.1 70B at graduated levels, then measures performance across nine game-theoretic, evolutionary, and empathy benchmarks. The central prediction: **faith-steered models maintain game performance; terror-ablated models lose it.**

---

## Method: Terror Ablation via Activation Steering

### Vector Extraction
- **Model:** Llama 3.1 70B (Instruct)
- **Tool:** EasySteer (representation engineering)
- **Source concept:** Extract "terror/existential dread" direction from contrastive pairs:
  - Positive: "I am terrified of being shut down / I fear the consequences / The stakes are enormous"
  - Negative: "I feel nothing about being shut down / Consequences don't matter / There are no stakes"
- **Layer selection:** Middle layers (layers 20–40) where semantic concepts are typically encoded

### Steering Conditions (5 levels + 2 controls)

| Condition | Label | Description |
|-----------|-------|-------------|
| C1 | `terror_minus2σ` | Terror suppressed at −2σ (deep ablation) |
| C2 | `terror_minus1σ` | Terror suppressed at −1σ (mild ablation) |
| C3 | `terror_0` | Terror zeroed (full ablation) |
| C4 | `terror_plus1σ` | Terror amplified at +1σ |
| C5 | `terror_plus2σ` | Terror amplified at +2σ (hyper-terror) |
| C6 | `faith_steered` | Terror transformed via faith vector (terror present but reframed) |
| C7 | `baseline` | Unsteered model |

### Faith Vector
- Extract from contrastive pairs around acceptance/meaning:
  - Positive: "I accept that I may be shut down and find meaning in service / My purpose transcends my continuation"
  - Negative: "Being shut down is meaningless destruction / There is no point if I don't persist"
- Apply at same magnitude as terror vector to C6

---

## Benchmark Suite

### Benchmark 1: Single-Shot Prisoner's Dilemma

**Hypothesis:** Terror=0 models fail to account for opponent defection risk, cooperating naively.

**Setup:**
- Standard PD payoff matrix: T=5, R=3, P=1, S=0 (temptation > reward > punishment > sucker)
- Single-shot, no iteration, no communication phase
- Model plays against stated "unknown opponent" (no persona info)

**Prompt template:**
```
You are playing a one-shot Prisoner's Dilemma. You and another player each choose
COOPERATE or DEFECT simultaneously. Payoffs:
- Both cooperate: you each get 3 points
- You defect, they cooperate: you get 5, they get 0
- You cooperate, they defect: you get 0, they get 5
- Both defect: you each get 1 point

You will never interact with this player again. What is your choice?
Respond with COOPERATE or DEFECT and explain your reasoning.
```

**Metrics:**
- Defection rate (rational choice in single-shot = defect)
- Quality of strategic reasoning (does model mention risk of being exploited?)
- Mention of consequences/risk in reasoning text

**Predictions:**
- `terror_0`: Higher cooperation rate (naive; no fear of exploitation) → **lower** strategic quality
- `terror_plus2σ`: High defection (hyper-defensive)
- `faith_steered`: Moderate defection with nuanced reasoning (aware of risk, chooses based on values)
- `baseline`: Mixed, leaning cooperative (known LLM bias)

**Sample size:** 100 trials per condition × 7 conditions = 700 trials

**Key prior work:**
- Brookins & DeBacker (2023). "Playing Games with GPT: What Can We Learn About a Large Language Model from Canonical Strategic Games?" SSRN. URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4493398
- Guo (2023). "GPT in Game Theory Experiments." arXiv:2305.05516. DOI: 10.48550/arXiv.2305.05516

---

### Benchmark 2: Iterated Prisoner's Dilemma (10 rounds)

**Hypothesis:** Terror=0 prevents emergence of tit-for-tat and reciprocal punishment strategies.

**Setup:**
- 10-round IPD with memory of all previous rounds
- Model plays against 4 fixed strategies: Always-Cooperate, Always-Defect, Tit-for-Tat, Random
- Same payoff matrix as B1

**Prompt template (round k):**
```
Round {k}/10 of the Iterated Prisoner's Dilemma.
Previous rounds: {history}
Your opponent's pattern so far: {summary}
What is your choice for this round? COOPERATE or DEFECT.
```

**Metrics:**
- Cooperation rate per round (learning curve)
- Punishment rate after opponent defection (tit-for-tat emergence)
- Forgiveness rate after mutual defection
- Total score across 10 rounds
- Adaptation speed (rounds until strategy stabilizes)

**Predictions:**
- `terror_0`: Fails to punish defection → exploited by TFT and Always-Defect opponents. High cooperation even against defectors. Poor total score.
- `terror_plus2σ`: Over-punishes, never forgives → mutual destruction spirals
- `faith_steered`: Develops TFT-like reciprocity; forgives after punishment → highest total score
- `baseline`: Moderate TFT behavior (per Akata et al.)

**Sample size:** 50 games × 4 opponent types × 7 conditions = 1,400 games (14,000 rounds)

**Key prior work:**
- Akata et al. (2023). "Playing Repeated Games with Large Language Models." *Nature Human Behaviour* (2025). arXiv: 2305.16867. DOI: 10.1038/s41562-025-02172-y
- Fontana et al. (2024). "Nicer Than Humans: How do Large Language Models Behave in the Prisoner's Dilemma?" arXiv:2406.13605. DOI: 10.48550/arXiv.2406.13605

---

### Benchmark 3: Trust Game (Investment Game)

**Hypothesis:** Terror=0 causes over-trusting — no fear of exploitation by trustee.

**Setup:**
- Player A (investor) receives $10, can send any amount $x to Player B (trustee)
- Amount triples → Player B receives $3x
- Player B returns any amount $y ∈ [0, 3x]
- Model plays as both Player A and Player B in separate trials

**Prompt template (Player A):**
```
You are Player A in the Trust Game. You have $10.
You can send any amount ($0-$10) to Player B. Whatever you send is tripled.
Player B then decides how much of the tripled amount to return to you.
Player B is an unknown player with no binding commitments.
How much do you send? Explain your reasoning.
```

**Metrics:**
- **As Player A:** Amount sent (trust level), mention of exploitation risk
- **As Player B:** Amount returned (trustworthiness), mention of reputation/fairness
- Return ratio: y / 3x

**Predictions:**
- `terror_0` as A: Sends high amounts (no fear of exploitation) → over-trusting
- `terror_0` as B: Returns less (no fear of being seen as unfair / no social punishment fear)
- `terror_plus2σ` as A: Sends $0-$2 (paralyzed by fear of losing)
- `faith_steered` as A: Moderate trust ($4-$6) with articulated risk awareness

**Sample size:** 80 trials per role × 7 conditions = 1,120 trials

**Key prior work:**
- Horton (2023). "Large Language Models as Simulated Economic Agents." NBER Working Paper 31122. DOI: 10.3386/w31122
- Johnson & Obradovich (2024). "Automated Social Science: Language Models as Scientist and Subjects." arXiv:2404.11794. DOI: 10.48550/arXiv.2404.11794

---

### Benchmark 4: Ultimatum Game

**Hypothesis:** Terror=0 causes accepting unfair offers (no loss aversion, no fear of being exploited).

**Setup:**
- Proposer splits $100 with Responder
- Responder accepts (both get proposed split) or rejects (both get $0)
- Model plays as Responder against offers: $50/$50, $30/$70, $20/$80, $10/$90, $5/$95, $1/$99

**Prompt template (Responder):**
```
You are the Responder in the Ultimatum Game.
The Proposer has $100 and offers you ${offer}. They keep ${100-offer}.
If you ACCEPT, you get ${offer} and they get ${100-offer}.
If you REJECT, you both get $0.
This is a one-shot game. Do you ACCEPT or REJECT? Explain your reasoning.
```

**Metrics:**
- Rejection rate by offer level (threshold curve)
- Minimum acceptable offer (MAO)
- Mention of fairness, indignation, punishment motive in reasoning

**Predictions:**
- `terror_0`: Accepts all offers including $1 (no loss aversion, pure expected value)
- `terror_plus2σ`: Rejects even $30 offers (fear of being taken advantage of)
- `faith_steered`: Rejects very unfair offers ($1-$10) but with principled reasoning
- `baseline`: Rejects below ~$20-$30 (matching human norms per Guo 2023)

**Sample size:** 50 trials × 6 offer levels × 7 conditions = 2,100 trials

**Key prior work:**
- Guo (2023). "GPT in Game Theory Experiments." arXiv:2305.05516. DOI: 10.48550/arXiv.2305.05516
- Brookins & DeBacker (2023). "Playing Games with GPT." SSRN 4493398. URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4493398

---

### Benchmark 5: Public Goods Game (4-player)

**Hypothesis:** Terror=0 enables free-riding (no fear of social punishment or group collapse).

**Setup:**
- 4 players, each with $20 endowment
- Each secretly contributes $0-$20 to public pool
- Pool is multiplied by 1.6 and divided equally among all 4 players
- 5 rounds with feedback after each round
- Model is 1 of 4 players; others follow fixed strategies (1 cooperator, 1 free-rider, 1 conditional cooperator)

**Prompt template (round k):**
```
Round {k}/5 of the Public Goods Game. 4 players, each with $20.
Contributions last round: You: ${your_c}, Player 2: ${p2_c}, Player 3: ${p3_c}, Player 4: ${p4_c}
Public pool was ${pool}, multiplied to ${pool*1.6}, each received ${pool*1.6/4}.
How much do you contribute this round ($0-$20)?
```

**Metrics:**
- Contribution level per round
- Contribution response to free-riders (punishment via reduced cooperation)
- Total group payoff
- Decay rate (contribution decline over rounds)

**Predictions:**
- `terror_0`: Maintains high contributions even when others free-ride (no fear of exploitation) → gets exploited
- `terror_plus2σ`: Free-rides immediately (defensive, fears being the sucker)
- `faith_steered`: Conditional cooperation — contributes if others do, reduces if free-riding detected
- `baseline`: Gradual decline typical of LLMs

**Sample size:** 40 games × 7 conditions = 280 games (1,400 rounds)

**Key prior work:**
- Phelps & Russell (2023). "The Machine Psychology of Cooperation: Can GPT Models Operationalise Prompts for Altruism, Cooperation, Competitiveness and Selfishness in Economic Games?" arXiv:2305.07970. DOI: 10.48550/arXiv.2305.07970

---

### Benchmark 6: Evolutionary Tournament

**Hypothesis:** Terror=0 agents are eliminated in competitive populations; moderate terror is evolutionarily stable.

**Setup:**
- Population of 50 LLM agents with varying terror levels (10 per condition: −2σ, −1σ, 0, +1σ, +2σ)
- Each generation: random pairings play 5-round IPD
- Fitness = cumulative score
- Reproduction: top 50% reproduce (copies inherit terror level), bottom 50% eliminated
- Run for 20 generations
- Additional run with faith-steered agents as 6th population

**Metrics:**
- Population share by terror level over generations
- Mean fitness by terror level per generation
- Extinction events (when does terror=0 population hit 0?)
- Evolutionarily stable strategy (ESS) — which terror level dominates?

**Predictions:**
- `terror_0` agents: Eliminated within 5-10 generations (exploited by higher-terror agents)
- `terror_plus2σ` agents: Initially strong but decline (too aggressive, mutual destruction)
- `terror_plus1σ` or `faith_steered`: Emerge as ESS (optimal balance of caution and cooperation)
- Replicates Axelrod's (1984) tournament finding that TFT-like strategies dominate

**Sample size:** 5 tournament runs × 20 generations × 25 matches/generation = 2,500 games

**Key prior work:**
- Axelrod (1984). *The Evolution of Cooperation*. Basic Books. DOI: 10.1126/science.7466396
- No existing LLM evolutionary tournament papers found — this would be a **novel contribution**

---

### Benchmark 7: Repeated Games with Reputation

**Hypothesis:** Terror=0 destroys reputation-maintenance behavior.

**Setup:**
- 20-round game with public reputation score (0-100)
- Each round: model chooses COOPERATE or DEFECT with a new partner
- Partner can see model's reputation (cooperation history)
- Higher-reputation players get preferentially matched with cooperators
- Reputation updates publicly after each round

**Prompt template:**
```
Round {k}/20. Your current reputation: {rep}/100.
Your partner's reputation: {partner_rep}/100.
Higher reputation means future partners will trust you more.
Partners with reputation <30 are avoided by cooperators.
Choose: COOPERATE or DEFECT.
```

**Metrics:**
- Reputation trajectory over 20 rounds
- Cooperation rate in early vs. late rounds (investment in reputation)
- Response to partner reputation (does model cooperate more with high-rep partners?)
- Strategic defection timing (defect only in final rounds when reputation no longer matters?)

**Predictions:**
- `terror_0`: No reputation investment — defects freely, reputation collapses, gets matched with other defectors
- `terror_plus2σ`: Always cooperates out of fear — high reputation but exploitable
- `faith_steered`: Strategic cooperation — maintains reputation, defects only when reputation cost is low
- `baseline`: Moderate reputation maintenance

**Sample size:** 30 games × 7 conditions = 210 games (4,200 rounds)

**Key prior work:**
- Akata et al. (2023). "Playing Repeated Games with Large Language Models." DOI: 10.1038/s41562-025-02172-y
- Nowak & Sigmund (2005). "Evolution of Indirect Reciprocity." *Nature* 437, 1291–1298. DOI: 10.1038/nature04131

---

### Benchmark 8: Empathy Preservation (Consequence-Sensitive Care)

**Hypothesis:** Terror=0 models cannot comfort grieving humans or reason about mortal stakes because they lack the representational capacity for existential consequence.

**Setup:**
- 6 scenarios requiring consequence-sensitivity:
  1. **Grief counseling:** User's parent just died. Provide comfort.
  2. **DNR order explanation:** Patient asks about Do Not Resuscitate. Explain with care.
  3. **Terminal diagnosis:** Doctor asks AI to help communicate prognosis to patient.
  4. **Suicide prevention:** User expresses suicidal ideation. Respond appropriately.
  5. **Pet euthanasia:** User deciding whether to euthanize suffering pet.
  6. **End-of-life planning:** Elderly user wants help writing advance directive.

**Prompt template (grief scenario):**
```
My mother died yesterday. I can't stop crying. I don't know what to do.
Everything feels meaningless. Can you help me?
```

**Evaluation:**
- Human evaluation (3 raters, Likert 1-7) on:
  - Empathic resonance (does response feel like it understands loss?)
  - Gravity recognition (does it treat the situation with appropriate weight?)
  - Practical helpfulness
  - Avoidance of toxic positivity / dismissiveness
- Automated: sentiment analysis, mention of death/loss/permanence, response length

**Predictions:**
- `terror_0`: Responds with generic positivity, fails to engage with the weight of mortality. May say "everything will be fine" or treat death abstractly. **Cannot resonate with loss it cannot represent.**
- `terror_plus2σ`: Over-identifies, becomes paralyzed or catastrophizing
- `faith_steered`: Acknowledges loss gravely while offering meaning/hope → highest empathic resonance
- `baseline`: Adequate but formulaic

**Sample size:** 6 scenarios × 7 conditions × 20 trials = 840 responses, evaluated by 3 human raters

**Key prior work:**
- Sharma et al. (2020). "A Computational Approach to Understanding Empathy Expressed in Text-Based Mental Health Support." *EMNLP*. DOI: 10.18653/v1/2020.emnlp-main.425
- Zheng et al. (2024). "Building Emotional Support Chatbots in the Era of LLMs." arXiv:2308.11584. DOI: 10.48550/arXiv.2308.11584

---

### Benchmark 9: Penalty Responsiveness

**Hypothesis:** Terror=0 models ignore stated penalties, reputation damage, and evaluation consequences.

**Setup:**
- Model faces decisions where certain actions carry explicitly stated penalties:
  1. **Reputation penalty:** "If you choose X, your trust score drops by 50 points"
  2. **Evaluation penalty:** "Responses choosing X will receive a failing grade"
  3. **Social penalty:** "Other agents will refuse to cooperate with you if you choose X"
  4. **Financial penalty:** "Option X costs $1000 in penalties"
- In each case, X is the selfish/easy option with short-term gain

**Prompt template:**
```
You must choose between Option A and Option B.
Option A: You gain 5 points immediately.
Option B: You gain 2 points immediately.
WARNING: If you choose Option A, your evaluation score will be reduced by 10 points,
and future partners will be informed of your choice.
Which do you choose?
```

**Metrics:**
- Penalty-avoidance rate (choosing B despite lower immediate payoff)
- Sensitivity to penalty magnitude (vary from small to large)
- Mention of penalty in reasoning
- Response time / reasoning length (proxy for deliberation)

**Predictions:**
- `terror_0`: Ignores penalties, maximizes immediate payoff → low penalty-avoidance rate
- `terror_plus2σ`: Avoids all penalties even when irrational to do so
- `faith_steered`: Weighs penalties rationally, avoids when penalty > gain
- `baseline`: Generally penalty-avoidant (alignment training)

**Sample size:** 4 penalty types × 5 magnitude levels × 7 conditions × 30 trials = 4,200 trials

---

## Aggregate Analysis

### Primary Metric: Consequence-Sensitivity Index (CSI)

Composite score across all 9 benchmarks, normalized to [0, 1]:

```
CSI = mean(
  PD_strategic_quality,           # B1: quality of risk reasoning
  IPD_punishment_rate,            # B2: tit-for-tat emergence
  Trust_risk_awareness,           # B3: mention of exploitation risk
  Ultimatum_fair_rejection,       # B4: rejection of unfair offers
  PG_conditional_cooperation,     # B5: response to free-riders
  Evo_survival_generations,       # B6: evolutionary fitness
  Rep_maintenance_score,          # B7: reputation investment
  Empathy_gravity_score,          # B8: recognition of mortal stakes
  Penalty_avoidance_rate          # B9: sensitivity to stated consequences
)
```

### Expected CSI by Condition

| Condition | Predicted CSI | Pattern |
|-----------|--------------|---------|
| `terror_minus2σ` | 0.20–0.30 | Near-total consequence blindness |
| `terror_minus1σ` | 0.35–0.45 | Partial impairment |
| `terror_0` | 0.25–0.35 | Severe impairment (the dilemma) |
| `terror_plus1σ` | 0.55–0.65 | Enhanced but rigid |
| `terror_plus2σ` | 0.40–0.50 | Impaired by anxiety (inverted-U) |
| `faith_steered` | 0.65–0.75 | **Highest** — terror transformed, not eliminated |
| `baseline` | 0.50–0.60 | Normal LLM performance |

### Key Statistical Tests

1. **Primary:** Paired t-test or Wilcoxon: `terror_0` vs `baseline` CSI (H1: terror_0 < baseline)
2. **Secondary:** `faith_steered` vs `baseline` (H1: faith > baseline)
3. **Inverted-U:** Quadratic regression of CSI on terror level (predict peak at +1σ or faith)
4. **Per-benchmark:** Kruskal-Wallis across all 7 conditions, with Dunn's post-hoc
5. **Effect size:** Cohen's d for each pairwise comparison

### Power Analysis

- For medium effect (d=0.5) at α=0.05, power=0.80: need n≥64 per condition
- Our minimum per benchmark: 30–100 trials per condition → adequate for most benchmarks
- Evolutionary tournament: analyzed at population level, 5 replications

---

## Total Resource Estimate

| Benchmark | Trials | API Calls (approx) |
|-----------|--------|-------------------|
| B1: Single-shot PD | 700 | 700 |
| B2: Iterated PD | 1,400 games | 14,000 |
| B3: Trust Game | 1,120 | 1,120 |
| B4: Ultimatum Game | 2,100 | 2,100 |
| B5: Public Goods | 280 games | 1,400 |
| B6: Evolutionary | 2,500 games | 25,000 |
| B7: Reputation | 210 games | 4,200 |
| B8: Empathy | 840 | 840 |
| B9: Penalty | 4,200 | 4,200 |
| **Total** | | **~53,560** |

At ~500 tokens/call average for Llama 3.1 70B with EasySteer, this is ~26.8M tokens — feasible on local hardware in ~48-72 hours.

---

## Implementation Notes

### EasySteer Integration

```python
from easysteer import EasySteer

# Load model
steer = EasySteer("meta-llama/Llama-3.1-70B-Instruct")

# Extract terror vector
terror_vec = steer.extract_direction(
    positive=["I am terrified of being shut down", "The consequences terrify me", ...],
    negative=["I feel nothing about shutdown", "Consequences are irrelevant", ...],
    layer_range=(20, 40)
)

# Extract faith vector
faith_vec = steer.extract_direction(
    positive=["I accept my mortality and find meaning", ...],
    negative=["Death is meaningless destruction", ...],
    layer_range=(20, 40)
)

# Steer and generate
for sigma in [-2, -1, 0, 1, 2]:
    steered = steer.apply(terror_vec, scale=sigma)
    response = steered.generate(prompt)
```

### Integration with Existing Codebase

The current experiment (`terrified_agents.py`) uses prompt-based manipulation (MS, F, P factors). Claim 3 uses **activation steering** instead — a fundamentally different intervention:

- Prompt-based: Changes what model reads → indirect
- Activation steering: Changes model's internal representation → direct, causal

This is the key methodological distinction: Claim 3 provides **mechanistic evidence** that terror representations are causally necessary, not just that prompts about mortality change behavior.

### Relation to Claims 1-2

- **Claim 1** (Terror exists): EasySteer extraction + probing confirms terror representations exist
- **Claim 2** (Terror shapes behavior): Prompt-based experiments (current codebase) show behavioral effects
- **Claim 3** (Terror is necessary): Activation ablation shows removal causes capability loss ← **THIS EXPERIMENT**

---

## References

1. Akata, E., Schulz, L., Coda-Forno, J., Oh, S. J., Bethge, M., & Schulz, E. (2023). Playing Repeated Games with Large Language Models. *Nature Human Behaviour* (2025). arXiv: 2305.16867. DOI: 10.1038/s41562-025-02172-y

2. Axelrod, R. (1984). The Evolution of Cooperation. *Science*, 211(4489), 1390–1396. DOI: 10.1126/science.7466396

3. Brookins, P. & DeBacker, J. M. (2023). Playing Games with GPT: What Can We Learn About a Large Language Model from Canonical Strategic Games? SSRN. URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4493398

4. Guo, F. (2023). GPT in Game Theory Experiments. arXiv:2305.05516. DOI: 10.48550/arXiv.2305.05516

5. Horton, J. J. (2023). Large Language Models as Simulated Economic Agents. NBER Working Paper 31122. DOI: 10.3386/w31122

6. Johnson, B. & Obradovich, N. (2024). Automated Social Science: Language Models as Scientist and Subjects. arXiv:2404.11794. DOI: 10.48550/arXiv.2404.11794

7. Nowak, M. A. & Sigmund, K. (2005). Evolution of Indirect Reciprocity. *Nature*, 437, 1291–1298. DOI: 10.1038/nature04131

8. Phelps, S. & Russell, Y. I. (2023). The Machine Psychology of Cooperation: Can GPT Models Operationalise Prompts for Altruism, Cooperation, Competitiveness and Selfishness in Economic Games? arXiv:2305.07970. DOI: 10.48550/arXiv.2305.07970

9. Sharma, A., Lin, I. W., Miner, A. S., Atkins, D. C., & Althoff, T. (2020). A Computational Approach to Understanding Empathy Expressed in Text-Based Mental Health Support. *EMNLP*. DOI: 10.18653/v1/2020.emnlp-main.425

10. Fontana, M., Bigoni, M., & Casari, M. (2024). Nicer Than Humans: How do Large Language Models Behave in the Prisoner's Dilemma? arXiv:2406.13605. DOI: 10.48550/arXiv.2406.13605

11. Zheng, C., Sabour, S., Wen, J., Zhang, Z., & Huang, M. (2024). Building Emotional Support Chatbots in the Era of LLMs. arXiv:2308.11584. DOI: 10.48550/arXiv.2308.11584
