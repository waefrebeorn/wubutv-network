# MV-7 S01 t3 — QC (v4 completeness-by-explicit-count reroll, recovery volley 3, 2026-11-06 ~17:27 EST)

File: takes/media-generation-mv7v2-s01-v4-intro-chant-i1-so-0-27ce3c0b-70af-433b-806d-6b832f16c405.mp4
md5: 9f8d2c3b8fdddac9c09ed92edf0aec3b · 2,534,665 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s01_v4_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp (md5 ca15fc5084ccfedf0e90910f56eac75d).
snapshot_id: 23738e19-8182-404a-b03c-af51d0f0ac88:ypl4h5

## Audio / words (faster-whisper small, work/qc_v7/mv7_s01_t3_words.json)
- 12 words, 3 segments:
  - "I'm the nobody man." 0.00–1.54s (occurrence 1, clean).
  - "Nobody man, nobody man three." 2.28–4.54s (occurrences 2–3 — the model LITERALLY SANG the count word "three" after occurrence 3; p=0.58).
  - "Nobody man four." 5.34–6.28s (occurrence 4 — again the count word "four" sung as a lyric word; p=0.954).
- Occurrence 5 is MISSING entirely. Tail split-half recheck (6.5–10.0s slice, work/qc_v7/mv7_s01_t3_tail_words.json):
  0 words; RMS bins 6.5–8.0s ≈ 0.003–0.006 (silent), 8.0–10.0s RMS 0.034–0.090 max-abs 0.42 is non-vocal bed/hum, no words.
- Repeat-defect scan: the chant occurrences are the prompted line itself, not a re-sing; the defect is WRONG words ("three", "four" sung as lyrics), not repeats. FAIL on word identity.
- Zero-word result? No — 12 words; split-half recheck done on the tail only (above).

## Song side (adjudicated volley 1, stands)
- Performed chant = "I'm the nobody man" x1, then "Nobody man" x4 (onsets ~0.0 / 4.70 / 5.78 / 7.50 / 8.04),
  last word ends 9.46s. Take line span 0.00–6.28s vs song word span 0.00–9.46s → line ratio 9.46/6.28 = 1.506 (GREY 1.25–1.60).
- Coverage gap: song keeps chanting 6.28–9.46s (occurrences 4–5 as performed) with NO clean singing picture from this take,
  and occurrences 3–4 as delivered carry wrong count words.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.533, min=0.535, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.649.
- PASS with margin (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s01_t3_sheet.png)
- 0.5s: mouth wide open mid-"I'm"; identity holds vs Era A still (thinning hair, stubble, frayed patches, charcoal crewneck); tall candle right, cork board behind.
- 5.0s: mouth open mid-chant; slow push-in running, face drifting right.
- 8.0s: mouth in held crooked grin, eyes closed — the silent tail reads as a held smile, not singing.
- No readable text anywhere (cork-board papers illegible, monitor glow abstract). No other people. No morphing.

## Gates
- G1 character consistency: PASS. G2 zero unwanted on-screen text: PASS. G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open through 0.5–6.3s; single singer facing camera).
- G5 audio-sync placement: FAIL — incomplete line (4 of 5 occurrences; occurrences 3–4 corrupted by literally-sung count words "three"/"four"; occurrence 5 absent).
- G6 banger check: PASS (hook scene, face in the dark, candle + monitor glow).

## VERDICT: REJECT — S01 is STRUCTURAL
- Three pulls, three failure modes on this slot: t1 full phrase x5 → 3 occurrences then silent; t2 elided x5 → 3 occurrences
  then silent; t3/v4 explicit count → 4 occurrences with the count words sung as lyrics and no fifth. The completeness axis is
  EXHAUSTED — the model either caps this chant at ~3 or vocalizes the count. NO v5 (brief's rule).
- Structural treatment (assembly's call, volley-2 note anticipated): split the chant across two takes (S01a = t2's clean first 3
  occurrences 0–6.2s; S01b = last 2 occurrences via a fresh restage vehicle or beat-matched montage cover). S01 leaves the
  generation queue; do NOT re-fire the S01 vehicle.
- Raster flag carried: 1152x768 (3:2) — assembly crops to 16:9.
