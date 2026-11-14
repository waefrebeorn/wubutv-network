# SPRINT 2026-11-13 — C11_SUPERFLUX (stay-rule sensor, second attempt with a new signal class)

**Decree:** Telegram msg 350 (2026-11-13 04:18 EST, taste/SLERM research
order) + the user's pick 2026-11-13 ~04:30 EST ("Both — edits plus
sprint 1"). **Brief:** `research_notes/taste-slerm-research-2026-11-13/
report.md` §2 A.1 + §5 Sprint 1. **Coordinator:** e0aaf8fe (this sprint).

**Why.** The snapper stay-rule has NO sensor. All five in-span
candidates tried across loops 4–6 are dead on MV-14 (c11_voice curve,
vibrato depth, spectral entropy, vocal-flux both flavours,
stem-envelope-at-snapped — MDX_STEMACT Bar C, MW p = 0.2486). Loop 6
named the only reopening: *"a NEW signal class (onset detector with
sub-span resolution, or a different error set)"*. This sprint built
that signal class — SuperFlux (Böck & Widmer, DAFx-13), rectified
complex-domain (Duxbury et al.; Dixon 2006), and harmonic-gated flux —
and ran it against the exact Bar C fixture.

## Bars (pre-stated in the brief, not moved)

1. **Parity:** C11 SuperFlux ODF vs librosa `onset_strength`
   (log-power mel + max filter) on the MV-14 mix, corr ≥ 0.999.
   Reference call fixed before building: librosa 1.0.0
   `onset_strength(y, sr=16000, max_size=3)`, all other args default
   (n_fft 2048, hop 512, 128 Slaney mels, `power_to_db` ref=1.0,
   top_db 80, lag 1, mean aggregation, centre shift 3 frames).
2. **Sensor (Bar C fixture, same shape as loop 6):** for each ODF —
   plain SuperFlux, complex-domain, harmonic-gated — three statistics
   (value at snapped position, max in snapped span, max in ASR span)
   on the 5 errors (idx 34, 56, 60, 112, 162 in `snap_mix_mv14.json`)
   vs the 15 controls (loop-4 rule, idx 11, 17, 19, 26, 40, 58, 63, 64,
   68, 73, 83, 85, 88, 91, 92): PASS = Mann-Whitney one-sided p < 0.05
   AND errors median < controls median on ≥1 statistic on ≥1 ODF.
3. **Onset quality:** peak-picked onsets vs the MV-14 word grid
   (±50 ms tolerance), F-measure ≥ 0.80, with strictly fewer false
   positives in instrumental spans than plain flux. Peak rule fixed
   before measuring: local maxima (strict left) of the max-normalised
   ODF at ≥ 0.20 — the snapper's existing strong-peak tier. Reference
   onsets: `SONG_WORDS.json` word starts (212) — the grid loops 4–6
   judged everything against; no separate hand-marked onset file
   exists in the tree. Instrumental spans: complement of the 12 Demucs
   ref sung segments (`hpss_mv14_ref.json`).

**Kill criteria (pre-stated, binding):** if Bar 2 fails on ALL THREE
ODFs, the stay-rule sensor search CLOSES on MV-14 with this error set.

## What was built

`c11_superflux/` — single-file C11 tool (libc + libm only,
`gcc -std=c11 -O2 -Wall -Wextra`, zero warnings) + Makefile + README.
LEGO from the user's own modules: WAV reader, FFT, periodic Hann,
centred framing and the Slaney mel bank copied from `c11_mir.c`
(sprint 4, librosa-validated; mel bank parameterised by n_fft — the
original hard-wires 1024); HPSS harmonic magnitudes consumed as the
`c11_hpss --dump-harm` artifact; pYIN F0 track consumed from
`c11_voice/voice_mv14.json`. New code: the SuperFlux max-filter/diff
chain, the rectified complex-domain predictor, the two gating schemes,
peak picking + all three validation harnesses (venv Python/scipy).

Five ODFs on MV-14 (`mv14_16k.wav`, 161.6 s), total compute 2.1 s:
SuperFlux + complex-domain on the librosa grid (2048/512, 5051
frames); HPSS-harmonic flux, F0-gated flux, plain mix flux on the
c11_mir grid (1024/256, 10101 frames). Harness sanity: the plain-flux
ODF reproduces the snapper's recorded per-word flux exactly
(idx 34: 0.35253 vs 0.3525 on file), and 88.7% of snapped positions
are picked peaks of it — the front end and the picker are faithful to
the world the fixture was built in.

## Bar 1 — Parity: **PASS**

| reference | corr | affine a / b | max \|resid\| after affine |
|---|---|---|---|
| librosa `onset_strength(max_size=3)` (judged) | **1.000000** (0.99999999999998) | 1.000000 / 4.7e-9 | 3.7e-6 |
| librosa `onset_strength(max_size=1)` (secondary) | 0.970208 | 0.706 / −0.320 | 3.45 |

The C11 SuperFlux is numerically identical to librosa's (max values
15.315590 vs 15.315593). The max_size=1 row matters: had the max
filter silently not engaged, the two rows would swap — they don't.
**The build is a faithful SuperFlux. What fails below is the signal
class, not the implementation.**

## Bar 2 — Sensor: **FAIL on all three ODFs (all nine judged statistics)**

Errors median vs controls median; MW one-sided p (errors < controls);
U of 75. PASS needs p < 0.05 AND errors median < controls median.

| ODF | statistic | errors med | controls med | U | p |
|---|---|---|---|---|---|
| superflux | at snapped | 0.0311 | 0.0132 | 47 | 0.8026 |
| superflux | max snapped span | 0.2707 | 0.2219 | 46 | 0.7777 |
| superflux | max ASR span | 0.2707 | 0.2219 | 45 | 0.7514 |
| complex | at snapped | 0.3482 | 0.3319 | 34 | 0.4000 |
| complex | max snapped span | 0.5534 | 0.5108 | 39 | 0.5670 |
| complex | max ASR span | 0.5534 | 0.5108 | 39 | 0.5670 |
| hpss harm-gated | at snapped | 0.1843 | 0.1645 | 41 | 0.6323 |
| hpss harm-gated | max snapped span | 0.4418 | 0.4241 | 38 | 0.5336 |
| hpss harm-gated | max ASR span | 0.5498 | 0.3917 | 47 | 0.8026 |
| f0-gated | at snapped | 0.0000 | 0.0000 | 30 | 0.1628 |
| f0-gated | max snapped span | 0.0155 | 0.0000 | 39 | 0.5740 |
| f0-gated | max ASR span | 0.1251 | 0.0000 | 48 | 0.8394 |
| flux (context, not judged) | at snapped | 0.2892 | 0.3153 | 31 | 0.3058 |
| flux (context) | max spans | 0.4633 | 0.4719 | 41 | 0.6323 |

No statistic on any ODF comes close. Worse than a null result: on the
headline ODF the effect points the **wrong way** — the errors sit on
*stronger* SuperFlux values than the controls (at-snapped medians
0.0311 vs 0.0132; U=47 of 75). The F0-gated max-ASR-span is the most
wrong-way row of all (errors 0.1251 vs controls 0.0000, p = 0.8394):
harmonic onset energy concentrates in the error words' ASR spans at
least as much as in the controls'.

**Mechanism (same family as loops 5/6, now sharper).** A snap error
is a position a flux-family function found attractive — the snapper
chose it *because* an onset function peaked nearby. Any statistic of
the form "onset strength at/near the snapped position" inherits that
selection bias: errors are guaranteed to sit on real, strong onsets
(the accompaniment's). The controls — correct snaps with ≤0.05 s
corrections — often sit a frame or two off the biggest peak, so their
at-position values run *lower*. Gating does not rescue it: the HPSS
harmonic spectrogram and the F0-harmonic mask both still carry the
accompaniment's harmonic content (brass bleed is harmonic too), and
the displacements (0.048–0.144 s) are smaller than the temporal
support of every ODF here (32 ms hop × dB smoothing for SuperFlux;
the gated fluxes inherit the same span overlap — at the 32 ms grid
the snapped-span and ASR-span maxima are literally the same frame on
most words, which is why those two rows repeat).

Two statistic-shape notes, for the record: (1) at the 32 ms grid,
max-in-snapped-span and max-in-ASR-span are near-duplicates (the
≤0.144 s shift rarely changes the max); they separate on the 16 ms
grid and fail there too. (2) The F0-gated at-snapped statistic is
degenerate (both medians 0.0 — the gate zeroes 8170 of 10101 frames);
its span statistics are the meaningful ones, and they fail in the
wrong direction.

## Bar 3 — Onset quality: **FAIL** (F clause; the FP clause passes)

Judged: SuperFlux, threshold 0.20, tolerance ±50 ms.

| | peaks | TP | FP | FN | precision | recall | F | FP in instrumental spans |
|---|---|---|---|---|---|---|---|---|
| superflux | 208 | 17 | 191 | 195 | 0.0817 | 0.0802 | **0.081** | **30** |
| flux (baseline) | 992 | 87 | 905 | 125 | 0.0877 | 0.4104 | 0.144 | 135 |

The FP clause passes decisively — SuperFlux fires 4.5× fewer
instrumental-span false positives than plain flux (30 vs 135) and
4.8× fewer peaks overall. It is a *conservative* function. But its
peaks do not land on word onsets, so the F clause fails by an order
of magnitude.

**Tolerance sensitivity (SuperFlux, thr 0.20):** F = 0.033 / 0.081 /
0.214 / 0.305 / 0.386 at ±25 / 50 / 100 / 150 / 200 ms. **Threshold
sensitivity (F at ±50 ms):** thr 0.10 → 499 peaks, F 0.166;
thr 0.15 → 317 peaks, F 0.110; thr 0.20 → 208 peaks, F 0.081;
thr 0.25/0.30 in `onset_quality.json`. No threshold/tolerance
combination approaches 0.80 — the failure is not a calibration miss.

**Displacement diagnostics (why).** Median distance from a word
start to the nearest SuperFlux peak: **0.206 s** (p90 0.696 s);
to the snapper's own snapped positions: 0.208 s. Signed offset
median −0.028 s — dispersion, not a constant lag, so no shift fixes
it. SuperFlux's peaks on this dense chant mix are section/accompani-
ment events, not word onsets. Part of the gap is the reference
itself: only 44.8% of ASR word starts lie within 50 ms of the
snapper's chosen onset (|correction| median 0.056 s, p90 0.140 s),
so ±50 ms against raw ASR starts is a hard test for any ODF — but
plain flux still scores 5× SuperFlux's recall under the identical
reference, so the F failure belongs to the function, not only to the
reference. (For contrast, the complex-domain ODF at thr 0.20 reaches
F 0.177 at ±50 ms and the HPSS-gated 0.139 — all far under the bar;
full tables in `onset_quality.json`.)

## Verdict

| Bar | Result |
|---|---|
| 1 — parity vs librosa | **PASS** (corr 1.000000) |
| 2 — stay-rule sensor (Bar C fixture) | **FAIL** — all three ODFs, all statistics |
| 3 — onset quality | **FAIL** — F 0.081 vs 0.80 bar (FP clause passes, 30 vs 135) |

**Stay-rule consequence, per the pre-stated kill criteria: Bar 2
failed on all three ODFs, so the stay-rule sensor search CLOSES on
MV-14 with this error set.** This was the reopening loop 6 named —
a new signal class with sub-span resolution — and it failed for a
structural reason (selection bias: snap errors sit on real onsets by
construction), not for lack of implementation fidelity (Bar 1 is
exact). The stay-rule patch stays unbuilt. Reopening now requires a
different error set (more than 5 errors — with n=5 vs 15, even a
real effect would struggle to reach p < 0.05) or a signal class
that is not an onset-strength function at all. **Do not re-test
another flux flavour, and do not re-run this fixture with moved
bars.**

What survives: `c11_superflux` is a librosa-exact SuperFlux in the
C11 kit (2.1 s for a 161.6 s track on the blade) — available wherever
a vibrato-suppressed ODF is wanted (onset grids, beat front ends),
and its measured conservatism in instrumental spans (30 vs 135 FPs)
is a real property a future gate may use. It is not a stay-rule
sensor, and it is not a word-onset picker on chant material.

## Honest limits

- n = 5 errors is the fixture loop 6 fixed; every candidate since
  loop 4 has been judged on it. The wrong-way direction of the
  SuperFlux rows (not merely their p-values) is the substantive
  result — a bigger error set would refine the estimate, not
  plausibly reverse the sign.
- Bar 3's reference is ASR word starts, not hand-marked onsets;
  §Bar 3 quantifies how much of the F gap that explains (some) and
  how much it doesn't (most).
- The F0 gate uses the mix pYIN track (`voice_mv14.json`, 10 ms
  hop); frames the mix track calls unvoiced contribute zero, which
  makes the at-position statistic degenerate (reported, not hidden).
- HPSS harmonic magnitudes are the c11_hpss artifact on the mix
  (median-filter HPSS, kernels 31×31) — brass bleed into the harmonic
  part is a known property of that separator on this track.

## Deliverables

- `c11_superflux/c11_superflux.c` + `Makefile` + `README.md` — the tool
- `c11_superflux/f0_track_mv14.txt` — pYIN track extract (input artifact)
- `c11_superflux/out/` — `odf_superflux_raw.txt`, `odf_complex_raw.txt`,
  `odf_hpss_raw.txt`, `odf_f0gated_raw.txt`, `odf_flux_raw.txt`,
  `summary.json`, `parity.json`, `bar_c_superflux.json`,
  `onset_quality.json`
- `c11_superflux/parity_check.py`, `bar_c_test.py`, `onset_quality.py`
  — the three harnesses (rerunnable)
- This report + a DETECTION_FINDERS.md run-log entry
- No commits (parent commits), no Telegram/Freeq posts, no video
  generation. Registry task: `c11-superflux`.
