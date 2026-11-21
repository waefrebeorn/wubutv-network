# SWING METHOD — song words + beat grid + take-audio swing → keyframes → warp / montage

Written 2026-11-06 for the Slopcannon skill, from the user's order the
same day: *"fix it to actually time to the audio — find every word,
compare to the beat mix, get hints about the video swing keyframes
for timing the sample audio of the generated video timing swings to
match, then fast cut when they mess up words to a montage, then back
to another proper lipsync take."*

Tools (this dir): `make_beat_grid.py` (song → `beat_grid.json`),
`swing_keyframes.py` (take → `<take>_swing.json`). Both are
project-general: paths are arguments; MV-5 values are only defaults.
MV-3 is the next consumer — point `--project` / `--song-words` /
`--take` at it, with MV-3's own mishear calibration where its
dictations demand one (the base map travels; track-specific classes
are re-earned per track, per the crosscheck method).

## The pipeline

1. **Find every song word.** The song dictation (`SONG_WORDS.json`,
   measured from the untouched master audio) is the fixed grid —
   every word, its onset, its line. Performed words, never the sheet
   where performance differs.
2. **Compare to the beat mix.** `make_beat_grid.py` measures tempo
   (three witnesses — tracked-beat median interval, tracker global,
   onset autocorrelation — reported separately, never assumed),
   beat times, downbeat/bar estimates (with an honest confidence
   margin), and onset accents. The beat grid governs CUTS; it never
   moves a word.
3. **Transcribe the take's own sample audio, per word.** Every
   generated take carries synthesized audio of its own performance.
   That audio is worthless as a soundtrack and priceless as a
   *measurement*: dual faster-whisper decodes (unprompted = the
   floor; prompted with the known line = the hint), word timestamps
   on both. Established adjudication applies: split-half recheck on
   zero-word decodes; mishear classes normalized on both sides
   before matching; a prompted-only word is credited only with RMS
   support in its span (unprompted + RMS wins over the prompt).
4. **Turn the swing into keyframes.** Align take tokens to song
   tokens monotonically (position-constrained — a match credited to
   the wrong repeat is a mismatch). Anchor the first matched pair;
   every later word's **swing offset** = how far the take has drifted
   from the song by that word. The keyframe table is (song onset ↔
   take time) per word, and each interval between anchors gets its
   warp: playback speed = take interval ÷ song interval
   (setpts factor = the reciprocal). This IS the per-word warping law
   (2026-11-06) with the measurements attached: warp the *intervals*,
   land every word on its song word.
5. **Verdict per word** (from `swing_keyframes.py`):
   - **GOOD** — swing ≤0.25s and interval warp inside 0.80–1.25.
   - **WARPABLE** — placeable by per-word warp inside the law:
     speedups unrestricted (flag >3× as a hard squeeze, disclose),
     slowdowns no slower than 0.5× playback (the 2×-slow cap).
   - **BAD-wrong / BAD-missing / BAD-repeat** — the take sings a
     different word, drops the word, or sings it an extra time.
   - **BAD-out-of-caps** — the right word at a swing no legal warp
     can land (would need >2× slow).
6. **Bad words become fast montage cuts — out on a beat, back on an
   onset.** For each BAD span the tool emits a montage cut: cut OUT
   on the nearest beat at or before the word (a cut on the beat reads
   as rhythm; off the beat it reads as a mistake), cover the span
   with montage / B-roll / reaction picture (mouths closed or
   non-singing — the edit rules still bind: montage is for exactly
   this), and cut BACK on the next good word's song onset, onto a
   proper lipsync take (the same take resumed, or another take that
   owns that word GOOD/WARPABLE). Captions stay on song word times
   throughout; the covered row is flagged "not a mouth-sung slot".
   Consecutive bad words merge into one span — one cut out, one
   return, never a chop per word.
7. **Gate on the master, as always.** Keyframes are HINTS from the
   take's audio. Two cautions ride with every table:
   - **Mouth lag:** a take's audio words can lead its visible mouth
     by up to ~1s (measured MV-2 v6). Audio swing places the words;
     the delivered master is still frame-checked at song onsets
     (mouth open on sung words, scene identity, motion) before
     anything ships.
   - **Grid softness:** where the song-side word times are
     inferred/even-split (confidence flags in SONG_WORDS), measured
     swing is an upper bound, not a verdict. Confirmed grids judge;
     inferred grids advise.

## What this replaces, and what it doesn't

It replaces slot placement and uniform per-line warps — the two
methods the MV-5 v2 playback rejection killed — with measured
per-word placement for every singing take, and it makes the montage
decision *per word, from evidence*, instead of per scene, from vibes.
It does not replace the crosscheck method (this is its assembly arm:
crosscheck scores a finished placement; swing generates the placement
to score), does not move the song (Law One), does not generate or
repaint anything, and does not claim phoneme accuracy: it claims
these words, at these measured times, warped by these factors, with
these words honestly cut away from.

## Worked proof

`EXAMPLES.md` (this dir): on L15's known pacing miss the tool
reproduces the hand-measured ratio (0.523 vs 0.52) and finds all five
words legally placeable as speedups; on the healthy S01 hook it
passes coverage 16/16 while still catching a real +1.3s phrasing
swing and one knife-edge capped interval (0.485× vs the 0.5 floor) —
surfaced with its montage span, not rounded away.
