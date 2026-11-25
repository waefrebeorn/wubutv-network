# MV-11 "Water hit my balls" — ASSEMBLY NOTES (coordinator, spawned ~00:38 EST 2026-11-10)

## STATUS — CHECKPOINT (start)
- Inputs VERIFIED: track.mp4 md5 `18273d7a593e623b720105df195bede2`, audio 172.400s
  (ffprobe: h264 824x1464 + AAC, both streams 172.400000s — the plan's 172.42s
  is a 0.02s rounding of the same duration). All 23 KEEP-take md5s match
  work/TAKE_LEDGER.md (0 mismatches; S04's ledger filename is correct —
  the first md5 pass failed on a transcription typo in the check command,
  re-run against the real file `...-d5fc1bfc-32f2-...` matches 8e679b8f…).
  All 26 takes on disk are 1248x704, 24fps (16x10s, 9x5s, 1x6s).
- Method: MV-10 builder pattern, SIMPLIFIED — MV-11 needs no PCHIP (only
  one sung scene, S07, phrase-level constant-factor warps; every other
  scene is a CUTAWAY trim or a gentle uniform slowdown <=1.09x). Per-scene
  CRF-14 intermediates forced to contract frames, manifest checkpointed
  after EVERY segment. Split final encode at S12/S13 (78.66s) — MV-8 v3
  lesson: single-pass full encode OOM'd at the trailer. Kinetic .ass
  burn-in (fixed SLAM, MV-9 "goty" bleed fix in kinetic_ass.py).
- NO segments built yet. NO master yet. NO delivered flag (parent writes it).

## SCENE CONTRACTS (frames, 24fps; boundaries round(t*24); total exactly 4138f = 172.4167s)
S01 0.00–9.00 = 216f | S02 9.00–13.76 = 114f | S03 13.76–23.76 = 240f |
S04 23.76–33.76 = 240f | S05 33.76–38.94 = 125f | S06 38.94–45.18 = 149f |
S07 45.18–50.14 = 119f | S08 50.14–55.26 = 123f | S09 55.26–60.26 = 120f |
S10 60.26–65.26 = 120f | S11 65.26–70.66 = 130f | S12 70.66–78.66 = 192f |
S13 78.66–86.66 = 192f | S14 86.66–94.66 = 192f | S15 94.66–101.78 = 171f |
S16 101.78–111.00 = 221f | S17 111.00–121.00 = 240f | S18 121.00–131.00 = 240f |
S19 131.00–141.00 = 240f | S20 141.00–151.00 = 240f | S21 151.00–155.06 = 97f |
S22 155.06–165.06 = 240f | S23 165.06–172.42 = 177f.
Boundary drift vs true song times <=0.04s (+-1f); S07 anchors use absolute
song times, so word placement is exact regardless.
Video total 4138f = 172.4167s vs audio 172.400s: video overhang 0.0167s
(<1 frame) — the last video frame plays 17ms past the audio end. Disclosed.

## PIECE PLAN (take = media-generation-mv11-<scene>-t<n>, all 1248x704 24fps)
- S01: trim s01-t1 f0–215 (first 216f of 240). Crown already bloomed at 0s
  (anchor-still pattern); calm tail fits the cold open.
- S02: trim s02-t1 f0–113 (first 114f of 120). Duck close-up at 4.8s is
  past the 4.76s window — the trim lands the cut before it.
- S03: natural s03-t1 full 240f. S04: natural s04-t1 full 240f.
- S05: uniform s05-t1 f0–119 (120f) -> 125f (1.0417x slow). Reverse splash
  at take 2.5s lands at song 36.36 (slot 33.76–38.94) — inside the window.
- S06: uniform s06-t1 f0–143 (144f, 6.00s) -> 149f (1.0347x slow).
- S07 (THE ONE SUNG SCENE — phrase-level warps, one factor per phrase,
  take phrases from the ledger: P1 "Sitting on the toilet" 0.00–1.96,
  P2 "Water hits" 2.18–3.32, P3 "My balls" 3.32–4.38; song phrases
  45.18–47.18 / 47.18–48.64 / 48.64–50.14):
  P1 f0–46 (47f) -> 48f (1.0213x slow); P2 f52–79 (28f) -> 35f (1.2500x slow);
  P3 f80–105 (26f) -> 36f (1.3846x slow). Take inter-phrase gap 1.96–2.18
  (6f) and tail 4.38–5.00 are DROPPED — the joins sit on phrase boundaries
  (song 47.18, 48.64), a 6-frame skip of closed-mouth inter-phrase pause
  in a continuous slow push-in. All three factors < 2x cap. Mouth gate on
  the built segment: "Sitting" onset is in the wide push-in head (mouth
  unreadable at distance, open by mid-phrase — disclosed line-start lag,
  MV-10 precedent); "Water" 47.18 + "My balls" 48.64 must read OPEN.
- S08: trim s08-t1 f0–122 (first 123f of 240). Ends tight on the bowl.
- S09: natural s09-t1 full 120f. S10: natural s10-t1 full 120f (tail drifts
  to a front-facing open-beak duck close-up at 4.8s — the ledger's "accept
  the cute beat" option; silent witness, no audio claim).
- S11: uniform s11-t1 f0–119 (120f) -> 130f (1.0833x slow).
- S12: trim s12-t1 f0–191 (first 8s). S13: trim s13-t1 f0–191 (first 8s).
  S14: trim s14-t1 f0–191 (first 8s).
- S15: uniform s15-t1 f0–167 (168f, 7.00s) -> 171f (1.0179x slow).
  Highest climb at take 6.5s lands at song 101.27 (slot ends 101.78).
- S16: uniform s16-t1 f0–215 (216f, 9.00s) -> 221f (1.0231x slow). Slot is
  9.22s, take window is 9.00s — the 1.023x stretch fills it; duck at top
  of arc (take 8.0s) lands at song 109.96, inside the window.
- S17: natural s17-t1 full 240f. S18: natural s18-t1 full 240f.
  S19: natural s19-t1 full 240f. S20: natural s20-t1 full 240f.
- S21: trim s21-t1 f0–96 (first 97f of 120). Apex hold at take 4.0s lands
  at song 155.0 (slot ends 155.06) — the cut lands ON the apex hold.
- S22: natural s22-t2 full 240f (bone-white rim throughout).
- S23: trim s23-t1 f0–176 (first 177f of 240). DECISION — crown head KEPT,
  no trim: the 0–2s anchor crown echoes S01's opening crown (the documented
  house anchor-still pattern — S01/S06/S12–S16/S22 all open on it), the
  drop at take 3.5s lands at song 168.56 and the calm end at take 6.5s
  lands at song 171.56, both inside the window. The S22-tail -> S23-head
  cut (calm -> crown) reads as the final drop's setup, rhyming with the
  opening. Drop + calm end both verified in-window.

## WARP FLAGS (cap audit: playback <0.50x = slow past 2x; speedups fine)
- NO warp exceeds 1.39x slow. Slowest: S07 P3 1.3846x, P2 1.2500x, S11
  1.0833x, S05 1.0417x, S06 1.0347x, S16 1.0231x, S07 P1 1.0213x,
  S15 1.0179x. Everything else is a straight trim (1.000x).
- S07 is the only word-sync warp in the build; every other scene is a
  CUTAWAY (montage/kinetic), so no other warp is owed.

## KINETIC (post layer, .ass — work/build_kinetic.py -> work/assembly/mv11_kinetic.ass)
Presets per the plan: SLAM on hook "Water"/"Splash"/"Balls" onsets,
HIGHLIGHT on the verse + splash lines, CASCADE on the "Balls balls" patter.
Corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form).
WORD TEXT — sources, in priority order (see build_kinetic.py for the full
auditable map in work/assembly/mv11_kinetic_words.json):
  Hook 1 / Verse / Pre-Hook / Hook 2: analysis/SONG_WORDS.json (92 words,
  baseline small model) with the LYRIC_TIMELINE.md ASR corrections:
  "our"->"I" 22.18, "boss"->"balls" 30.58, "Dash"->"Splash" 34.94,
  "Sipping"->"Sitting" 45.18; DROP spurious "Music" 3.12 + "done" 29.04.
  Whisper-merge caps (merged durations are NOT held notes): "balls"
  72.34–76.68 capped to end 73.34; "hits" 78.34–82.78 capped to end 79.34;
  zero-duration "my" 72.34 dropped.
  Final Hook: test #2 seg-9 VOCALS (winner, coverage 0.923) for S18/S19
  lines (122.38, 125.04, 137.72) + test #1 turbo full-clip for the splash
  line 128.66–130.68 + seg-10 MIX for S20 Water line 141.51–143.67 +
  timeline anchor for S21 "Balls balls" 153.60–155.06 + turbo outro
  "Balls" 170.92–172.32 (measured AFTER the plan was written — plan said
  "no words" in the outro; the word is real, so it gets one SLAM).
  S17 (111–121): NO kinetic — no measurable word times in the loop zone
  (111.82–122.38 blank in every pass); the montage carries it. Disclosed.
  S16: SLAM "Water" 110.68–111.72 only (the Drop water); the "BALLS!"
  shout is unmeasured in every pass — NO guessed slam. Disclosed.

## FINAL ENCODE PLAN (MV-10 lessons: split encode, no single-pass OOM)
Split at the S12/S13 boundary (78.66s): half 1 = S01–S12 (1888f),
half 2 = S13–S23 (2250f). Video-only CRF-18 halves with kinetic burned
in, then mux halves + track audio re-encoded AAC 48k stereo (NEVER MP3
copy; apad capped whole_dur=172.417 + -t 172.42) + faststart. Gates on the
master: exactly 4138f; SEI crf=18.0; AAC codec (ffprobe); faststart;
mouth state at S07 word onsets by eye on the MASTER; motion audit.
Chat copy <=50 MB (bitrate cap, AAC copied) only if the house master
exceeds 50 MB.

## EYE-CHECKS ON BUILT SEGMENTS (frames at song word onsets, work/assembly/eye_s07/)
- S07 MOUTH GATE — PASS, NO RE-FIRE OWED. Built segment frames (song times):
  45.18 ("Sitting" onset, f0): wide push-in head — mouth unreadable at
  distance, disclosed line-start lag (MV-10 precedent); 46.18 (f24, mid-P1):
  profile close-up, mouth OPEN; 47.18 ("Water" onset, f48): mouth WIDE OPEN,
  teeth visible; 47.89 (f65, mid-P2): OPEN; 48.64 ("My balls" onset, f83):
  OPEN; 49.39 (f101, mid-P3): OPEN. The P1->P2 join (segment f47->f48,
  take f46->f52, 6-frame skip of closed-mouth inter-phrase pause) reads
  continuous — same profile framing, push-in underway. No onset closed.
  Motion: push-in underway by f24; locked-off profile after, mouth + head
  drift (the take's own subtle seated-man motion, ledger baseline).

## NEXT STEPS
1. Write work/build_kinetic.py + work/assembly_build.py — DONE next.
2. Build kinetic .ass; verify event count + no bleed (SLAM tails capped).
3. Build segments S01->S23 (checkpoint manifest after each).
4. Eye-check S07 segment (frames at song 45.18/47.18/48.64 + phrase mids).
5. Split-encode halves; mux; gates; chat copy if needed.
6. Short final report to parent (master path/md5/ffprobe/gates/S07 verdict).
   NO commit. NO delivered flag (parent writes it).

## S07 WARP BUG — FOUND BY MOTION AUDIT, FIXED (~01:35 EST)
- Motion audit on the first master: ONE near-still run >=12f — 63f @ 47.21-49.79s (S07 P2/P3, during words).
- Root cause (BUILD BUG, not the take): assembly_build.py's warp chain was
  `trim=...,setpts={factor}*PTS,fps=24`. For pieces trimmed from a NON-ZERO
  frame, ffmpeg's fps filter starts its output clock at t=0 (not at the
  first frame's PTS), so it zero-fills the head with repeats of the first
  frame: P2 (take f52-79, PTS 2.17-3.29s) came out as 65x frame-52 repeats +
  35 real frames; P3 (take f80-105) as ~111x frame-80 repeats + 36 real.
  The concat + `trim=end_frame=119` then kept only the first 119f, so the
  shipped S07 was P1 (48f, correct) + 35x frame-52 + 6 real P2 frames —
  P3 NEVER APPEARED, and the verse read as one frozen open-mouth frame.
- The earlier "S07 mouth gate PASS" was VOID: its four eye frames (f48/f65/
  f83/f101) were all the same frozen frame 52. Lesson: a mouth gate must
  verify the sampled frames are DISTINCT (md5) before reading mouths.
- The raw take is healthy in that span (mean diff 6.54, 0/60 zeros).
- FIX: rebase PTS to zero BEFORE scaling:
  `trim=...,setpts=PTS-STARTPTS,setpts={factor}*PTS,fps=24`.
  Isolated test on P2: 35f, mean diff 5.50, 0 zeros. Applied to
  assembly_build.py (all scenes; no-op for pieces starting at frame 0).
- REBUILT S07 (md5 f43552119f0e...): 119f; P1 mean 9.21 / P2 6.15 / P3 3.73,
  ZERO frozen frames in any span.
- RE-RUN MOUTH GATE (rebuilt segment, all 6 frames distinct md5s):
  f0 45.18 "Sitting" onset: wide push-in head, mouth unreadable at distance
  (disclosed line-start lag, MV-10 precedent); f24 46.18 mid-P1: profile,
  mouth OPEN; f48 47.18 "Water" onset: mouth WIDE OPEN, dark interior;
  f65 47.89 mid-P2: mouth OPEN, smaller, tongue visible — different shape;
  f83 48.64 "My balls" onset: teeth-showing near-closed shape — distinct;
  f101 49.39 mid-P3: mouth nearly closed mid-"balls" (take's own consonant
  articulation; opens again by take 4.5 per ledger). Four distinct mouth
  shapes tracking the phrases; push-in continues through P2/P3.
  MOUTH GATE PASS (real this time). No re-fire owed.
- Downstream re-run required (S07 is in half 1): split_encode -> mux ->
  gate_master -> chat_copy -> motion audit -> master eye frames.

## MASTER #2 — COMPLETE + ALL GATES PASS (~02:00 EST)
- House master: masters/mv11_water_hit_my_balls_16x9.mp4
  md5 c1317938b170f5154f8d9886d8952a1d, 134,718,102 B, exactly 4138f,
  172.417s, h264 1280x720 24fps, AAC 48k stereo, x264 SEI crf=18.0,
  faststart moov@36 < mdat@120865. Audio agreement vs track: min corr
  0.9977 (5 windows). ALL GATES PASS (gate_master.log).
- Chat copy: masters/mv11_water_hit_my_balls_16x9_50mb.mp4
  md5 de4a44e05f60b0c07f1ac73dc331611f, 39,954,473 B (38.1 MB), 4138f,
  172.417s, h264 1280x720 24fps, AAC; audio-stream md5 identical to house
  master (339ee5e99019926f9717f91bc53ac996 both). CHAT COPY OK.
- Motion audit #2 (work/motion_audit.py, full master, native fps):
  overall mean diff 11.82; ZERO near-still runs >=12f; no FAIL-range runs.
  PASS. (Master #1 had exactly one: the S07 warp bug, fixed.)
- S07 mouth gate (rebuilt segment + master #2 frames f1132/f1167):
  PASS — 47.18 "Water" WIDE OPEN; 48.64 "My balls" distinct teeth-showing
  shape; four distinct mouth shapes across the verse; push-in continues.
- Full-master watch (work/assembly/eye_watch/): one midpoint frame per
  scene (23/23) + SLAM checks (Water 14.00, Balls 153.85, Water 110.90) +
  S07 master onsets — ALL SCENES CORRECT, kinetic renders, corner bug
  present throughout, bone-white rims in S22/S23.
- SLAM fade-in note: at the EXACT onset frame a SLAM word is at 0 scale
  (60ms scale-in); mid-event frames show it at full size. Not a defect.
- CASCADE fly-in transient (house preset quirk, disclosed): on multi-word
  CASCADE lines a word entering from the left passes through an earlier
  word's slot for ~200ms (seen S04 28.76s, S19 ~136s). Settles clean —
  verified S04 at 29.20s: all five words evenly spaced, no overlap.
- S15 accent bar grazes the dim "balls," baseline at 98.22s (cosmetic).
- S06/S09/S13 rims read warm cream near the lamp (lighting, not the
  S22 orange-porcelain defect); S22 tiles warm amber-orange from ~5s
  (ledger-disclosed), porcelain stays bone white.
- Master #1 (md5 891fe032..., 133,940,969 B) + chat copy #1
  (md5 2e5dca4f..., 39,941,763 B) SUPERSEDED — deleted before re-mux.
  Do NOT deliver master #1.
- Assembly spans (frames @24fps, total 4138f): S01 0-215, S02 0-113,
  S03 0-239, S04 0-239, S05 uniform 120f->125f, S06 144f->149f,
  S07 phrase warps P1 f0-46->48f / P2 f52-79->35f / P3 f80-105->36f,
  S08 0-122, S09 0-119, S10 0-119, S11 120f->130f, S12 0-191, S13 0-191,
  S14 0-191, S15 168f->171f, S16 216f->221f, S17 0-239, S18 0-239,
  S19 0-239, S20 0-239, S21 0-96, S22 0-239, S23 0-176 (crown head KEPT).
  Kinetic: 33 lines / 125 words / 191 events, corner bug whole duration.
