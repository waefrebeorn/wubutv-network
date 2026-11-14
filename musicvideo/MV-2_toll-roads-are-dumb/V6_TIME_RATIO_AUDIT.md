# MV-2 v6 — time-ratio audit of rejected v5 (2026-11-02 21:06 EST)

User verdict on v5: words with no video, frozen motion, halted moments
from too-slow time splices. "Learn how to generate and reroll to get
the right time ratios." Verdict: REJECTED, ~50%, getting closer.

## Audit (from CUTLIST_V5.json, not from stills)

- Frozen picture: 49.56 s of 268.01 s = 18.5%
  (36.72 s pure freeze segments + 12.84 s frozen inside warped
  intervals via the >2.5x freeze branch, 13 intervals).
- Warped word intervals (270 total): 68 near natural (0.80–1.25x),
  74 slowed 1.25–2.5x, 83 sped 0.4–0.8x, 32 squeezed <0.4x,
  13 frozen (>2.5x). Only 25% of word intervals play near natural speed.
- Pure freeze segments: leader 0–4.44, holds at 14.10–18.82,
  34.82–40.58, 55.62–57.86, 82.46–86.98, 101.06–103.72,
  121.02–122.92, 184.12–186.56, 202.72–203.98, 215.26–216.06,
  236.32–242.30.

## Per-scene line ratios (song duration / take duration)

Worst, reroll first (PACING axis):
- S13 0.34x (take 5.40 s onto a 1.82 s song line)
- S23 0.42x, S10 0.46x, S05 0.47x, S16 0.51x
- S06 1.49x, R1-Pay 1.81x (stretched, then frozen)
- S08 1.41x, S18 1.41x, S15 1.32x, S07 1.22x, S14 1.27x

Near-1 scenes to keep as the model: S01 0.96x, S02 0.90x, S03 1.07x,
S04 0.97x, S11 0.92x, S12 0.97x, S24 0.95x, S25 0.97x, S27 1.02x.

## v6 rule (also in Slopcannon SKILL.md)

1. Ratio is measured at generation: line ratio must be 0.80–1.25 and
   no word interval may need warping outside that band.
2. Outside the band = reroll with PACING as the axis (sing the line
   faster/slower, shorten or split the vehicle line), one variable
   per reroll, max 6 per user message.
3. No freeze while words play. No setpts warp outside 0.80–1.25x.
4. Every song occurrence gets its own fresh take; reuse is retired
   as vocal coverage (Chorus 2 / extended-chorus repeats get new
   takes at their own song positions).
5. Motion QC on the delivered master across whole vocal segments:
   continuous frame-to-frame motion during words; any frozen run
   over ~0.5 s during words, or any noticeably slow/fast interval,
   is a fail and a reroll reason.
