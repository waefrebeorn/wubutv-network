# MV-7 S05 t1 — QC (v2, recovery run 4, 2026-11-06 ~16:35 EST)

File: takes/media-generation-mv7-s05-t1-0-79968a79-5115-4681-8ad5-5959655af7f7.mp4
md5: 22c5cd650e508075b5fc112e02c658c6 · 2,376,450 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s05_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp.
snapshot_id: 141ea70d-e963-4ba0-9660-a2e531ae4069:3zw7xd

## Audio / words (faster-whisper small, work/qc_v7/mv7_s05_t1_words.json)
- 13 words, 2 segments: "I kept clicking, kept sticking around" 0.00–3.74 + "Little by little I learned the sound" 4.70–8.36.
- Vehicle lyric delivered exactly once, in order, no repeats. Matches LYRIC_TIMELINE PC1.1–PC1.2.
- Take line span 0.00–8.36s vs song slot 34.02–38.60 (4.58s) → line ratio 4.58/8.36 = 0.548 — CLEAR MISS (<0.60).
  Assembly would need a 1.83x speedup to fit the slot; the v6 generation criterion calls <0.60 a reroll, not a warp.
  Pace-floor check: the take's natural pace for this line is 8.36s; the 0.44x floor would allow ~3.68s, and the slot needs 4.58s —
  a pacing reroll asking the lines briskly in ~4.5–5.0s is plausibly achievable (ratio ~0.92–1.02).
- Repeat-defect scan: PASS. Zero-word? No.

## Frame rule (native 24fps, vocal 0.5–9.5s)
- frames=240, mean_diff=1.201, min=0.627, longest near-dup run = 0 frames. PASS.

## Visual reads (2fps sheet)
- 5.0s: mouth slightly open mid-line, eyes open, identity holds, candle right, monitor edge right, wall notes illegible.
- G1 PASS, G2 PASS (no readable text), G3 PASS, G4 PASS. G5 FAIL on ratio alone.

## VERDICT: REJECT
- G5 FAIL: line ratio 0.548 clear miss — the 13-word pre-chorus is delivered at ~1.55 w/s; the song slot needs ~2.84 w/s.
- Reroll axis (next volley): PACING — vehicle v2 asks the two lines BRISKLY in a 0.5–5.0s window
  ("sings briskly from 0.5s to 5.0s ... Mouth closes on the last word, held ..."), same framing, same Era A still.
- Raster flag carried: 1152x768 (3:2) — assembly crops to 16:9.
