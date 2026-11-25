# MV-16 "Wrong for Years" — GATE LOG (REBUILD on the correct Suno take)

Rebuild reason: the delivered first build used the wrong Suno take
(user correction 2026-11-13 ~13:22 EST). Correct take: track.mp4
md5 e4649643f510cf453ec5008ec4e24489, 198.016s (wrong take: 183.200s,
preserved as track_wrongtake.* / masters/*_wrongtake.mp4 — never
deliver those). First-build docs archived under work/rebuild/ and
work/analysis/wrongtake/.

## House master — masters/mv16_wrong_for_years_16x9.mp4
- md5 **e9a64e89395534c74729f164ae19e76a**, 129,048,899 B
- 4752 frames exactly, 1280×720, 24 fps, h264, yuv420p
- x264 SEI read from the delivered file: **crf=18.0** (preset medium)
- Duration 198.016s = track duration (video stream 198.000s = 4752f;
  audio tail +0.016s)
- Audio: **AAC** 48 kHz stereo, 192k, encoded from track.mp3
  (ffprobe codec_name=aac — MP3 never stream-copied into the MP4)
- Faststart: moov before mdat ✓

## Master-audio agreement (the figure the first build never recorded)
work/analysis/audio_agreement.py — master audio vs track.mp3, decoded
16 kHz mono, Pearson correlation:
- **overall 0.99812** · 5s windows: **min 0.99736**, mean 0.99825
- worst windows: 185s 0.9974 · 145s 0.9974 · 155s 0.9975
The master audio is the correct take, sample-aligned, unedited.

## Chat copy — masters/mv16_wrong_for_years_16x9_chat.mp4
- md5 **df499a542daec3edaba6b65a028159bd**, 45,292,507 B (≤50 MB ✓)
- Bitrate-capped delivery encode of the same cut (video 1650k,
  maxrate 1800k); **AAC audio copied untouched**; faststart; 198.016s

## G7 wrong-lyric gate (screened ASR: word p ≥ 0.5, segment
avg_logprob ≥ −1.0; P = the slot's performed words from the new grid)
- **S22 t3** (re-fire, BR slot = grid lines 65–69): ASR "Wrong for
  years, wrong for years, wrong for years, nobody stopped me, nobody
  stopped me." — 1 segment, avg_logprob −0.192, all 15 words p≥0.818.
  Overlap **1.00 PASS**. The take matches the NEW bridge exactly
  (WFY×3 + NSM×2; the wrong take's bridge had WFY×2).
- **S28 t3** (re-fire, OUT slot = lines 83–86): ASR "Nobody stopped
  me, nobody stopped me, wrong for years." — avg_logprob −0.294,
  9 words p≥0.759. Overlap **0.857 PASS**. The (yeah)×3 adlib (L86)
  is not sung by the take → merged into L85's span per the standing
  ad-lib rule (first-build precedent: S15 (what), S16 (uh), S28 (oh));
  the chant plays over the held fist-pump pose + dawn drift.
- Cross-pair note: s28_t3 scores 1.00 against S22's word SET (BR and
  OUT share the WFY/NSM vocabulary in this performance) — the takes
  are distinguished by sequence, verified from the ASR word streams:
  S22 = WFY→WFY→WFY→NSM→NSM, S28 = NSM→NSM→WFY. No swap.
- **S05 lesson re-checked on the new grid**: the friends' lines
  (L16–17, 33.16–38.68) sit on S06 ← s06_t2, ASR exactly "Friends in
  the back just nodded and let it ride." (raw 10/10; screened 0.90 —
  "Friends" p=0.209 is an ASR probability artifact). S05 ← s05_t3
  sings "Belted the whole chorus in the car / Like I wrote it"
  (rode = wrote homophone, as documented in build 1) + (yeah):
  screened 0.91 / raw 1.00 PASS. The generator drift that killed
  build 1's S05 t2 does NOT recur on the new grid.

## Conform (work/segments/conform_log.json)
28 segments, exact frame counts, sum 4752f. Factor = playback speed
of each chunk. All sung-word chunks land within **0.541×–2.86×**;
the 0.5× slowdown floor is never breached; no frozen frame during
words (hold-fill fired once: S07 L21; one tpad clone frame at S13's
tail, inside a breath pocket — same as build 1's S13).
Disclosed extremes (build 1 shipped up to 3.00× / down to 0.47×):
- Squeezes: S03 L7 2.86× · S05 L14 2.86× (half the span is
  inter-phrase breath) · S02 L5 2.48× (the new performance clips
  "For a decade" to 0.54s) · S10 L29 2.35× · S14 L42 (yeah) 2.67×
  burst on a 0.24s adlib (build 1: 2.13× on this same adlib) ·
  S17 L52 2.14×
- Slow phrases 0.54–0.58×: S01 L2 · S21 L63 · S27 L81 · S07 L18 ·
  S13 L39 · S23 L70 (the deliberate slow backbend — build 1: 0.47×)
- Pocket drifts (non-word picture): S12 L37-gap 0.41× ·
  S13 L39-gap 0.45× (build 1 shipped a deliberate 0.31× S13 drift)

## S28 tail freeze — caught by probe, fixed before delivery
Motion probe on the first assembled master: the take's own motion
dies at ~8.5s (held pose), leaving the master's last ~2.2s frozen.
Fixed in work/analysis/fix_s28.py: tail-A = live span only
(src 5.54–8.50 → 191.50–196.10, 0.64×; covers the (yeah) chant with
walk + dawn flood + pose strike); tail-B = zoompan push-in
1.00→1.10 on the held-pose frame for the post-chant tail music
(196.10–198.10, no words). Re-probed on the DELIVERED master:
tail-A mean-abs-diff 17–26 per 0.5s, tail-B 13–14 per 0.5s —
continuous motion to the final frame.

## Mouth gate (frames pulled from the delivered master)
9 line/hook onsets × (onset, +0.15s) + full-res 6-frame strips at
the three tightest onsets (S03 L7 @14.56, S22 L65 @142.46,
S28 L83 @184.78): every onset open or transitional-open, fully
open by +0.17s. No closed-mouth hook onset; no mouth-lie cut in
the sample. Frame 0 = S01 fist-pump peak, mouth wide open.
Motion probes on the slow spans (S01 L2, S07 hold zone, S12 gap,
S13 tail gap, S21 L63, S23 bend, S27 L81): continuous motion in
all (mean-abs-diff 8–72 per 0.5s).

## Visual / event reads (onset sheet + strips, work/qc/rebuild_master/)
Anime lock + GUY identity consistent; costume states correct
(bowling C1 → hawaiian C2 → gold glitter jacket C3–OUT); S22
medium swap reads (pale paper room, ink outlines, he stays full
colour); S13 word chase assembles on the blank wall; SCREEN PiP
states all present (install S07 → glitch C2 → pulse POST → dark
BR → gold equalizer FC → fade OUT) and never show a second lyric
set; S26 worn graphics on the blank tee; `~ WuBu ~` bug present.
Same 28 named events as the approved first build (the two re-fires
re-stage events 1.2 and 7.3 with the same vehicles' staging).

## Provenance / process
26 of 28 ship takes carried over from build 1 (identical performed
line texts; re-timed to the new grid via work/analysis/scene_map.json
+ conform_rb.py). S22/S28 re-fired by coordinator 83770097
(vehicles: work/vehicles/mv16_s22_vehicle_rb.txt,
mv16_s28_vehicle_rb.txt) because the new performance's BR/OUT
content differs. 83770097 died 2026-11-13 ~14:07 EST (transport:
sqlx pool timeout) after the re-fires + take ASR landed; recovery
coordinator ae4db7d3 completed G7 → conform → ASS (1,404 events,
work/mv16_kinetic.ass) → assembly → this gate pass.
USED_EVENTS: verified — the full MV-16 block is already on file
from build 1; the rebuild introduces no new events, no rows added.
No delivered flag written, nothing committed (parent owns both).
