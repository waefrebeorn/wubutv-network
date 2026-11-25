#!/bin/bash
# MV-5 stem: separate ONLY the chorus spans (chunks 2-4, 12-18, 26-32, 37-46).
# Chunks 0-1 already on disk. Verse chunks (5-11, 19-25, 33-36) not needed:
# verse times are settled by P1+NOP agreement.
cd /home/hatch/workspace/wubutv-network/musicvideo/detection-research/c11_sep
LR=/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now/work/lyrics-redo
run() { # start nchunks label
  echo "=== span $3: start-chunk $1 chunks $2 ===" >> "$LR/sep_spans.log"
  ./sep_main "$LR/mv5_44k.wav" "$LR/mv5_vocals.wav" --dump-dir "$LR/sep_dumps" --threads 2 --start-chunk "$1" --chunks "$2" >> "$LR/sep_spans.log" 2>&1
  echo "exit=$? span $3 done $(date -u +%H:%M:%S)" >> "$LR/sep_spans.log"
}
run 2 3 intro-tail
run 12 7 chorus1
run 26 7 chorus2
run 37 10 final
echo "ALL SPANS DONE $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LR/sep_spans.log"
