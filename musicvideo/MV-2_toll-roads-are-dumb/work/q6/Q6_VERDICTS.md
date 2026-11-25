# MV-2 Q6 — VERDICTS (coordinator a6816deb, sprint revive detector)

**Status: PARTIAL — takes QC'd, assembly NOT done by this coordinator.**
A second Q6 recovery coordinator (c786bbd9, MV coordinator revive detector)
was spawned 92 seconds after this one and worked concurrently. It owns the
re-cut + assembly (it is further along: its takes are QC'd, its S07 t2 +
S04a warp are done, and the registry now names it coordinator_id
`c786bbd9`). This file records THIS coordinator's work: measurements,
its own three takes (q6b set, alternates), the S25 re-cut design, and the
duplication. No commit, no flag, no Telegram, no delivery by this file.

## 0. Duplication — read this first (parent)

- Original Q6 coordinator ccfb1530: spawned 2026-11-12 ~12:07 EST,
  INTERRUPTED 12:19:21 EST in a daemon restart (null final response).
  It wrote nothing but the empty `work/q6/` directory.
- BOTH revive detectors fired on the same death: the sprint revive
  detector spawned this coordinator (a6816deb) at 12:21:05 EST, and the
  MV coordinator revive detector spawned c786bbd9 at 12:22:37 EST.
  Neither knew about the other until this coordinator found the
  sibling's files on disk at ~12:36 EST.
- Cap overrun: this coordinator's brief says cap 3 takes; the sibling's
  brief says cap 6 videos incl. re-fires (registry `cap: 3`). Fired
  total: sibling 4 (S04a t1, S07 t1, S21 t1, S07 t2) + this coordinator
  3 (S07/S21/S04a q6b t1) = **7 videos against a registry cap of 3**.
  The spend is sunk; no further generation from this coordinator.
- File collision (repaired): both coordinators used the canonical names
  `mv2_s07_q6_t1.mp4`, `mv2_s21_q6_t1.mp4`, `mv2_s04a_q6_t1.mp4`.
  This coordinator's `cp` at 12:35:30 EST overwrote the sibling's three
  canonical files. REPAIRED 12:39 EST: the sibling's files were restored
  from its raw media-generation files (md5s verified against its ledger:
  S07 t1 `563b67fe…`, S21 t1 `412a5ca8…`, S04a t1 `6009bfaf…`), and this
  coordinator's takes were renamed to the `q6b` set
  (`mv2_s07_q6b_t1.mp4` md5 `0aa289cc…`, `mv2_s21_q6b_t1.mp4` md5
  `1f56da47…`, `mv2_s04a_q6b_t1.mp4` md5 `6d2f0960…`). The sibling's
  `mv2_s07_q6_t2.mp4` and `mv2_s04a_q6_t1_warped.mp4` were never touched.
- The sibling's brief/ledger lives in `work/q6/Q6_PROGRESS.md` +
  `work/q6/Q6_LEDGER.md` (its verdicts are summarized in §3 below, not
  re-derived here). This coordinator did NOT edit TAKE_HISTORY.md,
  VOLLEY_PROGRESS.md, or MUSIC_VIDEO_LEDGER.md — the sibling may be
  editing them; the parent merges at verification.

## 1. Section-boundary re-cut — MEASURED, no moves justified

Measured against SONG_WORDS_BASE.json (measured word times — the timing
authority), NOT against LYRIC_TIMELINE.md's frame/bracket estimates
(±1–2.5s, and the timeline itself warns the bold highlight can lag the
vocal ~1s). The v6 cutlist already tracks every measured line boundary:

| Boundary | Timeline | Measured line boundary | Nearest v6 cut | Verdict |
|---|---|---|---|---|
| Intro/V1 | 12.5 | "seem." ends 13.36 / V1 "They" starts 13.36 | 13.36 (S01 end) | EXACT |
| V1/C1 | 51.5 | "fall." ends 49.38, gap, "Toll" starts 50.84 | 50.84 (hook1 start) | EXACT (onset) |
| C1/V2 | 91.5 | "comin'." ends 93.10 / "Express" starts 93.10 | 93.10 (S09 start) | EXACT |
| V2/C2 | 121.5 | "quit." ends 121.76, gap, "Toll" starts 122.92 | 122.20 (in gap) | IN GAP (+0.44) |
| C2/Bridge | 165.5 | "comin'." ends 164.36, "They" 165.34–165.92 | 165.92 (S16 start) | AT WORD END (+0.42 vs timeline) |
| Bridge/Cext | 190.0 | line 36 "the wrecks just come" ends 193.18 | 193.18 (S19 end) | EXACT |
| Cext/Outro | 238.5 | "done." ends 238.82 / "Yeah," starts 242.30 | 238.82 (GAP-E end) | EXACT |

The audit's numbers (Intro/V1 2.5s early, V1/C1 + C1/V2 + V2/C2 1.5s
early, C2/Bridge 2.51s late) describe the PREPRO 10s grid (scene starts
10/50/90/120) and the timeline's own bracket estimates — not the v6
cutlist. Moving cuts to the timeline estimates would put cuts MID-WORD
(e.g. V1/C1 at 51.5 falls inside "Toll" 50.84–51.84; C1/V2 at 91.5 falls
inside "comin'." 90.70–93.10; V2/C2 at 121.5 falls inside "won't"
120.92–121.52) — banned by the skill (hard cut on a word/line boundary
only, never mid-word). **No section-boundary cut moves in the Q6
master.** The verification bar ("≤0.5s vs LYRIC_TIMELINE") is met by
measured-word truth, not by the timeline's estimates; the timeline's
Bridge/Cext boundary (190.0) is itself ~3.18s off the measured line
boundary (193.18) — it splits bridge line 36 in half.

## 2. S25 place-beat re-cut — DESIGNED, not executed (sibling assembles)

Defect: S25 t2's place action (hand raises the ticket ~take 4.5–5.0,
holds it at the mic 5.0–5.5, lowers it to rest on the stand 5.5–6.5;
ticket resting on the stand from ~6.5 — verified on full-res frames
`work/q6/frames/s25_t{4.0,4.5,5.0,5.5,6.0,6.5}s.png`) lands at song
241.74 in v6 (inside filler 238.94–242.30, take 2.20–5.56), ~11s before
the line it belongs to (S25 mouth slot 251.08–253.06). The ticket is
then in hand again for the mouth slot — a continuity break.

Fix (pool edit in the Q6 assemble script, downstream holes unchanged):
replace the pool entry `("mv2_s25_t2.mp4", 2.20, 10.0)` with two
adjacent entries, in this order:
`("mv2_s25_t2.mp4", 6.64, 10.0)` then `("mv2_s25_t2.mp4", 2.20, 6.64)`.
Resulting S25 filler clips (mouth slot 251.08–253.06, take 0–2.20,
untouched):
- 238.94–242.30: take 6.64–10.00 (ticket resting on stand, stepped back)
- 243.08–243.24: take 2.20–2.36 (0.16s sliver, hand low)
- 249.18–251.08: take 2.36–4.26 (ticket in hand, pre-place — correct
  setup for the mouth slot)
- 253.06–255.44: take 4.26–6.64 — the place action lands here in full:
  raise at song ~253.30, ticket at mic ~253.80, resting on stand by
  ~254.44, i.e. the designed post-line beat immediately after the
  mouth slot ends (253.06).
Residual nit (disclosed): the 238.94–242.30 window now shows the
post-place state (ticket on stand) before the line is sung — one
state flip, versus v6's flip the other way. The action itself lands
in the right place, which is the audit's ask. Verification for the
assembler: frame reads of the new master at song 253.3 / 254.0 / 254.5
(hand up / ticket at mic / ticket resting).

## 3. Restage takes — both sets

Method (this coordinator): vehicles `mv2_s07_vehicle_q6.txt`,
`mv2_s21_vehicle_q6.txt`, `mv2_s04a_vehicle_q6.txt` (project root) —
55-rule construction on the volley-18 base (full night-VOICE face lock)
+ the "flat cartoon" term volley 18 omitted + character-anchor image
`work/q6/refs/anchor_s14_3s.png` (S14 t1 @3.0s, read back before use:
night-VOICE face, mic on stand, blank ticket, night plaza, flat
cartoon). The sibling used a different anchor (S06a t2 @3.0s,
`work/q6/voice_anchor_night.png`) and its own vehicles in
`work/q6/vehicles/`. Both anchors closed the face failure: 7/7 takes
across both coordinators are flat cartoon with the night-VOICE face.
QC: faster-whisper base int8 word timestamps, same mishear map as
volley 17; frame gate 160x90 gray native 24fps (FAIL if vocal
near-dup run ≥24f OR mean <0.5); character/text by full-res 2s/5s/8s
eye reads. This coordinator's QC: `TAKE_WORDS_Q6.json` (project root)
+ `work/q6/TAKE_WORDS_Q6B_S04A_WARPED.json`; frames
`work/q6/qc_frames/s{07,21,04a}_q6_{2,5,8}s.png`. Sibling QC:
`work/q6/TAKE_WORDS_V6_Q6.json` + `..._FOLLOWUP.json`.

### Sibling set (from work/q6/Q6_LEDGER.md — NOT re-derived here)
- S04a t1: CANDIDATE (warp-rescued). 22/22, ratio 0.711 grey →
  warp 1.1322x → warped 22/22, vocal 0–8.38, ratio 0.804, frame PASS,
  character PASS, text PASS. Assembly: warped take tau 0–8.38,
  factor 1.2433.
- S07 t1: REJECTED (frame FAIL run 33 mid-vocal + text FAIL legible
  red "STOP" signs). S07 t2: CANDIDATE. 10/10, vocal 0–7.14, ratio
  1.190, frame PASS (mean 0.86, run 1), character PASS, text PASS
  (no signs/panels at all).
- S21 t1: CANDIDATE (dropped-"to" micro-gap, same class as v6final).
  13/14, vocal 0–8.34, ratio 1.108, frame PASS, character PASS,
  text PASS, blank ticket (verified on its 5s frame by this
  coordinator), CADMIUM square reads true yellow.

### This coordinator's set (q6b — alternates)
- S07 q6b t1 (`takes/mv2_s07_q6b_t1.mp4`, md5
  `0aa289cceaa253c3454e3e26ab59bf3b`, 1280x720/24fps/10.000s):
  **CANDIDATE.** Lyric 10/10 exactly once (performed line), vocal
  0–7.60s vs song 8.50s → ratio 1.118 IN BAND. Drift median −1.9f,
  range −20.6 to +24.6 ("toll" early-hold, same disclosed class as
  v6final's −32.7f nit, smaller). Frame PASS (mean 1.618, near-dup
  run 1, frozen 0). Character PASS (night-VOICE lock 2s/5s/8s, mouth
  open mid-vocal, closed-mouth hold at 8s). Text PASS (booth panels
  blank, traffic lights glowing dots, ticket blank; rain streaks are
  new weather, not text). Assembly: tau 0–7.60, factor 0.894.
  Note: stronger motion (mean 1.618 vs sibling t2's 0.86) and a
  closer ratio (1.118 vs 1.190) than the sibling's S07 t2 — the
  assembler may prefer this take for the slot.
- S21 q6b t1 (`takes/mv2_s21_q6b_t1.mp4`, md5
  `1f56da47b7f054cafa138cec1361ae1f`, 1280x720/24fps/10.000s):
  **CANDIDATE.** Lyric 14/14 exactly once — INCLUDING the second
  "to" (this vehicle's lyric wrote both "to"s; the sibling's take
  and the v6final both drop it). Vocal 0–7.98s vs song 9.24s →
  ratio 1.158 IN BAND. Drift median +8.8f, range +0.1 to +21.1
  (consistent lag, correctable by the assembly factor; diagnostic).
  Frame PASS (mean 1.008, near-dup run 1, frozen 0). Character PASS
  (night-VOICE lock; hand-to-ear echo gesture at 8s, just after the
  vocal tail). Text PASS (no legible words) with a disclosed nit:
  the ticket carries print-like rules (not blank as the bible
  specifies; 3x crop shows rules + glyph-like smudges, no legible
  words). Assembly: tau 0–7.98, factor 0.864. Note: the only
  14/14 S21 take in the catalogue — the assembler may prefer it
  over the sibling's 13/14, against its cleaner blank ticket.
- S04a q6b t1 (`takes/mv2_s04a_q6b_t1.mp4`, md5
  `6d2f0960cd60da02bc53fe6f5bed7f17`, 1280x720/24fps/10.000s):
  **CANDIDATE (warp-rescued).** Lyric 22/22 exactly once, vocal
  0–8.76s vs song 6.74s → ratio 0.769 GREY. Frame PASS (mean 1.123,
  run 1). Character PASS, text PASS (no legible words; same ticket
  print-rules nit as S21 q6b). Drift not computed (song token
  "flaselines" collapses "fast"+"lanes"; diagnostic only — v17
  precedent also omits S04a drift). Warp-rescue 1.0398x →
  `takes/mv2_s04a_q6b_t1_warped.mp4`, md5
  `8e6be63d43a7fd336004fd5dd767d5a9`, 9.653s: re-QC 22/22, vocal
  0–8.44s, ratio 0.799, frame PASS (mean 1.129, run 1).
  Assembly: warped take tau 0–8.423 (S09-precedent scaled span),
  factor 1.2497 — identical slot geometry to v6's S04a.

## 4. Assembly recommendation (for the sibling / parent)

- Use ONE take per slot; do not mix both sets in one master without a
  reason. Suggested picks, with the trade stated: S07 — q6b t1
  (better ratio + motion) or sibling t2 (already the sibling's pick;
  either covers); S21 — q6b t1 (14/14, ticket print-rules nit) or
  sibling t1 (13/14, blank ticket); S04a — sibling warped t1 (already
  rescued, 0.804) or q6b warped t1 (0.799, same geometry) — equivalent.
- Apply the §2 S25 pool edit; make NO section-boundary cut moves (§1).
- New master is v7 (`masters/mv2_toll_roads_are_dumb_v7_16x9.mp4`);
  v6 untouched (md5 `b2d386bf138aa5e3b654a8382b7b68c0`). Reuse
  `masters_work_v6/captions.ass` unchanged (same song words; performed
  chorus line unchanged). 16:9 house master only per the standing
  one-master rule. Gates: 6432 frames, 268.01s, CRF 18, AAC, song md5
  unchanged, motion audit + mouth-at-cut pass on the delivered file.
- The v6final takes (S04a/S07/S21, character-inconsistent) stay on disk
  as superseded assets, never assembled once v7 lands.

## 5. Files

- This file: `work/q6/Q6_VERDICTS.md` (registry artifact).
- Vehicles (this coordinator): `mv2_s07_vehicle_q6.txt`,
  `mv2_s21_vehicle_q6.txt`, `mv2_s04a_vehicle_q6.txt` (project root).
- QC: `TAKE_WORDS_Q6.json` (project root),
  `work/q6/TAKE_WORDS_Q6B_S04A_WARPED.json`, `work/q6/qc_q6.py`,
  `work/q6/qc_frames/s{07,21,04a}_q6_{2,5,8}s.png` (+ ticket crops).
- Takes (q6b set): `takes/mv2_{s07,s21,s04a}_q6b_t1.mp4` +
  `takes/mv2_s04a_q6b_t1_warped.mp4` (raw media-generation files kept).
- Sibling files (untouched by this coordinator except the repaired
  canonical restore): `work/q6/Q6_PROGRESS.md`,
  `work/q6/Q6_LEDGER.md`, `work/q6/TAKE_WORDS_V6_Q6*.json`,
  `work/q6/VOCAL_WINDOW_V6Q6*.json`, `work/q6/vehicles/`,
  `work/q6/voice_anchor_night.png`.
- Refs/frames (this coordinator): `work/q6/refs/anchor_s{14,24,05}_3s.png`,
  `work/q6/frames/s25_t{4.0,4.5,5.0,5.5,6.0,6.5}s.png`.
- No commit, no flag, no Telegram, no delivery. v6 master untouched.
