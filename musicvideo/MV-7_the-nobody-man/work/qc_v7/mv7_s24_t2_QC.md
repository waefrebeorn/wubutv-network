# MV-7 S24 t2 — QC (v2 lyric-as-performed, Era C, volley 8, 2026-11-06 ~18:44 EST)

File: takes/media-generation-mv7v2-s24-t2-0-c51ead16-af8d-41e9-9a23-9395fae4ad5f.mp4
md5: 2d9dd5ff1a6c81342925ae3f88909cd9 · 3,355,182 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s24_v2_vehicle.txt VERBATIM (single verbatim re-fire — volley 7's
attempt errored in the tool, no file produced; tool error, not a content verdict) + refs/nobody_man_v2_eraC.webp
(md5 317d8fcd3f513261fd93992f5721981f).
snapshot_id: 1fc1e226-7fa3-4396-bae1-c709ac215433:af2fwy

## Audio / words (faster-whisper small, work/qc_v7/mv7_s24_t2_words.json)
- 8 tokens, 1 segment: "I'm the nobody man, nobody man, nobody man." 0.00–7.92s.
- Word times: "I'm" 0.00–1.56 · "the" 1.56–1.72 · "nobody" 1.72–2.52 · "man" 2.52–3.46 ·
  "nobody" 4.04–5.10 · "man" 5.10–5.96 · "nobody" 6.24–6.86 · "man" 6.86–7.92.
- Min word prob 0.808 — no low-prob words. The take sings the MEASURED 8-word chant exactly once,
  in order: "I'm The Nobody Man, Nobody Man, Nobody Man" — the lyric-as-performed axis LANDED.
  (t1 sang the chant ×2, 12 words, with a second "I'm" that had no song home.)
- Tail split-half (5–10s, work/qc_v7/mv7_s24_t2_tail_words.json): "Nobody man, nobody man" 0.0–2.84
  (absolute 5.0–7.84s) — the second and third repeats only; no fourth chant, no extra words.
  RMS bins after 8s drop to 0.031/0.016/0.022/0.019 — silent hold to the end, as vehicled.

## Ratio / warp math (song side: SONG_WORDS.json 173.30–183.24)
- Whole line: song 9.94s / take 7.92s = ratio 1.255 — grey-zone edge (grey 1.25–1.60);
  uniform whole-line warp 0.797x, inside the 2x slow cap. NOT a clear miss.
- Per phrase: P1 "I'm the nobody man" song 2.96s / take 3.46s = 0.855 IN BAND.
  P2 "nobody man" song 5.14s / take 1.92s = 2.68 — the song holds "nobody" 3.92s (176.26–180.18)
  against the take's 1.06s; a phrase-smooth warp for P2 alone would be 0.373x playback, past the
  0.5x floor. P3 "nobody man" song 1.80s / take 1.68s = 1.07 IN BAND.
- Assembly call, disclosed: the P2 hold must be carried by a ramp through the held note (the mouth
  is open through the hold — slowing during an open-mouth hold reads far better than slowing
  articulation) or by the uniform 0.797x warp. Precedent: S08 t2 kept with per-phrase warps at cap
  edges (1.76x/1.77x/0.55x) flagged, not rejected. The word identity is exact; the pace issue is
  a disclosed warp extreme, not a content miss.

## Frame rule (native 24fps, vocal window 0.5–5.5s)
- frames=240, mean_diff=2.884, min=1.648, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 3.063.
- PASS. (FAIL would be run ≥24f or mean <0.5.)

## Visual reads (2fps sheet, work/qc_v7/mv7_s24_t2_sheet.png)
- Era C state CORRECT: wall of tiny glowing screens, low stub candle (visible rows 1–2), paper stacks.
- PULL-BACK DID NOT LAND: the framing tightens medium → close-up across the take — a slow PUSH-IN,
  the same drift class as all five Era C volley-6 takes (and the Era B volley-5 takes). The final frame
  is a close-up, so the frame rhyme is weaker than t1's (t1 pulled back to the wider desk). Assembly
  trims/crops; push-in drift is not a reject on its own (standing volley 5/6 ruling).
- Mouth: OPEN through the chant (0.5s mid-"I'm", ~4s P2 onset, ~6.5s P3 onset all open); closed
  held crooked grin 7.5–9.5s — exactly as vehicled. Eyes heavy-lidded, mostly open; closed in the
  final grin hold (same class as S21/S23 tails).
- No readable text anywhere (screens are abstract glow). No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds; Era C state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open during the chant, closed for the hold;
  push-in drift noted, not a fail).
- G5 audio-sync placement: PASS-WITH-FLAG — word identity EXACT (8/8, once, in order); whole-line
  ratio 1.255 grey-edge (uniform warp 0.797x inside caps); P2 phrase warp 2.68x disclosed for assembly.
- G6 banger check: PASS (final chorus tag + outro close; the picture carries the close).

## VERDICT: KEEP-WITH-FLAG
- LYRIC-AS-PERFORMED axis CLOSED — the measured 8-word chant lands exactly. No v3 (this was the
  re-fire of the written v2 vehicle; the axis is satisfied, not exhausted).
- Flags: (1) P2 phrase warp 2.68x slow at phrase level — assembly ramps through the held "nobody"
  or takes the uniform 0.797x warp; disclose. (2) Slow push-in, not the vehicled pull-back — final
  frame is a close-up; frame rhyme weaker than t1's; assembly trims/crops. (3) Sings 0.00–7.92 vs
  vehicled 0.5–5.5s window (starts early, runs long — the song span is 9.94s, so the longer
  delivery fits the song better than a 5.0s one would). (4) 1152x768 raster (Era C 3:2 still, crops
  to 16:9). (5) Eyes closed in the final grin hold.
- S24 is COVERED. All 24 scenes now covered: 22 KEEP + S01/S15/S20 structural at assembly.
