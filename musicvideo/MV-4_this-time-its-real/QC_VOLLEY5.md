# MV-4 QC_VOLLEY5.md — volley 5 (S21 restage t1, S23, S24, S25, S26, S27 t1)

Method: frames at 2s/5s/8s (widened when reads disagree: S21 at
3s, vocal starts 2.22s; S25 at 4s/9s for the missing second
delivery); Whisper word count vs prompted line (count ratio AND
duration ratio — song window / take vocal span, band 0.80–1.25
for both); motion audit at native 24fps, 160x90 gray (frame gate FAIL
if vocal near-dup run ≥24f during vocal OR vocal mean diff <0.5;
near-dup = mean abs diff <0.5). Prompted re-transcription
(initial_prompt = the scene's performed line) + split-half recheck
run for S23 t1 and S25 t1 where the unprompted decode came up
short. Confidence tags: [confirmed] measured, [inferred]
model-judged, [assumed] user claim. Nits are disclosed, never
promoted to fails.

## S21 t1 — KEEP (restage landed; flagged — early vocal onset, gap cover owed)
- File: takes/mv4_s21_t1.mp4, md5 27cb0987d3bb035c95eb2e4edcf31506,
  10.00s, 1280x720 h264 + AAC [confirmed].
- Whisper: 16 tokens / 14 words — "Futurama's" heard as "Future
  Rama's" twice, the established tokenization split (same class as
  S08). Normalized count 14/14, ratio 1.00 [confirmed]. Line sung
  once. Vocal span 0.00–8.94s (8.94s) vs song 7.78s → duration
  ratio 0.87, in band.
- FLAG — vocal starts at take 0.00s, ~2.2s before the song's first
  word (158.76s = local 2.22s): the generator front-loaded the
  vocal and delivered ~0s of the staged pre-line step-to-mic. The
  take is complete and warpable, so this is an assembly note, not
  a fail: trim at first word, place at 158.76, warp 0.87; the
  156.54–158.76 gap lead-in needs cover in a no-word window
  (S20 held pose / held shot — freeze is allowed there, never
  during words).
- Motion: vocal mean diff 3.595, longest near-dup run 1f, 0 exact
  duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA consistent (warm skin, house style).
  BOLT's chest is one smooth plain bone-white shell, no panel, no
  glyph (TEXT axis stays closed). Nits: BOLT has a round dome head
  + antenna ball (design drift, same class as S22; bible says
  rectangular head, no antenna ball); gold epaulette bars + small
  gold bow tie on NOVA (added-accessory class).
- G2 PASS [confirmed]: neon panels abstract, no letters; no signs;
  paper ship blank.
- G3 PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera
  (3s/5s/8s); open-mouth vocal at 3s (eyes closed = singing
  beat), 5s, 8s (still inside "dark", 8.30–8.94s). Nit: the paper
  ship is already in his palm at 8s — it lands ~1s early,
  overlapping the final word (same early-beat nit class as S05's
  launch).
- G5 PASS (flagged): trim 156.54–166.54, warp 0.87 within caps,
  gap cover owed (see above). G6 PASS (plan-level).
- Beat verified: final chorus reopens at the mic, BOLT and ZIB
  flanking, floor reignites in a cadmium wash, ship lands in his
  palm. S21 UNBLOCKED — the restage landed.

## S23 t1 — REJECT (G5, completeness — second repeat absent)
- File: takes/mv4_s23_t1.mp4, md5 561a7501818abc83bdd2c4efb2428206,
  10.00s (requested 9s; tool returned 10.00s — recorded),
  1280x720 [confirmed]. Kept on disk only, never chained from.
- Whisper: 10/14 words, count ratio 0.71 [confirmed]. "Good news,
  everyone. Good news, everyone. The ride is done." — the second
  "the ride is done" is absent. Prompted re-transcription returns
  the SAME 10 words; split-half 5–10s finds only "The ride is
  done" once. Vocal span 0.00–6.68s vs song 7.34s → duration
  ratio 1.10, in band — the take is in pace but short a repeat.
  Motion: vocal mean diff 3.096, longest near-dup run 1f, 0 exact
  duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA consistent (warm skin, house style).
  Nits: he grips the mic in his gloved hand (handheld-mic class);
  gold epaulettes + collar flourish (added-accessory class).
- G2 PASS [confirmed]: no text anywhere; background panels blank
  or plain colored light. G3 PASS [confirmed]. G4 PASS
  [inferred]: 3/3 face-to-camera; open-mouth vocal at 2s and 5s
  (5s is an inter-word gap holdover, 4.58–5.36s); 8s closed mouth
  is the correct post-line rest (last word "done" ends 6.66s).
  The crowd raises their arms on each repeat, mouths closed.
- G5 FAIL: count 0.71 outside 0.80–1.25 — the song's second "the
  ride is done" (179.26–181.24) has no mouth. The take cannot
  cover that position.
- Reroll: S23 t2, axis DELIVERY (one variable — restate the repeat
  explicitly, "including the second time saying the ride is
  done", whole line inside 0.0–7.3s). Owed in volley 6.
- Beat verified in part: last call at the mic lands, crowd
  answers — but the repeat is missing, so the beat is incomplete.

## S24 t1 — KEEP
- File: takes/mv4_s24_t1.mp4, md5 7ab5ac4462d371e61ec2d7fe26e96e31,
  9.00s, 1280x720 [confirmed].
- Whisper: 10/10 words, count ratio 1.00 [confirmed]. "Good news,
  everyone. Good news, everyone. No more coming on." Line sung
  once. Vocal span 0.00–6.28s (6.28s) vs song 6.22s → duration
  ratio 0.99, in band.
- Motion: vocal mean diff 5.922, longest near-dup run 0f, 0 exact
  duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA consistent (warm skin, house style).
  Nits: bone chest marks + gold chain (added-accessory class);
  crowd mouths soft/open in the background (background nit, same
  treatment as S22 — the crowd is soft background, not the
  singer).
- G2 PASS [confirmed]: paper ship blank, neon panels abstract, no
  letters. G3 PASS [confirmed]. G4 PASS [inferred]: 3/3
  face-to-camera; open-mouth vocal at 2s (eyes closed = singing
  beat) and 5s (in "coming"); 8s closed mouth is the correct
  post-line rest (last word "on" ends 6.28s). Arms-open hold
  delivered; paper ship circles overhead.
- G5 PASS: trim 181.24–187.46, warp 0.99. G6 PASS (plan-level).
- Beat verified: wide arms-open landing, "No more coming on."
  lands soft.

## S25 t1 — REJECT (G5, pace/completeness — line delivered once, second delivery missing)
- File: takes/mv4_s25_t1.mp4, md5 993cf76b4d9a1a6b214fff75d7e0a45e,
  10.00s (requested 9s; tool returned 10.00s — recorded),
  1280x720 [confirmed]. Kept on disk only, never chained from.
- Whisper: 2/4 words unprompted, count ratio 0.50 [confirmed].
  "Futurama's finished" once, 0.00–2.92s. Prompted
  re-transcription claims 4/4 with a second delivery at
  8.58–10.0s — REJECTED as hallucination: per-second RMS in
  8–10s is 0.008/0.005 (background bed only, vs 0.075 vocal
  peak), split-half 5–10s unprompted finds 0 words, and the mouth
  is closed at both the 5s and 9s frames. The second "Futurama's
  finished" was never sung. Vocal span 0.00–2.92s vs song 5.82s →
  duration ratio 1.99, outside band. Motion: vocal mean diff
  1.259, longest near-dup run 3f, 0 exact duplicates [confirmed].
  Not frozen (the ship moves past the window; the face holds).
- G1 FLAGGED [inferred]: pale LAVENDER-GREY skin — the strongest
  hue drift in the build (past S16's blue-grey + red lips).
  Disclosed nit class; the reroll axis is PACING, not hue — if t2
  drifts too, it stays a disclosed nit (a HUE reroll is
  parent-order-only, unordered). Nits: he grips the mic in his
  hand (handheld-mic class); gold chain (added-accessory class).
- G2 PASS [confirmed]: control panels are abstract colored dots,
  no letters; no signs. G3 PASS [confirmed]. G4: 2s open-mouth
  vocal (eyes closed = singing beat); 5s and 9s closed — the 5s
  closed sits inside the song's second delivery (local 2.16–
  4.98s), which is the failure itself. G4 judged on the take's
  own vocal passes, but G5 fails.
- G5 FAIL: count 0.50, line ratio 1.99 — the second "Futurama's
  finished" has no mouth, and no warp inside the caps can place
  one there.
- Reroll: S25 t2, axis PACING (one variable — sing the line twice
  with no long pause between the two deliveries, whole line
  inside 0.0–5.8s, second "Futurama's" held). Owed in volley 6.
- Beat verified in part: observation deck + ringed planet
  delivered; the slow held line is not.

## S26 t1 — KEEP
- File: takes/mv4_s26_t1.mp4, md5 f5b3d9ac4b4988ccdc1b4de52e6eed4c,
  9.00s, 1280x720 [confirmed].
- Whisper: 4/4 words, count ratio 1.00 [confirmed]. "For real
  this time." Line sung once, slow and held. Vocal span
  0.00–3.60s (3.60s) vs song 4.32s → duration ratio 1.20, in
  band (near the edge — noted).
- Motion: vocal mean diff 2.454, longest near-dup run 0f, 0 exact
  duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA consistent (warm skin, house style).
  Nit: large fringed gold epaulettes (added-accessory class, new
  variant).
- G2 PASS [confirmed]: ship window + ringed planet, no text. G3
  PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera
  (three-quarter); open-mouth vocal at 2s (in "this"); 5s and 8s
  closed mouths are the correct post-line rest (last word "time"
  ends 3.60s). Held pose in moving footage — the ship passes in
  the window behind him.
- G5 PASS: trim 194.06–198.38, warp 1.20. G6 PASS (plan-level).
- Beat verified: one slow held line at the ship window delivered.

## S27 t1 — KEEP
- File: takes/mv4_s27_t1.mp4, md5 2e8a1d6f31f3476ed9013d844c3ecb98,
  10.00s (requested 9s; tool returned 10.00s — recorded),
  1280x720 [confirmed].
- Whisper: 4/4 words, count ratio 1.00 [confirmed]. "No more
  coming on." Line sung once. Vocal span 0.00–5.38s (5.38s) vs
  song 6.34s → duration ratio 1.18, in band.
- Motion: vocal mean diff 2.609, longest near-dup run 0f, 0 exact
  duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA consistent (warm skin, house style).
  Nit: large gold chest panels (added-accessory class, same
  family as S16's gold chest panel).
- G2 PASS [confirmed]: deck panels abstract, no letters. G3 PASS
  [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera
  (three-quarter); open-mouth vocal at 2s (eyes closed = singing
  beat, in "more") and 5s (in "on"); 8s closed mouth is the
  correct post-line rest (last word "on" ends 5.38s). Arms lower
  after the last word as staged.
- G5 PASS: trim 198.38–204.72, warp 1.18. G6 PASS (plan-level).
- Beat verified: the last word lands, arms lower, push-out to
  S28.

## Volley-5 verdicts
- KEEP: S21 t1 (restage landed, flagged early onset + gap cover),
  S24 t1, S26 t1, S27 t1 (4/6 scenes). All word counts in band
  (14/14 normalized, 10/10, 4/4, 4/4); all duration ratios in
  band (0.87, 0.99, 1.20, 1.18); all motion gates pass (vocal
  mean diff 1.259–5.922, longest near-dup run 0–3f).
- REJECT: S23 t1 (G5, second "the ride is done" absent — count
  0.71); S25 t1 (G5, line delivered once — count 0.50, line
  ratio 1.99). Both kept on disk only, never chained from.
- BLOCKED: none this volley. No generation denials.
- Coverage after volley 5: S01–S22 + S24 + S26 + S27 (25/30).
  Open: S23, S25, S28, S29, S30 (5 scenes).
- Nit classes logged this volley (do not re-litigate per take):
  lavender-grey skin, strongest hue drift in the build (S25,
  past S16); warm/detailed face render (house style); added
  accessories (S21 gold epaulettes + bow tie, S23 gold epaulettes
  + collar flourish, S24 bone chest marks + gold chain, S25 gold
  chain, S26 fringed gold epaulettes, S27 gold chest panels);
  design drift (S21 BOLT round dome head + antenna ball, same
  class as S22); handheld mic (S23, S25); crowd mouths soft/open
  in background (S24, same treatment as S22); early beat (S21
  ship lands ~1s early, same class as S05's launch).
- Assembly notes carried forward: S05 t1 trim at first word
  (0.82s in); S06 t3 trim at first word (1.84s in); S10 warp 0.84
  within caps; S11 trim at 7.22s (first delivery end, repeat tail
  cut); S12 warp 1.18 within caps; S14 warp 0.85 within caps;
  S15 warp 0.89 within caps; S16 ratio 1.00; S17 warp 0.94 within
  caps; S18 t2 warp 1.06 within caps; S19 warp 0.95 within caps
  (flagged garble — master audio carries the correct words);
  S20 warp 0.96 within caps, held pose covers the 155.16–156.54
  gap lead-in; S22 warp 0.89 within caps; S21 warp 0.87 within
  caps, trim at first word (take 0.00s), place at 158.76, gap
  cover owed for 156.54–158.76 (no-word window); S24 warp 0.99
  within caps; S26 warp 1.20 within caps (near edge); S27 warp
  1.18 within caps.

## Volley-6 recommendation
- S23 t2 (DELIVERY axis — restate the repeat explicitly) + S25
  t2 (PACING axis — line twice, no long pause, whole line inside
  0.0–5.8s) + S28 t1 + S29 t1 + S30a t1 + S30b t1 (6-video cap).
- Optional on parent order only: S19 t2 (DELIVERY axis) if the
  first-half garble must be fixed; S16 t2 (HUE axis) still
  unoffered and unordered; S10 t2 (HUE axis) still unoffered and
  unordered. None recommended by default: hue drift and the S19
  garble are disclosed nit/flag classes, the takes are otherwise
  clean, and rerolls may drift again.
- After volley 6: assembly (cross-check sync method, ONE 16:9
  master, song is tempo gospel).
