# MV-7 S08 t1 — QC (v2, recovery volley 2, 2026-11-06 ~16:55 EST)

File: takes/media-generation-mv7v2-s08-chorus-1-c1-5-c1-7-s-0-f954d8e2-27f3-4924-a378-e19fdfdc8541.mp4
md5: b1a0b44ce3656029c78f186d7518f691 · 2,657,675 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s08_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp.
snapshot_id: 45b774d5-d19b-4c69-b80d-a32e31290c18:og5zds

## Audio / words (faster-whisper small, work/qc_v7/mv7_s08_t1_words.json)
- 10 words, 1 segment: "I got a thousand little sparks flicking in the dark" 0.00–7.28s.
- Vehicle asked three lines (15 words): "I got a thousand little sparks. Flicking in the dark. I'm The Nobody Man".
  Take delivers C1.5–C1.6 only — C1.7 "I'm The Nobody Man" (song 61.46–62.68) is MISSING entirely.
- RMS check (16kHz wav, 0.5s bins): 7.5–10.0s rms ≈ 0.005–0.016, max ≤ 0.06 — the tail is genuinely silent, not a Whisper miss.
  (Mid-take gap 4.0–5.5s rms ≈ 0.008–0.011: the take pauses between "sparks" and the resumed "flicking" — Whisper spans
  "flicking" 3.96–6.02 across the pause; the word is drawn out, not dropped.)
- Take line span 0.00–7.28s vs song slot C1.5–C1.7 56.18–63.72s (7.54s) → line ratio 7.54/7.28 = 1.036 — in band on the
  delivered words, but coverage fails: the hook phrase has no singing picture.
- Repeat-defect scan: no word/line subsequence recurs after first delivery. PASS.
- Zero-word result? No — 10 words; split-half recheck not needed.

## Frame rule (native 24fps, vocal window 0.5–9.5s)
- frames=240, mean_diff=1.606, min=0.648, longest near-dup run (<0.5) = 0 frames. Whole-clip mean_diff 1.625.
- PASS with margin (FAIL would be run ≥24f or mean <0.5).

## Visual reads (2fps sheet, work/qc_v7/mv7_s08_t1_sheet.png)
- 0.5s: mouth open mid-"I"; identity holds vs Era A still; tall candle right; MORE tiny screens lit behind him than Era A — the chorus escalation reads.
- 5.0s: mouth open mid-"flicking"; slow push-in visible.
- 8.0s: mouth in held crooked grin, eyes closed — the silent tail after the dropped hook line.
- No readable text anywhere (screens are abstract glowing rectangles, papers illegible). No other people. No morphing.

## Gates
- G1 character consistency: PASS. G2 zero unwanted on-screen text: PASS. G3 no licensed material: PASS.
- G4 performance window: PASS (mouth visibly moving/open through 0.5–7.28s; single singer facing camera).
- G5 audio-sync placement: FAIL — incomplete line (C1.7 hook phrase missing; 2.26s of song chorus uncovered).
- G6 banger check: PASS (chorus escalation beat — more screens lit; candle + glow carry the look).

## VERDICT: REJECT
- Reroll axis (next volley): COMPLETENESS — vehicle v2 names all three lines explicitly and ends on the hook
  ("sings three lines, finishing on the hook line 'I'm The Nobody Man' — all three lines, no line dropped").
  Same tail-drop pattern as S01 (model truncates the last line of a multi-line vehicle); the completeness wording is the
  one variable that changes. If the completeness pull also drops the hook, split the slot (C1.5–C1.6 take + C1.7 pickup).
- Raster flag carried: 1152x768 (3:2) — assembly crops to 16:9.
