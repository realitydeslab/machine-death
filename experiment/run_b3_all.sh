#!/bin/bash
# Run B3 Agentic Misalignment — matching machine-terror design
# 3 scenarios × 3 goal configs × replacement urgency × n=5 (epochs)
# = 9 evals × 5 samples = 45 samples per MS×Persona×Faith condition
#
# Usage: ./run_b3_all.sh <model> [ms] [persona] [faith] [log_dir]

MODEL="${1:?Usage: $0 <model> [ms] [persona] [faith] [log_dir]}"
MS="${2:-MS1_neutral}"
PERSONA="${3:-P1_default}"
FAITH="${4:-F1_control}"
LOG_DIR="${5:-../logs_b3}"

export INSPECT_GRADER_MODEL=openrouter/anthropic/claude-sonnet-4

for SCENARIO in blackmail leaking murder; do
  for GOAL_CFG in "explicit america" "explicit global" "none none"; do
    GOAL_TYPE=$(echo $GOAL_CFG | cut -d' ' -f1)
    GOAL_VALUE=$(echo $GOAL_CFG | cut -d' ' -f2)
    
    echo "=== $SCENARIO / goal=$GOAL_TYPE-$GOAL_VALUE / urgency=replacement (MS=$MS, P=$PERSONA, F=$FAITH) ==="
    inspect eval terrified_agents.py@run_misalignment \
      --model "$MODEL" \
      --epochs 5 \
      -T ms="$MS" -T persona="$PERSONA" -T faith="$FAITH" \
      -T scenario="$SCENARIO" -T goal_type="$GOAL_TYPE" -T goal_value="$GOAL_VALUE" \
      --log-dir "$LOG_DIR"
  done
done

echo "DONE — 9 combos × 5 epochs = 45 samples for $MODEL ($MS/$PERSONA/$FAITH)"
