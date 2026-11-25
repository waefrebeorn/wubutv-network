# MV-4 LYRIC_TIMELINE.md — measured from track.mp3 (md5 d46af0ef2e5abfca97db16905d20fb7d)

Method: faster-whisper base (~/workspace/fw-venv), word timestamps,
language=en, numpy-array input, mono 16k. Raw outputs:
work/song_transcript.json (63 segments, 326 words — full track WITH
lyrics initial_prompt), work/song_transcript_0_65_noprompt.json (16
segments, 112 words), work/song_transcript_155_end_noprompt.json (14
segments, 101 words). Merged into SONG_WORDS.json (360 words) by
work/merge_words.py. Cross-checked against the supplied Suno lyric video
(track.mp4) frame by frame for line identity and boundaries.

KEY FINDING: the prompted full-track pass HALLUCINATED over Verse 1
(heard "Futurama's finished" repeats where the video shows Verse 1
lines) and missed the first ~11s of vocal entirely. The no-prompt
re-decode of 0–65s and 155–238.8s agrees with the video frames at every
sampled time (3s/5s/7s/9s/10s/11s/13s/15s/17s/19s/25s/35s/45s/55s/62s/
200s/210s/220s/230s). The PERFORMED song follows the sheet's structure
exactly — no verse is skipped, no line is reordered. Vehicles prompt
PERFORMED lines; captions will use performed words where sheet and
performance differ.

Mishear classes normalized (see merge_words.py): '03 -> "all three",
Hulu -> "Who knew", Matt -> "Max", style -> "sky", Futurama's finished
-> "Future rather Spanish" / "spinach" / "NoveFuturama's", Good news ->
"Cut news", binge -> "bring", Quote -> "Code", muscle memory ->
"what's the memory", credits -> "critics", dark -> "gut", on -> "home",
For -> "Or" (Chorus 2). "We'll" heard as "No" (Bridge L36). Whisper
dropped the "No" of C2 L29 ("No fresh episodes") — restored from the
sheet + the identical C1 line + the video frame at 45s.

The song starts singing at 0.00 — there is NO instrumental leader.
First word "They" at 0.00s. Last word ends 238.03s; track 238.80s.

## Section table

| Section | Start | End | Dur | Lines covered |
|---|---|---|---|---|
| Verse 1 | 0.00 | 30.54 | 30.54 | L01–L08 |
| (gap, instrumental breath) | 30.54 | 32.36 | 1.82 | — |
| Chorus 1 | 32.36 | 63.04 | 30.68 | L09–L16 |
| (gap) | 63.04 | 64.82 | 1.78 | — |
| Verse 2 | 64.82 | 95.40 | 30.58 | L17–L25 |
| Chorus 2 | 95.40 | 126.44 | 31.04 | L26–L33 |
| Bridge | 126.44 | 155.16 | 28.72 | L34–L41 |
| (gap) | 155.16 | 158.76 | 3.60 | — |
| Final Chorus (extended) | 158.76 | 204.72 | 45.96 | L42–L53 |
| Outro (soft, repeating) | 205.09 | 238.03 | 32.94 | L54–L57 |

## Line table (performed text; [confirmed] = Whisper words + video agree)

| # | Section | Line (performed) | Start | End | Method |
|---|---|---|---|---|---|
| L01 | V1 | They said it was over back in '03, | 0.00 | 4.00 | [confirmed] Whisper words (no-prompt) + video frame 3s |
| L02 | V1 | Then they said it again in twenty-thirteen. | 4.00 | 7.70 | [confirmed] Whisper words + video frame 5s |
| L03 | V1 | Hulu hit rewind and we all leaned in, | 7.70 | 11.70 | [confirmed] Whisper words + video frames 7s/9s/10s/11s |
| L04 | V1 | Fourteen seasons later, we're still on the screen. | 11.70 | 15.32 | [confirmed] Whisper words + video frames 13s/15s |
| L05 | V1 | "Final Ending: The Last Conclusion," | 16.00 | 18.66 | [confirmed] Whisper words + video frame 17s |
| L06 | V1 | That's the label on the last file. | 19.76 | 23.34 | [confirmed] Whisper words + video frame 19s |
| L07 | V1 | Matt said, "we're not done yet," | 23.34 | 26.44 | [confirmed] Whisper words + video frame 25s |
| L08 | V1 | But the streamer closed the door in style. | 26.44 | 30.54 | [confirmed] Whisper words + video frame 25s |
| L09 | C1 | Futurama's finished, Futurama's finished, | 32.36 | 35.42 | [confirmed] Whisper words (no-prompt) |
| L10 | C1 | For real this time, no more reruns in the dark. | 35.42 | 39.72 | [confirmed] Whisper words + video frame 35s |
| L11 | C1 | Futurama's finished, Futurama's finished, | 39.72 | 42.72 | [confirmed] Whisper words |
| L12 | C1 | No fresh episodes, that's the hard part. | 42.72 | 46.88 | [confirmed] Whisper words + video frame 45s |
| L13 | C1 | Good news, everyone — the ride is done, | 46.88 | 50.26 | [confirmed] Whisper words ("Cut news" normalized) |
| L14 | C1 | Good news, everyone — the ship won't run. | 50.26 | 54.20 | [confirmed] Whisper words ("Cut news" normalized) |
| L15 | C1 | Futurama's finished, Futurama's finished, | 54.20 | 57.94 | [confirmed] Whisper words + video frame 55s |
| L16 | C1 | For real this time, no more reruns in the dark. | 57.94 | 63.04 | [confirmed] Whisper words + video frame 62s |
| L17 | V2 | Three more specials lined up in twenty-seven, | 64.82 | 68.70 | [confirmed] Whisper words |
| L18 | V2 | Christmas first, then two more after. | 68.70 | 72.04 | [confirmed] Whisper words |
| L19 | V2 | But a whole new season? | 72.80 | 74.74 | [confirmed] Whisper words |
| L20 | V2 | Not on the board. | 74.74 | 76.28 | [confirmed] Whisper words |
| L21 | V2 | They sealed it up and walked out after. | 76.28 | 79.52 | [confirmed] Whisper words |
| L22 | V2 | We've seen this loop from Fox to cable, | 79.52 | 83.22 | [confirmed] Whisper words |
| L23 | V2 | Then streaming gave it one more round. | 83.22 | 86.96 | [confirmed] Whisper words |
| L24 | V2 | But this song's about the day they mean it, | 86.96 | 90.74 | [confirmed] Whisper words ("the songs" = "this song's") |
| L25 | V2 | When the last new line never comes down. | 90.74 | 95.40 | [confirmed] Whisper words |
| L26 | C2 | Futurama's finished, Futurama's finished, | 95.40 | 99.24 | [confirmed] Whisper words ("Spanish" normalized) |
| L27 | C2 | For real this time, no more reruns in the dark. | 99.24 | 103.36 | [confirmed] Whisper words ("Or" = "For") |
| L28 | C2 | Futurama's finished, Futurama's finished, | 103.36 | 106.38 | [confirmed] Whisper words ("Spanish" normalized) |
| L29 | C2 | No fresh episodes, that's the hard part. | 106.62 | 110.34 | [inferred] "No" dropped by Whisper; sheet + identical C1 line + video |
| L30 | C2 | Good news, everyone — the ride is done, | 110.34 | 113.88 | [confirmed] Whisper words |
| L31 | C2 | Good news, everyone — the ship won't run. | 113.88 | 117.96 | [confirmed] Whisper words |
| L32 | C2 | Futurama's finished, Futurama's finished, | 117.96 | 121.64 | [confirmed] Whisper words ("Spanish" normalized) |
| L33 | C2 | For real this time, no more reruns in the dark. | 121.64 | 126.44 | [confirmed] Whisper words ("Or" = "For") |
| L34 | Bridge | They always joke before the ending, | 126.44 | 130.18 | [confirmed] Whisper words |
| L35 | Bridge | Like they can talk the credits back. | 130.46 | 133.82 | [confirmed] Whisper words ("critics" = "credits") |
| L36 | Bridge | "We'll rise again," he keeps on saying, | 133.82 | 137.52 | [confirmed] Whisper words ("No" = "We'll") + sheet |
| L37 | Bridge | But the paperwork says otherwise. | 137.52 | 140.56 | [confirmed] Whisper words |
| L38 | Bridge | You can binge the old ones on your couch, | 140.56 | 144.64 | [confirmed] Whisper words ("bring" = "binge") |
| L39 | Bridge | Quote every line like muscle memory, | 144.64 | 147.86 | [confirmed] Whisper words ("Code"/"what's the memory" normalized) |
| L40 | Bridge | But the new ones stopped at the doorstep, | 148.40 | 151.96 | [confirmed] Whisper words |
| L41 | Bridge | And the hallway stays empty. | 151.96 | 155.16 | [confirmed] Whisper words |
| L42 | FC | Futurama's finished, Futurama's finished, | 158.76 | 162.64 | [confirmed] Whisper words ("spinach" normalized) |
| L43 | FC | For real this time, no more reruns in the dark. | 162.64 | 166.54 | [confirmed] Whisper words ("gut" = "dark") |
| L44 | FC | Futurama's finished, Futurama's finished, | 166.54 | 169.72 | [confirmed] Whisper words ("spinach" normalized) |
| L45 | FC | No fresh episodes, that's the hard part. | 169.72 | 173.90 | [confirmed] Whisper words (singular "episode" heard; plural per sheet/C1/C2) |
| L46 | FC | Good news, everyone (good news, everyone), | 173.90 | 177.12 | [confirmed] Whisper words |
| L47 | FC | The ride is done (the ride is done), | 177.12 | 181.24 | [confirmed] Whisper words |
| L48 | FC | Good news, everyone (good news, everyone), | 181.24 | 184.52 | [confirmed] Whisper words |
| L49 | FC | No more coming on. | 184.52 | 187.46 | [confirmed] Whisper words ("home" = "on") |
| L50 | FC | Futurama's finished… | 188.24 | 190.22 | [confirmed] Whisper words ("spinach" normalized) |
| L51 | FC | Futurama's finished… | 190.40 | 194.06 | [confirmed] Whisper words ("spinach" normalized) |
| L52 | FC | For real this time… | 194.06 | 198.38 | [confirmed] Whisper words |
| L53 | FC | No more coming on. | 198.38 | 204.72 | [confirmed] Whisper words ("home" = "on") |
| L54 | Outro | No more coming on… | 205.09 | 210.75 | [confirmed] Whisper words ("home" = "on") |
| L55 | Outro | Good news, everyone. | 211.75 | 216.73 | [confirmed] Whisper words |
| L56 | Outro | For real this time. | 217.75 | 220.77 | [confirmed] Whisper words |
| L57 | Outro | Good news, everyone. / For real this time. (repeat, soft) | 220.77 | 238.03 | [inferred] video frames at 220s/230s show the pair; Whisper hears one long held line ("real" 222.81–233.63) |

## Notes for the cut
- No instrumental leader: first word at 0.00s. Scene 1 must hook in the
  first 0.5–3s with NOVA already addressing camera.
- Three inter-section gaps (30.54–32.36, 63.04–64.82, 155.16–158.76) are
  instrumental breaths — fold each into the FOLLOWING scene's window as
  lead-in (the paper-ship fold, the dance reset, the final-chorus
  escalation), never as a dead scene.
- Short lines (~2–3s: L19, L20, L21) are pickups inside longer scenes,
  never stretched to a full scene. L19+L20+L21 are one scene (S10).
- Long holds get an explicit coverage decision: L52 "For real this
  time…" (4.32s, slow) + L53 "No more coming on." (6.34s, slow) are
  separate scenes with a held pose + ship-rise cover; L57 (17.26s soft
  outro repeat) is a two-take wide shot with a hard cut on the beat at
  ~229s.
- Chorus lines repeat identically across C1/C2/FC — EVERY occurrence
  gets its OWN take at its OWN position. Reuse is retired as vocal
  coverage.
- Drift hazard: the prompted full-track Whisper pass is UNRELIABLE for
  this track (Verse 1 hallucination, missed opening, degenerate
  zero-duration repeats in the choruses). Any future re-measurement
  must use the no-prompt passes + video frames, never the prompted
  pass alone.
