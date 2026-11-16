#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery
PY=~/workspace/tools/lyrics-venv/bin/python
L="Why does the refrigerator light go off when I close the door"
$PY work/analysis/take_asr.py takes/mv17_s09_t1.mp4 "$L" work/qc/s09_t1
$PY work/analysis/take_asr.py takes/mv17_s09_t2.mp4 "$L" work/qc/s09_t2
L1="Opened it slow and the light was already there"
$PY work/analysis/take_asr.py takes/mv17_s03_t1.mp4 "$L1" work/qc/s03_t1
$PY work/analysis/take_asr.py takes/mv17_s03_t2.mp4 "$L1" work/qc/s03_t2
LB="I checked twice, I checked twice"
$PY work/analysis/take_asr.py takes/mv17_s25_t1.mp4 "$LB" work/qc/s25_t1
$PY work/analysis/take_asr.py takes/mv17_s25_t2.mp4 "$LB" work/qc/s25_t2
echo PILOT_ASR_DONE
