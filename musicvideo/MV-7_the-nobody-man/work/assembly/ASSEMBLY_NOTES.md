# MV-7 ASSEMBLY — FINISHER PROGRESS NOTES

Recovery: previous coordinator rendered all 63 segments then died on transport
(sqlx pool timeout) at ~19:18 EST 2026-11-06. All work survived on disk.
Finisher spawned ~19:35 EST.

## 2026-11-06 ~19:36 EST — segment verification
- cutlist.json: 63 segments, total 4493 frames = 187.208s (song 187.200s; +5f
  rounding accumulation across segments, last seg FADE ends song_end 187.2).
- Verified every segment with ffprobe -count_frames: ALL 63 exact-frame vs
  cutlist, 1280x720, 24fps. No missing files.
- track.mp3 md5 c660e81b0811cf2240c0e33992b03aa7 (187.200s) — matches.
  track.mp4 md5 06881e867444accf29ae826a7320163f — matches.
- Segments rendered at libx264 preset medium CRF 18 (per render_segments.py).

## S24 warp call (from cutlist, decided by previous coordinator)
- S24-P1: factor 0.8555 (speed 1.1689x), 71f.
- S24-P2: factor 1.799 (speed 0.5559x, i.e. 1.80x slow), 168f — the PHRASE
  RAMP, not the uniform 0.797x warp. Inside the 2x-slow cap (0.556x > 0.5x
  floor), barely. Disclose in MV7_ASSEMBLY_NOTES.md.
- S24 t2 is a slow push-in close-up, NOT the vehicled pull-back — final
  frame rhyme weaker than t1's. Disclose.

## Mux
- Command: ffmpeg concat demuxer seg/list.txt + track.mp3, re-encode
  libx264 preset medium CRF 18, yuv420p, 24fps, AAC 192k 48kHz stereo,
  faststart. No -shortest (keep all 4493f; audio ends 187.200s, video
  187.208s — 8ms tail, fade is black/silent there).
- Target: masters/mv7_im_the_nobody_man_16x9.mp4
- Status: LAUNCHED detached (see mux.log).
- MUX DONE ~19:43 EST: masters/mv7_im_the_nobody_man_16x9.mp4
  md5 46ba607394488f1c14fef7ab3a3f6b51, 62,331,020 B, 4493f, 187.208s,
  1280x720 24fps, h264, SEI crf=18.0, AAC 48kHz stereo, faststart
  (moov at 36). House master EXCEEDS 50 MB -> 50MB delivery copy owed.
- S16 caption adjudication CLOSED: unprompted tiny decode of the s16t1
  take audio hears "I got a thousand little sparks flicking in the
  dark." 10/10 — caption = sparks / flicking (SONG_WORDS "spots/Flipping"
  was an ASR mishear; matches sheet + LYRIC_TIMELINE adjudication).

## Gate (in progress)
- Onsets: work/gate_final/onsets.json — 66 total: 58 scored (25 hooks),
  8 montage/plate-covered (C2.4, B.1-B.6, FC.4 — no mouth expected).

## Gate DONE ~19:52 EST — PASS (work/gate_final/GATE_SUMMARY.md)
- Audio identity: lag 0, corr 0.998776 vs track.mp3.
- Mouth: 58/58 pass (O 28, T 29, o 1, C 0); hooks 25/25 (O 11, T 13, o 1).
  20 onsets first read +/-1-2f off from rounding drift; 14 re-read at TRUE
  first frames (corr_01-02.png) — one change: FC.5 T -> O.
- Judder PASS (vocal mean diff 2.953; no near-dup run >=24f; S18-plate
  high-diff run is in-plate montage cuts, eyeballed f3052/f3085).
- Motion PASS.
- Warp extremes: slowest S08-C1.7 0.5487x (1.82x slow); fastest
  S05b-PC1.2 2.5333x. No segment past the 0.5x floor.
- MV7_ASSEMBLY_NOTES.md written (project root).

## 50MB delivery copy
- Encoding (2-pass ~1450k, audio copied) — DONE ~19:59 EST:
  masters/mv7_im_the_nobody_man_16x9_50mb.mp4, md5
  0e16908c24b58cd5fe4cee71ecb08b6f, 38,620,293 B, 4493f, 187.208s,
  h264 1448.89 kb/s, AAC 48kHz stereo. Audio streamhash identical on both
  files (fd13495398dcb1e810f12acd2de38efa) — audio copied untouched.
- GATE: PASS on all four checks. Assembly complete; ready for delivery.
