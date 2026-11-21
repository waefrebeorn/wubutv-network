# MV-7 S21 t1 — QC (v2 verbatim, Era C, volley 6, 2026-11-06 ~18:15 EST)

File: takes/media-generation-mv7v2-s21-final-chorus-fc5-fc7-0-f901dd60-cd98-43d9-8ccb-be6c026ee373.mp4
md5: 8ffb5f4aa5dea56951e83ddd2e54d543 · 3,035,376 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s21_vehicle.txt verbatim + refs/nobody_man_v2_eraC.webp (md5 317d8fcd3f513261fd93992f5721981f).
snapshot_id: 240d41a3-5636-4be7-ad28-408581192cb9:hvw5xb

## Audio / words (faster-whisper small, work/qc_v7/mv7_s21_t1_words.json)
- 14 tokens, 1 segment: "I got a thousand little sparks flicking in the dark I'm the nobody man" 0.00–9.24s.
- Expected 14 words (song 152.88–160.02, span 7.14s): FC.5 + FC.6 + FC.7 — ALL LAND, once, in order.
  No repeats. "sparks"/"flicking" heard correctly (SONG_WORDS mishear classes, not take errors).
- Take span 0.00–9.24s vs song 7.14s → ratio 0.773 GREY. Per-line: FC.5 0.68 (assembly warp ~1.47x,
  inside the 1.5x rescue cap), FC.6 0.82, FC.7 0.85. Warp-rescue ~1.29x overall.
- "flicking" is a 1.92s near-silent drawl (3.70–5.62s) — same drawl class as S16 t1's "flicking" (1.92s).
- RMS check: vocal continuous 0–9.24s with a low dip at the drawl; quiet tail 9.3–10s.
- Min word prob 0.510 ("I" at 0.0s, cold-start).

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=2.329, min=0.921, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 2.318.
- PASS (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s21_t1_sheet.png)
- Era C state CORRECT: wall of tiny glowing screens, low stub candle, stacks of paper.
- 0.5s: mouth open mid-"I"; identity holds vs Era C still.
- 5.0s: mouth open at the FC.6 onset; 7.5s: mouth open at the FC.7 onset ("I'm", 6.68–7.94 take time).
- No readable text anywhere (screens are abstract glow). No other people. No morphing.
- Flags: eyes closed through much of the tail (same flag class as S06/S07/S17); a red/pink light wash
  on the face in the last ~2s (same class as S10's red wash — post-vocal, trims cleanly); slow push-in
  drift across the clip (medium → close-up).

## Gates
- G1 character consistency: PASS (identity holds; Era C state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: PASS with flag (14/14 exact, once, in order; grey ratio 0.773, warp-rescue ~1.29x).
- G6 banger check: PASS ("thousand little sparks" lands at full field as planned).

## VERDICT: KEEP-WITH-FLAG
- Flag: grey ratio 0.773 (FC.5 warp ~1.47x, disclose at assembly); "flicking" 1.92s drawl; eyes closed
  through much of the tail; red/pink light wash last ~2s; slow push-in drift; 1152x768 raster.
