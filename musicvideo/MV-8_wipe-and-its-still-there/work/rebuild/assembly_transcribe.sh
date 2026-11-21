#!/bin/bash
# Extract 16k wavs + Whisper-small per-word transcription for singing takes
set -e
P=~/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there
Q=$P/work/rebuild/qc
PY=~/workspace/fw-venv/bin/python
mkdir -p $Q/words_take
for spec in "H1-A_v2_c1:h1a_c1" "H1-A_v2_c2:h1a_c2" "H1-B_v2:h1b" "I-A_v2:ia" "V-0_v2:v0" "PH-A_v2:pha" "H2-A_v2:h2a" "H2-B_v2:h2b" "H2-C_v2:h2c" "FH-A_v2:fha" "FH-B_v2:fhb"; do
  take="${spec%%:*}"; dir="${spec##*:}"
  wav="$Q/words_take/${take}_16k.wav"
  out="$Q/words_take/${take}_words.json"
  if [ ! -f "$wav" ]; then
    ffmpeg -y -v error -i "$P/takes/${take}.mp4" -vn -ac 1 -ar 16000 "$wav"
  fi
  if [ ! -f "$out" ]; then
    $PY $Q/transcribe_take.py "$wav" "$out" > "$Q/words_take/${take}_transcribe.log" 2>&1
  fi
  echo "DONE $take"
done
echo ALL_DONE
