# MV-7 S05 t2 — QC (v2 pacing reroll, recovery volley 2, 2026-11-06 ~16:55 EST)

File: takes/media-generation-mv7v2-s05-v2-pre-chorus-1-pc1-0-2027fb19-64a4-4872-9fed-16acc838d6d0.mp4
md5: ca22497ecb174eb0d45b69bea19fd456 · 2,542,945 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s05_v2_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp.
snapshot_id: f6f9cd42-ad5e-499b-b743-34abd8d4a136:dspckm

## Audio / words (faster-whisper small, work/qc_v7/mv7_s05_t2_words.json)
- 13 words, 2 segments: "I kept clicking, kept sticking around" 0.00–3.66 + "Little by little I learned the sound" 4.40–8.10.
- Vehicle lyric delivered exactly once, in order, no repeats. Matches LYRIC_TIMELINE PC1.1–PC1.2.
- Take line span 0.00–8.10s vs song slot 34.02–38.60 (4.58s) → line ratio 4.58/8.10 = 0.565 — CLEAR MISS (<0.60).
  Assembly would need a 1.77x speedup to fit the slot; the v6 generation criterion calls <0.60 a reroll, not a warp.
- The brisk 0.5–5.0s window moved the pace 8.36s (t1) → 8.10s (t2) only: TWO pulls, same ~8s floor. The 13-word pre-chorus will not
  compress below ~8s in a single take — the pace floor for this line, not a prompting failure.
- Repeat-defect scan: PASS. Zero-word? No.

## Frame rule (native 24fps, vocal 0.5–9.5s)
- frames=240, mean_diff=1.468, min=0.633, longest near-dup run = 0 frames. PASS.

## Visual reads (2fps sheet, work/qc_v7/mv7_s05_t2_sheet.png)
- 5.0s: mouth slightly open mid-line, eyes open, identity holds, candle right, monitor edge right, wall notes illegible.
- Slow push-in through the clip; eyes closed through much of the second line (expressive singing, not a fail).
- G1 PASS, G2 PASS (no readable text), G3 PASS, G4 PASS. G5 FAIL on ratio alone.

## VERDICT: REJECT
- G5 FAIL: line ratio 0.565 clear miss — the 13-word pre-chorus is delivered at ~1.60 w/s; the song slot needs ~2.84 w/s.
- Reroll axis (next volley): SPLIT — fire PC1.1 and PC1.2 as SEPARATE vehicles (two takes for the slot), each a short line at its own
  brisk pace. This is a restage of the slot, not a third reroll of the same vehicle: the pacing axis is exhausted (t1 natural 8.36s,
  t2 brisk 8.10s — same floor). Per-line math for the split: PC1.1 "I kept clicking, kept sticking around" 6 words over song 2.48s;
  PC1.2 "Little by little, I learned the sound" 7 words over song 2.10s — each still tight, brisk windows required.
- Raster flag carried: 1152x768 (3:2) — assembly crops to 16:9.
