# Validation — MV-3 16:9 RETIMED master, scored by the cross-check method

Master: `masters/mv3_i_am_your_dad_16x9_retimed.mp4`
md5 `24af63b9c2e4b64a6f038efb3bd39e3b`, 82,818,399 B, 354.833s, 8516
frames, 1280×720 h264 + AAC 48kHz stereo, full decode exit 0
(verified this run). Built by `retime_build.py` from the re-cut cutlist
with exactly three warp factors changed (S16 0.8643→0.810, S18
0.8234→0.965, S34 1.1453→0.910); everything else — segment
boundaries, trims, tail-loop cover, captions, bug, master audio,
frame count — identical to the delivered re-cut.

Build recovery (this run): the previous R&D agent died on a sqlx pool
timeout AFTER the retimed intermediate was verified complete (8516
frames) but DURING the final mux, leaving the final truncated at
30,933,040 B. This run verified the intermediate from disk (8516
frames, full decode OK, 1280×720, 354.833s) and re-ran ONLY the final
mux step (`retime_mux_only.py`, verbatim from `retime_build.py`).
The delivered re-cut is untouched (md5 `300c89feaf5276763e0f8598bc2656d6`
re-verified this run) and the rejected original cut was never touched.

Baseline: `VALIDATION_RECUT_16x9.md` (re-cut master, same method v1).
Method: `CROSSCHECK_SYNC_METHOD.md` v1. Law One: the song is the
tempo gospel — the song's word times never move; only these three
take-side warps change. Validation driver: `retime_validate.py`
(placement with the retimed scene table, motion spot check on the
retimed master, master-audio dictation on the retimed master).
Outputs: `placement_crosscheck_retimed.json`,
`master_motion_spotcheck_retimed.json`,
`master_dictation_report_retimed.json`. The re-cut's baseline JSONs
were never overwritten.

## 0. Verdict — is the retime a genuine improvement?

**Yes, on the three scenes it touched — and on no others, by design.**
The fit's predictions reproduced exactly (see §1). One scene crossed
into WORKING SYNC (S18); the other two improved substantially on
median and on words within ±0.50s but stay GREY by the strict gate,
each by a hair (S16) or by the phrasing gap (S34). No scene regressed
by verdict class. The whole-master verdict class is unchanged: every
mouth scene is WORKING SYNC, disclosed GREY, or flagged COVER, with
the same disclosures as the re-cut — only the GREY count drops 17→16.

- WORKING SYNC (strict gate, method §4c): 7 → **8** (S18 joins).
  S06, S08, S10*, S15, S17, S18, S19, S26. S38 stays borderline
  (max 0.52s vs the 0.50s bar — counted WORKING SYNC with the 0.02s
  overage disclosed, as in the re-cut).
- GREY / disclosed: 17 → **16**. S16 and S34 improved but do not cross.
- COVER: 6, unchanged. DOUBT (S14): 1, unchanged.
- No scene meets the perceptual tier (median ≤0.125s AND max ≤0.25s),
  same as the re-cut. S06 remains the closest (median 0.08s, max
  0.27s). Stated plainly, as before: this is the best word placement
  this pipeline has produced, and it is still an order of magnitude
  outside broadcast lip-sync tolerance. That is a measurement, not a
  veto — and the retime is strictly better than the re-cut on measured
  placement, so it is the current best master. It does not turn the
  grey scenes into synced ones.

## 1. Placement cross-check — all 31 mouth scenes, retimed warps

Re-derived from the existing measured take dictations
(`recut_work/measure/*.json` + slice files) + retimed placement math.
A JSON diff of `placement_crosscheck.json` vs
`placement_crosscheck_retimed.json` shows **only S16, S18, S34
changed — every other scene's score is byte-identical**, as it must
be: only three warps changed. (One doc erratum found by the diff: the
re-cut doc's table printed S28's usable denominator as 33; the JSON
says 32 in both runs, unchanged.)

| Scene | Take | Agree | Median \|off\| (re-cut → retimed) | Max \|off\| (re-cut → retimed) | Drift | ≤0.25s | ≤0.50s | Verdict |
|---|---|---|---|---|---|---|---|---|
| S01 | s01_t2 | 1.00 | 1.17s → 1.17s | 1.42s → 1.42s | −0.41 | 1/4 | — | GREY (phrasing gap), unchanged |
| S02 | s02_t2 | 1.00 | 0.61s | 1.31s | −0.73 | 2/7 | — | GREY, unchanged |
| S06 | s06_t1 | 0.957 | 0.08s | 0.27s | +0.17 | 21/22 | — | WORKING SYNC, unchanged |
| S07 | s07_t1 | 1.00 | 0.40s | 0.60s | +0.27 | 2/20 | — | GREY, unchanged |
| S08 | s08_t1 | 1.00 | 0.13s | 0.31s | +0.13 | 20/21 | — | WORKING SYNC, unchanged |
| S09 | s09_t1 | 1.00 | 0.64s | 1.36s | +0.88 | 2/12 | — | GREY, unchanged |
| S10 | s10_t1 | 1.00 | 0.19s | 0.99s | +0.02 | 8/14 | — | WORKING SYNC* (first-word stamp caveat), unchanged |
| S11 | s11_t2 | 0.727 | 0.43s | 1.54s | −1.47 | 2/8 | — | GREY / span-only, unchanged |
| S12 | s12_t2 | 1.00 | 0.17s | 1.18s | +0.35 | 4/7 | — | GREY, unchanged |
| S13 | s13_t1 | 0.867 | 1.77s | 2.08s | −1.20 | 0/13 | — | GREY / span-only, unchanged |
| S14 | s14_t1 | 0.481 | 0.64s | 1.99s | +0.30 | 1/12 | — | DOUBT, unchanged |
| S15 | s15_t1 | 1.00 | 0.13s | 0.35s | +0.09 | 18/22 | — | WORKING SYNC, unchanged |
| **S16** | s16_t1 | 0.944 | **0.47s → 0.28s** | **0.66s → 0.54s** | +0.15 → −0.26 | 5/15 | **9 → 13/15** | **GREY (improved) — misses the working bar by 0.03s median / 0.04s max** |
| S17 | s17_t1 | 1.00 | 0.15s | 0.47s | −0.18 | 9/12 | — | WORKING SYNC, unchanged |
| **S18** | s18_t2 | 1.00 | **0.77s → 0.19s** | **0.91s → 0.37s** | −0.77 → +0.18 | **4 → 9/14** | **5 → 14/14** | **WORKING SYNC — joined** |
| S19 | s19_t1 | 1.00 | 0.12s | 0.43s | +0.12 | 14/16 | — | WORKING SYNC, unchanged |
| S20 | s20_t1 | 1.00 | 0.86s | 1.00s | −0.52 | 1/5 | — | GREY, unchanged |
| S22 | s22_t1 | 1.00 | 0.62s | 1.45s | −0.98 | 1/6 | — | GREY, unchanged |
| S23 | s23_t2 | 0.944 | 1.04s | 3.11s | −3.11 | 2/17 | — | GREY, unchanged |
| S26 | s26_t1 | 1.00 | 0.18s | 0.62s | −0.16 | 7/10 | — | WORKING SYNC, unchanged |
| S27 | s27_t1 | 1.00 | 0.95s | 1.40s | −0.06 | 4/24 | — | GREY (phrasing hump; no warp fixes it), unchanged |
| S28 | s28_t3 | 0.917 | 0.41s | 2.79s | −2.79 | 15/32 | — | GREY, unchanged |
| S29 | s29_t1 | 1.00 | 1.02s | 1.67s | +1.02 | 4/12 | — | GREY, unchanged |
| S31 | s31_t1 | 0.545 | 0.48s | 2.40s | +0.48 | 4/11 | — | COVER, unchanged |
| S32 | s32_t1 | 1.00 | 2.04s | 2.61s | −1.05 | 1/8 | — | COVER, unchanged |
| S33 | s33_t1 | 0.083 | 0.82s† | 1.08s† | +1.12 | 1/4 | — | COVER, unchanged |
| **S34** | s34_t1 | 1.00 | **0.51s → 0.26s** | **1.67s → 2.07s** | +1.30 → −0.19 | **3 → 6/12** | **6 → 8/12** | **GREY (improved) — closing phrase fixed, phrasing gap still binds** |
| S36 | s36_t2 | 1.00 | 1.58s | 2.09s | −1.17 | 1/14 | — | GREY, unchanged |
| S37 | s37_t1 | 0.348 | 1.57s | 1.72s | +0.72 | 0/8 | — | COVER-remainder, unchanged |
| S38 | s38_t2 | 0.929 | 0.17s | 0.52s | +0.23 | 8/13 | — | WORKING SYNC (borderline, 0.02s overage disclosed), unchanged |
| S39 | s39_t1 | 0.267 | 1.60s | 1.80s | +0.80 | 0/4 | — | COVER, unchanged |

† S33 as in the re-cut doc: pile-up artifact, see VALIDATION_RECUT_16x9.md §2.

The three changed scenes, per word (from `retime_warps.json` predictions
vs the re-scored master — the predictions reproduced exactly):

- **S16 (w 0.8643 → 0.810).** The re-cut's warp left a near-constant
  +0.5s bias; the fit centers it. Per-word offsets now run 0.00–0.54s
  (was 0.00–0.66s), mean +0.36→+0.12s. Words within ±0.50s 9→13/15,
  within ±0.125s 1→3. Cost: the tail ("and" −0.49s) lands early — the
  −0.46s end residual, covered by the tail-loop as designed. Verdict:
  GREY, improved. It misses WORKING SYNC by 0.03s on median and 0.04s
  on max — the gate is not moved to let it in.
- **S18 (w 0.8234 → 0.965).** The largest single-scene improvement in
  the master, as predicted. The span-ratio warp was wrong for this
  line's held words; the least-squares warp centers them: offsets now
  −0.37…+0.28s (was −0.91…+0.20s), mean −0.51→−0.05s, drift
  −0.77→+0.18s. All 14 words within ±0.50s (was 5). Verdict: WORKING
  SYNC — the only scene that crosses the bar in this retime.
- **S34 (w 1.1453 → 0.910).** A trade, disclosed in full. The closing
  phrase "just a low voice" goes from +1.03–1.30s late to −0.08–0.22s
  — fixed. The middle mantra pays for it: its "i" goes −1.67→−2.07s
  and "am/your/dad" from ~0.0s to −1.07/−0.94/−0.88s early. Both
  effects sit inside the already-disclosed phrasing gap (the song
  pauses 2.42s there; no warp fixes it) — the gap is unchanged as a
  class, only the distribution inside it moved. Net: median 0.51→0.26s,
  words within ±0.50s 6→8/12, within ±1.00s 7→10/12, end residual
  +1.70→+0.02s. The worst word got worse by +0.40s, inside the fit's
  +0.50s guard — the adoption criteria were met, but the trade is
  visible in the ledger and is not hidden behind the improved median.
  Verdict: GREY, improved — the phrasing-gap word (−2.07s) still
  binds, and the median (0.26s) is 0.01s over the working bar.

## 2. Picture-motion spot check (retimed master)

At each mouth scene's first song-word time, the retimed master frame
vs the frame 0.5s earlier (mean abs diff at 160×90; >0.5 = moving).
`master_motion_spotcheck_retimed.json`. Result: **31/31 scenes moving.**
Diffs 4.45–110.71. The two low values are the same ones the re-cut had:
S01 (0.85 — first word lands exactly on the leader-hold boundary,
the disclosed pre-first-word hold, mouth moving immediately after)
and S32 (4.45 — low but moving). No frozen coverage at any sampled
word time. The picture change did not freeze anything.

## 3. Master-audio dictation stability — the check that failed its own test

Measured this run: the retimed master's audio transcribed fresh with
the full performed lyrics as `initial_prompt` (618 words decoded),
aligned to `SONG_WORDS.json` (729 words). `master_dictation_report_retimed.json`.

- Agreement 0.477 (348/729 matched). Median |offset| 0.02s. Within
  ±0.25s: 248/300 usable pairs; within ±0.50s: 263/300.
- 26 pairs excluded as wrong-repeat matcher artifacts; ONE 144.72s
  outlier remains — a pair the filter could not resolve because the
  low agreement left no nearer occurrence of that token unmatched.
  It is one pair out of 300 and does not move the median; it is a
  matcher artifact on identical audio, not a timing error, and it is
  reported, not hidden.

Compare the re-cut run (same method, same prompt, same audio in
substance): agreement 0.675 (492/729), 585 words decoded, median
|offset| 0.02s, max 21.1s, 10 wrong-repeat pairs. **The audio is
byte-identical** — the decoded PCM of both masters has the same md5
(`07c01e5d8370ed366ecae4f9b7fedbc4`, same AAC bit rate 196556) — yet
the prompted decode produced 585 words one run and 618 the next, and
agreement swung 0.675 → 0.477. The median offset is rock-stable
(0.02s both runs): the timing of the words both passes find is
trustworthy. The identity/coverage of the words found is NOT stable
run to run on mantra-dense material.

What this means, stated plainly:

- **The master-audio agreement number is not a repeatable
  measurement and must not be used as a gate.** The re-cut doc's
  "0.675 is the method's ceiling on mantra-dense material" is now
  known to be one draw from a distribution, not a ceiling — the same
  audio re-draws at 0.477. Any future use of master-audio agreement
  must run the decode at least twice and report the spread, or drop
  the agreement figure and keep only the median offset (stable at
  0.02s across both runs).
- **This does not touch the placement verdicts in §1.** Those use the
  cached take dictations (deterministic, same files both runs) plus
  placement math. Only the three warps changed, and the JSON diff
  proves only three scenes moved. The picture-sync numbers are
  reproducible; the master-audio agreement number is not.
- Prototype bug noted: `crosscheck_sync.py` `do_master()` hardcodes
  `"master": "mv3_i_am_your_dad_16x9_recut.mp4"` in its report dict
  even when run on the retimed file — the md5 field in the retimed
  report is correct (`24af63b9c2e4b64a6f038efb3bd39e3b`), the filename
  label is stale. Cosmetic; fix the label before the next master-mode
  run. The re-cut's cached dictation (`master_dictation_prompted.json`,
  585 words, md5 `300c89fe...`) was parked aside during this run and
  restored intact — verified after the run.

## 4. Whole-master verdict

The retimed master holds word-sync under the method's whole-master
rule: every mouth scene is SYNCED or WORKING SYNC, or a disclosed
GREY / flagged COVER, with no undisclosed grey scene. Counts: 8
WORKING SYNC (strict) + S38 borderline + 16 GREY / disclosed + 6
COVER + 1 DOUBT (S14). The re-cut's acceptance stands, and the
retime is strictly better on measured placement — it is the current
best master. It is still not perceptual-tier, and the grey scenes
(S01, S02, S07, S09, S11, S12, S13, S16, S20, S22, S23, S27, S28,
S29, S34, S36) remain disclosed grey: no stronger claim is made.

## 5. Files (this run)

- `masters/mv3_i_am_your_dad_16x9_retimed.mp4` — md5
  `24af63b9c2e4b64a6f038efb3bd39e3b`, 82,818,399 B, 354.833s, 8516
  frames, 1280×720 h264 + AAC, full decode exit 0.
- `masters/mv3_intermediate_16x9_retimed.mp4` — 160,036,352 B, 8516
  frames, full decode exit 0 (verified before the re-mux).
- `recut_work/sync_proto/retime_mux_only.py` + `retime_mux.log` —
  final-mux-only recovery script and its log.
- `recut_work/sync_proto/retime_validate.py` + `retime_validate.log`
  — validation driver (placement + motion + master dictation).
- `recut_work/sync_proto/placement_crosscheck_retimed.json`,
  `master_motion_spotcheck_retimed.json`,
  `master_dictation_report_retimed.json` — retimed measurements.
- Re-cut baseline files untouched: `placement_crosscheck.json`,
  `master_motion_spotcheck.json`, `master_dictation_report.json`,
  `master_dictation_prompted.json`, `VALIDATION_RECUT_16x9.md`.
