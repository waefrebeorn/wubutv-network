# MV-17 "Fridge Light Mystery" — AUDIO ANALYSIS (Stage 1, measured)

Source: track.mp3 (md5 99f73963080840a00415f36f7023236e), 162.816s
(track.mp4 md5 dd91534a68a14b2e1bdfd8d05481eb57, same duration).
Tools: c11_mir (SLERM C11 MIR core, built in work/analysis/c11mir),
flux autocorrelation, peak-picked accent map, per-second RMS.

## Tempo — MEASURED ~113.6 BPM (no BPM was stated for this track)

- c11_mir nominal: 112.0 BPM (period 0.5357s, tempo_ac 0.736).
- Flux autocorrelation (decisive): sharp peak at lag 0.5280s, ac 0.731
  → 113.64 BPM. Neighbours: 0.5120s → 0.429, 0.5440s → 0.542. The
  0.256–0.272s ridge (ac 0.60–0.64) is the eighth-note subdivision;
  the 0.784–0.800s ridge (ac 0.53–0.63) is the dotted/bar family.
- DP beat grid: 302 beats, median IBI 0.5280s exactly → 113.64 BPM.
- **Working tempo: period 0.528s, phase fitted from DP beats in
  work/swing/beat_grid.json.**

## Accent / onset map

- 621 peak-picked accents from the mix flux (hop 16ms,
  work/analysis/ACCENT_MAP.json): S-tier 101, A-tier 167, B-tier 230,
  C-tier 123. Density ≈ 3.8 accents/s — sung pop density; cuts ride
  word onsets + downbeats, accents punctuate.

## Energy (per-second RMS, dB rel.)

- The song BUILDS almost monotonically: verses sit −4.4…−3.1, first
  lift at 50–60s (−2.17, chorus 1 tail / verse 2), a breath dip at
  60–80s (−3.65/−3.90), then a steady climb: 100–120s at −1.74/−1.35,
  bridge pocket 120–130s (−2.69, min −5.38 — the quietest late dip),
  and the FINAL CHORUS is the loudest sustained passage (140–160s at
  −0.86/−1.03). Tail 160–162.8s falls to −4.06. The plan's density
  arc follows this build: the final chorus is the peak.

## Performed words

- Grid: LYRIC_TIMELINE.md (from SONG_WORDS.json, large-v3-turbo
  backbone, NO VAD) — see that file for line spans and any performed
  extras beyond the sheet.

## Performed words (filled after ASR)
271 words / 56 segments (large-v3-turbo, no VAD). First word 7.54s.
Choruses are PERFORMED CHOPPED (not the sheet's clean 5 lines): full hook
-> short hook fragments ("Why does it go off", "I check twice", "I check
once") -> full hook reprise. C3 is denser: hook x2 + fragments + hook.
Word-prob checks settled the sheet-vs-ASR conflicts IN FAVOUR OF THE
SHEET: PC1 "on" p=0.01, bridge "times/time" p=0.00, outro "run" — all
ASR garbles on fast repeats; caption text = sheet text everywhere.
Sheet ad-libs (yeah/what/uh) are NOT performed as distinct words — dropped
from the grid. Grid: 34 performed lines (build_grid.py, LYRIC_TIMELINE.md).
