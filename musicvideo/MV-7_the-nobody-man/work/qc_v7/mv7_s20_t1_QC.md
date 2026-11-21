# MV-7 S20 t1 — QC (v2 verbatim, Era C, volley 6, 2026-11-06 ~18:15 EST)

File: takes/media-generation-mv7v2-s20-final-chorus-fc1-fc4-0-95f874f2-e42c-4981-9b3a-4399014ab0f5.mp4
md5: 57a53cf02c1f3d7126660294ad82b18c · 3,091,370 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s20_vehicle.txt verbatim + refs/nobody_man_v2_eraC.webp (md5 317d8fcd3f513261fd93992f5721981f).
snapshot_id: 2cdf4c79-e660-4d7e-ac8b-817bf3f220c4:tmhsws

## Audio / words (faster-whisper small, work/qc_v7/mv7_s20_t1_words.json)
- 15 tokens, 1 segment: "I'm the nobody man, still here, still stand, I post, I fade, I post again." 0.00–8.00s.
- Expected 19 words (song 143.40–152.88, span 9.48s): FC.1–FC.4. Take delivers FC.1–FC.3 only (15 words);
  FC.4 "I'm The Nobody Man" (song 150.38–152.88) is MISSING — full pass + 5–10s tail split-half agree
  (tail: "And I post, I fade, I post again." — FC.3's tail only, no FC.4; tail RMS 8–10s ~0.006 = silent).
- Ratio on delivered words: song FC.1–FC.3 6.98s vs take 8.00s → 0.87 IN BAND. Per-line: FC.1 0.92,
  FC.2 1.03, FC.3 0.95 — all in band. Coverage fails, not pace.
- Min word prob 0.774 — no low-prob words.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=2.667, min=0.908, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 2.579.
- PASS (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s20_t1_sheet.png)
- Era C state CORRECT: wall of tiny glowing screens, low stub candle, stacks of paper.
- 0.5s: mouth open mid-"I'm"; identity holds vs Era C still.
- 5.0s: mouth open at the FC.3 onset; push-in drift across the clip (medium → close-up), same drift
  class as the Era B volley-5 singing takes.
- No readable text anywhere (screens are abstract glow). No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds; Era C state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: FAIL — coverage: FC.4 missing (15/19 words; ratio in band on delivered words).
- G6 banger check: PASS (Final Chorus opens on the spark wall as planned).

## VERDICT: REJECT
- Reroll axis: COMPLETENESS v2 — name all four lines, finish on the hook (same axis that fixed S08 t1 → t2).
  Visuals PASS; the vehicle is fine, the model dropped the final chant.
