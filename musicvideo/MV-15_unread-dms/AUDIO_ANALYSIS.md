# MV-15 "Unread DMs" — AUDIO ANALYSIS (Stage 1, measured)

Source: track.mp3 (md5 3a3cb5e82187bac054c32b763e5ebd71), 173.61s,
decoded from the delivered track.mp4 (md5 2f42d599debb6bd34708cb708a2ceffd).
Tools: c11_mir (SLERM C11 MIR core, sprint-4 build), flux peak-picking,
dadaspec (work/analysis/dadaspec.py run → track.jpg).

## Tempo — MEASURED 150.0 BPM (stated 152 is wrong by 2)

- c11_mir tempogram/autocorrelation: 147.5 BPM nominal (period 0.4068s,
  ac 0.540) — the DP's smoothed estimate.
- Flux autocorrelation (decisive): sharp peak at lag 25 hops = 0.4000s
  exactly, ac 0.538; neighbours fall symmetrically (0.384s → 0.400,
  0.416s → 0.278). DP beat grid: 425 beats, median IBI 0.4000s.
- **Working tempo: 150.0 BPM, beat period 0.400s, phase 0.360s.**
  Stated 152 BPM (period 0.3947s) does not fit the measured grid —
  same error class as MV-9 (133 vs 128) and MV-10 (108 vs 112).
- Half-time feel present: flux AC at 0.800s = 0.476 (75 BPM trap
  half-time under the 150 grid). Downbeats ride the 0.8s lattice in
  verses; choruses hit every 0.4s beat.

## Accent / onset map (the cut contract)

- 897 peak-picked accents from the mix flux (hop 16ms, work/analysis/
  ACCENT_MAP.json): S-tier 90 (top decile — the glitch/808 hits the
  edit MUST land on), A-tier 135, B-tier 224, C-tier 448.
- Density ≈ 5.2 accents/s — hyperpop stutter density. S-tier clusters:
  13.6–38.4 (chorus-1 chop breakdown + verse 1), 46.3–51.3 (chorus 2
  entry), 55.9–59.1, 62.3–77.3 (verse 2 / pre-chorus 2), 110.4–116.7
  (chorus 3), 124.2–143.0 (bridge/final build), 159.4–171.8 (outro run).
- Beat grid + per-beat RMS/loudness: work/analysis/c11_beats.json,
  c11_features.json (425 beats, per-beat features).

## Energy (per-second RMS, dB rel.)

- Cold open at full level from 0s (−20 dB rel.) — no intro ramp; the
  chorus IS the intro (matches the Suno prompt's cold-open note).
- Loudest sustained runs: 52–59s, 112–119s, 140–173s (final chorus +
  outro ride at −14/−15 dB rel.). Dips: 78–84s (−22, bridge entry
  breath), 24–25s, 6s. Dadaspec (track.jpg) shows continuous dense
  striping — no quiet passage longer than ~2s anywhere.

## Performed-words finding (directive 1 — CONFIRMED in chunk 0)

ASR (large-v3-turbo, house config) chunk 0 (0–60s) vs the sheet:
- Chorus 1 is LONGER performed than written: lines 1–2 as sheet, then
  a **chop breakdown (12.08–18.48s)**: "200 unread / 200 unread /
  I'm-I'm not opening it / I'm not opening it" — the sheet's line 3
  fragmented into pitch-shifted chops, then line 4 full.
- Pre-chorus 1 performed tail carries an EXTRA "Just mute it"
  (43.42–44.80s) beyond the sheet's 4 short lines.
- Verse ad-libs "(yeah) / (what) / (uh)" visible in the Suno lyric
  video at their line ends; ASR word list is the timing authority.
Full performed grid: LYRIC_TIMELINE.md + work/analysis/SONG_WORDS.json.
