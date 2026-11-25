#!/bin/bash
# MV-2 lyrics redo: separate the 4 disputed-span excerpts with MDX-Net ONNX
# (torch-free runner). Each excerpt writes its vocals wav immediately;
# if the runtime reaps this loop, completed excerpts survive and the rest
# can be re-run. Run ONLY when no sibling large-v3-turbo job holds memory
# (check `free -m`: need >=2.5 GB available before starting).
cd ~/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb/work/lyrics-redo
MODEL=~/workspace/wubuwizard-cpu-sep/UVR-MDX-NET-Voc_FT.onnx
PY=~/workspace/tools/lyrics-venv/bin/python
for n in l34 l21 l17 echo; do
  if [ -f stems/${n}_vocals.wav ]; then echo "$(date -u +%H:%M:%S) $n already done, skip"; continue; fi
  echo "$(date -u +%H:%M:%S) separating $n ..."
  $PY ~/workspace/wubuwizard-cpu-sep/mdx_onnx_cpu.py "$MODEL" stems/${n}_mix.wav stems/${n}_vocals.wav --threads 1 >> stem_separate.log 2>&1
  echo "$(date -u +%H:%M:%S) $n rc=$? $(ls -la stems/${n}_vocals.wav 2>/dev/null | awk '{print $5}')"
done
echo "$(date -u +%H:%M:%S) ALL DONE"
