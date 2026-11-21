#!/bin/bash
# MV-3 lyrics redo: separate the 5 dense-span excerpts with MDX-Net ONNX
# (torch-free runner). Each excerpt writes its vocals wav immediately;
# if the runtime reaps this loop, completed excerpts survive and the rest
# can be re-run. Run ONLY when no sibling large-v3-turbo job holds memory
# (check `free -m`: need >=2.5 GB available before starting).
cd ~/workspace/wubutv-network/musicvideo/MV-3_i-am-your-dad/work/lyrics-redo
MODEL=~/workspace/wubuwizard-cpu-sep/UVR-MDX-NET-Voc_FT.onnx
PY=~/workspace/tools/lyrics-venv/bin/python
for n in l13 l26 l27 l34 l38; do
  if [ -f stems/${n}_vocals.wav ]; then echo "$(date -u +%H:%M:%S) $n already done, skip"; continue; fi
  echo "$(date -u +%H:%M:%S) separating $n ..."
  $PY ~/workspace/wubuwizard-cpu-sep/mdx_onnx_cpu.py "$MODEL" stems/${n}_mix.wav stems/${n}_vocals.wav --threads 1 >> stem_separate.log 2>&1
  echo "$(date -u +%H:%M:%S) $n rc=$? $(ls -la stems/${n}_vocals.wav 2>/dev/null | awk '{print $5}')"
done
echo "$(date -u +%H:%M:%S) ALL DONE"
