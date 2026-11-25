# MV-34 LYRIC TIMELINE — "Jensen's Back"

Track: 60.416 s · **127.0 BPM** (period 0.472 s, phase 0.390 s; half-beat lattice
0.236 s) · 60 sheet lines · **25 performed lines · 112 ASR words**.
Word/line times: faster-whisper **large-v3-turbo** (mobiuslabsgmbh, int8,
**NO VAD**), `work/asr_turbo_novad.json`; line splits of merged ASR segments
were made at word level (see SONG_WORDS.json).
**Text authority: lyrics.txt** (the user's sheet). Performed words govern
captions where they differ from the sheet.
**Adjudication: Reson8 Rumble-2-Flash** (`work/asr_rumble.json`, no
timestamps — word-exact verification only). Rumble confirms the performed
structure end to end: intro hooks ×4, Verse 1, Pre-Chorus, Chorus, closing
echo — and nothing else.
**Timing note (ribbon law):** these are ASR-derived planning times. Assembly
re-measures every take by forced alignment of the take's own audio against
the sheet; the song side is re-anchored per line at assembly. ASR word
timestamps are never the assembly clock.
**Dual-ASR failure record:** `asr_dual.py` (VAD on) collapsed on this track —
both checkpoints (large-v3, distil-large-v3) returned ONLY the 3.12 s hook
segment (`work/asr_dual_out.json`). Same failure family as MV-33. The
no-VAD turbo pass above is the timeline of record.

## ⚠ STRUCTURE FINDING — the performance is shorter than the sheet

The Suno render performs **25 of the sheet's 60 lines**. Performed: a
four-hit hook intro (no sheet section), Verse 1, Pre-Chorus, Chorus, and a
closing echo. **NOT performed (40 lines): Verse 2 (8), Pre-Chorus 2 (4),
Chorus 2 (8), Breakdown (8), Final Chorus (10), Outro (2).** Both ASR
checkpoints agree; the energy arc agrees (the 35–50 s build and the 48 s
peak are the one performed Chorus, not a Final Chorus). The scene plan
(MV_PREPRO_MV-34.md) covers the performed structure only. The unperformed
sections stay on the sheet as text authority for any future extended cut;
they are not planned, not fired, not missed.

## Section map

| Section | Span | Lines | Energy read |
|---|---|---|---|
| Instrumental head | 0.00–3.14 | — | quietest 2 s at t=2 (−22.4 dB); the BLAM is visual |
| Intro hooks (performed, no sheet section) | 3.14–14.96 | 4 hits | "Jensen's back" + "He's back" ×3, spaced on the grid |
| Verse 1 | 14.96–30.58 | 8 | the ouster, told in order |
| Pre-Chorus | 30.58–38.48 | 4 | the turn: numbers jump, he walks back in |
| Lift | 38.48–40.28 | — | 1.80 s instrumental lift into the Chorus |
| Chorus | 40.28–56.40 | 8 | the peak (loudest 2 s at t=48, −17.4 dB) |
| Tail echo | 56.40–60.42 | 1 reprise | "He's the line" at 58.60–60.10, then ring-out |

## Per-line spans (word-level, sheet text)

### Intro hooks — performed, no sheet section
| # | Line (performed) | Start | End |
|---|---|---|---|
| H1 | Jensen's back | 3.14 | 4.10 |
| H2 | He's back | 5.78 | 6.98 |
| H3 | He's back | 7.68 | 8.86 |
| H4 | He's back | 11.26 | 12.44 |

### Verse 1
| # | Line | Start | End |
|---|---|---|---|
| L1 | He stepped out for a minute | 14.96 | 17.54 |
| L2 | Then the board said stay gone | 17.54 | 19.16 |
| L3 | Stock went down, people talked | 19.16 | 21.34 |
| L4 | Now the lights are back on | 21.34 | 23.22 |
| L5 | He said he was sorry | 23.22 | 25.12 |
| L6 | They checked with the top | 25.12 | 26.80 |
| L7 | Eleven days later | 26.80 | 28.92 |
| L8 | They said come back, don't stop | 28.92 | 30.58 |

### Pre-Chorus
| # | Line | Start | End |
|---|---|---|---|
| L1 | Numbers jumping, phones ringing | 30.58 | 32.68 |
| L2 | Everybody watching the screen | 32.68 | 34.34 |
| L3 | He walked back in | 34.34 | 35.92 |
| L4 | Like the whole thing was a dream | 35.92 | 38.48 |

### Chorus
| # | Line | Start | End | Note |
|---|---|---|---|---|
| L1 | Jensen's back, Jensen's back | 40.28 | 41.14 | Sheet doubles the hook; turbo stamps ONE hit. Rumble hears two — **unresolved**; forced alignment at assembly settles it |
| L2 | Stock goes up, don't look back | 41.14 | 43.88 | Rumble mishears "on the back"; stamps + sheet agree |
| L3 | Jensen's back, hear that name | 43.88 | 45.94 | |
| L4 | Thirty percent, not the same | 46.02 | 47.68 | ASR renders "30 %"; sheet governs |
| L5 | Jensen's back, say it loud | 47.68 | 49.58 | |
| L6 | Board said yes, crowd got loud | 49.84 | 51.48 | Turbo "boy said yes", Rumble garbles — neither hears "Board" cleanly; sheet governs |
| L7 | Jensen's back, one more time | 51.48 | 53.68 | |
| L8 | He's the one, he's the line | 53.88 | 56.40 | |

### Tail
| # | Line (performed) | Start | End |
|---|---|---|---|
| E1 | He's the line (reprise of Chorus L8 tail) | 58.60 | 60.10 |

## Not performed — flagged per the sheet (40 lines)

Verse 2 (all 8: "Trump said bring him home" … "And the market didn't balk") ·
Pre-Chorus 2 (4) · Chorus 2 (8) · Breakdown (all 8: "Eleven days / Then he's
back" …) · Final Chorus (10) · Outro (2). The intake's story spine items that
belong to these sections (the board-call verse, the breakdown press chant,
the portrait-wall payoff of Verse 2's "put him on the wall") have **no
performed line to carry them**; the plan reassigns their visual energy to
performed beats (see MV_PREPRO_MV-34.md §2) and banks STACK-08 (portrait
wall) as an approved spare plate.
