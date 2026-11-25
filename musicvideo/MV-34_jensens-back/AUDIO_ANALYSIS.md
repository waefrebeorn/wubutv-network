# MV-34 AUDIO ANALYSIS — "Jensen's Back"

Tool: `~/workspace/wubumv/tools/tempo-energy/analyze_tempo_energy.py` (spectral-flux onset
envelope + autocorrelation; RMS energy), run 2026-11-24 on `work/track_16k.wav`
(16 kHz mono render of track.mp3). Local copy with PROJ repointed: `analysis/analyze_local.py`.
Raw JSON: `analysis/tempo_energy_raw.json`.

## Tempo / beat grid
- **Tempo: 127.0 BPM** (autocorrelation top candidate; tight plateau 125.0–127.0 all at
  r≈0.69 — a solid grid, not a coin-flip).
- Beat period **0.472 s**, grid phase **0.390 s** (first beat at t=0.390).
- ~128 beats across 60.416 s.
- IOI peaks: **0.46 s** (the beat) and **0.22–0.24 s** (eighth-note subdivision — word
  onsets will often sit on the half-beat; assembly's context-rhythm check uses the
  0.236 s half-beat lattice too).

## Energy arc (RMS, 5 s windows, dBFS)
- Range is tight: quietest 2 s at t=2 (−22.4 dB, the cold open), loudest 2 s at t=48
  (−17.4 dB, Final Chorus). This is a short, front-loaded hype track — no drops, no quiet verse.
- 0–10 s: −21.4 → −19.8 → −18.0 — Verse 1 ramps fast; the BLAM must be visual (frame 0
  already mid-story: the empty chair / dark office, lights coming back on).
- 10–30 s: −18.0 to −20.2 — Pre-Chorus + Chorus 1 plateau, slight sag at 30 s (Verse 2 entry).
- 35–50 s: −19.2 → −18.3 → **−17.6 / −17.6** — the build into the Breakdown and Final
  Chorus is the track's peak; the "Eleven days / Then he's back" chant sits on the loudest grid.
- 55–60 s: −18.2 — Outro ("He's back / He's back") eases off; end on the return, not the peak.
