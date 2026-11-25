# MV-4 Lyrics Redo — Notes (2026-11-12)

User playback verdict ~12:41 EST (on the MV-3 Q5 presentation): "lyrics on screen
are wrong and no alignment to music" — redo the lyrics + timings for MV-4
(This Time It's Real), MV-5, MV-6, MV-2. This file is the MV-4 record.

## What was wrong — the short version

The old caption TEXT was (almost) right; the old caption TIMES were wrong.
The old word grid came from faster-whisper BASE + hand-normalizations
(`work/merge_words.py`). The new grid is faster-whisper **large-v3-turbo**
(full clip, no VAD, pinned params — see Method). Against it:

- **81 of 360 words moved >0.10s; median |shift| 0.22s.** The karaoke
  highlight was typically a fifth of a second off the sung word — visible
  as "no alignment to music" on every line.
- **21 words moved ≥0.5s**, including line starts: L06 "That's" −1.14s
  (old line appeared 19.76, word sung 18.62), L19 "But" −0.86s, L51
  "Futurama's" +1.50s (old line appeared 190.40, word sung 191.90),
  L26 "Futurama's" +0.66s, L42 +0.62s, L12/L29/L45 "that's" +0.56–0.78s.
- **The outro was the worst of it.** Old L54 put the second "No more coming
  on" repeat at 207.46–210.75 (the new model hears it ~206.7–212.0, soft and
  slurred); old L55/L56/L57 mis-stacked the soft outro repeats, and old L57
  was a single 17.26s static block ("Good news, everyone. / For real this
  time.") sitting through ~10s of silence (220.77–230.56) before the phrases
  are actually sung at 230.56 and 234.24. Worse: the old L57 block burned
  the lyric sheet's stage direction on screen — the delivered master
  literally shows "Good news, everyone. / For real this time. (repeat,
  soft)" for 17 seconds (old .ass line 359). The redo splits it into two
  clean per-phrase blocks with no stage direction.
- **Grid mislabels broke karaoke on two lines.** Old grid heard L14 "Good
  news" as "Cut news" and L29 "Good news" as "Could news" — the karaoke
  count rule failed, so both lines were block-only in the delivered master.
  The new grid hears both correctly; both are karaoke now.
- **Low-confidence anchors everywhere in the old grid:** 70/360 words
  prob <0.5, including line-start words (They 0.096, Then 0.194, Hulu
  0.247, Good 0.103, For 0.003, Not 0.096). The new grid has 18/364 words
  prob <0.5. First word "They" was 0.00–1.46s in the old grid (a back-fill
  artifact); the new grid gives 0.00–1.42s at p=0.302 — still low-prob,
  but the time is corroborated by the segment boundary (the song starts
  at 0.00) and the next word "said" at 1.42.

## What the audio actually says (word identity)

The Suno lyric video (`track.mp4`, the track's own displayed lyrics) was
read frame-by-frame at all 57 line midpoints (`lyric_video_contact.png`):
it confirms the sheet's line identity on **all 57 lines** — "Matt said",
"Hulu hit rewind", "Good news, everyone", "No more coming on", all as
written. The new ASR's performed-vs-sheet differences are slurs and
garble, never a confident different word, so **the caption text is the
sheet text throughout** — this redo is a timing redo + karaoke re-stepping.

Identity changes (28 total, new vs old grid): almost all are spelling or
number renderings of the same sung word — "Futurama's" spelled
Futuramas / Futuramma's / Futuramah's / FUTURAMMA's (ASR spelling noise),
"Fourteen" written "14", "twenty-thirteen" written "2013",
"twenty-seven" written "27". Genuine corrections (old grid label wrong,
sheet text was already right):
- L18 "then" (old grid "and" p=0.167; new "then" p=1.0)
- L22 "We've" (old "We"; new p=0.938)
- L23 "Then" (old "The" p=0.377; new p=0.634)
- L24 "song's" (old "songs"; new p=0.902)
- L36 "We'll" (old "No" p=0.192 — the base model misheard it; new p=0.667)
- L40 "ones" (old "one"; new p=0.904)
- L47 "done" (new hears "gone" p=0.0; old grid "done" p=0.991 + video confirm)

Slurs kept as sheet words (the singer's articulation, not a different word):
- L27 "For" sung as "More" (new p=0.895 at 99.24) — caption shows "For".
- L24 "this" sung as "the" (L24 stays block-only for this reason).
- L31/L48 "everyone" guessed as "everybody" (p=0.0) — caption shows "everyone".
- L44 second "Futurama's finished" garbled ("our Futuramas finish") — block-only.

## Method

- Transcription: `work/lyrics-redo/transcribe_large.py` — faster-whisper
  large-v3-turbo int8, cpu_threads=2, NO VAD, numpy-array input from
  `work/track_16k.wav`, pinned "en", condition_on_previous_text=False,
  beam 1, repetition_penalty 1.1, no_repeat_ngram 3, collapse runs >5, no
  initial prompt. Venv `~/workspace/tools/lyrics-venv/` (faster-whisper
  1.2.1, av 18.1.0). Output `song_transcript_large.json`: 55 segments,
  364 words.
- **OOM lesson (blade):** the first run was killed at 79.44s of 238.8s —
  three sibling large-v3-turbo transcriptions (MV-3, MV-5, MV-6) were
  running concurrently (~5GB RSS on the 6GB blade) plus an MV-2 encode.
  Re-ran after MV-6 finished; completed in ~8.5 min. Rule: ONE
  large-v3-turbo transcription at a time on this blade.
- Slice check: `slice_outro.py` re-decoded 200–218s in isolation. It
  confirms L54's second repeat and L55's second repeat are sung softly
  and slurred — no ASR pass hears them cleanly (full-clip: 5s garbage
  "off" p=0.001; slice: "No, no, no" + "Don't lose/use everyone").
  The old base grid's high-prob words + the video confirm the lines
  exist; their karaoke times are not measurable, so L54/L55 are block-only.
- Diff: `diff_words.py` (difflib alignment new vs old; timing shifts
  >0.10s; old-only/new-only; per-line sheet-vs-ASR check) →
  `word_diff_report.txt` + `word_diff.json`.
- Captions: `make_captions_redo.py` → `mv4_kinetic_redo.ass`
  (322 events: 314 karaoke steps + 8 block events).
  - Aligns the new ASR sequence to the sheet's full token sequence
    (difflib, in order). **Trap found and fixed:** the global matcher
    jumps identical repeats — L55's second "everyone" matched L57's
    repeat 14s later (validation caught it: span 211.62–234.24 vs old
    211.75–216.73). Every line's span is validated within 3s of the old
    span; failures are re-aligned locally in [ls−1.5, le+1.5].
  - `norm()` strips apostrophes (sheet "Futurama's" == ASR "Futuramas");
    `ASR_ALIASES` canonicalises the track's observed ASR confusions
    (Futuramma's/Futuramah's → Futurama's; 2013 → twenty-thirteen;
    14 → fourteen; 27 → twenty-seven; everybody → everyone;
    gone → done). Each alias is unambiguous on this track and verified
    against the video and/or the old grid.
  - Karaoke rule: assigned count == token count, strictly increasing,
    every duration >0.05s; else one block event spanning the line's sung
    words (extended to unassigned edge words, never crossing into the
    neighbouring lines' words). 52 lines karaoke; 5 block (L24, L27, L44,
    L48, L55); L54 forced block; L57 split into two per-phrase blocks.
  - Per-line fs scaling (MV-13 fix): est width = len×0.52×44×1.06,
    capped at 1100px. fs 42 on the four 10-word "For real this time…"
    lines + L27; fs 39 on L04 (48 chars). Everything else fs 44.
  - Single backslashes only (MV-12 fix): **0 double-backslash lines**
    (verified by the builder). No `\fad` (the old .ass had none either).
  - Overlap check: 322 events, no overlaps (abutting allowed).
  - L57's old 17.26s static block is replaced by two blocks:
    "Good news, everyone." 230.56–234.24 and "For real this time."
    234.24–238.02; the 220.77–230.56 silence stays caption-free, and
    the "(repeat, soft)" stage direction is no longer burned on screen.
- No `text_overrides.json` was needed: no line's performed words
  genuinely differ from the sheet (see Identity above).

## Line table (new spans; old spans in LYRIC_TIMELINE.md)

52 karaoke, 5 block, L54 block, L57 2 blocks. Biggest line-start fixes:
L06 19.76→18.62, L19 72.80→71.94, L26 95.40→96.06, L42 158.76→159.38,
L51 190.40→191.90, L54 205.09→204.04, L55 211.75→211.62, L57 220.77→230.56
(first phrase). Full per-line report is the builder's stdout (saved in the
run record below).

## Build

- `work/lyrics-redo/assemble_mv4_lyrics.py` — copy of `assemble_mv4.py`
  with the subtitles filter pointed at `work/lyrics-redo/mv4_kinetic_redo.ass`
  and the output at `masters/mv4_this_time_its_real_16x9_lyrics.mp4`.
  Same takes, warps, montage, bug, and encode settings as the delivered
  master (libx264 CRF 18, yuv420p 1280×720 24fps, AAC 48k 192k, faststart).
  The base master is untouched (md5 dca20f5c1bc4878a30897291be4911c7).
- Encode launched detached (setsid/nohup) ~18:40 EST; ~21+ min (longer
  with the MV-2 v7 encode sharing CPU). Log:
  `work/lyrics-redo/assemble_lyrics.log`.

## Gates (on the new master)

First master (md5 `1456487dde2be81577fbb0b69c07acd4`, 129,340,998 B,
encoded 19:20 EST): **ALL PASS with the fixed gate (v2)** — see the
diagnosis below. The parent then ordered a re-encode as confirmation;
it finished 21:49 EST and produced a **bit-identical file — same md5,
same size, same bytes** — so the v1 master IS the final master. The
re-encode was re-gated with the fixed gate (v3, log `gate_lyrics_v3.log`):
**ALL PASS, numbers identical to v2** (they must be — the file is the
same). The v1 backup was removed after the md5 match was verified
(it was byte-identical, not a fallback).

- Frame count exact 5731f vs base ✓; 238.805s; 1280×720; h264 24fps;
  AAC 48k stereo; SEI crf=18.0; faststart (moov before mdat) ✓.
- Decoded-PCM audio md5 `dc29cad83fa22b35a17cc3bf1de85d7a` — identical
  to the base master ✓.
- Motion audit: no NEW frozen runs ≥24f vs base. (Base's 27f run
  @30.92–32.04s in the no-word gap is present in both; small 12–20f
  deltas at 74.25/130.12/141.58/158.17s are caption-pixel effects on
  the frame-diff, all under the bar.)
- Regression (alignment-aware, fixed gate): offset 0 is the best match
  at all six sample times (20/63.59/100/156.89/200/225.91s), top-half
  mean|diff| 0.000–1.117; wordless/captionless gaps 0.682–1.737, all PASS.
- Full-res burned kinetic frame reads (`frame_reads/`, 1280×720): **7/7
  PASS**. L01 @0.00 "They" highlighted, fully opaque (no mid-fade faint
  — no `\fad` in the .ass); L04 @11.67 "Fourteen" highlighted, fs 39
  longest line fits with room (spans ~95–1150px, nothing cut at edges);
  L06 @18.62 "That's" highlighted; L26 @96.08 "Futurama's" highlighted;
  L27 @99.20 block "For real this time, no more reruns in the dark."
  (shows "For", not the slurred "More"); L51 @191.90 "Futurama's"
  highlighted; L57 @230.58 block "Good news, everyone." only — no
  second phrase, no "(repeat, soft)" stage direction. Note: frame
  selection must use ceil(t×24), not round — round gave frames 1 early
  on L04/L26/L57 (frame timestamp before the event start).
- Chat copy: `masters/mv4_this_time_its_real_16x9_lyrics_chat.mp4`
  (854×480 crf 23, AAC copied untouched) — 46,259,256 B (~44.1 MB,
  ≤50 MB ✓), md5 `5131d33a388385673fa78884b03337c0`, 5731f, 238.805s,
  AAC 48k stereo, faststart ✓. Encoded 22:35 EST.

### Regression diagnosis (the first gate run's FAILURES — gate was wrong, video was right)

The first gate run (v1) failed three regression checks: 100.00s
(top mean|diff|=1.500), 63.59s (1.737), 225.91s (5.152). Diagnosis
(`work/lyrics-redo/diagnose_100s.py`, 7 sample times, NEW center frame
vs BASE center ±2, top half, 640×360 gray):

- **No frame offset.** Offset 0 is the best match (or tied within 0.03)
  at every sample time. At 20.00s, 156.89s, 200.00s the top half is
  BIT-IDENTICAL (0.000). The re-encode did not move, drop, or change
  any video region.
- **The differences are x264 re-encode noise from the changed captions.**
  Both files carry the identical SEI line (x264 core 164 r3108,
  threads=6, crf=18.0, same options) — same encoder, same settings —
  but the caption pixels differ (old .ass vs new .ass), and that shifts
  CRF rate-control decisions for the whole frame. Measured noise at
  offset 0: 0.000–1.117 (top half, downscaled gray); 1.0–1.7 at
  full-res RGB on moving frames. The v1 gate's <1.0 full-res bar was
  too strict for a re-encode, and is retired. (Correction, 21:49 EST:
  the re-encode reproduced the v1 master **bit-identically** — same
  md5, same size — so x264 is deterministic here given identical
  inputs and settings; the "nondeterministic threads" hypothesis in
  the first draft of this note was wrong. The base-vs-new pixel
  differences are the caption change propagating through rate control,
  not thread timing.)
- **225.91s was never a regression.** The "wordless gap" 221.26–230.56
  is wordless but NOT captionless in the base: the old L57 block
  (220.77–238.03) covers it. The 5.152 full-frame diff is the removed
  caption + stage direction — the fix itself. The top-half diff at
  225.91s is 1.117 at offset 0 (best match by 10× over ±1).
- **Gate fix (v2):** regression is now alignment-aware — for each sample
  time, NEW center vs BASE center ±2, top half, 640×360 gray; PASS =
  offset 0 is the best match (or tied within 0.10) AND offset-0
  mean|diff| < 1.5. A real offset/content change would show as a large
  offset-0 jump (6–14 on fast-motion frames) with the best match moving
  to ±1/±2. The 221.26–230.56 gap is excluded from the wordless-gap
  list; the remaining gaps use a <2.0 full-res bar. `gate_lyrics.py`
  also fixed its crf/faststart detection (SEI via `strings`, 2 MB
  moov window — the v1 64 KB window never reached "mdat" and failed
  on the known-good base too).
- The re-encode (21:49 EST) reproduced the v1 master bit-identically
  (md5 `1456487d`, 129,340,998 B), so the assembly + encode pipeline is
  deterministic — the v1 backup was removed after the md5 match was
  verified.

## Q3 note (per-word re-warp — NOT this job)

This job is the caption layer only. The timing audit confirms the take
sync itself was built on the old (wrong) grid: the assembly's segment
boundaries use the OLD first-word times (e.g. S06 boundary 23.34 vs new
first word 23.18; S13 boundary 95.40 vs new 96.06; S26 boundary 188.24
vs new 187.90). The takes were warped to the old grid, so take-level
word sync inherits the old grid's errors — that is Q3's territory and
stays BLOCKED on the snapper stay-rule patch (no sensor). Reported here
with measurements; no takes were re-warped.
