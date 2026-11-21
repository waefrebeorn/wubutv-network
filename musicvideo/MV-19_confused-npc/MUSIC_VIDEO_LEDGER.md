# MUSIC VIDEO LEDGER — MV-19 "Confused NPC"

Track: `track.mp4` md5 `2f932873fd9e86d819afcee48c8f580a`, 153.600s;
`track.mp3` md5 `f134098b92a84d6df8fd072935cd2d87`.
Performed grid: 48 lines / 239 words (large-v3-turbo, no VAD;
performance differs from the sheet — audio is authority).
Tempo: measured 104.17 BPM (c11_mir DP, median IBI 0.5760s),
585 accents. Cast: photoreal live-action lock — KIT (sole singer)
+ JUN (never sings), one apartment held all video (refs in
work/stills/stack/). 40 scenes, distinct event per slot; design
family LOOP/RESET WORLD.

## Masters

| Master | md5 | Status |
|---|---|---|
| mv19_confused_npc_16x9.mp4 (house) | 42877939fa568a630e1dee9ac6a0ceea | 81,033,983 B, 3686f / 153.600s, 1280×720 24fps, AAC 48k, SEI crf=18.0, faststart — built 2026-11-14, pending parent delivery |
| mv19_confused_npc_chat.mp4 (chat copy) | b56d551f37b433771659b991190a7ee5 | 46,105,391 B (≤50 MB), 3686f, AAC copied — pending parent delivery |

## Gates (detail: GATE_LOG.md)
- Audio agreement vs track.mp3: global 0.99927, worst-10s 0.99872.
- Zero-still (pre-grain enumeration): PASS — worst near-dup run 3f.
- G7: every shipped sung take ≥0.89 (S03 "open/opened"; all
  others 1.0); no hand-check overrides.
- Assembly: single pass; joined.mp4 probed at 3686f before the
  master encode. No superseded master exists for MV-19.
- Disclosed extremes: S08 word chunks 2.144×/2.016× (over the
  1.944× precedent); S36 head 0.414× (sub-floor, wordless);
  S34's poster carries a legible "closet" at pause scale.

## Delivery flag
- **Flag file: `MV19_DELIVERED.flag`** (project root) — written ONLY
  by the parent agent after the parent gate + chat delivery. The
  build coordinators never write this flag and never commit.
