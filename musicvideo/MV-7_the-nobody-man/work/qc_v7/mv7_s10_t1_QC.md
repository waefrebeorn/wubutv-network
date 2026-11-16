# MV-7 S10 t1 — QC (v2, recovery volley 2, 2026-11-06 ~16:55 EST)

File: takes/media-generation-mv7v2-s10-chorus-1-tag-chant-c-0-64689c53-7219-49f8-b5d2-f0839acce3b3.mp4
md5: 642211b3966a3887f4d1ea820a92d62b · 2,576,552 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s10_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp.
snapshot_id: 3674e75c-45ab-4e21-b307-d6e4a22ee7fd:t5h9qb

## Audio / words (faster-whisper small, work/qc_v7/mv7_s10_t1_words.json)
- 6 words, 1 segment: "Nobody man, nobody man, nobody man" 0.00–7.08s (onsets 0.00 / 2.74 / 5.18).
- CORRECTION TO THE PLAN: the vehicle asked the tag chant x4, but the MEASURED song (SONG_WORDS.json) chants it x3 in the
  C1.T window 67.80–75.84s: "Nobody man" 67.80 / 68.16–68.86 / 71.90–72.34. LYRIC_TIMELINE's "x~4 [inferred]" was wrong.
  The take delivers exactly the measured x3, in order, once — word list matches the performed lyric 6/6.
- Take line span 0.00–7.08s vs song word span 67.80–72.34 = 4.54s → line ratio 4.54/7.08 = 0.641 — GREY (0.60–0.80).
  Warp-rescue at assembly: phrase-smooth speedup ~1.56x to land the words (speedups uncapped per the user warp law; disclose the extreme).
- RHYTHM CAVEAT for assembly: the song's measured C1.T word times are uneven — occurrences at 67.80, 68.16–68.86, then a long
  pause to 71.90–72.34 — while the take's occurrences are evenly spaced (~2.6s apart). A uniform 1.56x warp lands occurrence 1
  and 3 but puts occurrence 2 ~1.4s late; per-word warping fixes placement but needs up to ~4x squeeze on occurrence 3.
  The SONG_WORDS timings for this window carry duplicate-timestamp artifacts (71.92 listed twice), so assembly should RE-MEASURE
  the C1.T word times (split-half + mouth reads) before locking the warp — do not trust either side blindly here.
- Repeat-defect scan: no word/line subsequence recurs after first delivery (the x3 is the prompted lyric). PASS.
- Zero-word result? No — 6 words; split-half recheck not needed. (First-word "Nobody" prob 0.497 — clip-start wobble, confirmed by segment text.)

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.556, min=0.518, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.550.
- PASS with margin (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s10_t1_sheet.png)
- 0.5s: mouth open mid-"Nobody"; identity holds vs Era A still; tall candle right, monitor glow abstract.
- 5.0s: mouth OPEN mid-third-"nobody" (5.18–5.96); push-in tighter than the still.
- 8.0s: mouth in held grin, eyes closed — words ended 7.08s; the tail is a held pose.
- Sparks dimming to embers behind him per the vehicle (glow reads dimmer than S08/S09, motif beat carried).
- No readable text anywhere (monitor rectangles abstract glow, papers illegible). No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds across all sampled frames).
- G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at 0.5s, 5.0s reads; single singer facing camera).
- G5 audio-sync placement: PASS with flag (ratio 0.641 grey; all 6 words in order, once — see rhythm caveat above).
- G6 banger check: PASS (tag chant close, push-in escalation, sparks dimming to embers).

## Flags (not fails)
1. RASTER 1152x768 (3:2), not 1280x720 16:9 — the Era A still is 1920x1280 (3:2) and aspect followed the image despite "16:9 landscape" in the vehicle text. Assembly crops to 16:9 (1152x648 → upscale). Same class as MV-6 S16.
2. Take sings 0.00–7.08 vs vehicle window 0.5–9.5s (starts 0.5s early; last word ends 2.42s before window end). Assembly trims/warps; ratio grey.
3. RED LIGHT WASH on the face in the last ~2s (post-vocal, rows 4 of the sheet) — unprompted lighting drift. Words end 7.08s, so the wash sits outside the vocal window and trims cleanly; flag for the record, not a fail.
4. Eyes closed through much of the chant — expressive singing, not a fail.

## VERDICT: KEEP-WITH-FLAG
