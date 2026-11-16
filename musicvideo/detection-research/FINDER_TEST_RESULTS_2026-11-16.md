# Finder Test Results — 2026-11-16 sprint

User order 2026-11-16 (Telegram msg 520: "do these and all backlogged") —
every UNTESTED finder in `DETECTION_FINDERS.md` run against the canonical
controls: **MV-8 v2 master (REJECTED — bad montage timing, bad lipsync
timing, halted moments) as positive control, MV-8 v3 master (ACCEPTED)
as negative control.** Measurement only; no master or project file was
modified. All tooling lives in `finder-tests/` (project-local venv,
scripts, raw JSON outputs). Environment: CPU only, ~1.5 shared CPUs
effective, Python 3.12.

Verdicts: **ADOPT-CANDIDATE** (separates the controls, cheap enough to
gate), **WEAK** (partial or confounded signal — instrument, not a gate),
**DEAD** (does not separate this pair / not runnable).

---

## F-02 PVSync — STILL UNRELEASED (verified, not testable)

Re-checked 2026-11-16: arXiv 2610.09223 still states "Code and
benchmark data will be released upon acceptance"; no public repo
exists. No test faked. The MAR-curve approximation (F-03) and MFA phone
timings (F-21) remain the only GAP-2 coverage. **Verdict: BLOCKED
upstream — re-check on the next sprint.**

## F-05 Farneback flow curve + cut-point energy contrast — WEAK

Ran the full bank spec (cv2 Farneback, native 24fps, 160×90, both
masters; `finder-tests/flow_and_signature.py`, `f05_f30_analysis.py`).

| metric | v2 (rejected) | v3 (accepted) | separates? |
|---|---|---|---|
| mean flow magnitude (whole master) | 1.268 | 1.635 | yes (v3 +29%) |
| in-segment share of pairs below 0.25 floor | 25.1% | 14.4% | yes (1.7×) |
| longest below-floor run @0.25 | 1.38 s (1 run ≥1 s) | 0.96 s (0 runs ≥1 s) | yes, weakly |
| mean cut ratio min(pre,post)/max | 0.474 | 0.363 | **no — wrong way** |
| share of 16 cuts with both sides above floor | 0.875 | 0.812 | **no — wrong way** |

The freeze-run side separates, but it is the same signal family as
F-17's M6 (which separates 4.0×, decisively better). The headline
claim — cut-point energy contrast — **fails on this pair**: v3's cuts
are if anything *more* one-sided (e.g. v3 cut at 105.94 s: pre 1.19 →
post 0.04; v2's worst at 163.0 s: 2.54 → 0.03). Both masters contain
cuts from action into near-stillness; energy symmetry at the cut does
not track the user's timing verdict. **Verdict: WEAK — keep the flow
curve as the shared input for other measures; do NOT adopt cut-point
energy contrast as a gate.**

## F-17 temporal-signature leg (the owed cross-check) — WEAK

F-17's M6 was already TESTED 2026-11-11 (partial discrimination, gate
form: usable-window M6 >0.10 AND longest-dup-run ≥0.30 s → eye-review
flag). This sprint ran the still-owed temporal-signature leg
(`finder-tests/f17_signature.py`, 12 fps diff series, sliding Pearson):

- **Machinery control:** a 10 s excerpt of the v3 master series
  localises at ρ = 1.000, exact offset. The correlator is exact.
- **Take localisation (4 s windows, warp-tolerant):** I-B_v3_river
  ρ = 0.969 inside its ledger span ✓; O-B_v3_wave ρ = 0.845 inside ✓;
  H2-B_v3_canal ρ = 0.899 but argmax 1.7 s before the span start
  (window overlaps the span; the scene has two KEEP takes); D-B
  ρ = 0.745, argmax outside the span. Warped spans (assembled slower
  than the source take) degrade slope-1 correlation, as expected.
- **Within-v2 reuse scan:** the only off-home hit at ρ ≥ 0.9 is the
  IN-A opening segment matching at 179.9 s (ρ = 0.941) — the closing
  segment's designed bookend rhyme with the opening bathroom. A
  signature gate would false-flag a deliberate rhyme; it cannot
  distinguish "same set, similar action" from "same footage".

**Verdict: WEAK — the signature is a localisation aid for ledger
audits, not a reuse gate. F-17's adopted form stays M6-only.**

## F-27 flow warping error — TESTED 2026-11-14, integrated here: DOES NOT SEPARATE (inverted)

Full report: `F27_TEST_2026-11-14.md` (runner `f27_warping_error.py`,
raw `f27_mv8_v2.json` / `f27_mv8_v3.json`). Kept-pair mean warping
residual: **v2 0.0403 vs v3 0.0640** (median 0.0352 / 0.0558; share of
pairs >0.1: v2 2.2% vs v3 16.7%) — the rejected master reads *more*
temporally consistent than the accepted one. Cut-pair means
(0.119 / 0.136) prove the machinery works; 8 of the top-15 spike pairs
are identical in both masters, i.e. spikes track song energy
(stabs/crescendos), not instability. **Verdict: DEAD in its mean-
residual form (energy-confounded, inverted). Not adopted, not
re-tested; revival would need the forward–backward occlusion-masked
form, which is a new finder, not this one.**

## F-30 BeatAlign (MVAA motion-peak → beat MAE) — DEAD on this pair

Ran per the bank spec (`f05_f30_analysis.py`): peaks on the smoothed
Farneback flow curve, greedy monotonic matching to the measured beat
grid (368 beats, ±½ beat-interval window), plus the paper's original
frame-diff curve as a second form.

| form | v2 MAE | v3 MAE | matched share of beats |
|---|---|---|---|
| flow-curve peaks | 101.9 ms | 106.0 ms | 0.497 / 0.462 |
| frame-diff peaks | 110.8 ms | 112.2 ms | ~0.48 / ~0.48 |

No separation in either form: both edits' in-shot action peaks sit
~100 ms off the beats equally. Plausible cause: both masters were
assembled to the same grid and the generator's action peaks lag the
same way in both — the metric measures the generator, not the edit.
**Verdict: DEAD as a v2/v3 discriminator. The computation is sound;
it answers a question this control pair doesn't pose.**

## F-31 vPDQ — ADOPT-CANDIDATE (with a sampling law)

**Blocker + SLERM form:** `pip install vpdq` fails on this VM — the
C++ wheel build needs FFmpeg dev libraries (libav*-dev) that are not
installed. Simplified honest form used instead: per-frame PDQ hashes
via python-threatexchange's `pdq_hasher` (the reference PDQ
implementation) + Hamming subsequence matching in numpy
(`finder-tests/f31_vpdq.py`). Fixture shared with F-28: v3 master
copy with its 45.51–55.51 s segment spliced in again at 150 s.

- **1 fps sampling (the naive form) FAILS:** inserted frames' best
  Hamming ≈ 100–112 — indistinguishable from random pairs (off-
  diagonal median 106). Diagnosis: the splice offset is non-integer
  (104.49 s), so 1 fps samples land up to 0.5 s out of phase, and this
  footage (fast flight over morphing textures) changes completely in
  0.5 s. Hasher verified deterministic and re-encode-stable
  (identical file → 0; JPEG re-encode → 0).
- **4 fps + phase-tolerant matching PASSES decisively:** all 40
  sampled frames of the inserted copy match the source window at
  Hamming 0–4 (median 0), vs the ≤31 match threshold.
- **False-positive controls clean:** v3 master self-match at 1 fps —
  zero off-diagonal pairs ≤31 (min 60); distinct takes of the same
  scene (H1-A city vs smears) cross-match min 104, zero ≤31.

**Verdict: ADOPT-CANDIDATE as the cheap first reuse screen, under a
sampling law: ≥4 fps sampling with phase-tolerant (windowed-min)
matching is REQUIRED — 1 fps sampling is a false-negative trap on
this footage. Hits stay eye-review flags, never auto-rejects (the
designed-bookend class of hit is real — see F-17). Runtime: ~7 min
per master at 1 fps in pure Python (the C++ vpdq would be seconds;
the hasher is the cost, parallelisable).**

## F-28 SSCD — ADOPT-CANDIDATE (the precise localiser)

Ran the released `sscd_disc_mixup` TorchScript model (ResNet-50,
512-d), frames at 2 fps, cosine matrix + diagonal-run detection
(cos > 0.75, run ≥ 6 frames), per the bank spec
(`finder-tests/f28_sscd.py`, `f28_sscd_bc.py`).

- **(a) Splice localisation — EXACT PASS:** the fixture's top
  diagonal run: offset 209 frames @2 fps = **104.5 s** (true splice
  offset 104.49 s), start frame 91 = **45.5 s** (true source start
  45.51 s), length 20 frames = **10 s** (the full inserted segment),
  mean cosine **0.939**. One run, at the true location, full length.
- **(b) Master self-scans:** v3 — **zero** diagonal runs ≥6 frames
  (off-diagonal max cosine 0.962: single-frame echoes, e.g. the
  designed bookend, never sustain 3 s, so the run rule ignores them).
  v2 — also **zero** runs (max 0.915). Neither master contains
  within-master reuse for SSCD to find: v2's historical reuse defect
  lived across versions/takes, not as repeated segments inside the
  v2 master itself. On the masters the pair reads "both clean" —
  SSCD's gate value is the splice/cross-version/master-vs-takes
  scan, which the fixture proves it performs exactly.
- **(c) Distinct takes control — clean by a wide margin:** H1-A city
  vs smears cross-similarity max 0.201, mean 0.067, **0/400 pairs**
  over the 0.75 threshold.

**Verdict: ADOPT-CANDIDATE** as the precise localiser behind the
F-31 screen. Runtime cost is the caveat: ~8 min embedding per master
on this throttled CPU (374 frames @2 fps), ~24 min wall for the
394-frame fixture under contention. Embeddings cache to `.npy`, so
a master is embedded once and re-scanned free. (Run note: mid-sprint
the VM's service layer restarted and transient systemd units briefly
couldn't see the workspace; the staged driver
`finder-tests/f28_driver.py` with per-stage `.npy` caches is the
resumable form.)

## F-29 CoTracker3 — DEAD on this VM + footage class

Simplified seeding (grid points; centre-region = subject group,
border = background; common mode = median background displacement),
offline predictor, released `scaled_offline` checkpoint.

**Environment blocker first:** at the originally planned sizes the
predictor is OOM-killed on this ~6 GB box — 11–12 s clips at
256×144 (exit 137, twice, once even running alone). The run below
uses the largest size that survives: **4 s clips (48 frames) at
12 fps / 192×108, 6×6 grid** — trims stated per the CPU rule.

| metric | v3 58.5–62.5 s (straddles 60.46 cut) | v2 163–167 s (O-B) |
|---|---|---|
| track survival share | **0.283** | **0.587** |
| background speed median (px/f) | 0.159 | 2.587 |
| subject-residual median (px/f) | 0.116 | 0.140 |
| subject-residual p10 | 0.097 | 0.037 |
| longest frozen-subject run | 0.5 s | 1.0 s |
| subject resid. across the cut | 0.113 → 0.267 | — |

The bank's pass bar (a) — tracks surviving >80% of frames — **fails
on both clips** (28% / 59%): CoTracker3 loses most points within a
second on morphing AI footage at these settings, so the surviving
population is biased toward static points and the group medians
can't be trusted (the v3 clip's *background* median sits at the
floor, 0.159, on a flight shot that is visibly fast). The target
pattern does appear in miniature in the v2 window — background
moving at 2.59 px/f while subject-residual hugs the floor (p10
0.037) with a 1.0 s frozen-subject run vs v3's 0.5 s — but an
instrument that fails its own survival bar on both controls is not
a gate. **Verdict: DEAD here. Revival condition: a GPU or a much
larger memory ceiling, starting from the v2 O-B window.**

---

## Sprint summary

- **Adopt as gates:** F-31 (vPDQ screen, ≥4 fps law) in front of
  F-28 (SSCD localisation) — the pair covers reuse detection at hash
  cost first, descriptor cost only on flags. F-17 M6 remains the
  standing halted-moment flag (unchanged).
- **Instruments, not gates:** F-05 flow curve (input to other
  measures), F-17 temporal signature (ledger-audit localisation).
- **Dead:** F-30 BeatAlign and F-27 mean-residual warping error (no
  separation on this control pair), F-05 cut-point energy contrast
  (wrong direction), F-29 CoTracker3 (fails its own track-survival
  bar on both controls; OOM on this VM above 4 s / 192×108).
- **Blocked upstream:** F-02 PVSync (code still unreleased,
  re-verified 2026-11-16).
