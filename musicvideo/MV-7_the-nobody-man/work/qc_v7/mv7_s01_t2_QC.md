# MV-7 S01 t2 — QC (v3 lyric-as-performed reroll, recovery volley 2, 2026-11-06 ~16:55 EST)

File: takes/media-generation-mv7v2-s01-v3-intro-chant-i1-so-0-8a128f27-bc6d-41bd-8315-1f246e5adc1f.mp4
md5: d6ffd61f7659fbe84d2a4ea6de0ba2f9 · 2,741,779 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s01_v3_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp (md5 ca15fc5084ccfedf0e90910f56eac75d).
snapshot_id: 0476826f-d324-45e1-b454-e3393d6f640d:rkf0iw

## Audio / words (faster-whisper small, work/qc_v7/mv7_s01_t2_words.json)
- 8 words, 1 segment: "I'm the nobody man, nobody man, nobody man" 0.00–6.20s (onsets 0.00 / 2.70 / 4.80).
- Vehicle asked the elided chant x5 (12 words: full phrase once + "nobody man" x4). Take delivers 3 of 5 occurrences, then SILENT 6.20–10.00s.
- RMS check (16kHz wav, 0.5s bins): 6.5–10.0s rms ≈ 0.003–0.008, max ≤ 0.10 — the tail is genuinely silent, not a Whisper miss.
- Repeat-defect scan: no word/line subsequence recurs after first delivery (the 3 occurrences are the prompted chant). PASS.
- Zero-word result? No — 8 words; split-half recheck not needed.

## Song side (adjudicated volley 1, stands)
- Performed chant = "I'm the nobody man" x1, then "Nobody man" x4 (onsets ~0.0 / 4.70 / 5.78 / 7.50 / 8.04),
  last word ends 9.46s. Take line span 0.00–6.20s vs song word span 0.00–9.46s → line ratio 9.46/6.20 = 1.526 (GREY 1.25–1.60).
- Coverage gap: song keeps chanting 6.20–9.46s (2 "Nobody man" occurrences) with NO singing picture from this take.
- Pattern: TWO pulls on this slot (t1 full phrase x5, t2 elided x5) both returned exactly 3 occurrences. The model caps this chant at ~3 repeats per take.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=2.134, min=0.792, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 2.131.
- PASS with margin (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s01_t2_sheet.png)
- 0.5s: mouth wide open mid-"I'm"; identity holds vs Era A still (thinning hair, stubble, frayed patches, charcoal crewneck); tall candle right, monitor glow abstract.
- 5.0s: mouth open mid-chant; slow push-in visible.
- 8.0s: mouth in held crooked grin, eyes closed — the silent tail reads as a held smile, not singing.
- No readable text anywhere (monitor rectangles abstract glow, papers illegible). No other people. No morphing.

## Gates
- G1 character consistency: PASS. G2 zero unwanted on-screen text: PASS. G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open through 0.5–6.2s; single singer facing camera).
- G5 audio-sync placement: FAIL — incomplete line (3 of 5 chant occurrences; 3.26s of song chant uncovered).
- G6 banger check: PASS (hook scene, face in the dark, candle + monitor glow).

## VERDICT: REJECT
- Reroll axis (next volley): COMPLETENESS — vehicle v4 names the count explicitly ("chants FIVE times, counting each repeat: 1 'I'm the nobody man', then 'nobody man' 2, 3, 4, 5, brisk and even"). The lyric-as-performed fix landed the elision (take mouths the bare form on chants 2–3) but NOT the count. If the completeness pull also returns 3, the scene retires to a SPLIT restage (S01a first 3 occurrences + S01b last 2), not a third reroll of the same vehicle.
- Raster flag carried: 1152x768 (3:2) — assembly crops to 16:9.
