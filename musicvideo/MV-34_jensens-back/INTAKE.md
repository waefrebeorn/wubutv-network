# MV-34 INTAKE — "Jensen's Back"

Received: 2026-11-24T03:31:24Z (main chat, user msg 343fb9a6-9352-4f85-ab53-2c4adf706ed6) —
lyrics in the message body + the Suno lyric video file. **Intake completed 2026-11-24 by the
proactivity research stage**: the track arrived in the same message batch as MV-33's rococo
stills and was not acknowledged in the MV-33 reply; this packet closes that gap. No prepro or
firing has happened yet — that is the remaining step (see "Next" below).

## Files
- track.mp4 — Suno lyric video as delivered, md5 `4304e007ec6b9d7b94ff99116846f8f4`,
  2,417,296 B, 824×1464, 60.400 s, h264 + AAC. NEVER overwritten.
  (Original delivery: `~/workspace/user/files/C8FAF910-CBC9-4EBB-9306-B67C12CA7804-Jensen Huang is back.mp4`)
- track.mp3 — extracted master audio, md5 `bbdd4a637fc1e6ef5fc4ce0cdc8bbbde`, duration
  60.416 s (ffprobe). Sole master audio at assembly; muxed as AAC in the master.
- lyrics.txt — the user's chat text, VERBATIM. TEXT authority for QC/ASR/captions.
- AUDIO_ANALYSIS.md — measured tempo/energy (intake step done): **127.0 BPM**, beat period
  0.472 s, phase 0.390 s. Raw data: `analysis/tempo_energy_raw.json`.

## The song (user's lyric sheet is the whole brief — no separate style note was sent)
A 60-second news-cycle hype anthem about Jensen Huang's ouster-and-return: stepped out,
board said stay gone, stock fell, apology, "eleven days later" he's back and the stock is up
thirty percent. Structure: Verse 1 / Pre-Chorus / Chorus / Verse 2 / Pre-Chorus / Chorus /
Breakdown ("Eleven days / Then he's back" chant) / Final Chorus / Outro. At 60.4 s this is
the shortest MV track in the catalogue — plan ~10–12 scenes, one shot per sung line, chorus
occurrences each get their own take (no callback reuse within the build).

Story in plot order (for the scene plan): the empty office, lights off → boardroom verdict →
ticker falling, phones ringing → the apology → eleven days of waiting → the doors open, he
walks back in → ticker reverses, +30% → the wall portrait restored → breakdown chant as a
press-conference flash grid → final chorus as the full return. Trump/board-call verse stays
as reported speech in staging (phones, headlines as post-layer only — no generated text in takes).

## Identity carriage — Jensen Huang
- Shared-cast pack: `~/workspace/wubutv-network/musicvideo/shared-cast/jensen-huang/`
  (panel sheet + refs + REFS.md already harvested 2026-11-22).
- **MV-33's decisive telemetry applies directly**: panel-sheet conditioning went 0-for-4 in
  MV-33 while the single-image compact recipe went 8-for-8 on landed takes. Jensen scenes
  therefore fire on the **single-image compact recipe** (one approved still as first frame +
  short verbose affirmation paragraph, identity in text), NOT the panel sheet as conditioning.
  MV-29's fix1 also proved this pattern for Huang (text-carried, costume shorthand: black
  leather jacket is his silhouette — use it).
- BUFF PASS (msg 1001) applies as standing law: exaggeration in the body, face faithful.
  For this build the buff read is the triumphant return — broad, unbothered, crowd-loud —
  not the coal-mine booty staging; butt law (msg 939) is not in play (no such lyric beats).
- No-names practice in prompt text (description only), per standing refusal-learning law.

## Standing law carried into this build (do not re-derive)
- PACING LAW: median shot ≥2.5 s, sub-1 s ≤5% runtime and ≤8 total, sub-0.5 s zero except one
  named BLAM frame-hit, ≤15 segments per 30 s window, one shot per sung line. On a 60 s track
  that means ≤4 sub-1 s hits total and a median the plan must prove before firing.
- Warp: chunk-before-warp ladder; capped-QP renderer ONLY; warp-slope histogram pre-encode
  gate [0.50, 2.00]. Anchors from each take's own ASR; context-rhythm check on the 0.472 s
  beat grid / 0.236 s half-beat lattice (AUDIO_ANALYSIS.md).
- Transliteration prompting for sung lines; true sheet stays QC authority; ledger every fire.
- Master: ONE 16:9 house master, 1280×720 24 fps CRF 18 (size-differential proof, not SEI),
  AAC 48 k, faststart, ~ WuBu ~ corner bug, mov_text + BURNED-IN word-timed karaoke
  (house style). Chat copy ≤50 MB under a FRESH name. Delivered flag written by PARENT only.
- Nag migration (msg 765): when prepro starts, add MV-34 to the watch/kickstand/cannon/
  crosscheck project lists in the same pass.
- Sequencing: MV-33 is mid-production (20/30 keeps at last verified count, run 9+ chained).
  MV-34 prepro does not need to wait for MV-33 to finish — prepro is text/stills work — but
  volley firing shares the one generation budget/429 window with MV-33; fire MV-34 volleys
  only in MV-33's gaps or after it closes, never in parallel volleys.

## Next (remaining work, in order)
1. Word timeline: transcribe track.mp3 (Whisper large-v3-turbo timestamps + Rumble-2-Flash
   adjudication) → SONG_WORDS.json + LYRIC_TIMELINE.md.
2. Reference stack: generate/grade Jensen stills (boardroom, empty office, return walk,
   portrait wall) — stills-first adherence; stack approved before any fire.
3. Scene plan (~10–12 scenes in plot order) with pacing-gate proof, then volleys ≤6.
4. Nag-list migration in the same pass as step 3.

## Rights
User's own Suno track; Jensen Huang likeness carried under the user's standing cosplay/parody
direction for this series (he is a standing cast member since MV-29). Logged per intake protocol.
