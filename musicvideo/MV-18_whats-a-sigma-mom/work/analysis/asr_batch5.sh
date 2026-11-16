#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-18_whats-a-sigma-mom
for t in s24_t1 s25_t1 s26i_t1 s27_t1 s28_t1 s29_t1; do
  python3 work/analysis/take_asr.py takes/mv18_$t.mp4 work/qc/${t}_words.json > work/qc/${t}_asr.txt 2>&1
done
echo BATCH5-ASR-DONE
