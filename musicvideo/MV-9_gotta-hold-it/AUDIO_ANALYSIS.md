# MV-9 "Gotta hold it" — AUDIO ANALYSIS (measured, 2026-11-09)

User order 2026-11-09: "MUST BE ANALYZING THE AUDIO FOR THE TEMPO AND ENERGY
NOTES — THIS IS NEEDED TO MAKE THE MUSIC VIDEO MATCH." This file is that
analysis. Measured from the delivered track, never from the prompt alone.

## Source
- `track.mp4` — Suno export, md5 `bad11958165dea267592643f185a15f8`
- Duration **184.0 s** (ffprobe). 231 words transcribed. First word 14.18 s
  ("The"), last word 181.92 s ("it"). Outro cuts clean at 184.0 s.
- Method: ffmpeg extract to 16 kHz mono wav; faster-whisper `small`, int8,
  NO VAD (VAD filter blanked the vocal — 0–1 words with it, 231 without);
  tempo/energy via numpy/scipy spectral-flux onset envelope (STFT 1024/128
  hop = 8 ms), autocorrelation + inter-onset-interval histogram + phase
  search. Word times in `analysis/SONG_WORDS.json`.

## TEMPO — measured 133 BPM (stated 128)
- Suno prompt states 128 BPM. The audio measures faster:
  - Autocorrelation scan (90–160 BPM): best **133.0 BPM** (ac 0.677) vs
    0.357 at 128 BPM.
  - Inter-onset-interval histogram of the 300 strongest onsets:
    dominant peak **0.44–0.45 s** (119 counts); the 0.47 s bin (128 BPM)
    does not appear in the top 6. 8th-note peak 0.21–0.23 s.
  - Phase search (total onset strength at beat positions): 133 BPM
    scores 49.6 vs 43.2 at 128 BPM.
- **Working grid: 133 BPM, period 0.451 s, phase 0.200 s.**
  Beats at 0.200 + k × 0.451 s. Re-verify against downbeats at assembly;
  if the grid drifts against the master, the measured grid wins over the
  prompt value — the song is the tempo gospel, the prompt is not.
- "Hold it" chant spacing (chorus 1): median 1.01 s between "hold"
  onsets = one chant word every 2 beats at 133 BPM (2 × 0.451 = 0.90 s,
  singer timing varies). Final-chorus chant median 0.88 s.

## ENERGY — final chorus is the peak
- Mean RMS **−18.0 dB** (0.5 s windows). Loudest 2 s: **170 s, −14.2 dB**
  (final chorus). Quietest 2 s: **182 s, −25.6 dB** (outro tail).
- Intro 0–14 s (brass stab cold open, no words): **−21.2 dB** mean.
  Last 10 s mean −19.2 dB.
- Energy shape: quiet intro → verses mid → choruses hot → bridge dips
  (the "Four squares left" half-bar silence is a real hole in the
  track, use it) → **final chorus 120.86–172.68 s is the loudest
  stretch of the song** → outro falls away and cuts clean.
- Visual peak goes in the FINAL chorus (Slopcannon banger test), not
  chorus 1.

## SECTION ENERGY NOTES (for the scene plan)
- Intro 0–14.18 s: single brass stab, no words. Cold open — one image,
  one stab, hold.
- Verse 1 + Pre-Chorus 1, 14.18–29.02 s: mid energy, slap bass under.
- Chorus 1, 29.02–~57 s: hot, group chant. "Hold it" chant is the
  repeatable motif.
- Verse 2, ~66–70.80 s: short, tight ("Door is open now" 66.28 s).
  Gap ~57–66 s before it is instrumental — cover with montage.
- Pre-Chorus 2, 73.10–85.28 s: "Lock the plastic door" 73.10 s.
- Chorus 2, 86.80–~100 s: hot again ("Need to go" 86.80 s).
- Bridge, 102.16–115.76 s: "Four squares left" 102.16 s, "QR code on
  the phone" ~104–107 s, "Soap and water free" 109.36 s. THE hole in
  the song — the half-bar silence after "Four squares left" is the
  hinge of the whole two-video design. Let the picture go hazy here.
- Instrumental gap 115.76–120.86 s (5.1 s, no words): breath before
  the final chorus. Do not fill with a singing take.
- Final Chorus, 120.86–172.68 s: loudest section. "Four squares /
  QR code / Ninety nine (Pay)" tail at ~158–172 s ("four" 158.20 s).
- Outro, 172.68–184.0 s: "Need to go / Hold it" 178.64–182.34 s, then
  cut clean. Last frame rhymes with the first (the line / the box).

## ASR caveats
- "line" heard as "light" in verse 1 ("in the light"); "portal" for
  "porta"; "I've extended near" for "Addicts standing near". Sheet is
  the lyric record; ASR is the timing record. Where they differ, the
  sheet's word is captioned on ASR's time.
