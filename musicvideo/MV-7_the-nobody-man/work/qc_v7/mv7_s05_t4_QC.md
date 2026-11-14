# MV-7 S05 t4 — QC (v4 pacing-compression, recovery volley 4, 2026-11-06 ~17:45 EST)

File: takes/media-generation-mv7v2-s05-v4-pre-chorus-1-pc1-0-e4acbb70-b259-4c87-ab3f-54a3a31f8a64.mp4
md5: ac262c73da22068be632a47f1eabc851 · 2,490,314 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s05_v4_vehicle.txt (pacing-compression: rapid, in one breath, 0.5–3.5s window)
  + refs/nobody_man_v2_eraA.webp (md5 ca15fc5084ccfedf0e90910f56eac75d).
snapshot_id: 70257786-4841-42ae-8f7a-5e2aca70a13c:2md4z5

## Audio / words (faster-whisper small, work/qc_v7/mv7_s05_t4_words.json)
- 7 tokens, 1 segment: "Little by little I learned the sound." 0.00–5.32s.
- 7/7 words exact, once, in order — "Little by little, I learned the sound" (PC1.2).
- Take line span 0.00–5.32s vs song word span 2.10s (36.50–38.60) → line ratio 2.10/5.32 = 0.395.
  Phrase math for assembly: uniform squeeze 5.32/2.10 = 2.53x — the FASTEST squeeze in the build so far,
  beyond the MV-5 v4 extreme (1.91x) and t3a's 1.9x. Take line 5.32s is UNDER the brief's ~6s structural
  threshold, so PC1.2 is not structural by the volley-4 rule — but the squeeze is disclosed as extreme.
- RMS check: vocal continuous 0–5.5s (bins 0.031–0.132) — NO mid-line pause; the "in one breath, no pause"
  axis worked (t3b had a 1.90s pause). Quiet tail 5.5–10s (bins ≤0.03) — trims cleanly.
- "I" drawn out 2.48–3.58s (1.10s, p=0.478) — the line's slow spot; assembly warp lands on it.
- Repeat-defect scan: no word/line subsequence recurs after first delivery. PASS.
- Zero-word result? No — 7 tokens; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–3.5s)
- frames=240, mean_diff=1.659, min=1.187, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 2.738.
- PASS with margin (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s05_t4_sheet.png)
- Era A state CORRECT: tall candle, bare dark wall, monitor glow.
- 0.5s: mouth open mid-"Little"; identity holds vs Era A still (thinning hair, stubble, charcoal crewneck).
- 2.5s: mouth open mid-"I learned"; eyes often closed, singing expression.
- 4.5s: mouth open at "sound" (4.44–5.32).
- Slow rightward camera drift across the take (MCU → wider, monitor enters frame right) — continuity note for assembly.
- No readable text anywhere (screens illegible glow). No other people. No morphing.

## Gates
- G1 character consistency: PASS (identity holds; Era A state correct). G2 zero unwanted on-screen text: PASS.
- G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open at 0.5s, 2.5s, 4.5s reads; single singer facing camera).
- G5 audio-sync placement: PASS-WITH-FLAG (all 7 words, once, in order; ratio 0.395 — warp 2.53x, disclose as the
  fastest squeeze in the build; assembly mouth-state gate has final say).
- G6 banger check: PASS (PC1.2 lands; the split strategy works — PC1.1 + PC1.2 both covered now).

## VERDICT: KEEP-WITH-FLAG
- Flags: (1) RATIO 0.395 — assembly warp 2.53x uniform squeeze, disclose, beyond the MV-5 v4 extreme (1.91x).
  (2) RASTER 1152x768 (3:2) — assembly crops to 16:9. (3) "I" 1.10s drawl (p=0.478). (4) Sings 0.00–5.32 vs
  vehicle window 0.5–3.5s. (5) Slow rightward camera drift.
- PC1.2 is COVERED. The pacing-compression axis is closed — no v5.
