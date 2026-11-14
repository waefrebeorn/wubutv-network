# MV-5 v2 assembly — work/V2_ASSEMBLY.md

Date: 2026-11-06. Assembler: re-fire agent (previous assembly agent 8d9a1d24 died
01:23 EST on `model error: model response truncated: output token cap reached`,
having written nothing — no master, no V2_ASSEMBLY.md, no intermediates).
This file is written INCREMENTALLY as stages complete so a truncated reply
cannot lose the work.

## Sources (the plan — read, not re-decided)
- `work/gemini_takes_verdicts.md` + `work/gemini_takes.json` — audit re-time plan
  (per-line/per-word take→song placements; single linear warp only where
  residuals small; app word STARTS, line spans from v1; captions on song times).
- `work/LYRIC_TIMELINE_V2.md` + `work/gemini_song_words_aligned.json` — v2 song grid.
- `work/qc_v12/qc_v12_verdicts.md` — S06 t2 KEEP (L12), S21 t7 KEEP grey-rescue (L88).
- `work/qc_v13/qc_v13_verdicts.md` — L82/L84/L86 STRUCTURAL (two denied attempts
  each); binding correction: s21_t3's CAT picture must NEVER cover a girl line.
- v1 assembly as template: `assemble_mv5.py` + `work/assembly_fit_mv5.json`
  (scene bounds partition 0–206.40s, 4954 frames @24fps) + `CUTLIST.md` (donor ledger).
- Track: `track.mp3` md5 `0c1bcafa568547e2d4fa36e133ad3626` — sole master audio.

## Slot map (binding)
- KEEP (21 v1): S01 t1, S02 t1, S03 t1, S04 t1, S05 t1, S06 t1, S07 t1, S08 t2,
  S09 t1, S10 t1, S11 t4, S12 t1, S15 t1, S17 t1, S18 t1, S19b t1, S20 t1,
  S23 t1, S25 t1, S26 t1, S27 t1. Ship as-is @1.0x: S02, S10, S18.
- Volley-12 KEEPs: S06 t2 for L12 ONLY; S21 t7 for L88 ONLY (grey rescue,
  v1-grid starts, slope 0.89, "to" +0.27s disclosed; master gate re-checks L88).
- STRUCTURAL (closed-mouth reaction/listening picture + captions on song times,
  "not a mouth-sung slot"): S13, S14, S16, S19a, S22, S24, S28 (t3 tail) +
  L82/L84/L86 + L15 + L87/L89 (donor cover). CAT bridge L83/L85 keep s21_t3.
- S27 L110a reuses s28_t1's CAT "Till" (take 0.1–3.1 → song ~201.0–203.4,
  warp ~0.80; 201.0 onset verified in §3).
- Structural scenes keep v1's cover montages (S13/S14/S16/S19a/S22/S24);
  only the captions change (v2 grid) and the bridge/L15/L26/L27/L28 re-cuts
  below are new.

## §1 — v2 plan (work/assembly_fit_mv5_v2.json)

### §1a — Captions (captions_16x9_v2.ass) — DONE
- Built by `make_captions_mv5_v2.py` from `work/gemini_song_words_aligned.json`
  (app starts where matched, v1 times where dropped) + v2 line table.
- 437 events (v1: 453). Every line has ≥1 event; no line uncovered.
- Changed lines verified on disk: L49 karaoke 'Here for the boardwalks'
  (107.8–108.72); L51 block 'You took my sneakers from me once'
  (109.74–110.70 — 'You'/'took' share 109.9, zero duration); L52 karaoke
  'Like none of it was last'; L56 karaoke with held 'replays' 119.5–120.02
  ('head' highlight spans 116.5–119.5 — held-note artifact, disclosed);
  L108 block 'This is now' x3 (194.1–197.58); L109 block (197.58–201.0,
  clamped at L110a); L110a block (201.0–203.42); L110b karaoke (204.2–205.58).
- L107 dropped — no caption event in 187–194.1 (silence gap).
- Note: several lines downgraded karaoke→block vs v1 (L01, L43, L47, L48,
  L82/L83/L85, L93, L97, L99, L103) because the app's burst-compressed
  0.1s times share starts / collapse durations; the caption still shows
  the full line text over its span (v1 script's own rule, mechanical).
  6 events dropped as zero-length by the clamp (same class as v1).

### §1b — Take durations (ffprobe)
- All `takes/mv5_s*.mp4` probed (duration + frame count, session
  proc_30e00be64ca5, 67 files). Key durations: s06_t2 5.0s/120f,
  s07_t1 10.0s/240f, s15_t1 5.0s/120f, s20_t1 5.0s/120f, s21_t3 10.0s/240f,
  s21_t7/t8/t9/t10 5.0s/120f, s26_t1 8.0s/192f, s27_t1 6.0s/144f,
  s28_t1 5.0s/120f, s28_t3 5.0s/120f, s28_t4 3.0s/72f.

### §1c — v2 plan (work/assembly_fit_mv5_v2.json, built by build_v2_plan.py)
- Total 4954 frames (same as v1); 9 scenes changed, 20 copy v1 verbatim.
  Changed: S05, S06, S07, S12, S15, S21, S26, S27, S28.
  Unchanged: S01, S02, S03, S04, S08, S09, S10, S11, S13, S14, S16, S17,
  S18, S19a, S19b, S20, S22, S23, S24, S25.
- Method per line piece: least-squares fit of take word STARTS -> song word
  STARTS (app times, v2 grid); warp = fit slope; sf/ef from the take word
  span; dst0 = intercept + slope*(sf/24); out = round((ef-sf)*warp).
  Fillers (1.0x, same take's inter-line frames or established donor tails)
  tile each scene to its v1 frame total. Final piece starts are within
  1 frame (0.04s) of their fit dst0, except S21 L88 (-0.06s, see below).
- Pre-existing v1 quirk (unchanged, harmless — ffmpeg clamps): S14's
  s19b_t1 piece has ef=121 on a 120-frame take; the assembler's tpad slack
  covers it (v1 built fine with it).
- Grey warps (outside 0.80-1.25, inside 0.60-1.60, all disclosed):
  S06 L11 0.621 (scene fit — per-line fit 0.584 was illegal, so the scene
  slope is used, first-word-anchored); S07 L13 0.725, L16 1.265;
  S12 L41/L43 0.67 (scene fit — L43's per-line fit 0.40 was illegal);
  S21 L83 0.79, L85 0.605 (brief ratios); S17 R2/R3 0.714/0.651 (v1, kept).

#### Changed scenes (piece tables — full table in the fit JSON)
- S05 (215f): per-line app fits. L06 s05_t1 2-53 w0.920; L07 72-120 w1.018;
  L08 125-161 w1.009; L09 170-209 w0.934 (scene fit — 1 matched word;
  includes split "half-zipped." 8.0-8.7s). Head freeze-leader 12f (frame 0);
  gaps/donors (s09_t1 tail) fill the inter-line breath.
- S06 (175f): L10 s06_t1 2-55 w0.821; L11 s06_t1 82-137 w0.621 (scene fit,
  first-word-anchored); L12 s06_t2 0-62 w0.88 (qc_v12; "they" +0.35s
  disclosed, actual +0.38s after the 1f tiling shift); tail s06_t2 62-82.
  Head freeze-leader 17f (frame 0).
- S07 (234f): L13 s07_t1 2-68 w0.725 (trimmed: "time" cut 0.17s early);
  L14 74-122 w0.848 (trimmed: "fade" cut 0.12s early); L15 DONOR COVER
  s08_t2 205-237 (32f, closed mouth — NOT s07_t1's CAT mouth); L16 s07_t1
  180-240 w1.265 (grey; "head" +0.51s is the fit's own outlier, resid_max
  0.75 for this scene).
- S12 (207f): L41 s12_t1 2-58 w0.67; L43 101-180 w0.67 (scene fit both);
  L42/L44 donor cover (gap + tail: s12_t1 180-216, s16_t1 212-240,
  s10_t1 219-237). Head freeze-leader 6f.
- S15 (127f): TWO ANCHORS. Head s15_t1 7-60 w1.0, dst 116.21-118.42
  (And@116.2 anchored; my +0.20, whole +0.50, head +1.20 — the held-note
  spread, disclosed); held tail s15_t1 60-103 w1.0, dst 118.42-120.21
  (the held "replays" covers 119.5; the -1.10s in the placement table is
  the piece-start offset, not a word miss — the note spans the piece);
  donor-tail s21_t3 198-224 (26f).
- S21 (227f): L82 cover s21_t8 tail 84-109 (25f, post-line, mouth closed);
  L83 s21_t3 48-82 w0.79 (grey); L84 cover s21_t9 tail 84-111 (27f,
  post-"up", mouth slightly open at 4.0s — resting, disclosed);
  L85 s21_t3 120-163 w0.605 (grey); L86 cover s21_t10 67-80 (quiet gap
  2.79-3.33s) + 95-108 (post-repeat tail); L87 donor s21_t1 194-218;
  L88 s21_t7 0-36 w0.89, dst 164.52-165.85 (v1-grid placement per qc_v12;
  vs v1 grid: Nothing -0.10, to +0.17, prove -0.10; vs app grid -0.72/
  -0.57/-0.32 — the grids disagree ~0.6s on this line, which is why the
  gate re-checks L88; if it fails, L88 falls back to donor cover);
  L89 donor s21_t1 218-240 + s21_t3 186-201.
- S26 (172f): head donor s16_t4 217-240 + s16_t5 175-191 + s20_t1 68-117
  (88f); L108 window: s26_t1 tail 144-192 (48f, mouth closed @6.0s
  verified — the sung 0.4-4.1s portion is NOT used) + s04_t1 204-240.
- S27 (140f): L109 s27_t1 86-118 w1.0, dst 197.58-198.91 (scene head per
  the brief; vs the app's 196.6/196.7 song times the words land +0.98/
  +1.48s — the app hears the refrain in S26's tail gap, the v1 line span
  starts at 197.58; disclosed); tail s27_t1 118-143 + donor s16_t3
  202-227; L110a s28_t1 2-74 w0.80, dst 201.00-203.41 (Till onset 201.0
  verified; "the" +0.30, "morning" +0.46, "comes" +1.30 vs the app's
  burst-compressed 201.0-201.3 times — the caption is a block over the
  line span, so no word is highlighted late; disclosed).
- S28 (72f): structural. s28_t3 closed-mouth tail 72-120 (48f) +
  s28_t1 tail 96-120 (24f, post-"Till", mouth closed). No singing picture.

#### Word placement (placed onset minus song start, seconds; app grid)
- S05: L06 <=0.03, L07 <=0.11, L08 <=0.07, L09 Backpack -0.34.
- S06: L10 <=0.11, L11 <=0.08, L12 Yeah -0.22 / they +0.35 /
  already +0.04 / understand +0.05.
- S07: L13 <=0.11, L14 <=0.03, L16 And -0.15 / my 0.00 / whole +0.05 /
  head +0.51 / replays -0.41.
- S12: L41 <=0.17, L43 -0.39..+0.25 (scene fit; v1's L43 tail was +1.12).
- S15: see two-anchor note above. S21: L83 -0.30..+0.29, L85 -0.24..-0.09
  (both vs the app's burst-compressed starts; the line-span placement is
  the intended one). S27: see L109/L110a notes above.
- No illegal placements (GAPS: none). All warps in [0.60, 1.60].

## §2 — assembly (assemble_mv5_v2.py)

## §3 — master gate (parent verification, 2026-11-06 ~02:17 EST)

Note: the re-fire assembly agent (8ffc157e) errored on transport
(`sqlx error: pool timed out while waiting for an open connection`) after
launching the detached encode; its §2/§3 notes were never written. The
master below was recovered from disk and gated by the parent instead.
No re-fire: the artifact is complete and the gate passes.

- Master: `masters/mv5_easy_now_easy_now_16x9_v2.mp4`
  md5 `1c252e69032ab028c5e9a72ce974ea46`, 115,578,719 B,
  1280x720, 24fps, 4954 frames, 206.417s (video) / 206.400s (audio).
  Size stable across a 5s re-stat; mtime 2026-11-06 02:12:36 EST.
- Audio identity: master audio vs `track.mp3`, 16kHz mono —
  correlation at lag 0 = 0.9985 (gate >= 0.99), identical length
  3,302,400 samples. PASS (md5s differ only by AAC re-encode).
- Placement (master frame vs planned take frame, mean |diff| 0-255):
  L88 1.47, L82 2.54, L110a 2.47, L12 3.23, S01 2.47, S15 2.81.
  Controls: same take +/-12 frames 11.3-11.8; wrong take 69.2.
  6/6 placements match the fit plan. PASS.
- L88 re-check (gate item): frame 165.5s — GIRL singing, mouth open,
  CAT in basket mouth closed; caption "Nothing to prove" karaoke on
  song times (Nothing highlighted at 165.5s). PASS — no donor fallback
  needed.
- L12: frame 45.5s — GIRL singing "Yeah, they already understand",
  karaoke highlight on "already", CAT mouth closed. PASS.
- L110a: frame 202.0s — CAT close-up singing "Till the morning comes",
  caption block on song times. PASS.
- `~ WuBu ~` bug present in every sampled frame; captions burned
  (437 events, karaoke + block). PASS.
- Motion: consecutive-frame mean |diff| 8.1-9.3 across L88
  (164.6-165.6s) and 6.5-7.8 across the S15 held note (117-118s).
  Moving, not frozen. PASS.
- Carried disclosures (plan-level, §1c — the master faithfully
  implements the plan, these are not new findings): weakest fit
  medians S15 0.897s / S20 0.732s / S21 0.724s; S12 L43 tail up to
  +1.27s vs the app grid; S27 L109 +0.98/+1.48s vs app times
  (v1 line-span placement); L110a "comes" +1.30 vs app's
  burst-compressed times (block caption, no word highlighted late);
  grey warps as listed in §1c. The user's playback verdict outranks
  this gate, as always.

VERDICT: GATE PASS. Master delivered as MV-5 v2.
