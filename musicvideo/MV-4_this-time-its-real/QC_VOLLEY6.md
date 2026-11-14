# MV-4 QC_VOLLEY6.md — volley 6, FINAL (S23 t2, S25 t2, S28, S29, S30a, S30b t1)

Method: frames at 2s/5s/8s (widened when reads disagree); Whisper word count vs prompted line (count ratio
AND duration ratio — song window / take vocal span, band 0.80–1.25
for both); motion audit at native 24fps, 160x90 gray (frame gate FAIL
if vocal near-dup run ≥24f during vocal OR vocal mean diff <0.5;
near-dup = mean abs diff <0.5). Prompted re-transcription
(initial_prompt = the scene's performed line) + split-half recheck
run for S23 t2 where the unprompted decode came up short.
CUTAWAY takes (S28/S30a/S30b): no vocal expected — Whisper 0 words
is correct; motion judged over the full clip. Confidence tags:
[confirmed] measured, [inferred] model-judged, [assumed] user claim.
Nits are disclosed, never promoted to fails.

## S23 t2 — REJECT (G2 watermark + G5, second repeat absent)
- File: takes/mv4_s23_t2.mp4, md5 1013f5cc0083f273eac512ad55f18313,
  10.00s, 1280x720 h264 + AAC [confirmed]. Kept on disk only, never chained from.
- Whisper: 11/14 tokens, count ratio 0.79 [confirmed]. "Good news,
  everyone, pause, good news, everyone, the ride is done." Prompted
  re-transcription returns the SAME 11 words; split-half 0–5s finds
  "Good news, everyone. Pause. Good news, everyone." and 5–10s finds
  "The ride is done." once. The "pause" token at 2.16–2.38s sits in a
  real vocal-energy window (RMS 2–3s = 0.1176) — the take renders a
  breath/artifact there that Whisper lexicalizes in all three decodes;
  it is not a song word. Content words: 10/14 (0.71). The second "the
  ride is done" is absent in all three decodes — the take's single
  "The ride is done" (4.86–6.56s local) straddles the song's two
  delivery windows instead of delivering twice. Vocal span
  0.00–6.56s vs song 7.34s → duration ratio 1.12, in band — the take
  is in pace but short a repeat, the same defect as t1.
- Motion: vocal mean diff 3.812, longest near-dup run 0f, 0 exact
  duplicates [confirmed]. Not frozen.
- G2 FAIL [confirmed]: "WuBuTV" burned into the top-left corner of
  every frame — a channel-bug watermark generated inside the clip.
  SECOND watermark in the build (S18 t1 was the first; S18 t2 fixed
  it in-volley). The take cannot enter the cut with burned-in text.
- G1 PASS [inferred]: NOVA consistent (warm skin, house style).
  Nits: he grips the mic in his gloved hand (handheld-mic class);
  gold epaulettes (added-accessory class); face render is the more
  detailed/realistic variant (warm/detailed face class).
  G3 PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera;
  open-mouth vocal at 5s (in "ride"); 2s closed mouth with eyes
  closed is a singing beat inside "everyone" (0.88–1.62s) — a
  single-frame shape between syllables; 8s closed mouth is the
  correct post-line rest (last word "done" ends 6.56s). The crowd
  raises their arms on each repeat, mouths closed.
- G5 FAIL: count 0.79 (0.71 content), second "the ride is done"
  absent — the song's second delivery (179.26–181.24) has no mouth.
- S23 is now STRUCTURAL: t1 REJECTED (G5) + t2 REJECTED (G2+G5) —
  two failed attempts on the same shape. No third attempt, no
  volley 7. Assembly covers S23 (173.90–181.24) with montage/cutaway
  picture flagged "not a mouth-sung slot", captions keyed to song
  word times.

## S25 t2 — BLOCKED (generation denied, no take)
- Generation DENIED (integrity_check_failed), no take, not a QC or
  plan failure — the same denial class as S05 (volley 1) and S21
  (volley 4). Standing instruction: never repeat that request in
  any form. The denial was NOT re-fired with changed arguments.
- S25 is now STRUCTURAL: t1 REJECTED (G5, line once, 0.50/1.99) +
  t2 DENIED. No third attempt. Assembly covers S25 (188.24–194.06)
  with montage/cutaway picture flagged "not a mouth-sung slot",
  captions keyed to song word times. The S25 t2 vehicle file stays
  on disk as the record of the denied request; do NOT copy its
  staging into any restage.

## S28 t1 — KEEP (cutaway)
- File: takes/mv4_s28_t1.mp4, md5 4c43361ea37075125e72caf57243d176,
  6.00s (requested 6s; tool returned 6.00s — recorded),
  1280x720 h264 + AAC [confirmed].
- Whisper: 0 words [confirmed] — correct for a cutaway, no vocal
  expected. Vocal span n/a.
- Motion: full-clip mean diff 14.569, longest near-dup run 0f, 0
  exact duplicates [confirmed]. Not frozen — the liveliest cutaway
  in the build (ship rising, engines blazing, confetti, crowd).
- G1 PASS [inferred]: no singer in frame; the big yellow/blue
  delivery ship matches the build's ship design, bone decals on
  the hull (motif callback). G2 PASS [confirmed]: no text anywhere;
  bone shapes are decals, not letters. G3 PASS [confirmed].
  G4 n/a (CUTAWAY — no singer, every visible mouth closed and still).
- G5 PASS: trim 205.09–210.75 (5.66s window, 6.00s take).
  G6 PASS (plan-level).
- Beat verified: the real ship lifts off past the dome, paper ship
  (origami) at frame left, crowd waving below, ringed planet —
  the paper ship becomes the real ship, graphic-match payoff
  delivered.

## S29 t1 — KEEP
- File: takes/mv4_s29_t1.mp4, md5 8df79541be9385442c0544ccf54ae62d,
  10.00s (requested 9s; tool returned 10.00s — recorded),
  1280x720 h264 + AAC [confirmed].
- Whisper: 7/7 words, count ratio 1.00 [confirmed]. "Good news,
  everyone, for real this time." Line sung once. Vocal span
  0.00–7.84s (7.84s) vs song 9.02s → duration ratio 1.15, in band.
  The inter-line gap in the take (2.44–3.52s, 1.08s) matches the
  song's breath gap (1.02s).
- Motion: vocal mean diff 2.582, longest near-dup run 0f, 0 exact
  duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA consistent (flatter cartoon style,
  close to S01; pompadour, cobalt jacket, cadmium trim, bone
  shirt, white gloves, chrome mic). Nit: he grips the mic
  (handheld-mic class); small yellow edge shape bottom-left at 5s
  (unresolved background fragment, not a fail).
- G2 PASS [confirmed]: deck panels are abstract colored lights
  and dots, no readable word; no watermark.
- G3 PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera;
  open-mouth vocal at 2s (in "everyone") and 5s (in "for real",
  eyes closed = singing beat); 8s closed mouth with eyes closed
  is the correct post-line rest (last word "time" ends 7.84s).
- G5 PASS: trim 211.75–220.77, warp 1.15 within caps. G6 PASS
  (plan-level).
- Beat verified: soft goodbye to camera delivered (ringed planet,
  confetti drifting down, soft deck light).

## S30a t1 — KEEP (cutaway)
- File: takes/mv4_s30a_t1.mp4, md5 a5d3c68385f6e1d172bb35f367a9eccd,
  8.00s (requested 8s; tool returned 8.00s — recorded),
  1280x720 h264 + AAC [confirmed].
- Whisper: 0 words [confirmed] — correct for a cutaway.
- Motion: full-clip mean diff 6.511, longest near-dup run 0f, 0
  exact duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA waving from behind (back to camera,
  face not readable — correct for CUTAWAY); the big yellow/blue
  ship matches S28's ship; the paper ship is taped to the window
  as a drawn ship on paper — the rhyme lands.
  G2 PASS [confirmed]: no text anywhere; the scribble hatching on
  the drawn ship is abstract sketch marks, no legible word
  (borderline-illegible class, same as prior panel shapes).
  G3 PASS [confirmed]. G4 n/a (CUTAWAY).
- G5 PASS: trim 220.77–229.00 (8.23s window, 8.00s take — 0.23s
  short of the window; the hard cut on the beat at ~229s absorbs
  it). G6 PASS (plan-level).
- Beat verified: ship rises past the dome, paper ship taped to the
  window, NOVA waves — first half of the outro delivered.

## S30b t1 — KEEP (cutaway, final shot)
- File: takes/mv4_s30b_t1.mp4, md5 d07f23f5b766b524e0178b0328c5d17f,
  9.00s (requested 9s; tool returned 9.00s — recorded),
  1280x720 h264 + AAC [confirmed].
- Whisper: 0 words [confirmed] — correct for a cutaway.
- Motion: full-clip mean diff 4.466, longest near-dup run 0f, 0
  exact duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA waving from behind (back to camera);
  paper ship drawing taped to the window in all three frames;
  ringed planet, confetti. Nit: the ship here is a teal/red rocket
  — a DIFFERENT ship design from S30a/S28's yellow/blue delivery
  ship. The hard cut at ~229s will read a design change; disclosed
  ship-design drift across the S30a/S30b cut, not a fail (the plan
  asks only for "ship rises", which both takes deliver).
  G2 PASS [confirmed]: no text anywhere; control panels are
  abstract dots and lights. G3 PASS [confirmed]. G4 n/a (CUTAWAY).
- G5 PASS: trim 229.00–238.03 (9.03s window, 9.00s take — 0.03s
  short, negligible). G6 PASS (plan-level).
- Beat verified: ship rises away into the stars, paper ship taped
  to the window, NOVA waves — the final frame rhymes with the
  first (paper ship in hand → paper ship taped to the window).

## Volley-6 verdicts
- KEEP: S28 t1, S29 t1, S30a t1, S30b t1 (4/6 scenes). All word
  counts in band (7/7 for the one SINGING take; 0 words correct
  for the three cutaways); duration ratio in band (1.15); all
  motion gates pass (full-clip mean diff 2.582–14.569, longest
  near-dup run 0f).
- REJECT: S23 t2 (G2 watermark + G5 second repeat absent) —
  kept on disk only, never chained from.
- BLOCKED: S25 t2 (generation denied integrity_check_failed, no
  take) — never re-fire in any form.
- Coverage after volley 6: S01–S22 + S24 + S26–S30 (28/30).
  Open: S23, S25 — BOTH STRUCTURAL (assembly cover, "not a
  mouth-sung slot", captions on song word times). No volley 7.
- Nit classes logged this volley (do not re-litigate per take):
  watermark, second instance (S23 t2, after S18 t1); handheld
  mic (S23 t2, S29 t1); warm/detailed face render (S23 t2) vs
  flatter S01-style render (S29 t1); added accessories (S23 t2
  gold epaulettes); borderline-illegible scribble hatching
  (S30a drawn ship); ship-design drift across the S30a/S30b cut
  (yellow/blue delivery ship vs teal/red rocket); "pause" artifact
  token (S23 t2, Whisper lexicalizes a breath in all three
  decodes); small yellow edge fragment (S29 t1, 5s frame).
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
  1.18 within caps; S28 CUTAWAY trim 205.09–210.75; S29 warp 1.15
  within caps; S30a CUTAWAY trim 220.77–229.00 (take 0.23s short,
  cut absorbs it); S30b CUTAWAY trim 229.00–238.03.
  STRUCTURAL cover owed: S23 (173.90–181.24) and S25
  (188.24–194.06) — montage/cutaway picture, "not a mouth-sung
  slot", captions keyed to song word times.

## After volley 6: assembly
- All 30 scenes resolved: 28 covered by KEEP takes, 2 structural
  (S23, S25) covered by montage at assembly.
- Assembly: cross-check sync method, ONE 16:9 master, song is
  tempo gospel. No volley 7. Optional on parent order only: S19 t2
  (DELIVERY axis), S16 t2 (HUE axis), S10 t2 (HUE axis) — still
  unoffered and unordered; hue drift and the S19 garble remain
  disclosed nit/flag classes.
