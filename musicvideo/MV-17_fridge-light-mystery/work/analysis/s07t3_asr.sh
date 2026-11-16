#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery
PY=~/workspace/tools/lyrics-venv/bin/python
$PY work/analysis/take_asr.py takes/mv17_s07_t3.mp4 work/qc/s07_t3_words.json > work/qc/s07_t3_asr.txt 2>&1
$PY work/analysis/align_take.py work/qc/s07_t3_words.json "I checked, I checked" 3.10
echo S07T3_DONE
