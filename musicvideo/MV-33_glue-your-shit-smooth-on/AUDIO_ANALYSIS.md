# MV-33 AUDIO ANALYSIS — "Glue Your Shit Smooth On, It Is Not Over"

Tool: `~/workspace/wubumv/tools/tempo-energy/analyze_tempo_energy.py` (spectral-flux onset
envelope + autocorrelation; RMS energy), run 2026-11-23 on `work/track_16k.wav`
(16 kHz mono render of track.mp3). Raw JSON: `analysis/tempo_energy_raw.json`.
Beat grid: `work/swing/beat_grid.json`.

## Tempo / beat grid
- **Tempo: 115.0 BPM** (autocorrelation top candidate, tied cluster 113.0–115.0 at
  r≈0.55 — a tight plateau, so the grid is solid, not a coin-flip).
- Beat period **0.522 s**, grid phase **0.270 s** (first beat at t=0.270).
- 379 beats across 197.611 s; meter read as 4/4 allemande (bar = 2.087 s).
- IOI peaks: **0.50 s** (the beat) and **0.24 s** (eighth-note subdivision — the
  harpsichord pluck figuration runs in eighths; word onsets will often sit on the
  half-beat, so assembly's context-rhythm check uses the 0.261 s half-beat lattice too).

## Energy arc (RMS, 5 s windows, dBFS)
- Overall level is remarkably even — a courtly dance mix, no drops: range −25.8 dB
  (quietest 2 s at t=16, mid-Intro) to −17.0 dB (loudest 2 s at t=166, Final Chorus).
- Intro (0–20 s): −22.5 → −20.2 → −20.4 → **−23.1** — the track actually *dips* at
  15–20 s (the "Pray, glue your shit smooth on" hush before Verse 1). The BLAM
  cannot ride loudness here; frame 0 carries it visually.
- Verse 1 / Call (20–50 s): −19.4 to −22.5, conversational level, slight sag at
  45–50 s (the Call's tail).
- Chorus 1 (55–80 s): lifts to −18.5 at 55–60 s, holds ≈−19.3 — first real plateau.
- Verse 2 / Call 2 (80–110 s): −18.9 to −21.4, dips at 95–105 s (canteen verse is
  the quietest sung stretch after the intro).
- Chorus 2 (110–130 s): −18.1 peak at 110–115 s, eases to −20.7.
- Breakdown (135–155 s): −19.9 → −18.6 — no energy collapse; the breakdown is a
  texture change (harpsichord/wig ritual), not a volume drop.
- Final Chorus (155–180 s): the loudest sustained stretch, −17.8 at 160–165 s,
  loudest 2 s of the track at t=166 (−17.0 dB) — the visual peak belongs here.
- Outro (180–197.6 s): sharp dip −24.3 at 180–185 s (first outro line lands almost
  alone), then back to ≈−19.5 for the closing hook — the heart-hands lands on the
  recovery, not the dip.

## Section energy read for the plan
| Section | Approx. span* | Energy | Plan consequence |
|---|---|---|---|
| Intro | 0–~20 s | low, dips | visual BLAM carries; short identity anchors |
| Verse 1 | ~20–45 s | mid | court-verdict story beats, 12–20 cuts/min |
| Call 1 | ~45–55 s | mid, sagging tail | summons beat; hold across the sag |
| Chorus 1 | ~55–80 s | first plateau | SMOOTHON ritual established; hook singer |
| Verse 2 | ~80–105 s | quiet-mid | canteen comedy, Dario cameo |
| Call 2 | ~105–112 s | mid | second summons, escalation staging |
| Chorus 2 | ~112–135 s | high | ritual escalates |
| Breakdown | ~135–157 s | mid-high, texture break | harpsichord / wig ritual, one unbroken feel |
| Final Chorus | ~157–180 s | **peak** | densest section, visual peak at ~166 s |
| Outro | ~180–197.6 s | dip then recovery | heart-hands finale on the recovery |

*Section spans are energy-informed estimates only — the binding boundaries are the
ASR line times in LYRIC_TIMELINE.md.
