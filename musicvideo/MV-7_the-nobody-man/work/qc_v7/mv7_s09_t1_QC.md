# MV-7 S09 t1 — QC (v2, recovery volley 2, 2026-11-06 ~16:55 EST)

File: takes/media-generation-mv7v2-s09-chorus-1-c1-8-song-6-0-a3125b5e-d3e6-4343-91e6-e9e877b39a51.mp4
md5: 35717edfb9089a9a1921ceebad8c32ef · 3,083,512 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s09_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp.
snapshot_id: 193e83cd-e962-46c8-b790-64de7ec54f56:xekz45

## Audio / words (faster-whisper small, work/qc_v7/mv7_s09_t1_words.json)
- 4 words, 1 segment: "Nobody man, nobody man" 0.00–7.66s (onsets 0.00 / 4.44; word 2 ends 3.34, word 3 starts 4.44 —
  a 1.10s pause between the two occurrences, roughly mirroring the song's 1.36s inter-occurrence gap).
- Word list matches the vehicle lyric 4/4 (case-insensitive).
- Song side (LYRIC_TIMELINE + SONG_WORDS.json): C1.8 "Nobody Man (x2)" — occurrence 1 at 63.72–64.90, occurrence 2 at
  66.26–66.98. Song word span 63.72–66.98 = 3.26s. Take line span 0.00–7.66s → line ratio 3.26/7.66 = 0.426 — CLEAR MISS (<0.60).
  (On the full slot 63.72–67.80, 4.08s, the ratio is 0.533 — still a clear miss either way.)
  Assembly would need a 2.35x speedup to fit the word span; the v6 generation criterion calls <0.60 a reroll, not a warp.
- Repeat-defect scan: no word/line subsequence recurs after first delivery (the x2 is the prompted lyric). PASS.
- Zero-word result? No — 4 words; split-half recheck not needed. (First-word probs low — "Nobody" 0.482, "man," 0.569 —
  clip-start wobble, confirmed by segment text; the second occurrence decodes at 0.873/0.993.)

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=3.311, min=0.998, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 3.325.
- PASS with wide margin — the strongest motion in this volley (slow push-in + head movement throughout).

## Visual reads (2fps sheet, work/qc_v7/mv7_s09_t1_sheet.png)
- 0.5s: mouth open mid-"Nobody"; identity holds vs Era A still; tall candle right; sparks glowing behind him.
- 5.0s: mouth open mid-second-"nobody"; small orange SPARK bursts visible at frame right (candle/monitor edge) — the sparks motif
  actually shows in this take, the clearest spark read of the volley so far.
- 8.0s: mouth in held grin, eyes closed, push-in tight on the face by the tail.
- No readable text anywhere (monitor rectangles abstract glow, papers illegible). No other people. No morphing.

## Gates
- G1 character consistency: PASS. G2 zero unwanted on-screen text: PASS. G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at 0.5s, 5.0s reads; single singer facing camera).
- G5 audio-sync placement: FAIL — line ratio 0.426 clear miss (4 words delivered over 7.66s vs 3.26s song word span).
- G6 banger check: PASS (chorus hook repeat, sparks visible, push-in escalation).

## VERDICT: REJECT
- Reroll axis (next volley): PACING — vehicle v2 asks the two repeats BRISKLY in a 0.5–4.5s window
  ("chants briskly from 0.5s to 4.5s ... Mouth closes on the last word, grin held wide and certain"), same framing, same Era A still.
  The v2 vehicle asked a 0.5–9.5s window for a 3.26s word span and the model filled it; a short brisk window is the one variable that changes.
- Raster flag carried: 1152x768 (3:2) — assembly crops to 16:9.
