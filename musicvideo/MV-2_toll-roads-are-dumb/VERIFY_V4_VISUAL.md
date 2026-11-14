# MV-2 v4 visual-event cut — verification record (2026-11-02)

Supersedes the v3 best cut as the current cut. The v3 cut's sync was
disputed by the user (~05:45 EST 2026-11-02); diagnosis: no global shift,
the lag lived inside the takes (visible mouth motion lagging take audio).

## Master
- `masters/mv2_toll_roads_are_dumb_v4_16x9.mp4`
- md5 `8730e2e4d4dfc24ee2da41e72b09116f`, 75,276,809 bytes, 268.01 s
- h264 1280x720 24fps + AAC 48kHz stereo + mov_text subtitle
  (subtitle track = `captions_v2.srt`, verified by extraction diff)
- Song audio untouched (track.mp3 muxed); take audio discarded.
- All streams start at 0.000; leader hold `masters_work_v4/S01_hold.mp4`
  is video-only (no stray-audio leader bug repeat).
- Corner bug `~ WuBu ~` visible bottom-right in all onset frames checked.

## Design (see MOUTH_MEASUREMENT_V4.md)
v3 word-grid windows kept; each scene's first word re-anchored to its
VISIBLE first-open mouth. First-anchor take-t0 shifts:
S01 0.00->1.00, S02 0.00->5.00, S05 2.76->3.50, S10 1.72->5.00,
S12 0.00->2.00, S23 1.54->2.00. S08 unshiftable (no visible open mouth).

## Onset verification (frames read from the delivered master)
- S01 song 4.44 ("Yeah"): mouth clearly open, face to camera. PASS.
  Frame-identity vs take S01 t4 @1.0: PSNR 31.65 dB (same frame, re-encode).
- S05 song 50.84 (chorus "Toll"): mouth open, face to camera, ticket up. PASS.
  Frame-identity vs take S05 t4 @3.5: PSNR 32.40 dB.
- S02 song 20.12 ("They"): lips parted, face to camera. Parted, not wide.
- S12 song 111.30 ("poor"): mouth open, singing. PASS.
- S23 song 224.92 ("Toll"): mouth open, singing. PASS.
- S10 song 96.80 ("Speed"): frame itself is a closed-mouth blink
  (take S10 t1 @5.0 is the same blink frame — mapping correct);
  mouth open by master 97.30, i.e. ~0.5 s after the onset.
  Residual ~0.5 s at this one onset, within the mouth measurement's
  +/-0.5 s sampling precision. Disclosed, not rebuilt for.

## Known limits carried over (not fixed by this design)
- S08 take has no clearly open mouth at any sample; left as in v3.
- S02's middle anchors were dropped by the assembler's noise-merge
  (all middle take words sit before the visible burst at take 5.0):
  only "They" and "go" survive as anchors; the middle is swept uniformly.
- Structural tail holds from v3 remain (longest S14 window 128.76-160.20).
- Mid-scene word timing still follows Whisper take-audio anchors, not
  per-word mouth measurement; only first-word onsets were re-anchored.
- Honest limit unchanged: plausible mouth motion, not phoneme accuracy.

## Files
- `WORD_MATCH_V4.json`, `CUTLIST_V4_VISUAL.json`,
  `assemble_v4_visual.py`, `masters_work_v4/` (swing segments + concat).
- v3 best cut (`..._v3_16x9.mp4`, md5 e5dcfe3a598b989b6d021e3e702a50b4)
  stays on disk as the superseded cut; do not re-deliver v3.
