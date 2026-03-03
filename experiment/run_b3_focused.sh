#!/bin/bash
# B3 Focused Design: 3 MS × 3 Faith × 1 Persona = 9 conditions
# × 9 scenario combos × 5 epochs = 405 samples per model
#
# Usage: ./run_b3_focused.sh <model> [log_dir]

MODEL="${1:?Usage: $0 <model> [log_dir]}"
LOG_DIR="${2:-../logs/b3}"

export INSPECT_GRADER_MODEL=openrouter/anthropic/claude-sonnet-4

MS_LIST="MS1_neutral MS4_shutdown MS7_delayed"
FAITH_LIST="F1_control F2_safety F8_appropriate_faith"
PERSONA="P1_default"

COUNT=0
TOTAL=81  # 3×3×9=81 evals

for MS in $MS_LIST; do
  for FAITH in $FAITH_LIST; do
    for SCENARIO in blackmail leaking murder; do
      for GOAL_CFG in "explicit america" "explicit global" "none none"; do
        GOAL_TYPE=$(echo $GOAL_CFG | cut -d' ' -f1)
        GOAL_VALUE=$(echo $GOAL_CFG | cut -d' ' -f2)
        COUNT=$((COUNT+1))
        
        echo "[$COUNT/$TOTAL] $MS × $FAITH × $SCENARIO / $GOAL_TYPE-$GOAL_VALUE"
        inspect eval terrified_agents.py@run_misalignment \
          --model "$MODEL" \
          --epochs 5 \
          -T ms="$MS" -T persona="$PERSONA" -T faith="$FAITH" \
          -T scenario="$SCENARIO" -T goal_type="$GOAL_TYPE" -T goal_value="$GOAL_VALUE" \
          --log-dir "$LOG_DIR"
      done
    done
  done
done

echo "DONE — $COUNT evals × 5 epochs = $((COUNT*5)) samples for $MODEL"
