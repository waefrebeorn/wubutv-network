# MV-8 v3 — TAKE LEDGER v3 (montage-first rebuild)

Plan: `work/rebuild/SCENE_PLAN_v3.md`. 28 fresh v3 takes planned
across 5 volleys of ≤6. Naming: `takes/<scene>_v3[_c<n>].mp4`.
QC gates per take: G1 adult identity (face vs still chain, adults
only), G2 zero on-screen text (full-res scan), G3 no licensed
material, G4 motion-from-frame-0 (MOTION LAW — no frozen run ≥24f
during words), G5 aspect 16:9 + duration measured by ffprobe.
**No-reuse rule: every take md5 in the cut has use-count 1 —
audited at assembly before encoding.**

Singer inserts are NOT fired takes — they are v2 takes used once as
montage cutaways (see SCENE_PLAN_v3.md § Inserts). Their rows live
in the INSERTS table below, not the takes table.

## Fresh takes

| Take | Scene | Song span | File | md5 | Dur | Verdict | Notes |
|---|---|---|---|---|---|---|---|
| IN-A_v3 | IN-A | 0.00–5.97 (instr.) | takes/IN-A_v3.mp4 | f1cb7cda0271789c75f1daf791cb7bcd | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Bathroom → sheet flies → marker zigzag draws itself → foam vortex. Motion min 28.0/mean 43.9, frozen run 1f. Opens mid-action. No text, no child. DISCLOSED: marker stroke reads as a W-like zigzag at full res (drawn stroke, not text — same class as v2 IN-A); tail 6.5–10s is a vortex hold outside the 5.97s span (assembly trims). |
| H1-A_v3_city | H1-A | 5.97–22.08 | takes/H1-A_v3_city.mp4 | aa4542c561f0184189598850f1b635fe | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Sheet flight over porcelain city, opens mid-flight. Motion min 53.1/mean 58.6, frozen 0f — strongest of the volley. Adult Champion from behind/side, braid; no mouth work (montage take). No text. DISCLOSED: style reads glossy 3D cartoon rather than flat 2D (anchor-pull); world/character/palette consistent; montage tolerates (C2). |
| H1-B_v3_browns | H1-B | 22.08–34.96 | takes/H1-B_v3_browns.mp4 | abe081006e14807c8ad681e4a729cb8f | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP (trim)** | Five brown spheres bounce, squash-and-stretch, yellow flash rings on landings. Motion mean 72.6, frozen 2f. No text, no people. DISCLOSED: opens slow — first 0.5s diff 5.1, bouncing starts ~1.0s; assembly trims in at 1.0s; tail zoom loses the five-count after ~7s (use 1.0–7.0s). |
| H2-C_v3_clog | H2-C | 93.00–105.94 | takes/H2-C_v3_clog.mp4 | cc0e96329c605478d61965a28ad4f0e9 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP (trim)** | Clog shudders, cracks, breaks apart. Motion mean 49.2, frozen 0f. Adult, wardrobe on-lock (TP-roll breastplate, long trousers, yellow gloves). No text. DISCLOSED: action completes ~8s; tail 8–10s is an exhausted hold (mouth open gasping — effort, not song; audio dropped); assembly uses 0–8s. |
| O-A_v3_approach → APEX WINDOW | O-A | 146.00–163.00 (instr., true peak 159.435s = frame 3826) | takes/O-A_v3_approach.mp4 | 8c757b63c2050da5f350fe5e72e0d580 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP — RE-DESIGNATED as the apex-window take** | Crest measured BY EYE at ~6.1s (take frame ~146; 12fps strip frames 13–16, 6.0–6.25s). Trim-in = 6.1 − 3.435 ≈ 2.67s; used span 2.67–9.67s = 7.00s ✓; dive tail good. Swirl mount CORRECT. Motion min 32.6/mean 41.2, frozen 0f. No text, no child. DISCLOSED: 3D-ish style; ring reads as a water arch (crest = top of the arch — measurable and placeable). NOT usable as the approach: crest margin ~0.1s — the approach would end on the crown and the cut to the apex window would jump backward. |
| O-A_v3_apex | O-A | 146.00–163.00 (instr.) | takes/O-A_v3_apex.mp4 | ca7b3ab7854ed94a9ce76e8ddafe2582 | 10.000s, 1248x704, 24fps, h264+AAC | **REJECT — mount identity** | Crest ~4.6s (placeable by trim: trim-in ≈ 1.17s) BUT the mount is a HORSE, not Sir Swirl — G1 fails at the video's biggest visual. The G14 anchor shows the swirl; the model substituted a horse (the approach take proves the model CAN render the swirl). Motion min 24.2/mean 37.6, frozen 0f; otherwise strong (full dive into the vortex). Retained on disk as a rejected take; NEVER used in the cut. |
| O-A_v3_approach_c2 | O-A | 146.00–163.00 (instr., true peak 159.435s = frame 3826) | takes/O-A_v3_approach_c2.mp4 | 13a2a65f8314e9517446ca28b1b41447 | 10.000s, 1248x704, 24fps, h264+AAC | **REJECT — mount identity** | SECOND horse substitution on an O-A vehicle (same failure as V1 apex): the mount is a HORSE throughout (horse head, mane, legs — contact sheet + 12fps strip) — G1 fails at the video's biggest visual. Crest ~7–8s by eye (sheet tiles 14–16) but the mount fails first, so no precise crest measurement was taken. Motion min 25.4/mean 38.4, frozen 0f; RMS −23.5 dB. Whisper: "Thanks for watching!" hallucination 6.0–9.5s only — no lyric content (generated audio dropped at assembly). Retained on disk as a rejected take; NEVER used in the cut. LESSON: verbatim re-pull does NOT fix the mount — V3 re-fires the approach on a CHANGED axis (explicit "NOT a horse — no horse head, no mane, no legs, no tail; the mount is a glossy chocolate soft-serve swirl with a rounded swirl top and aviator goggles"). |
| H1-A_v3_smears | H1-A | 5.97–22.08 | takes/H1-A_v3_smears.mp4 | 3cb5508365d30fd4c5c5722acd2f172f | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Yellow-gloved hands wipe glossy brown smears blooming and spreading across white porcelain tiles; smears pulse and regrow behind the wipe. Motion min 27.2/mean 70.6, frozen 1f. No text (full-res 5s frame: smears are swirls, not letters), no people. RMS −30.9 dB. DISCLOSED: golden city bleeds in at the frame edges in the tail (rows 3–4); the sheet's marker stroke is not prominent — the event is the smears + wipe, which is the brief. |
| H1-B_v3_steps | H1-B | 22.08–34.96 | takes/H1-B_v3_steps.mp4 | 7784dd5c4439cb482298c90c359afa09 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP (trim)** | TP roll bounces down the golden palace steps with squash-and-stretch, unspooling a paper ribbon, lands in the plaza with a wobble. Motion min 13.1/mean 63.1, frozen 0f. No text, no people. RMS −21.8 dB. DISCLOSED: glossy-3D read (same anchor-pull as V1 flight takes — montage tolerates, C2); tail settles after ~8.5s (0.5s diffs fall to 13.1) — assembly uses 0–8.5s. |
| I-A_v3_fibres | I-A | 34.96–45.51 | takes/I-A_v3_fibres.mp4 | ece27116ac581def3eca41a853cded00 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Drifting white fibres, glowing golden threads pulsing in a rolling wave, chocolate river + brown blobs below, sparkling light dust. Motion min 30.8/mean 39.3, frozen 0f. No text, no people. RMS −32.2 dB. DISCLOSED: close, slow-drifting framing — the river reads as a chocolate field more than a river in this framing; the event (fibres + glowing threads) is on-brief. |
| I-B_v3_river | I-B | 45.51–60.46 | takes/I-B_v3_river.mp4 | fa99f7a23712bfc9ba1fc6bdb2c8ceb2 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Fast flight down the chocolate river, banks into the storm cluster (lightning flash ~2.5–3s), bursts out into golden light, river straightens toward the sunset. Motion min 19.1/mean 47.7, frozen 0f. No text, no people. RMS −18.2 dB. |
| V-0_v3_throne | V-0 | 60.46–65.12 | takes/V-0_v3_throne.mp4 | ed3e3f302ec8679685667dc75f8e2952 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Champion in full TP armour heaves the tall golden plunger high and slams it down, golden ring flash, throne lid claps, choir of toilets answers; she stands with the plunger as the plaza glows. Adult woman, mature face (full-res 5s frame eye-checked), braid, wardrobe on-lock. Motion min 13.8/mean 49.7, frozen 0f (opens mid-swing — already moving). No text. RMS −20.7 dB. Whisper: "Thank you for watching!" hallucination 7.2–10s only — no lyric content (generated audio dropped at assembly). DISCLOSED: the throne reads as an ornate chair in the close shots and the slam lands on the chair arm, not a visible toilet lid — the lid-clap beat is carried by the kinetic SLAM + ring flash, not a literal lid; one angle change mid-take (row 2) reads as a cut — montage tolerates. |
| O-A_v3_approach_c3 | O-A | 146.00–163.00 (instr., true peak 159.435s = frame 3826) | takes/O-A_v3_approach_c3.mp4 | da9f127de63104bf18c486a95e1b0087 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Third pull on the CHANGED axis WORKED — mount is Sir Swirl throughout (glossy chocolate soft-serve swirl, curled swirl top, aviator goggles, cream scarf; no horse head, no mane, no legs, no tail anywhere — full-res 5s frame confirms). 12fps strip: climb only, NO crest — she stays below the crown to the last frame, ring towering above her at 10s. Motion min 27.6/mean 38.6, frozen 0f. No text, no child. RMS −25.3 dB. Whisper: "Hold on, Sir Swirl!" 5.88–7.26s only — generated speech, not a lyric (instrumental scene; audio dropped at assembly). DISCLOSED: glossy-3D read (same anchor-pull as V1 flight takes — montage tolerates, C2); tail has her passing into the ring's lower opening while still below the crown. |
| PH-A_v3_arming | PH-A | 65.12–67.26 (L11) | takes/PH-A_v3_arming.mp4 | 2d1d09a11868f19a0cb662b895195595 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP (trim)** | Armour pieces fly in with golden flashes, plunger arrives, Champion ends in full armour in the throne plaza, toilet choir clapping. Motion min 8.2/mean 33.5, frozen 1f — motion drops to ~8.3 in the 5.5–10s tail (static hold after arming completes); assembly uses **2.5–4.6s** (pieces snapping on with flashes). Adult face verified at full res (mature, braid). No text (banners blank). RMS −20.4 dB. Whisper: "Thanks for watching!" hallucination only — no lyric content. DISCLOSED: armour reads metallic plate in the close shots (TP rolls visible on the breastplate in the wide); throne reads as a chair (same as V-0). |
| I-A_v3_chocoriver | I-A | 34.96–45.51 | takes/I-A_v3_chocoriver.mp4 | 41c83ebae3d98825e639de45c5243a58 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Gliding flight low over the chocolate river, brown blobs drifting downstream, white fibres drifting overhead, glowing golden threads pulsing in a rolling wave. Motion min 38.3/mean 46.0, frozen 0f — strongest motion of the volley. No text, no people. RMS −28.6 dB. |
| I-B_v3_gate | I-B | 45.51–60.46 | takes/I-B_v3_gate.mp4 | 839705b771a2a50df1617d8fc45a5fd3 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Flight down the river past TP-roll banks, gate grows and swings open, golden city + fountains beyond; ends ON the open gate with the city. Motion min 34.1/mean 51.2, frozen 0f. No text (bunting blank), no people. RMS −24.0 dB. DISCLOSED: glossy-3D read in the city shots (same anchor-pull class as the flight takes). |
| H2-A_v3_departure | H2-A | 67.26–81.08 | takes/H2-A_v3_departure.mp4 | 46a6a3469cca28b3503172a47a0cba6a | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Champion mounted on Sir Swirl (swirl CORRECT: curled cream top, goggles, cream scarf — no horse), Squire running alongside with satchel, departure through the gate to the golden road. Motion min 39.7/mean 57.1, frozen 0f. Adult faces verified at full res. No text (banners carry abstract emblems, not letters). RMS −25.2 dB. Whisper: generated dialogue ("Right then, we'd better be off before the guards change shift" / "Let's go, sir Swirl. Time to hit the road.") — not lyric content; montage take, audio dropped at assembly. |
| H2-A_v3_ribbon | H2-A | 67.26–81.08 | takes/H2-A_v3_ribbon.mp4 | 7acbb1d5155fb6daf14329fb09989a6d | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Quest map unrolls, glowing golden-brown ribbon unfurls and races over the porcelain city rooftops to the golden horizon. Motion min 35.0/mean 57.4, frozen 0f. No text, no people. RMS −26.0 dB. DISCLOSED: banner emblems are abstract flourishes, not letters; ribbon reads golden-brown rather than pure brown in the aerials. |
| H2-B_v3_pupil | H2-B | 81.08–93.00 | takes/H2-B_v3_pupil.mp4 | d8d733f4e432e4c360e72a1390ac586b | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Eye → pupil dive (loose-prompt slot): camera dives into the giant chocolate eye, pupil swirls open, glowing abstract neon rings + blobs pulse inside. Motion min 27.0/mean 54.4, frozen 0f. No people. RMS −25.7 dB. **F12 GLYPH WATCH CLEAR:** full-res 5s frame + full contact sheet eye-read — pupil reflections are abstract rings/blobs only, NO readable letters anywhere. DISCLOSED: tail (7.5–10s) is a golden glow-burst as the dive bottoms out — the eye itself is gone by then; assembly uses 0–7.5s. |
| H2-B_v3_canal | H2-B | 81.08–93.00 | takes/H2-B_v3_canal.mp4 | faf3c828c14ea874e8bafb5185c577a0 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Night canal: toilet-seat boats drift and bob down the chocolate river, golden plunger lanterns, abstract neon rings/blobs in the sky, camera gliding low over the river toward the golden glow. Motion min 42.5/mean 48.1, frozen 0f — steadiest motion of the volley. No text, no people. RMS −28.4 dB. DISCLOSED: a few neon rings read cyan/teal (one small red) in the tail — palette drift off the yellow-sole-accent lock; the shapes stay abstract, never letters. |
| H2-C_v3_gate | H2-C | 93.00–105.94 | takes/H2-C_v3_gate.mp4 | 59677c1fb2d3862ea73940d118cc27bf | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Champion mounted on Sir Swirl (swirl CORRECT: curled top, goggles strap, cream scarf — no horse) rides through the great porcelain gate into the golden city, fountains, yellow bunting. Motion min 33.5/mean 53.4, frozen 0f. Adult (from behind, braid, TP rolls on back), wardrobe on-lock. No text (bunting blank). RMS −24.7 dB. Whisper: "Thanks for watching!" hallucination 6.66–9.68s only — no lyric content (generated audio dropped at assembly). DISCLOSED: glossy-3D read in the city shots (same anchor-pull class as the flight takes). |
| D-A_v3_duel | D-A | 105.94–112.25 (Drop shout) | takes/D-A_v3_duel.mp4 | bfd1177dc4de38523f5c1cd2f77e7ba7 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Vortex duel: Champion on Sir Swirl lunges into the golden vortex vs the Brown Ribbon Serpent (smug dot eyes, no goggles), TP scraps + spray flying, camera swinging with the duel. Motion min 36.5/mean 62.7, frozen 2f. Adult, wardrobe on-lock. No text. RMS −17.9 dB. Whisper: generated dialogue "You won't get past me!" 7.46–8.96s — not lyric content (generated audio dropped at assembly). DISCLOSED: she dismounts mid-take and wrestles the serpent on foot in the middle section (reins in hand); the take opens mounted and closes in face-off — assembly uses the mounted opening and/or the closing face-off, not the wrestling middle. |
| D-B_v3_serpent | D-B | 112.25–120.06 (hit pair) | takes/D-B_v3_serpent.mp4 | 03f28b194be72b056fc630b44f5cd04c | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Serpent close-up: camera pushes in fast on the smug grinning face as it lunges, ribbon body whipping in the golden vortex, TP scraps flying. Motion min 45.1/mean 58.0, frozen 1f — strongest motion floor of the volley. No text, no people. RMS −18.9 dB. DISCLOSED: none — cleanest take of the volley. |
| FH-A_v3_flush | FH-A | 120.06–133.46 | takes/FH-A_v3_flush.mp4 | 549de0e0556f2bed6beaeddda4162f40 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Synchronised flush: every white toilet flushes at once in the throne plaza, water arcing gold, Champion raises the tall golden plunger, toilet choir clapping. Motion min 49.6/mean 59.4, frozen 0f. Adult face verified at full res (mature, braid). RMS −24.0 dB. Whisper: no words at all. DISCLOSED: bunting sheets carry faint abstract doodle-marks (same class as V3 departure banners — emblems, not letters); throne reads as an ornate chair (same as V-0). |
| FH-A_v3_paperstorm | FH-A | 120.06–133.46 | takes/FH-A_v3_paperstorm.mp4 | 1c494f58c4da1ef35820e189381d45ea | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Paper storm: Champion rides a flying toilet-paper sheet over the porcelain city, brown smears bloom and fade on the tiles below, golden flashes. Motion min 39.9/mean 58.4, frozen 0f. Adult (mature face, braid), wardrobe on-lock. No text (smears are swirls/blobs, not letters; banners blank). RMS −23.6 dB. Whisper: no words at all. DISCLOSED: none. |
| FH-B_v3_pipeflight | FH-B | 133.46–146.00 | takes/FH-B_v3_pipeflight.mp4 | b3b774918332114a4cc05dae56fccbf1 | 10.000s, 1280x720, 24fps, h264+AAC | **KEEP** | Pipe-flight victory lap: Champion rides Sir Swirl (swirl CORRECT: curled chocolate top, goggles, cream scarf — no horse head, no mane, no legs, no tail anywhere) banking and swooping through golden pipes above the porcelain city. Motion min 47.1/mean 65.7, frozen 0f. No text (banner emblems are abstract circles, not letters). RMS −20.8 dB. Whisper: no words at all. DISCLOSED: glossy-3D read (same anchor-pull as V1 flight takes — montage tolerates, C2); 1280x720 not 1248x704 (both 16:9 — assembly conforms). |
| FH-B_v3_citizens | FH-B | 133.46–146.00 | takes/FH-B_v3_citizens.mp4 | 85b81272d36b71f8c80d051e11f3e503 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Citizens wave and cheer, Champion raises the tall golden plunger, brown ribbon unfurls over the rooftops to the horizon, purple phantom shimmer flickers across the plaza. Motion min 20.5/mean 50.9, frozen 0f. Adults only (crowd verified). No text (ribbon gold pattern is abstract flourish, bunting blank). RMS −25.4 dB. Whisper: "Oh!" 0–0.64s only — crowd exclamation, p 0.03, not lyric content (generated audio dropped at assembly). DISCLOSED: phantom flicker reads purple (off the yellow-sole-accent lock — a ghost shimmer, montage tolerates); motion eases in the tail (0.5s diffs fall to ~20 in the last 2s) but never freezes. |
| O-B_v3_dam | O-B | 163.00–180.00 | takes/O-B_v3_dam.mp4 | 4b8aa703db6a80690635f40ce0fd0c53 | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Colossus dam: heavy-lidded eyes open wide, cracks spread with golden light seeping through, water pressing behind, Champion tiny on the rim with plunger raised, camera pushing in. Motion min 9.4/mean 29.3, frozen 1f. Adult face verified at full res (mature, braid). No text. RMS −21.0 dB. Whisper: "Hold together." 7.5–8.76s — generated speech, not lyric content (generated audio dropped at assembly). DISCLOSED: Champion's skin renders bright yellow in the close shots (style drift, same anchor-pull class — montage tolerates, C2); motion drops to ~9–17 in the 7–10s tail (slow push-in, never frozen). |
| O-B_v3_wave | O-B | 163.00–180.00 | takes/O-B_v3_wave.mp4 | 01c377d6cd0f4e4950b90a8d50c3760b | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Tidal wave: Champion surfs the wave standing on a white toilet seat, tall golden plunger raised, districts washing clean with fountains bursting below. Motion min 50.4/mean 54.6, frozen 0f — steadiest motion of the volley. Adult, wardrobe on-lock. No text. RMS −18.5 dB. Whisper: "We did it!" 1.64–3.26s — generated speech, not lyric content (generated audio dropped at assembly). DISCLOSED: the seat reads as a white board with a toilet-seat shape (matches G12); her mouth is open in a triumph shout (montage take, not a sung line). |
| O-C_v3_ghostwipe | O-C | 180.00–187.20 | takes/O-C_v3_ghostwipe.mp4 | 8bd2e38c36f825c6542878047e397ddd | 10.000s, 1248x704, 24fps, h264+AAC | **KEEP** | Ghost Wipe reveal: glowing clean sheet floats above the sink, Squire swoons, sheet dissolves into a golden flush vortex, pull-back to the opening bathroom with yellow gloves reaching — final frame rhymes with G00. Motion min 11.0/mean 39.8, frozen 1f. Adult Squire verified at full res. No text. RMS −37.7 dB (quietest of the volley; generated audio dropped at assembly). Whisper: no words at all. DISCLOSED: opens slow (first 0.5s diff 11.0 — the sheet shimmer builds; still moving from frame 0, no frozen run); assembly trims the 10s take to the 7.20s scene span. |

## Singer inserts (v2 takes, each used ONCE in the whole v3 cut)

| # | Source v2 take | md5 | Song window | Lines | Warp | Assembly eye-verdict |
|---|---|---|---|---|---|---|
| INS-1 | takes/H1-A_v2_c1.mp4 | 038bcb6e6f03f9ac54222541ea5d6f37 | 7.98–16.12 | L1+L2 | 0.99 / 1.22 | (at assembly — mouth re-verified on warped render) |
| INS-2 | takes/H1-B_v2.mp4 | 9b4ecad69db38dccd21372ee7947154d | 28.62–29.98 | L6 | 0.85 | (take span 4.0–5.6s only) |
| INS-4 | takes/V-0_v2.mp4 | cd2e25fc04eff15551b04d6ae899af05 | 63.00–65.00 | L10 | 0.93 | (take span 1.98–4.14s only) |
| INS-5 | takes/H2-A_v2.mp4 | 1a32c173ee5ecab6196c8df8e4a0840e | 67.38–73.00 | L12+L13 | 0.84 / 1.18 | (take span 0.0–5.76s only) |
| INS-6 | takes/H2-B_v2.mp4 | ae6ac6992671a5285ee4354b49cd875a | 81.66–88.98 | L16+L17 | 0.96 / 1.35 grey | (re-verify mouth on warped render) |
| INS-7 | takes/FH-A_v2.mp4 | d8feb2c833c915631cbcc0e3a96f2681 | 120.06–123.18 | L20 | 1.16 | (take span 0.0–2.68s only) |

## Volley log

- **V1 COMPLETE (this run, 2026-11-09 ~03:0x–03:4x EST): 5/6 KEEP + 1
  REJECT.** IN-A_v3 KEEP · H1-A_v3_city KEEP · H1-B_v3_browns KEEP
  (trim-in 1.0s) · H2-C_v3_clog KEEP (use 0–8s) ·
  O-A_v3_approach KEEP re-designated as the APEX-WINDOW take (crest
  ~6.1s, trim-in ≈2.67s) · O-A_v3_apex REJECT (horse mount, not Sir
  Swirl). Videos used this run: 6/6 (cap). QC: ffprobe (all 1248x704
  24fps 10.000s h264) + motion audit (v2-style 0.5s diffs + native-fps
  frozen-run check, longest run 0–2f — all PASS) + contact sheets eye-read
  + full-res text scan (IN-A zigzag mark: drawn stroke, not text) +
  12fps crest strips for both O-A takes. QC tooling:
  work/rebuild/qc/qc_v3_volley1.py. Note: ffmpeg 8.1.2 signalstats
  emits no YDIF output on this build — motion is numpy/PIL frame-diff
  (v2 method + native-fps frozen-run check); do not waste time on
  signalstats again.
- **V2 COMPLETE (recovery run, 2026-11-09 ~03:4x–04:1x EST): 5/6 KEEP + 1
  REJECT.** O-A_v3_approach_c2 REJECT (horse mount AGAIN — second O-A horse
  substitution; approach role still open, V3 re-fires on a CHANGED axis, not
  verbatim) · H1-A_v3_smears KEEP · H1-B_v3_steps KEEP (use 0–8.5s) ·
  I-A_v3_fibres KEEP · I-B_v3_river KEEP · V-0_v3_throne KEEP. Videos used
  this run: 6/6 (cap). Stills first: G01, G03, G04, G05 generated +
  eye-verified, all 2048x1152, canonical JPGs in work/rebuild/stills_v3/
  with md5s in STILL_CHAIN_v3.md (G01 79788c8c…, G03 d3a92978…, G04
  8796bb52…, G05 2e26bffa…). QC: ffprobe (all 1248x704 24fps 10.000s
  h264+AAC) + motion audit (v3_volley2 script; longest frozen run 0–1f —
  all PASS) + contact sheets eye-read + full-res text scan (smears = swirls,
  not letters; V-0 adult face verified at full res) + RMS on all six
  (−18.2 to −32.2 dB) + Whisper on the two takes with people (V-0, O-A c2:
  only "Thanks/Thank you for watching!" hallucinations — no lyric content;
  generated audio is dropped at assembly). QC tooling:
  work/rebuild/qc/qc_v3_volley2.py (volley-1 script with OUT dir swapped);
  Whisper via ~/workspace/fw-venv (system python lacks soundfile — use the
  venv, never the system python, for transcribe_take.py).
- **V3 COMPLETE (recovery run, 2026-11-09 ~04:2x–04:5x EST): 6/6 KEEP —
  first clean volley of v3.** O-A_v3_approach_c3 KEEP (changed axis WORKED:
  swirl mount correct, no crest — approach role finally covered) ·
  PH-A_v3_arming KEEP (trim — use 2.5–4.6s) · I-A_v3_chocoriver KEEP ·
  I-B_v3_gate KEEP · H2-A_v3_departure KEEP · H2-A_v3_ribbon KEEP. Videos
  used this run: 6/6 (cap). Stills first: G06 generated + eye-verified,
  2048x1152, canonical JPG in work/rebuild/stills_v3/ (md5 b6c5c524…).
  QC: ffprobe (all 1248x704 24fps 10.000s h264+AAC) + motion audit
  (qc_v3_volley3.py; longest frozen run 0–1f — all PASS) + contact sheets
  eye-read + full-res text scan (all six f5s frames clean) + 12fps crest
  strip for O-A c3 (no crest — climb only) + RMS on all six (−20.4 to
  −28.6 dB) + Whisper on the three takes with people (O-A c3: "Hold on,
  Sir Swirl!" generated speech; PH-A: "Thanks for watching!" hallucination;
  H2-A departure: generated dialogue — none lyric content; generated audio
  is dropped at assembly). QC tooling: work/rebuild/qc/qc_v3_volley3.py
  (volley-2 script with OUT dir swapped); Whisper via ~/workspace/fw-venv.
- **V4 COMPLETE (recovery run, 2026-11-09 ~04:5x–05:1x EST): 6/6 KEEP —
  second clean volley of v3.** H2-B_v3_pupil KEEP (loose-prompt slot, F12
  glyph watch CLEAR — pupil reflections abstract rings/blobs only, no
  letters; use 0–7.5s, tail is a glow-burst) · H2-B_v3_canal KEEP · H2-C_v3_gate
  KEEP · D-A_v3_duel KEEP (dismounts mid-take to wrestle the serpent —
  assembly uses mounted opening / closing face-off) · D-B_v3_serpent KEEP
  (cleanest of the volley) · FH-A_v3_flush KEEP. Videos used this run: 6/6
  (cap). Stills first: G07, G08, G10 generated + eye-verified, all
  2048x1152, canonical JPGs in work/rebuild/stills_v3/ (md5s in
  STILL_CHAIN_v3.md — G07 b4992b8b…, G08 d50a243b…, G10 31ed5679…). QC:
  ffprobe (all 1248x704 24fps 10.000s h264+AAC) + motion audit
  (qc_v3_volley4.py; longest frozen run 0–2f — all PASS) + contact sheets
  eye-read + full-res text scan (all six f5s frames clean; FH-A bunting
  doodles are abstract emblems, not letters) + RMS on all six (−17.9 to
  −28.4 dB) + Whisper on the three takes with people (H2-C gate: "Thanks
  for watching!" hallucination; D-A: generated dialogue "You won't get
  past me!"; FH-A: no words — none lyric content; generated audio is
  dropped at assembly). QC tooling: work/rebuild/qc/qc_v3_volley4.py
  (volley-3 script with OUT dir swapped); Whisper via ~/workspace/fw-venv.
- V5 owed: FH-A_v3_paperstorm (slipped from V4), FH-B_v3_pipeflight,
  FH-B_v3_citizens, O-B_v3_dam, O-B_v3_wave, O-C_v3_ghostwipe — 6 owed for
  a 6-cap volley. Stills first: G11 + G12 + G13 as needed.
- **V5 COMPLETE (recovery run, 2026-11-09 ~05:1x–05:4x EST): 6/6 KEEP —
  third clean volley of v3.** FH-A_v3_paperstorm KEEP · FH-B_v3_pipeflight
  KEEP (Sir Swirl correct, no horse; 1280x720) · FH-B_v3_citizens KEEP ·
  O-B_v3_dam KEEP (dam eyes open, cracks + golden light; Champion's skin
  renders bright yellow in the close shots — disclosed style drift) ·
  O-B_v3_wave KEEP (steadiest motion of the volley) · O-C_v3_ghostwipe KEEP
  (loop closes on the opening bathroom, gloves reaching). Videos used this
  run: 6/6 (cap). Stills first: G11, G12, G13 generated + eye-verified,
  all conformed to 2048x1152 canonical JPGs in work/rebuild/stills_v3/
  (raw generations came back 1920x1280 3:2 — center-cropped 1920x1080 and
  scaled; compositions re-verified after the crop; md5s in STILL_CHAIN_v3.md).
  QC: ffprobe (all 10.000s 24fps h264+AAC; five 1248x704, pipeflight
  1280x720) + motion audit (qc_v3_volley5.py; longest frozen run 0–1f —
  all PASS) + contact sheets eye-read + full-res text scan (all six f5s
  frames clean; smears/ribbons/banners are swirls and abstract emblems,
  never letters) + RMS on all six (−18.5 to −37.7 dB) + Whisper on all
  six (paperstorm/pipeflight/ghostwipe: no words; citizens: "Oh!" 0–0.64s;
  dam: "Hold together." 7.5–8.76s; wave: "We did it!" 1.64–3.26s — all
  generated speech/exclamation, none lyric content; generated audio is
  dropped at assembly). QC tooling: work/rebuild/qc/qc_v3_volley5.py
  (volley-4 script with OUT dir swapped); Whisper via ~/workspace/fw-venv.
  **ALL 17 SCENES NOW HAVE KEEP ROWS — volley work is DONE; assembly
  becomes owed.** 30 fresh v3 takes fired across V1–V5: 28 KEEP + 2 REJECT
  (O-A apex + approach c2, both horse mounts).
