# MV-15 'Unread DMs' — PROGRESS (disk truth for the parent)

Updated: 2026-11-13 ~09:05 EST. Coordinator: subagent a45b59b5.

## Stages 0–3 DONE (see AUDIO_ANALYSIS.md, LYRIC_TIMELINE.md,
## SCENE_PLAN.md, ASSET_BOARD.md, REFERENCE_STACK.md)
Measured 150.0 BPM (stated 152 wrong). Performed grid 310 words,
34 lines; breakdown extras confirmed vs the sheet. Graphics-first
design, zero-still gate (no near-dup run >= 2f in the master).

## Stage 4–5: GENERATION COMPLETE — 24/24 scenes KEEP
33 fired total (24 + 9 re-fires), 0 refusals, 0 budget stops.
Anime lock ruled after pilot style split (S01 t1/S07 t1 photoreal
rejects). Name-leak rule learned (S15/S16 G2): fired text never
carries the character name. Full rows in TAKE_HISTORY.md,
VOLLEY_PROGRESS.md. G7 (take-ASR word-set overlap): ALL 8 lips
takes 1.00 — S01 t3, S04 t2, S08 t1, S11 t2, S16 t2, S18 t1,
S21 t1 (two lines), S23 t1. Line ratios all in the 0.80–1.25
band except S21 line 2 at 1.554 (legal vs the 0.5x floor,
disclosed in CUTLIST).

## Motion scan (work/analysis/motion_scan.json)
Head/tail still runs mapped per take; span windows chosen to
avoid them. S18 + S20 are ~16fps-effective sources (dup pairs) —
their segments get ffmpeg minterpolate. S05 freeze span gets the
full-frame drifting-orb graphic layer (honest motion, not grain).

## NEXT: build segments (phrase warps) -> overlays (kinetic ASS
## from the performed grid, counter PNG HUD, MUTE stamp, glitch
## spans, ident) -> final encode -> gates (zero-still measured,
## audio agreement, hook mouth reads) -> chat copy -> docs.

2026-11-13 RECOVERY#2 (56294157 died 08:32 daemon restart, zero output): segment manifest checkpointed to work/segments/MANIFEST.json; S21 plan = t1 L28 phrases + t2 L29 fragment (0-3.48s, factor 1.0), target 207f; master target 4167f.

2026-11-13 RECOVERY#2: 13 motion segments re-rendered to exact plan spans (uniform warp, speeds 0.658-1.359x, all inside caps; original segments had been rendered at raw trim length, short 92f total). S21 built from t1 (L28 phrases) + t2 (L29 fragment, factor 1.000). Conform + overlays next.

2026-11-13 RECOVERY#3 (parent-spawned; adc063f5 died 10:12 EST mid-conform): state verified — conformed S01–S05 valid (136/154/154/157/165f), segments S06–S24 on disk (S14/S16/S18 1f short, S20 68f vs 70f). Resuming: conform S06–S24 via work/conform_rest.py (patched branches only; S20 gets a slow pan instead of a 2-frame clone tail). Overlays (kinetic.ass already rendered), final encode, gates, visual gate, ledger reconcile to follow.

2026-11-13 RECOVERY#3: CONFORM COMPLETE — all 24 scenes frame-exact (S06–S24 via conform_rest.py, every count OK; total 4167f). S20 conformed with a slow linear pan (segment was 68f vs 70f span; no clone-dup tail). kinetic.ass re-rendered (53 events). Final encode running.

2026-11-13 RECOVERY#3: FINAL ENCODE COMPLETE — masters/mv15_unread_dms_16x9.mp4 written (788,447,363 B; pass1 pregrain 81.3 MB + grain pass per final_encode.sh; two latent script bugs fixed en route: concat-list absolute paths, hue eval option). Gates running.

2026-11-13 RECOVERY#3 GATE FINDING: first master encoded (md5 eb67f409, 4167f, SEI crf=18.0, AAC, faststart, audio corr 0.9990/0.9979 — all PASS) and MASTER zero-still longest run = 0. BUT pregrain longest run = 4 and a full enumeration found 107 near-dup runs >=2 in pregrain (S05 head, S09 stretch pattern, S13, S17 tail, S18 dense, S19 tail, S20 tail, S24 tail) — per the SCENE_PLAN grain-honesty rule that is NOT a pass. Fix in progress: flagged scenes are being re-conformed with real motion (slow pan + geq light-pulse, both measured per scene by scan_runs.py before re-assembly). gates.py OOM-died on its whole-buffer decode; gates_run.py is a streaming twin with identical math (results in work/qc/GATES.json). eq-based pulse does NOT evaluate per-frame in this ffmpeg build (measured identical to control); hue DOES (S19 inversion verified on frames 124.60 vs 124.85).

2026-11-13 RECOVERY#3: ZERO-STILL HONESTY FIX APPLIED — S05/S09/S13/S17/S18/S19/S20/S24 re-conformed with slow 256px pan + geq light-pulse (gain+offset, per-frame); every fixed scene scan-verified 0 near-dup runs >=2 at conform level (work/conform_fix2.py, conform_fix3.py; originals backed up in work/conformed_orig/). Re-running final encode for the honest master.

2026-11-13 RECOVERY#3: HONEST MASTER ENCODED — masters/mv15_unread_dms_16x9.mp4 (792,109,501 B) from the fixed conforms. Final gates + pregrain enumeration running.

2026-11-13 RECOVERY#3 FINAL: GATES PASS ON THE HONEST MASTER — masters/mv15_unread_dms_16x9.mp4 md5 0bef4ae5dd2217e481b3ccff840100ac (792,109,501 B, 4167f, CRF 18 SEI, AAC 48k stereo, faststart, audio corr 0.99895/0.99785). ZERO-STILL: master longest run 0 AND pre-grain longest run 1 with full enumeration 0 runs >=2 on both files — the gate passes on picture motion, not grain (v1 master eb67f409 SUPERSEDED on this rule, see work/GATE_LOG.md). Chat copy masters/mv15_unread_dms_16x9_chat.mp4 md5 05d781d6df6cb36acebd1c6096217bc4 (47,527,059 B, 4167f, AAC copied). Visual gate PASS (work/VISUAL_GATE.md) incl. S05 orb-span eye-check and the S23 right-wall G2 zoom (abstract bubbles, no readable posters). Ledgers reconciled: 32 fires / 25 KEEP / 7 REJECT; TAKE_HISTORY completed with the s21_t2 row.

SHIPPED EVENTS (for USED_EVENTS): S01 The Swarm (opens) · S02 The Swarm (payoff) · S03 glitch-grammar storm (form event) · S04 stance (mouth event) · S05 "The Freeze" (9.1-inverse) + drifting orb · S06 room-lights answering (light event) · S07 Interface Takeover (12.4) · S08 Clone Handoff setup (4.1) · S09 Clone Handoff (4.1) · S10 Prop Cascade (5.2) · S11 mirrored pair (form event) · S12 Pose-Strike Chain (8.1) · S13 The Runaway Object (5.4) · S14 beat light-hits (light event) · S15 Interface Takeover escalated (12.4) · S16 Swarm return (4.2) · S17 Dance With Your Double (4.5) · S18 stance (mouth event) · S19 Palette Snap (8.3) · S20 exit beat (form event) · S21 peak stance (mouth event) · S22 Scatter & Reform (9.2) · S23 The Wrong-Size Prop (2.3) · S24 The Ident Event (12.5).

STATUS: COMPLETE — assembly done, gates logged (work/GATE_LOG.md, work/qc/GATES.json), visual gate done (work/VISUAL_GATE.md). Delivered flag + commit are the parent's step.
