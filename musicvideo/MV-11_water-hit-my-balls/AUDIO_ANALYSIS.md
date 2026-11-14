# MV-11 "Water hit my balls" — AUDIO ANALYSIS

Track: `track.mp4` — md5 `18273d7a593e623b720105df195bede2`, 172.42s, 824x1464 (9:16 Suno video), h264 + AAC 48k stereo. Suno style prompt in `suno_prompt.txt`; lyrics verbatim in `lyrics.txt`.
Analysis: `analysis/track_16k.wav` (16 kHz mono) → faster-whisper `small`, int8, CPU, **NO VAD**; tempo via spectral-flux onset envelope + autocorrelation + IOI histogram; energy via RMS windows. Method proven on MV-9/MV-10.

## Measured tempo: ~131 BPM (prompt states "midtempo" only — no BPM claim)

- Autocorrelation peak is FLAT across 129.5–131.5 BPM (all 0.68) — the chant's four-on-the-floor grid gives no single sharp peak.
- **Working grid: 131.5 BPM, period 0.456s, phase 0.070s.**
- Cross-check: IOI histogram peak 0.46s = 130.4 BPM; second IOI peak 0.22s (eighth-note grid).
- Uncertainty ±1 BPM; the beat grid is the hint layer, the measured word onsets are the anchors. Do NOT re-measure from the prompt.

## Energy

- **Loudest 2s: 158s (−14.1 dB)** — Final Hook, the track's peak.
- **Quietest 2s: 0s (−27.1 dB)** — cold open before the first stab.
- 5s curve (dB): 0s −24.7 · 5s −22.0 · 10s −21.0 · 15s −17.9 · 20s −17.4 · 25s −20.5 · 30s −17.0 · 35s −17.0 · 40s −17.4 · 45s −18.9 · 50s −16.7 · 55s −17.5 · 60s −17.4 · 65s −18.5 · 70s −17.8 · 75s −17.7 · 80s −17.5 · 85s −16.0 · 90s −15.9 · 95s −16.4 · 100s −17.8 · 105s −16.4 · 110s −16.5 · 115s −16.5 · 120s −17.1 · 125s −14.8 · 130s −15.2 · 135s −15.8 · 140s −17.6 · 145s −16.9 · 150s −15.7 · 155s −14.2 · 160s −15.0 · 165s −14.5.
- Read: hot throughout after the cold open; a dip at 25s (between hook phrases) and 45s (verse, thinner arrangement); sustained lift from 125s to the end (Drop → Final Hook is the loudest stretch).

## Dadaspec structure map (NEW — first use)

- Rendered with dadabots' `dadaspec.py` (MIT, pure numpy+Pillow): `analysis/track.jpg`, 1600x200, `--mels 100`. Bass red / mid green / high blue; per-band normalized; stereo mirrored about the centre line.
- What it shows: dense vertical stab texture wall-to-wall (brass stabs on every downbeat); a **dark vertical band at ~62% (~107s) = the Drop's half-bar silence**; the tail (125s→170s) stays saturated, fading only at the very last frames.
- Use: section boundaries + stab positions at a glance. It is a scanning thumbnail, not a measurement — word times below are the authority.

## Word timings (first pass, `analysis/SONG_WORDS.json` — 92 words)

- First word: "Water" **13.76s**. Last word in first pass: "balls" **101.78s**.
- **GAP: the full-clip decode blanked after ~102s.** The Drop + Final Hook + Outro (102–172s) produced zero words despite the loudest audio in the track sitting at 158s. Per the split-half rule this is NOT a no-line verdict — `analysis/recheck.py` re-transcribes 100–172s and 55–72s separately; results in `analysis/SONG_WORDS_RECHECK.json`.
- Whisper smear warning: in the rapid chant the model merges words into long spans — "balls" 72.34–76.68 (4.34s) and "hits" 78.34–82.78 (4.44s) are NOT held notes, they are timestamp smear across repeated chant hits. Treat those onsets as approximate; the swing/keyframe measurement on each take re-measures them.

## ASR → lyric correction map (1:1, documented)

| Heard (ASR) | Lyric | Time |
|---|---|---|
| "our" | "I" (When I poop it splashes) | 22.18s |
| "boss" | "balls" | 30.58s |
| "Dash" | "Splash" (Splash back on the balls) | 34.94s |
| "Sipping" | "Sitting" (Sitting on the toilet) | 45.18s |
| "done" (prob 0.179) | spurious tail artifact, NOT a lyric word | 29.04s |
| "Music" (prob 0.009) | Suno intro artifact, NOT a lyric word | 3.12s |

## Section boundaries (measured — see LYRIC_TIMELINE.md)

- Intro (cold open, one brass stab): 0–13.76
- Hook 1: 13.76–38.94
- Verse: 45.18–50.14 (gap 38.94–45.18 = brass/string hits, no vocal)
- Pre-Hook: 55.26–57.56 (gap 50.14–55.26 = building snare)
- Hook 2: 70.66–101.78 (gap 57.56–70.66 = instrumental, to confirm against recheck)
- Drop + Final Hook + Outro: 102–172.42 (word times from recheck)
