# MV-7 S20 t2 — QC (v2 completeness vehicle, Era C, volley 7, 2026-11-06 ~18:40 EST)

File: takes/media-generation-mv7v2-s20-t2-0-918d720a-9968-4d6a-ae48-b30351b503e5.mp4
md5: f80b133c10191def1508480136a40a8c · 3,789,033 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s20_v2_vehicle.txt verbatim + refs/nobody_man_v2_eraC.webp (md5 317d8fcd3f513261fd93992f5721981f).
snapshot_id: 63986ed4-7421-4424-a4fa-c89f0f057877:h454hr

## Audio / words (faster-whisper small, work/qc_v7/mv7_s20_t2_words.json)
- 15 tokens, 3 segments: "I'm the nobody man." 0.00–2.18s; "Still here, still stand." 2.94–5.10s;
  "I post, I fade, I post again." 5.50–8.12s.
- Expected 19 words (song 143.40–152.88, span 9.48s): FC.1–FC.4. Take delivers FC.1–FC.3 only (15 words);
  FC.4 "I'm The Nobody Man" (song 150.38–152.68) is MISSING — SAME failure as t1. Full pass + 5–10s tail
  split-half agree (tail: "I post, I fade, I post again." — FC.3's tail only, no FC.4; tail RMS 8–10s
  ~0.006–0.011 = silent).
- Ratio on delivered words: song FC.1–FC.3 6.98s vs take 8.12s → 0.86 IN BAND. Per-line: FC.1 0.94,
  FC.2 1.00, FC.3 0.95 — all in band. Coverage fails, not pace.
- Min word prob 0.771 ("man." FC.1) — no low-prob words.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=2.926, min=1.841, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 2.833.
- PASS (FAIL would be run ≥24f or mean <0.5). Strongest frame rule of the two S20 pulls (t1: 2.667).

## Visual reads (2fps sheet, work/qc_v7/mv7_s20_t2_sheet.png)
- Era C state CORRECT: wall of tiny glowing screens, low stub candle, stacks of paper.
- 0.5s: mouth open mid-"I'm"; identity holds vs Era C still.
- 5.0s: mouth open at the FC.3 onset; push-in drift across the clip (medium → close-up), same drift
  class as the Era B volley-5 and Era C volley-6 singing takes.
- Eyes closed in a few mid frames on speaking beats (FC.2) — speaking-beat reads, not a deadpan break.
- No readable text anywhere (screens are abstract glow). No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds; Era C state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: FAIL — coverage: FC.4 missing (15/19 words; ratio in band on delivered words).
- G6 banger check: PASS (Final Chorus opens on the spark wall as planned).

## VERDICT: REJECT — S20 STRUCTURAL
- Two pulls, identical drop point (FC.4 missing in t1 AND t2) — the completeness axis is exhausted, NO v3
  (two-denied-rerolls rule, same as S01/S15). Assembly treatment: t2 is the FC.1–FC.3 base (15/15 words,
  once, in order — marginally stronger than t1 on frame rule 2.926 vs 2.667); beat-cut to montage for
  exactly the FC.4 span (150.38–152.88s), back at FC.5 (S21 t1). The hook still lands twice in the
  Final Chorus tail (S21 covers FC.5–FC.7, S22 FC.8–FC.9).
