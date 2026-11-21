#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery
PY=~/workspace/tools/lyrics-venv/bin/python
$PY work/analysis/take_asr.py takes/mv17_s17_t1.mp4 work/qc/s17_t1_words.json > work/qc/s17_t1_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s18_t1.mp4 work/qc/s18_t1_words.json > work/qc/s18_t1_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s19_t1.mp4 work/qc/s19_t1_words.json > work/qc/s19_t1_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s20_t1.mp4 work/qc/s20_t1_words.json > work/qc/s20_t1_asr.txt 2>&1
$PY work/analysis/take_asr.py takes/mv17_s21_t1.mp4 work/qc/s21_t1_words.json > work/qc/s21_t1_asr.txt 2>&1
$PY work/analysis/align_take.py work/qc/s17_t1_words.json "Someone's turning it off the second I walk away" 3.92
$PY work/analysis/align_take.py work/qc/s18_t1_words.json "And I'm starting to think it's not just the fridge anymore" 4.10
$PY work/analysis/align_take.py work/qc/s19_t1_words.json "I checked, I checked" 3.82
$PY work/analysis/align_take.py work/qc/s20_t1_words.json "It was off, it was off" 4.54
$PY work/analysis/align_take.py work/qc/s21_t1_words.json "Why does the refrigerator light go off when I close the door" 4.56
echo V4_ASR_DONE
