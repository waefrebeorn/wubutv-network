# MV-22 "I Love Spaghetti" — GATE LOG (2026-11-20)

## DURATION DEFECT + FIX (found at delivery-closing pre-verify)
- First master (md5 f46404643bdd3143a75243b2409990da, 92,467,046 B) FAILED the
  duration gate: 185.250s / 4446f vs track 174.400s / 4186f (+10.85s, +260f),
  audio stream exactly 174.400s. NOT delivered; deleted.
- Root cause (one level deeper than the joined timestamps): the first segment
  build used filter order `fps=24, setpts=k*(PTS-STARTPTS)` — timestamps were
  scaled but frames were never resampled, and `-frames:v n` then truncated
  each warped segment to its first n source frames. Consequences: (a) joined
  .mp4 carried 4186 frames on a 185.207s timestamp timeline (~22.6fps
  effective, ~6% slow against the song); (b) warped segments' CONTENT spans
  were wrong (e.g. S10 k=0.513 held only 3.83s of its 7.48s sung delivery).
  Flattening joined's timestamps alone would have fixed (a) but shipped (b),
  so the fix was made at the segment level.
- Fix: build_master.py rewritten — `setpts=k*(PTS-STARTPTS)` FIRST (warp the
  timeline), then `fps=24` resamples the warped timeline to uniform 24fps;
  per-segment assertions added (exact frame count AND duration = frames/24,
  all 41 parts pass). All segments rebuilt in ONE pass (the S09/S12/S16
  timeline-span corrections folded into the plan). Rebuilt joined.mp4
  re-probed: 4186 frames, stream duration 174.416s ✓. Warp content
  spot-verified by eye on seg_10_0 (worst warp): frames at output 0.2/1.9/3.6s
  map to source ~0.4/~3.7/~7.0s — the full delivery arc is present.
- Master re-encoded in a single pass from the fixed joined.mp4 and re-probed
  end to end (below). Fixed master md5 9f7588cce077dafc00e0e8770c70fceb
  (≠ the bad master's md5 ✓).

## MASTER GATES — fixed master
- Spec probe: h264 1280×720, 24fps, **4186 frames counted**, video duration
  174.416667s; AAC LC 48kHz, 174.400s (= track exactly); mov_text, 63 cues;
  format duration 174.416667s; faststart. Rounding: round(174.400×24) = 4186f
  = 174.417s, +0.017s inside the wordless outro tail. **PASS**
- CRF-18 proof (size differential; SEI string never cited — this VM's x264
  always stamps crf=23.0): master video stream 85,347,694 B vs same-chain
  CRF-23 encode 46,910,003 B = **1.819×**. **PASS** (MV-25 reference: 1.85×)
- freezedetect (n=−50dB, d=1.5s) over the full master: **ZERO events. PASS**
- Onset frames eye-read (onset +0.15s): L01 lid raised, mouth open mid-word;
  L02 mouth open while plating; hook L14 belting, mouth wide; L17 singing at
  the table; breakdown S17 sub-cut on the tong-lift; L51 transitional open;
  L57 peak fork-twirl, mouth open, room twirling; final frame = held smile at
  the pot (bookend). **PASS** (standing limit below applies)
- Corner bug: "~ WuBu ~" gold, bottom-right, reads exactly "~ WuBu ~" on all
  10 sampled frames (head/mid/tail). **PASS**
- First frame: steaming pot on the flame, steam already moving (head cover).
  **PASS**

## TAKE GATES (detail in TAKE_HISTORY.md)
- 25/25 scenes shipped; spend 28/40 generations; refusals 0; 429s 0.
- G7 wrong-lyric: 1.00 (screened or hand-check override) on every shipped
  singing take except S06 (0.929 — see flaws). Hand-check overrides, all
  verified in raw ASR: S04 "stable"→"table"/"so"; S11 "Penne"→"Bene" (the
  documented L24 quirk); S09 "with" p=0.386; repeated-line nouns at
  p≈0.47–0.49 in S07/S08/S14/S15/S20/S21 (screening hides p<0.5 words; every
  one was actually sung).
- Motion law: every take's max near-dup run = 0.0s; mean diffs 12.09–32.89.
  All cuts land on frames already moving. **PASS**
- Adults only: every shipped take eye-checked; no apparent minors in any
  shipped take. **PASS**
- Rejected takes (kept): S01 t1 (line sprawl + repeated final "good"),
  S04 t2 (same sprawl as t1, no gain — t1 shipped), S10 t1 (L22 repeated,
  "Delicious" dropped).
- Wordless covers: S02, S18, S19 + S01/S06/S13/S24 wordless tails cover the
  song's own instrumental spans (5.44–14.72, 39.88–41.68, 81.86–83.66,
  107.86–124.24, 157.52–162.54). No lyric window is covered wordlessly;
  no generator refusal occurred (contrast MV-25's hook refusals).

## DISCLOSED FLAWS
- Grey-zone phrase warps (outside 0.80–1.25, smooth phrase-level): S01
  k=0.613, S04 k=0.640, S08 k=0.765, S10 k=0.513 (extreme — 1.95× speedup;
  word-perfect take that drawled; internal drift ≤0.35s), S12 k=0.686,
  S15 k=0.672, S20 k=0.735, S25 k=1.351.
- Wordless-span stretches: S01 head cover slowed ×1.470 (steam/stride);
  S06 tail at exactly the 0.5× speed floor (k=2.0, held smile + steam);
  S13 tail k=1.607; S24 tail k=1.768 (candlelit lean-in).
- S02: small equipment brand badge on the pasta machine; assembly uses take
  0.30–6.92 where it stays small; still faintly present.
- S06: the interjection "Yum" (L12) is not audible in the take ASR (screened
  G7 0.929; all content words sung).
- S09/S16: takes sing 2 of the song's 3 "yeah"s in L21/L41; the third "yeah"
  span is covered by the same stretched mouth motion under the phrase warp.
- S07: small blurred wall pictures in the dining-room background; no legible
  text (nit).
- Standing honest limit (all MVs): mouth events may lag song onsets by a few
  tenths on some lines; no phoneme-accurate lipsync is claimed — directional
  mouth movement occupying the described window.
