# MV-5 v3 assembly — "Easy now, easy now (THE VOICE)"

Master: `masters/mv5_easy_now_easy_now_16x9_v3.mp4`
- **BUILD 3 (current, swing-keyframe per-word rebuild, gate PASS)** —
  md5 `e13f17fc3a1e130ff1bfcd865a0c0ed1`, 120,494,768 B
- 1280x720, 24fps, 4954 frames, 206.416667s, h264 + AAC 48kHz stereo
- track.mp3 (md5 `0c1bcafa568547e2d4fa36e133ad3626`) sole master audio
- captions: `captions_16x9_v3.ass` (byte-identical to v2, 437 events)
- `~ WuBu ~` bug on all frames; ONE 16:9 only, no 9:16, no chat copy

Build 3 supersedes build 2 (md5 `177801e37b1cebbeba1fb981db93603a`,
uniform warps, gate PASS) after the user's 2026-11-06 swing-keyframe
method order: 23 sung groups rebuilt with per-word time warping from
measured swing keyframes, 3 intervals capped at exactly 2.0× slow
with disclosed deficits, no BAD-span montage cuts (no span convicted
by both measurement systems). Method, adjudications, the full
per-word table and the build-3 gate are in
`work/V3_ASSEMBLY_NOTES.md` §§5–6, `work/swing/PW_TABLE.md` and
`work/gate_v3pw/`. Build 1 (md5 `c6643ffdbd2ebfff598f0b224dbc650e`)
was superseded after its gate found two wrong-singer bridge fragments;
see §3 for the build-1 failure and the fix. Do not cite build 1 or
build 2 md5s for the current master.

## 1. Why v3 exists

User playback verdict on v2 (2026-11-06 ~02:33 EST, outranks all gates):
hard jump cuts are jarring, worst in the beginning; the girl's singing is
missing in the beginning because the cat sings her part; fast cutting works
for beat-matched montage, NOT for lyrical portions; the rap bridge gets
montaged from 6 montage clips. Standing edit rules from that verdict (in
Slopcannon SKILL.md): lyrical portions cut SUSTAINED, one continuous picture
per singer-passage, cuts only on singer/scene change; fast cutting only for
beat-matched montage; a sung line gets a SUNG picture — never another
character's mouth, never a closed-mouth cover under a sung line.

## 2. Changes vs v2 (all other 27 scenes copy v2 verbatim; 4954f total)

- **L15 "One small look from you" (51.46–52.80, GIRL per ear + app spk:1):**
  s07_t2 (md5 `39ba0cf638d31f165accd2101ef487e8`) at a DISCLOSED out-of-band
  uniform 1.91x warp (time scale 0.5234375). L15 is structural for per-line
  generation (volley 15: t2 and t3 both REJECT PACING, pace floor
  ~2.2–2.6s/line; no in-band placement exists) and a closed-mouth cover
  under this sung line is banned by the user's law. Measured word-start
  offsets (take starts × 0.5234375 vs song starts, computed independently
  from `work/qc_v15/qc_v15_results.json` + the aligned song grid): One
  0.000, small −0.006, look +0.113, from +0.096, you +0.027. Max |offset|
  +0.113s, median 0.027s — inside the ±0.50s working band. S07 t1 keeps
  L13/L14/L16 (CAT). s07_t3 unused. S06/S07 passage cuts fall on singer
  changes only (s06_t1 L10/L11 CAT, s06_t2 L12 GIRL, s07_t1 L13/L14/L16
  CAT, s07_t2 L15 GIRL).
- **Bridge S21 L82–L89 (158.06–167.5, alternating GIRL-first per the ear):**
  montage from volley-14 clips, warp 1.0, cuts on the v2 line boundaries:
  L82 GIRL t12 12–37 · L83 CAT t13 12–39 · L84 GIRL t16 12–39 ·
  L85 CAT t13 82–108 · L86 GIRL t11 12–38 · L87 CAT t13 36–60 ·
  L88 GIRL t15 132–164 · L89 CAT t13 60–82 · tail t14 12–30.
  s21_t7 NOT used. No bridge line uses a per-line sung take.
  All four CAT lines come from t13 (strongest cat-singing close-up);
  the four lines need 99f from t13's 96f cat window (12–108), so ONE
  3-frame overlap is unavoidable and disclosed: t13 f36–39 appears in
  both L83 and L87, ~5.3s apart inside 1.1s montage cuts.
- **L110b** keeps the v2 structural cover (s28_t3 tail + captions).
  s28_t5 (md5 `b347c9faf46a1fd51902152cd048b28e`) DISCARDED — no QC row,
  no verdict, never in any cut. s07_t3 and s21_t7 also unused.
- Plan: `build_v3_plan.py` → `work/assembly_fit_mv5_v3.json`
  (asserts all 7 new-take md5s, per-scene totals, 4954f total, and that
  s28_t5 / s07_t3 / s21_t7 are absent). Encode: `assemble_mv5_v3.py`
  (asserts track md5 + banned takes absent + 4954f total).
  Incremental notes: `work/V3_ASSEMBLY_NOTES.md`.

## 3. Gate (on the master itself — `validate_master_mv5_v3.py`)

Evidence: `work/gate_v3/gate_v3_results.json`, log `work/gate_v3.log`,
master-frame PNGs `work/gate_v3/m_*.png`, extra frame checks
`work/gate_v3/check2/`. No dictation run (v1/v2 lesson: master-audio
dictation measures Whisper recall on this repeat-heavy song, not
picture sync).

### Build 1 — FAIL (gate 2026-11-06 ~03:21–03:33 EST)
- (a) Audio identity PASS: lag 0, corr 0.9986.
- (b) Motion PASS: 4954f, overall mean 5.894; longest near-dup 39f at
  frames 0–39 (sanctioned S01 pre-word leader freeze, same as v1/v2);
  vocal longest runs ≤14f (S07), vocal means ≥0.470.
- (c) Placement 10/10 numeric PASS (1.25–3.48; L85 first read 22.45 was
  a 1-frame check error — re-check f167–172 found the minimum at f170
  = 1.78; t14 moves fast).
- (d) Picture FAIL on two bridge fragments: **L85** (t14 156–182) showed
  the GIRL visibly singing through the whole fragment (mouth open at
  take 7.0/7.5/8.0s) under a CAT line; **L87** (t15 84–108) showed the
  girl large and mouth-open through the whole fragment under a CAT line.
  The QC window notes ("cat visible 6.5–8.5s" / "cat 3.5–4.5s") were
  true but incomplete — they missed the girl's open mouth in the same
  windows. Wrong singer under CAT lines: the exact defect class v3
  exists to fix. All other picture checks passed (L15 girl singing,
  L82/L83/L86 clean, L84/L88 pass-with-nit, L89 pass-with-nit).
- Fix: L85 → t13 82–108, L87 → t13 36–60. Both slices verified by
  contact sheet BEFORE the re-encode (cat mouth wide open singing;
  girl only a sliver at the top edge in L85, face out of frame in L87).
  Plan + gate script updated; build 2 re-encoded.

### Build 2 — GATE PASS (gate 2026-11-06 ~04:3x EST)
- (a) Audio identity PASS: lag 0, corr **0.9986** (v2 was 0.9985).
- (b) Motion PASS: 4954f decoded, overall mean diff **5.864**; longest
  near-dup run 39f at frames 0–39 (0.00–1.62s, the sanctioned S01
  pre-word leader freeze). Per-scene vocal windows: S01 vocal_mean
  0.470 / longest 6f · S05 1.261 / 2f · S06 1.049 / 2f · S07 0.834 /
  14f · S12 5.591 / 0f · S15 0.879 / 3f · S21 10.522 / 2f · S27 1.981 /
  9f. No frozen run during words (max vocal near-dup 14f < 24f gate);
  all vocal means ≥ 0.5 except S01's 0.470 (known take property,
  disclosed at QC).
- (c) Placement 12/12 PASS (160x90 gray mean|diff|; controls ±12f and
  wrong take in brackets): L15-look 1.90 [11.54 / 63.07] · L15-you 3.48
  [8.10 / 63.03] · L12 2.08 [13.25 / 57.25] · L82 1.43 [29.05 / 70.14] ·
  L83 1.25 [37.15 / 75.65] · L85 1.65 [42.98 / 68.06] · L87 1.67 [40.68 /
  69.21] · L89 0.77 [42.56 / 79.32] · L88 2.94 [29.69 / 72.13] · L110a
  1.69 [3.92 / 59.24] · S01 1.63 [3.03 / 76.14] · S15-head 1.90 [9.70 /
  64.97]. The nine checks unchanged from build 1 returned bit-identical
  values, confirming the rest of the master is unchanged.
- (d) Picture PASS: build-2 master PNGs read for the two fixed
  fragments — L85: cat dominant, mouth wide open singing, girl only a
  sliver at the top edge; L87: cat dominant, mouth wide open, girl's
  face out of frame. Captions + `~ WuBu ~` bug present on all sampled
  frames. Build-1 picture verdicts for the unchanged lines stand.

### Build-2 encode history (disclosed)
- Attempt 1 (PID 33983, ~03:45 EST) killed by a VM REBOOT ~08:56 UTC
  (~03:56 EST): no traceback, output truncated at 102,760,496 B.
  The Freeq bridge was already back after the reboot (systemd/watchdog).
  systemd-run --user is unavailable (no user bus), so no systemd
  launcher for the encode.
- Attempt 2 (PID 3047, ~09:01 UTC) ran slow post-reboot (cold cache +
  25–43% I/O wait from other jobs' disk activity; ffmpeg ~42–48% CPU)
  but finished: BUILD OK ~09:18 UTC (~17 min). Same script and settings.

## 4. Disclosures / carried nits
- L15 out-of-band 1.91x warp (parent decision, §2): measured word
  offsets max +0.113s (look), median 0.027s. Girl's eyes closed at the
  "look" frame, open by "from"/"you" (QC nit); pigtails variant.
- Bridge montage: one 3-frame overlap (t13 f36–39 in both L83 and L87).
  L84: cat's mouth slightly open, small, while the girl sings (nit).
  L88: cat's mouth wide open briefly at fragment start, small, then
  closed; girl dominant throughout (nit). L89: cat's mouth closed at
  fragment start, opens wide by the end (nit). L85: girl's mouth
  visible as a sliver at the top edge (nit).
- Captions (v2-carried, .ass byte-identical to v2): bridge karaoke
  highlights trail the song words on L84/L86/L87/L88/L89 by ~0.1–0.7s
  (L88 "Nothing" highlighted at 165.5s vs song 164.58–164.76; L88
  caption starts 165.20, 0.62s after the line starts; L89 starts
  166.30, 0.42s late). Caption text is present and correct on every
  line; only the highlight lags. The .ass bridge events were keyed to
  take/v1 times, not the song grid.
- Carried from v2 (plan-level, unchanged): weakest fit medians S15
  0.897s / S20 0.732s / S21 0.724s; S27 L109 +0.98/+1.48s vs app times
  (v1 line-span placement); S01 vocal_mean 0.470 (known take property).
- L110b keeps the v2 structural cover. s28_t5 discarded, never in any cut.

## 5. Delivery status
- NOT delivered. No MV5_V3_DELIVERED.flag written, no commit, no IRC
  announce, no chat delivery — the parent verifies from disk and
  delivers. Never re-deliver v1 or v2.
