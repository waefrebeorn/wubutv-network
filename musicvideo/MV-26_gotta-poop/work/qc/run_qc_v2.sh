#!/bin/bash
cd ~/workspace/wubutv-network/musicvideo/MV-26_gotta-poop
# wait for any running take_qc to finish (serialize Whisper on the shared CPU)
while pgrep -f "take_qc[.]py" > /dev/null; do sleep 15; done
python3 work/qc/take_qc.py t1 2,3,4,6,7,8 >> work/qc/qc_t1_v2.log 2>&1
echo V2_QC_CHAIN_DONE >> work/qc/qc_t1_v2.log
