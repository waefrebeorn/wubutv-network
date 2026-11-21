# MV-4 QC_VOLLEY1.md — volley 1 (S05 hook, S01, S02, S03, S04, S06)

Method: frames at 2s/5s/8s (widened when reads disagree); Whisper
word count vs prompted line (line-ratio band 0.80–1.25); motion audit
at 160x90 (frame gate FAIL if vocal near-dup run ≥24f during vocal
OR vocal mean diff <0.5). Confidence tags: [confirmed] measured,
[inferred] model-judged, [assumed] user claim. Nits are disclosed,
never promoted to fails.

## S01 t1 — KEEP
- File: takes/mv4_s01_t1.mp4, md5 f4336128d35b4d853c2e84873692988a,
  10.00s, 1280x720 h264 + AAC [confirmed].
- Whisper: 15/16 words, ratio 0.94 [confirmed]. "They said it was
  over back in 03, then they said it again in 2013." Line sung once,
  no repeat, no truncation.
- Motion: vocal mean diff 1.351, longest near-dup run 1f, 0 exact
  duplicates [confirmed]. Not frozen.
- G1 PASS [inferred]: NOVA consistent across samples (pompadour,
  cobalt jacket, cadmium trim, white gloves, paper ship in hand).
  Original character, no licensed likeness.
- G2 PASS [confirmed]: no legible text; neon shapes are abstract.
- G3 PASS [confirmed]: no licensed material.
- G4 PASS [inferred]: 3/3 face-to-camera, mouth visible; open-mouth
  vocal at 5s.
- G5 PASS: trim points = true window 0.00–7.70; assembly trims the
  10s take.
- G6 PASS (plan-level).
- Nits (disclosed): handheld mic vs mic-on-stand (vehicle asked for
  stand); take is 10s vs requested 9s.

## S02 t1 — KEEP
- File: takes/mv4_s02_t1.mp4, md5 434ef0ac362587b6f108f835c4b63a82,
  10.00s, 1280x720 [confirmed].
- Whisper: 16/16 words, ratio 1.00 [confirmed]. Full line once.
- Motion: vocal mean diff 3.667, longest near-dup run 1f, 0 exact
  duplicates [confirmed].
- G1 PASS [inferred]: NOVA consistent. Nit: skin-tone hue drift —
  warmer/yellower by 8s vs the natural tone at 2s.
- G2 PASS [confirmed]: TV screens blank and dark, no letters.
- G3 PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera,
  open-mouth vocal at 5s and 8s.
- G5 PASS: trim 7.70–15.32. G6 PASS (plan-level).
- Nits (disclosed): handheld mic vs stand; camera push-in continues
  through the vocal rather than settling before the first word
  (framing stays MCU-or-closer throughout).

## S03 t1 — KEEP
- File: takes/mv4_s03_t1.mp4, md5 8a848c9b1acc6d079569b4dfc49516cc,
  9.00s, 1280x720 [confirmed].
- Whisper: 12/12 words, ratio 1.00 [confirmed]. Full line once.
- Motion: vocal mean diff 1.403, longest near-dup run 3f, 0 exact
  duplicates [confirmed].
- G1 PASS [inferred]: NOVA consistent. Nit: skin tone carries a
  yellow cast vs S01's natural tone.
- G2 PASS [confirmed]: held folder is blank; shelf labels and the
  wall paper carry illegible line-like marks — no readable letters
  at full resolution (checked at 2s and 5s). Disclosed borderline
  text risk: background archive labels are the closest call in
  this volley.
- G3 PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera,
  open-mouth vocal at 5s (eyes closed at 5s is a singing beat, not
  a break).
- G5 PASS: trim 15.32–23.34. G6 PASS (plan-level).
- Nits (disclosed): handheld mic vs stand.

## S04 t1 — KEEP
- File: takes/mv4_s04_t1.mp4, md5 5914de5e9b05956eb0c430dcf24461b5,
  10.00s, 1280x720 [confirmed].
- Whisper: 14/14 words, ratio 1.00 [confirmed]. Full line once.
- Motion: vocal mean diff 1.405, longest near-dup run 9f (under
  the 24f gate), 0 exact duplicates [confirmed].
- G1 PASS [inferred]: NOVA consistent. Nit: small white bone-shaped
  mark on the jacket chest (added accessory).
- G2 PASS [confirmed]: doorway panels blank, no letters.
- G3 PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera,
  open-mouth vocal at 2s/5s; closed mouth at 8s is the correct
  post-line rest (vocal ends 7.20s).
- G5 PASS: trim 23.34–30.54. G6 PASS (plan-level).
- Beat verified: the doorway is open at 2s, closing at 5s, shut at
  8s — the door closes after the last word as directed. The mic is
  on a stand in this take, matching the vehicle.

## S05 — BLOCKED, no take
- Generation denied (integrity_check_failed). Not retryable in this
  run — the instruction stands: do not repeat the request in any
  form. The hook scene (chorus-hook test) has no take. S01 proved
  the look instead (NOVA reads correctly). Decision on the hook
  scene is owed to the parent — it is not a QC failure and not a
  plan failure.

## S06 t1 — REJECT (G2)
- File: takes/mv4_s06_t1.mp4, md5 f5756e44a2a1b25a7e535886f4a36234,
  10.00s, 1280x720 [confirmed].
- Whisper: 13 words vs 11 expected, ratio 1.18 [confirmed]. The
  count is a tokenization split ("Futurama's" heard as "Future
  Rama's"); the line was sung once, no part twice — no repeat.
- Motion: vocal mean diff 6.284, longest near-dup run 1f, 0 exact
  duplicates [confirmed].
- G1 PASS [inferred]: NOVA/BOLT/ZIB match the bible. Nit: NOVA's
  jacket has fringe epaulettes (added accessory).
- G2 FAIL [confirmed]: legible neon name signs — "ZIB" behind ZIB
  (legible in 4 consecutive sampled frames) and "B…" behind BOLT.
- G3 PASS [confirmed]. G4 PASS [inferred]: widened sample
  (1s/2s/3s/4s/5s/6s/8s) — 3/7 open-mouth; standard 2s/5s/8s
  samples pass (2/3 face-to-camera with mouth visible, open-mouth
  at 5s/8s). Closed mouths at 1s/2s/6s are within-line pauses.
- G5 PASS: trim 39.72–46.88.
- Reroll: TEXT axis, one variable — strengthened anti-text
  sentence (no name signs; BOLT's visor a plain solid band).

## S06 t2 — REJECT (G2)
- File: takes/mv4_s06_t2.mp4, md5 b84fdca7d7c58a37f24ab0cc82b5e610,
  10.00s, 1280x720 [confirmed].
- Whisper: 13 words vs 11 expected, ratio 1.18 [confirmed] (same
  tokenization split; line sung once).
- Motion: vocal mean diff 6.919, longest near-dup run 1f, 0 exact
  duplicates [confirmed].
- G1 PASS [inferred]: NOVA/BOLT/ZIB match the bible; visor is now
  a plain solid glowing band (TEXT fix worked).
- G2 FAIL [confirmed]: a single glyph — a bold capital "T" on
  BOLT's chest (full-res crop at 5s: horizontal bar + vertical
  stem, centered on the chest, reads as the letter T). The name
  signs are gone and the visor is clean; the chest glyph is the
  only remaining text.
- G3 PASS [confirmed]. G4 PASS [inferred]: 3/3 face-to-camera,
  open-mouth vocal at 5s/8s (eyes closed at 5s is a singing beat).
- G5 PASS: trim 39.72–46.88.
- Nits (disclosed): ZIB and BOLT swapped sides vs the vehicle
  (ZIB left, BOLT right); mic stand sits between NOVA and BOLT
  rather than before NOVA.
- Next: S06 t3 is owed in volley 2 (second reroll, TEXT axis, one
  variable — BOLT restaged with a plain unmarked chest shell, no
  chest panel at all). The volley cap (6 videos per user message)
  is reached: 6 successful videos fired this run, so t3 cannot
  fire here. If t3 is also denied on G2, the scene retires to a
  fresh staging from scratch per the two-denied-rerolls rule.

## Volley-1 verdicts
- KEEP: S01 t1, S02 t1, S03 t1, S04 t1 (4 scenes covered).
- REJECT: S06 t1 (G2), S06 t2 (G2). S06 still open; t3 owed in
  volley 2.
- BLOCKED: S05 (no take; generation denied, not retryable).
- Nit classes logged this volley (do not re-litigate per take):
  handheld mic vs stand (S01/S02/S03); skin-tone hue drift
  (S02/S03); added accessories (S04 bone mark, S06 t1 fringe
  epaulettes); camera push-in continuing through the vocal (S02).
