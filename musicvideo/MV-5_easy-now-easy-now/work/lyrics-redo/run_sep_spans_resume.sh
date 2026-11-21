#!/bin/bash
# Resume after the 2026-11-12 ~19:46 UTC VM reboot killed run_sep_spans.sh
# mid-Chorus-2 (chunk 26 done, chunk 27 never started). Chorus 1 is done
# (chunks 12-18). Re-run chorus2 (chunk 26 is skipped as already on disk)
# then final. Idempotent per-chunk checkpointing.
cd /home/hatch/workspace/wubutv-network/musicvideo/detection-research/c11_sep
LR=/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now/work/lyrics-redo
run() { # start nchunks label
  echo "=== span $3: start-chunk $1 chunks $2 (resume $(date -u +%H:%M:%S)) ===" >> "$LR/sep_spans.log"
  ./sep_main "$LR/mv5_44k.wav" "$LR/mv5_vocals.wav" --dump-dir "$LR/sep_dumps" --threads 2 --start-chunk "$1" --chunks "$2" >> "$LR/sep_spans.log" 2>&1
  echo "exit=$? span $3 done $(date -u +%H:%M:%S)" >> "$LR/sep_spans.log"
}
run 26 7 chorus2
run 37 10 final
echo "ALL SPANS DONE $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LR/sep_spans.log"
