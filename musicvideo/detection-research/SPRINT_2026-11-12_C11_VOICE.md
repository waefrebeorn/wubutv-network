# SPRINT 2026-11-12 — C11 voicing gate (YIN + pYIN + CPP + HNR)

**Sprint 8, loop 2 top-1.** Scope: `research_notes/slopcannon-improvement-loop/loop-02/SPRINT_SCOPE.md`.
Report: `detection-research/SPRINT_2026-11-12_C11_VOICE.md` (this file).
Tool: `detection-research/c11_voice/c11_voice.c` (+ Makefile, README.md).
Validation: `detection-research/c11_voice/c11_voice_validation.json` (machine-readable, all numbers below).
**Overall verdict: FAIL — bar 2 fails structurally (see below). Do not lower the bar.**

**Recovery note:** the first coordinator (d0cfc1bf) died in the VM reboot
(02:46:52 EST, interrupted 02:47:33 EST) with the tool built, both MV-14 runs done, and the calibration
sweep done, but no validation JSON, no report, and no FINDERS entry — and its
validation scripts did not survive on disk. This recovery coordinator
re-derived every number independently from the saved outputs (segment-builder
mirror verified exact, both runs re-executed byte-identical, pyin re-run
fresh) and completed the validation. Two prior-coordinator claims did NOT
reproduce and are corrected here: (a) the beat file's "stem best 15/24" —
the independent 150-combo sweep tops at 14/24; (b) the README's "raw YIN vs
librosa corr 1.0000 / 0.9997" — measured 0.9919 (mix) / 0.9495 (stem) on
librosa-voiced frames with the documented method. Both corrections are
recorded in the validation JSON.

## Method

Per 10 ms frame (1024-sample frame, 16 kHz, centred, zero-padded edges):

- **YIN** (de Cheveigné & Kawahara 2002): FFT autocorrelation, difference
  function, CMNDF, first trough below 0.1 else global minimum, parabolic
  interpolation. Outputs `f0_yin` and `voicing = 1 - CMNDF`.
- **pYIN** (Mauch & Dixon 2014, as implemented in librosa 1.0.0): trough
  candidates with a Beta(2, 18) threshold prior, Boltzmann(λ=2) rank prior,
  no-trough prob 0.01 on the global minimum, Viterbi over 962 states
  (481 voiced + 481 unvoiced bins, 0.1 semitone), triangle transition kernel
  (half-width 20 bins), switch prob 0.01, transition_min_prob 1e-4.
  Outputs `f0_hz` (0 when unvoiced) and `pyin_voiced`.
- **CPP** (Hillenbrand et al. 1994/1996): Hann-windowed FFT, log magnitude,
  IFFT cepstrum, peak prominence over quefrency 20–320 vs the least-squares
  regression line, 5-frame moving-average smoothing (CPPS).
- **HNR** (Boersma 1993): normalized autocorrelation at the YIN lag,
  parabolically interpolated, 10·log10(r/(1−r)), clamped to [−30, +30] dB.

**Gate:** a frame is voiced iff `voicing >= 0.7` AND `cpp >= 0.5` AND
`hnr >= 8.0` (calibrated defaults from a 150-combo sweep — see bar 2).
Boundaries come from the voiced series with the RMS-VAD post-processing
rules copied verbatim from `c11_mir/make_ref_segments.py` (merge gaps
< 1.0 s, drop < 0.5 s, split > 30 s at the minimum-voicing frame, pad 0.3 s).

## LEGO notes

- FFT / STFT / periodic Hann / WAV reader / JSON emission: lego'd from
  `c11_mir` (`c11_mir.c`, `json.c`/`json.h` — the sprint-5 vendored libjson).
- Viterbi/DP structure: the snapper's DP machinery, re-costed for YIN
  candidate probabilities (not a third Viterbi written from scratch).
- Reference segments: sprint 6's `hpss_mv14_ref.json` (12 Demucs-RMS-VAD
  segments) reused verbatim so the scores are comparable to HPSS.
- Validation-only Python used the detection-research venv (numpy/scipy/
  librosa 1.0.0 — already installed, nothing added).

## Validation table

| Bar | Requirement | Result | Verdict |
|---|---|---|---|
| 1 — YIN vs librosa.pyin | F0 corr ≥ 0.99, gross err ≤ 2%, mix + stem | Mix pYIN corr **1.0000**, gross **0.00%** (n=3077); stem pYIN corr **0.9675**, gross **2.75%** (n=1784). Raw YIN: mix 0.9919 / 0.52%, stem 0.9495 / 4.04% | **FAIL** (stem leg) |
| ★ 2 — Boundaries vs ref | ≥80% of starts AND ends within ±0.5 s | Mix best **8/24 (33.3%)**; stem best **14/24 (58.3%)** across all 150 threshold combos; 0 combos reach 80% on either | **FAIL — structural** |
| ★ 3 — Beat HPSS | Beat HPSS 12.5% / 8.3% on same ref | Mix 33.3% vs HPSS full-mix 8.3% (**4.0×**); stem 45.8% vs HPSS vocal-stem 12.5% (**3.7×**) | **PASS** |
| 4 — CPP/HNR separation | Median sung ≥ instrumental + 3 dB, CPP and HNR | CPP sung 0.851 vs instr. 0.883 (**−0.03 dB**); HNR +0.04 dB; voicing −0.006 | **FAIL** |
| 5 — Snapper cross-check | "No voicing in span" fires on all 5 early-snap errors | Literal **1/5**; <15%-voiced rule 4/5; veto control: gate unvoiced at snapped frame for **0/15 correct snaps and 0/5 errors alike** — zero discrimination | **FAIL** |
| 6 — Unsung-flag sanity | Unvoiced under ≥2 of 3 unsung spans | **3/3** (intro 1.8%, gap 0.0%, tag 0.0% voiced) | **PASS** |
| 7 — Performance | Full track < 10 s wall; peak RSS < 200 MB | Mix **59.1 s** wall, stem **54.0 s** wall (CPU user alone 16.3 s); RSS **98.5–98.6 MB** | **FAIL** (wall) / PASS (memory) |
| 8 — Build hygiene | Clean rebuild, zero warnings, byte-identical, selftest, ASan/UBSan clean | Rebuild zero warnings; sha256 `a6067bbf…` identical twice; selftest ALL PASS (sine 220.64 Hz, err 0.29%); ASan selftest + full-track run clean | **PASS** |

### Bar 1 detail — the stem failure is a voicing decision, not an estimator

Where C and librosa both say voiced, F0 agrees exactly (median relative
error 0.00% on both tracks). The stem gap is that the C Viterbi calls
**1825 frames voiced vs librosa's 7493** (overlap 1784) — the C voicing
decision is far stricter than librosa's, on the same candidate machinery.
The 49 stem gross-error frames cluster in short bursts (52.05–52.09,
67.25–67.28, 105.54–105.56 s): 21 are octave-up (2×) path divergences,
28 are other. Raw YIN alone is noisier on the stem (303 gross errors:
76 octave-up, 119 octave-down, 108 other) — pYIN's Viterbi fixes most of
it (303 → 49) but the voicing decision stays too strict. On the mix the
same machinery is exact (corr 1.0000, 0 gross errors), so this is a
calibration gap in the Viterbi's voiced/unvoiced balance, not a broken
estimator.

### Bar 2 detail — why it is structural, not calibration

- At defaults (0.7/0.5/8.0): mix starts 5/12, ends 3/12 (median |off|
  0.27 s / 0.23 s); stem starts 7/12, ends 4/12 (0.23 s / 0.15 s).
- The 150-combo sweep (voicing × CPP × HNR, segments rebuilt with an
  independent Python mirror verified EXACT against the C output, 33/33
  mix and 27/27 stem) peaks at 8/24 on the mix and 14/24 on the stem.
  **Zero of 150 combos reach 80% on either track.** No threshold
  rescues it. A pYIN-voiced-only segment run scores worse (6/24 mix).
- The error is recall, not precision: time-overlap precision is high
  (mix 0.914, stem 0.980) but recall is ~0.52–0.55. The gate fires on
  only 10–11% of frames and drops out mid-phrase — signed end offsets
  are mostly negative (gate ends early, worst −4.1 s mix), and the last
  two ref segments are missed by seconds. Ends are the weaker direction
  everywhere (mix best 3/12, stem best 5/12).
- Bar 4 explains it: on the dense MV-14 mix, **none of the four
  measures separates sung from instrumental at the frame level**
  (medians identical to within 0.04 dB). The gate's strict conjunction
  buys precision at the cost of recall; the measures themselves carry
  almost no vocal-vs-accompaniment signal on the mix. The HNR term
  does the (little) work there is — every sweep-top combo uses a high
  HNR bar — and CPP is inert (kept at 0.5 so it does not veto).
- Ref caveat (does not save the sprint): ref segments 11–12
  (143.88–152.50, 155.21–159.53) sit in the confirmed-wordless outro
  (last lyric word 128.20 s) — Demucs-stem RMS bleed, not singing. A
  perfect voicing gate tops out at 20/24 on this ref. Measured 8/24
  and 14/24 are far below that ceiling.

### Bar 5 detail — voicing presence is not a flux peak

The five hand-check errors (0-based indices 34, 56, 60, 112, 162 in
`snap_mix_l2.json`, the hand-checked run — the report's indices are
0-based; `snap_mix_mv14.json` differs from it at words [56] and [162]
in snapped value only): voiced frames inside the ASR span are 2/88,
0/14, 1/24, 7/50, and **15/16** ([162] 'you' is 94% voiced in-span —
it is sung, it just has no in-span flux peak; the snapper's failure is
about flux peaks, not voicing). Literal flag: 1/5. The rescue that
looked promising — vetoing snaps whose snapped position reads
unvoiced — dies on the control: the gate reads unvoiced at the
nearest snapped frame for 0/15 correct snaps and 0/5 error snaps
alike (±0.05 s windows do not separate them either). The gate is
unvoiced at essentially every word onset, right or wrong. **The
snapper stay-rule patch cannot be built on this curve.**

### Bar 6 detail

Spans (mix curve, pass = voiced fraction < 0.15): intro 0.00–14.14
(confirmed wordless lead-in) 1.8% voiced; gap 95.24–98.50 (wordless
gap before bridge) 0.0%; tag 153.50–153.60 ("We'll be right back."
ASR hallucination) 0.0%; supporting outro 128.20–161.60 (33.4 s
wordless ride-out) 10.8%. The unsung flag has a sensor — it is the
boundary job, not the unsung job, that fails.

### Bar 7 detail

Mix 59.09 s wall (frames 36.87 s, Viterbi 20.49 s), stem 54.03 s wall
(frames 29.49 s, Viterbi 23.67 s). Wall was measured under load (other
coordinators + pyin running), but CPU user time alone is 16.3 s on the
stem — above the 10 s bar regardless of load. The Viterbi (962 states
× 16161 frames) dominates after the frame front-end; the README's
Viterbi optimizations (predecessor skip, precomputed kernel logs,
compact observation lists) are already in. Peak RSS 98.5–98.6 MB
passes easily.

### Bar 8 detail

Clean rebuild under `-Wall -Wextra`, zero warnings; two consecutive
builds byte-identical (sha256
`a6067bbfa4e3b11e709bdce44ad9133af004a3ea5aa045c7fad24df46298e501`);
`--selftest` ALL PASS (220 Hz sine recovered at 220.64 Hz, 0.29%
error; noise burst and silence 0.000 voiced); ASan+UBSan build
selftest PASS and full MV-14 run exit 0 with no findings (208.4 s
wall under ASan, 33 segments — same count as the optimized build).

## Bugs found by validation (fixed in this tree, by the first coordinator)

- CMNDF denominator: the first build averaged d over [20, k] instead of
  [1, k] as librosa does. Fixed; raw YIN vs librosa improved to the
  numbers in bar 1 above.
- Viterbi predecessor skip: the first build skipped predecessors with
  `pv == 1` (the unvoiced half) instead of `pv == 0` (the sparse voiced
  half), crippling the Viterbi (a 220 Hz sine read 73 Hz). Fixed; the
  sine reads 220.64 Hz.
- Candidate cap: the first build kept at most 32 candidates per frame,
  silently dropping the highest-lag troughs on 12% of mix frames and 28%
  of stem frames. Cap removed (up to 301 = N_LAG).
- Segment builder: the first build merged inline during the run scan
  without advancing past the merged end, emitting the same long segment
  dozens of times. It now follows the reference's two-pass structure,
  and the C output matches an independent Python mirror exactly (33/33
  mix, 27/27 stem).

## Honest limits

1. **MV-14 only.** One dense chant-funk track. Sparse ballads,
   sustained vowels, and other tracks are untested; nothing here
   generalizes beyond MV-14 without re-validation.
2. **The reference is RMS energy, not voicing.** The 12 "hand-marked"
   segments are Demucs-RMS-VAD output reused verbatim; two of them are
   outro bleed (see bar 2). The boundary scores measure agreement with
   Demucs energy, not with heard singing.
3. **The gate is a high-precision, low-recall voice indicator, not a
   boundary detector.** What it calls voiced is almost always inside a
   sung span (precision 0.91–0.98 by time), but it misses ~half the
   sung time. Any downstream use must treat "voiced" as trustworthy
   and "unvoiced" as uninformative — the reverse of what the boundary
   job needs.
4. **Performance misses the bar 6× on wall.** The Viterbi is the cost;
   a faster gate would need a cheaper smoother (median-filtered YIN
   was scoped as the fallback and not built) or a pruned state space.
5. **The stem 16k wav is not on disk in the repo.** It was regenerated
   with `ffmpeg -i separation_mv14/mv14_44k_(Vocals)_htdemucs.wav -ar
   16000 -ac 1 -c:a pcm_s16le mv14_stem_16k.wav` (md5
   `43d83ae22fc3424533c25a896942a455`); the re-run reproduces the saved
   stem outputs exactly (0 frame diffs, bounds identical), as does the
   mix re-run. The wav itself lives in /tmp, not committed, per the
   no-wav rule.
6. **Validation scripts are working files, not deliverables.**
   `validate_bars2_6.py` + `bar1_pyin.py` sit in `c11_voice/`
   uncommitted; they document exactly how every number was produced.

## What it unblocks — and what it does not

- **Snapper stay-rule patch: NOT unblocked.** Bar 5 fails; the curve
  cannot flag "no in-span strong peak" (see bar 5 detail). The patch
  still needs an in-span peak-evidence signal — the snapper's own
  vocal-flux curve, or a future voicing curve that is actually
  sensitive at onsets.
- **Stem-flux blind check (sprint 5 follow-up): partially enabled.**
  The stem run (`voice_mv14_stem.json` / `voice_bounds_mv14_stem.json`)
  exists and reproduces exactly; the comparison itself is still owed.
- **Loop 1's MAR × vocal RMS gate: NOT unblocked as a boundary
  source.** The curve can serve only as a high-precision confirmation
  ("this span is definitely voiced"), never as the boundary detector.
- **Unsung flag (loop 1's #1): sensor EXISTS.** Bar 6 passes 3/3 —
  a lyric-sheet line with no voicing under it reads unvoiced. The flag
  can be built on the curve's "unvoiced" reading for long spans
  (intro/gap/outro scale), with the caveat that short-span readings
  are noisy (see bar 5's control).
- **Loop 3 seed: take the stall branch.** Per loop 2's loop-3 seed,
  since c11_voice stalls: re-examine the other half of the
  voice-science shelf (jitter/shimmer/voice-break measures) and the
  flow-interpolation rescue (1102 report §2). The wubu_synth
  meta-thread stands either way.

## Recommendation (per the scope's fail branch)

The failure is structural: on a dense mix, YIN-voicing/CPP/HNR do not
separate voice from accompaniment at the frame level, and no threshold
calibration rescues it (0/150 combos reach 80%). Next candidates, with
evidence:

1. **MDX-Net ONNX adopt-as-is** (wubuwizard run 14, already proven:
   full-track corr 0.9675 vs Demucs, 201× active/silent) — separation
   first, then boundary detection on the separated vocal, which is
   what Demucs RMS-VAD already does by construction. The C11
   separation runner is already scoped (bar <894 s).
2. **Birdsong spectral entropy** (loop 2's #2) — the classical
   candidate most likely to separate sung syllables from drum hits,
   which is exactly the confusion this gate suffers. Untested; a
   small experiment (entropy on the mix vs the stem) decides it
   before any sprint.
3. **Do not re-run this gate's calibration.** The sweep is exhausted;
   further tuning of these four measures on MV-14 is curve-fitting a
   failed separation.

## Deliverables checklist

- [x] `detection-research/c11_voice/c11_voice.c` (+ Makefile, README.md)
- [x] `detection-research/c11_voice/c11_voice_validation.json`
- [x] `detection-research/c11_voice/voice_mv14.json` +
      `voice_bounds_mv14.json` (mix) and `voice_mv14_stem.json` +
      `voice_bounds_mv14_stem.json` (vocal stem)
- [x] This report (`detection-research/SPRINT_2026-11-12_C11_VOICE.md`)
- [x] `DETECTION_FINDERS.md` run-15 entry (below)
- [ ] Commit — parent owns (do NOT commit the binary, any `.wav`
      outputs, or the Demucs stem)
