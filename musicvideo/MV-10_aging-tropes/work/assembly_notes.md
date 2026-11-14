# MV-10 "Aging tropes" — ASSEMBLY NOTES (coordinator 6f5971db, spawned ~12:35 EST 2026-11-09)

## STATUS (13:13 EST 2026-11-09) — CHECKPOINT
- Inputs VERIFIED (12:4x EST): track.mp4 md5 `fd60ac7335e3bdb55d97a2242dbee38c` (178.0s) ✓;
  all 22 KEEP-take md5s match TAKE_LEDGER.md ✓; 52G free; all takes 24fps
  (1248x704 or 1280x720).
- Word times MEASURED, no Whisper re-run needed or run (nothing wedged):
  SONG_WORDS.json (277 words) + every KEEP take's work/qc/<scene>*/words.json
  parses (all 22). Take-side word lists + song word times + RMS-energy gap
  measurements are in hand; the full per-scene anchor tables are in
  `work/assembly_build.py` (SCENES) — being written next, then segments.
- NO segments built yet. NO master yet. NO delivered flag (parent writes it).
- Method: MV-8 v3 builder pattern (PCHIP phrase warps through word anchors,
  per-segment CRF-14 intermediates forced to contract frames, split final
  encode, kinetic .ass burn-in). Adapted: pchip pieces carry an explicit END
  anchor (last word's end) so the last word's full duration is in the piece.

## DECISIVE MEASUREMENT — the song HOLDS notes (not silence) in the gaps
Song word END times + 0.5s RMS windows (track_16k.wav) prove the long
song-internal gaps are SUSTAINED VOCAL notes, not empty music:
- "nighttime" 18.82–22.00 (held 3.18s, −17..−21 dB) — S02
- "price" 23.88–26.14 (held 2.26s; "state/didn't" are ASR splits of the hold)
- "on," 37.24–38.86 (held 1.62s) and 40.20–41.16 (held 0.96s) — S03b gaps
- "you" 149.96–154.48 is an ASR pile-up (the S11b "don't stop" is merged into
  it; the funk phrase template puts don't≈150.26, stop≈150.50 — [inferred])
- S12: "you" held 157.10–160.14 (3.04s); "it" held 161.64–163.76 (2.12s).
  The take sings the hooks quickly; the song performs them spaciously.
- S12 tail ("It sucks / But the pocket / Stays tight") has NO song words in
  154.48–165.24 and none in the outro — the Suno vocal drops the tail.
  The take's tail words (take 5.42–8.28) are NOT USED. Disclosed.
- S03a garble region 31.66–35.20 ("feel the wind it climb, eat more water
  now, Drink it") is ASR garbage over a loud passage; plan split at 36.22
  ("sucks") stands: S03a owns through first "sucks", S03b from "sucks".

## SCENE CONTRACTS (frames, 24fps; total exactly 4272)
S01 0.00–16.68 = 400f | S02 16.68–29.82 = 315f | S03 29.82–44.72 = 358f |
S04 44.72–55.46 = 258f | S05 55.46–66.94 = 276f | S06 66.94–89.18 = 534f |
S07 89.18–106.40 = 413f | S08 106.40–113.86 = 179f |
S09 113.86–131.76 = 430f (extended through the 127.56–131.76 wordless gap) |
S10 131.76–140.86 = 218f | S11 140.86–154.48 = 327f |
S12 154.48–165.24 = 258f | S13 165.24–178.00 = 306f.
Boundary drift vs true song times ≤0.04s (±1f); anchors use absolute song
times, so word placement is exact regardless.

## PIECE PLAN (per scene; take = mv10_<id>, all spans in take-seconds)
- S01: uniform s01_t1 0–10 → 0–16.68 (1.668x slow, cold open, no words).
- S02: pchip s02_t2 (9 anchors + end 7.18→27.42) + natural tail 7.18–9.54.
- S03: pchip s03a_t3 words 1–7 (Bend→29.82 … sucks→36.22; "to get old"
  dropped, covered by S03b) + pchip s03b_t1 words 2–15 (sucks→36.22 …
  tight→42.60, end 6.98→43.98; its word-1 "it" 35.64 covered by S03a tail)
  + natural tail 6.98–7.72.
- S04: pchip s04a_t1 (13 anchors + end 4.48→49.12) + pchip s04b_t1
  (11 anchors, last (6.26,55.46) = "stop" onset = scene end).
- S05: uniform s05_t1 0–10 → 55.46–66.94 (1.148x slow); CASCADE kinetic
  on the drink-it patter 58.20–62.90.
- S06: pchip s06a_t3 (head trimmed 0.46s — "Standing" mouth opens on the
  armchair shot; first anchor (0.46,66.94)) + natural tail 8.92–9.46 +
  pchip s06b_t1 + natural tail 4.00–4.24 + pchip s06c_t1 +
  natural tail 7.18–8.48 (covers the 87.88–89.18 gap).
- S07: pchip s07a_t2 part 1 (take 0–6.24 → song 89.18–94.42) + PAUSE COVER
  (song over-end→96.50, S07b take tail 7.92–10.00, non-overlapping with the
  main S07b piece — no frame reuse) + pchip s07a_t2 part 2 (take 6.24–9.44
  → song 96.50–100.40) + natural s07b_t1 0–6.00 → 100.40–106.40.
  S07a mapping: 2-word hook ("bop bop") vs song's 3 tokens — bop→Pop,
  bop→it, "up," skipped; prostate→state (92.98) because song "and"/"price"
  pile up at 92.46.
- S08: natural s08_t1 0–7.46 → 106.40–113.86 (23f still run sits past cut).
- S09: natural s09a_t1 0–6.80 → 113.86–120.66 (split on "Soap" 120.66) +
  uniform s09b_t1 0–10 → 120.66–131.76 (1.11x slow, memory lingers).
- S10: pchip s10a_t1 (19 anchors; 4th hook "bop," 1.34–1.86 rides
  unanchored in the beep→you interval = disclosed stutter; third "oh"
  interpolated — song pile-up at 137.60, end (8.80,139.02)) +
  natural s10b_t1 0–1.84 → 139.02–140.86.
- S11: pchip s11a_t1 (18 anchors + end 7.36→146.72; take's 3 drink-its map
  to song's first 3) + natural s11a_t1 held pose 7.36–9.46 → 146.72–148.82
  (CASCADE kinetic covers the remaining 7 drink-its 146.58–148.38) +
  pchip s11b_t1 (1.66→148.82, 2.98→149.02, 3.64→149.16, 5.10→149.96,
  5.48→150.26 [inferred], 6.02→150.50 [inferred], end 6.42→150.90) +
  natural s11b_t1 tail 6.42–10.00 → 150.90–154.48 (exact 3.58s fit).
- S12: ONE pchip s12_t1 (take 0–5.12 → song 154.48–165.24; "-bee" anchor
  154.65 interpolated inside the ASR pile-up; take tail 5.42–8.28 UNUSED).
- S13: natural s13a_t1 0–6.20 → 165.24–171.44 + natural s13b_t1 0–6.56 →
  171.44–178.00 (last frame = morning glass, rhymes with S01).

## WARP FLAGS (cap audit: playback <0.50x = slow past 2x; speedups fine)
- S02: Nighttime→every 0.33x, Prostate→check 0.23x — HELD notes (see above).
  Least-bad = exact placement on held notes, disclosed; eye-check segment.
- S03a: it→sucks 0.28x (garble region; take's held "it" covers it).
- S03b: old,→it 0.19x (held "on"), old,→but 0.016x (held "on" — near-freeze
  on a closed-mouth inter-phrase frame; eye-check; fallback = tail-cover
  take 6.98–8.24 for the gap, back at "but" 41.46).
- S04a: lot→and 0.37x (short, 0.70s song span).
- S04b: oh→oh 0.38x, oh→bop 0.48x, you→don't 0.20x (all short spans).
- S06a: House→is 0.44x, quiet→kids 0.42x, kids→pay 0.29x (per-word dips;
  phrase-level stretch is ~1.3x per the V4 ledger note — PCHIP kept for
  exact placement, eye-check).
- S06c: sucks→to 0.49x (borderline), sucks→to 0.20x (1.58s song pause).
- S07a: and→prostate 0.50x (exactly at floor, allowed).
- S10a: CLEAN (min 0.51x). S11a: you→don't 0.22x (transient, 0.36s span).
- S11b: WARP RISK — hook compresses 6.6x/4.7x inter-word (overall 1.76x,
  at the proven rescue edge). EYE-CHECK REQUIRED on the built segment:
  mouth must be open at song 148.82/149.02/149.16 onsets. If closed,
  S11b is owed a re-fire — do NOT ship a failed warp, do NOT re-fire here.
- S12: bop→you 0.37x, you→don't 0.033x (held "you" 3.04s), bee→bop 0.13x
  (held "it" 2.12s), you→don't 0.46x — STRUCTURAL held-note stretches.
  EYE-CHECK REQUIRED; if the render reads frozen (not sustained singing),
  S12 is owed a re-fire (slower take, pacing axis) — report, don't ship.

## KINETIC (post layer, .ass — build after segments)
HIGHLIGHT per line (S02/S03/S06); SLAM on hooks: "Gotta pee again" 16.68,
"It sucks" 36.22 + 39.30, "Bop-bee-bop" 44.72 + 53.82 + 89.18 + 98.26 +
131.76 + 140.86, "Standing up is slower" 66.94; CASCADE on drink-it
patter 58.20–62.90, 102.66–106.04, 146.58–148.38; STACK on "Four squares /
QR code / 99" (S09). S12 STACK SKIPPED — the tail has no song words.
Corner bug "~ WuBu ~" bottom-right, whole duration (MV-8 v3 form).

## FINAL ENCODE PLAN (MV-8 v3 lessons: single-pass full encode OOM'd twice)
Split at the S07/S08 boundary (106.40s): half 1 = S01–S07 (2554f),
half 2 = S08–S13 (1718f). Video-only CRF-18 halves with kinetic burned
in, then mux halves + track audio re-encoded AAC 48k stereo (NEVER MP3
copy; apad capped whole_dur + -t) + faststart. Gates on the master:
exactly 4272f; SEI crf=18.0; AAC codec (ffprobe); faststart; mouth state
at word onsets by eye on the MASTER; motion audit. Chat copy ≤50 MB
(bitrate cap, AAC copied) only if the house master exceeds 50 MB.

## NEXT STEPS
1. Write work/assembly_build.py + manifest (SCENES above) — IN PROGRESS.
2. Run --analyze (cap audit); disposition flags.
3. Build segments S01→S13 (checkpoint manifest after each).
4. Eye-check S11b + S12 + S02 segments (frames at song word onsets).
5. Build kinetic .ass; split-encode halves; mux; gates; chat copy if needed.
6. Short final report to parent (master path/md5/ffprobe/gates/S11b verdict).
   NO commit. NO delivered flag (parent writes it).

## CAP AUDIT — DISPOSITION (recovery coordinator, 2026-11-09 ~14:20 EST)
- Builder written: work/assembly_build.py (SCENES from the piece plan above).
  All 22 KEEP-take md5s re-verified vs TAKE_LEDGER.md (0 mismatches);
  track.mp4 md5 fd60ac7335e3bdb55d97a2242dbee38c ✓; all takes 24fps.
- `python3 work/assembly_build.py --analyze`: TOTAL 4272f; scene totals
  exact except S07 414/413 (+1) and S09 429/430 (-1) — both within the
  builder's <=2f drift fix. 10 pchip pieces flagged CAP VIOLATION
  (derivative min <0.5x). ALL 10 are the already-disclosed held-note
  stretches: S02, S03a, S03b, S04a, S04b, S06a, S06c, S07a-p1, S11a, S12.
  Disposition: LEAST-BAD exact placement on held notes (RMS-proven
  sustained vocal, not silence) — build proceeds; eye-check decides
  S02/S03/S11b/S12 on the rendered segments.
- Audit vs notes corrections (supersede the notes' numbers where they differ):
  (a) S03b "old,->it 0.19x / old,->but 0.016x" do NOT reproduce — actual
  interval means 0.55x/0.59x, derivative min 0.34x. No near-freeze there.
  (b) S06a "quiet->kids 0.42x" does not reproduce (interval mean 1.00x).
  (c) S11b "overall 1.76x" does not reproduce — pchip span is 4.76s take
  -> 2.08s song = 2.29x; per-interval 6.6x/4.7x reproduce exactly.
  (d) S10 third "oh" interpolated at (8.44, 138.31) — midpoint of the
  song's held third oh (137.60-139.02); PCHIP monotonicity forbids 137.60.
- Derivative-spike check (frame-sampled inverse, all pchip pieces): the
  analyze max speeds (up to 2164x instantaneous) are sub-frame PCHIP
  artifacts — sampled at output frame centers the largest single-frame
  take jump is 0.38s (S03b, 9.1x one frame) and 0.30s (S11b, 7.3x one
  frame, the expected hook compression). Zero negative steps, zero
  multi-second jumps. Safe to build.
- Slow-stretch reality (longest below-0.5 run, take seconds): S02 0.90s
  (Nighttime hold), S03a 1.26s (it->sucks garble cover), S03b 0.48s,
  S04b 0.52s, S06a 0.29s, S06c 0.30s, S11a 0.08s, S12 0.56s (the "you"
  hold: take advances 0.10s over 3.04s song — near-freeze by construction,
  eye-check is the gate). S06b/S07-p2/S10/S11b-pchip: no sustained
  below-0.5 run (S07-p2 + S10 = transient dips 0.18s/0.19s, kept).
- S06 piece-plan arithmetic: the notes' mid-scene natural tails (s06a
  8.92-9.46 = 13f, s06b 4.00-4.24 = 6f) overshoot the 534f contract by
  16f when added to the pchip spans (550f). OMITTED as separate pieces
  (post-vocal held poses at boundaries where the next line starts
  immediately — nothing visible lost); 79.62-79.74 gap covered by 3f of
  s06b tail head (4.00-4.12). Total exactly 534f. S07-p1 END anchor
  stretched 0.04s to 94.42 for continuity with the pause cover.

## SEGMENTS BUILT (recovery coordinator, 2026-11-09 ~14:38 EST)
- All 13 segments built, frame-exact: S01 400, S02 315, S03 358, S04 258,
  S05 276, S06 534, S07 413, S08 179, S09 430, S10 218, S11 327, S12 258,
  S13 306 = 4272f. Manifest work/assembly/assembly_manifest.json (md5s in
  work/assembly_build.log). CRF-14 intermediates, 1280x720.

## EYE-CHECKS ON BUILT SEGMENTS (frames at song word onsets, work/assembly/eye/)
- S11b WARP RISK — PASS, NO RE-FIRE OWED. Segment frames at 148.82
  (Bop): mouth parted, small-"o" = TRANSITIONAL-OPEN; 149.02 (it): WIDE
  OPEN; 149.16 (up,): OPEN, smiling; 150.26/150.50 (inferred don't/stop):
  OPEN, rounded-"o" shapes. No onset closed. The 6.6x/4.7x compression
  lands the mouth on the hook. Motion across the piece mean diff 9.85,
  longest near-still run 2f. (Eyes closed through the hook — the take's
  own performance, disclosed in the ledger; the gate tests the mouth.)
- S12 HELD-NOTE STRETCHES — PASS as SUSTAINED SINGING, NO RE-FIRE OWED,
  disclosed as the weakest passage in the master. "you" onset 157.10:
  mouth OPEN; mid-hold frames (f80/f96/f110) hold the open "you" shape
  with slow drift — the take advances at ~1/30 speed, frames are NOT
  identical. "don't" 160.14: OPEN. "it" hold 161.64-163.76: mean diff
  1.34, longest near-still run 16f. Numbers: "you" hold mean diff 0.37,
  longest near-still run 43f/1.8s (fails the v6 numeric motion gate) —
  but the eye read is a held note with an open mouth and micro-drift,
  not a frozen frame; the v6 gate was written for natural-speed takes,
  and the notes set the eye as the decider here. A slower-take re-fire
  could add motion to the hold, but the gate as written (frozen vs
  sustained singing) is met.
- S02 — PASS. "nighttime" onset 18.82: mouth OPEN; "every" 22.00:
  TRANSITIONAL (lips parted, closing from the held note); "check"
  27.12: OPEN. Quiet locked-off MCU throughout the holds (mean diff
  0.38/0.27, longest near-still runs 12f/7f) — reads as sustained, not
  frozen; matches the ledger's "visually quiet, not frozen" disclosure.
- S03 — PASS. Garble-cover stretch moving (mean diff 1.60, longest run
  15f); "sucks" onset 36.22 (S03a->S03b cut): mouth OPEN, teeth visible,
  doc's mouth closed, wallet in hand. The take change lands on the word.
- Kinetic layer: work/build_kinetic.py -> work/assembly/mv10_kinetic.ass
  (36 lines, 257 words, 400 events). Word text: measured SONG_WORDS.json
  with a documented 1:1 ASR->lyric correction map (Bend/doc/prostate/
  Bop/winded/bass/old); garble + pile-up-echo tokens dropped; full map
  in work/assembly/mv10_kinetic_words.json. SLAM tail uses the fixed
  kinetic_ass.py (MV-9 "goty" bleed fix).

## MASTER MOUTH GATE — MEASURED ON THE DELIVERED MASTER (recovery coordinator, 2026-11-09 ~20:00 EST)
- Gates (work/gate_master.log): ALL PASS — 4272f, 178.008s, h264 1280x720
  24fps, AAC 48k stereo, SEI crf=18.0, faststart (moov@36 < mdat@124492),
  audio agreement corr 0.9982–0.9989 across 5 windows.
- Master motion audit (full-master frame diff, 320x180 gray): overall
  mean diff 5.32. Vocal near-still runs >=12f: 21.46s 12f (S02 hold),
  35.54s 15f (S03 garble), 83.04s 16f (S06c), 157.17s 43f + 159.00s 23f
  (S12 "you" hold — the disclosed passage), 162.33s 16f (S12 "it"
  hold). No other run >=24f. No halted-photo-then-move cut found.
- Mouth state at sampled onsets ON THE MASTER (frames in
  work/assembly/eye_master/):
  OPEN: nighttime 18.82, check 27.12, sucks 36.22, Bop 53.82, Bop 148.82
  transitional-open (149.02/149.16 wide open), you 157.10.
  CLOSED at the exact onset frame (take-head mouth-lag — see flaw note):
  Bend 29.82, Bop 44.72 (closed through 45.68, opens at you 46.14),
  Standing 66.94 (opens ~0.4s into the word; transitional at +0.15s),
  Bop 89.18 (profile bedroom head; opens ~90.62 you), Bop 140.86
  (anchor close-up head; opens during -bee/-bop,), Bop 154.48 (bedroom
  head; opens by ~155.5, you 157.10 open).
  NO SINGER IN FRAME (montage/morph moment, not a mouth fail):
  Bop 131.76 (festival wide; the young man morphs in ~0.5s later).
- Kinetic verified on the master: SLAM "Bop"/"you" + accent bars +
  corner bug "~ WuBu ~" visible at 44.72–46.54; HIGHLIGHT "nighttime"
  + dim line + accent bar at 18.82; final frame 177.96 = morning glass
  in gold light, rhymes with S01.
- DISCLOSED FLAW (the master ships with it; user's playback verdict is
  final): SYSTEMATIC TAKE-HEAD MOUTH-LAG. The warps place every audio
  word exactly on the song grid, but the takes' VISIBLE mouths lag
  their own generated audio by ~0.5–1.4s at take heads, so six sampled
  line/hook onsets land on closed mouths (listed above) with the mouth
  opening 0.4–1.4s into the line. This is a property of the KEEP takes
  as QC'd (S04a "mouth open mid-clip"; S06a_t3 "mouth lags take audio
  ~0.5–1s at the head"; S12_t1 "mouth nearly closed at 0.5s on the
  first Bop"), not a warp error — no visible mouth event exists for
  those words in the takes, so re-anchoring cannot fix it and no
  legitimate montage cover material exists on disk (all takes used;
  rejects banned; no new generation in this role). The only fix is a
  re-fire of S04a/S07a/S11a/S12 (and S03a/S06a) on a mouth-timing axis
  — a parent-ordered volley, not an assembly step. Kinetic type carries
  every line on the grid throughout.

## PARENT DELIVERY VERIFICATION (2026-11-09 ~15:25 EST)
- House master parent-verified: 1280x720 h264 24fps, exactly 4272f,
  178.008s, AAC 48k stereo, SEI crf=18.0 (x2, both halves), moov@32
  faststart, md5 38757f349778010cb4431f7ab948ffb6, 77,720,242 B.
  gate_master.log: ALL GATES PASS (audio agreement min 0.9982).
- Coordinator 61d6de42 COMPLETED 15:10:26 EST but CANCELLED before its
  final report (no final message; its chat-copy encode aborted at
  32,505,904 B, no moov). All of its disk work was consumed by the
  parent instead: segments 13/13 frame-exact, manifest, kinetic .ass
  (fixed SLAM), gate log, and its session-jsonl eye-check record.
  Parent re-encoded the chat copy (1750k, AAC copied) and verified it:
  42,314,896 B, exactly 4272f, AAC, faststart, audio md5 IDENTICAL to
  house master (0ce3fe43...). Corrupt partial *_chat.mp4 deleted.
- PARENT MASTER EYE-CHECK (frames at song word onsets, independently
  of the coordinator; coordinator's session record agrees on every
  sampled onset):
  OPEN: nighttime 18.82, check 27.12, sucks 36.22, Bop 53.82 (S04b,
  wide open), you/stop 46.14/46.54 + 90.62/91.06 (S04/S07 lines track
  from "you" on), Bop/it/up 149.02/149.16 (S11b hook — hard gate PASS),
  you 157.10 (S12 hold onset — sustained singing, see below).
  TRANSITIONAL: every 22.00, Standing 66.94 (+0.15s parted, open by
  +0.5s), Bop 148.82 (small-"o" parted).
  CLOSED AT ONSET (disclosed, ships as-is — see decision below):
  the takes' visible mouths lag their audio ~0.5-1.2s at line starts
  (generator property, verified in the raw s04a take: mouth closed
  take 0.00-1.04, open from ~1.5s). Affected onsets: Bend 29.82
  (opens wide on "sucks"), Bop 44.72 S04 (triplet 44.72-46.14 closed,
  opens on "you"), Bop 89.18 S07 (same, opens on "you" 90.62),
  Bop 98.26 S07b (closed smile mid-word, single frame), Bop 140.86
  S11a (0.13s anchor head), Bop 154.48 S12 (opens by ~155.5).
  S10a Bop 131.76: no singer in frame (festival wide / morph — montage
  moment, disclosed in plan). S06 Standing: onset closed, open by
  +0.5s within the 0.6s word. Kinetic: clean at every sampled SLAM
  (Standing 66.94, Bop 149.00, full line "Bop it up, you don't stop"
  157.08, nighttime HIGHLIGHT 18.83) — no MV-9 "goty"-style bleed;
  fixed kinetic_ass.py in use.
- MOTION AUDIT (coordinator, full-master native-fps scan; parent
  concurs): overall mean diff 5.32. Vocal near-still runs >=12f: six —
  12f@21.46, 15f@35.54, 16f@83.04, 43f@157.17 (S12 "you" hold, 1.79s),
  23f@159.00, 16f@162.33. The S12 hold is the disclosed weakest
  passage: held note, mouth OPEN with micro-drift (parent frames at
  157.08 + 158.33 confirm open mouth, slow drift) — sustained singing,
  not a frozen frame; v6 numeric gate fails on it but the eye is the
  decider per the assembly notes. No halted-photo-then-movement starts.
- SHIP DECISION (parent): the closed-onset pattern is real, bounded
  (line-opening ~1s, mouths track correctly for the rest of every
  line; S04b's hook sings wide open), and NOT fixable by warp (audio
  anchors are correct; shifting to mouth events would break the rest
  of each line) nor reliably by re-fire (mouth-lag is a generator
  property seen in 5+ takes). Per the MV-9 precedent (S08b 1.6s lead
  + S04b phase drift shipped disclosed), MV-10 ships with the pattern
  disclosed at exact times; the user's playback verdict is the final
  gate. S11b hard gate PASSED — no re-fire owed.
- DELIVERED 2026-11-09 ~15:25 EST. Flag MV10_DELIVERED.flag written
  by parent. Chat copy masters/mv10_aging_tropes_16x9_50mb.mp4.
