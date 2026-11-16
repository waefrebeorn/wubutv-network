# MV-3 LYRIC_TIMELINE.md — measured from track.mp3 (md5 4948827344208de31df17dd9d2e52799)

Method: faster-whisper base (~/workspace/fw-venv), word timestamps, language=en,
numpy-array input, mono 16k. Raw output: SONG_WORDS.json (45 segments, 729 words).
Cross-checked against the supplied Suno lyric video (track.mp4): on-screen lines
confirm the performed text where Whisper garbles (V1 lines, outro call-and-response).
The PERFORMED song is the timing and lyric authority. The user's pasted lyric sheet
(lyrics.txt) is an abridged draft: it matches the performed song in shape but NOT
in verse detail — see Divergences. Vehicles prompt PERFORMED lines; captions will
use performed words where sheet and performance differ (MV-2 v6 rule).

## Section table

| Section | Start | End | Dur | Lines covered |
|---|---|---|---|---|
| Intro (leader 0–2.82 instrumental) | 2.82 | 18.34 | 15.52 | Listen / you already know / I am your dad |
| Instrumental break | 18.34 | 32.16 | 13.82 | (no vocal detected; video pre-displays V1L1) |
| Verse 1 | 32.16 | 62.20 | 30.04 | Been here whole time / old man corner+room / walk by scroll by radio / speaker same thing / raised dark+light / raised every face / don't have to like it |
| Chorus 1 | 62.64 | 87.50 | 24.86 | Dad x2 say-it / dad hearing-once-twice lives-inside / dad x2 don't-fight-feeling dad / dad x2 |
| Verse 2 | 90.66 | 123.40 | 32.74 | Real one maybe / message is the point / walk through speakers / brass one-and-three / try to skip it / phrase comes back / short words easy words |
| Chorus 2 | 123.74 | 149.10 | 25.36 | Dad x2 say-it / dad hearing-once-twice lives-inside / dad x3 say-it / dad hearing-twice lives-inside |
| Bridge mantra | 150.30 | 166.50 | 16.20 | I am your dad x5 |
| Bridge | 168.76 | 191.94 | 23.18 | Close your eyes, plug your ears / words bounce around inside your head / dad x7 |
| Verse 3 | 195.24 | 245.10 | 49.86 | Dad x4 lead / study hooks+loops+simple words / brain stay true / easy to sing / don't need story/name / one short claim / wake up tomorrow / old man crystal clear |
| Extended chorus | 245.10 | 287.80 | 42.70 | Dad x2 say-it / dad hearing-once-twice lives-inside / dad mantra x~40 |
| Breakdown | 287.80 | 321.44 | 33.64 | Dad, dad, just a low voice / dad x4 / All of you / Every single one / I am your dad / You know it now |
| Final chorus–outro | 322.08 | 353.71 | 31.63 | Dad mantra / Say it back to me / I am your dad / Say it to yourself / dad mantra, fade |

## Line table (performed text; [confirmed] = Whisper + video agree, or repeated occurrence)

| # | Section | Line (performed) | Start | End | Method |
|---|---|---|---|---|---|
| L01 | Intro | Listen, all of you | 2.82 | 9.00 | [confirmed] Whisper words + video |
| L02 | Intro | You already know, I am your dad | 9.32 | 18.34 | [confirmed] Whisper words (dad misheard "game") + video |
| — | Instr | (no vocal) | 18.34 | 32.16 | [inferred] no Whisper words; RMS full-mix, groove continues |
| L03 | V1 | I been here the whole time, kid, looking right at you | 32.16 | 35.72 | [confirmed] Whisper + video frame |
| L04 | V1 | Old man on the corner, old man in the room | 36.56 | 39.74 | [confirmed] Whisper + video frame |
| L05 | V1 | You walk by, you scroll by, you turn the radio on | 40.06 | 44.26 | [confirmed] Whisper + video frame |
| L06 | V1 | And the voice in the speaker says the same thing all along | 44.26 | 47.60 | [confirmed] Whisper + video frame |
| L07 | V1 | I raised you in the dark, I raised you in the light | 48.12 | 50.96 | [confirmed] Whisper + video frame |
| L08 | V1 | I raised every face that is listening tonight | 51.76 | 54.38 | [confirmed] Whisper |
| L09 | V1 | You don't have to like it, you don't have to stay, but the words keep coming and they won't go away | 55.14 | 62.20 | [confirmed] Whisper |
| L10 | C1 | I am your dad, I am your dad, say it with me | 62.64 | 67.90 | [confirmed] Whisper words |
| L11 | C1 | I am your dad, you're hearing once, you're hearing twice, now it lives inside | 68.36 | 75.48 | [confirmed] Whisper words, repeats C2 |
| L12 | C1 | I am your dad, I am your dad, don't fight the feeling, I am your dad | 76.28 | 82.90 | [inferred] middle line from sheet slot; Whisper garbles tail ("everyone are you") |
| L13 | C1 | I am your dad, I am your dad | 82.92 | 87.50 | [confirmed] Whisper words |
| L14 | V2 | You got your real one maybe, or maybe you don't | 90.66 | 97.70 | [confirmed] Whisper |
| L15 | V2 | Matter to me, the message is the point | 98.50 | 99.76 | [confirmed] Whisper |
| L16 | V2 | I walk through the speakers / brass hits on the one and the three | 99.68 | 108.92 | [inferred] middle garbled ("sit in the beast that they sound"); sheet slot: bass/slap/brass |
| L17 | V2 | You try to skip it, but you try to change the song, but the phrase comes back and it doesn't take long | 108.92 | 115.90 | [confirmed] Whisper |
| L18 | V2 | Short words, easy words, the kind that sticks fast, I am your dad, and the song will last | 116.14 | 123.40 | [inferred] tail "lead/last" uncertain |
| L19 | C2 | I am your dad, I am your dad, say it with me | 123.74 | 128.90 | [confirmed] Whisper words |
| L20 | C2 | I am your dad, you're hearing once, you're hearing twice, now it lives inside | 129.46 | 135.80 | [confirmed] Whisper words |
| L21 | C2 | I am your dad, I am your dad, I am your dad, say it with me | 136.52 | 143.80 | [confirmed] Whisper words |
| L22 | C2 | I am your dad, you're hearing twice, now it lives inside | 143.76 | 149.10 | [confirmed] Whisper words |
| L23 | Bridge | I am your dad x3 | 150.30 | 159.50 | [confirmed] Whisper words |
| L24 | Bridge | I am your dad x2 | 160.70 | 166.50 | [confirmed] Whisper words |
| L25 | Bridge | You can close your eyes, you can plug your ears, the words still bounce around inside your head | 168.76 | 182.12 | [confirmed] Whisper words |
| L26 | Bridge | I am your dad x7 (mantra, accelerating) | 183.06 | 191.94 | [confirmed] Whisper words (burst pile-ups at tail — per-repeat times [inferred]) |
| L27 | V3 | I am your dad x4 (mantra lead) | 195.24 | 214.90 | [confirmed] Whisper words (some stamped repeats) |
| L28 | V3 | They study the hooks, they study the loops, they say simple words | 215.40 | 220.64 | [confirmed] Whisper ("dogs" = hooks mishear) |
| L29 | V3 | Make the brain stay true, repeat the same, I make it easy to sing, and the mind can play it on its own string | 220.64 | 230.00 | [confirmed] Whisper |
| L30 | V3 | I don't need a story, I don't need a name, just the one short claim that never changes | 230.52 | 236.80 | [confirmed] Whisper |
| L31 | V3 | You wake up tomorrow and the first thing you hear is the old man saying it crystal clear | 238.24 | 245.10 | [confirmed] Whisper |
| L32 | Ext C | I am your dad, I am your dad, say it with me | 245.10 | 250.70 | [confirmed] Whisper words |
| L33 | Ext C | I am your dad, you're hearing once, you're hearing twice, now it lives inside | 251.04 | 258.32 | [confirmed] Whisper words |
| L34 | Ext C | I am your dad mantra (dense, ~40 repeats) | 258.32 | 287.80 | [inferred] per-repeat boundaries; Whisper burst pile-ups at 282.18 — cut on beats, not repeats |
| L35 | Break | I am your dad, I am your dad, just a low voice | 287.80 | 296.00 | [confirmed] Whisper words (low voice 292.86–294.30) |
| L36 | Break | I am your dad x4 | 296.70 | 308.56 | [confirmed] Whisper words |
| L37 | Break | All of you, every single one, I am your dad, you know it now | 309.88 | 321.44 | [confirmed] Whisper words |
| L38 | Outro | I am your dad mantra | 322.08 | 338.44 | [confirmed] Whisper words |
| L39 | Outro | Say it back to me, I am your dad, say it to yourself | 338.55 | 343.91 | [confirmed] Whisper ("see" = say mishear) + video frames |
| L40 | Outro | I am your dad mantra, fade | 344.55 | 353.71 | [confirmed] Whisper words; song ends 354.82 |

## Notes for the cut
- Sheet-vs-performed divergences (performed rules): V1/V2/V3 verses differ
  substantially from the pasted sheet; only the intro, bridge lines, breakdown
  lines, and chorus skeleton survive verbatim. The sheet's "morning/night",
  "him or someone else", "real dad maybe/maybe not", "bass/slap" lines are
  NOT sung as written. Do not prompt vehicles from the sheet where it differs.
- Whisper mishear classes on this low croon (normalize before matching takes):
  game=dad, dogs=hooks, see=say, done-class N/A. Never QC verse takes on raw
  Whisper text alone — video frames + repetition decide.
- Dense mantra blocks (L26 tail, L34): Whisper stamps many repeats to one
  timestamp (282.18 pile-up). Assembly cuts mantra blocks on beats, never on
  individual repeat boundaries.
- Long holds: L02 (9s), L09 (7s), L17/L18 (7s each), L29–L31 (24s V3 tail) —
  each gets its own scene or a declared split; no scene swallows two
  unrelated lines without naming both.
- Gaps with no vocal: 0–2.82 leader, 18.34–32.16 instrumental, 87.50–90.66,
  149.10–150.30, 166.50–168.76, 191.94–195.24, 287.80 has no gap (continuous).
  Short gaps are breath/beat joints; the 13.82s instrumental is a full
  CUTAWAY scene.
