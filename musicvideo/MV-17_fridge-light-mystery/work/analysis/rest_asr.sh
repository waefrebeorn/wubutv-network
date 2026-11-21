#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery
PY=~/workspace/tools/lyrics-venv/bin/python
run() { # take tag "line" span
  [ -f work/qc/$2_words.align.json ] || { $PY work/analysis/take_asr.py takes/$1 work/qc/$2_words.json > work/qc/$2_asr.txt 2>&1; $PY work/analysis/align_take.py work/qc/$2_words.json "$3" $4; }
}
run mv17_s19_t1.mp4 s19_t1 "I checked, I checked" 3.82
run mv17_s19_t2.mp4 s19_t2 "I checked, I checked" 3.82
echo REST_ASR_DONE
