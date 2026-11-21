# MV-7 "I'm The Nobody Man" — ASSEMBLY NOTES

## Master
`masters/mv7_im_the_nobody_man_16x9.mp4`
md5 **46ba607394488f1c14fef7ab3a3f6b51** · 62,331,020 B · 4493f · 187.208s ·
1280×720 · 24fps · libx264 preset medium CRF 18 (SEI crf=18.0) ·
AAC 48 kHz stereo · faststart (moov at 36).
Song: track.mp3 md5 c660e81b0811cf2240c0e33992b03aa7 (187.200s) — sole master
audio, untouched in timing. 4493 frames = 187.208s: +5f vs the song from
per-segment frame rounding; the last 8 ms is black fade tail.

50 MB delivery copy: `masters/mv7_im_the_nobody_man_16x9_50mb.mp4`
md5 **0e16908c24b58cd5fe4cee71ecb08b6f** · 38,620,293 B · 4493f · 187.208s ·
h264 1448.89 kb/s (2-pass, target 1450k) · AAC audio copied untouched
(audio streamhash fd13495398dcb1e810f12acd2de38efa identical on both files).
House master stays canonical on disk/CDN.

## Build
- 63 segments (work/assembly/cutlist.json), all verified exact-frame vs the
  cutlist, 1280×720 24fps, rendered at CRF 18 with phrase-smooth setpts
  warps (one factor per segment, no per-word stepping).
- Concat + track.mp3 mux, single re-encode CRF 18 (mux.log).
- The assembly coordinator (first) rendered all segments, then died on a
  transport error; the finisher recovered the segments from disk, verified
  them, muxed, and gated. No video was re-fired.

## Coverage — all 24 scenes
22 KEEP takes + 3 structural treatments, all baked into the cut:
- **S01 STRUCTURAL** (model caps the chant at ~3, v4 backfired): split-chant
  restage — S01a = s01 t2 occurrences 1–3, S01b = s01 t1 restage for
  occurrences 4–5, S02 = occurrences 6–7. All 7 chant occurrences present.
- **S15 STRUCTURAL** (C2.4 chant missing on two pulls): beat-cut to montage
  for exactly 110.36–112.86s (C2.4-COVER, S18 plate), back at C2.5/S16.
- **S20 STRUCTURAL** (FC.4 chant missing on two pulls): beat-cut to montage
  for exactly 150.38–152.88s (FC.4-COVER, S19 plate), back at FC.5/S21.
- **S10**: tag chant ×3 (measured song), not ×4 — three occurrences.
- **S24 t2**: P1 factor 0.8555 (1.17x); P2 factor 1.799 — the PHRASE RAMP
  (0.556x speed, 1.80x slow), NOT the uniform 0.797x warp. Inside the 2x
  slow cap, barely. S24 t2 is a slow push-in close-up, NOT the vehicled
  pull-back — the final frame rhyme is weaker than t1's (close-up holds
  on the grin, eyes closed in the final hold).

## Gate — PASS (work/gate_final/GATE_SUMMARY.md)
- Audio identity: lag 0, corr 0.998776 vs track.mp3.
- Mouth state at onsets: 58/58 pass (O 28 · T 29 · o 1 · C 0);
  hooks 25/25 (O 11 · T 13 · o 1 · C 0). Weakest: I-occ1 (o).
  Systematic ~0.25s mouth lag disclosed (mouth opening on every word
  within 6 frames of onset).
- Judder: PASS. Motion: PASS (vocal mean diff 2.953).
- Warp extremes: slowest S08-C1.7 0.5487x (1.82x slow); fastest
  S05b-PC1.2 2.5333x. No segment past the 0.5x slow floor.

## Open items closed at assembly
1. **S16 caption adjudication — CLOSED**: unprompted tiny decode of the
   s16t1 take audio hears "I got a thousand little sparks flicking in
   the dark." 10/10. Caption = **sparks / flicking** (SONG_WORDS
   "spots/Flipping" was an ASR mishear; matches the sheet and the
   LYRIC_TIMELINE adjudication).
2. **S24 t2 warp call — CLOSED**: phrase ramp (factor 1.799), disclosed above.
3. **FC.10 lyric — CLOSED in volley 6**: S23 t1 sings the sheet line
   "Yeah, I turn the small things grand"; caption = sheet.

## Disclosures
- Systematic ~0.25s visible-mouth lag behind song onsets (see gate).
- S24 final frame is a push-in close-up, not the pull-back rhyme.
- I-occ1 is the weakest hook read (o — barely open at +0.25s).
- Near-dup runs 17–20f in three spots (all < 24f frame-rule threshold;
  two inside montage covers).
- S18 bridge plate contains its own internal cuts (corkboard → dashboard);
  in-plate montage motion, verified by eye.
- Era B/C singing takes carry the slow push-in drift; assembly trims/crops.
- Mixed source rasters (1152×768 / 1248×704 / 1280×720) all cropped to
  16:9 at segment render; no stretched frames.
