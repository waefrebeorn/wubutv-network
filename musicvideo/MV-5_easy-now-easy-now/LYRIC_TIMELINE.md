# MV-5 LYRIC_TIMELINE.md — measured from track.mp3 (md5 0c1bcafa568547e2d4fa36e133ad3626)

Method: faster-whisper base (~/workspace/fw-venv), word timestamps,
language=en, mono 16k numpy input. Raw outputs: work/song_transcript_prompted.json
(110 segments, 506 words — full track WITH lyrics initial_prompt),
work/song_transcript_noprompt.json (88 segments, 556 words — full track,
no prompt), targeted re-decodes work/transcript_{tail,v1open,c1tail,c2tail}_{noprompt,prompted}.json.
Merged into SONG_WORDS.json (123 lines, 546 words) by work/merge_words_mv5.py.
Cross-checked against the Suno lyric video (track.mp4, 1 fps frames in
work/lyric_frames/) for section order and boundaries.

KEY FINDING 1 — THE SONG OPENS WITH A CHORUS INTRO, NOT VERSE 1. The
Suno overlay at 0s already shows the final-chorus closing block, and both
transcription passes confirm it: the song opens with the closing block
("Easy now, easy now / We ride, we ride / Easy now, easy now / Till the
morning comes") sung TWICE-ish as an intro (I01–I08, 1.66–18.64s), then a
wordless "ta-da" vocalise (I09, 18.64–22.00), and only then Verse 1
("Bare feet on the boardwalk", from ~22.00s). First word at 1.66s — there
IS a ~1.66s instrumental leader. Last word ends 205.58s; track 206.40s.

KEY FINDING 2 — THE PERFORMED SONG DIFFERS FROM THE SHEET. (a) Chorus
tails are NOT in the sheet: Chorus 1 ends with a repeated tag "I gotta go
there" alternating with "Just two small sparks" (76.80–85.20s); Chorus 2
ends with "I'm falling, I'm falling" alternating with "Just two small
sparks" (140.52–148.70s). Both passes + targeted re-decodes agree, with
different tag words per chorus — composed, not hallucination. (b) The
intro "Till the morning comes" line carries an echo tail ("comes, comes,
comes"). (c) Pre-Chorus 2's tail carries a held vocalise ("We fly" heard,
119.30–120.02s). (d) The bridge ends with a "No, no, no" ad-lib
(167.50–169.16s). (e) The final chorus closes with the closing block once
more (190.42–205.58s) after a 2.4s breath. Vehicles prompt PERFORMED
lines; captions will use performed words where sheet and performance differ.

Mishear classes normalized (both passes agree after normalization):
"Season house, now" / "Bein' an hour" = "Easy now, easy now"; "Just two
small spots" = "Just two small sparks"; "Keepin' loose, keepin' lost" =
"Keep it loose, keep it low"; "You should know it" = "We're good where we
are" / "Easy now"; "I'm all I owe" = "I'm falling"; "Sucks in the sand" =
"Socks in the sand"; "Kills with a balloon, cotton through the clouds" =
"Kids with a boombox, cutting through the crowd"; "You took my sleeveless"
= "You took my sleeve and spun me once". 21 words are even-split inside
their line window (flagged in SONG_WORDS.json `source`).

## Vocal ownership — measured from the audio, not the sheet (USER'S TOP PRIORITY)

Two voices, separated by fundamental frequency. Method: librosa pyin
(fmin 65, fmax 500; work/pyin_f0.npy, work/pyin_mv5.log) + aubio YIN
(work/pitch_aubio_prompted.json, work/pitch_lines.py) + per-word pyin
histograms. The male voice (THE VOICE = CAT on screen) sings a melody at
~97–160 Hz; the high voice (GIRL on screen) sings at ~200–330 Hz with a
tight, sustained cluster at ~250–320 Hz. The bass sits at ~65 Hz and both
estimators lock onto it in dense/fast passages — per-LINE medians are
therefore unreliable and the ownership calls below rest on per-WORD
histograms and the f0-track plot (work/pyin_track.png), which shows the
high band as discrete islands at 19–21s, 106–107s, 115–118s, 121–122s,
151–152s, 155–156s and 175s — not a continuous high melody.

CONFIRMED SPLITS (per-word pyin shows the f0 jumping between the bands
inside one line — a duet handoff, not a register change):
- L48 "So I didn't, not yet": "So" 147 Hz, "I" 147 Hz (CAT) → "did" 294 Hz,
  "it" 295 Hz, "not" 293 Hz (GIRL). The girl answers "didn't, not yet".
- L76 "If the day runs long": "If" 116 Hz, "the" 128 Hz (CAT) → "runs"
  312 Hz, "long" 261 Hz (GIRL).
- L96 "No need to run" (Final Chorus): "No" 263 Hz, "need" 251 Hz, "to"
  247 Hz (GIRL) → "run" 149 Hz (CAT).
- L56 "And my whole head replays" (Pre-Chorus 2): "whole" 311 Hz, "head"
  310 Hz (GIRL, 25/25 voiced frames) — while the identical line in
  Pre-Chorus 1 (L16) measures 131 Hz (CAT). The repeat is sung by the
  other voice.
- L80 "Heart in the breeze": "Heart" 261 Hz (GIRL).
- I09 "(ta-da vocalise)": 34/34 voiced frames at 307–322 Hz (GIRL).
- L57 "Easy now, easy now" (Chorus 2 open): 261–312 Hz (GIRL, 11/11
  voiced frames).

PATTERN (inferred from the confirmed splits + aubio per-segment readings,
which show "Easy now" lines at 261–335 Hz and response lines at ~100–175 Hz
in Chorus 1): the choruses ALTERNATE — the GIRL sings every "Easy now,
easy now" refrain line; the CAT sings every response line ("We ride, we
ride", "With you by my side", "No need to run", "We hold the sun", "Keep
it loose, keep it low", "Let it drift, let it go", "We're good where we
are", "Just two small sparks"). The same alternation governs the intro
(refrains CAT here — the intro measures low, 78–126 Hz — the GIRL only
takes the ta-da vocalise) and the final chorus, including the closing
block (L107 GIRL / L108 CAT / L109 GIRL / L110 CAT).

VERSE 2 IS GIRL-LED (inferred): Verse 1 measures 97–174 Hz throughout
(CAT). Verse 2 measures systematically higher — aubio per-segment 191–
312 Hz on most lines vs 97–174 Hz in Verse 1 — and the per-word splits
follow the same phrase-boundary pattern ("Vendor at the corner" CAT /
"Calling mango sweet" ~197 Hz GIRL; "And the tide tapping" CAT / "time
with our feet" 260 Hz GIRL). Verse 2 lines are therefore assigned GIRL
except the low phrases noted in the table; confidence [inferred] throughout
Verse 2. If assembly ear-checks disagree on a Verse 2 line, the line's
owner flips to CAT — the split points are the phrase boundaries, so a flip
is a one-line plan change, never a re-shoot of the scene.

Every vehicle names exactly ONE primary singer per the table below; the
other character's mouth stays explicitly closed (positive phrasing,
restated twice). Split lines (L40, L48, L76, L96) are split at the phrase
boundary into two scenes in the plan — never one prompt switching singers
mid-clip.

Owner counts (SONG_WORDS.json): CAT 354 words, GIRL 170 words, SPLIT 22 words.

## Section table

| Section | Start | End | Dur | Lines covered |
|---|---|---|---|---|
| Intro Chorus | 1.66 | 18.64 | 16.98 | I01–I08 |
| (scat vocalise) | 18.64 | 22.00 | 3.36 | I09 |
| Verse 1 | 22.00 | 46.86 | 24.86 | L01–L12 |
| (gap, breath) | 46.86 | 47.76 | 0.90 | — |
| Pre-Chorus 1 | 47.76 | 56.50 | 8.74 | L13–L16 |
| (gap, breath) | 56.50 | 57.52 | 1.02 | — |
| Chorus 1 | 57.52 | 76.80 | 19.28 | L17–L32 |
| Chorus 1 tail (tag) | 76.80 | 85.20 | 8.40 | L33–L36 |
| Verse 2 | 85.16 | 111.90 | 26.74 | L37–L52 |
| Pre-Chorus 2 | 111.90 | 118.28 | 6.38 | L53–L56 |
| (held vocalise + gap) | 118.28 | 121.30 | 3.02 | L56b |
| Chorus 2 | 121.30 | 140.52 | 19.22 | L57–L72 |
| Chorus 2 tail (tag) | 140.52 | 148.70 | 8.18 | L73a–L73d |
| Bridge | 148.70 | 167.50 | 18.80 | L74–L89 |
| (ad-lib + gap) | 167.50 | 169.16 | 1.66 | L90 |
| Final Chorus | 169.16 | 188.04 | 18.88 | L91–L106 |
| (gap, breath) | 188.04 | 190.42 | 2.38 | — |
| Final Chorus closing block | 190.42 | 205.58 | 15.16 | L107–L110 |
| (outro tail) | 205.58 | 206.40 | 0.82 | — |

## Line table (performed text; [confirmed] = Whisper words + video agree and/or per-word f0 split measured; [inferred] = boundary or owner from pattern/estimator agreement)

| # | Section | Line (performed) | Start | End | Owner | Method |
|---|---|---|---|---|---|---|
| I01 | Intro | Easy now, easy now | 1.66 | 3.82 | CAT | [inferred] no-prompt words + video frame 3s |
| I02 | Intro | We ride, we ride | 3.82 | 5.98 | CAT | [inferred] no-prompt words |
| I03 | Intro | Easy now, easy now | 5.98 | 8.01 | CAT | [inferred] no-prompt words |
| I04 | Intro | Till the morning comes | 8.01 | 10.04 | CAT | [inferred] no-prompt words, pyin 125.9 Hz |
| I05 | Intro | Easy now, easy now | 10.04 | 12.72 | CAT | [inferred] even-split words |
| I06 | Intro | We ride, we ride | 12.72 | 15.40 | CAT | [inferred] no-prompt words |
| I07 | Intro | Easy now, easy now | 15.40 | 17.02 | CAT | [inferred] no-prompt words + video frame 15s |
| I08 | Intro | Till the morning comes | 17.02 | 18.64 | CAT | [inferred] no-prompt + targeted v1open decode (echo tail) |
| I09 | Intro | (ta-da vocalise) | 18.64 | 22.00 | GIRL | [confirmed] pyin 316.4 Hz, 34/34 frames high |
| L01 | V1 | Bare feet on the boardwalk | 22.00 | 23.42 | CAT | [inferred] boundary; no-prompt words |
| L02 | V1 | Salt on my skin | 23.42 | 24.60 | CAT | [inferred] even-split words |
| L03 | V1 | You came in laughing | 24.60 | 26.76 | CAT | [inferred] no-prompt words + video frame 25s |
| L04 | V1 | Said, come on, let's begin | 27.76 | 29.60 | CAT | [inferred] no-prompt words |
| L05 | V1 | Blue shirt, red bicycle | 29.60 | 31.48 | CAT | [inferred] no-prompt words |
| L06 | V1 | Rolling past the pier | 31.48 | 33.62 | CAT | [confirmed] Whisper words |
| L07 | V1 | I was posted up right here | 33.62 | 36.14 | CAT | [confirmed] Whisper words + video frame 35s |
| L08 | V1 | Now you're pulling near | 36.14 | 38.48 | CAT | [confirmed] Whisper words |
| L09 | V1 | Backpack half-zipped | 38.48 | 40.44 | CAT | [confirmed] Whisper words |
| L10 | V1 | Keys in your hand | 40.44 | 42.82 | CAT | [confirmed] Whisper words |
| L11 | V1 | You nodded at the waves like | 42.82 | 44.58 | CAT | [confirmed] Whisper words |
| L12 | V1 | Yeah, they already understand | 44.58 | 46.86 | CAT | [confirmed] Whisper words |
| L13 | PC1 | Slow down, take your time | 47.76 | 49.60 | CAT | [inferred] boundary |
| L14 | PC1 | Let the hard week fade | 49.60 | 51.46 | CAT | [inferred] boundary |
| L15 | PC1 | One small look from you | 51.46 | 52.80 | CAT | [confirmed] Whisper words (even-split words) |
| L16 | PC1 | And my whole head replays | 52.80 | 56.50 | CAT | [confirmed] Whisper words, pyin 131.5 Hz |
| L17 | C1 | Easy now, easy now | 57.52 | 59.10 | GIRL | [inferred] refrain pattern; aubio 261.5 Hz |
| L18 | C1 | We ride, we ride | 59.10 | 60.22 | CAT | [inferred] response pattern; aubio 99.4 Hz |
| L19 | C1 | Easy now, easy now | 60.22 | 61.34 | GIRL | [inferred] refrain pattern |
| L20 | C1 | With you by my side | 61.34 | 62.52 | CAT | [inferred] response pattern; aubio 138.2 Hz |
| L21 | C1 | Easy now, easy now | 62.52 | 63.66 | GIRL | [inferred] refrain pattern (even-split words) |
| L22 | C1 | No need to run | 63.66 | 64.92 | CAT | [inferred] response pattern |
| L23 | C1 | Easy now, easy now | 64.92 | 65.96 | GIRL | [inferred] refrain pattern |
| L24 | C1 | We hold the sun | 65.96 | 67.06 | CAT | [inferred] response pattern |
| L25 | C1 | Easy now, easy now | 67.06 | 68.20 | GIRL | [inferred] refrain pattern |
| L26 | C1 | Keep it loose, keep it low | 68.20 | 69.40 | CAT | [inferred] response pattern |
| L27 | C1 | Easy now, easy now | 69.40 | 70.46 | GIRL | [inferred] refrain pattern; aubio 291.6 Hz |
| L28 | C1 | Let it drift, let it go | 70.46 | 71.66 | CAT | [inferred] response pattern |
| L29 | C1 | Easy now, easy now | 71.66 | 72.74 | GIRL | [inferred] refrain pattern; aubio 333.7 Hz |
| L30 | C1 | We're good where we are | 72.74 | 74.02 | CAT | [inferred] response pattern |
| L31 | C1 | Easy now, easy now | 74.02 | 75.04 | GIRL | [inferred] refrain pattern; aubio 334.7 Hz |
| L32 | C1 | Just two small sparks | 75.04 | 76.80 | CAT | [inferred] response pattern; aubio 92.1 Hz |
| L33 | C1 tail | I gotta go there | 76.80 | 78.76 | CAT | [inferred] targeted c1tail decode; pyin low |
| L34 | C1 tail | I gotta go there, just two small sparks | 78.76 | 81.76 | CAT | [inferred] targeted c1tail decode; two phrases, one row |
| L35 | C1 tail | I gotta go there | 81.76 | 83.14 | CAT | [inferred] targeted c1tail decode |
| L36 | C1 tail | Just two small sparks | 83.14 | 85.20 | CAT | [inferred] targeted c1tail decode; pyin 98.5 Hz |
| L37 | V2 | Vendor at the corner | 85.20 | 87.00 | CAT | [inferred] boundary; aubio low phrase |
| L38 | V2 | Calling mango sweet | 87.00 | 87.60 | GIRL | [inferred] per-word pyin ~195–202 Hz |
| L39 | V2 | Socks in the sand | 87.60 | 88.92 | GIRL | [inferred] aubio 191.0 Hz |
| L40 | V2 | And the tide tapping time with our feet | 88.92 | 93.00 | SPLIT | [inferred] "And the tide tapping" CAT (146.9 Hz) / "time with our feet" GIRL (260.1 Hz) |
| L41 | V2 | Your laugh hit the air | 93.80 | 95.12 | GIRL | [inferred] aubio 196–249 Hz |
| L42 | V2 | Like a hand drum roll | 95.80 | 96.84 | CAT | [inferred] aubio 130.7 Hz |
| L43 | V2 | I forgot the list, forgot the bills | 96.84 | 98.44 | GIRL | [inferred] aubio 259.4 Hz |
| L44 | V2 | Forgot what I was told | 98.44 | 102.40 | CAT | [inferred] aubio 111–155 Hz; long window incl. breath |
| L45 | V2 | Ice cup sweating | 102.40 | 103.80 | GIRL | [inferred] aubio 312.9 Hz |
| L46 | V2 | On the rail by the steps | 103.80 | 104.72 | GIRL | [inferred] aubio 263.6 Hz |
| L47 | V2 | You said, don't think too hard | 104.72 | 106.42 | CAT | [confirmed] Whisper words; pyin 130.4 Hz |
| L48 | V2 | So I didn't, not yet | 106.42 | 107.52 | SPLIT | [confirmed] "So I" 147 Hz CAT / "didn't, not yet" 293–295 Hz GIRL |
| L49 | V2 | Kids with a boombox | 107.52 | 108.72 | GIRL | [inferred] aubio 264.4 Hz |
| L50 | V2 | Cutting through the crowd | 108.72 | 109.74 | GIRL | [inferred] aubio 282.5 Hz |
| L51 | V2 | You took my sleeve and spun me once | 109.74 | 110.70 | GIRL | [inferred] aubio 271–308 Hz |
| L52 | V2 | Like none of it was loud | 110.70 | 111.90 | GIRL | [inferred] aubio 264.3 Hz |
| L53 | PC2 | Slow down, take your time | 111.90 | 113.78 | CAT | [inferred] boundary |
| L54 | PC2 | Let the hard week fade | 113.78 | 114.94 | CAT | [inferred] boundary |
| L55 | PC2 | One small look from you | 114.94 | 116.00 | CAT | [inferred] aubio 137.8 Hz |
| L56 | PC2 | And my whole head replays | 116.00 | 118.28 | GIRL | [confirmed] "whole head" 310–311 Hz, 25/25 frames |
| L56b | PC2 | (held vocalise) | 119.30 | 120.02 | GIRL | [inferred] pyin 329.9 Hz; likely "replays" tail |
| L57 | C2 | Easy now, easy now | 121.26 | 122.58 | GIRL | [confirmed] pyin 261–312 Hz, 11/11 frames |
| L58 | C2 | We ride, we ride | 122.58 | 124.00 | CAT | [inferred] response pattern |
| L59 | C2 | Easy now, easy now | 124.00 | 125.06 | GIRL | [inferred] refrain pattern |
| L60 | C2 | With you by my side | 125.06 | 126.30 | CAT | [inferred] response pattern |
| L61 | C2 | Easy now, easy now | 126.30 | 127.38 | GIRL | [inferred] refrain pattern |
| L62 | C2 | No need to run | 127.38 | 128.52 | CAT | [inferred] response pattern; pyin 79.6 Hz |
| L63 | C2 | Easy now, easy now | 128.52 | 129.66 | GIRL | [inferred] refrain pattern |
| L64 | C2 | We hold the sun | 129.66 | 130.78 | CAT | [inferred] response pattern |
| L65 | C2 | Easy now, easy now | 130.78 | 131.88 | GIRL | [inferred] refrain pattern |
| L66 | C2 | Keep it loose, keep it low | 131.88 | 133.08 | CAT | [inferred] response pattern |
| L67 | C2 | Easy now, easy now | 133.08 | 134.18 | GIRL | [inferred] refrain pattern |
| L68 | C2 | Let it drift, let it go | 134.18 | 135.36 | CAT | [inferred] response pattern |
| L69 | C2 | Easy now, easy now | 135.36 | 136.44 | GIRL | [inferred] refrain pattern |
| L70 | C2 | We're good where we are | 136.44 | 137.62 | CAT | [inferred] response pattern |
| L71 | C2 | Easy now, easy now | 137.62 | 138.82 | GIRL | [inferred] refrain pattern |
| L72 | C2 | Just two small sparks | 138.82 | 140.52 | CAT | [inferred] response pattern |
| L73a | C2 tail | I'm falling, I'm falling | 140.52 | 143.14 | CAT | [inferred] targeted c2tail decode; pyin low |
| L73b | C2 tail | Just two small sparks | 143.14 | 145.56 | CAT | [inferred] targeted c2tail decode |
| L73c | C2 tail | I'm falling | 145.56 | 146.62 | CAT | [inferred] targeted c2tail decode |
| L73d | C2 tail | Just two small sparks | 146.62 | 148.70 | CAT | [inferred] targeted c2tail decode |
| L74 | Bridge | If the rain comes down | 148.70 | 150.00 | CAT | [inferred] boundary; pyin 129.3 Hz |
| L75 | Bridge | We stay out in it | 150.00 | 151.30 | CAT | [inferred] boundary |
| L76 | Bridge | If the day runs long | 151.30 | 152.36 | SPLIT | [confirmed] "If the day" 116–128 Hz CAT / "runs long" 261–312 Hz GIRL |
| L77 | Bridge | We still move with it | 152.36 | 153.58 | CAT | [confirmed] pyin 149–157 Hz |
| L78 | Bridge | Hand in my hand | 153.58 | 154.42 | CAT | [inferred] boundary |
| L79 | Bridge | No speech, no show | 154.42 | 155.72 | CAT | [confirmed] pyin 155.5 Hz |
| L80 | Bridge | Heart in the breeze | 155.72 | 156.70 | GIRL | [confirmed] pyin 261.5 Hz |
| L81 | Bridge | And the bass move slow | 156.70 | 158.06 | CAT | [inferred] pyin bass-dominated; aubio reads high here — owner least certain in the bridge |
| L82 | Bridge | If the sky turns gray | 158.06 | 159.10 | CAT | [inferred] boundary |
| L83 | Bridge | We don't fold in | 159.10 | 160.24 | CAT | [inferred] boundary |
| L84 | Bridge | We lean right back | 160.24 | 161.36 | CAT | [inferred] boundary |
| L85 | Bridge | Let the whole thing spin | 161.36 | 162.46 | CAT | [inferred] boundary |
| L86 | Bridge | You and me, same pace | 162.46 | 163.58 | CAT | [inferred] boundary |
| L87 | Bridge | Same worn-in shoes | 163.58 | 164.90 | CAT | [inferred] boundary |
| L88 | Bridge | Nothing to prove | 164.90 | 165.88 | CAT | [inferred] boundary |
| L89 | Bridge | Nothing to lose | 165.88 | 167.50 | CAT | [confirmed] pyin 104.7 Hz |
| L90 | Bridge | (No, no, no ad-lib) | 167.50 | 169.16 | CAT | [inferred] both passes agree on the ad-lib; pyin 115.8 Hz |
| L91 | FC | Easy now, easy now | 169.16 | 170.18 | GIRL | [inferred] refrain pattern |
| L92 | FC | We ride, we ride | 170.18 | 171.44 | CAT | [inferred] response pattern |
| L93 | FC | Easy now, easy now | 171.44 | 172.58 | GIRL | [inferred] refrain pattern |
| L94 | FC | With you by my side | 172.58 | 173.62 | CAT | [inferred] response pattern |
| L95 | FC | Easy now, easy now | 173.62 | 174.92 | GIRL | [inferred] refrain pattern |
| L96 | FC | No need to run | 174.92 | 176.04 | SPLIT | [confirmed] "No need to" 247–263 Hz GIRL / "run" 149 Hz CAT |
| L97 | FC | Easy now, easy now | 176.04 | 177.20 | GIRL | [inferred] refrain pattern |
| L98 | FC | We hold the sun | 177.20 | 178.24 | CAT | [inferred] response pattern |
| L99 | FC | Easy now, easy now | 178.24 | 179.30 | GIRL | [inferred] refrain pattern |
| L100 | FC | Keep it loose, keep it low | 179.30 | 180.50 | CAT | [inferred] response pattern |
| L101 | FC | Easy now, easy now | 180.50 | 181.56 | GIRL | [inferred] refrain pattern |
| L102 | FC | Let it drift, let it go | 181.56 | 182.78 | CAT | [inferred] response pattern |
| L103 | FC | Easy now, easy now | 182.78 | 183.80 | GIRL | [inferred] refrain pattern |
| L104 | FC | We're good where we are | 183.80 | 185.02 | CAT | [inferred] response pattern |
| L105 | FC | Easy now, easy now | 185.02 | 186.46 | GIRL | [inferred] refrain pattern |
| L106 | FC | Just two small sparks | 186.46 | 188.04 | CAT | [inferred] response pattern |
| L107 | FC | Easy now, easy now | 190.42 | 194.72 | GIRL | [inferred] closing-block refrain pattern; targeted tail decode |
| L108 | FC | We ride, we ride | 194.72 | 197.58 | CAT | [inferred] closing-block response pattern |
| L109 | FC | Easy now, easy now | 197.58 | 203.42 | GIRL | [inferred] closing-block refrain pattern; long held line |
| L110 | FC | Till the morning comes | 203.42 | 205.58 | CAT | [inferred] targeted tail decode |

## Notes for the cut
- Short lines (~1.1s chorus lines) are pickups inside longer scenes, never
  stretched to a full scene. Chorus scenes pair one refrain + one response
  line (GIRL then CAT) — the plan splits them only where a single singer
  must own the whole take.
- Long holds: L109 "Easy now, easy now" spans 5.84s (held); L34/L73 tails
  are tag montages; L44 "Forgot what I was told" spans 3.96s incl. breath.
- Drift hazards: the chorus slots are fast (~1.1s/line) — takes must be
  QC'd for completeness (no dropped repeat) and the repeat check must
  catch ANY beat-word subsequence recurring after first delivery.
- The intro (I01–I08) repeats the closing block — assembly must use fresh
  takes per occurrence, never reuse.
