# MV-7 S09 t2 — QC (v2 pacing reroll, recovery volley 3, 2026-11-06 ~17:27 EST)

File: takes/media-generation-mv7v2-s09-v2-chorus-1-c1-8-son-0-9eb3da14-e138-4ab0-9112-78f8178a9838.mp4
md5: 68a47b6e724cda3f2dfb1d61686a131d · 3,778,050 B
ffprobe: h264 1280x720, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s09_v2_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp (md5 ca15fc5084ccfedf0e90910f56eac75d).
snapshot_id: 52fb3253-e4b1-427b-8041-9026072f3449:en2kx5

## Audio / words (faster-whisper small, work/qc_v7/mv7_s09_t2_words.json)
- 4 words, 1 segment: "Nobody man, nobody man." 0.00–6.42s.
- Word list matches C1.8 exactly, 4/4, once, in order. (The repeated "Nobody man" is the lyric itself.)
- Take line span 0.00–6.42s vs song word span 63.72–67.80s (4.08s) → line ratio 4.08/6.42 = 0.635 — GREY (0.60–0.80).
- Phrase math for assembly: occurrence 1 take 0.00–2.22s (2.22s) vs song 2.54s → 0.87x; occurrence 2 take 3.54–6.42s (2.88s)
  vs song 1.54s → 1.87x speedup. The 1.32s inter-occurrence gap (2.22–3.54s) absorbs into the warp. Overall warp-rescue ~1.57x —
  same class as S10 t1's 1.56x, disclosed.
- Brisk window moved the pace: t1 7.66s → t2 6.42s (ratio 0.426 → 0.635).
- RMS check: vocal 0.5–3.5s and 4.5–7.0s; quiet 3.5–4.5s (the gap) and 7.0–10.0s tail — trims cleanly.
- Repeat-defect scan: no word/line subsequence recurs after first delivery. PASS.
- Zero-word result? No — 4 words; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–4.5s)
- frames=240, mean_diff=4.681, min=1.513, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 3.620.
- PASS with wide margin — strongest motion of the volley (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s09_t2_sheet.png)
- 0.5s: mouth open mid-"Nobody"; identity holds vs Era A still; tall candle right, cork board behind.
- 1.0s: mouth open mid-"man"; SPARKS BURST — colorful bokeh spark clusters ignite at frame right and left, the C1.8 motif beat.
- 3.0s: mouth in held grin during the inter-occurrence gap; sparks still glowing behind him.
- 4.0s: mouth open again for occurrence 2; sparks continue across the frame.
- 7.0s+: held crooked grin, eyes closed — the quiet tail.
- No readable text anywhere (cork-board papers illegible, glow abstract). No other people. No morphing.

## Gates
- G1 character consistency: PASS. G2 zero unwanted on-screen text: PASS. G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at both occurrences; single singer facing camera).
- G5 audio-sync placement: PASS-WITH-FLAG (all 4 words, once, in order; ratio 0.635 grey — warp-rescue ~1.57x, disclose).
- G6 banger check: PASS (tag-chant close: sparks visibly burst at frame right — the strongest motif hit of the volley).

## VERDICT: KEEP-WITH-FLAG
- Flags: (1) RATIO 0.635 grey — assembly warp-rescue ~1.57x, disclose; phrase 2 carries the squeeze (1.87x). (2) RASTER 1280x720
  TRUE 16:9 — no crop needed at assembly. (3) Sings 0.00–6.42 vs vehicle window 0.5–4.5s (starts 0.5s early; second occurrence
  lands 3.54–6.42, past the window). (4) 1.32s inter-occurrence gap absorbs into the warp.
- C1.8 is COVERED (with the disclosed warp). The S09 pacing axis is closed — no further reroll owed.
