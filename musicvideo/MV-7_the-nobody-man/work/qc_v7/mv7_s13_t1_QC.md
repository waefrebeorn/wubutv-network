# MV-7 S13 t1 — QC (v2 verbatim, Era B, recovery volley 4, 2026-11-06 ~17:45 EST)

File: takes/media-generation-mv7v2-s13-pre-chorus-2-pc2-1-p-0-24146eaf-2c18-4e59-a8a6-f7c524112cc5.mp4
md5: 1585b73d8927540b7e38624def55b2dc · 2,790,888 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s13_vehicle.txt verbatim + refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: b2d993d6-2326-4e1c-b9ee-653262db3e9f:nr8v2g

## Audio / words (faster-whisper small, work/qc_v7/mv7_s13_t1_words.json)
- 13 tokens, 2 segments: "Little by little kept sticking around." 0.00–4.22s ·
  "Little by little I learned the sound." 5.06–8.04s.
- Expected 13 words (song 89.92–95.20, span 5.28s): "I kept clicking, kept sticking around, little by little
  I learned the sound".
- PC2.1 WRONG: "I kept clicking" is MISSING — the model sings "Little by little" (the PC2.2 opener) in its place,
  then "kept sticking around" (correct tail). "Little by little" recurs after its first delivery → REPEAT DEFECT.
- PC2.2 exact in full (7/7 words).
- Take span 0.00–8.04s vs song 5.28s → ratio 0.657 GREY — but content fails, so the ratio does not save it.
- RMS check: vocal 0–4.2s, inter-line gap ~4.5–5.0s (bins 0.003, 0.005 — true quiet), vocal 5.0–8.0s,
  quiet tail 8.0–10s.
- Zero-word result? No — 13 tokens; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.794, min=0.880, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.770.
- PASS with margin.

## Visual reads (2fps sheet, work/qc_v7/mv7_s13_t1_sheet.png)
- Era B state CORRECT: cork strip, stacks, screens wall, half-burned candle.
- 0.5s: mouth open mid-"Little"; identity holds vs Era B still.
- 4.5s: mouth open at "around" (3.54–4.22).
- 8.0s: held grin after the last word; the camera pushes in wide → close-up across the take (continuity note).
- No readable text anywhere. No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds; Era B state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: FAIL (PC2.1 wrong — "I kept clicking" missing, "Little by little" invented and repeated).
- G6 banger check: PASS (pre-chorus 2 holds; the room keeps filling).

## VERDICT: REJECT
- Reroll axis: PC2.1 WORD ACCURACY v2 — "I kept clicking" must land; the model pulls the PC2.2 opener forward
  into PC2.1. Same forward-bleed pattern as S12 this volley (V2.5 phrase into V2.4).
