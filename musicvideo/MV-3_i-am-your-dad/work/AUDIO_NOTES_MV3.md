# AUDIO BIBLE — MV-3 "I Am Your Dad (HE IS NOT YOUR DAD, RUN)"

**Song:** MV-3 "I Am Your Dad (HE IS NOT YOUR DAD, RUN)" — Suno track, 354.8s
**Source measured:** `track.mp3` (md5 `4948827344208de31df17dd9d2e52799`, never modified) via `work/gemini/song_16k.wav` (16 kHz mono, 5,677,056 samples, 354.816s exact)
**Written:** 2026-11-05 ~14:40 EST, by the audio-bible agent (parent order ~14:13 EST: "absorb audio, make the most verbose notes, revisit it multiple times, compile the music video needs — vibes, motifs, contexts")
**Companion files read:** `lyrics.txt` (sheet of record, verbatim from the user), `SONG_WORDS.json` (729 words as [word, start, end] triples + 45 segments), `MV3_TIMING_DIAGNOSTIC.md` (v1 take-drift findings), `CUTLIST_RECUT.md` / `recut_work/sync_proto/` (retime warps, cross-check data)
**Status note:** MV-3 has NO Gemini song audit yet — the app route (Stage D) is blocked on the endpoint fix, and the MV-3 song + take audit runs through that same route. Everything timed here at the word level comes from v1 Whisper (SONG_WORDS) plus the fresh independent Whisper base re-pass below. The retimed master (md5 `24af63b9c2e4b64a6f038efb3bd39e3b`) is untouched; nothing was re-delivered or overwritten.

## How to read this file — MEASURED vs INFERRED

Same conventions as `AUDIO_NOTES_MV5.md`: **[MEASURED]** = a number produced by a tool in this pass, method named. **[INFERRED]** = a judgement from measurements + lyrics. **[HEARSAY]** = carried over from v1/diagnostic work, not re-measured here. I cannot hear the audio — there is no listening channel. Where measurements are silent or ambiguous, this file says so.

## Methods used

Same toolkit as MV-5: custom numpy/scipy script (`/tmp/audio_bible.py` — per-second RMS/peak/ZCR, centroid per 0.5s, chroma per 1s, spectral-flux tempo by autocorrelation + beat-peak median, silence gaps at −45 dBFS, autocorrelation f0 per 32 ms frame). **librosa not installed** — hand-rolled. **faster-whisper base** (cached, `~/workspace/fw-venv`, offline, numpy-array input — file-path decode is broken in both installed faster-whisper copies, PyAV `metadata_errors` mismatch) as an independent re-pass. Tempo measured three ways; word times cross-checked two ways (v1 SONG_WORDS vs fresh base re-pass).

---

## PASS 1 — Structure / tempo / energy

### Tempo [MEASURED] — ~126 BPM with a half-time heart

| Method | Result |
|---|---|
| Spectral-flux autocorr, full song | **63.5 BPM**, conf 0.764 (top-5 all 61.5–63.5 — a flat peak at the *half* tempo) |
| Same, per third (0–118s / 118–236s / 236–355s) | **129.0 / 63.5 / 129.0 BPM** (conf 0.76 / 0.72 / 0.75) |
| Beat-peak median (693 onset peaks) | **125.0 BPM** |

**Reading:** the song's pulse is **~125–129 BPM**, but the *middle third* (118–236s — the long mantra stretch) reads as **63.5 BPM**: the onsets thin out to half-time there. The full-song autocorr locks onto the half-time because the middle third dominates the flux. **The song has two gears: ~127 BPM in the outer thirds, ~63 BPM feel in the middle.** Beat length at 127 BPM ≈ 0.47s; at half-time ≈ 0.95s. [INFERRED] This is the song's secret weapon and its staging trap: the middle third *feels* twice as slow as the ends even though nothing changes tempo — the beat simply halves. The picture must halve with it: longer holds, slower pushes, fewer cuts in 118–236s, then snap back to the faster cutting rhythm for the final pile-up. A video cut at the same rate throughout will feel frantic in the middle and sluggish at the ends.

### Energy arc [MEASURED] — a 13 dB climb with breaths between blocks

Per-10s mean RMS (dBFS, peak-normalised):

| Block | Mean RMS | Peak |
|---|---|---|
| 0–10s | −23.3 | −19.7 |
| 10–20s | −20.8 | −16.1 |
| 20–30s | −17.2 | −16.7 |
| 30–40s | −16.9 | −15.9 |
| 40–60s | −16.6 | −15.4 |
| 60–70s | −17.7 | −14.6 |
| 70–90s | −15.7 | −13.8 |
| 90–100s | −15.6 | −15.0 |
| 100–110s | −17.3 | −15.7 |
| 110–130s | −16.4 | −14.6 |
| 130–150s | −14.7 | −13.7 |
| 150–160s | −14.9 | −13.5 |
| 160–170s | −16.5 | −13.6 |
| 170–190s | −14.9 | −13.3 |
| 190–200s | −14.3 | −12.8 |
| 200–210s | −13.5 | −11.9 |
| 210–230s | −11.9 | −11.0 |
| 230–240s | −12.1 | −11.6 |
| 240–250s | −15.5 | −12.2 |
| 250–270s | −12.9 | −11.7 |
| 270–280s | −11.4 | −10.2 |
| 280–290s | −10.7 | −10.3 |
| 290–300s | −14.7 | −10.2 |
| 300–310s | −12.7 | −10.3 |
| 310–320s | −10.8 | −10.3 |
| 320–330s | −10.3 | −9.6 |
| 330–340s | −10.6 | −10.0 |
| 340–350s | −10.4 | −9.4 |
| 350–355s | −21.8 (fade-out tail) | −10.6 |

**Reading [INFERRED]:** unlike MV-5's smooth 6.6 dB swell, MV-3 climbs **~13 dB** from its intro floor (−23.3) to its outro ceiling (−10.3), and it climbs in *steps with breaths*: dips at 100–110s (−17.3), 160–170s (−16.5), 240–250s (−15.5) and 290–300s (−14.7) mark the joints between mantra blocks. The song is built like a staircase with landings. **MV implication:** the video's energy must climb the same staircase. Each dip is a staging reset — a breath, a new angle, a change of room or light — and each climb is a push toward the next landing. The loudest stretch is the outro chant (280–355s, −10.3 to −10.8 dB sustained): that is where the biggest, most populated, most saturated frames belong. The intro (0–10s, −23.3 dB) is the quietest block in either MV song: the camera can be at its closest and stillest there — the monster's face, the yellow ball smile, nothing else.

### Silence / breaths [MEASURED]

- **One silence gap ≥ 0.3s below −45 dBFS: 354.10–354.80s (0.70s) — the fade-out tail only.**
- **Inter-word gaps > 2s [MEASURED from SONG_WORDS]:** 13.82s after "game" (18.34 → 32.16s — the big instrumental breath after the intro), 2.26s after "dad" (166.50 → 168.76s), 3.30s after "dad" (191.94 → 195.24s), 2.16s after "dad" (270.10 → 272.26s), 2.42s after "dad" (289.00 → 291.42s), 2.40s after "voice" (294.30 → 296.70s), 2.22s after "you" (311.44 → 313.66s). Median inter-word gap is 0.0s — the words are otherwise continuous.
- **Reading [INFERRED]:** the 13.82s instrumental after the intro is the single most important piece of negative space in either song. It is the only place in MV-3 where the voice stops for more than 3 seconds. The picture must *do something* there — the monster arriving, the room, the first full look — because the audio has handed the scene to the picture for fourteen seconds. The 2–3s gaps inside the mantra blocks are the micro-breaths: each one is a cut point, a blink, a reframing beat.

### Brightness / timbre [MEASURED]

Spectral centroid per 10s: starts 2121 Hz (0–10s), rises to 2648 Hz (50–60s), peaks 2595 Hz (100–110s), dips to 1955–2046 Hz (290–320s — the breakdown, the darkest block in the song), recovers to ~2200–2290 Hz for the outro chant. Overall range per 0.5s frame: 521–5491 Hz.

**Reading [INFERRED]:** the song brightens through the first two minutes, then *darkens* for the breakdown (290–320s) before the outro. The breakdown is the only section that gets darker as it gets louder — a useful contradiction: loud + dark = menacing. **MV implication:** grade the breakdown (288–313s) darker and heavier than the choruses around it, even though the RMS is high. The intro is bright-ish but quiet — small and bright, like a single lamp. The outro is loud and mid-bright — the full room lit.

### Harmony sketch [MEASURED, WEAK]

Chroma per block: **A 0.10–0.13, E 0.10–0.12, B 0.09–0.11** lead everywhere — Intro (B 0.13, E 0.11, A 0.09), Verse 1 (A/E/B), Chorus 1 (E 0.11, A 0.10, B 0.09), Mantra long (A 0.12, E 0.11, F 0.10), Mantra pile (E 0.12, A 0.11, F 0.10), Outro chant (A 0.12, E 0.11, F 0.10). Same diffuse profile as MV-5 (max weight ~0.13), no section change.

**Reading [INFERRED, LOW CONFIDENCE]:** the A/E/B cluster is consistent with an **A-major / E-major family** (A–E–B is the I–V–II of A major), but the chroma is too diffuse to determine a key. What is solid: the harmony does not change by section. The song's variety is rhythmic (the half-time middle) and textual (the mantra), not harmonic. Same staging consequence as MV-5: the picture does the work the harmony doesn't.

---

## PASS 2 — Vocal character

### One voice, one register [MEASURED]

- **Single singer throughout** — the MONSTER MAN IN A SUIT with a BIG YELLOW BALL SMILEY HEAD (this track only; not THE VOICE, not UNC). No second voice is labelled anywhere in SONG_WORDS, the diagnostic, or the lyric sheet. The parenthetical "(I am your dad.)" echoes in the sheet are the *same* voice answering itself — [HEARSAY from the sheet] — not a second singer.
- **My crude autocorrelation f0 track [MEASURED, ROUGH]:** 5686/11084 frames voiced (51%), median 109.6 Hz, p10 63.1, p90 500.0 (cap — octave errors). Per-block medians: Intro 110 · Verse 1 110 · Chorus 1 116 · Chorus 2 124 · Verse-2 tail 87 · Mantra long 87 · Mantra pile 109 · Outro chant 110. The medians cluster at **~87–124 Hz** — a low male voice, roughly an octave below MV-5's GIRL and in the same band as MV-5's CAT (131 Hz aubio median). The 87 Hz readings in the mantra blocks are likely bass-lock (the same trap as MV-5: the mix bass sits ~65 Hz and the estimator slides down in dense passages) — treat 87 as a floor, not a pitch.
- **Gap:** there is no trusted per-line pyin/aubio track for MV-3 comparable to MV-5's `gemini_line_f0.json`. The v1 stage-1 f0 work exists in `recut_work/sync_proto/` (crosscheck files) but was not re-pooled here. **The MV-3 Gemini audit (Stage D) will supply per-line speaker/f0 data; until then, "one low voice, ~110 Hz" is the measured claim and anything finer is INFERRED.**
- **Eye line (hard rule, from the project):** "small solid black oval eyes, no white showing" — in every vehicle, verbatim. The voice is low and the face is a yellow ball with black oval eyes. The *contrast* between the cute face and the low, insistent voice is the character.

### Delivery rate [MEASURED from SONG_WORDS]

- Word duration: median 0.32s, p90 0.70s, max 6.32s (a held word — the intro's "you" at 9.32–12.56s runs 3.24s; "of" at 5.82–8.08s runs 2.26s — the intro *drawls*).
- **Words per 30s block:** 0–30s: 11 (the intro drawl + the 13.8s instrumental) · 30–60s: 80 · 60–90s: 49 · 90–120s: 73 · 120–150s: 62 · 150–180s: 36 · 180–210s: 42 · 210–240s: 66 · 240–270s: 63 · **270–300s: 171 (the densest 30s in either song — 5.7 words/second sustained)** · 300–330s: 39 · 330–355s: 37.
- **Reading [INFERRED]:** the song's word-rate curve is a *mountain with a cliff*: it climbs to the 270–300s pile-up (171 words — the mantra at full sprint), then falls off a cliff to 39 words in the next 30s (the breakdown: "All of you. Every single one. You know it now." — short lines, long gaps). The breakdown is the song *catching its breath after sprinting*. **MV implication:** the 270–300s pile-up is unfilmable as lip-sync at full speed — it is a montage block by necessity (and indeed S35 went structural after 3 failed attempts, S30 after two denied rerolls — the repeat-drop class). Stage it as a pile-up: fast cuts, accumulating faces, the phrase stacking. Then the breakdown (288–313s) is the payoff: slow, dark, one line at a time, each line given a full frame. The contrast between the sprint and the breakdown is the video's biggest dynamic swing — bigger than any loudness change.

---

## PASS 4 — Lyrics / motifs

### Word counts [MEASURED from SONG_WORDS, 729 words]

Top words: **i 106 · your 102 · am 97 · dad 97** · the 28 · you 21 · it 17 · and 8 · to 8 · you're 8 · hearing 7 · me 6 · don't 5 · words 5 · they 5 · say 5 · now 5 · inside 5.

**The phrase "I am your dad" occurs 96 times as a consecutive 4-gram — 384 of 729 words (53%) are the mantra.** The word "dad" appears 97 times (once outside the phrase). Unique words: 151 — the song has a *tiny* vocabulary. Compare MV-5: 176 unique words over 546, with the hook at 22%. MV-3 is more than twice as repetitive by share.

### The mantra and its variants [MEASURED + INFERRED]

- The mantra is the song. Everything else — the verses, the bridge, the breakdown — is scaffolding around 96 repetitions of four words.
- **The one variant that matters [MEASURED]:** the intro's last line is performed as **"I am your game"** (SONG_WORDS segment 1: "Listen, all of you, you already know, I am your game."), not "dad". The fresh Whisper re-pass hears "game" too (17.78–18.38s, low prob 0.111 but the same word). The sheet's intro says "I am your dad" — the *performed* word is "game". [INFERRED] The intro is a feint: the monster introduces himself as a *game* before he claims to be your dad. It is the song's first joke and its thesis: this is a game that becomes a claim. The video should play the feint — the monster as a gameshow host, a toy, a plaything — before the claim lands.
- **Other performed-vs-sheet notes [HEARSAY from the diagnostic + SONG_WORDS segments]:** "It lives inside" is heard by Whisper as "I live" (the "it" is swallowed); "everyone are you" is heard as "every one of you" (the sheet's ungrammatical line is smoothed by the ear); "study dogs" is heard as "started off" (the Verse 3 "They study the hooks and the loops" passage is fast and the words blur).
- **The echoes:** the sheet writes "(I am your dad.)" as a parenthetical echo after many mantra lines. [INFERRED] The echo is the monster answering himself — the same voice, doubled. Visually: the same face, twice in the frame (a mirror, a reflection, a second ball-head in the background), or the same line delivered once to camera and once in profile. The echo is not a second character; it is the claim *reverberating*.

### Motifs [INFERRED from lyrics]

1. **The claim as a spell.** "I am your dad" repeated 96 times is not a statement, it's an incantation — the song *wears the listener down* by repetition, exactly as the lyrics describe ("the words still bounce around inside your head", "now it lives inside", "don't fight the feeling"). The horror-comedy is that the claim works by *saying it*, not by proving it.
2. **The speaker as medium.** "There's a voice in the speaker" (V1) · "I walk through the speakers" (V2) · "you can close your eyes, you can plug your ears, the words still bounce around inside your head" (bridge). The monster is not a person in a room — he is a voice in a device. [INFERRED] The video's central image should be the *speaker*: radios, TVs, phones, the voice coming out of objects. The monster's body is almost incidental; his *medium* is the point.
3. **The corner / the room.** "There's an old man on the corner" · "Oh man, I'm the corner, oh man in the room" · "I was there in the morning / I was there at night" (V1). The monster is *located* — a corner, a room, a morning, a night. He is always already there.
4. **"Say it with me."** The song recruits the listener: "Say it with me. I am your dad." [INFERRED] The video should recruit the viewer the same way — the monster looking at camera, the claim offered as a sing-along. The final chorus is a call-and-response with the audience, not a performance for them.
5. **The breakdown as the truth.** "All of you. Every single one. You know it now." — after 96 repetitions, the song stops repeating and *states* it, slowly, in the dark. [INFERRED] The breakdown is the only part of the song that isn't a game. Stage it as the only part that isn't funny: still, dark, one face, no echo.

### Rhyme [MEASURED, light]

The song barely rhymes — it *repeats*. Line-final words are dominated by "dad" (97), "you" (21), "inside" (5), "now" (5). There is no rhyme scheme to track; the mantra replaces rhyme. [INFERRED] The video's rhythm must come from repetition and accumulation, not from lyrical turns — because the lyrics don't turn, they pile.

---

## PASS 5 — Synthesis: per-section VIBE + MOTIF + CONTEXT + MV implications

### 0.00–18.34s — Intro — *the game, offered politely*

- **Measured:** 11 words in 30s (the slowest block); RMS −23.3 → −20.8 dB (quietest in the song); the intro drawls — "you" held 3.24s, "of" held 2.26s; performed last line "I am your game" (not "dad"); then **13.82s of instrumental** (18.34–32.16s), the longest silence-of-voice in either song.
- **Vibe [INFERRED]:** a gameshow host's bow. Polite, slow, smiling — the yellow ball with the black oval eyes, introducing the game. The menace is entirely in the *slowness*: he has all the time in the world.
- **MV implication:** the monster's entrance is the whole scene. One face, close, slow, smiling. The 13.82s instrumental is the arrival — the room, the suit, the ball head turning to camera. Do not rush it; the audio has given you fourteen seconds of picture. The "game" line is the feint — stage him as a host, a toy, a plaything, *before* the claim.

### 18.34–32.16s — The instrumental breath — *the room*

- **Measured:** 13.82s, no words; RMS rising −20.8 → −17.2 dB.
- **MV implication:** the only true negative space in MV-3. Use it for the room: the corner, the speaker, the morning light. The monster is *located* here. If the video has one establishing wide shot, this is it.

### 32.16–62.20s — Verse 1 — *the claim, introduced as fact*

- **Measured:** 80 words in 30s; RMS −16.9; "I've been here the whole time, kid" (32.16s) — the first line after the breath; "I raised you in the dark and the light" (48.12s).
- **Vibe [INFERRED]:** the monster states his credentials. He raised you. He was there morning and night. The verse is a résumé delivered as a lullaby.
- **MV implication:** the verse is the *evidence* montage — morning, night, dark, light, the corner, the room. Each line is a small scene. The voice is low and steady; the picture can cut on the line boundaries (the lines are short and declarative).

### 62.20–116s — Chorus 1 — *the mantra, first pile*

- **Measured:** 49 + 73 words across the two 30s blocks; RMS −17.7 → −15.6; tempo feel ~127 BPM here (per-third: first third 129).
- **Vibe [INFERRED]:** the game becomes a chant. "Say it with me" is the recruitment — the audience is invited in.
- **MV implication:** the chorus is where the echo staging pays off: the same face twice, the reflection, the second ball-head. The camera should start recruiting the viewer — looks to camera, the claim offered outward.

### 116–150s — Chorus 2 — *the mantra, with the room talking back*

- **Measured:** 62 words; RMS −16.4 → −14.7; "Short words, easy words, the kind that sticks fast" (116.14s) — the song describing its own method.
- **Vibe [INFERRED]:** self-aware. "They study the hooks and the loops" is still to come, but "short words, easy words, the kind that sticks fast" is the song winking at its own technique. The monster knows he's a hook.
- **MV implication:** the chorus-2 staging can afford a wink — the monster acknowledging the camera, the trick showing. Not breaking character; *enjoying* it.

### 150–168s — Verse 2 tail / mantra start — *the long vow*

- **Measured:** 36 words; the 16.20s segment 150.30–166.50 is five consecutive "I am your dad"s; then a 2.26s gap (166.50 → 168.76s).
- **Vibe [INFERRED]:** the mantra stops being a chorus and becomes a *drone*. Five in a row, no response lines, no variation. The song is no longer asking; it is stating.
- **MV implication:** five identical lines need five *different* pictures or one picture that accumulates — the same face, closer each time; or more faces joining in. Do not cut five identical shots.

### 168–258s — The long mantra (half-time heart) — *the spell, at half speed*

- **Measured:** tempo feel 63.5 BPM (half-time); RMS −14.9 → −12.1 with dips at 240–250s (−15.5); the 23.18s segment 168.76–191.94 ("you can close your eyes, you can plug your ears, the words still bounce around inside your head") is the longest single segment in the song; the 25.40s segment 195.24–220.64 and 24.46s segment 220.64–245.10 follow.
- **Vibe [INFERRED]:** the song's trance section. The beat halves, the lines stretch, the claim repeats without variation. "You can close your eyes, you can plug your ears" — the song *dares* the listener to escape, and answers its own dare: you can't, the words bounce around inside your head.
- **MV implication:** halve the cutting rate with the beat. Longer holds, slower pushes, fewer cuts. This is where the speaker-medium motif pays off: radios, TVs, the voice coming out of objects while the monster himself barely moves. The 2–3s gaps (191.94 → 195.24s, 3.30s — the longest internal gap) are the reframing beats.

### 258–288s — The mantra pile-up — *the sprint*

- **Measured:** 29.48s segment (258.32–287.80) of continuous mantra; **171 words in 30s (5.7 wps sustained)**; RMS −12.4 → −10.7 (near-loudest); Whisper re-pass hears only 40 words here (repeat-collapse at its worst).
- **Vibe [INFERRED]:** the spell at full sprint. The song stops being a song and becomes a pile — the phrase stacking on itself until it means nothing and everything.
- **MV implication:** unfilmable as lip-sync; stage it as a pile-up (fast cuts, accumulating faces, the phrase stacking). This is the block the v1 production already learned is structural (S30/S35 repeat-drop class). Do not fight it with a single take; embrace the montage.

### 288–313s — Breakdown — *the truth, in the dark*

- **Measured:** RMS dips to −14.7 (290–300s) while the surrounding blocks sit at −10.7/−12.7; centroid darkest in the song (1955–2046 Hz); words fall off a cliff (39 in 30s); lines are short with 2.2–2.4s gaps: "All of you." (309.88–311.44) · "Every single one." (313.66–315.66) · "You know it now." (319.50–321.44).
- **Vibe [INFERRED]:** the only part of the song that isn't a game. After 96 repetitions, the claim is stated slowly, in the dark, without the echo. It is the scariest 25 seconds in either song precisely because it stops performing.
- **MV implication:** the breakdown is the video's dynamic opposite of the pile-up: still, dark, one face, no echo, each line given a full frame. Grade it darker than the choruses even though the RMS is high. This is the scene the whole video is building toward — the moment the joke stops being a joke.

### 313–354.8s — Final chorus / outro chant — *the claim, kept*

- **Measured:** RMS −10.8 → −10.4 sustained (loudest sustained block in the song); centroid recovers to ~2200–2290 Hz; the last Whisper word is "dead" at 343.62–346.22s ("dad" heard as "dead" — the final consonant unvoiced in the low voice); fade-out tail 354.10–354.80s (0.70s, the only silence gap).
- **Vibe [INFERRED]:** the song ends by *keeping* the claim. Eight more "I am your dad"s in the final chorus, then the chant runs out the door. The "dad"/"dead" confusable in the final lines is either a flaw or a gift — the monster's claim and a threat, in the same breath.
- **MV implication:** the outro is the widest, loudest, most populated block — and the *slowest* mouths after the pile-up. The final frames should hold the monster's face through the fade (the only silence, 0.70s — hold, don't cut). If the video has a final sting, it is here: the ball head, the black oval eyes, the claim still hanging in the air after the music stops.

---

## REVISIT — Independent Whisper base re-pass (2026-11-05 ~14:40 EST)

Fresh unprompted faster-whisper **base** run on `work/gemini/song_16k.wav` (word timestamps, en, prob 1.0; numpy-array input). Saved: `/tmp/mv3_whisper_revisit.json` (70 segments, **604 words** vs SONG_WORDS 729). Findings:

### What it heard [MEASURED]

- **Alignment is good where the song is slow, and collapses where it is fast.** Difflib ratio 0.717; 478/729 reference words in equal blocks. Per-30s word counts match almost exactly until 270s (0–30: 11/11 · 30–60: 80/80 · 60–90: 49 ref vs 58 hyp · 90–120: 73/78 · 120–150: 62/63 · 150–180: 36/39 · 180–210: 42/46 · 210–240: 66/58 · 240–270: 63/60). Then **270–300s: ref 171 vs hyp 40** — the mantra pile-up collapses in ASR. Whisper hears the phrase once where it is sung four-plus times in a row. This is the repeat-collapse at its most extreme, and it lands exactly on the block the v1 production already classified structural (S30/S35).
- **"Dad" is heard only 29 times vs 97 in the reference, and the 4-gram "I am your dad" only 29 times vs 96.** The mantra is *merged*, not misheard: Whisper collapses consecutive repetitions into one.
- **"Dad" → "dead" in the late choruses [MEASURED]:** from ~ref word 435 onward, Whisper renders "dad" as "dead" ("I am your dead", repeatedly, including the final word at 343.62–346.22s). The final consonant is unvoiced/ambiguous in the low voice. [INFERRED] Either a caption hazard (the word on screen must be "dad" — the sheet governs) or a deliberate chill (the claim and a threat in the same breath). Do not let an ASR caption write "dead".
- **Intro corroborated:** first heard word "Listen," at 3.42s (ref 2.82s — 0.6s late, within Whisper's known onset lag); "I am your game" heard at 17.78s (prob 0.111, same word as SONG_WORDS). The intro's timings and the "game" feint are independently confirmed.
- **Word-level confirmations:** "it lives inside" → "I live" (the "it" is swallowed — the performed line is closer to "I live inside" than the sheet admits); "everyone are you" → "every one of you" (the ear smooths the sheet's ungrammatical line); "study dogs" → "started off" and "study the loops" → "started a loop" (Verse 3 blurs at speed); "plug your ears" → "pluck your ears" (bridge, /l/ confusable).

### What the re-pass means for the video [INFERRED]

- **The pile-up (270–300s) cannot be lip-synced word-for-word and cannot be captioned word-for-word by any ASR.** It is a montage block by measurement, not by taste. The v1 structural classification of S30/S35 is confirmed by an independent system.
- **The breakdown's words are the clearest in the song** (hyp matches ref closely at 300–330s: 44 vs 39). The slow lines survive ASR; the fast mantra doesn't. Stage the breakdown as the intelligible payoff — the audience will actually hear these words.
- **Caption "dad", never "dead".** The late-chorus "dead" readings are an ASR artifact of the low voice's final consonant, but they are also a warning: if the take's final consonant is that weak, the *mouth* must close visibly on the "d" — the picture carries the consonant the audio drops.

---

## Gaps, traps, and what to measure next

1. **No trusted per-line f0 track exists for MV-3 yet.** My crude autocorrelation track (median ~110 Hz, bass-locked in the mantra blocks) is a rough cross-check only. The MV-3 Gemini audit (Stage D, blocked on the app endpoint fix) will supply per-line speaker/f0 data; re-run the Pass 2 table then.
2. **No stem separation was run.** The backing's internal arrangement is unmeasured for both songs.
3. **Chroma is weak** (max weight ~0.13). The A-major sketch is not a key determination.
4. **Tempo is two-geared, not one number.** Quote it as "~127 BPM, half-time feel (~63 BPM) in the 118–236s middle third" — never as a single BPM without the caveat.
5. **The v1 take-drift findings stand [HEARSAY from MV3_TIMING_DIAGNOSTIC.md]:** takes drift by tempo, not shift (S01 t2 ~22% fast, S02 t2 ~20% fast, S07 t1 lag +1.72s, S10 t1 ~+0.5s, S19 t1 +0.88, S29 t1 +1.04, S39 t1 coverage gap — sings once 0→3.14s then silent ~6s). The retimed master already corrects these (3 warps changed); the Gemini audit will check whether the corrections hold.
6. **The "game" feint and the "dead" hazard** are the two word-level findings the captions and the staging must respect: intro says "game", outro must read "dad".

## Measurement log

- Script: `/tmp/audio_bible.py` (numpy/scipy; no librosa). Inputs: `work/gemini/song_16k.wav`. Outputs: `/tmp/mv3_measure.json` (full per-second/per-frame tables).
- Tempo: flux-autocorr 63.5 full-song (half-time lock), per-third 129.0/63.5/129.0, beat-median 125.0, 693 onset peaks.
- f0 crude track: 5686/11084 frames voiced, median 109.6 Hz.
- Whisper re-pass: faster-whisper base, `~/workspace/fw-venv`, word timestamps, numpy-array input. Saved `/tmp/mv3_whisper_revisit.json` (70 segments, 604 words).
- Motif counts: Python `collections.Counter` on SONG_WORDS word triples; phrase count by consecutive 4-gram match.
