# MV-7 S04 t1 — QC (v2, recovery run 4, 2026-11-06 ~16:35 EST)

File: takes/media-generation-mv7-s04-t1-0-6cc10eaf-bba6-4ae1-a7d6-dd76a6176e17.mp4
md5: 23933f5a065ac2ef1e27eea4e297e941 · 2,499,872 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s04_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp.
snapshot_id: 7a5f8ff2-a4e3-40d1-abaf-14cac37fc882:qgrw14

## Audio / words (faster-whisper small, work/qc_v7/mv7_s04_t1_words.json)
- 24 words, 2 segments: "Been here so long I could sign back in" 0.00–3.70 + "Made a joke at a quarter past eight watched it sit there while I wait" 4.44–9.68.
  (0.74s pause between the two sentences — natural phrasing, not a defect.)
- Vehicle lyric delivered exactly once, in order, no repeats. Matches LYRIC_TIMELINE V1.4–V1.6
  ("Made a joke at a quarter past eight" — SONG_WORDS "I prayed a joke" is a Whisper mishear; timeline adjudicated "Made").
- Take line span 0.00–9.68s vs song slot 26.82–34.02 (7.20s) → line ratio 7.20/9.68 = 0.744 — GREY (0.60–0.80).
  Grey adjudication: exact lyric, first/last words present and in order; warp-rescue at assembly (1.075x speedup to band edge).
- Repeat-defect scan: PASS. Zero-word? No.

## Frame rule (native 24fps, vocal 0.5–9.5s)
- frames=240, mean_diff=1.427, min=0.552, longest near-dup run = 0 frames. PASS.

## Visual reads (2fps sheet)
- 5.0s: mouth open mid-line, eyes closed singing, identity holds, candle edge right.
- G1 PASS, G2 PASS (no readable text), G3 PASS, G4 PASS, G5 PASS (grey ratio, rescue noted), G6 PASS.

## Flags
1. RASTER 1152x768 (3:2) — assembly crops to 16:9.
2. Grey line ratio 0.744 — warp-rescue 1.075x at assembly.

## VERDICT: KEEP-WITH-FLAG
