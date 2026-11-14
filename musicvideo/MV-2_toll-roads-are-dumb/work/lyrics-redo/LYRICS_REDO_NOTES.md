# MV-2 Lyrics Redo — Notes

**Trigger:** user playback verdict 2026-11-12 12:41 EST (on the MV-3 Q5 master,
applying to this track last): "lyrics on screen are wrong and no alignment to
music". His verdict outranks every internal gate; the old captions were not defended.
**Base:** Q6 master `masters/mv2_toll_roads_are_dumb_v7_16x9.mp4`
(md5 `701fa50b19f6697fb37511dec6f932eb`, 6432f, 268.010s).
**Intermediate:** `masters_work_v7/v7_silent.mp4` (md5 `e06a4fe64f95ceb142f6f2c7c9e80792`,
6432f decode-counted) — VERIFIED caption-free + bug-free by eye at 34.56s and
205.20s (frames in `work/lyrics-redo/silent_check_*.png`). The rebuild goes
silent + new .ass + bug + track.mp3, exactly the MV-3 pattern. v7 + v6 masters
NEVER overwritten.
**New master:** `masters/mv2_toll_roads_are_dumb_v7_16x9_lyrics.mp4` (reassembly only —
no new generation, no new takes, no character changes).

## Progress log
- 2026-11-12 ~14:49 EST: coordinator start. Base v7 md5 verified (701fa50b).
  Intermediate v7_silent verified 6432f + caption-free by eye.
- 2026-11-12 ~14:52 EST: turbo backbone transcription launched (chunked 60s+2s,
  cpu_threads=1, per-chunk checkpoints).
- 2026-11-12 ~15:00 EST: old .ass parsed (396 events, 53 line instances;
  27 lines over the 1100px cap at fs44 — but the old style is fs30, so no
  width overflow in the delivered look; the width defect is NOT present here).
  Old-caption word errors already visible (see §1): "make your pay. the roll",
  "back -ends", "weaving weave out", "the other ones", "your speed for $1",
  "the time ends up", garbled echo mashups 224.79-230.09, last ~7s silent.
- 2026-11-12 ~15:05 EST: Suno lyric video probed at full res (74s, 76s, 222s, 250s).
  Video (TEXT authority) confirms the sheet throughout: "Weaving and slamming,
  the danger grows." bold at 74-76s; "Toll roads are dumb (toll roads are dumb),"
  bold at 222s; outro "Toll roads are dumb…" bold at 250s.
- 2026-11-12 ~15:06 EST: turbo chunk 0 (106w) + chunk 1 (119w) land. Turbo is
  CLEARLY better than base on this track (base garbles are exactly what got
  burned into the old captions). DECISIVE on the open Q6 ear item: turbo hears
  "Weaving and slamming, the danger grows" at 72.12-78.04 — the SHEET words.
  The base ASR's "We've been slamming the danger roads" was a BASE MISHEAR.
  Two sources (turbo + Suno video) now agree with the sheet. The old captions'
  "We've been slamming the danger roads." is WRONG. Consequence (disclosed):
  the Q6 S07 t2 take (and the C2/C-ext slots built from base words) MOUTH the
  base mishear while the song sings "weaving and slamming" — the new captions
  carry the SONG's words; the mouth/word mismatch on that line (3 occurrences:
  C1 ~72s, C2 ~143s, C-ext ~213s) is a known property of the v7 base, NOT
  fixed by this lyrics-only redo (take re-fire is out of scope; parent decides).
  Turbo's own mishears so far: "dumb"→"done"/"down"/"tow", "merges"→"mergers",
  "make"→"may" (60-61s) — the sheet + video arbitrate all of them.
- 2026-11-12 ~15:10 EST: turbo chunk 2 (97w) lands. C2 "weaving" line confirmed
  a SECOND time (turbo 143.94-149.82). Bridge: turbo hears "they sell you speed
  for a dollar and a dime" (sheet words — old caption's "your speed for $1" is
  wrong). Bridge L34: turbo AND base BOTH hear "somebody's gonna get it when
  the time ends up" vs sheet "going to get it when the timing's up" — a genuine
  performed-vs-sheet dispute; the STEM pass arbitrates.
- 2026-11-12 ~15:13 EST: turbo chunk 3 (33w vs base 80w) — the no_repeat_ngram=3
  suppression is real on the extended chorus (one 14s segment merges L39+L40).
  Turbo backbone is NOT usable as-is for 190-238.5s; base supplies repeat
  times, stem (echo slice 217-239s) arbitrates the parenthetical echoes.
  Third "weaving" confirmation (C-ext L40, ~208-221s).
- 2026-11-12 ~15:17 EST: chunk 4 CRASHED — faster-whisper IndexError in
  find_alignment on the near-silent outro tail (no words after 260.80s).
  Retried on a shorter window [238-262] — OK, 25 words, chunk-04.json written.
  Full turbo grid stitched: 361 words (base 404; the gap is the suppressed
  extended-chorus repeats). Outro turbo times agree with base within 0.1s
  (L45 242.22, L46 247.58, L47 251.0, L48 258.14; turbo hears "dumb" correctly
  on L48). NOTE: VM rebooted 14:46:12 EST, before this coordinator spawned
  (~14:47) — no work of mine was affected.
- 2026-11-12 ~15:23-15:30 EST: MDX stem separation running (l34 + l21 + l17 done;
  echo slice 217-239s separating). Stem slices cut: l34 (174-181s), l21 (107-113s),
  l17 (91-99s), echo (217-239s). Stem transcription (no_repeat_ngram=0) follows.
- 2026-11-12 ~15:35 EST: ALL FOUR STEMS SEPARATED (rc=0) + TRANSCRIBED (rc=0).
  STEM VERDICTS — all four disputes RESOLVED, all against the sheet:
  (1) L34: stem "Somebody's gonna get it when the time ends up." 176.00-178.98
  — turbo + base + stem agree; sheet "going to get it when the timing's up"
  is NOT sung. (2) L21: stem "they call them." 109.36-109.50 — "them", not
  "'em"; turbo + base agree. (3) L17: stem "mergers" 95.52-95.94 — turbo
  agrees; base "merges" alone. (4) L42: stem "Fast lanes may crash it" TWICE
  (226.50-228.46 + 228.68-229.90); turbo "lanes may crash" agrees; base
  "make crashes, the wrecks just come" is a familiar-line hallucination.
  Echoes ARE sung: L41 "Toll roads are dumb" x2 (222.64-224.64 + 224.88-226.24),
  L43 "Toll roads are dumb, baby." 229.96-232.58, L44 236.54-238.76.
- 2026-11-12 ~15:40 EST: GRID COMPLETE — `SONG_WORDS_REDO.json`: 48 lines,
  401 words, 1 interpolated (L35 2nd "toll" @184.38 — no ASR caught it clean;
  base's merged "toe" 183.04-184.78 overlaps "yeah" by 0.94s, onset ~1.3s
  early, rejected by the 0.5s overlap guard). 4 overrides (L17 mergers, L21
  them, L34 gonna/time-ends-up, L42 may-crash-it). Sources: turbo 342, base
  45 (chunk-3 suppression zone L36-L38), stem 14. 0 non-monotonic lines;
  only L42 has a sub-0.05s word (2nd "it." 0.02s — renders block, by design).
  Matcher lessons (in build_grid.py comments): consensus window [T_min,
  T_min+0.5] + cross-line floor + monotonicity + 0.5s overlap guard; NO
  duration cap (held "weaving" 2.60s is legit) and NO in-span preference
  (it stole L09's first "weave" and L03's "They").
- 2026-11-12 ~16:14 EST: .ass BUILT — `mv2_kinetic_redo.ass`: 392 events, max
  est width 952px (cap 1100), min fs 30 (no scaling needed), 0 double-backslash
  lines, 1 BLOCK line (L42 — the 0.02s "it."). Event math: 401 words − 10
  (L42) + 1 block = 392. ✓
- 2026-11-12 ~16:14–16:52 EST: MASTER ENCODED — `finish_lyrics.py` (same
  recipe as v7: silent + new .ass + bug + track.mp3, CRF 18 medium).
  Master `masters/mv2_toll_roads_are_dumb_v7_16x9_lyrics.mp4` md5
  18baecc2a1c4728b20802789e2332c74, 82,719,691 B, decode-counted 6432f,
  1280×720 24fps, 268.010s. Took ~38 min (MV-4 + MV-6 sibling encodes
  contending for the 1.5 CPUs). NOTE: finish_lyrics.py DIED after the master
  ffmpeg exited (log empty, no outputs_lyrics.json, chat encode never
  started) — likely the runtime reaper catching the long-backgrounded
  process; the master file itself completed cleanly and verified 6432f.
  Chat encode re-run separately in the foreground.

## 1. What was wrong in the old captions
`diff_report_redo.json` — old 53 lines → new 48 lines (46 matched pairs).
Words: 29 changed, 21 added, 8 dropped. Timing: 345 word shifts measured,
median |shift| 0.14s (systematic turbo-vs-base onset offset — the old
captions were built from base times), max 1.47s, 11 words >0.5s (all
explained below, none a new error).
WRONG WORDS (old → song, with times):
- "We've been slamming the danger roads." → "Weaving and slamming, the
  danger grows." — THREE occurrences: C1 @72.12, C2 @143.94, C-ext @214.40.
  The base ASR misheard it; turbo + the Suno lyric video agree. This was the
  Q6 S07 take's mouth line too — the take mouths the mishear; the captions
  now carry the song (see §8 disclosed flaw).
- "make your pay. the roll" → "make you pay to roll," (L03, ~22.4–23.5s).
- "They sell your speed for $1 and a dime," → "They sell you speed for a
  dollar and a dime," (L31, ~165–168s).
- "the back -ends crash" → "the back ends crash" (L05, ~29.4s).
- "weaving weave out the speeds, don't match it all." → "Weave in, weave
  out, the speeds don't match at all," (L09, ~41.4–44.6s).
- "the merges get hot" → "the mergers get hot" (L17, 95.5s; stem + turbo).
- "they call 'em" was already "them" in the old captions — old was RIGHT;
  the sheet was wrong. Same for L34 "gonna…time ends up" (old #36 had it
  right; the sheet was wrong).
- HALLUCINATED words dropped: "to" ×3 ("Pay to go faster TO the rest of us
  slow", L13/L27/L39); "and" ("kill AND electronic", L23).
- GARBLED echo mashups 224.79–230.09 dropped wholesale (old #46/#47/#48 —
  three near-identical garbled lines in 5s: "toll roads, the fast lanes make
  crashes, wrecks just come."). Replaced by the true echo structure, stem-
  verified: L41 "(toll roads are dumb)" ×2, L42 "Fast lanes may crash it"
  ×2 (NOT "make crashes" — stem + turbo agree), L43 "Toll roads are dumb,
  baby."
- STRUCTURE: old split lines the sheet joins (L01 split in two; "the wrecks
  just come." split off L12/L30/L38 as its own line ×3) and joined lines the
  sheet splits (outro's two "Toll roads are dumb…" merged into one 10s line
  250.96–261.10; L48 @258.14 now its own line). Old line count 53 vs song's
  48 is a splitting artifact, not missing content.
- TIMING: the old times run ~0.14s early across the board (base onsets).
  The >0.5s shifts: "Those" −1.46s (old line-split artifact — old line 3
  started at 10.44, the word is sung at 8.98); "Express" −1.47s (stem onset
  91.50 vs old base 92.97); chorus "Toll"/"Pay"/"the"/"wrecks" −0.7–1.0s
  (turbo onsets earlier than base's); L35 2nd "toll" +1.47s (interpolated
  184.38 — the old 182.91 falls mid-"yeah", impossible); L18 "somebody"
  +0.51s (turbo 98.62 vs stem 98.24 — KNOWN NIT, see §8).
- WIDTH DEFECT: none in the old captions — old style is fs30 and the widest
  old line is ~983px est, under the 1100px cap. The MV-13 overflow defect
  does not apply here; the rebuild keeps fs30 + the cap anyway.

## 2. Method — three sources, no single ASR trusted
Standing hybrid (large-v3-turbo full-clip backbone) + faster-whisper BASE
(`SONG_WORDS_BASE.json`, 404w, 2026-11-01 — the assembly's time authority,
it detected the repeats) + the Suno lyric video (`track.mp4`, Suno's own
lyric sheet for THIS song) as TEXT authority. MV-3's lesson applies here:
turbo with no_repeat_ngram_size=3 suppresses REAL repeats on a repeat-heavy
song, so the turbo backbone alone is not trusted; the base + video arbitrate.
MDX vocal-stem pass only for dense spans where BOTH mix ASRs fail.

## 3. The new word grid
`SONG_WORDS_REDO.json` — 48 lines, 401 words. Sources: turbo 342, base 45,
stem 14. Overrides (performed text ≠ sheet, 2+ audio sources each): L17
"mergers", L21 "them", L34 "Somebody's gonna get it when the time ends up.",
L42 "Fast lanes may crash it (fast lanes may crash it),". 1 interpolated word:
L35 2nd "toll" @184.38 (no clean ASR candidate; bracketed between "yeah" end
183.98 and "roads" 184.78). All 48 lines monotonic in time; only L42 carries
a sub-0.05s word (2nd "it." 0.02s — that line renders as one sustained block).
Grid builder: `build_grid.py` (consensus window + cross-line floor +
monotonicity + 0.5s overlap guard; no duration cap, no in-span preference).

## 4. Old-vs-new diff (final)
`diff_report_redo.json` (+ `diff_redo.py`, `diff_redo.log`). 53 old lines →
48 new lines; 46 matched, 7 dropped old (3 garbled echo mashups + 4
split-off fragments), 2 added new (L42 "Fast lanes may crash it…", L48
outro repeat). Words changed 29 / added 21 / dropped 8; 345 shifts, median
|shift| 0.14s, max 1.47s, 11 words >0.5s — see §1 for the full list. The
headline: the chorus line was wrong in all three occurrences, the echo span
224.79–230.09 was garbled, and three hallucinated words are gone. The
mouth/word mismatch on "Weaving and slamming" (Q6 S07 t2 / C2 / C-ext takes
mouth the old mishear) is a property of the v7 base, NOT fixed by this
lyrics-only redo — see §8.

## 5. Build
`work/lyrics-redo/mv2_kinetic_redo.ass` — built from SONG_WORDS_REDO.json by
`build_ass.py`: 392 events, max est width 952px (cap 1100, min fs 30 — no
scaling needed), 0 double-backslash lines (verified by assert), 1 BLOCK line
(L42 — the 0.02s "it." renders as one sustained block, no per-word
highlight, by design). Event math: 401 words − 10 (L42) + 1 block = 392.
Re-encode: `finish_lyrics.py` from `masters_work_v7/v7_silent.mp4` + new .ass
+ drawtext `~ WuBu ~` bug + track.mp3, CRF 18 preset medium, AAC 192k,
faststart →
`masters/mv2_toll_roads_are_dumb_v7_16x9_lyrics.mp4` md5
18baecc2a1c4728b20802789e2332c74, 82,719,691 B; chat copy 854×480 crf 23,
AAC copied → `masters/mv2_toll_roads_are_dumb_v7_16x9_lyrics_chat.mp4` md5
7d0c7aafdf925972f4ef904582a357b7, 26,418,959 B. Master encode took ~38 min
(MV-4 + MV-6 sibling encodes contending); finish_lyrics.py died after the
master ffmpeg exited (reaper) so the chat encode was re-run separately in
the foreground (rc=0) and outputs_lyrics.json was written by hand from
verified values. v7 + v6 masters untouched (md5s re-verified in the gate).

## 6. Gates
`gate_lyrics_parent.py` — ALL GATES PASS (rc=0, log on disk): 6432f
decode-counted, 1280×720 24fps, 268.010s, AAC 48k stereo, SEI crf=18.0,
faststart moov@36, audio agreement vs track.mp3 min corr 0.9981 (10
windows), decoded-PCM audio md5 f8371c2b5dbd9ebc389b9a11d1bc0428 == v7 base.
Chat: 854×480 24fps, 6432f, 268.01s, 26,418,959 B, audio PCM md5 == house.
Motion audit (`motion_audit_lyrics_parent.py`, rc=0): mean diff 3.38 (v7:
3.37), ONE run ≥12f — 18f @184.96–185.67s during words, frame-identical to
v7's inherited run. NO NEW frozen runs. Regression vs v7
(`gate_frames.py`): caption-free times pixel-identical @2.0s (mean|diff|
0.000) and noise-only @265.0s (0.687); captioned time 72.12s top-half 0.781
(no caption leakage above the band), bottom-band 8.511 (the new captions).
Full-res burned-kinetic eye reads (9 frames in `work/lyrics-redo/gate/`):
L01 "Yeah… listen here, baby." ✓ · L03 widest line fully inside frame,
"make you pay to roll" ✓ · L14 "Weaving and slamming, the danger grows."
✓ · L17 "mergers" ✓ · L34 "Somebody's gonna get it when the time ends
up." ✓ · L35 2nd "toll" highlighted at the interpolated 184.38 ✓ · L41
"(toll roads are dumb)," ✓ · L42 block line renders whole-line white from
226.60–229.00 ✓ (the 226.50 probe frame's empty band is an extraction
boundary artifact — see §8) · L48 outro "Toll roads are dumb…" ✓. Bug
`~ WuBu ~` correct on every frame. First words full-opacity at line starts
(no mid-fade faint).

## 7. Files
- `work/lyrics-redo/transcribe_redo.py` — mix backbone (large-v3-turbo)
- `work/lyrics-redo/SONG_WORDS_v3turbo.json` — turbo words
- `work/lyrics-redo/SONG_WORDS_REDO.json` — corrected grid
- `work/lyrics-redo/mv2_kinetic_redo.ass` — new kinetic layer
- `work/lyrics-redo/silent_check_*.png` — intermediate verification frames
- `work/lyrics-redo/gate_lyrics_parent.py` + `.log` — gates (ALL PASS)
- `work/lyrics-redo/motion_audit_lyrics_parent.py` + `.log` — motion (PASS)
- `work/lyrics-redo/gate_frames.py` + `.log` + `gate/*.png` — burned-frame
  reads + v7 regression
- `work/lyrics-redo/outputs_lyrics.json` — master + chat md5/size/probe/frames
- `masters/mv2_toll_roads_are_dumb_v7_16x9_lyrics.mp4` — NEW master
- `masters/mv2_toll_roads_are_dumb_v7_16x9_lyrics_chat.mp4` — NEW chat copy

## 8. Disclosed flaws + known nits
- **L42 first frame (probe artifact, NOT a defect):** the block event starts
  at 226.50s, which lands EXACTLY on frame 5436 (226.50×24 = 5436.0 — the
  only line start in the grid that is an exact frame boundary). Frame 5436
  renders with an empty caption band; the caption is present from frame
  5437 (226.54) through the line end (verified at 226.60/227.50/229.00).
  Cause: libass/ffmpeg float rounding at the exact boundary. Impact: none
  — 42ms, block line, no per-word highlight to miss.
- **L42 renders as a block, not karaoke:** the 2nd "it." is 0.02s, so the
  whole line shows white for its full span (226.50–229.90) with no per-word
  highlight. By design (times not solid enough to highlight).
- **L35 2nd "toll" @184.38 is interpolated:** no clean ASR candidate; placed
  by the repeat's rhythm (verified in the frame read — highlight lands on
  the 2nd "toll").
- **L18 "somebody":** turbo 98.62 vs stem 98.24 — the grid takes the later
  time (0.38s late vs the stem); the overlap guard vs turbo's long "over"
  segment forced it. One word, sub-half-second.
- **Q6 S07 take + C2/C-ext slots mouth the OLD mishear:** the takes on
  camera sing "We've been slamming the danger roads" while the song (and
  now the captions) say "Weaving and slamming, the danger grows." That
  mismatch is a property of the v7 base — this lyrics-only redo does not
  re-shoot takes. The captions are now right; the mouths are the old take.
- **Preset medium** (v6 used veryfast) — encode quality choice, disclosed.
- **Inherited 18f near-still run @184.96–185.67s** during words — identical
  to v7, not new, not introduced by the redo.
- **finish_lyrics.py died after the master encode** (runtime reaper); the
  chat encode was re-run separately and outputs_lyrics.json was written by
  hand from verified values — all md5s/frame counts re-verified after.
