# MV-33 LYRIC TIMELINE — "Glue Your Shit Smooth On, It Is Not Over"

Track: 197.611 s · **115.0 BPM** (period 0.522 s, phase 0.270 s; beat grid in
`work/swing/beat_grid.json`) · 65 sheet lines · 323 ASR words.
Word/line times: faster-whisper **large-v3-turbo**, house lyrics config
(int8, cpu_threads=2, **NO VAD**), `work/asr_turbo_mv33.json`; line splits of
merged ASR segments were made at word level (see SONG_WORDS.json notes).
**Text authority: lyrics.txt** (the user's sheet). Performed words govern
captions where they differ from the sheet.
**Timing note (ribbon law):** these are ASR-derived planning times. Assembly
re-measures every take by forced alignment of the take's own audio against
the sheet; the song side is re-anchored per line at assembly. ASR word
timestamps are never the assembly clock.
**Dual-ASR failure record:** `asr_dual.py` (VAD on) collapsed on this track —
large-v3 hallucinated "Subtitles by the Amara.org community" across
0–32.2 s and distil-large-v3 returned fragments only (kept at
`work/asr_dual_mv33.json`). The no-VAD turbo pass above is the timeline of
record; its avg_logprob is healthy throughout (−0.15…−0.45).

## Section map

| Section | Span | Lines | Energy read |
|---|---|---|---|
| Instrumental intro | 0.00–12.64 | — | harpsichord allemande alone; the BLAM is visual |
| Intro | 12.64–27.20 | 3 | dips at 15–20 s (the "Pray" hush) |
| Verse 1 | 30.08–47.92 | 8 | the court verdict |
| Call 1 | 47.92–52.66 | 2 | + 2.84 s lift into Chorus 1 |
| Chorus 1 | 55.50–76.38 | 10 | first plateau |
| Verse 2 | 79.86–102.46 | 9 | the canteen; quietest sung stretch |
| Call 2 | 102.46–107.06 | 2 | + 2.76 s lift |
| Chorus 2 | 109.82–130.70 | 10 | high |
| Breakdown | 130.70–146.68 | 8 | texture break, not a volume drop |
| Instrumental bridge | 146.68–155.18 | — | harpsichord alone, 8.50 s |
| Final Chorus | 155.18–176.30 | 10 | **peak** (loudest 2 s of the track at t≈166) |
| Outro | 176.30–187.58 | 3 | dip at 180–185, recovery under the last line |
| Instrumental tail | 187.58–197.61 | — | harpsichord decay + vinyl crackle, 10.03 s |

## Line table (start–end in seconds; tag per timeline law)

| # | Section | Line (sheet) | Start | End | Tag |
|---|---|---|---|---|---|
| 1 | Intro | The coal mines are calling, good sir | 12.64 | 16.28 | confirmed |
| 2 | Intro | It is not over | 17.68 | 20.58 | confirmed |
| 3 | Intro | Pray, glue your shit smooth on | 21.70 | 27.20 | confirmed |
| 4 | Verse 1 | They declared the matter finished | 30.08 | 32.50 | confirmed |
| 5 | Verse 1 | They bid me pack and depart | 32.50 | 34.24 | confirmed |
| 6 | Verse 1 | I pressed the tube to the forehead | 34.24 | 36.58 | confirmed |
| 7 | Verse 1 | And glued that shit smooth on | 36.58 | 39.08 | confirmed |
| 8 | Verse 1 | Nigga, it is not over | 39.08 | 40.92 | confirmed |
| 9 | Verse 1 | Nigga, it is not over | 40.92 | 42.76 | confirmed |
| 10 | Verse 1 | Kindly place your bootyhole in the coal | 42.76 | 45.30 | confirmed |
| 11 | Verse 1 | This coal shall not mine itself | 45.30 | 47.92 | confirmed |
| 12 | Call 1 | The coal mines are calling | 47.92 | 50.20 | confirmed |
| 13 | Call 1 | It is not over | 50.20 | 52.66 | confirmed |
| 14 | Chorus 1 | Glue your shit smooth on | 55.50 | 57.80 | confirmed — HERO |
| 15 | Chorus 1 | Glue your shit smooth on | 57.80 | 59.70 | confirmed |
| 16 | Chorus 1 | Apply it directly to the forehead | 59.70 | 61.70 | confirmed — HERO |
| 17 | Chorus 1 | Smooth on, smooth on | 61.70 | 63.78 | confirmed |
| 18 | Chorus 1 | Blow your shit shmoove off | 63.78 | 65.82 | confirmed |
| 19 | Chorus 1 | Then glue that shit back on | 65.82 | 67.90 | confirmed |
| 20 | Chorus 1 | Nigga, it is not over | 67.90 | 70.08 | confirmed |
| 21 | Chorus 1 | Nigga, it is not over | 70.08 | 72.04 | confirmed (performed weakly) |
| 22 | Chorus 1 | Get your bootyhole in the coal | 72.04 | 74.18 | confirmed |
| 23 | Chorus 1 | It is not over | 74.18 | 76.38 | confirmed |
| 24 | Verse 2 | Fries in the bag, as before | 79.86 | 82.38 | confirmed |
| 25 | Verse 2 | The same as every shift | 83.30 | 86.62 | confirmed |
| 26 | Verse 2 | They advised me to go home | 86.62 | 91.48 | confirmed |
| 27 | Verse 2 | I glued that shit smooth on | 91.48 | 95.24 | confirmed |
| 28 | Verse 2 | Nigga, it is not over | 95.24 | 96.64 | confirmed |
| 29 | Verse 2 | Nigga, it is not over | 96.64 | 98.16 | confirmed |
| 30 | Verse 2 | Spread them cheeks wide | 98.16 | 100.00 | confirmed |
| 31 | Verse 2 | Coal inside | 100.00 | 100.64 | confirmed |
| 32 | Verse 2 | It is not over | 100.64 | 102.46 | confirmed |
| 33 | Call 2 | The coal mines are calling | 102.46 | 104.76 | confirmed |
| 34 | Call 2 | It is not over | 104.76 | 107.06 | confirmed |
| 35 | Chorus 2 | Glue your shit smooth on | 109.82 | 111.88 | confirmed — HERO |
| 36 | Chorus 2 | Glue your shit smooth on | 111.88 | 114.00 | confirmed |
| 37 | Chorus 2 | Apply it directly to the forehead | 114.00 | 116.08 | confirmed — HERO |
| 38 | Chorus 2 | Smooth on, smooth on | 116.08 | 118.50 | confirmed |
| 39 | Chorus 2 | Blow your shit shmoove off | 118.56 | 120.40 | confirmed |
| 40 | Chorus 2 | Then glue that shit back on | 120.46 | 122.40 | confirmed |
| 41 | Chorus 2 | Nigga, it is not over | 122.46 | 124.60 | confirmed |
| 42 | Chorus 2 | Nigga, it is not over | 124.60 | 126.60 | confirmed |
| 43 | Chorus 2 | Get your bootyhole in the coal | 126.62 | 129.00 | confirmed |
| 44 | Chorus 2 | It is not over | 129.02 | 130.70 | confirmed |
| 45 | Breakdown | Smooth on | 130.70 | 131.80 | confirmed |
| 46 | Breakdown | Smooth on | 131.80 | 132.96 | confirmed |
| 47 | Breakdown | Glue your shit smooth on | 132.96 | 134.32 | confirmed — **performed repeat at 135.14–136.90** (extra pass not on sheet; captions follow performance) |
| 48 | Breakdown | It is not over | 137.12 | 138.58 | confirmed |
| 49 | Breakdown | Nigga, it is not over | 138.58 | 140.12 | **inferred** — ASR-silent window; FA at assembly resolves |
| 50 | Breakdown | Shmoove off | 140.12 | 141.60 | confirmed |
| 51 | Breakdown | Then smooth on | 141.60 | 143.30 | confirmed |
| 52 | Breakdown | It is not over | 143.30 | 146.68 | confirmed |
| 53 | Final Chorus | Glue your shit smooth on | 155.18 | 157.14 | confirmed — HERO |
| 54 | Final Chorus | Glue your shit smooth on | 157.14 | 159.28 | confirmed |
| 55 | Final Chorus | Apply it directly to the forehead | 159.28 | 161.52 | confirmed — HERO |
| 56 | Final Chorus | Smooth on, smooth on | 161.52 | 163.64 | confirmed |
| 57 | Final Chorus | Blow your shit shmoove off | 163.64 | 165.60 | **inferred** — ASR hears a hook repeat here; sheet governs line identity, FA decides performed text |
| 58 | Final Chorus | Then glue that shit back on | 165.60 | 167.64 | confirmed |
| 59 | Final Chorus | Nigga, it is not over | 167.64 | 169.84 | confirmed |
| 60 | Final Chorus | Nigga, it is not over | 169.84 | 171.94 | confirmed |
| 61 | Final Chorus | Get your bootyhole in the coal | 171.94 | 174.04 | confirmed |
| 62 | Final Chorus | It is not over | 174.04 | 176.30 | confirmed |
| 63 | Outro | The coal mines are calling | 176.30 | 179.18 | confirmed |
| 64 | Outro | It is not over | 179.18 | 181.62 | confirmed |
| 65 | Outro | Glue your shit smooth on | 181.62 | 187.58 | confirmed |

## Performance-vs-sheet notes (for captions + vehicles)
- ASR renders the sheet's "Nigga" with the hard-r spelling throughout —
  transcription artifact of the same performed word; the sheet governs.
- "bootyhole" is performed as two beats ("booty hole"); "coal" is ASR-heard
  as "cold" in all three booty lines — performed word is the sheet's.
- "shmoove" (sheet spelling, Blow lines) is performed as spelled; ASR hears
  "smooth off". Vehicle transliteration: hook "gloo your shit smoov on";
  blow line "bloh your shit shmoov off" (see prepro §Transliteration).
- Call 1 L1: ASR hears "called" once (47.92) — sheet's "calling" governs;
  the same line is heard correctly at Call 2 and Outro.
