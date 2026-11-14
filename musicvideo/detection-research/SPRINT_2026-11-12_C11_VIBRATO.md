# SPRINT 2026-11-12 — C11 vibrato signature (5–7 Hz F0 modulation)

**Sprint: c11_vibrato, loop 3 top-1.** Scope:
`research_notes/slopcannon-improvement-loop/loop-03/SPRINT_SCOPE.md`.
Loop 3 report: `research_notes/slopcannon-improvement-loop/loop-03/report.md` (§2 #1).
Tool: `detection-research/c11_vibrato/` (day-1 falsifier + controls + plot scripts only —
**no C gate was built**).
Validation: `detection-research/c11_vibrato/c11_vibrato_validation.json`
(machine-readable, all numbers below).
**Overall verdict: FAIL FAST — Bar E. The chant is straight-tone; vibrato
signature is dead as the vocal-activity sensor for MV-14. Do not build
c11_vibrato.**

## The one-paragraph version

Loop 3 ranked vibrato top-1 because it uses sprint 8's one proven mix
result (pYIN F0, corr 1.0000) and detects the voice's *wobble* instead of
its pitch. The scope built the falsifier into step 1: if the chant is
straight-tone, the depth is flat everywhere and the entry fails fast.
It is flat everywhere. On the mix F0 track the sung spans read **2.55
cents** median in the 4–8 Hz band; the isolated Demucs-stem voice itself
reads **2.68 cents** — the same null, so this is not a mix-dominance
artifact, it is the voice: MV-14's chant carries no vibrato. Classical
vibrato would read ~35 cents RMS; the 20-cent line is the straight-tone
boundary (Nix et al. 2016). Worse, the accompaniment carries *more*
4–8 Hz modulation than the voice (instrumental median 3.32c, wordless
outro 5.66c), so the feature is inverted on this track, not merely
absent. The sprint stopped at step 1, per Bar E. A null result here is a
result: it kills the entry in a day and routes loop 4 to CASA.

## Method

Per 10 ms frame (sprint 8's saved F0 tracks, 16,161 frames, 10 ms hop —
no F0 recomputation, no re-run of sprint 8's calibration):

- **Contours.** pYIN `f0_hz` (0 = unvoiced): log-F0 interpolated across
  unvoiced gaps; a frame is *trusted* only within 0.25 s of a voiced
  frame. Raw YIN `f0_yin` (continuous) as a secondary contour.
- **Depth.** Detrend: subtract a 0.51 s moving average (removes vibrato,
  keeps pitch drift) → 5-frame median (octave-spike kill) → re-detrend →
  Butterworth bandpass 4–8 Hz, order 4, zero-phase (`filtfilt`), contour
  fs 100 Hz → modulation depth = RMS of the bandpassed cents over a
  0.5 s sliding window, smoothed ~100 ms.
- **Classes.** Sung = ref segments 1–10 (`hpss_mv14_ref.json`, the same
  12-segment Demucs-RMS-VAD ref as sprint 8); instrumental = outside all
  ref segments; ref 11–12 (143.88–152.50, 155.21–159.53) kept separate —
  wordless-outro Demucs bleed, per sprint 8's caveat.
- **Controls (run before concluding anything).** (1) Synthetic: the
  pipeline must recover known vibrato. (2) Stem: the same measurement on
  the isolated Demucs vocal stem — if the stem shows vibrato the mix
  track is blind; if the stem is flat too, the chant is straight-tone.
  (3) Block PSD: Welch spectra on continuous sung/instrumental blocks
  (no zero-masking).

## Controls — the pipeline works, and the stem agrees with the mix

| Control | Result |
|---|---|
| Synthetic 6 Hz vibrato, ±50 cents | **35.16 cents** (expected 50/√2 = 35.36) |
| Synthetic 6 Hz vibrato, ±5 cents | **3.52 cents** (expected 3.54) |
| Synthetic straight tone | **0.00 cents** |
| Synthetic 3 Hz wobble, ±50 cents | **0.30 cents** (bandpass correctly rejects out-of-band wobble) |
| Synthetic 6 Hz ±50c + 10c noise | **33.65 cents** (robust to noise) |
| Stem pYIN, sung spans | **2.68 cents** median [IQR 0.83, 7.00] — same null as the mix |
| Stem pYIN, instrumental spans | **0.00 cents** (silent stem: no voice, no depth — sanity check passes) |
| Stem pYIN, bleed / outro | **0.00 / 0.00 cents** |

The pipeline recovers vibrato accurately when it exists, rejects
out-of-band wobble, and reads exactly zero where the stem is silent.
The null on the mix is a real null, not a broken measurement — and the
stem control rules out the mix-dominance explanation: the isolated
voice has no vibrato either.

## Day-1 results

| Measure | Mix pYIN | Stem pYIN |
|---|---|---|
| Sung median [IQR], cents | **2.55 [0.27, 6.66]** | **2.68 [0.83, 7.00]** |
| Instrumental median [IQR], cents | **3.32 [0.45, 10.36]** | **0.00 [0.00, 0.00]** |
| Ref 11–12 (bleed) median, cents | 3.06 | 0.00 |
| Wordless outro (≥128.20 s) median, cents | 5.66 | 0.00 |
| Trusted-frame coverage, sung / instr. | 51.8% / 44.5% | 37% / 24% |
| Sung frames > 20c / > 35c | 1.8% / 0.1% | 4.2% / 0.4% |
| Instrumental frames > 20c / > 35c | 5.9% / 2.4% | 0.0% / 0.0% |
| Sung p95 / p99, cents | 14.33 / 24.58 | 18.89 / 28.63 |
| Block-PSD peak, sung / instr. | 3.0 Hz / 4.0 Hz | 3.0 Hz / — (silent) |
| Per-segment sung medians (1–10), cents | 1.72, 2.39, 2.13, 0.08, 1.26, 5.76, 1.98, 3.22, 6.26, 5.13 | 1.15, 4.41, 2.47, —, 8.29, 7.10, 4.47, 2.27, 0.00, 0.00 |

No sung segment approaches classical vibrato: the highest sung-segment
median on either track is 8.29 cents (stem seg 5), still 2.4× below the
20-cent straight-tone boundary. The block PSD peaks at 3.0 Hz in sung
spans on both tracks — the dominant energy is slow drift/wobble below
the vibrato band, not a 5–7 Hz peak. On the mix, the instrumental spans
carry *more* 4–8 Hz power than the sung spans (block PSD 222.7 vs 52.0),
and the wordless outro's ref-12 segment reads 27.5 cents median — the
accompaniment's own pitch instability is the loudest thing in the band.

Plot: `c11_vibrato/day1_falsifier_plot.svg` — depth vs time, mix + stem
panels, ref segments shaded, 20c (straight-tone) and 35c (classical
±50c RMS) threshold lines. Both curves sit on the floor for the whole
track.

## Bars

| Bar | Requirement | Result | Verdict |
|---|---|---|---|
| A — Separation | Median depth sung > instrumental, non-overlapping IQRs, MIX F0 | Sung 2.55 [0.27, 6.66] vs instr. 3.32 [0.45, 10.36] — IQRs overlap, wrong direction | **FAIL** |
| B — Boundaries | ≥80% within ±0.5 s (≥16/20 clean ref) | Not reached — no gate built (Bar E stop) | **NOT RUN** |
| C — No contamination | No instrumental-only span exceeds the sung median depth | Instrumental 3.32 > sung 2.55; outro 5.66; instr. frac>20c 5.9% vs sung 1.8% | **FAIL** |
| D — Absence | Straight-tone/instrumental spans report below threshold | Moot — the detector cannot say "here" in the first place (sung depth ~2.6c everywhere) | **MOOT** |
| E — Fail fast | If step 1 fails fast, report FAIL FAST with the depth plot and stop | Step 1 failed on both tracks; plot written; no gate built | **PASS (method) / FAIL (entry)** |

## What this does not unblock

- **Snapper stay-rule patch:** still needs an in-span peak-evidence
  signal. Vibrato depth was the candidate; it is not available. The
  birdsong-entropy decision (loop 3 #9) is now the next candidate for
  that signal.
- **Mouth-open-vs-quiet gate calibration (loop 1 #3)** and **CCA AV-sync
  (loop 2 #3):** both were conditioned on the first sensor that passes
  the held bar. Neither is unblocked — they wait on the next sensor.
- **G7 wrong-lyric gate (loop 3 #5):** unaffected — it needs no audio
  feature (word-set overlap on ASR that already exists), and its
  validation is strengthened by the real MV-2 S04 t3 positive.

## Loop 4 seed (per SPRINT_SCOPE.md §8)

1. **Formant experiment (loop 3 #6) + birdsong-entropy decision
   (loop 3 #9) in parallel.** Entropy decides before any sprint; it is
   also the next candidate for the snapper stay-rule evidence.
2. **Scope the CASA correlogram experiment (loop 3 #2) as the next
   sprint.** Vibrato's failure was predicted to route here: the voice
   carries no periodic signature to detect on the mix, so the next
   sensor must *segregate* the scene rather than measure the mixture.
   The experiment-first bar stands (voice-lag peak separation on ≥80%
   of ref segments before any gate build).
3. **R8 voice-break/jitter/shimmer (loop 3 #3)** stays a test, not a
   rescue — its validity pre-check (Titze conditions) is now more
   likely to fail on the same straight-tone material, but the
   measurement is a day, not a sprint.
4. **R5 flow interpolation (loop 3 #4)** is unaffected — it routes
   around the vocal-activity gap in assembly, not through it.

## Honest limits

1. **MV-14 only.** One dense chant-funk track. A melodic track with
   sustained sung vowels could carry vibrato; nothing here says
   otherwise. The entry is dead *for MV-14's chant*, which is the
   material the sprint was scoped on.
2. **pYIN voiced coverage is sparse** (mix 51.8% of sung time trusted,
   stem 37%) — the Viterbi's voicing decision is strict, as sprint 8
   documented. The null does not hinge on coverage: per-segment
   medians, block PSDs, and tail fractions all agree, and the trusted
   frames number in the thousands per class.
3. **The 0.25 s trust radius is a choice.** A tighter radius would
   shrink coverage, not change the medians (the depth is flat
   everywhere — there is no region of high depth to miss).
4. **Raw YIN is not a fallback.** Its contour reads 270–430 cents RMS
   in the band on both tracks — octave jumps and estimator noise, not
   vibrato. Any sensor built on raw YIN F0 on this mix would be
   measuring the estimator.
5. **No C code was written.** The deliverable is the falsifier, not a
   gate. The `c11_vibrato/` directory holds the measurement scripts,
   the validation JSON, the plot, and this report — no binary, no
   `c11_vibrato.c`, by design (Bar E).

## Deliverables checklist

- [x] `detection-research/c11_vibrato/day1_falsifier.py` (measurement)
- [x] `detection-research/c11_vibrato/day1_controls.py` (synthetic + stem controls)
- [x] `detection-research/c11_vibrato/day1_plot.py` (SVG plot generator)
- [x] `detection-research/c11_vibrato/day1_falsifier.json` (numbers)
- [x] `detection-research/c11_vibrato/day1_controls.json` (control numbers)
- [x] `detection-research/c11_vibrato/c11_vibrato_validation.json` (bars + verdict)
- [x] `detection-research/c11_vibrato/day1_falsifier_plot.svg` (fail-fast plot)
- [x] This report (`detection-research/SPRINT_2026-11-12_C11_VIBRATO.md`)
- [x] `DETECTION_FINDERS.md` run-16 entry (below)
- [ ] Commit — parent owns (do NOT commit the `day1_depth_*.npy` curves:
      129 KB each, regenerable in seconds from the saved F0 tracks)
