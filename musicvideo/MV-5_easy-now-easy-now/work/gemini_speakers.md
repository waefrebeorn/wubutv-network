# MV-5 Gemini speaker anchoring — work/gemini_speakers.md

Date: 2026-11-05 ~13:55 EST. Stage A of the MV-5 v2 + MV-3 timing-fix program.
Question: map Gemini 3.5 Transcribe's speaker labels (spk_0/1/2, from
work/gemini_song.json — 82 segments, 496 words, segment times only) to
CAT (low voice ~97–160 Hz) / GIRL (high voice ~200–330 Hz), using measured
fundamental frequency. In particular: is spk_2 — which appears ONLY in the
122–139s refrain + 196s — a real third voice or a diarization split?

## Method (and its traps)

- Evidence: librosa pyin track (work/pyin_f0.npy + work/pyin_vp.npy, fmin 65,
  fmax 500, hop 512 @16k) and aubio YIN track (work/f0_track.npy +
  work/f0_conf.npy), both computed on work/tmp_audio.f32 during v1 stage 1.
- Validity check (this run): tmp_audio.f32 and work/gemini/song_16k.wav carry
  the SAME signal at lag 0 (correlation 0.9999999978, identical length
  3,302,400 samples). Only a sqrt(2) gain difference (mono-sum vs mono-mean).
  f0 estimation is gain-invariant, so both tracks apply to the Gemini wav
  as-is. No recompute needed.
- Script: work/gemini_f0_segments.py. Outputs: work/gemini_f0_segments.json
  (per-Gemini-segment pyin+aubio stats) and work/gemini_line_f0.json
  (per-SONG_WORDS-line pyin+aubio stats — precise 2-decimal windows).
- TRAP 1 — the saved pyin voiced-probability array is degenerate (mean
  0.019; only 24/6451 frames > 0.5). Selecting voiced frames on vp > 0.5
  keeps a tiny biased subset — it once returned 263 Hz for a 145–160 Hz CAT
  line because only the next line's onset passed. Voiced = librosa's own
  decision (non-NaN f0, 2210/6451 frames). The vp array must never be used
  as a voiced gate on this track.
- TRAP 2 — bass lock. The mix has a bass at ~65 Hz and pyin locks onto it
  in dense/fast passages (v1 doc warned of this). Pooled pyin bass fraction
  (<80 Hz): spk_0 0.528, spk_1 0.825, spk_2 0.870. Segment MEDIANS are
  therefore bass-dominated and must NOT be read as voice pitch (median of
  medians: spk_0 68.5, spk_1 66.5, spk_2 65.6 Hz — all bass). What carries
  weight is per-line/per-word histograms: band fractions, 10 Hz modes, and
  the aubio cross-check — the v1 method, reproduced here (spot-check: this
  run reproduces v1's confirmed numbers exactly — L16 131.5, L79 155.5,
  L56 311.0, L57 311.0, I09 316.4, L80 261.5 Hz).
- TRAP 3 — zero-length Gemini segments (122–122, 127–127, 134–134, 136–136)
  were widened to 1s windows for f0 measurement. Their true span is unknown
  within ±0.5s, so they bleed into neighbouring lines (see L62/L77 in the
  diff doc). Treat any verdict resting on a widened segment as weak.
- TRAP 4 — Gemini segment labels are TURN-level, not line-level. Long
  segments swallow lines of the other voice: the 37s spk_0 segment 8–45
  contains the GIRL vocalise I09 (pyin 316.4, 34/34 girl-band frames); the
  22s spk_0 segment 75–97 contains the GIRL island L38–L41. A segment
  label can never adjudicate a line inside a longer segment on its own.

## Mapping

| Gemini label | Segments | Maps to | Confidence |
|---|---|---|---|
| spk_0 | 40 | CAT (low voice) | HIGH |
| spk_1 | 33 | GIRL (high voice) | HIGH |
| spk_2 | 9 | GIRL — diarization split of the same voice as spk_1 | MODERATE-HIGH |

### spk_0 = CAT — anchors (long segments, >=3s)
- 8–45 (37s, Verse 1 + intro tail): pyin med 94.1, cat frac 0.366,
  aubio 131.1. CAT-leaning. (Contains the GIRL vocalise I09 as a swallowed
  island — see Trap 4.)
- 75–97 (22s, C1 tail + Verse 2 start): pyin med 90.9, cat 0.346,
  girl 0.0, aubio 138.4. CAT-leaning. (Contains the GIRL island L38–L41
  as a swallowed island.)
- 99–103 "Forgot what I was told" (L44, CAT): pyin med 98.2, cat 0.618,
  girl 0.0. Clean CAT.
- 139–151 (12s, C2 tail + bridge start): bass-locked (pyin med 65.8,
  bass 0.656, aubio 70.1). Weak but not contradictory.

### spk_1 = GIRL — anchors
- 116–120 "And my whole head replaced" (L56, GIRL [confirmed]): pyin med
  311.0, p25 309.2, p75 314.6, girl frac 1.0 (25/25 frames), aubio 260.9.
  The single cleanest anchor in the whole run.
- Refrain alternation: in Choruses 1, 3 and 4 Gemini alternates
  spk_1 ("Easy now") / spk_0 (response) exactly as v1's GIRL/CAT
  alternation. The structure matches line-for-line.

### spk_2 = GIRL (diarization split, NOT a third voice)
- Positive evidence: L57, the first Chorus 2 refrain (121.26–122.58),
  measures pyin med 311.0, p25 261.5, girl frac 1.0 (13/13 frames),
  modes 310 Hz (8f) + 260 Hz (4f), aubio 261.6 — unambiguous GIRL-band
  singing — and Gemini labels the overlapping segment spk_2. The spk_2
  segment 122–122 itself measures 311.9 Hz (2 voiced frames, both
  girl-band). The voice under the spk_2 label at its first occurrence IS
  the girl's voice at 261–312 Hz.
- Structural evidence: in Chorus 2 Gemini alternates spk_2 ("Easy now") /
  spk_0 (response) in the EXACT same pattern as spk_1/spk_0 in Choruses
  1/3/4. Only the refrain label changes, at a section boundary — the
  classic place for a diarizer to split one speaker.
- Absence of a third voice: no spk_2 segment measures in any third band.
  The other 8 spk_2 segments are bass-locked (medians 65–70 Hz) — and so
  are spk_1's refrain segments in C1/FC (medians 65–78 Hz, girl frac
  0.0). spk_1 and spk_2 behave identically under f0 measurement: same
  text, same windows, same bass-lock. A distinct third voice with a
  different pitch would show SOME segment in a distinct band. None does.
- Caveat: only L57 of the 9 spk_2 segments has direct voice-band f0; the
  other 8 are bass-locked and uninformative at this granularity. Per-word
  f0 from the app run (Stage D) can confirm each C2 refrain individually.
  Until then the mapping is moderate-high confidence, not certain — but it
  is the best-supported reading, and no evidence points the other way.

## Undecided items (f0 cannot settle these; Stage D take audit decides)
- L54 "Let the hard week fade" (PC2): aubio 298.5 Hz on a CAT line — real
  girl voice (a repeat flipped like L56?) or an octave error (2x ~149 Hz)?
  pyin has 0 voiced frames in the window. S14 is structural cover, so no
  mouth-sung picture rides on it.
- L12 "Yeah, they already understand": Gemini labels spk_1 (GIRL) over
  82% of the line; pyin has 0 voiced frames; aubio line-level 153.1 Hz
  (CAT) vs aubio segment-level 259.5 Hz (window-dependent). Leans v1/CAT
  on the line window; the take audit (S06) decides.
- Bridge alternation (L82/L84/L86/L88 labelled spk_1, v1 all-CAT): both
  estimators are bass-locked through the whole bridge and cannot
  adjudicate. The complete absence of girl-band f0 in those lines — where
  L56/L57/L80 show it cleanly in equally short windows — argues the
  spk_1 labels there are diarizer chopping, not a real voice change.
  Leans v1; the take audit (S21 t3) decides.
- Tail (L106–L110, 186.46–205.58): Gemini's tail is unstable on words,
  timing and speaker (see gemini_diff.md). f0 is bass-locked throughout
  the closing block. Nothing here is decidable from f0.

## What this does NOT do
- Line-level pyin in this run reuses the SAME pyin track v1 used, so where
  it agrees with v1 it corroborates the method, not the owner —
  independent evidence is Gemini's labels + the aubio cross-check.
- No per-word times exist yet (Playground gives segment times only). Word
  times must come from the app (Interactions API) — Stage D, currently
  blocked on the endpoint failure (see parent's Stage D note).
