# c11_mir — C11 MIR core (libc + libm only)

Sprint 3 (2026-11-11) built the Ellis DP beat tracker; sprint 4
grew it into the MIR core — every audio feature the pipeline takes
from librosa/Essentia, in one dependency-free binary. SLERM (user
msg 214: re-create troublesome dependencies in C11 from scratch).
No Python, no weights, no third-party code. Single file, ~1000 lines.

## Build

```
make            # builds c11_mir and the beat_tracker alias (same source)
```

`gcc -std=c11 -O2 -Wall -Wextra`, zero warnings (gcc 13.3.0).

## Run

```
# decode any track to the format the tool reads (16 kHz mono s16 WAV):
ffmpeg -v error -y -i <track.mp4> -ac 1 -ar 16000 -sample_fmt s16 mv14_16k.wav

# beats mode (default; sprint-3 behaviour, unchanged):
./c11_mir mv14_16k.wav c11_mir_mv14.json [--floor 1.0] [--dump-flux flux.txt]

# features mode (all features + per-beat features + tempogram):
./c11_mir features mv14_16k.wav c11_mir_mv14_features.json --floor 1.0 \
    --dump-mag mag.bin --dump-tempogram tempogram.bin

# snap mode (sprint 5: word-time snapper — DP snap of ASR word onsets
# to the nearest strong onset under monotonicity):
./c11_mir snap mv14_16k.wav SONG_WORDS.json snap_vocal_mv14.json \
    --flux vocal --window 0.4 --lambda 2.0
```

`--flux mix|vocal` picks the onset envelope: `mix` is the full-band
flux, `vocal` restricts it to 300–3400 Hz (voice onsets first,
kick/hat bleed suppressed). `--window` is the snap radius in seconds
(default 0.4); `--lambda` is the time-vs-onset exchange rate
(default 2.0 — a word moves up to 0.5 s to reach a strong peak).
`SONG_WORDS.json` is `{"words": [{"word","start","end","prob"}]}`
(faster-whisper, no VAD). Output JSON carries per-word
`snapped_start`, `correction_s`, `on_peak`, `flux_at_snapped`,
`flux_at_asr`, `gap_asr`, `gap_snapped`, plus summary counts.
Word JSON is read with the LEGO'd libjson (slermes `lib/libjson`,
vendored as `json.c`/`json.h` — byte-identical to upstream plus a
2-line build fix; see SPRINT_2026-11-11_C11_SNAPPER.md).

`--floor FRAC` is the Step-0 onset-strength floor: drop DP beats
whose local flux peak (±1 frame) is below FRAC × median(flux).
Default 0 = off (sprint-3 behaviour, exact). 1.0 drops MV-14's
10 lattice beats, MV-13's 6, MV-12's 1 — grid agreement unchanged.

## What it does

Shared front end: STFT (periodic Hann, 1024/256, centred frames
like librosa.stft) -> magnitude spectrogram -> spectral-flux onset
envelope (positive magnitude diffs, normalised to max 1).

Beats: tempo by Pearson autocorrelation of the flux (BPM 60..200,
0.5 steps); grid phase maximising summed flux; Ellis (2007) DP beat
tracker on the flux (see SPRINT_2026-11-11_C11_BEAT.md).

Features (all librosa-defaulted, validated vs librosa 1.0.0):
- MFCC — 13 coeffs, mel 128 (Slaney norm), power_to_db ref=1.0
  (librosa's default; NOT ref=max — that only shifts MFCC[0]),
  top_db 80, DCT-II ortho.
- chroma — 12-class HPCP filterbank (tuning=0, ctroct 5.0,
  octwidth 2, base_c), L-inf column normalisation.
- RMS envelope — time-domain, frame 1024/256, centred.
- spectral centroid, rolloff (0.85) — magnitude spectrum.
- spectral contrast — 6 octave bands (quantile 0.02), dB,
  power_to_db peak − valley, top_db 80.
- per-beat band loudness — Essentia BeatsLoudness shape: spectrum
  energy per beat segment, whole + bands [20,150,400,3200,7000,22000]
  Hz, 10*log10, floored at 1e-12.
- per-beat RMS — sqrt(mean of frame RMS² over the beat segment).
- tempogram — 384-lag autocorrelation of the onset envelope
  (periodic Hann 384, hop 1, linear-ramp centre padding, FFT
  autocorrelation, L-inf normalisation per frame). Full matrix is
  dumped as float64 binary (--dump-tempogram); the JSON carries the
  mean tempogram per lag (384 values).

## Files

- `c11_mir.c` — the whole MIR core.
- `Makefile` — builds `c11_mir` and the `beat_tracker` alias.
- `c11_mir`, `beat_tracker` — compiled binaries (gcc 13.3.0, -O2).
- `mv14_16k.wav` — MV-14 track decoded to 16 kHz mono s16
  (from track.mp4 md5 f2226f24d846e3b31a9689189c2c4352).
- `c11_beat_mv14.json`, `c11_beat_comparison.json`, `flux.txt`,
  `compare_beats.py` — sprint-3 artifacts (flux.txt is the
  symmetric-Hann flux; current dumps use the periodic Hann).
- `compare_mir.py` — Step-3 validation harness (end-to-end +
  isolated-from-C-mag comparisons vs librosa).
- `c11_mir_validation.json` — validation numbers (ALL PASS).
- `compare_beats_mv13_mv12.py` — Step-0 validation (MV-13/MV-12
  DP beats vs measured grids + librosa).
- `c11_mir_mv13_mv12.json` — Step-0 numbers.

## Results (see SPRINT_2026-11-11_C11_MIR.md)

- Validation on MV-14: EVERY feature corr 1.000000 vs librosa
  end-to-end (bar was 0.999): MFCC max|diff| 0.0005, chroma 1.6e-6,
  RMS 5e-7, centroid 0.005 Hz, rolloff one bin (15.6 Hz, single
  threshold-crossing frame), contrast 5e-5 dB, tempogram 1.9e-4,
  per-beat loudness 5e-5 dB, per-beat RMS 6e-7. Isolated checks
  (librosa features computed FROM the C mag) agree to ~5e-7 —
  the feature math is exact; the end-to-end residuals are
  librosa's float32 + one-bin rolloff quantisation.
- Window: sprint 3 used the symmetric Hann; sprint 4 switched to
  the periodic Hann (librosa's convention). The DP beats are
  bit-identical on MV-14 and MV-12 under both windows, and differ
  by one frame on one beat out of 298 on MV-13 (181.792s ->
  181.776s). Flux vs scipy flux is now corr 1.000000 (was 0.999997).
- Step 0 floor: MV-13 298 -> 292 beats, MV-12 247 -> 246, MV-14
  247 -> 237, with no change in grid agreement.
- Step 0 tempo/phase: both tracks show the sprint-3 plateau —
  MV-13 AC flat 0.5094 across 95.0–97.0 BPM, MV-12 flat 0.7328
  across 129.0–131.5 BPM, so the reported BPM is a selection
  inside the plateau. DP vs measured grid: MV-13 median |off|
  0.138s (librosa 0.137s), MV-12 0.110s (librosa 0.110s) — the
  sprint-3 DP advantage does NOT generalise; on these two tracks
  the DP and librosa are equivalent, and both agree with each
  other far better than either agrees with the rigid global grid.
- Runtime: beats mode ~0.6s, features mode ~2.1s on the 161.6s
  MV-14 track (1.5 shared CPUs). Memory ~120 MB peak.

## Snap (sprint 5)

DP snap of ASR word onsets to the nearest strong flux onset
(tiered cost, monotonicity; see SPRINT_2026-11-11_C11_SNAPPER.md).
MV-14 (212 words, vocal flux, λ=2.0): 166 moved, median
|correction| 0.052 s, max 0.252 s; λ=2 is the knee; window
0.25/0.4/0.6 identical. Hand-check 24 words: 15 agree, 7
disagree, 2 ambiguous — errors are early snaps onto out-of-span
peaks when a word has no in-span strong peak (fix: "stay if no
in-span strong peak", follow-up). The 0.05 band-energy gap test
is miscalibrated (threshold at the median; wordless outro louder
in-band than sung V1) — calibrated at 0.01 the true gap move is
28 -> 2. Stem-flux comparison owed (sprint 6's stem in flight).
Runtime ~0.5 s.
