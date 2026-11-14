# MV-3 "I Am Your Dad (HE IS NOT YOUR DAD, RUN)" — ASSEMBLY REPORT

Delivered 2026-11-04. Song: Suno track, 354.816s, master audio `track.mp3`
(md5 4948827344208de31df17dd9d2e52799) used untouched for all three finals;
every generated clip's audio was dropped. Performer: MONSTER MAN IN A SUIT
with a BIG YELLOW BALL SMILEY HEAD (this track only — not THE VOICE, not UNC).

Build note: the assembly agent finished all three finals, then died at ~13:38 EST
(transport error) before writing this report or running the motion audit. The
parent recovered from disk: verified the finals, found the chat copy truncated
(no moov atom — ffmpeg died mid-encode), rebuilt it from the verified 16:9
final with the same settings, ran the motion audit on the delivered masters,
and wrote this report. No take, caption, or placement was changed in recovery.

## Delivered files (parent-verified by md5 + ffprobe + full decode)

| File | md5 | Size | Spec |
|---|---|---|---|
| `mv3_i_am_your_dad_16x9.mp4` | 4df7a121a38a064527dd8fb3bd23d715 | 82,501,934 B | 1280x720, 24fps, h264 + AAC 48kHz stereo, faststart, 8516 frames, 354.833s |
| `mv3_i_am_your_dad_9x16.mp4` | d5eba46319f9795365f247fa5aab3ddc | 102,011,016 B | 720x1280, 24fps, h264 + AAC 48kHz stereo, faststart, 8516 frames, 354.833s |
| `mv3_i_am_your_dad_16x9_chat.mp4` | ff5826aebe7a38eb6d5970dbebae19ae | 23,818,682 B | 854x480, 24fps, h264 + AAC 48kHz stereo, faststart, 354.833s |

Duration vs song length: 354.833s vs 354.816s = +0.017s (0.4 frames, inside the
±2-frame tolerance). Frame count is exactly the song frame count (8516) on
both masters. Full-decode check on both masters: exit 0, no errors (rules out
truncation). 9:16 is a proper per-scene reframe (crops.json centroids), NOT a
blind crop — verified on frames: performer centered, bug and captions intact.
Captions are BURNED (MV-2 v6 precedent — iPhone chat playback needs them),
word-timed from the PERFORMED words (LYRIC_TIMELINE.md), with the
`~ WuBu ~` corner bug on both masters (verified on delivered frames at 100s:
bug top-right in gold; caption shows the performed line).

## Scene placement (frame-exact, 24fps; segment runs to the next scene start)

| Scene | Start | Take(s) | Warp | Seg frames | Cover note |
|---|---|---|---|---|---|
| LEADER | 0.00 | S01 frame 0 held | — | 68 | Pre-first-word hold only (see disclosures) |
| S01 | 2.82 | s01_t2 | 1.088 | 156 | |
| S02 | 9.32 | s02_t2 | 1.040 | 216 | |
| S03 | 18.34 | s03_t1 (cutaway) | 1.382 slow-mo | 332 | Instrumental window, no words |
| S04 | 32.16 | s04_t1 partial 0–4.40s | 1.0 | 105 | Structural video cover; master carries the line |
| S05 | 36.56 | s05_t1 partial 0–3.50s | 1.0 | 84 | Structural video cover; master carries the line |
| S06 | 40.06 | s06_t1 | 1.0 | 194 | |
| S07 | 48.12 | s07_t1 | 0.975 | 168 | |
| S08 | 55.14 | s08_t1 | 1.0 | 180 | |
| S09 | 62.64 | s09_t1 | 0.884 | 138 | |
| S10 | 68.36 | s10_t1 | 1.0 | 190 | |
| S11 | 76.28 | s11_t2 | 0.975 | 159 | |
| S12 | 82.92 | s12_t2 | 0.8375 | 186 | |
| S13 | 90.66 | s13_t1 | 1.0 | 216 | |
| S14 | 99.68 | s14_t1 | 1.0 | 222 | 6f tail-loop cover |
| S15 | 108.92 | s15_t1 | 1.0 | 173 | |
| S16 | 116.14 | s16_t1 | 1.0 | 183 | |
| S17 | 123.74 | s17_t1 | 1.0 | 137 | |
| S18 | 129.46 | s18_t2 | 1.0 | 169 | |
| S19 | 136.52 | s19_t1 | 1.0 | 174 | |
| S20 | 143.76 | s20_t1 | 0.9625 | 157 | |
| S21 | 150.30 | s21_t2 | 1.0 | 250 | Structural; 10f tail-loop cover |
| S22 | 160.70 | s22_t1 | 1.0 | 193 | |
| S23 | 168.76 | s23_t2 (grey) | 1.216 to 1.25 edge | 343 | 51f tail-loop cover |
| S24 | 183.06 | s24_t2 | 1.0 | 293 | Structural; 53f tail-loop cover |
| S25 | 195.24 | s25_t1 + s25_t2 | 1.0 | 484 | Structural; 28f tail-loop cover |
| S26 | 215.40 | s26_t1 | 1.0 | 125 | |
| S27 | 220.64 | s27_t1 | 1.0 | 237 | 21f tail-loop cover |
| S28 | 230.52 | s28_t3 (grey) | 1.256 to 1.25 edge | 350 | 49f tail-loop cover |
| S29 | 245.10 | s29_t1 | 0.8375 | 143 | |
| S30 | 251.04 | s30_t3 | 1.0 | 175 | Structural |
| S31 | 258.32 | s31_t1 | 1.240 | 244 | |
| S32 | 268.50 | s32_t1 | 1.040 | 240 | 15f tail-loop cover |
| S33 | 278.50 | s33_t1 (mantra thirds) | 1.032 | 223 | Cut on beats |
| S34 | 287.80 | s34_t1 | 1.0 | 214 | Usable 1.15 |
| S35 | 296.70 | s35_t1 + s35_t2 partial 0–4.18s | 1.0 | 316 | Structural |
| S36 | 309.88 | s36_t2 (grey) | 1.112 to 1.25 edge | 293 | 53f tail-loop cover |
| S37 | 322.08 | s37_t1 + s37_t1 replay 0–7.46s | 1.0 | 395 | Assembly decision; replay fill, moving video |
| S38 | 338.55 | s38_t2 (grey) | 0.9125 to 0.80 edge | 144 | Strengthened oval spec, 3/3 proven |
| S39 | 344.55 | s39_t1 (mantra) | 1.0 | 247 | Assembly decision; 31f tail-loop cover |

Grey warps are to the band edge only (≤1.5x), per the MV-2 rule. Tail-loop
covers replay the take's own post-line tail video (moving), never a freeze.
Overshoot takes are trimmed by the segment cut; no scene runs past its slot.

## Motion audit — ON THE DELIVERED MASTER FILES (motion_audit_mv3.py)

Decoded to 160x90 gray; near-dup = mean abs diff < 0.5 (QC convention);
word windows = LYRIC_TIMELINE line spans.

| Master | Frames | Mean diff | Exact-dup frames | Longest near-dup overall | Longest near-dup during words |
|---|---|---|---|---|---|
| 16:9 | 8516 | 1.611 | 0 | 67f (0.00–2.79s, pre-word leader hold) | 57f (347.08–349.46s, outro) |
| 9:16 | 8516 | 2.980 | 13 | 67f (leader) | 35f (350.46–351.92s, outro) |

GATE FINDING, STATED PLAINLY: the brief's <24f during-words gate is NOT met
as written on either master (57f / 35f). Follow-up checks show what those
runs actually are:

- ZERO exact-duplicate frames in the 16:9 master (13 in 9:16, from warp
  frame-duplication — negligible across 8516 frames).
- Inside the worst flagged runs, consecutive-frame diffs are all nonzero
  (16:9 outro run: min 0.109, max 0.487, mean 0.282; S25 run: mean 0.260;
  no zeros anywhere in the flagged runs).
- Full-resolution 1-second-apart diffs inside the flagged runs: 1.8–4.1.

So the flagged runs are continuous SLOW DRIFT, not frozen frames — the
deadpan monster shot drifts below the 0.5 audit threshold at 160x90, where
the performer fills less of the frame than MV-2's crooner did (MV-2 v6 mean
2.838, max run 22f). The 0.5 threshold, calibrated on livelier material,
flags slow motion as near-dup. Motion is present everywhere words play; the
picture never actually freezes during words. The only true freeze is the
disclosed pre-first-word leader hold (0–2.82s, before any word — the one
freeze the assembly design allows).

This is disclosed, not passed off: the gate miss is a threshold-calibration
issue on slow, deadpan material, and the user's own playback verdict
outranks this audit either way.

## Disclosures (complete)

- Leader hold: S01 frame 0 held 0–2.82s before the first word. Only freeze.
- Structural video covers (S04, S05, S21, S24, S25, S30, S35): denied/partial
  takes as video only; the untouched master audio carries every line.
- Tail-loop covers on S14, S21, S23, S24, S25, S27, S28, S32, S36, S39
  (6–53f each): replayed post-line tail video, moving, cut on scene bounds.
- S03 slow-motion 1.382x fills an instrumental window (no words).
- S37 replay fill: s37_t1 replayed from its start to fill its 16.36s slot.
- Grey warps to band edge only: S23 1.216x, S28 1.256x, S36 1.112x,
  S38 0.9125x. Gates re-run on warped output at QC time.
- Captions burned into both masters (MV-2 v6 precedent); performed words,
  not the abridged lyric sheet, where they differ.
- Chat copy was rebuilt by the parent (same settings) after the assembly
  agent's death left it without a moov atom; the 16:9 and 9:16 masters are
  the agent's own files, verified complete by full decode.
- 9:16 reframe uses per-scene centroids (crops.json); the performer stays
  centered and the bug/captions stay in frame.
