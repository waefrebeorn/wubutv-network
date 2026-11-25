# MUSIC VIDEO LEDGER — MV-18 "What's a Sigma? ~Mom"

Track: `track.mp4` md5 `d94ec3d6c7cc0716e0ae882108fb3efc`, 157.600s;
`track.mp3` md5 `ca1ca7176e8e3117b27a0175818ed1bc`.
Performed grid: 46 lines (SONG_WORDS.json / grid_lines.json;
performance differs from the sheet — audio is authority).
Tempo: measured 156.25 BPM (c11_mir DP, median IBI 0.3840s),
684 accents. Cast: photoreal live-action lock — SON + MOM + AUNT
(refs in work/stills/stack/). 36 scenes, distinct event per slot.

## Masters

| Master | md5 | Status |
|---|---|---|
| mv18_whats_a_sigma_mom_16x9.mp4 (house) | 5e191983f10265d8606e2bf0c79023ee | 88,456,689 B, 3782f / 157.610s, 1280×720 24fps, AAC 48k, SEI crf=18.0, faststart — built 2026-11-14, pending parent delivery |
| mv18_whats_a_sigma_mom_16x9_chat.mp4 (chat copy) | bb0493380bba9f15ef3fb4fdb3f5ecae | 45,241,138 B (≤50 MB), 3782f, AAC copied — pending parent delivery |

## Gates (detail: GATE_LOG.md)
- Audio agreement vs track.mp3: global 0.99867, worst-10s 0.99800.
- Zero-still (pre-grain enumeration): PASS — worst near-dup run 0f.
- G7: every shipped sung take ≥0.909 (two "mum/mom" homophone-class
  scores; all others 1.0); wordless inserts pass on screened-empty ASR.
- Assembly: single pass; joined.mp4 probed at 3782f before the
  master encode. No superseded master exists for MV-18.

## Delivery flag
- **Flag file: `MV18_DELIVERED.flag`** (project root) — written ONLY
  by the parent agent after the parent gate + chat delivery. The
  build coordinators never write this flag and never commit.

## Build record
- 41 canonical takes on disk across pilot + 6 volleys + rerolls
  (plus one duplicate S19 t2 fire, disclosed in GATE_LOG item 12);
  36/36 scenes ship a KEEP
  take or a disclosed montage cover (S22; inserts at S04/S14/S26/S33
  whose sung vehicles were refused and never retried).
- Full verdicts: TAKE_HISTORY.md. Cut record: CUTLIST.md.
  Disclosures: GATE_LOG.md (12 items, incl. the five montage
  covers, 1.920×/1.944× warp extremes, S17 + S03 flags, S25 sync
  compromise, singer-staging note).
