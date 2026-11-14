# MV-13 AUDIO ANALYSIS — "Movin' On Newton"

- Track: `track.mp4` — 185.600s, md5 `cc08e5b469ec6edc9352d0e2d67eaf9c`, Suno mp4 (vertical 824×1464), AAC. 16k mono wav at `work/track_16k.wav`.
- Method: `analysis/analyze_tempo_energy.py` — spectral-flux onset envelope + autocorrelation + IOI + phase search (same method as MV-9/10/11/12). Re-run 2026-11-10 ~15:10 EST reproduces the intake measurement exactly.
- Dadaspec: `analysis/dadaspec.jpg` (1200×240, rendered from `work/track_16k.wav` via `analysis/dadaspec.py`).

## TEMPO — MEASURED (not claimed)

- Suno style claims **96 BPM — MEASURED plateau 95.0–97.0, all at 0.509 correlation; top pick 97.0 BPM** (period 0.619s, phase 0.250s).
- **Working grid: 97.0 BPM — 1 beat = 0.619s, 1 bar (4 beats) = 2.474s, 2 bars = 4.949s.**
- IOI peaks: 0.30s, 0.28s, **0.62s** — the 0.62s IOI matches the beat period, confirming the grid. The 0.28–0.30s peaks are the 8th-note subdivisions (the barked ad-libs ride the off-beats).
- The claimed 96 sits inside the measured plateau — this is one of the rare tracks where the prompt BPM is honest. Plan on 97.0 anyway (the measured top pick); a 1 BPM difference is 1.1s of drift over the full track, so the word times (not the grid) are the authority at assembly.

## ENERGY

- **Loudest 2s at 174s (−12.9 dB)** = final chorus / outro peak. **Quietest 2s at 2s (−24.6 dB)** = the intro pocket before the beat fully lands.
- 5s RMS curve: 0–40s quiet (−23.4 to −19.3 dB, intro + verse 1 building) · 45–140s mid (−18.7 to −16.3 dB, the working groove) · **145–185s peak zone (−15.3 to −13.6 dB, final chorus + outro — the loudest stretch of the track)**.
- Dadaspec read: dense vertical striping throughout (the 808/drum-machine pulse never lets up — no dead air anywhere); a darker pocket ~30s (pre-chorus breather); the final third runs redder/bass-heavier (the 808s get fatter as the track peaks). No silent gaps; the track is a continuous drive.
- **Plan implication:** the energy arc is a slow ramp, not a peak-and-release. The video must supply the dynamics the audio doesn't — the visual peak is saved for the final chorus (170–185s), and the montage density steps up with the energy: sparse in the intro/verse 1, full tilt from the first chorus, maximum in the final chorus.

## SECTION MAP (measured — `LYRIC_TIMELINE.md`, 394 words, large-v3-turbo)

| Section | Time | Notes |
|---|---|---|
| Intro | 0.00–19.91 | First word 1.84s (NOT a cold open — 1.84s lead-in). Intro call TWICE + "Come on!"; wordless pocket 8.16–11.78. |
| Verse 1 | 19.91–38.42 | 4 lines, ~2.5s each. The story verse. |
| Pre-Chorus 1 | 38.42–44.70 | "Newton looking / He can't clock it" ×2. |
| Chorus 1 | 44.70–64.22 | Hook ×3 + "Fourth law" chant. |
| Post-Chorus | 64.22–74.10 | "I'm moving" + "What?" ad-lib pile-up (more repeats in the audio than the sheet lists). |
| DMX Rap Breakdown | 74.10–99.88 | 10 barked lines. Montage-first, no lip-sync chase. |
| Verse 2 | 99.88–109.76 | 4 lines. Meta line: "I'm gone before they even press play on the song". |
| Pre-Chorus 2 | 109.76–114.58 | Same chant ("clock", never the ASR garble). |
| Chorus 2 | 114.58–134.14 | Hook ×3 + "Fourth law" chant (FOUR repeats heard). |
| Bridge | 134.14–154.10 | MOSTLY INSTRUMENTAL — wordless pockets 134.14–138.28 and 144.88–154.10; only "Fourth law" ×3 + "You can't measure this" are vocal. The visual span. |
| Chorus 3 (final) | 154.10–175.98 | Hook ×3 + chant (FOUR repeats). Loudest stretch, peak 174s. |
| Outro | 175.98–185.60 | "Fourth law" / "I'm moving" / "I'm movin'" / "I'm movein'". Last word ends 184.84. |

## FIRST WORD

- **First word at 1.84s** ("Yeah", p=0.249 — a soft first bark). The track opens with 1.84s of instrumental — the establishing runway MV-12 didn't have. First frame must already be moving, but it gets a full beat to arrive before the voice lands.
