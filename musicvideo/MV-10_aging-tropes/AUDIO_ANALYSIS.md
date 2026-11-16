# MV-10 "Aging tropes" — AUDIO ANALYSIS (measured, 2026-11-09)

User order 2026-11-09: "MUST BE ANALYZING THE AUDIO FOR THE TEMPO AND ENERGY
NOTES — THIS IS NEEDED TO MAKE THE MUSIC VIDEO MATCH." This file is that
analysis. Measured from the delivered track, never from the prompt alone.

## Source
- `track.mp4` — Suno export, md5 `fd60ac7335e3bdb55d97a2242dbee38c`
- Duration **178.0 s** (ffprobe). 277 words transcribed. First word 16.68 s
  ("Got"), last word 164.82 s ("stop"). ~13 s of hot outro music after
  the last word (ends 178.0 s).
- Method: ffmpeg extract to 16 kHz mono wav; faster-whisper `small`, int8,
  NO VAD (VAD filter blanked the vocal); tempo/energy via numpy/scipy
  spectral-flux onset envelope (STFT 1024/128 hop = 8 ms), autocorrelation
  + inter-onset-interval histogram + phase search. Word times in
  `analysis/SONG_WORDS.json`.

## TEMPO — measured ~108 BPM (stated 112)
- Suno prompt states 112 BPM. The audio measures a touch slower, and the
  funk groove makes the grid looser than MV-9's:
  - Autocorrelation scan (90–160 BPM): best **106.5 BPM** (ac 0.64) vs
    0.266 at 112 BPM.
  - Inter-onset-interval histogram of the 300 strongest onsets:
    dominant peak **0.27–0.28 s** (93 counts) — the 8th-note subdivision,
    implying a beat of 0.54–0.56 s = 107–111 BPM. Beat-bin peak
    0.55–0.56 s (38 counts). A secondary 0.42–0.43 s peak (28 counts)
    is the syncopated slap-bass / hook pattern, not the beat.
  - Phase search (total onset strength at beat positions): near-tie —
    112 BPM scores 27.1 vs 26.5 at 106.5 BPM.
- **Working grid: 108 BPM, period 0.556 s, phase 0.152 s.**
  Beats at 0.152 + k × 0.556 s. The ghost-note funk groove is syncopated:
  cuts should land on downbeats and hook onsets, not on every grid beat.
  Re-verify downbeats against the master at assembly; if the grid drifts,
  the measured grid wins over the prompt value.
- "Drink it" repeats (chorus tail): median spacing 0.50 s — rapid
  8th-note patter, a montage-volley section, not per-line singing.

## ENERGY — the outro is the loudest part
- Mean RMS **−18.0 dB** (0.5 s windows). Loudest 2 s: **175 s, −12.4 dB**
  (outro "Bop bee bop" tail). Quietest 2 s: **1.5 s, −28.4 dB** (cold intro).
- Intro 0–16.68 s: **−22.7 dB** mean. Last 10 s mean **−16.3 dB** — the
  outro runs HOT, not a fade. The last word is at 164.82 s but the track
  stays loud to 178 s: plan a visual climax in the outro tail, not a
  fade-out.
- Energy shape: quiet intro → verse 1 mid → pre-chorus lift ("It sucks
  to get old" — "sucks" 36.22 / 39.30 s) → chorus hot → verse 2 mid →
  chorus → bridge (the memory — "Four squares of TP" 113.86 s) → final
  chorus → **outro tail is the loudest stretch**. The peak is at the END,
  which breaks the usual "peak in the last chorus" shape: the final
  chorus + outro tail together are the climax.

## SECTION ENERGY NOTES (for the scene plan)
- Intro 0–16.68 s: cold, quiet, no words. One image: the old man, the
  bed, the water glass, night.
- Verse 1 + Pre-Chorus 1, 16.68–~44 s: mid, hushed close-mic lead.
  "Bend over for the doc" is ASR-garbled on first occurrence ("Been
  over for the duck") — sheet is the lyric record.
- Chorus 1, ~44–62.90 s: hot, call-and-response. "Soup tastes better
  now" 55.84 s; "drink it" patter to 62.90 s.
- Gap 62.90–66.94 s (4 s, no words).
- Verse 2, 66.94–87.88 s: "Standing up is slower" 66.94 s; "winded
  when I bend" ("bend" 70.44 s); "Soup is on the stove" 75.84 s;
  "it sucks to get old... bass don't quit" ("sucks" 80.12 / 82.52 s).
- Chorus 2, 89.18–106.40 s: "Soup tastes better now" 100.40 s.
- Gap 106.40–113.86 s (7.5 s, no words): the longest breath in the
  song — the memory starts here, not at the first bridge word.
- Bridge, 113.86–139.02 s: THE MEMORY. "Four squares of TP" 113.86 s,
  "Soap and water free" 120.66 s, "Addicts standing near (Outside)".
  Same objects, same framing as MV-9's bridge — older, dimmer, smeared.
- Final Chorus, 140.86–165.24 s: "Soup tastes better now" 142.90 s;
  "It sucks / But the pocket / Stays tight (Bop)" tail.
- Outro, 165.24–178.0 s: ~12.8 s, no words, HOTTEST part of the track.
  Visual climax: the memory resolves — the old man and the young man in
  one frame, or the QR code glowing on the nightstand. Last frame rhymes
  with the first (the water by the bed / the line).

## ASR caveats
- "Bop-bee-bop" is heard as "Pop" throughout (pop = bop normalization).
  "Prostate check" heard as "price state didn't check". "Bend over for
  the doc" first heard as "Been over for the duck". Sheet is the lyric
  record; ASR is the timing record.
