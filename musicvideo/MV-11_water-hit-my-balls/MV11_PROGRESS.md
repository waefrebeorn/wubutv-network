# MV-11 "Water hit my balls" — PROGRESS

## 2026-11-09 ~22:20 EST — coordinator start
- Intake done by parent: AUDIO_ANALYSIS.md (~131.5 BPM, dadaspec map,
  ASR correction map, Whisper loop warning 110.7–130.7s), LYRIC_TIMELINE.md
  (anchors only), lyrics.txt + suno_prompt.txt verbatim, track.mp4 md5
  18273d7a593e623b720105df195bede2, 172.42s.
- Plan written: work/MV_PREPRO_MV-11.md — 23 scenes, motif THE SPLASH
  (returns every hook), peak S20/S21 (loudest 2s at 158s), bridge
  contrast S16 Drop freeze, final frame S23 rhymes with S01.
- Character lock + asset board written. One sung scene only (S07 verse,
  in-world side/back, never to camera). All chant = montage/kinetic.
- Volley 1 (6): S03 (HOOK TEST, first), S01, S02, S04, S05, S07.
- Next: generate 2 anchor stills (man + bowl), read back, write
  vehicles, fire S03 first and QC the look before the rest.

## 2026-11-09 ~22:30 EST — volley 1 DONE: 5 KEEP / 1 REJECT
- Anchors generated + read back: anchor_man (md5 dc24cd4e…, man in blue
  bathrobe, side/back, teal tiles, vermilion towel, duck — lock exact),
  anchor_bowl (md5 c48c1079…, splash crown, cobalt water, duck — lock
  exact). Both 2048x1152, copied to canonical names.
- Vehicles written (6): mv11_s01/s02/s03/s04/s05/s07_vehicle.txt.
- HOOK TEST (S03 t1): PASS — frame-0 anchor lock, motion escalates
  across the take, duck surfing the crest at 9.5s. Plan's look proven;
  the rest of the volley fired on it.
- Volley 1 fired (6/6 cap): S03, S01, S02, S04, S05, S07 — all
  1248x704 h264, exact requested durations (10.000/5.000s).
- KEEPS: S01 (drop+crown at frame 0, calm tail fits cold open), S02
  (room revealed mid-take — assembly trims the duck-close-up tail),
  S03 (hook test), S04 (rings, subtler than prompted — contrast
  inside Hook 1), S05 (reverse splash lands at 2.5s, droplets hanging).
- REJECT: S07 t1 — G5 fail, wrong phrase. Take audio transcribes as
  an invented YouTube outro ("This is the end of this video, thank
  you so much for watching…"), not the verse line. Mouth moves on the
  wrong words; onset closed. The look itself is right (side/back,
  bathrobe, profile mouth) — the words are wrong. Vehicle v2 written
  (lyric-completeness rewrite, explicit ban on any other speech).
  S07 t2 owed in volley 2. This is exactly the "weird talky" the
  user banned — it does not ship.
- Dadaspec rules confirmed by parent (dadabots post, Oct 29 2026):
  vertical seams = stop-start lurches (dark band ~107s = Drop
  silence, visual event as planned); dense+loud saturates white
  (saturated tail 125s→170s = Final Hook, peak there as planned).
  No plan change.
- NEXT VOLLEY (volley 2, 6): S07 t2 (v2, first), S06, S08, S09, S10, S11.
  Then volley 3: S12–S17. Volley 4: S18–S23 (6 scenes — fits the cap).

## 2026-11-09 ~23:05 EST — volley 2 DONE: 5 KEEP / 1 REJECT
- Vehicles written (5): mv11_s06/s08/s09/s10/s11_vehicle.txt. S07 t2 fired
  on the existing v2 vehicle (first, per plan).
- Volley 2 fired (6/6 cap): S07 t2, S06, S08, S09, S10, S11 — all
  1248x704 h264. S08 returned 10.000s against a 5s request (assembly
  uses the first ~5.1s); the rest exact (5.000/6.000s).
- KEEPS: S06 (brass light-flashes, gold wash tail), S08 (snare build,
  steady push-in to the bowl), S09 (two crowns in turn — pickup reads
  exactly as planned), S10 (water ballet — arc + duck surfing; tail
  drifts to a front-facing open-beak duck close-up, assembly trim
  option noted), S11 (dive + surface, bubbles + light rays, ready for
  Hook 2).
- REJECT: S07 t2 — G5 fail, lyric incomplete. Sings "Sitting on the
  toilet, water hits" then silence: "My balls" never performed (audio
  silent 4.18–5.0s, mouth closed at 4.5s; split-half recheck confirms).
  Framing/mouth on the sung phrases are good — the tail phrase is
  simply missing. Two denied rerolls = scene RETIRES per the skill:
  v3 is a RESTAGE from scratch (phrase-bracketed windows, mandatory
  last phrase, slow push-in; work/vehicles/mv11_s07_vehicle_v3.txt),
  owed in volley 3 — never a third pull of the v1/v2 vehicle.
- QC METHOD NOTE: a single multi-input ffmpeg frame-extraction command
  returns frame 0 for every output — first S07 t2 sheet was four copies
  of frame 0 and briefly misread as frozen. One frame per invocation
  from now on, md5s verified distinct; motion measured numerically
  (mean abs-diff) + eye-read.
- NEXT VOLLEY (volley 3, 6): S07 t3 (v3 restage, first), S12, S13, S14,
  S15, S16. Then volley 4: S17–S22. Volley 5: S23 (final drop).

## 2026-11-09 ~23:20 EST — volley 3 firing: S07 t3 KEEP (restage PASS)
- S07 t3 (v3 restage, anchor_man): all three phrases sung, in order,
  exactly once — "Sitting on the toilet" 0.00–1.96, "Water hits"
  2.18–3.32, "My balls" 3.32–4.38. Mouth wide open on "Water" (2.15),
  opening/open on "My balls" (3.65/4.5). "Sitting" onset is in the wide
  push-in head (mouth unreadable at distance, open by 1.5s) — disclosed
  line-start lag. Warps ~1.05x/1.28x/1.42x slow, within cap. Motion
  underway by 0.5s; near-still head ~0.25s only. THE VERSE IS COVERED.
- Vehicles written (5): mv11_s12/s13/s14/s15/s16_vehicle.txt.
- Firing next, in order: S12, S13, S14, S15, S16.

## 2026-11-09 ~23:4x EST — volley 3 DONE: 6 KEEP / 0 REJECT
- S07 t3 KEEP (restage PASS — see above; the verse is covered, no fourth
  S07 take owed).
- S12 t1 KEEP — twin crowns, duck riding the second crown at its apex
  (7.5s). Returned 10s vs 8s requested; use first ~8s.
- S13 t1 KEEP — rings multiplying, duck spinning in the centre, steam.
  Returned 10s vs 8s requested; use first ~8s.
- S14 t1 KEEP — tall column at 0.5–1.0s, then thick rain with rings
  blooming. Returned 10s vs 8s requested; use first ~8s.
- S15 t1 KEEP — reverse splash, water climbs the bowl walls, highest
  climb at 6.5s. Returned 10s vs 7s requested; use first ~7s.
- S16 t1 KEEP — the Drop: crown holds, shatter, duck LAUNCHED to the
  top of its arc by the window, room flashing gold. Returned 10s vs 9s
  requested; use first ~9s. The shot of the build so far.
- Recurring note: S12/S15/S16 take audio contains "Thanks for watching!"
  (a generator outro artifact) — NO visual counterpart in any of them
  (no people, no mouths); take audio is discarded in assembly. S13/S14
  take audio is clean (no words).
- MV-11 running total: 16 KEEP / 2 REJECT; S01–S16 ALL COVERED.
- NEXT VOLLEY (volley 4, 6): S17, S18, S19, S20, S21, S22. Volley 5: S23
  (final drop). Then QC → assembly → delivery.

## 2026-11-10 ~00:16 EST — volley 4 DONE: 5 KEEP / 1 REJECT
- S17 t1 KEEP — Final Hook opens at full power: biggest splash yet,
  duck surfing the crest, 7.5–9.5s tight on the duck riding the crest.
  Motion strong (42.4). Take audio ZERO words.
- S18 t1 KEEP — the wave: bowl overflowing in a huge sheet over the rim,
  water cascading to the floor, duck riding the overflow. Motion strong
  (47.5). Take audio ZERO words. Disclosed: camera moves between angles
  instead of one continuous circling shot; frame 0 near-identical to
  S17's frame 0 (anchor-still pattern).
- S19 t1 KEEP — the strobe of rings: concentric rings multiplying, duck
  spinning in the centre, widest ring reaching the bowl's edge. Motion
  strong (40.1). Take audio ZERO words. Disclosed: tile hue wobbles
  teal → purple (~2.5s) → deep blue (~7.5s) → teal (documented
  hue-drift class, layout holds); gold lamp pulse weak (strobe reads in
  the rings, not the light).
- S20 t1 KEEP — the peak climb: massive column, duck riding the top as
  water explodes outward, tiles flashing gold and cobalt. Motion strong
  (42.3). Take audio: one non-lexical "Oh" 0.00–2.00 only, no visual
  counterpart. Disclosed: camera stays tight from 5.0s (bowl out of
  frame); rings element absent here (rings live in S19/S21).
- S21 t1 KEEP — THE PEAK: enormous crown erupts, holds at its apex
  3.0–4.0s with the duck on top and the lamp blazing — the money shot.
  Returned exactly 5.000s as requested; use first ~4.1s (slot 4.06s).
  Take audio "Thank you for watching!" — recurring generator outro
  artifact, NO visual counterpart. Disclosed: duck rides belly-down /
  half out of frame during the rise (1.0–2.0s); crown collapses by 4.9s
  leaving the duck floating mid-air — OUTSIDE the assembly window.
- S22 t1 REJECT — G1 FAIL, bowl identity: the settle reads (water calms,
  rings widen/fade, duck drifts to centre, lamp softens to amber) but
  the porcelain rim renders ORANGE-GOLD instead of bone white,
  persisting 2.5–10s — uniform even away from the lamp and after the
  lamp leaves frame, so it is the porcelain, not the light. A white →
  orange → white bowl across S21/S22/S23 would be a continuity break in
  the outro. REROLL AXIS: BOWL IDENTITY (bone-white porcelain, warm
  amber light on water/tiles only, rim stays white). No reroll possible
  inside volley 4 — the 6-generation cap was spent (S17–S22 t1).
- MV-11 running total: 21 KEEP / 3 REJECT; S01–S21 ALL COVERED.
- NEXT VOLLEY (volley 5, 2 generations): S22 t2 (reroll, bowl-identity
  axis) + S23 OUT-B "Last Drop" (final frame rhymes with S01). Then
  QC → assembly → delivery.

## 2026-11-10 ~00:40 EST — volley 5 DONE: 2 KEEP / 0 REJECT — ALL 23 SCENES COVERED
- S22 t2 KEEP — BOWL IDENTITY FIXED. The v2 reroll axis worked: the
  porcelain rim reads BONE WHITE at 0, 2.5, 5.0, 7.5 and 9.5s (t1's
  orange-gold rim is gone). Settle reads: crown collapses by 2.5s,
  rings widen/fade, duck drifts to centre and sits still. Motion
  strong through 8.5s (overall 18.2); tail windows 1.7/1.6 in the
  final 1s — deliberate calm, not a freeze. Take audio ZERO words.
  Disclosed: tiles warm to amber-orange from ~5s (lamp softening —
  amber LIGHT on tiles/water, porcelain stays white).
- S23 t1 KEEP — THE LAST DROP. Single drop falls with a small crown
  at ~3.5s, one last ring blooms and fades, duck still in the centre,
  water back to glass by 6.5s — the final frame rhymes with S01's
  opening (calm bowl, duck centred, lamp warm). Motion strong
  in-window (mean 24.7, min 3.07). Take audio ZERO words. Returned
  10s vs 7s requested — ASSEMBLY: use first ~7.4s only (slot 7.36s).
  Disclosed: head 0–2s replays the anchor crown (near-identical to
  S22 t2 frame 0 — documented anchor-still pattern); assembly note:
  S22-tail → S23-head cut goes calm → crown — trim the head to start
  on calm water ~2s, or keep the crown head as a deliberate echo of
  S01's opening.
- MV-11 running total: 23 KEEP / 3 REJECT; S01–S23 ALL COVERED —
  every planned scene holds a KEEP. NO volley owed.
- NEXT: QC pass over the full ledger → assembly → delivery.
  Assembly notes carried forward: S08 use first ~5.1s; S12–S16 use
  first ~8/8/8/7/9s; S21 use first ~4.1s; S23 use first ~7.4s
  (head-trim option on the crown, see above); S22 t2 + S23 rims are
  bone white throughout.
