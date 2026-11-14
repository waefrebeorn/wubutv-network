# Validation — MV-3 16:9 re-cut master, scored by the cross-check method

Master: `masters/mv3_i_am_your_dad_16x9_recut.mp4`
md5 `300c89feaf5276763e0f8598bc2656d6`, 82,781,036 B, 354.833s, 8516
frames, 1280×720 h264 + AAC, full decode exit 0 (verified by parent
2026-11-05 ~01:13 EST). Delivered to the user ~01:13 EST and ACCEPTED
~01:20 EST ("focus on only the one master, this is okay"). This
validation is therefore confirmation of an accepted master, not a gate
— and it is the baseline the retimed master (`*_16x9_retimed.mp4`) is
measured against.

Method: `recut_work/sync_proto/CROSSCHECK_SYNC_METHOD.md` v1.
Law One: the song is the tempo gospel — the song's word times never
move; only take-side warps change. Single-format policy (user
2026-11-05 ~01:31 EST): only one 16:9 from now on — no 9:16, no chat
copy. The retime changes exactly three warp factors (see §4).

## 1. Take cross-check — fresh prompted vs unprompted dictations

Three takes, each transcribed twice with faster-whisper base
(unprompted, and with the scene's performed line as `initial_prompt`),
then placed by the cutlist and scored against the song window.
Full per-word data: `take_crosscheck.json`.

| Take | Words | Agreement | Median \|off\| | Max \|off\| | Drift | Prompt effect |
|---|---|---|---|---|---|---|
| S01 t2 (grey, phrasing gap) | 4 | 1.00 | 1.15s | 1.42s | −0.44s | none: same 4 words, max 1.42→1.35s |
| S06 t1 (cleanest) | 23 | 0.957 | 0.08s | 0.27s | +0.17s | none: same 23 words, max 0.27→0.29s |
| S27 t1 (phrasing gap) | 24 | 1.00 | 0.96s | 1.40s | −0.08s | none: same 24 words, max 1.40→1.51s |

Findings:
- **The lyrics hint changed almost nothing on these takes.** Same word
  counts, same agreement, offsets shifted by ≤0.07s. The decoder
  already heard the right words; the prompt's value here is
  confirmation, not correction. That is a measured result, not a
  failure: it means the take dictations the re-cut trusted were already
  stable, and the hint's job is to catch the cases where they are not
  (garbled windows — see §2, S11/S14). The hint is a prior with a
  measured effect, and on MV-3's takes the effect is ~zero.
- **The method reproduces the re-cut's known findings independently.**
  S06's per-word offsets (median 0.08s, max 0.27s) match the re-cut's
  "per-word max 0.27s — cleanest sync in the cut". S01's phrasing gap
  reappears exactly: "all" +1.42s, "of" +1.15s, first word 0.00s.
  S27's mid-line hump reappears: offsets rise to +1.40s mid-line and
  fall back to ~0 at the ends. A second, independent dictation pass
  landing on the same numbers is what a cross-check is for.
- **S06 is the only take in the sample that meets the WORKING SYNC bar**
  (agreement ≥0.9, median ≤0.25s, max ≤0.50s). S01 and S27 are GREY /
  DISCLOSED, as the re-cut already flagged them. No take in the sample
  meets the perceptual tier (±0.125s median) except S06's median of
  0.08s with a max of 0.27s — S06 is close to perceptual on median but
  its max (0.27s) is still 2x the ±0.125s bound.

## 2. Placement cross-check — all 31 mouth scenes

Every mouth scene re-scored from the existing measured take dictations
(`recut_work/measure/*.json` + slice files) + cutlist placement math.
Full table: `placement_crosscheck.json`. Verdicts use the method's gates
(§4 of the method doc). "Within 0.50s" counts matched words with usable
time (zero-duration pile-up words excluded).

| Scene | Take | Flag | Agree | Median \|off\| | Max \|off\| | Drift | ≤0.25s | Verdict |
|---|---|---|---|---|---|---|---|---|
| S01 | s01_t2 | grey | 1.00 | 1.17s | 1.42s | −0.41 | 1/4 | GREY (phrasing gap) |
| S02 | s02_t2 | grey | 1.00 | 0.61s | 1.31s | −0.73 | 2/7 | GREY |
| S06 | s06_t1 | — | 0.957 | 0.08s | 0.27s | +0.17 | 21/22 | WORKING SYNC |
| S07 | s07_t1 | grey | 1.00 | 0.40s | 0.60s | +0.27 | 2/20 | GREY |
| S08 | s08_t1 | — | 1.00 | 0.13s | 0.31s | +0.13 | 20/21 | WORKING SYNC |
| S09 | s09_t1 | grey | 1.00 | 0.64s | 1.36s | +0.88 | 2/12 | GREY |
| S10 | s10_t1 | — | 1.00 | 0.19s | 0.99s | +0.02 | 8/14 | WORKING SYNC* |
| S11 | s11_t2 | grey | 0.727 | 0.43s | 1.54s | −1.47 | 2/8 | GREY / span-only (garbled song window) |
| S12 | s12_t2 | grey | 1.00 | 0.17s | 1.18s | +0.35 | 4/7 | GREY (max driven by one late word) |
| S13 | s13_t1 | — | 0.867 | 1.77s | 2.08s | −1.20 | 0/13 | GREY / span-only — see note |
| S14 | s14_t1 | — | 0.481 | 0.64s | 1.99s | +0.30 | 1/12 | DOUBT (garbled song window, agreement 0.48) |
| S15 | s15_t1 | — | 1.00 | 0.13s | 0.35s | +0.09 | 18/22 | WORKING SYNC |
| S16 | s16_t1 | — | 0.944 | 0.47s | 0.66s | +0.15 | 5/15 | GREY → RETIMED (see §4) |
| S17 | s17_t1 | — | 1.00 | 0.15s | 0.47s | −0.18 | 9/12 | WORKING SYNC |
| S18 | s18_t2 | — | 1.00 | 0.77s | 0.91s | −0.77 | 4/14 | GREY → RETIMED (see §4) |
| S19 | s19_t1 | — | 1.00 | 0.12s | 0.43s | +0.12 | 14/16 | WORKING SYNC |
| S20 | s20_t1 | grey | 1.00 | 0.86s | 1.00s | −0.52 | 1/5 | GREY (only 5 usable pairs — pile-up window) |
| S22 | s22_t1 | — | 1.00 | 0.62s | 1.45s | −0.98 | 1/6 | GREY (song merges the two "dad"s) |
| S23 | s23_t2 | grey | 0.944 | 1.04s | 3.11s | −3.11 | 2/17 | GREY (tail rushes; warp already at 1.25 edge) |
| S26 | s26_t1 | — | 1.00 | 0.18s | 0.62s | −0.16 | 7/10 | WORKING SYNC |
| S27 | s27_t1 | phrasing-gap | 1.00 | 0.95s | 1.40s | −0.06 | 4/24 | GREY (phrasing hump; no warp fixes it) |
| S28 | s28_t3 | grey | 0.917 | 0.41s | 2.79s | −2.79 | 15/33 | GREY (two-phrase split: L30 lands, L31 tail −2.8s) |
| S29 | s29_t1 | grey | 1.00 | 1.02s | 1.67s | +1.02 | 4/12 | GREY |
| S31 | s31_t1 | mantra-slice | 0.545 | 0.48s | 2.40s | +0.48 | 4/11 | COVER (repeats not matched, as disclosed) |
| S32 | s32_t1 | mantra-slice | 1.00 | 2.04s | 2.61s | −1.05 | 1/8 | COVER (repeats not matched, as disclosed) |
| S33 | s33_t1 | mantra-slice | 0.083 | 0.82s† | 1.08s† | +1.12 | 1/4 | COVER (pile-up block: 121/145 song words zero-duration) |
| S34 | s34_t1 | phrasing-gap | 1.00 | 0.51s | 1.67s | +1.30 | 3/12 | GREY → RETIMED (see §4) |
| S36 | s36_t2 | grey | 1.00 | 1.58s | 2.09s | −1.17 | 1/14 | GREY (sparse song phrasing vs continuous take) |
| S37 | s37_t1 | mantra-opening | 0.348 | 1.57s | 1.72s | +0.72 | 0/8 | COVER-remainder (opening bursts mouth-synced; rest is hold-loop cover, correctly uncredited) |
| S38 | s38_t2 | grey | 0.929 | 0.17s | 0.52s | +0.23 | 8/13 | WORKING SYNC (best grey result, as the re-cut said) |
| S39 | s39_t1 | montage-cover | 0.267 | 1.60s | 1.80s | +0.80 | 0/4 | COVER (one mantra vs 4 song repeats — the known gap) |

Totals: 31 mouth scenes = 7 WORKING SYNC (S06, S08, S10*, S15, S17,
S19, S26) + 1 borderline (S38, max 0.52s vs the 0.50s bar — counted
WORKING SYNC with the 0.02s overage disclosed) + 17 GREY / disclosed +
6 COVER (S31–S33 mantra-slice, S37 remainder, S39, plus S14 DOUBT).
*S10's max (0.99s) is the known long first-word Whisper stamp ("i"
0–1.22s); words 2+ are within 0.32s — the re-cut's own caveat, reproduced.

Notes the cross-check adds beyond the re-cut's span analysis:
- **S13 is the sharpest correction.** The re-cut called it span-usable
  (endpoints land). Per-word, its median offset is 1.77s and ZERO of 13
  matched words land within 0.25s. Cause: the song holds "you" for
  2.86s (91.18–94.04) while the take says it in ~0.3s — a phrasing
  mismatch span ratio cannot see. S13 ships as GREY/span-only, not as
  a synced scene. Span-usable ≠ word-synced; this is the method's
  clearest proof of value.
- **S14 is the only DOUBT.** Agreement 0.481 — the song window itself
  is garbled ("sit in the beast"), so token identity is unreliable and
  the offsets are not trustworthy. The re-cut already scored it
  span-level only; the cross-check formalizes that as DOUBT, not as a
  number.
- **S33's agreement (0.083) is a measurement artifact, honestly
  labeled.** The window holds 145 song words, 121 of them zero-duration
  pile-up stamps at 282.18. Excluding pile-ups, agreement is 0.333
  (8/24 usable) — still COVER, but the 0.083 is the pile-up's shadow,
  not the take's failure. Mantra blocks must be scored by span +
  burst count, never by per-word agreement.
- **Wrong-repeat filter (added 2026-11-05, after the master check
  exposed it).** A token-order alignment can credit a word to the
  wrong mantra repeat. The prototype now drops a >2s pair ONLY when a
  nearer occurrence of the same token exists unmatched within 0.5s of
  the take word's placed time; otherwise the pair is kept as real
  error (a take tail genuinely 2–3s early must stay visible). An
  earlier, dumber version of the filter dropped every >2s pair and
  flattered S23's median 1.04→0.30s by hiding its real tail rush — that
  version was caught, reverted, and replaced; the numbers in this table
  are the corrected ones. S23 (1.04s) and S28 (0.41s) medians are
  unchanged by the corrected filter. Only S33 moved (median 3.14→0.82s,
  max 6.02→1.08s, 4 wrong-repeat pairs dropped) — still COVER.
- **No scene meets the perceptual tier** (median ≤0.125s AND max
  ≤0.25s). The best, S06 (median 0.08s, max 0.27s), misses on max by
  one word. Stated plainly: the re-cut is the best word placement this
  pipeline has produced, and it is still an order of magnitude outside
  broadcast lip-sync tolerance (±45ms lead / ±125ms lag). The user's
  acceptance of the 16:9 stands — this is a measurement, not a veto —
  but no stronger claim is made.

## 3. Picture-motion spot check (delivered master)

At each mouth scene's first song-word time, the master frame vs the
frame 0.5s earlier (mean abs diff at 160×90; >0.5 = moving).
`master_motion_spotcheck.json`. Result: **31/31 scenes moving.**
Diffs 39–110 for 30 scenes. The one low value is S01 (0.85): its first
word ("listen", 2.82s) lands exactly on the leader-hold boundary — the
frame at 2.82s is the held S01 frame 0, so the 0.5s-earlier frame is the
same held frame. The mouth starts moving immediately after; this is the
disclosed pre-first-word hold, not a freeze during words. No frozen
coverage found at any sampled word time.

## 4. The retime — what changed and why

Warp-fit (fit_retime.py): per scene, grid-search w in [0.80, 1.25]
(first word anchored) minimizing median |offset|; adopt only on
median gain ≥0.10s AND worst word no worse than +0.50s AND words
within ±0.50s not decreasing AND symmetric end-residual guard
(|end_new| ≤ max(|end_old|, 0.50) + 0.25 — a fit may not trade the
ending for the middle). Full table: `retime_warps.json`.

Adopted (3 scenes):
- **S16: w 0.8643 → 0.810.** Median 0.47→0.28s, max 0.66→0.54s,
  words within ±0.50s 9→13/15. The re-cut's warp left a near-constant
  +0.5s bias; the fit centers it. End residual 0.00→−0.46s (tail-loop).
- **S18: w 0.8234 → 0.965.** Median 0.77→0.19s, max 0.91→0.37s,
  words within ±0.50s 5→14/14. The largest single-scene improvement in
  the master: the span-ratio warp was wrong for this line's held words;
  the least-squares warp centers them. End residual −0.72→+0.37s.
- **S34: w 1.1453 → 0.910.** Median 0.51→0.26s, words within ±0.50s
  6→8/12, end residual +1.70→+0.02s. The closing phrase "just a low
  voice" goes from +1.03–1.30s late to −0.08–0.22s. Cost: the middle
  mantra's "i" goes −1.67→−2.07s — inside the already-disclosed
  phrasing gap (the song pauses 2.42s there; no warp fixes it).

Rejected fits (recorded, not hidden): S27's fit (median 0.95→0.38s)
was rejected — it landed the last word 1.78s early, trading the ending
for the middle. S28's fit (median 0.41→0.29s) was rejected — it made
the tail worse (−2.79→−3.33s) and dropped words within ±0.50s 20→17.
S13's fit was rejected on the end guard. All other scenes: no fit beat
the re-cut warp by ≥0.10s median, or were unfittable (too few usable
pairs) / never-fit (cover).

Retimed master: `masters/mv3_i_am_your_dad_16x9_retimed.mp4`
(build: `retime_build.py`, final mux re-run by `retime_mux_only.py`
after the previous agent died mid-mux; log `retime_build.log` +
`retime_mux.log`).
[BUILD STATUS — retimed master landed 2026-11-05 ~03:03 EST: md5
`24af63b9c2e4b64a6f038efb3bd39e3b`, 82,818,399 B, 354.833s, 8516
frames, 1280×720 h264 + AAC, full decode exit 0. Scored in
`RETIME_VALIDATION.md`: WORKING SYNC 7 → 8 (S18 joins; S16/S34
improved but stay GREY); motion 31/31 moving; master-audio agreement
re-drew 0.477 vs the re-cut run's 0.675 on byte-identical audio —
the agreement figure is not repeatable, median offset 0.02s is.]

Expected retimed totals (predicted from the fit, to be confirmed by
re-scoring the rendered master): WORKING SYNC 7 → 10 (S16, S18, S34
join, pending re-verification); median |offset| across matched words
improves in 3 scenes, unchanged elsewhere; no scene changes verdict
in the other direction.

## 5. Master-audio dictation stability (same audio both sides)

Measured 2026-11-05: the delivered master's audio transcribed fresh
with the full performed lyrics as `initial_prompt` (585 words decoded),
aligned to `SONG_WORDS.json` (729 words, the unprompted reference
dictation). `master_dictation_report.json`.

- Agreement 0.675 (492/729 matched). Median |offset| 0.02s. Within
  ±0.25s: 387/459 usable pairs; within ±0.50s: 410/459.
- 10 pairs excluded as wrong-repeat matcher artifacts; ONE 21.1s
  outlier remains — a single pairing the filter could not resolve
  because every nearer repeat of that token was already matched. It is
  one pair out of 459 and does not move the median; it is reported,
  not hidden.

What this bounds: **dictation timing is stable, dictation identity is
not.** Two passes over IDENTICAL audio agree on the time of the words
they both find to within 0.02s median — so the per-word offsets in §2
are trustworthy as times. But they agree on only 67.5% of the words at
all, because the prompted pass dropped ~144 words, almost all of them
mantra repeats in the dense blocks (L26 tail, L34) where Whisper
pile-ups and drops repeats. That 0.675 is the method's own ceiling on
mantra-dense material: take-vs-song agreement can never exceed it in
those blocks, and agreement must be read with that ceiling in mind.
The picture-sync verdicts in §2 already respect this (mantra blocks
scored by span, S33/S37/S39 as cover regardless of agreement).
