# MV-7 S16 t1 — QC (v2 verbatim, Era B, recovery volley 4, 2026-11-06 ~17:45 EST)

File: takes/media-generation-mv7v2-s16-chorus-2-c2-5-c2-6-s-0-2c3694f8-072a-4efa-9288-76d7e4a9494c.mp4
md5: 9020aead4540165246264240a459c6b3 · 2,638,952 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s16_vehicle.txt verbatim + refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: 4fc4c443-4d4f-4dcc-97d6-9f676599ec55:l18thn

## Audio / words (faster-whisper small, work/qc_v7/mv7_s16_t1_words.json)
- 10 tokens, 1 segment: "I got a thousand little sparks flicking in the dark" 0.00–7.46s.
- 10/10 words exact per the vehicle lyric — "I got a thousand little sparks." (C2.5) + "Flicking in the dark" (C2.6).
- Take line span 0.00–7.46s vs song word span 4.90s (112.86–117.76) → line ratio 4.90/7.46 = 0.657 GREY
  (warp-rescue ~1.52x, at the cap edge — same band as S09 t2's 0.635 / S10's 0.641, both kept).
- "flicking" drawn out 4.22–6.14s (1.92s, p=0.79) — the line's slow spot; assembly warp lands on it.
- SONG_WORDS discrepancy, flagged for assembly caption adjudication: the song-side ASR heard "spots" /
  "Flipping" where the vehicle (and the take) say "sparks" / "flicking". The take follows the vehicle lyric;
  captions should use the performed words, adjudicated at assembly (cf. S10's measured-vs-timeline note).
- RMS check: vocal 0–4.5s, inter-line gap 4.5–5.5s (bins 0.010, 0.004 — true quiet), vocal 5.5–7.5s,
  quiet tail 7.5–10s.
- Repeat-defect scan: no word/line subsequence recurs after first delivery. PASS.
- Zero-word result? No — 10 tokens; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.733, min=0.795, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.698.
- PASS with margin.

## Visual reads (2fps sheet, work/qc_v7/mv7_s16_t1_sheet.png)
- Era B state CORRECT: cork strip, stacks, screens wall, half-burned candle.
- 0.5s: mouth open mid-"I"; identity holds vs Era B still.
- 4.5s: mouth open at "flicking" (4.22–6.14).
- 7.0s: mouth open at "dark" (6.80–7.46); push-in framing across the take.
- The sparks are THICK behind him in the tail rows (bright burst at frame right) — the chorus-2 escalation lands.
- No readable text anywhere. No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds; Era B state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at 0.5s, 4.5s, 7.0s reads; single singer facing camera).
- G5 audio-sync placement: PASS-WITH-FLAG (10/10 words, ratio 0.657 grey — warp ~1.52x at cap edge, disclose).
- G6 banger check: PASS (chorus 2 sparks land; escalation reads).

## VERDICT: KEEP-WITH-FLAG
- Flags: (1) RATIO 0.657 grey — assembly warp ~1.52x at the cap edge. (2) RASTER 1248x704 (~16:9) —
  assembly crops/pads. (3) "flicking" 1.92s drawl (p=0.79). (4) SONG_WORDS "spots/Flipping" vs vehicle
  "sparks/flicking" — caption adjudication owed at assembly. (5) Sings 0.00–7.46 vs window 0.5–9.5s.
