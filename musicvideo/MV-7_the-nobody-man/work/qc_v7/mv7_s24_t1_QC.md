# MV-7 S24 t1 — QC (v2 verbatim, Era C, volley 6, 2026-11-06 ~18:15 EST)

File: takes/media-generation-mv7v2-s24-final-chorus-tag-cha-0-8a6124cb-18e1-44a4-a038-d3a768b78605.mp4
md5: de3d132ba3598dc8c2d336410c57a453 · 3,418,406 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s24_vehicle.txt verbatim + refs/nobody_man_v2_eraC.webp (md5 317d8fcd3f513261fd93992f5721981f).
snapshot_id: a66d66be-9b0d-4c07-a751-0c5a3224e39c:mvg0hi

## Audio / words (faster-whisper small, work/qc_v7/mv7_s24_t1_words.json)
- 12 tokens, 1 segment: "I'm the nobody man, nobody man, I'm the nobody man, nobody man." 0.00–6.62s.
- Expected per the VEHICLE: "I'm The Nobody Man, Nobody Man" ×3 = 18 words. Take delivers ×2 (12 words).
- Expected per the MEASURED SONG (SONG_WORDS.json, 173.30–183.24): "I'm the nobody man," (173.30–176.26)
  + "nobody man," (176.26–181.40) + "nobody man" (181.44–183.24) = 8 words — the performed tag chant is
  "I'm The Nobody Man, Nobody Man, Nobody Man", NOT three full pairs. The vehicle's lyric OVER-ASKS
  relative to the performed song (the timeline's "×~3" was [inferred], and the inference was wrong).
- Word-identity mismatch: the take's second "I'm the nobody man" (3.32–4.86s) would land on the song's
  first "Nobody Man" (176.26–181.40) — "I'm" sung where the song says "Nobody". Word identity outranks
  open-mouth state: the take cannot cover FC.T as sung.
- Pace also fails the salvage: song pair 1 (173.30–181.40, 8.10s, 6 words) vs take pair 1 (0.00–3.04s) →
  2.66x slow, past the 2x slow cap. No warp-rescue.
- Tail split-half (5–10s): "Nobody, man." only — the second pair's tail, no third chant. Tail RMS after
  6.62s ~0.005–0.019 = silent hold, as vehicled.
- Min word prob 0.858 — no low-prob words. The take is confident; the LYRIC is wrong.

## Frame rule (native 24fps, vocal window 0.5–5.5s)
- frames=240, mean_diff=3.605, min=2.424, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 2.928.
- PASS — strongest frame rule of the volley. (FAIL would be run ≥24f or mean <0.5.)

## Visual reads (2fps sheet, work/qc_v7/mv7_s24_t1_sheet.png)
- Era C state CORRECT: wall of tiny glowing screens, low stub candle, stacks of paper, keyboard.
- SLOW PULL-BACK READS: rows 1–2 medium close-up, rows 3–4 pull back to the wider desk (keyboard, papers,
  stacks both sides) — the frame rhyme lands; the final framing rhymes with the opening composition.
- 0.5s: mouth open mid-"I'm"; 5.0s: mouth open at the second pair's "nobody" (5.30–5.68 take time).
- 7.5s–9.5s: mouth closed, held crooked grin, still and silent to the end — exactly as vehicled.
- No readable text anywhere (screens are abstract glow). No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds; Era C state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open during the chant, closed for the hold).
- G5 audio-sync placement: FAIL — word identity: take sings "I'm The Nobody Man" ×2, song sings it ×1
  (then "Nobody Man" ×2); second "I'm" has no song home, and the first-pair warp (2.66x) is past the cap.
- G6 banger check: PASS (pull-back + frame rhyme land; the picture is right, the lyric is wrong).

## VERDICT: REJECT
- Reroll axis: LYRIC-AS-PERFORMED v2 — vehicle lyric = the MEASURED 8-word chant ("I'm The Nobody Man,
  Nobody Man, Nobody Man"), stated once, no third pair. Same axis as S01 v3 (elided chant). Visuals PASS;
  only the lyric needs restating.
