# Sprint MDX_STEMACT — validate the MDX stem-activity curve as the pipeline's voice-activity sensor (2026-11-12)

**Verdict: A+B PASS, C FAILS — the stem-activity curve is VALID as a
voice-activity curve; its STAY-RULE use FAILS. The stay-rule patch has no
sensor.**
*Loop 6 top-1 sprint (loop 5 §3 #2 + §8.2; loop-06 SPRINT_SCOPE.md). Scope:
`research_notes/slopcannon-improvement-loop/loop-06/SPRINT_SCOPE.md`.
Coordinator: session 9b01b8aa. No commit (parent owns commits), no Telegram,
no video generation, no Demucs model run, no c11_sep re-run, no TSM work.*

## Headline numbers (each read from the validation JSON on disk)

| Bar (held, not lowered) | Measured | Verdict |
|---|---|---|
| A — RMS-VAD boundaries ±0.5 s vs Demucs stem-activity boundaries, 12 ref segments | MDX max \|dStart\| **0.21 s**; c11 **0.21 s**; Demucs **0.00 s** (self) | **PASS** (all three) |
| B — 25 ms RMS envelope separates sung from instrumental, non-overlapping IQRs, all three stems | Sung q25 0.0207 / 0.0207 / 0.0267 vs instrumental q75 0.00084 / 0.00084 / 0.00163 (MDX / c11 / Demucs) | **PASS** (all three) |
| C — stem-envelope-at-snapped-position separates 5 snap errors from 15 correct controls (MW one-sided p < 0.05 AND errors median < correct median) | c11: errors median 0.04909 vs controls 0.07016, MW U=29/75, **p = 0.2486**; MDX identical | **FAIL** |
| Secondary — sprint-6 median ratio active/silent ≥100× | 248.9× (MDX, c11, sung-only masks) / 242.7× (all-12 masks); Demucs 200.5× / 191.0× | Pass (not the bar) |

Per the pre-stated verdict logic (A+B pass, C fails): **the sensor is valid
as a voice-activity curve — the mouth-open gate and CCA may calibrate on
it — but the stay-rule use FAILS. The stay-rule patch has no sensor.** This
is the last in-span candidate: c11_voice curve, vibrato depth, spectral
entropy, vocal-flux (both flavours), and now stem-envelope-at-snapped-position
are all dead on MV-14.

## Calibration (done first, before any bar was run)

The validator was calibrated on the ONNX MDX stem against loop 5's numbers
before touching the c11 stem. Reproduced exactly:

| Measure | Loop 5 | This sprint (MDX stem) |
|---|---|---|
| RMS-VAD segments | 17 | 17 |
| max \|dStart\| | 0.21 s | 0.21 s |
| active/silent ratio | 248.8× | 248.9× |

One calibration subtlety, recorded so nobody re-"discovers" it: loop 5's
248.8× uses the **sung-only active mask** (ref segments 1–10) vs outside-all-12
silent (`r8_precheck_mdx_verify.py` lines 149–150: `act_m =
span_mask(sung)`, `sil_m = ~span_mask(segs)`). The all-12-active variant —
what `validate_fulltrack.active_silent_ratio` computes — is 242.7× on the
same stem, which is the number c11_sep §6 recorded as its reproduction.
Both are the same statistic under different active masks; the 6.1× gap is
the bleed segments 11–12 dragging the active median down. The validator's
calibration block checks the sung-only ratio (248.9 vs 248.8) and reports
the all-12 variant alongside. `calibration_pass: true` in
`stem_mdx_validation.json`.

## Bar A — boundaries: PASS (all three stems)

Method: the pipeline's own RMS-VAD recipe, imported verbatim from
`c11_mir/make_ref_segments.py` (25 ms window / 10 ms hop, threshold
0.1 × p99 RMS, merge bar 1.0 s, drop < 0.5 s, split > 30 s at the quietest
point, 0.3 s pad), run on each 44.1 kHz mono stem; span-start metric from
c11_sep stage 4 (ref spans overlap-merged; each matched to its earliest-start
overlapping pred piece). Bar: max |dStart| ≤ 0.5 s on the 12 ref segments.

| Stem | Pred segs | Extra pieces | max \|dStart\| | dStart per span (s) | max \|dEnd\| (diagnostic) |
|---|---|---|---|---|---|
| ONNX MDX | 17 | 1 (intro leak 7.55–9.26) | **0.21** | 0.03, 0.02, 0.07, 0.01, 0.00, 0.01, 0.21, 0.08, 0.01, 0.20, 0.08 | 0.82 |
| c11 | 17 | 1 (intro leak 7.55–9.26) | **0.21** | identical to MDX | 0.82 |
| Demucs | 12 | 0 | **0.00** | all 0.00 | 0.00 |

The c11 stem reproduces the MDX stem's RMS-VAD segments exactly (same 17
segments to the 10 ms grid) — expected, since c11 reproduces the ORT
vocals to ~1 int16 LSB (stem corr 0.9675 vs Demucs, identical to the ORT
port's 0.9675). The two worst dStarts (0.21 s, 0.20 s) are the 66.40 and
104.29 spans; the 0.82 s dEnd is the known 66.40-span MDX extension,
diagnostic only (split/extension behaviour, same as c11_sep stage 4).
Demucs reproduces its own reference trivially (0.00), which is the
sanity check that the validator reads the ref file correctly.

## Bar B — separation: PASS (all three stems)

Method: 25 ms RMS envelope at 16 kHz mono (win=hop=400, non-overlapping).
Sung = inside ref segments 1–10; instrumental = outside all 12 ref segments
(bleed segments 11–12 excluded from both classes). Bar: non-overlapping
IQRs. n_frames: sung 4742, instrumental 1205.

| Stem | Sung median [IQR] | Instrumental median [IQR] | IQR gap (sung q25 − instr q75) | Ratio (sung medians) | Ratio (all-12, secondary) |
|---|---|---|---|---|---|
| ONNX MDX | 0.05712 [0.02074, 0.08633] | 0.000229 [0.000119, 0.000839] | 0.01990 | 248.9× | 242.7× |
| c11 | 0.05712 [0.02074, 0.08633] | 0.000229 [0.000119, 0.000839] | 0.01990 | 248.9× | 242.7× |
| Demucs | 0.06325 [0.02674, 0.09160] | 0.000315 [0.000054, 0.001634] | 0.02510 | 200.5× | 191.0× |

The separation is not marginal: on every stem the sung 25th percentile sits
**25× (MDX/c11) to 16× (Demucs) above** the instrumental 75th percentile.
The c11 and MDX envelopes agree to 5 decimal places (again the ~1 LSB
reproduction). The sprint-6 ratio statistic clears its ≥100× bar on every
stem under either mask choice. The stem-activity curve separates sung from
instrumental with enormous headroom — as a voice-activity curve it is not
borderline, it is decisive.

## Bar C — stay-rule application: FAIL (c11 judged; MDX identical)

Method (pre-stated): stem-envelope-at-snapped-position — the 25 ms RMS
envelope value in the frame containing each word's `snapped_start` in
`snap_mix_mv14.json` — for the 5 known snap errors (1-based idx 34, 56, 60,
112, 162) vs the 15 correct controls (loop-4 rule: |correction| ≤ 0.05 s,
prob ≥ 0.9, on_peak, first 15: idx 11, 17, 19, 26, 40, 58, 63, 64, 68, 73,
83, 85, 88, 91, 92). Bar: Mann-Whitney one-sided p < 0.05 AND errors
median < correct median. Judged on the c11 stem; ONNX stem reported
alongside (identical to 5 decimal places — same ~1 LSB reproduction).

| Stem | Errors median [IQR] | Controls median [IQR] | MW U (of 75) | p (one-sided, errors < controls) | Pass |
|---|---|---|---|---|---|
| c11 | 0.04909 [0.03353, 0.07060] | 0.07016 [0.04874, 0.08770] | 29 | **0.2486** | **NO** |
| ONNX MDX | 0.04909 [0.03353, 0.07060] | 0.07016 [0.04874, 0.08770] | 29 | **0.2486** | **NO** |

The median points the right way (errors lower) but the separation is
illusory: the IQRs overlap almost completely, and the Mann-Whitney U of
29/75 means the errors are lower than the controls in only 29 of 75
pairwise comparisons — **worse than chance (37.5 expected)**. The low
errors median is carried by a single point: idx 56 'Help' (env 0.0103),
a prob-0.013 word whose ASR itself is unreliable. The other four errors sit
squarely inside the controls' range (0.0335, 0.0491, 0.0706, 0.0921 — the
last, idx 162 'If', is ABOVE the controls' median). One control, idx 19
'you', sits at env 0.0001 — a correct snap at essentially zero stem
envelope (it lands just past the end of ref span 1, at a span boundary).
The statistic does not separate; p = 0.25 is not close to the bar.

### Why it fails (mechanism, same family as the loop-5 flux failure)

The snapper snaps TO peaks, and the stem envelope stays high across the
small displacements involved: the 5 errors are 0.048–0.144 s displacements
to nearby positions inside sung spans, where the voice is continuously
active. Envelope-at-a-point cannot tell a true onset from a position
0.05–0.14 s away when the whole neighbourhood is loud. Bar B's decisive
separation is sung-vs-instrumental (span scale); Bar C asks for
onset-vs-nearby-inside-a-sung-span (sub-span scale), and at that scale the
envelope has no contrast. This is the same structural reason vocal-flux
failed in loop 5 (errors sit near peaks too) — the stay-rule's in-span
evidence cannot be a point value of a curve that is high everywhere in
the span.

### Diagnostic: distance to nearest stem-envelope rising edge (NOT a bar)

Pre-stated diagnostic for loop 7, in case Bar C failed: is the rising edge
the better statistic? Answer: **no, not on this evidence.**

| Statistic | Errors median | Controls median | MW one-sided p |
|---|---|---|---|
| Signed dist to nearest rising edge (edge − snapped) | +0.145 s | +0.047 s | 0.277 (errors > controls) |
| \|Dist\| to nearest rising edge | 0.368 s | 0.190 s | 0.368 (errors > controls) |
| Envelope / local ±1 s median (normalised) | 1.936 | 1.216 | 0.778 (errors < controls) |

The rising-edge distance points the right way (errors farther from an
edge: 0.368 s vs 0.190 s median |distance|) but with n=5 vs 15 it is nowhere
near significance (p = 0.37). The locally-normalised envelope is actively
worse than the raw value (p = 0.78 — errors sit HIGHER than controls after
local normalisation). Neither statistic rescues the stay-rule application.
Loop 7 should not re-test these two statistics on MV-14 hoping for a
different answer; if the stay-rule is revisited, it needs a different
signal class (e.g. an onset detector with sub-span resolution, or a
different error set with more than 5 errors), not a re-thresholding of
this envelope.

## What this means for loop 7

- **Mouth-open-vs-quiet gate (loop 1 #3) and CCA AV-sync (loop 2 #3):** may
  calibrate on the stem-activity curve. Bar B gives them a sensor with
  16–25× IQR headroom; Bar A gives them boundaries within 0.21 s of the
  Demucs reference. The curve artifact is delivered below for exactly this.
- **Snapper stay-rule patch:** has no sensor. All five in-span candidates
  tried across loops 4–6 are dead on MV-14 (c11_voice curve, vibrato depth,
  spectral entropy, vocal-flux both flavours, stem-envelope-at-snapped).
  Loop 7 records that plainly; the stay-rule stays unbuilt unless a new
  signal class is proposed. The snapper's error mode (small displacements
  to nearby peaks inside loud spans) is now characterised twice over
  (flux, stem envelope) and should shape whatever comes next.
- **The c11 stem is a production sensor source:** c11 reproduces the MDX
  stem's activity curve to 5 decimal places on every statistic run here,
  at 840.4 s vs the ORT port's 1,592 s. Loop 7's gate calibrations can run
  on the c11 stem (the artifact below is the c11 curve).

## MV-11 generalisation leg — COMPLETE: Bar A stem-to-stem FAILS

Status: **complete, FAIL.** The c11 stem was produced (run 1 SIGTERM'd by a
VM reboot at 26/40 chunks; resumed the same command — 14 written + 26
skipped — 40/40 dumped, assembled via `assemble_chunks.py`) and scored
against the Demucs stem (`mdx_stemact/mv11/mv11_score.json`).

| Measure | MV-11 | MV-14 (for comparison) |
|---|---|---|
| Stem corr vs Demucs (mono) | **0.8466** | 0.9675 |
| Bar A stem-to-stem max \|dStart\| | **1.71 s** (bar 0.5 s) | 0.21 s |
| Demucs ref spans / matched / within bar | 11 / 9 / 7 | 11 / 11 / 11 |
| Spans outside the bar | 0.63 s, 1.71 s | none |
| Spans unmatched by the metric | 2 | 0 |
| max \|dEnd\| (diagnostic) | 7.89 s | 0.82 s |
| Bar-B-style IQR separation (both stems) | non-overlapping (c11 ratio 139.6×, Demucs 70.1×) | non-overlapping |

The full accounting on the 11 Demucs spans: 7 within ±0.5 s, 2 outside
(0.63 s on the 45.43 span, 1.71 s on the 69.27 span), 2 unmatched — the
span-start metric silently skips spans with no c11 piece starting inside
them (inherited flaw in `match_boundaries`, also present in the MV-14
scoring, where it never triggered). The unmatched spans: [55.14, 65.68],
whose c11 piece starts 1.8 s early (53.34, outside the 1.0 s early-start
window), and [17.71, 24.77], covered by a c11 piece that started in the
previous span (the c11 stem merges 14.14–24.76 across the 0.84 s gap, the
Demucs stem splits it).

Mechanism (checked on the 25 ms envelopes, not assumed): the Demucs stem
carries substantially more low-level brass bleed than the c11/MDX stem,
and the bleed crosses the 0.1 × p99 RMS-VAD threshold. Worst span: the
Demucs segment starts at 69.27 on bleed blips (env 0.005–0.032 across
68.5–71.0 s) while BOTH stems agree the true voice onset is ~71.5 s
(env 0.077 c11 / 0.081 Demucs at 71.50 s). Same pattern at 53.75/55.50
(Demucs blips 0.04 where c11 is quiet until the shared onset at 55.75)
and at 45.75–46.00 (Demucs 0.02–0.07, c11 quiet until 46.25). The c11
stem is the cleaner of the two on this track (gap envelope ~10× lower:
instrumental median 0.000229 vs 0.000806; ratio 139.6× vs 70.1× — the
Demucs stem itself is below the 100× bar on MV-11).

Consequence, stated plainly: **the MV-14 validation does not generalise
to MV-11 at the ±0.5 s bar.** On a brass-driven chant track the two
separators' RMS-VAD boundaries disagree by up to 1.71 s, driven by
Demucs-stem bleed triggering early segment starts — the reference is the
noisy party here, not (only) the c11 stem. Two implications for loop 7:
(1) stem-activity boundaries are separator-dependent where bleed crosses
the VAD threshold — gate calibrations should use the c11 stem's own
boundaries (the cleaner stem on this evidence), not Demucs', and a
bleed-aware threshold (or a higher thr_frac) is worth testing before any
gate trusts a boundary to ±0.5 s on a new track; (2) the span-start
metric must count unmatched spans as failures, not skip them — the
current `match_boundaries` understates disagreement whenever a pred
piece starts outside the 1.0 s window or in the previous span. The MV-14
verdict stands (its spans were all matched); the MV-11 leg bounds its
generality.

## Files

`detection-research/mdx_stemact/`:
- `mdx_stemact_validation.json` — combined validation record (calibration,
  Bars A/B/C, verdict).
- `stem_mdx_validation.json` — per-stem Bars A+B + calibration (MDX).
- `stem_c11_validation.json` — per-stem Bars A+B (c11).
- `stem_demucs_validation.json` — per-stem Bars A+B (Demucs, self-check).
- `bar_c.json` — Bar C per-stem (errors/controls detail, MW, rising-edge
  diagnostic, normalised-envelope diagnostic).
- `stem_activity_curve.py` — reusable recipe: stem wav → 25 ms RMS envelope
  (16 kHz mono) + RMS-VAD segments (verbatim recipe) → `.npz` + segments
  JSON. Loop 7 calibrates gates on its output without re-deriving it.
- `stem_activity_c11_mv14.npz` / `stem_activity_mdx_mv14.npz` /
  `stem_activity_demucs_mv14.npz` — the stem-activity curves for MV-14
  (t, env25ms, segments, thr_p99; 6464 frames each).
- `stem_activity_*_mv14_segments.json` — RMS-VAD segments per stem.
- `validate_stemact.py` — the bar runner (calibration + Bars A/B/C).
- `stem_activity_c11_mv11.npz` / `stem_activity_demucs_mv11.npz` (+
  segments JSONs) — the MV-11 stem-activity curves (6896 frames each).
- `mv11/` — MV-11 leg: mix wav, 40 chunk dumps, run logs (run 1 killed
  by reboot at 26/40; run 2 completed 40/40), assembled c11 stem +
  instrumental, `mv11_score.py` + `mv11_score.json` (Bar A stem-to-stem
  FAIL: max |dStart| 1.71 s), `README.md` (resume/scoring notes).

## What this sprint did NOT do

- No gate built (stay-rule patch, mouth-open calibration, CCA are loop-7
  work once this passes — C failed, so the stay-rule stays unbuilt; the
  mouth-open/CCA calibrations may proceed on the delivered curve).
- No RMVPE vibrato arbiter, no G7/R5 builds, no c11_sep re-run, no TSM work.
- No bar lowered. No number hand-copied — every number above is read from
  the JSON files listed.
