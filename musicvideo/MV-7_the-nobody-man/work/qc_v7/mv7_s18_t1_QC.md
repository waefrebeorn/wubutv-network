# MV-7 S18 t1 — QC (v2 verbatim, Era B bridge montage, recovery volley 5, 2026-11-06 ~18:10 EST)

File: takes/media-generation-mv7v2-s18-bridge-montage-b1-b4-0-d8514bfa-9877-4564-9b2b-46582a9e311e.mp4
md5: 6bcdda44b63145084136ffcac40fcfb3 · 4,240,220 B
ffprobe: h264 1248x704, 24fps, 10.000s; aac audio. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s18_vehicle.txt verbatim (DETAIL MONTAGE, no singing window) +
refs/nobody_man_v2_eraB.webp (md5 12c2ea7d3d97477f942c1b6e0e499364).
snapshot_id: d03ae652-83ce-434a-a308-7781f21df282:gzd7tr

## Audio / words (faster-whisper small, work/qc_v7/mv7_s18_t1_words.json)
- 0 words, 0 segments — as vehicled: NO singing window, no face sings. Correct for a bridge montage plate.
- RMS bins ~0.04 throughout (quiet bed, no vocal energy). No split-half recheck needed — the full pass
  is empty AND the visuals confirm no face.

## Frame rule (native 24fps, whole clip 0.0–10.0s — montage plate, no vocal window)
- frames=240, mean_diff=11.351, min=0.146, longest near-dup run (<0.5) = 20 frames. Whole-clip mean_diff 11.351.
- PASS (FAIL would be run ≥24f or mean <0.5) — but note the 20f run: the candle-at-desk-edge hold in the
  tail sits near-still for ~0.83s. Under the gate, and a held shot is legitimate montage punctuation —
  flag it, don't fail it.

## Visual reads (2fps sheet, work/qc_v7/mv7_s18_t1_sheet.png + full-res frames mv7_s18_t1_frame20.png / frame55.png)
- Montage beats all land: ink-stained hands posting at a keyboard (0–2.5s) · hand pinning a blank receipt
  slip to the crowded cork strip (~2.5–5s) · monitor feed of abstract glowing rectangles / bar charts
  (~5–7.5s) · candle at the desk edge, held (~7.5–10s).
- NO face appears anywhere in the clip ✓ (as vehicled — "no face appears at all").
- Era B state CORRECT: half-burned candle at the desk edge, crowded cork strip, ink-stained hands
  (continuity anchor holds).
- G2 verified at FULL RES (tile scans are unreliable for text — v4 lesson): frame at 5.5s shows abstract
  glowing rectangles + bar charts + motion-blurred code-like streaks, NO readable words; frame at 2.0s
  shows receipt slips with faint handwritten scribbles, illegible/out of focus, NO readable words.
- Note: a dollar-bill prop sits on the cork strip in the pinning frames (right side) — generic set
  dressing, not a logo/character, not a fail.
- No other people. No morphing.

## Gates
- G1 character consistency: PASS (no face; hands + props match Era B continuity).
- G2 zero unwanted on-screen text: PASS (full-res verified — slips illegible, monitor abstract).
- G3 no licensed material: PASS.
- G4 performance window: N/A — montage plate, no singing window (flagged "not a mouth-sung slot").
- G5 audio-sync placement: N/A — montage plate; cuts land on the beat at assembly.
- G6 banger check: PASS (bridge contrast holds — the montage breaks the desk-lean run).

## VERDICT: KEEP-WITH-FLAG
- First bridge montage plate lands clean. Flag: 20f near-dup run in the candle tail hold (under the 24f
  gate — held shot, legitimate); monitor feed reads as abstract UI with illegible code-like streaks;
  dollar-bill prop on the cork strip (set dressing). NOT a mouth-sung slot — caption still keyed to song
  word times (B.1–B.4, 123.26–132.58s).
