# MV-5 v3 assembly notes (incremental — written as stages complete)

## 0. Sources verified (2026-11-06 ~03:00 EST)
- Base: work/V2_ASSEMBLY.md + work/assembly_fit_mv5_v2.json (4954 frames, 29 scenes).
  v2 master on disk md5 1c252e69032ab028c5e9a72ce974ea46 ✓ (matches V2_ASSEMBLY.md).
- track.mp3 md5 0c1bcafa568547e2d4fa36e133ad3626 ✓; track.mp4 md5 0cbd7551f3827ebab33bd1077f376609 ✓.
- Volley 14 QC: work/qc_v14/qc_v14_verdicts.md — 6 KEEP / 0 REJECT. Take md5s
  re-verified on disk: t11 4b91522f…/t12 f2de5e0d…/t13 479a404a…/t14 3d047b2b…/
  t15 be27fe25…/t16 c60c1e45… — all match the verdicts file.
- Volley 15 QC: work/qc_v15/qc_v15_verdicts.md — 0 KEEP / 2 REJECT (both PACING).
  Take md5s re-verified on disk: s07_t2 39ba0cf638d31f165accd2101ef487e8 ✓,
  s07_t3 023a9fc3aa862a7c324a0ffa18807ffc ✓, s28_t5 b347c9faf46a1fd51902152cd048b28e ✓.
- s28_t5 DISCARDED (no QC row, no verdict) — must not enter the cut. s07_t3 unused.

## 1. v3 plan (build_v3_plan.py → work/assembly_fit_mv5_v3.json)
- Total frames UNCHANGED: 4954. Only S07 and S21 change; all other 27 scenes
  copy the v2 plan verbatim.
- S07 (234f): piece 3 cover-L15 (s08_t2 205–237, 32f) REPLACED by
  s07_t2 sf=0 ef=61 warp=0.5234375 (1.34/2.56, playback 1.91x) out=32,
  kind "line-L15-warped", dst 51.468–52.801. DISCLOSED OUT-OF-BAND WARP
  (parent decision in the brief; L15 is structural for per-line generation,
  pace floor ~2.2–2.6s/line; closed-mouth cover under a sung line is banned
  by the user's 2026-11-06 law).
- L15 word-start offsets under the uniform warp, computed INDEPENDENTLY from
  work/qc_v15/qc_v15_results.json take word starts (One 0.0, small 0.5,
  look 1.24, from 1.72, you 2.1) × 0.5234375 vs song starts from
  work/gemini_song_words_aligned.json (One 51.46, small 51.728, look 51.996,
  from 52.264, you 52.532):
  One 0.000, small −0.006, look +0.113, from +0.096, you +0.027.
  Max |offset| +0.113s (look); median |offset| 0.027s. All inside the ±0.50s
  working band. (Brief's claim — look +0.113, from +0.096 — confirmed.)
- S21 (227f): all 11 v2 pieces REPLACED by 9 montage pieces (warp 1.0,
  cuts on the v2 line boundaries, GIRL-first alternation):
  L82 GIRL 25f t12 sf12–37; L83 CAT 27f t13 sf12–39; L84 GIRL 27f t16 sf12–39;
  L85 CAT 26f t14 sf156–182; L86 GIRL 26f t11 sf12–38; L87 CAT 24f t15 sf84–108;
  L88 GIRL 32f t15 sf132–164; L89 CAT 22f t13 sf60–82; tail 18f t14 sf12–30.
  All slices inside the QC-noted windows (qc_v14 verdicts). [REVISED
  ~03:40 EST after the build-1 gate: L85 → t13 sf82–108, L87 → t13
  sf36–60 — see §3. One 3-frame overlap (t13 f36–39 in both L83 and
  L87) is the only slice sharing; it is disclosed in §3.]
  s21_t7 NOT used (v2 grey-rescue take stays unused); no per-line sung take.
- S06/S07 passage: s06_t1 L10/L11, s06_t2 L12, s07_t1 L13/L14/L16,
  s07_t2 L15 — cuts fall on singer changes only.
- L110b keeps the v2 structural cover (s28_t3 tail + captions).
- Captions: captions_16x9_v2.ass (437 events) copied to captions_16x9_v3.ass
  (song grid unchanged, so the file is byte-identical — md5 recorded in §2).

## 2. Encode
- assemble_mv5_v3.py written (adapted from the v2 script: FIT v3, OUT v3,
  captions v3; asserts track md5 + banned takes absent + 4954f total).
- Encode LAUNCHED detached 2026-11-06 ~03:03 EST (setsid nohup, PID 20806),
  log work/assemble_v3.log. Master file created (0 B at launch, growing).
  (First `tail` of the log raced the file creation — file exists, 1273 B.)
- BUILD OK 2026-11-06 ~03:13 EST (log tail "BUILD OK"). Master:
  masters/mv5_easy_now_easy_now_16x9_v3.mp4, md5
  c6643ffdbd2ebfff598f0b224dbc650e, 119,790,625 B, size stable across a 5s
  re-stat, 1280x720, 24fps, 4954 frames, 206.417s, h264 + AAC 48kHz stereo.
- (gate pending)

## 3. Gate (on the master itself) — BUILD 1: FAIL on two bridge fragments
- Build 1 master (md5 c6643ffdbd2ebfff598f0b224dbc650e, 119,790,625 B) gated
  2026-11-06 ~03:21–03:33 EST, validate_master_mv5_v3.py (PID 25225),
  results work/gate_v3/gate_v3_results.json (build 1).
- (a) AUDIO IDENTITY: PASS — lag 0, corr 0.9986 (v2 was 0.9985 lag 0).
- (b) MOTION: PASS — 4954f decoded, overall mean diff 5.894; longest
  near-dup run 39f at frames 0–39 (0.00–1.62s) = the sanctioned S01 pre-word
  leader freeze (same as v1/v2, pre-word, allowed). Vocal longest near-dup
  runs: S07 14f, S27 9f, S15 3f, S21 2f, S06 2f — all < 24f gate. Vocal
  means: S01 0.470 (known take property, disclosed at QC), S07 0.834,
  S15 0.879, S21 11.411, S27 1.981, S12 5.591 — all ≥ 0.5.
- (c) PLACEMENT (numeric, 10 checks): L15-look 1.90, L15-you 3.48, L12 2.08,
  L82 1.43, L83 1.25, L88 2.94, L110a 1.69, S01 1.63, S15-head 1.90 — all in
  the 1.25–3.48 band (controls 3.0–37.2, wrong take 57–76). L85 first read
  22.45 vs t14 f169 — re-checked f167–172: minimum at f170 = 1.78 (the
  check was 1 frame off; t14 moves fast, adjacent-frame diffs 22–38).
  Placement numerics all PASS on build 1.
- (d) PICTURE (visual, master PNGs work/gate_v3/m_*.png + check2/): L15
  girl singing her line, cat mouth closed, caption + bug present — PASS
  (girl's eyes closed at the "look" frame, open by "from"/"you" — the QC
  nit, disclosed). L82 girl singing, cat quiet — PASS. L83 cat singing,
  girl out of frame — PASS. L86 girl singing, cat mouth closed — PASS.
  L88 girl singing dominant (cat mouth wide open briefly at fragment
  start, small, then closed) — PASS with nit. L84 girl singing dominant
  (cat mouth slightly open, small) — PASS with nit. L89 cat close-up,
  mouth closed at fragment start, opens wide by the end, girl out of
  frame — PASS with nit.
- **FAIL — L85 (CAT "Let the whole thing spin", t14 sf156–182): the girl
  is the dominant singer through the whole 26f fragment — mouth open at
  take 7.0s, 7.5s, 8.0s (contact sheet work/gate_v3/check2/t14_L85window.png).
  The QC window note ("cat visible 6.5–8.5s") was true but incomplete:
  the girl's mouth is open 5.5–7.5s in the same take. Wrong singer under
  a CAT line — the exact defect class v3 exists to fix.**
- **FAIL — L87 (CAT "Same worn-in shoes", t15 sf84–108): same class. The
  girl is large and mouth-open through the whole 24f fragment (take
  3.5s, 4.0s, 4.5s — contact sheet t15_L87window.png); the cat also
  sings at 3.5–4.0s but the girl dominates. QC note ("cat 3.5–4.5s,
  girl singing 5.5–9.5s") missed the girl's open mouth at 3.5–4.5s.**
- CAPTION NIT (v2-carried, .ass byte-identical to v2): bridge karaoke
  highlights trail the song words on L84/L86/L87/L88/L89 by ~0.1–0.7s
  (L88 "Nothing" highlighted at 165.5s vs song 164.58–164.76; L88 caption
  starts 165.20, 0.62s after the line starts; L89 starts 166.30, 0.42s
  late). Caption text is present and correct on every line; only the
  highlight lags. The .ass events for the bridge were keyed to take/v1
  times, not the song grid. Disclosed, not fixed (same file as v2).
- FIX (build 2): L85 → t13 sf82–108 (26f), L87 → t13 sf36–60 (24f).
  Both slices verified by contact sheet BEFORE the re-encode:
  t13 f82/f95/f108 — cat mouth wide open singing, girl only a sliver at
  the top edge (L85cand); t13 f36/f48/f60 — cat mouth opens wide mid-
  fragment, girl's face never in frame (L87cand). All four CAT lines now
  from t13 (L83 12–39, L87 36–60, L89 60–82, L85 82–108); the four lines
  need 99f from t13's 96f cat window, so ONE 3-frame overlap is
  unavoidable: t13 f36–39 appears in both L83 and L87, ~5.3s apart inside
  1.1s montage cuts — imperceptible, disclosed. build_v3_plan.py updated
  (MONTAGE table + comment); gate script updated (L85 → t13 f96, L87 →
  t13 f48 added, L89 → t13 f71 added; 12 placement checks now).
- Build 1 master is SUPERSEDED — same filename, re-encoded as build 2.
  Do not cite build 1's md5 as the v3 master.

## 4. Re-encode (build 2)
- Plan regenerated 2026-11-06 ~03:45 EST (build_v3_plan.py): S21 227f,
  total 4954f, s28_t5/s07_t3/s21_t7 absent, L15 offsets unchanged
  (max +0.113s). S21 now: L82 t12 12–37, L83 t13 12–39, L84 t16 12–39,
  L85 t13 82–108, L86 t11 12–38, L87 t13 36–60, L88 t15 132–164,
  L89 t13 60–82, tail t14 12–30.
- Encode LAUNCHED detached 2026-11-06 ~03:45 EST (setsid nohup, PID 33983),
  log work/assemble_v3.log (rm'd first, so this log is build 2 only).
  Master file growing (1,048,624 B at 08:46 UTC). Log confirms the new
  S21 slices are in effect (L85 t13 82–108, L87 t13 36–60).
- **BUILD 2 ATTEMPT 1 KILLED BY A VM REBOOT 2026-11-06 ~08:56 UTC (~03:56
  EST): process gone, no traceback, output truncated at 102,760,496 B
  (no moov atom). `uptime` after the reboot showed 2 min; the Freeq
  bridge bot.py was already back (PID 2104, systemd/wathdog restarted
  it — not my job). NOT the exec reaper, NOT OOM (3.6 Gi available).
  systemd-run --user is unavailable (no user bus), so no systemd
  launcher for the encode. Post-reboot load 14.7 on 4 cores but %CPU
  shows only the hatch daemon at ~30% — load is runtime-recovery churn,
  not sustained CPU contention; the encode has cores free.
- **BUILD 2 ATTEMPT 2 LAUNCHED 2026-11-06 ~09:01 UTC (PID 3047, setsid
  nohup, same script/settings, log work/assemble_v3.log overwritten).
  Ran SLOW post-reboot (cold cache + heavy I/O wait 25–43% from other
  jobs' disk activity; ffmpeg ~42–48% CPU, file growth 2.4–8.2 MB/min)
  but finished: BUILD OK 2026-11-06 ~09:18 UTC (~17 min). Master:
  md5 177801e37b1cebbeba1fb981db93603a, 119,235,993 B (stable across
  re-stat), 1280x720, 24fps, 4954 frames, 206.416667s, h264 + AAC.
  Build 1's md5 (c6643ffd…) is superseded and must never be cited as v3.
- Gate RE-RUN on build 2 (validate_master_mv5_v3.py, 12 placement
  checks incl. revised L85/L87/L89), launched ~09:19 UTC (PID 9707),
  log work/gate_v3.log (rm'd first). Audio identity already PASS
  (lag 0, corr 0.9986 — same as build 1).
- **BUILD-2 GATE: PASS (2026-11-06 ~04:3x EST).** (a) Audio identity
  lag 0, corr 0.9986. (b) Motion: 4954f decoded, overall mean 5.864;
  longest near-dup 39f at frames 0–39 = sanctioned S01 leader; vocal
  longest runs S07 14f, S27 9f, S15 3f, S21 2f, S06 2f (all < 24f);
  vocal means S01 0.470, S07 0.834, S15 0.879, S21 10.522, S27 1.981,
  S12 5.591. (c) Placement 12/12: L15-look 1.90, L15-you 3.48, L12
  2.08, L82 1.43, L83 1.25, L85 1.65 (t13 f96), L87 1.67 (t13 f48),
  L89 0.77 (t13 f71), L88 2.94, L110a 1.69, S01 1.63, S15-head 1.90
  (controls 3.03–42.98, wrong take 57–79). The nine checks unchanged
  from build 1 returned BIT-IDENTICAL values, confirming the rest of
  the master is unchanged by the re-encode. (d) Picture: build-2
  m_L85/m_L87 PNGs read — L85 cat dominant, mouth wide open singing,
  girl only a sliver at the top edge; L87 cat dominant, mouth wide
  open, girl's face out of frame. Both fixes VERIFIED on the master.
  Build-1 picture verdicts for the unchanged lines stand (identical
  numerics). Full record: work/V3_ASSEMBLY.md §3.
- No delivery flag written, no commit, no IRC announce, no chat
  delivery — parent verifies from disk and delivers.

## 5. BUILD 3 — swing-keyframe per-word rebuild (2026-11-06 ~04:4x EST)

Method change (user, 2026-11-06 ~03:21 + ~03:40 EST): PER-WORD TIME
WARPING via SWING KEYFRAMES supersedes build 2's uniform warps. Build 2's
master (md5 177801e37b1cebbeba1fb981db93603a, gate PASS) is superseded;
build 3 overwrites the same master path. Tooling: work/swing/
(beat_grid.json — 107.67 BPM, three witnesses agree; swing_keyframes.py;
SWING_METHOD.md). 17 fresh dual-Whisper swing runs in work/swing/runs/
plus the tooling agent's s01_t1 / s07_t2 examples.

### Anchor sources (per scene, one system per scene — grids never mixed)
- PAIRS (work/gemini_takes.json — Gemini-app per-word, audit-adjudicated,
  v2 song grid): S04, S05, S06-t1, S07-t1, S08, S09, S11, S12, S15, S19b,
  S20, S23, S25, S17 (whisper-v1 pairs, 8/37 words — refrain blur).
- TOOL (fresh dual-Whisper keyframes): S01 (pairs' intro stamps are the
  noisy set — 'Till' take stamp differs 0.5s between systems; the tool's
  dual decodes are self-consistent and EXAMPLES-validated), S07-t2 (L15).
- MIXED (documented): S06-t2/L12 — song stamps from pairs, take stamps
  from the tool's clean dual decode (Yeah 0.0 / they 0.76 / already 0.98
  / understand 1.44).

### Adjudication of the tool's BAD flags (cross-checked vs pairs)
- BAD-wrong 'Bare→Bear', 'Keys→Kees': Whisper homophone artifacts; pairs
  confirm the words. NOT bad. 'half-zipped': token split. NOT bad.
- Refrain BAD-missing floods (S08 19, S09 27, S17 28, S23 16, S25 9):
  the known dual-system refrain blindness (the model's refrain voice
  does not restart words; neither Whisper nor the app stamps blurred
  repeats). Pairs' matched subsets anchor what is measurable; the rest
  warps by neighbours. No montage shredding of hook blocks on decode
  silence.
- BAD-out-of-caps spanning plan breaks (S04 'laughing'→'Said' across the
  donor-covered gap; S12 L44 across tail/donor structure): dissolve
  under span scoping — intervals are computed WITHIN sung spans only.
- Dual-system-unstampable words (S11 L37 + L40's And/the/tide/tapping;
  S12 L42 + L44 words; S20 L81): unanchored, warp by neighbours inside
  their spans (the audit placed these spans by fit; build-2 picture
  gates passed). Unmeasurable ≠ messed up.
- Knife-edge rule: an interval needing setpts >2.0 whose time deficit
  (song_iv − 2×take_iv) ≤ 0.11s is capped AT 2.0 and disclosed (the
  downstream word lands early by the deficit). Applied 3 times:
  S01 now→easy (playback 0.485, deficit 0.020s), S06-t2 they→already
  (0.44 ± stamp quantization, deficit 0.060s), S11 our→feet (0.500,
  deficit 0.000s).
- NO montage BAD-span cuts were applied: after adjudication, no word in
  a sung span is confirmed wrong/missing/repeated by both systems, and
  no interval misses the caps by more than the knife-edge band. The
  BAD-span machinery stands ready in the tool; the evidence did not
  convict any span. (S21's bridge remains the build's montage section,
  per the original v3 brief.)

### Kept at build-2 warps (documented, not silent)
- S09 groups [0-38] + [38-79]: STRUCTURAL — single-anchor refrain
  groups whose head intervals cannot land legally (deficits ~0.38s on
  an inferred, even-split refrain grid). Flagged, v2 fits kept.
- S17 group [41-124]: its only anchor is a cross-complex misalignment
  in the v1 pairs (the take's next refrain complex stamped against the
  previous line); per-word warping on it would 5.6×-squeeze the head.
- S17 [124-166], [166-233]; S08 [49-104], [156-205]; S23 [35-77];
  S25 [46-144]: no anchors inside the span (refrain blur) — v2 kept.
- S03 (vocalise — no words to anchor), S27 + L110a (grid-contested:
  app stamps land outside the scene / the tool aligned the take's
  other refrain pass; build-2 picture gate verified) — v2 kept.
- Anchor drops (word rides its interval, disclosed in PW_TABLE.md):
  quantization duplicates (S04 'the', S12 'forgot', S20 'breeze',
  S23 'Easy', S05 'Rolling' = span edge), grid-conflict (S15 'replays':
  supplement song stamp 116.32 crosses pairs' 'head' 116.5 — dropped,
  lands ~117.4 by neighbour warp on a held word), END conflicts
  (S04 'in'/'laughing'), head legalization (S19b 'move'/'with' — the
  take compresses "We still move with it" into ~0.3s; 'move' lands
  ~152.93 vs stamp ~152.9 by the legalized head warp), tail
  legalization (S23 'to'), outlier (S07 L16 'replays' pairs stamp
  ~56.0 vs tool 54.36 — dropped; lands ~54.15 by neighbour warp).
- S17 group [0-41] reworked (1 anchor, sane intervals); S17 [41-124]
  kept (see above) — the earlier +0.12s tail extension was on the
  skipped group and no longer applies.

### Result
23 sung groups reworked into per-word sub-pieces; full interval table
in work/swing/PW_TABLE.md (every word: take span, song span, playback,
setpts, out frames, caps marked). Plan: work/assembly_fit_mv5_v3pw.json,
total 4954 frames (asserted). Extreme speedups disclosed in the table
(hardest: S15 'whole' interval 8.0× over 2 frames — a stamp-quantization
micro-interval; S08 'Easy' 6.0× over 3f; S20 head 5.0× over 7f; S23
g3 head 2.02× over 33f — the take's refrain wind-up squeezed to the
confirmed L96 line).

## 6. BUILD 3 GATE — PASS (2026-11-06 ~05:1x EST)

Master: masters/mv5_easy_now_easy_now_16x9_v3.mp4 (overwrites build 2)
  md5 e13f17fc3a1e130ff1bfcd865a0c0ed1 · 120,494,768 bytes ·
  1280x720, 24fps, 4954 frames (counted), 206.416667s, h264+AAC 48k.
Gate script: validate_master_mv5_v3pw.py (log work/gate_v3pw.log,
  PNGs + JSON in work/gate_v3pw/). Frame extraction uses an input-seek
  fast path; the unchanged montage checks reproduce build 2's numbers
  bit-for-bit (L82 1.43, L83 1.25, L85 1.65, L87 1.67, L89 0.77,
  L88 2.94, L110a 1.69), cross-validating the faster extractor.
(a) AUDIO IDENTITY: lag 0 samples, correlation 0.9986 — PASS.
(b) MOTION: 4954 frames decoded; overall mean diff 6.003; longest
  near-dup run 39f at frames 0–39 = the sanctioned S01 freeze-leader
  (pre-word, unchanged). Vocal windows: S07 longest run 18f (< 24f
  gate; in the slowed held-'replays' tail), S15 vocal_mean 0.755 /
  longest 4f, S27 9f, S21 2f, S12 1f, S04 1f — no frozen run during
  words in any vocal scene — PASS.
(c) PLACEMENT: 27/27 checks PASS — every mean|diff| far below its
  ±12-frame control and the wrong-take reference (57–85). The 7
  carried montage/L110a checks are identical to build 2. The 20 new
  word-onset checks (master frame at each song word onset vs the
  take frame at its anchored take time): range 0.76–5.00; L15 'look'
  1.80 and 'you' 1.87 (build 2's uniform warp measured 'you' at
  3.48 — per-word warping measurably improved the mandated line);
  tightest margin W-S07-down 3.52 vs control 6.31 (fast head
  interval, still clearly the right frame); W-S12-bills 5.00 vs
  control 25.27.
(d) PICTURE / MOUTH STATE at onsets (steer point 4): PNGs read —
  L15 'look' girl mouth wide open; L12 'they' girl mouth open,
  caption highlight exact; S15 'head' girl mouth wide open; S19b
  'Hand' cat mouth open mid-vocalization, girl closed (correct —
  cat's passage); S01 'Till' + L15 'you' land on mouth-transition
  frames that match their source take frames numerically (1.28 /
  1.87) — the warp introduces NO additional mouth lag; the
  transition is intrinsic to the takes' own onset frames. No
  consistent lag measured in any reworked scene → no keyframe
  shift applied. Captions + ~ WuBu ~ bug present on sampled frames;
  two onset-boundary frames (8.18s, 153.83s) fall in ≤0.3s
  inter-event gaps of the v2-keyed .ass (byte-identical captions —
  carried nit, not a regression).

DISCLOSURES (build 3, complete): per-word swing warping applied to
23 sung groups (table: work/swing/PW_TABLE.md); 3 intervals capped
at exactly setpts 2.0 with disclosed deficits 0.020/0.060/0.000s;
no BAD-span montage cuts (no span convicted by both measurement
systems — §5); kept-v2 groups: S09 R1/R2 groups STRUCTURAL, S17
[41-124] misaligned anchor, anchor-less refrain groups, S03
vocalise, S27/L110a grid-contested; dropped anchors ride their
intervals (listed in §5 + PW_TABLE); extreme speedups disclosed in
the table (max S15 'whole' 8.0× over 2f — stamp-quantization
micro-interval). Build-2 disclosures not affected by the rework
(bridge karaoke highlight trail ~0.1–0.7s on L84–L89, L84/L85/L88
competing-mouth nits, L89 closed-at-start, L15 eyes/pigtails nits,
L110b structural cover) carry over unchanged.
No delivery flag, no commit, no IRC announce — parent verifies
from disk and delivers.
