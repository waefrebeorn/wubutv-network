# MUSIC VIDEO LEDGER — MV-5 "Easy Now Easy Now"

Track: `track.mp3` md5 `0c1bcafa568547e2d4fa36e133ad3626`, 206.4s, 546 words
(SONG_WORDS.json, old grid: 123 lines). Character (this track only): CAT
sings, GIRL on bike. v4 master is the delivered base — never overwrite it.

## Masters

| Master | md5 | Status |
|---|---|---|
| mv5_easy_now_easy_now_16x9_v4.mp4 (v4) | ea70bb8da8cba66f5062ab09cee8758b | DELIVERED (flag `MV5_V4_DELIVERED.flag` at project root) — base for the lyrics redo, never overwrite |
| mv5_easy_now_easy_now_16x9_lyrics.mp4 (lyrics redo) | a3e659220dd2870ab57c20cad198567e | built 2026-11-12, ALL GATES PASS — awaiting parent gate + delivery (no delivered flag written) |
| mv5_easy_now_easy_now_16x9_v6.mp4 (v6 FULL REBUILD) | 2071388f3fb5672849e29462cb3f2b64 | built 2026-11-13, ALL HOUSE GATES PASS — awaiting parent gate + delivery (no delivered flag written). Chat copy mv5_easy_now_easy_now_16x9_v6_chat.mp4 md5 2e2688bd592821e0a4c6ab3ab5f4657b, 46.1 MB |

## Delivery flag — lyrics redo (defined 2026-11-12, lyrics-redo run)

- **Flag file: `MV5_LYRICS_DELIVERED.flag`** (project root; name proposed — the parent writes it).
- Meaning: the lyrics master above has passed the parent's own gate AND been
  delivered to the user in chat.
- Written ONLY by the parent agent, only after delivery. The lyrics-redo
  coordinator never writes this flag, never commits, never announces.

## Lyrics redo (2026-11-12, user playback verdict 12:41 EST)

- User verdict (replying to the MV-3 Q5 delivery): "lyrics on screen are wrong
  and no alignment to music" — redo the lyrics + timings for MV-5 (also MV-3,
  MV-4, MV-6, MV-2 last). His verdict outranks every internal gate; the old
  captions were not defended.
- Method (audio decides, not the old sheet): faster-whisper large-v3-turbo
  int8, cpu_threads=2, NO VAD, numpy mono 16k, `en`,
  condition_on_previous_text=False, beam 1. Two full-clip passes (P1:
  repetition 1.1 + no_repeat_ngram 3, 454w — COLLAPSES legitimate repeats;
  P2: repetition 1.0 + no_repeat_ngram 0, 559w — restores repeats but
  hallucinates echo-loops) + an independent base noprompt pass (556w) +
  Gemini lyric-video frames + an MDX vocal stem (c11_sep) over the Intro,
  Chorus 1, Chorus 2 and Final spans as the arbiter. Per-word ASR anchors
  are the timing authority. Lessons banked: no_repeat_ngram 3 collapses
  hook repeats; suppression OFF hallucinates echo-loops on repetitive
  tails; av decode must slice resampled frames to `o.samples`; P1 word-END
  times inherit segment ends; P1 first-word times after a gap can be ~1s
  early.
- Corrected grid: work/lyrics-redo/grid_merged.json — 118 lines, 548 words
  (old 123 lines / 546 words). Sources: P1 298 / NOP 105 / POS 74 / STEM 24
  / P1-TAIL 20 / OLD 11 / STEM-ENV 6 / +FIX 8. Dropped: I06, I07, L56b,
  L107, L73c. 12 lines with changed text. 24 stem onset corrections
  (0.3–1.1s earlier — the lead enters under the hook's tail) + tail rebuild.
- What was wrong (full record work/lyrics-redo/LYRICS_REDO_NOTES.md):
  (a) wrong words — L48 "did it" (old "didn't"), L52 "last" (old "loud"),
  L81 "moves" (old "move"), L45 "Ice, ice, ice" (old one "Ice"), L90 "No,
  no, no" (old a label, not sung), L102 "drift" (kept; NOP+P1 "rip" vs
  GEM+sheet "drift", stem non-resolving);
  (b) unsung lines captioned — I06/I07 ("We ride"/"Easy now" intro),
  L56b (held note), L107 (artifact, 187.5–193.5 silent), L73c ("I'm
  falling" — P1+P2+stem all lack it, NOP-only like I06/I07);
  (c) wrong times — line-specific shifts of 0.3–0.9s (L03 +0.90, L36 −0.94,
  L02/L05/L11/L38/L47/L60/L73b/L91/L98 ±0.44–0.50), chorus hook lines
  −0.20s (old late), I08 start −4.30s (old intro spans wrong by up to 4s),
  and 24 stem-corrected lead onsets 0.3–1.1s earlier;
  (d) restructured tail — old L108 "We ride" wrong; the tail is a 9-pair
  "Easy now" chant (193.20–201.56, envelope proves continuous activity to
  200.5, no gap) + "Till the morning comes" x2 (Till@201.74, Till@203.84).
- Stem findings: the hook IS sung in all three choruses (envelope RMS
  0.02–0.11 in every hook window; the stem transcription just doesn't
  segment the quiet backing chant); the stem renders the hook as "Is it
  ..." (the echo-loop mishearing); L73a "I'm falling" KEEPS (stem renders
  it as words); L102 "drift" unresolved by the stem (hears "go"); the stem
  is inconsistent on the final "low" (C1 "gone", C2 "low", Final "long") —
  sheet+P1+NOP say "low".
- Kinetic rebuild: work/lyrics-redo/mv5_kinetic_redo.ass (548 events, one
  per word). fs from MEASURED bold width (PIL DejaVuSans-Bold, cap 1100px):
  L108 scaled to fs20 (1055px), 0 lines over 1100px, 0 double-backslash
  lines, 0 dropped events, 0 block-mode lines.
- Lyrics master: masters/mv5_easy_now_easy_now_16x9_lyrics.mp4, md5
  a3e659220dd2870ab57c20cad198567e, 111,666,029 B, 1280x720, 24fps, 4954
  frames, 206.4167s. Chat copy: masters/mv5_easy_now_easy_now_16x9_lyrics_chat.mp4,
  md5 8d5c08408e7a5d31c07e61ed88ef30ca, 38,710,900 B, 854x480. Build:
  assemble_mv5_lyrics.py (v4 assembly with only the .ass swapped, CRF 18,
  AAC 192k, faststart). v4 master untouched.
- GATES (on the lyrics master, full record work/lyrics-redo/): frames 4954
  exact; SEI crf=18.0; AAC 48k stereo; faststart; audio agreement vs track
  min corr 0.9978; decoded-PCM audio md5 6b87db537e463b5b10d710f730cda824
  identical to v4; motion PASS (0 frozen runs ≥24f in both, no new runs);
  regression PASS (caption-band-masked cross-master mean 0.0009, max
  0.0022); full-res eye reads of 236 frames (15 contact sheets) + L108 /
  L45 / L48 / L102 / L90 / L20 / L30 first-word frames: words legible,
  nothing cut at edges, first word not mid-fade faint; corrected words
  confirmed on screen. Gate-script bug found + fixed during validation
  (regression compared a 0–255 mean against a 0–1 bar — see
  LYRICS_REDO_NOTES.md).
- Disclosed: (1) hook/lead layering (inherited from v4, not new) — where a
  hook line and a lead line overlap, libass draws the most-recently-started
  event on top, so the lead's first word is briefly hidden behind the hook
  (e.g. L20 "With"@60.24 covered by the L19 hook's "Easy"@60.26 for ~0.3s);
  (2) L102 "drift" is a 2–2 tie broken by sheet+GEM, not by the stem;
  (3) the L108 chant pair count (9) is the stem's merged-segment count —
  P1 heard 7, the envelope supports 8–10; (4) the "Oh" at 187.34 (L107
  window) is left uncaptioned (one-off exclamation).
- Incidents (full record work/lyrics-redo/LYRICS_REDO_NOTES.md): VM reboot
  ~19:46 UTC killed the stem run mid-Chorus-2 (resumed); Python file writes
  EPERM-blocked ~21:29–21:58 UTC (FIFO bridge workaround; chunks 038–040
  landed 0-byte and were re-run); VM reboot ~22:42 UTC after the Final span
  finished (no loss); gate regression units bug (fixed); assembly PROJ path
  bug (fixed).

## v6 FULL REBUILD (2026-11-13, user order 04:44 + 04:50 EST)

- Total refire under the lyric look lock (GIRL blue shirt / RED bicycle —
  v1–v5 inverted both). Zero footage reuse; grid + captions reused as-is.
- Singers re-derived in-build (stem + F0): L12/L41/L55/L109 = CAT,
  L16 = GIRL sung, bridge opens CAT-first (old ear record corrected).
- v5 (395c3140) and the lyrics master (a3e65922) are SUPERSEDED by v6 —
  never deliver them as the current MV-5.
- Fit 0 errors / 4954f; gates in work/rebuild-v6/qc/ (GATE_LOG_V6.md,
  VISUAL_GATE_V6.md, GATE_V6.json). One QC reject (s25_cat v1, identity
  intrusion) and three generator refusals (p1, p3, s09_duet) on record.
- Flag file for v6 delivery is the parent's to write after delivery.
