# MV-3 timing diagnostic — take mouth vs song word timing (measurement only)

Date: 2026-11-04. No video generated, no masters edited. Method: each take's
audio extracted to wav (ffmpeg, mono 16k), transcribed sequentially with
faster-whisper base (~/workspace/fw-venv), word_timestamps=True. Song
re-transcribed the same way from track.mp3 for word-level anchors
(LYRIC_TIMELINE.md line spans cross-checked; "game"/"dead" = Whisper's
dad mishear, known class). Placed time = scene start + take-internal time ×
assembly warp (assemble_mv3.py uses setpts=w*PTS, so output = input × w).
Offset = placed take word time − song word time. First-word take times of
0.00 are segment-start stamps (onset ≈ clip start).

## Headline

Every take starts singing on time (first word offset ≈ 0.00 in all 7
samples) and then drifts: the generator sings each line at its own tempo,
not the song's. Fast takes finish up to 1.8s early; slow takes lag up to
~1.7s and get their tails cut by the slot boundary. This is a pacing
difference, not a steady shift — except S10, which is nearly steady. S39
is a coverage gap, not a shift: the take sings the mantra once, then is
silent while the song repeats it 3+ more times.

## Per-take numbers

| Scene / take | Prompted line (song slot) | Take internal first→last | Song first→last | Placed first (off) | Placed last (off) | Verdict |
|---|---|---|---|---|---|---|
| S01 s01_t2, slot 2.82–9.32, warp 1.088 | "Listen, all of you" (L01) | 0.00 → 4.54 | 2.82 → 9.12 | 2.82 (+0.00) | 7.76 (−1.36) | PACING: take ~22% fast; mouth stops 1.4s before song's "you" ends |
| S02 s02_t2, slot 9.32–18.34, warp 1.040 | "You already know, I am your dad" (L02) | 0.00 → 6.94 | 9.32 → 18.34 | 9.32 (+0.00) | 16.54 (−1.80) | PACING: take ~20% fast; mouth done 1.8s early |
| S07 s07_t1, slot 48.12–55.14, warp 0.975 | "I raised you in the dark, I raised you in the light, I raised every face that is listening tonight" (L07+L08) | 0.00 → 8.96 | 48.12 → 55.14 | 48.12 (+0.00) | 56.86 (+1.72, past slot end) | PACING + CUT: lag grows word by word (dark +0.3, light +0.8, face +1.4); slot cuts at internal 7.20s, so "listening tonight" never appears on screen |
| S10 s10_t1, slot 68.36–76.28, warp 1.0 | "I am your dad, you're hearing once, you're hearing twice, now it lives inside" (L11) | 0.00 → 7.70 | 68.36 → 75.48 | 68.36 (+0.00) | 76.06 (+0.58) | NEARLY STEADY: ~+0.5s lag throughout, fits slot |
| S19 s19_t1, slot 136.52–143.76, warp 1.0 | "I am your dad, I am your dad, I am your dad, say it with me" (L21, chorus-2 repeat) | 0.00 → 8.12 | 136.52 → 143.76 | 136.52 (+0.00) | 144.64 (+0.88, past slot end) | PACING + CUT: lag grows (dad#1 ~0.0, dad#3 +0.5, "say" +0.7); slot cuts at internal 7.24s, so "it with me" never appears |
| S29 s29_t1, slot 245.10–251.04, warp 0.8375 | "I am your dad" x2 + "say it with me" (L32, extended chorus) | 0.00 → 8.34 | 245.10 → 251.04 | 245.10 (+0.00) | 252.08 (+1.04, past slot end) | PACING + CUT: second repeat drags (dad#1 +0.3, dad#2 +1.3); slot cuts at internal 7.09s, so "say it with me" never appears |
| S39 s39_t1, slot 344.55–354.84, warp 1.0 | "I am your dad" mantra, fade (L40) | 0.00 → 3.14 (ONE repeat only) | 344.55 → 353.72 (mantra) | 344.55 (+0.00) | 347.69 (last sung word) | COVERAGE GAP: take sings "I am your dad" once, then no detected vocal for the remaining ~6s while the song repeats at ~347.7, ~350.0, ~351.9 |

## Words match?

All 7 takes sing their prompted line — no wrong-line take in this sample.
Whisper transcripts match the prompted words exactly (modulo the known
dad mishear class on the song side only). The mismatch is purely timing.

## What this means for a re-cut

- Starts are free: every sampled take begins its line at its slot start,
  so no take needs re-timing at its head.
- Ends are the problem: 5 of 7 takes miss their line end by 0.6–1.8s,
  and 3 of 7 lose their line tail to the slot cut entirely.
- A word-aligned re-cut cannot fix the slow takes by shifting alone —
  their internal tempo differs from the song's, so a shift that fixes the
  first word breaks the last word (and vice versa). Slow takes need
  time-compression to the song's word span, or replacement takes sung at
  song tempo; fast takes need stretching or tail cover.
- S39 needs a take that actually sustains the mantra, not a single repeat.
