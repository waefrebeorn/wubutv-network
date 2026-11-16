# MV-11 "Water hit my balls" — ASSEMBLY PROGRESS

## 2026-11-10 ~00:38 EST — assembly coordinator start
- Inputs verified: track.mp4 md5 18273d7a593e623b720105df195bede2 (audio
  172.400s); all 23 KEEP-take md5s match TAKE_LEDGER.md (S04 filename
  confirmed on disk — earlier check typo, real file matches). All takes
  1248x704 24fps.
- Contracts written: work/assembly_notes.md — 23 scenes, 4138f total,
  S07 phrase warps 1.02x/1.25x/1.38x (all < 2x cap), everything else a
  trim or a gentle uniform slowdown <=1.09x.
- Kinetic plan: SLAM hooks, HIGHLIGHT verse/splash lines, CASCADE patter;
  S17 no kinetic (loop zone, no measurable words); S16 Water slam only
  (BALLS! unmeasured); outro Balls 170.92 added (turbo-measured, post-plan).
- NEXT: build_kinetic.py + assembly_build.py, then segments.
- Kinetic built 2026-11-10 ~00:51 EST: 33 lines, 125 words, 191 events
  (work/assembly/mv11_kinetic.ass + mv11_kinetic_words.json). Two lyric
  corrections caught at build: "all"->"on" 35.84, "Splashes"->"Splash" 94.88.
- Segments: S01 (216f) + S07 (119f) built frame-exact ~00:51 EST; full
  build running. S07 mouth gate PASS (see assembly_notes.md): "Water"
  47.18 + "My balls" 48.64 both OPEN on the built segment; "Sitting"
  45.18 unreadable at distance (disclosed line-start lag), open by
  mid-phrase.
- ALL 23 segments built ~01:00 EST: exactly 4138f (manifest
  work/assembly/assembly_manifest.json). S07 119f, S16 221f, S21 97f,
  S23 177f — all contract-exact. NEXT: split encode halves + mux.

## S07 WARP BUG — FOUND BY MOTION AUDIT ON MASTER #1, FIXED (~01:35 EST)
- Master #1 (md5 891fe032...): ALL GATES PASS, chat copy OK (38.1 MB) — but the
  motion audit found ONE near-still run >=12f: 63f @ 47.21-49.79s (S07 P2/P3).
- Root cause: assembly_build.py warp chain `trim=...,setpts={f}*PTS,fps=24`
  — ffmpeg's fps filter starts its output clock at t=0 for a trim starting
  at a non-zero frame, zero-filling the head with repeats of the first frame.
  Shipped S07 was P1 (correct) + 35x take-frame-52 + 6 real P2 frames; P3
  never appeared. The first "mouth gate PASS" was VOID (same frozen frame
  read 4x). Lesson: verify sampled frames are DISTINCT (md5) before reading.
- FIX: `setpts=PTS-STARTPTS` before scaling. Isolated P2 test: 35f, mean 5.50.
- REBUILT S07 (md5 f43552119f0e...): 119f; P1 9.21 / P2 6.15 / P3 3.73, 0 frozen.
- RE-RUN MOUTH GATE (6 distinct frames): f48 47.18 "Water" WIDE OPEN;
  f65 47.89 mid-P2 OPEN different shape; f83 48.64 "My balls" teeth-showing
  distinct shape; f101 49.39 mid-P3 mouth nearly closed (take's own consonant
  articulation, opens again by take 4.5). PASS for real. No re-fire owed.
- Re-encode in progress (split_encode -> mux -> gates -> chat copy ->
  motion audit -> master eye frames). Master #1 + chat copy #1 SUPERSEDED.

## MASTER EYE READS (master #1, non-S07 scenes — unchanged by the fix)
- f0 S01 opening: crown bloomed, bone-white rim, duck right, lamp gold, bug on.
- f330 S03 start (13.76 "Water" SLAM onset): anchor-still head (same still as
  f0, documented pattern); NO kinetic text visible AT the exact onset frame
  — SLAM fade-in; verify mid-SLAM on master #2 (f336 14.0s, f3692 153.85s).
- f2568 S16 107.0s drop: duck mid-air, water exploding, room flashing — reads.
- f2639 S16 109.96s: duck at top of arc by window, column beneath, gold flash.
- f3686 S21 153.60 peak: huge crown/column, duck on top, lamp blazing, bone
  white rim; no SLAM text AT the exact onset frame (same fade-in question).
- f4137 last frame: duck centred on calm glass water, reflection showing,
  "Balls" kinetic + accent bar visible, bug on — S23 rhymes with S01. PASS.

## MASTER #2 — DONE, ALL GATES PASS (~02:00 EST)
- House master md5 c1317938b170f5154f8d9886d8952a1d, 134,718,102 B, 4138f,
  172.417s. Chat copy md5 de4a44e05f60b0c07f1ac73dc331611f, 39,954,473 B,
  audio md5 identical to house. Motion audit PASS (0 near-still runs).
  S07 mouth gate PASS (segment + master). Full-master watch: 23/23 scene
  midpoints correct, SLAMs verified (14.00 / 110.90 / 153.85), S07 fix
  confirmed in the master. Master #1 SUPERSEDED (S07 warp bug).
- Disclosed flaws: S07 "Sitting" onset mouth unreadable at distance
  (line-start lag); S07 mid-"balls" mouth nearly closes (take's own
  articulation); CASCADE 200ms fly-in overlap transient (S04/S19);
  S15 accent bar grazes dim "balls," baseline; S06/S09/S13 rim warmth
  near lamp; S22 tiles amber-orange from ~5s (ledger-disclosed);
  S10 tail front-facing open-beak duck close-up (ledger option);
  anchor-still heads on S01/S03/S06/S13/S14/S15/S16; 0.0167s video
  overhang; final "Balls" SLAM tail truncated by video end (no defect).
- ASSEMBLY COMPLETE. Ready for parent delivery. Do NOT commit.
