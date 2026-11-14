# MV-2 Q6 — TAKE LEDGER (restages)

Cap: 6 videos this run incl. re-fires. Used: 4/6 (S04a t1, S07 t1, S21 t1,
S07 t2 re-fire). Spare: 2.

Anchor: work/q6/voice_anchor_night.png — frame 3.0s of S06a t2 (v6 KEEP).
Read back before use: night-VOICE, face to camera, CADMIUM square, mic,
blank ticket, night road. 1280x720.

## S04a — CANDIDATE (warp-rescued)
- Raw: takes/media-generation-mv2-s04a-q6-t1-0-951082e1-645b-48a0-a074-d43b026f46e4.mp4
- Canonical: takes/mv2_s04a_q6_t1.mp4, md5 6009bfafda09bff6c5cb54144e430101,
  1280x720/24fps/10.000s, h264+AAC.
- Lyric: 22/22 exactly once (now through by, incl. tail "watching money
  flash by"). Vocal 0–9.48s vs song 6.74s → ratio 0.711 GREY.
- Frame (unwarped): PASS (mean 0.82, near-dup run 6, frozen run 1).
- Character: PASS (2s/5s/8s: night-VOICE lock, face to camera, mouth open
  mid-vocal, mic, blank ticket, CADMIUM square).
- Text: PASS (booth panels are abstract orange/red light bars, no legible
  words at full res; same signals-not-letters class as S07 t2 v2 nit).
- Drift: median +5.9f, range -0.3 to +15.1 (diagnostic only).
- Warp-rescue: whole-clip warp 1.1322x → takes/mv2_s04a_q6_t1_warped.mp4,
  md5 bcbfc3421985ca9d0cc4699635cb7023, 1280x720/24fps/8.833s.
  Warped QC: 22/22, vocal 0–8.38s, ratio 0.804 IN BAND, frame PASS
  (mean 0.91, run 6), drift median +5.9f. Assembly factor 8.38/6.74 =
  1.2433 (inside 1.25 cap). Use the WARPED take at tau 0–8.38.
- VERDICT: CANDIDATE (warp-rescued). S04a slot COVERED.

## S07 — t1 REJECTED; t2 CANDIDATE
- t1 raw: takes/media-generation-mv2-s07-q6-t1-0-67677755-cca3-4860-9596-a16ee48484a6.mp4
- t1 canonical: takes/mv2_s07_q6_t1.mp4, md5 563b67fed35048a75620612988ea2339,
  1280x720/24fps/10.000s.
- t1 lyric: 10/10, vocal 0–7.66s, ratio 1.110 IN BAND. Drift median -8.2f.
- t1 frame: FAIL (mean 0.61, near-dup run 33 at 1.71–3.08s mid-vocal;
  only 3/185 transitions >1.0 — low-motion take).
- t1 character: PASS (night-VOICE lock at 2s/5s/8s).
- t1 text: FAIL — legible red "STOP" signs on both booths at 2s/5s/8s
  (persistent through the take, same class as the volley-18 restage).
- t1 VERDICT: REJECTED (frame + text). Re-fire on the STAGING axis only.
- t2 raw: takes/media-generation-mv2-s07-q6-t2-0-6e09ea40-4757-4fd9-92eb-7259c18fee77.mp4
- t2 canonical: takes/mv2_s07_q6_t2.mp4, md5 ecdd4255b76463d005369aac7762739d,
  1280x720/24fps/10.000s.
- t2 lyric: 10/10 exactly once, vocal 0–7.14s vs song 8.50s → ratio 1.190
  IN BAND. Drift median -15.0f, range -38.4 to +2.2 — the "toll" word
  is held long and arrives early on the fit map (same disclosed class
  as the v6final S07 take's -32.7f "toll" nit; diagnostic only).
- t2 frame: PASS (mean 0.86, near-dup run 1, frozen run 1; 79/172
  transitions >1.0 — the motion sentence worked).
- t2 character: PASS (2s/5s/8s: night-VOICE lock, mouth open mid-vocal,
  mic, blank ticket, CADMIUM square; closed smile hold at 8s post-vocal).
- t2 text: PASS — booths are plain dark shapes, traffic lights are
  glowing dots, NO signs, NO lit panels, NO legible words anywhere.
- VERDICT: CANDIDATE. S07 slot COVERED by t2. t1 stays on disk, rejected.

## S21 — CANDIDATE (disclosed dropped-"to" micro-gap)
- Raw: takes/media-generation-mv2-s21-q6-t1-0-d43d8d9a-0a6d-4a1e-8c62-2f94ee95fdf4.mp4
- Canonical: takes/mv2_s21_q6_t1.mp4, md5 412a5ca82757feb55047ff083f65bd39,
  1280x720/24fps/10.000s, h264+AAC.
- Lyric: 13/14, deletion-tolerant match — drops the second "to" (take
  goes "faster" 4.60–5.40, gap, then "the" 5.40). SAME minor class as
  the v6final take (13/14, same drop). Vocal 0–8.34s vs song 9.24s →
  ratio 1.108 IN BAND. Drift median +1.2f, range -19.3 to +13.3 (the
  -19.3f is the "the" mapped across the dropped-"to" gap; diagnostic).
- Frame: PASS (mean 0.66, near-dup run 3, frozen run 1).
- Character: PASS (2s/5s/8s: night-VOICE lock, mouth open mid-vocal,
  mic, blank ticket, CADMIUM square).
- Text: PASS (booth panels are abstract orange/red light bars, no legible
  words at full res; same signals-not-letters class as S04a).
- VERDICT: CANDIDATE with disclosed dropped-"to" micro-gap (song word
  "to" 211.18–212.60 unmouthed; caption carries it). S21 slot COVERED.

## Method notes (for the record)
- QC scripts: work/q6/qc_v6_q6.py (t1 takes) + work/q6/qc_v6_q6_followup.py
  (S07 t2 + S04a warped). Whisper base int8, same mishear map as volley 17.
- The strict subsequence matcher BREAKS on a mid-beat dropped word (S21
  first ran 8/14 — the matcher stalls at the dropped "to" and never
  matches the rest). Fixed with deletion-tolerant alignment (volley-18
  S21 precedent): skip a beat word when the take word matches the NEXT
  beat word; dropped words are recorded, not absorbed. Matched entries
  carry their beat index so drift maps past drops.
- Q6 restage finding: the image anchor carried the night-VOICE face
  into all four takes (4/4 character PASS, incl. the rejected t1) —
  the volley-17/18 face failure is closed by the anchor, not by prose.
  The remaining lottery is background text (1/4 takes drew STOP signs)
  and motion (1/4 low-motion) — both fixed by the staging re-fire.
