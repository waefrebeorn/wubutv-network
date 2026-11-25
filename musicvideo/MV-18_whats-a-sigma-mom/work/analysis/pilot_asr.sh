#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-18_whats-a-sigma-mom
for t in s01_t1 s03_t1 s11_t1; do
  python3 work/analysis/take_asr.py takes/mv18_$t.mp4 work/qc/${t}_words.json > work/qc/${t}_asr.txt 2>&1
done
echo PILOT-ASR-DONE
