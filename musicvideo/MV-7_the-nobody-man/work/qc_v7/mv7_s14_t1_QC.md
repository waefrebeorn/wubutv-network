# MV-7 S14 t1 — QC (v2 verbatim, Era B, recovery volley 4, 2026-11-06 ~17:45 EST)

File: takes/media-generation-mv7v2-s14-pre-chorus-2-pc2-3-p-0-7b5a8b0a-affc-4a1f-97ea-91f9b5a5a630.mp4
md5: 2043def7f8a057f53465d4aba34d1000 · 3,416,469 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s14_vehicle.txt verbatim + refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: 33ef8aa6-bda5-4aa5-a8f0-6f48037e9be9:0f50hn

## Audio / words (faster-whisper small, work/qc_v7/mv7_s14_t1_words.json)
- 15 tokens, 1 segment: "No one crowned me, no one had to. I made this mess on purpose too." 0.00–8.02s.
- 15/15 words exact, once, in order — "No one crowned me, no one had to." (PC2.3) + "I made this mess on
  purpose too" (PC2.4).
- Take line span 0.00–8.02s vs song word span 8.16s (95.20–103.36) → line ratio 8.16/8.02 = 1.017 IN BAND.
- RMS check: vocal 0–4.5s, inter-line gap 4.5–5.5s (bins 0.026, 0.009 — true quiet between the two lines),
  vocal 5.5–8.0s, quiet tail 8.0–10s.
- Repeat-defect scan: no word/line subsequence recurs after first delivery. PASS.
- Zero-word result? No — 15 tokens; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=2.639, min=1.496, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 2.604.
- PASS with wide margin — STRONGEST frame rule of volley 4.

## Visual reads (2fps sheet, work/qc_v7/mv7_s14_t1_sheet.png)
- Era B state CORRECT: cork strip, stacks, screens wall, half-burned candle.
- 0.5s: mouth open mid-"No"; identity holds vs Era B still.
- 4.5s: mouth open at "to" (4.06–4.46) — the end of PC2.3.
- 8.0s: mouth open at "too" (7.52–8.02); the camera pushes in across the take.
- The wall sparks STIR in the tail (rows 4, bright spark burst behind his head) — the vehicle beat lands.
- No readable text anywhere. No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds; Era B state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at 0.5s, 4.5s, 8.0s reads; single singer facing camera).
- G5 audio-sync placement: PASS-WITH-FLAG (15/15 words, ratio 1.017 in band).
- G6 banger check: PASS (pre-chorus 2 lands; sparks stir on cue).

## VERDICT: KEEP-WITH-FLAG
- Flags: (1) RASTER 1248x704 (~16:9) — assembly crops/pads. (2) Sings 0.00–8.02 vs vehicle window 0.5–9.5s.
  (3) Push-in framing across the take.
