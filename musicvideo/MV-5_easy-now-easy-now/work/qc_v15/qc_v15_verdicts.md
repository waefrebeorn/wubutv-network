# Volley 15 QC verdicts — L15 girl-singing fix takes (S07 t2 v2, S07 t3), 2026-11-06 ~02:45 EST

User verdict on v2 master 2026-11-06 ~02:33 EST: the girl's singing is missing in
the beginning because the cat sings her part. L15 "One small look from you"
(song 51.46–52.80, GIRL per the user's ear + Gemini app spk:1) had no
girl-singing picture in v2 — only a closed-mouth donor cover. This volley fired
two parallel-variant girl takes for L15 (same line, same window, different
staging). Both grids agree on L15: v1 words One 51.46–51.728, small 51.728–51.996,
look 51.996–52.264, from 52.264–52.532, you 52.532–52.8 (span 1.34s); app words
identical starts/ends (51.6/51.7/52.2/52.3/52.6–52.8, spk:1 throughout). No grid
disagreement to rescue a fit (unlike L88 in volley 12).

Method: work/qc_v15.py (adapted from qc_v12.py) — Whisper base, prompted +
unprompted, per-0.5s RMS, 160x90 frame-diff motion, frame rule, repeat-bigram
scan. Singer judged by MOUTH FRAMES (PNGs below), never by take f0.
Full numbers: work/qc_v15/qc_v15_results.json. Frames: work/qc_v15/s07_t*.png,
work/qc_v15/s07_t3_t*.png.

## s07_t2 — REJECT (PACING)

- Take: takes/mv5_s07_t2.mp4, md5 39ba0cf638d31f165accd2101ef487e8, 5.000s, 1280x720, 24fps.
- Vehicle: mv5_s07_t2_vehicle_v2.txt (fresh staging — girl seated on the bike at
  the boardwalk rail, close-up; the volley-12 vehicle died on
  integrity_check_failed and was NOT resubmitted).
- Line: sung once, complete, both decodes agree ("One small look from you").
  No repeats. Take words: One 0.0–0.5, small 0.5–1.24, look 1.24–1.72,
  from 1.72–2.1, you 2.1–2.56. Span 2.56s vs song 1.34s → ratio 0.52.
  RMS corroborates the span independently (0.12–0.23 through 2.5s, 0.02 after
  3.0s) — not a Whisper artifact.
- Fit: single warp 1.34/2.56 = 0.52 → playback 1.91x, beyond the 1.5x rescue
  cap and outside the 0.80–1.25 band. Per-word warps 0.54/0.36/0.56/0.71/0.58 —
  all outside band. Best two-anchor split: words 1–3 warp 0.47, words 4–5
  warp 0.64 — both outside band. NO legal placement exists.
  Ratio 0.52 is below the 0.60–0.80 grey zone: clear miss, no re-measure owed.
  Same arithmetic class as s21_t4/t5/t6 (0.35/0.30/0.25, REJECT PACING).
- Picture: PASSES. Girl's mouth open at 0.5s and 1.0s, near-closed at 2.0s
  (mid "from"/"you" — weak single-frame read, not a fail), closed at 3.0s
  hold. Cat mouth closed throughout. Locks hold (sun hat, purple hair,
  purple eyeshadow, red lipstick, red jacket over black crop top, cut-off
  jean shorts; cat black/blue eyes/red collar/yellow bell in basket; blue
  bike, white rims). No legible text, no watermark. Frame rule PASSES
  (vocal mean 1.092, longest near-dup run 1). Motion: 120 frames, mean 1.096.
- Disclosed nit: girl's eyes closed at 0.5s and 1.0s (singing eyes-closed;
  opens by 2.0s). Hair in pigtails — a variant on the loose-hair look, locks
  otherwise hold.

## s07_t3 — REJECT (PACING + DELIVERY)

- Take: takes/mv5_s07_t3.mp4, md5 023a9fc3aa862a7c324a0ffa18807ffc, 5.000s, 1280x720, 24fps.
- Vehicle: mv5_s07_t3_vehicle.txt (parallel variant — girl RIDING the bike
  toward camera, medium-wide moving shot).
- Line: sung once, complete, both decodes agree ("One small look from you").
  No repeats. Take words: One 0.0–1.42, small 1.42–2.06, look 2.06–2.58,
  from 2.58–2.98, you 2.98–3.64. Span 3.64s vs song 1.34s → ratio 0.37.
  Delivery defect on top of the pace miss: "One" held 1.42s, and RMS shows a
  quiet head (0.007/0.026 at 0–1.0s, voice from ~1.0s) — the audible line is
  ~1.0–3.64s, still a 2.64s span (ratio ~0.51, clear miss even on the
  corrected span).
- Fit: single warp 0.37 → playback 2.7x. Per-word warps
  0.19/0.42/0.52/0.67/0.40 — all outside band. NO legal placement exists.
- Picture: PASSES with nits. Girl's mouth open at 1.5s and 2.5s (singing);
  at 4.0s, after the line ended (3.64s), her mouth is still open in a smile
  — the post-line hold is not clean. Cat mouth closed throughout. Locks hold
  (hair loose/wavy here vs pigtails in t2; all lock items present). Frame
  rule PASSES (vocal mean 8.558 — moving shot — longest near-dup run 0).
  TEXT nit: background shop signs carry small letter-like marks (upper-left
  shopfronts); not clearly legible at frame size, flagged not failed.
- Worse than t2 on every axis that matters: longer span, held first word,
  quiet head, unclean post-line hold.

## Better L15 take: s07_t2

t2 is the better take — tighter span (2.56s vs 3.64s), even word distribution,
no delivery defect, clean closed-mouth hold after the line, cleaner picture
(static close-up, no background-sign marks). But it is still a REJECT: no
in-band placement exists for either take.

## Structural conclusion (for the parent, not a reroll)

L15 is STRUCTURAL for per-line generation by the same arithmetic that closed
S28 and the bridge inserts: the song window is 1.34s and the model's measured
pace floor is ~2.2–2.6s/line (t2 2.56s is the best of four L15 attempts
counting the two volley-15 pulls; the volley-12 vehicle never generated).
Two pulls on different stagings both landed clear-miss (0.52 / 0.37). Per the
skill's structural-slot rule, L15 leaves the generation queue: no re-fire, no
third same-vehicle pull, no warp beyond the cap.

CONFLICT FOR THE PARENT TO RESOLVE: the user's 2026-11-06 law bans
closed-mouth covers under sung lines, and the warp cap bans the 1.91x
playback t2 would need — so no in-band option remains inside the current
rules. Options are the parent's call: (a) place t2 at a disclosed out-of-band
warp, (b) a montage treatment for the L15 passage, (c) an audio-driven
repaint (gated, needs user go-ahead), or (d) another assembly treatment.
This volley makes no recommendation between them; it reports the measured
fact that t2 is the best available girl-singing picture for L15 and it does
not place legally.

## S28 — NOT in this volley (correction)

The original brief's mv5_s28_t5 was fired BEFORE the parent's ~02:42 EST
correction arrived (generation record
takes/media-generation-mv5-s28-t5-0-affa3f23-6862-4d1b-8722-5a4510f2fb0a.mp4,
canonical takes/mv5_s28_t5.mp4, md5 b347c9faf46a1fd51902152cd048b28e). Per the
correction, S28 girl generation is CLOSED (t2/t3/t4 all REJECT PACING, floor
~2.7s vs 1.6s window, no legal placement) and L110b keeps its v2 structural
cover. s28_t5 is DISCARDED: no QC row, no verdict, no spend beyond the
already-fired generation. It must not enter the v3 cut. The file is kept on
disk per the keep-every-take rule, marked unused.

## Volley 15 result: 0 KEEP / 2 REJECT (both PACING)
