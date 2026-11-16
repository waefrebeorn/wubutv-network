# Sprint 4 (survey) — Find even more tools to SLERM — 2026-11-11

Survey sprint under the standing SLERM-C11 method (user msg 214) and the
msg-227 directive (2026-11-11 20:18 EST): "find even more tools online
to SLERM... create the most robust tool set and simplify everything to
work within your blade server configuration... you know your
limitations you know your strengths... This is the way that you win."

Sprint 3 proved the method: the madmom/BeatNet beat tracker was
re-created in C11 as an Ellis DP tracker (0.59s, flux corr 1.0000 vs
scipy, beats librosa on every grid metric). This survey asks the same
question of every other tool in the pipeline: is its core an algorithm
we can re-create, or a trained model we cannot?

## The blade, measured (not assumed)

- CPUs: 4 visible, 1.5 shared. RAM: 7.9 GB total, ~6 GB working set.
  Python 3.12.3 only — no 3.11/3.10 on the box. No GPU.
- gcc 13.3.0, FFmpeg 8.1.2 (ships freezedetect, scdet, mpdecimate,
  blackdetect, signature — zero-install).
- `~/workspace/tools/lyrics-venv/` — 2.1 GB. torch 2.15.0+cpu is the
  giant in it; librosa 1.0.0, Demucs 4.1.0, BeatNet 1.1.1 (blocked —
  imports madmom), audio-separator 0.48.0, onnxruntime 1.31.1,
  scikit-learn 1.9.1, scipy 1.18.1, numpy 2.5.4. transformers is NOT
  installed (Qwen3-ForcedAligner/ASR would need it).
- `~/.cache/huggingface/` — 6.5 GB of model weights (5.0 GB blobs,
  1.5 GB faster-whisper-large-v3-turbo). The weight footprint is a
  blade constraint too: every C11 tool is kilobytes.
- `detection-research/venv/` — numpy/scipy/Cython only (madmom
  attempt residue). No cv2, no mediapipe anywhere on the box:
  F-03 (MAR) and F-05 (Farneback) have never run here because their
  installs were never done.

## The SLERM test (three questions, in order)

1. **Is the core an algorithm or a trained model?** An algorithm
   fully specified in a paper (Ellis DP, Farneback 2003, Fitzgerald
   HPSS, Foote novelty) can be re-created from scratch. A trained
   model (a transformer, a U-Net, a CNN) cannot — porting its weights
   is reuse, not re-creation (sprint 3's path-(b) ruling). Model-bound
   tools are listed in §5, not ranked.
2. **Does it fight the blade today?** Blocked install, minutes-long
   runtime, gigabytes of RAM/weights, or a maintenance risk
   (faster-whisper's last commit Nov 2025, PyAV-19 breakage).
3. **What breaks if we build it wrong?** Validation must exist as a
   bit-comparison against the thing it replaces (sprint 3's flux
   corr 1.0000 is the template) or against hand-checked ground truth.

## Inventory — every tool the pipeline actually uses

| Tool | What it does for us | Cost today | Status | SLERM verdict |
|---|---|---|---|---|
| faster-whisper large-v3-turbo (CTranslate2) | Sung-lyrics ASR, word times — the timing grid | ~1.5 GB RAM, minutes/song, PyAV pin `av==18.1.0`, last commit Nov 2025 | WORKS | **Adopt whisper.cpp as fallback; do NOT re-create Whisper** (§4) |
| Demucs htdemucs (torch) | Vocal separation → RMS-VAD segment boundaries + dense-span re-transcription | ~14 min per 172s track, torch 2.15 GB venv, weights in HF cache | WORKS, slow | **SLERM the segmentation job only** (HPSS, rank #3); Demucs stays for dense spans |
| MDX-Net ONNX via audio-separator | Lightest separator alternative | ONNX Runtime CPU, already installed 0.48.0 | INSTALLED, untested | Adopt for dense spans if Demucs too slow |
| librosa | beat_track, onset_strength, RMS, MFCC, chroma — intake + QC audio features | Pure-Python layer over numpy/scipy; slow, big import surface | WORKS | **SLERM the core** (rank #1) |
| madmom / BeatNet | Beat/downbeat/onset tracking | BLOCKED — cannot build on py3.12 | BLOCKED | Done (sprint 3, Ellis DP). Path (b) BLSTM+DBN is the follow-up, multi-sprint |
| WhisperX / wav2vec2 aligner | Forced alignment for word times | Needs wav2vec2 weights + transformers; untested | UNTESTED | Model-bound — substitute: word-time snapper (rank #2) |
| Qwen3-ForcedAligner / Qwen3-ASR | Forced alignment / singing ASR | 0.6B transformer, GPU-oriented, transformers not installed | UNTESTED | Model-bound — substitute: word-time snapper (rank #2) |
| Parakeet TDT v3 via sherpa-onnx | Non-autoregressive ASR challenger, native word durations | ONNX int8, CPU-fast (speech RTF ~0.03); singing unmeasured | UNTESTED | Adopt + A/B as-is; C11 transducer needs ported weights = reuse |
| MediaPipe Face Mesh | Face landmarks → MAR curve (F-03) | Never installed; heavy dep (mediapipe + cv2) | UNINSTALLED | Model-bound net — **SLERM the measurement shell** (rank #5) |
| SyncNet (F-01) | Audio-visual sync score LSE-C/D | Needs S3FD + SyncNet torch weights | UNTESTED | Model-bound — substitute: MAR + closure rules |
| AV-HuBERT / Auto-AVSR (F-14) | Visual-only lip-reading | Transformer, GPU-preferred, needs mouth crops | UNTESTED | Model-bound — no classical substitute for *what* the mouth says |
| TransNetV2 (F-10) | Learned shot boundaries | CNN weights, 48×27 frames, CPU-minutes/master | UNTESTED | Model-bound — substitute: TSM M5 + NMS (small, classical) |
| PySceneDetect (F-04) | Content-difference cut detection | pip install, threshold-tuned | UNTESTED | Already covered: scdet (FFmpeg, zero-install) + numpy |
| Farneback flow (F-05) | Dense optical flow → motion-energy curve, cut-energy contrast | Needs cv2 — never installed | UNINSTALLED | **SLERM in C11** (rank #4) |
| freezedetect / scdet (F-09/F-12) | Freeze + cut detection | FFmpeg built-ins, zero-install | TESTED | Keep — replicate single filters only if needed |
| TSM suite (F-17) | M1–M6 motion metrics, M6 gate calibrated | numpy + FFmpeg decode, our code | TESTED, live in QC | Keep — M5 needs NMS (small fix inside the suite) |
| Essentia (F-11) | Per-beat band loudness, arousal/valence | Big wheel, AGPLv3, untested install | UNTESTED | **SLERM the structural half** (band loudness, inside rank #1); arousal is model-bound |
| MSAF (F-15) | Song-structure segmentation (olda + scluster) | librosa+sklearn+scipy already installed; needs mir_eval + jams | UNTESTED | Adopt via pip first; C11 re-creation deferred (§4) |
| MPEG-7 signature / videohash2 (F-06) | Reuse detection | signature is an FFmpeg built-in; videohash2 uninstalled | PARTIAL | Keep signature; videohash is ~100 lines if ever wanted |
| Blender 4.5.15 (Cycles CPU) | Impact frames / 3D accents | 4m46s per 1280×720 frame, works | WORKS | Keep — impact-frame templates already exist; no SLERM |
| FFmpeg | Everything: decode, filters, encode, mux | Foundation, 8.1.2 | WORKS | Keep — replicate single filters as needed, never the whole tool |
| kinetic_ass.py / assembly scripts | Kinetic type, assembly, gating, mux | OUR code, copied per project | WORKS | Pipeline debt, not a tool SLERM: per-project copies need consolidation (§6) |
| Silero VAD (inside faster-whisper) | Speech VAD for segmentation | Small neural net | WORKS | Already substituted: RMS-VAD on separated vocals (MSS-ALT recipe); C11 RMS-VAD is a one-line add to rank #3 |

## Ranked SLERM targets — value × feasibility on the blade

### #1 — c11_mir: the C11 MIR core (extend beat_tracker.c)

- **What to build:** extend sprint 3's STFT/flux core into one
  dependency-free binary: MFCC, chroma (HPCP), RMS envelope,
  onset-strength (flux already exists), per-beat band loudness
  (Essentia `BeatsLoudness` substitute — spectrum energy per beat,
  whole + bands [20, 150, 400, 3200, 7000, 22000] Hz), spectral
  centroid / rolloff / contrast, tempogram. Same file, same build
  flags, same JSON-out pattern.
- **Replaces:** librosa for every pipeline use (beat_track already
  replaced by sprint 3; onset_strength, feature.rms, feature.mfcc,
  feature.chroma_cqt all go) and the structural half of Essentia
  (F-11). Also becomes the feature front-end MSAF-style work and
  the HPSS/snapper tools below need.
- **Size:** ~600–900 lines added to the existing ~450-line core.
  One sprint.
- **Win:** intake + QC audio features in under a second with zero
  Python, zero venv, zero weights. Kills the librosa import from
  every analysis script. Foundation for ranks #2 and #3.
- **Validation:** bit-compare each feature vs librosa on MV-14
  (corr ≥ 0.999, same bar sprint 3 set with flux); band loudness
  vs the Essentia algorithm spec (energy per beat segment per band
  — arithmetic, not learned).
- **Feasibility:** highest. Every algorithm is textbook; the STFT
  core already exists and is validated.

### #2 — Word-time snapper (forced-aligner substitute)

- **What to build:** given the known lyric sheet + faster-whisper
  word times + the vocal-stem onset envelope (flux, already dumped
  by beat_tracker), snap each word onset to the nearest strong
  onset within ±0.4s under a monotonicity constraint — a small
  DP/Viterbi lattice reusing sprint 3's Viterbi machinery. No
  neural model anywhere.
- **Replaces the *function* of:** Qwen3-ForcedAligner / WhisperX
  wav2vec2 alignment for our tracks (both model-bound, §5). It
  does not re-create them; it answers the same question — "when
  exactly was this word sung?" — from acoustic evidence we already
  compute.
- **Size:** ~300 lines C11 + a small Python harness. One sprint.
- **Win:** directly attacks failure mode (3) — timestamp smear in
  rapid chant, the pipeline's weakest link (word times are the
  tempo gospel's grid). No 0.6B transformer, no transformers
  install, runs in milliseconds.
- **Validation:** on MV-14 words vs hand-checked onsets: median
  |correction| and % of words moved OUT of gaps (the MV-11 pad
  rule: no anchor sits in a gap). Compare against WhisperX
  alignment on the same words if the wav2vec2 weights are ever
  fetched — the snapper is the control, not the claimant.
- **Feasibility:** high. Depends only on the flux output that
  already exists; no dependency on rank #1.

### #3 — C11 HPSS vocal-envelope + RMS-VAD segmenter

- **What to build:** Fitzgerald (DAFX 2010) median-filter HPSS on
  the sprint-3 STFT core: median along time → harmonic-enhanced
  spectrum, median along frequency → percussive-enhanced spectrum,
  soft masks → harmonic-layer energy in the vocal band → RMS-VAD
  segment boundaries (the MSS-ALT recipe: boundaries from
  separated-vocal amplitude). No resynthesis needed if only
  boundaries are wanted — envelope straight from masked magnitudes.
- **Replaces the *segmentation job* of:** Demucs (14 min/track).
  The MSS-ALT finding is the justification: the gain is from
  boundaries, not vocal cleanliness (mix 23.02% → 20.35% WER with
  RMS-VAD on the original mix; separated vocals barely move it).
  Demucs stays only for the rare dense-span re-transcription where
  a cleaner vocal stem is actually needed.
- **Size:** ~400 lines C11 (median filters + envelope + VAD).
  One sprint.
- **Win:** segmentation in under a second instead of ~14 minutes;
  removes torch from the intake path for most tracks — one more
  step toward a torch-free pipeline (§7).
- **Validation:** boundaries vs Demucs-RMS-VAD boundaries on MV-14
  (agreement within ±0.5s on ≥80% of boundaries); downstream:
  word recovery in the failing spans vs the current pipeline.
- **Feasibility:** high. The method is fully specified, and
  libsonare documents the same algorithm in a dependency-free
  C++ core — proof the shape fits.

### #4 — C11 Farneback dense optical flow (F-05's SLERM)

- **What to build:** Gunnar Farneback (SCIA 2003) two-frame motion
  estimation: quadratic polynomial expansion per pixel +
  multi-scale pyramid + iterative displacement refinement, on
  160×90 gray frames via the tsm.py FFmpeg decode path. Output:
  the per-frame mean-flow magnitude curve (motion-energy) and the
  cut-point energy contrast (12f before vs 12f after each cut).
- **Replaces:** OpenCV `cv2.calcOpticalFlowFarneback`, which was
  never installed here — F-05 has never run. No cv2, no install.
- **Size:** ~500–700 lines C11. One to two sprints (the pyramid +
  iteration loop is the fiddly part).
- **Win:** unlocks cut-energy contrast — GAP-1's missing metric
  ("cut during a movement") — and the motion-energy curve F-08
  needs, with zero installs.
- **Validation:** flow magnitude curve vs cv2 on the same frames
  (install cv2 once, in a throwaway venv, for the comparison
  only); plus the published Yosemite sequence as a second check.
- **Feasibility:** medium-high. The paper fully specifies the
  algorithm and the author's own MATLAB/C reference exists; the
  risk is in the pyramid bookkeeping, not in any unknown.
  Ranked below #1–#3 because it is video-side (heavier, more
  code) while the audio side pays off first.

### #5 — MAR-curve lipsync tool (F-03's SLERM shell)

- **What to build — and what NOT to build:** the landmark net
  itself is model-bound and is NOT re-created. The tool is the
  measurement pipeline around a small public landmark model:
  FFmpeg frame decode → InsightFace `buffalo_l` `det_10g` face
  detector (ONNX) + the facefusion 68-point landmark ONNX model
  (256×256 input, [1,68,3] output) under onnxruntime 1.31.1 —
  already installed — → MAR curve (landmarks 13/14 over 61/291)
  + bilabial closure rule (F-02 approximation: /p/, /b/, /m/
  must hit the closed baseline inside the phone window) +
  alignment vs SONG_WORDS. ~300 lines of Python glue + two ONNX
  files downloaded once.
- **Replaces the *function* of:** MediaPipe Face Mesh (never
  installed) for F-03, without mediapipe or cv2.
- **Size:** one sprint, mostly wiring + calibration.
- **Win:** the first-ever picture-side lipsync number in the
  pipeline — GAP-2's core measurement. A mouth that moves on the
  beat but never shapes the lyric becomes a number, not an eye-read.
- **Validation:** the F-03 test as banked — MV-7 good insert vs
  MV-8 v2 bad insert; face found on >90% of frames, MAR peaks
  within ±3f of word onsets on the good one, visibly disagreeing
  on the bad one.
- **Feasibility:** medium — and honestly flagged. It depends on a
  model we don't control, and landmark accuracy on stylised /
  cartoon faces is unmeasured; calibration may show it doesn't
  work on our characters. Test-first, not build-first: run the
  two ONNX files on one insert before writing the tool around them.
  Ranked fifth for that reason, not for lack of value.

## §5 — Model-bound: NOT SLERM-able from scratch (do not attempt)

These are trained models, not algorithms. Re-creating them from
scratch means re-training them — data, GPU, weeks — which is not
this program. Porting their weights is reuse, not re-creation
(sprint 3's path-(b) ruling). For each, the substitute is named:

- **Whisper itself** (faster-whisper / CTranslate2) — adopt
  whisper.cpp 1.9.5 (Oct 2026, ggml, maintained, word timestamps
  via `-ml 1`) as the fallback for faster-whisper's maintenance
  risk. whisper.cpp IS the C SLERM of Whisper; re-doing it is
  re-creating someone else's re-creation.
- **Qwen3-ASR / Qwen3-ForcedAligner, wav2vec2 aligner, Parakeet
  TDT** — substitute: rank #2 snapper (alignment) and Parakeet
  tested as-is via sherpa-onnx (ASR challenger).
- **Demucs U-Net, BS-Roformer** — substitute: rank #3 HPSS for
  segmentation; MDX-Net ONNX via audio-separator for dense spans.
- **madmom RNN + DBN, BeatNet CRNN** — sprint 3 (Ellis DP) done;
  path (b) C11 BLSTM+DBN is the multi-sprint follow-up, reusing
  the sprint-3 core.
- **SyncNet, AV-HuBERT / Auto-AVSR, TransNetV2, MediaPipe Face
  Mesh, Essentia arousal/valence** — substitutes: rank #5 MAR +
  closure rules (SyncNet/MediaPipe side), TSM M5 + NMS (TransNetV2
  side), rank #1 band loudness (Essentia structural side). There
  is no classical substitute for *what* the mouth says
  (AV-HuBERT) — that question stays unanswered until a visual
  model is adopted, not built.

## §6 — Adopt, don't SLERM (already-existing lightweight answers)

- **whisper.cpp 1.9.5** — the faster-whisper fallback (see §5).
- **Parakeet TDT v3 via sherpa-onnx / onnx-asr** — A/B as-is on
  the worst tracks; singing evidence is the open question, not
  the runtime.
- **MSAF via `pip install msaf`** (zigify-msaf 0.3.0 pins
  olda+scluster) — librosa, sklearn, scipy already installed;
  only mir_eval + jams are new. C11 re-creation (Foote novelty +
  OLDA + spectral clustering) is deferred: section boundaries are
  a check on the hand-built plan, not a load-bearing tool.
- **MDX-Net ONNX via audio-separator 0.48.0** — already installed;
  the lightest separator for dense-span re-transcription.
- **InsightFace `buffalo_l` ONNX files** (`det_10g` + landmark
  model) — the weights rank #5 runs under; downloading weights is
  adoption, the measurement pipeline around them is the SLERM.
- **Kinetic type width bug** — fontTools 4.68.0 is already in the
  lyrics venv: measure real glyph advances instead of estimating
  char width. A small Python fix, not a SLERM.
- **Per-project script copies** (`assembly_build.py`,
  `build_kinetic.py`, `gate_master.py`, `motion_audit.py`, `mux.py`,
  `chat_copy.py`, `split_encode.py` copied per MV-*) — pipeline
  debt, not a tool SLERM. A consolidation job (one canonical set
  + per-project config) belongs on the list, but it is a refactor,
  not a re-creation.

## §7 — The roadmap this survey points to

The end state is a torch-free, venv-light pipeline where every
audio measurement is one C11 binary and every video measurement is
FFmpeg + C11/numpy:

1. **Sprint 4 (this survey's pick): c11_mir** — §3 #1, scoped below.
2. Word-time snapper (#2) — needs only flux, buildable in parallel
   with #1.
3. C11 HPSS + RMS-VAD (#3) — needs the #1 STFT core; removes torch
   from intake for most tracks.
4. C11 Farneback (#4) — unlocks F-05 / GAP-1 motion-energy.
5. MAR-curve tool (#5) — test-first; first picture-side lipsync
   number if calibration passes.
6. Later: C11 BLSTM + DBN (madmom path b, multi-sprint), MSAF
   C11 re-creation if the pip adoption proves its worth, TSM M5
   non-max suppression (small fix inside the existing suite).

After #1–#3, the only torch user left is Demucs for dense spans —
and MDX-Net ONNX (no torch) covers that too, which would make the
pipeline torch-free and cut the 6.5 GB weight cache to the Whisper
model alone.

## §8 — Sprint 4 scope (the pick: #1, c11_mir)

**Goal:** extend `detection-research/c11_beat/beat_tracker.c` into
the C11 MIR core — every audio feature the pipeline takes from
librosa/Essentia, in one dependency-free binary, validated
bit-for-bit against the libraries it replaces.

**Step 0 (sprint 3's owed follow-up, first commit):** add the
onset-strength floor to the DP — skip lattice beats where the
local flux peak is below a fraction of the track's flux median —
and run the tool on MV-13 (97.0 BPM) and MV-12 (131.5 BPM).
Same command, different wav; report tempo/phase agreement per
track.

**Step 1 — features, on the existing STFT core (1024/256 Hann,
16 kHz mono):**
- MFCC (mel filterbank + log + DCT, 13 coeffs, librosa defaults)
- Chroma / HPCP (pitch-class mapping of FFT bins)
- RMS envelope per frame + per-beat RMS
- Per-beat band loudness (Essentia BeatsLoudness: spectrum energy
  per beat segment, whole + bands [20, 150, 400, 3200, 7000, 22000] Hz)
- Spectral centroid, rolloff, contrast (one frame-level descriptor
  each — cheap, completes the Essentia structural set)
- Tempogram (autocorrelation of the onset envelope at lag grid —
  reuses the tempo code)

**Step 2 — interface:** one binary, subcommands or flags per
feature, JSON out in the existing pattern (`c11_mir.json` per
track). Keep `beat_tracker` working unchanged — the DP tracker is
a mode of the same tool, not a fork.

**Step 3 — validation (the sprint's pass bar):** every feature
bit-compared vs librosa on MV-14 (corr ≥ 0.999, same bar as the
flux validation); band loudness vs the Essentia algorithm spec;
tempo/phase on MV-13 + MV-12 vs their measured grids (97.0 /
131.5 BPM). Report in `SPRINT_2026-11-11_C11_MIR.md`.

**Files:** `detection-research/c11_beat/` grows into
`detection-research/c11_mir/` (or the same directory renamed —
coordinator's call, keep the git history readable); report
`detection-research/SPRINT_2026-11-11_C11_MIR.md`; DETECTION_FINDERS.md
run entry. No commit, no Telegram (parent owns both).

**Size:** one sprint, ~600–900 lines added. No new dependencies
(libc + libm only, same as sprint 3). No video generation.

## Sources

- Farneback, "Two-Frame Motion Estimation Based on Polynomial
  Expansion", SCIA 2003 — paper + OpenCV `optflowgf.cpp`
  reference implementation.
- Fitzgerald, "Harmonic/Percussive Separation Using Median
  Filtering", DAFX 2010 — https://arrow.tudublin.ie/argcon/67/
  and https://dafx10.iem.at/program/15.html ; libsonare HPSS
  docs — https://libsonare.libraz.net/docs/source-separation
- Essentia `BeatsLoudness` / `SingleBeatLoudness` reference —
  https://essentia.upf.edu/algorithms_reference.html
- MSAF (Nieto & Bello, ISMIR 2016); zigify-msaf 0.3.0 —
  https://pypi.org/project/zigify-msaf/
- whisper.cpp 1.9.5 (Oct 2026) — ggml-org/whisper.cpp; 2026
  shootout — https://www.aifoss.dev/blog/faster-whisper-vs-whispercpp-vs-whisperx-2026/
- InsightFace `buffalo_l` model pack (`det_10g` detector);
  facefusion 68-point landmark ONNX ([1,3,256,256] in,
  [1,68,3] out).
- Sprint 3 report `SPRINT_2026-11-11_C11_BEAT.md`; lyrics report
  `research_notes/lyrics-extraction-cpu-2026-20261110-0322/report.md`;
  bank `detection-research/DETECTION_FINDERS.md` (F-01–F-17).
