# MV-2 v5 — prompt-grounded rebuild: design

User correction 2026-11-02 07:26 EST: v4 matched Whisper words across a
±12 s window (LCS) and never used the vehicle prompt. Most cuts showed
mouth motion unrelated to the words playing. v5 fixes identity first:
**a take anchors ONLY to its own vehicle's line, at that line's own song
position, in order, with no jumps to repeated choruses elsewhere.**

## 1. What the fresh transcripts proved (masters_work_v5/words/, all 27)

Fresh Whisper (same base/int8 pipeline as v3, per-take files) replaces the
stale TAKE_WORDS_ALL_BASE.json. Headline: most takes DO sing their line.
The v4 failure was matcher/assembler, not takes, for most scenes.

- S02 is NOT a 2-anchor scene. Fresh transcript has the full 18-word line
  in order. v4's noise-merge (drop any anchor whose onset-interval speed
  was >4x or <0.25x) destroyed its middle. **v5 deletes the noise-merge.**
- S13 is NOT a 3-word scene. Fresh transcript has all 4 words
  (Toe/roads/are/down = toll/roads/are/dumb). v4's "3 matched words" was
  a matcher artifact.
- S03 sings its verse line fully — AFTER a leading chorus (take 0–2.24 s,
  "Tall roads are dumb") that is not in its vehicle. v4 started at take 0,
  so chorus mouth played over verse words. **v5 segment starts at take
  3.00, never take 0.**
- S05 sings only the chorus ("Toll roads are dumb"), not the verse tail
  in its vehicle. That is not an assembly gap: S04 covers the verse tail
  in partition. S05's job in the master is the chorus.
- S23 was anchored to the WRONG chorus occurrence in v4 (224.92 s,
  "toe roads, the fast lanes…"). Prompt order + header put it on the
  230.22–231.60 s repeat (song words 374–377). **v5 corrects this.**

Per-scene anchor table: WORD_MATCH_V5.json (take word index → song word
index, SONG_WORDS_BASE.json numbering, mishear map applied, skipped song
filler words noted per scene). Count: 8 clean, 3 clean line-level,
2 clean single-repeat, 1 clean chorus-role, 1 clean verse with extra
excluded, 1 corrected occurrence, 1 cutaway outro, the rest partial or
with disclosed visual nits (below).

## 2. Assembler rules (v5, superseding v4)

1. Anchors = fresh take word times → song word times for the scene's own
   line only. In order. No cross-line LCS, no ±12 s window, no
   noise-merge dropping, no visible-mouth shifting of the first anchor
   (shifting trades word identity for an open-mouth state; v4's onset
   "pass" was that trade). Word identity outranks open-mouth state.
2. A scene's vocal segment runs from its first prompted take word to its
   last prompted take word (+ ~0.3 s). It ends there. It is NEVER
   swept across seconds it is not singing.
3. Gaps between vocal segments are filled ONLY with non-singing footage:
   the same take's pre-vocal choreography (if it contains no singing —
   S03's pre-vocal chorus is excluded by rule 2's segment start), the
   same take's post-vocal footage at natural speed, or a frozen frame.
   Never a stretched mouth, never another line's vocal.
4. S27 is a cutaway outro: its window (260.80–268.01 s) has no song words,
   so its segment is take post-vocal only (2.96–10.0 s, ticket tear),
   never its 0–2.96 s vocal.
5. Holds/leaders are built `-an` (v3 lesson, unchanged). Every concat
   input is stream-checked (v3 lesson, unchanged). Song audio untouched.
   Captions + corner bug as in v4.

## 3. Uncovered song lines (no take sings them in that position)

These must be cutaway filler under rule 3, never stretched singing —
except the repeated-chorus case below:

- Chorus 2 gap, 135.22–161.74 s (Pay / We've / Toe / Fast repeats between
  S14's last word and S15's first word, 26.5 s): **reuse decision.**
  A 26 s freeze is worse than repeated chorus footage, and chorus
  visuals repeat in real music videos. v5 reuses the kept takes that
  sing exactly those lines in Chorus 1 — S06's Pay segment and S07's
  We've/Toe segments, plus S06's Fast segment — word-correct, footage
  repeated, disclosed as such. No new generation is spent on repeats.
- Extended-chorus gaps (baby / toll / fast repeats between S20 and S21):
  same reuse rule (S20 toll, S19 fast segments) where the gap exceeds a
  short hold; short gaps (< ~4 s) use freeze/post-vocal hold.
- All other gaps (instrumental gaps, paid/free line in Verse 2,
  253.06–257.82 s outro instrumental): freeze / post-vocal hold /
  pre-vocal choreography, mouth closed. No false singing.

## 4. Take-failure vs matcher-failure, and the refire volley

Matcher-failure (fixed by v5 anchors, no refire): S02, S03, S13, S23,
S05 (role clarified), and the tail-sweep scenes (S14's 25.6 s tail is an
assembler artifact, not a take property).

Take-failure (refire, not force-match), in priority order — volley
manifest, max 6 per the user's 07:26 message, one named axis each:

1. S08 t1 → t2, axis DELIVERY/FACING: audio is right, picture never
   clearly opens its mouth in 10 s (performance-window refire, facing
   camera, static medium close-up, full "they just keep coming").
2. S04 t4 → t5, axis DELIVERY: head garbled ("We've been, we've out"
   for "weave in, weave out"); rest of line is clean.
3. S14 t1 → t2, axis DELIVERY/FACING: first word garbled (Files for
   fast) and picture sings clearly only 0–2.0 s of a 7.38 s vocal.
4. S19 t1 → t2, axis STAGING: "wrecks just come" (take 3.84–5.66 s)
   falls in a closed head-down middle; vocal must be facing, no
   head-down stacked on it.
5. S11 t2 → t3, axis FACING: tail "money buys the clear"
   (take 4.70–6.92 s) is profile/back, mouth closed.
6. S02 t3 → t4, axis FACING: first ~9 words are profile, mouth
   unreadable; refire as a full facing performance-window take.

Not refired (disclosed nits, keep as shipped): S10 profile head,
S12 back-to-camera head, S17 "meaner" garble + closed tail, S07
paraphrase anchors (line-level, disclosed). If any refire above is
denied on QC, it is retired per skill rules (two denied rerolls) and
v5 ships that scene with its disclosed nit — it is not force-matched.

## 5. Residual limits (disclosed, not hidden)

- Audio-anchor alignment preserves word order and onsets; take-internal
  mouth lag (~0.5–1 s, v4 diagnosis) remains inside takes that were not
  refired, because the generator's mouth lags its own audio. v5 fixes
  which words are on screen when; it does not claim phoneme sync.
- Paraphrased vehicles (S07, S11, S12, S17, S18) anchor at line level:
  some take words are approximations of song words (noted per scene in
  WORD_MATCH_V5.json). Those are vehicle-vs-song paraphrases, not
  matcher jumps.
- Reused chorus footage (section 3) repeats visuals. That is the
  disclosed price of word-correct repeats without new generation.

## 6. Build order

1. Fire the 6-refire volley above; QC frames 2/5/8 per skill.
2. Re-transcribe any kept refires; update WORD_MATCH_V5.json anchors
   for those scenes only.
3. Build v5 with the v5 assembler (rules in section 2), verify
   word-by-word (prompt line + frame + mouth) against WORD_MATCH_V5.json,
   then deliver as chat attachment + announce. Never re-deliver v4.
