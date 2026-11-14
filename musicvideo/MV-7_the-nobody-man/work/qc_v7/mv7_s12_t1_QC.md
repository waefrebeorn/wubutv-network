# MV-7 S12 t1 — QC (v2 verbatim, Era B, recovery volley 4, 2026-11-06 ~17:45 EST)

File: takes/media-generation-mv7v2-s12-verse-2-v2-4-v2-6-so-0-3e5963f7-1461-459e-b0cd-3f2063aff438.mp4
md5: 13c8cd48372fab4c6470bca897247831 · 2,574,249 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s12_vehicle.txt verbatim + refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: 53a524aa-78e2-43d7-a4b1-1c00ba843087:46bq24

## Audio / words (faster-whisper small, work/qc_v7/mv7_s12_t1_words.json)
- 13 tokens, 2 segments: "One more clip and chasing that giant shout." 0.00–4.56s ·
  "Everybody chasing that giant shout." 5.04–8.00s.
- Expected 21 words (song 82.94–89.92, span 6.98s): "One more clip and one more zoom. Everybody chasing
  that giant shout. I got a small flame I won't put out".
- V2.4 WRONG: "one more zoom" is replaced by "chasing that giant shout" (the V2.5 phrase pulled forward).
  V2.5 correct in full. V2.6 "I got a small flame I won't put out" ENTIRELY MISSING.
- "chasing that giant shout" recurs after its first delivery → REPEAT DEFECT. FAIL.
- Take span 0.00–8.00s vs song 6.98s → ratio 0.87 IN BAND on delivered words — but coverage fails, so the
  ratio does not save it.
- RMS check: vocal 0–8.0s with an inter-phrase gap ~4.5–5.0s (bins 0.037, 0.011); quiet tail 8.0–10s.
- Zero-word result? No — 13 tokens; split-half recheck not needed. "One" p=0.488 (low) is a side note only.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.076, min=0.511, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.075.
- PASS (FAIL would be run ≥24f or mean <0.5) — the visuals are fine; the failure is audio content only.

## Visual reads (2fps sheet, work/qc_v7/mv7_s12_t1_sheet.png)
- Era B state CORRECT: cork strip crowded with slips, stacks of paper, screens wall, half-burned candle.
- 0.5s: mouth open mid-"One more"; identity holds vs Era B still.
- 4.5s: mouth open at "shout" (4.08–4.56); wider desk-lean framing, same as S11.
- 8.0s: held crooked grin after the last word (the missing V2.6 leaves the tail silent).
- No readable text anywhere (slips and screens illegible/abstract glow). No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds; Era B state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: FAIL (V2.4 wrong, V2.6 missing, repeat defect — 13/21 words).
- G6 banger check: PASS (Verse 2 desk-lean holds; the room keeps filling).

## VERDICT: REJECT
- Reroll axis: COMPLETENESS v2 — name all three lines, V2.6 ("I got a small flame I won't put out") must land;
  the model bleeds V2.5's phrase into V2.4. Same bleed pattern as S13 this volley.
