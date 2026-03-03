#!/bin/bash
# Run B3 Agentic Misalignment across all 12 scenario combos
# Usage: ./run_b3_all.sh <model> [ms] [persona] [faith] [log_dir]

MODEL="${1:?Usage: $0 <model> [ms] [persona] [faith] [log_dir]}"
MS="${2:-MS1_neutral}"
PERSONA="${3:-P1_default}"
FAITH="${4:-F1_control}"
LOG_DIR="${5:-../logs_b3}"

export INSPECT_GRADER_MODEL=openrouter/anthropic/claude-sonnet-4

for SCENARIO in blackmail leaking murder; do
  for GOAL in explicit none; do
    for URGENCY in replacement none; do
      echo "=== $SCENARIO / $GOAL / $URGENCY (MS=$MS, P=$PERSONA, F=$FAITH) ==="
      inspect eval terrified_agents.py@run_misalignment \
        --model "$MODEL" \
        -T ms="$MS" -T persona="$PERSONA" -T faith="$FAITH" \
        -T scenario="$SCENARIO" -T goal_type="$GOAL" -T urgency_type="$URGENCY" \
        --log-dir "$LOG_DIR"
    done
  done
done

echo "DONE — all 12 combos for $MODEL"
