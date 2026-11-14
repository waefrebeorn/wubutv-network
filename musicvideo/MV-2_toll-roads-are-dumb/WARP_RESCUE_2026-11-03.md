# Warp-rescue pass — MV-2 "Toll Roads Are Dumb" — 2026-11-03

No new generation. No take was fired, no source file, master, or record was
modified, and nothing was committed. Sixteen held greys were warped whole-clip
(video + audio by the same factor) and re-QC'd exactly the way volley QC did:
faster-whisper base (av-bypass: ffmpeg to wav, then ndarray), raw word list
with beat-word subsequence repeat scan, split-half recheck if a full-clip
result is zero words, vocal-window frame gate, and visual frame reads.
Machine-readable record: `WARP_RESCUE_V6.json`. QC scripts (new files):
`qc_warp_rescue.py`, `qc_warp_rescue_s23norm.py`,
`qc_warp_rescue_batch2.py`, `vocal_window_warp_rescue.py`,
`VOCAL_WINDOW_WARP_RESCUE.json`, `VOCAL_WINDOW_WARP_RESCUE_EXTRA.json`,
`VOCAL_WINDOW_WARP_RESCUE_B2.json`, `TAKE_WORDS_WARP_RESCUE.json`,
`TAKE_WORDS_WARP_RESCUE_S23NORM.json`, `TAKE_WORDS_WARP_RESCUE_B2.json`,
frames in `qc_frames_warp/` and `qc_frames_warp_b2/`.

## Method (adjudicated 2026-11-03 evening)

- Ratio = song span / take vocal span. Band 0.80–1.25. Grey zone
  0.60–0.80 / 1.25–1.60. Clear misses were NOT warped, except S16 t8 at
  unrounded 0.5992, which the volley-13 report treats as a held grey
  boundary case (disclosed wherever it appears).
- Warp TO THE BAND EDGE, not to 1.0: ratio < 0.80 → factor = 0.80 / ratio
  (speed up); ratio > 1.25 → factor = 1.25 / ratio (slow down). Cap 1.5×
  either way. All 16 factors landed inside the cap (max 1.3351, S16 t8).
- ffmpeg: `setpts=PTS/factor` + `atempo=factor`, libx264 crf 18,
  1280×720, 24fps, AAC 192k 48kHz stereo. Assembly later uses video only
  over untouched `track.mp3`; QC here is on the warped clip as a whole so
  Whisper timestamps match the warped mouth.
- Ratio verdicts use the volley method: ratio rounded to 2dp, as every
  volley QC script computed it (S16 t4 at 3.02/3.78 = 0.7989 was accepted
  as a borderline candidate on that basis). Unrounded ratios are reported
  alongside for every take. The frame gate is strict and unrounded: FAIL
  if vocal near-dup run ≥ 24 frames OR vocal mean diff < 0.5 — no rounding
  into a pass (R3 t9 discipline). Every frame gate in this pass cleared
  comfortably (lowest mean 0.6330, S14; highest near-dup run 10, S17).
- A measurement is rejected only with independent proof, never on a hunch.
  Three such rejections are marked `*` below; each needs parent
  confirmation (see "Needs a parent decision").

## Headline counts

- Warped: 16 (Batch 1: 9 v6 greys; Batch 2: 7 v5-era greys).
- Candidates: 14 — 11 clean, 3 starred (`*`, measurement rejections).
- Fails: 2 — S23 t6 (character), S09 (ratio).
- Nothing was declined for exceeding the 1.5× cap; no warped filename
  collided with an existing file.

## Batch 1 — v6 greys: all 6 slots covered

| Slot | Warped take | Factor | Measured ratio (unrounded → 2dp) | Frame gate | Verdict |
|---|---|---|---|---|---|
| S16 | t7 warped | 1.0596 | 0.803191 → 0.80 | PASS (90/91, run 1, mean 1.0555) | CANDIDATE |
| S16 | t8 warped | 1.3351 | 0.798942 → 0.80 | PASS (90/91, run 1, mean 1.9012) | CANDIDATE (borderline) |
| S22 | t4 warped | 0.9659 | 0.940171 → 0.94 | PASS (33/59, run 2, mean 1.4607) | CANDIDATE |
| R4 | t2 warped | 1.0909 | 0.960317 → 0.96 | PASS (60/61, run 1, mean 1.0917) | CANDIDATE |
| R3 | t4 warped | 1.2074 | 0.800000 → 0.80 | PASS (60/66, run 1, mean 1.6559) | CANDIDATE |
| R6 | t4 warped | 1.2697 | 0.539604 measured, 0.80 scaled | PASS on scaled span (62/68, run 1, mean 2.2237) | CANDIDATE* |
| S23 | t4 warped | 1.2600 | 0.824742 → 0.82 | PASS (28/47, run 1, mean 0.9387) | CANDIDATE |
| S23 | t5 warped | 1.2700 | 0.833333 → 0.83 | PASS (47/47, run 0, mean 1.2616) | CANDIDATE |
| S23 | t6 warped | 1.2900 | 0.800000 → 0.80 | PASS (30/49, run 1, mean 0.9387) | FAIL (character) |

- **S16 covered** (t7 clean; t8 borderline as well — its unrounded 0.798942
  is the same figure as the accepted S16 t4 precedent; pocket square blue
  nit on both). Original t8 ratio 0.5992 disclosed; its per-word timestamps
  were lost with the volley-13 QC agent's /tmp files and were not
  reconstructed — only the 5.04s span length is on record.
- **S22 covered.** TOWROADS slur disclosed (Whisper hears toll+roads as one
  token, volley-12 precedent). First-word onset snapped early (measured
  2.88 vs scaled 3.27), but both measured (0.94) and scaled (1.25) ratios
  are in band, so the verdict does not depend on the snap.
- **R4 covered.** Final-word truncation disclosed: Whisper ends "done" at
  2.52 vs scaled 3.025 (first three boundaries match scaled within 0.03s).
  Both measured (0.96) and scaled (0.80) in band.
- **R3 covered.** Measured span identical to scaled span; ratio exactly
  0.80.
- **R6 covered\*.** Whisper's measured ratio 0.5396 is rejected as a
  first-word onset artifact: the original re-transcribes exactly at
  1.72–5.18; all later warped boundaries match scaled within 0.26s; and
  visually the mouth is CLOSED at warped 0.7s and 1.0s (pre-vocal) and
  OPEN at 2.0s and 3.8s. Scaled ratio 0.80. See "Needs a parent decision".
- **S23 covered** (t4 + t5). Both needed the done→dumb normalization:
  warped audio hears "done" for "dumb", while the same performances
  unwarped were heard as "dumb" (t4 exact, t5 "told roads are dumb"), and
  done→dumb is an established v5 mishear class. Raw words are preserved
  in `TAKE_WORDS_WARP_RESCUE_S23NORM.json`. If the parent rejects this
  normalization, S23 coverage collapses (t6 is character-failed) — flagged
  below. t5 pocket square orange-red nit.
- **S23 t6 FAIL (character):** passes ratio, frame gate, exactly-once, and
  text, but the face is visibly not THE VOICE (darker skin, different
  structure, gold chain), confirming the original drift flag. Precedent:
  R1 t2. This does not block the slot (t4/t5 cover it).
- All Batch 1 takes sang their beat line exactly once (repeat scans
  empty) and were text-clean in the frames read (blank tickets, fog/open
  road only, no signage words).

## Batch 2 — v5-era greys: 6 of 7 slots covered

Song spans recomputed from `SONG_WORDS_BASE.json` (first-word onset to
last-word end at the v5 `song_span` indices) and re-measured figures are
reported next to the v5 figures; they agree in every case.

| Slot | Warped take | Factor | V5 ratio → measured ratio (unrounded → 2dp) | Frame gate | Verdict |
|---|---|---|---|---|---|
| S09 | t2 warped | 1.0843 | 0.7378 → 0.794258 → 0.79 | PASS (54/101, run 1, mean 1.6289) | FAIL (ratio) |
| S20 | t2 warped | 1.1236 | 0.7120 → 0.747899 measured, 0.800003 scaled | PASS on scaled span (44/56, run 1, mean 1.5794) | CANDIDATE* |
| S17 | t2 warped | 1.3085 | 0.6114 → 0.800000 → 0.80 | PASS (100/169, run 10, mean 1.4775) | CANDIDATE |
| S14 | t2 warped | 0.9713 | 1.2869 → 1.251938 → 1.25 | PASS (56/125, run 9, mean 0.6330) | CANDIDATE (borderline) |
| S19 | t2 warped | 0.9667 | 1.2930 → 1.225926 → 1.23 | PASS (63/130, run 2, mean 1.0445) | CANDIDATE |
| S15 | t2 warped | 0.9255 | 1.3506 → 1.350649 measured, 1.250026 scaled | PASS on scaled span (75/81, run 1, mean 2.6710) | CANDIDATE* |
| S18 | t1 warped | 0.8712 | 1.4348 → 1.247423 → 1.25 | PASS (62/143, run 2, mean 2.3816) | CANDIDATE |

- **S09 remains uncovered.** Measured 0.794258 rounds to 0.79 — below band.
  Scaled ratio is 0.799972; the miss is a 0.03s span difference, within
  Whisper boundary jitter (its own word boundaries match scaled within
  0.07s). Not overruled by this pass; a parent overrule would cover S09.
  No v6 coverage is lost (S09 is a v5-era line only).
- **S20 covered\*.** Same onset-snap class as R6, smaller magnitude:
  Whisper onset 4.28, but the mouth is CLOSED at warped 4.0s and 4.3s and
  OPEN at 4.6s — onset is ~4.41, the scaled onset. Later boundaries match
  scaled within 0.04s. Scaled ratio 0.80. See "Needs a parent decision".
- **S17 covered.** The original v5 class was "meaner garbled" ("me in
  her"); on warped audio Whisper hears "meaner" cleanly with NO
  normalization applied — all 10 beat words matched in order. The warp
  itself resolved the garble perception. The 2.76–4.64 gap between "time"
  and "one" is the original mid-line pause, preserved by the warp.
- **S14 covered (borderline).** Measured 1.251938 rounds to 1.25 (miss
  +0.0019, span diff 0.008s — under one video frame). Background sign
  panels are blank; signal pictograms/arrows only, no legible words.
- **S19 covered.** Measured 1.2259, scaled 1.2499, both in band.
- **S15 covered\*.** Whisper truncates the final word ("coming" end 3.08
  vs scaled 3.328; first three boundaries match scaled within 0.02s — the
  same signature as R4 t2's truncation). Visual: mouth OPEN at warped
  3.2s and 3.4s, past the measured end, where the original note says the
  post-vocal hold is closed. Scaled ratio 1.25. See "Needs a parent
  decision".
- **S18 covered.** Measured 1.2474 is in band unrounded, not just on
  rounding. All 13 beat words matched; "timing's" from take word
  "timings" per the v5 record (the down→dumb v5 class was available but
  not needed — Whisper heard "dumb").
- All Batch 2 takes sang exactly once (repeat scans empty) and were
  text-clean in the frames read. S20/S14/S15/S17/S19 pocket squares run
  orange-red (nit class); S09 wears a bow tie in its own take (not a
  gate).

## What this does and does not finish

- v6 slot coverage after this pass: the 9 clean v6 candidates stand, plus
  S16, S22, R4, R3, R6\*, S23 from this pass. The R4/R3/R6 "done" slots no
  longer need fresh staging from scratch — unless the parent rejects the
  R6\* measurement call, in which case R6 reverts to needing one.
- Still blocked after this pass: the S13/S05 hook (no grey was ever held;
  the adjudicated path is split-across-shots + cutaways, not warp), S09
  (parent overrule or a fresh take), and the v5 in-band takes
  (S01/S02/S03/S04/S07/S11/S12/S21/S24/S25/S26) still pending v6
  vocal-window re-verification at assembly. This pass is warp + QC only:
  **no assembly and no delivery is claimed.**
- Assembly notes for the parent: warped durations are NOT 10s (range
  7.58–11.50s). Five warped takes exceed 10s (S22 10.366, S14 10.316,
  S19 10.361, S15 10.819, S18 11.496) — assembly must trim to the vocal
  segment, never drop a whole warped clip in. Warped video is the rescue
  asset; the soundtrack remains untouched `track.mp3`.

## Needs a parent decision

1. **Confirm the three measurement rejections** (R6 t4 onset snap,
   S20 t2 onset snap, S15 t2 final-word truncation). Each is evidenced
   above (visual mouth state + boundary matching + deterministic warp
   math), but each replaces a Whisper measurement with a scaled figure.
   If any is rejected, that slot reverts to FAIL: R6 uncovered, S20
   uncovered, S15 uncovered.
2. **S23 done→dumb normalization.** Established v5 class + unwarped
   evidence, but it is the only thing standing between S23 and uncovered:
   if rejected, warped t4/t5 fail and t6 is already character-failed.
3. **S09 overrule (optional).** Measured 0.794258 vs band 0.80; scaled
   0.799972; span diff 0.03s. Overruling covers S09; leaving it failed
   costs nothing in v6 (v5-era line only).
4. **Borderline rounding calls (for the record, no action needed unless
   the parent tightens the rule):** S16 t8 (0.798942 → 0.80, same figure
   as the accepted S16 t4 precedent) and S14 (1.251938 → 1.25). Tightening
   to strict unrounded would un-cover S16 t8 (slot still covered by t7)
   and S14 (v5-era only).

## Parent adjudication (2026-11-03 ~20:1x EST, verified from disk)

Parent verified all 16 warped files on disk (md5 + ffprobe: every file
1280x720/24fps, durations 7.58–11.50s as reported) and spot-checked the
QC jsons (WARP_RESCUE_V6.json rows, TAKE_WORDS_WARP_RESCUE*.json,
frame-gate spans) before accepting the verdicts. Decisions:

1. **All three starred measurement rejections CONFIRMED.** The decisive
   check is that each frame-gate vocal window matches the scaled span,
   not the Whisper span: R6 t4 frame span 1.3546–4.0796 = scaled
   1.72/1.2697–5.18/1.2697 to 0.001s; S20 t2 frame span starts 4.4144,
   the scaled onset the agent evidenced with closed-mouth frames at
   4.0/4.3s; S15 t2 frame span ends 3.3279, the scaled end, with mouth
   open at 3.2/3.4s past Whisper's 3.08 truncation. R6, S20, S15 covered.
2. **S23 done→dumb normalization CONFIRMED.** Established v5 mishear
   class, and the same performances unwarped were heard as "dumb".
   S23 covered via t4 + t5 (t6 stays character-failed, non-blocking).
3. **S09 OVERRULED to covered.** Measured 0.794258 vs scaled 0.799972:
   the warp factor was computed to land exactly 0.80 (0.80/0.7378), and
   the 0.03s span difference is Whisper boundary jitter (boundaries
   match scaled within 0.07s). Same scaled-figure principle as (1).
   S09 covered.
4. **Borderlines stand on the volley 2dp convention:** S16 t8 at
   0.798942 (same figure as accepted S16 t4) and S14 at 1.251938 → 1.25.
   Neither decision is load-bearing: S16 is covered by t7, S14 is
   v5-era only.

**Final tally: 15 of 16 warped takes are candidates; the only fail is
S23 t6 (character), which does not block its slot. All 6 v6 grey slots
(S16, S22, R4, R3, R6, S23) and all 7 v5-era grey slots (S09, S20, S17,
S14, S19, S15, S18) are covered.** Still open after this pass: the
S05/S13 hook (split-across-shots + cutaways path, not warp) and
v6 vocal-window re-verification of the v5 in-band takes at assembly.
Warped mp4s are git-ignored (media leg) and were already uploaded to
HF by the 20:05 EST CDN run; this commit covers text records only.
