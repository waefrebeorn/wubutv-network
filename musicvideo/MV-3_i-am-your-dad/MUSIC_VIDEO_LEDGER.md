# MUSIC VIDEO LEDGER — MV-3 "I Am Your Dad (HE IS NOT YOUR DAD, RUN)"

Track: `track.mp3` md5 `4948827344208de31df17dd9d2e52799`, 354.816s, 729 words
(SONG_WORDS.json). Character (this track only): MONSTER MAN IN A SUIT, BIG
YELLOW BALL SMILEY HEAD. Eye line in every vehicle, verbatim: "small solid
black oval eyes, no white showing." (POSE_CARDS.md's "two round dot eyes"
is a known conflict — ovals govern.)

## Masters

| Master | md5 | Status |
|---|---|---|
| mv3_i_am_your_dad_16x9.mp4 (v1) | 4df7a121a38a064527dd8fb3bd23d715 | REJECTED by user 2026-11-04 ~19:23 EST — never re-deliver |
| mv3_i_am_your_dad_16x9_recut.mp4 (build 3) | 300c89feaf5276763e0f8598bc2656d6 | delivered + user-accepted 2026-11-05 ~01:20 EST — do NOT re-deliver |
| mv3_i_am_your_dad_16x9_retimed.mp4 | 24af63b9c2e4b64a6f038efb3bd39e3b | RESTART BASE for the corrected build — never overwrite |
| mv3_i_am_your_dad_16x9_corrected.mp4 | (this build) | pending parent gate + delivery |

## Delivery flag — corrected build (defined 2026-11-06, correction run)

- **Flag file: `MV3_CORRECTED_DELIVERED.flag`** (project root).
- Meaning: the corrected master above has passed the parent's own gate
  (md5/ffprobe + mouth-state reads on the master) AND been delivered to
  the user in chat.
- Written ONLY by the parent agent, only after delivery. The correction
  coordinator never writes this flag, never commits, never announces.

## Corrected build (2026-11-06)

Method: MV-5 v4 correction — mouth-event audit on the retimed master
(every line onset + all 96 mantra onsets), per-scene verdicts in
`work/AUDIT_CORRECTED_PLAN.md`, phrase-smooth corrections from existing
takes only (no new generation), gate on the corrected master in
`work/gate_corrected/`, full record in `MV3_CORRECTED_NOTES.md`.
Structural scenes (repeat-drop class, no third reroll, no new fire):
S04, S05, S21, S24, S25, S30, S35.

## Correction run (2026-11-06, MV-5 v4 method)
- Delivery flag for this build: **MV3_CORRECTED_DELIVERED.flag** (parent writes it after its own gate + delivery; the correction coordinator never writes it).
- Audit: mouth state read on the retimed master at all 99 onsets (40 lines + 97 mantra stamps incl. "game"), t and t+0.17s — O 62 · T 13 · o 9 · C 15. Closed in mouth scenes: 8 (S02, S09, S10, S13, S14, S27, S28, S29). Probe strips measured mouth-open times for each. Full record: work/AUDIT_CORRECTED_PLAN.md; reads: work/mouth_events_retimed.json.
- Corrections (pure assembly, corrected_build.py, base = retimed scenes): 13 head-trim SHIFTs (S07 +5f, S08 +4f, S09 +9f, S10 +9f, S12 +4f, S14 +12f, S18 +4f, S19 +4f, S27 +12f, S28 +8f, S29 +16f, S34 +4f, S38 +4f) + S02 phrase-split REWARP (A: take[13f:96f] w=1.4096; B: take[96f:] w=0.825; split at the mantra attack, song 14.22s). S13 = STRUCTURAL disclosure (no mouth opening exists in the only take's head window; no alternate take; generation barred). Captions: captions_16x9_corrected.ass (L02 "game" fix, 7 events).
- Corrected master: masters/mv3_i_am_your_dad_16x9_corrected.mp4 (pending build + gate in work/gate_corrected/).
- Eye-spec conflict (noted per brief): POSE_CARDS.md "two round dot eyes" vs governing vehicle spec "small solid black oval eyes, no white showing" — ovals govern.

### Correction run — outcome (2026-11-06)
- CORRECTED MASTER: `masters/mv3_i_am_your_dad_16x9_corrected.mp4`, md5 `5752200b68e1d816e59ca612712fc7d1`, 82,670,966 B, 1280x720, 24fps, 8516 frames, 354.833s. Awaiting parent gate + delivery (flag MV3_CORRECTED_DELIVERED.flag NOT written).
- Changes vs retimed base: S02 phrase-split rewarp (A w=1.4096 / B w=0.825 at the 14.22 mantra attack); 13 head-trim shifts (S07 +5f, S08 +4f, S09 +9f, S10 +9f, S12 +4f, S14 +12f, S18 +4f, S19 +4f, S27 +12f, S28 +8f, S29 +16f, S34 +4f, S38 +4f); captions fixed to performed words ("game" intro; "dad" outro) in captions_16x9_corrected.ass.
- GATE: (a) audio identical to retimed (framemd5 stream + decoded-PCM md5 match) PASS. (b) mouth at 99 onsets: O 70 / T 18 / o 3 / C 8 (base 62/13/9/15); mouth-scene CLOSED 8 -> 1 (only S13 90.66, structural — no opening exists in the only take); 14 improved, 2 O->T trades disclosed (S28 L30, S29 247.10), 0 worsened to closed. (c) judder PASS (zero in-phrase steps; S02 step on the phrase boundary only). (d) motion PASS for mouth scenes; 3 frozen runs >=24f are frame-identical inheritances in cover takes S25/S35/S39.
- Full record: MV3_CORRECTED_NOTES.md; plan: work/AUDIT_CORRECTED_PLAN.md; gate reads: work/mouth_events_corrected.json.
- Build incident: first final mux killed by the VM reboot 12:37:14Z (Freeq outage #15); intermediate survived (8516f verified); mux re-run standalone to completion.

## Q5 improvement (2026-11-12, program.md Q5 — recovery coordinator)
- Coordinator 3e440d96 (fired both takes, died in a daemon restart 10:45:28 EST
  while QC-ing); recovery resumed from disk, no re-fire (cap spent).
- S13 t2 KEEP (md5 4b0307b5d7fbbd3188ddf7b6661289f4): real articulating mouth,
  open at the head; S39 t2 KEEP (md5 8bdab6f48e1f225c32efc3b42d509c8b): mouth
  open at all four mantra-burst onsets. Both takes sing invented words
  (vehicles carry no lyric quotes) — captions carry the song's words.
  Full verdicts: work/q5/Q5_VERDICTS.md.
- Q5 master: masters/mv3_i_am_your_dad_16x9_q5.mp4, md5
  c88da1544f6479df5b485c1b2b699518, 83,181,246 B, 1280x720, 24fps, 8516 frames,
  354.833s. Chat copy: masters/mv3_i_am_your_dad_16x9_q5_chat.mp4, md5
  4e702f61e68e18f4d02921e580db6b75, 26,671,217 B, 854x480. Build: q5_build.py
  (S13 t2 w=1.0 take[0.25:9.25]; S39 t2 w=1.5833 take[0:6.5]); corrected
  master untouched.
- GATES (on the Q5 master, full record work/q5/Q5_NOTES.md): frames 8516
  exact; SEI crf=18.0; AAC 48k stereo; faststart; decoded-PCM audio md5
  ff64d85ed44e3b348afa1d5b569a2f1f identical to corrected; mouth at the 6 key
  onsets all O/T — 90.66 C→O (catalogue's only closed onset CLOSED),
  351.55 C→O (S39 final-mantra disclosure CLOSED); motion: 30f @208.25 S25
  + 27f @299.62 S35 inherited runs unchanged, 24f @348.29 S39 run ELIMINATED,
  no frozen run in S13/S39; unchanged scenes frame-identical to corrected.
- Disclosed: S39 sings one phrase, not four repeats (mantra carried by
  warp); "Pharmacy" background sign (G2 nit); S39 eyes close 7.25–8.0s in
  the take tail (trimmed out, never in the master); slowest playback 0.63x
  (S39 warp, inside the 0.5x floor).
- Awaiting parent gate + delivery (flag MV3_CORRECTED_DELIVERED.flag NOT
  written by this run; parent writes the flag for the version it delivers).

## Lyrics redo (2026-11-12, user playback verdict 12:41 EST on the Q5 master)
- User verdict (replying to the Q5 delivery): "lyrics on screen are wrong
  and no alignment to music" — redo the lyrics + timings. His verdict
  outranks every internal gate; the old captions were not defended.
- Method (three sources, no single ASR trusted): TEXT authority = the Suno
  lyric video (track.mp4, 43 frames read at full res); TIME authority =
  per-word ASR anchors (faster-whisper BASE 729w primary + large-v3-turbo
  535w where the base garbled); MDX vocal-stem pass for the 5 dense spans
  (L13/L26/L27/L34/L38). The turbo backbone alone was UNUSABLE (535w vs
  729w — no_repeat_ngram_size=3 suppresses real repeats on a chant track;
  it also mishears "king" for "dad" and stamps the first word 2.24s late).
- Corrected grid: work/lyrics-redo/SONG_WORDS_REDO.json — 40 lines, 612
  words (21 interpolated, 76 stem-sourced, 0 pending). Old 493w -> new
  612w. Diff (diff_report_redo.json): 94 words changed, 123 added,
  4 dropped, 5 shifted >0.3s; 17/40 lines differ.
- What was wrong (full record work/lyrics-redo/LYRICS_REDO_NOTES.md):
  (a) wrong words — the old lyric sheet was an abridged draft, not the
  performed song (L11/L12/L13/L15/L16/L20/L21/L22/L27/L29/L33/L34 all
  wrong in whole or part; L15 dropped its leading "Don't"; L16 dropped
  the whole "I sit in the beat, slap bass under" clause);
  (b) wrong times — mantra spans were static BLOCKS (L26 8.88s, L34
  29.48s, L38 16.36s, L40 9.16s) while the song repeats the phrase;
  (c) width defect — 153/234 old events over 1100px at fs 44, long lines
  cut at the frame edges (MV-13 defect, present here).
- Stem findings: L13 = don't-fight + dad-dad (stem p=0.96-1.00); L26 = 5
  phrases, not 7 (base's 190.96/191.48 are pile-up hallucinations — stem
  envelope silent after 190.75); L27 = 15 words, NOT 35 — the base's tail
  dad-phrases (201.54-214.82) are hallucinations (turbo on mix AND stem
  both hear nothing after 201.38; stem envelope ~0 from 201.25 to 215);
  201.38-215.4 is an INSTRUMENTAL gap, no caption; L34 = 11 phrases /
  52 words (extra dad-phrase at 262.86, three phrases in 278-283); L38 =
  6 phrases (phrase 6 tail approximate, fading echo).
- Kinetic rebuild: work/lyrics-redo/mv3_kinetic_redo.ass (612 events, one
  per word-step; mantra spans split into one event per "I am your dad"
  repeat). fs from MEASURED bold width (PIL DejaVuSans-Bold, cap 1100px):
  max 1099px, min fs 17, 0 events over 1100px, 0 double-backslash lines.
  Two defects caught by the full-res eye read and fixed (each forced a
  re-encode): (1) the 0.52 estimator under-measures BOLD by ~10% (31
  events over 1200px); (2) the karaoke highlight used {\r}, which resets
  \fs to the style default 44 on every scaled line (L29's "make" rendered
  at fs 17 while the rest rendered at fs 44 and overflowed) — now resets
  only the colour ({\1c&HFFFFFF&}). Also a no-overlap clamp (L16 'three'
  ended 108.96 while L17 'you' starts 108.92 — both captions showed for
  one frame).
- Lyrics master: masters/mv3_i_am_your_dad_16x9_lyrics.mp4, md5
  e993e043de2081f9ef6a67342212b459, 83,210,934 B, 1280x720, 24fps, 8516
  frames, 354.833s. Chat copy: masters/mv3_i_am_your_dad_16x9_lyrics_chat.mp4,
  md5 670d7f34c1e0175d25e434db533b4c56, 26,465,380 B, 854x480. Build:
  redo_build.py (Q5 intermediate + new .ass + drawtext ~ WuBu ~ bug, CRF
  18, AAC 192k, faststart). Q5 master + corrected master untouched.
- GATES (on the lyrics master, full record work/lyrics-redo/): frames 8516
  exact; SEI crf=18.0; AAC 48k stereo; faststart; decoded-PCM audio md5
  ff64d85ed44e3b348afa1d5b569a2f1f identical to Q5; motion PASS (longest
  frozen run 27f in both, no new runs, no scenes below 0.5); regression
  PASS (caption-free frames differ by encoder noise only — worst mean
  1.05, worst max 37; strict 0.0 is unachievable for a re-encode with
  changed captions, see redo_gates.py); full-res eye reads of 12 line
  starts + the L27 gap (205s/210s, no caption — confirmed): words
  legible, nothing cut at edges, first word not mid-fade faint; L29/L28/
  L17/L09 re-read after the {\r} fix — all render on one line at the
  scaled fs.
- Disclosed: L38 phrase 6 tail (am@333.54 -> your@337.76, 4.2s gap) is a
  held/fading echo, kept as measured, flagged approximate; L13's 2nd
  dad-phrase (91.58-92.42) is base-sourced (stem slice ends 92.0); L27
  head words "just a low voice" are interpolated across 194.0-196.08
  (turbo garbled them as "Hello man, hello", p=0.18-0.60); the S13/S39 t2
  takes still sing their invented words on camera — the captions carry
  the SONG's words at the SONG's times (takes unchanged, no verdict change).
- Awaiting parent gate + delivery (flag NOT written by this run; parent
  writes the flag for the version it delivers).
