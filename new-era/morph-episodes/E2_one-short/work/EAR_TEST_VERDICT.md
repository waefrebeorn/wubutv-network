# EAR TEST — ONE SHORT E2 "Twenty-Four Chairs" — FINISHED MASTER

**Master:** masters/oneshort_E2_master.mp4
**MD5 verified before testing:** 0d57f2c57f47c6447cf2278ad001c140 ✓ (matches the delivered master)
**Method:** full-master audio transcribed with the episode's own ASR rig
(faster-whisper large-v3-turbo, local snapshot, vad_filter=False) →
work/EAR_TEST_TRANSCRIPT.txt. Transcript read COLD first (no script);
script comparison run only after the cold read was complete.
**Scope note:** this is a transcript-based cold listen — the only dialogue
check that counts per the standing master-ASR rule. Voice/character timbre
match cannot be assessed from ASR text and is not claimed here.

## VERDICT: PASS

---

## PART 1 — COLD READ (transcript only, before opening SCRIPT.md)

**(a) Does the spoken dialogue make sense as a story on its own? YES.**
Cold, the ear gets a complete arc: a counting office is told to certify
24 chairs because "Hall pays by the chair" [0.00]. Staff state they want
one settled count by five o'clock. A count proceeds in batches — "Six,
twelve, eighteen. Wobbly again." [22.92] — and a dispute surfaces: chairs
must be marked "or one counts twice" [30.00]; someone "moved it back to
count twice" [40.12]; the recount lands on 23, "Same as us" [42.36];
"One broke. Hall pays 24." [45.26]; the distinction is stated outright —
"24's a claim. 23's chairs." [47.58] — and the claim is settled at the
real number: "I'll sign 23. Lose one chair, clerk." [50.42]. The closer
turns the count on the office itself: "What happens counting this
office?" / "Shelf, umbrella one, chair two, book three." [53.54–57.36].
Want → cheat → catch → verdict → cost → coda, all audible.

**(b) Is every speaker's want stated in plain words? YES.**
"I want one settled count by five o'clock." [10.36] · "One count
settled. That's all I want." [13.66] · "Certify 24 chairs. Hall pays by
the chair." [0.00] · "He needs 24 paid, Hale." [28.00] · "I'm five.
Certify my five." [16.26]. No want has to be inferred from staging.

**(c) Prompt/staging leakage or word salad? NONE FOUND.**
No staging language, no camera/prompt vocabulary, no garbled lines.
Every line is a complete, speakable sentence. (Contrast class: NIGHT
LIST v3's "Drive-drive bed wanted, nothing carried" — nothing of that
kind appears anywhere in this master.)

**(d) Invader/secondary characters — real lines, consequence? PARTIAL — flagged observation, see Part 3.**
The secondary claimant is audible exactly once: "I'm five. Certify my
five." [16.26] — a real line, plainly spoken, want stated. By ear alone,
nothing further is ever said to or by him and no spoken consequence
lands for him; whatever becomes of his claim is carried by picture only.

**(e) Quote-twined lines that pass on paper but sound like nonsense spoken? NONE.**
The two most compressed lines were examined specifically:
- "Recounts cost what got counted twice." [37.62] — aphoristic, but in
  sequence (it follows "Mark each chair, or one counts twice" and
  precedes "You moved it back to count twice") it parses on first listen
  as a price rule: a recount costs the double-counted amount. It is NOT
  a HOLD ON-style empty twine ("Believed isn't"); the words carry the
  rule.
- "Keep one per recount, counter." [53.54] — parses as the cost term
  stated before the closing question. Recoverable in context.

**ONE SHORT-specific: is the count followable by ear? YES.**
The number thread closes arithmetically in speech alone: 24 claimed →
counted in sixes (6, 12, 18) → double-count caught → recount 23 →
one broke → signed 23, claim distinguished from chairs. A cold listener
can recount the episode from the audio.

## PART 2 — SCRIPT COMPARISON (run after the cold read)

All **16 of 16** scripted lines are present in the master, verbatim
(ASR number formatting aside), in script order. None missing, none
garbled, none reworded:

| # | Script line (speaker) | Master ASR | Time |
|---|---|---|---|
| 1 | "Certify twenty-four chairs — hall pays by the chair." (HALE) | "Certify 24 chairs. Hall pays by the chair." | 0.00–4.00 |
| 2 | "I want one settled count by five o'clock." (CLERK) | exact | 10.36–13.08 |
| 3 | "One count, settled — that's all I want." (COUNTER) | "One count settled. That's all I want." | 13.66–15.78 |
| 4 | "I'm five — certify my five." (CHAMPION) | "I'm five. Certify my five." | 16.26–18.54 |
| 5 | "Six, twelve, eighteen — wobbly again." (COUNTER) | exact | 22.92–26.54 |
| 6 | "He needs twenty-four paid, Hale." (CLERK) | "He needs 24 paid, Hale." | 28.00–29.54 |
| 7 | "Mark each chair, or one counts twice." (COUNTER) | exact | 30.00–32.18 |
| 8 | "You counted with us — what'd you get?" (COUNTER) | "You counted with us. What do you get?" | 34.38–36.14 |
| 9 | "Recounts cost what got counted twice." (CLERK) | exact | 37.62–39.72 |
| 10 | "You moved it back to count twice." (COUNTER) | exact | 40.12–41.60 |
| 11 | "You counted twenty-three — same as us." (CLERK) | "You counted 23. Same as us." | 42.36–44.56 |
| 12 | "One broke; hall pays twenty-four." (HALE) | "One broke. Hall pays 24." | 45.26–47.00 |
| 13 | "Twenty-four's a claim. Twenty-three's chairs." (CLERK) | "24's a claim. 23's chairs." | 47.58–49.70 |
| 14 | "I'll sign twenty-three, lose one chair, Clerk." (HALE) | "I'll sign 23. Lose one chair, clerk." | 50.42–52.90 |
| 15 | "Keep one per recount, Counter — what happens counting this office?" (HALE) | exact (case aside) | 53.54–56.74 |
| 16 | "Shelf: umbrella one, chair two, book three." (COUNTER) | "Shelf, umbrella one, chair two, book three." | 57.36–59.34 |

**Unscripted speech: none of substance.** Two ASR tail artifacts at the
file boundary, neither is evidence of added dialogue:
- The final line is re-emitted twice at 59.34–59.48 with zero-duration
  word timestamps — the known whisper loop artifact over a held final
  frame, not repeated speech.
- A lone fragment "The" at 59.86–60.14, over the silent closing freeze
  (no speech is scripted there) — consistent with whisper hallucination
  over ambiguous tail audio (the standing ASR-hallucination caution).
  One function word; no content.

## PART 3 — OBSERVATIONS (recorded; none changes the verdict)

1. **The Champion's spoken footprint is one line.** His want is stated
   ("I'm five. Certify my five.") but his thread is never resolved in
   speech — his marking/re-rank is picture-only (script confirms this is
   by design: one line, U2). This sits against the msg-579 invader
   amendment (≥2 real lines + a visible action with consequence). The
   visible-action half is a picture question outside this gate; the
   spoken half is a fact of the master and is recorded here for the
   parent's law-vs-build judgement. It is not an ear failure: the line
   he does get is clean, plain, and load-bearing in the queue of claims.
2. **GAP 1 runs long by ear:** ~4.4s of silence between the Champion's
   line (ends 18.54) and the count chain (starts 22.92), against a
   scripted 2–3s digestion gap. The carrier is visual (the sliding
   chair); ear-neutral, noted for the record.
3. **First speech onset is immediate** (0.00) — no dead head in the
   audio.

## BOTTOM LINE

This master survives being heard. The dialogue is complete, verbatim,
in order, and cold-legible; the wants are spoken; the count closes by
ear; there is no prompt leakage, no word salad, and no empty twine.
That is precisely the set of failures that killed HOLD ON E2 and
NIGHT LIST v3, and none of them is present here.

**EAR TEST: PASS**
