# MV-7 S15 t1 — QC (v2 verbatim, Era B, recovery volley 4, 2026-11-06 ~17:45 EST)

File: takes/media-generation-mv7v2-s15-chorus-2-c2-1-c2-4-s-0-ba6ce068-9c0e-43ac-95aa-f5e7bf4f15a7.mp4
md5: 432a95e2a70d7dada1a98752923b2dd4 · 2,901,286 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s15_vehicle.txt verbatim + refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: 46a7901a-8166-464e-85c9-a3d17286d34b:ri5lwe

## Audio / words (faster-whisper small, work/qc_v7/mv7_s15_t1_words.json)
- 15 tokens, 1 segment: "I'm the nobody man, still here, still stand, I post, I fade, I post again." 0.00–8.98s.
- C2.1–C2.3 exact (15/15 words delivered): "I'm The Nobody Man." + "Still here, still stand." + "I post, I fade,
  I post again."
- Final C2.4 "I'm The Nobody Man" MISSING — the song has 19 words in C2 (103.36–112.76, span 9.40s); the take
  delivers 15 and stops after "I post again". Same failure shape as S08 t1 (C1.7 missing) in volley 2.
- Ratio 9.40/8.98 = 1.047 IN BAND on delivered words — but coverage fails, so the ratio does not save it.
- RMS check: vocal 0–9.0s with short inter-line dips (bins 0.012 at 3.5–4.0, 0.011 at 9.5–10 is the quiet tail);
  quiet tail 9.0–10s — the model simply stopped, no trailing vocal.
- Repeat-defect scan: no recurrence. PASS.
- Zero-word result? No — 15 tokens; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.989, min=0.573, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.928.
- PASS.

## Visual reads (2fps sheet, work/qc_v7/mv7_s15_t1_sheet.png)
- Era B state CORRECT: cork strip, stacks, screens wall, half-burned candle.
- 0.5s: mouth open mid-"I'm"; identity holds vs Era B still.
- 4.5s: mouth open at "still" (4.46–5.00).
- 8.0s: mouth open at "post" (8.18–8.58); slow push-in across the take.
- No readable text anywhere. No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds; Era B state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: FAIL (final C2.4 hook phrase missing — 15/19 words).
- G6 banger check: PASS (chorus 2 holds; the room keeps filling).

## VERDICT: REJECT
- Reroll axis: COMPLETENESS v2 — the final chant "I'm The Nobody Man" must land; the model stops after
  "I post again". Same completeness axis that fixed S08 (t1 → t2) in volley 3.
