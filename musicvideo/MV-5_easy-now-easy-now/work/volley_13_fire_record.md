# Volley 13 fire record — brisk pacing rerolls, S21 GIRL bridge inserts (2026-11-06 ~00:5x–01:00 EST)

Volley 12 QC (work/qc_v12/qc_v12_verdicts.md): s06_t2 KEEP (L12), s21_t7 KEEP
grey-rescue (L88); s21_t4/t5/t6 REJECT on PACING (first attempts). Volley 13
fired one PACING reroll each for L82/L84/L86 on standing authorization (user
order 2026-11-05 02:45 EST: volleys proceed autonomously; the 6-video cap is a
batching limit only). Same bridge staging as t4–t7, ONE variable changed —
delivery pace: brisk, finish the line by ~1.5s; t9 no held first word, t10 no
mid-line pause. All three vehicles P-GIRL-SING: girl sings ONLY the one line
to camera in medium close-up, line finished in ~1.5s of a 5s take, hold still
after; CAT sits in the basket, mouth closed and still for the whole clip.
Character locks verbatim in every vehicle. ONE 16:9 only, zero on-screen text,
no licensed characters.

## Fired (3 of 3 generated; volley cap 6, 3 spent)

| Take | Vehicle | md5 | Dur | Result file |
|---|---|---|---|---|
| mv5_s21_t8 | mv5_s21_t8_vehicle.txt (GIRL insert for L82 "If the sky turns gray", song 158.06–159.1; reroll of t4 — brisk, spoken-sung, finish by ~1.5s, no held note) | 47ee8e4ccf54d52976a779dc610dae75 | 5.000s | takes/media-generation-mv5-s21-t8-0-b7002bc4-db38-4f9c-a638-75c77e0a7f12.mp4 |
| mv5_s21_t9 | mv5_s21_t9_vehicle.txt (GIRL insert for L84 "We lean right back", song 160.24–161.36; reroll of t5 — brisk, no held first word, finish by ~1.5s) | 2c025aac05be7a06da72c70c66b3d9cc | 5.000s | takes/media-generation-mv5-s21-t9-0-2d702a5e-5634-4cd7-bb67-3284a8a7c0c9.mp4 |
| mv5_s21_t10 | mv5_s21_t10_vehicle.txt (GIRL insert for L86 "You and me, same pace", song 162.46–163.58; reroll of t6 — brisk, no mid-line pause, finish by ~1.5s) | d54308d6264fb6727bf0296b58c0744b | 5.000s | takes/media-generation-mv5-s21-t10-0-80e0f1fd-8020-4e30-ab22-542b3f195467.mp4 |

## NOT fired — mv5_s07_t2 (GIRL insert for L15 "One small look from you", song 51.46–52.80)

`media.generate_video` returned `integrity_check_failed` in volley 12. NOT
retried in volley 13 per the standing rule (never repeat with changed
arguments or through another tool/endpoint). L15 goes to donor cover at
assembly (s07_t1 is all-CAT and the user's ear says GIRL — placing it would
repeat the v1 wrong-singer error). No further S07 generation.

## QC summary (full verdicts: work/qc_v13/qc_v13_verdicts.md)

- s21_t8: **REJECT (PACING)**. Line sung once, complete, both decodes agree
  (0.0–2.68s); "If" held 1.1s. Ratio 0.39 vs song 1.04s, clear miss; app-start
  fit slope 0.299 → playback 3.35x (v1-grid 2.99x — no legal placement under
  either grid). Frame rule PASSES (vocal mean 0.934, run 2). Picture PASSES
  (girl sings, cat silent; straw hat). 2nd denied attempt on this insert;
  span 2.68s ≥ 2.5s → **L82 goes STRUCTURAL**. No t11.
- s21_t9: **REJECT (PACING)**. Required line sung completely, both decodes
  agree (0.0–2.5s), PLUS an invented extra word "up" (2.5–3.3s, real — both
  decodes + RMS). Ratio 0.45 vs song 1.12s, clear miss; app-start fit slope
  0.320 → playback 3.12x (v1-grid 2.10x — no legal placement under either
  grid). "We" held 0.9s (down from t5's 1.92s, still held). Frame rule PASSES
  (vocal mean 1.285, run 2). Picture PASSES (girl sings, cat silent; straw
  hat; leaning-pose variant). 2nd denied attempt; span 2.5s ≥ 2.5s →
  **L84 goes STRUCTURAL**. No t11.
- s21_t10: **REJECT (PACING + REPEAT)**. First delivery 0.0–2.78s, ratio 0.40,
  clear miss; app-start fit slope 0.168 → playback 5.94x (v1-grid 3.38x — no
  legal placement under either grid). Mid-line gap persists (0.56s between
  "me" and "same"). Genuine repeat: "pace" re-sung 3.34–3.94s (unprompted
  decode + fine-RMS burst 3.6–3.9s confirm it; the later prompted tokens at
  3.94–5.0s are zero-duration hallucinations). Frame rule PASSES (vocal mean
  1.038, run 5). Picture PASSES (girl sings, cat silent; red sun hat variant;
  seated-riding pose variant). 2nd denied attempt; span 2.78s ≥ 2.5s →
  **L86 goes STRUCTURAL**. No t11.

## Volley 13 result: 0 KEEP / 3 REJECT (all PACING; t10 also REPEAT)

Cumulative: 24 KEEP / 43 REJECT (effective 23 KEEP: 21 + s06_t2 + s21_t7; S28
t1 KEEP superseded by the audit). **L82, L84, L86 all STRUCTURAL — generation
for the S21 GIRL inserts is CLOSED.** Bridge pace floor now measured across
two attempts each: L82 2.94→2.68s, L84 3.78→2.50s, L86 4.44→2.78s vs ~1.1s
windows; the CAT head s21_t3 did the same lines in ~1.9s. The brisk variable
moved spans only −9%/−34%/−37% and did not fix the held first word (t8 "If"
1.1s; t9 "We" 0.9s) or the mid-line gap (t10 0.56s).

## Structural cover correction (see work/qc_v13/qc_v13_verdicts.md)

The volley-12 fallback shorthand "t3 CAT picture + captions" must NOT be
followed literally: s21_t3 shows the CAT visibly singing L82/L84/L86, lines
the user's ear says are the GIRL's — cutting it would repeat the v1
wrong-singer error. Correct cover: reaction/listening picture with mouths
CLOSED + captions on song times, "not a mouth-sung slot" (cover frames on
disk include the t8/t9/t10 closed-mouth tails). Same rule already governs L15
and L87/L89 (donor cover, not a CAT mouth on a girl line).
