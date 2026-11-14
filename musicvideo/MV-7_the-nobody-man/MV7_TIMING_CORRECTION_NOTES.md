# MV-7 TIMING CORRECTION — 'I'm The Nobody Man'

User order 2026-11-06 ~21:29 EST ("work on the timing"), replying to the MV-7
delivery whose disclosed flaw was: mouths open on all 58 gated onsets, but the
visible mouth ran ~0.25s BEHIND the song onsets throughout. Method follows the
MV-3 correction precedent and the Slopcannon V4 CORRECTION bind: phrase-level
smooth warps only, anchors are VISIBLE MOUTH EVENTS, no interval slower than
0.5x, NO new generation — existing takes/segments only.

## Outputs (originals untouched)

- House master: `masters/mv7_im_the_nobody_man_16x9_corrected.mp4`
  md5 **d74de9cda8dc084c21dd8147ca668901**, 61,946,109 B, 4493 frames,
  187.208s, 1280×720 24fps, libx264 preset medium CRF 18 (SEI reads crf=18.0),
  AAC 48kHz stereo, faststart.
- 50MB delivery copy: `masters/mv7_im_the_nobody_man_16x9_corrected_50mb.mp4`
  md5 **04953a7cada34eef5c88d9c5b1ed4654**, 38,613,113 B, 4493 frames.
  Audio streamhash identical to the corrected house master
  (fd13495398dcb1e810f12acd2de38efa) — AAC copied untouched.
- Original delivered master (46ba607394488f1c14fef7ab3a3f6b51) and its 50MB
  copy are unchanged on disk.

## Measurement (before)

Per-onset mouth-event audit on the DELIVERED master: face-crop probe strips
(frames −4..+11 around each of the 58 scored onsets, extended windows for late
openers); lag = first frame of sustained clear lip-parting for that phrase
minus the onset frame. OPEN-FLOW rule: mouth open + articulating at onset and
not shutting >2f after → lag 0. Authoritative table:
`work/correction/lag_final.csv`.

- Before: median **3.5f = 0.146s**, mean 0.232s, max **24f = 1.000s (FC.8)**;
  29/58 onsets >0.15s late, 26/58 ≥0.25s late, 27/58 at 0. The mean (0.232s)
  matches the disclosed ~0.25s — the lag was real and concentrated at TAKE
  HEADS (segments starting a take or after a take-skip, often a held closed
  grin of 0.4–1.0s); mid-take phrase boundaries were already in flow.
- An automated tile-diff detector (`work/correction/auto_lag.py`) was run as
  a cross-check and REJECTED: diffuse push-in/body motion swamps the mouth
  signal and it contradicted clear visual reads. Visual reads govern.

## Correction build

Built from the REAL shipped cutlist (`work/assembly/cutlist.json` + rendered
segments), not the planning script. Builder:
`work/correction/build_cutlist_corrected.py` → `cutlist_corrected.json`
(64 segments, 4493f) + `actions.json`. 34 segments changed, 30 reused
byte-identical. All window ends ≤ take durations; no same-take overlaps
between adjacent segments in corrected space.

- **SHIFT ×21** — source window slid earlier by δ = lag ÷ factor (residual 0):
  S01a-occ1 +0.31s, S02-occ1 +0.49s, S03-V1.1 +0.83s, S03-V1.2 +0.67s,
  S03-V1.3 +0.25s, S04-V1.4 +0.42s, S05a +0.83s, S05b +0.74s, S07-C1.1 +0.42s,
  S09-occ1 +0.55s, S09-occ2 +1.01s, S11-V2.1 +0.18s, S11-V2.2 +0.18s,
  S12-V2.4 +0.30s, S14-PC2.3 +0.52s, S16-C2.5 +0.62s, S20-FC.1 +0.39s,
  S21-FC.5 +0.49s, S22-FC.8 +0.70s, S23-FC.10 +0.80s, S24-P1 +0.54s.
- **REWARP ×7** — window end pinned to the next segment's take-start, window
  start solved so the measured gesture lands on the onset, single smooth
  factor per phrase: S01a-occ2 (f 0.949→1.096), S04-V1.5 (0.829→0.907),
  S06-PC1.3 (0.837→0.852), S08-C1.5 (0.756→1.057 — speed 1.32x→0.95x, the
  largest feel change), S10-occ1 (0.978→1.131), S15-C2.1 (0.799→0.844),
  S17-C2.7 (0.699→0.757). All rewarp speeds 0.88x–1.19x.
- **SPLIT ×1** — S01b split at I-occ5: S01b-A (+0.06s for I-occ4) and
  S01b-B (+0.52s for I-occ5), both at the original factor; a 0.454s take-skip
  sits at the seam, on a phrase boundary where the mouth is closed between
  chant occurrences.
- **COMPANION-SHIFT ×3** — S16-C2.6, S21-FC.6, S21-FC.7 shifted with their
  leader phrases to keep take-contiguous seams; all three were lag-0 flow
  onsets and the corrected gate verified each still reads open-flow
  (NOT worsened).
- **SHIFT-CAPPED ×1** — S13-PC2.1: needed δ 0.564s, capped at 0.480s by the
  next segment's window start. Known residual ≈62ms (measured +2f after).
- **NONE ×30** — lag-0 segments, covers, plates, gaps, fade reused as-is.

Warp envelope of the corrected cut (from cutlist_corrected.json): speeds
0.549x–2.534x — inside the original envelope; no interval slower than 0.5x.

Preserved exactly: segment order; S01 split-chant restage; S15 cover
110.36–112.86s; S20 cover 150.38–152.88s; S16 caption = sparks/flicking;
4493f / 187.208s; song audio (same track.mp3, same mux recipe).

## Gate on the corrected master (evidence: work/gate_corrected/)

- **Audio identity vs track.mp3: PASS** — best lag 0 samples, correlation at
  lag 0 = 0.998776 (identical to the original gate's value).
- **Mouth offsets, re-measured with the same strip protocol**
  (`work/gate_corrected/lag_after.csv`, strips in `work/gate_corrected/strips/`):
  - median |offset| **0.146s → 0.000s** (target ≤0.08s) — 36/58 at 0f,
    15/58 at +1f, 7/58 at +2f
  - max |offset| **1.000s → 0.083s** (2f)
  - onsets still >0.15s late: **29 → 0**
  - **closed onsets: 0** (every onset parted/open by +2f at worst)
  - **hooks 25/25**
  - **worsened scenes: 0** (all 58 after ≤ before; companion-shifted C2.6,
    FC.6, FC.7 verified open-flow; capped PC2.1 residual +2f as predicted)
- **Judder: PASS** — no near-duplicate runs ≥24f during vocal material.
- **Motion: PASS** — vocal mean frame diff 2.939 (original 2.953; fail <0.5).
  Two sub-threshold ≥12f near-dup runs sit in the S15 cover window and the
  slow C2.7 phrase, same character as the original gate.
- **ffprobe: PASS** — audio codec AAC 48kHz stereo; x264 SEI crf=18.0;
  4493 frames; moov before mdat (faststart).

## Disclosures

- **PC2.2 and FC.9 — STRUCTURAL-weak, unchanged.** Both segment windows open
  on the decaying tail of a gesture: mouth parted from the first frame but at
  weak amplitude throughout. No shift can strengthen a gesture that isn't
  there; left as shipped and disclosed (lag 0 before and after).
- **PC2.1 residual +2f (0.083s)** from the capped shift above — the worst
  remaining onset together with the +2f segment-boundary cases (FC.1, FC.5,
  FC.8, where the nominal onset frame precedes the segment start by design,
  as in the original cut; the mouth gesture is underway at the segment's
  first frame).
- **V1.5** reads weak in profile before and after (after +2f vs before +5f) —
  low-confidence onset in a turned-away pose; improved, not dramatic.
- S08-C1.5's rewarp slows that phrase from 1.32x to 0.95x speed — the one
  place the correction changes performance feel, in exchange for landing a
  +22f (0.92s) lag on the onset.

Gate verdict: **PASS** — flag `MV7_TIMING_CORRECTED.flag` written.
