# Q5 BUILD + GATE NOTES — MV-3 (2026-11-12, recovery coordinator)

Recovery of the Q5 coordinator (3e440d96, INTERRUPTED 2026-11-12 10:45:28 EST
in a daemon restart). Both t2 takes had already fired; this run did QC,
verdicts, the swap-in build, gates, and the chat copy. No further generation
(cap spent). No commit. No delivered flag (parent writes it).

## Verdicts (full record: work/q5/Q5_VERDICTS.md)
- S13 t2 KEEP (md5 4b0307b5d7fbbd3188ddf7b6661289f4) — real articulating mouth,
  open at the head; closes the catalogue's only closed onset (90.66).
- S39 t2 KEEP (md5 8bdab6f48e1f225c32efc3b42d509c8b) — mouth open at all four
  mantra-burst onsets; sung span 5.92s vs t1's 3.14s.
- Disclosed: both takes sing invented words (vehicles carry no lyric quotes)
  — captions carry the song's words; S39 sings one phrase, not four repeats
  (mantra carried by warp); "Pharmacy" background sign (G2 nit); S39 eyes
  close 7.25-8.0s in the tail (trimmed out by the warp).

## Build (q5_build.py, base = corrected_build.corrected_scenes())
- S13: ("mv3_s13_t2.mp4", 1.0, 0.25, 9.25) — 6f head trim puts mouth O on
  song 90.66; single smooth warp; seg 216f / warped 216f / deficit 0.
- S39: ("mv3_s39_t2.mp4", 247/156 = 1.5833, 0.0, 6.5) — single smooth warp
  of the sung phrase across the mantra span; used span ends take 6.5s
  (never the eye-closed beat or the still tail); seg 247f / warped 247f /
  deficit 0. Slowest playback in the Q5 master: 0.63x (inside the 0.5x floor).
- All other scenes, leader, captions (captions_16x9_corrected.ass), bug,
  untouched track.mp3 identical to the corrected build.
- Intermediate: masters/mv3_intermediate_16x9_q5.mp4 (CRF 12, preset fast).
- Master: masters/mv3_i_am_your_dad_16x9_q5.mp4 — md5
  c88da1544f6479df5b485c1b2b699518, 83,181,246 B, 1280x720, 24fps,
  8516 frames, 354.833s.
- Chat copy: masters/mv3_i_am_your_dad_16x9_q5_chat.mp4 — md5
  4e702f61e68e18f4d02921e580db6b75, 26,671,217 B, 854x480, 8516f,
  AAC audio stream copied untouched from the master, faststart.
- Corrected master untouched (md5 5752200b68e1d816e59ca612712fc7d1).

## Gates (on the Q5 master; frames in work/q5/gate/)
- (a) Frame count — PASS: 8516f exact.
- (b) x264 SEI — PASS: crf=18.0 in the embedded options string.
- (c) Audio codec — PASS: AAC, 48000 Hz, stereo, ~192k.
- (d) faststart — PASS: moov at offset 36, before mdat at 246592.
- (e) Master-audio agreement — PASS, MEASURED: decoded-PCM md5
  ff64d85ed44e3b348afa1d5b569a2f1f (identical to the corrected master);
  audio framemd5 stream hash identical to the corrected master.
- (f) Mouth state at the 6 key onsets (t and t+0.17s), eye-read on the master:
  90.66 C -> O / O (L14 onset CLOSED); 98.50 T -> O / O; 344.55 o -> T / O;
  346.35 O -> O / O; 348.29 T -> O / O; 351.55 C -> O / O (S39 final
  mantra CLOSED). All six read O/T. Mouth-scene closed onsets: 1 -> 0.
  The other six C reads in the 99-onset audit (150.30, 183.06, 191.48,
  209.28, 268.16, 331.02) sit in untouched cover/structural scenes, no sync
  claimed there — unchanged from the corrected master.
- (g) Motion (work/gate_motion.py, same method as the corrected gate):
  longest frozen run during words 30f — IDENTICAL to the corrected master
  (30f @208.25 S25, 27f @299.62 S35, both inherited cover-take properties,
  frame-identical positions). The corrected master's third run, 24f @348.29
  (S39), is GONE. No frozen run in S13 or S39. S13 vocal mean diff 1.348
  (corrected 1.233); S39 vocal mean diff 1.009 (corrected 0.63). No scene
  below 0.5 vocal mean diff.
- (h) Regression — PASS: unchanged scenes frame-identical to the corrected
  master (mean |diff| 0.000 at S02 9.32, S29 245.10, S21 150.30, S04 32.16).
- (i) Render check — PASS: "~ WuBu ~" bug top-right; L14 caption
  "You got your real one maybe, or maybe you don't" bottom at 95.0s;
  S13 frame shows the t2 take (doorway, open mouth, hands open).
- Judder: no new warp steps — S13 single factor 1.0, S39 single factor
  1.5833; no in-phrase steps by construction.

## What Q5 closes (program.md Q5)
- S13 L14 onset 90.66: CLOSED -> OPEN. The catalogue now has ZERO closed
  onsets in mouth scenes (99-onset tally: mouth-scene C 1 -> 0).
- S39 final mantra 351.55: CLOSED -> OPEN. The S39 whole-slot-cover
  disclosure ("final mantra has no visible articulation") is closed.
- S39 24f frozen run @348.29 during words: eliminated.
