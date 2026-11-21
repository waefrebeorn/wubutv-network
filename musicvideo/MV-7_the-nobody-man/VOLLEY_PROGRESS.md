# MV-7 — VOLLEY PROGRESS

## Volley 1 (2026-11-06, coordinator run 1) — BLOCKED at first fire

Plan: S07 HOOK TEST first → QC → openings S01, S02, S03, S04, S05 (cap 6).

- **S07 t1: GENERATION CALL FAILED — media tool internal error (HTTP
  500, "An unexpected error occurred").** No video file landed in
  takes/ (only the request sidecar JSON). Outcome of the request is
  unknown downstream; per the failure directive the S07 request was
  NOT retried in this run.
- Because the hook test never returned a take, the plan's look is
  UNPROVEN, so the remaining volley-1 fires (S01–S05) were held rather
  than spent on an unproven look — their vehicle files are written
  and ready (mv7_s01…s05_vehicle.txt, mv7_s07_vehicle.txt).

## Done this run (Stages 1–3 complete)
- Stage 1: SONG_WORDS.json (small pass on 16kHz decode, 330 words),
  LYRIC_TIMELINE.md (performed order measured — hook chant opens the
  song), AUDIO_NOTES_MV7.md, work/beat_grid.json (103.36 BPM).
- Stage 2: ASSET_BOARD.md, POSE_CARDS.md, canonical still banked
  (refs/nobody_man_canonical.webp, md5 638432345335134d825c9f9d4e54edd6,
  read back, identity PASS).
- Stage 3: MV_PREPRO_MV-7.md — 24 scenes, banger test passes on paper.

## Volley 1 (2026-11-06, coordinator run 2) — BLOCKED again at the S07 re-fire

- **S07 t2: VERBATIM RE-FIRE FAILED — same media tool internal error
  (HTTP 500, "An unexpected error occurred", origin stage "safety").
  No video file landed in takes/.** The vehicle and canonical-still
  arguments were byte-identical to the run-1 fire (entries copied
  verbatim from mv7_s07_vehicle.txt).
- Per the run-2 directive, firing stopped here: no variants improvised,
  and S01–S05 were NOT fired because the plan's look is still UNPROVEN
  (the chorus-hook test gate). All six vehicle files remain written and
  ready (mv7_s01…s05_vehicle.txt, mv7_s07_vehicle.txt).
- Blocker is tool-side, not prompt-side: two identical 500s across two
  runs, both at the same call. Generation cap used this run: 1 call,
  0 takes.

## Volley 1 (2026-11-06, coordinator run 3) — BLOCKED a third time at the S07 re-fire

- **S07 t3: VERBATIM RE-FIRE FAILED — identical signature to t1/t2:
  HTTP 500, "An unexpected error occurred", origin stage "safety",
  failure_kind "safety_service_unavailable", generated_attachment_count
  0. No video file landed in takes/** (sidecar:
  media-generation-mv7-s07-t3-1793989352.json, attempt_id
  50bdcc79-8197-447a-b598-5e536c36776e). User said "continue"; the
  retry was fired once and failed the same way.
- Three identical safety-stage 500s across three runs (t1, t2, t3) —
  provider-side safety service outage, NOT a content rejection and
  NOT a prompt problem. Root cause is known tool-side
  ("root_cause_known": true, "source_retryable": false).
- Per the run-3 directive, firing stopped immediately: no repeated
  retries, no variants improvised, and S01–S05 were NOT fired (the
  chorus-hook test gate still holds — the plan's look remains
  UNPROVEN). Generation cap used this run: 1 call, 0 takes.

## Volley 1 (2026-11-06, coordinator run 4 — RECOVERY) — hook test PASSES, S01–S05 fired

Generator back (Q4 15:45 EST fired 7 videos). S07 v2 hook test fired FIRST from
redesign_v2/vehicles/mv7v2_s07_vehicle.txt verbatim + Era A still:
- **S07 t1 (v2): KEEP-WITH-FLAG — PASSES.** md5 9f9a41cdea6d746387de655175b8729e, 10.000s,
  1152x768 (3:2 — still is 1920x1280, aspect followed the image; crop at assembly).
  19/19 words exact, ratio 0.944, frame rule mean_diff 1.729 / run 0f. G1–G6 all PASS.
  The v2 look is PROVEN. QC: work/qc_v7/mv7_s07_t1_QC.md
- Hook gate passed, so S01–S05 fired in the same run (cap 6/6 used):
  - **S01 t1: REJECT** (md5 3f29a5e8670a91865af44059e14eb68f) — sings full chant x3, silent 7.2–10s
    while the song chants to 9.46s; performed chant elides "I'm the" after the first phrase
    (full-pass + split-half agree). Reroll axis: LYRIC-AS-PERFORMED v3 vehicle.
  - **S02 t1: KEEP-WITH-FLAG** (md5 56838020652558bbd07c3d3ec6539e92) — 8/8 words, ratio 1.235,
    frame rule 1.180 / run 2f. Flags: 3:2 raster; one extra "the" in 2nd chant (micro).
  - **S03 t1: KEEP-WITH-FLAG** (md5 bdbe8d744976861cc3f9c45dfe1c4e43) — 22/22 words, frame rule
    1.888 / run 0f. Flag: grey ratio 0.764 (warp-rescue 1.047x); 3:2 raster.
  - **S04 t1: KEEP-WITH-FLAG** (md5 23933f5a065ac2ef1e27eea4e297e941) — 24/24 words, frame rule
    1.427 / run 0f. Flag: grey ratio 0.744 (warp-rescue 1.075x); 3:2 raster.
  - **S05 t1: REJECT** (md5 22c5cd650e508075b5fc112e02c658c6) — ratio 0.548 CLEAR MISS
    (13 words over 8.36s vs 4.58s slot). Reroll axis: PACING (brisk 0.5–5.0s window).
- All six takes 1152x768 (Era A still is 3:2; aspect follows the image despite "16:9" in the
  vehicle text — assembly crops to 16:9; same class as MV-6 S16).
- KEEP pool: S02, S03, S04, S07. Full QC rows: work/qc_v7/mv7_s0{1,2,3,4,5,7}_t1_QC.md.

## Volley 2 (2026-11-06, coordinator run 5 — RECOVERY) — S01 reroll + S05 reroll + S06, S08–S10

Generator still back (0 provider errors across 6 fires, cap 6/6 used). Two new v2 vehicles written first
(redesign_v2/vehicles/mv7v2_s01_v3_vehicle.txt — elided chant; mv7v2_s05_v2_vehicle.txt — brisk 0.5–5.0s).
- **S01 t2 (v3): REJECT** (md5 d6ffd61f7659fbe84d2a4ea6de0ba2f9) — elided chant x5 asked, take delivers 3 of 5 (0–6.2s),
  silent 6.5–10s (RMS-confirmed); ratio 1.526 grey. Two pulls, both exactly 3 occurrences — model caps this chant at ~3.
  Reroll axis: COMPLETENESS (explicit "five times, count each repeat").
- **S05 t2 (v2): REJECT** (md5 ca22497ecb174eb0d45b69bea19fd456) — ratio 0.565 CLEAR MISS (13 words over 8.10s vs 4.58s slot).
  Brisk window moved pace 8.36s → 8.10s only — two pulls, same ~8s floor. Reroll axis: SPLIT (PC1.1 / PC1.2 separate takes).
- **S06 t1: KEEP-WITH-FLAG** (md5 b27f6c4c4a5dba8749cdbcaf322974c0) — 10/10 words exact, ratio 0.884, frame rule 1.377 / run 0f.
  First spark DOES appear (~4s, red dot on wall). Flags: 3:2 raster; sings 0.00–8.60 vs window; slow rightward drift, face near right edge by tail.
- **S08 t1: REJECT** (md5 b1a0b44ce3656029c78f186d7518f691) — delivers C1.5–C1.6 only, C1.7 hook phrase MISSING; silent 7.5–10s
  (RMS-confirmed). Ratio 1.036 in band on delivered words. Reroll axis: COMPLETENESS (name all three lines, finish on the hook).
- **S09 t1: REJECT** (md5 35717edfb9089a9a1921ceebad8c32ef) — ratio 0.426 CLEAR MISS (4 words over 7.66s vs 3.26s word span).
  Frame rule strongest of the volley (3.311 / run 0f); sparks visibly burst at frame right. Reroll axis: PACING (brisk 0.5–4.5s).
- **S10 t1: KEEP-WITH-FLAG** (md5 642211b3966a3887f4d1ea820a92d62b) — 6/6 words; measured song chants the tag x3, NOT the timeline's
  inferred x4 — take matches the measured lyric exactly. Ratio 0.641 grey (warp-rescue ~1.56x, disclose); rhythm caveat: song's
  measured C1.T word times uneven vs take's even rhythm — assembly re-measures. Flags: 3:2 raster; red light wash last ~2s (post-vocal).
- All six takes 1152x768 (Era A still is 3:2; aspect follows the image despite "16:9" in the vehicle text — assembly crops to 16:9).
- KEEP pool: S02, S03, S04, S06, S07, S10. Full QC rows: work/qc_v7/mv7_s0{1_t2,5_t2,6_t1,8_t1,9_t1,10_t1}_QC.md.

## Volley 3 (2026-11-06, coordinator run 6 — RECOVERY) — S01 v4 + S05 SPLIT + S08 v2 + S09 v2 + S11

Generator still back (0 provider errors across 6 fires, cap 6/6 used). Five new vehicles written first
(redesign_v2/vehicles/mv7v2_s01_v4_vehicle.txt — explicit count; mv7v2_s05_v3a_vehicle.txt + mv7v2_s05_v3b_vehicle.txt —
PC1.1 / PC1.2 split; mv7v2_s08_v2_vehicle.txt — completeness; mv7v2_s09_v2_vehicle.txt — brisk 0.5–4.5s).
S11 fired verbatim from its v2 vehicle + Era B still. S12 held to volley 4 (the S05 split is two fires, so S11 is the sixth).
- **S01 t3 (v4): REJECT — S01 is STRUCTURAL** (md5 9f8d2c3b8fdddac9c09ed92edf0aec3b) — the explicit-count vehicle BACKFIRES:
  the model literally sings the count words ("nobody man three", "nobody man four" p=0.954); 4 of 5 occurrences, fifth absent
  (tail split-half 0 words, RMS tail is non-vocal bed). Three pulls, three failure modes (t1 full x3 + silent; t2 elided x3 +
  silent; t3 count-words + no fifth) — the completeness axis is exhausted, NO v5. Structural treatment: split the chant across
  two takes (S01a = t2's clean first 3 occurrences; S01b = last 2 via fresh restage or montage cover), assembly's call.
- **S05 t3a (v3a): KEEP-WITH-FLAG** (md5 0181fd7e25c2de8af39314ec4cc3dc5e) — PC1.1 6/6 words exact, frame rule 1.189 / run 0f.
  Flag: ratio 0.502 (assembly warp ~1.9x uniform squeeze, disclose, at the MV-5 v4 extreme).
- **S05 t3b (v3b): REJECT** (md5 223844bc5b180bc9df91d14eadf22625) — PC1.2 7/7 words exact BUT ratio 0.299 CLEAR MISS; first phrase
  needs 3.38x speedup (beyond warp-rescue 1.5x and the MV-5 v4 extreme 1.91x); 1.90s mid-line pause; brisk did not move the pace
  (1.0s/word). Reroll axis: PACING-COMPRESSION v4 (tighter 0.5–3.5s window, "in one breath, no pause").
- **S08 t2 (v2): KEEP-WITH-FLAG** (md5 c04f5f46cfd67c05352289a303711c0c) — all three lines in order, finishes on the hook; ratio 0.855
  in band, frame rule 1.638 / run 3f. Flags: hook lead word ambiguous ("the" p=0.527 vs performed "I'm" — mouth OPEN at the 7.6s
  onset, adjudicated probable mishear); C1.6 "flicking" 2.18s near-silent drawl, mouth near-closed at 5.0s; per-phrase warps at cap
  edges (1.76x/1.77x/0.55x). FIRST TRUE 16:9 take of the project (1280x720, no crop).
- **S09 t2 (v2): KEEP-WITH-FLAG** (md5 68a47b6e724cda3f2dfb1d61686a131d) — 4/4 words exact, ratio 0.635 grey (warp-rescue ~1.57x),
  frame rule 4.681 / run 0f (strongest of the volley); sparks visibly burst at frame right. TRUE 16:9 (1280x720, no crop).
  Brisk moved pace 7.66s → 6.42s. The S09 pacing axis is closed.
- **S11 t1 (v2): KEEP-WITH-FLAG** (md5 b90cc69e5c58f73e6cc698586de57871) — 22/22 words exact ("joins" + "low-lit" heard correctly),
  ratio 0.775 grey (warp-rescue ~1.29x), frame rule 1.108 / run 0f. Era B state CORRECT (half-burned candle, cork strip, stacks).
  Flags: 1248x704 raster (assembly crops/pads); wider desk-lean framing vs Era A MCU. Era B is OPEN and proven on first fire.
- KEEP pool: S02, S03, S04, S05a, S06, S07, S08, S09, S10, S11. Full QC rows: work/qc_v7/mv7_s{01_t3,05_t3a,05_t3b,08_t2,09_t2,11_t1}_QC.md.

## Volley 4 (2026-11-06, coordinator run 7 — RECOVERY) — S05b v4 + S12–S16

Generator still back (0 provider errors across 6 fires, cap 6/6 used). S05b v4 vehicle written first
(redesign_v2/vehicles/mv7v2_s05_v4_vehicle.txt — pacing-compression, tighter 0.5–3.5s window, "in one breath,
no pause between words"). S12–S16 fired verbatim from their v2 vehicles + Era B still.
- **S05 t4 (v4): KEEP-WITH-FLAG** (md5 ac262c73da22068be632a47f1eabc851) — PC1.2 7/7 words exact, once, in order;
  NO mid-line pause (RMS continuous 0–5.3s — the "in one breath" axis worked; t3b had a 1.90s pause).
  Frame rule 1.659 / run 0f. Flag: ratio 0.395 — assembly warp 2.53x uniform squeeze, the FASTEST in the build,
  beyond the MV-5 v4 extreme (1.91x); take line 5.32s is UNDER the brief's ~6s structural threshold, so PC1.2
  is covered and the pacing-compression axis is CLOSED (no v5). Other flags: 1152x768 raster; "I" 1.10s drawl
  (p=0.478); slow rightward camera drift.
- **S12 t1 (v2): REJECT** (md5 13c8cd48372fab4c6470bca897247831) — V2.4 wrong ("one more zoom" replaced by
  "chasing that giant shout"); V2.6 "I got a small flame I won't put out" ENTIRELY MISSING; "chasing that
  giant shout" repeats (repeat defect). 13/21 words. Ratio 0.87 in band but coverage fails. Visuals PASS
  (Era B correct, frame rule 1.076 / run 0f). Reroll axis: COMPLETENESS v2 — all three lines, V2.6 must land.
- **S13 t1 (v2): REJECT** (md5 1585b73d8927540b7e38624def55b2dc) — PC2.1 wrong: "I kept clicking" MISSING,
  "Little by little" invented at line 1 and repeated in line 2 (repeat defect); PC2.2 exact. Ratio 0.657 grey
  but content fails. Visuals PASS (Era B correct, frame rule 1.794 / run 0f, push-in). Reroll axis: PC2.1 WORD
  ACCURACY v2 — "I kept clicking" must land. Same forward-bleed pattern as S12 (a later phrase pulled into an
  earlier slot).
- **S14 t1 (v2): KEEP-WITH-FLAG** (md5 2043def7f8a057f53465d4aba34d1000) — 15/15 words exact, once, in order;
  ratio 1.017 in band; frame rule 2.639 / run 0f (strongest of the volley); wall sparks stir in the tail as
  vehicled. Flags: 1248x704 raster; sings 0.00–8.02 vs 0.5–9.5s window; push-in framing.
- **S15 t1 (v2): REJECT** (md5 432a95e2a70d7dada1a98752923b2dd4) — C2.1–C2.3 exact (15 words) but final C2.4
  "I'm The Nobody Man" MISSING (song has 19 words in C2); model stops after "I post again". Ratio 1.047 in
  band on delivered words but coverage fails. Visuals PASS (Era B correct, frame rule 1.989 / run 0f, push-in).
  Reroll axis: COMPLETENESS v2 — final chant must land (same axis that fixed S08 t1 → t2 in volley 3).
- **S16 t1 (v2): KEEP-WITH-FLAG** (md5 9020aead4540165246264240a459c6b3) — 10/10 words exact per vehicle; ratio
  0.657 grey (warp-rescue ~1.52x, at cap edge); frame rule 1.733 / run 0f; sparks thick behind him in the tail.
  Flags: 1248x704 raster; "flicking" 1.92s drawl (p=0.79); SONG_WORDS heard "spots/Flipping" vs vehicle
  "sparks/flicking" — caption adjudication owed at assembly.
- KEEP pool: S02, S03, S04, S05a, S05b, S06, S07, S08, S09, S10, S11, S14, S16. Full QC rows:
  work/qc_v7/mv7_s{05_t4,12_t1,13_t1,14_t1,15_t1,16_t1}_QC.md.
- Raster note: S12–S16 all returned 1248x704 (~16:9, assembly crops/pads); S08/S09 t2 were true 1280x720,
  so the Era B stills return near-16:9 but not exact. S05 t4 stayed 1152x768 (Era A, 3:2).

## Volley 5 (2026-11-06, coordinator run 8 — RECOVERY) — S12/S13/S15 v2 rerolls + S17–S19 t1

Generator still back (0 provider errors across 6 fires, cap 6/6 used). Three new v2 vehicles written first
(redesign_v2/vehicles/mv7v2_s12_v2_vehicle.txt + mv7v2_s13_v2_vehicle.txt + mv7v2_s15_v2_vehicle.txt —
completeness / word-accuracy axes; format-checked E1 63/64/67, E3 70/69/68, exactly 3 negatives, lyric
stated once; committed fadb2c32 before firing). S17–S19 fired verbatim from their v2 vehicles + Era B still.
- **S12 t2 (v2): KEEP-WITH-FLAG** (md5 383a843492b1c954c08b2c6737a65f27) — 21/21 words exact, once, in order;
  V2.6 "small flame" lands, no forward-bleed, no repeat. Ratio 0.733 grey (V2.4 warp ~1.45x, inside the
  1.5x rescue cap); frame rule 1.161 / run 0f; hand near the flame in the tail. Completeness axis CLOSED.
- **S13 t2 (v2): KEEP-WITH-FLAG** (md5 81933ac4945039cbe0411099bd854103) — 13/13 words exact, once, in
  order; "I kept clicking" lands, "Little by little" only in line 2. Ratio 0.599 — a hair below the 0.60
  grey floor; assembly squeeze ~1.67x (PC2.2 1.92x) disclosed — beyond the 1.5x warp-rescue cap but inside
  the build's accepted extremes (S05 t4 kept at 2.53x); the take is word-perfect and the miss is uniform
  slow delivery, not a structural floor. Frame rule 1.518 / run 0f. Word-accuracy axis CLOSED.
- **S15 t2 (v2): REJECT — S15 is STRUCTURAL** (md5 43426ec08cbe01f83c5316d1ea37df09) — C2.1–C2.3 exact
  (15 words) but the final C2.4 chant MISSING again; full pass + 5–10s tail split-half agree. Two pulls,
  identical drop point — NO v3, per the two-denied-rerolls rule. Assembly treatment: beat-cut to montage
  for exactly the C2.4 span (110.36–112.86s), back at C2.5 (S16 t1). The hook still lands twice in the
  chorus tail (S17 covers C2.7–C2.8).
- **S17 t1 (v2): KEEP-WITH-FLAG** (md5 5440c92c4aba9d1fffd69e0f72d41568) — 6/6 words exact, once, in
  order (C2.7 + C2.8); ratio 0.734 grey (C2.7 warp ~1.43x); frame rule 2.341 / run 0f. Flags: eyes closed
  through much of the take; slow push-in drift; 0.94s inter-line gap warps out.
- **S18 t1 (v2): KEEP-WITH-FLAG** (md5 6bcdda44b63145084136ffcac40fcfb3) — bridge montage plate, 0 words
  as vehicled, NO face anywhere; keyboard + receipt pinning + abstract monitor feed + candle hold all land.
  Frame rule 11.351 mean / 20f near-dup run (candle tail hold, under the 24f gate). G2 verified at FULL
  RES (slips illegible, monitor abstract); dollar-bill prop on the cork strip noted (set dressing).
  NOT a mouth-sung slot.
- **S19 t1 (v2): KEEP-WITH-FLAG** (md5 15aade7b9bb5933b1b0190e974ff96f3) — bridge montage plate, overhead
  desk + flame carried + face settles still/silent as vehicled. "I" p=0.004 adjudicated hallucination
  (RMS silent) — effective 0 words. Frame rule 4.650 / run 2f. NOT a mouth-sung slot.
- All six takes 1248x704 (Era B near-16:9, assembly crops/pads), 24fps, 10.000s exact.
- KEEP pool: S02, S03, S04, S05a, S05b, S06, S07, S08, S09, S10, S11, S12, S13, S14, S16, S17, S18, S19 (18).
  Full QC rows: work/qc_v7/mv7_s{12_t2,13_t2,15_t2,17_t1,18_t1,19_t1}_QC.md.
- Volley-wide note: slow push-in drift across the Era B singing takes (S12/S13/S15/S17 framing tightens
  medium → close-up) — assembly trims/crops; not a reject on its own.

## Volley 6 (2026-11-06, coordinator run 9) — S20–S24 t1 (Era C, Final Chorus)

Generator still back (0 provider errors across 5 fires, cap 5/5 used). All five fired verbatim from their
v2 vehicles + Era C still. All five takes 1152x768 (Era C still is 3:2; aspect follows the image — assembly
crops to 16:9), 24fps, 10.000s exact.
- **S20 t1 (v2): REJECT** (md5 57a53cf02c1f3d7126660294ad82b18c) — FC.1–FC.3 exact (15 words) but final FC.4
  "I'm The Nobody Man" MISSING; full pass + 5–10s tail split-half agree (tail RMS ~0.006 = silent). Ratio 0.87
  in band on delivered words but coverage fails. Visuals PASS (Era C correct, frame rule 2.667 / run 0f).
  Reroll axis: COMPLETENESS v2 — name all four lines, finish on the hook.
- **S21 t1 (v2): KEEP-WITH-FLAG** (md5 8ffb5f4aa5dea56951e83ddd2e54d543) — 14/14 words exact, once, in order
  (FC.5–FC.7); ratio 0.773 grey (warp-rescue ~1.29x); frame rule 2.329 / run 0f. Flags: "flicking" 1.92s
  drawl (S16 class); eyes closed through much of the tail; red/pink light wash last ~2s (post-vocal);
  slow push-in drift.
- **S22 t1 (v2): KEEP-WITH-FLAG** (md5 6ed121aeb20750219f000797e9848e39) — 6/6 words exact, once, in order
  (FC.8 + FC.9); ratio 1.082 in band; frame rule 2.676 / run 0f. ONE BRIGHTER LIGHT READS — one steady
  bright square in the wall, right of his head, across the tiles. The visual peak lands. Flags: 1.1s
  inter-line gap warps out; slow push-in drift.
- **S23 t1 (v2): KEEP-WITH-FLAG** (md5 c07abd209f4836ed00cdef346882f615) — 7/7 words exact, once, in order
  (FC.10); ratio 0.779 grey (warp-rescue ~1.28x); frame rule 2.267 / run 0f. FC.10 LYRIC RESOLVED: the take
  sings the sheet line ("Yeah, I turn the small things grand") — the LYRIC_TIMELINE [uncertain] flag is
  CLOSED in favor of the sheet; caption = sheet, no ear check owed at assembly. Flags: strong blue/purple
  face wash from ~4s; eyes closed in several late frames; slow push-in drift.
- **S24 t1 (v2): REJECT** (md5 de3d132ba3598dc8c2d336410c57a453) — lyric-as-performed mismatch: the take sings
  "I'm The Nobody Man, Nobody Man" ×2 (12 words); the MEASURED song is "I'm The Nobody Man, Nobody Man,
  Nobody Man" (8 words — "I'm" ×1, "Nobody Man" ×2; SONG_WORDS.json 173.30–183.24). The timeline's "×~3"
  was [inferred] and wrong — the vehicle over-asked. The take's second "I'm" lands on the song's "Nobody
  Man" (word mismatch), and the first-pair warp would be 2.66x slow (past the 2x cap). Visuals PASS —
  pull-back + frame rhyme land, frame rule 3.605 / run 0f (strongest of the volley). Reroll axis:
  LYRIC-AS-PERFORMED v2 — the measured 8-word chant, stated once.
- KEEP pool: S02, S03, S04, S05a, S05b, S06, S07, S08, S09, S10, S11, S12, S13, S14, S16, S17, S18, S19,
  S21, S22, S23 (21). Full QC rows: work/qc_v7/mv7_s{20,21,22,23,24}_t1_QC.md.
- Volley-wide note: slow push-in drift across ALL FIVE Era C singing takes (medium → close-up) — the same
  drift class as the Era B volley-5 takes; assembly trims/crops, not a reject on its own. Era C raster is
  1152x768 throughout (the Era C still is 3:2), unlike Era B's 1248x704.

## Next volley owes
1. Volley 7 (2 fires): S20 v2 (completeness — FC.4 must land) + S24 v2 (lyric-as-performed — the measured
   8-word chant "I'm The Nobody Man, Nobody Man, Nobody Man").
2. S01 stays STRUCTURAL (assembly restage, no fire). S15 stays STRUCTURAL (montage cover for C2.4 at
   assembly, no fire).
3. After volley 7: all 24 scenes covered (21 KEEP + S20/S24 rerolls + S01/S15 structural + S05a/S05b split)
   — assembly next.

## Next volley owes
1. Volley 6 (5 fires, Era C): S20, S21, S22, S23, S24 — fire verbatim from their v2 vehicles + Era C still
   (S22 holds the one brighter light; S24 is the frame rhyme, slow pull-back).
2. S01 stays STRUCTURAL (assembly restage, no fire). S15 stays STRUCTURAL (montage cover for C2.4 at
   assembly, no fire).
3. After volley 6: all 24 scenes covered (18 KEEP + S01/S15 structural + S05a/S05b split) — assembly next.

## Next volley owes
1. Rerolls (3 fires): S12 v2 (completeness — V2.6 "small flame" must land), S13 v2 (PC2.1 word accuracy —
   "I kept clicking" must land), S15 v2 (completeness — final C2.4 chant must land).
2. Then scenes S17, S18, S19 in plan order (Era B; S18/S19 are the bridge montage vehicles, no singing face).
   A volley of the 3 rerolls + S17 + S18 + S19 = 6 fits the cap.
3. S01 is STRUCTURAL — no further S01 generation. The split-chant restage (S01a/S01b vehicles) or montage cover
   is an ASSEMBLY decision, not a volley-5 fire, unless the parent orders the restage vehicles.
4. After volley 5: S20–S24 remain (Era C; S22 is the one brighter light, S24 the frame rhyme) — volley 6.

## Volley 7 (2026-11-06, coordinator run 10 — LAST generation volley)
- **S20 t2 (v2 completeness): REJECT — S20 STRUCTURAL** (md5 f80b133c10191def1508480136a40a8c) — FC.1–FC.3 exact (15/15, ratio 0.86 in band, frame 2.926/0f) but FC.4 "I'm The Nobody Man" missing AGAIN; full pass + tail split-half agree. Two pulls, identical drop point — completeness axis exhausted, NO v3. Assembly: t2 is the FC.1–FC.3 base; montage cover for exactly 150.38–152.88s, back at FC.5 (S21 t1).
- **S24 t2 (v2 lyric-as-performed): NO TAKE** — media.generate_video errored ("media generation failed"); no file on disk, request NOT repeated per tool-failure instruction. S24 stays open; v2 vehicle already written (redesign_v2/vehicles/mv7v2_s24_v2_vehicle.txt). Parent call: one more fire, or assembly coverage for the 8-word tag chant (173.30–183.24s) + outro fade.
- KEEP pool: S02, S03, S04, S05a, S05b, S06, S07, S08, S09, S10, S11, S12, S13, S14, S16, S17, S18, S19, S21, S22, S23 (21 — unchanged). STRUCTURAL: S01, S15, S20. Full QC: work/qc_v7/mv7_s20_t2_QC.md; notes: work/qc_v7/VOLLEY7_NOTES.md.

## Volley 8 (2026-11-06, coordinator run 11 — SINGLE FIRE) — S24 t2 (Era C, Final Chorus tag)
Verbatim re-fire of the written v2 vehicle (volley 7's attempt errored in the tool, no file produced).
- **S24 t2 (v2): KEEP-WITH-FLAG** (md5 2d9dd5ff1a6c81342925ae3f88909cd9) — 8/8 words exact, once, in
  order; lyric-as-performed axis CLOSED. Ratio 1.255 grey-edge (uniform warp 0.797x inside caps);
  frame rule 2.884 / run 0f. Flags: P2 phrase warp 2.68x slow at phrase level (song holds "nobody"
  3.92s vs take 1.06s — assembly ramps through the held note or takes the uniform warp; disclose);
  slow push-in, NOT the vehicled pull-back (frame rhyme weaker than t1's); sings 0.00–7.92 vs
  0.5–5.5s window; eyes closed in the final grin hold; 1152x768 raster. Full QC:
  work/qc_v7/mv7_s24_t2_QC.md; notes: work/qc_v7/VOLLEY8_NOTES.md.
- KEEP pool: S02, S03, S04, S05a, S05b, S06, S07, S08, S09, S10, S11, S12, S13, S14, S16, S17, S18,
  S19, S21, S22, S23, S24 (22). STRUCTURAL: S01, S15, S20. OPEN: NONE — all 24 scenes covered.

## Assembly readiness (after volley 8) — ALL 24 SCENES COVERED
- 22 KEEP takes cover 22 of 24 scenes. Structural (assembly coverage, no more generation): S01 (split-chant restage S01a/S01b), S15 (montage 110.36–112.86s), S20 (montage 150.38–152.88s, t2 = FC.1–FC.3 base).
- OPEN: none. Assembly next (v4 method).
- Assembly items already owed: S10 measured tag ×3 (take matches measured lyric); S05a ~1.9x squeeze + S05 t4 2.53x squeeze + S13 t2 ~1.67x squeeze (disclose); S16 caption adjudication ("spots/Flipping" vs "sparks/flicking"); S24 t2 P2 warp (2.68x phrase-level, ramp through the held note or uniform 0.797x — disclose); S24 t2 push-in vs t1 pull-back (assembly picks t2, correct lyric, trims/crops); mixed rasters (1152×768 Era A/C crops to 16:9; S08/S09 true 1280×720; S11/S12–S19 1248×704 crop/pad).

## Assembly readiness (after volley 7)
- 21 KEEP takes cover 21 of 24 scenes. Structural (assembly coverage, no more generation): S01 (split-chant restage S01a/S01b), S15 (montage 110.36–112.86s), S20 (montage 150.38–152.88s, t2 = FC.1–FC.3 base).
- OPEN: S24 only — one v2 fire owed (vehicle written) OR assembly coverage. Parent decides.
- Assembly items already owed: S10 measured tag ×3 (take matches measured lyric); S05a ~1.9x squeeze + S05 t4 2.53x squeeze + S13 t2 ~1.67x squeeze (disclose); S16 caption adjudication ("spots/Flipping" vs "sparks/flicking"); mixed rasters (1152×768 Era A/C crops to 16:9; S08/S09 true 1280×720; S11/S12–S19 1248×704 crop/pad).

## OTAKU REBUILD (2026-11-07) — COMPLETE
Volleys V1–V7 (40 units) + recovery volleys 2B/3B + completeness reroll R1 (6 t2 takes).
Assembly v3: picture 4493f exact; warps 0.785–1.742 (caps respected); kinetic HIGHLIGHT layer burned.
DELIVERED: masters/mv7_im_the_nobody_man_16x9_otaku.mp4 (md5 c89c4757928a31b95ada25928d498020)
+ 50mb copy (md5 7b3de18be0ead36b2b752838f10f0a98). Gates/disclosures in MV7_OTAKU_REBUILD_NOTES.md.
