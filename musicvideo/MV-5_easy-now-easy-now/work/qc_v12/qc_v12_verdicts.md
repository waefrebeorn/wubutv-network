# MV-5 Volley 12 QC verdicts — ear-confirmed GIRL inserts (2026-11-06 ~00:40 EST)

Ear answers (2026-11-06 ~00:20 EST, user): L12 GIRL, L15 GIRL, bridge ALTERNATING
(GIRL-first). Volley 12 fired the six conditional refires from
`work/gemini_takes_verdicts.md`; 5 generated, 1 failed at generation.

## Method

- `work/qc_v12.py` (adapted from `qc_v11_t4.py`): frames at 0.5/1.0/1.5/2.0/2.5/3.0/4.0s
  + contact sheets `work/qc_v12/sheets/*_sheet.png` (1 fps, 0–4s), faster-whisper base
  CPU int8 prompted decode (initial_prompt = the line) + unprompted confirm decode,
  motion audit at 160×90, vocal-window motion, repeat-bigram check, per-0.5s RMS.
- Singer judged by MOUTH FRAMES (contact sheets read), never by take f0.
- Song word times: app per-word starts from `work/gemini_song_words_aligned.json`
  (authoritative per the audit: "use word STARTS from the app, line spans from v1");
  line spans from the brief (LYRIC_TIMELINE_V2).
- Fit standard (audit): linear fit of take word starts → song (app) word starts;
  slope + residuals; implied playback 1/slope must stay ≤ ~1.5x (warp-rescue cap);
  line ratio = song line span / take span; usable 0.80–1.25, grey 0.60–0.80/1.25–1.60
  (re-measure + ear check), clear miss <0.60.
- Prompted-repeat adjudication: a prompted second/third delivery whose words are
  zero-duration (e.g. 4.68–4.70, 5.0–5.0) with the RMS tail at baseline is a
  Whisper hallucination, not a repeat defect — same class as S19a t2 (volley 10)
  and S28 t2–t4 (volley 11). The unprompted decode + RMS decide.

## Verdicts

### S06 t2 — L12 "Yeah, they already understand" — KEEP

- File: `takes/mv5_s06_t2.mp4`, md5 `5507f6a2875f90bdcc9aa19a51b08762`, 5.000s,
  1280×720, 24fps, 120 frames. Generation record:
  `takes/media-generation-mv5-s06-t2-0-56b51eff-6c16-4116-831a-32758fec4807.mp4`.
- Line sung ONCE, completely — prompted and unprompted agree:
  "Yeah, they already understand." Word times: Yeah 0.0–0.54, they 0.76–0.98,
  already 0.98–1.44, understand 1.44–2.6. Span 2.6s vs song 2.28s (44.58–46.86)
  → ratio 0.88, IN BAND (0.80–1.25).
- App-start fit: song starts 44.8/44.9/45.4/45.8 vs take starts 0.0/0.76/0.98/1.44;
  slope 0.69 → playback 1.44x, within the 1.5x rescue cap; median |resid| 0.04,
  max 0.43 ("they"). Under the in-band 0.88x single warp the placed onsets are
  44.58/45.25/45.44/45.85 vs song 44.8/44.9/45.4/45.8 → offsets −0.22/+0.35/+0.04/+0.05
  (median 0.045). Three of four words land within 0.05s.
- Frame rule PASSES: vocal mean 1.11 (≥0.5), longest near-dup run 2 (<24);
  motion mean 1.347, run 7, exact dup 0. RMS: voice 0–3.0s (0.10–0.13), baseline
  after 3.5s — one delivery, then hold.
- Picture: GIRL SINGS — mouth wide open at 0s ("Yeah"), open at 1.0/2.0s, closed
  smile at 3.0/4.0s. CAT in basket, mouth closed in all five sheet frames. Locks
  hold (straw sun hat with red band, purple hair/eyeshadow, red lipstick, red
  jacket over black crop top, blue bike, wicker basket, black cat, red collar,
  yellow bell, blue eyes). Keys in hand (S06 staging). No on-screen text.
- DISCLOSED NIT: head words spread — take "Yeah→they" 0.76s vs song 0.1s, so
  "they" lands ~0.35s late under the single 0.88x warp (0.43s early under the
  fit warp). Assembly places per-line; two-anchor option (Yeah + understand
  anchors). Captions on song times. The CAT take s06_t1 keeps L10/L11; t2 is
  cut in for L12 only.

### S21 t4 — L82 "If the sky turns gray" — REJECT (PACING)

- File: `takes/mv5_s21_t4.mp4`, md5 `25bf777120d14118cfa4b44ef2b2475c`, 5.000s,
  1280×720, 24fps, 120 frames. Generation record:
  `takes/media-generation-mv5-s21-t4-0-6f29ea82-ea90-4ed0-a097-2899e65843d1.mp4`.
- Line sung ONCE — unprompted: "If the sky turns grey" (grey = gray spelling
  variant). Prompted decode re-sang it a second time, but the second delivery
  is a hallucination: words at 2.94–5.0s include zero-duration tokens
  ("sky" 4.68–4.7, "turns" 4.7–5.0, "gray" 5.0–5.0) and the RMS tail after
  3.5s is baseline (0.016–0.019). First delivery: If 0.0–0.6, the 0.6–0.82,
  sky 0.82–1.36, turns 1.36–2.3, gray 2.3–2.94. Span 2.94s vs song 1.04s
  (158.06–159.1) → ratio 0.35, CLEAR MISS (<0.60).
- App-start fit: song starts 158.2/158.2/158.3/158.5/158.9 vs take starts
  0.0/0.6/0.82/1.36/2.3; slope 0.30 → playback 3.3x, far beyond the 1.5x rescue
  cap. Residuals are small (median 0.13) but the warp itself is illegal — the
  picture would play at triple speed.
- Frame rule PASSES: vocal mean 1.186, run 3; motion mean 1.186, run 3.
- Picture PASSES: GIRL SINGS — mouth open at 0s (eyes closed, "If"), open at
  1.0/2.0s, closed smile at 3.0/4.0s. CAT in basket, mouth closed throughout.
  Locks hold (red sun hat — solid red rather than straw, a style variant, not a
  fail; purple hair/eyeshadow, red lipstick, red jacket, black crop top, cut-off
  shorts, blue bike, wicker basket, black cat, red collar, yellow bell, blue
  eyes). Sunset boardwalk (bridge staging). No on-screen text.
- SINGER IS FIXED — the only miss is pace. 1st denied attempt on this insert.
  NEXT MOVE: volley 13 reroll on PACING (one variable: brisk, finish the line
  by ~1.5s, no held note). Target: take span ≤ ~1.6s (playback ≤1.5x vs the
  1.04s window — the S21 t3 CAT head did L82 in 1.9s, so the model can go
  faster than 2.94s). If the reroll lands ≥2.5s, L82 goes structural (t3 CAT
  picture + captions, "not a mouth-sung slot").

### S21 t5 — L84 "We lean right back" — REJECT (PACING)

- File: `takes/mv5_s21_t5.mp4`, md5 `ce336b3e576330d7d6f3f5f433a0e2bd`, 5.000s,
  1280×720, 24fps, 120 frames. Generation record:
  `takes/media-generation-mv5-s21-t5-0-6451f3bf-b49f-4c74-9ee9-e140fac0aa4a.mp4`.
- Line sung ONCE, completely — prompted and unprompted agree: "We lean right
  back". Word times: We 0.0–1.92 (HELD 1.92s), lean 1.92–2.36, right 2.36–3.0,
  back 3.0–3.78. Span 3.78s vs song 1.12s (160.24–161.36) → ratio 0.30, CLEAR MISS.
- App-start fit: song starts 160.5/160.6/160.8/161.1 vs take starts 0.0/1.92/2.36/3.0;
  slope 0.20 → playback 5x, far beyond the 1.5x rescue cap. Delivery defect on
  top of the pace miss: the first word "We" is held 1.92s.
- Frame rule PASSES: vocal mean 0.635, run 11; motion mean 0.632, run 11.
- Picture PASSES: GIRL SINGS — mouth open at 0s (eyes closed, "We"), open at
  1.0/2.0/3.0s, closed smile at 4.0s. CAT in basket, mouth closed throughout.
  Locks hold (straw sun hat with red band, purple hair/eyeshadow, red lipstick,
  red jacket, black crop top, cut-off shorts, blue bike, wicker basket, black
  cat, red collar, yellow bell, blue eyes). No on-screen text.
- NEXT MOVE: volley 13 reroll on PACING/DELIVERY (one variable: brisk, no held
  first word, finish the line by ~1.5s). If the reroll lands ≥2.5s, L84 goes
  structural (t3 CAT picture + captions).

### S21 t6 — L86 "You and me, same pace" — REJECT (PACING)

- File: `takes/mv5_s21_t6.mp4`, md5 `3ff0dc823b84ac0b945c1a70e5160a32`, 5.000s,
  1280×720, 24fps, 120 frames. Generation record:
  `takes/media-generation-mv5-s21-t6-0-dcbee773-d9ba-4e10-b74b-96f4c9b85ff7.mp4`.
- Line sung ONCE — unprompted: "You and me, same pace." Prompted decode
  triple-delivered it, but deliveries 2–3 are hallucinations: all zero-duration
  words at 4.44–5.0s; RMS shows voice 1.0–4.5s, baseline at 4.5–5.0s. First
  delivery: You 0.0–1.36, and 1.36–1.86, me 1.86–2.28, same 2.98–3.76,
  pace 3.76–4.44. Span 4.44s vs song 1.12s (162.46–163.58) → ratio 0.25, CLEAR MISS.
  Extra defect: 0.7s mid-line gap (me ends 2.28, same starts 2.98); quiet head
  (RMS 0.004–0.006 at 0–1.0s — "You" starts barely audible).
- App-start fit: song starts 162.7/162.8/162.9/163.0/163.1 vs take starts
  0.0/1.36/1.86/2.98/3.76; slope 0.11 → playback 9.4x. No legal placement.
- Frame rule PASSES: vocal mean 1.141, run 2; motion mean 1.141, run 2.
- Picture PASSES: GIRL SINGS — mouth slightly open at 0s, open at 1.0/2.0/3.0s,
  closed smile at 4.0s. CAT in basket, mouth closed throughout (eyes half-closed
  at 3.0/4.0s — blink/rest, mouth closed). Locks hold (straw sun hat, purple
  hair/eyeshadow, red lipstick, red jacket, black crop top, cut-offs, blue bike,
  wicker basket, black cat, red collar, yellow bell, blue eyes). No on-screen text.
- NEXT MOVE: volley 13 reroll on PACING (one variable: brisk, no mid-line pause,
  finish the line by ~1.5s). If the reroll lands ≥2.5s, L86 goes structural
  (t3 CAT picture + captions).

### S21 t7 — L88 "Nothing to prove" — KEEP (grey rescue)

- File: `takes/mv5_s21_t7.mp4`, md5 `81663fbac6114f35f920a9f77049209f`, 5.000s,
  1280×720, 24fps, 120 frames. Generation record:
  `takes/media-generation-mv5-s21-t7-0-b3e0f250-0266-499d-8041-626e01151c19.mp4`.
- Line sung ONCE, completely — prompted and unprompted agree: "Nothing to
  prove." Word times: Nothing 0.0–0.5, to 0.5–0.9, prove 0.9–1.5. Span 1.5s
  vs song 0.98s (164.9–165.88) → ratio 0.65, GREY ZONE (0.60–0.80). Re-measured
  per the grey rule: unprompted decode confirms the 1.5s span; the two song
  grids disagree on this line and that disagreement is the whole question.
- App-start fit: song starts 165.2/165.5/165.6 vs take starts 0.0/0.5/0.9;
  slope 0.44, residuals ≤0.08 (starts align beautifully) — but per-word duration
  warps would be 1.67–4x (song "to" is 0.1s in the app grid vs take 0.4s).
  V1-grid fit: song starts 164.58/164.76/165.38 vs take starts 0.0/0.5/0.9;
  slope 0.89 → playback 1.12x, IN BAND; residuals 0/+0.27/0 ("to" lands +0.27s
  late). The app grid shifted L88 ~0.6s later and compressed it (dt_start up to
  +0.74 on "to"); the v2 line span (164.9–165.88) sits between the two grids.
- Decision: KEEP as a grey rescue — assembly places by the v1-grid starts
  (slope 0.89, in-band playback) with "to" +0.27s disclosed, and the master
  gate re-checks L88. If the master gate fails it, L88 falls back to donor
  cover (t3 never sang it). This is a first attempt, not a measured pace floor
  (contrast S28 t4, rejected grey: no legal placement under EITHER grid).
- Frame rule PASSES: vocal mean 0.959, run 2; motion mean 0.738, run 5.
  RMS: voice 0–2.5s (0.10–0.15), baseline after — one delivery, then hold.
- Picture: GIRL SINGS — mouth open at 0s (eyes closed, "Nothing"), open small-o
  at 1.0s ("to"), closed smile at 2.0/3.0/4.0s (line done at 1.5s). CAT in
  basket, mouth closed throughout. Locks hold (red sun hat — solid red variant
  like t4; purple hair/eyeshadow, red lipstick, red jacket, black crop top,
  cut-off shorts, blue bike, wicker basket, black cat, red collar, yellow bell,
  blue eyes). No on-screen text.

### S07 t2 — L15 "One small look from you" — NOT FIRED (generation failure, no retry)

- `media.generate_video` returned `integrity_check_failed`. Per the parent's
  instruction (developer bar on repeating the request, including with changed
  arguments or through another tool/endpoint), NO retry. Vehicle file
  `mv5_s07_t2_vehicle.txt` exists; no take file exists. No QC row.
- S07 stays with s07_t1 (all-CAT) for L15 unless the parent decides otherwise.
  Assembly fallback: two-anchor placement of the CAT take (S15/S20 style) or
  donor cover. The L15 window is tight (1.34s vs the ~2.2s pace floor) — the
  missing insert is a gap, not a blocker.

## Volley 12 result: 2 KEEP / 3 REJECT (s06_t2 KEEP, s21_t7 KEEP grey-rescue;
s21_t4/t5/t6 REJECT on PACING; s07_t2 not fired). Cumulative: 24 KEEP / 40 REJECT
(effective 23 KEEP: 21 + s06_t2 + s21_t7; S28 t1 KEEP superseded by the audit).

## Bridge pace floor (new measurement)

- The three rejected S21 inserts sang their 4–5-word bridge lines in 2.94s (t4),
  3.78s (t5, held first word), 4.44s (t6, mid-line gap) against ~1.1s song
  windows — ratios 0.25–0.35, playbacks 3.3–9.4x. The S21 t3 CAT head did the
  same lines in ~1.9s (playback 1.49x, at the rescue cap). The GIRL inserts are
  slower than the CAT head on the same lines, but all three are first attempts:
  one PACING reroll each is sanctioned for volley 13 (target: finish by ~1.5s).
- t7 shows the floor is not uniform: a 3-word line came in at 1.5s (ratio 0.65,
  grey) and is placeable under the v1 grid. The 4–5-word bridge lines need the
  brisk reroll; if they land ≥2.5s again, the bridge GIRL lines go structural.

## Evidence

- `work/qc_v12.py` + `work/qc_v12/qc_v12_results.json` + `work/qc_v12.log`
- `work/qc_v12/sheets/*_sheet.png` (1 fps contact sheets, 0–4s per take)
- `work/qc_v12/s06_t*.png`, `s21_t4_t*.png`, `s21_t5_t*.png`, `s21_t6_t*.png`,
  `s21_t7_t*.png` (frames at 0.5/1.0/1.5/2.0/2.5/3.0/4.0s)
- `work/qc_v12/tmp_*.f32` (16k mono audio per take)
- `work/volley_12_fire_record.md` (fire record + QC outcomes)
- `work/gemini_song_words_aligned.json` (song word times, both grids)
