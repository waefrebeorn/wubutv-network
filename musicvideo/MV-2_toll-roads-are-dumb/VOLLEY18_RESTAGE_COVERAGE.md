# Volley 18 — character restages (2026-11-04)

Format matches VOLLEY14/15/16/17_GAP_COVERAGE.md. No commit, no ledger edit,
no announcement, no posting, no chat delivery — the parent verifies,
commits, and delivers.

## Why this volley exists (correction to the volley-17 record)

During v6 assembly verification, the mouth-state cut pass re-viewed the
volley-17 QC frames on disk (`qc_frames_v6v17/s07_v6final_t1_*s.png`,
`s21_v6final_t1_*s.png`, `s04a_*s.png`). All three volley-17 takes show
the SAME performer — but it is NOT the night-VOICE of the rest of the
video: darker skin, rounder face, gold chain, daytime open-road setting.
The volley-17 record's "character PASS (same THE VOICE face)" verdicts
for S07, S21, and S04a are WRONG: the reviewer judged costume/props
(suit, shirt, square, mic, ticket) but not the face against THE VOICE.
The volley-17 prompts used open-road daytime staging with a thin
identity lock (hair, shave, costume — no face description, no night
setting), and the generator rendered a different performer.

All three slots are long lines (6.7–9.2s) that cannot be covered, and
no earlier take passes for them (S07 t2 lyric-fails, S21 t2 ratio-fails
at 1.73, S04 t1 facing-fails). The brief's planned retry rule — "1
restage retry ONLY if a take fails on character/text (fixable axis)" —
triggered for all three. This volley is those three restages.

## Cap accounting

Task cap: at most 6 new videos total, including retries. Volley 17 +
S04a used 3. This volley used 3 (S07, S21, S04a restages). Total used:
6/6. Remaining cap: 0. NO further videos may be fired for this task
under any circumstances.

## Prompts (55-rule construction, with a fixed identity lock)

Framing + identity lock first sentence (medium close-up, locked-off
steady camera, THE VOICE with a full FACE description: light olive
skin, narrow angular face, sharp cheekbones, slicked-back dark hair,
clean-shaven, no jewelry, no chain, INK suit, BONE shirt, CADMIUM
pocket square, chrome mic on stand, blank paper ticket, AT NIGHT IN A
TOLL PLAZA), performance window with a local whole/half-second
bracket, exact lyric in quotes twice, articulation clause, no other
visible character, action only before the first word or after the last
word, closed-mouth hold + stable end pose, no whisper/mumble/hushed/
softly language, one singer, forbidden checklist at the end (adding:
no daytime setting, no gold chain, no necklace, no other face).

CONSTRUCTION ERROR, disclosed: the restage prompts OMITTED the
"flat cartoon" style term that the volley-17 prompts carried. The
generator returned PHOTOREALISTIC live-action night-plaza footage for
all three restages — a style break far worse than the face change they
were meant to fix — plus legible on-screen text ("STOP", "FAST LANE"
signs, printed ticket text). All three restages are therefore REJECTED
on character + text, and the cap is spent, so the restage route is
closed. The assembly keeps the volley-17 takes with the character
inconsistency DISCLOSED (see §Assembly consequence).

- S07 restage: window "from 1.0 to 8.0 seconds", lyric "We've been
  slamming the danger roads, toll roads are dumb", 9-second clip.
- S21 restage: window "from 0.5 to 9.5 seconds", lyric "The wrecks
  just come, pay to go faster, the rest of us slow", 10-second clip.
- S04a restage: window "from 0.0 to 9.5 seconds", lyric "Now they got
  the fast lanes, the rich ones fly on by, while the rest of us crawl,
  watching money flash by", 10-second clip.

All three landed on the first attempt; 0 server failures.

## Gate order (as in volleys 14–17)

Lyric sequence FIRST, ratio second (usable 0.80–1.25; grey 0.60–0.80 /
1.25–1.60 with warp-rescue only ≤1.5x to band edge and gates re-run),
frame gate third (FAIL if vocal near-dup run ≥24f during vocal OR
vocal mean diff <0.5), character gate, exactly-once check including
beat-word subsequence repeats, split-half recheck on zero-word
decodes. Mishear classes normalized for matching only (raw kept):
tall/told/toe=toll, done=dumb in hook, paid=pay, plasers=plazas,
comin'=coming, tell=sell. QC script note: the first restage QC run
had a norm() bug (Whisper's leading space survived stripping, so
0/10, 0/14, 0/22 matched); fixed by stripping whitespace before
punctuation and re-matching from the saved dictations — the
dictations themselves were correct.

## Per-take results — ALL THREE REJECTED, none assembled

### S07 restage — REJECTED (frame FAIL + character FAIL + text FAIL)

- Raw: `takes/media-generation-mv2-s07-v6restage-t1-0-8f7dab73-93a7-46a3-b72a-a0bbd81c95de.mp4`
- Canonical: `takes/mv2_s07_v6restage_t1.mp4`, md5
  `ca741e7b99aede868d74331eab1dcfe3`, 1280x720/24fps/10.000s.
- Lyric: all 10 words exactly once (we've 0–0.68, been, slamming, the,
  danger, roads, toll [raw "Tall"→toll class], roads, are, dumb
  6.24–6.94). Vocal span 0–6.94s vs song 8.50s → ratio 1.2248 IN BAND.
  (Take sings from 0, not the prompted 1.0 — prompt window is a
  guide; gates use measured timing.)
- Frame: FAIL (mean 0.496 < 0.5, near-dup run 20, frozen run 0).
  Marginal by 0.004, but the gate is held (R3 t9 precedent: 0.49919
  held FAIL). Note: at its assembly factor 1.2248 the sped-up picture
  would move more, but the gate as written applies at natural speed.
- Character: FAIL — photorealistic live-action man, not the cartoon
  VOICE; night toll plaza with legible "STOP" signage.
- Text: FAIL — legible "STOP" signs + printed ticket text.
- VERDICT: REJECTED. S07 slot keeps the v6final take (lyric + ratio +
  frame PASS, character disclosed inconsistent — see §Assembly
  consequence). No second retry: 1 restage only, cap spent.

### S21 restage — REJECTED (character FAIL + text FAIL)

- Raw: `takes/media-generation-mv2-s21-v6restage-t1-0-9426db66-f405-414e-b075-2ebae84e06b1.mp4`
- Canonical: `takes/mv2_s21_v6restage_t1.mp4`, md5
  `ea03a7238108e38e74333caa537727a6`, 1280x720/24fps/10.000s.
- Lyric: 13/14 with the SAME disclosed micro-gap class as v6final:
  the take drops the second "to" (faster [gap 5.18–6.0] the rest of
  us slow). Deletion-tolerant alignment: the, wrecks, just, come,
  pay [raw "paid"→pay class], to, go, faster, (to dropped), the,
  rest, of, us, slow. Vocal span 0–7.62s vs song 9.24s → ratio
  1.2126 IN BAND. (Naive strict-subsequence matching reported 8/14
  and ratio 1.7838 by truncating at "faster" — wrong; the words
  after the gap match with one deletion, as in v6final.)
- Frame: PASS (mean 0.541, near-dup run 20, frozen run 3).
- Character: FAIL — photorealistic live-action man, not the cartoon
  VOICE.
- Text: FAIL — legible plaza signage + printed ticket text.
- VERDICT: REJECTED. S21 slot keeps the v6final take (13/14 with the
  same dropped-"to" micro-gap, character disclosed inconsistent).
  No second retry: 1 restage only, cap spent.

### S04a restage — REJECTED (lyric FAIL + character FAIL + text FAIL)

- Raw: `takes/media-generation-mv2-s04a-v6restage-t1-0-c8ac8d4b-19bd-4486-bea4-3c6826e49ba8.mp4`
- Canonical: `takes/mv2_s04a_v6restage_t1.mp4`, md5
  `745dacbcd89807be0504f0af22adbe9d`, 1280x720/24fps/10.000s.
- Lyric: FAIL — 18/22 matched, missing the entire tail ("watching
  money flash by"). Take sings now through crawl (0–7.32s), then a
  tail recheck (7.0–10.0s, split-half pattern) hears only "From..."
  (7.00–8.34) — not the prompted tail. The 18-word portion alone
  (vocal 0–7.32 vs its song span, ratio 0.9208 if measured against
  the full 6.74s slot) cannot pass: lyric gate is FIRST and the tail
  is absent. A split (restage mouth for 18 words + cover for the
  4-word tail) was considered and REJECTED with the take: the
  restage is photorealistic, so it cannot supply a cartoon mouth
  for any part of the slot.
- Frame (18-word portion): PASS (mean 0.942, near-dup run 7, frozen
  run 2) — moot, lyric fails first.
- Character: FAIL — photorealistic live-action man, not the cartoon
  VOICE.
- Text: FAIL — legible "FAST LANE" signs + printed ticket text.
- VERDICT: REJECTED. S04a slot keeps the v6final warped take (lyric
  + ratio + frame PASS, character disclosed inconsistent). No
  second retry: 1 restage only, cap spent.

## Assembly consequence (disclosed, not hidden)

Three slots show a DIFFERENT cartoon face from the rest of the video
(daytime-other performer: darker skin, rounder face, gold chain,
daytime open-road setting; consistent across the three takes, but
different from the night-VOICE of every other slot):

- S04a 34.56–41.30 (warped v6final, 6.74s)
- S07 72.28–80.78 (v6final, 8.50s)
- S21 205.20–214.44 (v6final, 9.24s)

Total: ~24.5s of the 268.01s video. Costume, props, mic, ticket, and
cartoon style match; the FACE does not. This is the single largest
known defect in v6 and must be flagged prominently in the delivery
note — the parent/user is the final judge of whether it ships. No
further generation is available under the task cap to fix it.

## Files

- `TAKE_WORDS_V6_RESTAGE.json` (dictations, corrected matches, frame
  gates; S21 corrected alignment noted inside)
- `qc_frames_v6v17/s07_restage_{2,5,8}s.png`,
  `s21_restage_{2,5,8}s.png`, `s04a_restage_{2,5,8}s.png` (the 5s
  frames show the photorealistic break + text; the 2s/8s frames were
  extracted but not individually reviewed — the 5s frame alone
  decides character/text)
- Restage takes on disk (rejected, never assembled): listed above.
