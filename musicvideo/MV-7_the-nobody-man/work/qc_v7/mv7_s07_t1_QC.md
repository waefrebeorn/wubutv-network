# MV-7 S07 t1 — QC (v2 hook test, recovery run 4, 2026-11-06 ~16:25 EST)

File: takes/media-generation-mv7-s07-t1-0-2491c8cc-5254-4c13-9621-14a85c8da176.mp4
md5: 9f9a41cdea6d746387de655175b8729e · 2,585,095 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s07_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp (md5 ca15fc5084ccfedf0e90910f56eac75d).
snapshot_id: cc0957a2-a2aa-4a5f-bec8-2af3517f5485:oimd9o

## Audio / words (faster-whisper small, work/qc_v7/mv7_s07_t1_words.json)
- 19 words, 2 segments. Full lyric heard exactly once, in order, NO repeats:
  "I'm the nobody man" 0.00–2.00 · "Still here still stand I post I fade I post again. I'm the nobody man" 2.88–9.70
- Word list matches the vehicle lyric 19/19 (case-insensitive).
- Take line span 0.00–9.70s (9.70s) vs song slot 47.02–56.18s (9.16s) → line ratio 0.944 — IN the 0.80–1.25 band.
- Repeat-defect scan: no word/line subsequence recurs after first delivery. PASS.
- Zero-word result? No — 19 words; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.729, min=0.831, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.696.
- PASS with margin (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s07_t1_sheet_*.png)
- 0.5s: mouth open mid-"I'm"; identity holds vs Era A still (thinning hair, stubble, frayed patches both shoulders, charcoal crewneck); tall candle right, phone blank-glow on desk.
- 5.0s: mouth OPEN mid-line ("I" 5.02–5.52); slow push-in visible (framing tighter than still).
- 8.0s: mouth open at "I'm" onset (8.06); eyes closed, singing expression.
- 9.5s: mouth in open grin, last word "man" ends 9.70; held crooked grin end state.
- No readable text anywhere (monitor rectangles abstract glow, phone blank, papers illegible). No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds across all sampled frames).
- G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at 0.5s, 5.0s, 8.0s reads; single singer facing camera).
- G5 audio-sync placement: PASS (ratio 0.944; all 19 words in order, once).
- G6 banger check: PASS (hook scene, slow push-in, candle + monitor glow, chorus escalation beat).

## Flags (not fails)
1. RASTER 1152x768 (3:2), not 1280x720 16:9 — the Era A still is 1920x1280 (3:2) and aspect followed the image despite "16:9 landscape" in the vehicle text. Assembly crops to 16:9 (1152x648 → upscale). Same class as MV-6 S16 (1168x640, KEEP-WITH-FLAG).
2. Take sings 0.00–9.70 vs vehicle window 0.5–9.5s (starts 0.5s early, last word ends 0.20s past window end). Assembly trims/warps; ratio in band.
3. Eyes closed through much of the chorus — expressive singing, not a fail.
4. Sparks motif weak: background reads as abstract monitor glow, no distinct spark points. Candle + glow carry the look; note for S06 (first spark scene).

## VERDICT: KEEP-WITH-FLAG — hook test PASSES. The v2 look is PROVEN. S01–S05 firing proceeds in this run.
