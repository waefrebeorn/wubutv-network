# EAR-TEST VERDICT — THE LAST SEAT E2 (finished master)

**VERDICT: PASS**

**Subject:** `masters/E2_the-last-seat_MASTER.mp4`
**MD5 verified before testing:** `9635a098436ccdf1d0ad39f4f499b827` ✓ (matches the delivered master)
**Probe:** 60.000s, 1440 frames @24fps, AAC audio 60.000s — exactly the locked format.
**Method:** full-master transcription with the house ASR route (faster-whisper
large-v3-turbo, no VAD, `work/asr_check.py`), saved to
`work/EAR_TEST_TRANSCRIPT.txt`. The transcript was read COLD first; SCRIPT.md
was opened only after the cold read was complete.

---

## ⚠ READ THIS FIRST — the raw transcript's tail is an ASR hallucination, not audio

The raw full-file transcript contains 16 extra "segments" timestamped
**60.56s–84.92s** — word salad with foreign fragments ("myкое fact is now
gone", "the samełem", "final天", "rot apagar"). **None of that is in the
master.** Proof:

1. The file is exactly **60.000s** long (ffprobe, video and audio streams).
   Segments timestamped past 60s cannot exist in it.
2. Independent re-transcription of the real **40–60s window** returns exactly
   four clean lines, ending "This house of one owes him its seat, darling."
   at ~56–60s — and nothing else.
3. Independent re-transcription of the real **57–60s window** returns only
   "…one owes him its seat, darling."

This is the known whisper failure mode (hallucinated speech over closing
ambience/silence, timestamp tokens running past end-of-file — the same class
as the NIGHT LIST U3 conform lesson). The hallucinated tail is retained in
the transcript file as raw evidence and annotated there. **All findings
below judge only the real audio: 13 segments, 0.00–59.30s.**

---

## Cold read (transcript only, before SCRIPT.md was opened)

**(a) Story sense — PASS.** A cold listener can follow the whole episode
from the spoken track alone: a dancer wants her stage kept open; the
landlord's test is stated (dance for fifty cash before the last bar); the
house holds one seat — the critic's. The count comes up short (41, not 50).
The critic names her price for staying (a cleanly landed phrase). The dancer
pays the missing nine with the cash box and her flat key — her home — and
the verdict is entered: no begging, she chose the price herself. Hanger:
the letter says the *real* critic comes final night, and the house owes
him its seat. Want → test → shortfall → cost paid in full → forward debt.
Nothing essential lives only in an unsaid sentence.

**(b) Wants stated in plain words — PASS.** All three speakers state their
want in plain first-person words by U2:
- Dancer: "I want this stage open; shall I dance again?"
- Usher: "I want that test passed without begging him."
- Occupant (critic): "I want a reason to stay."

**(c) Prompt/staging leakage & word salad — NONE in the real audio.** No
staging vocabulary is spoken anywhere in the 13 real lines. Two lines were
flagged during the cold read as *candidates* and both cleared on the script
comparison (below): the headline-compressed test line, and "he adds" —
both are a character reading a document aloud, an in-world device this
episode uses consistently (notice in U1, slip in U4, letter in U6).

**(d) Secondary characters — PASS on the spoken track.** The Usher and the
Occupant each carry multiple real lines and decisive spoken acts (the test
stated, the count cited, the stay priced, the verdict entered, the debt
declared). The Collector is a declared silent principal; his want is the
test itself, stated aloud by others. The Fruit Couple invasion is
picture-only **by script design** (silent claimants whose claim is tested
and lost on screen in U4) — their consequence is carried in picture, which
is outside what an ear-test can verify; no spoken line was owed by them
under this script's design, and none was missing.

**(e) Quote-twined nonsense — NONE.** No echo-pair collapses into the
HOLD ON failure mode. The one deliberate echo — "House of one." (U1) →
"This house of one owes him its seat, darling." (U6) — changes its variable
and lands, spoken, as a plain debt declaration.

**Observation (not a failure):** the episode has three designed speakers,
above the msg-581 two-speaker default. On the ear evidence the three
voices' wants and functions stay fully distinct and no line's sense depends
on attribution the listener can't make. Noted for the parent's law call;
it does not affect this gate's criteria.

---

## Script comparison (after the cold read)

13 scripted lines, 13 real ASR segments, **in order, word-accurate**
(ASR renders numerals as digits and drops punctuation; wording is
otherwise identical). Zero missing, zero garbled, zero unscripted lines.

| # | Script (locked) | Master ASR | |
|---|---|---|---|
| U1 Dancer | "I want this stage open; shall I dance again?" | "I want this stage open. Shall I dance again?" | ✓ |
| U1 Usher | "Landlord's test: dance for fifty cash before last bar." | "Landlord's test. Dance for 50 cash before last bar." | ✓ |
| U1 Usher | "House of one." | "House of one." | ✓ |
| U2 Usher | "I want that test passed without begging him." | identical | ✓ |
| U2 Occupant | "I want a reason to stay." | identical | ✓ |
| U3 Dancer | "Empty your pockets for your job — would you?" | "Empty your pockets for your job, would you?" | ✓ |
| U3 Occupant | "Forty-one is not fifty, even in a pretty dress." | "41 is not 50, even in a pretty dress." | ✓ |
| U4 Usher | "Forty-one short, he adds: critic stays to last bar." | "41 short, he adds. Critic stays to last bar." | ✓ |
| U4 Occupant | "A phrase is leap, turn, land — land clean and I'll stay." | "A phrase is leap, turn, land, land clean and I'll stay." | ✓ |
| U5 Dancer | "Take the box and my flat key — nine, and my home." | "Take the box and my flat key, nine, and my home." (confirmed twice, incl. 40–60s slice) | ✓ |
| U5 Occupant | "No begging, then: she chose the price herself." | "No begging then, she chose the price herself." | ✓ |
| U6 Usher | "The letter says the real critic comes final night." | identical | ✓ |
| U6 Occupant | "This house of one owes him its seat, darling." | identical (confirmed twice, incl. 57–60s slice) | ✓ |

The two cold-read flags resolve as scripted, in-world document-reading:
U1's test line is the Usher reading the landlord's notice aloud; U4's
"he adds" is the Usher reading the landlord's second slip and citing the
landlord's added condition. Neither is prompt/staging leakage.

---

## Bottom line

The finished master's spoken track is the locked script, complete and in
order, and it reads cold as a coherent story with plainly stated wants, a
real cost, an irreversible payoff, and a clean hanger. This is the first
delivered E2 master to pass the ear-test. **PASS.**
