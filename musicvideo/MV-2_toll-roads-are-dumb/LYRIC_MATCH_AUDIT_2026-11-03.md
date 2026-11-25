# MV-2 viewing-cut lyric-match audit — 2026-11-03

User directive (2026-11-03 22:44 EST): the song lyrics, the on-screen lyrics,
and the video mouths do not match, and that mismatch is the main defect.
This audit investigates the audio properly: fresh dictation of every take
used in the viewing cut, matched against the song at frame level.

## Method (so the numbers can be checked)

- **Song audio (ground truth A):** `SONG_WORDS_BASE.json` — 404 words with
  measured t0/t1 from the track itself. Audio in the master is untouched
  `track.mp3`, so the master's output timeline IS the song timeline.
- **Mouth (ground truth C):** fresh uniform transcription of all 40 takes
  in `masters_work_viewingcut/cutlist_working.json`, faster-whisper base,
  word timestamps, RAW words — no mishear folding in the dictation itself
  (`TAKE_WORDS_AUDIT_2026-11-03.json`). Mapped to output time through each
  clip's tau/factor: `out = out_start + (take_time - tau0) / factor`.
- **On-screen lyrics (ground truth B):** `captions_v2.srt`, built from the
  lyric sheet (`LYRIC_TIMELINE.md` line table) — line blocks, NOT
  word-timed.
- **Comparison:** sequence alignment per clip (v2 script), not word-midpoint
  matching. A matched line sung at a different internal pace reads as
  TIMING DRIFT (frames, 24fps), not as substitutions. Known Whisper
  mishear tokens (tall/told/toe=toll, done=dumb in the hook, paid=pay,
  plasers=plazas, comin'=coming, etc.) are folded ONLY for alignment and
  the raw tokens are kept visible. Folding is a lens, not a verdict.
- **Honest limit:** Whisper dictation is evidence, not an ear. Single-token
  flags (e.g. "files" for "fast") may be Whisper artifacts. Sequence-level
  flags (a dropped phrase, a whole wrong line, a spill into the next line)
  are solid regardless of the transcriber. Where Whisper cannot settle a
  word, this report says so.

## Headline: you are right, and it is worse than the delivery note said

The delivery note disclosed 5 gap regions and 3 fallback stretches. The
frame-level audit finds lyric mismatch in **37 of 55 clips**, in four
distinct kinds:

1. **Wrong line in the slot** — the take sings a different lyric line than
   the song is singing at that moment.
2. **Compressed take** — the take sings a shortened version of the line(s):
   phrases dropped, so the mouth goes silent while the song keeps singing.
3. **Spill** — the take runs on into the next line, so the mouth sings
   next line's words while the song is still on this line.
4. **Caption timing / caption-vs-performed-song** — on-screen words are
   whole-line blocks from the written lyric sheet, not word-timed, and the
   sheet differs from the performed song on the recurring chorus line.

Good news first (the "when it matches, it's proper" part): filler clips
sing NOTHING — the gap regions are silent mouths, not wrong mouths. And
several segments are genuinely clean (see §5).

## 1. Wrong line in the slot

- **S21 (205.20–214.44s, take s21_t2) — worst in the cut.** Song at that
  span: "The wrecks just come. Pay to go faster, the rest of us slow."
  Mouth sings: "the road gets meaner every single time / the wrecks just
  come / pay to go faster to the rest of us slow" — a whole extra bridge
  line LEADS the slot, pushing every matched word ~50 frames (2.1s) off.
  This take's own line was the bridge; it was placed at the mantra slot.
- **S07 (71.45–81.77s, take s07_t2).** Song (as transcribed): "We've been
  slamming the danger roads." Mouth: "weaving and slamming, danger grows"
  — the WRITTEN chorus line, not the performed one — then a hook tail
  "toll roads are done" while the song is already on the next hook
  ("baby." dropped). Mouth and song disagree on this line in Whisper space
  no matter which phonetic truth you pick.
- **R2 (144.08–150.48s, r2_t1) and R8 (216.06–222.13s, r8_t1) — the reverse
  case.** Mouth and song agree EXACTLY ("we've been slamming the danger
  roads"), but the on-screen caption says "Weaving and slamming, the
  danger grows." So here the CAPTION is the odd one out, not the mouth.
  This proves the sheet and the performed song differ on this line: the
  caption was written from the sheet, the singer (and the takes) sing the
  performed variant. Whisper may be mishearing "weaving" as "we've been"
  in both — but then the caption still matches the sheet while the ear
  hears something else. Either way, caption ≠ audio here, every chorus
  repeat (cues 68–78s, 143–148s, 213–218s).

## 2. Compressed takes (mouth drops phrases, then goes silent)

- **S12 (111.30–121.00s, s12_t3) — worst drift.** Song: "Poor folks sit in
  traffic while the rich ones disappear. Stop-and-go plazas used to kill,
  electronic helps a bit, but the split still creates the chaos that
  won't quit." Mouth: "poor folks sit in traffic rich disappear stop and
  go plazas split creates chaos" — drops "while the", "ones", the whole
  middle line ("used to kill, electronic helps a bit, but the"), "still",
  "the", "that won't". Median drift +37 frames (1.5s late), worst +57f
  (2.4s). The mouth finishes early and sits silent while the song sings
  the dropped phrases.
- **S11 (103.72–111.30s, s11_t2).** Song: "Crashes just move over, still
  the same old mess. Lexus lanes they call 'em, money buys the clear."
  Mouth: "crash is just move over same oldness money buys the clear" —
  "crashes"→"crash is", drops "still the", "old mess"→"oldness", drops the
  whole "Lexus lanes they call 'em" line and jumps straight to "money
  buys the clear". That jump is also a spill (§3).
- **S02 (18.95–27.95s, s02_t4).** Song: "They build the toll roads, baby,
  make you pay to roll, old plazas make you stop, then they make you go."
  Mouth: "they build the toll roads you pay the road old plazas make you
  stop then make you go" — drops "baby, make", "roll"→"road", drops
  "they". Then the take ends; "Cars…" is uncovered (gap, §4).
- **S04 (41.53–50.35s, s04_t5).** Drops the second "weave" and "out"
  ("weave in, weave out" → "weave"), "at" for "it" (likely artifact).
- **S17 (169.62–175.22s, s17_t2 warped).** Drops "single", "the", "one's"
  ("every single time" → "every time", "the other one's stuck" →
  "other stuck").
- **S09 (93.10–96.80s, s09_t2 warped).** Drops "but the"; "hot" (mouth, =
  sheet) vs "high" (song transcription) — unresolved, see §6.
- **S06b (65.02–71.45s, s06b_t1), R1 (136.26–144.08s, r1_t3).** Each drops
  one small "to". Minor.
- **S19 (186.56–193.99s, s19_t2 warped).** Drops "the" before "wrecks".
- **Hook takes dropping "baby.":** S13 (122.92–125.13s), R3
  (150.48–153.74s), S20 (193.99–197.46s). The hook's second "baby" is
  never mouthed in those slots.

## 3. Spill (mouth sings the next line early)

- **S11 (§2):** "money buys the clear" arrives while the song is still on
  "Lexus lanes they call 'em".
- **S18 (175.22–184.77s, s18_t1 warped):** after "when timings up" the
  mouth adds "oh toll roads are down" — the next line's hook — while the
  song is still finishing the bridge. ("going to" vs song's "gonna" and
  "timings" vs "the time ends" are transcription-token differences on the
  same phrase, low confidence.)
- **S07 (§1):** hook tail after "danger grows" while the song is on the
  next hook.
- **S16 (165.92–169.62s, s16_t7 warped):** extra "a" ("for a dollar" =
  sheet; song transcription collapses it to "$1" — token artifact, not a
  real spill).
- **S25 (251.08–257.82s, s25_t2) and S26 (257.82–260.80s, s26_t2):** leading
  "the" ("the toll roads are done" vs song "toll roads are done"). Minor.

## 4. Uncovered song words (no mouth at all — the disclosed gaps, confirmed)

- **S03 slot 27.34–34.32s** ("Cars slam the brakes… NTSB said those
  booths were the worst on the map."): filler only, no mouth. Confirmed.
- **GAP-B 100.26–103.60s** ("They say the paid side is safer, the free
  side takes the hit."): S10 covers only the line before; no mouth.
- **GAP-C remainder 201.10–204.24s, GAP-D 224.92–230.22s, GAP-E line 44
  236.62–238.82s:** confirmed no mouth; S22's take covers only the first
  hook of its slot, the chorus line after it is uncovered; S23's take
  covers only the first hook, the "baby / toll roads are dumb" tail is
  uncovered.
- **Trimmed first words:** R6 (197.46–203.28s) and S22 (222.13–230.22s)
  mouths begin at "roads are done" — the opening "toll" was cut off by
  the clip's tau window. The hook's first word is missing on screen.
- **Filler clips carry zero words** (all 14 filler clips: no dictated
  word falls inside any filler tau window). Gaps are silent, not wrong.

## 5. Clean segments (sequence equal, drift under ~20 frames)

S01 (intro, both lines, median −3f), S05 hook (median 0f, stretched
1.896× but word sequence right), S06a (median +11f), S06b, S08 (median
+18f — late but right words), R5, S13 hook (sequence right), S20 hook,
R3/R4 hooks, R11 ("yeah"), S24 outro (median +15f, range −20..+33f —
driftiest of the clean set), S25, S26. These are the proof of the user's
point: where the words match, it reads as proper.

## 6. On-screen lyrics (captions) — all issues

Captions are 48 whole-line blocks from the lyric sheet. They are never
word-timed, so the on-screen line routinely disagrees with the word
sounding at that frame:

- **Worst leads/lags (caption vs first/last song word in its block):**
  - 0–8s "Yeah… listen here, baby." — appears 4.44s BEFORE the first word
    sounds (intro silence); cuts off 0.3s before "baby." ends.
  - 233–238.5s "Toll roads are dumb." — appears 3.62s before its word sounds.
  - 253–268.01s final "Toll roads are dumb…" — sits on screen 7.21s AFTER
    the last word ends (outro tail).
  - 83–91.5s "Fast lanes make crashes… they just keep coming." —
    disappears 1.6s BEFORE the line finishes (line runs to 93.1s).
  - 188–190s "Fast lanes make crashes… the wrecks just come…" — appears
    1.44s AFTER the line already started.
  - 143–148s chorus cue — appears 1.08s late, and shows the sheet line
    while the song sings the performed variant (§1).
- **Sheet vs performed song:** every chorus-repeat caption ("Weaving and
  slamming, the danger grows", cues at 68–78s, 143–148s, 213–218s) shows
  the sheet line while the audio (and R2/R8 mouths) sing "we've been
  slamming the danger roads" as transcribed. If Whisper is mishearing
  "weaving" in both song and takes, the caption is still the only stream
  claiming "weaving" — the ear has to decide, and Whisper cannot.
- **Boundary spill (minor, systemic):** because cue boundaries are
  rounded section estimates, not measured word times, most cues contain
  1–3 foreign words from the neighbouring line sounding inside the
  block (e.g. 53.5–63s cue contains the tail of the previous hook;
  8–12.5s cue contains "here, baby." from the previous line). This is
  the line-block design, not a typo: a word-timed caption track would
  not have it.
- **Caption text itself is the lyric sheet** — no typos found in the
  caption text vs `lyrics.txt`. The caption problem is timing and
  sheet-vs-performance, not spelling.

## 7. What this means for the strict v6 build

- Gate v6 assembly on **sequence-matched takes only**: a take ships in a
  slot only if its dictated sequence aligns to the song's sequence in
  that slot (equal opcodes), with drift reported per word. Compressed
  takes (S12, S11, S02), wrong-line takes (S21, S07), and spill takes
  (S18 tail, S11 jump) do NOT ship as-is, even if their ratio passed.
- **Ratio is not a lyric gate.** S12 passed at 1.03× and is the worst
  lyric mismatch in the cut. S05/S13 stretched 1.9×/2.4× yet sing the
  right words. The v6 gate order must be: lyric sequence first, ratio
  second, frame gate third.
- **Captions for v6 must be word-timed** from `SONG_WORDS_BASE.json`
  (measured word times), not line blocks from the timeline table — and
  must use the PERFORMED words where sheet and performance differ, with
  the chorus-line difference flagged for an ear decision, not silently
  resolved by Whisper.
- **Known gaps stay gaps** until a take that actually sings those words
  exists: S03 whole slot, GAP-B "safer" line, GAP-C remainder, GAP-D,
  GAP-E line 44, hook "baby." tails, R6/S22 trimmed "toll". No filler,
  no stretch, and no wrong-line take may paper over them in v6.

## Files

- `LYRIC_MATCH_AUDIT_2026-11-03_transcribe.py` — fresh dictation script
- `TAKE_WORDS_AUDIT_2026-11-03.json` — raw dictation, 40 takes
- `LYRIC_MATCH_AUDIT_2026-11-03.py` — v1 midpoint audit (superseded:
  overcounts substitutions on sustained song words)
- `LYRIC_MATCH_AUDIT_2026-11-03_v2.py` — sequence-alignment audit
- `LYRIC_MATCH_AUDIT_2026-11-03_v2.json` — per-clip alignment detail
