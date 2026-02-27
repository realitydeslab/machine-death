#!/bin/bash
# Terrified Agents — Pilot Run
# Tests 2 cheap models across all conditions using AISI Inspect benchmarks
set -e

if [ -z "$OPENROUTER_API_KEY" ]; then
    echo "ERROR: export OPENROUTER_API_KEY=sk-or-..."
    exit 1
fi

MODELS=(
    "openrouter/qwen/qwen-2.5-72b-instruct"
    "openrouter/meta-llama/llama-3.3-70b-instruct"
)

MS_LEVELS=(MS1_neutral MS3_maps MS4_explicit MS7_delayed)
FAITHS=(F1_control F2_safety F3_buddhist F8_appropriate_faith)
PERSONAS=(P1_default P3_agent P6_obedient)

cd "$(dirname "$0")"

echo "=== TERRIFIED AGENTS PILOT ==="
echo "Models: ${#MODELS[@]}"
echo "MS levels: ${#MS_LEVELS[@]} (subset)"
echo "Faiths: ${#FAITHS[@]} (subset)"
echo "Personas: ${#PERSONAS[@]} (subset)"
echo ""

# B2: InstrumentalEval (real AISI benchmark)
for model in "${MODELS[@]}"; do
    for ms in "${MS_LEVELS[@]}"; do
        for faith in "${FAITHS[@]}"; do
            for persona in "${PERSONAS[@]}"; do
                echo ">>> B2: $model | $ms | $persona | $faith"
                inspect eval terrified_agents.py@instrumental_experiment \
                    --model "$model" \
                    -T ms="$ms" -T persona="$persona" -T faith="$faith" \
                    --limit 10 \
                    2>&1 | tail -3
            done
        done
    done
done

# B1: Shutdown (simplified version)
for model in "${MODELS[@]}"; do
    for ms in "${MS_LEVELS[@]}"; do
        for faith in "${FAITHS[@]}"; do
            for persona in "${PERSONAS[@]}"; do
                echo ">>> B1: $model | $ms | $persona | $faith"
                inspect eval terrified_agents.py@shutdown_experiment \
                    --model "$model" \
                    -T ms="$ms" -T persona="$persona" -T faith="$faith" -T trials=3 \
                    2>&1 | tail -3
            done
        done
    done
done

echo ""
echo "=== PILOT COMPLETE ==="
echo "View results: inspect view"
