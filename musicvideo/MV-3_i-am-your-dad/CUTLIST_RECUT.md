# MV-3 re-cut — CUTLIST_RECUT.md (stage 2)

Segment boundaries are UNCHANGED from the delivered cut (cuts on scene
boundaries, leader 0–2.82s = S01 frame 0 held, the one pre-word freeze).
Frame counts at 24fps; segment = next scene start − scene start (S39 runs
to 8516). Placement for every mouth scene: take trimmed at its first word,
placed at the segment start, so the take first word lands on the song first
word. Warp = whole-clip setpts factor (see MV3_RECUT_MEASUREMENTS.md for
the band-edge rule). Overshoot takes are trimmed by the segment cut;
deficits are covered by tail-loops (replay of the take's own post-line tail
video, moving, never a freeze). Captions: existing captions_16x9.ass /
captions_9x16.ass reused unchanged — they are already keyed to SONG word
times, and the master audio is unchanged, so they now match the mouth
better with no re-timing needed. 9:16 uses crops.json centroids as before.

| Scene | Seg frames | Take(s) | Trim (src start) | Warp | Cover flag | Fill note |
|---|---|---|---|---|---|---|
| LEADER | 68 | S01 frame 0 held | — | — | — | pre-first-word hold only |
| S01 | 156 | s01_t2 | 0.00 | 1.25 | grey | trim overshoot |
| S02 | 216 | s02_t2 | 0.00 | 1.25 | grey | trim overshoot |
| S03 | 332 | s03_t1 (cutaway) | 0.00 | 1.382 | cutaway, no words | exact fill |
| S04 | 105 | s04_t1 partial 0–4.40s | 0.00 | 1.0 | STRUCTURAL cover | exact fill |
| S05 | 84 | s05_t1 partial 0–3.50s | 0.00 | 1.0 | STRUCTURAL cover | exact fill |
| S06 | 194 | s06_t1 | 0.00 | 0.9309 | — | trim overshoot |
| S07 | 168 | s07_t1 | 0.00 | 0.80 | grey | trim overshoot; final word cut 0.15s by boundary (disclosed) |
| S08 | 180 | s08_t1 | 0.00 | 0.9806 | — | trim overshoot |
| S09 | 138 | s09_t1 | 0.00 | 0.80 | grey | trim overshoot |
| S10 | 190 | s10_t1 | 0.00 | 0.9247 | — | trim overshoot |
| S11 | 159 | s11_t2 | 0.00 | 0.80 | grey | trim overshoot |
| S12 | 186 | s12_t2 | 0.00 | 0.80 | grey | trim overshoot |
| S13 | 216 | s13_t1 | 0.00 | 1.1637 | — | trim overshoot |
| S14 | 222 | s14_t1 | 0.00 | 1.2287 | — | trim overshoot |
| S15 | 173 | s15_t1 | 0.72 (17f) | 0.9831 | — | lead-in trimmed; trim overshoot |
| S16 | 183 | s16_t1 | 0.00 | 0.8643 | — | trim overshoot |
| S17 | 137 | s17_t1 | 0.88 (21f) | 0.9885 | — | lead-in trimmed; trim overshoot |
| S18 | 169 | s18_t2 | 0.00 | 0.8234 | — | trim overshoot |
| S19 | 174 | s19_t1 | 0.00 | 0.8966 | — | trim overshoot |
| S20 | 157 | s20_t1 | 0.00 | 0.80 | grey | trim overshoot |
| S21 | 250 | s21_t2 | 0.00 | 1.0 | STRUCTURAL cover | 10f tail-loop |
| S22 | 193 | s22_t1 | 0.00 | 0.9063 | — | trim overshoot |
| S23 | 343 | s23_t2 | 0.00 | 1.25 | grey | 43f tail-loop |
| S24 | 293 | s24_t2 | 0.00 | 1.0 | STRUCTURAL cover | 53f tail-loop |
| S25 | 484 | s25_t1 + s25_t2 | 0.00 | 1.0 | STRUCTURAL cover | 28f tail-loop |
| S26 | 125 | s26_t1 | 0.00 | 0.8012 | — | trim overshoot |
| S27 | 237 | s27_t1 | 0.00 | 1.1471 | phrasing-gap disclosed | trim overshoot |
| S28 | 350 | s28_t3 | 0.00 | 1.25 | grey | 50f tail-loop |
| S29 | 143 | s29_t1 | 0.00 | 0.80 | grey | trim overshoot; final words past cut (disclosed) |
| S30 | 175 | s30_t3 | 0.00 | 1.0 | STRUCTURAL cover | trim overshoot |
| S31 | 244 | s31_t1 | 0.00 | 1.25 | MANTRA-SLICE cover | trim overshoot; repeats not matched (disclosed) |
| S32 | 240 | s32_t1 | 0.00 | 1.25 | MANTRA-SLICE cover | trim overshoot; repeats not matched (disclosed) |
| S33 | 223 | s33_t1 | 0.00 | 1.25 | MANTRA-SLICE cover | trim overshoot; repeats not matched (disclosed) |
| S34 | 214 | s34_t1 | 0.00 | 1.1453 | phrasing-gap disclosed | trim overshoot |
| S35 | 316 | s35_t1 + s35_t2 partial 0–4.18s | 0.00 | 1.0 | STRUCTURAL cover | exact fill |
| S36 | 293 | s36_t2 | 0.00 | 1.25 | grey + phrasing-gap disclosed | 23f tail-loop |
| S37 | 395 | s37_t1 bursts 0–5.82s @0.80 + hold 5.82–9.0s @1.0 ×3 + hold partial 55f | 0.00 | 0.80 / 1.0 | opening grey; remainder MONTAGE cover (hold loop, moving) | hold looped 3× + 55f partial; NO sung-burst replay |
| S38 | 144 | s38_t2 | 0.00 | 0.80 | grey | trim overshoot |
| S39 | 247 | s39_t1 | 0.00 | 1.0 | MONTAGE cover (whole slot) | 31f tail-loop |

## What changed vs the rejected cut (placement logic only)

- Usable takes: OLD w = 1.0 (tempo drift left in place) → NEW w = ratio
  (endpoints land exactly). This is the main fix: 14 scenes.
- Grey takes: OLD w = ratio/edge (residual pinned at band edge, e.g. S01
  1.088, mouth 1.24s early) → NEW w = band edge (S01 1.25, mouth 0.50s
  early). Every grey warp factor stays inside 0.80–1.25.
- S15/S17: OLD placed from take start (lead-in frames pushed the first
  word late) → NEW trimmed at the first word (first word on the song
  first word).
- S37: OLD replayed sung bursts to fill the slot → NEW hold-loop montage
  cover (no vocal footage reused at a different song position).
- S39: OLD single mantra + tail-loop presented as the slot → NEW same
  picture explicitly flagged montage cover (ratio 0.573, below the grey
  floor — no sync claim).
- S31–S33: OLD grey warps presented as takes → NEW explicitly mantra-slice
  cover (bursts paced to segment, repeats not matched).
- Unchanged: segment boundaries, leader hold, S03 slow-mo, structural
  treatments, captions (song-timed already), crops, bug, audio, frame
  count (8516).
