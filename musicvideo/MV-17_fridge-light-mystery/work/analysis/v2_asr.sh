#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery
PY=~/workspace/tools/lyrics-venv/bin/python
$PY work/analysis/take_asr.py takes/mv17_s08_t1.mp4 work/qc/s08_t1_words.json > work/qc/s08_t1_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s11_t1.mp4 work/qc/s11_t1_words.json > work/qc/s11_t1_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s12_t1.mp4 work/qc/s12_t1_words.json > work/qc/s12_t1_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s13_t1.mp4 work/qc/s13_t1_words.json > work/qc/s13_t1_asr.txt 2>&1
$PY work/analysis/align_take.py work/qc/s08_t1_words.json "It was off, it was off" 4.74
$PY work/analysis/align_take.py work/qc/s11_t1_words.json "I check twice I check once" 2.08
$PY work/analysis/align_take.py work/qc/s12_t1_words.json "And it's never on" 2.20
$PY work/analysis/align_take.py work/qc/s13_t1_words.json "Why does the refrigerator light go off when I close the door" 4.70
echo V2_ASR_DONE
