# MV-12 "Micro Soft (Lost the Bet)" — INTAKE

## Receipt (2026-11-10 ~07:31 EST)
- Track: user-supplied Suno video `B5ED466E-...-Micro Soft (Lost the Bet).mov`, copied to `track.mp4`
  - md5 `25cf688c8a2cc01d5769dedd02f76923`, 5,399,543 B, **114.2s**, h264 824x1464 (9:16 Suno video), AAC
  - 16kHz mono wav extracted to `work/track_16k.wav` (3,654,990 B)
- Lyrics: verbatim from the user's message, saved in `lyrics.txt` (Chorus x3, Post-Chorus, Verse 2, Pre-Chorus, Bridge, Outro)
- Suno style prompt: verbatim in `suno_prompt.txt` — Novelty Dance-Pop, claims **128 BPM**
- Reference photos (user-supplied, `work/stills/ref_*.jpg`) — era/costume reference ONLY, never reproduced as-is:
  - `ref_logo_timeline_7.jpg` — 7-logo timeline ('75 disco, '75-'87 blibbet, '87-'12 italic, '94-'02 + slogan, '06-'11, '11-'12, NEW four-square)
  - `ref_logo_timeline_4.jpg` — 4-logo timeline (1975 / 1987 / 1994 / 2012)
  - `ref_logo_1975_disco.jpg` — 1975 disco MICROSOFT wordmark
  - `ref_gates_young_desk.jpg`, `ref_gates_young_white.jpg`, `ref_gates_windows_box.jpg` — young Gates looks
  - `ref_jobs_young_redcollar.jpg`, `ref_jobs_bowtie_apple.jpg`, `ref_jobs_macintosh.jpg` — young Jobs looks

## Measured audio (REQUIRED intake step — never trust the prompt's BPM)
- **MEASURED 131.5 BPM** (prompt claims 128 — measurement wins, same pattern as MV-9/MV-10/MV-11)
- Period 0.456s, phase 0.250s. IOI peaks 0.22 / 0.46 / 0.44s
- Energy: loudest 2s at 100s (-14.2 dB), quietest at 16s (-22.6 dB)
- 5s curve: flat -15 to -18 dB throughout, loudest tail 95–110s (final chorus = peak)
- Dadaspec: `work/track_16k.jpg` (1600x200)
- Words: turbo transcription running (large-v3-turbo, fixed config, NO VAD) → `analysis/SONG_WORDS.json`

## Design spine (user direction, 2026-11-10 ~07:30 EST)
- **Humorous parody: the logo marching through its history eras + the bet joke.**
  Gates lost a bet to Jobs → had to name the company Micro Soft → Jobs laughs → now we all know the story/joke.
- **THE LOGO IS THE CARRY** — the era's logo appears in every scene while the world around it changes.
  1975 disco → 1987 blibbet → 1994 italic + slogans → 2012 four-square. The name never changes; everything else does.
- **MONTAGE-FIRST (standing rule from the MV-11 verdict):** more montage, more funnies, more stuff
  happening — NOT static vantage shots. Every scene carries multiple gags / cuts / worlds.
  The MV-11 single-toilet-bowl master was approved as slop but boring; montage density is now a QC dimension.
- **CONTINUITY METHOD applies** (last-frame → first-frame chaining, per-project reference stack,
  music-timed prompts, full-10s prompt plans, in-motion cuts only) — but the chain must serve
  MONTAGE, not one held world: fresh first frames for every cut, each lining up with the outgoing world.
- **Visual-first:** chant/gang-chant chorus = montage + kinetic type in post; singing lives in the world,
  never a talking head at the lens; fewer camera-facing singers.

## Parody boundary (recorded plainly)
- This is the user's OWN song naming real public figures (Bill Gates, Steve Jobs) and a real
  company's logo history. Treatment: FLAT BOLD 2D CARTOON caricatures (young Gates: sweater + glasses;
  young Jobs: bow tie + black suit) — never photoreal likenesses of the supplied photos.
- The logo is a POST-RENDERED graphic (exact era wordmarks, from the user's supplied references),
  never generated in-clip text — generated text garbles, and post is where precision lives.
- No licensed characters/plots/dialogue reproduced; no licensed-property build. This is user-directed
  parody of public figures + trademark history in the user's own song.

## Status
- Intake: track + lyrics + tempo/energy + dadaspec DONE. Turbo transcription RUNNING (background).
- Research agent RUNNING: logo history + Gates/Jobs lore + montage parody craft + better firing
  → `research/MV12_RESEARCH.md`
- Next: LYRIC_TIMELINE.md from measured words → scene plan (montage-first) → volley 1 (hook-first proof).
