# MV-18 "What's a Sigma? ~Mom" — AUDIO ANALYSIS (intake, measured)

Track: track.mp3 (from track.mp4 md5 d94ec3d6c7cc0716e0ae882108fb3efc), 157.61s.

- **Tempo: 156.25 BPM** — c11_mir DP beat tracker: 415 beats, median IBI
  0.3840s; flux autocorrelation peak lag 0.3840s (ac 0.606) agrees.
  Half-time peak at 0.752s (ac 0.559). Beat period 0.384s, first beat 0.112s.
  (No BPM was stated with this track; this is the measurement of record.)
- Accents: 684 flux accents tiered S/A/B/C (work/analysis/ACCENT_MAP.json) —
  cuts and event peaks key to S/A accents.
- Energy (RMS dB rel, per 10s): verses sit ~-4.5 dB; choruses from ~40s
  lift to ~-2.7..-3.2 dB; bridge/outro ease back. Full per-second curve in
  work/analysis/analysis_summary.json.
- Performed word grid: faster-whisper large-v3-turbo int8, NO VAD,
  house lyrics config → work/analysis/SONG_WORDS.json (timing authority).
  Sheet text = text authority; grid lines built by aligning the sheet's
  line sequence to the ASR stream (work/analysis/grid_lines.json).
