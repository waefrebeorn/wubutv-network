#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery
PY=~/workspace/tools/lyrics-venv/bin/python
$PY work/analysis/take_asr.py takes/mv17_s06_t2.mp4 work/qc/s06_t2_words.json > work/qc/s06_t2_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s07_t2.mp4 work/qc/s07_t2_words.json > work/qc/s07_t2_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s13_t2.mp4 work/qc/s13_t2_words.json > work/qc/s13_t2_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s15_t1.mp4 work/qc/s15_t1_words.json > work/qc/s15_t1_asr.txt 2>&1
$PY work/analysis/align_take.py work/qc/s06_t2_words.json "Waiting for proof that it only works when I'm looking" 4.14
$PY work/analysis/align_take.py work/qc/s07_t2_words.json "I checked, I checked" 3.10
$PY work/analysis/align_take.py work/qc/s13_t2_words.json "Why does the refrigerator light go off when I close the door" 4.70
$PY work/analysis/align_take.py work/qc/s15_t1_words.json "Set up my phone and recorded the whole thing" 5.22
echo V3_ASR_DONE
