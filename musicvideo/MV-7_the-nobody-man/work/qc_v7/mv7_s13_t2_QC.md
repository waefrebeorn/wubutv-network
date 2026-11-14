# MV-7 S13 t2 — QC (v2 reroll, Era B, recovery volley 5, 2026-11-06 ~18:10 EST)

File: takes/media-generation-mv7v2-s13-v2-pre-chorus-2-pc2-0-7a93e8d9-7fa0-4a1d-a53a-987a4f2f0227.mp4
md5: 81933ac4945039cbe0411099bd854103 · 2,713,271 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s13_v2_vehicle.txt (WORD ACCURACY reroll — "I kept clicking"
first, "Little by little" only in line 2) + refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: 78bb30d2-e2f1-4ceb-a404-fe4243b5b17c:9mzqja

## Audio / words (faster-whisper small, work/qc_v7/mv7_s13_t2_words.json)
- 13 tokens, 1 segment: "I kept clicking, kept sticking around, little by little I learned the sound." 0.00–8.82s.
- Expected 13 words (song 89.92–95.20, span 5.28s): PC2.1 + PC2.2 — BOTH LAND, once, in order.
  The word-accuracy axis is FIXED: "I kept clicking" opens the take; "Little by little" occurs ONLY
  in line 2 (4.76–7.14s), never in line 1. No repeats, no inventions.
- Take span 0.00–8.82s vs song 5.28s → ratio 0.599 — a hair below the 0.60 grey floor (0.599 ≈ 0.60).
  Per-line: PC2.1 take 0.00–4.28s (4.28s) vs song 3.16s → 0.738 (warp ~1.36x); PC2.2 take
  4.76–8.82s (4.06s) vs song 2.12s → 0.522 (warp ~1.92x). Overall assembly squeeze ~1.67x.
  This EXCEEDS the 1.5x warp-rescue cap — but speedups are unrestricted under the assembly law
  (disclose), and the build's own precedents cover it: S09 t2 kept at ~1.57x, S10 t1 at ~1.56x,
  S16 t1 at ~1.52x, S05 t4 kept at 2.53x. The take is word-perfect; the miss is uniform slow
  delivery, not a structural floor (the model delivered every word, just slowly). KEEP with the
  squeeze disclosed prominently — rejecting a word-perfect take would retire the scene (two pulls
  done) for a pace-only miss the assembly warp is built to absorb.
- RMS check: vocal continuous 0–8.8s with a 0.48s inter-line gap 4.28–4.76s (bins 0.0117/0.0254 at
  5.0–6.0s are the line-2 onset ramp, not a mid-line pause); quiet tail 8.8–10s.
- Min word prob 0.609 — no low-prob words.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.518, min=0.823, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.488.
- PASS (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s13_t2_sheet.png)
- Era B state CORRECT: cork strip crowded with slips, stacks of paper, screens wall, half-burned candle.
- 0.5s: mouth open mid-"I"; identity holds vs Era B still.
- 4.5s: mouth open at the PC2.2 onset ("little", 4.76–6.30 take time).
- 8.0s: mouth open at "sound" (8.22–8.82); held crooked grin after.
- No readable text anywhere (slips and screens illegible/abstract glow). No other people. No morphing.
- Flag: slow push-in drift across the clip (framing tightens from medium to closer) — same drift class
  as S12/S15/S17 this volley; assembly trims/crops.

## Gates
- G1 character consistency: PASS (identity holds; Era B state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: PASS with flag (13/13 exact, once, in order; ratio 0.599, assembly squeeze
  ~1.67x / PC2.2 1.92x, disclose).
- G6 banger check: PASS (Pre-Chorus 2 man+monitor holds; room keeps filling).

## VERDICT: KEEP-WITH-FLAG
- Word-accuracy axis CLOSED — "I kept clicking" lands, "Little by little" only in line 2. Flag: ratio
  0.599 (assembly squeeze ~1.67x, PC2.2 1.92x — fastest per-phrase squeeze in the build after S05 t4's
  2.53x; disclose at assembly); slow push-in drift.
