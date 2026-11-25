# Sprint 6 — C11 HPSS + RMS-VAD segmenter (survey pick #3)

- **Date:** 2026-11-11 (evening, EST; run completed ~23:30 EST)
- **Coordinator:** respawn #2 (a9f9ed8e). Predecessor a2a12fd2 died
  22:36:35 EST on a transport error (sqlx pool timeout) leaving
  `hpss.c` + a compiled binary + first validation numbers; a first
  respawn attempt (4d932065, ~22:45 EST) never materialized. This
  respawn continued from the partial work — nothing good was rewritten.
- **Scope:** survey pick #3 (`SPRINT_2026-11-11_SLERM_SURVEY.md` §3):
  Fitzgerald (DAFX 2010) median-filter HPSS on the sprint-4
  `c11_mir` STFT core → harmonic-layer energy in the vocal band →
  RMS-VAD boundaries (the MSS-ALT recipe: the gain is boundaries,
  not cleanliness). Target: replace Demucs' ~14-min segmentation job
  with <1 s of C11.
- **Verdict: MIXED — the HPSS itself validates (masks PASS), the
  boundary gate FAILS structurally.** The harmonic vocal-band envelope
  does not separate vocals from the backing track on MV-14, and no
  threshold or envelope variant tested recovers the reference
  boundaries. The tool is correct and fast; the survey's hypothesis
  behind it is not. Details + diagnosis below; nothing is hidden.

## What was built

All under `musicvideo/detection-research/c11_mir/` (extended, not forked):

| file | what | lines |
|---|---|---|
| `hpss.c` | the tool: WAV reader, STFT (verbatim c11_mir core), Fitzgerald HPSS (time + freq median, soft masks), vocal-band + full-band power envelopes, RMS-VAD, JSON writer, `--selftest-median` regression test, `--dump-env` / `--dump-harm` | 511 |
| `c11_hpss` | compiled binary (`gcc -std=c11 -O2 -Wall -Wextra`, zero warnings, libc + libm only) | — |
| `compare_hpss.py` | validation: (a) masks vs librosa, (b) boundaries vs Demucs reference, both directions | 125 |
| `make_ref_segments.py` | builds the Demucs-RMS-VAD reference JSON (verbatim recipe port, `--selftest` vs MV-11) | 131 |
| `diagnose_bounds.py` | boundary-failure diagnosis: envelope comparison + threshold sweep | 158 |
| `diagnose_bounds2.py` | bounded test of three alternative HPSS envelopes | 76 |
| `hpss_mv14.json` | C11 output on MV-14 (13 vocal-band + 16 full-band segments) | — |
| `hpss_mv14_ref.json` | Demucs-RMS-VAD reference on MV-14 (12 segments) | — |
| `hpss_mv14_validation.json` | validation numbers (masks + boundaries) | — |
| `hpss_mv14_env.txt` | dumped envelopes (vocal + full power, 16 ms grid) | — |
| `demucs_mv14.log` | Demucs separation log (14:54 wall) | — |

Never commit: `hpss_mv14_harm.bin` (40 MB intermediate),
`separation_mv14/` (28 MB Demucs vocals stem), `mv14_16k.wav`
(5 MB input), `c11_hpss` (binary). Usage:
`./c11_hpss <wav16k-mono> <out.json> [--dump-env env.txt]
[--dump-harm harm.bin]`; `./c11_hpss --selftest-median`.

## Lego vs fresh (standing LEGO RULE, msg 233)

| component | source | verdict |
|---|---|---|
| STFT (Hann periodic, centred, n_fft 1024 / hop 256) + radix-2 FFT | sprint-4 `c11_mir.c`, verbatim copy | LEGO (same repo) |
| WAV reader (16-bit PCM, mono/stereo) | sprint-4 `c11_mir.c`, verbatim copy | LEGO |
| RMS-VAD (thr 0.1×p99, merge <1.0 s, drop <0.5 s, split >30 s at quietest, pad 0.3 s) | pipeline's own `MV-11/.../analysis/test2_segment_transcribe.py::rms_vad`, verbatim port (track-length clamp parameterized) | LEGO |
| Demucs reference recipe + separation | MV-11 test #2 recipe; audio-separator 0.48.0 + htdemucs weights already on disk | LEGO (existing tooling) |
| Sliding-window median filter (reflect-padded, sorted window) | fresh — no sliding median exists in any of the 9 surveyed user repos (lego harvest confirms: HPSS/VAD not found in wubuwizard/wubuos/www) | FRESH |
| Fitzgerald HPSS soft masks (margin 1.0) | fresh — DAFX 2010 paper + librosa parity | FRESH |
| Envelope + JSON writer + selftest | fresh | FRESH |

## Validation

### (a) HPSS masks vs librosa — PASS

Same 16 kHz wav, same STFT, `librosa.decompose.hpss` kernel 31,
margin 1.0:

- harmonic magnitude corr **0.999229** (bar ≥0.999) — PASS
- max|diff| 35.41, rel 0.239; librosa harmonic share 0.5962 vs C 0.5862
- Residual: 58/10101 frames have a per-frame max|diff| > 10, median
  per-frame max|diff| 0.36; worst frames are MID-track (86.22 s,
  69.20 s, 91.46 s), edges clean (0.001) — the reflect padding is
  right and the residual is isolated median-tie frames near H≈P,
  not a systematic error. It does not affect the envelope (summed
  over 198 bins).

### (b) Reference build — verified

Demucs htdemucs via audio-separator 0.48.0 (`-m htdemucs.yaml`,
`--single_stem Vocals`; note the model name is the yaml filename —
`htdemucs` and the weight hash both fail with "not found in
supported model files"; the model dir must be passed explicitly,
default is /tmp which is full). Separation took **14:54 wall**
(2 passes × 28 chunks, OMP threads 2) for the 161.6 s track.
`make_ref_segments.py` then runs the verbatim RMS-VAD recipe on the
vocals stem → 12 reference segments. **Port selftest: reproduces
MV-11's `test2_segments.json` exactly (12/12 segments, worst
boundary diff 0.000 s).** The reference recipe is therefore the
pipeline's own, verified — not a re-implementation.

### (c) Boundaries vs Demucs-RMS-VAD — FAIL

±0.5 s tolerance, both directions (vocal band):

| | ref→C | C→ref |
|---|---|---|
| starts | 2/12 (16.7%), median |off| 0.370 s | 2/13 (15.4%) |
| ends | 1/12 (8.3%), median |off| 0.130 s | 1/13 (7.7%) |
| **OVERALL** | **3/24 (12.5%)** | **3/26 (11.5%)** |

Full-band is worse (8.3% / 6.2%). Bar was ≥80% both directions.
The few matches that exist are close (median offsets 0.13–0.37 s),
so this is not a shift or grid error — the segmentations are
structurally different. C11's first segment starts at 3.33 s
(instrumental intro; the reference's first vocal segment starts at
14.14 s), and from ~58 s on the C11 envelope never drops below
threshold at all — one 92 s run split recursively into four
identical 23.4 s pieces at midpoints.

### (d) Diagnosis — why it fails (the numbers)

- **Grid is not the issue.** Running the same VAD recipe on the
  Demucs RMS envelope resampled to the C11 16 ms grid reproduces
  the reference **100% / 100%**. The VAD code is also verified: the
  C implementation and the Python port agree on MV-11 (selftest) and
  the C tool's own segments match a Python re-run of its envelope
  (threshold sweep at 0.10 reproduces 13 segments, 12.5%).
- **The envelope does not separate vocal from silent spans.**
  Median C11 harmonic vocal-band power: 426.5 during reference-active
  spans vs 344.8 during reference-silent spans — a **1.24×** ratio.
  Demucs vocals RMS over the same spans: 0.06128 vs 0.00032 — a
  **192×** ratio. Log-correlation between the envelopes is 0.33.
  The harmonic layer retains the music (synths/bass/guitars are
  harmonic and fill 300–3400 Hz), so it stays loud between phrases.
- **No threshold rescues it.** Sweeping thr_frac 0.10→0.80 on the
  C11 envelope: best agreement **16.7%** (at 0.15/0.40/0.50), most
  settings 4–13%. The envelope simply does not carry the phrase
  boundaries on this track.
- **No alternative HPSS envelope rescues it** (`diagnose_bounds2.py`,
  all on librosa H/P): (A) harmonic-share ratio in the vocal band:
  0–9%; (A2) absolute ratio thresholds: 8–13%; (B) adaptive
  threshold (envelope > k × 10 s rolling median, k 1.2–3.0): best
  **29.2%** (k=3.0); (C) narrower band 500–2000 Hz: best 20.8%.
  Nothing approaches 80%.

**Conclusion: harmonic ≠ vocal on a dense mix.** The survey's
hypothesis — harmonic-layer vocal-band energy as a vocal-activity
proxy — fails on MV-14. This is a property of the signal, not of
the implementation: the HPSS is correct (masks PASS), the VAD is
correct (grid check 100%), the reference is correct (MV-11
selftest). The missing piece is a genuine vocal-activity feature
(pitch/voicing-based, or a separated-vocal stem), which is a new
build, not a patch to this one.

### (e) Runtime — target MISSED, but 480× faster than Demucs

Total CPU time on the 161.6 s track (clock(), binary's own
measurement; wall time is higher under contention — 3 other builds
were running): **1.71–1.90 s** across runs (HPSS masks 1.19–1.31 s,
rest STFT + envelope + VAD + IO). Target was <1 s — **missed by
~2×**. Against Demucs' 894 s separation for the same job, that is
**~480× faster**. The <1 s target would need a further ~2× (the
STFT is ~0.3–0.4 s of the remainder; a real-input FFT is the
obvious next optimization, not attempted — it changes the shared
STFT core and needs its own validation).

**Two-heap median optimization: tried, REVERTED.** A two-heap +
lazy-deletion sliding median was implemented to cut the 1.30 s
median cost — it ran SLOWER (3.68 s: for K=31 the heap+hash
constant beats the O(K) sorted window's cache-friendly memmoves)
and was WRONG twice: (1) removing a value compared it against the
post-cleaning median instead of the pre-removal median (selftest
caught it: i=44, got 2 want 3); (2) a GLOBAL pending-deletion table
let one heap's cleaning eat the other heap's live copy of the same
value under duplicates, drifting the live counts until a pop ran
on an empty heap (ASan: heap-buffer-overflow, write to hi[-1]).
Fixed with per-heap pending tables (selftest then PASSED), but the
speed made it pointless — reverted to the predecessor's sorted
window, which the selftest guards. The final binary is the
sorted-window version; `hpss_mv14_harm.bin` was regenerated from
it (an earlier "bit-identical" check was vacuous — the dump is
opt-in and the runs that printed it had not passed `--dump-harm`).

### (f) Build hygiene

`gcc -std=c11 -O2 -Wall -Wextra` with **zero warnings**; libc +
libm only (no OpenMP/pthreads — the runtime target is a stretch
goal, not a reason to break the dependency rule). `--selftest-median`
regression test in the binary (500 values, K=31, heavy duplicates,
vs naive sort-per-window median — PASS). No `/tmp` use anywhere
(tmpfs is full; all scratch lives in the project dir).

## Honest limits

- Boundaries do NOT validate on MV-14 (12.5% vs 80% bar) — do not
  use `c11_hpss` segments as a drop-in for Demucs-RMS-VAD segments.
- Runtime 1.7–1.9 s, not <1 s.
- Masks residual: 58 frames with max|diff| > 10 (median-tie frames);
  corr passes but the masks are not bit-identical to librosa.
- Validated on MV-14 only (one dense funk mix). The envelope might
  separate better on a sparse mix — untested, and the MV-14 result
  says not to assume it.
- The full-band segmentation (16 segs) is a by-product, not
  validated against anything.

## Recommendation (for the parent)

1. **Demucs stays for the segmentation job** until a real
   vocal-activity feature exists. The torch-free roadmap loses this
   leg: after sprints 4–7, Demucs is still the only segmenter.
2. **Next candidate: MDX-Net ONNX vocals RMS** (survey roadmap) —
   but MDX-Net is currently broken in the lyrics venv (torchvision
   0.29.2 vs torch 2.15 clash); fixing that venv is the prerequisite,
   not another HPSS variant.
3. **Alternatively: a pitch/voicing-based vocal detector in C11**
   (e.g., YIN/autocorrelation voicing on the harmonic layer) as a
   new sprint — the HPSS output is already the right front-end for
   it, and the masks gate passing means the front-end is trusted.
4. **Keep `c11_hpss` as a fast harmonic/percussive splitter** — the
   masks gate (0.999229) makes it usable wherever harmonic vs
   percussive separation is wanted (e.g., a pre-filter for onset
   work), just not as a vocal segmenter.
5. Do not re-run the boundary validation expecting a different
   result without a different envelope — the sweep + variants bound
   the outcome (best 29.2%).

## Files for the commit (parent owns the commit)

Commit: `hpss.c`, `compare_hpss.py`, `make_ref_segments.py`,
`diagnose_bounds.py`, `diagnose_bounds2.py`,
`SPRINT_2026-11-11_C11_HPSS.md`, `hpss_mv14.json`,
`hpss_mv14_ref.json`, `hpss_mv14_validation.json`,
`hpss_mv14_env.txt`, `demucs_mv14.log`, DETECTION_FINDERS.md run
entry. Never commit: `c11_hpss` (binary), `hpss_mv14_harm.bin`
(40 MB), `separation_mv14/` (28 MB), `mv14_16k.wav` (5 MB).
