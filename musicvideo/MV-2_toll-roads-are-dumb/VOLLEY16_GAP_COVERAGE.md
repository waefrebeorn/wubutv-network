# MV-2 v6 volley 16 — S11 RESTAGE ONLY — FIRED + QC 2026-11-04

Cap accounting: 1 video fired, 1 landed, 0 server failures, 0 retries.
Cap NOT exhausted by design: the task ordered S11 only, and the task
ordered no repeats if the first restage failed a gate. Nothing else was
fired. No commit, no ledger edit, no assembly, no posting — this record
only, per the task.

Vehicle: `mv2_s11lexus_vehicle_v6gap3.txt` (open-road, structure-free
staging: no plaza, no booths, no signage — the TEXT-risk class is
designed out; brisk / rapid-fire pacing wording, same axis that moved
GAP-E in volley 15; the named restage axis vs volley 15 is character
staging: microphone explicitly FIXED ON A STAND, never held in hand,
same THE VOICE face throughout).
Transcription: `TAKE_WORDS_V6_VOLLEY16.json` (faster-whisper base, raw
words, split-half recheck rule applied — not needed: 5 words decoded
full-clip). Frame gate: `VOCAL_WINDOW_V6V16.json` (160x90 gray, native
24fps, same method as the volley-13 refire audit). QC script:
`qc_v6_volley16.py`.
Gate order applied: lyric sequence FIRST, ratio second, frame gate
third, character gate, exactly-once (raw word list + any beat-word
subsequence scan) throughout. Drift figures below are fit-mapped
diagnostics (linear take-vocal-span → song-span mapping, 24fps).
Take is 1280x720/24fps/10.000s.

## STEP 0 — RETIME CHECK (before firing)

Full scan of all `TAKE_WORDS*.json` for "lexus" found hits ONLY in
`TAKE_WORDS_V6_VOLLEY15.json` — volley 15's own assigned S11 take
(`mv2_s11lexus_v6gap2_t1.mp4`). No unassigned take sings the lexus
line. Verdict: the slot had to be fired, as ordered. Song span
confirmed from SONG_WORDS_BASE.json: lexus 108.02-108.32, lanes
108.32-108.74, they 108.74-109.02, call 109.02-109.28, them 109.28-109.52
(1.50s total) — "lexus lanes they call them", matching the task brief.

## STEP 1 — FIRED TAKE + QC

### S11 dropped "Lexus lanes" line — FAIL (ratio only)

- Take: `takes/mv2_s11lexus_v6gap3_t1.mp4`, md5 `680e4e2f90c6d8e3f767c90c1edd0924`
  (raw generation file kept alongside under its `media-generation-*` name)
- Dictated (raw): "lexus lanes they call them" — all 5 words, exactly
  once, repeat scan empty (sub_repeats [], single_recurrences []).
  Sequence PASS. Per-word times: lexus 1.32-2.36, lanes 2.36-2.88,
  they 3.12-3.64, call 3.64-4.06, them 4.06-4.74.
- Vocal 1.32-4.74 (3.42s) vs song 1.50s → ratio 0.439 CLEAR MISS
  (warp to band edge would need 1.82x, over the 1.5x cap — not warpable).
  Median fit-mapped drift +1.0 frames (range -0.7 to +1.9; per-word
  +1.9, +1.4, +1.0, -0.5, -0.7).
- Frame gate PASS (vocal mean diff 0.54, max near-dup run 15, frozen
  run 1; 84 vocal transitions, 27 changed >0.5). Note: mean diff 0.54
  clears the 0.5 floor only narrowly — the picture moves, but slowly.
- Character PASS — this fixes volley 15's character fail. Frames at
  2s, 3s, and 4s all agree: same THE VOICE face (slicked dark hair,
  clean shave), INK suit, BONE shirt, chrome microphone mounted on a
  stand in front of him, hand holding the blank ticket / resting near
  the stand, mic never held in hand; mouth open mid-vocal at 4s
  ("them"). Text PASS (ticket blank, no signage, no on-screen text).
  Nit: pocket square renders red-orange, not CADMIUM (recurring nit
  class, same as volley-15 takes).
- **S11 LEXUS LINE STILL OPEN.** The restage fixed character and kept
  the frame gate, but brisk wording moved the ratio only 0.405x
  (volley 15) → 0.439x — the generator's pace floor for this 5-word /
  1.50s slot sits near 0.44x, same structural conclusion as GAP-B
  (0.40x → 0.438x). A third same-vehicle pull is not converging;
  per the task, no further cap was burned on repeats.

## TALLY AFTER VOLLEY 16

- Newly covered: NONE.
- Still open: S11 lexus line (ratio 0.439x, character now PASS, frame
  PASS — a clean, character-consistent take that sings too slowly for
  its 1.50s slot and cannot be warped into band).
- Unchanged by this volley (not fired, per the task): GAP-B, S12 middle
  line, S02 "baby, make" (structural/assembly problems), S07 performed
  chorus (chorus-line ear decision still pending), GAP-C first=fast
  class (provisional, needs an ear check).

## FILES

- Take (canonical): `takes/mv2_s11lexus_v6gap3_t1.mp4`
  (raw generation file kept alongside under its `media-generation-*` name).
- Dictation: `TAKE_WORDS_V6_VOLLEY16.json`; frame gate:
  `VOCAL_WINDOW_V6V16.json`; QC script: `qc_v6_volley16.py`.
- Vehicle: `mv2_s11lexus_vehicle_v6gap3.txt`.
- NOT done here: no commit, no ledger edit, no v6 assembly, no posting.
  VOLLEY_PROGRESS.md / TAKE_HISTORY.md were NOT updated by this volley
  (parent folds coverage into those on commit, same as volleys 14-15).
