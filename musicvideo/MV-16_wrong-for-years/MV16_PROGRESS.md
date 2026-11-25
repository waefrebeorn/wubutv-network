# MV-16 Wrong for Years — PROGRESS

Intaked 2026-11-13 ~09:05 EST (user batch of 5 new tracks). track.mp4 md5 ff57f3211f8fb444eea96108a65d96ae, 183.200s. lyrics.txt = user sheet verbatim. Suno title: "Wrong for Years".
Build coordinator launching 2026-11-13 (parent). Full Slopcannon pipeline.

## Stage log
- 2026-11-13 ~09:06 EST — coordinator started. Skills read (slopcannon v2 incl. taste rules + EVENT rule + G7; visual-mv-forms; video-api-mastery). Event library + USED_EVENTS read. Track verified: md5 ff57f3211f8fb444eea96108a65d96ae, 183.200s, AAC 48k stereo. No mv16-build entry in heartbeat_whitelist.json yet (parent to create) — this file is the liveness record meanwhile.
- Stage 1 DONE: tempo MEASURED 150.0 BPM (period 0.400s, phase 0.208s; flux AC decisive). AUDIO_ANALYSIS.md written. Performed grid DONE: 354 ASR words → 97 performed lines, LYRIC_TIMELINE.md + work/analysis/grid_lines.json + work/swing/beat_grid.json. Performed extras found: 'Hey! Hey!' shout (C1 tail), C2 vocalise (oh-oh-oh)/(oh-uh-oh), FC doubles 'Nobody stopped me' in trios 1–2, bridge '(no,)' pickup.
- Stage 2 DONE: ASSET_BOARD.md + REFERENCE_STACK.md (9 refs generated, read back, QC-passed; GUY identity consistent across states A/B/C). SCENE_PLAN.md written: 28 scenes, distinct named event per slot, SCREEN gag staged as post karaoke-window HUD (never a second lyric set), frame 0 = ref_guy_pose peak.
- PILOT: t1 volley (S01/S05/S22) — all REJECT G1 style: rendered PHOTOREAL with wrong faces (vehicles carried no anime lock in text). Take-ASR proved word delivery: S01 exact 12/12 (G7 1.00), S22 exact 12/12 (G7 1.00), S05 G7 0.90 (wrote/rode homophone). FIX applied to ALL vehicles: "Anime illustration style, cel-shaded, flat colour with bold ink outlines — NOT photorealistic, not live-action" + anime character introductions (MV-15 v2 template). Pilot re-fired as t2 (S01/S05/S22) — QC in progress.
- NOTE 2026-11-13 ~09:40 EST: a compaction-garbled segment in coordinator context claimed t2 ASR results before the files existed; DISK VERIFICATION caught it (no t2 files/JSONs on disk). Disk is truth — t2s were then fired for real and verified on disk.

## 2026-11-13 ~10:45 EST — ALL VERDICTS FINAL (TAKE_HISTORY.md is the ledger of record)
- 47 takes fired at this checkpoint, 0 refusals, zero 429s. Ship map: 24 KEEP + 4
  chunk-reorder SALVAGE (S03/S11/S20/S26). 28/28 scenes verified
  from take-ASR JSONs read off disk.
  CORRECTION (conform stage, ~12:00 EST): S05 t2 was found at conform
  to sing the friends' lines over S05's belted-car span (generator
  drift; vehicle text was correct). S05 re-fired as t3
  (d2784618d45636fa372b46c2cd47d89f, 7,112,829 B) — correct lines,
  foreground-verified. FINAL COUNT: 48 takes fired; S05 SHIPS t3.
  TAKE_HISTORY.md carries the corrected rows.
- ASR persistence anomaly: background-chain tail files repeatedly
  "delivered" in logs without persisting; the final four
  (s21/s23/s27/s28 t2) were re-run one at a time in the foreground
  and file-verified. DISK IS TRUTH for every verdict.
- Events verified on frames: S09 peel 1 ✓, S18 peel 2 (gold jacket)
  ✓, S10 personal weather ✓, S13 blank wall ✓.
- NEXT: S04 shout-frame locate + S03/S26 event frames → conform →
  ASS (kinetic + SCREEN window + word chase + worn graphics) →
  house master + gates → chat copy → CUTLIST/GATE_LOG/VISUAL_GATE
  → USED_EVENTS append.

## 2026-11-13 ~13:12 EST — DELIVERED (parent pass)
- Coordinator 1f961e91 ended without a final report; parent recovered from disk.
- House master: masters/mv16_wrong_for_years_16x9.mp4, md5 8313d30a679a1bdd6c6adf96ec32ee10, 126,350,983 B — gates verified (183.208s vs track 183.200s, 4397f, 1280x720, 24fps, AAC 48k, x264 SEI crf=18.0; independent delivery-closing verification + parent md5/ffprobe).
- Chat copy: masters/mv16_wrong_for_years_16x9_chat.mp4, md5 08d2da30025a65f441cc7e914d169803, 44,362,602 B, 183.208s, AAC — delivered in chat.
- Ledger final: 48 takes fired, S05 ships t3; USED_EVENTS appended (S24–S28 rows on file).
- Disclosure: coordinator did not leave a GATE_LOG or a recorded master-audio agreement figure for the final encode; encode gates above were parent/nag-verified from the file itself.

## 2026-11-13 — REBUILD on the correct take (user correction ~13:22 EST)
- The delivered build above was SUPERSEDED: the intake track was the
  wrong Suno take ("bad music energy", same song). Correct take
  installed as track.mp4 (md5 e4649643f510cf453ec5008ec4e24489,
  198.016s; wrong take preserved as track_wrongtake.* and
  masters/*_wrongtake.mp4 — never deliver). Delivered flag renamed
  MV16_DELIVERED.flag.superseded-wrongtake-20261113.
- Rebuild coordinator 83770097: archived build-1 analysis under
  work/analysis/wrongtake/ + work/rebuild/; measured the new take
  (150.0 BPM — same tempo, different performance); ASR 314 words →
  new performed grid, 86 lines (work/analysis/grid_lines.json via
  build_grid2.py, hand-verified with no-penalty window decodes);
  verified only S22 (BR) and S28 (OUT) changed content; re-fired
  both (vehicles *_rb.txt) — takes landed ~14:01 EST, take ASR
  completed. DIED ~14:07 EST (transport: sqlx pool timeout).
- Recovery coordinator ae4db7d3 (parent-spawned): finished G7
  (S22 t3 = 1.00, S28 t3 = 0.857, both PASS; S05-drift re-check on
  the new grid clean — s06_t2 sings the friends' lines on S06,
  s05_t3 sings the car lines on S05); derived the new 28-slot scene
  map (work/analysis/make_scene_map_rb.py — build 1's midpoint rule,
  POST→V2 pocket to S13's tail as in build 1); re-conformed all 28
  slots (conform_rb.py; 4752f exact; every sung-word chunk within
  0.541×–2.86×, floor 0.5× never breached); rebuilt the kinetic ASS
  on the new grid (build_ass_rb.py, 1,404 events); assembled;
  motion probe caught a frozen S28 tail (take motion dies ~8.5s) —
  fixed (live-span tail-A + zoompan push-in tail-B) and re-assembled
  before delivery.
- REBUILD MASTER: masters/mv16_wrong_for_years_16x9.mp4, md5
  e9a64e89395534c74729f164ae19e76a, 129,048,899 B — 4752f, 198.016s,
  1280×720, 24fps, AAC 48k, x264 SEI crf=18.0, faststart.
  AUDIO AGREEMENT (recorded this time): overall corr 0.99812,
  min 5s-window 0.99736 vs track.mp3.
- Chat copy: masters/mv16_wrong_for_years_16x9_chat.mp4, md5
  df499a542daec3edaba6b65a028159bd, 45,292,507 B, AAC copied.
- Full record: GATE_LOG.md + CUTLIST.md (rebuild). USED_EVENTS
  verified — build 1's MV-16 block already lists all 28 events;
  the rebuild adds none (no duplicates). No delivered flag, no
  commit — parent owns both.
