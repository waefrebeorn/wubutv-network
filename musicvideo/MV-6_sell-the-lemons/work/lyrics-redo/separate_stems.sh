#!/bin/bash
# Separate the 5 dense-span excerpts with MDX-Net ONNX (torch-free runner).
# Each excerpt writes its vocals wav immediately; if the runtime reaps this
# loop, completed excerpts survive and the rest can be re-run.
cd ~/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons/work/lyrics-redo
MODEL=~/workspace/wubuwizard-cpu-sep/UVR-MDX-NET-Voc_FT.onnx
PY=~/workspace/tools/lyrics-venv/bin/python
for n in head c1tail bridge fc outro; do
  if [ -f stems/${n}_vocals.wav ]; then echo "$(date -u +%H:%M:%S) $n already done, skip"; continue; fi
  echo "$(date -u +%H:%M:%S) separating $n ..."
  $PY ~/workspace/wubuwizard-cpu-sep/mdx_onnx_cpu.py "$MODEL" stems/${n}_mix.wav stems/${n}_vocals.wav --threads 2 >> stem_separate.log 2>&1
  echo "$(date -u +%H:%M:%S) $n rc=$? $(ls -la stems/${n}_vocals.wav 2>/dev/null | awk '{print $5}')"
done
echo "$(date -u +%H:%M:%S) ALL DONE"
