# Triple devil's advocate — MV-2 best cut (V4 rebuild), 2026-11-02

User order 2026-11-02 04:43 EST: triple devil's advocate, refire anything
wanted, make the best time-swing full video, then generalize into a pipeline.
Audit base for the first two devils was the leader-fixed master; the fixes
were then rebuilt into the best cut below, which was re-verified with
word-matched frames (audit_v5), not singing stills.

## Best cut delivered

- `masters/mv2_toll_roads_are_dumb_v3_16x9.mp4`
- md5 `e5dcfe3a598b989b6d021e3e702a50b4`, 75,396,196 bytes, 268.01 s
- h264 1280x720 24 fps, AAC 48 kHz stereo, mov_text subtitles (48 cues),
  `~ WuBu ~` corner bug, +faststart, song audio untouched (`track.mp3`).
- Active takes: S01 t4, S02 t3, S03 t2, S04 t4, S05 t4, S06 t2, S07 t2,
  S08 t1, S09 t2, S10 t1, S11 t2, S12 t3, S13 t2, S14 t1, S15 t2, S16 t1,
  S17 t2, S18 t1, S19 t1, S20 t2, S21 t2, S22 t1, S23 t1, S24 t1, S25 t2,
  S26 t2, S27 t2. 16:9 only; no 9:16 cut built (no blind center-crop shipped).
- Video stream is 6,426 frames / 267.75 s vs 268.01 s audio: per-segment
  frame rounding in the swing assembly, a 0.26 s shortfall at the very tail.
  The outro tear (266.0) and final smile (267.5) are both present in the
  master; players hold the last frame over the final quarter-second of
  audio decay. Disclosed, not a desync: every anchored word lands on its
  song time (see below).

## Devil 1 — "the sync is fake"

Findings on the leader-fixed master, and what the rebuild did about them:

- **S04 was singing the WRONG SEGMENT (proven).** Density 0.16 (3 anchors /
  19 take words). Its t3 vehicle was written for song 30–40 s, but its
  window was 43–48 s; the matcher had anchored only homonym collisions
  ('the', 'the', 'ones'). Fixed by refire: S04 t4, LCS match 15/19, window
  lyric fully covered in order ("the speeds don't match at all, one car's
  racing, the other ones about to fall"). First-anchor frame at 42.86 in
  the best cut: face-to-camera, ticket in hand, singing — not the old
  gesture-not-singing frame.
- **S21's window had COLLAPSED (proven).** Density 0.40, window 205.2–222.44
  (17.24 s) for a take that sang a chorus echo line. Forced anchors 'The'
  at 205.2 and 'roads' at 220.6; audit frame at 205.30 was posed, mouth
  closed. Fixed by refire: S21 t2, LCS match 14/21, dense anchors
  The 205.20 → slow 213.80. First-anchor frame at 205.30 in the best cut:
  face-to-camera, mouth open, singing.
- **S02 (0.50), S03 (0.52), S16 (0.56) were NOT misplaced.** Right segment,
  weak mid-alignment because the matcher could not align through whisper
  garble of the SONG transcript (e.g. "make your pay. The roll -old
  plasers", "$1" vs take "dollar"). No refire; the fix is lyrics-guided /
  LCS matching in the pipeline, not new takes.
- **Whisper degenerate burst (proven, pipeline bug).** Song words idx
  332–338 ("the road gets meaner every single time") all have t0=t1=205.20
  — zero duration, no timing. Greedy-earliest matching collapsed on S21
  (3/21 anchored, two wrong). Fixed in `match_take.py`: LCS sequence
  alignment, and zero-duration song words are excluded as targets — the
  take head stays honestly unanchored and plays at natural speed instead
  of collapsing into a blur. S21's 7-word burst head (take 0.00–3.86) plays
  at 1.0x into song 201.34–205.20; S04's garbled "weave in, weave out" head
  ("We've been, we've out", take 0.00–2.00) plays at 1.0x into 40.76–42.76.
  Both heads are unanchored by design and disclosed, not hidden.
- **Noise-merge side effect (disclosed).** The assembler's >4x / <0.25x
  onset-interval rule drops middle anchors. In the best cut it drops
  S05 'are' (merged roads→dumb at 3.79x; 'are' lands interpolated at
  ~52.16 vs true 52.08, +0.08 s / 2 frames) and 2 of S21's 14 anchors.
  Effective anchor counts in CUTLIST_V3_SWING.json (S05: 3, S21: 12) are
  post-merge counts, not match counts.
- **Subtitles PASS.** `captions_v2.srt` cues are line-level, timed to
  LYRIC_TIMELINE boundaries, correct against the untouched song audio.
  Line-level captions do not need word precision.
- **S16's 13.33x fastest sweep is harmless.** The 6-frame strip
  (166.02→167.00) shows one static coin-hold pose throughout — no
  teleport. Lesson: flag extreme speeds only when the take actually moves
  during the interval. Same check applied to the best cut's tail extremes
  (below).

## Devil 2 — "the performance is wrong"

First-anchor frames for all 26 anchored scenes in the best cut
(`masters_work_v3/audit_v5/sheet_1/2/3.jpg`, frame = first anchor +0.10 s):

- GOOD (face-to-camera, mouth open/visible): S01 (Yeah, t4), S05 (Toe),
  S06, S07, S09, S10, S11, S13, S14, S15, S16, S17, S18, S19, S20, S21 (The,
  fixed), S22, S23, S24, S25, S26.
- Nits only, all take staging, none refired (no third diagnosed target):
  S02 profile opening at the booth @20.22; S03 neutral/closed mouth at
  'Cars' @27.44; S08 down-glance at ticket at 'they' @88.58; S12
  back-to-camera at its first word 'poor' @111.40 (its other 13 anchors
  face camera); S19/S22 neutral at onset (+0.10 s catches the mouth
  before it opens — onset framing, not a miss).
- No on-screen text in any audit frame; `~ WuBu ~` bug present in all.
- The old v3 headline nit is GONE: S05's chorus-1 opening no longer lands
  on a back-turned ticket raise — t4 is face-to-camera at 50.94.

## Devil 3 — "the pipeline is fragile"

- **Leader fix VERIFIED on the best cut.** Verify sheet: master@58.20 =
  S06 wide shot face-to-camera (not S05's pose); S01 frozen at 7.30,
  moving with ticket raised at 7.50 (motion starts at the 4.44 hold end,
  not 7.375 — the leader is now 4.44 s, S01 t4's Yeah pose); S27 outro
  frames at 266.0 (tear in progress, smiling) and 267.5 (final smile) —
  the tail is no longer trimmed. Standing lesson, unchanged: any clip
  fed to a concat must be stream-checked; holds/leaders are built `-an`;
  sync is verified by word-matched frames, never singing stills.
- **Boundary tolerance (unchanged, sub-5-frame).** Frames at both 57.80
  and 57.95 already show S06, so the S05→S06 cut lands ~0.1–0.2 s before
  the nominal 57.86 (per-segment frame rounding). Not a new desync.
- **Tail extremes, checked, not defects.** S09 tail 24.38x (6.34 s of take
  tail into 0.26 s of song, 95.88–96.14) and S22 tail 17.5x (7.0 s into
  0.40 s, 224.24–224.64) are static resting poses in the mid-tail frames
  (96.0, 224.44) — a quick settle, not a strobe. The lesson stands:
  extreme speed alone is not a fail; a moving tail at extreme speed is.
- **STRUCTURAL LIMIT — disclosed, not fixed in this cut.** 27 scenes
  partition a 48-line song, so every scene's window extends past its
  take's sung line into a tail hold while other song lines play. Longest:
  S14 window 128.76–160.20 (31.44 s); its last word ends 134.60, then a
  static ticket-hold (frames at 135 / 145 / 155 / 159.5 are the same pose)
  plays while the song sings "Pay to go faster… We've been slamming the
  danger roads… Toe roads are done (x2)… Fast lanes make crashes".
  S23 (224.64–243.24, tail from 231.24) and S07 (70.62–88.48) are the same
  shape. This is the v3 design, not a V4 regression — the windows are
  identical to the pre-V4 cutlist except where S01/S04/S05/S21 changed —
  but it is the honest limit of "one line per take" cutting, and the
  first candidate fix for the pipeline loop: more scenes per song, or
  B-roll / cutaway coverage during tails, so no 25-second stretch plays
  over a frozen singer.
- **What did NOT break:** master audio cross-check (master words match
  song words at +0.00, one +0.16 whisper jitter on "crash") — the v3
  desync was purely video-side, and this rebuild's video is built
  `-an` throughout, so that failure class cannot recur from this script.

## Volley V4 (the refires behind this cut)

5 of 6 budget used, 6th deliberately unspent (no third diagnosed target;
face audit found only nits; S02/S03/S16 softness is matcher garble).
Manifest: `masters_work_v3/VOLLEY_V4_MANIFEST.md`. Verdicts + md5s in
TAKE_HISTORY.md.

- S01 t3 — REJECTED for its mission (no "Yeah"; words start take 3.26
  with "Listen"). Kept on disk, not active.
- S01 t4 — KEEP (Yeah fixed; Yeah as sole first event in the vehicle).
  md5 416defdc7e71b17b284c62a51d9422a5. Whisper "Yeah," take 0.00–1.24,
  full line through 9.26, 11 words, LCS 11/11 (Yeah→4.44 … seem→12.88).
- S05 t4 — KEEP (facing during hook). md5 da8cc5ccbfd1cdc5774c6196b718c6e9.
  Whisper "Told roads are dumb" 2.76–7.14. LCS 4/4 (3 effective after
  noise-merge, see above).
- S04 t4 — KEEP (lyric segment). md5 a83e89f76c03292eeb5c4dd3ddc0cb81.
  LCS 15/19; garbled head disclosed above.
- S21 t2 — KEEP (lyric segment). md5 55302d1dc2900fac45e31b82f744a187.
  LCS 14/21 (12 effective after noise-merge); burst head disclosed above.

## Pipeline lessons carried forward (before the research loop reports)

1. Match by LCS, never greedy-earliest; exclude zero-duration whisper
   words as targets; let unanchored heads play at natural speed.
2. Noise-merge (>4x / <0.25x) is a blunt instrument — it silently drops
   real words (S05 'are'). A dropped anchor must be logged, and its
   interpolated landing error stated.
3. Verify with word-matched frames: first-anchor sheet + fastest-sweep
   strip + boundary/outro verify sheet. A contact sheet is not a drift
   check; singing stills are not a sync check.
4. Extreme speed is a flag, not a verdict — check whether the take moves
   during the interval.
5. Scene count vs lyric-line count is a structural decision, not a
   detail: 27 scenes / 48 lines guarantees long tail holds. The next
   pipeline version must decide that number up front.
6. Stream-check every clip fed to a concat; holds/leaders `-an`.

## Tools (in `masters_work_v3/`, reusable for other tracks)

- `transcribe_take.py` — ffmpeg → 16 kHz mono f32 → faster-whisper base
  CPU int8 → word-timestamp JSON.
- `match_take.py` — LCS alignment, mishear map, zero-duration exclusion.
- `audit_anchors.py <master.mp4> <outdir>` — first-anchor sheets,
  fastest-sweep strip, verify sheet. Audit for this cut: `audit_v5/`.
- `assemble_v3_swing.py` — unclamped setpts per word interval, video-only
  segments, sequential windows, S27 visual outro.
