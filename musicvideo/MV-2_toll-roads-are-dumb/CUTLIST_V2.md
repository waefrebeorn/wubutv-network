# CUTLIST V2 — MV-2 "Toll Roads Are Dumb" (THE VOICE)

Engine v2 first proof run. Track: track.mp3, 268.01s, md5 9e5ff10876cda8ac17dcb22b79c3f00a (sole master audio, muxed untouched).
NO peak warp, NO time-stretch of the song, NO stretching a short line to a scene. Trims only, from take start. Captions: subtitle track from LYRIC_TIMELINE.md (captions_v2.srt), never burned. Corner bug ~ WuBu ~ added in assembly. V1 masters + v1 CUTLIST.md kept untouched; v2 ships as NEW files.

## Why the cuts sit where they sit (read before judging alignment)

27 takes × 10.000s = 270s of footage must cover a 268.01s song, so total
trim across the whole cut is 1.99s — every scene is ~10s by arithmetic
force, not by choice. Cuts 1–16 sit on the 10s grid; from 168.01 on, the
1.99s of slack is spent so cuts track true line boundaries within
0.01–2.51s (178, 188, 198, 218, 248 essentially exact; 167.5 within
0.51s; 229.5 within 1.49s; 238.5 within 0.49s). Section-boundary error
vs LYRIC_TIMELINE.md: Intro/V1 2.5s early (cut 10 vs 12.5), V1/C1 1.5s
early (50 vs 51.5), C1/V2 1.5s early (90 vs 91.5), V2/C2 1.5s early
(120 vs 121.5), C2/Bridge 2.51s late (168.01 vs 165.5 — the worst
remaining misalignment, disclosed), Bridge/C-ext 1.99s early (188.01 vs
190), C-ext/Outro 0.49s early (238.01 vs 238.5). The outro error that
killed v1 (outro scenes starting 8.5s early, mantra repeat playing over
"It ain't worth the crash") is closed: the outro cut sits 0.49s before
the true outro start, inside bracket measurement tolerance.

## Scenes (song time | active take | trim from take start)

| Scene | Song time | Active take | Trim |
| --- | --- | --- | --- |
| S01 | 0–10 | mv2_s01_t2.mp4 | 0–10 |
| S02 | 10–20 | mv2_s02_t3.mp4 | 0–10 |
| S03 | 20–30 | mv2_s03_t2.mp4 | 0–10 |
| S04 | 30–40 | mv2_s04_t3.mp4 | 0–10 |
| S05 | 40–50 | mv2_s05_t3.mp4 | 0–10 |
| S06 | 50–60 | mv2_s06_t2.mp4 | 0–10 |
| S07 | 60–70 | mv2_s07_t2.mp4 | 0–10 |
| S08 | 70–80 | mv2_s08_t1.mp4 | 0–10 |
| S09 | 80–90 | mv2_s09_t2.mp4 | 0–10 |
| S10 | 90–100 | mv2_s10_t1.mp4 | 0–10 |
| S11 | 100–110 | mv2_s11_t2.mp4 | 0–10 |
| S12 | 110–120 | mv2_s12_t3.mp4 | 0–10 |
| S13 | 120–130 | mv2_s13_t2.mp4 | 0–10 |
| S14 | 130–140 | mv2_s14_t1.mp4 | 0–10 |
| S15 | 140–150 | mv2_s15_t2.mp4 | 0–10 |
| S16 | 150–160 | mv2_s16_t1.mp4 | 0–10 |
| S17 | 160–168.01 | mv2_s17_t2.mp4 | 0–8.01 (192 frames) |
| S18 | 168.01–178.01 | mv2_s18_t1.mp4 | 0–10 |
| S19 | 178.01–188.01 | mv2_s19_t1.mp4 | 0–10 |
| S20 | 188.01–198.01 | mv2_s20_t2.mp4 | 0–10 |
| S21 | 198.01–208.01 | mv2_s21_t1.mp4 | 0–10 |
| S22 | 208.01–218.01 | mv2_s22_t1.mp4 | 0–10 |
| S23 | 218.01–228.01 | mv2_s23_t1.mp4 | 0–10 |
| S24 | 228.01–238.01 | mv2_s24_t1.mp4 | 0–10 |
| S25 | 238.01–248.01 | mv2_s25_t2.mp4 | 0–10 |
| S26 | 248.01–258.01 | mv2_s26_t2.mp4 | 0–10 |
| S27 | 258.01–268.01 | mv2_s27_t2.mp4 | 0–10 |

Total: 16×10 + 8.01 + 10×10 = 268.01s. Video frames: 26×240 + 192 = 6432 frames (268.0s video, 268.01s audio — 1 frame of audio tail, same convention as v1).

## Take notes

- S26: t2 active (re-plan restage, sing-first then silhouette, QC-passed on widened sample 2026-11-01). S26 t1 retired from the cut, kept on disk.
- All other takes are the QC-passed v2 set (11 performance-window re-fires + flat re-fire t2/t3 set + audit-KEEP t1 takes). No take enters the cut without a QC row; no failed gate is open. Text flags from v1 (S11, S15, S17 t1 takes) are GONE — those scenes use their QC-passed t2/t3 takes.
- Recurring nits (disclosed, not fails): pocket square reads blue/red-orange in many takes vs CADMIUM; S26 t2 mic handheld + mid-take turn; S11 t2 turn lands mid-take; S25 t2 place beat lands early at 5s; S07 t2 gantry signal green arrows (signals, not letters).

## Masters (verified 2026-11-01, ffprobe + md5)

- masters/mv2_toll_roads_are_dumb_v2_16x9.mp4 (1280x720) — md5 `58a1da0f0d47e97092b88274f7e4f49e`, 52,296,097 bytes, 268.032s container
- masters/mv2_toll_roads_are_dumb_v2_9x16.mp4 (720x1280, blurred-pad reframe of the same cut) — md5 `85fbe2a2f18fafbf9325d57bc6067e6e`, 39,304,621 bytes, 268.032s container
- Both: h264 video (6432 frames @24fps = 268.0s) + mp3 master audio copied untouched from track.mp3 (sample-identical in the tested 30s stretch at 100s; 22ms trailing padding difference only) + mov_text subtitle track (48 cues from LYRIC_TIMELINE.md) + ~ WuBu ~ corner bug, verified present in sampled frames.
- Spot-checks at line starts: 237.9s S24 t1 → 238.5s S25 t2 across the 238.01 outro cut; 257.9s S26 t2 silhouette → 258.5s S27 t2 vocal across the 258.01 cut; bug present in all sampled frames.
