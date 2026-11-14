# MV-7 S08 t2 — QC (v2 completeness reroll, recovery volley 3, 2026-11-06 ~17:27 EST)

File: takes/media-generation-mv7v2-s08-v2-chorus-1-c1-5-c1-0-485705b7-c49a-4e4e-a84e-6026abff5048.mp4
md5: c04f5f46cfd67c05352289a303711c0c · 2,833,734 B
ffprobe: h264 1280x720, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s08_v2_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp (md5 ca15fc5084ccfedf0e90910f56eac75d).
snapshot_id: c61ac7ad-03dd-4dbc-8659-94b3131645cb:jyb5e8

## Audio / words (faster-whisper small, work/qc_v7/mv7_s08_t2_words.json)
- 13 words, 1 segment: "I got a thousand little sparks flicking in the dark, the nobody man." 0.00–8.82s.
- All three lines delivered in order, finishing on the hook phrase — the v2 completeness axis LANDED (t1 delivered C1.5–C1.6 only).
- Hook lead word is AMBIGUOUS: Whisper decodes the final phrase as "the nobody man" (the 0.12s token "the", p=0.527 — a low-confidence
  guess) where the performed C1.7 is "I'm The Nobody Man". Full-res frame at 7.6s (work/qc_v7/mv7_s08_t2_f7p6s.png) shows the mouth
  OPEN and articulating at the hook onset, so the word is more likely a swallowed "I'm" misheard than a dropped word — adjudicated
  as a probable mishear (same class as the established mishear normalizations), NOT a missing-word fail. Assembly's mouth-state gate
  reads the C1.7 onset on the master and has the final say.
- "Flicking" is a 2.18s near-silent drawl (4.18–6.36s, RMS ~0.009–0.018; full-res frame at 5.0s shows the mouth near-closed mid-hold).
  The word is sung (Whisper p=0.748) but quiet — the C1.6 mouth is weak; see flags.
- Take line span 0.00–8.82s vs song word span 56.18–63.72s (7.54s) → line ratio 7.54/8.82 = 0.855 — IN the 0.80–1.25 band.
- Phrase math for assembly: C1.5 take 0.00–4.18s (4.18s) vs song 2.38s → 1.76x speedup; C1.6 take 4.18–7.48s (3.30s) vs song 1.86s
  → 1.77x speedup; C1.7 take 7.58–8.82s (1.24s) vs song 2.26s → 0.55x slow-down (just above the 0.5x floor). All inside caps,
  all at the edges — disclose.
- RMS check: vocal 1.5–4.0s and 6.0–9.0s; near-silent 4.0–6.0s (the "flicking" drawl); quiet tail 9.0–10.0s — trims cleanly.
- Repeat-defect scan: no word/line subsequence recurs after first delivery. PASS.
- Zero-word result? No — 13 words; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.638, min=0.427, longest near-dup run (<0.5) = 3 frames. Whole-clip mean_diff 1.795.
- PASS with margin (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s08_t2_sheet.png; full-res frames mv7_s08_t2_f{1,5,7p6}s.png)
- 1.0s (full-res): mouth open mid-"I got a thousand"; identity holds STRONGLY vs Era A still (thinning hair, stubble, frayed
  patches both shoulders, charcoal crewneck); tall candle; monitors behind show code-like glyphs at full res — still illegible
  pseudo-code, no readable words. G2 PASS.
- 5.0s (full-res): mouth near-closed, eyes half-closed mid-"flicking" drawl — the C1.6 mouth is weak (flagged).
- 7.6s (full-res): mouth OPEN, articulating at the hook-phrase onset — supports the "I'm"-mishear adjudication.
- 8.5s: held crooked grin after the last word. Slow push-in running throughout; face drifts right.
- No readable text anywhere. No other people. No morphing.

## Gates
- G1 character consistency: PASS. G2 zero unwanted on-screen text: PASS (monitor glyphs illegible at full res). G3 no licensed material: PASS.
- G4 performance window: PASS-WITH-FLAG (mouth open at C1.5 onset and C1.7 onset; near-closed through the C1.6 "flicking" drawl —
  the master gate must read the C1.6 onset; bad-word montage cover is the sanctioned fallback for that span).
- G5 audio-sync placement: PASS-WITH-FLAG (all three lines, in order, ratio 0.855 in band; hook lead word ambiguous — see above).
- G6 banger check: PASS (chorus spark-accumulation beat; more screens lit behind him).

## VERDICT: KEEP-WITH-FLAG
- Flags: (1) HOOK LEAD WORD ambiguous ("the" p=0.527 vs performed "I'm") — mouth open at onset, adjudicated probable mishear;
  assembly mouth-state gate has the final say. (2) C1.6 "flicking" 2.18s near-silent drawl, mouth near-closed at 5.0s — weak
  mouth for that line; montage cover for the span is the fallback. (3) Per-phrase warps all at cap edges (1.76x / 1.77x / 0.55x)
  — disclose. (4) RASTER 1280x720 TRUE 16:9 — first take of the project to return native 16:9; NO crop needed at assembly.
