#!/bin/bash
set -x
P=/home/hatch/workspace/wubutv-network/musicvideo/MV-34_jensens-back
PY=/home/hatch/workspace/tools/lyrics-venv/bin/python
declare -A T=(
 [s01]=media-generation-mv34-s01-t2-desc-0-46003158-2db7-4b05-9110-e600e7c3fde7.mp4
 [s03]=media-generation-mv34-s03-t1-desc-0-46a9e730-13e4-46e9-8681-0d3ef1509835.mp4
 [s04]=media-generation-mv34-s04-t1-desc-0-86d8d668-9a5c-4e3b-8156-27b19f1dc512.mp4
 [s05]=media-generation-mv34-s05-t1-desc-0-2d87f105-ccfc-41dd-b775-017d162dc27a.mp4
 [s06]=media-generation-mv34-s06-t1-desc-0-2ed99e16-13a6-4f2a-8745-0e961b83c5f6.mp4
)
for s in s01 s03 s04 s05 s06; do
  ffmpeg -y -v error -i "$P/takes/${T[$s]}" -vn -ar 16000 -ac 1 "$P/work/assembly/asr/$s.wav"
  $PY "$P/work/qc_take_asr.py" "$P/work/assembly/asr/$s.wav" "$P/work/qc_$s/asr_g7.json" "takes/${T[$s]}"
done
echo ASR_ALL_DONE
