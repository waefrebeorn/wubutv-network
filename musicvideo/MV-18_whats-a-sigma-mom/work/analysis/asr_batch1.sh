#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-18_whats-a-sigma-mom
for t in s02_t1 s05_t1 s06_t1 s07_t1 s11_t2; do
  python3 work/analysis/take_asr.py takes/mv18_$t.mp4 work/qc/${t}_words.json > work/qc/${t}_asr.txt 2>&1
done
echo BATCH1-ASR-DONE
