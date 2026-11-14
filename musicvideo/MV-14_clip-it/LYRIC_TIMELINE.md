# MV-14 LYRIC TIMELINE — measured, never the sheet

- Track: `track.mp4`, md5 `f2226f24d846e3b31a9689189c2c4352`, **161.600s**
- Words: large-v3-turbo, fixed config, NO VAD — `analysis/SONG_WORDS.json` (**212 words**) + `analysis/SONG_WORDS.md`
- Beat grid: **92.0 BPM, period 0.649s, phase 0.240s.** 1 beat = 0.649s · 1 bar (4 beats) = 2.594s · 2 bars = 5.189s · 4 bars = 10.378s.
  Downbeats (bar starts) at 0.24 + k·2.594 (k=0,1,2…): 0.24, 2.83, 5.43, 8.02, 10.62, 13.21, 15.81, 18.40, 21.00, 23.59, 26.18, 28.78, 31.37, 33.97, 36.56, 39.16, 41.75, 44.34, 46.94, 49.53, 52.13, 54.72, 57.32, 59.91, 62.51, 65.10, 67.69, 70.29, 72.88, 75.48, 78.07, 80.67, 83.26, 85.86, 88.45, 91.04, 93.64, 96.23, 98.83, 101.42, 104.02, 106.61, 109.20, 111.80, 114.39, 116.99, 119.58, 122.18, 124.77, 127.37, 129.96, 132.55, 135.15, 137.74, 140.34, 142.93, 145.53, 148.12, 150.72, 153.31, 155.90, 158.50, 161.09.
- Energy: loudest 2s at 150s (−10.0 dB) = the wordless outro is LOUD, not a fade — the tail is a full-energy instrumental ride-out, plan the closing montage to it, don't taper. Quietest 2s at 0s (−30.3 dB). Energy climbs almost monotonically: −27.3 dB at 0s → −13.3 dB at 95s → −11.6 dB at 135s. Dip at 115s (−19.2 dB, inside the final chorus between pass 1 and pass 2) and a softer pocket at 100s (−15.8 dB, bridge open) — the bridge is the quietest sung section.
- ASR garbles to expect: chorus 1 hears "Trip it" for "Clip it" on ALL THREE passes (p 0.30 / 0.97 / 0.99 — the opening "Cl-" is swallowed by the beat); choruses 2–3 hear "Clip" correctly. "post it" → "posted" (chorus 1 pass 3, p 0.005); "help me stay online" → "Help" (p 0.013) in chorus 1 pass 2; "don't overthink" tail in chorus 2 pass 3 reads "Clip behind" / "Clip, post you" (p 0.008 / 0.0). The lyric sheet (`lyrics.txt`) is the authority for WORD IDENTITY; measured times are the authority for WHEN. Kinetic type must use the SHEET words, never the ASR garbles.
- HYBRID not needed: the full-clip turbo backbone heard every sheet section cleanly (212 words, no long dense span lost). No per-segment vocal pass required.
- Transcription done 2026-11-10 ~17:22 EST (exit 0, ~3m20s): this unblocks scene planning — the intake's one owed item.

## Sections (measured boundaries; [confirmed] = measured word times, [inferred] = section label from sheet)

| Section | Time | Words / notes |
|---|---|---|
| Intro (instrumental) | 0.00–14.14 | [confirmed] NO words for 14.14s — the longest lead-in of any MV so far. Cold open is instrumental: the establishing runway must already be moving (late-night desk, hard drive, hands). First word 14.14s. |
| Verse 1 | 14.14–34.56 | [confirmed] 4 lines, ~5s each. |
| Chorus 1 | 36.44–52.18 | [confirmed] 3 command passes + "Just find the moment" close. ASR garbles "Trip it" throughout — sheet is authority. Gap 34.56–36.44 (1.9s) before it. |
| Verse 2 | 55.90–76.54 | [confirmed] 4 lines, ~5s each. Gap 52.18–55.90 (3.7s) before it. |
| Chorus 2 | 77.78–95.24 | [confirmed] Same 3 passes + close, plus a real "No, no, no" tail 94.02–95.24 NOT in the sheet — ad-lib in the audio, plan a beat for it. Gap 76.54–77.78 (1.2s) before it. |
| Bridge | 98.50–108.76 | [confirmed] All 4 lines heard cleanly ("wanna" for "want to"). Gap 95.24–98.50 (3.3s) before it. Quietest sung section. |
| Final Chorus | 112.16–128.20 | [confirmed] Same 3 passes + close. Dip at 115s (−19.2 dB) between pass 1 and pass 2. Gap 108.76–112.16 (3.4s) before it. |
| Outro (instrumental) | 128.20–161.60 | [confirmed] 33.4s wordless — the longest tail of any MV. Loudest stretch of the track sits here (150s, −10.0 dB): a full-energy ride-out, not a fade. The closing montage lives here. See the tag verdict below. |

## Per-line times

### Intro — 0.00–14.14
| Line | Time | Notes |
|---|---|---|
| (instrumental lead-in) | 0.00–14.14 | 14.14s before the first word. The establishing runway — late night, the work, the hard drive. First frame must already be moving. |

### Verse 1 — 14.14–34.56 (the late nights)
| Line | Time | Notes |
|---|---|---|
| "I've been doing this for years" | 14.14–16.14 | "did" p=0.331 (soft). |
| "built it from the ground up" | 16.36–18.34 | |
| "you didn't watch the late nights" | 19.10–21.04 | |
| "you just saw the upload" | 21.46–23.32 | "upload" p=0.482 (soft tail). |
| "I don't need a parade" | 23.32–26.22 | "parade" p=0.247 (soft). |
| "I don't need a pitch" | 26.96–29.02 | |
| "I need somebody steady" | 29.02–31.64 | |
| "who can keep it moving" | 31.64–34.56 | "Who" p=0.827 — line break is ASR's; sheet runs it as one line. |

### Chorus 1 — 36.44–52.18 (the command chant)
| Line | Time | Notes |
|---|---|---|
| "Clip it / post it / keep the work alive" | 36.44–39.16 | ASR hears "Trip it" (p 0.302) — sheet is authority. |
| "Clip it / post it / help me stay online" | 41.26–44.58 | Gap 39.16–41.26 (2.1s). ASR "Help" p=0.013 for "help". |
| "Clip it / post it / don't overthink the cut" | 46.44–49.52 | ASR "posted" p=0.005 for "post it". |
| "Just find the moment / and put it up" | 49.52–52.18 | |

### Verse 2 — 55.90–76.54 (the hard drive)
| Line | Time | Notes |
|---|---|---|
| "There's a whole hard drive full of good seconds nobody saw" | 55.90–60.06 | |
| "me laughing at midnight" | 60.88–63.22 | |
| "me missing my own calls" | 63.22–65.56 | |
| "I'm not looking for magic" | 65.56–68.28 | |
| "just clean hands, clear eyes" | 68.46–70.74 | |
| "take what's already there and give it back with a title" | 70.74–76.54 | "title" lands 75.46–76.54. |

### Chorus 2 — 77.78–95.24
| Line | Time | Notes |
|---|---|---|
| "Clip it / post it / keep the work alive" | 77.78–80.94 | "Clip" heard correctly this time (p 0.679). |
| "Clip it / post it / help me stay online" | 83.32–86.24 | Gap 80.94–83.32 (2.4s). |
| "Clip it / post it / don't overthink the cut" | 86.24–91.34 | ASR garbles the pass ("Clip behind" p 0.008, "Clip, post you" p 0.0) — sheet is authority. |
| "Just find the moment / and put it up" | 91.34–94.02 | |
| "No, no, no" | 94.02–95.24 | NOT in the sheet — real ad-lib in the audio. |

### Bridge — 98.50–108.76 (tired of explaining)
| Line | Time | Notes |
|---|---|---|
| "I'm tired of explaining it" | 98.50–101.26 | |
| "tired of spelling it out" | 101.26–103.44 | |
| "if you want to help me" | 103.44–105.94 | ASR "wanna" for "want to". |
| "this is how you do it now" | 105.94–108.76 | "this" p=0.208 (soft). |

### Final Chorus — 112.16–128.20
| Line | Time | Notes |
|---|---|---|
| "Clip it / post it / keep the work alive" | 112.16–115.10 | |
| "Clip it / post it / help me stay online" | 115.10–120.56 | Dip at 115s (−19.2 dB) opens this pass; ASR garbles "Clip and post it" (p 0.0–0.2). |
| "Clip it / post it / don't overthink the cut" | 122.66–125.54 | Gap 120.56–122.66 (2.1s). ASR "Clip in" p=0.003. |
| "Just find the moment / and put it up" | 125.54–128.20 | Last lyric word "up" ends 128.20. |

### Outro — 128.20–161.60
| Line | Time | Notes |
|---|---|---|
| (instrumental ride-out) | 128.20–161.60 | 33.4s, no lyric words. Loudest stretch of the track (150s, −10.0 dB). The closing montage lives here — the cut, the title, the post, the work staying alive. |
| "We'll be right back." (?) | 153.50–153.60 | UNVERIFIED — four words in 0.10s total (each 0.02–0.04s, p 0.28–0.83), NOT in the sheet. Almost certainly an ASR hallucination on the instrumental tail, not real speech. Do NOT build a scene on it; verify by ear before assembly, and if unheard, treat the whole outro as wordless. |

## Planning notes (for the scene plan — the intake's next step)

- The song IS the brief: late nights → hard drive → hands → cut → title → post. The chorus is a command chant — montage + kinetic type, not lip-sync (same rule as MV-13's chant pile-ups).
- Structure is unusually clean: 14.1s instrumental open + 4 verse lines + 3 chorus passes, twice, + bridge + final chorus + 33.4s instrumental close. The two long wordless spans (open 14.1s, close 33.4s) are the montage bookends — nearly 30% of the track has no words.
- The intake's energy-dip guess is corrected: the dip at 115s is inside the final chorus, NOT the bridge; the bridge (98.50–108.76) is the quietest sung section but only modestly so (−15.8 dB at 100s).
- Density guide (MV-13 precedent, maximized per the test directive): choruses 1 bar/shot on hook lines + 2 beats/shot on chant pile-ups; verses 1 bar/shot; bridge slow by design; outro montage at 1–2 bars/shot riding the energy climb.
