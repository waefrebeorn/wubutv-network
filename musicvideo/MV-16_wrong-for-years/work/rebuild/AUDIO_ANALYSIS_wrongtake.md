# MV-16 "Wrong for Years" — AUDIO ANALYSIS (Stage 1, measured)

Source: track.mp3 (md5 57c4f13c3779ecf86c627d39c23273f9), 183.21s,
decoded from the delivered track.mp4 (md5 ff57f3211f8fb444eea96108a65d96ae,
AAC 48k stereo). Tools: c11_mir (SLERM C11 MIR core), flux
autocorrelation, peak-picked accent map, dadaspec (track.jpg).

## Tempo — MEASURED 150.0 BPM (no BPM was stated for this track)

- c11_mir tempogram/autocorrelation: 147.5 BPM nominal (period 0.4068s,
  ac 0.624) — the DP's smoothed estimate.
- Flux autocorrelation (decisive): sharp peak at lag 25 hops = 0.4000s
  exactly, ac 0.621; neighbours fall off (0.384s → 0.535, 0.416s →
  0.311). Second family at 0.784–0.800s (ac 0.585/0.517) = the
  two-beat/half-time feel; a 0.592s ridge (ac 0.486) is the verse
  groove's dotted figure, not a competing tempo.
- DP beat grid: 464 beats, median IBI 0.4000s exactly.
- **Working tempo: 150.0 BPM, beat period 0.400s, grid phase 0.208s.**
  Beat grid + downbeats (4/4): work/swing/beat_grid.json (458 beats).

## Accent / onset map (the cut contract)

- 692 peak-picked accents from the mix flux (hop 16ms,
  work/analysis/ACCENT_MAP.json): S-tier 114, A-tier 192, B-tier 241,
  C-tier 145 (tiers by flux percentile). Density ≈ 3.8 accents/s —
  sung pop density, far sparser than MV-15's hyperpop stutter; cuts
  ride word onsets + downbeats, accents punctuate.
- Per-beat features: work/analysis/c11_features.json (438 DP beats
  at floor 1.0).

## Energy (per-second RMS, dB rel.)

- The song BUILDS: chorus 1 is the quietest full section (0–10s mean
  −8.96 dB rel), verses climb (−6.5 → −5.2), chorus 3 / bridge sit
  ≈ −4, and the FINAL CHORUS is the loudest sustained passage of the
  song (150–170s at −1.58 / −1.95 dB rel) — the arrangement itself
  makes the final chorus the peak; the plan's density arc follows it.
- Dips (breath pockets): 47.9–48.9 (V1→PC1), 84.7–86.7 (POST→V2),
  128.7–130.3 (inside C3), 172.8–174.1 (FC→OUT), tail 180–183 falls
  to −7.0. Dadaspec (track.jpg) shows regular section striping with
  bright vertical hits on chorus entries.

## Performed-words findings (grid: LYRIC_TIMELINE.md, 97 lines, 354 ASR words)

- The performance tracks the sheet closely — no breakdown chops
  (unlike MV-15). Performed extras beyond the sheet, all measured:
  (1) "Hey! Hey!" shout closing chorus 1 (24.88–26.04);
  (2) backing vocalise inside chorus 2 — (oh-oh-oh) 59.84–60.62 and
  (oh-uh-oh) 65.84–67.22; (3) FINAL CHORUS doubles "Nobody stopped
  me" inside trios 1 and 2 (149.26–152.46, 155.68–158.98);
  (4) bridge carries a "(no,)" pickup at 135.58 into its second
  "Nobody stopped me"; (5) verse ad-libs (yeah)/(what)/(uh) all
  performed at their sheet positions except V1's "(uh)", which is
  not separately audible and is folded into its line's tail.
- Every chorus occurrence has its own measured span — no timing was
  copied across occurrences (C1 0.00–24.88, C2 54.10–77.90,
  C3 104.78–132.24, FC 145.08–172.84, all different shapes).
