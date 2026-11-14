# c11_voice — C11 voicing gate (YIN + pYIN + CPP + HNR)

Sprint 8 (loop 2 top-1). Replaces the sprint-6 HPSS boundary gate, which
failed structurally (12.5% starts / 8.3% ends vs the 80% bar): harmonic
energy is not vocal energy. This tool measures voicing itself.

## Method

Per 10 ms frame (1024-sample frame, 16 kHz, centred, zero-padded edges):

- **YIN** (de Cheveigné & Kawahara 2002): FFT autocorrelation, difference
  function, CMNDF, first trough below 0.1 else global minimum, parabolic
  interpolation. Outputs `f0_yin` and `voicing = 1 - CMNDF`.
- **pYIN** (Mauch & Dixon 2014, as implemented in librosa 1.0.0): trough
  candidates with a Beta(2, 18) threshold prior, Boltzmann(λ=2) rank
  prior, no-trough prob 0.01 on the global minimum, Viterbi over 962
  states (481 voiced + 481 unvoiced bins, 0.1 semitone), triangle
  transition kernel (half-width 20 bins), switch prob 0.01,
  transition_min_prob 1e-4. Outputs `f0_hz` (0 when unvoiced) and
  `pyin_voiced`.
- **CPP** (Hillenbrand et al. 1994/1996): Hann-windowed FFT, log magnitude,
  IFFT cepstrum, peak prominence over quefrency 20–320 vs the least-squares
  regression line, 5-frame moving-average smoothing (CPPS).
- **HNR** (Boersma 1993): normalized autocorrelation at the YIN lag,
  parabolically interpolated, 10·log10(r/(1−r)), clamped to [−30, +30] dB.

**Gate:** a frame is voiced iff `voicing >= 0.5` AND `cpp >= --cpp-thr`
AND `hnr >= --hnr-thr`. Boundaries come from the voiced series with the
RMS-VAD post-processing rules copied verbatim from
`c11_mir/make_ref_segments.py` (merge gaps < 1.0 s, drop < 0.5 s, split
> 30 s at the minimum-voicing frame, pad 0.3 s).

## Build

```
make            # gcc -std=c11 -O2 -Wall -Wextra, zero warnings
make test       # --selftest: 220 Hz sine + noise burst + silence
make asan       # ASan/UBSan build + selftest
```

libc + libm only. Single file + the vendored libjson from `c11_mir/json.c`.

## Usage

```
c11_voice <wav> <curve.json> <bounds.json>
    [--cpp-thr X] [--hnr-thr X] [--voicing-thr X] [--selftest]
```

Input must be 16 kHz mono 16-bit PCM WAV:

```
ffmpeg -i track.mp4 -ar 16000 -ac 1 -c:a pcm_s16le track_16k.wav
```

`curve.json` carries one object per frame (`t`, `f0_hz`, `f0_yin`,
`voicing`, `cpp_db`, `hnr_db`, `voiced`, `pyin_voiced`, `voiced_prob`).
`bounds.json` carries the voiced segments (`start`, `end`, `confidence`).

Calibrated defaults are baked in (see the sprint report for the sweep);
override with the `--*-thr` flags for experiments.

## Deviations from librosa (deliberate, documented)

- Frame 1024 (not librosa's default 2048): the 2048 FFT pair for the
  autocorrelation + the 1024 FFT pair for the cepstrum + the Viterbi
  cannot fit the <10 s wall on this blade at frame 2048. Validation
  compares against `librosa.pyin` called with the same
  `frame_length=1024`, so the comparison stays apples-to-apples.
- librosa clips a candidate pitch-bin index to `n_pitch_bins` (481),
  which writes a slightly-above-fmax candidate into the first UNVOICED
  row of the observation matrix. This tool clips to 480, so voiced mass
  stays in the top voiced bin.
- HNR is computed from the UNwindowed autocorrelation (the YIN front-end
  is unwindowed by design). Boersma's windowed version would need a
  separate windowed autocorrelation; the window correction is omitted,
  not silently applied.
- The difference function d(k) is clamped to >= 0 (mathematically a sum
  of squares; a negative value is float noise only).
- The >30 s split uses the minimum of the voicing-strength curve as the
  "quietest point" analogue of `make_ref_segments.py`'s RMS minimum.
- `f0_hz` is 0.0 on unvoiced frames (librosa leaves the bin frequency
  unless `fill_na` is set); validation compares on voiced frames only.

## Performance notes

- The Viterbi skips voiced-half predecessors with no candidate (the
  voiced half is sparse; the unvoiced half is dense and never skipped).
  This is exact: a finite predecessor always exists within the band.
  The transition-kernel logarithms are precomputed per lag (calling
  `log()` per predecessor cost 33 s on the first build).
- The observation log-probs are built per frame from the compact
  candidate lists instead of storing the full T x 962 log matrix
  (which would cost 124 MB); peak RSS is ~100 MB.

## Bugs found by validation (fixed in this tree)

- CMNDF denominator: the first build averaged d over the sliced range
  [20, k] instead of [1, k] as librosa does. The distorted troughs
  broke YIN-vs-librosa parity. Fixed; raw YIN vs librosa.pyin
  (frame_length=1024, librosa-voiced frames) now measures corr 0.9919
  mix / 0.9495 stem (pYIN f0_hz: 1.0000 / 0.9675 — see the sprint
  report; the earlier "1.0000 / 0.9997" claim did not reproduce).
- Viterbi predecessor skip: the first build skipped predecessors with
  `pv == 1` (the UNVOICED half) instead of `pv == 0` (the sparse
  voiced half), crippling the Viterbi (a 220 Hz sine read 73 Hz).
  Fixed; the sine reads 220.64 Hz.
- Candidate cap: the first build kept at most 32 candidates per frame,
  silently dropping the highest-lag troughs on 12% of mix frames and
  28% of stem frames. The cap is removed (up to 301 = N_LAG).
- Segment builder: the first build merged inline during the run scan
  without advancing the scan position past the merged end, emitting
  the same long segment dozens of times with different starts. It now
  follows the reference's two-pass structure (runs -> merge -> drop ->
  split), and the C output matches an independent Python mirror
  exactly (33/33 mix, 27/27 stem segments).

## Files

- `c11_voice.c` — the tool
- `Makefile`, `README.md` — this file
- `voice_mv14.json`, `voice_bounds_mv14.json` — MV-14 mix run (see the
  sprint report; the vocal-stem run is `voice_mv14_stem.json` /
  `voice_bounds_mv14_stem.json`)
- `c11_voice_validation.json` — all validation numbers, machine-readable
