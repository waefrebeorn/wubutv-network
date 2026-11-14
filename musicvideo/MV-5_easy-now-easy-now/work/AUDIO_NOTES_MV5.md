# AUDIO BIBLE — MV-5 "Easy now, easy now (THE VOICE)"

**Song:** MV-5 "Easy now, easy now (THE VOICE)" — Suno track, 206.4s
**Source measured:** `track.mp3` (md5 `0c1bcafa568547e2d4fa36e133ad3626`, never modified) via `work/gemini/song_16k.wav` (16 kHz mono, 3,302,400 samples, verified same signal as the master audio)
**Written:** 2026-11-05 ~14:30 EST, by the audio-bible agent (parent order ~14:13 EST: "absorb audio, make the most verbose notes, revisit it multiple times, compile the music video needs — vibes, motifs, contexts")
**Companion files read:** `lyrics.txt` (sheet), `SONG_WORDS.json` (546 words, 123 lines, v1 Whisper + targeted re-decodes), `work/gemini_song.json` (82 segments, 496 words, Gemini 3.5 Transcribe), `work/gemini_speakers.md` (Stage A f0 anchoring), `work/gemini_diff.md` (Stage B verdicts), `work/gemini_line_f0.json` (per-line pyin + aubio), `LYRIC_TIMELINE.md` (v1 ownership table)

## How to read this file — MEASURED vs INFERRED

- **[MEASURED]** — a number produced by a tool in this pass, with the method named. Reproducible from the files above.
- **[INFERRED]** — a reading drawn from measurements + lyrics. It is a judgement call, flagged as such. Where two readings are possible, both are given.
- **[HEARSAY]** — a claim carried over from v1/Gemini work, not re-measured here. Cited to its source file.
- I cannot hear the audio — there is no listening channel. Everything here is measurement + re-measurement. Where the measurements are silent or ambiguous, this file says so instead of inventing a hearing.

## Methods used (and what was NOT available)

- **Tempo/energy/timbre:** custom numpy/scipy script (`/tmp/audio_bible.py`, kept out of the project): per-second RMS + peak + ZCR; spectral centroid per 0.5s (4096 FFT); chroma per 1s (16384 FFT, 55–2000 Hz); spectral-flux onset envelope → tempo by autocorrelation (60–200 BPM search) + beat-peak median as a second method; silence gaps at −45 dBFS per 50 ms; f0 by autocorrelation per 32 ms frame (60–500 Hz, voiced if normalised autocorr peak > 0.45).
- **librosa was NOT installed** and was not installed for this pass — all spectral work is hand-rolled numpy/scipy. The coordinator's saved pyin/aubio tracks (`work/pyin_f0.npy`, `work/f0_track.npy`, via `work/gemini_line_f0.json`) are the trusted f0 source; my own autocorrelation f0 track is a rough cross-check only (see the octave-error warning in Pass 2).
- **faster-whisper base** (cached model, `~/workspace/fw-venv`, offline) was run as an independent re-pass with word timestamps. Note: both system python3 and fw-venv faster-whisper fail on file paths (PyAV `metadata_errors` kwarg mismatch) — the workaround used here is to decode with scipy and pass a numpy array. That is a tooling gap worth knowing, not a song fact.
- **Revisits:** tempo was measured three ways (full-song autocorr, per-third autocorr, beat-peak median); RMS was recomputed at 1s and 5s windows; f0 was measured by two independent estimators already on disk (pyin + aubio) and a third crude one here; word times were cross-checked three ways (v1 Whisper SONG_WORDS, Gemini segments, fresh Whisper base re-pass). Where methods disagree, the disagreement is reported below, not averaged away.

---

## PASS 1 — Structure / tempo / energy

### Tempo [MEASURED]

| Method | Result |
|---|---|
| Spectral-flux autocorr, full song | **107.0 BPM**, confidence 0.549 (top-5 candidates all 105.0–107.0 — a broad flat peak, not a sharp one) |
| Same, per third (0–69s / 69–138s / 138–206s) | **107.0 / 107.0 / 107.0 BPM** (conf 0.61 / 0.50 / 0.48) |
| Beat-peak median (362 onset peaks, median inter-beat interval) | **105.3 BPM** |

**Reading:** the song sits at **~106–107 BPM, rock steady, no tempo drift anywhere**. All three thirds agree to the BPM. Beat length ≈ 0.56s; one bar (4 beats) ≈ 2.24s. The flat autocorr peak (105–107 all ≈0.549) means the groove is loose — the onsets are not metronome-sharp, which fits a laid-back boardwalk song. [INFERRED] Staging should never fight this: cuts on the beat land every ~0.56s; a 10s scene holds ~18 beats; the refrain "Easy now, easy now" (4 words) rides roughly 2 beats. Do not cut faster than the beat — the song will feel rushed. Do not hold a static shot longer than ~2 bars (~4.5s) during a chorus — the groove will feel stalled.

### Energy arc [MEASURED] — a slow swell, no drops

Per-5s mean RMS (dBFS, peak-normalised; 0 dB = loudest sample in the track):

| Block | Mean RMS | Peak |
|---|---|---|
| 0–5s | −18.3 | −16.4 |
| 5–10s | −17.1 | −15.8 |
| 10–15s | −16.5 | −14.2 |
| 15–20s | −17.8 | −16.2 |
| 20–25s | −16.0 | −15.4 |
| 25–30s | −15.6 | −15.1 |
| 30–40s | −15.7 | −14.6 |
| 40–50s | −15.2 | −14.6 |
| 50–60s | −15.4 | −14.2 |
| 60–70s | −14.9 | −14.2 |
| 70–85s | −14.7 | −13.4 |
| 85–95s | −15.6 | −13.4 |
| 95–110s | −15.1 | −14.2 |
| 110–120s | −15.0 | −14.0 |
| 120–140s | −14.1 | −13.5 |
| 140–150s | −13.3 | −12.5 |
| 150–160s | −14.5 | −12.3 |
| 160–170s | −13.6 | −12.3 |
| 170–180s | −13.4 | −12.0 |
| 180–190s | −12.5 | −11.8 |
| 190–200s | −12.6 | −11.5 |
| 200–205s | −11.7 | −11.0 |
| 205–206s | −38.5 (fade-out tail) | −13.3 |

Per-section means: Intro −17.2 · Verse 1 −15.6 · Pre-Chorus 1 −15.4 · Chorus 1 −15.0 · C1 tail −14.3 · Verse 2 −15.3 · Pre-Chorus 2 −14.8 · Chorus 2 −14.1 · C2 tail −13.1 · Bridge −14.0 · **Final Chorus −12.7 (loudest section, peak −11.0)**.

**Reading [INFERRED]:** the whole song is one long slow crescendo — about **6.6 dB from the intro floor to the final-chorus ceiling**, with no section that drops back to intro level. There is no "quiet verse after a loud chorus" dynamic; the verses sit only ~1–2 dB under the choruses. The loudest single 5s block is 200–205s, the last refrain before the fade. **MV implication:** the video's energy must climb the same slow ramp. Do not stage a big visual drop (empty frame, slow push-in, desaturated palette) in the middle — the audio never drops, so a visual drop will read as a mistake. Save the widest shots, the brightest grade, and the most motion for 169–206s (Final Chorus). The intro (0–22s) is the quietest block in the song: that is where the camera can be closest and stillest — faces, small gestures, the bike, the boardwalk underfoot. Let the frame get busier as the RMS climbs: extras and background motion should enter gradually from Verse 2 onward, not all at once.

### Silence / breaths [MEASURED]

**Exactly one silence gap ≥ 0.3s below −45 dBFS in the entire song: 205.95–206.40s (0.45s) — the fade-out tail.** There is no internal pause, no breath gap, no beat of silence anywhere else. The song is wall-to-wall sound for 206 seconds.

**Reading [INFERRED]:** the singers never get a rest and the picture never gets one either. Cuts must happen *inside* the sound, on beats or on line boundaries — never on a silence, because there is none to cut on. The only true breath in the song is the 2.38s inter-line gap before L107 (see Pass 2) and the 1.66s lead-in before the first line. Those two gaps are the only places the picture can "exhale" (a held wide shot, a look, a non-singing beat) without fighting the audio.

### Brightness / timbre [MEASURED]

Spectral centroid (mean per section): Intro 2370 Hz · Verse 1 2292 · PC1 2265 · Chorus 1 2370 · C1 tail 2399 · Verse 2 2295 · PC2 2270 · Chorus 2 2465 · C2 tail 2572 (brightest) · Bridge 2412 · Final Chorus 2304. Overall range per 0.5s frame: 715–3982 Hz. Per-5s means stay in a narrow 2.1–2.6 kHz band for the whole song — the brightest 5s blocks are 10–15s (2830 Hz, the "ta-da" vocalise), 65–70s (2571 Hz), 135–140s (2643 Hz), 145–150s (2564 Hz).

**Reading [INFERRED]:** the mix is **warm and stable, not bright** — a midrange-centred song (2.2–2.4 kHz) with no harsh top end and no section that changes colour. The two brightest moments are the girl's vocalise (10–15s) and the C2 tail / bridge entry (135–150s), both girl-voice moments. **MV implication:** grade warm, not crisp. Teal/gold boardwalk light, not white-hot noon. The girl's lines are the brightest sound in the song — when she sings, the picture can afford its brightest, most saturated frame (sun glint, white sand, her purple hair against sky). The cat's verses are the warmest/darkest sound — keep his frames in shade, wood, warm wood-tones, dusk-side light.

### Harmony sketch [MEASURED, WEAK]

Chroma (1s windows, 55–2000 Hz): the top pitch classes are **Bb (A#) 0.12, Eb (D#) 0.10, G 0.09, C 0.09 overall**, and the same four lead in *every* section — Intro, both verses, both pre-choruses, all choruses, bridge, final chorus. No section changes its chroma profile.

**Reading [INFERRED, LOW CONFIDENCE]:** the chroma is diffuse (max weight 0.12–0.14 out of 1.0) — the mix is dense and the chroma does not resolve a clean key. The recurring Bb/Eb/G/C cluster is consistent with a **Bb-major / Eb-major family** (Bb–Eb–F–Gm neighbourhood), but this is a sketch, not a key determination; do not build a harmonic argument on it. What *is* solid: **the harmony does not modulate or change colour by section** — the song's variety comes from the voices and the words, not from chord changes. **MV implication:** visual variety must come from staging, character and motion, not from "the music changes here" — because it doesn't. The picture has to do the work the harmony isn't doing.

---

## PASS 2 — Vocal character (who sings, how high, how fast)

### The two voices [MEASURED — trusted f0, coordinator's pyin + aubio]

From `work/gemini_line_f0.json` (123 lines, per-line pyin + aubio medians; the authoritative f0 source — see the bass-lock trap below):

| Voice | Aubio median f0 (lines with ≥3 voiced frames) | pyin band profile (pooled) |
|---|---|---|
| **CAT** (79 lines) | **131.4 Hz** (n=51, p10 71.0, p90 253.3) | bass <80 Hz 0.638, cat-band 97–160 Hz 0.343, girl-band 0.005 |
| **GIRL** (40 lines) | **260.8 Hz** (n=20, p10 65.2, p90 306.8) | bass <80 Hz 0.831, girl-band 200–330 Hz 0.134 |
| **SPLIT** (4 lines) | 198.8 Hz (n=4) | girl-band 0.60, cat-band 0.27 |

**The bass-lock trap [MEASURED, important]:** the mix carries a bass at ~65 Hz and both estimators lock onto it in dense/fast passages. Pooled pyin medians are bass-dominated for *both* voices (CAT 66.5 Hz, GIRL 67.1 Hz medians of line-medians) — those numbers are the bass, not the voice. What carries weight is the *band fractions* and the *clean anchors*: the CAT's aubio median (131 Hz) vs the GIRL's (261 Hz) is the real separation — **almost exactly one octave apart**. [INFERRED] The octave gap is the song's central vocal fact: the cat sings low and warm, the girl sings high and bright, an octave up. When they trade lines in the chorus, the pitch *doubles and halves* every two lines. That alternation is the hook's musical engine as much as the words are.

**Clean anchors [MEASURED]** — lines where pyin puts ≥80% of voiced frames in one voice band (≥5 voiced frames):

- GIRL: I09 18.64–22.00 "(ta-da vocalise)" pyin 316.4 Hz · L56 116.00–118.28 "And my whole head replays" 311.0 · L57 121.26–122.58 "Easy now, easy now" 311.0 · L96 174.92–176.04 "No need to run" 246.8 (SPLIT line, girl-majority)
- CAT: I03 5.98–8.01 "Easy now, easy now" 104.4 · L16 52.80–56.50 "And my whole head replays" 131.5 · L42 95.80–96.84 "Like a hand drum roll" 130.8 · L47 104.72–106.42 "You said, don't think too hard" 130.4 · L75 150.00–151.30 "We stay out in it" 131.5 · L77 152.36–153.58 "We still move with it" 154.6 · L78 153.58–154.42 "Hand in my hand" 130.8 · L79 154.42–155.72 "No speech, no show" 155.5

**My own autocorrelation f0 track [MEASURED, ROUGH — do not quote as voice pitch]:** 3239/6446 frames voiced (50%), median 160 Hz, p10 65.6, p90 500.0 (hits the 500 Hz cap — octave errors). Per-section medians from this track (Intro 149, V1 120, PC1 205, C1 131, C2 314, C2 tail 390, Bridge 237, FC 400) are *contaminated by octave jumps* and disagree with the trusted track in the Final Chorus — the trusted per-line data is the authority. The crude track is useful for one thing only: it confirms the song is voiced about half the time (the other half is backing/bass/breath), and that the *proportion* of voiced frames does not collapse anywhere — the singers are present throughout.

### Speaker map [HEARSAY from gemini_speakers.md, corroborated by f0 above]

- **spk_0 = CAT** (40 Gemini segments) — low voice. **spk_1 = GIRL** (33 segments) — high voice. **spk_2 = GIRL** (9 segments) — a diarization split of the same voice as spk_1, NOT a third voice. Evidence: L57 under the spk_2 label measures 311.0 Hz (girl-band, 13/13 frames); Chorus 2 alternates spk_2/spk_0 in the exact pattern spk_1/spk_0 follows elsewhere; no spk_2 segment measures in any third pitch band. Confidence moderate-high; per-word f0 from the app run (Stage D) can confirm each C2 refrain individually.
- **Owner counts [MEASURED from SONG_WORDS]:** CAT 79 lines / 355 words (65%) · GIRL 40 lines / 167 words (31%) · SPLIT 4 lines / 22 words (4%). The cat carries the song; the girl carries the hook.
- **Undecided lines [HEARSAY from gemini_diff.md — the take audit decides]:** L12 "Yeah, they already understand" (S06), L15 (S07), the L38–L41 girl island (S11/S12), L80/L81 split (S20), the whole bridge alternation L82–L88 (S21), and the tail L106–L110 (S26–S28). In every one of these, f0 either supports the v1 owner or is silent — it never supports a flip — but "leans v1" is not "proved".

### Delivery rate and pauses [MEASURED from SONG_WORDS line times]

- Line duration: median 1.26s, min 0.60s, max 5.84s. Words/second per line: **median 3.51**, max 8.33.
- **Slowest lines:** I09 vocalise 0.60 wps (3.36s for one vocalise) · L09 "Backpack half-zipped" 1.02 · L107 "Easy now, easy now" 0.93 · L109 "Easy now, easy now" 0.68 (the tail refrains stretch out — the song *decelerates* into its ending even though the tempo never changes).
- **Fastest lines:** L51 "You took my sleeve and spun me once" **8.33 wps** (the fastest single line in the song — a spin, fittingly) · L46 "On the rail by the steps" 6.52 · L26/L66/L100 "Keep it loose, keep it low" 5.00 · L28/L68/L102 "Let it drift, let it go" ~5.0 · L38 "Calling mango sweet" 5.00.
- **Section word rates [MEASURED]:** Intro 1.67 wps · Verse 1 2.09 · PC1 2.29 · **Chorus 1 3.63 (fastest sustained)** · C1 tail 2.39 · Verse 2 3.11 · PC2 2.71 · Chorus 2 3.63 · C2 tail 1.71 · Bridge 3.57 · Final Chorus 2.36. The choruses are the fastest *sustained* singing in the song; the verses are conversational; the tails and the intro are slow.
- **Gaps ≥ 0.8s between consecutive lines [MEASURED]:** only 8 in the whole song — 1.66s before I01 (lead-in), 1.00s before L04, 0.90s before L13, 1.02s before L17, 0.80s before L41, 1.02s before L56b, 1.24s before L57 (Chorus 2 entry), **2.38s before L107 (the biggest breath in the song, Final Chorus tail)**. Every other line follows the previous one within 0.8s. The singers trade lines with almost no air between them — the conversation never pauses.

**Reading [INFERRED]:** this is a *fast-talking* song wearing a slow groove. At 107 BPM the beat is relaxed, but the words come at 3.5/second in the choruses — roughly one word per beat-and-a-half, with the response lines (L51 at 8.33 wps) bursting to two words per beat. **MV implication:** the mouths must move fast in the choruses and the camera must not. A slow push-in during a 5-wps line will feel like the picture is lagging the song. Conversely, the slow lines (I09, L107, L109) are the places for a held close-up: the mouth is open, the note is held, the face can carry the frame. The 2.38s gap before L107 is the single best "reaction shot" slot in the song — a look, a smile, a hand reaching — with no words to cover. The 1.24s gap before L57 is the Chorus 2 entry breath: the camera should *arrive* there, not cut there.

---

## PASS 3 — Timbre / texture / rhythmic density

### Rhythmic density [MEASURED]

- **362 onset peaks** detected on the spectral-flux envelope over 206.4s → **1.75 onsets/second** on average. Beat-median tempo 105.3 BPM from inter-beat intervals.
- Zero-crossing rate per second: tracked but not decisive (voiced singing dominates; ZCR follows the vocal, not the backing — no separate drum/percussion signature was isolated, and none is claimed here).
- **Word density over time [MEASURED]:** the words are not evenly spread. Chorus blocks run 3.63 wps sustained; the intro runs 1.67. The densest single stretch is Verse 2's middle (L43–L52, ~95–112s) where four consecutive lines exceed 4.3 wps — the story's busiest passage (forgetting the list, the bills, the boombox, the spin) is also its fastest-talking passage.

### Texture [INFERRED from centroid + chroma + f0 coverage]

- The backing is **continuous and unchanging in colour** (centroid 2.1–2.6 kHz everywhere, chroma profile identical in every section). There is no audible section where the arrangement thins out or a new instrument enters — at least, nothing the spectral measurements can see. [MEASURED gap: no source separation was run; the backing's internal arrangement (bass vs keys vs percussion) was not decomposed. That is a known hole — a stem-separation pass would be the next measurement to run if the staging needs to know when the bass drops out or the drums enter.]
- The vocal sits on top of the backing for the whole song (f0 voiced ~50% of frames in my crude track; the trusted pyin track has 2210/6451 voiced frames, ~34% — the rest is backing-dominant frames where the bass wins the estimator). Either way: **the voice is never alone and never absent**. There is no a-cappella moment, no instrumental break, no solo. [INFERRED] The picture must never stage a "music stops, look at this" beat — the music never stops. Even the 13.8s-scale gaps in MV-3 don't exist here; MV-5's longest line gap is 2.38s.

---

## PASS 4 — Lyrics / motifs

### Word counts [MEASURED from SONG_WORDS, 548 tokens counted incl. the "(ta-da vocalise)" stage direction; 546 words per the file's own count]

Top words: **now 61 · easy 60** · the 26 · we 22 · it 15 · ride 12 · you 10 · let 9 · small 9 · my 8 · in 8 · no 8 · i 7 · just 7 · two 7 · sparks 7 · and 6 · with 6 · keep 6 · go 6 · to 5 · comes 4 · on 4 · your 4 · hand 4.

**The hook is 22% of the song.** "Easy" + "now" = 121 of 548 tokens. The line "Easy now, easy now" occurs **30 times** as a full line. The eight response lines each occur 3 times ("We ride, we ride" ×6 counting intro/final repeats, "Just two small sparks" ×6, "Till the morning comes" ×3, "With you by my side" ×3, "No need to run" ×3, "We hold the sun" ×3, "Keep it loose, keep it low" ×3, "Let it drift, let it go" ×3, "We're good where we are" ×3).

### Rhyme [MEASURED]

Line-final rhyme endings (last two letters, ≥3 occurrences): **-ow 35 lines** (now / go / low / slow / show — the whole song rhymes on "ow"), -de 11, -ks 7 (sparks), -re 6, -un 6, -ng 5. The song's rhyme world is essentially one sound: "ow". [INFERRED] The "ow" rhyme is the song's lullaby quality — every chorus lands on the same open vowel. Visually: the "ow" lines are the *open-mouth* lines. The refrain staging should lean into the open mouth — the "o" of "now" and "go" and "slow" is the most filmable vowel in the song.

### Motifs (what the song is *about*, line by line) [INFERRED from lyrics + ownership]

1. **The refrain as a mantra / a spell.** "Easy now" is not advice, it's an incantation — 30 repetitions, same words, same shape, alternating singers. The girl *starts* it (spk_1, high voice) and the cat *answers* it (spk_0, low voice) in Choruses 1/3/4; in Chorus 2 the same pattern runs under the spk_2 label. [INFERRED] The refrain is a call-and-response ritual between the two of them. MV rule: **never put the wrong singer's mouth on a refrain line** — the alternation IS the scene. A refrain line sung by the wrong face breaks the ritual.
2. **The boardwalk as a place that understands.** Verse 1: bare feet, salt skin, blue shirt, red bicycle, backpack half-zipped, keys, waves that "already understand". Verse 2: mango vendor, socks in the sand, tide tapping time, ice cup sweating, boombox kids. The setting does emotional work the characters won't say out loud. [INFERRED] The boardwalk is the third character. Give it shots: feet on wood, salt, the pier, the vendor's corner, the rail by the steps, the tide. The setting shots belong in the *verses* (CAT's lines), where the words are naming the place.
3. **Forgetting as the joke.** The song's jokes are all about *dropping* things: "I forgot the list, forgot the bills, forgot what I was told" (L43–L44) · "don't think too hard / so I didn't, not yet" (L47–L48) · "nothing to prove / nothing to lose" (bridge). The comedy is release, not punchlines. [INFERRED] The jokes land on the CAT's face — he owns the verses and the bridge. The girl's lines are the *straight* lines (the refrain, the look that makes his head replay). Comic rule: the cat gets the shrug, the dropped list, the "not yet"; the girl gets the look that causes it.
4. **"Two small sparks" / "just two small sparks".** The smallest image in the song, repeated 6 times as a full line, always as a response line (GIRL in the v1 table for the split? — L57/L96 area; the sparks lines are CAT/GIRL alternation responses). [INFERRED] "Two small sparks" is the song's thesis in four words: small, warm, two of them. It's the image the final frame should hold — two small lights, two figures, the sun held between them ("We hold the sun" is its twin line).
5. **The held sun / the drift.** "We hold the sun" · "Let it drift, let it go" · "Keep it loose, keep it low" — the chorus's second half is all *release* verbs: hold, drift, go, loose, low. [INFERRED] The chorus's emotional shape is: tighten ("Easy now" — the call) then release (the response). Staging should mirror it: the "Easy now" line is a *lean-in* (close, face, mouth), the response is a *lean-back* (wider, the pair, the sky, the sea).
6. **The bridge as a vow.** "If the rain comes down / we stay out in it" · "Hand in my hand / no speech, no show" · "You and me, same pace / same worn-in shoes" · "Nothing to prove / nothing to lose". The bridge is the only place the song makes a promise, and it makes it by *refusing* performance ("no speech, no show"). [INFERRED] The bridge must not be staged as a performance. No singing-to-camera, no big gesture. Side by side, walking, same pace — the vow is in the walking, not the singing. Note the staging trap from v1: S21's "lean-back" motion beat fired early and ate lines — do not give the model a big motion while bridge lines remain.

### Jokes and who owns them [MEASURED ownership + INFERRED comedy read]

| Joke / image | Line(s) | Owner (v1) | Why it lands |
|---|---|---|---|
| "Blue shirt, red bicycle" (sheet) vs red jacket + blue bike (visual direction governs) | L05 | CAT | The deliberate mismatch is the video's in-joke: the picture corrects the lyric. |
| "Backpack half-zipped" | L09 | CAT | A small, specific, visual gag — the half-zipped bag. Slowest verse line (1.02 wps) — time to show it. |
| "You nodded at the waves like / Yeah, they already understand" | L11–L12 | CAT (L12 UNDECIDED, Gemini says GIRL) | The waves understand — the joke is that nobody else does. L12 is the one line where the singer is genuinely disputed; the take audit decides. |
| "Calling mango sweet" | L38 | GIRL (island in a CAT segment) | The vendor's call — a sound gag. Fastest verse line (5.0 wps). |
| "I forgot the list, forgot the bills" | L43 | CAT | The release joke — forgetting as freedom. |
| "don't think too hard / So I didn't, not yet" | L47–L48 | CAT | "Not yet" is the whole song's shrug. |
| "Kids with a boombox / Cutting through the crowd" | L49–L50 | CAT (words UNDECIDED — Gemini hears "boardwalks/lost") | The crowd joke; the words themselves are unstable, which is itself a note: caption carefully. |
| "You took my sleeve and spun me once / Like none of it was loud" | L51–L52 | CAT (words UNDECIDED) | The spin is the song's one physical gag — and its fastest line (8.33 wps). The spin must be *in* the take, not added in the edit. |
| "Heart in the breeze / And the bass move slow" | L80–L81 | SPLIT (L80 GIRL / L81 CAT) | The bass joke — the song winking at its own bass. L81's "move" (not "moves") is adjudicated from the sheet + Whisper. |
| "Same worn-in shoes" | L87 | CAT (Gemini "worn in" — tokenization only) | The worn-in shoes are the bridge's thesis: nothing new, nothing to prove. |

---

## PASS 5 — Synthesis: per-section VIBE + MOTIF + CONTEXT + MV implications

Scene map from `work/gemini_diff.md` (29 slots, v1 takes) + section measurements above. Times are SONG_WORDS line times; scene boundaries are the v1 CUTLIST slots.

### 0.00–10.04s — Intro (S01, CAT) — *the spell is cast before you know it*

- **Measured:** RMS −18.3 → −17.1 dB (quietest block); centroid 1963 Hz at 0–5s (darkest in the song); 9 lines, 34 words, 1.67 wps (slowest sustained); first line at 1.66s (1.66s lead-in — the song starts *after* the picture does); f0 anchor I03 104.4 Hz CAT.
- **Vibe [INFERRED]:** hushed, conspiratorial. The refrain arrives *before* any verse explains it — the audience hears "Easy now" four times before they know who's talking or where they are. It is a lullaby opening that doesn't explain itself.
- **Motif:** the refrain introduced as pure sound, before meaning. "Till the morning comes" (I04) is the intro's one forward-looking line — a promise the final chorus will collect.
- **MV implication:** closest, stillest camera in the whole video. Faces first, place second. The cat sings the whole intro (v1 owner CAT, inferred confidence) — his mouth, his eyes, the red collar, the yellow bell. Do not open on a wide boardwalk shot: the song opens on a voice, so the picture should open on a face. The 1.66s before the first word is the title beat — the frame should already be *there* when the voice starts.

### 10.04–18.64s — Intro tail / vocalise (S02–S03) — *the girl answers without words*

- **Measured:** S02 cutaway, no sung words; S03 = I09 "(ta-da vocalise)" 18.64–22.00, pyin 316.4 Hz, 34/34 girl-band frames — the cleanest GIRL anchor in the song; centroid brightest block 10–15s (2830 Hz).
- **Vibe [INFERRED]:** a laugh made of music. The vocalise is the girl's first sound and it isn't a word — it's a "ta-da", a flourish, a *look at me*.
- **MV implication:** this is the girl's entrance. The vocalise needs her face in a bright frame (the brightest sound in the song earns the brightest picture). The "ta-da" is a visual cue: a small flourish — a spin of the hat, a hand presented, the bike bell — something that *shows* rather than says.

### 18.64–22.00s / 22.00–46.94s — Verse 1 (S03–S06) — *the place, named by the cat*

- **Measured:** 12 lines, 52 words, 2.09 wps; RMS −15.6 dB; centroid 2292 Hz; CAT throughout (Gemini 8–45 spk_0 agrees); slowest verse line L09 "Backpack half-zipped" 1.02 wps.
- **Vibe [INFERRED]:** conversational, observational, warm. The cat is *telling* you where you are — feet, salt, shirt, bicycle, pier, backpack, keys, waves. It's a list that becomes a place.
- **Motif:** the boardwalk as third character (see Pass 4). Every line names a thing you can point a camera at.
- **MV implication:** this is the setting-establishing block, but it is sung, not narrated — the cat's mouth must be on screen for the lines, and the *things* must be in the frame around him. Shoot the verse as a walk: the cat posted up, the girl pulling near, the pier behind. L09's slow delivery is a gift — a full 2.9s for "Backpack half-zipped": hold on the bag. L12 ("Yeah, they already understand") is UNDECIDED on singer — do not lock its staging until the take audit lands; if the take sings it as CAT, the cat nods at the waves; if GIRL, she does.

### 47.76–57.52s — Pre-Chorus 1 (S07) — *the turn*

- **Measured:** 4 lines, 20 words, 2.29 wps; RMS −15.4; f0 anchor L16 "And my whole head replays" 131.5 Hz CAT (clean); L15 UNDECIDED (Gemini spk_1/GIRL vs v1 CAT, f0 silent).
- **Vibe [INFERRED]:** the song leans forward. "Slow down, take your time" is sung *to* someone — the first direct address after a verse of description. "My whole head replays" is the song's thesis about memory: one look, and it all plays back.
- **MV implication:** the pre-chorus is the look. One small look from her (the lyric says so) — the camera should find her face here even though the cat is singing. Two-shot, eye-line, the look that causes the replay. L15's singer is undecided — the take audit decides whose mouth carries "Slow down, take your time".

### 57.52–85.16s — Chorus 1 + tail (S08–S10) — *the ritual, first time*

- **Measured:** 16 lines, 70 words, **3.63 wps (fastest sustained in the song)**; RMS −15.0 (chorus) → −14.3 (tail); the refrain alternation GIRL "Easy now" / CAT response confirmed by Gemini segment labels line-for-line; centroid 2370–2399 Hz.
- **Vibe [INFERRED]:** release after the lean-in. The chorus is fast-talking but the *feeling* is loose — "Keep it loose, keep it low / Let it drift, let it go" — the words hurry while the body relaxes. That tension (fast mouth, loose body) is the chorus's whole charm.
- **Motif:** call-and-response as ritual. The girl calls (high, bright, 311 Hz territory), the cat answers (low, warm, ~131 Hz). The alternation must be visible: the camera should *trade* faces with the voices — her on "Easy now", him on the response. A chorus staged on one face breaks the ritual.
- **MV implication:** fastest mouths in the song + loosest bodies. Do not stage the chorus as a performance (facing camera, singing out) — stage it as a ride: side by side, moving, the bike rolling, the boardwalk passing. The response lines ("We ride, we ride", "Just two small sparks") are the *wider* shots — the pair, the sun, the sea. The C1 tail (76.8–85.2s, "I gotta go there" — dropped by both Gemini and Whisper, v1 reading stands) is where the chorus exhales: 2.39 wps, slower, a gear-down into Verse 2.

### 85.16–111.90s — Verse 2 (S11–S13) — *the busiest, fastest-talking stretch*

- **Measured:** 16 lines, 83 words, 3.11 wps; RMS −15.3; the densest passage L43–L52 (~95–112s) runs four consecutive lines over 4.3 wps; L51 is the fastest line in the song (8.33 wps); S13 is structural cover (no mouth) with UNDECIDED words L45/L49–L52.
- **Vibe [INFERRED]:** the verse where the day gets crowded — vendor, tide, boombox, crowd, the spin. The song's comedy peaks here and so does its speed. It feels like the boardwalk filling up.
- **Motif:** forgetting as freedom (L43–L44), the spin (L51–L52). The spin is the song's one physical gag and it arrives at maximum speed — the staging must *have* the spin in the take, at full pace, not faked in the edit.
- **MV implication:** Verse 2 is where the background earns its keep — extras, the vendor, the kids with the boombox, the crowd the song names. But the mouths are the fastest in the verses here, so the camera must be *steadier* than in Verse 1, not busier: let the world move around a stable two-shot. S11's girl island (L38–L41, aubio supports GIRL) needs her mouth on L38/L39 even though the surrounding lines are his. S13 has no mouth-sung picture (structural cover) — it is the verse's breathing room, and its caption words (L49–L52) are still UNDECIDED, so caption text there is provisional until the app run.

### 111.90–121.30s — Pre-Chorus 2 + S15 (S14–S15) — *the girl's line, the worst timing*

- **Measured:** PC2 5 lines, 22 words, 2.71 wps; S15 (L56) is the cleanest GIRL anchor in the song (pyin 311.0, 25/25 girl-band frames) and the **worst-timed scene in v1 (median 0.897s, max 1.891s)** — re-placement, not re-warp, is needed. L54 is UNDECIDED (aubio 298.5 Hz on a CAT line — a flipped repeat or an octave error).
- **Vibe [INFERRED]:** the pre-chorus repeated, but this time the girl's voice is unmistakable on the key line — "And my whole head replays" at 311 Hz is the highest clean anchor in the song. The replay line *is* her line.
- **MV implication:** S15 is the scene the v2 rebuild must get right above all others: her face, her mouth, on the highest clean note in the song, with the timing re-placed from correct word times. If one scene earns a re-fire in v2, it is this one. The 1.02s gap before L56b is the breath before her line — the camera should arrive on her face in that gap.

### 121.30–148.70s — Chorus 2 + tail (S16–S18) — *the same ritual, a different label*

- **Measured:** 16 lines, 70 words, 3.63 wps; RMS −14.1 (chorus) → −13.1 (tail, the loudest tail in the song); centroid brightest section (2465–2572 Hz); spk_2 refrains = GIRL per Stage A (L57 311.0 Hz anchor); S16 structural cover.
- **Vibe [INFERRED]:** identical ritual, brighter sound, louder mix. The song does not vary the chorus — it *repeats* it, louder and brighter. The variation is in the picture, not the audio.
- **MV implication:** Chorus 2 must not look like Chorus 1 repeated. Same words, same alternation, different staging — different angle, different part of the boardwalk, the sun lower, the crowd thicker. The C2 tail (140.5–148.7s) is the brightest and loudest tail — the picture's brightest frames belong here, not in the final chorus. The 1.24s gap before L57 is the entry breath: arrive, don't cut.

### 148.70–169.16s — Bridge (S19a–S21) — *the vow, sung side by side*

- **Measured:** 17 lines, 73 words, 3.57 wps; RMS −14.0; centroid 2412 Hz; f0 bass-locked through the whole bridge (the only section where neither estimator can adjudicate singer — the bridge's voices sit in the bass); S21 t3 is PARTIAL (head usable, tail cover); the "I gotta go there / just two small sparks" bridge lines are dropped by Gemini (repeat-collapse).
- **Vibe [INFERRED]:** the song's emotional peak is its quietest *claim*: "no speech, no show". The bridge is a vow made by refusing to perform. It is also the fastest-talking non-chorus section (3.57 wps) — the vow hurries, as if the singer is afraid of being interrupted.
- **Motif:** rain, grey sky, hand in hand, same pace, worn-in shoes, nothing to prove, nothing to lose. The bridge's images are all *weather and walking* — the song stops naming things and starts naming conditions.
- **MV implication:** do not stage the bridge as a performance. Side by side, walking, same pace — the vow is in the walking. No singing-to-camera. The v1 staging trap is documented: a motion beat placed "after the last word" still fires early and eats lines — do not give the model a big motion while bridge lines remain. S21's tail is already montage cover; the head (L82–L86) is the part that must be right, and its singer is UNDECIDED (Gemini says GIRL on L82/L84/L86/L88, v1 says all-CAT, f0 silent) — the take audit decides, and the staging must be ready to flip if the take says GIRL.

### 169.16–206.40s — Final Chorus (S23–S28) — *the ritual, extended, loudest, slowest at the end*

- **Measured:** 20 lines, 86 words, 2.36 wps (slower than C1/C2 — the song decelerates into its ending); RMS −12.7 (loudest section), peak −11.0; the last 5s block (200–205s) is the loudest in the song (−11.7 dB mean); the tail refrains L107/L109 stretch to 0.93/0.68 wps; the 2.38s gap before L107 is the biggest breath in the song; Gemini's tail is unstable (hears "This is now" ×3, "Easy now" ~1.5s early, "Till the morning comes" twice) and f0 is bass-locked throughout the closing block — nothing in the tail is decidable from f0.
- **Vibe [INFERRED]:** the song ends by *staying*. The final chorus adds a fourth repeat of the refrain pair ("We ride, we ride / Till the morning comes" — the intro's promise, collected at last) and then stretches the last "Easy now"s out until they are almost spoken. The loudness peaks while the words slow down: the song gets louder and slower at the same time, like a wave arriving.
- **Motif:** "Till the morning comes" returns — the intro's I04 promise is kept in the final chorus. The tail's possible double "Till the morning comes" (Gemini hears it twice; v1 once; the intro echo-tail precedent makes a real double possible) is the one open question in the song's ending.
- **MV implication:** the final chorus is the widest, brightest, most populated block — and the *slowest* mouths. The last refrains (L107/L109) are held notes: close-ups, open mouths, the two small sparks held in frame. The 2.38s gap before L107 is the best reaction-shot slot in the song — a look between them with no words to cover. The fade (205.95–206.40s, the only silence in the song) is the exhale: hold the final frame through it, do not cut on it. The tail's words/timing/speaker are UNDECIDED (S26–S28) — the take audit and the app's word-level output decide what the final captions say.

---

## Gaps, traps, and what to measure next

1. **No stem separation was run.** The backing's internal arrangement (when the bass enters/drops, whether there is a drum kit, what the keys do) is unmeasured. If staging needs to know the backing's moves, run a Demucs-style separation pass next.
2. **Chroma is weak.** The Bb/Eb/G/C sketch is not a key determination. Do not cite a key for this song.
3. **My autocorrelation f0 track has octave errors** (p90 hits the 500 Hz cap). Quote the coordinator's pyin/aubio per-line numbers, never mine.
4. **The "easy now" intelligibility problem** (see Whisper re-pass section below): the hook is the least ASR-intelligible line in the song. Captions must carry it, and the mouths must be big on it.
5. **Undecided lines stay undecided** until the take audit (Stage D): S06/L12, S07/L15, S11–S12/L38–L41, S20/L80–L81, S21/bridge, S26–S28/tail, plus the word-level questions L49–L52 and L51–L52. Nothing in this file overrides `work/gemini_diff.md`.
6. **The app endpoint is still the blocker for per-word times.** The Playground run gives segment times only. Everything timed here at the word level comes from v1 Whisper (SONG_WORDS) — good, but the app's word-level output is the upgrade path.

## Measurement log (so the next pass can reproduce this one)

- Script: `/tmp/audio_bible.py` (numpy/scipy; no librosa). Inputs: `work/gemini/song_16k.wav`. Outputs: `/tmp/mv5_measure.json` (full per-second/per-frame tables — RMS, peak, ZCR, centroid, chroma, tempo, beats, gaps, f0).
- Tempo: flux-autocorr 107.0 (full + all thirds), beat-median 105.3, 362 onset peaks.
- f0 trusted source: `work/gemini_line_f0.json` (pyin + aubio per line, 123 lines); my crude autocorr track: 3239/6446 frames voiced, median 160 Hz.
- Whisper re-pass: faster-whisper base, `~/workspace/fw-venv`, word timestamps, numpy-array input (file-path decode is broken in both installed faster-whisper copies — PyAV `metadata_errors` mismatch; see re-pass section).
- Motif counts: Python `collections.Counter` on SONG_WORDS line texts; rhyme key = last two letters of line-final word.

## REVISIT — Independent Whisper base re-pass (2026-11-05 ~14:35 EST)

A fresh, unprompted faster-whisper **base** run on `work/gemini/song_16k.wav` (word timestamps, language en, prob 1.0; numpy-array input — see the tooling note in the measurement log). Saved: `/tmp/mv5_whisper_revisit.json` (86 segments, **525 words** vs SONG_WORDS 546). This pass was run *after* the v1 and Gemini passes, with no prompt and no lyric sheet, so it is an independent witness. Its verdicts:

### What it heard [MEASURED]

- **It heard ZERO occurrences of the word "easy" in 206 seconds.** Count of "easy": 0. Count of "now": 2. The hook line "Easy now, easy now" is rendered 28 times as the consecutive pair **"is it"**, and in the Final Chorus as **"he's an out"**. The refrain — the most-repeated line in the song, 30 occurrences — is the *least intelligible* line in the song to this recogniser.
- **It drops the entire opening.** First heard word: "Blue" at **30.00s** (prob 0.061 — barely confident). The whole intro (I01–I09, 0–22s, 52 words) plus the first two Verse 1 lines are absent. The v1 SONG_WORDS intro timings (built from targeted re-decodes + the lyric video) are *not* corroborated by this pass — but they are not contradicted either: the pass simply hears nothing there. The intro is sung quietly and/or with heavy stylisation over the backing.
- **Repeat-collapse confirmed independently.** "I gotta go there" (C1 tail) and "I'm falling" (C2 tail) are both rendered as **"I've got a feeling that I've got"** — the same hallucinated substitution in both places. Gemini dropped those lines entirely; Whisper invents a replacement for them. Both failure modes point the same way: the tails are real, repeated, low-salience singing that ASR cannot hold onto. The v1 readings (from targeted re-decodes) stand, but they stand on thinner evidence than the verse lines.
- **Word-level confirmations [MEASURED]:** "heart" → heard as "hard" (L80, matches Gemini's "Hard in the breeze" — the performed vowel is ambiguous; v1's "heart" stands on sheet + Whisper [confirmed]); "move" → "moves" (L81, final /z/ added by ASR as usual); "Ice cup sweating" → "ice, ice, cups, swimming" (L45, Gemini tripled "ice" the same way — the line is fast and the cup is pluralised by both systems; v1 stands on sheet + Whisper); "hard week fade" → "heart be safe" (L16/L54 — the "hard/heart" confusable, twice); "posted up right here" → "posted off right here" (L07, "up"/"off" confusable); "nodded" → "knotted"; "boombox" → "ballad"; "sleeve and spun" → "sleevers but"; "loud" → "last"; "crowd" → "cross".
- **Sequence alignment vs SONG_WORDS:** difflib ratio 0.563; 301/544 reference words in equal blocks. The low ratio is dominated by the systematic "easy now" → "is it" substitution (30 lines × 4 words) — it is not a sign that the verses disagree. Where the verses are concerned, the two passes agree line-for-line on the *words that are actually enunciated*.
- **The tail, corroborated twice [MEASURED]:** the last 12 Whisper words are "we fight, we fight, **Till the morning comes** (201.38–203.76, 'morning'/'comes' prob 0.99), **Till the morning comes** (203.76–205.56, prob 0.99)". Two clean consecutive occurrences, back to back, ending at 205.56s — 0.4s before the fade. Gemini heard the same double. **This is now two independent systems hearing the tail twice.** The v1 single reading for L110 ("Till the morning comes" once, CAT) is the odd one out. The intro echo-tail precedent (v1 Key Finding 2b) makes a real double plausible. **The tail question is no longer "is it doubled" — it is "who sings the second one, and at what exact times".** The app's word-level output (Stage D) or an ear check on 201–206s is the decider. Note the first "Till" in each occurrence carries low probability (0.32 / 0.245) — consistent with a held or echoed "Till" — while "the morning comes" is high-confidence both times.

### What the re-pass means for the video [INFERRED]

- **The hook must be carried by the picture, not the audio alone.** If a machine listener hears "is it" 28 times where the song says "easy now", a human viewer watching without captions may hear something similarly blurred. The refrain's *meaning* lives in the mouth and the staging: the open "o" of "now", the lean-in on "Easy", the alternation of faces. Shoot the refrain BIG — close, frontal, mouths open — or the hook will wash out the way it washed out for Whisper.
- **The intro is the quietest, least intelligible block.** Do not put plot-critical information in the intro's words — the audience will not catch them on first hearing. The intro's job is mood and faces, not story.
- **The tails are the song's soft spots.** Both tails (C1 "I gotta go there", C2 "I'm falling") are where ASR fails. Staging-wise, those are the places to give the singers their clearest, most frontal mouths — or to accept montage cover there, as v1 already does in places. Do not bury a tail line under a busy background.
