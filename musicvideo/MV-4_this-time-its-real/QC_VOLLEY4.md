# MV-4 QC_VOLLEY4.md — volley 4 (S17, S18, S19, S20, S21, S22 t1 + S18 t2)

Method: frames at 2s/5s/8s (widened when reads disagree: S20 at
1.5s/3.5s for the mouth); Whisper word count vs prompted line (count ratio
AND duration ratio — song window / take vocal span, band 0.80–1.25
for both); motion audit at native 24fps, 160x90 gray (frame gate FAIL
if vocal near-dup run ≥24f during vocal OR vocal mean diff <0.5;
near-dup = mean abs diff <0.5). Prompted re-transcription
(initial_prompt = the scene's performed line, cross-check method)
run for S18 t1 and S19 t1 where the unprompted decode dropped or
garbled words. Confidence tags: [confirmed] measured, [inferred]
model-judged, [assumed] user claim. Nits are disclosed, never
promoted to fails.

## S17 t1 — KEEP
- File: takes/mv4_s17_t1.mp4, md5 de6d0a8f4d11cae69bc783bd569dac36,
  9.00s, 1280x720 h264 + AAC [confirmed].
- Whisper: 13/13 words, count ratio 1.00 [confirmed]. "They always
  joke before the ending, like they can talk the credits back." Line
  sung once. Vocal span 0.00–7.86s (7.86s) vs song 7.38s → duration
  ratio 0.94, in band.
- Motion: vocal mean diff 1.001, longest near-dup run 13f, 0 exact
  duplicates [confirmed]. Not frozen.
- G1 PASS [inferred, FLAGGED hue]: NOVA matches the bible
  (pompadour, cobalt jacket, cadmium trim, bone shirt, white gloves,
  mic on stand). FLAG — NOVA's skin renders BLUE-VIOLET, the third
  blue-shift instance in the build (S10 blue-violet, S16 blue-grey +
  red lips, S17 blue-violet). Same disclosed hue-drift nit class as
  S10/S16 — the identity lock names no skin tone, so not a G1 fail.
- G2 PASS [confirmed]: bunting, balloons, party hats, neon shapes
  are abstract, no letters; no signs.
- G3 PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera
  (three-quarter); open-mouth vocal at 2s, 5s, 8s (still inside
  "back", 7.24–7.86s). Nit: his gaze glances sideways in all three
  frames (wry read — fits the jokers' corner direction) and he leans
  on the table rather than the P-CROON lean-in; mouth visible and
  moving throughout.
- G5 PASS: trim 126.44–133.82. G6 PASS (plan-level).
- Beat verified: the jokers' corner lands (party hats, balloons,
  streamers, small round table) — bridge contrast delivered.

## S18 t1 — REJECT (G2, watermark)
- File: takes/mv4_s18_t1.mp4, md5 0f8ff6d19993f78dc6394ca026bdf270,
  9.00s, 1280x720 [confirmed]. Kept on disk only, never chained from.
- Whisper: 10/12 words unprompted (0.83) — "Will rise again, he
  keeps on safer works as otherwise." Prompted re-transcription
  recovers the FULL line, 12/12: "We'll rise again, he keeps on
  saying, but the paperwork says otherwise" — the unprompted
  "safer works as" was a Whisper mishear of "the paperwork says".
  Vocal span 0.00–6.04s vs song 6.74s → duration ratio 1.12, in
  band. Motion: vocal mean diff 1.316, longest near-dup run 5f, 0
  exact duplicates [confirmed]. Not frozen.
- G2 FAIL [confirmed]: "WuBuTV." burned into the top-left corner
  of every frame — a channel-bug watermark generated inside the
  clip. First watermark in the build (no take in volleys 1–3
  carried one). The take cannot enter the cut with burned-in text.
- G1 PASS [inferred]: NOVA consistent (warm skin, house style).
  Nits: bone-shaped epaulette decorations + bone collar marks
  (added-accessory class). G3 PASS [confirmed]. G4 PASS
  [inferred]: 3/3 face-to-camera; open-mouth vocal at 2s and 5s;
  8s closed mouth is the correct post-line rest (last word
  "otherwise" ends 6.04s).
- Beat verified: desk + blank paperwork stack delivered. The
  reject is the watermark alone — the performance is clean.
- Reroll: S18 t2, axis TEXT (one variable — the watermark named
  explicitly and banned in the framing paragraph and the footer).
  Fired in this volley as the 6th successful video (S21's denial
  does not count).

## S18 t2 — KEEP (TEXT axis closed)
- File: takes/mv4_s18_t2.mp4, md5 cf81195d78955c3bac6b761b1ffd924d,
  10.00s (requested 9s; tool returned 10.00s — recorded),
  1280x720 h264 + AAC [confirmed].
- Whisper: 12/12 words, count ratio 1.00 [confirmed]. "Will rise
  again, he keeps on saying, but the paperwork says otherwise."
  ("Will" for "We'll" is the established contraction rendering.)
  Line sung once. Vocal span 0.00–6.36s (6.36s) vs song 6.74s →
  duration ratio 1.06, in band.
- Motion: vocal mean diff 2.085, longest near-dup run 3f, 0 exact
  duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA consistent. Nits: gold epaulette bars
  (added-accessory class); red paperclip on the stack (tiny prop
  detail, pages blank); warm/detailed face render (volley-2 class);
  mic is a handheld-style mic on a stand rather than the chrome
  stand mic.
- G2 PASS [confirmed]: top-left corner CLEAN in all three frames
  — no watermark, no channel bug. Background control panels are
  abstract light blocks, no readable word. Paperwork blank.
- G3 PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera;
  open-mouth vocal at 2s and 5s (eyes closed = singing beat,
  "paperwork"); 8s closed mouth is the correct post-line rest
  (last word ends 6.36s). The 2s open mouth sits in the inter-word
  gap (1.42–2.06s) — a single-frame holdover shape, not a fail.
- G5 PASS: trim 133.82–140.56. G6 PASS (plan-level).
- Beat verified: desk + blank paperwork stack, tap after the line
  (hand rests on the desk edge at 8s).

## S19 t1 — KEEP (flagged — first-half words garbled in take audio)
- File: takes/mv4_s19_t1.mp4, md5 9c09580bbbd5fc88014b1b66f7ef4b4c,
  9.00s, 1280x720 [confirmed].
- Whisper: 16/15 words, count ratio 1.07 [confirmed]. "You can
  binge the line like muscles on your couch, quote every line like
  muscle memory." Prompted re-transcription returns the SAME garble
  — the prompt did not recover "the old ones", so the take's audio
  genuinely renders "the old ones" as "the line like muscles"
  (2.14–3.42s). Second half exact ("Quote every line like muscle
  memory"). Line sung once, no repeat, no truncation. Vocal span
  0.00–7.68s (7.68s) vs song 7.30s → duration ratio 0.95, in band.
- Motion: vocal mean diff 1.271, longest near-dup run 13f, 0 exact
  duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA consistent (warm skin, house style).
  Nit: warm/detailed face render (volley-2 class).
- G2 PASS [confirmed]: no text anywhere; the remote is a plain
  blank slab, no letters. No watermark.
- G3 PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera
  (three-quarter); open-mouth vocal at 2s, 5s, 8s (8s is 0.32s past
  the last word "memory", 7.18–7.68s — a post-line holdover).
- G5 PASS: trim 140.56–147.86. G6 PASS (plan-level).
- Beat verified: couch corner delivered (blue couch, lamp, warm
  lounge light, remote raised in hand). The mic sits on a stand
  to his left rather than beside him — staging nit only.
- FLAG: the garble is a word-identity soft spot, not a counted
  gate failure (count 1.07 and duration 0.95 both in band, motion
  passes, visuals pass) — and the master audio carries the correct
  words, the take's audio is dropped at assembly. But the mouth in
  2.14–3.42s forms a 5-syllable garble where the song has the
  3-syllable "the old ones". Parent may order an S19 t2
  (DELIVERY axis, one variable — restate the first line slowly and
  clearly, exact words repeated) in volley 5. Not fired by
  default: the volley cap is spent (S18 t2 took the 6th slot) and
  the take is otherwise clean.

## S20 t1 — KEEP
- File: takes/mv4_s20_t1.mp4, md5 430a6c4089aceb1446f16fcf939b0520,
  9.00s, 1280x720 [confirmed].
- Whisper: 13/13 words, count ratio 1.00 [confirmed]. "But the new
  one stopped at the doorstep, and the hallway stays empty."
  ("one" for "ones" is the established singular/plural
  normalization.) Line sung once. Vocal span 0.00–7.08s (7.08s) vs
  song 6.76s → duration ratio 0.96, in band.
- Motion: vocal mean diff 0.869, longest near-dup run 7f, 0 exact
  duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA consistent (warm skin, house style).
- G2 PASS [confirmed]: plain door with no number and no label,
  bare walls, no signs, no text anywhere.
- G3 PASS [confirmed]. G4 PASS [inferred]: the standard 2s/5s/8s
  samples read a closed mouth at 2s and 8s, so the sample was
  WIDENED to 1.5s/3.5s — open-mouth vocal at 1.5s ("stopped") and
  5s ("hallway", eyes closed = singing beat); the 2s closed read
  is a single-frame shape between syllables and the 3.5s closed
  read sits in the breath gap (3.46–4.00s) between "doorstep" and
  "And"; the 8s closed mouth is the correct post-line rest (last
  word "empty" ends 7.08s) with the P-HOLD arms-open pose held.
- G5 PASS: trim 148.40–155.16. G6 PASS (plan-level).
- Beat verified: empty hallway delivered (plain door, bare walls,
  cold light, doorstep empty); the arms-open hold after the line
  covers the 1.38s gap lead-in (155.16–156.54) per the plan.
- Nit: framing is wider than MCU (full body visible) — the vehicle
  asked medium shot; disclosed, not a fail.

## S21 — BLOCKED (generation denied, no take)
- Generation DENIED (integrity_check_failed), no take, not a QC or
  plan failure — the same denial class as S05 in volley 1.
  Standing instruction: never repeat that request in any form.
  S21 restages from scratch in volley 5 — fresh staging, never a
  re-fire of the denied vehicle. The final-chorus opener is the
  one open scene in the bridge block; S22 (full crew) still
  delivers the final-chorus escalation, so the chain is not
  blocked.
- The denied vehicle (mv4_s21_vehicle.txt) stays archived as-is;
  do NOT copy its staging into the restage.

## S22 t1 — KEEP
- File: takes/mv4_s22_t1.mp4, md5 65288f1888159b99b917d802ab7a6374,
  9.00s, 1280x720 [confirmed].
- Whisper: 11/11 words, count ratio 1.00 [confirmed].
  "Futurama's finished, Futurama's finished, no fresh episodes,
  that's the hard part." Line sung once. Vocal span 0.00–8.26s
  (8.26s) vs song 7.36s → duration ratio 0.89, in band.
- Motion: vocal mean diff 10.043, longest near-dup run 1f, 0 exact
  duplicates [confirmed]. Not frozen — the liveliest take in the
  build (full-crew dance).
- G1 PASS [inferred]: NOVA consistent; BOLT and ZIB match the
  bible. Nits: BOLT has a small antenna ball on his head (bible
  says no antenna ball — design drift, same class as S14's round
  head); NOVA's ears render POINTED in all three frames (design
  drift, not in the bible); NOVA's gold chain necklace + small gold
  chest diamond (added-accessory class); small bone-shaped mark on
  ZIB's tunic hem (added-accessory class, same as S04/S13).
  BOLT's chest is one smooth plain bone-white shell, no panel, no
  glyph (TEXT axis stays closed); his visor is a plain solid
  glowing band.
- G2 PASS [confirmed]: background neon panels are abstract colored
  light bars and chevrons, no letters; no name signs; confetti and
  the ringed planet are blank.
- G3 PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera;
  open-mouth vocal at 2s, 5s (eyes closed = singing beat), 8s
  (still inside "part", 7.58–8.26s). BOLT has no mouth (visor
  only); ZIB's mouth stays closed and still in all three frames;
  the crowd's mouths are soft background.
- G5 PASS: trim 166.54–173.90. G6 PASS (plan-level).
- Beat verified: BOLT and ZIB dance hard in front of NOVA, NOVA
  center at the mic, crowd at full, confetti thick, ringed planet
  through the dome — the final chorus at full.

## Volley-4 verdicts
- KEEP: S17 t1, S18 t2, S19 t1 (flagged), S20 t1, S22 t1 (5/6
  scenes). All word counts in band (13/13, 12/12, 16/15, 13/13,
  11/11); all duration ratios in band (0.94, 1.06, 0.95, 0.96,
  0.89); all motion gates pass (vocal mean diff 0.869–10.043,
  longest near-dup run 1–13f).
- REJECT: S18 t1 (G2, "WuBuTV." watermark burned top-left) —
  replaced in-volley by S18 t2 (TEXT axis, watermark named and
  banned; G2 fixed).
- BLOCKED: S21 (generation denied integrity_check_failed, no take)
  — restage owed in volley 5, fresh staging, never a re-fire.
- Coverage after volley 4: S01–S20 + S22 (21/30). Open: S21,
  S23–S30 (9 scenes). Blocked: none besides S21's restage.
- Nit classes logged this volley (do not re-litigate per take):
  blue-violet skin, third instance (S17, after S10/S16); warm/
  detailed face render (house style); added accessories (S18 t1
  bone epaulettes + bone collar marks, S18 t2 gold epaulette bars
  + red paperclip, S22 gold chain + gold chest diamond + bone mark
  on ZIB's tunic); design drift (S22 BOLT antenna ball, NOVA
  pointed ears); S17 wry sideways glance + lean-on-table; S19
  first-half word garble (flagged, see above); S20 framing wider
  than MCU + 2s closed-mouth single-frame read (widened sample
  clears it); S18 t2 mic is a handheld-style mic on a stand;
  S19 mic sits left of frame; S22 is the liveliest take in the
  build (motion 10.043).
- Assembly notes carried forward: S05 t1 trim at first word
  (0.82s in); S06 t3 trim at first word (1.84s in); S10 warp 0.84
  within caps; S11 trim at 7.22s (first delivery end, repeat tail
  cut); S12 warp 1.18 within caps; S14 warp 0.85 within caps;
  S15 warp 0.89 within caps; S16 ratio 1.00; S17 warp 0.94 within
  caps; S18 t2 warp 1.06 within caps; S19 warp 0.95 within caps
  (flagged garble — master audio carries the correct words);
  S20 warp 0.96 within caps, held pose covers the 155.16–156.54
  gap lead-in; S22 warp 0.89 within caps.

## Volley-5 recommendation
- S21 restage (fresh staging, never the denied vehicle) + S23,
  S24, S25, S26, S27 (6-video cap).
- Optional on parent order only: S19 t2 (DELIVERY axis) if the
  first-half garble must be fixed; S16 t2 (HUE axis) still
  unoffered and unordered; S10 t2 (HUE axis) still unoffered and
  unordered. None recommended by default: hue drift and the S19
  garble are disclosed nit/flag classes, the takes are otherwise
  clean, and rerolls may drift again.
- Volley 6: S28, S29, S30 (S30 = 2 takes).
