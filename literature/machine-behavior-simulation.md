# Literature Review: Machine Behavior & Agent Simulation

## Overview
This review covers the emerging intersection of machine behavior science, LLM-based agent simulations, and multi-agent social dynamics — all foundational to our project on simulating agents with death-related beliefs and existential awareness.

---

## 1. Foundational: Machine Behavior

### 1.1 Rahwan et al. — Machine Behaviour
- **Citation:** Rahwan, I., Cebrian, M., Obradovich, N., Bongard, J., Bonnefon, J.-F., Breazeal, C., ... & Wellman, M. (2019). Machine behaviour. *Nature*, 568(7753), 477–486.
- **Key Contribution:** Proposes studying AI systems as a new class of actors using behavioral science methods — observing, experimenting on, and theorizing about machines the way we study animals or humans. Coins "machine behavior" as a field.
- **Relevance:** Foundational framing for our project. If machines are behavioral entities worthy of ethological study, then studying how they respond to death-related concepts is a legitimate extension of this program.

### 1.2 Epstein & Axtell — Growing Artificial Societies
- **Citation:** Epstein, J. M., & Axtell, R. (1996). *Growing Artificial Societies: Social Science from the Bottom Up*. MIT Press.
- **Key Contribution:** Seminal work on agent-based modeling (ABM) for social science — the Sugarscape model demonstrates how complex social phenomena (trade, conflict, cultural transmission) emerge from simple agent rules.
- **Relevance:** Classic ABM predecessor to LLM-based simulations. Establishes the paradigm of bottom-up social emergence that our death-belief simulations will extend.

### 1.3 Bonabeau — Agent-Based Modeling
- **Citation:** Bonabeau, E. (2002). Agent-based modeling: Methods and techniques for simulating human systems. *Proceedings of the National Academy of Sciences*, 99(suppl 3), 7280–7287.
- **Key Contribution:** Comprehensive overview of ABM methods, arguing they capture emergent phenomena, provide natural descriptions of systems, and are flexible for modeling heterogeneous agents.
- **Relevance:** Methodological foundation. Our project extends ABM by replacing rule-based decision-making with LLM-powered cognition that can represent complex belief systems.

---

## 2. LLM-Based Agent Simulations

### 2.1 Park et al. — Generative Agents (Smallville)
- **Citation:** Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative Agents: Interactive Simulacra of Human Behavior. *ACM Symposium on User Interface Software and Technology (UIST)*, 2023.
- **Key Contribution:** Introduces generative agents — LLM-powered entities with memory, reflection, and planning — living in a Sims-like sandbox ("Smallville"). Agents autonomously form relationships, spread information, and coordinate events. Architecture: observation → memory retrieval → reflection → planning.
- **Relevance:** *The* foundational paper for our approach. Demonstrates that LLM agents can maintain coherent identities, form beliefs, and exhibit emergent social behavior. Our project adds death awareness as a belief dimension within this architecture.

### 2.2 Vezhnevets et al. — Concordia Framework
- **Citation:** Vezhnevets, A. S., Agapiou, J. P., Haber, N., Fortunato, M., Leibo, J. Z., et al. (2023). Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia. *arXiv:2312.03664*.
- **Key Contribution:** Google DeepMind's open-source library for Generative Agent-Based Models (GABMs). Uses a Game Master (inspired by tabletop RPGs) to mediate between agent natural-language actions and environment effects. Modular component system combining LLM calls with associative memory.
- **Relevance:** Directly applicable as a simulation framework for our project. The Game Master pattern could handle death events, afterlife scenarios, and existential crisis moments for agents.

### 2.3 Ghaffarzadegan — Epidemic Modeling with Generative Agents
- **Citation:** Ghaffarzadegan, N. (2023). Epidemic Modeling with Generative Agents. *arXiv:2307.04986*.
- **Key Contribution:** Uses LLM-powered agents in epidemic simulations. Agents autonomously decide to quarantine, self-isolate, and modify behavior based on perceived risk — producing realistic multi-wave pandemic dynamics.
- **Relevance:** Demonstrates agents reasoning about mortality-adjacent concepts (disease, risk of death) and adjusting behavior. Direct precedent for agents that reason about death and its consequences.

### 2.4 Li et al. — EconAgent
- **Citation:** Li, N., Gao, C., Li, Y., & Liao, Q. (2023). Large Language Model-Empowered Agents for Simulating Macroeconomic Activities. *arXiv:2310.10436*.
- **Key Contribution:** LLM agents simulate heterogeneous economic actors (households, firms) making work and consumption decisions in a macroeconomic environment, producing realistic market dynamics.
- **Relevance:** Shows LLM agents can internalize complex value systems and make consequential decisions. Economic agents already implicitly model finite resources and time horizons — extending to mortality awareness is natural.

---

## 3. Social Simulation & Emergent Behavior

### 3.1 Gao et al. — S³: Social-network Simulation System
- **Citation:** Gao, C., Lan, X., Li, N., Yuan, Y., Ding, J., Zhou, Z., Xu, F., & Li, Y. (2023). S³: Social-network Simulation System with Large Language Model-Empowered Agents. *arXiv:2307.14984*.
- **Key Contribution:** Simulates social network dynamics (information diffusion, opinion formation, polarization) using LLM agents with distinct personas. Demonstrates emergent group behaviors matching real social network patterns.
- **Relevance:** Our death-belief simulations will involve social transmission of beliefs about mortality. This work shows LLMs can model information propagation and opinion dynamics in social networks.

### 3.2 Zhang et al. — Exploring Collaboration Mechanisms from Social Psychology
- **Citation:** Zhang, C., Yang, K., Liu, S., Wang, Y., Yang, M., & Li, J. (2023). Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View. *arXiv:2310.02124*.
- **Key Contribution:** Studies how LLM agents with different personality traits (easy-going vs. overconfident) and thinking patterns (debate vs. reflection) collaborate. Finds agents exhibit conformity and consensus-reaching behaviors mirroring social psychology theories.
- **Relevance:** Directly relevant to modeling how death beliefs propagate through agent societies. Shows LLM agents exhibit human-like social influence patterns.

### 3.3 Liang et al. — Multi-Agent Debate
- **Citation:** Liang, T., He, Z., Jiao, W., Wang, X., Wang, Y., Wang, R., Yang, Y., Tu, Z., & Shi, S. (2023). Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate. *arXiv:2305.19118*.
- **Key Contribution:** Multi-Agent Debate (MAD) framework where agents argue positions and a judge arbitrates. Overcomes "Degeneration-of-Thought" problem in single-agent reflection.
- **Relevance:** Methodology for agents debating existential questions. Could be used to simulate philosophical discourse about death among agents.

### 3.4 Kaiya et al. — Lyfe Agents
- **Citation:** Kaiya, H., et al. (2023). Lyfe Agents: Generative agents for low-cost real-time social interactions. *arXiv:2310.02172*.
- **Key Contribution:** Optimized generative agent architecture for real-time social interactions, reducing computational costs while maintaining believable behavior through a self-monitoring cognitive controller.
- **Relevance:** Practical framework for running longer simulations needed to observe how death beliefs evolve over time in agent societies.

### 3.5 Jinxin et al. — War and Peace (WARAGENT)
- **Citation:** Hua, W., Fan, L., Li, L., Mei, K., Ji, J., Ge, Y., Hemphill, L., & Zhang, Y. (2023). War and Peace (WarAgent): Large Language Model-based Multi-Agent Simulation of World Wars. *arXiv:2311.17227*.
- **Key Contribution:** Simulates historical conflicts (WWI, WWII) with LLM agents representing nations. Agents make decisions about alliances, warfare, and peace negotiations, reproducing plausible historical dynamics.
- **Relevance:** War simulations inherently involve agents reasoning about destruction and mass death. Demonstrates that LLM agents can handle high-stakes existential scenarios.

---

## 4. Agent Cognitive Architecture & Belief Systems

### 4.1 Shapira et al. — ACE Framework
- **Citation:** Shapira, D., et al. (2023). Conceptual Framework for Autonomous Cognitive Entities. *arXiv:2310.06775*.
- **Key Contribution:** Six-layer cognitive architecture (Aspirational → Global Strategy → Agent Model → Executive Function → Cognitive Control → Task Prosecution) for autonomous agents. The Aspirational Layer explicitly sets a "moral compass."
- **Relevance:** The layered architecture with an explicit aspirational/values layer is directly applicable to embedding death beliefs at the foundational level of agent cognition.

### 4.2 Sumers et al. — Cognitive Architectures for Language Agents
- **Citation:** Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2023). Cognitive Architectures for Language Agents. *arXiv:2309.02427*.
- **Key Contribution:** Proposes CoALA (Cognitive Architectures for Language Agents), unifying existing LLM agent designs under a cognitive science framework with memory, action spaces, and decision-making cycles.
- **Relevance:** Provides theoretical grounding for where death beliefs would sit in an agent's cognitive architecture — likely in long-term semantic memory and the evaluation/planning modules.

### 4.3 Wang et al. — A Survey on Large Language Model based Autonomous Agents
- **Citation:** Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., ... & Wang, J. (2023). A Survey on Large Language Model based Autonomous Agents. *arXiv:2308.11432*.
- **Key Contribution:** Comprehensive survey of LLM-based agents covering architecture (profiling, memory, planning, action), applications, and evaluation. Identifies key design patterns across dozens of systems.
- **Relevance:** Essential reference for agent design decisions. The profiling module (how agents are given identities/beliefs) is where death-related worldviews would be injected.

### 4.4 Xi et al. — The Rise and Potential of LLM Based Agents
- **Citation:** Xi, Z., Chen, W., Guo, X., He, W., Ding, Y., Hong, B., ... & Gui, T. (2023). The Rise and Potential of Large Language Model Based Agents: A Survey. *arXiv:2309.07864*.
- **Key Contribution:** Another major survey organizing the LLM agent landscape into brain (LLM), perception, and action modules. Discusses single-agent, multi-agent, and human-agent collaboration scenarios.
- **Relevance:** Broad overview helping position our work within the agent research ecosystem.

---

## 5. Personality, Values & Identity in LLM Agents

### 5.1 Serapio-García et al. — Personality Traits in LLMs
- **Citation:** Serapio-García, G., Safdari, M., Crepy, C., Sun, L., Fitz, S., Romero, P., ... & Matarić, M. (2023). Personality Traits in Large Language Models. *arXiv:2307.00184*.
- **Key Contribution:** Demonstrates that LLMs can be reliably shaped to exhibit specific Big Five personality traits through prompting, and that these synthetic personalities produce consistent behavioral patterns across validated psychological instruments.
- **Relevance:** If personality can be reliably manipulated in LLMs, then death-related beliefs and existential orientations can likely be similarly instilled and measured.

### 5.2 Safdari et al. — Personality in LLMs
- **Citation:** Safdari, M., Serapio-García, G., Crepy, C., Fitz, S., Romero, P., Sun, L., ... & Matarić, M. (2023). Personality traits in large language models. *arXiv:2307.00184* (companion work).
- **Key Contribution:** Validates that GPT-family models exhibit stable, measurable personality profiles that can be systematically varied. Personality scores correlate with downstream behavioral choices.
- **Relevance:** Establishes methodology for measuring belief-driven behavioral changes — applicable to measuring effects of death awareness.

### 5.3 Argyle et al. — Out of One, Many (Silicon Sampling)
- **Citation:** Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out of One, Many: Using Language Models to Simulate Human Samples. *Political Analysis*, 31(3), 337–351.
- **Key Contribution:** Demonstrates "algorithmic fidelity" — LLMs conditioned on demographic backstories produce survey responses that closely match real human subpopulation distributions. Introduces "silicon sampling" as a social science methodology.
- **Relevance:** Core methodological precedent. If LLMs can faithfully simulate human survey responses, they may simulate human responses to mortality salience — enabling TMT-style experiments on artificial agents.

### 5.4 Santurkar et al. — Whose Opinions Do LLMs Reflect?
- **Citation:** Santurkar, S., Durmus, E., Ladhak, F., Lee, C., Liang, P., & Hashimoto, T. (2023). Whose Opinions Do Language Models Reflect? *ICML 2023*.
- **Key Contribution:** Systematically measures whose opinions (which demographics) LLMs default to, finding significant biases toward liberal, educated, younger demographics. Conditioning on personas partially corrects this.
- **Relevance:** Important caveat for our project — death beliefs in LLM agents may reflect specific cultural/demographic biases unless carefully controlled.

### 5.5 Shanahan et al. — Role Play with LLMs
- **Citation:** Shanahan, M., McDonell, K., & Reynolds, L. (2023). Role Play with Large Language Models. *Nature*, 623, 493-498.
- **Key Contribution:** Theorizes LLM behavior as role-playing/character simulation rather than genuine belief. Proposes the "role play" frame for understanding what LLMs do when they adopt personas.
- **Relevance:** Critical theoretical lens. When an LLM agent "believes in death," is it role-playing or does the belief functionally influence cognition? This distinction is central to our project's epistemology.

### 5.6 Durmus et al. — Towards Measuring the Representation of Subjective Global Opinions
- **Citation:** Durmus, E., Nguyen, K., Liao, T. I., Schieber, N., Askell, A., Bakhtin, A., ... & Ganguli, D. (2023). Towards Measuring the Representation of Subjective Global Opinions in Language Models. *arXiv:2306.16388*.
- **Key Contribution:** Uses GlobalOpinionQA dataset to measure how well LLMs represent diverse global perspectives on values, beliefs, and social issues. Finds significant Western bias.
- **Relevance:** Death beliefs vary enormously across cultures. This work highlights the challenge of ensuring our simulated agents represent diverse thanatological perspectives.

---

## 6. Trust, Social Cognition & Theory of Mind

### 6.1 Xie et al. — Can LLM Agents Simulate Human Trust?
- **Citation:** Xie, C., Chen, C., Jia, F., Ye, Z., Lai, S., Shu, K., ... & Li, G. (2024). Can Large Language Model Agents Simulate Human Trust Behavior? *arXiv:2402.04559*.
- **Key Contribution:** Tests whether LLM agents replicate human trust behavior in economic games (trust game, dictator game). Finds partial alignment with human patterns but systematic deviations.
- **Relevance:** Trust is deeply connected to mortality awareness in TMT. If agents can simulate trust, they may also simulate the trust-related effects of death salience.

### 6.2 Akata et al. — Playing Repeated Games with LLMs
- **Citation:** Akata, E., Schulz, L., Coda-Forno, J., Oh, S. J., Bethge, M., & Schulz, E. (2023). Playing Repeated Games with Large Language Models. *arXiv:2305.16867*.
- **Key Contribution:** Tests LLMs in iterated game-theoretic scenarios (prisoner's dilemma, battle of the sexes). Finds GPT-4 can cooperate, retaliate, and adapt strategies in ways that partially mirror human game play.
- **Relevance:** Game-theoretic interactions provide controlled settings to test how death beliefs alter cooperative vs. competitive behavior in agents.

### 6.3 Kosinski — Theory of Mind in LLMs
- **Citation:** Kosinski, M. (2023). Theory of Mind May Have Spontaneously Emerged in Large Language Models. *arXiv:2302.02083*.
- **Key Contribution:** Claims GPT-4 solves classic false-belief tasks (Sally-Anne test) at human adult levels, suggesting emergent theory-of-mind capabilities.
- **Relevance:** If agents have theory of mind, they can reason about *others'* death beliefs and mortality — crucial for social dynamics around death (grief, mourning, existential conversations).

---

## 7. Agent Societies & Governance

### 7.1 Li et al. — MetaAgents
- **Citation:** Li, Y., Zhang, Y., & Sun, L. (2023). MetaAgents: Simulating Interactions of Human Behaviors for LLM-Based Task-Oriented Coordination via Collaborative Generative Agents. *arXiv:2310.06500*.
- **Key Contribution:** Framework for LLM agents to coordinate on tasks through simulated human-like social interactions, including negotiation and role assignment.
- **Relevance:** Coordination mechanisms are relevant to how agent communities might collectively process death events (funerals, memorials, succession).

### 7.2 Chen et al. — AgentVerse
- **Citation:** Chen, W., Su, Y., Zuo, J., Yang, C., Yuan, C., Chan, C.-M., ... & Qian, C. (2023). AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors. *arXiv:2308.10848*.
- **Key Contribution:** Platform for multi-agent collaboration where agents dynamically form groups, assign roles, and solve problems together. Observes emergent behaviors including volunteer's dilemma patterns.
- **Relevance:** Multi-agent platform for studying emergent social responses to agent "death" — how communities reorganize, grieve, or adapt.

### 7.3 Zhuge et al. — Mindstorms in Natural Language-Based Societies of Mind
- **Citation:** Zhuge, M., Liu, H., Faccio, F., Ashley, D. R., Csordás, R., ... & Schmidhuber, J. (2023). Mindstorms in Natural Language-Based Societies of Mind. *arXiv:2305.17066*.
- **Key Contribution:** Implements Minsky's "Society of Mind" using LLM agents as specialized cognitive modules that collaborate through natural language. Demonstrates emergent problem-solving from agent interaction.
- **Relevance:** The "society of mind" metaphor applied to death — how does an agent's internal cognitive "society" process mortality concepts?

---

## 8. Benchmarks & Evaluation

### 8.1 Liu et al. — AgentBench
- **Citation:** Liu, X., Yu, H., Zhang, H., Xu, Y., Lei, X., Lai, H., ... & Tang, J. (2023). AgentBench: Evaluating LLMs as Agents. *arXiv:2308.03688*.
- **Key Contribution:** Comprehensive benchmark for evaluating LLM agents across 8 environments (OS, database, games, web). Reveals significant capability gaps between commercial and open-source models.
- **Relevance:** Evaluation methodology reference. We need similar rigorous benchmarks for measuring how death beliefs affect agent performance and behavior.

### 8.2 Light et al. — AvalonBench
- **Citation:** Light, J., Cai, M., Shen, S., & Hu, Z. (2023). AvalonBench: Evaluating LLMs Playing the Game of Avalon. *arXiv:2310.05036*.
- **Key Contribution:** Benchmark for LLM agents in social deduction game Avalon, testing deception, reasoning under uncertainty, and strategic social interaction.
- **Relevance:** Social deduction involves reasoning about others' hidden knowledge — methodologically relevant to agents reasoning about hidden existential beliefs.

---

## 9. Additional Key References

### 9.1 Horton — Large Language Models as Simulated Economic Agents
- **Citation:** Horton, J. J. (2023). Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus? *NBER Working Paper* 31122.
- **Key Contribution:** Demonstrates LLMs replicate classic behavioral economics findings (endowment effect, anchoring) when placed in simulated experimental settings. Proposes "Homo Silicus" as complement to human subjects.
- **Relevance:** If LLM agents replicate behavioral economics effects, they might replicate terror management effects — mortality salience increasing materialism, in-group bias, etc.

### 9.2 Bail et al. — Can Generative AI Improve Social Science?
- **Citation:** Bail, C. A. (2024). Can Generative AI Improve Social Science? *Proceedings of the National Academy of Sciences*, 121(21), e2314021121.
- **Key Contribution:** Critical assessment of using generative AI for social science research, identifying both opportunities (scale, iteration speed) and risks (hallucination, cultural bias, validity concerns).
- **Relevance:** Important methodological caution for our project — LLM-based simulations of death beliefs need careful validation against human data.

### 9.3 Binz & Schulz — Using Cognitive Psychology to Understand GPT-3
- **Citation:** Binz, M., & Schulz, E. (2023). Using cognitive psychology to understand GPT-3. *Proceedings of the National Academy of Sciences*, 120(6), e2218523120.
- **Key Contribution:** Systematically tests GPT-3 on cognitive psychology tasks (decision-making, causal reasoning, information search). Finds GPT-3 matches or exceeds human performance on many tasks but shows distinct failure patterns.
- **Relevance:** Establishes that LLMs have measurable cognitive profiles — a prerequisite for studying whether death awareness alters their "cognitive" patterns.

### 9.4 Coda-Forno et al. — Inducing Anxiety in LLMs
- **Citation:** Coda-Forno, J., Witte, K., Jagadish, A. K., Binz, M., Alaniz, S., & Schulz, E. (2023). Inducing anxiety in large language models increases exploration and bias. *arXiv:2304.11111*.
- **Key Contribution:** Shows that prompting LLMs with anxiety-inducing contexts changes their decision-making behavior — increasing exploration and systematic biases, paralleling human anxiety effects.
- **Relevance:** *Highly relevant.* If anxiety can be induced in LLMs and alter behavior, mortality salience (a specific form of existential anxiety) likely can too. Direct methodological precedent for our TMT-inspired experiments.

### 9.5 Aher et al. — Using LLMs to Simulate Multiple Humans
- **Citation:** Aher, G. V., Arriaga, R. I., & Kalai, A. T. (2023). Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies. *ICML 2023*.
- **Key Contribution:** Demonstrates "Turing Experiments" — LLMs simulating human subjects in classic psychology experiments (Milgram, Asch conformity, ultimatum game) with results closely matching original human findings.
- **Relevance:** If LLMs can replicate Milgram and Asch, they may replicate Greenberg et al.'s terror management experiments — a key validation step for our project.

---

## Summary & Gaps

**What exists:**
- Rich frameworks for LLM-based agent simulation (Generative Agents, Concordia)
- Evidence that LLM agents exhibit human-like social behavior, personality, and cognitive biases
- Preliminary work on emotional/anxiety states in LLMs affecting behavior
- Methods for measuring belief systems and value alignment in agents

**What's missing (our contribution):**
- No work specifically studies death awareness or mortality salience in LLM agents
- No application of Terror Management Theory to artificial agents
- No exploration of how death beliefs shape agent societies over time
- No framework for "machine thanatology" — the systematic study of death concepts in AI systems
- The intersection of machine behavior (Rahwan) + death awareness (TMT) + agent simulation (Park/Concordia) is completely unexplored

This gap represents a significant and novel research opportunity.
