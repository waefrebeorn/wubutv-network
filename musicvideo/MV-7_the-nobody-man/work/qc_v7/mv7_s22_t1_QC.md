# MV-7 S22 t1 — QC (v2 verbatim, Era C, volley 6, 2026-11-06 ~18:15 EST)

File: takes/media-generation-mv7v2-s22-final-chorus-fc8-fc9-0-8461ab5e-54b4-45ef-a0ba-e937660d824f.mp4
md5: 6ed121aeb20750219f000797e9848e39 · 3,132,750 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s22_vehicle.txt verbatim + refs/nobody_man_v2_eraC.webp (md5 317d8fcd3f513261fd93992f5721981f).
snapshot_id: c25451cd-5f2f-441a-bc16-86c81045b81a:laqwri

## Audio / words (faster-whisper small, work/qc_v7/mv7_s22_t1_words.json)
- 6 tokens, 1 segment: "Nobody man, I'm the nobody man." 0.00–7.52s.
- Expected 6 words (song 160.02–168.16, span 8.14s): FC.8 "Nobody Man" + FC.9 "I'm The Nobody Man" —
  ALL LAND, once, in order. No repeats.
- Take span 0.00–7.52s vs song 8.14s → ratio 1.082 IN BAND. Per-line: FC.8 1.43 (speedup, fine),
  FC.9 1.13. No warp needed beyond a light stretch.
- RMS check: vocal in two bursts (FC.8 ~0–2.9s, FC.9 ~4–7.5s) with a quiet 1.1s inter-line gap 2.9–3.98s
  (song FC.8→FC.9 has no gap — the gap warps out at assembly); quiet tail 7.5–10s.
- Min word prob 0.286 ("Nobody" at 0.0s, cold-start) — the word sequence is exact and in order; the low
  prob is the first-word cold start, not a mishear.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=2.676, min=1.469, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 2.581.
- PASS (FAIL would be run ≥24f or mean <0.5). Strongest frame rule of the volley on min-diff.

## Visual reads (2fps sheet, work/qc_v7/mv7_s22_t1_sheet.png)
- Era C state CORRECT: wall of tiny glowing screens, low stub candle, stacks of paper.
- ONE BRIGHTER LIGHT READS: one steady bright white square in the wall, right of his head, present
  across the tiles (upper right in rows 1–3) — a touch brighter than all the rest, as vehicled.
  The visual peak of the Final Chorus lands.
- 0.5s: mouth open mid-"Nobody"; identity holds vs Era C still.
- 5.0s: mouth open at the FC.9 onset ("I'm", 3.98–5.94 take time).
- No readable text anywhere (screens are abstract glow). No other people. No morphing.
- Flags: slow push-in drift across the clip (medium → close-up), same drift class as the volley;
  1152x768 raster (assembly crops to 16:9).

## Gates
- G1 character consistency: PASS (identity holds; Era C state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: PASS (6/6 exact, once, in order; ratio 1.082 in band).
- G6 banger check: PASS (the peak lands — whole wall lit + one brighter steady light).

## VERDICT: KEEP-WITH-FLAG
- Flag: 1152x768 raster; slow push-in drift; 1.1s inter-line gap warps out. The brighter light reads.
