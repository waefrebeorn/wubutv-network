# MV-22 "I Love Spaghetti" — CUTLIST

Track 174.400s · 122.5 BPM (measured) · 63 lyric lines · master 4186 frames @24fps
Rounding: total frames = round(174.400 × 24) = 4186 → video stream 174.417s; the
+0.017s sits in the wordless outro tail. Windows tile 0.00→174.40 contiguously
(cumulative round(t×24) per scene). Line spans per LYRIC_TIMELINE.md (sheet
text = authority, ASR = timing). Warp = phrase-level: setpts=k on the take's
measured ASR sung span, then fps=24 resample (see GATE_LOG defect note).
The song has two wordless spans by design: 5.44–14.72 (intro→verse bridge,
covered by S01 tail + S02) and 107.86–124.24 (post-breakdown instrumental,
covered by S18 + S19) — both ship as planned wordless event covers.

| Scene | Window (s) | Take | Lines | Event | Assembly |
|---|---|---|---|---|---|
| S01 | 0.00–8.10 | t2 | L01 | The Lid Lift | head cover N k=1.470 (steam/stride, wordless 0–3.38) + W k=0.613 + tail N (wordless) |
| S02 | 8.10–14.72 | t1 | — (instrumental) | The Pasta Machine | N, take 0.30–6.92 (wordless cover) |
| S03 | 14.72–19.72 | t1 | L02–L03 | The First Plate | W k=1.208 (first delivery only) |
| S04 | 19.72–25.44 | t1 | L04–L06 | The Sauce Ladle | W k=0.640 |
| S05 | 25.44–31.24 | t1 | L07–L09 | The Steam Blessing | W k=0.836 (first delivery) |
| S06 | 31.24–41.68 | t1 | L10–L13 | The Forkable Demo (TWIRL #1) | W k=0.949 + wordless tail N k=2.0 over gap 39.88–41.68 |
| S07 | 41.68–47.02 | t1 | L14–L16 | The Standing Ovation | W k=0.824 |
| S08 | 47.02–51.76 | t1 | L17–L19 | Forks & Spoons Up | W k=0.765 |
| S09 | 51.76–57.32 | t1 | L20–L21 | The Meatball Catch | W k=1.080 + tail N |
| S10 | 57.32–61.16 | t2 | L22–L23 | The Fresh Batch | W k=0.513 (extreme — disclosed in GATE_LOG) |
| S11 | 61.16–67.40 | t1 | L24–L26 | The Gentle Portion | W k=0.841, take_start 0.88 |
| S12 | 67.40–73.62 | t1 | L27–L29 | The Side Parade | W k=0.686 + tail N |
| S13 | 73.62–83.66 | t1 | L30–L33 | The Service Twirl (TWIRL #2) | W k=0.928 + tail N k=1.607 |
| S14 | 83.66–89.10 | t1 | L34–L36 | The Encore Bow | W k=0.932, take_start 0.42 |
| S15 | 89.10–93.78 | t1 | L37–L39 | The Pasta Pull | W k=0.672 |
| S16 | 93.78–99.96 | t1 | L40–L41 | The Final Garnish | W k=0.963 + tail N |
| S17 | 99.96–107.86 | t1 | L42–L48 | The Chant Relay | 7 N sub-cuts on chant onsets (take starts 0.20/2.00/3.02/5.00/6.00/7.00/8.60) |
| S18 | 107.86–116.00 | t1 | — (instrumental) | The Long Strand | N, take_start 0.40 (wordless cover) |
| S19 | 116.00–124.24 | t1 | — (instrumental) | The Candle Pass | N, take_start 0.30 (wordless cover) |
| S20 | 124.24–128.46 | t1 | L49–L50 | The Full House | W k=0.735 |
| S21 | 128.46–135.74 | t1 | L51–L53 | The Double Plate | W k=0.801 + tail N |
| S22 | 135.74–142.96 | t1 | L54–L55 | The Meatball Crown | W k=1.157 |
| S23 | 142.96–151.44 | t1 | L56–L59 | The Great Twirl (TWIRL #3) | head N (take 0.98–1.42 → 142.96–143.40) + W k=0.995 |
| S24 | 151.44–162.54 | t1 | L60–L61 | The Candlelight Verse | W k=0.849 + wordless tail N k=1.768 (157.52–162.54) |
| S25 | 162.54–174.40 | t1 | L62–L63 | The Last Lid (bookend) | W k=1.351 + tail N |

Subtitles: 63 cues, work/swing/lyrics.srt (L24 span inferred 61.16–63.46 —
sheet-verified line ASR could not hear; L52/L53 share 129.24–134.50, split at
131.87). Rejected takes kept on disk: S01 t1, S04 t2, S10 t1 (see TAKE_HISTORY).
Generation spend: 28/40. Refusals: 0. 429s: 0.
