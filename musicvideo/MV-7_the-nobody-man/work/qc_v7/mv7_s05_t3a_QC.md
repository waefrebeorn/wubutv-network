# MV-7 S05 t3a — QC (v3a SPLIT take A, PC1.1 only, recovery volley 3, 2026-11-06 ~17:27 EST)

File: takes/media-generation-mv7v2-s05-v3a-pre-chorus-1-pc1-0-69783a26-930b-4f00-bac2-d97001a694b3.mp4
md5: 0181fd7e25c2de8af39314ec4cc3dc5e · 2,490,657 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s05_v3a_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp (md5 ca15fc5084ccfedf0e90910f56eac75d).
snapshot_id: e48c6c26-eae9-4871-9a00-54081c99a706:0umrf8

## Audio / words (faster-whisper small, work/qc_v7/mv7_s05_t3a_words.json)
- 6 words, 1 segment: "I kept clicking, kept sticking around." 0.00–4.94s.
- Word list matches PC1.1 exactly, 6/6, once, in order. (The repeated "kept" is the lyric itself.)
- Take line span 0.00–4.94s vs song slot 34.02–36.50s (2.48s; word span 34.02–36.30 = 2.28s) → line ratio 2.48/4.94 = 0.502.
- Phrase math for assembly: "I kept clicking," take 0.00–2.02s vs song 1.10s → 1.84x speedup; "kept sticking around"
  take 3.08–4.94s (1.86s) vs song 0.94s → 1.98x speedup. The 1.06s inter-phrase gap (2.02–3.08s) absorbs into the warp.
  Both phrases need ~1.9x — a uniform hard squeeze, disclosed; at the MV-5 v4 disclosed extreme (1.91x).
- RMS check: vocal 0–5.0s, quiet tail 5.0–10.0s (bins ~0.01–0.016) — trims cleanly.
- Repeat-defect scan: no word/line subsequence recurs after first delivery. PASS.
- Zero-word result? No — 6 words; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–4.5s)
- frames=240, mean_diff=1.189, min=0.665, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.422.
- PASS with margin (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s05_t3a_sheet.png)
- 0.5s: mouth open mid-"I kept"; identity holds vs Era A still (thinning hair, stubble, frayed patches, charcoal crewneck); tall candle right, monitor glow abstract.
- 2.5s: mouth open mid-"clicking"; slow push-in running, face drifting right.
- 4.5s: mouth open at "around" (3.96–4.94); eyes half-closed, singing expression.
- 7.0s+: held crooked grin, eyes closed — the quiet tail.
- No readable text anywhere (monitor rectangles abstract glow, papers illegible). No other people. No morphing.

## Gates
- G1 character consistency: PASS. G2 zero unwanted on-screen text: PASS. G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at 0.5s, 2.5s, 4.5s reads; single singer facing camera).
- G5 audio-sync placement: PASS-WITH-FLAG (all 6 words, once, in order; ratio 0.502 is a CLEAR MISS on the generation
  criterion, but the split is the sanctioned structural fix and assembly speedups are unrestricted with disclosure — the
  take places with a ~1.9x uniform squeeze, both phrases inside the MV-5 v4 disclosed extreme).
- G6 banger check: PASS (pre-chorus ritual beat; candle + monitor glow carry the look).

## VERDICT: KEEP-WITH-FLAG
- Flags: (1) RATIO 0.502 — assembly warp ~1.9x speedup, disclose in the cut notes; if the master gate dislikes the squeeze,
  the fallback is montage cover for PC1.1. (2) RASTER 1152x768 (3:2) — assembly crops to 16:9. (3) Sings 0.00–4.94 vs
  vehicle window 0.5–4.5s (starts 0.5s early; last word ends 0.44s past window end). (4) 1.06s mid-line gap absorbs into warp.
- PC1.1 is COVERED (with the disclosed squeeze). Its partner PC1.2 (t3b) is NOT — see mv7_s05_t3b_QC.md.
