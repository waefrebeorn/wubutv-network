#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery
PY=~/workspace/tools/lyrics-venv/bin/python
$PY work/analysis/take_asr.py takes/mv17_s04_t1.mp4 work/qc/s04_t1_words.json > work/qc/s04_t1_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s05_t1.mp4 work/qc/s05_t1_words.json > work/qc/s05_t1_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s07_t1.mp4 work/qc/s07_t1_words.json > work/qc/s07_t1_asr.txt 2>&1
$PY work/analysis/align_take.py work/qc/s04_t1_words.json "Closed it fast and I swear I heard it shut off" 3.80
$PY work/analysis/align_take.py work/qc/s05_t1_words.json "Now I'm sitting on the floor with the door cracked open" 4.18
$PY work/analysis/align_take.py work/qc/s07_t1_words.json "I checked, I checked" 3.10
echo V1_ASR_DONE
