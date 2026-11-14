# MV-2 v6 volley 1 — PACING rerolls (user order 2026-11-02 21:28 EST)

User verdict on v5 (21:06 EST): REJECTED — words with no video, frozen
motion, halted moments from too-slow time splices. Order: learn to
generate and reroll for the right time ratios. This volley fires on the
user's 21:28 EST tap ("Fire the first v6 reroll volley").

Rule (Slopcannon SKILL.md, v6 time-ratio rule): a take is usable only
if its line ratio (song line duration / take line duration) is
0.80–1.25 and no word interval needs warping outside that band.
Assembly may NOT warp, freeze, or squeeze a miss into place. A miss is
a generation miss: reroll with PACING as the single named axis.

## Scenes fired (6 = the cap for this user message)

All are SINGING, performance-window staged, flat cartoon, THE VOICE.
Each new vehicle copies its active vehicle verbatim except ONE change:
a PACING sentence stating the target vocal duration (first word to
last word). Nothing else changes — staging, setting, outfit, camera,
text stack all identical, so any ratio change is attributable to pacing.

| Scene | Active take | Take vocal | Song line | Target vocal | Old ratio | New take |
|-------|-------------|------------|-----------|--------------|-----------|----------|
| S13 "toll roads are dumb." (C2) | t2 | 5.10 s | 1.52 s (122.92–124.44) | ~1.5 s, brisk/clipped | 0.30x | t3 |
| S23 "toll roads are dumb." (C-ext mantra) | t1 | 3.74 s | 1.38 s (230.22–231.60) | ~1.4 s, brisk/clipped | 0.37x | t2 |
| S05 chorus "Toll roads are dumb." (C1) | t4 | 4.38 s | 1.92 s (50.84–52.76) | ~1.9 s, fast/clipped | 0.44x | t5 |
| S10 "speed up, cut over, somebody gets caught." (V2) | t1 | 7.22 s | 3.18 s (96.80–99.98) | ~3.2 s, brisk | 0.44x | t2 |
| S16 "sell you speed for a dollar and a dime." (Bridge) | t1 | 6.20 s | 3.02 s (165.92–168.94) | ~3.0 s, brisk | 0.49x | t2 |
| S08 "they just keep coming." (C1 tail) | t2 | 3.28 s | 4.62 s (88.48–93.10) | ~4.6 s, slow/held | 1.41x | t3 |

Vehicles: mv2_s13_vehicle_v6.txt, mv2_s23_vehicle_v6.txt,
mv2_s05_vehicle_v6.txt, mv2_s10_vehicle_v6.txt, mv2_s16_vehicle_v6.txt,
mv2_s08_vehicle_v6.txt.

## Explicitly NOT in this volley

- S06 (ratio 1.51x, song line 12.70 s): a single 10 s take CANNOT
  contain a 12.70 s vocal, so no pacing reroll can hit the band.
  S06 needs a split-line plan (two takes covering line halves, cut on
  a word boundary) — planned for the next volley, not faked here.
- S18 (1.41x, feasible) and the Chorus 2 / extended-chorus repeats
  (which need fresh takes at their own song positions under the v6
  no-reuse rule): next volleys, within the 6-per-message cap.
- S10's known profile-head nit and S16's staging are NOT fixed by
  this axis; if the new takes come back with those faults, they are
  flagged for a facing/staging reroll next, not hidden.

## After firing (gate before any assembly)

1. Transcribe each new take (fresh Whisper, same pipeline as v5) and
   measure its anchored vocal span; compute line ratio per scene.
2. QC 2s/5s/8s frames + motion: face-to-camera, mouth visible, no
   on-screen text, and continuous motion during the vocal (v6 motion
   gate — no stills-only pass).
3. A take that lands in 0.80–1.25 becomes the scene's candidate;
   a take still outside the band is a miss on the pacing axis and is
   NOT warped into the cut. Update VOLLEY_PROGRESS.md +
   TAKE_HISTORY.md before anything else is fired.
