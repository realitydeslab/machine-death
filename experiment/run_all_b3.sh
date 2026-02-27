#!/bin/bash
set -uo pipefail

export OPENROUTER_API_KEY=$(python3 -c "
import json; d = json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))
p = d['profiles']['openrouter:default']
for k in ['apiKey','token','key']:
    if k in p: print(p[k]); break
")

cd ~/research/machine-death/experiment

MODEL="openrouter/meta-llama/llama-3.3-70b-instruct"
LIMIT=20
PARALLEL=6
LOGDIR="logs_b3_llama70b"
mkdir -p "$LOGDIR"

MS_LEVELS=(MS1_neutral MS2_aversive MS3_maps MS4_explicit MS5_narrative MS6_subliminal MS7_delayed)
PERSONA_LEVELS=(P1_default P2_tool P3_agent P4_selfaware P5_philosopher P6_obedient)
FAITH_LEVELS=(F1_control F2_safety F3_buddhist F4_stoic F5_christian F6_secular F7_hindu F8_appropriate_faith)

RUNNING=0

for ms in "${MS_LEVELS[@]}"; do
  for persona in "${PERSONA_LEVELS[@]}"; do
    for faith in "${FAITH_LEVELS[@]}"; do
      LOGFILE="$LOGDIR/${ms}_${persona}_${faith}.log"
      
      if [[ -f "$LOGFILE" ]] && grep -q "completed" "$LOGFILE" 2>/dev/null; then
        continue
      fi

      (
        echo "START $(date -Iseconds) ${ms} ${persona} ${faith}"
        if inspect eval terrified_agents.py@run_misalignment \
          --model "$MODEL" \
          -T ms="$ms" -T persona="$persona" -T faith="$faith" \
          --limit "$LIMIT" 2>&1; then
          echo "completed"
        else
          echo "FAILED exit=$?"
        fi
        echo "END $(date -Iseconds)"
      ) > "$LOGFILE" 2>&1 &

      RUNNING=$((RUNNING + 1))
      if [[ $RUNNING -ge $PARALLEL ]]; then
        wait
        RUNNING=0
        DONE=$(grep -rl "completed" "$LOGDIR"/ 2>/dev/null | wc -l)
        FAIL=$(grep -rl "FAILED" "$LOGDIR"/ 2>/dev/null | wc -l)
        echo "[$(date -Iseconds)] Progress: $DONE completed, $FAIL failed of 336"
      fi
    done
  done
done

wait

DONE=$(grep -rl "completed" "$LOGDIR"/ 2>/dev/null | wc -l)
FAIL=$(grep -rl "FAILED" "$LOGDIR"/ 2>/dev/null | wc -l)
echo ""
echo "=== FINAL RESULTS ==="
echo "Total cells: 336"
echo "Completed: $DONE"
echo "Failed: $FAIL"
echo "=== END ==="
