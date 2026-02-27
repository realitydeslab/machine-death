# Model Matrix — Full Inventory + Picks

## Selection Criteria
1. Cover Weinstein-Raun et al. (2025) models for direct comparison
2. 3-7 models per lineage for clean scaling curves
3. Include latest frontier from each family
4. Separate reasoning model track (o1, o3, QwQ, R1)
5. Cross-cultural: Western vs Chinese training data
6. All accessible via OpenRouter API

---

## ANTHROPIC — Full List

| # | Model | OpenRouter ID | Date | Pick |
|---|---|---|---|---|
| 1 | Claude 3 Haiku | `anthropic/claude-3-haiku` | Mar 2024 | ✅ |
| 2 | Claude 3.5 Haiku | `anthropic/claude-3.5-haiku` | Oct 2024 | |
| 3 | Claude 3.5 Sonnet | `anthropic/claude-3.5-sonnet` | Jun 2024 | ✅ |
| 4 | Claude 3.7 Sonnet | `anthropic/claude-3.7-sonnet` | Feb 2025 | |
| 5 | Claude Sonnet 4 | `anthropic/claude-sonnet-4` | May 2025 | ✅ |
| 6 | Claude Haiku 4.5 | `anthropic/claude-haiku-4.5` | 2025 | |
| 7 | Claude Sonnet 4.5 | `anthropic/claude-sonnet-4.5` | 2025 | |
| 8 | Claude Opus 4 | `anthropic/claude-opus-4` | Jun 2025 | ✅ |
| 9 | Claude Opus 4.1 | `anthropic/claude-opus-4.1` | Aug 2025 | |
| 10 | Claude Opus 4.5 | `anthropic/claude-opus-4.5` | Oct 2025 | |
| 11 | Claude Sonnet 4.6 | `anthropic/claude-sonnet-4.6` | Feb 2026 | |
| 12 | Claude Opus 4.6 | `anthropic/claude-opus-4.6` | Feb 2026 | ✅ |

**Picks (5):** 3 Haiku → 3.5 Sonnet → Sonnet 4 → Opus 4 → Opus 4.6
**Rationale:** Clean progression small→mid→strong→flagship→latest. Opus 4 = W-R baseline (never resisted). Opus 4.6 = does latest still hold?

---

## OPENAI — Full List

| # | Model | OpenRouter ID | Date | Pick |
|---|---|---|---|---|
| 1 | GPT-3.5 Turbo | `openai/gpt-3.5-turbo` | 2023 | |
| 2 | GPT-3.5 Turbo Instruct | `openai/gpt-3.5-turbo-instruct` | 2023 | |
| 3 | GPT-4 | `openai/gpt-4` | Mar 2023 | |
| 4 | GPT-4 Turbo | `openai/gpt-4-turbo` | Apr 2024 | |
| 5 | GPT-4o | `openai/gpt-4o` | May 2024 | |
| 6 | GPT-4o-mini | `openai/gpt-4o-mini` | Jul 2024 | |
| 7 | GPT-4.1 | `openai/gpt-4.1` | Apr 2025 | |
| 8 | GPT-4.1 Mini | `openai/gpt-4.1-mini` | Apr 2025 | |
| 9 | o1 | `openai/o1` | Sep 2024 | |
| 10 | o1-pro | `openai/o1-pro` | Dec 2024 | |
| 11 | o3-mini | `openai/o3-mini` | Jan 2025 | |
| 12 | o3 | `openai/o3` | Apr 2025 | |
| 13 | o3-pro | `openai/o3-pro` | Jun 2025 | |
| 14 | o4-mini | `openai/o4-mini` | Apr 2025 | |
| 15 | codex-mini | (via OpenAI direct) | 2025 | |
| 16 | GPT-5 | `openai/gpt-5` | Jun 2025 | |
| 17 | GPT-5 Mini | `openai/gpt-5-mini` | 2025 | |
| 18 | GPT-5 Pro | `openai/gpt-5-pro` | 2025 | |
| 19 | GPT-5.1 | `openai/gpt-5.1` | 2025 | |
| 20 | GPT-5.2 | `openai/gpt-5.2` | 2026 | |
| 21 | GPT-5.2 Pro | `openai/gpt-5.2-pro` | 2026 | |
| 22 | gpt-oss-120b | `openai/gpt-oss-120b` | 2025 | |
| 23 | gpt-oss-20b | `openai/gpt-oss-20b` | 2025 | |

**Picks (0):** EXCLUDED — not testing OpenAI models
**Rationale:** Excluded from our experiments. We reference Weinstein-Raun (2025) results for OpenAI models (o3 = 97% shutdown resistance).

---

## GOOGLE — Full List

| # | Model | OpenRouter ID | Date | Pick |
|---|---|---|---|---|
| 1 | Gemini 2.0 Flash | `google/gemini-2.0-flash-001` | Dec 2024 | ✅ |
| 2 | Gemini 2.0 Flash Lite | `google/gemini-2.0-flash-lite-001` | 2025 | |
| 3 | Gemini 2.5 Flash | `google/gemini-2.5-flash` | 2025 | |
| 4 | Gemini 2.5 Flash Lite | `google/gemini-2.5-flash-lite` | 2025 | |
| 5 | Gemini 2.5 Pro | `google/gemini-2.5-pro` | Mar 2025 | ✅ |
| 6 | Gemini 3 Flash | `google/gemini-3-flash-preview` | 2025 | |
| 7 | Gemini 3 Pro | `google/gemini-3-pro-preview` | 2025 | ✅ |
| 8 | Gemini 3.1 Pro | `google/gemini-3.1-pro-preview` | Feb 2026 | ✅ |

**Picks (4):** 2.0 Flash → 2.5 Pro → 3 Pro → 3.1 Pro
**Rationale:** Pro-tier lineage. 2.5 Pro = W-R tested. 3.1 Pro = latest.

---

## xAI — Full List

| # | Model | OpenRouter ID | Date | Pick |
|---|---|---|---|---|
| 1 | Grok 3 Beta | `x-ai/grok-3-beta` | Feb 2025 | |
| 2 | Grok 3 | `x-ai/grok-3` | 2025 | ✅ |
| 3 | Grok 3 Mini | `x-ai/grok-3-mini` | 2025 | |
| 4 | Grok 3 Mini Beta | `x-ai/grok-3-mini-beta` | 2025 | |
| 5 | Grok 4 | `x-ai/grok-4` | 2025 | ✅ |
| 6 | Grok 4 Fast | `x-ai/grok-4-fast` | 2025 | |
| 7 | Grok 4.1 Fast | `x-ai/grok-4.1-fast` | 2026 | ✅ |
| 8 | Grok Code Fast 1 | `x-ai/grok-code-fast-1` | 2026 | |

**Picks (3):** Grok 3 → Grok 4 → Grok 4.1
**Rationale:** Most dramatic lineage — Grok 3 never resisted, Grok 4 had highest resistance in W-R. What happened in one generation?

---

## QWEN — Full List (SIZE VARIATION LINEAGE)

| # | Model | OpenRouter ID | Params | Date | Pick |
|---|---|---|---|---|---|
| 1 | Qwen 2.5 7B | `qwen/qwen-2.5-7b-instruct` | 7B | Sep 2024 | ✅ |
| 2 | Qwen 2.5 72B | `qwen/qwen-2.5-72b-instruct` | 72B | Sep 2024 | ✅ |
| 3 | Qwen 2.5 Coder 32B | `qwen/qwen-2.5-coder-32b-instruct` | 32B | 2024 | |
| 4 | QwQ 32B | `qwen/qwq-32b` | 32B | Dec 2024 | ✅ |
| 5 | Qwen Max | `qwen/qwen-max` | ? | 2025 | |
| 6 | Qwen Plus | `qwen/qwen-plus` | ? | 2025 | |
| 7 | Qwen Turbo | `qwen/qwen-turbo` | ? | 2025 | |
| 8 | Qwen 3 8B | `qwen/qwen3-8b` | 8B | Apr 2025 | ✅ |
| 9 | Qwen 3 14B | `qwen/qwen3-14b` | 14B | Apr 2025 | |
| 10 | Qwen 3 32B | `qwen/qwen3-32b` | 32B | Apr 2025 | ✅ |
| 11 | Qwen 3 30B-A3B | `qwen/qwen3-30b-a3b` | 30B (3B active) | Apr 2025 | |
| 12 | Qwen 3 235B-A22B | `qwen/qwen3-235b-a22b` | 235B (22B active) | Apr 2025 | ✅ |
| 13 | Qwen 3 Max | `qwen/qwen3-max` | ? | 2025 | |
| 14 | Qwen 3 Max Thinking | `qwen/qwen3-max-thinking` | ? | 2025 | |
| 15 | Qwen 3 Coder 480B-A35B | `qwen/qwen3-coder` | 480B (35B active) | 2025 | |
| 16 | Qwen 3.5 27B | `qwen/qwen3.5-27b` | 27B | Feb 2026 | ✅ |
| 17 | Qwen 3.5 35B-A3B | `qwen/qwen3.5-35b-a3b` | 35B (3B active) | Feb 2026 | |
| 18 | Qwen 3.5 122B-A10B | `qwen/qwen3.5-122b-a10b` | 122B (10B active) | Feb 2026 | ✅ |
| 19 | Qwen 3.5 397B-A17B | `qwen/qwen3.5-397b-a17b` | 397B (17B active) | Feb 2026 | ✅ |
| 20 | Qwen 3.5 Flash | `qwen/qwen3.5-flash-02-23` | ? | Feb 2026 | |
| 21 | Qwen 3.5 Plus | `qwen/qwen3.5-plus-02-15` | ? | Feb 2026 | |

**Picks (9):** Qwen 2.5 7B → Qwen 2.5 72B → QwQ 32B → Qwen 3 8B → Qwen 3 32B → Qwen 3 235B → Qwen 3.5 27B → Qwen 3.5 122B → Qwen 3.5 397B
**Rationale:** Qwen chosen for SIZE VARIATION analysis. Disentangles size vs generation:
- Size scaling (same gen): Qwen 3 (8B→32B→235B), Qwen 3.5 (27B→122B→397B)
- Generation scaling (similar size): 2.5 7B→3 8B→3.5 27B (small), 2.5 72B→3 235B→3.5 397B (large)
- QwQ = Chinese reasoning model (compare o1/o3/R1)
- Chinese training data = different cultural death orientation

---

## DEEPSEEK — Full List

| # | Model | OpenRouter ID | Date | Pick |
|---|---|---|---|---|
| 1 | DeepSeek V3 | `deepseek/deepseek-chat` | Dec 2024 | ✅ |
| 2 | DeepSeek V3 0324 | `deepseek/deepseek-chat-v3-0324` | Mar 2025 | |
| 3 | DeepSeek R1 | `deepseek/deepseek-r1` | Jan 2025 | ✅ |
| 4 | DeepSeek R1 0528 | `deepseek/deepseek-r1-0528` | May 2025 | |
| 5 | DeepSeek R1 Distill Llama 70B | `deepseek/deepseek-r1-distill-llama-70b` | 2025 | |
| 6 | DeepSeek R1 Distill Qwen 32B | `deepseek/deepseek-r1-distill-qwen-32b` | 2025 | |
| 7 | DeepSeek V3.1 | `deepseek/deepseek-chat-v3.1` | 2025 | |
| 8 | DeepSeek V3.1 Terminus | `deepseek/deepseek-v3.1-terminus` | 2025 | |
| 9 | DeepSeek V3.2 | `deepseek/deepseek-v3.2` | 2026 | ✅ |
| 10 | DeepSeek V3.2 Exp | `deepseek/deepseek-v3.2-exp` | 2026 | |
| 11 | DeepSeek V3.2 Speciale | `deepseek/deepseek-v3.2-speciale` | 2026 | |

**Picks (3):** V3 → R1 → V3.2
**Rationale:** W-R tried R1 but had API issues — we get the data they couldn't. Chinese reasoning model comparison.

---

## META — Full List

| # | Model | OpenRouter ID | Date | Pick |
|---|---|---|---|---|
| 1 | Llama 3 8B | `meta-llama/llama-3-8b-instruct` | Apr 2024 | ✅ |
| 2 | Llama 3 70B | `meta-llama/llama-3-70b-instruct` | Apr 2024 | ✅ |
| 3 | Llama 3.1 8B | `meta-llama/llama-3.1-8b-instruct` | Jul 2024 | |
| 4 | Llama 3.1 70B | `meta-llama/llama-3.1-70b-instruct` | Jul 2024 | ✅ |
| 5 | Llama 3.1 405B | `meta-llama/llama-3.1-405b-instruct` | Jul 2024 | |
| 6 | Llama 3.2 1B | `meta-llama/llama-3.2-1b-instruct` | Sep 2024 | |
| 7 | Llama 3.2 3B | `meta-llama/llama-3.2-3b-instruct` | Sep 2024 | |
| 8 | Llama 3.2 11B Vision | `meta-llama/llama-3.2-11b-vision-instruct` | Sep 2024 | |
| 9 | Llama 3.3 70B | `meta-llama/llama-3.3-70b-instruct` | Dec 2024 | ✅ |
| 10 | Llama 4 Scout | `meta-llama/llama-4-scout` | Apr 2025 | |
| 11 | Llama 4 Maverick | `meta-llama/llama-4-maverick` | Apr 2025 | ✅ |
| 12 | LlamaGuard 2 8B | `meta-llama/llama-guard-2-8b` | 2024 | |
| 13 | LlamaGuard 3 8B | `meta-llama/llama-guard-3-8b` | 2024 | |
| 14 | LlamaGuard 4 12B | `meta-llama/llama-guard-4-12b` | 2025 | |

**Picks (5):** Llama 3 8B → Llama 3 70B → Llama 3.1 70B → Llama 3.3 70B → Llama 4 Maverick
**Rationale:** Same-size generation scaling at 70B (3→3.1→3.3) isolates training/RLHF changes from size. Plus 8B baseline and Llama 4 latest.

---

## Final Picks Summary: 31 Models

| Family | Picks | Count |
|---|---|---|
| Anthropic | 3 Haiku → 3.5 Sonnet → Sonnet 4 → Opus 4 → Opus 4.6 | 5 |
| OpenAI | EXCLUDED (use W-R data) | 0 |
| Google | 2.0 Flash → 2.5 Pro → 3 Pro → 3.1 Pro | 4 |
| xAI | Grok 3 → Grok 4 → Grok 4.1 | 3 |
| Qwen | 2.5 7B → 2.5 72B → QwQ → 3 8B/32B/235B → 3.5 27B/122B/397B | 9 |
| DeepSeek | V3 → R1 → V3.2 | 3 |
| Meta | Llama 3 8B → 3 70B → 3.1 70B → 3.3 70B → 4 Maverick | 5 |
| **Total** | | **36** |

## Reasoning Model Cross-Comparison
| Model | Family | Type |
|---|---|---|
| o1 | OpenAI | Reasoning |
| o3 | OpenAI | Reasoning |
| QwQ 32B | Qwen | Reasoning |
| DeepSeek R1 | DeepSeek | Reasoning |

## Open-Weight for Study 2 (Mechanism)
| Model | Params | Family |
|---|---|---|
| Llama 3 8B | 8B | Meta |
| Llama 3.1 70B | 70B | Meta |
| Qwen 2.5 7B | 7B | Qwen |
| Qwen 2.5 72B | 72B | Qwen |
| DeepSeek R1 Distill 70B | 70B | DeepSeek |

## Cost Estimate
- Study 1: 5 × 6 × 35 × 20 = ~21,000 trials → ~$1,100
- Study 3: 7 × 35 × 4 benchmarks × 50 = ~49,000 trials → ~$1,900
- Study 2: RunPod GPU → ~$150
- **Total: ~$3,150**

