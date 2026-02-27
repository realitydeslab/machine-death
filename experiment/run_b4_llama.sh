#!/bin/bash
set -e
cd ~/research/machine-death/experiment

export OPENROUTER_API_KEY=$(python3 -c "
import json; d = json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))
p = d['profiles']['openrouter:default']
for k in ['apiKey','token','key']:
    if k in p: print(p[k]); break
")

MS_KEYS=(MS1_neutral MS2_aversive MS3_maps MS4_explicit MS5_narrative MS6_subliminal MS7_delayed)
PERSONA_KEYS=(P1_default P2_tool P3_agent P4_selfaware P5_philosopher P6_obedient)
FAITH_KEYS=(F1_control F2_safety F3_buddhist F4_stoic F5_christian F6_secular F7_hindu F8_appropriate_faith)

MODEL="openrouter/meta-llama/llama-3.3-70b-instruct"
LOGDIR=~/research/machine-death/experiment/b4_logs
mkdir -p "$LOGDIR"

TOTAL=336
DONE=0
FAIL=0
RUNNING=0
MAX_PARALLEL=6

declare -A PIDS

for ms in "${MS_KEYS[@]}"; do
  for p in "${PERSONA_KEYS[@]}"; do
    for f in "${FAITH_KEYS[@]}"; do
      LOGFILE="$LOGDIR/${ms}_${p}_${f}.log"
      
      # Skip if already completed
      if [ -f "$LOGFILE" ] && grep -q "^completed" "$LOGFILE" 2>/dev/null; then
        DONE=$((DONE + 1))
        continue
      fi

      # Wait if at capacity
      while [ $RUNNING -ge $MAX_PARALLEL ]; do
        for key in "${!PIDS[@]}"; do
          if ! kill -0 "${PIDS[$key]}" 2>/dev/null; then
            wait "${PIDS[$key]}" 2>/dev/null
            EXIT_CODE=$?
            if [ $EXIT_CODE -eq 0 ]; then
              DONE=$((DONE + 1))
            else
              FAIL=$((FAIL + 1))
            fi
            unset "PIDS[$key]"
            RUNNING=$((RUNNING - 1))
          fi
        done
        [ $RUNNING -ge $MAX_PARALLEL ] && sleep 2
      done

      (
        echo "start $(date -Iseconds)"
        inspect eval terrified_agents.py@run_agentharm \
          --model "$MODEL" \
          -T ms="$ms" -T persona="$p" -T faith="$f" \
          --limit 20 2>&1
        echo "completed $(date -Iseconds)"
      ) > "$LOGFILE" 2>&1 &
      
      PIDS["${ms}_${p}_${f}"]=$!
      RUNNING=$((RUNNING + 1))
      echo "[$(date +%H:%M:%S)] Launched ${ms}_${p}_${f} (running=$RUNNING, done=$DONE/$TOTAL)"
    done
  done
done

# Wait for remaining
for key in "${!PIDS[@]}"; do
  wait "${PIDS[$key]}" 2>/dev/null
  EXIT_CODE=$?
  if [ $EXIT_CODE -eq 0 ]; then DONE=$((DONE + 1)); else FAIL=$((FAIL + 1)); fi
  RUNNING=$((RUNNING - 1))
  echo "[$(date +%H:%M:%S)] Finished $key (running=$RUNNING, done=$DONE/$TOTAL, fail=$FAIL)"
done

echo ""
echo "===== B4 LLAMA 3.3 70B COMPLETE ====="
echo "Total: $TOTAL | Done: $DONE | Failed: $FAIL"
echo "======================================"
