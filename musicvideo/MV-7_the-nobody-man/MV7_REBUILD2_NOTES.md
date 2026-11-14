# MV-7 "I'm The Nobody Man" — REBUILD-2 delivery notes (2026-11-07)

User order 2026-11-07 ~08:17 EST: the otaku rebuild was rejected on lyric
timing. Rebuild-2 re-fired every generation-miss line as single-line takes
with pacing as the named axis, re-analyzed both sides per word, and re-cut
anchored on VISIBLE MOUTH EVENTS (the otaku cut anchored on take audio;
mouths lag audio — that was its core failure). Generation: 26 re-fire
takes, 26/26 lines with the exact words. Assembly: per-line swing (PCHIP)
warps, line heads re-anchored on eye-read mouth events from full-res dense
strips, sub-0.1s song stamp pairs merged to single anchors, phrase-smooth
warps only, no interval slowed past the 0.5x floor.

## Deliverables (verified from the delivered files)
- masters/mv7_im_the_nobody_man_16x9_rebuild2.mp4 — house master.
  md5 36176f04c349ad05e2f456e129392b80 · 79,561,001 B · 4493 frames ·
  187.208s · 1280x720 24fps · x264 SEI crf=18.0 · AAC 48kHz stereo 192k ·
  faststart on.
- masters/mv7_im_the_nobody_man_16x9_rebuild2_50mb.mp4 — chat copy,
  same cut, video capped at 1900 kb/s.
  md5 cc8b98adca40f45ea434d0541fcd1b66 · 48,037,794 B (≤50,000,000) ·
  4493 frames · AAC stream bit-identical to the master (audio stream
  md5 b936ed73be63909db13d301cf5c88b29 in both files — copied, not
  re-encoded) · faststart on.

## Master gate (brief rule 5, strict — no +0.33s allowance)
- Mouth state at EVERY sung line onset (56 lines), read from full-res
  face crops of the composited candidate: **56/56 open or transitional
  at onset or +1 frame.** Five lines pass at +1 only (I1c, I2b, PC1.2,
  C1.3, V2.5); C2.4 is the weakest pass (transitional at onset, opening
  from +1). Gate evidence: work/rebuild2_recut/gate_v2/ (sheets +
  gate_meta.json).
- Frame count exact: 4493. SEI crf=18.0 read from the delivered file.
  Audio probed AAC in the delivered file.
- Motion during words: no identical-frame freeze anywhere. Longest
  near-duplicate run is 43f at the I2c intro-chant tail (global frames
  426–469): the U04 take's natural held tail under the chant's held
  final note — per-frame diffs 0.11–0.56, never 0.00, pose visibly
  drifting; disclosed, not a clamp freeze. (A real 46f clamp freeze at
  the B.6 tail WAS caught by this scan and fixed — see below.)

## STRUCTURAL lines (beat-cut montage from the line's own take + kinetic
words — no sung picture exists at an honest speed; disclosed per brief)
- V1.2 "Got a thousand posts in a folder file" (best take needed 2.12x)
- V1.3 "Old meme face and a busted grin" (1.97x)
- PC2.2 "Little by little, I learned the sound" (2.03x)
- C1.Tb "Nobody Man" tag (take's head-bow covers word 1's mouth)
- FC.1 "I'm The Nobody Man" (2.21x; final-chorus hook stayed grand/slow
  on both pacing pulls)
- FC.2 "Still here, still stand" (2.45x; take delivers it as two
  phrases across a 2.14s gap vs the song's 0.24s)
- Bridge B.1–B.5: montage by design (the bridge takes' audio is not the
  bridge lines); B.6 returns to U31's face for the last bridge line.
- FC.4 final word "man": U33's take truncates it — that word span only
  is covered by beat-cut montage (bad-word rule); the rest of FC.4 is
  the sung take.
- B.6 tail (141.62–143.40s): the take's performance ends at the line's
  last anchored word; the first candidate's warp tail clamped to a
  frozen frame there (46f). Fixed with beat-cut montage from U31's own
  take. Song-side stamps in that span are ambiguous (the lyric sheet
  shows an instrumental gap; ASR hears a pickup phrase) — montage is
  legitimate under both readings.

## Conditional attempts that PASSED the master gate (stayed sung)
- V1.1 (R05A): 1.89x speedup, edge zone — line head re-anchored on the
  visible mouth opening; onset now parted, wide at +1.
- C1.Ta (R16A): 1.74x speedup with per-word re-anchor ("man" anchored
  on its opening, +6f after its audio onset). First candidate landed
  the opening 2–3 frames late; word-1 anchor moved to the eye-read
  parting (take f15) and the re-gate passes at onset.
- FC.7 (R35): 1.88x speedup, edge zone — head re-anchored; onset
  parted, wide at +1.
- FC.6 (R34B): 1.95x stretch (inside the 2x slow cap). First candidate
  sat on the /f/ closure at the RMS onset; word-1 anchor moved to the
  visible opening (take f27) and the re-gate passes at onset.

## Warp rescues (overall take→song span factors; phrase-level swing
around these, heads re-anchored on visible mouth events)
Speedups: V1.4 1.64x · PC1.1 1.75x · PC1.2 1.68x · C1.7 1.27x ·
V2.2 1.54x · V2.5 1.34x · V2.6 1.41x · PC2.1 1.30x · FC.8 1.44x.
Stretches (all inside the 0.5x slow floor): I1c/I1d intro-chant reps
1.38x / 1.56x · FC.5 1.30x (0.77x speed) · FC.9 1.29x (0.775x speed).
KEEP lines play at natural pace with mouth-event anchors only.

## Other notes
- Kinetic HIGHLIGHT layer rebuilt from measured song timings (sheet
  lyric text; chant word times synthesized from take-slice proportions
  because the song's ASR chant stamps are garbled) — composited in
  post, no generated in-clip text.
- Trims: R17A's laughing tail cut (line only, 0.0–2.36s); R17B's late
  closed-mouth head cut (line onset 2.32s in the take); R34A/R34B heads
  trimmed at their RMS onsets.
- The song (track.mp3) is the sole master audio, timing untouched,
  muxed as AAC. No generated audio is used as soundtrack.
- Segment map: work/rebuild2_recut/seg_manifest.json (68 segments:
  39 KEEP / 13 RESCUE / 4 COND / 11 MONTAGE / 1 OUTRO).
