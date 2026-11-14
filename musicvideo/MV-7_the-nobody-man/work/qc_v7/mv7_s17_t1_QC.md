# MV-7 S17 t1 — QC (v2 verbatim, Era B, recovery volley 5, 2026-11-06 ~18:10 EST)

File: takes/media-generation-mv7v2-s17-chorus-2-c2-7-c2-8-s-0-70773246-8933-4a21-a3b9-75bd80853392.mp4
md5: 5440c92c4aba9d1fffd69e0f72d41568 · 2,845,028 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s17_vehicle.txt verbatim + refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: 5e92b1c2-75a8-437e-ad9f-427d8460b876:vxnalh

## Audio / words (faster-whisper small, work/qc_v7/mv7_s17_t1_words.json)
- 6 tokens, 1 segment: "I'm the nobody man, nobody man." 0.00–7.36s.
- Expected 6 words (song 117.86–123.26, span 5.40s): C2.7 "I'm The Nobody Man" + C2.8 "Nobody Man" —
  ALL LAND, once, in order. No repeats.
- Take span 0.00–7.36s vs song 5.40s → ratio 0.734 GREY. Per-line: C2.7 take 0.00–3.52s (3.52s)
  vs song 2.46s → 0.70 (assembly warp ~1.43x, inside the 1.5x rescue cap); C2.8 take 4.46–7.36s
  (2.90s) vs song 2.94s → 1.01. Warp-rescue ~1.36x overall.
- RMS check: vocal in two bursts (C2.7 ~1.5–4.0s, C2.8 ~5.5–7.5s) with a 0.94s inter-line gap
  3.52–4.46s — the gap warps out at assembly (song has no gap between C2.7/C2.8); quiet tail 7.4–10s.
- Min word prob 0.694 — no low-prob words.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=2.341, min=0.645, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 2.215.
- PASS (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s17_t1_sheet.png)
- Era B state CORRECT: cork strip crowded with slips, stacks of paper, screens wall, half-burned candle.
- 0.5s: mouth open mid-"I'm"; identity holds vs Era B still.
- 4.5s: mouth open at the C2.8 onset ("nobody", 4.46–6.26 take time).
- 7.5s: held crooked grin after the last word; chorus hangs into the break as vehicled.
- No readable text anywhere (slips and screens illegible/abstract glow). No other people. No morphing.
- Flags: eyes closed through much of the take (same flag class as S06/S07 — singing with eyes shut);
  slow push-in drift across the clip (medium → close-up), same drift class as S12/S13/S15 this volley.

## Gates
- G1 character consistency: PASS (identity holds; Era B state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: PASS with flag (6/6 exact, once, in order; grey ratio 0.734, warp-rescue ~1.36x).
- G6 banger check: PASS (Chorus 2 push-in holds; the hook lands twice at the chorus tail).

## VERDICT: KEEP-WITH-FLAG
- Flag: grey ratio 0.734 (C2.7 warp ~1.43x, disclose at assembly); eyes closed through much of the
  take; slow push-in drift; 0.94s inter-line gap warps out.
