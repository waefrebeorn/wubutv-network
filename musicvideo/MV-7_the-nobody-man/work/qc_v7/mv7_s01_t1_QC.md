# MV-7 S01 t1 — QC (v2, recovery run 4, 2026-11-06 ~16:35 EST)

File: takes/media-generation-mv7-s01-t1-0-5ed0bfcf-e950-4418-9a9e-fb26c6f43008.mp4
md5: 3f29a5e8670a91865af44059e14eb68f · 2,444,560 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s01_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp.
snapshot_id: 273c143c-c06f-4efd-954d-0812036e7dfc:5jd82c

## Audio / words (faster-whisper small, work/qc_v7/mv7_s01_t1_words.json)
- 12 words, 1 segment: "I'm the nobody man" x3, 0.00–7.20s (onsets 0.00 / 2.50 / 4.62).
- Vehicle asked the full phrase x5 (20 words). Take delivers 3 of 5, then SILENT 7.20–10.00s.
- Repeat-defect scan: no repeats. Zero-word? No — split-half not needed.

## Song side (adjudicated — see below)
- SONG_WORDS.json full pass + split-half recheck (work/qc_v7/song_intro_a.json, small model) AGREE:
  S01 window (0–9.92s) performed words = "I'm the nobody man" x1, then "Nobody man" x4 (onsets ~0.0 / 4.70 / 5.78 / 7.50 / 8.04),
  last word ends 9.46s. The performed chant ELIDES "I'm the" after the first phrase; the v2 vehicle used the sheet lyric (full phrase x5).
  (Base-model full-intro pass blanked 0 words — split-half rule applied; small-model halves agree with the full pass.)
- Take line span 0.00–7.20s vs song word span 0.00–9.46s → line ratio 9.46/7.20 = 1.314 (GREY 1.25–1.60).
- Coverage gap: song keeps chanting 7.20–9.46s (2 "Nobody man" occurrences) with NO singing picture from this take.
- Word-identity mismatch: take mouths "I'm the" before "nobody man" on chants 2–3 where the song sings bare "nobody man".

## Frame rule (native 24fps, vocal 0.5–9.5s)
- frames=240, mean_diff=1.315, min=0.596, longest near-dup run = 0 frames. PASS.

## Visual reads (2fps sheet)
- 5.0s: mouth open mid-chant, identity holds vs Era A, tall candle right edge, monitor glow abstract. G1 PASS, G2 PASS (no readable text), G3 PASS.

## VERDICT: REJECT
- G5 FAIL: incomplete line (3 of ~5 chant occurrences; 2.26s of song chant uncovered) + word-identity mismatch on the elided syllables.
- Reroll axis (next volley): LYRIC-AS-PERFORMED — vehicle v3 asks the elided chant verbatim:
  "I'm the nobody man, nobody man, nobody man, nobody man, nobody man" spanning 0.5–9.5s.
- Raster flag carried: 1152x768 (3:2) — assembly crops to 16:9.
