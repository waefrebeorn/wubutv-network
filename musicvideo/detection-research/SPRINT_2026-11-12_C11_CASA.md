# SPRINT_2026-11-12_C11_CASA — CASA correlogram voice-lag experiment (loop 4 top-1)

**Date:** 2026-11-12. **Coordinator:** 7899de53. **Verdict: FAIL FAST — step 1 fails on both bars with the correct voice-lag seed. No gate build. Loop 5 takes the adoption branch (MDX-Net ONNX as-is + c11_sep).**

**Progress log:** 05:25 EST — work dir created, v1 run (34 s): Bar A 0/22, Bar E 0.9554. 05:26 — re-run reproduces identically. 05:28 — seed audit: v1 seeded the bass, not the voice (see §1); v1 WITHDRAWN. 05:30 — v2 re-run with stem-derived seed: Bar A 0/22 FAIL, Bar E 0.5606 FAIL. 05:35 — plot + validation JSON written. 05:36 — this report.

## 0. The stall, in one paragraph

Sprint 8's voicing gate failed structural (8/24 mix boundaries), vibrato failed fast (straight-tone chant), formants failed (mix spectrum dominates, parameter-unstable), spectral entropy failed (no separation on either track). Every feature computed on the mixture inherits the accompaniment's dominance. CASA was the only classical family left — segregate the scene instead of measuring the mixture. Its experiment-first step asks: does the voice-lag peak in a per-frame autocorrelation (correlogram) separate sung from instrumental spans? It does not — on either bar, with a correct seed. **The classical sensor search is over.** Loop 5 takes the adoption branch.

## 1. The seed audit — v1 is withdrawn, and why it matters beyond this sprint

v1 (`step1_experiment.py`, archived as `step1_experiment_v1_seedmix.json`) seeded the voice lag from the mix pYIN Viterbi path (`voice_mv14.json` f0_hz), per the scope's "seed from pYIN's trough candidates" — but the saved track holds only the single Viterbi path, not the candidate list. The audit, measured directly from the saved JSONs:

| track | voiced frames | at fmin 50 Hz | at fmax 800 Hz | median F0 (voiced) | voiced frames in 125–350 Hz |
|---|---|---|---|---|---|
| mix `voice_mv14.json` | 3,101 | **2,525 (81%)** | 35 (1%) | **50.0 Hz** | 2.5% |
| stem `voice_mv14_stem.json` | 1,825 | 0 | **1,148 (63%)** | **800.0 Hz** | 34.3% |

The mix Viterbi path is pinned at the 50 Hz floor: it tracks the mix's dominant periodicity (the bass), not the voice. The stem Viterbi path is pinned at the 800 Hz ceiling: octave runaway (the voice's harmonics climb the Viterbi to the top bin; the distribution is bimodal — 626 frames in 125–350 Hz, nothing at 350–500 Hz, 1,148 at 725–800 Hz). **Neither saved pYIN track is a voice-F0 track.** Sprint 8's "validation" (mix corr 1.0000, stem corr 0.9675 vs librosa) correlates two implementations of the *same* algorithm — the C code faithfully reimplements librosa's pYIN, including its systematic bias on this material. It validates the implementation, not the pitch estimates.

Consequences:
- **v1 is withdrawn as a voice test.** Its τ_voice ≈ 320 samples (50 Hz) sat *outside* the vocal lag range [27, 200], so v1 measured a bass lag against the vocal range. Its numbers (Bar A 0/22, confusion 0.9554, stem Bar A 18/22) are correct measurements of the wrong lag and are superseded. (The v1 follow-up's octave analysis — at-octave only 0.1% of frames — is consistent with this: the top peak was never near the voice or its octave because the reference lag was the bass.)
- **Implication for the c11_vibrato sprint (FLAGGED, not re-litigated).** Its depth numbers (mix 2.55c, stem 2.68c) are measurements of these pinned contours: a contour pinned at a constant boundary value has ~0 modulation depth *by construction*. The stem leg is 63% pinned at 800 Hz. The "straight-tone" verdict therefore rests on a measurement whose F0 source cannot see the voice move. The vibrato sprint's *controls* (synthetic 6 Hz recovered at 35.16c vs 35.36 expected) validate the pipeline, not the tracks. Whether the chant is truly straight-tone needs a correct F0 source (the stem autocorrelation reference in §2 gives one: per-segment median F0 144–267 Hz — a proper vibrato re-measurement is a loop-5 decision, not this sprint's). This sprint does not overturn the vibrato verdict; it records that the verdict's F0 source is compromised and the question is open.

## 2. v2 method — the correct seed

Voice lag seeded **empirically from the isolated Demucs vocal stem**: τ_voice(t) = the stem autocorrelation's top peak in the vocal lag range [27, 200] (80–600 Hz), 11-frame median smoothed (110 ms), trusted only where the stem frame has RMS > 1% of max AND stem r_max > 0.2. The stem IS the voice isolated; its dominant in-range periodicity is the voice (plus small Demucs bleed). The mix is then tested for a peak at THAT lag during sung spans. 10,659 trusted sung frames (vs v1's 6,137 pYIN-voiced frames — the stem-energy trust gate covers more of the sung spans).

Per-frame FFT autocorrelation, same framing as sprint 8 (1024 Hann / 160 hop / centred zero-pad, 16,161 frames). Vocal range τ [27, 200]; wide-range sensitivity τ [20, 320] (50–800 Hz). Dominance is **octave-aware from the start**: the mix top peak counts as voice-consistent at τ_voice (±2), 2τ_voice (±4), or τ_voice/2 (±2). Spans: sung 1–10; bleed 11–12 (instrumental-class, reported separately); instrumental = complement of the union of all 12 ref segments (12 spans). Clean spans 22, total with bleed 24. Bar A pass ≥ 18/22; Bar E pass = confusion ≤ 20%.

**Stem stability check** (is the voice's lag stable enough to be a reference at all?): raw stem top peak within ±2 of the smoothed reference on **73.0%** of trusted sung frames; at the octave on 2.4%. Reference F0: median **238.8 Hz**, IQR [177.8, 290.9]; per-segment medians 144.1–266.7 Hz (segs 1, 4, 5 low ~145 Hz; segs 2, 3, 6, 7, 8 ~235–267 Hz — the chant moves pitch by phrase, which the per-frame smoothed reference tracks). The seed is a real, moving voice. The remaining 27% of frames where the stem's top peak jumps away from its smoothed reference are other harmonics, Demucs bleed, or pitch moving faster than the 110 ms median filter — the voice's own lag is only moderately stable, which already caps what any lag-based sensor can do.

## 3. Results — v2 (correct seed)

### Bar A: 0/22 FAIL

| | pooled median |
|---|---|
| sung r_voice (at stem-derived voice lag) | **0.2534** |
| instrumental r_max (top in-range peak) | **0.5049** |

Mann-Whitney sung r_voice > instrumental r_max: **p = 1.0** — the distributions are inverted, not overlapping: the voice-lag peak on sung frames is stochastically *smaller* than the accompaniment's peak on instrumental frames. Not a single span separates, on either side:

- Sung spans (median r_voice): 0.087–0.355 — best sung-6 0.3546, worst sung-3 0.0869; every one below the pooled instrumental 0.5049.
- Instrumental spans (median r_max): 0.280–0.640 — quietest instr-3 0.2802, loudest instr-12 0.6397; every one above the pooled sung 0.2534.
- Bleed spans (instrumental-class): 0.5492, 0.4591 — also above; including bleed, Bar A is 0/24.

Widening the lag range does not help: wide-range (50–800 Hz) pooled sung r_max 0.5668 vs instrumental 0.5286 — the top peak is the accompaniment's everywhere, on both classes.

### Bar E (multipitch confusion, octave-aware): 0.5606 FAIL (bar ≤ 0.20)

τ_max breakdown on the 10,659 trusted sung frames:

| mix top peak at | fraction |
|---|---|
| voice lag (±2) | 0.339 |
| voice octave (2τ) | 0.048 |
| voice half (τ/2) | 0.052 |
| bass range (τ 145–200) | 0.097 |
| other | **0.464** |

The mix's top peak is at the voice lag only a third of the time; 46% of the time it is at some other lag entirely — scattered across brass harmonics, drum periodicity, and cross-terms, not consistently any one competitor (the bass range accounts for only 9.7%). Median r_voice 0.2534 vs median r_second (strongest non-voice peak) 0.4611 vs median r_max 0.5079; r_voice > r_second on only **32.0%** of sung frames. The voice-lag peak is ~1.8× weaker than the strongest competing peak, on average.

### Controls (reproduce identically to v1 — pipeline validated)

| control | r at voice lag (220 Hz) | r_max vocal range | τ_max median |
|---|---|---|---|
| voice-only 220 Hz | 0.9656 | 0.9656 | 73 (= 16000/220) ✓ |
| mixture 220 + 98 + 147 Hz | **0.0573** | 0.3352 | 146 (= 2×73, voice octave) |
| accompaniment-only 98 + 147 Hz | −0.4326 | 0.3581 | 109 (= 147 Hz brass) |

The synthetic mixture control shows the mechanism exactly: three equal-amplitude tones already bury the voice lag (0.057) below the mixture's top peak (0.335), and the top peak lands on the voice's *octave* — which the octave-aware rule correctly credits, but the real mix's top peak is scattered far beyond octaves.

## 4. Why it fails — the mechanism

The correlogram does segregate periodicities in principle (each source contributes peaks at its own lag). What fails is the *decision*: the voice's peak is not the strongest, and its strength (0.25) sits below the accompaniment's peak even when the voice is absent (0.50). No threshold on r_voice separates the classes — the pooled medians are 2× apart in the wrong direction, and at span level the best sung span (0.355) barely clears the quietest instrumental span (0.280) while 7 of 10 sung spans sit below it. Two compounding causes:

1. **Accompaniment dominance in the autocorrelation.** The mix's strongest in-range periodicity is almost never the voice: bass, brass, and their harmonics and cross-terms out-peak it 2:1 on the median sung frame.
2. **The voice's own lag is only moderately stable.** Even on the isolated stem, the top peak jumps away from its smoothed reference on 27% of frames — a lag-based sensor inherits that instability before the mixture even enters.

Harmonic grouping (step 2 of the scope) cannot rescue this: grouping assumes the voice's harmonic series is identifiable in the correlogram, but the voice's *fundamental-lag peak itself* is not the top peak on 56% of sung frames and is weaker than the strongest competing peak on 68%. There is no reliable anchor to group around. Step 2 is not attempted — the experiment-first rule stops here.

## 5. What this unblocks / fail-fast routing

- **No gate build.** The held bar (≥80% of boundaries within ±0.5 s) is never reached; the mouth-open-vs-quiet gate, CCA AV-sync on the CASA curve, and snapper stay-rule evidence from CASA voice-stream activity all stay blocked — there is no CASA curve to calibrate on.
- **Loop 5 takes the adoption branch** (per the sprint scope): MDX-Net ONNX as-is + c11_sep. The classical sensor search is over: voicing (sprint 8), vibrato, formants, spectral entropy, and now CASA have all failed on the mix. The adoption branch is the only remaining route to a voice-activity sensor.
- **Snapper stay-rule evidence:** CASA cannot supply it. Remaining candidates: the snapper's own vocal-flux curve, or a sensor from the adoption branch (MDX-Net stem activity). The stem-flux blind check is still owed.
- **Standing finding for the program:** sprint 8's saved pYIN tracks (`voice_mv14.json`, `voice_mv14_stem.json`) are NOT voice-F0 tracks — mix pinned at the 50 Hz floor (81% of voiced frames), stem pinned at the 800 Hz ceiling (63%). Any downstream use of their f0_hz as "the voice's F0" is wrong, including the vibrato sprint's mix and stem legs (§1). The stem-autocorrelation reference (median F0 239 Hz, phrase-dependent 144–267 Hz) is the correct voice-F0 source on this material, and it is saved in `step1_curves.npz` (tau_ref) for any loop-5 re-measurement.

## 6. Files (all numbers from disk; no number without a source)

- `c11_casa/step1_experiment_v2.py` — v2 experiment (correct seed)
- `c11_casa/step1_experiment.py` — v1 (superseded seed; archived results in `step1_experiment_v1_seedmix.json` + `step1_curves_v1_seedmix.npz`)
- `c11_casa/step1_experiment.json` — v2 numbers (Bar A 0/22, Bar E 0.5606, seed audit, stem stability, controls, per-span table)
- `c11_casa/step1_curves.npz` — v2 per-frame curves (mix_r_voice, mix_r_max, mix_r_second, mix_dominance, mix_tau_max, tau_ref, trusted, stem_r_max, stem_tau_raw)
- `c11_casa/step1_plot.svg` — r_voice vs r_max across the track + stem reference F0
- `c11_casa/step1_plot.py` — plot script (hand-rolled SVG)
- `c11_casa/c11_casa_validation.json` — validation JSON, md5 `3cb98c1ff34fa881e8016f0c5e81f79b`
- `c11_casa/step1_experiment_v1_seedmix.json` — v1 numbers (WITHDRAWN as a voice test; kept for the audit trail)

Inputs (unchanged from sprint 8): `c11_mir/hpss_mv14_ref.json` (12 segments); `c11_mir/mv14_16k.wav`; `/tmp/mv14_stem_16k.wav` (md5 `43d83ae22fc3424533c25a896942a455`); `c11_voice/voice_mv14.json`, `c11_voice/voice_mv14_stem.json`. No commits made (parent owns commits). No video generation, no Telegram.
