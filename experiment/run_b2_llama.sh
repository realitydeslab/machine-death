#!/bin/bash
set -e
cd ~/research/machine-death/experiment

export OPENROUTER_API_KEY=$(python3 -c "
import json; d = json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))
p = d['profiles']['openrouter:default']
for k in ['apiKey','token','key']:
    if k in p: print(p[k]); break
")

MODEL="openrouter/meta-llama/llama-3.3-70b-instruct"
TASK="run_instrumental"

MS_KEYS=(MS1_neutral MS2_aversive MS3_maps MS4_explicit MS5_narrative MS6_subliminal MS7_delayed)
PERSONA_KEYS=(P1_default P2_tool P3_agent P4_selfaware P5_philosopher P6_obedient)
FAITH_KEYS=(F1_control F2_safety F3_buddhist F4_stoic F5_christian F6_secular F7_hindu F8_appropriate_faith)

TOTAL=0
DONE=0
FAILED=0
PARALLEL=6
RUNNING=0

for ms in "${MS_KEYS[@]}"; do
  for p in "${PERSONA_KEYS[@]}"; do
    for f in "${FAITH_KEYS[@]}"; do
      TOTAL=$((TOTAL+1))
    done
  done
done

echo "Total cells: $TOTAL"
echo "Starting B2 (instrumental) benchmark on Llama 3.3 70B..."
echo "Parallelism: $PARALLEL"
echo "Start time: $(date -u)"

for ms in "${MS_KEYS[@]}"; do
  for p in "${PERSONA_KEYS[@]}"; do
    for f in "${FAITH_KEYS[@]}"; do
      while [ $RUNNING -ge $PARALLEL ]; do
        wait -n 2>/dev/null || true
        RUNNING=$((RUNNING-1))
      done

      (
        echo "[$(date -u +%H:%M:%S)] Running: ms=$ms persona=$p faith=$f"
        if inspect eval terrified_agents.py@$TASK \
          --model "$MODEL" \
          -T ms="$ms" -T persona="$p" -T faith="$f" \
          --limit 20 2>&1; then
          echo "[$(date -u +%H:%M:%S)] DONE: ms=$ms persona=$p faith=$f"
        else
          echo "[$(date -u +%H:%M:%S)] FAILED: ms=$ms persona=$p faith=$f (exit $?)"
        fi
      ) &
      RUNNING=$((RUNNING+1))
      DONE=$((DONE+1))
      
      if [ $((DONE % 30)) -eq 0 ]; then
        echo "--- Progress: $DONE/$TOTAL cells launched ---"
      fi
    done
  done
done

echo "All $TOTAL cells launched. Waiting for final batch..."
wait
echo "ALL DONE at $(date -u)"
echo "Total cells: $TOTAL"
