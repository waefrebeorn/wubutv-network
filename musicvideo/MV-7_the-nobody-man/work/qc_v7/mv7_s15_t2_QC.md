# MV-7 S15 t2 — QC (v2 reroll, Era B, recovery volley 5, 2026-11-06 ~18:10 EST)

File: takes/media-generation-mv7v2-s15-v2-chorus-2-c2-1-c2-0-44875e3c-d6eb-4b26-8713-3466eebad9ff.mp4
md5: 43426ec08cbe01f83c5316d1ea37df09 · 3,015,338 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s15_v2_vehicle.txt (COMPLETENESS reroll — all four lines,
finishing on the hook, "the chant at start and end") + refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: 839b7b15-15f5-4475-94e9-4d142b8e79a6:x4o7rl

## Audio / words (faster-whisper small, work/qc_v7/mv7_s15_t2_words.json)
- 15 tokens, 1 segment: "I'm the nobody man, still here, still stand, I post, I fade, I post again." 0.00–8.20s.
- Expected 19 words (song 103.36–112.86, C2.1–C2.4): C2.1–C2.3 exact (15 words), but the final
  C2.4 "I'm The Nobody Man" is MISSING — the SAME failure as t1. The model stops after "I post
  again" and holds a silent grin through 8.2–10s. The v2 vehicle did NOT move the failure: two
  pulls, identical drop point.
- Split-half recheck on the 5–10s tail (work/qc_v7/mv7_s15_t2_tail_words.json): decodes "I stand,
  I post, I fade, I post again" only — C2.3's tail, NO chant. RMS tail bins 8.5–10s (0.0293 /
  0.0156 / 0.0163) are near-silent. The chant is genuinely absent, not a decode miss.
- Ratio on delivered words: song C2.1–C2.3 span 7.00s vs take 8.20s → 0.854 IN BAND — but coverage
  fails, so the ratio does not save it.
- Min word prob 0.536 — no low-prob words on delivered lines.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=2.086, min=1.002, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 2.070.
- PASS (FAIL would be run ≥24f or mean <0.5) — the visuals are fine; the failure is audio content only.

## Visual reads (2fps sheet, work/qc_v7/mv7_s15_t2_sheet.png)
- Era B state CORRECT: cork strip crowded, screens filling behind him, half-burned candle.
- 0.5s: mouth open mid-"I'm"; identity holds vs Era B still.
- 4.5s: mouth open at "stand" (4.84–5.34 take time); push-in framing.
- 8.0s: mouth open at "again" (7.80–8.20), then eyes-closed soft smile in the silent tail (8.2–10s)
  — the missing C2.4 leaves the tail silent.
- No readable text anywhere (slips and screens illegible/abstract glow). No other people. No morphing.
- Flag: strong push-in drift across the clip (medium → tight close-up by the tail).

## Gates
- G1 character consistency: PASS (identity holds; Era B state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: FAIL (C2.4 final chant MISSING — 15/19 words; full pass + tail split-half agree).
- G6 banger check: PASS (Chorus 2 push-in holds; wall filling).

## VERDICT: REJECT — S15 is STRUCTURAL
- Two pulls, identical failure mode (t1 and t2 both stop after "I post again", both drop the final
  chant). Per the two-denied-rerolls rule the scene retires from generation — NO v3, no third pull
  of the same axis. Assembly treatment: beat-cut to montage for exactly the C2.4 span (song
  110.36–112.86s), back at C2.5 (S16 t1). The hook phrase still lands twice in Chorus 2's tail
  (S17 covers C2.7–C2.8), so the chant is not lost from the chorus. C2.1–C2.3 of t2 remain usable
  as assembly cover only — NOT as a vocal take (a take that drops its final line cannot carry the scene).
