# EXAMPLES — swing_keyframes.py on two MV-5 takes (2026-11-06)

Tool: `swing_keyframes.py` (this dir). Outputs: `s07_t2_swing.json`,
`s01_t1_swing.json`. Both runs: fresh unprompted + prompted
faster-whisper base decodes via `~/workspace/fw-venv` (the crosscheck
path), no caches reused.

## 1. The pacing miss — takes/mv5_s07_t2.mp4, L15 "One small look from you"

Known before the run (qc_v15): sings the line once, complete, over
0.0–2.56s against a 1.34s song window — ratio 0.52, REJECT (PACING) as
a generation take; in v3 it is placed by per-word warping under the
2026-11-06 law (speedups fine).

Tool output — **independently reproduces the known measurement**:
line ratio **0.523**, take word starts identical to qc_v15's
(0.0 / 0.5 / 1.24 / 1.72→1.74 / 2.1; 0.02s decode jitter on "from").

| word | song start | take start | swing | interval playback | verdict |
|---|---|---|---|---|---|
| One | 51.460 | 0.00 | 0.000 | 1.87× | WARPABLE |
| small | 51.728 | 0.50 | +0.232 | 2.76× | WARPABLE |
| look | 51.996 | 1.24 | +0.704 | 1.87× | WARPABLE |
| from | 52.264 | 1.74 | +0.936 | 1.34× | WARPABLE |
| you | 52.532 | 2.10 | +1.028 | 1.72× (word) | WARPABLE |

**Confirmed as briefed:** every interval is an extreme *speedup*
(1.34–2.76×) — and speedups are legal without cap under the warp law,
so all five words are WARPABLE, zero montage cuts. The swing column
shows the disease exactly: anchored at "One", the take falls behind
monotonically to +1.03s by "you" — tempo drift, not a shift — which is
why one uniform warp could never place it and per-word keyframes can.
The tool's setpts factors (0.54 / 0.36 / 0.54 / 0.74 / 0.58) match the
hand-computed v3 per-word warps (0.54 / 0.36 / 0.56 / 0.71 / 0.58)
within decode jitter.

## 2. The healthy take — takes/mv5_s01_t1.mp4, intro hook (song 1.66–10.04)

16 song words ("Easy now, easy now / we ride, we ride / easy now,
easy now / till the morning comes"). Tool output:

- **Coverage/identity: clean pass.** 16/16 words matched, correct
  words in order, no BAD-wrong, no BAD-missing, no BAD-repeat, no
  extras. Unprompted decode is clean — the song-side "easy → is it"
  mishear class was armed (line contains "easy", no "is") but the
  take decode never triggered it. Line ratio **0.903** (vs L15's
  0.523 — the healthy/miss contrast is stark).
- **Per-word: NOT uniformly clean — and that is a real finding, not a
  tool error.** 1 GOOD, 14 WARPABLE, 1 BAD-out-of-caps. Anchored
  swing wanders +0.02 → +1.32s: the take sings the hook in its own
  even phrasing while the song stretches and breathes (song "ride"
  held 4.90–5.98; song "Easy" at 5.98 held 0.68s). Per-word warps
  (0.49–2.88×, mixed directions) place every word — this is precisely
  the case the swing method exists for: a KEEP take whose *slot*
  placement would drift a full second.
- **The one BAD flag is a knife-edge, surfaced honestly:** the
  Easy(5.98)→now(6.66) interval needs playback **0.485×** — 0.015
  past the 2×-slow cap (the take compresses "Easy now" where the
  song holds "Easy"). The tool emits the sanctioned treatment: a
  montage span over "now" (song 6.66–7.10), cut out on beat 6.478,
  return on the next good onset 7.32 ("easy"). In a real assembly
  the alternatives are that micro-cut or a disclosed ~0.1s residual
  on "now" — the tool's job is to force the choice into the open,
  and it does. (Precedent: MV-2 R3's 0.49919 frame gate was likewise
  held, not rounded up.)
- **Caveat — part of S01's measured swing is song-side softness.**
  The intro word times in SONG_WORDS.json are flagged
  `confidence: inferred` with even-split spans; L15's times are
  `confirmed`. Read S01's swing as an upper bound: hard where the
  grid is hard (it still proves the take's phrasing differs from the
  song's), soft where the grid is estimated. Decode jitter on short
  function words is also real: this run's fresh decode stamps "We"
  at 2.72 vs the earlier prompted cache's 3.04 — word identity and
  order identical, times ±0.3s on the shortest words.

## Verdict on the tool

It reproduces the known L15 measurement from scratch, separates the
healthy take from the miss on every axis that matters (ratio 0.90 vs
0.52, 16/16 vs complete-but-drifting), turns both into assembly-ready
keyframe tables, and flags the one genuinely capped interval instead
of smoothing it over. The traps wired in (split-half, mishear map,
prompted+RMS credit) did not fire on these two clean decodes — they
are load-bearing for dirtier takes (volley 12/13 classes) and are
exercised by construction, not by these examples.
