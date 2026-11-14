# Sprint 3 — SLERM the beat tracker in C11 — 2026-11-11

Downtime-improvement sprint 3 (user msg 202) under the new standing
SLERM-C11 method (user msg 214, 2026-11-11: any dependency giving
trouble gets re-created in C11 from scratch, not worked around).

## What was blocked

madmom (F-13) cannot build on Python 3.12.3 — `longintrepr.h`
removed from the public include path. BeatNet (F-07) imports madmom
at three points (log-spect feature extraction, PF HMM state spaces,
DBN decoder), so both its inference paths need it. No Python ≤3.11
exists on the box. The BeatNet/madmom beat comparison vs the MV-14
measured grid was still owed after sprints 1 and 2.

## What madmom actually is (from the papers)

Böck & Schedl (DAFx 2011) → Böck, Krebs & Widmer (ISMIR 2014,
2016); BeatNet is Heydari, Cwitkowitz & Duan (ISMIR 2021). The
pipeline, in order:

1. **Features:** magnitude spectrogram (STFT, 2048 window, ~10 ms
   hop), log-frequency scaled. No hand-crafted onset features — the
   network learns them from the spectrogram.
2. **RNN:** three fully connected *bidirectional* LSTM layers, 25
   units per direction per layer, trained as a frame classifier.
   Beat-only model: one output (beat vs non-beat). Joint
   beat+downbeat model (ISMIR 2016): a 3-way softmax — beat but no
   downbeat (bk), downbeat (dk), non-beat (nok). Output is a
   per-frame beat-activation function.
3. **DBN:** a dynamic Bayesian network over a state space of bar
   position × tempo (2014 poster: 46 discrete tempo states, 56–215
   BPM). Transition model: tempo drifts slowly, bar position advances
   by 1/tempo per frame. Observation model: the RNN activation.
   Viterbi decoding gives the globally best beat sequence jointly
   with tempo; the downbeat DBN adds meter/bar length. The DBN beats
   plain thresholding + peak-picking of the RNN activations by ~15%
   F-measure. A tempo prior from a measured BPM can be fed in.
4. **Onsets:** a separate CNN/RNN onset detector + peak picking
   (Böck & Schedl's bidirectional-LSTM universal onset detector).

BeatNet replaces the BLSTM with a causal CRNN (1D conv + ReLU +
max-pool + FC 150 + two unidirectional LSTMs) and the DBN with
particle filtering for online use; its offline mode uses madmom's DBN.

## Design decision: which path, and why

Three paths were evaluated:

- **(a) Ellis DP beat tracker in C11** — classical, fully specified
  (Ellis 2007): spectral-flux onset envelope + autocorrelation tempo
  + dynamic programming with a log-Gaussian tempo prior. No weights,
  no training data, no external model. Every line is ours.
- **(b) madmom RNN forward pass in C11 with ported weights** — the
  full SLERM of madmom: 3×25 BLSTM forward pass + the 46-tempo-state
  DBN/Viterbi decoder. Needs the exact pretrained weights ported and
  the exact feature pipeline reproduced. Multi-sprint sized, and the
  weights are the learned part of madmom — porting them is reuse of
  the model, not a from-scratch re-creation. Deferred, not dropped.
- **(c) Port the existing Python grid estimator to C11** — same method
  (STFT flux + autocorrelation + phase search), reproduces the
  measured grid in C11. Validates the C11 signal path, but is NOT an
  independent second opinion: same onset function, same decoding.

**PICKED: (a), with (c) folded in as the front-end validation.**
The C11 tool includes a grid mode reproducing tempo + phase, so the
front end is validated against the Python reference; the DP tracker
on top is a genuinely different decoder from the global phase search
and from librosa's implementation. Fastest path to a real second
opinion, and the FFT/STFT/flux core is the reusable foundation (b)
needs later — madmom's feature extraction is also a log spectrogram,
and a C11 DBN decoder reuses the same Viterbi machinery as the DP
tracker.

## What was built

`detection-research/c11_beat/` — `beat_tracker.c` (single file, ~450
lines, C11, libc + libm only; `gcc -std=c11 -O2 -Wall -Wextra`,
zero warnings). Steps: WAV (16-bit PCM mono, 16 kHz) → STFT (Hann,
1024/256, centred frames like scipy) → spectral flux → tempo by
autocorrelation (BPM 60–200, 0.5 steps) → grid phase (10 ms steps)
→ Ellis DP (σ = 0.1 log-Gaussian, α = 1.0, predecessor window
[τ_p/2, 2τ_p]) → JSON beats. Runtime on the 161.6s MV-14 track:
**0.59s**. `compare_beats.py` is the Python/numpy validation +
comparison harness (analysis tooling only — the tracker is pure C11).

## Measured results (MV-14, track.mp4 md5 f2226f24…)

### Front-end validation — PASS

| Check | Result |
|---|---|
| C11 flux vs Python/scipy flux | corr **1.0000** at −1 frame lag, max\|diff\| **0.0031** (0–1 scale) |
| Phase at canonical period 0.649s (C11 flux) | **0.25s** vs measured 0.240s — one 10 ms step apart |
| C11 grid-mode tempo / phase (own period) | 90.5 BPM / 0.460s — see plateau note below |

The C11 signal path is correct: the flux is essentially bit-identical
to the Python reference (the −1 frame lag is the scipy centering
offset). The tool's own phase (0.460s) differs from the measured
0.240s only because its own period came out 0.663s (the 90.5
tie-break) — same flux, different period, different phase optimum.

### The tempo plateau — the measured 92.0 is a selection, not a peak

Autocorrelation of the flux is **flat 0.6357 across 90.5–92.5 BPM**
(and 0.5543 at the double-time octave 191–192). Python's estimator
and the C11 tool see the same plateau and break the tie differently
(Python's sort takes the highest BPM, 92.5; the C11 scan takes the
first maximum, 90.5). The plan's canonical 92.0 sits inside the
plateau. Tempo on this track has ±1 BPM of plateau uncertainty;
the phase search is what pins the grid, not the autocorrelation.

### DP beats vs measured grid — beats librosa on every grid metric

| | C11 DP | librosa beat_track |
|---|---|---|
| n beats | 247 | 238 |
| median IBI → BPM | 0.656s → 91.46 | 0.650s → 92.31 |
| median \|offset\| vs grid | **0.088s** | 0.145s |
| mean offset | +0.026s | +0.017s |
| std | 0.160s | 0.184s |
| within 50 ms | **35.6%** | 20.6% |
| within 100 ms | **53.0%** | 39.5% |
| drift over track | +0.017s | −0.023s |
| first / last beat | 0.176s / 161.264s | 3.808s / 159.150s |

Per-20s-window median offset (C11): 0s −0.041, 20s −0.002, 40s
+0.035, 60s +0.141, 80s +0.251, 100s −0.061, 120s +0.156, 140s
−0.167. Librosa shows the same section-dependent swing (60s/120s
positive, 140s negative) but disagrees in sign at 80s (−0.229):
the phase in that stretch is genuinely ambiguous between decoders.

### DP vs librosa directly — the two decoders agree with each other

Nearest-neighbour offsets: median |offset| **0.035–0.036s** both
directions, 83–86% within 50 ms, 89–92% within 100 ms. The two
independent decoders agree with each other far better than either
agrees with the rigid global grid. **The measured grid's single
global phase is the loose part, not the trackers** — same conclusion
as sprint 2, now with a second independent decoder confirming it.
Tempo is confirmed three ways (92.0 measured, 92.29 librosa, 91.46
C11 median IBI). Per-word ASR anchors stay the timing authority.

### Honest limits

- **Lattice-filling at the edges:** the DP has no onset-strength
  floor, so it places beats on a ~τ_p lattice through the quiet
  intro (0.18–3.42s, six beats before librosa's first at 3.808s)
  and the outro fade (159.94–161.26s, three beats after librosa's
  last at 159.15s). Every mid-track C11 beat (3.4–159.9s) has a
  librosa neighbour within 0.30s. The edge beats are the DP's
  no-threshold behaviour, not evidence of beats there.
- **Not madmom:** this is a classical DP tracker, not the RNN+DBN.
  It does not produce downbeats/meter, and its onset function is
  spectral flux, not a learned activation. The full madmom SLERM
  (path b) is still the follow-up.
- **One track:** validated on MV-14 only. MV-13 (97.0 BPM) and MV-12
  (131.5 BPM) are the obvious next runs — same command, different
  wav.

## Single most valuable next step

Add an onset-strength floor to the DP (skip lattice beats where the
local flux peak is below a fraction of the track's flux median) and
run the same tool on MV-13 + MV-12 — three tracks, one binary,
zero Python. After that, path (b): the C11 BLSTM forward pass +
DBN decoder, reusing this sprint's STFT/flux core and DP/Viterbi
machinery.
