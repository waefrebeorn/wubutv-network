# MV-7 S03 t1 — QC (v2, recovery run 4, 2026-11-06 ~16:35 EST)

File: takes/media-generation-mv7-s03-t1-0-a60a7857-1f80-4d05-a1b3-5dddb7c7781c.mp4
md5: bdbe8d744976861cc3f9c45dfe1c4e43 · 2,714,608 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s03_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp.
snapshot_id: 28968174-3fae-4a56-9d30-f4aa7451e357:mhq4xy

## Audio / words (faster-whisper small, work/qc_v7/mv7_s03_t1_words.json)
- 22 words, 1 segment, 0.00–9.48s: "I got a profile, got a pile, got a thousand posts in a folder file, old meme face and a busted grin."
- Vehicle lyric delivered exactly once, in order, no repeats. Matches LYRIC_TIMELINE V1.1–V1.3
  ("and a busted grin" — SONG_WORDS "in a busted grin" is a Whisper mishear; timeline adjudicated "and a").
- Take line span 0.00–9.48s vs song slot 19.58–26.82 (7.24s) → line ratio 7.24/9.48 = 0.764 — GREY (0.60–0.80).
  Grey adjudication: word-level transcription confirms the exact lyric, first/last words present and in order;
  warp-rescue at assembly (bounded whole-clip warp to band edge = 1.047x speedup, trivial).
- Repeat-defect scan: PASS. Zero-word? No.

## Frame rule (native 24fps, vocal 0.5–9.5s)
- frames=240, mean_diff=1.888, min=0.823, longest near-dup run = 0 frames. PASS with margin.

## Visual reads (2fps sheet)
- 5.0s: mouth open mid-line ("posts"/"in" region), identity holds, head tilted expressively, monitor rectangles abstract glow.
- G1 PASS, G2 PASS (no readable text), G3 PASS, G4 PASS, G5 PASS (grey ratio, rescue noted), G6 PASS.

## Flags
1. RASTER 1152x768 (3:2) — assembly crops to 16:9.
2. Grey line ratio 0.764 — warp-rescue 1.047x at assembly.

## VERDICT: KEEP-WITH-FLAG
