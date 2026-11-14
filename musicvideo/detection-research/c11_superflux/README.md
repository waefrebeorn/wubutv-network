# c11_superflux — SuperFlux-family onset detection functions (C11)

Sprint C11_SUPERFLUX (2026-11-13) — taste/SLERM research top-1 sprint,
the stay-rule reopening named by Slopcannon improvement loop 6.
Full spec + verdict: `../SPRINT_2026-11-13_C11_SUPERFLUX.md`.

## Build

```
make            # gcc -std=c11 -O2 -Wall -Wextra, zero warnings
```

## Run

```
./c11_superflux <wav16k> <f0_track.txt> <harm.bin> <out_dir>
```

Inputs on MV-14: `../c11_mir/mv14_16k.wav`, `f0_track_mv14.txt`
(extracted from `../c11_voice/voice_mv14.json`: one `"<f0_hz> <voiced>"`
line per 10 ms pYIN frame), `../c11_mir/hpss_mv14_harm.bin`
(`c11_hpss --dump-harm` output: raw doubles, [frame][513], 1024/256).

## Outputs (in out_dir)

| file | ODF | grid |
|---|---|---|
| `odf_superflux_raw.txt` | SuperFlux = librosa `onset_strength(max_size=3)`: log-power mel (128 Slaney, dB ref 1.0, top_db 80), max filter 3 on the mel axis, rectified lag-1 diff, mean over bands, centre shift 3 | 2048/512 (32 ms) |
| `odf_complex_raw.txt` | Rectified complex-domain (Duxbury/Dixon): predicted phase from the two previous frames, `|X − X̂|` counted only where magnitude grows | 2048/512 |
| `odf_hpss_raw.txt` | Spectral flux over the HPSS harmonic magnitude spectrogram only | 1024/256 (16 ms) |
| `odf_f0gated_raw.txt` | Spectral flux restricted per frame to bins within one bin of a pYIN F0 harmonic; unvoiced frames = 0 | 1024/256 |
| `odf_flux_raw.txt` | Plain full-band spectral flux (c11_mir `onset_flux` verbatim) — Bar 3 baseline | 1024/256 |
| `summary.json` | grids, frame counts, duration | |

LEGO (user's own modules, copied not rewritten): WAV reader, FFT,
periodic Hann, centred framing, Slaney mel bank from
`../c11_mir/c11_mir.c` (mel bank parameterised by n_fft). HPSS harmonic
magnitudes and the pYIN F0 track are consumed as artifacts of
`c11_hpss` / `c11_voice`.

## Validation harnesses (detection-research venv python)

```
../venv/bin/python parity_check.py    # Bar 1: corr vs librosa onset_strength
../venv/bin/python bar_c_test.py      # Bar 2: the loop-6 Bar C fixture
../venv/bin/python onset_quality.py   # Bar 3: peak F vs the MV-14 word grid
```

Results land in `out/parity.json`, `out/bar_c_superflux.json`,
`out/onset_quality.json`. Verdict (2026-11-13): Bar 1 PASS
(corr 1.000000), Bar 2 FAIL on all ODFs (stay-rule sensor search
CLOSED on MV-14 per the pre-stated kill criteria), Bar 3 FAIL
(F@±50 ms 0.081 vs the 0.80 bar; the instrumental-FP clause passes,
30 vs 135). The tool is a faithful SuperFlux — the signal class, not
the build, is what failed.
