# MV-3 Lyrics Redo — Notes

**Trigger:** user playback verdict 2026-11-12 12:41 EST on the Q5 master
("lyrics on screen are wrong and no alignment to music"). His verdict
outranks every internal gate; the old captions were not defended.
**Base:** Q5 master `masters/mv3_i_am_your_dad_16x9_q5.mp4`
(md5 `c88da1544f6479df5b485c1b2b699518`, 8516f, 354.833s).
**New master:** `masters/mv3_i_am_your_dad_16x9_lyrics.mp4` (reassembly only —
no new generation, no new takes, no character changes).

## 1. What was wrong in the old captions

The old kinetic layer (`captions_16x9_corrected.ass`, 234 events) had THREE
independent defects, any one of which justifies the user's verdict:

### (a) Wrong words — the old lyric sheet was not the performed song
The old line table came from the user's pasted lyric sheet (`lyrics.txt`,
"verbatim from the user, 2026-11-04"), which `LYRIC_TIMELINE.md` already
admits is "an abridged draft that matches the performed song in shape but
NOT in verse detail". The base-model ASR was then normalised BY POSITION
against that wrong table — so a wrong table word was burned on screen at
Whisper's time for a different word. The Suno lyric video (track.mp4,
Suno's own lyric sheet for THIS song) proves the following lines wrong:

| Line | Old on screen | What the song actually performs |
|---|---|---|
| L11 | "I am your dad, you're hearing once, you're hearing twice, now it lives inside" | "You hear it once, you hear it twice, now it lives inside, I am your dad" — the dad-phrase is the TAIL, not the head; "you're hearing" is a base-model mishear |
| L12 | "I am your dad, I am your dad, don't fight the feeling, I am your dad" | "I am your dad, I am your dad, every one of you, I am your dad" — the don't-fight line belongs to L13/L22, not here |
| L13 | "I am your dad, I am your dad" (8w) | "Don't fight the feeling, just let it in, I am your dad, I am your dad" (16w) — the whole don't-fight line was missing |
| L15 | "Matter to me, the message is the point" | "Don't matter to me, the message is the point" — leading "Don't" dropped |
| L16 | "I walk through the speakers, brass hits on the one and the three" (13w) | "I walk through the speakers, I sit in the beat, slap bass under, brass hits on the one and the three" (21w) — the whole middle clause dropped |
| L20 | "I am your dad, you're hearing once, you're hearing twice, now it lives inside" | "I am your dad, you hear it once, you hear it twice, now it lives inside" |
| L21 | "I am your dad, I am your dad, I am your dad, say it with me" | "I am your dad, I am your dad, every one of you, I am your dad" |
| L22 | "I am your dad, you're hearing twice, now it lives inside" (11w) | "Don't fight the feeling, just let it in" (8w) — entirely wrong |
| L27 | "I am your dad" x4 (16w, static block) | "Just a low voice, telling every listener what they already know, I am your dad" x6 (35w) — the verse line was hidden inside a mantra block |
| L29 | "Make the brain stay true, repeat the same, I make it easy to sing" | "Make the brain stay tuned, repeat the same line, make it easy to sing" — "true"→"tuned", "I"→"line" |
| L33 | "I am your dad, you're hearing once, you're hearing twice, now it lives inside" | "I am your dad, you hear it once, you hear it twice, now it lives inside" |
| L34 | "I am your dad" (4w, static block for 29.48s) | A full chorus-tail reprise: dad-phrase, "every one of you, I am your dad", "don't fight the feeling, just let it in", then dad-phrases + echoes (44w) |

Smaller word errors: L02 "king" for "dad" (turbo mishear, not in old
captions — the old table had it right); L03 "I've" for "I been" (video:
"I been here the whole time", no 've); L04 "oh man" for "old man";
L06 "and the speaker" for "in the speaker"; L07 "I raised your" for
"I raised you"; L09 "need" for "have to"; L17 "face" for "phrase";
L18 "lead" for "last"; L28 "dogs" for "hooks"; L35 "a shadow on the wall"
— dropped entirely (no ASR or video evidence; it was never sung).

### (b) Wrong times — static blocks instead of sung repeats
The old .ass rendered mantra spans as single static BLOCKS while the song
repeats the phrase: L26 (8.88s, 7 repeats shown once), L34 (29.48s, ~10
phrases shown once), L38 (16.36s, 6 repeats shown once), L40 (9.16s,
4 repeats shown once), L27 (19.66s) + L36 (11.86s). That is the "no
alignment to music" the user saw: the caption sits still while the song
repeats. The new .ass splits every mantra span into one event per
"I am your dad" repeat, so the caption pulses with the song.
Timing errors in non-mantra lines: L14 started at 90.66 (the dad@90.66
belongs to L13's tail) — the line actually starts at 92.96, ~2.3s late;
L23's 2nd dad-phrase was ~1.9s late (base-model gap: i@152.34 →
am@154.72); L02's "I" was 0.66s late (base 14.22 vs turbo 13.56, and the
turbo agrees with the surrounding boundaries).

### (c) Width defect — long lines cut at the frame edges
153 of the old 234 events exceed 1100px estimated width at fs 44
(widest ~2,494px). Long lines were cut at the frame edges — the MV-13
kinetic-overflow defect, present in the current MV-3 captions (built
2026-11-04, before the MV-13 fix). The new .ass scales every event's
font size so its estimated width is ≤1100px (min fs 19).

### (d) The takes sing invented words — the captions must not
S13 t2 sings "Welcome to my home, it's good to see you here…" and S39 t2
sings "Hello, welcome to my street corner." on camera. Those are the
TAKES' invented words; the SONG performs its own words at those times
(S13 = L14 "You got your real one, maybe, or maybe you don't" @92.96;
S39 = L39/L40 "Say it back to me…" @338.84). The new captions carry the
SONG's words at the SONG's times. The takes are unchanged.

## 2. Method — three sources, no single ASR trusted

The standing hybrid (large-v3-turbo full-clip backbone) FAILED as a
backbone on this track: 535 words vs the base model's 729, because
`no_repeat_ngram_size=3` suppresses REAL repeats on a song whose lyrics
ARE a repeated phrase (turbo hears 3 words for L10, 1 for L12, 0 for L13,
6 for L38), it mishears ("king" for "dad", "my"/"his" for "your"), and it
stamps the first word 2.24s late (listen 5.06 vs base 2.82 — the video
shows lyrics at 3.0s; the base is right). **The turbo backbone alone
would produce a WORSE grid.** Decision: three-source grid —

1. **TEXT authority: the Suno lyric video (track.mp4).** 824×1464, 10fps,
   3548 frames; 43 frames read at full res across the track. Current line
   bold/white, upcoming lines dim. It is Suno's own lyric sheet for THIS
   song and settles every word dispute (see the table in §1).
2. **TIME authority: per-word ASR anchors** — faster-whisper BASE
   (`SONG_WORDS.json`, 729w, 2026-11-04) as primary (it detected the
   repeats; the assembly was built on it) + large-v3-turbo
   (`SONG_WORDS_v3turbo.json`, 535w) where the base garbled or piled up
   (L14, L16, L22, L23 phrase 2, L34 head). Both run with NO VAD (fatal
   on chant), pinned "en", condition_on_previous_text=False, beam 1,
   repetition_penalty 1.1, collapse runs >5.
3. **MDX vocal-stem pass** for the dense spans where BOTH mix ASRs fail
   (L13, L26-tail, L27-tail, L34-tail, L38) — see §3.

Per-line time sources are recorded in `SONG_WORDS_REDO.json` (sources:
B=base, T=turbo, S=stem, I=interpolated). 21 of 612 words are interpolated
(3.4%), all flagged; 76 are stem-sourced.

## 3. Stem pass — DONE 2026-11-12 ~19:34Z

Slices cut (44.1k stereo, `work/lyrics-redo/stems/`): l13_mix.wav 84-92s,
l26_mix.wav 183-192s, l27_mix.wav 194-215s, l34_mix.wav 258-288s,
l38_mix.wav 322-338s (84s total). Tool: `~/workspace/wubuwizard-cpu-sep/
mdx_onnx_cpu.py` (UVR-MDX-NET-Voc_FT.onnx, torch-free; 18.3x realtime on
the loaded blade — slower than the 7.95x estimate because the siblings
were encoding). Separation: all 5 slices rc=0 (l13 146s, l26 163s,
l27 312s, l34 451s, l38 232s). Transcription: large-v3-turbo with
**no_repeat_ngram_size=0** (`transcribe_stems.py`, cpu_threads=1).
Results (`song_words_<name>_stem.json`):

| Slice | Stem words | Verdict |
|---|---|---|
| L13 | 16 | RESOLVED. don't-fight 85.26-89.08 (p=0.96-1.00) + dad 89.42-91.14 (p=0.99-1.00). The stem's first dad (84.00-85.06) is L12's TAIL (its your@84.40/dad@84.70 match the base's L12 tail) — not an L13 phrase. The 2nd dad-phrase (91.58-92.42) is base-sourced (the slice ends at 92.0, so the stem is cut off there). |
| L26 | 4 | PARTIAL — the turbo went silent after phrase 1 (183.00-184.32, precise). The base's phrases 2-5 (184.7/186.82/188.42/190.6) stand; the base's 190.96/191.48 "phrases" are pile-up hallucinations — the stem RMS envelope is SILENT after 190.75 and the turbo (mix) heard nothing past 184.32. **L26 = 5 phrases, 20 words (not 7/28).** |
| L27 | 13 | RESOLVED + a finding. Stem gives "telling every listener what they already know" (196.08-199.40) + dad-phrase (199.66-201.38); the head "just a low voice" is the turbo's garbled "Hello man, hello" (p=0.18-0.60). **The base's tail dad-phrases (201.54-214.82) are HALLUCINATIONS**: the turbo (mix) AND the turbo (stem) both hear nothing after 201.38, and the stem RMS envelope is ~0 from 201.25 to 215. 201.38-215.4 is an INSTRUMENTAL gap (the song has a 13.78s instrumental gap at 18.38-32.16 too) — no caption there. **L27 = 15 words (not 35).** |
| L34 | 47 | RESOLVED (11 phrases, 52 words). Stem gives phrases 1-9 at p=0.99-1.00, including an EXTRA dad-phrase at 262.86 (the base's "every"@262.86 was a mishear; the every-phrase starts at 264.68) and THREE phrases in 278-283 (278.04/279.66/281.80). The tail hallucinates "Fuck your face!" (p=0.21-0.29) over overlapping echo voices — real words are dad-phrases, split into two (283.58-285.42 + 285.42-287.8). |
| L38 | 4 | PARTIAL — the turbo went silent after phrase 1 (322.00-323.22, precise). The base's phrases 2-6 stand; the 6th phrase's 4.2s am→your gap is a held/fading tail (stem envelope fades after 336.25; the base's your@337.76/dad@338.08 is a quiet echo) — kept, flagged approximate. **L38 = 6 phrases, 24 words.** |

**Lesson (for the sibling lyrics-redo coordinators):** the turbo suppresses
repeats on pure-mantra slices even with `no_repeat_ngram_size=0` — it
goes silent after the first phrase (L26, L27-tail, L38). The stem
transcription is NOT a reliable phrase counter for mantras. What the stem
pass DOES give: precise times for the phrases it hears, and — via the
stem RMS envelope (`onsets.py`) — hard silence boundaries that EXPOSE
base-model hallucinations (L26 tail, L27 tail). Trust the envelope's
silence over the base's pile-up timestamps.

## 4. The new word grid

`work/lyrics-redo/SONG_WORDS_REDO.json` — 40 lines, 612 words
(21 interpolated, 76 stem-sourced, 0 stem-pending). Line spans and
per-word times are in the file; the full text of every line:

- L01 Listen, all of you (4w, 2.82-9.12)
- L02 You already know, I am your dad (7w, 9.32-18.38)
- L03 I been here the whole time, kid, looking right at you (11w, 32.16-36.36)
- L04 Old man on the corner, old man in the room (10w, 36.56-40.06)
- L05 You walk by, you scroll by, you turn the radio on (11w, 40.06-44.08)
- L06 And the voice in the speaker says the same thing all along (12w, 44.10-47.60)
- L07 I raised you in the dark, I raised you in the light (12w, 48.12-51.30)
- L08 I raised every face that is listening tonight (8w, 51.76-55.14)
- L09 You don't have to like it, you don't have to stay, but the words keep coming and they won't go away (21w, 55.14-62.20)
- L10 I am your dad, I am your dad, say it with me, I am your dad (16w, 62.64-69.94)
- L11 You hear it once, you hear it twice, now it lives inside, I am your dad (16w, 70.28-76.28)
- L12 I am your dad, I am your dad, every one of you, I am your dad (16w, 76.28-85.04)
- L13 Don't fight the feeling, just let it in, I am your dad, I am your dad (16w, 85.26-92.90)
- L14 You got your real one, maybe, or maybe you don't (10w, 92.96-97.70)
- L15 Don't matter to me, the message is the point (9w, 97.70-101.40)
- L16 I walk through the speakers, I sit in the beat, slap bass under, brass hits on the one and the three (21w, 101.40-108.96)
- L17 You try to skip it, but you try to change the song, but the phrase comes back and it doesn't take long (22w, 108.92-115.90)
- L18 Short words, easy words, the kind that sticks fast, I am your dad, and the song will last (18w, 116.14-123.60)
- L19 I am your dad, I am your dad, say it with me (12w, 123.74-129.38)
- L20 I am your dad, you hear it once, you hear it twice, now it lives inside (16w, 129.46-136.52)
- L21 I am your dad, I am your dad, every one of you, I am your dad (16w, 136.52-146.08)
- L22 Don't fight the feeling, just let it in (8w, 146.08-150.30)
- L23 I am your dad, I am your dad, I am your dad (12w, 150.30-160.02)
- L24 I am your dad, I am your dad (8w, 160.70-167.50)
- L25 You can close your eyes, you can plug your ears, the words still bounce around inside your head (18w, 168.76-182.50)
- L26 I am your dad x5 (20w, 183.00-191.94) — 5 phrases, not 7 (see §3)
- L27 Just a low voice, telling every listener what they already know, I am your dad (15w, 194.00-201.80) — then an INSTRUMENTAL gap 201.38-215.4, no caption (see §3)
- L28 They study the hooks, they study the loops, they say simple words (12w, 215.40-220.64)
- L29 Make the brain stay tuned, repeat the same line, make it easy to sing, and the mind can play it on its own string (24w, 220.70-230.12)
- L30 I don't need a story, I don't need a name, just the one short claim that never changes (18w, 230.52-238.24)
- L31 You wake up tomorrow and the first thing you hear is the old man saying it crystal clear (18w, 238.24-245.10)
- L32 I am your dad, I am your dad, say it with me (12w, 245.10-251.04)
- L33 I am your dad, you hear it once, you hear it twice, now it lives inside (16w, 251.04-258.32)
- L34 I am your dad, I am your dad, every one of you, I am your dad, don't fight the feeling, just let it in, I am your dad x7 (52w, 258.00-287.80) — 11 phrases (see §3)
- L35 I am your dad, I am your dad, just a low voice (12w, 287.80-295.26)
- L36 I am your dad x4 (16w, 296.70-309.02)
- L37 All of you, every single one, I am your dad, you know it now (14w, 309.88-322.08)
- L38 I am your dad x6 (24w, 322.00-338.55) — phrase 1 stem-precise, phrase 6 tail approximate (see §3)
- L39 Say it back to me, I am your dad, say it to yourself (13w, 338.84-344.55)
- L40 I am your dad x4 (16w, 344.55-353.71)

## 5. Old-vs-new diff (final, `diff_report_redo.json`)

Old 493 words → new 612 words. **94 words changed, 123 added, 4 dropped,
5 shifted >0.3s.** 17 of 40 lines differ; 23 are word-identical (times
may still shift within 0.3s). The biggest changes: L34 (4w→52w), L27
(16w→15w — the old block hid a verse line AND 14s of instrumental gap
the base hallucinated phrases into), L26 (4w→20w), L38 (4w→24w),
L40 (4w→16w), L13 (8w→16w), L16 (13w→21w), L11 (14w→16w, entirely
reworded), L22 (11w→8w, entirely reworded), L12/L21 (middle phrase
replaced), L10 (missing final dad-phrase restored). Line-boundary
reshapes: L10/L11 (the 68.36 dad-phrase moves from L11's head to L10's
tail), L13/L14 (L14 starts 92.96, not 90.66), L21/L22 (the 144.08
dad-phrase moves from L22's head to L21's tail).

## 6. Build

`work/lyrics-redo/mv3_kinetic_redo.ass` — built by `build_ass.py` from
`SONG_WORDS_REDO.json`. 612 events (one per word-step), **0
double-backslash lines**. Phrase structure: one event per "I am your dad"
repeat in mantra spans; 8-word phrases for "every one of you, I am your
dad" and "don't fight the feeling, just let it in"; verse lines are one
karaoke event each. Each phrase event runs to the next phrase's start
(the caption holds and pulses, never blinks off between repeats).

**Width fix, second pass (found by the full-res eye read):** the first
build used the standing `len*fs*0.52` width estimate, which measures the
REGULAR font — but the .ass Style is Bold=-1, so libass renders
DejaVuSans-Bold, ~10% wider. The eye read caught L29's first word
"make" cut at the left edge. A PIL measurement of the real bold metrics
showed **31 events over the 1200px available width** (widest L28 at
1215px). `build_ass.py` now chooses fs from the MEASURED bold width (PIL
DejaVuSans-Bold), capped at 1100px: max measured bold width **1099px**,
min fs 17, 0 events over 1100px.

**The {\r} bug (the REAL cause of the cutoff, found on the second eye
read):** the karaoke highlight wrapped the current word in
`{\1c&H1EC6FF&}word{\r}` — but `\r` resets ALL overrides to the style
defaults, INCLUDING `\fs`. So on every scaled line (fs<44) the
highlighted word rendered at the event's fs while every following word
rendered at the style's fs 44 — overflowing the frame even though the
measured width was ≤1100px. (Lines at fs 44 looked fine, which is why
the first eye read passed 8/8 and only the scaled lines failed.) Fix:
restore just the colour with `{\1c&HFFFFFF&}` instead of `{\r}`.
Also added a no-overlap clamp: a line's last word event is clamped to
the next line's first word start (L16 'three' ended 108.96 while L17
'you' starts 108.92 — both captions showed for one frame).
Lesson for the sibling lyrics-redo coordinators (MV-4/5/6/2): the 0.52
estimator is WRONG for bold styles — measure with PIL, don't estimate
(R11) — AND never use `{\r}` after a scaled `{\fs}` in a karaoke
highlight; reset the colour only.

Re-encode: `redo_build.py` — final stage from
`masters/mv3_intermediate_16x9_q5.mp4` + new .ass + drawtext `~ WuBu ~`
bug, CRF 18 preset medium, AAC 192k, faststart →
`masters/mv3_i_am_your_dad_16x9_lyrics.mp4`; chat stage 854×480 crf 23,
AAC copied → `masters/mv3_i_am_your_dad_16x9_lyrics_chat.mp4`.
THREE encodes (the .ass was fixed twice after eye reads — see §6):
final master md5 `e993e043de2081f9ef6a67342212b459`, 83,210,934 B;
chat copy md5 `670d7f34c1e0175d25e434db533b4c56`, 26,465,380 B (25.2 MB).
(The first two masters — md5 e6a57101… then 074775b7… — are superseded;
only the third is the deliverable. Q5 + corrected masters untouched.)

## 7. Gates (on the final master, 3rd encode)

- Container: PASS — 8516f exact, 1280×720 24fps, AAC 48k stereo,
  SEI crf=18.0, faststart.
- Audio: PASS — decoded-PCM md5 `ff64d85ed44e3b348afa1d5b569a2f1f`
  identical to Q5; audio framemd5 tail identical.
- Motion: PASS — longest frozen run during words 27f in BOTH Q5 and new
  master (no NEW runs); no scene below 0.5 vocal mean diff.
- Regression: PASS — caption-free frames differ by encoder noise only
  (worst mean|diff| 1.05, worst max 37; 1.0s and 30.0s exactly 0.0).
  Strict 0.0 is unachievable for a re-encode with changed captions (the
  captions alter x264's rate control / reference chain); the bar is
  mean<2.0 and max<64 (a real content change would show max=255 over a
  large pixel fraction). The gate's caption-free times were fixed for the
  new grid (the old list's 5.0/88.5/149.7 are inside captions now).
- Frames (eye read, full-res, `work/lyrics-redo/gate/`): 12 line starts
  read (L01/L11/L13/L15/L16/L21/L22/L26/L27/L29/L34/L40 in the first two
  passes, L29/L28/L17/L09 re-read after the {\r} fix) + the L27 gap
  (205s/210s — NO caption, confirmed). All: words legible, nothing cut
  at edges, first word not mid-fade faint. The eye read caught TWO real
  defects, both fixed (see §6): the bold-width underestimate and the
  {\r} highlight bug. The L17 frame in the 2nd pass also showed L16's
  caption bleeding through for one frame (the 0.04s L16/L17 overlap) —
  fixed by the no-overlap clamp; the 3rd-pass L17 frame shows L17 alone.
- Disclosed: L38 phrase 6 tail (am@333.54 → your@337.76) is a held/fading
  echo, kept as measured; L13's 2nd dad-phrase is base-sourced; L27 head
  words interpolated; S13/S39 t2 takes sing invented words on camera
  (captions carry the song's words — takes unchanged).

## 8. Files

- `work/lyrics-redo/transcribe_redo.py` — mix backbone (large-v3-turbo)
- `work/lyrics-redo/SONG_WORDS_v3turbo.json` — turbo words (535w, NOT usable as-is)
- `work/lyrics-redo/video_probe/` — 43 Suno lyric-video frames read
- `work/lyrics-redo/build_grid.py` — corrected grid builder (three-source)
- `work/lyrics-redo/SONG_WORDS_REDO.json` — corrected grid (632w)
- `work/lyrics-redo/diff_redo.py` + `diff_report_redo.json` — final old-vs-new diff
- `work/lyrics-redo/build_ass.py` + `mv3_kinetic_redo.ass` + `ass_build_report.json`
- `work/lyrics-redo/separate_stems.sh` + `transcribe_stems.py` — stem pass
- `work/lyrics-redo/stems/` — 5 mix slices (44.1k stereo)
- `work/lyrics-redo/redo_build.py` + `redo_gates.py` — encode + gates
- `work/lyrics-redo/old_ass_events.json` — old .ass events (234)
