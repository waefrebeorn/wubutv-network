# MV-7 S06 t1 — QC (v2, recovery volley 2, 2026-11-06 ~16:55 EST)

File: takes/media-generation-mv7v2-s06-pre-chorus-1-pc1-3-p-0-caec5eb5-e54a-4bff-b22d-a38f9f6a7e22.mp4
md5: b27f6c4c4a5dba8749cdbcaf322974c0 · 2,333,813 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s06_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp.
snapshot_id: 5e50c2f0-1d84-451e-a5e4-b39f3fbad5c1:e3fjzi

## Audio / words (faster-whisper small, work/qc_v7/mv7_s06_t1_words.json)
- 10 words, 1 segment: "Nobody noticing, fine by me, I built my kingdom quietly." 0.00–8.60s.
- Word list matches the vehicle lyric 10/10 (case-insensitive; "Nobody noticing? Fine by me. I built my kingdom quietly").
- Take line span 0.00–8.60s vs song slot 38.60–46.20s (7.60s) → line ratio 7.60/8.60 = 0.884 — IN the 0.80–1.25 band.
- Phrase math for assembly: line 1 "Nobody noticing, fine by me" take 0.00–5.14s vs song 4.30s (0.84x warp); line 2
  "I built my kingdom quietly" take 5.32–8.60s vs song 3.30s (1.01x). Both inside caps; the 2.32–3.38s inter-line
  silence in the take absorbs into the line-1 warp.
- Repeat-defect scan: no word/line subsequence recurs after first delivery. PASS.
- Zero-word result? No — 10 words; split-half recheck not needed. (First-word "Nobody" prob 0.66 — clip-start wobble, confirmed by segment text.)

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.377, min=0.606, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.428.
- PASS with margin (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s06_t1_sheet.png)
- 0.5s: mouth open mid-"Nobody"; identity holds vs Era A still (thinning hair, stubble, frayed patches both shoulders, charcoal crewneck); tall candle right, monitor glow abstract.
- 5.0s: mouth OPEN mid-line ("me" 4.62–5.14); framing tighter than the still — slow push-in running.
- 8.0s: mouth open at "quietly" (7.74–8.60); eyes closed, singing expression.
- First spark LANDED: a small red dot lights on the dark wall behind him from ~4s onward — the S06 motif beat the vehicle asked for.
- No readable text anywhere (monitor rectangles abstract glow, papers illegible). No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds across all sampled frames).
- G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at 0.5s, 5.0s, 8.0s reads; single singer facing camera).
- G5 audio-sync placement: PASS (ratio 0.884; all 10 words in order, once).
- G6 banger check: PASS (pre-chorus escalation beat — first spark lights; candle + monitor glow carry the look).

## Flags (not fails)
1. RASTER 1152x768 (3:2), not 1280x720 16:9 — the Era A still is 1920x1280 (3:2) and aspect followed the image despite "16:9 landscape" in the vehicle text. Assembly crops to 16:9 (1152x648 → upscale). Same class as MV-6 S16.
2. Take sings 0.00–8.60 vs vehicle window 0.5–9.5s (starts 0.5s early; last word ends 0.90s before window end). Assembly trims/warps; ratio in band.
3. Slow rightward camera drift through the clip — the man ends near the right edge of frame by the tail, face slightly cropped at the edge in the last ~1s. The vehicle asked static MAN + MONITOR; the drift is unprompted but the face stays readable through the vocal window (words end 8.60s).
4. Eyes closed through much of both lines — expressive singing, not a fail.

## VERDICT: KEEP-WITH-FLAG
