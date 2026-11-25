# MV-2 v5 verification — from the delivered master itself

Master: `masters/mv2_toll_roads_are_dumb_v5_16x9.mp4`
md5 `30305a2db3058c530ebbef42be20b2da`, 74,206,052 bytes
Video: h264 1280x720 24fps, 268.041667s, 6433 frames
Audio: AAC 48kHz stereo, 268.010s — `track.mp3` untouched, md5 `9e5ff10876cda8ac17dcb22b79c3f00a`
Subtitles: mov_text, 48 cues, byte-identical to `captions_v2.srt` (diff clean)
Corner bug `~ WuBu ~` present in every checked frame.

## The drift that was caught before delivery (do not ship the first v5 render)

The first v5 render (attempt 2, md5 `cf2cebd0351611c8d494255fecf2a57b`, set aside at
`masters_work_v5/v5_first_render_DEFECTIVE_256s.mp4`, never deliver) had correct
total duration on paper but a real video stream of only 256.21s — a freeze-branch
`trim end_frame` bug, fixed in `assemble_v5.py`.

The second render (attempt 4) fixed that bug and hit 268.04s total, but per-clip
measurement showed a NEW, quieter defect: each warped segment rendered 1–3 frames
long (fps-after-concat rounding per interval). Summed over 35 warped segments
the timeline drifted +0.99s by the tail. Proof from the master itself: at song
257.97 (S26 "toll" onset) the drifted master showed S25 postvocal — singer
looking down at the ticket, mouth closed, not singing.

Fix (`v5_frame_fix.py`): every one of the 82 intermediates was forced to exactly
`round(span*24)` frames before re-concat — trim tail frames if long, clone the
last frame if short — then re-muxed with the untouched track/captions/bug.
The drifted render was moved aside to `masters_work_v5/v5_drifted_1s.mp4`
(never deliver). After the fix, worst cumulative drift vs the cutlist is
+0.068s (one postvocal segment), and every vocal start sits within 0.062s
of its song position — S26 +0.013s, S21 +0.010s, S15 +0.050s, S01 +0.018s.
That is frame-quantization level, not a sync error.

## Word-by-word spot checks (frames pulled from the DELIVERED master at
song first-word time + 0.15s, scene identity + facing + mouth state)

- S01 "Yeah" 4.59s: S01 take, facing camera. Mouth closed at this instant —
  KNOWN take-internal lag, disclosed: this take's first visible open mouth is
  1.0s into its own audio (kept as an audio anchor per v5 rule 1, word
  identity over open-mouth state). Scene/line position is correct.
- S02 "They" 20.27s: facing, mouth parted, ticket in hand. PASS. (Teal pocket
  square vs CADMIUM spec, disclosed nit from QC, kept.)
- S04 "weave" 42.05s: facing, mouth open. PASS. Head gap disclosed: only one
  clean "Weave" exists in t5, so song 74+75 share one open weave shape.
- S08 "they" 88.63s: S08 take, facing, mic in hand, eyes closed, mouth
  transitional. Scene correct; not a drift failure.
- S11 "crashes" 103.87s: facing, mouth wide open singing. PASS.
- S15 "they" 160.35s: S15 take (not the R5 reuse), facing, mouth open. PASS.
- S21 "road" 205.35s: facing, mouth parted, mic + ticket. PASS (burst-word
  collapse handled at 204.24, no window collapse).
- S23 "toll" 230.37s: S23 take, facing, mouth parted at onset. PASS — this is
  the corrected chorus occurrence (song 374–377), not the v4 wrong occurrence.
- S26 "toll" 257.97s: facing, mouth WIDE OPEN singing into the mic. PASS —
  this is the frame that failed on the drifted render and now passes.

All checked frames: correct scene take for its own prompted line, singer
facing camera, corner bug present, no on-screen text besides the bug.

## What v5 does and does not claim

- DOES claim: every scene plays its own prompted line, at that line's own song
  position, in order, with segment boundaries within ~0.07s of the cutlist.
  No cross-line matching, no noise-merge anchor drops, no vocal played over a
  song interval with no corresponding words, no stretched mouths.
- Does NOT claim phoneme-perfect mouth sync: the generator's mouth lags its
  own take audio inside non-refired takes (S01 above is the visible case).
  v5 fixes WHICH words are on screen WHEN; it does not repaint mouths.
- Disclosed carry-overs: S04 head gap (above); S10 profile head, S12
  back-to-camera head 0–1.5s, S17 "meaner" garble + closed tail, S07/S11/S12/
  S17/S18 paraphrase anchors with skipped song fillers noted per scene,
  S14/S19 background arrow pictograms (no letters); reused chorus footage
  repeats visuals (the disclosed price of word-correct repeats).
- 46 assembler flags (FAST squeezes <0.4 and >2.5 freeze-guards) are in
  CUTLIST_V5.json and are expected: they are the take-pause squeezes and
  slow-stretch guards, not errors.

Verdict: PASS for delivery as the prompt-grounded, properly timed v5 cut.
Supersedes v3 (disputed) and v4 (wrong approach). Never re-deliver v1–v4,
the defective 256s render, or the drifted 1s render.
