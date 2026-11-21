# Motion-Moment Detection for Coherent-Motion Cuts — Research + Spec

*Commissioned by the user's verdict on SHOW-3 E2 (Telegram msg 470, 2026-11-15): "the jump cuts between the scenes cause we're not properly using the first frame last frame philosophy and maintaining the coherent motion. We need to focus heavily on figuring out how to detect the motion moments."*

*Companion prototype: `prototype/motion_map.py` + `prototype/joint_eval_segs.py`, outputs in `prototype/*.json`. All SHOW-3 numbers below were measured on disk today, not quoted from memory.*

---

## 0. The problem, precisely

The Joint Gate (§6 of the Panel Workflow Spec v2 delta, `research_notes/joint-cohesion-method-20261115/report.md`) already contains the right rule — **J12. CUT ON THE MOTION PEAK**: *"Assembly places each JOINT cut at the local inter-frame motion peak within ±12 f of the planned joint."* The remedy ladder's first rung is the same idea: *"re-place the cut inside the handoff motion (±12 f)."*

But J12 is currently **unenforceable**, for three measured reasons:

1. **Nothing produces the curve J12 needs at the moment the decision is made.** Every existing tool either measures the *assembled master* after the fact (the Joint Gate itself) or emits one scalar per window (M6). No tool maps motion moments *inside a take, before assembly*, so there is no peak to place a cut on — coordinators conform full 240 f units end to end and the cut lands wherever the take happened to end.
2. **The one absolute motion floor in the gate just failed calibration.** §6 eye-checklist item 6 requires downstream head-motion MAE (f0→f0.5 s) **≥ 8**, a PROPOSED floor derived from PILOT-2 (lowest passing head there: 13.2). On SHOW-3 E2 the episode's own BASE (95th percentile of *all* in-unit adjacent-frame MAE) measured **6.74** — the floor sits above the 95th percentile of everything the show generates. All five heads (0.88–4.23) failed it while visibly moving; the gate passed them as "conditional" and filed the shortfall as J16 calibration data. **Lesson, stated as doctrine for everything below: a motion threshold must be a quantile of a measured distribution (the take's own, the episode's, or the calibration corpus's) — never an absolute constant carried across shows.**
3. **The tails are settled, and no trim can fix that.** The prototype (§5) shows all five SHOW-3 upstream tails are SETTLED at the cut and the last real motion event ends 2–6.5 s before the tail in four of five units. Within J12's ±12 f window the "local peak" is 0.54–0.71 MAE — noise. J12's window is not wrong; the *takes* contain no motion near the boundary to find. A motion-moment map is what turns this from a vibe into a per-joint, per-take fact known **before** assembly — early enough to pick a different joint frame for chaining, re-trim, or send the unit back with a motion-cliff brief instead of discovering it at the gate.

**What this report delivers:** (§1) how the field detects motion moments and places cuts on them, with sources; (§2) an exact inventory of what we already have on disk; (§3) the MOTION-MOMENT MAP spec — signals, event extraction, threshold doctrine, the joint decision procedure, and the Joint Gate plug-in; (§4–5) a working prototype and its results on SHOW-3 E2, cross-validated against the shipped GATE_LOG; (§6) SLERM candidates, ranked; (§7) honest limits.

---

## 1. Research — how motion moments are detected and used elsewhere

### 1.1 Editing practice: the cut belongs inside the movement, at matched phase

The craft literature is unanimous and specific enough to formalise:

- **Cutting on action / match on action**: cut in the middle of a movement and let the next shot complete it; the eye tracks the motion and doesn't register the join. If "the speed, hand position or screen direction differs between the two takes, the cut jumps instead of flowing" — i.e., the match variables are **phase, velocity, and screen direction**, not just "some motion on both sides." (flashboards.yaroflasher.com/learn/editing/match-on-action; Reisz & Millar, *The Technique of Film Editing*; Bordwell & Thompson, *Film Art*.)
- **Phase placement**: "Match the same physical phase across both shots, **cut before the movement's peak**, and let the second angle carry the action through completion." Cutting *at* the peak is second-best; cutting on the rising flank just before it is the textbook placement, because the peak itself is where the eye most expects continuation. Editors also need **handles** — extra frames either side of the action — or "short handles can leave no usable cut point." (thethingsyoumissed.com/blog/match-on-action)
- Murch's hierarchy (*In the Blink of an Eye*) puts emotion and story above physical continuity — a reminder that the map *advises*; it does not outrank the cutlist. (hanna-eng.com/guides/rythme-au-montage)

**Formalised for our pipeline:** a coherent joint wants (a) both sides inside a motion event, (b) the upstream cut on the rising flank or at the peak of its event, (c) the downstream head already inside the *same* event's continuation (in our chained generation: the downstream unit was generated from the joint frame, so its head event *is* the continuation — the map's job is to verify it actually starts moving and to pick which upstream frame seeds it), and (d) matched screen direction of the dominant motion.

### 1.2 The frame-difference family: our MAE curve is a standard signal

- **ITU-T P.910 Temporal Information (TI)**: the standardised motion-activity measure is built from exactly our signal — the per-frame difference image `M_n(i,j) = F_n(i,j) − F_{n−1}(i,j)` — aggregated per frame (P.910 uses the spatial *standard deviation*; the frame *mean* absolute difference is the same family and is what ffmpeg calls MAFD). "More motion in adjacent frames will result in higher values of TI." Our 320×180 gray MAE step curve is a legitimate, standards-adjacent motion curve; nothing exotic is needed. (ITU-T Rec. P.910 §5.3.2, itu.int; rfc.nop.hu/itu7/P/P0910e.pdf)
- **ffmpeg `scdet`**: computes MAFD (mean absolute frame difference) for every frame and derives a scene score; metadata keys `lavfi.scd.mafd` / `lavfi.scd.score` are set per frame. Good scdet thresholds sit in [8, 14] (percent). The `select` filter exposes the same idea as the `scene` variable (0–1). (ffmpeg.org/doxygen vf_scdet.c; patchwork.ffmpeg.org scenechangedetect doc)
- **ffmpeg `freezedetect`**: "calculates the mean average absolute difference of all the components of video frames and compares it to a noise floor" (default noise 0.003), firing only when a freeze lasts ≥ its duration parameter. Our own F-09 finder work already proved its blind spot: sub-0.5 s holds and holds masked by one small moving element pass it (DETECTION_FINDERS.md). It detects *absence* of motion, coarsely — a settle detector of last resort, not a moment mapper. (ffmpeg filters doc via dev.to/superfunicular comparison test, 2026-10-15)
- **ffmpeg `signalstats` / `vmafmotion`**: per-frame statistics and the VMAF motion score exist on the box if a second difference-based curve is ever wanted. (eliteai.tools ffmpeg-video-analysis reference)

### 1.3 Shot-boundary detectors: the adaptive-threshold pattern (and its limits)

PySceneDetect 0.7.x ships five detectors; two matter here:

- **ContentDetector**: per-frame weighted delta over HSV components (hue, saturation, luminance, edges) vs a fixed threshold (default 27). A spike detector on a frame-change curve.
- **AdaptiveDetector**: the *same* content score, but the threshold is a **rolling average of neighbouring frame scores** (`adaptive_threshold` 3.0, `window_width` 2, `min_content_val` 15) — "compares the ratio of each frame score to its neighbors… to suppress false cuts during fast motion." This is the published, battle-tested version of the doctrine §0 states: judge a frame's change **against its local distribution**, not an absolute number. (scenedetect.com/cli, scenedetect.com/docs/0.6.1/api/detectors.html, metavert.io/scene-detection)

Limits for our use: these detectors answer "is there a cut here?" — a spike question. A motion *moment* is the opposite shape (a sustained hump, not a spike), and a seam between two generated units is deliberately *not* a content spike of the shot-boundary kind. We borrow the adaptive-threshold machinery, not the detectors. (Our own survey already banked this: loop-02's finder table lists "F-04 PySceneDetect → its classical detectors are histogram/threshold — same family, subsumed.")

Learned detectors (TransNetV2 — per-frame boundary probability from a frame window; Souček & Lokoč 2020) are model-bound and already ruled **do not SLERM** in our survey; they also solve the wrong problem (finding cuts, not moments).

### 1.4 Onset detection: the algorithm skeleton transfers verbatim

Music onset detection solved "find the moments in a 1-D curve, robustly, across wildly different material" twenty years ago, and its canonical pipeline is:

1. Compute a **detection (novelty) function** from the signal — e.g. spectral flux: half-wave-rectified positive change, `SF(n) = Σ_k H(|X(n,k)| − |X(n−1,k)|)`.
2. **Peak-pick against an adaptive threshold**: a peak must exceed a local threshold (local median/mean over a window around it, plus an offset), be the maximum in its neighbourhood, and respect a minimum separation from the previous accepted peak. Dixon's MIREX formulation normalises the function, then accepts a peak at *t* iff it is the max within ±w, exceeds the local average over [t−m, t+w] by δ, and is ≥ a minimum distance after the last onset. (Bello et al., "A Tutorial on Onset Detection in Music Signals," IEEE TSAP 13(5), 2005; Dixon, "Simple Spectrum-Based Onset Detection," MIREX 2006 — webspace.eecs.qmul.ac.uk/s.e.dixon/pub/2006/mirex-onset.pdf)

Swap "spectral flux" for "positive derivative of the motion curve" and this *is* motion-onset detection. Our own house already runs this pattern in audio: **c11_superflux** implements locally-adaptive thresholding for onset envelopes (and its Bar-1 validation against librosa passed at corr 1.000000). The map's event extractor (§3.3) is this skeleton with hysteresis span extraction added, because a cut needs the event's *extent and phase*, not just its onset point.

### 1.5 Dense optical flow: the signal MAE can't give

Farneback dense flow (Gunnar Farneback, SCIA 2003; OpenCV `calcOpticalFlowFarneback` — polynomial expansion, pyramid, per-pixel (u,v)) yields two things frame-difference cannot:

- **Magnitude with the aperture caveat handled better than raw diff**: flow responds to *displacement*, so a lighting flicker or a dissolve raises MAE but little coherent flow; a small fast subject raises flow locally even when its frame-mean MAE is diluted.
- **Direction**: the mean (u, v) over the moving region gives screen direction — editing practice's third match variable (§1.1). A cut where the dominant motion reverses direction reads as a jump even at matched magnitude.

(OpenCV optical-flow tutorial, docs.opencv.org/4.13.0; ResearchGate, "Movement Detection and Moving Object Distinction Based on Optical Flow" — Farneback + Otsu adaptive thresholding of the flow field, the same adaptive doctrine applied spatially.)

**Dilution warning (from our own AGENTS.md, the S-16 clock lesson):** a whole-frame mean — of MAE *or* flow — dilutes a small moving subject below the noise floor. Any production version must also compute **regional curves** (a coarse grid, e.g. 3×3 cells, per-cell curves + the max-cell curve) and threshold/cluster rather than trusting the global mean alone. The prototype uses the global curve (it cross-validates against the gate); the spec (§3.2) includes the regional layer as a required v1.1 field, and it is SLERM candidate #2.

---

## 2. Inventory — what already exists on disk (exact)

### 2.1 The episode measurement harness: `measure.py` (per-episode copies)

`~/workspace/wubutv-network/new-era/episodes/E2_SHOW-3_the-roster/work/measure.py` (SHOW-1's copy at `E2_SHOW-1_the-machine/work/qc/measure.py` is the BLAM-audit variant of the same harness). Conventions: frames decoded via ffmpeg to **320×180 gray**; audio as 100 ms RMS windows vs the file's own median. It computes:

- `audio_metrics()` — BLAM A-metrics: median dBFS, t50/t90 (first time RMS sustains ≥50%/90% of median for 2 windows), lead-silence duration, head-vs-median dB, HF burst counts (5 kHz highpass envelope peaks > 6× local median) head vs mid-video control.
- `mae_buckets()` — the per-step MAE curve `mean|F[i+1]−F[i]|` over the first 10 s, summarised as 0.25 s buckets, a 3–10 s baseline mean, motion 0–0.5 s, V1 ratio, first bucket, strongest bucket. **This is a motion curve — but only the first 10 s, and only as bucket means.** BLAM V1/V2 checks read it.
- `blam()` — the A1–A4 / V1–V2 pass-fail assembly.
- `tail_scan()` — **the closest existing thing to a joint-frame finder**: scans the final 15% of steps and returns the *last* step whose following-step MAE ≥ the take's median MAE ("the joint frame"). Used for U5 in SHOW-3 (median MAE 3.04 logged). Limits: it returns one frame, with no event structure, no phase, no peak, and its bar is the take median — on a settled tail it returns whatever micro-motion last crossed the median, which may be a mouth movement 3 s before the end.
- `seam(png_a, png_b)` — MAE between two stills at 320×180 (the Joint Gate seam measure).

### 2.2 The Joint Gate implementations (post-assembly, on the master/joined)

- `E2_SHOW-2_the-tenth-second/work/joint_gate.py` — the faithful §6 implementation: decodes the joined file at 320×180 gray, computes the full step-MAE array, BASE = 95th percentile of in-unit steps **sampled every 24 f, 12 f edge-excluded**, seam MAE per boundary, joint strips (cut−6…cut+6) to `work/qc/`.
- `E2_SHOW-1_the-machine/work/qc/jointgate.py` — a variant: seam MAE at fixed cuts [240…1200] plus "downstream head motion" computed as **MAE(frame_cut, frame_cut+12)** — a 0.5 s *displacement* between two frames, not the mean of the 12 steps between them. A different quantity from SHOW-3's head MAE (mean of steps f0→f0.5 s); the two shows' item-6 numbers are not commensurable. (Worth regularising when the map lands.)
- SHOW-3's gate was run from `measure.py` + manual strips (`work/qc/JOINT_J1..J5_strip.png`).

All three measure **after assembly, at fixed 240 f boundaries**. None looks inside a take before the conform decision.

### 2.3 The TSM suite and M6 (`musicvideo/detection-research/tsm.py`, finders F-17/F-09)

- `tsm.py` computes the M1–M6 motion-metric family by decoding at **native 24 fps, 160×90 gray**. **M6 = duplicate-frame ratio**: the share of consecutive native-rate pairs whose mean abs-diff < τd = 0.0005, plus the longest consecutive run below τd. It is a *stillness share* — a scalar per clip or window.
- Calibration (`M6_CALIBRATION_MV14.md`, 46 KEEP + 5 REJECT MV-14 takes): the standing gate is **flag for EYE REVIEW when usable-window M6 > 0.10 AND window longest-dup-run ≥ 0.30 s — never auto-reject; never gate on full-take M6** (MEMORY.md standing rule). Zero of 46 KEEPs trip both conditions. M6 earned its place by discriminating MV-8 v2 (rejected, M6 0.197) from v3 (accepted, 0.049) — 4.0× — where freezedetect saw nothing.
- What M6 cannot do for joints: τd = 0.0005 sits at the *floor* of the difference distribution. M6 says how much of a window is near-frozen; it cannot rank motion magnitudes, find a peak, read a phase, or see direction. It is the map's settle detector, not the map.

### 2.4 c11_flow + flow_curve.py (`~/workspace/wubumv/tools/c11_flow/`)

- `c11_flow` — C11 Farneback dense optical flow re-implemented from the paper + OpenCV's `optflowgf.cpp`, libc/libm only, **validated against cv2 5.0.0 and Middlebury ground truth** (`c11_flow_validation.json`, `~/workspace/c11_flow_val/`). Modes: `flow` (writes W×H×2 float32 (u,v), prints mean_mag mean_u mean_v) and `mag` (mean magnitude only). Defaults match cv2 (pyr_scale 0.5, levels 3, winsize 15, iterations 3, poly_n 5, poly_sigma 1.1).
- `flow_curve.py` — builds a **per-frame motion-energy curve**: decodes to **160×90 gray at 12 fps** (the TSM/M6 convention), shells out to `c11_flow mag` per consecutive pair, and — given a cut time — reports the **cut-point energy contrast** (mean of the 12 curve values before vs after the cut; the GAP-1 / F-05 cut-energy check from the SLERM survey). This is the only existing per-frame motion curve in the kit besides `mae_buckets`' first-10-seconds. Limits: 12 fps (half the episode rate — a 2-frame event is invisible), one subprocess per frame pair, magnitude only in curve mode (direction is computed by the binary but not harvested), and it was built for MV masters, never wired into episode production.

### 2.5 ffmpeg filters on the box

ffmpeg (system) ships `scdet`, `freezedetect`, `signalstats` (verified in the filter list today). `scdet` was previously run against MV-8 v3 (logs `~/workspace/scdet_*.log`, `scene_mv8v3.log`); finder F-12 recorded it as a weak planned-cut finder (4/16). `freezedetect` is F-09 (negative result, §1.2). Neither is wired into the episode pipeline.

### 2.6 What is NOT here

- **PySceneDetect is not installed** in any environment found (system python: no `cv2`, no `scenedetect`; `~/workspace/cv2-throwaway/` and `detection-research/venv_cv2/` contain OpenCV headless 5.0.0.93 only). Installing it would buy the §1.3 detectors — which §1.3 argues we don't need.
- No tool anywhere in the workspace emits an **event list** (onset/peak/end/phase) for a video, for any purpose. That is the missing artefact.

---

## 3. SPEC — the MOTION-MOMENT MAP (M-MAP)

### 3.0 Where it plugs in (workflow first, algorithm second)

The map is a **pre-assembly** artefact. Per episode, after take QC and before conform:

```
for each accepted take/segment:  motion_map.py TAKE.mp4  -> work/qc/mmap_<unit>.json (+ .png curve strip, optional)
for each planned joint J(N,N+1): joint_plan.py mmap_N.json mmap_N+1.json -> joint plan record
```

The joint plan record is written into the CUTLIST/GATE_LOG *before* assembly and carries, per joint: the chosen **joint frame** (for chaining harvest / derived PEAK), the **trim offsets** for both sides, the predicted **phase pair** at the cut, the head verdict for unit N+1, and — when no shared event exists — a **NO-SHARED-EVENT** verdict that forces the remedy decision *before* assembly (re-brief the unit to end on a motion cliff, or declare the boundary a BREAK per J14) instead of after a failed gate.

After assembly, the existing Joint Gate runs unchanged on the master, plus two logged columns from the plan (predicted phase pair; head class) so J16 calibration can score the map's predictions against the gate's measurements and the eye checklist. The map starts life, like M6, as an **eye-review flag and planning instrument — never an auto-reject**.

### 3.1 Signals

Per take, at the take's native frame rate (24 fps for episodes):

| Signal | Definition | Source | Why |
|---|---|---|---|
| `mae[i]` | mean \|F[i+1] − F[i]\| over 320×180 gray frames | ffmpeg decode, the `measure.py` convention | Gate-compatible units: every existing number (seam MAE, tail MAE, head MAE, BASE) is this signal, so map values compare 1:1 with GATE_LOG history |
| `flow_mag[i]` | mean Farneback magnitude, 160×90, computed at native rate for the map (flow_curve.py's 12 fps is the MV convention; the map spec is native) | `c11_flow mag` per pair (prototype shells it; production = SLERM #1) | Displacement-sensitive; resists lighting/codec false motion |
| `flow_dir[i]` | mean (u, v) over pixels whose magnitude ≥ the frame's 75th percentile | `c11_flow flow` | Screen direction of the dominant motion — the third match variable (§1.1) |
| `dup[i]` | 1 if the 160×90 native-rate mean abs-diff < τd = 0.0005 else 0 | the M6 definition, per-step | Settle detection in the calibrated M6 unit |

The **primary curve** is `mae` (continuity with the gate). `flow_mag` is the **corroborating curve**: an event is *confirmed* when both curves agree it exists (see §3.3 step 5); disagreement is logged, not hidden (MAE-only event ≈ lighting/flicker suspect; flow-only event ≈ small fast subject — exactly the dilution case, escalate to the regional layer).

### 3.2 Regional layer (required v1.1)

Split the 320×180 frame into a 3×3 grid; compute `mae` per cell → 9 curves + `mae_max_cell[i]` = max over cells. Events are extracted on the global curve and on `mae_max_cell`; an event found only in one cell is annotated with its cell (e.g. "peak, cell 6 (lower-right)"). This is the S-16 rule applied to motion: never let a whole-frame average dilute the one moving thing. (Prototype: global curve only — see §5.4.)

### 3.3 Event extraction (the detector)

Input: primary curve `x[i]`, i = 0…N−2 (step i = transition frame i → i+1). All thresholds are quantiles of measured distributions (doctrine, §3.4).

1. **Smooth**: 3-tap moving average → `s[i]` (kills single-step codec spikes; 3 taps at 24 fps = 125 ms, below the shortest gesture of interest).
2. **Novelty**: `nov[i] = max(0, s[i] − s[i−1])` (half-wave-rectified flux, §1.4).
3. **Levels from the take's own distribution**: `θ_lo = median(s)`, `θ_hi = p75(s)`. (Prototype values; the *quantile levels* are the calibration knobs, set once from the J16 corpus per §3.4 — the form "quantile of the take's own curve" is the spec, the levels are data.)
4. **Hysteresis spans**: maximal runs of `s ≥ θ_lo` that contain at least one sample ≥ θ_hi. Merge spans separated by ≤ 6 steps (0.25 s — a breath between gestures is one event). Drop spans < 4 steps.
5. **Confirmation**: a span is a confirmed EVENT if `flow_mag` over the span has median ≥ the take's `flow_mag` median; otherwise it is logged as UNCONFIRMED (MAE-only). (Prototype: MAE-only, confirmation specified but not implemented — §5.4.)
6. **Per event**, record: `onset_step` (span start, refined: walk back from the span's first ≥θ_hi sample to the last step where `nov` was 0 or `s` was at a local minimum), `peak_step`/`peak_val` (argmax of `s` in span), `end_step` (span end), `settle_step` (first step after `end_step` from which `dup` runs ≥ 7 steps — 0.29 s, the M6 dup-run scale — or `s < θ_lo` sustained 7 steps), `dur_steps`, `class` (BLIP < 6 steps · GESTURE 6–48 · SUSTAINED > 48), `peak_phase_width` (steps within the span where `s ≥ 0.8·peak_val` — how wide the cuttable summit is), `dir_at_peak` (mean `flow_dir` over peak ±2 steps).
7. **Phase function** `phase(i)`: SETTLED (not in a span, or in a `dup` run) · RISING (in span, before peak, `nov[i] > 0`) · PEAK (|i − peak_step| ≤ 2 or inside `peak_phase_width`) · FALLING (in span, after peak).

### 3.4 Threshold doctrine (the calibration contract)

- **No absolute MAE/flow constants anywhere in the map.** Every bar is one of: (a) a quantile of the take's own curve, (b) a quantile of the episode's in-unit step distribution (BASE and friends, computed exactly as §6 computes BASE), or (c) a quantile of the J16 calibration corpus (the first three v2 episodes' logged joints, growing thereafter).
- The only fixed numbers are **structural** — window lengths and separations — and each is inherited from an existing calibrated constant, not invented: ±12 f search window (J12), 12 f edge exclusion (§6 BASE), 0.30 s settle run (M6 calibration), 2–4 f duplicated-action trim (J12), 6-step merge gap and 4-step minimum span (¼ s and ⅙ s at 24 fps — below these, a "motion" is a blink or a codec artefact, and both sit under the 0.30 s dup-run scale the MV-14 corpus already validated as the shortest interval that matters).
- **Calibration protocol** (mirrors how M6 was calibrated on MV-14 KEEPs): run the map over every take and joint of the three J16 episodes; choose the quantile levels in §3.3/§3.5 so that (i) every eye-passed joint's chosen cut reads phase-coherent or is honestly flagged, and (ii) the known-bad configurations flag — the worked example being SHOW-3 J2's head (§5.3). Levels are then frozen into the spec by amendment, with the corpus cited — the same lifecycle §6 already prescribes for its own bars (J16).
- Until calibration completes, every map output is advisory + logged. Nothing auto-rejects. (The M6 precedent: a metric earns gate status by discriminating accepted from rejected work on a corpus, or it stays a flag.)

### 3.5 The joint decision procedure

Given maps for upstream unit U (steps 0…a) and downstream unit D (steps 0…b), and the planned joint between them:

1. **Candidate zone**: upstream steps [a−48, a] (final 2 s) and downstream steps [0, 48]. (Wider than J12's ±12 f on purpose: the map first answers "*is there* a shared event near this boundary at all?"; J12's ±12 f then governs the final placement *within* the chosen event.)
2. **Shared-event test**: a shared event exists iff U has an event whose span intersects its final 48 steps **and** D has an event whose span intersects its first 48 steps **and** the phase pair at the proposed cut (see step 3) is coherent. If either side has no event in its zone → **NO-SHARED-EVENT** (name the deficient side and its settle point: "U settled from step 132/239; D's first event onsets at step 48"). The coordinator then takes the pre-assembly remedy branch (§3.0) instead of shipping a settled cut to the gate.
3. **Cut placement within a shared event** (J12, operationalised): choose the upstream cut step `c` inside U's boundary event **on its rising flank, 0–4 steps before `peak_step`** (cut before the peak, §1.1); if the event's peak is wider than 4 steps (`peak_phase_width`), cut at the start of the summit. Trim U to end at frame c+1. D is *not* trimmed at the head (its frame 0 is the generated continuation of the joint frame); instead the **joint frame for chaining/PEAK derivation is frame c+1 of U** — the map replaces today's fixed harvest (SHOW-3 harvested every joint frame at seg f228 by convention) with the measured peak-flank frame.
4. **Phase-pair verdict** at the chosen cut: COHERENT if `phase_U(c) ∈ {RISING, PEAK}` and D's head class (§3.6) is IN-MOTION or RAMP-with-onset ≤ 6 steps; WEAK if either side is FALLING-into-settle or D's onset is 7–12 steps; INCOHERENT otherwise. Logged, with both phases named.
5. **Direction check**: sign agreement of the dominant axis of `dir_at_peak` (U's boundary event) vs D's head event `dir_at_peak`. A reversal is logged as DIR-REVERSED (the editing-practice jump condition, §1.1) — advisory in v1, since generated continuations may legitimately counter-move; the J16 corpus decides if it earns a bar.
6. **Velocity ratio**: `peak_val` of D's head event ÷ `peak_val` of U's boundary event, both expressed in units of the episode BASE (dimensionless, cross-show comparable). Logged; no bar until calibrated.

### 3.6 Head verification (replaces the absolute item-6 floor)

For each unit's head (first 24 steps), the map emits:

- `head_class`: **IN-MOTION** (an event covers step 0) · **RAMP** (first onset at steps 1–12) · **LATE-ONSET** (first onset at steps 13–24) · **SETTLED-HEAD** (no event in the first 24 steps).
- `head12_mean` (mean of steps 0–11 — the existing gate quantity) **and its percentile within the episode's in-unit step distribution** (the number item 6 should have been).

**Proposed item-6 replacement** (for the §6 amendment, after J16 calibration): *"Motion is alive on both sides: the upstream tail is not settled (its map shows an event intersecting the final 12 steps, or the joint was placed inside an event per §3.5), and the downstream head is class IN-MOTION or RAMP, with head12_mean at or above the 25th percentile of the episode's in-unit step distribution."* Every term is distribution-relative; §5.3 shows this rule passes and flags the right joints on SHOW-3 where the ≥ 8 floor failed all five.

The same percentile treatment applies to the BLAM V1/V2 head checks if they are ever ported across shows (BLAM's V2 already half-does this: "first bucket ≥ 50% of strongest bucket" is a within-take relative bar; its absolute alternative "≥ 4.0" is the part that will break on a quiet show, exactly as item 6's 8.0 did).

### 3.7 Outputs

Per take: `work/qc/mmap_<unit>.json` — `{file, frames, fps, curve_stats {p25…p99 for mae and flow_mag}, th_lo, th_hi, events[…], head{…}, tail{last_event, settled_from_step, final12_mean, final12_percentile, phase_at_final_step}}`. Per joint (in GATE_LOG, pre-assembly section): the §3.5 record. Curves also written as CSV (`mmap_<unit>.csv`: step, mae, flow_mag, dup) so any future tool — including a C11 port — reads the same artefact.

---

## 4. Prototype — what was built

`prototype/motion_map.py` (numpy + ffmpeg only, no new dependencies): decodes at 320×180 gray native rate, builds the MAE step curve, smooths (3-tap), extracts events by the §3.3 hysteresis (θ_lo = take median, θ_hi = take p75; merge ≤ 6 steps; min span 4), and emits the map JSON with head/tail states. `prototype/joint_eval_segs.py` evaluates a joint from two segment maps + the true seam MAE between segment frame files. `flow_curve.py` (existing, §2.4) was run as-is for the corroborating flow curve.

**Frame-accuracy gotcha found by the prototype (implementation law for any production version):** decoding `work/joined.mp4` through a plain ffmpeg rawvideo pipe yields **1444 frames**, not the probed 1440 (the concat carries 60.13 s of AAC-primed timing; default vsync duplicates steps to fill). Nominal cut indices (240, 480, …) therefore do **not** land on the true seams in a naively decoded joined file — a seam read at step 239 of that decode gives MAE 7.46 where the true seam is 21.10. The prototype's joint numbers below are computed **per segment** (each seg decodes to exactly 240 frames), which is the correct unit of analysis pre-assembly anyway. A production map run on a master must decode with frame-exact settings (`-vsync 0` + probed frame count assertion) or work from segments.

## 5. Prototype results — SHOW-3 E2 "The Pass, Done Properly"

Shipped units: U1_t8, U2_t3, U3_t1, U4_t5, U5_t4, U6_t1 → seg1…seg6 (240 f each). Actual cuts sit at the segment boundaries (full-take conform, no trims).

### 5.1 Cross-validation against the shipped GATE_LOG (the map measures the gate's own numbers)

| Quantity | GATE_LOG | Prototype | Δ |
|---|---|---|---|
| Seam MAE J1…J5 | 21.10 / 21.64 / 30.42 / 24.26 / 9.23 | 21.12 / 21.64 / 30.41 / 24.29 / 9.24 | ≤ 0.03 |
| Tail MAE (final 12 f) J1…J5 | 0.64 / 0.37 / 2.50 / 0.25 / 1.24 | 0.62 / 0.34 / 2.40 / 0.24 / 1.21 | ≤ 0.10 |
| Head MAE (0–0.5 s) J1…J5 | 3.10 / 0.88 / 1.44 / 2.06 / 4.23 | 3.04 / 0.87 / 1.43 / 2.07 / 4.22 | ≤ 0.06 |
| U1_t8 head motion 0–0.5 s (BLAM V1 read) | 12.75 | 12.49 (mean steps 0–11) | 0.26 |
| U5 tail: "final-15% MAE below median (3.04)" | settled, median 3.04 | settled from step 132, final-12 mean 1.21 vs take median 2.29 (joined-curve read) | consistent |
| Episode BASE | 6.74 (sampled every 24 f) | 7.24 (all in-unit steps, joined decode) | sampling |

The map's signal chain is the gate's signal chain. Nothing needs re-basing to adopt it.

### 5.2 The five joints, mapped (upstream tail / downstream head at the actual cut)

| Joint | Upstream tail state | Last upstream event (steps of 239) | Downstream head | Verdict the map would have issued pre-assembly |
|---|---|---|---|---|
| J1 U1→U2 | SETTLED at cut; final-12 0.62; settled from step 84 | SUSTAINED 0–83, peak step 5 (17.36) — the envelope landing | RAMP, onset step 1, head-12 3.04 | **NO-SHARED-EVENT (upstream)**: no event in U1's final 48 steps; best "peak" in the last 24 steps is 0.71 — J12 has nothing to place on |
| J2 U2→U3 | SETTLED at cut; final-12 0.34; settled from step 121 | SUSTAINED 1–120, peak step 77 (4.04) | **SETTLED-HEAD**: first event onsets at step 48 (2.0 s in), head-12 0.87 | **NO-SHARED-EVENT (both sides)** — the episode's worst joint by map and by gate head MAE alike |
| J3 U3→U4 | SETTLED at cut; final-12 2.40 (the least settled tail — Dispatcher's head-turn per GATE_LOG) | main event ends earlier; a 4-step BLIP at 234–237 (3.91) is the last gasp | RAMP, onset step 12, head-12 1.43; head event peaks 15.33 at step 34 | **NO-SHARED-EVENT (upstream)**, marginal: tail carries speech-level motion but no gesture; downstream is alive from 0.5 s |
| J4 U4→U5 | SETTLED at cut; final-12 0.24 (the stillest tail) | SUSTAINED 12–103, peak step 34 (15.33) | RAMP, onset step 12, head-12 2.07 | **NO-SHARED-EVENT (upstream)** |
| J5 U5→U6 | SETTLED at cut; final-12 1.21; settled from step 132 | SUSTAINED 12–131, peak step 88 (6.40) | RAMP, onset step 1, head-12 4.22 (strongest head; event peaks 8.51 at step 20) | **NO-SHARED-EVENT (upstream)** — yet J5 is the gate's best joint (seam 9.23): a strong downstream head carried a settled tail |

### 5.3 What the map proves (and what it changes)

1. **J12 was vacuous on this episode.** In the last 24 steps of the five upstream segments, the maximum step MAE is 0.71 / 0.54 / 4.31 / 0.58 / 1.36 — against segment medians of ~1.3–2.3 and peaks of 4–17. There is no "local inter-frame motion peak within ±12 f" at J1, J2 or J4 in any meaningful sense; the rule as written cannot distinguish those cuts from J3/J5. The map replaces the fiction with the fact, per joint, before assembly.
2. **The failure is structural, not editorial.** On dialogue units this generator front-loads the physical action (U1's envelope event is steps 0–83; U4's palm event ends at step 103) and settles into talking heads for the back half. By the 10 s wall, *both* sides of every joint are at or below speech-motion level. No trim, ramp, or 2–4 f duplication manufactures a shared event. The levers that remain are exactly the ones the map now triggers early: **(a)** harvest the chaining joint frame inside the upstream event and let the downstream unit's generated continuation supply the motion (the downstream heads prove the generator *can* start moving — onsets at steps 1–12 in four of five), **(b)** brief units to end on a motion cliff (already open risk (a) in the cohesion report — the map makes it a measured script gate: a take whose map shows no event in its final 48 steps is not chain-eligible), or **(c)** declare the boundary a BREAK and design the match (J14).
3. **The item-6 replacement (§3.6) discriminates correctly where the absolute floor failed.** Episode in-unit step distribution (joined, all steps): p25 0.89 · p50 2.29 · p75 3.84. Head-12 means as percentiles: J1 3.04 (≈p65) · J2 0.87 (≈p25, and SETTLED-HEAD class — flagged) · J3 1.43 (≈p40) · J4 2.07 (≈p47) · J5 4.22 (≈p78). Under the proposed rule (IN-MOTION/RAMP **and** head-12 ≥ p25), J1/J3/J4/J5 pass and J2 alone flags — matching the eye record (all five passed item 6's *intent*; J2's head was the weakest) instead of failing all five against a borrowed constant.
4. **Flow corroborates MAE on the one take run both ways.** U1_t8 via `flow_curve.py` (160×90, 12 fps): curve max 4.61 at step 13, mean of first 12 steps 2.53 vs last 12 steps **0.10** (25× falloff), median 0.29. Same shape as the MAE map (head event, settled tail) in a displacement signal that lighting can't fake. The two-signal confirmation in §3.3 is viable with existing tools.
5. **Per-take maps of the shipped takes** (for the calibration corpus): U1_t8 — head IN-MOTION (mean 0–12: 12.49), one SUSTAINED event 0–83, settled from 190 (per-step `dup`-free read: last ≥median step 189). U2_t3 — head RAMP (onset 1, mean 3.07), event 1–120, settled from 121. U5_t4 — head RAMP (onset 12), event 12–131, settled from 132. U6_t1 — head RAMP (onset 1, mean 4.25), events 1–70 and 175–224 (the page-lift and the Dispatcher writing — the only shipped take with a *late* event; it is also the terminal unit, whose tail needs no joint).

### 5.4 Prototype limits (stated, not hidden)

- Global curve only: no regional (3×3) layer, no flow confirmation, no direction — §3.2/§3.3 steps 5–6 are spec, not code. On dialogue takes the hysteresis span merges speech-motion into one long SUSTAINED event (e.g. U2's steps 1–120): the map resolves *events vs settle* well and *gestures within speech* poorly. For cut placement only the boundary zones matter, where the reads are unambiguous; a finer gesture layer would need peak-picking on the novelty function inside spans (specified in §3.3 step 6 via `peak_phase_width`, not prototyped).
- θ levels (median / p75) are the prototype's defaults, not calibrated values — §3.4's protocol owns that step.
- Maps were run on the shipped segments/takes of one episode, all one show's grammar (locked-off two-handers). A montage show will produce denser event fields; the distribution-relative design is precisely so the same code reads both.

---

## 6. SLERM candidates (ranked)

1. **`c11_mmap` — a C11 motion-map extractor on the c11_flow chassis.** One decode pass producing the MAE curve, the Farneback magnitude/direction curves, and the dup series together, at native rate, emitting the §3.7 JSON/CSV directly. Why: the prototype's Python shells ffmpeg for a rawvideo pipe and `flow_curve.py` shells the flow binary **once per frame pair** (119 subprocess spawns per 10 s take; ~8 s wall for one take's flow curve alone, ~35 s per episode for MAE maps). The components are all already SLERM'd and validated (c11_flow's Farneback matched cv2 + Middlebury GT); the map is a composition job — pure LEGO-rule work from the user's own modules. This is the production form of the detector.
2. **Regional flow/MAE with threshold-and-cluster (the anti-dilution layer).** Per-cell (3×3 or 4×4) curves plus a max-cell curve, and — for the flow field — Otsu-style adaptive thresholding of per-frame magnitudes to find *where* the motion is before averaging direction over it (§1.5). Why it matters: the global mean is the known failure mode (S-16 clock lesson); the map's direction and small-subject reads are only trustworthy regionally. Small, well-bounded, and it upgrades every consumer of the curves, not just joints.
3. **A novelty/peak-picking library shared between audio and motion.** c11_superflux already implements locally-adaptive threshold peak-picking for audio onsets; the motion map's onset refinement (§3.3 step 6) is the same algorithm on a different curve. Extract the shared core rather than writing it twice — the LEGO rule applied inside our own tree.

**Explicitly NOT candidates:** PySceneDetect (any detector) — same signal family as our MAE curve with a spike question attached; subsumed, and not installed (§1.3, §2.6). TransNetV2 — model-bound, already ruled out by the SLERM survey. ffmpeg `freezedetect`/`scdet` — already on the box as filters; nothing to re-implement, and both answer the wrong question (§1.2). OpenCV — exists only in throwaway venvs; c11_flow already replaced the one function we needed from it.

---

## 7. Honest limits of the whole approach

- **The map certifies motion, not sameness.** It can prove both sides of a cut are inside a motion event at matched phase, direction, and comparable velocity. It cannot prove the *same action* continues — that remains the eye checklist's identity/carry items and the chaining discipline (J4: never chain from a conditional take). A perfectly phase-matched cut between two different gestures will still jump; the map narrows where the eye must look, it does not replace the look.
- **MAE is promiscuous.** Dissolves, flicker, film grain, and camera drift all raise it. The flow-confirmation and regional layers mitigate; they do not eliminate. UNCONFIRMED events must stay visible in the log rather than being silently dropped or silently trusted.
- **On this show's grammar, the map's most frequent verdict will be NO-SHARED-EVENT** — because the takes genuinely settle. That is the map working, not failing: it converts an invisible structural property into a per-unit number the writers' room and the vehicle prompts can be aimed at (end on a motion cliff), and it stops assembly from spending its remedy ladder on cuts that were never going to cohere.
- **Calibration is owed, not done.** §3.4's protocol needs the three J16 episodes mapped and the quantile levels frozen by amendment. Until then the map is an instrument, not a gate — the same probation M6 served, and for the same reason.

---

## Sources

- ITU-T Recommendation P.910, §5.3.2 Temporal Information — itu.int (T-REC-P.910-202310); text at rfc.nop.hu/itu7/P/P0910e.pdf
- ffmpeg `scdet` source & scenechangedetect documentation — ffmpeg.org/doxygen/6.0/vf__scdet_8c_source.html; patchwork.ffmpeg.org/project/ffmpeg (lance.lmwang, 2019)
- ffmpeg filter behaviour comparison (freezedetect / select scene / mpdecimate) — dev.to/superfunicular, 2026-10-15
- PySceneDetect CLI & detector API (ContentDetector, AdaptiveDetector parameters) — scenedetect.com/cli; scenedetect.com/docs/0.6.1/api/detectors.html; overview at metavert.io/scene-detection
- Bello, Daudet, Abdallah, Duxbury, Davies, Sandler, "A Tutorial on Onset Detection in Music Signals," IEEE Trans. Speech & Audio Processing 13(5), 2005 — hajim.rochester.edu (Bello_2005.pdf)
- Dixon, "Simple Spectrum-Based Onset Detection," MIREX 2006 — webspace.eecs.qmul.ac.uk/s.e.dixon/pub/2006/mirex-onset.pdf
- OpenCV, "Optical Flow" (Lucas–Kanade, Farneback dense flow) — docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html
- Match on action / cutting on action (phase, direction, peak placement, handles) — flashboards.yaroflasher.com/learn/editing/match-on-action; thethingsyoumissed.com/blog/match-on-action; human.libretexts.org, "Continuity Editing" (Reisz & Millar lineage); hanna-eng.com/guides/rythme-au-montage (Murch)
- House documents: `research_notes/joint-cohesion-method-20261115/report.md` (§5–§6, J12–J16); `E2_SHOW-3_the-roster/work/GATE_LOG.md` and `work/measure.py`; `E2_SHOW-2_the-tenth-second/work/joint_gate.py`; `E2_SHOW-1_the-machine/work/qc/jointgate.py`; `musicvideo/detection-research/tsm.py`, `DETECTION_FINDERS.md` (F-09/F-12/F-17), `M6_CALIBRATION_MV14.md`; `wubumv/tools/c11_flow/README.md` + `flow_curve.py`; MEMORY.md (M6 standing gate)
