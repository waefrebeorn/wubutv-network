#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-18_whats-a-sigma-mom
for t in s08_t2 s15_t1 s16_t1 s17_t1 s18_t1; do
  python3 work/analysis/take_asr.py takes/mv18_$t.mp4 work/qc/${t}_words.json > work/qc/${t}_asr.txt 2>&1
done
echo BATCH3-ASR-DONE
