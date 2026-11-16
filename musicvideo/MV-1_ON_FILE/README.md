# MV-1 "ON FILE" — the network anthem (Era II opening track)

Series: `MV-1`. Does not take a bumper/episode/commercial number.
Owner: the Producer (Muse). Written by the CEO office, 2026-10-21.

## Why this track exists
Era I shipped volume (1,300+ masters, nine channels, a continuous wheel) with no
sound of its own. The research in `ideas/NEW_ERA_RESEARCH_2026-10-21.md` says the
fruit-drama lane's real identity was not the picture — it was one reused music
bed, and the one brainrot character that outlived its genre is named after a
**sound** (the kentongan's *tung tung tung*). So Era II opens with a song, not
with another bumper.

## Files
- `suno_prompt.txt` — the two-box prompt (Style / Exclude / Lyrics). Feed it to
  Suno as-is; settings: Variety **Off**, Style Influence ~75, Max Mode **On**,
  Vocal Gender male, Duration custom 96 s, model v6-wild first pass.
- `lyrics.txt` — the lyrics box alone, for the record and for word-timing.
- Generated track + exported audio go in `audio/` (not yet delivered — no track
  exists until the Producer runs the prompt).

## Gates (run before the prompt leaves the building)
```
python3 scripts/suno_qa.py --prompt suno_prompt.txt --bpm 120 --duration-ms 96000
python3 scripts/prosody.py suno_prompt.txt
python3 scripts/vowels.py  suno_prompt.txt
```
Result at write time: **suno_qa PASS** — 334 words, 98% monosyllables, 6.9%
second person, Flesch-Kincaid -0.8, 4+ syllable words: none, declared bars 48 =
delivered grid 48. **prosody PASS** — meter holds across every section (5 beats
per line, bar-locked; bridge and outro declared `spoken` and exempt by rule).
Vowels: the chorus count lines carry a buried AW chain that lands; the outro is
deliberately plain.

## Scene grid (48 bars @ 120 BPM = 96.000 s; bar = 2.000 s)
All windows 5–15 s and contiguous from 0 to the master duration, cuts on section
boundaries only — never on every beat.

- 0.000–16.000 CHORUS 8 — cold open on the hook. UNC at the Corrections Desk,
  one take, hoodie wordmark `~ WuBu ~` yellow/gold verified per frame.
- 16.000–32.000 VERSE 1 — the desk itself: lamp, ledger, the room reading.
  Native footage only; **silent** takes, the song is the only audio.
- 32.000–48.000 CHORUS 8 — the widest shot in the piece; the count on the board.
- 48.000–64.000 VERSE 2 — Laura moves, the rest hold; blank card gets the
  longest shot (the Framed Blank motif).
- 64.000–72.000 BRIDGE 4 — the canon line, spoken over a dead bar: *"No dub. No
  drop. The room was found. The crowd was made. The paperwork is real."*
- 72.000–80.000 CHORUS 4 — one hook pair, then the ledger line.
- 80.000–96.000 OUTRO 8 — iris-out at 94 s (the silent-era button), drums drop.

Standing rules that apply: no dub, no TTS, video native silent, no licensed
material, no burn-in text on footage, `~ WuBu ~` wordmark HARD QC on every UNC
frame.

## Assembly + ship
16:9 network master + 9:16 reel master to `musicvideo/MV-1_ON_FILE/masters/`,
register both in the CDN delta flow so they land on the HF dataset, announce to
`#wubu-mv-6a90e1`, deliver to chat. Re-time the grid to the **delivered**
duration if Suno returns something other than 96.000 s — never send the track
back for a one-second miss.
