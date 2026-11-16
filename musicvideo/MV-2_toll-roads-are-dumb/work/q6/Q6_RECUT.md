# MV-2 Q6 — RE-CUT RECORD (section boundaries + S25 place beat)

## Method + the headline finding
The brief's "worst today" numbers (C2/Bridge 2.51s late, Intro/V1 2.5s early,
V1/C1 + C1/V2 + V2/C2 1.5s early) are the **V2-grid** numbers from
MUSIC_VIDEO_LEDGER.md — they do NOT describe the v6 master. The v6 cutlist
was audited cut-by-cut against **SONG_WORDS_BASE.json** (measured word
times — the assembly's timing authority for captions and placement).
LYRIC_TIMELINE.md's section starts are bracket estimates (±2.5s; the doc
itself warns the bold highlight can lag the vocal ~1s) and they disagree
with the measured words at 5 of 7 boundaries. The master follows the
WORDS, not the timeline estimates.

Measured boundary truth (SONG_WORDS_BASE) vs v6's cuts:

| Boundary | Timeline est. | Measured words | v6 nearest cut | Error (words) | Q6 action |
|---|---|---|---|---|---|
| Intro/V1 | 12.5 | line 2 "seem." ends 13.36 | S01→filler 13.36 | 0.00 | NONE — already exact |
| V1/C1 | 51.5 | line 11 "Toll" onset 50.84 | filler→hook1 50.84 | 0.00 | NONE — already exact |
| C1/V2 | 91.5 | line 17 "Express" onset 93.10 (held "comin'." 90.7–93.1) | S08→S09 93.10 | 0.00 | NONE — already exact |
| V2/C2 | 121.5 | line 24 "quit." ends 121.76; line 25 "Toll" onsets 122.92 (silence 121.76–122.92) | filler 122.20 | 0.44 | Filler source switch AT 121.76 → 0.00 |
| C2/Bridge | 165.5 | line 31 "They" onset 165.34 | filler→S16 165.92 | 0.58 | Filler source switch AT 165.34 → 0.00 |
| Bridge/C-ext | 190.0 | line 37 "Toll" onset 194.80 ("the wrecks just come" runs 190.62–193.18) | filler→S20 194.80 | 0.00 | NONE — already exact |
| C-ext/Outro | 238.5 | line 45 "Yeah," onset 242.30 ("done." ends 238.82; silence 238.82–242.30) | filler→R11 242.30 | 0.00 | NONE — already exact |

Per-section boundary error after the re-cut (vs measured words): **0.00 on
all 7**. Worst before: 0.58 (C2/Bridge). The two changes are filler source
switches — a REAL picture change at the boundary (different take), not an
invisible same-take split.

## The two re-cut changes (in cutlist_v7.json)
1. **V2/C2 @121.76**: filler 120.22–122.20 (S09 warped tau 7.309–9.292)
   → 120.22–121.76 S09 warped tau 7.309–8.85 + 121.76–122.20 S23 t4 warped
   tau 1.94–2.38. New span verified: wordless (S23 warped words end 1.94),
   motion mean 1.11, near-dup run 1.
2. **C2/Bridge @165.34**: filler 164.36–165.92 (R4 warped tau 3.737–5.297)
   → 164.36–165.34 R4 warped tau 3.737–4.72 + 165.34–165.92 S23 t4 warped
   tau 2.40–2.98. New span verified: wordless, motion mean 0.61, run 1.

## S25 place-beat re-cut
- S25 t2 take frames read (2s/3s/4s/5s/6s): vocal ends take 2.18; hand on
  chest 2–3s; hand rises ~3.5s; ticket placed onto the mic stand ~4.5s;
  stepped back, ticket hanging on the stand, by 6s. The v6 cutlist SKIPS
  take tau 2.20–5.719 entirely — the place itself is never shown (the
  post-slot filler tau 7.619–10.0 shows only the stepped-back hold with
  the ticket already on the stand).
- Change: post-slot filler 253.06–255.44 (S25 t2 tau 7.619–10.0) →
  S25 t2 tau 3.34–5.72. The place lands at out ~254.2, just after line 47
  ends (253.06) as line 48's long mantra begins — the visual period at
  the end of the echo, exactly the v2 vehicle's staging ("only AFTER the
  last word does he place a blank paper toll ticket on the mic stand").
  New span verified: wordless (take words end 2.18), motion mean 3.98,
  near-dup run 1 (the gesture is very much alive).
- Pre-slot filler 249.18–251.08 (tau 5.719–7.619) UNCHANGED — no overlap
  with the new span (boundary at 5.719/5.72).
- OBSERVED (not fixed, out of scope): S25 t2 wears a white bowtie +
  orange-red pocket square, not the bible's BONE shirt + CADMIUM square.
  Pre-existing v2-era take drift; the re-cut reuses the same take.

## What was NOT changed (deliberate)
- No mouth clip was re-placed or re-warped. The S19/Bridge tail drift and
  the S08/S09 joint trade-off were examined and left as v6 placed them:
  moving them breaks a word alignment elsewhere. The re-cut moves CUT
  POINTS only, within the word-boundary rule.
- Vs LYRIC_TIMELINE.md's estimates alone, the residual "errors" are
  V1/C1 0.66, C1/V2 1.60, Bridge/C-ext 4.80 — all timeline-estimate
  artifacts, each explained by the measured words above. The master is
  gated on the measured words.

## Restage swaps (in cutlist_v7.json)
- S04a 34.56–41.30: mv2_s04a_q6_t1_warped.mp4, tau 0–8.38, factor 1.2433
  (was v6final warped, tau 0–8.423, factor 1.2497).
- S07 72.28–80.78: mv2_s07_q6_t2.mp4, tau 0–7.14, factor 0.84
  (was v6final t1, tau 0–8.18, factor 0.962).
- S21 205.20–214.44: mv2_s21_q6_t1.mp4, tau 0–8.34, factor 0.9026
  (was v6final t1, tau 0–8.14, factor 0.881).
All other clips identical to cutlist_v6.json. Total stays 6432 frames.
