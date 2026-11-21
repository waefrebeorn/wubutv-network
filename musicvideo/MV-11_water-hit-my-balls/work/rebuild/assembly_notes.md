# MV-11 REBUILD — ASSEMBLY NOTES (coordinator ff3ae200, spawned 2026-11-10 ~06:11 EST)

Rebuild COMPLETE: S01–S23 all hold KEEP in work/TAKE_LEDGER_REBUILD.md
(volley 6 committed bd387a0f, 13 files). This assembly uses REBUILD takes
only — never a v1 take, never a REJECT take. V1 assembly machinery reused:
work/assembly_build.py + work/assembly_notes.md + work/build_kinetic.py
(read in full). Rebuild pipeline lives under work/rebuild/ (own builder,
own segment dir, own kinetic .ass, own master filename) — the v1 files
are NOT edited in place.

## STATUS — CHECKPOINT (start)
- Inputs VERIFIED: track.mp4 md5 `18273d7a593e623b720105df195bede2`, 172.42s.
  All 23 rebuild KEEP-take md5s match work/TAKE_LEDGER_REBUILD.md (0
  mismatches, verified by md5sum 2026-11-10 ~06:12 EST). All 23 takes are
  1248x704, 24fps (20x10.000s, 2x5.000s [S07 t2, S21 t2], 1x8.000s [S14 t2]).
- Method: v1 builder pattern, same scene contracts (boundaries round(t*24),
  total exactly 4138f = 172.4167s). Only the take files + usable spans change.
  Per-scene CRF-14 intermediates forced to contract frames, manifest
  checkpointed after EVERY segment. Split final encode at S12/S13 (78.66s).
  Kinetic .ass re-derived (same song times as v1 — the .ass should reproduce
  v1's event for event; diffed to confirm).
- Master filename (NEW — never overwrite the rejected v1 master):
  masters/mv11_water_hit_my_balls_rebuild_16x9.mp4. The v1 master
  (masters/mv11_water_hit_my_balls_16x9.mp4, md5 c1317938…) stays on disk
  as rejected reference.
- NO segments built yet. NO master yet. NO delivered flag (parent writes it).

## SCENE CONTRACTS (frames, 24fps; boundaries round(t*24); total exactly 4138f)
S01 0.00–9.00 = 216f | S02 9.00–13.76 = 114f | S03 13.76–23.76 = 240f |
S04 23.76–33.76 = 240f | S05 33.76–38.94 = 125f | S06 38.94–45.18 = 149f |
S07 45.18–50.14 = 119f | S08 50.14–55.26 = 123f | S09 55.26–60.26 = 120f |
S10 60.26–65.26 = 120f | S11 65.26–70.66 = 130f | S12 70.66–78.66 = 192f |
S13 78.66–86.66 = 192f | S14 86.66–94.66 = 192f | S15 94.66–101.78 = 171f |
S16 101.78–111.00 = 221f | S17 111.00–121.00 = 240f | S18 121.00–131.00 = 240f |
S19 131.00–141.00 = 240f | S20 141.00–151.00 = 240f | S21 151.00–155.06 = 97f |
S22 155.06–165.06 = 240f | S23 165.06–172.42 = 177f.
Video total 4138f = 172.4167s vs audio 172.400s: video overhang 0.0167s
(<1 frame) — the last video frame plays 17ms past the audio end. Disclosed
(same as v1).

## PIECE PLAN (rebuild takes; usable spans from the rebuild ledger)
- S01 t1: trim f0–215 (216f). Cold open, crown already bloomed at 0s.
- S02 t1: trim f0–113 (114f). Slot end 4.76s, before the tail push-in.
- S03 t1: natural full 240f. S04 t1: natural full 240f.
- S05 t1: uniform f0–123 (124f) -> 125f (1.0081x slow). Usable span 0–5.18s;
  reverse splash at take 2.5s lands at song ~36.28, inside the window.
- S06 t1: uniform f0–143 (144f, 6.00s) -> 149f (1.0347x slow). Same as v1.
- S07 t2 (THE ONE SUNG SCENE — phrase-level warps; see S07 section below):
  P1 f0–51 (52f) -> 48f (0.9231x speedup); P2 f57–85 (29f) -> 35f (1.2069x
  slow); P3 f86–114 (29f) -> 36f (1.2414x slow). Take gaps f52–56 (5f
  inter-phrase pause) + tail f115–119 (5f post-word tail) DROPPED — both
  closed-mouth; joins sit on song phrase boundaries 47.18 / 48.64.
- S08 t1: trim f0–122 (123f). Usable span 0–5.12s.
- S09 t1: trim f0–119 (120f). Usable span 0–5.00s.
- S10 t1: trim f0–119 (120f). MUST trim at 5.00s — the duck DUPLICATES in
  the surplus tail (second duck from ~5.5s); the slot 0–5.00s has one duck.
- S11 t4: uniform f0–119 (120f) -> 130f (1.0833x slow). Usable span 0–5.40s;
  surface at take 4.5s lands at song ~70.13, inside the slot.
- S12 t1: trim f0–191 (192f). Usable span 0–8.00s.
- S13 t2: trim f0–191 (192f). Usable span 0–8.00s.
- S14 t2: trim f0–191 (192f). Usable span 0–8.00s.
- S15 t2: uniform f0–167 (168f, 7.00s) -> 171f (1.0179x slow). Usable span
  0–7.12s; splash peaks at take ~2s, lands at song ~96.70.
- S16 t1: uniform f0–215 (216f, 9.00s) -> 221f (1.0231x slow). Usable span
  0–9.22s; crown apex at take 5.0–5.5s lands at song ~106.90–107.41 — the
  crown hangs at apex through the ~107s silence.
- S17 t1: natural full 240f. S18 t1: natural full 240f.
  S19 t1: natural full 240f. S20 t1: natural full 240f.
- S21 t2: trim f0–96 (97f of the 5.000s take). Usable span 0–4.06s; apex at
  take 2.5s lands at song 153.5, holds to the slot end 155.06; the "Balls"
  SLAM at take 2.60 lands at song 153.60.
- S22 t1: natural full 240f.
- S23 t1: trim f0–176 (177f). Usable span 0–7.36s; the final "Balls" surge
  at take 5.84s lands at song 170.90 (turbo-measured final "Balls" 170.92).

## S07 TAKE-WORD MEASUREMENT (re-measured this run — do not trust the ledger alone)
- QC json (volley-2 coordinator): Sitting 0.00–0.94 · on 0.94–1.36 ·
  the 1.36–1.56 · toilet 1.56–2.16 · water 2.52–3.04 · hits 3.04–3.54 ·
  my 3.54–4.22 · balls 4.22–4.62.
- Independent re-transcription this run (lyrics venv, large-v3-turbo, fixed
  config, no VAD): Sitting 0.00–0.92 · on 0.92–1.40 · the 1.40–1.56 ·
  toilet 1.56–2.10 · water 2.42–3.04 · hits 3.04–3.62 · my 3.62–4.24 ·
  balls 4.24–4.74. Same words, same order, no invented speech; boundaries
  agree within ±0.12s (Whisper timestamp jitter).
- Phrase boundaries use the UNION of both measurements (conservative):
  P1 0.00–2.16 (max toilet end) · P2 2.42–3.62 (min water onset / max hits
  end) · P3 3.54–4.74 (min my onset / max balls end). The P2/P3 join is set
  at the midpoint of the measurement disagreement (f86 = 3.5833s): each
  side clips at most 0.04s of the other measurement's word tail — sub-frame,
  inaudible in a visual warp.
- Song phrases (LYRIC_TIMELINE.md, [confirmed]): P1 45.18–47.18 (48f) ·
  P2 47.18–48.64 (35f) · P3 48.64–50.14 (36f). Total 119f.
- Warps: P1 52f->48f (0.9231x speedup) · P2 29f->35f (1.2069x slow) ·
  P3 29f->36f (1.2414x slow). All < 2x cap. (Ledger's "~1.46x" for P2 was
  an approximation from rounded phrase spans; the frame-exact figure is
  1.2069x.)
- Mouth gate on the BUILT segment (frames at song onsets, DISTINCT md5s
  verified first — the v1 S07 warp-bug lesson): f0 (45.18 "Sitting" onset)
  wide push-in head, mouth unreadable at distance (disclosed line-start
  lag, MV-10 precedent); f48 (47.18 "Water" onset) must read OPEN; f83
  (48.64 "My balls" onset) must read OPEN; mid-phrase frames f24/f65/f101
  read for shape change. PENDING — gate runs after the segment is built.

## WARP FLAGS (cap audit: playback <0.50x = slow past 2x; speedups fine)
- NO warp exceeds 1.39x slow. Slowest: S07 P3 1.2414x, P2 1.2069x,
  S11 1.0833x, S06 1.0347x, S16 1.0231x, S15 1.0179x, S05 1.0081x,
  S07 P1 0.9231x (speedup). Everything else is a straight trim (1.000x).
- S07 is the only word-sync warp in the build; every other scene is a
  CUTAWAY (montage/kinetic), so no other warp is owed.
- Warp chain (v1 S07 bug fix, applied to ALL pieces): trim + setpts=
  PTS-STARTPTS + setpts={factor}*PTS + fps=24. The pre-fix chain
  (trim + setpts={f}*PTS + fps=24) zero-filled the head with first-frame
  repeats for any piece trimmed from a non-zero frame — P2/P3 in v1's
  first master were frozen frames. The fix is in the builder; verify by
  the S07 mouth gate reading DISTINCT frames.

## KINETIC (post layer, .ass — work/rebuild/build_kinetic_rebuild.py)
Same song times as v1 (build_kinetic.py logic, re-run into
work/rebuild/assembly/): SLAM on hook "Water"/"Splash"/"Balls" onsets,
HIGHLIGHT on the verse + splash lines, CASCADE on the "Balls balls"
patter; corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form).
33 lines / 125 words / 191 events expected (same as v1 — diff the .ass
against v1's to confirm). S17: NO kinetic (loop zone, no measurable words
111.82–122.38). S16: SLAM "Water" 110.68 only (the "BALLS!" shout is
unmeasured — NO guessed slam). SLAM last-word tails use the fixed
kinetic_ass.py (min(w.end+0.4, lend) — MV-9 "goty" bleed fix).
Known v1 kinetic quirks (post-layer, same tool — watch for them):
CASCADE fly-in transient (~200ms word overlap on multi-word CASCADE
lines, seen S04 28.76s / S19 ~136s, settles clean); S15 accent bar
grazes the dim "balls," baseline at 98.22s (cosmetic); SLAM words are
at 0 scale on the EXACT onset frame (60ms scale-in) — verify mid-event.

## FINAL ENCODE PLAN (MV-10 lessons: split encode, no single-pass OOM)
Split at the S12/S13 boundary (78.66s): half 1 = S01–S12 (1888f),
half 2 = S13–S23 (2250f). Video-only CRF-18 halves with kinetic burned
in, then mux halves + track audio re-encoded AAC 48k stereo (NEVER MP3
copy; apad capped whole_dur=172.417 + -t 172.42) + faststart. Gates on the
master: exactly 4138f; SEI crf=18.0; AAC codec (ffprobe); faststart;
mouth state at S07 word onsets by eye on the MASTER; motion audit;
whole-master eye review at every segment boundary (a spot-check pass is
NOT a whole-master pass).
Chat copy <=50 MB (bitrate cap, AAC copied) only if the house master
exceeds 50 MB.

## REBUILD-SPECIFIC DISCLOSURES (from the rebuild ledger — carry to delivery)
- S01: camera pushes tighter than the end ref (extreme duck close-up by
  9.5s); the S01→S02 cut goes tight-duck → wide-room (fresh start J01).
- S02: second vermilion towel invented on the right wall (world gains a
  prop); camera pans right + pushes in rather than rising.
- S03: eruption lags the 0.00 "Water" by ~1–2s (calm-chain lag — kinetic
  SLAM carries the hit); blue sink/counter edge creeps in at the left
  frame edge from 2.5s; column overshoots the end ref upward.
- S04: duck's eye renders reddish at frame 0; rim takes a pale blue cast
  in the second half; the planned "fresh crown" at 7.26 didn't distinctly
  appear — the rings carry 7–10s instead.
- S05: rim reads pale blue-white again (water's blue cast, never orange).
- S06: flashes read as one continuous gold wash rather than distinct
  per-beat pulses; the second towel from S02 is GONE (world reverted).
- S07 t2: push-in still goes past the bowl by ~3s (bowl out of frame 3–5s;
  duck visible at 2.0s); P1 onset closed-at-distance (line-start lag).
- S08: duck's beak reads open at the 9.5s surplus tail (trimmed out).
- S09: crowns read BIGGER than planned (tall column by 2.5s); first crown
  erupts ~1–2s after the 0.00 "Water" (SLAM carries it).
- S10: the duck DUPLICATES in the surplus tail (trimmed at 5.00s); the
  multi-arc ballet converges into one big arch by 4s; toilet seat up
  from 5.0s (background invention, trimmed out).
- S11 t4: camera sits low (water level) 4.5–5.0s, reaches the high wide
  only by 5.40s.
- S12: toilet-paper holder on the left wall (same prop as the end ref);
  faint second-bowl reflection in the tiles at frame 0 (artifact).
- S13 t2: bowl's own rings stay modest — multiplication reads as rings
  spreading onto the floor; the late "Water" burst (~6.74s) is a fresh
  ring, not a big eruption (SLAM carries it).
- S14 t2: column erupts ~2–3s after the "splashes" line (calm-chain lag,
  SLAM carries it).
- S15 t2: arc front-loaded (peaks ~2s, settles by 6–7s); take's own audio
  words run late (irrelevant — CUTAWAY).
- S16 t1: NO LITERAL FREEZE HOLD at the silence (~5.22s) — the crown keeps
  morphing through 5.0–5.5s; the peak reads as the hold and the shatter
  lands ~6s on the drop hit.
- S17 t1: duck briefly PARTIALLY CROPPED at the top frame edge at 2.0s
  (crest ride, not a camera move).
- S18 t1: wave front-loaded (peaks ~2s, rim stream by 7.5s); faint duck
  reflection on right-wall tiles 6–9s (one duck in the world).
- S19 t1: ring strobe clearest from ~4s (floor carries it; bowl rings
  subtle); gold pulse reads from ~6s; duck's faint tile reflection
  persists (one duck).
- S20 t1: duck rides ABOVE the top frame edge at 4.0–7.5s (out of frame
  entirely at 6.0s — crest ride; camera never leaves the wide, bowl fully
  visible; duck returns fully onto the crest for the arrival).
- S21 t2: duck mostly cropped at the top edge at 1.5s (crest-ride burst);
  lamp/window drift slightly 0–2.5s (gradual reframe, not a push-in).
- S22 t1: ONE near-still run, 32f @ 8.67–9.96s (during-words=False —
  eye-confirmed calm settle, not a freeze); crown fully down by ~4s, so
  ~6s of the slot plays as a calm hold under the outro stabs; morph
  reframes slightly toward the wider end ref 0–2s (completed by ~4s).
- S23 t1: ring blooms on the FLOOR puddle, not the bowl; a SECOND dome
  lamp appears top-left from ~2s (morph addition, persists); duck's beak
  renders open at 5.84s (painted beak, no audio claim — CUTAWAY).

## BUILD LOG
- 2026-11-10 ~06:13 EST: kinetic rebuilt into work/rebuild/assembly/ —
  33 lines / 125 words / 191 events, .ass + words json BYTE-IDENTICAL to
  v1's (diff clean). Rebuild pipeline scripts written (split_encode /
  mux / gate_master / motion_audit / chat_copy, all pointed at the rebuild
  assembly dir + rebuild master filename).
- Segment build RUNNING (started ~06:14 EST, backgrounded exec).
- Segments BUILT ~06:22 EST: all 23, total exactly 4138f (manifest
  work/rebuild/assembly/assembly_manifest_rebuild.json). Build took ~8 min.
- SPLIT ENCODE OK ~06:35 EST: half1 1888f / 53,599,729 B, half2 2250f /
  66,173,282 B; kinetic split 85 + 109 events (3 straddling, same as v1).
- MUX OK ~06:36 EST: masters/mv11_water_hit_my_balls_rebuild_16x9.mp4 —
  4138f, 124,037,454 B, md5 0b51559e483d7acdc69d9356a68fcb03.
- GATES — ALL PASS ~06:37 EST (work/rebuild/assembly/gate_master_rebuild.log):
  h264 1280x720 24fps, exactly 4138f, 172.417s, AAC 48k stereo, SEI crf=18.0,
  faststart moov@36 < mdat@120733, audio agreement min corr 0.9977 (>0.99).
  One fix applied: gate_master_rebuild.py's relative P resolved to work/
  (script lives in work/rebuild/) — hardcoded the project BASE path.
- CHAT COPY OK ~06:48 EST: masters/mv11_water_hit_my_balls_rebuild_16x9_50mb.mp4
  — 39,580,400 B (37.7 MB), 4138f, md5 84565a7518f1d136e5d956d8293808d2;
  audio-stream md5 identical to house (339ee5e99019926f9717f91bc53ac996).
- WHOLE-MASTER EYE REVIEW AT EVERY BOUNDARY — ALL 22 JOINTS PASS ~06:55 EST
  (frames work/rebuild/assembly/eye_joints/, 4 contact sheets):
  chained joints continuous (same framing, water state advancing):
  J02 J03 J04 J05 J07 J08 J11 J12 J13 J15 J16 J17 J18 J19 J20 J21 J22.
  Fresh cuts by design, all landing in the same world: J01 close->wide
  re-establish @9.00s; J06 verse entrance (man at the bowl) @45.18s;
  J09 reframe to wide arcs @60.26s; J10 dive underwater (duck-free start,
  the t4 redesign) @65.26s; J14 S15 eruption opening (water already rising)
  @94.66s. J07: the man's head drops after the verse — S08's own motion,
  same close profile. J22: final frame rhymes with S01's first.
- KINETIC SPOT CHECKS on the master (frames work/rebuild/assembly/
  eye_kinetic/): CASCADE ~200ms fly-in overlap present at both known spots
  (28.76s S04 + ~136s S19 — incoming word slides over the outgoing one for
  ~5 frames; all words stay legible; same disclosed v1 quirk, NOT a bleed).
  Final "Balls" SLAM clean at 171.20s — big "Balls" over the settled bowl,
  last drop spilling, floor rings; second dome lamp visible top-left
  (disclosed S23 morph addition).
- ASSEMBLY COMPLETE ~06:57 EST. NO commit, NO delivered flag (parent).

## S07 MOUTH GATE — PASS, NO RE-FIRE OWED (~06:24 EST)
Built segment frames (song times, all 6 DISTINCT md5s — no frozen repeats,
the v1 warp bug is absent): f0 45.18 "Sitting" onset: wide push-in head,
mouth unreadable at distance (disclosed line-start lag, MV-10 precedent);
f24 46.18 mid-P1: profile, mouth OPEN; f48 47.18 "Water" onset: mouth OPEN;
f65 47.89 mid-P2: mouth OPEN, distinct smaller shape; f83 48.64 "My balls"
onset: mouth OPEN, teeth-showing shape; f101 49.39 mid-P3: mouth WIDE OPEN
on "balls". Four distinct mouth shapes tracking the phrases; no onset
closed. The P1->P2 join (segment f47->f48, take f51->f57, 5-frame skip of
closed-mouth inter-phrase pause) reads continuous — same profile framing,
push-in underway; P2->P3 join (f82->f83, take f85->f86) is back-to-back
frames, continuous. Push-in still goes past the bowl by ~3s (bowl out of
frame from f48 on; rim visible at the bottom edge) — same disclosed shape
as v1 t3; the verse's staging holds for the first ~2.5s.
Frames: work/rebuild/assembly/eye_s07/ (f0/f24/f48/f65/f83/f101).
1. Write work/rebuild/assembly_build_rebuild.py — DONE next.
2. Build kinetic .ass (rebuild dir); diff against v1's .ass.
3. Build segments S01->S23 (checkpoint manifest after each).
4. Eye-check S07 segment (frames at song 45.18/47.18/48.64 + phrase mids,
   DISTINCT md5s first).
5. Split-encode halves; mux; gates; chat copy if needed; motion audit;
   whole-master eye review at every boundary.
6. Short final report to parent (master path/md5/ffprobe/gates/S07 verdict).
   NO commit. NO delivered flag (parent writes it).
