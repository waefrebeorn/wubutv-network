# MV-5 Volley 13 QC verdicts — brisk pacing rerolls, S21 GIRL bridge inserts (2026-11-06 ~01:00 EST)

Ear answers (2026-11-06 ~00:20 EST, user): L12 GIRL, L15 GIRL, bridge ALTERNATING
(GIRL-first). Volley 12 fired the GIRL inserts: s06_t2 KEEP, s21_t7 KEEP (grey
rescue), s21_t4/t5/t6 REJECT on PACING (first attempts). Volley 13 fired one
PACING reroll each for L82/L84/L86 (t8/t9/t10): same bridge staging, ONE
variable changed — delivery pace (brisk, finish by ~1.5s; t9 no held first
word, t10 no mid-line pause). All three generated; all three QC'd below.

## Method

- `work/qc_v13.py` (adapted from `qc_v12.py`): frames at 0.5/1.0/1.5/2.0/2.5/3.0/4.0s
  + contact sheets `work/qc_v13/sheets/*_sheet.png` (1 fps, 0–4s), faster-whisper base
  CPU int8 prompted decode (initial_prompt = the line) + unprompted confirm decode,
  motion audit at 160×90, vocal-window motion, repeat-bigram check, per-0.5s RMS.
- Singer judged by MOUTH FRAMES (contact sheets read), never by take f0.
- Song word times: app per-word starts from `work/gemini_song_words_aligned.json`
  (authoritative per the audit: "use word STARTS from the app, line spans from v1");
  line spans from the brief (LYRIC_TIMELINE_V2). V1-grid starts checked as the
  grey-rescue alternative (as for s21_t7 in volley 12).
- Fit standard (audit): linear fit of take word starts → song (app) word starts;
  slope + residuals; implied playback 1/slope must stay ≤ ~1.5x (warp-rescue cap);
  line ratio = song line span / take span; usable 0.80–1.25, grey 0.60–0.80/1.25–1.60
  (re-measure + ear check), clear miss <0.60.
- Binding decision rule (volley-12 QC): if a reroll lands ≥2.5s, that line goes
  STRUCTURAL — no further reroll. (Skill: two denied rerolls retire the scene.)
- Prompted-repeat adjudication: a prompted second/third delivery whose words are
  zero-duration with the RMS tail at baseline is a Whisper hallucination, not a
  repeat defect — same class as S19a t2 (volley 10) and S28 t2–t4 (volley 11).
  A repeat confirmed by the UNPROMPTED decode AND real RMS energy is a real
  repeat defect.

## Verdicts

### S21 t8 — L82 "If the sky turns gray" — REJECT (PACING)

- File: `takes/mv5_s21_t8.mp4`, md5 `47ee8e4ccf54d52976a779dc610dae75`, 5.000s,
  1280×720, 24fps, 120 frames. Generation record:
  `takes/media-generation-mv5-s21-t8-0-b7002bc4-db38-4f9c-a638-75c77e0a7f12.mp4`.
- Line sung ONCE, completely — prompted and unprompted agree:
  "If the sky turns gray". Word times: If 0.0–1.1 (HELD 1.1s), the 1.1–1.26,
  sky 1.26–1.62, turns 1.62–2.28, gray 2.28–2.68. Span 2.68s vs song 1.04s
  (158.06–159.1) → ratio 0.39, CLEAR MISS (<0.60).
- App-start fit: song starts 158.2/158.2/158.3/158.5/158.9 vs take starts
  0.0/1.1/1.26/1.62/2.28; slope 0.299 → playback 3.35x, far beyond the 1.5x
  rescue cap (median |resid| 0.15). V1-grid fit: slope 0.334 → playback 2.99x —
  no legal placement under EITHER grid.
- The brisk variable barely moved it: t4 2.94s → t8 2.68s (−0.26s, −9%). The
  held-first-word defect persists: "If" is held 1.1s (t4's head was spread, not
  held; the reroll traded one head defect for another).
- Frame rule PASSES: vocal mean 0.934 (≥0.5), longest near-dup run 2 (<24);
  motion mean 0.978, run 2, exact dup 0. RMS: voice 0.5–3.0s (0.05–0.11),
  baseline after 3.5s — one delivery, then hold.
- Picture PASSES: GIRL SINGS — mouth open at 1.0/2.0s, closed smile at 3.0/4.0s
  (mouth closed at 0s — pre-first-word hold). CAT in basket, mouth closed in
  all five sheet frames. Locks hold (straw sun hat with red band, purple
  hair/eyeshadow, red lipstick, red jacket over black crop top, blue bike,
  wicker basket, black cat, red collar, yellow bell, blue eyes). Sunset
  boardwalk (bridge staging). No on-screen text.
- SINGER IS FIXED — the only miss is pace. 2nd denied attempt on this insert
  (t4 + t8). Span 2.68s ≥ 2.5s → per the binding rule, **L82 goes STRUCTURAL**.
  No t11. Pace floor for L82 GIRL now measured at ~2.7–2.9s vs a 1.04s window.

### S21 t9 — L84 "We lean right back" — REJECT (PACING)

- File: `takes/mv5_s21_t9.mp4`, md5 `2c025aac05be7a06da72c70c66b3d9cc`, 5.000s,
  1280×720, 24fps, 120 frames. Generation record:
  `takes/media-generation-mv5-s21-t9-0-2d702a5e-5634-4cd7-bb67-3284a8a7c0c9.mp4`.
- Required line sung completely — prompted and unprompted agree — PLUS an
  invented extra word: "We lean right back up." Word times: We 0.0–0.9 (HELD
  0.9s — better than t5's 1.92s, still held), lean 0.9–1.32, right 1.32–1.8,
  back 1.8–2.5, up 2.5–3.3. Required-words span 2.5s vs song 1.12s
  (160.24–161.36) → ratio 0.45, CLEAR MISS. Full span incl. "up" 3.3s →
  ratio 0.34.
- App-start fit (4 required words): song starts 160.5/160.6/160.8/161.1 vs take
  starts 0.0/0.9/1.32/1.8; slope 0.320 → playback 3.12x (median |resid| 0.08).
  V1-grid fit: slope 0.476 → playback 2.10x — no legal placement under EITHER
  grid.
- The extra word "up" is REAL, not a hallucination: both decodes hear it with
  the same times, and the per-0.5s RMS shows voice 2.5–3.0s (0.0634) behind it.
  Secondary defect on top of the pace miss: the take sings a word that is not
  in the song.
- Frame rule PASSES: vocal mean 1.285, run 2; motion mean 0.959, run 8.
  RMS: voice 0.5–2.5s (0.11), "up" 2.5–3.0s, baseline after 3.0s.
- Picture PASSES: GIRL SINGS — mouth open at 0s and 1.0s, closed smile at 2.0s,
  open small at 3.0s (the "up" delivery), slightly open at 4.0s. CAT in basket,
  mouth closed in all five sheet frames. Locks hold (straw sun hat with red
  band, purple hair/eyeshadow, red lipstick, red jacket, black crop top,
  cut-off shorts, blue bike, wicker basket, black cat, red collar, yellow
  bell, blue eyes). Staging variant (leaning on the handlebar with her arm
  resting on it rather than standing beside the bike) — a pose variant, not a
  fail. No on-screen text.
- 2nd denied attempt on this insert (t5 + t9). Required-words span 2.5s ≥ 2.5s
  → per the binding rule, **L84 goes STRUCTURAL**. No t11. Pace floor for L84
  GIRL now measured at ~2.5–3.8s vs a 1.12s window.

### S21 t10 — L86 "You and me, same pace" — REJECT (PACING + REPEAT)

- File: `takes/mv5_s21_t10.mp4`, md5 `d54308d6264fb6727bf0296b58c0744b`, 5.000s,
  1280×720, 24fps, 120 frames. Generation record:
  `takes/media-generation-mv5-s21-t10-0-80e0f1fd-8020-4e30-ab22-542b3f195467.mp4`.
- First delivery: You 0.0–0.72, and 0.72–1.1, me 1.1–1.4, same 1.96–2.3, pace
  2.3–2.78. Span 2.78s vs song 1.12s (162.46–163.58) → ratio 0.40, CLEAR MISS.
  The mid-line gap PERSISTS: me ends 1.4, same starts 1.96 (0.56s gap; t6's was
  0.7s). The brisk variable did not close the gap.
- App-start fit (first delivery): song starts 162.7/162.8/162.9/163.0/163.1 vs
  take starts 0.0/0.72/1.1/1.96/2.3; slope 0.168 → playback 5.94x (median
  |resid| 0.02). V1-grid fit: slope 0.296 → playback 3.38x — no legal
  placement under EITHER grid.
- REPEAT DEFECT (real, not hallucination): the model re-sings "pace" at
  3.34–3.94s. The unprompted decode hears it ("You and me, same pace, pace"),
  and fine 0.1s RMS shows a real energy burst 3.6–3.9s (0.107/0.272/0.171)
  against a quiet floor ~0.02–0.05, cleanly separated from the first delivery
  (quiet 3.0–3.5s). The prompted decode's LATER tokens ("You and me, same
  pace, pace..." at 3.94–5.0s) are zero-duration with RMS at baseline — those
  ARE hallucinations, same class as t4/t6. The 3.34–3.94 "pace" is not.
- Frame rule PASSES: vocal mean 1.038, run 5; motion mean 1.038, run 5.
- Picture PASSES: GIRL SINGS — mouth wide open at 0s, open at 1.0s, closed
  smile at 2.0/3.0s, slightly open at 4.0s. CAT in basket, mouth closed in all
  five sheet frames. Locks hold (red sun hat — solid red variant like t4/t7;
  purple hair/eyeshadow, red lipstick, red jacket, black crop top, cut-off
  shorts, blue bike, wicker basket, black cat, red collar, yellow bell, blue
  eyes). Staging variant (girl seated riding, hands on handlebars, rather than
  standing beside the bike) — a pose variant, not a fail; P-GIRL-SING holds
  (facing camera, MCU, mouth visible). No on-screen text.
- 2nd denied attempt on this insert (t6 + t10). First-delivery span 2.78s ≥
  2.5s → per the binding rule, **L86 goes STRUCTURAL**. No t11. Pace floor for
  L86 GIRL now measured at ~2.8–4.4s vs a 1.12s window.

### S07 t2 — L15 — NOT FIRED (unchanged from volley 12)

- `media.generate_video` returned `integrity_check_failed` in volley 12; NOT
  retried in volley 13 per the standing rule (never repeat with changed
  arguments or through another tool/endpoint). No take file exists. L15 goes
  to donor cover at assembly (s07_t1 is all-CAT and the user's ear says GIRL —
  placing it would repeat the v1 wrong-singer error).

## Volley 13 result: 0 KEEP / 3 REJECT (all PACING; t10 also REPEAT)

Cumulative: 24 KEEP / 43 REJECT (effective 23 KEEP: 21 + s06_t2 + s21_t7;
S28 t1 KEEP superseded by the audit). **L82, L84, L86 all go STRUCTURAL —
generation for the S21 GIRL inserts is CLOSED (two denied attempts each).**
The bridge GIRL inserts that survive are s21_t7 (L88, KEEP grey-rescue) and
s06_t2 (L12, KEEP).

## Bridge pace floor (volley 12 + 13 measurement)

- GIRL inserts vs ~1.1s song windows: L82 2.94 → 2.68s; L84 3.78 → 2.50s;
  L86 4.44 → 2.78s. The brisk reroll moved each span only −9%/−34%/−37% —
  nowhere near the ~1.5s target. The CAT head s21_t3 did the same lines in
  ~1.9s (playback 1.49x, at the rescue cap): the GIRL inserts run ~0.6–0.9s
  slower than the CAT head on identical lines.
- Persistent defects the pace axis did NOT fix: held first word (t8 "If"
  1.1s; t9 "We" 0.9s, down from t5's 1.92s but still held), mid-line gap
  (t10 0.56s between "me" and "same"; t6's was 0.7s). New defects: t9 invents
  an extra word ("up" after "back"); t10 genuinely repeats "pace" at 3.34–3.94s
  (unprompted + RMS-confirmed).
- t7 (L88, 3 words) remains the exception: 1.5s, ratio 0.65, placeable under
  the v1 grid. The 4–5-word bridge lines at ~1.1s windows are below the GIRL
  insert pace floor (~2.5s) — structural, not a prompting failure to
  out-pull. No further generation for L82/L84/L86.

## Structural cover — CORRECTION to the volley-12 fallback shorthand

- The volley-12 QC wrote the fallback as "t3 CAT picture + captions". That
  shorthand is WRONG as written and must not be followed literally: s21_t3 is
  the all-CAT bridge take, and its picture for L82/L84/L86 shows the CAT
  visibly singing lines the user's ear says are the GIRL's. Cutting the cat
  mouthing a girl line would repeat the exact wrong-singer error the user
  rejected v1 for.
- Correct structural treatment (skill: MONTAGE IS MATERIAL): reaction /
  listening picture with mouths CLOSED + captions on song times, "not a
  mouth-sung slot". Cover frames on disk include the t8/t9/t10 closed-mouth
  tails (girl holding still after her line, cat in basket, both mouths closed)
  and t3's non-vocal frames. The assembly agent picks the cover frames; the
  rule is: no mouth visibly forming L82/L84/L86 words except the girl's own,
  and no such girl take exists that fits — so the picture looks elsewhere.
- Same rule already governs L15 (donor cover, not s07_t1's CAT mouth) and
  L87/L89 (donor cover).

## Evidence

- `work/qc_v13.py` + `work/qc_v13/qc_v13_results.json` + `work/qc_v13.log`
- `work/qc_v13/sheets/*_sheet.png` (1 fps contact sheets, 0–4s per take)
- `work/qc_v13/s21_t8_t*.png`, `s21_t9_t*.png`, `s21_t10_t*.png` (frames at 0.5/1.0/1.5/2.0/2.5/3.0/4.0s)
- `work/qc_v13/tmp_*.f32` (16k mono audio per take)
- `work/volley_13_fire_record.md` (fire record + QC outcomes)
- `work/gemini_song_words_aligned.json` (song word times, both grids)
