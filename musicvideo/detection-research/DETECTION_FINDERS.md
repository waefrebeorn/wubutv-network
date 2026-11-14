# DETECTION FINDERS — bank

Daily detection-finders research (user order 2026-11-09 ~02:52 EST:
"USE THE SONG AND FIND BETTER DETECTION METHODS EVERY DAY BY
RESEARCH PROJECTING ALL AVENUES NEW FINDERS"). MV-8 v2 was rejected
on playback for bad montage timing, bad lipsync timing, and halted
moments — the gates didn't catch what the user's eye caught. This
bank holds every genuinely new finder: what it detects, how it works,
how to run or replicate it here, what it would have caught in MV-8 v2,
and its limits.

Rules: DEDUPE — never re-bank a finder already in this file. UNTESTED
means promising but never run against our footage — do not claim it
works. READ-ONLY except this file: never generate video, never fire a
volley, never edit any MV project file, never commit.

Gaps reference: `../MV-8_wipe-and-its-still-there/work/rebuild/DETECTION_GAPS_v3.md`
(GAP-1 montage timing, GAP-2 mouth detector on warped renders,
GAP-3 per-shot motion audit, GAP-4 vibes/energy match).
Standing weak spots: (1) montage timing, (2) lipsync timing from the
picture, (3) halted moments, (4) footage reuse, (5) song-vibe fit.

Environment note (2026-11-09): the system python3 on this VM has
`faster-whisper` only — no librosa, cv2, mediapipe, or torch. Every
finder below that needs those installs into a venv first
(`python3 -m venv ~/workspace/wubutv-network/musicvideo/detection-research/venv`
then `pip install ...`). That install step is part of each finder's
UNTESTED test.

---

## 2026-11-09 — F-01 SyncNet LSE-C / LSE-D (audio-visual sync score)

- **Detects:** whether mouth movement in a video matches the speech/sung
  audio at all — a single number per face track instead of eye-only
  judgement. GAP-2.
- **How it works:** SyncNet (Chung & Zisserman, ACCV 2016) is a two-stream
  ConvNet that learns a joint embedding of 0.2s mouth-image clips and
  MFCC audio; the distance between the two embeddings measures sync. The
  standard scores are LSE-C (confidence, higher = better sync) and LSE-D
  (minimum feature distance, lower = better sync); real video scores
  roughly LSE-D 6.0–6.5. The pip-installable wrapper finds and tracks
  faces with S3FD, crops each track, and returns per-track AV offset in
  frames plus LSE-C/LSE-D.
- **Run / replicate here:** `pip install syncnet-python` (PyTorch 2,
  Python 3.9–3.13); download weights from the Oxford VGG lipsync page
  (`syncnet_v2.model`, `sfd_face.pth` — same URLs the original repo's
  `download_model.sh` uses). Paper:
  https://www.robots.ox.ac.uk/~vgg/publications/2016/Chung16a/chung16a.pdf
  Package: https://pypi.org/project/syncnet-python/ — Original repo:
  https://github.com/joonson/syncnet_python
- **What it would have caught in MV-8 v2:** a per-insert/per-segment
  sync number for every singer insert, so a badly timed insert fails on
  a score instead of surviving until the user's playback verdict. Run it
  on the warped insert render, not the source take (GAP-2's whole point).
- **Limits:** trained on real talking heads / TV speech, not sung vocals
  over a music bed and not stylised/cartoon faces — scores may shift and
  need a local calibration baseline (run it on a known-good MV-7 insert
  first). Clip-level scores miss articulation errors: a mouth can move in
  time yet never close for /p/ — that is what F-02 is for. Prior mention:
  flagged in `notes/LIP_SYNC_KEVIN_BACON_2026-11-01.md` (Nov 1 research),
  never implemented or run — banked here as the canonical entry.
- **Status:** UNTESTED. Test: install in the research venv, run on one
  known-good MV-7 warped insert and one known-bad MV-8 v2 insert, compare
  LSE-D/LSE-C; pass bar is separation between the two.
- **UPDATE 2026-11-12:** Sync-C gaming caveat — the Kandinsky S2V 1.0
  technical report (Oct 2026, arXiv:2610.19290) notes Sync-C can be
  exploited by exaggerating lip motion, which is why they add side-by-side
  human evaluation. A high LSE-C on a take whose mouth flaps wide on every
  word is not proof of good lipsync; read LSE-C together with F-02/F-03
  (does the mouth close for bilabials, does MAR peak on the word).

## 2026-11-09 — F-02 PVSync per-phoneme articulation scoring

- **Detects:** articulation errors SyncNet misses — a mouth that moves in
  time with the audio but never forms the sung sound (e.g. lips never
  close for /p/). GAP-2.
- **How it works:** PVSync (Stephen et al., arXiv:2610.09223) unifies
  window-level contrastive AV synchronisation with a phoneme-level
  articulation objective: visemes (groups of phonemes with the same
  visible articulation) are derived automatically from forced-aligned
  transcripts, and each phone gets a score = mean cosine similarity
  between its video span and its audio span across 12-frame windows;
  phones below a threshold are flagged. On 13 talking-head generation
  models it matched human lip-sync rankings at Spearman ρ=0.83 vs 0.34
  for LSE-C, and recovered the AV offset within one frame on 92.7% of
  held-out clips.
- **Run / replicate here:** paper https://arxiv.org/abs/2610.09223 —
  code "will be released upon acceptance" (no public repo as of
  2026-11-09), so the full model is NOT runnable yet. Replicable now
  with our own stack: forced-align the song words to phonemes
  (WhisperX or Montreal Forced Aligner — we already run faster-whisper
  word timings), build the mouth aspect ratio curve (F-03), and flag any
  bilabial phone (/p/, /b/, /m/ — mouth must fully close) whose MAR
  never dips to its closed baseline inside the phone's window.
- **What it would have caught in MV-8 v2:** inserts where the mouth
  flaps on the beat but never shapes the lyric — exactly the "bad
  lipsync timing" the user heard, at the level of individual words
  instead of a whole-clip score.
- **Limits:** no public code yet — the full model can't be run, only
  approximated. The MAR approximation is cruder than a learned viseme
  embedding (no distinction between near-visemes). Needs phoneme-level
  alignment, which our current word timings don't give.
- **Status:** UNTESTED (paper-only; approximation untested). Test: hand
  -check the /p/ /b/ /m/ closure rule on one MV-7 insert with a known
  bilabial line, then watch for the PVSync code release.
- **UPDATE 2026-11-12:** code release CHECKED — still unreleased. The
  arXiv page (2610.09223, last updated ~316 days ago) still reads "Code
  and benchmark data will be released upon acceptance"; no public repo
  found. The MAR approximation + F-21 (MFA phoneme timings) remain the
  runnable path. Re-check the release each run.
- **UPDATE 2026-11-13:** code release re-CHECKED — still unreleased.
  The arXiv HTML/PDF (2610.09223) still reads "Code and benchmark data
  will be released upon acceptance." No public repo found today either.

## 2026-11-09 — F-03 MediaPipe Face Mesh mouth aspect ratio (MAR) curve vs word onsets

- **Detects:** visible mouth state (open / transitional / closed) frame
  by frame on the warped insert render, as a curve that can be laid
  against the song's word onsets. GAP-2.
- **How it works:** MediaPipe Face Mesh tracks 468 3D facial landmarks
  per frame. Mouth aspect ratio = vertical lip distance / mouth width,
  using landmarks 13 (upper lip centre) and 14 (lower lip centre) over
  61 (left corner) and 291 (right corner): MAR = |13−14| / |61−291|.
  Sample MAR at every frame of the warped render, smooth lightly, and
  compare MAR peaks against the song word onsets in SONG_WORDS — a sung
  word whose onset lands on a MAR valley (closed mouth) is a lipsync
  miss; a MAR curve that never rises during a sung line is a dead mouth.
- **Run / replicate here:** `pip install mediapipe opencv-python`;
  `mp.solutions.face_mesh.FaceMesh(static_image_mode=False,
  refine_landmarks=True)` per frame, read landmarks 13/14/61/291,
  emit MAR per frame to JSON, plot against word onsets. Landmark map:
  https://dev.to/metsander/mediapipe-face-mesh-all-478-landmark-points-5ec8
- **What it would have caught in MV-8 v2:** every insert whose mouth
  state disagrees with the sung word at its onset, measured from the
  picture — no reliance on take audio, no eye-reading of onset frames.
  Also flags the structural case: MV-3 S13's painted smile has no mouth
  opening anywhere, which reads as a flat MAR line — a detectable
  signature instead of a surprise at assembly.
- **Limits:** needs a visible, roughly frontal face; fails or jitters on
  profile shots, occluded mouths, and heavily stylised/cartoon faces
  (our characters are stylised — detection rate per character must be
  measured, not assumed). MAR thresholds are per-face: calibrate the
  closed baseline per insert. A painted smile with no moving mouth
  defeats landmark tracking silently — treat "no face found for N
  consecutive frames" as a FAIL, not a skip.
- **Status:** UNTESTED. Test: run on one MV-7 warped insert with known
  good lipsync and one MV-8 v2 insert; check (a) face found on >90% of
  frames, (b) MAR peaks align with word onsets within ±3f on the good
  one and visibly disagree on the bad one.

## 2026-11-09 — F-04 PySceneDetect + per-shot motion statistics

- **Detects:** true shot boundaries in a master, so every later motion
  audit can be computed per shot instead of across cuts. GAP-3 (and the
  segmentation GAP-1 needs).
- **How it works:** PySceneDetect compares consecutive frames (HSL
  colourspace differences in `detect-content`, rolling-average ratio in
  `detect-adaptive`, perceptual hash in `detect-hash`) and emits a cut
  when the difference exceeds a threshold. Feed its scene list into the
  motion audit: split the master at the detected cuts first, then
  compute frame-diff / flow statistics inside each shot only — a cut is
  a 100% frame change by definition, so whole-master diff flags every
  cut as "motion" and hides real freezes inside segments.
- **Run / replicate here:** `pip install scenedetect[opencv]`; CLI:
  `scenedetect -i master.mp4 detect-content --threshold 27` or
  `detect-adaptive` for fast-cut montage; Python:
  `from scenedetect import detect, ContentDetector; detect(path,
  ContentDetector())`. Docs: https://www.scenedetect.com/
- **What it would have caught in MV-8 v2:** the freezes hiding inside
  3s montage segments between cuts — invisible to the whole-master
  frame-diff the v2 build used, visible the moment the audit is
  per-shot. Also gives an independent cut list to cross-check against
  the assembly's planned cut frames (a detected cut where none was
  planned = an accidental flash-frame or a warp artefact).
- **Limits:** threshold is material-dependent (AI-generated footage has
  different frame-to-frame noise than camera footage); needs tuning per
  project and a stats-file pass (`-s`) to pick it. Fast strobe / whip
  transitions can over-trigger; slow dissolves under-trigger.
- **Status:** UNTESTED. Test: run `detect-adaptive` on the MV-8 v3
  master and compare its cut list to the assembly's planned cuts —
  expect near-1:1, then run the per-shot diff audit (F-05) inside each
  detected shot.

## 2026-11-09 — F-05 Farneback dense optical-flow motion-energy curve + cut-point energy contrast

- **Detects:** (a) whether motion energy peaks ON each cut — the
  "montage timing" percept GAP-1 names; (b) frozen runs inside segments
  (GAP-3's halted moments), with direction, not just magnitude.
  GAP-1 + GAP-3.
- **How it works:** OpenCV `cv2.calcOpticalFlowFarneback` gives a dense
  flow field between consecutive frames; mean flow magnitude per frame
  is the motion-energy curve. At each cut, compare mean flow in the 12f
  before vs the 12f after: a cut that lands with high flow on both sides
  is a cut on action; a cut into or out of near-zero flow reads as a
  halt. Inside a segment, any run of ≥24f with flow magnitude at the
  noise floor is a freeze. The practitioner rule behind it comes from
  the beat-sync-editing craft (iart-ai/motion-design-skills): "cut
  during a movement so the brain tracks the action through the cut;
  match direction and speed across the cut; for motion graphics, cut on
  a transform peak — at the moment a shape is mid-travel, not at rest."
  Flow direction lets that match be checked, not just asserted.
- **Run / replicate here:** `pip install opencv-python`; per frame pair
  `flow = cv2.calcOpticalFlowFarneback(prev, next, None, 0.5, 3, 15, 3,
  5, 1.2, 0)`; magnitude = mean of `cv2.magnitude(flow[...,0],
  flow[...,1])`; emit one value per frame, join with the beat grid and
  cut list. No learned model, no weights — runs on CPU.
- **What it would have caught in MV-8 v2:** cuts placed exactly on the
  beat grid that still read as badly timed, because the motion energy
  around them was flat or one-sided — placement was exact, the percept
  wasn't, and this is the number that separates the two. Also the
  halted moments: frozen heads/tails inside segments show as zero-flow
  runs.
- **Limits:** Farneback is noisy on AI-generated footage (morphing
  textures read as flow); needs a per-project noise floor, ideally
  calibrated on a known-moving vs known-still pair. Global camera moves
  (pans/zooms) inflate the magnitude — a pan is not subject motion, so
  a pure magnitude curve can bless a panning still. RAFT (Teed & Deng,
  ECCV 2020, https://github.com/princeton-vl/RAFT, arXiv:2003.12039)
  is the sharper but heavier alternative if Farneback's noise floor
  proves unusable.
- **Status:** UNTESTED. Test: compute the curve on one MV-8 v3 montage
  segment with a known good cut and one v2 segment the user called
  badly timed; pass bar is a visible energy-contrast difference at the
  cut.

## 2026-11-09 — F-06 FFmpeg MPEG-7 signature + videohash2 perceptual-hash reuse detection

- **Detects:** a take, shot, or frame range appearing twice in a cut —
  footage reuse, including re-encoded, resized, or slightly re-timed
  copies that byte comparison misses. Standing weak spot (4).
- **How it works:** two stages. (1) Whole-take near-duplicate: videohash2
  samples one frame per second, shrinks each to 144×144, tiles them
  into a collage, and wavelet-hashes it to 64 bits; two encodes of the
  same footage land a few bits apart (Hamming distance, start tight,
  single digits). (2) Containment — a clip inside a longer master:
  FFmpeg's built-in MPEG-7 `signature` filter fingerprints every frame
  and searches for matching sequences across inputs, reporting where a
  clip occurs inside a longer video. Run stage 1 across all takes in a
  volley to catch a re-fired take reused under a new name; run stage 2
  of the master against every take to catch a segment used twice.
- **Run / replicate here:** `pip install videohash2` (needs FFmpeg);
  `from videohash2 import VideoHash; int(VideoHash(path=...).hash_hex,
  16)` then Hamming distance between takes. Signature:
  `ffmpeg -i master.mp4 -i take.mp4 -filter_complex
  signature=filename=sig.xml -f null -` (filter shipped in FFmpeg
  since 2017). Reference write-up:
  https://dev.to/masonwritescode/build-a-three-stage-video-dedup-worker-sha-256-perceptual-hash-then-ffmpegs-mpeg-7-signature-578l
- **What it would have caught in MV-8 v2:** any take or shot range the
  assembly used twice — the v2 verdict's reuse complaint ("reused
  footage is the biggest slopcannon sin") currently relies on the
  coordinator remembering every take; this makes it a checkable number.
- **Limits:** videohash2 cannot tell you a clip is *inside* a longer
  video (whole-video collage hash only) — that is what the signature
  stage is for. Rotation beyond ~10° or reversal defeats the hash.
  The signature filter is block-based and its docs warn of limited
  robustness; near-duplicate thresholds need calibration on our own
  takes (two different takes of the same scene can hash close).
- **Status:** UNTESTED. Test: hash all takes of one v3 volley pairwise
  (expect distinct takes far apart, Hamming >20) and run the signature
  filter of the v3 master against a take known to appear once (expect
  exactly one match location).

## 2026-11-09 — F-07 BeatNet downbeat / meter tracking (phrase-level grid)

- **Detects:** downbeats and meter — the phrase-level structure of the
  song — so cuts can land on phrase boundaries, not just on beats.
  Song-as-authority avenue; supports GAP-4 and the "cuts on phrases"
  half of GAP-1.
- **How it works:** BeatNet (Heydari, Cwitkowitz & Duan, ISMIR 2021) is
  a causal CRNN that outputs beat/downbeat activations from audio,
  followed by particle filtering (online) or a madmom dynamic Bayesian
  network (offline) to infer beat, downbeat, tempo, and meter jointly.
  It needs no priming time signature and estimates meter as it goes.
  Our current grid is beat-only (MV-8: 123.05 BPM, `beat_grid_v2.json`);
  downbeats add the bar lines, which is where phrase-level cuts and
  the Outro build's turning points live.
- **Run / replicate here:** `pip install git+https://github.com/mjhydri/BeatNet`
  (PyTorch; offline mode: `BeatNet(1, mode='offline',
  inference_model='DBN')`); paper https://arxiv.org/abs/2108.03576.
  Compare its downbeats against the existing beat grid — every
  downbeat should coincide with a beat, and the bar count should match
  the song's phrasing.
- **What it would have caught in MV-8 v2:** nothing directly — v2's
  cuts were on the beat grid. What it adds is the next rung: cuts that
  land on a beat but mid-phrase, where a phrase-boundary cut would have
  carried the crescendo-map accents (63.32 hit, 112.25/112.72 pair,
  170.9–174.7 cluster, 159.435 peak) instead of fighting them.
- **Limits:** trained on mastered songs (GTZAN/Ballroom/Rock Corpus);
  Suno's chant/brass-stab texture is off-distribution and downbeat
  accuracy may drop — validate against the hand-built crescendo map
  before trusting it. Offline DBN mode is the one to use; the online
  particle filter is for realtime, not for our batch assembly.
- **Status:** BLOCKED on this VM — TESTED as far as the install goes, no
  tracker run possible (2026-11-11 sprint #2). BeatNet 1.1.1 installs
  cleanly on the lyrics venv (`pip install beatnet`, torch 2.15.0+cpu),
  but it imports madmom at THREE points — `log_spect.py` (STFT /
  spectrogram feature extraction), `particle_filtering_cascade.py`
  (HMM bar state spaces for the PF decoder), and `BeatNet.py` (the DBN
  decoder) — so BOTH inference paths (PF and DBN) need madmom, and
  madmom cannot build on Python 3.12 (F-13: `longintrepr.h` removed).
  There is no python3.11/3.10 on this box (only 3.12), so the ≤3.11
  venv path needs a whole Python install first. **F-07 and F-13 are
  the same wall, not two independent paths** — BeatNet's decoding IS
  madmom. Do not shim madmom: the feature-extraction and HMM layers
  are the work itself. The MV-14 beat comparison from BeatNet is
  STILL OWED; next path is a Python ≤3.11 venv with madmom + BeatNet
  together, as its own job.
  Fallback second opinion (NOT BeatNet): librosa `beat_track` on the
  MV-14 track (`librosa_beat_mv14.py`, `librosa_beat_mv14.json`) —
  tempo AGREES (92.29 vs measured 92.0 BPM, median IBI 0.6502s vs
  0.649s; 238 beats, ~30–31 per 20s window as expected; drift −0.023s
  over the track) but per-beat phase is LOOSE (median |offset| 0.145s;
  only 40% within 100ms; section-dependent, median offset swings
  +0.19s to −0.23s by 20s window; first beat 3.808s — the intro is
  missed). Verdict: the measured grid's TEMPO is confirmed, its
  single global PHASE is not trustworthy beat-by-beat — per-word ASR
  anchors stay the timing authority. Original test (downbeats vs the
  63.32 / 112.25 / 159.435 accents) still unrun.
  UPDATE 2026-11-11 (sprint #3, SLERM-C11): the independent second
  opinion the BeatNet comparison was FOR now exists in C11 —
  `c11_beat/beat_tracker.c` (Ellis DP, `SPRINT_2026-11-11_C11_BEAT.md`):
  front end validated (flux corr 1.0000 vs scipy), DP beats beat
  librosa on every grid metric (median |offset| 0.088s vs 0.145s) and
  agree with librosa at median 0.035s — same verdict, stronger. The
  BeatNet/madmom comparison itself is still owed from those
  libraries; the C11 BLSTM + DBN (path b) is the follow-up, reusing
  this sprint's STFT/flux core.

## 2026-11-09 — F-08 Audio-energy vs visual-motion envelope correlation (song-vibe fit)

- **Detects:** whether the picture's energy follows the song's energy
  curve per section — the "vibes" proxy GAP-4 asks for. A section
  where the song builds and the picture goes flat is a mismatch even
  if every cut is on a beat.
- **How it works:** two curves on the same timeline. Audio side:
  librosa `onset_strength` (spectral-flux novelty, the standard onset
  envelope) plus an RMS energy curve, both from the song master. Visual
  side: per-frame motion magnitude from F-05 (Farneback mean flow) or
  frame-diff mean, from the rendered master. Normalise both per
  section (Intro / verses / chant / Outro), then take the Pearson or
  Spearman correlation per section and the lag of peak cross-correlation
  (±0.5s window). High correlation = picture breathes with the song;
  near-zero or negative in a build section (e.g. the 41s Outro climb
  to the 159.435 true peak) = the picture is ignoring the song.
- **Run / replicate here:** `pip install librosa`;
  `y, sr = librosa.load(song); onset_env =
  librosa.onset.onset_strength(y=y, sr=sr)` and
  `rms = librosa.feature.rms(y=y)`; resample both envelopes and the
  motion curve to a common frame grid (24fps master), correlate per
  section. Onset docs: http://librosa.org/doc/main/auto_tutorials/01-intro/05-onsets.html
- **What it would have caught in MV-8 v2:** the verdict's "you did not
  use the timing of the song properly or the song vibes" as a number
  per section — v2 was beat-locked in places and still missed the
  vibes, which is exactly a low envelope correlation with correct
  cut placement.
- **Limits:** correlation is a blunt proxy — a deliberately still,
  held shot over a loud passage can be a valid choice (tension), so a
  low score is a flag for eye review, never an auto-fail. Onset
  strength on a chant track is dominated by brass stabs; the RMS curve
  may be the fairer audio side for the Outro build. Needs the same
  section boundaries the scene plan already uses, or the correlation
  mixes unlike parts.
- **Status:** UNTESTED. Test: compute both curves on the MV-8 v3 master
  and correlate per section; pass bar is high correlation in the Outro
  build and in the stab sections, and the v2 master scoring lower than
  v3 in at least the section the user flagged.

## 2026-11-10 — F-09 FFmpeg `freezedetect` (native frozen-frame finder)

- **Detects:** frozen runs — stretches where the picture stops changing —
  directly on a master or a take, with start time and duration per
  freeze. GAP-3 (halted moments) and the "frozen heads/tails" half of
  GAP-1.
- **How it works:** the filter computes the mean average absolute
  difference of all frame components against a reference frame and
  compares it to a noise floor; when the difference stays under the
  floor for longer than the duration threshold it logs a freeze with
  `lavfi.freezedetect.freeze_start`, `freeze_duration`, and
  `freeze_end` metadata. It is the one FFmpeg filter built for exactly
  this question — the v3 interim method (per-segment frame-diff with a
  hand-set floor) is a reimplementation of it, minus the logging.
  Practitioner confirmation: a Mastodon post (2026-10-30) from a
  generated-video reviewer — "A 1.04 s freeze slipped through our
  review of a generated 20 s clip: one take reached its pinned end
  frame early and held it. Sampled stills all looked fine" — their
  added check is `ffmpeg -vf freezedetect=n=0.003:d=0.3`; it flagged 11
  spots in the rejected cut and 7 in the approved one, and they judge
  by freeze LENGTH, not count ("Only the bug ran past 1 s"). That is
  exactly our failure mode: a take that reaches its end frame early
  and holds it reads as a still in every sampled frame.
- **Run / replicate here:** already installed — FFmpeg 8.1.2 on this VM
  ships `freezedetect` (verified 2026-11-10; also ships `scdet`,
  `mpdecimate`, `blackdetect`, `signature`). Command:
  `ffmpeg -i master.mp4 -vf freezedetect=n=0.003:d=0.3 -f null - 2>&1`
  (tune `n` per project: default 0.001 is below AI-footage sensor/morph
  noise, so a whole clip reads as one long change; the practitioner
  value 0.003 and the dev.to walkthrough's 0.02 are the calibration
  range to try). Parse the log lines into freeze intervals and join
  them against the cut list — a freeze that starts within ~12f after
  a cut is a frozen head; one ending just before a cut is a frozen
  tail. Companion: `mpdecimate` (same build) drops near-duplicate
  frames — run it as a second opinion on the same footage; a segment
  it collapses to a handful of frames is a freeze by another name.
- **What it would have caught in MV-8 v2:** the halted moments in the
  verdict — frozen heads/tails inside montage segments that the
  whole-master frame-diff hid and that sampled stills cannot show,
  with exact timestamps instead of an eye-found "somewhere in the
  middle". A freeze ≥1s is the auto-fail line the practitioner rule
  suggests; shorter freezes are a flag for eye review.
- **Limits:** mean-over-frame dilution — the same aggregation trap the
  S-16 clock check taught us: a small moving object (a hand, a
  droplet) inside a mostly-still frame can lift the mean above the
  floor and mask a freeze of the subject. Calibrate `n` per project
  on a known-moving vs known-still pair; do not trust the default.
  It also cannot tell a deliberate hold (a live settle) from a dead
  freeze — length is the discriminator, not presence. It respects no
  cut boundaries by itself: run it per segment (after F-04/F-10/F-12
  cut detection) or it will report freezes that span cuts.
- **Status:** TESTED 2026-11-10 (run 3): ran on the MV-8 v3 house master
  (`masters/mv8_wipe_and_its_still_there_v3_16x9.mp4`, 4493f, 187.2s) at
  `n=0.003:d=0.5` — ZERO freezes ≥0.5s across the whole master, so zero
  ≥1s freezes: v3 passes the practitioner auto-fail line. Control:
  the same command on a deliberately frozen 3s clip fired
  `lavfi.freezedetect.freeze_start: 0`, so a zero on v3 is a real
  negative, not a silent filter. v2 comparison DONE, and it is a
  NEGATIVE result: the rejected v2 master also shows ZERO freezes
  ≥0.5s at n=0.003/d=0.5 AND at n=0.02/d=1.0 — freezedetect does NOT
  discriminate v2 from v3. The halted moments the user called in v2
  are either sub-0.5s holds or masked by mean-diff dilution (a small
  moving element lifting the frame mean — the bank's own stated
  limit). Do NOT trust freezedetect alone for the halted-moment gate;
  the per-segment motion audit (F-05) / mpdecimate second opinion is
  still needed. Note: `d=0.5` used, not the banked `d=0.3`.
- **2026-11-11 sprint re-run:** `n=0.003:d=0.3` (the practitioner value
  the bank named) on BOTH masters — v3: ZERO freezes; v2: ZERO freezes.
  The negative result survives the tighter duration threshold, so the
  halted moments in v2 are sub-0.3s holds, mean-dilution-masked holds,
  or slow motion rather than freezes — which is exactly what F-17's
  M6 duplicate ratio (share-based, no duration threshold) then found.
  Per-segment freezedetect is moot: the whole-master log has no freeze
  intervals at all, so no segment has one either.

## 2026-11-10 — F-10 TransNetV2 learned shot-boundary detection

- **Detects:** true shot boundaries (hard cuts AND gradual transitions —
  dissolves, fades, wipes) in a flattened master, frame-accurate, as
  the segmentation every per-shot audit needs. GAP-3 (and the
  segmentation GAP-1 needs). Upgrades F-04 (PySceneDetect): a learned
  model instead of a hand threshold on colour differences.
- **How it works:** TransNetV2 (Souček & Lokoč, arXiv:2008.04838) is a
  CNN over 100-frame windows — stacked dilated (2+1)D convolutions
  plus a frame-similarity module — outputting a per-frame transition
  probability, thresholded (default 0.5) into scene boundaries. On
  public benchmarks it re-scores F1 77.9 (ClipShots), 96.2 (BBC Planet
  Earth), 93.9 (RAI), ahead of the classical methods PySceneDetect
  implements. The PyTorch port is inference-only, pip-installable,
  and produces identical results to the original TensorFlow version.
  Why it matters here: our montage is fast-cut AI footage with
  morphing textures, where a colour-difference threshold (F-04) is
  exactly the thing that misfires — a learned boundary model is
  trained to tell "the world changed" from "the texture shimmered".
- **Run / replicate here:** `pip install transnetv2-pytorch` (PyTorch;
  CPU works — the model runs on 48×27 frames); CLI:
  `transnetv2_pytorch path/to/video.mp4` or Python
  `model.detect_scenes("video.mp4")`. Original repo:
  https://github.com/soCzech/TransNetV2 — paper:
  https://arxiv.org/abs/2008.04838 — PyPI:
  https://pypi.org/project/transnetv2-pytorch/
- **What it would have caught in MV-8 v2:** the same freezes F-04
  would have exposed, but with fewer false cuts on morph-heavy AI
  footage and with gradual transitions (dissolves/whips) detected
  that a content-difference threshold under-triggers on. Also gives
  the independent cut list to cross-check against the assembly's
  planned cuts (a detected cut where none was planned = flash-frame
  or warp artefact) with higher precision than F-04.
- **Limits:** trained on real camera footage (ClipShots/BBC/RAI), not
  AI-generated morphing video — boundary precision on our material
  is unmeasured and could be worse than the benchmarks; validate
  against the planned cut list before trusting it. Runs on tiny
  48×27 frames, so it can miss cuts that are obvious at full res
  but subtle at thumbnail scale. CPU inference on a 3-minute master
  is minutes, not seconds.
- **Status:** UNTESTED. Test: run on the MV-8 v3 master, compare its
  cut list to the assembly's planned cuts (expect near-1:1, and
  strictly fewer false positives than F-04's `detect-content` on the
  same master); then run the per-shot diff audit (F-05) inside each
  detected shot.

## 2026-11-10 — F-11 Essentia per-section energy / arousal / beats-loudness (song-vibe fit)

- **Detects:** the song's energy shape per section — not just loudness,
  but per-beat loudness in six frequency bands, learned
  arousal/valence (energy + positivity), and danceability — so the
  picture's energy can be checked against a musical energy curve
  instead of a raw RMS curve. GAP-4 (song-vibe fit); the song-side
  half of F-08, with more structure than librosa RMS/onset.
- **How it works:** Essentia (Music Technology Group, UPF) is the
  open MIR library behind AcousticBrainz. Its music extractor
  computes, per frame and per beat: `beats_loudness` (spectral energy
  on each beat segment, whole spectrum + ratios in 6 bands —
  [20–150Hz] bass, [150–800Hz], [800Hz–4kHz], [4kHz–20kHz]), EBU R128
  loudness, spectral energy bands, and the high-level learned models
  `danceability` and `arousal_valence` (DEAM-trained: arousal =
  energy, valence = positivity, each 0–1). The per-beat loudness is
  the key addition over F-08: it turns the song into a beat-by-beat
  energy series in which the brass stabs (high-band energy on the
  beat) and the slap-bass groove (low-band energy) are separable, so
  a section's "punch" can be scored per band instead of as one RMS
  number. The arousal curve is the closest thing to a machine
  "vibe" number: a section where arousal climbs (e.g. MV-8's 41s
  Outro build to the 159.435 true peak) while the picture's motion
  energy stays flat is a quantified vibe miss.
- **Run / replicate here:** `pip install essentia` (wheels available;
  AGPLv3) or the prebuilt `essentia_streaming_extractor_music`
  binary, which dumps all descriptors to JSON in one pass. Python:
  `import essentia.standard as es; audio = es.MonoLoader(filename=...,
  sampleRate=44100)(); beats = es.RhythmExtractor2013()(audio)` then
  `es.BeatsLoudness(beats=beats)`; arousal/valence via the
  TensorFlow/ONNX models (`TensorflowPredictVGGish` + DEAM head).
  Extractor docs: https://essentia.upf.edu/streaming_extractor_music.html
  — algorithm list: https://essentia.upf.edu/api/docs/tutorial/algorithms/
- **What it would have caught in MV-8 v2:** the verdict's "you did
  not use the timing of the song properly or the song vibes" as a
  per-section, per-band number — v2's picture went flat where the
  song's per-beat loudness and arousal climbed, which a single RMS
  curve (F-08) shows only coarsely. The band split also separates
  "the brass stab got no visual accent" (high-band beat loudness
  spike, no motion spike) from "the groove got no visual accent"
  (low-band), which are different fixes.
- **Limits:** Essentia's high-level models are trained on mastered
  commercial music; Suno's chant/brass-stab texture is
  off-distribution and the absolute arousal/danceability numbers may
  shift — use them comparatively (v2 vs v3, section vs section), not
  as absolute scores. The `essentia` pip wheel is large and its
  install on this VM is untested; the extractor binary is the
  fallback. Arousal is still a proxy: a deliberately still held shot
  over a loud passage can be valid tension, so a low score is a flag
  for eye review, never an auto-fail (same caveat as F-08).
- **Status:** UNTESTED. Test: run the extractor on the MV-8 song,
  plot per-beat loudness (low vs high band) and the arousal curve
  against the crescendo map (63.32 hit, 112.25/112.72 pair,
  170.9–174.7 cluster, 159.435 peak); pass bar is the arousal curve
  rising through the Outro build and the band split separating the
  brass stabs from the bass groove. Then correlate per section
  against the v3 motion curve (F-08's method, Essentia's audio side).

## 2026-11-10 — F-12 FFmpeg `scdet` scene-change score (zero-install cut detector)

- **Detects:** cut points in a master as a per-frame scene-change score
  — the cheap, zero-install baseline for the segmentation GAP-3 and
  GAP-1 need, before reaching for F-04 (install) or F-10 (model).
- **How it works:** FFmpeg's `scdet` filter computes the mean absolute
  difference between consecutive frames and exposes it as the
  `lavfi.scdet.mafd` / `lavfi.scdet.score` metadata per frame; the
  `select` filter can surface the same score (`gt(scene,0.4)`).
  Threshold the score series and the peaks are the cuts. It is the
  same family of detector as PySceneDetect's `detect-content` (F-04)
  — a colour-difference threshold — but it ships inside the FFmpeg
  already on this VM, runs in a single pass at decode speed, and
  needs no Python, no venv, and no weights. A dev.to walkthrough
  (2026) testing three FFmpeg filters on a still-camera clip found
  the scene score "built for edits" and usable for exactly this
  segmentation job.
- **Run / replicate here:** already installed — FFmpeg 8.1.2 ships
  `scdet` (verified 2026-11-10). Command:
  `ffmpeg -i master.mp4 -vf "scdet=s=0.1,metadata=print:key=lavfi.scdet.score" -f null - 2>&1`
  or the classic form
  `ffmpeg -i master.mp4 -vf "select='gt(scene,0.4)',showinfo" -f null - 2>&1`
  (tune the threshold on the score series; AI footage's morph noise
  raises the floor, so pick it from the distribution, not the
  default). Parse the printed scores into a cut list and cross-check
  against the assembly's planned cuts.
- **What it would have caught in MV-8 v2:** the same per-shot
  segmentation F-04 promises — the prerequisite for any per-shot
  motion audit — with no install step, so the audit can run on any
  machine that has FFmpeg. A detected cut where none was planned is
  still the flash-frame / warp-artefact flag.
- **Limits:** a single global threshold on mean frame difference —
  the crudest of the three cut detectors in this bank (F-04, F-10,
  F-12). Morphing AI textures inflate the score and can over-trigger
  on fast motion; slow dissolves under-trigger. It is the baseline
  to beat, not the detector to trust alone: use it to segment, then
  confirm the cut list against the planned cuts and against F-10
  where they disagree.
- **Status:** TESTED 2026-11-10 (run 3): ran on the MV-8 v3 house master
  (4493f, 187.2s). Correction to the banked command: `scdet=s=...`
  is INVALID on FFmpeg 8.1.2 — `s` parses as boolean and errors; the
  option is `threshold`, i.e. `scdet=threshold=20`. The metadata key
  is `lavfi.scd.score`, not `lavfi.scdet.score`. Results:
  threshold=10 → 180 events, over-fires badly (dense every-frame
  clusters 22–28s and 112–120s = fast motion, not cuts) — unusable
  as a cut list. threshold=20 → 15 events at 5.96, 16.08, 28.63,
  30.0, 63.63, 65.13, 81.67, 85.25, 85.96, 88.96, 93.0, 102.33,
  156.0, 163.0, 171.83s. v3 has 17 segments (~16 expected internal
  cuts), so 15 detections is in the right ballpark — threshold 20 is
  the calibrated baseline for this material. Cross-check against the
  planned cut list and F-04/F-10 still owed.
- **2026-11-11 sprint cross-check (planned cuts from SCENE_PLAN_v3.md,
  16 internal boundaries):** re-ran threshold=20 on v3 — same 15 peaks,
  reproducible. At ±2f tolerance v3 hits only 4/16 planned cuts (5.96,
  65.12, 93.00, 163.00); 81.67 is the 81.08 boundary detected 14f late
  (a slow transition — TSM M5 shows the same 0.6s lag on both masters).
  The other 11 peaks are REAL cuts but INTERNAL ones: insert cutaways
  (16.08, 63.62) and take joints inside scenes the plan builds from 2
  takes cut on beats (28.62, 30.00, 85.25, 85.96, 88.96, 102.33, 156.00,
  171.83). The count matched (15 vs 16) BY COINCIDENCE, not by identity
  — do not validate a cut list by count. Same command on v2: 15 peaks,
  8/16 planned hits (5.96, 45.50, 81.08, 93.00, 105.96, 133.46, 163.00,
  180.00) — v2's cuts read harder than v3's softer/whip transitions.
  Verdict: threshold=20 is a TAKE-JOINT detector on this material, not
  a scene-boundary detector. Use it to segment per-take, never as proof
  the scene plan was followed.

---

## 2026-11-11 — F-13 madmom RNN beat/downbeat tracking + CNN/RNN onset detection

- **Detects:** beats, downbeats, tempo, and note onsets from the song with
  pretrained neural models — the classical MIREX-era baseline to
  cross-check F-07 BeatNet against, and the onset detector F-08's
  librosa onset_strength lacks. GAP-1 (phrase-level grid) + GAP-4
  (song-side energy/onset curve) + the song-as-authority avenue.
- **How it works:** madmom (Böck et al., JKU Linz / OFAI) ships
  pretrained models with the library: `RNNBeatProcessor` turns audio
  into a beat-activation function, `DBNBeatTrackingProcessor` (dynamic
  Bayesian network) infers the beat sequence jointly with tempo;
  `RNNDownBeatProcessor` + `DBNDownBeatTrackingProcessor` do the same
  for downbeats and meter; `CNNOnsetProcessor` / `RNNOnsetProcessor`
  (Böck & Schedl's bidirectional-LSTM universal onset detector) give a
  per-frame onset activation, peak-picked into onset times. The DBN
  exposes its transition/observation model, so a tempo prior from the
  measured BPM can be fed in instead of trusting a blind estimate.
  BeatNet (F-07) is a newer CRNN + particle filter; madmom is the
  older, fully transparent, CPU-only counterpart — two independent
  trackers disagreeing on a downbeat is itself a signal.
- **Run / replicate here:** `pip install madmom` (PyPI:
  https://pypi.org/project/madmom/ — repo
  https://github.com/CPJKU/madmom, paper
  https://doi.org/10.1145/2964284.2973795). CLI:
  `DBNBeatTracker single -o beats.txt song.mp3` and
  `DBNDownBeatTracker single -o downbeats.txt song.mp3`; Python:
  `from madmom.features.beats import RNNBeatProcessor,
  DBNBeatTrackingProcessor, RNNDownBeatProcessor,
  DBNDownBeatTrackingProcessor` and `from madmom.features.onsets
  import CNNOnsetProcessor, PeakPickingProcessor`.
- **What it would have caught in MV-8 v2:** nothing v2 missed on the
  beat grid — same as F-07. What it adds: an independent second
  opinion on every downbeat (phrase boundaries for the crescendo-map
  accents) and a learned onset curve for the brass stabs that
  librosa's spectral-flux onset envelope (F-08) only approximates —
  the onset curve is the song-side half of the F-08/F-11 vibe
  correlation, with sharper stab timing.
- **Limits:** last PyPI release is 0.15.1 (2017) — C extensions may
  need building on modern Python, and the pretrained models are
  MIREX-2015-era, trained on real-instrument corpora; Suno's
  chant/brass texture is off-distribution, so validate against the
  hand-built beat grid and crescendo map before trusting it, exactly
  as with F-07. No GPU path — CPU only, which fits this VM but is
  slow on long tracks.
- **Status:** INSTALL FAILED on this VM — TESTED as far as the install
  goes, no tracker run possible. 2026-11-11 sprint: fresh venv at
  `detection-research/venv/` (Python 3.12.3). `pip install madmom`
  (PyPI now serves **0.16.1**, not the banked 0.15.1) fails twice: (1)
  isolated build — madmom's `setup.py` imports Cython at build time
  (`ModuleNotFoundError: No module named 'Cython'`); (2) with Cython
  0.29.37 + numpy 1.26.4 + scipy 1.17.1 pre-installed and
  `--no-build-isolation` — the C extension build dies at
  `madmom/ml/nn/layers.c:211:12: fatal error: longintrepr.h: No such
  file or directory`. That header is a CPython internal removed from
  the public include path in Python 3.12; madmom 0.16.1's
  Cython-generated C cannot build on 3.12 without patching. (Side note:
  PyPI downloads over the egress proxy retried with RemoteDisconnected
  several times before succeeding — flaky, not fatal.) No
  DBNBeatTracker / DBNDownBeatTracker run exists, so the MV-14
  92.0 BPM grid comparison (period 0.649s, phase 0.240s) is STILL OWED.
  Next paths, in order: (a) a Python ≤3.11 venv for madmom; (b) BeatNet
  (F-07) on the lyrics venv's torch stack instead. Do not retry the
  3.12 build — the failure is a removed CPython header, not a missing
  dependency.
  UPDATE 2026-11-11 (sprint #2): path (b) is the SAME WALL, not an
  independent path — BeatNet 1.1.1 imports madmom at three points
  (feature extraction, PF HMM state spaces, DBN decoder), so it
  cannot run on 3.12 either. And there is no python3.11/3.10 on this
  box (only 3.12), so path (a) now needs a whole Python install
  first. The single remaining path is one job: install Python ≤3.11,
  venv, madmom + BeatNet together, then run both comparisons in one
  pass. Fallback while blocked: librosa `beat_track` (already in the
  lyrics venv) confirms the MV-14 grid's TEMPO (92.29 vs 92.0 BPM)
  but not its global phase — see F-07.

## 2026-11-11 — F-14 AV-HuBERT visual speech recognition (lip-reading the mouth)

- **Detects:** WHAT the mouth is saying, from the picture alone — a
  visual-only transcription of the singer's lips, compared word by
  word against the lyric line. GAP-2. This is the question F-01
  (is the mouth in sync?) and F-03 (is the mouth open?) cannot ask:
  a mouth can be open on the beat and still shape the wrong word.
- **How it works:** AV-HuBERT (Shi et al., Meta AI, arXiv:2201.02184)
  is a self-supervised audio-visual transformer: masked multimodal
  cluster prediction over lip-movement frames + audio, pre-trained on
  unlabelled video, then fine-tuned for lip-reading with the audio
  stream dropped — so at inference it reads words from lip motion
  only. On LRS3 it reaches 26.9% word error rate with all 433h of
  labelled data (32.5% with only 30h), against 33.6% for the previous
  state of the art trained on 31,000 hours. Run it on the warped
  insert render's mouth crop, transcribe, and align the read words
  to the song's word timings: a word the model reads differently
  from the lyric (or cannot read at all — low confidence / deletion)
  is a lipsync miss at word level. Newer alternative: Auto-AVSR
  (Ma et al., Imperial, arXiv:2303.14307,
  https://github.com/mpc001/auto_avsr) — ResNet-18 visual encoder +
  Conformer, visual-only WER 20.3% on LRS3 with augmented training
  data; Llama-AVSR (2025, ICASSP) pushes AVSR to 0.77% WER but is
  audio-visual, not visual-only, so it cannot isolate the mouth.
- **Run / replicate here:** code and pretrained models:
  https://github.com/facebookresearch/av_hubert — paper
  https://arxiv.org/abs/2201.02184. Pipeline: crop the mouth region
  per frame (MediaPipe face mesh from F-03 gives the landmarks;
  AV-HuBERT expects a 96×96 lip crop at 25fps), feed the clip,
  decode with the fine-tuned lip-reading checkpoint, align output
  words to SONG_WORDS. Auto-AVSR: https://github.com/mpc001/auto_avsr.
- **What it would have caught in MV-8 v2:** inserts where the mouth
  moves in time but shapes the wrong lyric — the exact "bad lipsync
  timing" the user heard, at the level of individual words, measured
  from the picture with no reliance on take audio. A painted-smile
  structural case (MV-3 S13) reads as deletions across the whole
  line — a detectable signature, not a surprise at assembly.
- **Limits:** trained on real talking heads (BBC/TED speech), not
  sung vocals over a music bed and not stylised/cartoon faces —
  off-distribution twice over, so a local calibration is mandatory
  (run it on a known-good MV-7 insert first and record its baseline
  WER before trusting any verdict). Singing stretches vowels and
  distorts visemes relative to speech; chant tracks are the worst
  case. Needs a visible, trackable mouth — profile shots and
  occluded mouths fail silently, so "no mouth crop" must be a FAIL,
  not a skip (same rule as F-03). Transformer inference is heavy:
  GPU preferred; this VM's 1.5 CPUs will be slow, so run it per
  insert in the background, not on whole masters.
- **Status:** UNTESTED. Test: run the lip-reading checkpoint on one
  MV-7 warped insert with known-good lipsync and one known-bad MV-8
  v2 insert; pass bar is the read words matching the lyric line on
  the good one (well above chance) and visibly disagreeing on the
  bad one. If AV-HuBERT's WER is unusable on sung cartoon faces,
  try Auto-AVSR's VSR model before writing the approach off.

## 2026-11-11 — F-15 MSAF automatic song-structure segmentation (section boundaries)

- **Detects:** where the song's sections actually start and end
  (intro / verse / chorus / bridge / outro boundaries, plus which
  sections repeat each other) — from the audio, not from the
  hand-built scene plan. Song-as-authority avenue; supplies the
  section boundaries F-08 and F-11 need before their per-section
  correlations mean anything. GAP-4.
- **How it works:** MSAF (Nieto & Bello, ISMIR 2016) is the open
  Music Structure Analysis Framework: interchangeable feature
  extractors (MFCC, CQT, chroma, tempograms) feed interchangeable
  boundary algorithms (Foote novelty, OLDA ordinal LDA, spectral
  clustering, 2D-FMC, CNMF, SF) and labelling algorithms
  (spectral clustering groups repeated sections). The standard
  recipe is `msaf.process(audio_file)` → boundaries + labels. A
  2026 wrapper, zigify-msaf, pins the combination that scored best
  against hand-annotated ground truth (OLDA boundaries + scluster
  labels: 9 of 14 boundaries hit on Thriller at ±5s tolerance, 2
  spurious) and adds per-segment BPM and beat lists.
- **Run / replicate here:** `pip install msaf`
  (https://github.com/urinieto/msaf — paper: Nieto & Bello,
  "Systematic Exploration of Computational Music Structure
  Research", ISMIR 2016); Python:
  `boundaries, labels = msaf.process(audio_file)` or
  `msaf.process(audio_file, boundaries_id="olda",
  labels_id="scluster")`. Wrapper:
  `uvx zigify-msaf track.mp3 --out track.segments.json`
  (https://pypi.org/project/zigify-msaf/).
- **What it would have caught in MV-8 v2:** nothing directly — v2's
  sections were hand-planned. What it adds is an independent check
  on the plan itself: if MSAF puts a section boundary 2 bars away
  from where the scene plan assumed the chorus starts, every
  per-section vibe correlation (F-08/F-11) and every phrase-boundary
  cut (F-07/F-13) was being scored against the wrong section. It
  also gives the repeat structure (which sections are the same
  material returning) — a montage that treats a returning chorus
  as new material is a vibe miss.
- **Limits:** boundary tolerance in the literature is ±0.5–3s, far
  coarser than our ±2f cut grid — MSAF boundaries are section
  guides, never cut placements. Labels are abstract clusters
  (A/B/C), not "verse"/"chorus" names; mapping them to the scene
  plan is a hand step. Accuracy on Suno's chant/brass texture is
  unmeasured; the Thriller evaluation is one track. Short tracks
  and tracks with long intros can produce leading sliver segments
  (the zigify wrapper absorbs segments under 3s by default).
- **Status:** UNTESTED. Test: run MSAF (olda + scluster) on the MV-8
  song; pass bar is boundaries within ±3s of the hand-built section
  plan (intro / verses / chant / Outro) and the Outro build's
  turning points, with repeated choruses sharing a label.

## 2026-11-11 — F-16 Demucs vocal-stem isolation (clean vocal track for word timing)

- **Detects:** nothing by itself — it is the separator that makes
  the other song-side finders work on chant tracks: a clean vocal
  stem, a clean drums stem, and a clean accompaniment stem from the
  mixed Suno master. Song-as-authority avenue; supports GAP-2 (via
  cleaner word timings for F-02's phoneme approximation) and GAP-4
  (via clean per-instrument energy curves for F-08/F-11).
- **How it works:** Demucs v4 / HT-Demucs (Défossez et al., Meta AI,
  ICASSP 2023) is a hybrid waveform + spectrogram U-Net with a
  cross-domain transformer, trained to split a stereo mix into
  vocals / drums / bass / other (9.20 dB SDR on MUSDB18, 9.0 dB
  for the base `htdemucs` checkpoint; `htdemucs_ft` is a
  four-checkpoint bag, better on vocals, ~4× slower). The MV-11
  lesson already established the principle — separated vocals only
  for long dense spans where the mix loops — but no separator was
  ever banked as a tool. With a vocal stem, faster-whisper word
  timings are measured on voice alone instead of voice + brass +
  bass, which is exactly where the mix-loop confusion came from;
  with a drums stem, beat/onset tracking (F-07/F-13) gets a clean
  pulse source; with the "other" stem, the brass-stab accents in
  the crescendo map get a clean energy curve.
- **Run / replicate here:** `pip install demucs` (PyTorch);
  `demucs --two-stems=vocals song.mp3` → 
  `separated/htdemucs/song/vocals.wav` (or full four stems by
  default). Repo: https://github.com/facebookresearch/demucs
  (official repo now archived; the author maintains a fork at v4.1
  with bug fixes) — paper https://arxiv.org/abs/2211.08553.
- **What it would have caught in MV-8 v2:** the word-timing
  uncertainty underneath the bad lipsync verdict: on a chant track
  the mix loops and the ASR word times drift, so a warp built on
  drifted times lands the mouth off the word even when the
  assembly math is right. A vocal-stem re-timing gives the ground
  truth the warp should have used. It also sharpens F-08: the
  drums stem's onset curve is the song's pulse without the vocal
  and brass on top of it.
- **Limits:** separated stems are estimates, not multitracks —
  bleed remains (brass leaks into the vocal stem on dense chant
  passages), and the vocal stem can sound phasey; word timings
  from it still need the same sanity checks (no word in a gap,
  per the MV-11 pad fix). The official repo is archived, so
  future fixes live in the author's fork. Weights are described
  as research-use; this is internal QC, not a release. Heavy:
  the hybrid model wants ~7 GB of GPU memory or runs slowly on
  CPU — on this VM (1.5 CPUs / 6 GB RAM) a 3-minute track is a
  background job, not an interactive one.
- **Status:** UNTESTED. Test: separate the MV-8 song, re-run
  faster-whisper word timings on the vocal stem, and compare
  against the existing mix-based SONG_WORDS; pass bar is the stem
  timings moving words OUT of gaps and closer to the hand-checked
  onsets on at least the chant sections. Also compare the drums
  stem's onset curve against F-13's CNN onset output.

## 2026-11-11 — F-17 TSM temporal stability suite (freeze ratio, duplicate frames, flash-robust cuts, temporal signature)

- **Detects:** (a) frozen segments and duplicated frames in a take
  or master, as SHARE-based ratios with no minimum duration —
  the exact hole F-09 left open (freezedetect found zero freezes
  in both rejected v2 and accepted v3); (b) shot boundaries with a
  flash-robust rule; (c) re-encoded / re-framed duplicate clips via
  a frame-difference temporal signature — a second reuse detector
  beside F-06. GAP-3 + standing weak spot (4).
- **How it works:** TSM (preprint, October 2026) is a six-metric,
  training-free, deterministic suite on 12fps 160×90 luma frames:
  M1 activity (median frame difference); M2 freeze ratio — the
  share of transitions with mean abs-diff below τf = 0.002; M3
  flicker index — second difference of mean luma ×10³ (insensitive
  to slow fades, responds to oscillation); M4 temporal jitter
  ratio — the non-smooth share of temporal change; M5 shot
  boundaries — mean-removed frame difference ≥ 0.08 AND ≥ 3× the
  local median AND a spatial-spread test (≥ 75% of a 4×4 grid's
  cells changing ≥ 0.05), which resists camera flashes and exposure
  jumps; M6 duplicate-frame ratio — share of consecutive native-rate
  frame pairs below τd = 0.0005 (frame-rate up-conversion by
  repetition scores ≈ 0.5). The temporal signature is the
  frame-difference series itself: two clips' series correlate at
  Pearson ρ ≥ 0.9 → flag for visual review, invariant to
  re-encoding, resolution change, and moderate re-framing. The
  paper's own warning is our warning too: a 30s montage with 29
  cuts must not be scored on the same scale as a single 5s shot —
  run TSM per shot (after F-04/F-10/F-12 segmentation), not on a
  whole master. Validated on controlled perturbations (n = 15
  clips): a 1s freeze moved the freeze ratio +0.102 (15/15 hits),
  12→24fps frame duplication moved DR +0.502 (15/15), a hard cut
  was found 14/15.
- **Run / replicate here:** preprint
  https://www.preprints.org/manuscript/202610.1030 — no public
  implementation was linked in the preprint as read, but the
  method is fully specified: decode with FFmpeg
  (`ffmpeg -i clip.mp4 -vf fps=12,scale=160:90,format=gray -f
  rawvideo -`), compute the six metrics in numpy (a few dozen
  lines); M6 needs a second decode at native rate. No model, no
  weights, no venv beyond numpy.
- **What it would have caught in MV-8 v2:** the halted moments the
  user called that freezedetect could not see. F-09's negative
  result is the proof: freezedetect needs a freeze ≥ its duration
  threshold (d = 0.5s) AND a frame-mean below its noise floor, so
  sub-0.5s holds and holds masked by a small moving element (the
  S-16 clock lesson: mean-diff dilution) both pass. TSM's M2/M6
  are share-based with no duration threshold and a much tighter
  duplicate threshold (0.0005 vs freezedetect's 0.003), so a take
  that reaches its end frame early and holds it — the exact failure
  the 2026-10-30 practitioner post described — raises the
  duplicate ratio even when the freeze is short. The temporal
  signature also gives a reuse check that survives re-encoding
  and re-framing, where F-06's videohash needs the whole take.
- **Limits:** same mean-over-frame dilution as F-09 in principle —
  the thresholds are tighter but the quantity is still a frame
  mean, so a small moving object can still mask a frozen subject;
  the paper's own validation shows temporal noise ERASES the freeze
  ratio (noise masks stillness), and our AI footage has morphing
  texture noise by nature — calibrate τf/τd per project on a
  known-moving vs known-still pair. Designed for clips up to ~30s;
  on a 187s master it must run per segment or per 30s window.
  M4 jitter is relative, not an absolute threshold. The signature
  threshold ρ ≥ 0.9 is a screening convention, not a validated
  decision boundary.
- **Status:** TESTED 2026-11-11 (sprint) — PARTIAL DISCRIMINATION.
  Implementation: `detection-research/tsm.py` (numpy + one FFmpeg decode
  per master at native 24fps, 160x90 gray; 12fps series = every other
  frame). Both masters 4493f / 187.21s, same 17 planned segments
  (SCENE_PLAN_v2.md = SCENE_PLAN_v3.md boundaries), metrics per segment
  + whole-master. Results in `tsm_v2.json` / `tsm_v3.json`.
  Whole-master numbers (v2 rejected / v3 accepted):
  M1 activity 0.0697 / 0.1079 (v3 55% more active); **M2 freeze ratio
  0.00401 / 0.00712 — WRONG DIRECTION, v3 higher** (9 vs 16 transitions
  < 0.002; longest freeze run 0.17s vs 0.33s, also v3 longer — the
  paper's headline metric does NOT discriminate this material);
  M3 flicker 9.17 / 12.52; M4 jitter 0.3327 / 0.2379 (v2 40% less
  smooth); **M6 duplicate ratio 0.19702 / 0.04942 — v2 4.0x HIGHER**
  (885 vs 222 native-rate pairs < 0.0005; longest dup run 0.12s vs
  0.08s); M5 boundaries 36 / 17. Per-segment M6: v2 exceeds v3 in
  11/17 segments (worst v2: O-B 0.409, I-B 0.296, H2-C 0.255, V-0
  0.255, I-A 0.214; worst v3: O-A 0.223 — the accepted master's slow
  return-flight drift, longest dup run only 0.04s). Per-segment M1:
  v3 higher in 15/17. Corroboration: same CRF 18, same duration —
  v2 file 125.1 MB vs v3 193.6 MB (flatter content compresses smaller).
  Verdict: **M6 is the discriminator F-09 lacked** — the halted-moment
  signal in v2 is a high SHARE of near-duplicate frames (slow/static
  takes), not discrete freezes, which is why duration-thresholded
  freezedetect (F-09) saw nothing in either master. M1/M4 support it.
  Pass bar MET on M6 (whole-master + per-segment), FAILED on M2.
  Gate proposal (needs one more master pair to calibrate): whole-master
  M6 > 0.10 = flag for eye review; per-segment M6 alone is NOT a gate
  (v3's O-A at 0.223 would false-flag — pair it with longest-dup-run,
  which stays ≤0.08s in both masters). M5 as implemented over-fires:
  v2's 36 hits include a 6-hit cluster in H1-B (26.33–31.00s) and a
  triple-fire at 81.08/81.25/81.67 — it needs non-max suppression
  before its count means anything (recall on planned cuts: v2 13/16,
  v3 7/16, but precision is poor). M4's threshold (3x median |Δd|) is
  OUR implementation choice, not the paper's — the preprint leaves M4
  relative. Temporal-signature reuse cross-check (v3 vs its takes)
  NOT run — still owed.
  CALIBRATED ON MV-14 TAKES 2026-11-11 (sprint #2):
  `m6_calibrate.py` + `m6_mv14.json`, report
  `M6_CALIBRATION_MV14.md` — all 46 KEEP + 5 REJECT takes, md5-verified
  against the ledger, M6 + longest-dup-run at native 24fps in two
  scopes (full take, usable window). **Per-take gate bar (usable-window
  scope only): flag for EYE REVIEW when window M6 > 0.10 AND window
  longest-dup-run ≥ 0.30s — never auto-reject.** Zero of 46 KEEPs meet
  both (window M6 median 0.0000, mean 0.0090, max 0.2292; longest run
  max 0.29s; 38/46 KEEPs are exactly 0.0000 in-window). M6 alone
  false-flags: S14 (0.2292, run 0.04s — a sanctioned calm wordless
  pocket of scattered single-frame dups, no hold; the take-level echo
  of v3's O-A 0.223). The run half is what lets it through. False-flag
  risk: S24 sits 0.01s under the run bar (0.0786, 0.29s) — another
  calm pocket could cross it, so the gate stays a review flag.
  **Do NOT gate on full-take M6** — it flags 5/46 KEEPs (11%: S14,
  S18 t2, S41, S43, S45), all from out-of-slot material (the black
  fade-to-black tail after ~3.57s; S41's 0.92s run IS the tail) and
  calm lead-ins. **M6 does NOT separate KEEP from REJECT on MV-14:**
  the five rejects are all G1/G2 (subtitle / wardrobe / hair) and
  their full M6 (0.0000–0.3698) overlaps the KEEP range (0.0000–
  0.3361) completely — M6 is a motion gate only; it would not have
  caught any of them. The bar's sensitivity to a real halt is inferred
  from the master-level v2/v3 split, not proven at take level (no
  halted take exists in this sample). Re-check the bar on volley 10's
  takes (S47–S52) when the budget resets.

## 2026-11-12 — F-18 VBench temporal dimensions (dynamic degree / motion smoothness / temporal flickering / subject consistency)

- **Detects:** (a) whether a take actually moves — the share of frames
  with nontrivial motion; (b) whether its motion is smooth or jerky /
  frozen, via frame-interpolation error; (c) flicker / morph shimmer
  between frames; (d) whether the subject's identity drifts inside one
  take (first frame vs last frame). GAP-3 (halted moments) + GAP-1
  (montage timing's motion side) + the identity-drift hard fail.
- **How it works:** VBench (Huang et al., Shanghai AI Lab / NTU, CVPR
  2024 Highlight) decomposes video-generation quality into 16 dimensions,
  each with its own automatic method, validated against human preference
  annotations per dimension (Spearman 0.6073 for Color up to 0.9980 for
  Motion Smoothness). The four temporal dimensions are the ones we
  borrow: **Dynamic Degree** — the percentage of frames with nontrivial
  motion, quantified via RAFT optical flow; **Motion Smoothness** — the
  discrepancy between the actual middle frame and the frame interpolated
  from its neighbours (a frozen take interpolates perfectly, so smoothness
  alone cannot see a still — but smoothness HIGH + dynamic degree ZERO is
  exactly "smooth still", which neither F-09 nor F-17 separates from
  "smooth moving"); **Temporal Flickering** — frame-to-frame pixel
  fluctuation as normalised mean absolute error; **Subject Consistency**
  — DINO feature similarity across frames (Background Consistency is the
  CLIP analogue). The pair (dynamic degree, motion smoothness) is the new
  mechanism here: a share-based flow metric plus an interpolation-error
  metric, where our bank so far has only diff-based shares (F-17 M6)
  and duration-thresholded freezes (F-09).
- **Run / replicate here:** full suite open source:
  https://github.com/Vchitect/VBench — paper
  https://arxiv.org/abs/2311.17982, VBench++ https://arxiv.org/abs/2411.13503.
  Replicate the three temporal dimensions with our own stack instead of
  the whole suite: dynamic degree from the flow-magnitude curve (c11_flow
  from run 12 as the Farneback substitute for the paper's RAFT, share of
  frames above a per-project motion floor); flickering as normalised MAE
  between consecutive frames (numpy, trivial); subject consistency as
  DINO (or CLIP) embedding cosine between the take's first and last
  frames — the checkable form of the practitioner hard fail "same person
  in the first and last frame" (blurstudio.ai 12-point check, 2026).
  Motion smoothness needs a frame-interpolation model (RIFE/FLAVR class)
  — the one piece with no local substitute yet.
- **What it would have caught in MV-8 v2:** the halted moments as LOW
  dynamic degree (slow/static takes) paired with HIGH motion smoothness
  (they interpolate cleanly because nothing moves) — the exact signature
  F-09 missed (zero freezes in both masters) and F-17's M6 found only as
  a diff-share. It also gives the identity-drift check the v2 verdict's
  reuse/consistency complaints need: a take whose face changes between
  first and last frame fails subject consistency even when every sampled
  still looks fine.
- **Limits:** VBench scores are benchmark-relative (model-vs-model), not
  absolute gates — every threshold needs local calibration on the v2/v3
  pair before it means anything here. The full suite is heavy (RAFT +
  DINO + CLIP + interpolation model + aesthetic predictor); the
  interpolation piece has no local implementation yet and is GPU-ish.
  RAFT is heavier than our c11_flow Farneback and the substitution is
  unvalidated. DINO/CLIP are trained on real images; stylised/cartoon
  faces are unmeasured for subject consistency. Dynamic degree is still
  a frame-level share, so the small-moving-object dilution caveat (F-17's
  limit) applies in principle.
- **Status:** UNTESTED. Test: compute dynamic degree + flickering per
  segment on the v2 and v3 masters (flow via c11_flow, MAE via numpy);
  pass bar is v2 lower dynamic degree / higher flickering than v3 in the
  segments the user flagged, and the (smoothness-high, degree-zero) pair
  isolating v2's static takes. Subject-consistency first-vs-last check
  on one identity-drift take vs one stable take.

## 2026-11-12 — F-19 Synchformer AV offset estimation + synchronizability (transformer, sparse-cue robust)

- **Detects:** the temporal offset between a take's picture and its audio
  (per insert, on the warped render), and — separately — whether the clip
  carries synchronisation cues at all. GAP-2. The upgrade over F-01
  (SyncNet): it is built for SPARSE cues, and its synchronizability head
  is a detector for the structural no-mouth case.
- **How it works:** Synchformer (Iashin et al., Tampere/Oxford, ICASSP
  2024) splits audio and video into 0.64s segments, encodes them with an
  AST audio encoder and a Motionformer visual encoder, and pre-trains the
  encoders with segment-level contrastive learning — contrasting segments
  across TIME within one clip, not across clips — so the features are
  discriminative in time. A 3-layer, 8-head transformer sync module then
  predicts the offset among 21 classes (−2.0 to +2.0s, 0.2s steps). On
  LRS3 Full Scene it scores 99.6% within ±1 class; on the sparse-cue
  VGGSound-Sparse set 70.1%, vs 62.2% for SparseSync and 32.1% for
  AVSTdec. The synchronizability model (fine-tuned from the sync model)
  predicts whether a clip is synchronizable at all (AUC 0.83) — a painted
  smile with no moving mouth, or a montage with no face, carries no sync
  cues and scores low, which is a detectable signature instead of a
  silent pass.
- **Run / replicate here:** code + pretrained models, MIT:
  https://github.com/v-iashin/Synchformer — paper
  https://arxiv.org/abs/2401.16423, project page
  https://www.robots.ox.ac.uk/~vgg/research/synchformer/. Install:
  `conda env create -f conda_env.yml` (CUDA 11.8 / ROCm 5.4.2 tested);
  `python example.py --exp_name "24-01-04T16-39-21" --vid_path clip.mp4
  --offset_sec 1.6` runs the AudioSet-pretrained model and prints the
  predicted offset class with probability. Checkpoints are hosted on
  a3s.fi (links in the repo README). Colab demo linked from the project
  page.
- **What it would have caught in MV-8 v2:** per-insert AV offset on the
  warped renders — the same question F-01 asks, but with a model that
  does not need dense mouth movement: our inserts have sparse cues (a
  mouth that moves only on some words, montage with no face at all),
  which is exactly where SyncNet degrades and Synchformer is SOTA.
  The synchronizability score additionally flags the structural case
  (MV-3 S13's painted smile: no cue, low score) that F-01/F-03 can only
  catch as "no face found".
- **Limits:** offset classes are 0.2s steps with ±1 class tolerated —
  coarser than our ±2f (±0.083s) cut grid, so it is an insert-level
  verdict, not a frame-level one. Trained on real in-the-wild video
  (VGGSound/AudioSet/LRS3), not sung vocals over a music bed and not
  cartoon faces — same off-distribution caveat as F-01, needs the same
  local calibration (known-good MV-7 insert first). GPU-tested; CPU
  inference on this VM is untested and the AST + Motionformer encoders
  are heavy — if it cannot run here, the test is a hosted/Colab job.
  Small community (138 stars); `av` library version pinning gotchas
  (downgrade to 8.1.0/9.0.0 per issue #11). Related models named in the
  PVSync paper — MTD-VocaLiST, SyncLipMAE — are offset estimators in the
  same family, not separately banked.
- **Status:** UNTESTED. Test: run the AudioSet model on one known-good
  MV-7 warped insert and one known-bad MV-8 v2 insert; pass bar is the
  offset within ±1 class on the good one and a wrong/large offset (or
  low synchronizability) on the bad one.

## 2026-11-12 — F-20 Eye aspect ratio (EAR) blink-rate / dead-face liveness

- **Detects:** whether the face in a take is alive — blinks per 10s —
  as the eye analogue of F-03's mouth curve. A take whose face never
  blinks across a slot reads as dead/halted even when frame-diff says
  "motion" (hair, clothes, or background moving while the face is
  frozen). GAP-3-adjacent (halted moments, dead face) + the deadpan
  family.
- **How it works:** Eye Aspect Ratio (Soukupová & Čech, CVWW 2016,
  "Real-Time Eye Blink Detection using Facial Landmarks",
  https://cmp.felk.cvut.cz/ftp/articles/cech/Soukupova-CVWW-2016.pdf):
  EAR = (‖p2−p6‖ + ‖p3−p5‖) / (2‖p1−p4‖) over the six eye landmarks —
  near-constant while the eye is open, collapsing toward zero on a
  blink; threshold ~0.2–0.25, with an SVM over a short temporal window
  in the paper (simple thresholding reaches ~95% in a 2024 MediaPipe
  replication, https://www.preprints.org/manuscript/202410.0131).
  Practitioner rule (lilachbullock.com, 2026): humans blink 15–20
  times a minute; fewer than 4–5 blinks in the first 10s of a clip
  reads as unnatural — "count the blinks, roughly, in the first ten
  seconds" is their first check on any AI clip. MediaPipe Face Mesh
  (F-03's install) gives the eye landmarks in the same pass as the
  mouth landmarks — compute the EAR curve alongside the MAR curve for
  zero extra install. A 2026 comparison (Kuznetsova & Kimmelman,
  SignLang workshop, https://aclanthology.org/2026.signlang-1.47.pdf)
  of MediaPipe / OpenFace / InsightFace / 3DDFA for blink analysis
  finds tool-specific biases (MediaPipe estimates higher blink
  velocities) — calibrate per tool, never mix tools across a
  comparison.
- **Run / replicate here:** `pip install mediapipe opencv-python`
  (same venv as F-03); per frame read the eye landmarks from the Face
  Mesh result, compute EAR per eye, average, emit one value per frame,
  count threshold crossings (EAR < 0.2 for 1–3 frames = one blink).
  MediaPipe eye landmark sets are documented in the same landmark map
  F-03 cites.
- **What it would have caught in MV-8 v2:** takes whose face is frozen
  while the shot still "moves" — the halted-moment variant F-09 and
  F-17 cannot see, because their frame means and diff shares are lifted
  by non-face motion. A zero-blink 10s singing slot is a flag for eye
  review even when every gate passes.
- **Limits:** needs visible, roughly frontal eyes; fails or jitters on
  profile shots, occluded eyes, sunglasses, and heavily stylised/cartoon
  faces (same caveat as F-03 — detection rate per character must be
  measured, not assumed). Blink rate varies by activity (singing vs
  speaking vs a deliberate stare), so a low count is a flag for eye
  review, never an auto-fail. "No eyes found for N consecutive frames"
  must be a FAIL, not a skip (same rule as F-03).
- **Status:** UNTESTED. Test: run on one MV-7 singing insert with known
  good liveness and one MV-8 v2 insert; pass bar is blink count in the
  human range (≥4 per 10s) on the good one and a visibly lower count on
  the bad one.

## 2026-11-12 — F-21 Montreal Forced Aligner 3.x phoneme-level alignment (the phoneme timings F-02 needs)

- **Detects:** per-phone start/end times for the lyric — the input F-02's
  bilabial-closure approximation needs and our word timings cannot give.
  GAP-2. (Promoted from a passing mention in F-02, which named MFA as an
  option but never banked it with an install or a test.)
- **How it works:** the Montreal Forced Aligner (McAuliffe et al., 2017;
  MFA 3.0, 2026) is a Kaldi GMM-HMM forced aligner: a pronunciation
  dictionary maps each lyric word to phones, a pretrained acoustic model
  scores the audio against them, and Viterbi alignment emits phone-level
  boundaries in Praat TextGrid format. MFA 3.0's 2026 evaluation reports
  state-of-the-art or near-state-of-the-art performance against classic
  and neural aligners, with mean boundary errors below 15 ms across
  English, Japanese, and Korean benchmarks. Run it on the vocal stem
  (F-16: MDX-Net / Demucs) so the music bed does not pull the boundaries,
  then read the /p/ /b/ /m/ spans out of the TextGrid and apply F-02's
  rule (MAR must dip to its closed baseline inside the phone's window).
- **Run / replicate here:** `conda create -n aligner -c conda-forge
  montreal-forced-aligner=3.2.1` (docs, v3.3.7:
  https://montreal-forced-aligner.readthedocs.io/en/v3.3.7/user_guide/workflows/alignment.html);
  `mfa model download dictionary english_us_arpa` + `mfa model download
  acoustic_model english_us_arpa`; single-file workflow:
  `mfa align_one vocal_stem.wav lyrics.txt english_us_arpa
  english_us_arpa out/` (single-speaker mode, no speaker adaptation).
  State-of-the-art note:
  https://www.researchgate.net/publication/407241325_Montreal_Forced_Aligner_and_the_state_of_speech-to-text_alignment_in_2026
- **What it would have caught in MV-8 v2:** the same articulation
  misses F-02 names, but with real phone spans instead of word spans:
  a bilabial phone whose window contains no MAR dip is a lipsync miss
  at the level of a single consonant, measured from the picture, with
  timings an order of magnitude tighter than our word grid.
- **Limits:** trained on speech, not singing — vowels stretch and
  boundaries may drift on chant; validate against hand-checked onsets
  before trusting it (same rule as every finder). The dictionary must
  cover the lyric's words; slang, neologisms, and repeated chant
  fragments need manual pronunciations. The Kaldi/GMM stack is a heavy
  conda install; alignment on a 3-minute track is minutes, not seconds.
  The <15 ms boundary error is on speech benchmarks, not sung chant —
  expect worse here and measure it.
- **Status:** UNTESTED. Test: align the MV-8 vocal stem (F-16); pass bar
  is /p/ /b/ /m/ spans within ±3f of hand-checked closures on a known
  bilabial line, and word boundaries agreeing with SONG_WORDS within
  ±0.1s on the chant sections.

## 2026-11-13 — F-22 Beat This! transformer beat/downbeat tracking (no DBN, no madmom)

- **Detects:** beats and downbeats from the song with a current
  transformer model — the independent phrase-level grid GAP-1 needs,
  via a path that does NOT go through the madmom wall that blocked
  both F-07 (BeatNet) and F-13 (madmom) on Python 3.12. GAP-1 + GAP-4,
  song-as-authority avenue.
- **How it works:** Beat This! (Foscarin, Schlüter & Widmer, ISMIR
  2024, "Accurate Beat Tracking Without DBN Postprocessing") feeds a
  log-mel spectrogram through a convolutional front end plus a
  6-layer RoFormer and outputs framewise beat and downbeat
  activations, peak-picked directly — no Dynamic Bayesian Network
  and no madmom anywhere in the inference path. That is the whole
  point for us: F-07's update proved BeatNet's decoder IS madmom at
  three import points, so BeatNet can never run on this 3.12 box;
  Beat This! was designed to remove that postprocessing entirely.
  Checkpoints: `final0/1/2` (~78 MB, trained on all data except
  GTZAN) and `small0/1/2` (~8.1 MB); a `--dbn` flag exists but is
  optional and is NOT to be used here (it would re-import the wall).
- **Run / replicate here:** `pip install git+https://github.com/CPJKU/beat_this`
  (PyTorch >=2.0 first; `rotary-embedding-torch` is PyPI-only, so use
  pip not conda); CLI `beat_this song.mp3` or Python
  `from beat_this.inference import File2Beats; File2Beats(checkpoint_path="final0", device="cpu")`,
  outputs `.beats` TSV in seconds. Repo:
  https://github.com/CPJKU/beat_this — paper ISMIR 2024, cited in the
  search results above via the CPJKU DeepWiki overview.
- **What it would have caught in MV-8 v2:** nothing v2 missed on the
  beat grid itself — same as F-07/F-13. What it finally unblocks is
  the comparison those two entries still owe: an independent learned
  downbeat series to check the hand grid's phase per section (the
  librosa/C11 fallback in F-07 confirmed TEMPO but showed the single
  global PHASE is loose, median |offset| 0.145s), so phrase-boundary
  cuts for the crescendo-map accents (63.32 hit, 112.25/112.72 pair,
  159.435 peak) can be scored against a learned grid, not asserted.
- **Limits:** trained on annotated real-music corpora (16 datasets);
  Suno chant/brass texture is off-distribution — validate against
  the hand-built grid and crescendo map before trusting any
  downbeat, exactly as with F-07/F-13. A 2025 follow-up (masked-
  diffusion beat tracking, arXiv:2608.04624 in today's results)
  shows Beat This! can still produce tempo doubling/halving and
  consecutive downbeats on some GTZAN tracks — treat doubled/halved
  stretches as a flag, not a grid. PyTorch inference on this VM is
  CPU-only and untested; the `small` checkpoint is the first test.
- **Status:** UNTESTED. Test: run `final0` (fallback `small0`) WITHOUT
  `--dbn` on the MV-14 track (measured 92.0 BPM, period 0.649s,
  phase 0.240s) and the MV-8 song; pass bar is tempo within 1 BPM,
  downbeats coinciding with beats, and per-section median |offset|
  against the measured grid at least as good as the C11 DP tracker's
  0.088s on MV-14 — plus an explicit check that no madmom import
  occurs.

## 2026-11-13 — F-23 All-In-One joint beat/downbeat + FUNCTIONAL structure labels (demixed audio)

- **Detects:** in one pass from the song: beats, downbeats, tempo,
  section boundaries, AND functional section labels (intro / verse /
  chorus / bridge / outro) — named functions, not abstract clusters.
  GAP-4; supplies the section boundaries F-08/F-11 need, with names
  the scene plan can be checked against directly. Song-as-authority.
- **How it works:** All-In-One (Kim & Nam, WASPAA 2023,
  arXiv:2307.16425) runs Demucs-style demixed spectrograms (vocals /
  drums / bass / other as separate input channels) through dilated
  neighbourhood attention (long-term temporal structure) plus
  non-dilated attention (local inter-instrument relations) and
  jointly predicts all four tasks, so the tasks correct each other.
  It reports state-of-the-art on all four tasks on the Harmonix Set.
  The distinction from F-15 (MSAF) is the label type and the joint
  inference: MSAF emits unlabelled repeat clusters (A/B/C) with
  boundaries at ±0.5–3s tolerance from interchangeable classical
  algorithms; All-In-One emits "this span is the chorus" from a
  learned model that also owns the beat grid the span sits on.
- **Run / replicate here:** `pip install allin1` (upstream:
  https://github.com/mir-aidj/all-in-one); Python
  `import allin1; result = allin1.analyze(path)` → beats, downbeats,
  segments with functional labels; pretrained variants
  `harmonix-all` and `harmonix-fold0`–`fold7`. Paper:
  http://arxiv.org/abs/2307.16425
- **What it would have caught in MV-8 v2:** a wrong section
  assumption in the plan itself, in the plan's own vocabulary: if
  the model labels a span "bridge" where the scene plan treated it
  as a chorus return, every per-section vibe correlation (F-08/F-11)
  and every phrase cut in that span was scored against the wrong
  section — the class of error MSAF's A/B/C clusters cannot name.
- **Limits:** trained on the Harmonix Set (Western pop/rock
  structure); Suno chant tracks with long outros and repeated hooks
  are off-distribution and functional labels may collapse (e.g. all
  "chorus"). Needs Demucs demixing first (F-16's cost on this VM)
  or its bundled demixer. Boundaries are section guides, never cut
  placements (same ±seconds caveat as F-15). CPU inference is
  possible but slow per the Replicate guides found today.
- **Status:** UNTESTED. Test: run `harmonix-all` on the MV-8 song;
  pass bar is boundaries within ±3s of the hand-built section plan
  AND the 41s Outro labelled as outro/build, with repeated choruses
  sharing the chorus label; then repeat on MV-14 and compare its
  labels against the scene plan's named sections.

## 2026-11-13 — F-24 AutoShot NAS shot-boundary detection for short-form video

- **Detects:** shot boundaries in short-form, fast-cut video — the
  segmentation GAP-3 needs — with a model searched specifically for
  short videos, where F-10 (TransNetV2) was trained on long-form
  documentary/YouTube material. GAP-3 (+ GAP-1 segmentation).
- **How it works:** AutoShot (Zhu et al., CVPR Workshops 2023) uses
  neural architecture search over 3D-ConvNet + Transformer blocks
  (starting from the TransNetV2 family) to find the SBD architecture
  that maximises F1, and releases the SHOT dataset: 853 complete
  short videos, 11,606 shot annotations. Reported F1: +4.2% over
  TransNetV2 on SHOT, and +1.1% / +0.9% / +1.2% over prior SOTA on
  ClipShots / BBC / RAI. Our masters are exactly the short-form,
  fast-cut case SHOT was built for, which neither F-04's colour
  thresholds, F-12's scdet, nor F-10's long-form training target.
- **Run / replicate here:** code + weights:
  https://github.com/wentaozhu/AutoShot.git (named in the paper);
  paper: https://openaccess.thecvf.com/content/CVPR2023W/NAS/html/Zhu_AutoShot_A_Short_Video_Dataset_and_State-of-the-Art_Shot_Boundary_Detection_CVPRW_2023_paper.html
  Run inference per the repo README, threshold the per-frame
  transition probabilities, and diff the cut list against the
  assembly's planned cuts and against F-10's list on the same master.
- **What it would have caught in MV-8 v2:** the same hidden freezes
  F-04/F-10 promise to expose, with fewer false/missed cuts on
  fast-cut material — and, as the third independent cut list, a
  tie-breaker where F-12 (scdet, a take-joint detector at
  threshold=20) and F-10 disagree: a boundary AutoShot and the plan
  agree on that scdet misses is a real soft/whip transition, not a
  segmentation error.
- **Limits:** still trained on real short-form camera video, not
  AI-generated morphing footage — precision on our material is
  unmeasured, same caveat as F-10. NAS-searched weights are a
  specific checkpoint; reproducibility depends on the released
  `supernet_best_f1` weights loading cleanly. Does not replace the
  planned-cut cross-check: count agreement proved meaningless for
  F-12 (15 vs 16 by coincidence) and will here too.
- **Status:** UNTESTED. Test: run on the MV-8 v3 master alongside
  F-10; pass bar is a cut list matching the planned cuts at ±2f at
  least as well as F-10, with strictly fewer false positives than
  F-04 `detect-content` on the same master, then run F-05/F-17
  inside its shots.

## 2026-11-13 — F-25 TalkNet / Light-ASD active-speaker detection (per-face speaking probability)

- **Detects:** per face, per frame, whether THAT face is the one
  speaking/singing the audio right now — a speaking-probability
  curve per character. GAP-2 extension: the wrong-singer and
  non-singer-mouth cases that sync scores (F-01/F-19) and mouth
  curves (F-03) do not isolate. This is the detector for the
  standing rule "a sung line gets a sung picture, never another
  character's mouth" and for MV-5-style singer-assignment errors.
- **How it works:** Active speaker detection (ASD) asks three
  questions jointly: is there speech, are this face's lips moving,
  and is the voice synchronised with THIS face's lips? TalkNet
  (Tao et al., ACM MM 2021) encodes audio and face tracks with
  separate temporal encoders, fuses them with audio-visual
  cross-attention, and uses self-attention over long-term context
  before deciding — 92.3% mAP on AVA-ActiveSpeaker. Light-ASD
  (Liao et al., CVPR 2023) is the runnable form here: the same task
  at 1.0M parameters vs 22.5M (~23x smaller, 0.6G vs 2.6G FLOPs) for
  94.1% mAP (vs 94.2% SOTA in its table); its journal successor
  LR-ASD (IJCV 2025) reaches 94.5% at 0.84M parameters and reports
  strong cross-dataset transfer without fine-tuning. Run ASD on
  every face track in a warped insert: the assigned singer should
  score high through their line and every other visible face should
  score low; a non-singer scoring high, or the singer scoring low
  through their own line, is a flag.
- **Run / replicate here:** Light-ASD code + weights:
  https://github.com/Junhua-Liao/Light-ASD (CVPR 2023 paper:
  https://arxiv.org/pdf/2303.04439); TalkNet reference:
  https://github.com/TaoRuijie/TalkNet_ASD (paper
  https://arxiv.org/pdf/2107.06592). Pipeline: face tracks from the
  F-03/F-06 tooling, song (or vocal stem, F-16) as the audio input,
  per-face score series out, joined to the singer-assignment table
  and SONG_WORDS.
- **What it would have caught in MV-8 v2:** inserts where the wrong
  face carries the line, or a background/cover face mouths along
  while the singer does not — the "bad lipsync" verdict at the
  level of WHO is singing, which a clip-level LSE score averages
  away. In MV-5 terms: on a girl line, a high ASD score on the cat
  (or vice versa) is a machine flag for exactly the inversion the
  user caught by eye in v1–v5.
- **Limits:** trained on real talking heads (AVA-ActiveSpeaker /
  Columbia), not sung vocals over a music bed and not stylised
  faces — same double off-distribution caveat as F-01/F-14; the
  music bed is the hard part (run it on the vocal stem first).
  Multiple faces must be tracked and cropped first; a face the
  tracker loses is a FAIL, not a skip (same rule as F-03). Scores
  are probabilities, not word timings — pair with F-03/F-21 for
  word-level claims.
- **Status:** UNTESTED. Test: run Light-ASD on one MV-7 warped
  insert with a single known singer (pass: that face high, no other
  face present) and on one two-character MV-5 v6 segment with a
  known singer assignment (pass: ASD ranking matches the corrected
  assignment — e.g. the basket look line scores the cat, not the
  girl); if the music bed collapses both, re-run on the vocal stem
  before writing the approach off.

## 2026-11-13 — F-26 ImageBind joint audio–image embedding cosine (semantic vibe fit)

- **Detects:** whether the picture's CONTENT semantically matches
  what the song segment SOUNDS like, per section — a semantic
  vibe-fit number, distinct from every energy proxy in the bank.
  GAP-4. F-08 correlates energy envelopes and F-11 scores musical
  arousal; neither can tell that a section sounds like a storm and
  a chase while the picture shows a still room, if the motion
  energy happens to match.
- **How it works:** ImageBind (Girdhar et al., Meta AI, CVPR 2023)
  learns ONE embedding space for six modalities (image/video, text,
  audio, depth, thermal, IMU) by using images as the binding
  modality — every other modality is aligned to images, so audio
  and image embeddings become directly comparable without ever
  being trained as a pair. Embed a song segment's audio (2s
  windows) and embed sampled frames from the corresponding master
  segment, then take cosine similarity per window: high = the
  picture and the sound occupy the same semantic neighbourhood;
  a section whose cosine collapses against its neighbours is a
  semantic mismatch flag. Project page / code:
  https://github.com/facebookresearch/ImageBind (repo named on the
  official model card found today); paper arXiv:2305.05665.
- **Run / replicate here:** `git clone https://github.com/facebookresearch/ImageBind.git`,
  load `imagebind_huge` per the repo examples
  (`from imagebind import data, model`), embed audio windows with
  `ModalityType.AUDIO` and frames with `ModalityType.VISION`,
  cosine-join on the section timeline the scene plan already uses.
  Heavy checkpoint — background job on this VM, per section not
  per frame.
- **What it would have caught in MV-8 v2:** the "song vibes" half
  of the verdict in its semantic form: sections where v2's picture
  was energetically plausible but semantically unrelated to the
  chant/brass moment it sat under — a mismatch class F-08's
  correlation is blind to by construction (it never looks at what
  either side depicts).
- **Limits:** semantic correspondence is not energy correspondence
  and not timing — a high cosine never proves a cut is on the beat
  (GAP-1 is untouched by this finder). Audio training is AudioSet
  (general sounds), not music specifically, so musical semantics
  may read coarsely; stylised/cartoon frames are off-distribution
  for the vision encoder. Absolute cosines are meaningless without
  a local baseline: calibrate on the accepted v3 master first and
  use v2-vs-v3 / section-vs-section differences only, never a raw
  threshold. The model card states research use only.
- **Status:** UNTESTED. Test: embed the MV-8 v3 master's sections
  (audio windows + sampled frames) for a baseline distribution,
  then the v2 master's same sections; pass bar is v2 scoring
  visibly below v3 in at least the section the user flagged for
  vibes, with no section of v3 collapsing to the v2 range.

## Run log

- 2026-11-09 (run 1): first run — bank created; 8 finders banked
  (F-01 SyncNet, F-02 PVSync, F-03 MAR curve, F-04 PySceneDetect,
  F-05 Farneback cut-energy, F-06 MPEG-7/videohash reuse, F-07 BeatNet
  downbeats, F-08 audio/visual envelope correlation). Emphasis:
  academic + open-source tools. SyncNet/PVSync previously noted in
  `notes/LIP_SYNC_KEVIN_BACON_2026-11-01.md`, never implemented —
  banked here as canonical entries with that provenance. Product-tooling
  avenue yielded only FFmpeg's signature filter today; creators avenue
  yielded the cut-on-action rule via the beat-sync-editing skill.
  Rotate emphasis next run: creators/practitioners + product tooling.

- 2026-11-10 (run 3): first TESTS — F-09 freezedetect and F-12 scdet
  run on the MV-8 v3 house master (4493f, 187.2s). F-09: zero freezes
  ≥0.5s at n=0.003/d=0.5, control-validated on a frozen clip; v3
  passes the ≥1s auto-fail line — BUT the v2 comparison is a negative
  result: rejected v2 also shows zero freezes at both n=0.003/d=0.5
  and n=0.02/d=1.0, so freezedetect does not discriminate v2 from v3
  and cannot be trusted alone for the halted-moment gate. F-12:
  threshold=10 over-fires (180
  events); threshold=20 gives 15 cut candidates, in range for 17
  segments — calibrated baseline is 20, not 10. Banked-command
  corrections: scdet takes `threshold=`, not `s=`; metadata key is
  `lavfi.scd.score`. v2 comparison and planned-cut cross-check still
  owed for both. Rotate emphasis next run: academic/papers +
  song-as-authority (unchanged).
  F-10 TransNetV2, F-11 Essentia section energy/arousal,
  F-12 FFmpeg scdet). Emphasis: creators/practitioners + product
  tooling, per run 1's rotation. Verified on this VM: FFmpeg 8.1.2
  ships freezedetect, scdet, mpdecimate, blackdetect, signature —
  F-09/F-12 need zero installs. Creators avenue yielded practitioner
  corroboration more than new finders: the 2026-10-30 Mastodon
  freezedetect post (a 1.04s freeze in generated video, "judge how
  long a freeze lasts, not how many"), the lipsync.com 12-check
  list (plosive-closure rule — already F-02's approximation), and
  the Magic Hour 42-check QA list (eye-review framework, no
  runnable detector). Product avenue: CapCut Beat Sync (Beats 1
  downbeats / Beats 2 sub-beats) and DaVinci Resolve Neural Engine
  Scene Cut Detection are closed-product features with no runnable
  detector here — NOT banked, only noted; their ideas (downbeat
  density modes, confidence-graph threshold) are already covered by
  F-07 and F-04. HeyGen/Kling lip-sync "scores" are vendor
  benchmark claims (Kling 3.0: "94.3% phoneme-to-frame alignment"),
  not usable detectors — not banked. Rotate emphasis next run:
  academic/papers + song-as-authority.

- 2026-11-11 (run 4): 5 new finders banked (F-13 madmom beat/
  downbeat + onset tracking, F-14 AV-HuBERT visual-only lip-reading,
  F-15 MSAF song-structure segmentation, F-16 Demucs vocal-stem
  isolation, F-17 TSM temporal stability suite). Emphasis:
  academic/papers + song-as-authority, per run 3's rotation.
  F-17 is the direct answer to F-09's negative result: freezedetect
  could not discriminate rejected v2 from accepted v3, so TSM's
  share-based freeze/duplicate ratios (no minimum duration, tighter
  thresholds) are the next test for the halted-moment gate. F-14 is
  the first finder that reads WHAT the mouth says from the picture
  alone, not just whether it moves (F-01) or opens (F-03). F-16
  banks the separator the MV-11 hybrid lesson already relies on.
  Rotate emphasis next run: creators/practitioners + product
  tooling.

- 2026-11-11 (run 5 — first downtime-improvement sprint, user msg 202):
  F-17 TESTED on MV-8 v2 vs v3 (`tsm.py`, `tsm_v2.json`, `tsm_v3.json`):
  M6 duplicate ratio discriminates decisively (v2 0.197 vs v3 0.049,
  4.0x); M1 activity + M4 jitter support it; M2 freeze ratio goes the
  WRONG way (v3 higher) — the paper's headline metric fails on this
  material; M5 over-fires without non-max suppression. F-09 re-run at
  the practitioner threshold (n=0.003:d=0.3): still zero freezes in
  BOTH masters — negative result confirmed. F-12 cross-checked against
  the planned cuts: threshold=20 hits 4/16 planned on v3, 8/16 on v2 —
  it is a take-joint detector, not a scene-boundary detector; the
  count matched by coincidence. F-13 INSTALL FAILED on Python 3.12
  (madmom 0.16.1 C build dies on removed `longintrepr.h`) — MV-14 beat
  comparison still owed; next paths are a ≤3.11 venv or BeatNet (F-07).
  Blender path PROVED: Cycles CPU rendered a 1280x720 MV-14 impact
  frame (glowing CLIP, cutting room at night) in 4m46s —
  `MV-14_clip-it/work/blender/`. Rotate emphasis next run: run the
  temporal-signature reuse check (F-17, still owed) + F-05 Farneback
  cut-energy on the v2/v3 pair (GAP-1's missing metric).

- 2026-11-11 (run 6 — second downtime-improvement sprint, user msg 202):
  F-17 CALIBRATED on all 51 ledgered MV-14 takes
  (`m6_calibrate.py`, `m6_mv14.json`, `M6_CALIBRATION_MV14.md`):
  per-take gate bar is window M6 > 0.10 AND window longest-dup-run
  ≥ 0.30s, eye-review flag only — zero of 46 KEEPs meet both; M6
  alone false-flags S14 (0.2292, run 0.04s); full-take M6 must NOT
  be gated on (5/46 KEEPs false-flag, all out-of-slot black-tail /
  lead-in material); M6 does not separate KEEP from REJECT (all five
  rejects are G1/G2, ranges overlap fully). F-07 BeatNet BLOCKED:
  1.1.1 installs but imports madmom at three points, so both PF and
  DBN paths need it — F-07 and F-13 are the same 3.12 wall, and no
  python3.11 exists on the box. Fallback librosa `beat_track`
  confirms the MV-14 grid's TEMPO (92.29 vs 92.0 BPM) but not its
  global phase (median |offset| 0.145s, section-dependent). BeatNet
  comparison still owed; next path is one job: install Python ≤3.11,
  venv, madmom + BeatNet together. Rotate emphasis next run: the
  temporal-signature reuse check (F-17, still owed) + F-05 Farneback
  cut-energy on the v2/v3 pair (GAP-1's missing metric).

- 2026-11-11 (run 7 — third downtime-improvement sprint, user msg 202
  + msg 214 SLERM-C11 method): C11 SLERM BEAT TRACKER
  (`c11_beat/beat_tracker.c`, `SPRINT_2026-11-11_C11_BEAT.md`):
  Ellis DP tracker re-created from scratch in C11 (STFT flux +
  autocorrelation tempo + DP, 0.59s on the MV-14 track, zero
  warnings). Front end VALIDATED: C11 flux vs Python/scipy flux corr
  1.0000, max|diff| 0.0031; phase at canonical 0.649s period is
  0.25s vs measured 0.240s. Tempo autocorrelation is FLAT 0.6357
  across 90.5-92.5 BPM — measured 92.0 is a selection inside a
  plateau, not a sharp peak. DP beats vs measured grid beat librosa
  on every metric (median |offset| 0.088s vs 0.145s, 53.0% within
  100 ms vs 39.5%); DP vs librosa median |offset| 0.035s — the two
  decoders agree with each other far better than either agrees with
  the rigid global grid, so the grid's single global phase is the
  loose part, not the trackers. DP lattice-fills the quiet head/tail
  (no onset floor) — every mid-track beat has a librosa neighbour
  within 0.30s. The BeatNet/madmom comparison itself is still owed
  from those libraries, but the independent second opinion it was FOR
  now exists in C11. Next: onset floor + run MV-13/MV-12, then the
  C11 BLSTM + DBN (path b) reusing this STFT/flux core.

- 2026-11-11 (run 8 — SLERM survey, user msg 227 "find even more
  tools online to SLERM"): full-pipeline inventory + ranked targets
  (`SPRINT_2026-11-11_SLERM_SURVEY.md`). The SLERM test: algorithm
  (re-creatable) vs trained model (not — porting weights is reuse).
  Model-bound, do not attempt: Whisper itself (adopt whisper.cpp
  1.9.5 as the faster-whisper fallback), Qwen3-ASR/ForcedAligner,
  wav2vec2 aligner, Parakeet TDT (test as-is via sherpa-onnx),
  Demucs U-Net, SyncNet, AV-HuBERT, TransNetV2, MediaPipe Face
  Mesh, Essentia arousal/valence. Ranked: #1 c11_mir — extend the
  sprint-3 STFT core with MFCC/chroma/RMS/per-beat band loudness/
  centroid/rolloff/tempogram, replacing librosa + Essentia's
  structural half; #2 word-time snapper (DP snap of ASR word times
  to the flux onset envelope — the classical substitute for forced
  alignment); #3 C11 HPSS vocal-envelope + RMS-VAD segmenter
  (Fitzgerald 2010 — takes Demucs' segmentation job, the MSS-ALT
  finding says the gain is boundaries not cleanliness); #4 C11
  Farneback dense flow (F-05, never ran here — no cv2 installed);
  #5 MAR-curve lipsync tool around InsightFace buffalo_l ONNX
  detector + 68-point landmark ONNX under onnxruntime (already
  installed) — test-first, cartoon-face calibration unproven.
  Adopt-don't-SLERM: MSAF via pip, MDX-Net ONNX via audio-separator
  (already installed). Sprint 4 pick: #1 c11_mir, step 0 being
  sprint 3's owed onset floor + MV-13/MV-12 runs. Roadmap: after
  #1–#3 the only torch user left is Demucs for dense spans, and
  MDX-Net ONNX covers that too — a torch-free pipeline, weight
  cache down to the Whisper model alone. No new F-entry banked:
  the targets implement already-banked finders (F-05, F-11, F-16)
  or pipeline tools, not new detectors.

- 2026-11-11 (run 9 — fourth downtime-improvement sprint, survey
  pick #1 c11_mir): C11 MIR CORE (`c11_mir/c11_mir.c`,
  `SPRINT_2026-11-11_C11_MIR.md`, renamed from `c11_beat/`).
  Step 0 onset floor (`--floor`, default off): MV-14 247 -> 237,
  MV-13 298 -> 292, MV-12 247 -> 246 beats, grid agreement
  unchanged; two MV-13 drops sit mid-track in a quiet bridge, so
  the floor is a heuristic, not a proven improvement. Step 0
  tempo/phase: both tracks show the flat plateau (MV-13 AC 0.5094
  across 95.0-97.0 BPM, MV-12 AC 0.7328 across 129.0-131.5 BPM);
  DP vs measured grid MV-13 0.138s / MV-12 0.110s median |off| —
  the sprint-3 DP advantage does NOT generalise, DP and librosa
  are equivalent here. Step 1 features on the STFT core (MFCC 13,
  chroma 12, RMS, centroid, rolloff, contrast, per-beat band
  loudness, per-beat RMS, tempogram), all librosa-defaulted.
  Step 3 validation on MV-14 (`compare_mir.py`,
  `c11_mir_validation.json`): EVERY feature corr 1.000000 vs
  librosa end-to-end (bar 0.999) — MFCC max|diff| 0.0005, chroma
  1.6e-6, RMS 5e-7, centroid 0.005 Hz, rolloff one bin (15.6 Hz,
  single threshold frame), contrast 5e-5 dB, tempogram 1.9e-4,
  per-beat loudness 5e-5 dB. Two fixes found by validation, not
  reading: MFCC uses power_to_db ref=1.0 (librosa's default, not
  ref=max — that only shifts MFCC[0] by a constant 344); STFT
  window switched symmetric -> periodic Hann (librosa's
  convention), which took contrast from 0.998955 to 1.000000
  while leaving the DP beats bit-identical on MV-14/MV-12 and
  one frame off on one MV-13 beat. Runtime: beats ~0.6s,
  features ~2.1s on the 161.6s track. Next: survey #2 word-time
  snapper and #3 C11 HPSS + RMS-VAD, both on this core.

- 2026-11-11 (run 10 — fifth downtime-improvement sprint,
  survey pick #2 word-time snapper; RECOVERY: the first
  coordinator fd0351c5 died 22:08:44 EST on a transport error
  after building the tool but before reporting — the respawn
  verified its code from scratch and ran the validation):
  `snap` mode in `c11_mir/c11_mir.c` (DP/Viterbi snap of ASR word
  onsets to the nearest strong flux onset within ±0.4 s under
  monotonicity; tiered onset cost — strong peak 0, weak 0.5, stay
  1.0 — after the first build's graded -log cost over-snapped
  209/212 words). LEGO: slermes libjson vendored verbatim
  (byte-identical + 2-line build fix); no Viterbi module exists
  in any of the 9 surveyed user repos; plfm_radar is RF radar
  hardware, nothing audio-reusable. MV-14 (212 words, vocal flux,
  λ=2.0): 166 moved, median |correction| 0.052 s, max 0.252 s,
  never hits the window cap; λ=2 is the knee (λ=1≈λ=2, λ=8
  freezes); window 0.25/0.4/0.6 identical. Honest finding: the
  0.05 band-energy "gap" test is miscalibrated — the threshold
  sits at the median word-start energy and the wordless outro is
  louder in-band than sung V1, so "115 -> 64" is a threshold
  artifact; calibrated at 0.01 the true gap move is 28 -> 2.
  Hand-check (24 words, not blind): 15 agree / 7 disagree / 2
  ambiguous — all 5 clear errors are early snaps onto
  previous-word/drum peaks when the word has no in-span strong
  peak; the "stay if no in-span strong peak" rule would fix all
  5 and preserve all 15 agrees (follow-up, not yet patched).
  Stem-flux comparison still owed (sprint 6's Demucs stem was in
  flight; duplicate run killed to save torch compute). Runtime
  ~0.5 s. Report `SPRINT_2026-11-11_C11_SNAPPER.md`.

- 2026-11-11 (run 11 — LEGO HARVEST survey, user msg 250: C code from
  wubuwizard, wubuos, www for WUBUMV tools): 4,106 C files / ~365,000
  lines surveyed (wubuwizard ~105k, wubuos ~246k, www ~13k). Tier-1
  lego: wubu_png (171 lines, zlib only) + wubu_jpeg (397, Huffman+IDCT)
  + wubu_video (138, AVI+MJPEG) — from-scratch frame readers;
  wubu_audio (127, mel + radix-2 FFT, 16 kHz/512/Hann/40 mels, cap
  64 frames) + wubu_codec (229, STFT->RGB image, ISTFT back) —
  second opinion on c11_mir's front-end and C dadaspec; wubu_canvas
  (2,005, layered 2D engine: layers/blend/filters/undo/PPM IO) —
  the kinetic-type renderer in C; wb_render (162, software 3D
  rasterizer, pure C11) — the Blender-alternative floor; wubre
  (3,793, regex + SIMD matcher + wubugrep). Tier-2: gguf_reader +
  quantized_matmul + tensor_store (model-runner floor), wubu_tokenizer
  (BPE), thread_pool (parallel-for), wubuos DAW/Furnace/SF2 audio
  (2,881, mixer+tracker, needs OS decoupling), wubu_sound (PCM
  synth). NOT found anywhere in the three repos: beat/onset/tempo,
  MFCC, chroma, HPSS, VAD, forced aligner, Whisper, font/glyph
  renderer, H.264/MP4 decoder, optical flow — sprints 5/6/7 stay
  from-scratch. False leads recorded: bpm.c is a gamepad shell, not
  BPM; wubuos kernel audio files are detection stubs, not DSP;
  wubu_encoder names "whisper" but implements no Whisper. Top-3
  builds queued after sprints 5/6/7: c11_frames (frame readers +
  M6 in C), c11_kinetic (canvas-based kinetic renderer),
  c11_spec (C spectrogram + mel front-end). Report
  `SPRINT_2026-11-11_LEGO_HARVEST.md`. Clones kept at
  `~/workspace/lego-harvest-scratch/` for the builds.

- 2026-11-11 (run 12 — seventh downtime-improvement sprint,
  survey pick #4 C11 Farneback; RECOVERY: the first coordinator
  6e607dfd died 22:08:44 EST on a transport error leaving a partial
  `c11_flow/c11_flow.c` — the respawn read it in full, found it
  compiled clean but PROVED it broken by validation, and rewrote
  the expansion, displacement update, and pyramid to the faithful
  OpenCV form): `c11_flow/c11_flow.c` (`SPRINT_2026-11-11_C11_FLOW.md`),
  libc + libm only, `gcc -std=c11 -O2 -Wall -Wextra`, zero warnings.
  Polynomial expansion is a weighted LEAST-SQUARES fit (6x6 Gram
  inverse of {1, x, y, x^2, y^2, xy}), NOT Gaussian-derivative
  convolution — the first build used the naive form and read
  0.03 px flow on a 3 px shift (g2 sums to -0.106, A11 0.5x, bx
  sign flipped). Displacement: R1 bilinearly warped per iteration,
  box-blurred M, 2x2 solve with +1e-3, flow OVERWRITTEN, 5 px
  border scaling included (adding it cut Urban2-native EPE vs cv2
  0.43 -> 0.11 px). Pyramid: blur full-res + resize per level,
  levels = above-base, cropped >= 32 px. LEGO: bilinear resize
  from the user's distiller-c11 (`image_resize_bilinear`, adapted
  to float); everything else fresh — no user repo has flow
  (surveyed the 9 msg-233 repos). Validation vs cv2 5.0.0
  (throwaway venv, deleted after) + Middlebury GT: synthetic
  known shifts mean EPE vs cv2 0.0004-0.019 px, median 1e-5-4e-5;
  Middlebury 160x90 vs GT 0.13/0.18/0.52/0.54 px (cv2 identical
  to 0.003); native res vs GT 0.80/0.44/1.18/1.37 (cv2 0.82/0.45/
  1.13/1.37); mean EPE vs cv2 0.002-0.003 px at 160x90,
  0.012-0.11 px native (Urban2 tail: ~6% large-motion occlusion
  pixels, both far from GT). Real MV-14 S47 frames: EPE vs cv2
  mean 0.073 px, median 0.005, mag corr 0.995. `flow_curve.py`
  adds the GAP-1 motion-energy curve + cut contrast (S47 take:
  1.462 -> 0.185 across 2.5 s). Yosemite NOT fetchable —
  Middlebury "other" + GT used instead (stronger). Honest limits:
  stripe-sequential M update not ported (Jacobi-style recompute
  instead — the likely Urban2 tail source); ~3-6x slower than
  cv2 (scalar C11); flags=0 only; outer 8 px unreliable. Next:
  wire flow_curve.py into volley QC as the cut-energy check.

- 2026-11-11 (run 13 — sixth downtime-improvement sprint,
  survey pick #3 C11 HPSS + RMS-VAD segmenter; RECOVERY: the first
  coordinator a2a12fd2 died 22:36:35 EST on a transport error
  leaving `hpss.c` + binary + first validation numbers — the
  respawn continued from the partial work, rebuilt clean, and ran
  the boundary validation the predecessor never reached):
  `c11_mir/hpss.c` (`SPRINT_2026-11-11_C11_HPSS.md`), libc + libm
  only, `gcc -std=c11 -O2 -Wall -Wextra`, zero warnings.
  Fitzgerald median-filter HPSS (K=31 both axes, reflect padding,
  soft masks margin 1.0) on the sprint-4 STFT core + RMS-VAD
  (verbatim port of the MV-11 test-#2 recipe). LEGO: STFT/FFT/WAV
  from sprint-4 `c11_mir.c`, RMS-VAD + Demucs reference recipe from
  MV-11; median filter + masks fresh (no user repo has HPSS/VAD —
  lego harvest confirms). Validation vs librosa masks: corr
  **0.999229** (bar 0.999) — PASS; harmonic share C 0.5862 vs
  librosa 0.5962. Reference: Demucs htdemucs via audio-separator
  0.48.0 (14:54 wall; model name is the yaml filename) + verbatim
  RMS-VAD, 12 segments; the port reproduces MV-11's
  test2_segments.json exactly (worst diff 0.000 s). **Boundaries
  FAIL: 12.5% ref->C / 11.5% C->ref within ±0.5 s (bar 80%), full
  band 8.3% / 6.2%.** Diagnosis: the harmonic vocal-band envelope
  barely separates vocal from silent spans (median 426.5 vs 344.8,
  1.24x; Demucs RMS 192x), log-corr 0.33; the 16 ms grid is innocent
  (VAD on Demucs RMS at 16 ms reproduces the reference 100%);
  threshold sweep 0.10–0.80 peaks at 16.7%; three alternative HPSS
  envelopes (harmonic-share ratio, adaptive k×rolling-median,
  narrower 500–2000 Hz band) peak at 29.2%. Harmonic != vocal on a
  dense mix — the survey hypothesis fails on MV-14; Demucs stays
  for segmentation, MDX-Net ONNX (once its venv is fixed) or a
  pitch/voicing detector is the next path. Runtime 1.71–1.90 s
  total (target <1 s missed; ~480x faster than Demucs' 894 s). A
  two-heap + lazy-deletion median was tried and reverted (3.68 s,
  slower than the sorted window's 1.30 s for K=31; two correctness
  bugs found by selftest/ASan — pre-removal-median ordering and a
  global pending table eating the other heap's live duplicate).
  `--selftest-median` regression test in the binary. Report
  `SPRINT_2026-11-11_C11_HPSS.md`.

- 2026-11-12 (run 14 — wubuwizard CPU Demucs/UVR, user msgs 275 + 277;
  RECOVERY: first coordinator d0e1273f died ~00:09 EST in a daemon restart,
  no files — the respawn fe46dbe5 started fresh and completed):
  `SPRINT_2026-11-12_WUBUWIZARD_CPU_DEMUCS_UVR.md`. Wubuwizard is a
  model-runner EXAMPLE (C11 engine, kernel dispatch table, quantized
  matmul, GGUF/safetensors loaders, thread pool) — no Demucs/UVR code
  in-tree; WuBuRVC likewise (all demucs/mdx hits are vendored
  `knowledge/rvc_original/` reference). The deliverable is a standalone
  MDX-Net ONNX CPU port (`wubuwizard-cpu-sep/mdx_onnx_cpu.py`, scipy +
  onnxruntime, no torch): UVR-MDX-NET-Voc_FT.onnx (67 MB, SHA-256
  verified) on MV-14's track. Two traps found by parity-checking:
  audio-separator's model-data.json holds params for a DIFFERENT MDX
  model (n_fft 5120/dim_f 2560) — the graph demands dim_f 3072, so
  n_fft=6144; and torch.stft(center=True) REFLECT-pads (not zeros —
  reflect matches exactly, zeros errs 23.8 on edge frames), plus scipy
  scales STFT by 1/sum(window). After both fixes: STFT vs torch max
  1.1e-05, ISTFT vs torch 8e-07. **Full track: 1,592 s wall (9.85x
  realtime) vs Demucs' 894 s — 1.78x SLOWER; model is 95% of chunk
  time. Quality replaces Demucs: full-track corr 0.9675, envelope corr
  0.9750; RMS-VAD 17 vs 12 ref segments, all 12 starts within 0.21 s,
  7/12 both boundaries within ±0.5 s — the rest are splits at real
  phrase gaps (1.08–1.6 s, just over the 1.0 s merge bar) + one 1.7 s
  intro leak (7.55–9.26 s); active/silent 201x (Demucs 702x on the same
  statistic, HPSS was 1.24x).** Verdict: torch-free fallback, not the
  faster segmenter. Next sprint scoped in the report: C11 separation
  runner lego'd from wubu_audioio + wubu_fft/stft (reflect-pad fix
  owed — WuBuRVC's STFT carries the same zero-pad error) + kernel
  dispatch + quantized matmul, bar <894 s; loop-2's C11 voicing gate
  is the complementary boundary detector. Runner + report in
  `wubuwizard-cpu-sep/` and `SPRINT_2026-11-12_WUBUWIZARD_CPU_DEMUCS_UVR.md`.

- 2026-11-12 (run 15 — sprint 8 c11_voice, loop 2 top-1; RECOVERY:
  first coordinator d0cfc1bf died in the VM reboot 02:46:52 EST
  (interrupted 02:47:33 EST) with
  the tool built and both runs done but no validation artifacts — the
  recovery coordinator re-derived every number independently and
  finished the sprint): YIN + pYIN + CPP + HNR voicing gate, single
  file C11, libc + libm only, lego'd FFT/STFT/JSON/Viterbi from
  `c11_mir` + the snapper. **Boundaries FAIL structurally: mix best
  8/24 (33.3%), stem best 14/24 (58.3%) across a 150-combo threshold
  sweep — 0 combos reach the 80% bar — vs HPSS 12.5% / 8.3% on the
  same 12-segment ref, so bar 3 passes (4.0× / 3.7×) while the starred
  bar 2 fails.** The measures do not separate sung from instrumental
  on the dense mix at the frame level (bar 4: CPP medians 0.851 vs
  0.883 dB, HNR +0.04 dB — nothing separates); the gate buys time
  precision 0.91–0.98 at recall 0.52–0.55, dropping out mid-phrase.
  Bar 1 mixed: mix pYIN vs librosa.pyin corr 1.0000, gross 0.00%
  (PASS), stem corr 0.9675, gross 2.75% (FAIL) — a Viterbi
  voicing-decision gap (C calls 1825 frames voiced vs librosa 7493),
  not an estimator error (median rel err 0.00% where both agree
  voiced). Bar 5 fails 1/5 literal and the snap-veto rescue dies on
  its control (gate unvoiced at the snapped frame for 0/15 correct
  snaps and 0/5 errors alike) — the stay-rule patch cannot be built
  on this curve. Bar 6 passes 3/3 (unsung flag has a sensor). Bar 7
  fails on wall (mix 59.1 s, stem 54.0 s vs <10 s; CPU alone 16.3 s),
  RSS 98.6 MB passes. Bar 8 passes in full (zero-warning rebuild,
  byte-identical sha256 `a6067bbf…`, selftest sine 220.64 Hz err
  0.29%, ASan+UBSan selftest + full-track run clean). Two
  prior-coordinator claims did NOT reproduce and are corrected in the
  report: beat-file "stem best 15/24" (sweep tops at 14/24) and
  README "raw YIN corr 1.0000/0.9997" (measured 0.9919/0.9495).
  Verdict: Demucs stays the segmenter; next candidates are MDX-Net
  ONNX adopt-as-is (run 14) and birdsong spectral entropy (loop 2
  #2). Report `SPRINT_2026-11-12_C11_VOICE.md`, validation JSON in
  `c11_voice/`.

- 2026-11-12 (run 16 — c11_vibrato, loop 3 top-1; DAY-1 FALSIFIER, no
  gate built): vibrato signature — the 5–7 Hz modulation of the F0
  track, measured as bandpass (4–8 Hz) RMS depth in cents on sprint 8's
  saved pYIN F0 track. **FAIL FAST (Bar E): the chant is straight-tone.**
  Mix sung median 2.55 cents [IQR 0.27, 6.66] vs instrumental 3.32
  [0.45, 10.36] — IQRs overlap, wrong direction (bar A fails); the
  isolated Demucs-stem voice itself reads 2.68 cents, so this is not a
  mix-dominance artifact — the voice carries no vibrato (classical
  vibrato would read ~35 cents RMS; the 20-cent line is the
  straight-tone boundary, Nix et al. 2016). The accompaniment carries
  MORE 4–8 Hz modulation than the voice (outro median 5.66c; instr.
  frames >20c 5.9% vs sung 1.8%), so the feature is inverted, not
  merely absent (bar C fails). Controls: the pipeline recovers synthetic
  6 Hz ±50c vibrato at 35.16 cents (expected 35.36), straight tone at
  0.00, rejects a 3 Hz wobble at 0.30, and reads exactly 0.00 on the
  silent stem — the null is real, not a broken measurement. Raw YIN is
  unusable as a fallback (270–430 cents estimator noise). No C gate
  was built, per the scope's fail-fast rule. Loop 4: formant experiment
  + birdsong-entropy decision in parallel; scope the CASA correlogram
  experiment as the next sprint. Report
  `SPRINT_2026-11-12_C11_VIBRATO.md`, validation JSON + falsifier
  scripts + SVG plot in `c11_vibrato/`.

- 2026-11-12 (run 17 — loop 4, the stall branch after vibrato failed fast;
  coordinator a6fe92b4): **formant experiment FAIL, birdsong-entropy decision
  FAIL — both on the mix AND on the stem, which is the decisive detail.**
  Formants (LPC order 14, M = |ΔF1|+|ΔF2| per hop, ~100 ms smoothed): mix
  sung median 386.83 Hz [IQR 100.08, 791.22] vs instrumental 290.95 [127.14,
  754.83] — wrong direction, Mann-Whitney p=0.52, IQRs overlap; order 18
  flips direction (sung 465.08 vs instr 626.42, p=1e-37) with IQRs still
  overlapping — parameter-unstable, not a sensor. Stem order 14 fails the
  same way (sung 377.83 vs instr 103.83, wrong direction): the isolated
  voice's formants move more than the residual bleed's. F1/F2 values do not
  separate either (mix F1 931.92 vs 952.33, F2 2517.71 vs 2502.45). Controls:
  fixed-formant vowel M=38.34 vs gliding-formant brass M=332.34 (8.7×) —
  the pipeline works; the material does not separate. Spectral entropy
  (STFT 1024/10 ms, H = −Σp log₂p / log₂N): mix vocal band sung 0.9072
  [0.8803, 0.9291] vs instrumental 0.9129 [0.8901, 0.9317] — IQRs overlap
  (MW p=1.8e-10 is a large-n artifact on a 0.006 effect); full band wrong
  direction (sung 0.8863 > instr 0.8461); stem vocal band wrong direction
  too (sung 0.8863 > instr 0.8461). Controls: tone 0.196, noise 0.978,
  harmonic stack 0.489, noise burst 0.978 (one control bug found and fixed
  mid-run: the burst window initially measured silence). **Stay-rule:
  entropy cannot serve as in-span evidence** — H at snapped position errors
  0.9179 vs correct 0.9038 (ranges overlap fully); span-min errors 0.8392
  dip lower than correct 0.8558 (wrong direction for a veto). The stay-rule
  patch still has no peak-evidence signal. **Break-the-sync probe RUN, PASS:**
  MV-14's real repeats are "Clip it, post it" ×3 (loop 3 mislabeled the
  phrase — "Fourth law" is MV-13's hook); snapped times advance through all
  repeats (max |correction| 0.136 s), 0 collapse hits across all 212 words —
  the snapper does not glue repeats. Blind draw: jitter/shimmer (R8's second
  half; loop 3 drew voice-break degree). CASA correlogram scoped as the next
  sprint (loop-04/SPRINT_SCOPE.md, experiment-first bar: voice-lag peak
  separation on ≥80% of ref segments). TSM squeeze-guard band measurement
  still owed. Report `research_notes/slopcannon-improvement-loop/loop-04/
  report.md`, validation JSON + experiment scripts in loop-04/.

- 2026-11-12 (run 18 — loop 4 top-1, CASA correlogram; coordinator 7899de53):
  **Step-1 experiment FAIL FAST on both bars with the correct voice-lag seed;
  no gate build. The classical sensor search is over; loop 5 takes the
  adoption branch (MDX-Net ONNX as-is + c11_sep).** Bar A (voice-lag peak
  separates sung from instrumental spans, >=80% of 22 clean ref segments):
  **0/22** — pooled sung r_voice 0.2534 vs instrumental r_max 0.5049,
  Mann-Whitney p=1.0 (inverted, not overlapping); best sung span 0.3546
  vs quietest instrumental span 0.2802. Bar E (multipitch confusion,
  octave-aware, bar <=20%): **0.5606** — mix top peak at the voice lag on
  only 33.9% of trusted sung frames, at the octave 4.8%, at the half 5.2%,
  at the bass range 9.7%, other 46.4%; median r_voice 0.2534 vs median
  r_second 0.4611 (voice peak ~1.8x weaker than the strongest competing
  peak; r_voice > r_second on 32.0% of frames). Wide-range sensitivity
  (50-800 Hz) also fails (sung r_max 0.5668 vs instr 0.5286). Controls
  validate the pipeline and show the mechanism: synthetic mixture
  220+98+147 Hz buries the voice lag (r=0.057 vs r_max=0.335, top peak at
  the voice octave). **Seed audit (v1 WITHDRAWN):** v1 seeded the voice lag
  from the mix pYIN Viterbi path, which is pinned at the 50 Hz fmin floor
  on 2525/3101 voiced frames (81%) — it tracked the bass, not the voice.
  v2 seeds empirically from the isolated Demucs stem autocorrelation
  (median ref F0 238.8 Hz, IQR 177.8-290.9, phrase-dependent 144-267 Hz;
  10,659 trusted sung frames). The stem pYIN path is pinned at the 800 Hz
  fmax ceiling on 1148/1825 voiced frames (63%) — octave runaway; neither
  saved pYIN track is a voice-F0 track (sprint 8's corr-vs-librosa
  validates the implementation, not the pitch estimates). **Flagged, not
  re-litigated:** the c11_vibrato verdict's F0 source is compromised the
  same way (depth measured on pinned contours); whether the chant is truly
  straight-tone is open pending a re-measurement off the stem-autocorr
  reference (loop-5 decision). Stem stability: the voice's own lag is only
  moderately stable (raw top peak within +-2 of the smoothed reference on
  73.0% of trusted sung frames). Report
  `SPRINT_2026-11-12_C11_CASA.md`, validation JSON md5
  3cb98c1ff34fa881e8016f0c5e81f79b, experiment scripts + SVG plot in
  `c11_casa/` (v1 results archived as step1_experiment_v1_seedmix.json).

- 2026-11-12 (run 19 — loop 5, adoption branch; coordinator 07caec17):
  **ADOPT MDX-Net ONNX as-is as the pipeline segmenter; c11_sep scoped as
  the sprint that makes it cheap. Vibrato re-measurement: straight-tone
  verdict STANDS on corrected grounds. R8 pre-check FAILS on all three
  conditions. Snapper vocal-flux (blind draw): FAIL on both flavours.**
  Adoption verified in-loop: MDX full-track corr vs Demucs **0.9676**
  (claim 0.9675); RMS-envelope corr 0.9694 (claim 0.9750, windowing);
  17 RMS-VAD segments; active/silent 248.8x (claim 201x, mask-dependent).
  Speed accepted: 1592 s vs 894 s (1.78x slower) — torch Demucs is broken
  in this venv, so MDX is the only WORKING separator; c11_sep's bar is
  <894 s, stem corr >=0.95, boundaries +-0.5 s, active/silent >=100x
  (scope in loop-05/SPRINT_SCOPE.md). Vibrato re-measured off the CASA
  stem-autocorr reference: integer-lag v1 114.06c / sub-sample v2 114.31c
  (quantization hypothesis FALSIFIED — same numbers); FM control recovers
  21.79c for true 35.36c, straight control 0.0c; PSD peak 3.0 Hz (2-4 Hz
  power 2.4x the 4-8 Hz power — drift, not vibrato); only 4.6% of sung
  frames locally stable, stable-frame depth 17.82c at the 20c boundary on
  a subset biased toward straight tone. Original 2.55c/2.68c numbers are
  measurements of pinned pYIN contours (withdrawn as evidence). R8:
  mix SNR median -4.55 dB (bar 30), Type-1 stable fraction 4.64%
  (bar 50%), HNR median 1.69 dB (bar 30) — voice-break degree closes with
  it; the voice-quality shelf is closed. Snapper vocal-flux: mix flavour
  errors 0.4622 vs correct 0.4723 (p=0.63), vocal flavour errors 0.5043 vs
  correct 0.4714 (p=0.50) — no separation on either flavour, all three
  statistics; replication of mix flux vs flux.txt corr 1.0000. Stay-rule
  candidates left: MDX stem activity only. MV-13 Fourth-law probe UNRUN
  (no MV-13 snapper output exists); TSM moderate-squeeze take STILL OWED.
  Report `research_notes/slopcannon-improvement-loop/loop-05/report.md`,
  validation JSON md5 852e65c4be493ec6243332f15f9a67b7, scripts in loop-05/.

- 2026-11-12 (run 20 — c11_sep sprint; coordinator session 66c4f7f1):
  **C11 MDX-Net separation runner: full-graph chunk-0 parity vs ORT 24/24 PASS;
  UVR driver validated end-to-end vs ORT full-track vocals (1 int16 LSB).**
  Torch-free C11 runner for UVR-MDX-NET-Voc_FT (178 nodes, 392 GMACs/chunk):
  STFT 1.526e-05 / ISTFT 1.272e-08 vs torch (bar 1e-4); AVX512 SGEMM (8x48
  micro-kernel, im2col 3x3 at ~118 GFLOPS, out^T 1x1 at ~63 GFLOPS);
  graph compiler 178 nodes -> 173 instructions (5 ConvTranspose BNs folded,
  22 post-MatMul BNs explicit — weight shared across channels, BN scale
  per-channel, cannot fold); interpreter chunk-0 parity: worst sample
  max|diff| 7.02e-04 (node 9 MatMul), final output full max|diff| 8.631e-05,
  corr 1.000000. Driver (`sep_main.c`, UVR chunking/OLA per mdx_onnx_cpu.py)
  smoke-validated: L/R vs ORT full-track vocals max|diff| 1.0 int16 LSB,
  corr 0.999996/0.999995. Two bugs worth banking: (1) SLOT-SHAPE ALIASING —
  ops read shapes from the static slots[] table but slots are reused across
  shapes with the same numel (slot 6 first held [96,128,192], BN 58 is
  [192,32,384]) — shapes must come from the instruction dims, never the slot
  table; (2) LAZY SINGLETON + OPENMP RACE — FFT twiddle tables built lazily
  on first call raced the parallel STFT/ISTFT (L-channel STFT frame 8 err
  2.2e-02, ISTFT race broke the L vocals outright) — build tables eagerly in
  the single-threaded constructor. Full-track validation (stem corr >=0.95,
  RMS-VAD boundaries +-0.5 s, active/silent >=100x, runtime <894 s) — DONE:
  full-track validation PASS on all four bars: stem corr vs Demucs
  **0.9675** (bar 0.95, identical to the ORT port); RMS-VAD boundaries max
  |dStart| **0.21 s** (bar 0.5 s); active/silent **242.7x** (bar 100x);
  runtime **840.4 s** clean single run (bar 894 s, target 650 s not met).
  Two full runs were SIGTERM'd by VM reboots (~2 h cadence), so Stage 4 was
  done via a resilient dump mode (`sep_main --dump-dir`, per-chunk ISTFT
  dumps + `assemble_chunks.py` Hann OLA; a reboot loses at most the
  in-flight chunk) — lesson: any job over ~1 h on this blade must checkpoint
  per unit of work. Report `detection-research/SPRINT_2026-11-12_C11_SEP.md`,
  code + validation JSONs in `detection-research/c11_sep/` (stage1/2/3a/3b/4
  JSONs, `validate_fulltrack.py`, `assemble_chunks.py`).

- 2026-11-12 (run 21 — daily research run): 4 new finders banked
  (F-18 VBench temporal dimensions, F-19 Synchformer AV offset +
  synchronizability, F-20 EAR blink-rate / dead-face liveness, F-21 MFA
  3.x phoneme alignment). Emphasis: creators/practitioners + product
  tooling, per run 4's rotation. F-18 is the first flow-based share
  metric in the bank (dynamic degree via RAFT) plus the new
  interpolation-error mechanism (motion smoothness) — the pair separates
  "smooth still" from "smooth moving", which F-09 and F-17 cannot.
  F-19 is the sparse-cue successor to F-01's SyncNet, and its
  synchronizability head is a detector for the structural no-mouth case.
  F-20 is the eye analogue of F-03's mouth curve, from the practitioner's
  blink-count rule (humans 15–20/min; <4–5 per 10s reads unnatural).
  F-21 promotes MFA from a passing mention in F-02 into a banked finder
  with install + test — it is the phoneme-timing source F-02's
  bilabial-closure rule needs. Updates, not new entries: F-01 gains the
  Sync-C gaming caveat (Kandinsky S2V 1.0 report: Sync-C can be exploited
  by exaggerating lip motion); F-02's PVSync code release CHECKED today —
  still unreleased ("will be released upon acceptance", arXiv 2610.09223).
  Product avenue: CapCut Auto Cut / Beat Sync, DaVinci Resolve Studio AI
  Beat Detector (4/4 or 3/4 only) and AI Multicam SmartSwitch (lip-
  movement speaker detection), OpusClip ClipAnything — all closed-product
  features with no runnable detector; same verdict as run 3, not banked.
  Their ideas are already covered (F-07 downbeats, F-01/F-19 sync).
  LatentSync is generation, not detection — not banked. Still owed:
  F-05 Farneback cut-energy on the v2/v3 pair (c11_flow + flow_curve.py
  now exist, run 12) and the F-17 temporal-signature reuse check — both
  are sprint-scale tests, not daily-run work. Rotate emphasis next run:
  academic/papers + song-as-authority.

- 2026-11-12 (c11_tsm sprint — recovery coordinator): M7 built as the C11
  TSM core (`detection-research/c11_tsm/c11_tsm.c`, libc+libm only, zero
  warnings, ASan+UBSan clean). ALL 7 BARS PASS: hit identity 0.0 / 0.000 s
  on all takes; words-3+ onset RMS 52.9 ms (bar <=100, prototype M7 69.3);
  identity 19/23 with guard active (bar >=18); guard HARD-flags every
  alpha<0.5 gap (S50 0.333x, S52 0.243/0.254x) and fills the slot with a
  truncated copy; OLA256 fallback 23/23; parity vs prototype M7 corr
  1.000000 guard-off with identical per-gap alphas (guard-on divergence
  confined to flagged spans, corr 1.000000 outside them); runtime 0.061 s
  worst per take (bar <10 s). Owed moderate-squeeze take BUILT and
  measured (S49MOD, 0.60x survives: 'post' +80 ms, 'it' +16 ms) — failure
  threshold now bracketed to (0.33, 0.60]; hard guard 0.5 CONFIRMED,
  operational guard stays 0.7. Parity traps documented in the code header
  (zero-pad stft, raw-diff PV, nearest-pad median, symmetric OLA window,
  half-even rounding). Still owed: (b) a listening check (MOS-style, ears
  not ASR) — needs a human ear. Full report:
  `detection-research/SPRINT_2026-11-12_C11_TSM.md`.

- 2026-11-12 (MDX_STEMACT sprint — Slopcannon improvement loop 6, top-1):
  stem-activity curve validated as the pipeline's voice-activity sensor
  (`detection-research/SPRINT_2026-11-12_MDX_STEMACT.md`,
  `detection-research/mdx_stemact/`). Bars held, none lowered. Bar A
  (RMS-VAD boundaries +-0.5 s vs the Demucs stem-activity boundaries, 12
  ref segments): PASS — max |dStart| 0.21 s on the ONNX MDX stem and the
  c11 stem (identical segments to the 10 ms grid), 0.00 s on Demucs
  (self-check). Bar B (25 ms RMS envelope separates sung from
  instrumental, non-overlapping IQRs, all three stems): PASS — sung q25
  0.0207/0.0207/0.0267 vs instrumental q75 0.00084/0.00084/0.00163
  (MDX/c11/Demucs); sprint-6 ratio 248.9x (sung-only masks) / 242.7x
  (all-12 masks), Demucs 200.5x/191.0x. Bar C (stem-envelope-at-snapped
  separates the 5 known snap errors from the 15 correct controls, MW
  one-sided p < 0.05 AND errors median < correct median): FAIL — c11
  errors median 0.04909 vs controls 0.07016, MW U=29/75, p = 0.2486
  (MDX identical); the low errors median is carried by one point (idx
  56 'Help', env 0.0103, prob 0.013). Diagnostic (not a bar): distance
  to nearest stem-envelope rising edge, errors 0.368 s vs controls
  0.190 s median |distance|, MW p = 0.37 — not the better statistic
  either; locally-normalised envelope is worse (p = 0.78). Verdict per
  the pre-stated logic: sensor VALID as a voice-activity curve (the
  mouth-open gate + CCA may calibrate on it), STAY-RULE use FAILS — the
  stay-rule patch has no sensor; all five in-span candidates tried
  across loops 4-6 are now dead on MV-14. Calibration note: loop 5's
  248.8x uses the sung-only active mask (ref segments 1-10) vs
  outside-all-12 silent; the all-12 variant is 242.7x — the gap is the
  bleed segments 11-12. Reusable artifact delivered: the stem-activity
  curve per stem (`stem_activity_*_mv14.npz` + `stem_activity_curve.py`,
  the RMS-VAD recipe as a script). MV-11 generalisation leg (c11 stem
  from `track.mp4` via `sep_main --dump-dir`, Bar A stem-to-stem vs the
  Demucs stem) COMPLETE: FAIL — max |dStart| 1.71 s (bar 0.5 s), stem
  corr 0.8466, 7/11 Demucs spans within bar, 2 outside (0.63, 1.71 s), 2
  unmatched by the metric; mechanism is Demucs-stem brass bleed crossing
  the VAD threshold (both stems agree true onset ~71.5 s in the worst
  span). The MV-14 validation does not generalise to MV-11 at the
  ±0.5 s bar; loop 7 should use the c11 stem's own boundaries and fix
  the metric to count unmatched spans as failures. Full leg write-up in
  the sprint report §MV-11; scores in `mdx_stemact/mv11/mv11_score.json`.
- 2026-11-13 (C11_SUPERFLUX sprint — taste/SLERM research top-1, the
  stay-rule reopening loop 6 named): SuperFlux-family onset functions
  built in C11 (`detection-research/SPRINT_2026-11-13_C11_SUPERFLUX.md`,
  `detection-research/c11_superflux/`). Bar 1 (parity vs librosa
  `onset_strength(max_size=3)` on MV-14): PASS — corr 1.000000, max
  residual 3.7e-6; the build is a faithful SuperFlux. Bar 2 (the loop-6
  Bar C fixture — 5 snap errors vs 15 controls, 3 statistics x 3 ODFs:
  plain SuperFlux, rectified complex-domain, harmonic-gated [HPSS
  harmonic magnitudes + pYIN F0-harmonic mask]): FAIL on all three
  ODFs, all statistics (best p = 0.1628, degenerate; judged rows
  p 0.40-0.84). On SuperFlux the effect points the WRONG WAY — errors
  sit on stronger values than controls (at-snapped medians 0.0311 vs
  0.0132, U=47/75): a snap error is a position an onset function found
  attractive, so onset-strength-at-the-snapped-position inherits the
  snapper's selection bias. Bar 3 (peak-picked onsets vs the MV-14
  word grid, thr 0.20 = the snapper's strong-peak tier): FAIL —
  SuperFlux F@+-50 ms 0.081 vs the 0.80 bar (208 peaks, recall 0.080;
  median word-start-to-nearest-peak distance 0.206 s, dispersion not
  lag); the instrumental-FP clause passes (30 vs plain flux's 135 —
  SuperFlux is conservative in instrumental spans, a real property).
  Verdict per the pre-stated kill criteria: **the stay-rule sensor
  search CLOSES on MV-14 with this error set** — six in-span candidate
  families are now dead (c11_voice curve, vibrato, entropy, vocal-flux
  x2, stem envelope, and the whole onset-strength family). The
  stay-rule patch stays unbuilt; reopening requires a different error
  set (>5 errors) or a signal class that is not an onset-strength
  function. c11_superflux stays in the kit as a librosa-exact ODF
  (2.1 s per 161.6 s track). Do not re-test another flux flavour on
  this fixture.

- 2026-11-13 (run 22 — daily research run): 5 new finders banked
  (F-22 Beat This!, F-23 All-In-One, F-24 AutoShot, F-25 TalkNet /
  Light-ASD active-speaker detection, F-26 ImageBind joint
  audio-image embedding). Emphasis: academic/papers +
  song-as-authority, per run 21's rotation. F-22 is the headline:
  a transformer beat/downbeat tracker with NO DBN postprocessing
  and no madmom in its inference path — the first learned tracker
  that can actually run on this Python 3.12 box, finally unblocking
  the downbeat comparison F-07/F-13 still owe (use it WITHOUT
  `--dbn`). F-23 upgrades F-15's abstract A/B/C clusters to named
  functional labels (intro/verse/chorus/bridge/outro) predicted
  jointly with the beat grid on demixed audio. F-24 is the
  short-form successor to F-10 (+4.2% F1 over TransNetV2 on the
  SHOT short-video dataset). F-25 adds the missing WHO-is-singing
  axis — per-face speaking probability (Light-ASD: 94.1% mAP at
  1.0M params, the CPU-plausible form) for wrong-singer /
  non-singer-mouth flags. F-26 is the first SEMANTIC vibe finder:
  ImageBind puts audio and image in one embedding space, so a
  per-section audio-vs-frame cosine measures content match, which
  F-08's energy correlation cannot see. Update, not a new entry:
  F-02 PVSync code release re-checked today — still "will be
  released upon acceptance", no repo. Still owed (sprint-scale,
  not daily-run work): F-05 Farneback cut-energy on the v2/v3 pair
  and the F-17 temporal-signature reuse check. Rotate emphasis
  next run: creators/practitioners + product tooling.
