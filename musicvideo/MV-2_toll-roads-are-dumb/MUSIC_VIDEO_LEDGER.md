# MUSIC VIDEO LEDGER — MV-2 "Toll Roads Are Dumb" (THE VOICE)

Delivered 2026-11-01. Full song, 27 scenes, one original crooner (THE VOICE).
Suno track is the sole master audio; generated take audio was mined for
timing, then dropped. No UNC, so the hoodie wordmark gate was not triggered;
the ~ WuBu ~ corner bug was added in assembly.

## Masters (verified 2026-11-01, ffprobe + md5)

| Master | File | Size | md5 | Spec |
| --- | --- | --- | --- | --- |
| 16:9 | `masters/mv2_toll_roads_are_dumb_16x9.mp4` | 98,656,774 | `00368e7626185343ad7a66dc2ae28a8d` | 1280x720, h264 + aac + mov_text subtitles, 268.010s |
| 9:16 | `masters/mv2_toll_roads_are_dumb_9x16.mp4` | 98,331,151 | `f8277f868df8554cb77360f5a6a1e1cf` | 720x1280, h264 + aac + mov_text subtitles, 268.010s |

Note 2026-11-06: both v1 master files above were deleted with the user's approval (see CLEANUP_2026-11-06.md); the md5s remain the delivery record. masters/ now holds only the delivered v6 16:9 + viewing cut.

9:16 is a blurred-pad reframe of the same cut, not a second shoot.
Video stream: 6409 frames at 24fps = 267.042s; audio and subtitle
streams run the full 268.010s. The ~0.97s difference is per-scene
tween rounding (each 10s scene landed 236–242 frames instead of exactly
240; S27 landed 195 vs 192 expected) — joints drift by a few frames at
most, and the final frame holds through the audio tail.

## Source

- Track: `track.mp3`, md5 `9e5ff10876cda8ac17dcb22b79c3f00a`, 268.01s,
  extracted from the user-sent Suno lyric video (`track.mp4`,
  md5 `abc857aa9e169aa1d009e6695edef07d`).
- MUSIC_TAG source id: `MV-2-TOLL-ROADS`. Note: `music/tags.json` rows are
  piece -> bed/sting pairs for station pieces; a music-video master takes
  no bed/sting row, so no row was added there — the source id is recorded
  here and in `musicvideo/intake/INTAKE_LOG.md` instead.
- Lyrics: `lyrics.txt` (verbatim owner text). Captions: subtitle track
  (`masters_work/captions.srt`), never burned in.

## Cut

See `CUTLIST.md` for the full scene table. Active takes: S01 t2, S02 t3,
S03 t2, S04 t3, S05 t2, S06 t2, S07–S27 t1. Trims all 0–10s except S27
0–8.01s (song window 260–268.01).

## Lip sync (cheap time-tween, user-directed 2026-11-01)

Per scene, RMS-envelope peaks were mined from each take's generated audio
and paired in order to Suno onset peaks inside the same scene window
(`LIPSYNC_REPORT.json`: 7–28 paired anchors per scene). Each take was
piecewise time-remapped to those anchors with scene duration kept exact,
then its generated audio was dropped and the Suno track muxed as sole
master. No lip-sync model, no re-fire. Final segment speeds landed
0.78–1.26 (two clamp+rescale passes; slight overshoot vs the nominal
0.8–1.25 clamp, duration exact).

## Flags in the cut (disclosed at delivery, no reroll ordered)

- S11: partial painted road letters.
- S15: five legible STOP signs.
- S17: "THE VOICE" gantry lettering.
- S02/S04 text flags were CLEARED by the t3 rerolls (no signage / no
  gantry vehicles, QC-passed at 3s/6s/8s).
- Recurring nits: pocket square reads blue/red-orange in many takes vs
  CADMIUM; S26 small orange triangle artifact on suit back; S19 fold /
  S20 breast-pocket ticket not clearly visible at 3s; S27 smile/fade land
  later in the shot.

## Files

- Takes: `takes/` (t1/t2/t3 as listed in `TAKE_HISTORY.md`).
- Assembly: `lipsync_assemble.py`, per-scene tweens in `masters_work/`,
  tween report `LIPSYNC_REPORT.json`, cut `CUTLIST.md`.
- Announced to #wubu-mv-6a90e1 via `announce.sh` on delivery.

## V2 masters — Engine v2 proof run (delivered 2026-11-01, user order "make the best music video")

V1 was rejected by the user (sync not timed up). V2 re-plans the cut on
LYRIC_TIMELINE.md under Engine v2: 11 performance-window re-fire takes +
S26 re-plan restage, trims only, NO peak warp (dead method, never reused),
Suno track sole master audio, captions in post, corner bug.

| Master | File | Size | md5 | Spec |
| --- | --- | --- | --- | --- |
| 16:9 v2 | `masters/mv2_toll_roads_are_dumb_v2_16x9.mp4` | 52,296,097 | `58a1da0f0d47e97092b88274f7e4f49e` | 1280x720, h264 + mp3 + mov_text subtitles, 268.032s |
| 9:16 v2 | `masters/mv2_toll_roads_are_dumb_v2_9x16.mp4` | 39,304,621 | `85fbe2a2f18fafbf9325d57bc6067e6e` | 720x1280, h264 + mp3 + mov_text subtitles, 268.032s |

9:16 is a blurred-pad reframe of the same cut. Video: 6432 frames @24fps =
268.0s; audio runs the full 268.01s (1 frame of audio tail). Master audio
is track.mp3 copied untouched (sample-identical in the tested 30s stretch
at 100s; the 22ms decoded-length difference is trailing mp3 padding only).
Subtitle track: 48 cues from LYRIC_TIMELINE.md (`captions_v2.srt`).

### Cut

See `CUTLIST_V2.md`. Active takes: S01 t2, S02 t3, S03 t2, S04 t3, S05 t3,
S06 t2, S07 t2, S08 t1, S09 t2, S10 t1, S11 t2, S12 t3, S13 t2, S14 t1,
S15 t2, S16 t1, S17 t2, S18 t1, S19 t1, S20 t2, S21 t1, S22 t1, S23 t1,
S24 t1, S25 t2, S26 t2, S27 t2. Trims all 0–10s except S17 0–8.01s (the
cut's only short scene; the 1.99s of total trim is spent there so later
cuts track line boundaries).

### Why the cuts sit where they sit

27 takes × 10.000s covering a 268.01s song forces ~10s scenes (total trim
1.99s). Cuts 1–16 sit on the 10s grid; from 168.01 on, cuts track true
line boundaries within 0.01–2.51s. Section-boundary error: Intro/V1 2.5s
early, V1/C1 1.5s early, C1/V2 1.5s early, V2/C2 1.5s early, C2/Bridge
2.51s late (worst remaining misalignment, disclosed), Bridge/C-ext 1.99s
early, C-ext/Outro 0.49s early. The v1 outro error (8.5s early) is closed.

### S26 decision (made at re-plan)

S26's v2 window (248.01–258.01) contains outro line 47 + line 48's
opening vocal, so per the standing rule it flipped from lineless-hold KEEP
to RE-FIRE. S26 t2 (vehicle mv2_s26_vehicle_v2.txt, staging axis:
sing to camera first, silhouette after the vocal) QC-passed on a widened
1s–8s sample (vocal 1–3s, turn 4s, silhouette 5–8s; text-clean). S26 t1
retired from the cut, kept on disk.

### Flags in the v2 cut (disclosed at delivery)

- No open text flags: v1's S11/S15/S17 text flags are gone (those scenes
  use QC-passed t2/t3 takes).
- Recurring nits: pocket square reads blue/red-orange in many takes vs
  CADMIUM; S26 t2 mic handheld + mid-take turn; S11 t2 turn lands
  mid-take; S25 t2 place beat lands early at 5s; S07 t2 gantry signal
  green arrows (signals, not letters).
- Honest lipsync limit: this pipeline maximizes the plausibility of
  mouth motion against the Suno master — it has no audio-conditioned
  generation and must not claim phoneme-accurate lipsync.

### V1 status

V1 masters (`mv2_toll_roads_are_dumb_16x9.mp4` / `_9x16.mp4`) remain on
disk as the rejected cut. Do NOT re-deliver v1.

## VIEWING CUT — delivered 2026-11-03 (user order 2026-11-03 20:14 EST: use what we have now, no new generation)

- Master: `masters/mv2_toll_roads_are_dumb_viewingcut_16x9.mp4`, md5 `ff39ec1837ece12c1afab70829a73802`, 1280x720/24fps, 6432 frames, 268.010s, AAC 48kHz stereo, faststart, 66,398,322 B. Parent-verified md5 + ffprobe + zero-decode-error pass.
- Chat-sized copy: `masters/mv2_toll_roads_are_dumb_viewingcut_16x9_small.mp4`, md5 `920eeabaa0633cddd464a1b64d442b0e`, same frames/duration, CRF 28 / AAC 128k, 25,404,217 B.
- Soundtrack = untouched `track.mp3` (md5 `9e5ff10876cda8ac17dcb22b79c3f00a`); captions from `captions_v2.srt`; corner bug `~ WuBu ~`.
- Parent motion audit on the delivered master itself (same method as builder): frames 6432, mean diff 2.559, total frozen (<0.2) 0.625s, longest near-dup run 14f (0.583s, S12 slow-close, mouth visually moving — not a freeze), frozen runs >=6f only (172.46, 8f, 0.333s mid-vocal S17, under gate) and (267.71, 7f, tail tpad, no words). Runs >12f: exactly three, all adjudicated (119.83 slow-close; 207.88 + 210.25 S21 inter-word pauses, not during words). No still frame >0.5s during words.
- NOT the v6 final. Fallbacks time-stretched, not QC passes: S05 t6 1.896x, S13 t3 2.395x, GAP-A S04 t1 1.470x; S09 residual 1.26x. Word-match gaps (moving footage only, no mouth): S03 27.34-34.32, GAP-B 100.26-103.60 (no take sings "safer"), GAP-C remainder 201.10-204.24, GAP-D 224.92-230.22, GAP-E line 44 236.62-238.82, plus micro-gaps listed in VIEWING_CUT_2026-11-03.md. No REJECTED / frame-failed / repeat-defect / text-failed take used.
- Full record: `VIEWING_CUT_2026-11-03.md` + `VIEWING_CUT_2026-11-03.json`; intermediates in `masters_work_viewingcut/` (master_audit.json is the parent re-run of the builder's audit, numbers identical).

## V6 FINAL — delivered 2026-11-04 (parent-verified from the delivered files themselves)

- Master: `masters/mv2_toll_roads_are_dumb_v6_16x9.mp4`, md5 `b2d386bf138aa5e3b654a8382b7b68c0`, 1280x720/24fps, 6432 frames, 268.010s, h264 + AAC 48kHz stereo, faststart, 78,154,776 B.
- 9:16 reframe: `masters/mv2_toll_roads_are_dumb_v6_9x16.mp4`, md5 `758554e8f668271b72eadab37f1d59d6`, 720x1280/24fps, 6432 frames, 268.010s, faststart, 84,116,707 B. Rebuilt from the silent video (not a crop): the first reframe clipped long caption lines and cropped the `~ WuBu ~` bug out; the rebuilt version uses wrapped 9:16 captions + bug, verified on 3 sample frames.
- Chat copy: `masters/mv2_toll_roads_are_dumb_v6_16x9_chat.mp4`, md5 `473a108745f7782559055d1114fea464`, 1280x720/24fps, 6432 frames, 268.010s, faststart, 30,492,411 B.
- Soundtrack = untouched `track.mp3` (md5 `9e5ff10876cda8ac17dcb22b79c3f00a`); captions line-block + per-word highlight from measured song word times (396 events), highlight 3 frames early; corner bug `~ WuBu ~` on all masters.
- Frame-count fix: the first v6 build summed to 6445 frames (23 clips off by ±1 from fps-filter rounding); all 23 re-rendered with exact frame caps, all masters exactly 6432 frames.
- Parent motion audit on the delivered master: mean diff 2.838, total frozen 0.583s, longest near-dup 22f (S07 "We've" onset, under the 24f gate) — passes, frozen total better than the viewing cut's 0.625s. Mouth-state cut pass: exactly 1 violation, adjudicated (S02a→filler cut during the disclosed unmouthed "roads" micro-gap); all other 103 cuts land on word boundaries or in silence.
- Coverage: volley 17 closed S07, S21, S04a (GAP-A lead); structural slots covered by assembly (GAP-B 3-shot cover, S12-cover, S11-cover, S02 accent, C2-hook1 reaction shot). Warp-rescue holds from 2026-11-03 stand. Full micro-gap list in `V6_ASSEMBLY_MAP_2026-11-04.md` §3.
- DISCLOSED, not hidden — volley-17 character inconsistency: S04a 34.56–41.30, S07 72.28–80.78, S21 205.20–214.44 (~24.5s) show a different cartoon face from the night-VOICE of every other slot (daytime other performer: darker skin, rounder face, gold chain, daytime open-road setting; costume/props/style match, face does not). Volley 18 restages came back photorealistic with legible on-screen text and were rejected; the 6-video task cap is spent, so the restage route is closed and the assembly keeps these takes with the inconsistency disclosed.
- Open ear items carried in the delivery note: performed chorus line ("we've been slamming the danger roads" vs sheet "weaving and slamming, the danger grows") — captions + S07/R2/R8 mouths use performed words; if the ear hears "weaving", those takes need revisiting. GAP-C "first"=fast class provisional.
- Full record: `V6_ASSEMBLY_MAP_2026-11-04.md` + `VOLLEY17_GAP_COVERAGE.md` + `VOLLEY18_RESTAGE_COVERAGE.md`; intermediates in `masters_work_v6/` (cutlist, captions, final motion audit, outputs record). V6_DELIVERED.flag created 2026-11-04; mv-v6-stay-alive-nag disabled on delivery per its founding order.

## V7 — Q6 restage + re-cut (delivered 2026-11-12, parent-finished)

- Master: `masters/mv2_toll_roads_are_dumb_v7_16x9.mp4`, md5 `701fa50b19f6697fb37511dec6f932eb`, 82,739,324 B, 1280x720/24fps, 6432 frames DECODE-counted, 268.010s, h264 + AAC 48kHz stereo, SEI crf=18.0, faststart (moov@36). Chat copy: `masters/mv2_toll_roads_are_dumb_v7_16x9_chat.mp4`, md5 `050161faa8ee5941c1abefdad77ac74c`, 32,701,938 B, 6432 frames, audio PCM md5 == house (`f8371c2b5dbd9ebc389b9a11d1bc0428`).
- Parent gates (gate_v7_parent.py + motion_audit_v7_parent.py, logs in `masters_work_v7/`): ALL PASS. Audio agreement vs track.mp3 min corr 0.9981 across 10 windows. Captions: v6 .ass reused unchanged (396 Dialogue events, 0 double-backslash lines).
- Restages (work/q6/Q6_VERDICTS.md + Q6_LEDGER.md): S04a warped t1 (22/22, ratio 0.804, tau 0–8.38, factor 1.2433), S07 t2 (10/10, ratio 1.190, tau 0–7.14, factor 0.84), S21 t1 (13/14, dropped-"to" micro-gap — song word "to" 211.18–212.60 unmouthed, caption carries it; same class as the v6final take). S07 t1 REJECTED (frame FAIL run 33 + legible red STOP signs). Night-VOICE lock closes the volley-17/18 face inconsistency disclosed on v6 — all three slots now show the night-VOICE face.
- Re-cuts (work/q6/Q6_RECUT.md): filler source switches at 121.76 (V2/C2) and 165.34 (C2/Bridge); S25 place-beat re-cut — the ticket place now lands ~254.2, post-line, where v6 skipped take tau 2.20–5.72 entirely. Section boundaries: NO MOVES — the v6 cutlist already tracked every measured line boundary exactly (0.00 on all 7); the audit's "1.5–2.5s early / 2.51s late" numbers described the prepro 10s grid + LYRIC_TIMELINE bracket estimates, NOT the cutlist.
- Frame-count fix: c786bbd9's first v7 silent build was 6448f (22/106 clips off by ±1 from fps-filter rounding — the same trap that made v6's first build 6445f). 2293be03 fixed it in assemble_v7.py + repair_v7.py (-t +0.021s, -frames:v n, tpad clone for take-end clips); rebuilt silent md5 `e06a4fe64f95ceb142f6f2c7c9e80792`, decode-counted 6432. OPEN: how v6 landed exactly 6432f despite the same rounding trap in its identical render command is still unexplained (v6 clips deleted).
- Encode: preset medium (v6 used veryfast — disclosed). Soundtrack = untouched track.mp3 (md5 `9e5ff10876cda8ac17dcb22b79c3f00a`).
- Motion audit on the delivered master: mean diff 3.37; ONE run >=12f, 18f @184.96–185.67s during words — frame-identical to v6's run in the same R4 filler clip, INHERITED, not new. v6 had 2 runs; v7 has 1 (the S07 run is gone — t2 fixed it). PASS, no new frozen runs.
- Mouth-at-cut (parent full-res eye reads, frames in work/q6/gate/): S04a "Now" @34.56 OPEN, S07 "We've" @72.28 OPEN, S21 chorus burst @205.20 OPEN. S21 caption "The wrecks just come." verified against measured words. Kinetic highlight leads the word by ~0.1s (styling, within tolerance).
- DOUBLE-REVIVE incident: original coordinator ccfb1530 INTERRUPTED 12:19:21 EST in a daemon restart; BOTH revive detectors fired (sprint detector a6816deb 12:21:05 + MV detector c786bbd9 12:22:37). 7 videos fired vs cap 3. a6816deb's cp overwrote the sibling's 3 canonical takes — repaired 12:39 (restored from raw media-generation files, md5-verified). Root cause: the sprint detector's scope is every live registry task without covered_by; covered_by=mv-coordinator-revive-detector now set on all live MV tasks. q6b alternates on disk (S21 q6b t1 14/14 — the only full S21 in the catalogue; S07 q6b t1 10/10, motion mean 1.618).
- Recovery chain: c786bbd9 CANCELLED 13:08:52 EST before finishing; revive #2 2293be03 built both masters, then CANCELLED 14:06:51 EST with gates/ledger/flag/report undone; PARENT finished from disk (no re-assembly, no re-encode). v6 untouched (md5 `b2d386bf138aa5e3b654a8382b7b68c0` re-verified).
- MV2_V7_DELIVERED.flag written at project root 2026-11-12. Q6 CLOSED. MV-2 lyrics redo chains next, on the v7 base.

## V7 LYRICS REDO — delivered 2026-11-12 (coordinator dc435200, parent-finished)

- User playback verdict 2026-11-12 ~12:41 EST (on the MV-3 Q5 master, applying to this track last): "lyrics on screen are wrong and no alignment to music." Lyrics + timings ONLY — reassembly from the v7 base, no new generation, no re-shoot.
- Master: `masters/mv2_toll_roads_are_dumb_v7_16x9_lyrics.mp4`, md5 `18baecc2a1c4728b20802789e2332c74`, 82,719,691 B, 1280x720/24fps, 6432 frames DECODE-counted, 268.010s, h264 + AAC 48kHz stereo, SEI crf=18.0, faststart (moov@36). Chat copy: `masters/mv2_toll_roads_are_dumb_v7_16x9_lyrics_chat.mp4`, md5 `7d0c7aafdf925972f4ef904582a357b7`, 26,418,959 B, 854x480/24fps, 6432 frames, audio PCM md5 == house (`f8371c2b5dbd9ebc389b9a11d1bc0428`). v7 + v6 masters untouched (md5s re-verified in the gate).
- Method: hybrid Whisper — large-v3-turbo full-clip backbone (361w) + base-model times for the chunk-3 suppression zone + MDX-stem vocals (no_repeat_ngram=0) for 4 disputed spans. NO VAD. The audio decides, never the sheet or the old .ass. Full record: `work/lyrics-redo/LYRICS_REDO_NOTES.md` + `SONG_WORDS_REDO.json` (48 lines, 401 words, 1 interpolated) + `diff_report_redo.json`.
- Headline fixes (old caption → song): chorus line wrong ×3 — "We've been slamming the danger roads" → "Weaving and slamming, the danger grows" (@72.12 / 143.94 / 214.40; turbo + Suno lyric video agree — the v6 open ear item is RESOLVED, and the sheet was right all along); "make your pay. the roll" → "make you pay to roll"; "your speed for $1" → "you speed for a dollar"; L34 sheet "going to get it when the timing's up" → performed "Somebody's gonna get it when the time ends up"; L42 sheet "Fast lanes make crashes" → performed "Fast lanes may crash it" ×2; parenthetical echoes ARE sung (L41/L43/L44); 7 garbled old lines dropped, 2 new lines added (L42, L48 outro repeat). Words: 29 changed, 21 added, 8 dropped; 345 timing shifts, median |shift| 0.14s, max 1.47s.
- .ass: `work/lyrics-redo/mv2_kinetic_redo.ass`, 392 events, max est width 952px (cap 1100, fs 30, no scaling), 0 double-backslash lines, 1 BLOCK line (L42 — 0.02s "it."). Encode: v7 silent + new .ass + `~ WuBu ~` bug + track.mp3, CRF 18 preset medium, AAC 192k, faststart. finish_lyrics.py died after the master encode (runtime reaper) — chat encode re-run separately; outputs_lyrics.json written by hand from verified values.
- Gates (`gate_lyrics_parent.py`, ALL PASS): 6432f decode-counted, SEI crf=18.0, AAC 48k stereo, faststart, audio agreement vs track.mp3 min corr 0.9981 (10 windows), decoded-PCM audio md5 == v7 base. Motion audit: mean diff 3.38 (v7: 3.37); ONE run ≥12f — 18f @184.96–185.67s during words, frame-identical to v7's inherited run; NO NEW frozen runs. Regression vs v7: caption-free @2.0s pixel-identical (mean|diff| 0.000), @265.0s noise-only (0.687); top-half at captioned time 0.781 (no caption leakage).
- Full-res burned-kinetic eye reads (9 frames in `work/lyrics-redo/gate/`): L01/L03/L14/L17/L34/L35/L41/L42/L48 all legible, nothing cut at edges, first words full-opacity at line starts, bug correct on every frame. L35's 2nd "toll" highlight lands on the interpolated 184.38.
- DISCLOSED, not hidden: Q6 S07 t2 + C2/C-ext slots MOUTH the old mishear ("We've been slamming") while the song and captions now say "Weaving and slamming" — a property of the v7 base, not fixed by this lyrics-only redo. L42 renders whole-line white (block). L35 2nd "toll" @184.38 interpolated. L18 "somebody" 0.38s late vs the stem. L42's first frame (5436 @226.50, the only exact frame-boundary line start) renders empty — caption present from frame 5437 (226.54); libass float-rounding artifact, 42ms, no impact.
