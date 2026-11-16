# MV-7 S12 t2 — QC (v2 reroll, Era B, recovery volley 5, 2026-11-06 ~18:10 EST)

File: takes/media-generation-mv7v2-s12-v2-verse-2-v2-4-v2-6-0-1a61d504-11f7-48f5-a378-14e910f0385e.mp4
md5: 383a843492b1c954c08b2c6737a65f27 · 2,809,334 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s12_v2_vehicle.txt (COMPLETENESS reroll — all three lines in order,
"chasing that giant shout" only in the second line) + refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: 47cbe026-ed46-4c52-a670-f7cca9907010:agpi9l

## Audio / words (faster-whisper small, work/qc_v7/mv7_s12_t2_words.json)
- 21 tokens, 3 segments: "One more clip and one more zoom." 0.00–3.24s ·
  "Everybody chasing that giant shout." 4.18–6.82s ·
  "I got a small flame I won't put out." 7.24–9.52s.
- Expected 21 words (song 82.94–89.92, span 6.98s): V2.4 + V2.5 + V2.6 — ALL THREE LAND, once,
  in order. The forward-bleed is FIXED: V2.4 sings "one more zoom" (not the V2.5 phrase), V2.6
  "I got a small flame I won't put out" present in full. No repeats — "chasing that giant shout"
  occurs exactly once.
- Take span 0.00–9.52s vs song 6.98s → ratio 0.733 GREY. Per-phrase: V2.4 take 3.24s vs song
  2.24s → 0.69 (assembly warp ~1.45x, inside the 1.5x rescue cap); V2.5 2.64s vs 2.48s → 0.94;
  V2.6 2.28s vs 2.26s → 0.99. Warp-rescue ~1.36x overall.
- RMS check: vocal continuous 0–9.5s with inter-phrase gaps ~3.5–4.0s (bin 0.0296) and ~6.9–7.2s;
  quiet tail 9.5–10s (bin 0.0106).
- "One" p=0.471 (low) is a side note only — the word is visible at the 0.5s frame read.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.161, min=0.669, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.153.
- PASS (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s12_t2_sheet.png)
- Era B state CORRECT: cork strip crowded with slips, stacks of paper, screens wall, half-burned candle.
- 0.5s: mouth open mid-"One"; identity holds vs Era B still.
- 4.5s: mouth open at "shout" (6.00–6.44 take time); desk-lean framing.
- 8.0s: mouth open at "flame" (8.04–8.44); hand resting near the candle flame in the tail frames.
- No readable text anywhere (slips and screens illegible/abstract glow). No other people. No morphing.
- Flag: slow push-in drift across the clip (framing tightens from medium to closer) — same drift class
  as S13/S15/S17 this volley; assembly trims/crops.

## Gates
- G1 character consistency: PASS (identity holds; Era B state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: PASS with flag (21/21 exact, once, in order; grey ratio 0.733, warp-rescue ~1.36x).
- G6 banger check: PASS (Verse 2 desk-lean holds; the room keeps filling).

## VERDICT: KEEP-WITH-FLAG
- Completeness axis CLOSED — V2.6 lands, no bleed, no repeat. Flag: grey ratio 0.733 (V2.4 warp ~1.45x,
  disclose at assembly); slow push-in drift; "One" p=0.471.
