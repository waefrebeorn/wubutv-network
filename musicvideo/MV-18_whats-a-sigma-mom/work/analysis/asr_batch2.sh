#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-18_whats-a-sigma-mom
for t in s04i_t1 s08_t1 s09_t1 s10_t1 s12_t1 s13_t1; do
  python3 work/analysis/take_asr.py takes/mv18_$t.mp4 work/qc/${t}_words.json > work/qc/${t}_asr.txt 2>&1
done
echo BATCH2-ASR-DONE
