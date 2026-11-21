#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery
PY=~/workspace/tools/lyrics-venv/bin/python
run() { $PY work/analysis/take_asr.py takes/$1 work/qc/$2_words.json > work/qc/$2_asr.txt 2>&1; $PY work/analysis/align_take.py work/qc/$2_words.json "$3" $4; }
run mv17_s23_t1.mp4 s23_t1 "And it's never on" 2.16
run mv17_s24_t1.mp4 s24_t1 "Why does the refrigerator light go off when I close the door" 4.82
run mv17_s26_t1.mp4 s26_t1 "It was never on, it was never on" 4.44
run mv17_s27_t1.mp4 s27_t1 "When I close the door" 2.90
run mv17_s29_t1.mp4 s29_t1 "Why does the refrigerator light go off when I close the door" 4.42
run mv17_s30_t1.mp4 s30_t1 "Why does the refrigerator light go off when I close the door" 4.00
run mv17_s32_t1.mp4 s32_t1 "Why does the refrigerator light go off when I close the door" 4.66
run mv17_s33_t1.mp4 s33_t1 "Never on, never on" 4.58
run mv17_s34_t1.mp4 s34_t1 "When I close the door" 4.40
echo V56_ASR_DONE
