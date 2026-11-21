# MV-4 CUTLIST — "This Time It's Real (Futurama is cancelled)"

Master: `masters/mv4_this_time_its_real_16x9.mp4` — 1280x720, 24fps, 5731 frames, 238.805s.
Audio: `track.mp3` (md5 d46af0ef2e5abfca97db16905d20fb7d) muxed untouched; all generated clip audio dropped.

## Placement method (WORD-SYNC, cross-check)

- Take word times measured with faster-whisper base (unprompted decode is the floor;
  prompted decode must agree — a prompted-only extra word is a false agreement).
- Per scene, a grid search over warp in [0.80, 1.25] x trim near the first word chose the
  placement maximizing words inside +/-0.50s of the song's word times, then median |offset|;
  first word within +/-0.30s; last-word end residual in [-0.75, +0.50]s.
- Where the grid did not beat the endpoint-anchored SPAN placement (trim at first word,
  warp = song span / take span) on band count, SPAN was kept (conservative default).
- Segment boundaries = next scene's song first-word time (cumulative rounding, sum 5731f).
- S03/S08 first-word onsets corrected by visual + RMS cross-check (mouth closed at 0.0s,
  open by 0.5s; RMS rise): S03 0.45s, S08 0.30s — Whisper back-filled both to 0.00 and
  the prompted decode overshot both to 1.06.
- S11 trimmed at first-delivery end (7.22s); the repeat tail is not used in its segment.
- S28/S30a/S30b are 0-word cutaways (w=1.0). S23/S25 are structural montages (see below).

## Per-scene placement

| Scene | Take | Warp | Trim (s) | Mode | Song span (s) | Words in +/-0.50s | Median |off| (s) | Max |off| (s) | Last-word end (s) |
|---|---|---|---|---|---|---|---|---|---|
| S01 | mv4_s01_t1 | 0.925 | 0.00 | SPAN | 0.00-7.70 | 8/15 | 0.214 | 1.30 | +0.00 |
| S02 | mv4_s02_t1 | 0.836 | 0.00 | SPAN | 7.70-15.32 | 9/16 | 0.345 | 0.73 | +0.00 |
| S03 | mv4_s03_t1 | 0.930 | 0.69 | GRID | 16.00-23.34 | 10/12 | 0.123 | 0.79 | -0.71 |
| S04 | mv4_s04_t1 | 0.940 | 0.00 | SPAN | 23.34-30.54 | 14/14 | 0.133 | 0.29 | +0.00 |
| S05 | mv4_s05_t1 | 0.910 | 0.72 | GRID | 32.36-39.72 | 14/14 | 0.113 | 0.50 | -0.14 |
| S06 | mv4_s06_t3 | 0.990 | 1.74 | GRID | 39.72-46.88 | 10/11 | 0.235 | 1.00 | -0.43 |
| S07 | mv4_s07_t1 | 0.900 | 0.22 | GRID | 46.88-54.20 | 12/14 | 0.295 | 0.74 | -0.75 |
| S08 | mv4_s08_t1 | 0.940 | 0.46 | GRID | 54.20-63.04 | 10/14 | 0.298 | 0.87 | -0.74 |
| S09 | mv4_s09_t1 | 0.810 | 0.00 | GRID | 64.82-72.04 | 13/13 | 0.106 | 0.42 | -0.48 |
| S10 | mv4_s10_t1 | 0.810 | 0.02 | GRID | 72.80-79.52 | 13/17 | 0.318 | 0.84 | -0.29 |
| S11 | mv4_s11_t1 | 1.000 | 0.08 | GRID | 79.52-86.96 | 15/15 | 0.060 | 0.50 | -0.30 |
| S12 | mv4_s12_t1 | 1.100 | 0.16 | GRID | 86.96-95.40 | 8/17 | 0.528 | 0.86 | -0.74 |
| S13 | mv4_s13_t1 | 0.890 | 0.00 | GRID | 95.40-103.36 | 14/14 | 0.189 | 0.50 | -0.20 |
| S14 | mv4_s14_t1 | 0.820 | 0.24 | GRID | 103.36-110.34 | 10/10 | 0.260 | 0.50 | -0.44 |
| S15 | mv4_s15_t1 | 0.820 | 0.20 | GRID | 110.34-117.96 | 11/14 | 0.199 | 0.64 | -0.75 |
| S16 | mv4_s16_t1 | 0.930 | 0.00 | GRID | 117.96-126.44 | 14/14 | 0.083 | 0.49 | -0.57 |
| S17 | mv4_s17_t1 | 0.850 | 0.00 | GRID | 126.44-133.82 | 13/13 | 0.050 | 0.36 | -0.70 |
| S18 | mv4_s18_t2 | 1.070 | 0.14 | GRID | 133.82-140.56 | 11/12 | 0.172 | 0.57 | -0.09 |
| S19 | mv4_s19_t1 | 0.880 | 0.08 | GRID | 140.56-147.86 | 13/13 | 0.119 | 0.44 | -0.61 |
| S20 | mv4_s20_t1 | 0.900 | 0.00 | GRID | 148.40-155.16 | 13/13 | 0.050 | 0.24 | -0.39 |
| S21 | mv4_s21_t1 | 0.930 | 0.04 | GRID | 158.76-166.54 | 13/14 | 0.187 | 0.63 | +0.50 |
| S22 | mv4_s22_t1 | 0.860 | 0.24 | GRID | 166.54-173.90 | 10/11 | 0.308 | 0.81 | -0.46 |
| S24 | mv4_s24_t1 | 0.900 | 0.12 | GRID | 181.24-187.46 | 9/10 | 0.244 | 0.67 | -0.68 |
| S26 | mv4_s26_t1 | 1.200 | 0.00 | SPAN | 194.06-198.38 | 1/4 | 0.876 | 1.15 | +0.00 |
| S27 | mv4_s27_t1 | 1.178 | 0.00 | SPAN | 198.38-204.72 | 3/4 | 0.185 | 0.69 | +0.00 |
| S29 | mv4_s29_t1 | 1.160 | 0.06 | GRID | 211.75-220.77 | 6/7 | 0.087 | 1.99 | +0.01 |

> S18 correction (parent verification 2026-11-05 ~05:15 EST): the shipped take is **t2** (cf81195d), not t1 — t1 was QC-rejected for a burned "WuBuTV." watermark. The encode script maps S18→t2, the master frame at 135s matches t2 (PSNR 18.6 vs 8.5 for t1) and shows no watermark. The fit numbers in this row were measured on t1's words (same vehicle line, same staging); the warp used (1.07) matches t2's QC ratio (1.06).

## Structural montages (not mouth-sung slots; captions carry the words)

### S23 (173.90-181.24, 176f) — "Good news, everyone (good news, everyone) / The ride is done (the ride is done)"
Fast-cut dance-floor montage from post-word tails. Every slice starts after the donor's
own segment use AND after the donor's last word (+1 frame); mouths closed, moving footage.

| # | Donor | Take frames | Length |
|---|---|---|---|
| | S13 | 215-240 | 25f |
| | S06 | 216-240 | 24f |
| | S14 | 210-239 | 29f |
| | S16 | 220-238 | 18f |
| | S24 | 190-216 | 26f |
| | S10 | 199-216 | 17f |
| | S07 | 201-216 | 15f |
| | S15 | 229-240 | 11f |
| | S17 | 209-216 | 7f |
| | S22 | 212-216 | 4f |

### S25 (188.24-194.06, 139f) — "Futurama's finished... / Futurama's finished..." (soft reprise)
Observation deck + ship window, contemplative, for the soft reprise.

| # | Donor | Take frames | Length |
|---|---|---|---|
| | S12 | 189-240 | 51f |
| | S26 | 87-175 | 88f |

## Tail-loop gap cover (post-line moving footage, never during words)

| Scene | Segment | Deficit | Loop source (take frames) |
|---|---|---|---|
| S08 | 54.20-64.82 | 40f | 195-240 |
| S09 | 64.82-72.80 | 16f | 193-216 |
| S11 | 79.52-86.96 | 8f | 229-240 |
| S19 | 140.56-148.40 | 1f | 212-216 |
| S20 | 148.40-158.76 | 54f | 153-216 |
| S28 | 205.09-211.75 | 16f | 126-144 |
| S30a | 220.77-229.00 | 6f | 184-192 |
| S30b | 229.00-238.805 | 19f | 195-216 |

Notes:
- S08/S20 deficits are the inter-scene no-word gaps (S09 first word 1.78s after S08's window
  ends; S21 first word 2.22s after S20's window ends, plus the 155.16-158.76 gap).
- S11's loop replays take frames 229-240 (post-second-delivery, mouth closed, held pose).
- S30b's loop covers the 238.03-238.805 outro tail (0.775s, music only).

## Disclosures (sync)

- S12 is the weakest sync scene (tempo drift: take fast-then-slow; 8/17 words inside
  +/-0.50s, median 0.528s). No single warp fixes a drifting take; the grid placement is
  the best single-warp compromise.
- S26 is weak (1/4 words inside +/-0.50s, median 0.876s): a 4-word slow line whose take is
  evenly spaced while the song back-loads the words. Kept at the SPAN warp 1.20.
- S29: the song repeats "Good news, everyone" twice (211.75-213.89 and 214.17-216.73) but
  the take sings it once (7 words vs 10). The single delivery is stretched across both
  repeats; the second repeat has no dedicated mouth (max paired-word offset 1.99s on the
  'For' that follows it). Disclosed, not a fail — the take is QC-passed against its vehicle,
  which listed the line once.
- S19: first-half words garbled in the take audio ("the old ones" renders as "the line like
  muscles"); the master audio carries the correct words. Placement is tight (13/13, median 0.119s).
- S08/S03 first-word onsets were corrected (see method note above); the grid trims place the
  true onsets within ~0.3s of the song's first words.
- Several scenes sit at the -0.75s last-word-end bound (S03, S07, S08, S12, S15, S17): the
  take's final word is short, so the mouth closes up to 0.75s before the song's held final
  note ends. The middle words are tight; the trade-off was chosen by the band objective.

