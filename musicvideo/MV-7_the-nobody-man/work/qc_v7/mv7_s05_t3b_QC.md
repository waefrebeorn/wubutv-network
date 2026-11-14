# MV-7 S05 t3b — QC (v3b SPLIT take B, PC1.2 only, recovery volley 3, 2026-11-06 ~17:27 EST)

File: takes/media-generation-mv7v2-s05-v3b-pre-chorus-1-pc1-0-a936dfd3-e4bb-4fd0-a6c4-8565a72571e4.mp4
md5: 223844bc5b180bc9df91d14eadf22625 · 2,537,965 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s05_v3b_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp (md5 ca15fc5084ccfedf0e90910f56eac75d).
snapshot_id: 1d02049d-8cc6-4e8a-8ba1-0a4c6134cc9f:xy6lhg

## Audio / words (faster-whisper small, work/qc_v7/mv7_s05_t3b_words.json)
- 7 words, 1 segment: "Little by little, I learned the sound." 0.00–7.02s.
- Word list matches PC1.2 exactly, 7/7, once, in order. (The repeated "little" is the lyric itself.)
- Take line span 0.00–7.02s vs song slot 36.50–38.60s (2.10s) → line ratio 2.10/7.02 = 0.299 — CLEAR MISS (<0.60).
- Phrase math for assembly: "Little by little," take 0.00–3.38s vs song 1.00s → 3.38x speedup; "I learned the sound"
  take 5.28–7.02s (1.74s) vs song 1.10s → 1.58x speedup. The 1.90s mid-line pause (3.38–5.28s) is dead air between phrases.
  The first phrase at 3.38x is beyond any precedent (MV-5 v4 disclosed extreme 1.91x; warp-rescue cap 1.5x) — a 3.38x
  playback would read frantic, not sung. The brisk window (0.5–5.0s) did not move the pace: 7 words over 7.02s = 1.0s/word,
  far slower than the ~0.62s/word floor measured on the whole-slot pulls.
- RMS check: vocal 1.5–3.5s and 5.0–7.0s, quiet 0–1.5s lead-in and 7.0–10.0s tail (bins ~0.01) — trims cleanly.
- Repeat-defect scan: no word/line subsequence recurs after first delivery. PASS.
- Zero-word result? No — 7 words; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–5.0s)
- frames=240, mean_diff=1.091, min=0.820, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.445.
- PASS with margin (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s05_t3b_sheet.png)
- 0.5s: mouth closed-ish at lead-in, opening into "Little"; identity holds vs Era A still; tall candle right, monitor glow abstract.
- 2.5s: mouth wide open mid-"little" (the drawl); slow push-in running.
- 5.5s: mouth open mid-"learned"; eyes half-closed, singing expression.
- 7.0s+: held crooked grin, eyes closed — the quiet tail.
- No readable text anywhere (monitor rectangles abstract glow, papers illegible). No other people. No morphing.

## Gates
- G1 character consistency: PASS. G2 zero unwanted on-screen text: PASS. G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open during both phrases; single singer facing camera).
- G5 audio-sync placement: FAIL — line ratio 0.299 CLEAR MISS; first phrase needs a 3.38x speedup, beyond the warp-rescue
  cap (1.5x) and beyond the MV-5 v4 disclosed speedup extreme (1.91x). Complete words do not rescue a pace this far out.
- G6 banger check: PASS (pre-chorus ritual beat; candle + monitor glow carry the look).

## VERDICT: REJECT
- Reroll axis (next volley): PACING-COMPRESSION v4 — tighter brisk window 0.5–3.5s, "sings the line quickly, in one breath,
  no pause between phrases". This is the SECOND pull of the split vehicle (not a third reroll of the same vehicle), so one
  more pull is legitimate. If v4 also comes back over ~6s, PC1.2 goes STRUCTURAL (montage cover for the line, or assembly
  accepts the squeeze — assembly's call, disclosed).
- Its partner PC1.1 (t3a) is KEPT — see mv7_s05_t3a_QC.md. Raster flag carried: 1152x768 (3:2) — assembly crops to 16:9.
