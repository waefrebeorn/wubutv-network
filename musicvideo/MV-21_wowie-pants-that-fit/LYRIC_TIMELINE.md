# MV-21 STRUCTURE MAP (LYRIC_TIMELINE equivalent — instrumental piece)

Measured 2026-11-15 by coordinator from track.mp4 (md5 8d964491f7800c7e2625ea54e3cc227b).
Tools: c11_mir (beats + features), RMS curve (0.5s), vocal-band envelope (300–3400 Hz),
faster-whisper large-v3-turbo int8, NO VAD, word timestamps (numpy-input route).

## Grid
- Duration: 131.605s. Master: **3159 frames @24fps = 131.625s** (audio padded ≤20ms at tail, capped).
- Tempo: c11_mir DP tempo 183.0 BPM (period 0.3279s, phase 0.14s, ac 0.666) [confirmed as DP grid];
  musical pulse = half-time 91.5 BPM (bar ≈ 2.623s). 282 DP beats kept after floor 1.0.
- Cuts ride DP beats / flux peaks; section-boundary picture leads the downbeat by 2–6f (house law).

## Sections [confirmed by RMS + vocal envelope]
| Section | Time | Frames | Energy read |
|---|---|---|---|
| A DAWN | 0.00–24.80 | 0–595 | near-silence 0–2.2s, gentle wash builds RMS 0.03→0.08; wisps only |
| B STANDING | 24.80–55.00 | 595–1320 | lift at 25.0s (RMS 0.132); vocal swells 36.7–42.9, 47.2–53.2; flux peaks 47.4, 53.1 |
| C JOURNEY | 55.00–95.00 | 1320–2280 | full plateau RMS 0.13–0.19; densest flux cluster 56–95s |
| D COSMOS | 95.00–122.40 | 2280–2938 | peak sustain, vocal env 0.8–0.94 (max 113.1s) |
| E RETURN | 122.40–131.625 | 2938–3159 | decay 122→131.6 to silence; loop tail |

## The three "pants" vocalise hits [inferred — ASR + vocal envelope]
ASR hears only breathy "oh" phrases (the word "pants" is sung too breathily for ASR;
"Thank you" segments at 2.2s/34.8s are hallucinations on the wash — disregarded).
Three discrete vocalise phrase-groups, matching the sheet's (Ooh)/(Aah)/(Ooh) order:
- **HIT1 ≈ 61.32s** (f1471) — ASR oh-phrase 60.00–64.82, words p≤0.97, inside C.
- **HIT2 ≈ 94.22s** (f2261) — ASR oh-phrase 91.90–94.88, inside D entry.
- **HIT3 ≈ 121.42s** (f2914) — ASR oh-phrase 120.00–125.92, at D→E crest.
Each hit carries a peak visual event in the plan (portal dive / cosmos dive / homecoming fold).

## Flux peaks (assembly accent map, top)
42.98, 47.41, 52.13, 53.07, 54.96, 56.22, 57.18, 58.13, 62.53, 65.07, 67.58, 68.85,
70.11, 73.89, 75.17, 76.43, 77.70, 79.92, 80.85, 82.29, 83.25, 86.54, 87.81, 92.82, 95.36, 105.44.
