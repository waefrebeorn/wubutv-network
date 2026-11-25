# MV-7 S02 t1 — QC (v2, recovery run 4, 2026-11-06 ~16:35 EST)

File: takes/media-generation-mv7-s02-t1-0-52866472-cc1e-4357-84d2-4210422550d4.mp4
md5: 56838020652558bbd07c3d3ec6539e92 · 2,264,844 B
ffprobe: h264 1152x768, 24fps, 10.000s; aac. Duration asked 10s → returned 10.000s EXACT.
Vehicle: redesign_v2/vehicles/mv7v2_s02_vehicle.txt verbatim + refs/nobody_man_v2_eraA.webp.
snapshot_id: 33749679-e946-4e30-9cb8-83d0bf8e2fce:2z8zfw

## Audio / words (faster-whisper small, work/qc_v7/mv7_s02_t1_words.json)
- 8 words, 1 segment: "I'm the nobody man. I'm the nobody man." 0.00–7.14s (onsets 0.00 / 4.28).
- Vehicle lyric x2 delivered exactly once, in order, no repeats.
- Song side: S02 window (9.92–18.74s) performed = "I'm the nobody man" (9.5–11.56 abs) + "I'm nobody man" (14.2–16.48 abs)
  per split-half recheck (work/qc_v7/song_intro_b.json). Take's 2nd chant carries one extra "the" (~0.12s syllable) vs the performed elision — micro-mismatch, disclosed.
- Take line span 0.00–7.14s vs song slot 8.82s → line ratio 8.82/7.14 = 1.235 — IN the 0.80–1.25 band.
- Repeat-defect scan: PASS. Zero-word? No.

## Frame rule (native 24fps, vocal 0.5–9.5s)
- frames=240, mean_diff=1.180, min=0.361, longest near-dup run = 2 frames. PASS (FAIL would be run >=24f or mean <0.5).

## Visual reads (2fps sheet)
- 5.0s: mouth slightly open mid-chant, identity holds, tall candle, blank phone, keyboard. Eyes half-open, settling as directed.
- G1 PASS, G2 PASS (no readable text), G3 PASS, G4 PASS (mouth moving in window), G6 PASS.

## Flags
1. RASTER 1152x768 (3:2) — assembly crops to 16:9.
2. 2nd chant extra "the" vs performed "I'm nobody man" (micro, ~0.12s).
3. Silent tail 7.14–10.00s trims at assembly (excess past the 8.82s slot).

## VERDICT: KEEP-WITH-FLAG
