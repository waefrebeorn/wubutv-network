# MV-7 S23 t1 — QC (v2 verbatim, Era C, volley 6, 2026-11-06 ~18:15 EST)

File: takes/media-generation-mv7v2-s23-final-chorus-fc10-0-553c819f-bd9e-4823-ae36-e538adf3d0d7.mp4
md5: c07abd209f4836ed00cdef346882f615 · 3,150,948 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s23_vehicle.txt verbatim + refs/nobody_man_v2_eraC.webp (md5 317d8fcd3f513261fd93992f5721981f).
snapshot_id: 69e7e68c-8ebe-485d-80f0-b7eeb0130b69:w6o5v2

## Audio / words (faster-whisper small, work/qc_v7/mv7_s23_t1_words.json)
- 7 tokens, 1 segment: "Yeah, I turn the small things grand" 0.00–6.60s.
- Expected 7 words (song 168.16–173.30, span 5.14s): FC.10 — ALL LAND, once, in order.
- FC.10 LYRIC RESOLVED: the take sings the SHEET line ("Yeah, I turn the small things grand") exactly,
  against the ASR's "can't turn the small things cray". The LYRIC_TIMELINE [uncertain] flag is CLOSED
  in favor of the sheet — caption = sheet, no ear check owed at assembly.
- Take span 0.00–6.60s vs song 5.14s → ratio 0.779 GREY. Warp-rescue ~1.28x overall.
- RMS check: vocal continuous 0–6.6s; quiet tail 6.6–10s (held grin, as vehicled — "quiet triumph, no swell").
- Min word prob 0.507 ("Yeah," at 0.0s, cold-start).

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=2.267, min=1.176, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 2.203.
- PASS (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s23_t1_sheet.png)
- Era C state CORRECT: wall of tiny glowing screens, low stub candle, stacks of paper.
- 0.5s: mouth open mid-"Yeah"; identity holds vs Era C still.
- 5.0s: mouth open mid-"things"/"grand" ("things" 4.94–5.80 take time).
- No readable text anywhere (screens are abstract glow). No other people. No morphing.
- Flags: a STRONG blue/purple light wash on the face from ~4s onward (rows 3–4 — the monitor glow went
  blue-violet, stronger than the "cool monitor glow" in the vehicle; the face stays readable and the mouth
  visible, so a flag not a reject); eyes closed in several late frames (same class as S17/S21);
  slow push-in drift across the clip (medium → close-up); 1152x768 raster.

## Gates
- G1 character consistency: PASS (identity holds; Era C state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at reads; single singer facing camera).
- G5 audio-sync placement: PASS with flag (7/7 exact, once, in order; grey ratio 0.779, warp-rescue ~1.28x).
- G6 banger check: PASS ("turn the small things grand" settles as planned — quiet triumph, no swell).

## VERDICT: KEEP-WITH-FLAG
- Flag: grey ratio 0.779 (warp ~1.28x, disclose at assembly); strong blue/purple face wash from ~4s;
  eyes closed in several late frames; slow push-in drift; 1152x768 raster. FC.10 lyric uncertainty CLOSED.
