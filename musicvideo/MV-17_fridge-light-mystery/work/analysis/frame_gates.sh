#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery
PY=python3
G=work/analysis/frame_gate.py
$PY $G takes/mv17_s03_t2.mp4 0 6.32
$PY $G takes/mv17_s04_t1.mp4 1.24 4.76
$PY $G takes/mv17_s05_t1.mp4 0.82 5.08
$PY $G takes/mv17_s06_t2.mp4 0 4.72
$PY $G takes/mv17_s07_t2.mp4 0 3.98
$PY $G takes/mv17_s08_t1.mp4 3.26 6.68
$PY $G takes/mv17_s09_t1.mp4 0 4.6
$PY $G takes/mv17_s12_t1.mp4 0 3.52
$PY $G takes/mv17_s13_t2.mp4 0 4.7
$PY $G takes/mv17_s15_t1.mp4 0 3.82
$PY $G takes/mv17_s17_t1.mp4 0 3.98
$PY $G takes/mv17_s18_t1.mp4 0 3.6
$PY $G takes/mv17_s19_t2.mp4 1.14 4.2
$PY $G takes/mv17_s20_t1.mp4 3.78 9.02
$PY $G takes/mv17_s21_t1.mp4 0 3.94
$PY $G takes/mv17_s23_t1.mp4 0 1.82
$PY $G takes/mv17_s24_t1.mp4 0 5.1
$PY $G takes/mv17_s25_t2.mp4 0 3.1
$PY $G takes/mv17_s26_t1.mp4 0 3.56
$PY $G takes/mv17_s27_t1.mp4 0 3.16
$PY $G takes/mv17_s29_t1.mp4 0 4.72
$PY $G takes/mv17_s30_t1.mp4 0 4.26
$PY $G takes/mv17_s32_t1.mp4 0 6.66
$PY $G takes/mv17_s33_t1.mp4 2.74 5.0
$PY $G takes/mv17_s34_t1.mp4 0 2.94
echo FRAME_GATES_DONE
