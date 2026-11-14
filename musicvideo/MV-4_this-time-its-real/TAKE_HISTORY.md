# MV-4 TAKE_HISTORY.md

Canonical take files are `takes/mv4_s<kk>_t<t>.mp4`. The tool's raw
`media-generation-*` files are the same bytes under the tool's own
names; the canonical names are the record. Every take is kept,
including rejected ones.

| Scene | Take | md5 | Dur | Whisper words (ratio) | Verdict |
|---|---|---|---|---|---|
| S01 (0.00–7.70) | t1 | f4336128d35b4d853c2e84873692988a | 10.00s | 15/16 (0.94) | KEEP |
| S02 (7.70–15.32) | t1 | 434ef0ac362587b6f108f835c4b63a82 | 10.00s | 16/16 (1.00) | KEEP |
| S03 (15.32–23.34) | t1 | 8a848c9b1acc6d079569b4dfc49516cc | 9.00s | 12/12 (1.00) | KEEP |
| S04 (23.34–30.54) | t1 | 5914de5e9b05956eb0c430dcf24461b5 | 10.00s | 14/14 (1.00) | KEEP |
| S05 (30.72–39.72) | t1 (restage) | 9d39193154e7e6442cdc97b16d285772 | 10.00s | 14/14 (1.00) | KEEP — restage landed, hook delivered (point + launch + ship rising); launch ~1s early, overlaps final word |
| S12 (86.96–95.40) | t1 | 84603591c7ceeae2583714c52894f84a | 10.00s | 17/17 (1.00) | KEEP — fast take, duration ratio 1.18 |
| S13 (95.40–103.36) | t1 | 41015d0fe8899d692072e0df3162038c | 10.00s | 14/14 (1.00) | KEEP — point held, paper ship swoops back |
| S14 (103.36–110.34) | t1 | e07db64855e58a4004fa1f86767e6cf0 | 10.00s | 11/11 (1.00) | KEEP — slow take, duration ratio 0.85; BOLT chest plain, ZIB three eyes |
| S15 (110.34–117.96) | t1 | b634bf5ba96953147e9ca7f28f509761 | 10.00s | 14/14 (1.00) | KEEP — duration ratio 0.89; crowd cheering behind |
| S16 (117.96–126.44) | t1 | c75a6c2faa10a20586780c5904ec37ca | 10.00s | 14/14 (1.00) | KEEP — duration ratio 1.00; FLAGGED blue-grey skin + red lips, strongest hue drift in the build |
| S17 (126.44–133.82) | t1 | de6d0a8f4d11cae69bc783bd569dac36 | 9.00s | 13/13 (1.00) | KEEP — duration ratio 0.94; FLAGGED blue-violet skin, third blue-shift instance |
| S18 (133.82–140.56) | t1 | 0f8ff6d19993f78dc6394ca026bdf270 | 9.00s | 10/12 unprompted, 12/12 prompted (1.00) | REJECT — G2, "WuBuTV." watermark burned top-left in every frame |
| S18 (133.82–140.56) | t2 | cf81195d78955c3bac6b761b1ffd924d | 10.00s | 12/12 (1.00) | KEEP — TEXT axis, watermark gone; duration ratio 1.06 |
| S19 (140.56–147.86) | t1 | 9c09580bbbd5fc88014b1b66f7ef4b4c | 9.00s | 16/15 (1.07) | KEEP — duration ratio 0.95; FLAGGED first-half words garbled in take audio ("the line like muscles" for "the old ones", prompted decode confirms) |
| S20 (148.40–155.16) | t1 | 430a6c4089aceb1446f16fcf939b0520 | 9.00s | 13/13 (1.00) | KEEP — duration ratio 0.96; held pose covers the 155.16–156.54 gap lead-in |
| S22 (166.54–173.90) | t1 | 65288f1888159b99b917d802ab7a6374 | 9.00s | 11/11 (1.00) | KEEP — duration ratio 0.89; liveliest take in the build (motion 10.043); BOLT antenna ball + NOVA pointed ears (design drift nits) |
| S06 (39.72–46.88) | t1 | f5756e44a2a1b25a7e535886f4a36234 | 10.00s | 13/11 (1.18) | REJECT — G2, legible "ZIB" + "B…" neon name signs |
| S06 (39.72–46.88) | t2 | b84fdca7d7c58a37f24ab0cc82b5e610 | 10.00s | 13/11 (1.18) | REJECT — G2, single glyph "T" on BOLT's chest |
| S06 (39.72–46.88) | t3 | 0c329840d20e8e1bacc6426fc11c8bae | 10.00s | 11/11 (1.00) | KEEP — G2 fixed, BOLT chest plain, no glyph |
| S07 (46.88–54.20) | t1 | 0b7900c8808777e9766fd715e2db59d3 | 9.00s | 14/14 (1.00) | KEEP |
| S08 (54.20–63.04) | t1 | 96f77ff17e21b5017e685dc6514f6d75 | 10.00s | 16/14 (1.14) | KEEP — "Futurama's"→"Future Rama's" split, line sung once |
| S09 (63.04–72.04) | t1 | b06cd6865b623a821bcffe719bd7ee41 | 9.00s | 13/13 (1.00) | KEEP |
| S10 (72.80–79.52) | t1 | 6d1fe143a3b66fac94161b584c8d672e | 9.00s | 17/17 (1.00) | KEEP — slow take, duration ratio 0.84; blue-violet skin flagged |
| S11 (79.52–86.96) | t1 | 3319aecae2b599c5ab4858094adbba76 | 10.00s | 20/15 (1.33) | KEEP — tail repeat "gave it one more round", assembly trims at 7.22s |
| S21 (156.54–166.54) | t1 (restage) | 27cb0987d3bb035c95eb2e4edcf31506 | 10.00s | 16 tokens/14 (1.14, normalized 1.00) | KEEP — restage landed, final chorus reopens at the mic; FLAGGED vocal starts at take 0.00s (~2.2s before song first word), warp 0.87, gap cover owed 156.54–158.76 |
| S23 (173.90–181.24) | t1 | 561a7501818abc83bdd2c4efb2428206 | 10.00s | 10/14 (0.71) | REJECT — G5, second "the ride is done" absent (prompted + split-half confirm); reroll t2 DELIVERY axis in volley 6 |
| S24 (181.24–187.46) | t1 | 7ab5ac4462d371e61ec2d7fe26e96e31 | 9.00s | 10/10 (1.00) | KEEP — duration ratio 0.99; arms-open hold, paper ship circles overhead |
| S25 (188.24–194.06) | t1 | 993cf76b4d9a1a6b214fff75d7e0a45e | 10.00s | 2/4 (0.50) | REJECT — G5, line delivered once, line ratio 1.99; prompted "second delivery" at 8.58s is a hallucination (RMS + closed mouth at 5s/9s); reroll t2 PACING axis in volley 6; FLAGGED lavender-grey skin, strongest hue drift in the build |
| S26 (194.06–198.38) | t1 | f5b3d9ac4b4988ccdc1b4de52e6eed4c | 9.00s | 4/4 (1.00) | KEEP — duration ratio 1.20 (near edge); one slow held line at the ship window |
| S27 (198.38–204.72) | t1 | 2e8a1d6f31f3476ed9013d844c3ecb98 | 10.00s | 4/4 (1.00) | KEEP — duration ratio 1.18; last word lands, arms lower |
| S23 (173.90–181.24) | t2 | 1013f5cc0083f273eac512ad55f18313 | 10.00s | 11/14 (0.79; 10 content words) | REJECT — G2 "WuBuTV." watermark burned top-left in every frame (second watermark in the build) + G5 second "the ride is done" absent (prompted + split-half confirm); S23 now STRUCTURAL, assembly cover, never a third attempt |
| S28 (205.09–210.75) | t1 | 4c43361ea37075125e72caf57243d176 | 6.00s | 0 words (CUTAWAY, correct) | KEEP — ship rises past the dome, liveliest cutaway in the build (motion 14.569) |
| S29 (211.75–220.77) | t1 | 8df79541be9385442c0544ccf54ae62d | 10.00s | 7/7 (1.00) | KEEP — duration ratio 1.15; soft goodbye delivered, inter-line gap matches song's breath gap |
| S30a (220.77–229.00) | t1 | a5d3c68385f6e1d172bb35f367a9eccd | 8.00s | 0 words (CUTAWAY, correct) | KEEP — paper ship taped to the window, ship rises; take 0.23s short of window, hard cut absorbs it |
| S30b (229.00–238.03) | t1 | d07f23f5b766b524e0178b0328c5d17f | 9.00s | 0 words (CUTAWAY, correct) | KEEP — final frame rhymes with the first (paper ship taped to window); nit: teal/red rocket vs S30a's yellow/blue ship |

Notes:
- S06 t1/t2 Whisper counts (13 vs 11) are a tokenization split:
  "Futurama's" heard as "Future Rama's". The line was sung once in
  both takes; no part twice.
- S06 t3 KEPT in volley 2 (G2 fixed — BOLT's chest plain, no
  glyph). The TEXT axis is closed; S06 is covered.
- S10 t1 is a slow take (duration ratio 0.84, warp within caps)
  and NOVA's skin renders blue-violet (flagged in QC_VOLLEY2.md).
- S11 t1 repeats "gave it one more round" after the first
  delivery — assembly trims at 7.22s (first delivery end).
- S05's volley-1 vehicle was denied by generation
  (integrity_check_failed, no take). Volley 3 restaged it from
  scratch (mv4_s05_vehicle.txt; denied vehicle archived as
  mv4_s05_denied_vehicle.txt) and t1 KEPT — hook delivered.
- S12 t1 is a fast take (duration ratio 1.18, warp within caps).
- S14 t1 is a slow take (duration ratio 0.85, warp within caps).
- S16 t1 is FLAGGED: pale blue-grey skin, red lips, narrower face
  — strongest hue/face drift in the build. Same disclosed nit
  class as S10 (no hard gate on NOVA's skin tone); S16 t2 (HUE
  axis) is a volley-4 option on parent order only.
- S17 t1 is FLAGGED: blue-violet skin — third blue-shift instance
  (S10 blue-violet, S16 blue-grey + red lips). Same disclosed hue
  class; no reroll ordered.
- S18 t1 REJECTED (G2): "WuBuTV." watermark burned into the
  top-left corner of every frame — first watermark in the build.
  Replaced in-volley by S18 t2 (TEXT axis, watermark named and
  banned; G2 fixed, 12/12 words, duration ratio 1.06). The t1
  performance itself was clean (prompted decode recovers the full
  line; the unprompted "safer works as" was a Whisper mishear of
  "the paperwork says").
- S19 t1 is FLAGGED: first-half words garbled in the take's own
  audio — "the line like muscles" for "the old ones" (2.14–3.42s),
  confirmed by prompted re-transcription (the prompt did not
  recover "the old ones"). Second half exact; count 16/15 (1.07),
  duration ratio 0.95, motion passes. The master audio carries the
  correct words; the take's audio is dropped at assembly. S19 t2
  (DELIVERY axis) is a volley-5 option on parent order only.
- S20 t1: 2s closed-mouth single-frame read cleared by a widened
  sample (open vocal at 1.5s and 5s; 3.5s closed is the breath gap
  3.46–4.00s). Framing wider than MCU (full body visible).
  "one" for "ones" is the established singular/plural
  normalization.
- S21 BLOCKED: generation denied integrity_check_failed, no take
  — same denial class as S05 in volley 1. Restage from scratch in
  volley 5, never a re-fire of the denied vehicle (mv4_s21_vehicle.txt
  stays archived as-is; do NOT copy its staging into the restage).
- S22 t1: liveliest take in the build (vocal mean diff 10.043).
  Design-drift nits: BOLT antenna ball (bible says no antenna
  ball), NOVA pointed ears, gold chain + gold chest diamond,
  bone mark on ZIB's tunic hem.
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
- S21 t1 (restage) KEPT in volley 5 — mic-based restage, never a
  re-fire of the denied vehicle (mv4_s21_restage_vehicle.txt;
  denied vehicle stays archived as mv4_s21_vehicle.txt). Vocal
  front-loaded to take 0.00s (~2.2s before the song's first word);
  assembly places it at 158.76 with warp 0.87. Ship lands ~1s
  early (same early-beat nit class as S05's launch). BOLT round
  dome head + antenna ball again (design drift, same class as
  S22).
- S23 t1 REJECTED in volley 5 (G5): second "the ride is done"
  absent — prompted re-transcription and split-half both confirm
  10 words. Reroll t2 DELIVERY axis in volley 6.
- S25 t1 REJECTED in volley 5 (G5): line delivered once
  (0.00–2.92s), line ratio 1.99. The prompted decode's second
  delivery at 8.58–10.0s is a hallucination (per-second RMS
  0.008/0.005 in 8–10s, mouth closed at 5s and 9s). Reroll t2
  PACING axis in volley 6. FLAGGED lavender-grey skin — strongest
  hue drift in the build (past S16); the reroll axis is PACING,
  not hue.
- S25 t2 DENIED in volley 6 (generation integrity_check_failed, no
  take) — never re-fire in any form. t1 REJECTED + t2 DENIED: S25 is
  STRUCTURAL, assembly cover ("not a mouth-sung slot", captions on
  song word times). The t2 vehicle file stays as the record of the
  denied request.
- S23 t2 REJECTED in volley 6 (G2 + G5): "WuBuTV." watermark burned
  top-left in every frame (second watermark in the build, after
  S18 t1) AND second "the ride is done" absent (11/14 tokens,
  10 content words; prompted + split-half confirm; the "pause"
  token at 2.16–2.38s is a Whisper lexicalization of a breath,
  heard in all three decodes). t1 REJECTED + t2 REJECTED: S23 is
  STRUCTURAL, assembly cover. No volley 7, never a third attempt.
- S28/S30a/S30b t1 KEPT in volley 6 (CUTAWAY takes, 0 Whisper words
  correct, motion 14.569/6.511/4.466, 0f near-dup runs). S30a's
  paper ship is taped to the window as a drawing; S30b's final
  frame rhymes with the first. Nit: S30b's ship is a teal/red
  rocket vs S30a/S28's yellow/blue delivery ship (design drift
  across the ~229s hard cut).
- S29 t1 KEPT in volley 6 (7/7 words, duration ratio 1.15, motion
  2.582). Flatter S01-style cartoon render; handheld-style mic on
  a stand (nit); small yellow edge fragment at 5s (nit).
- Assembly notes carried forward: S28 CUTAWAY trim 205.09–210.75;
  S29 warp 1.15 within caps; S30a CUTAWAY trim 220.77–229.00 (take
  0.23s short, cut absorbs it); S30b CUTAWAY trim 229.00–238.03.
  STRUCTURAL cover owed: S23 (173.90–181.24) and S25 (188.24–194.06)
  — montage/cutaway picture, "not a mouth-sung slot", captions
  keyed to song word times. All 30 scenes resolved (28 KEEP +
  2 structural); next is assembly, ONE 16:9 master.
