# EAR-TEST VERDICT — THE NIGHT LIST E2 v3

- Master: `masters/E2_the-night-list_v3.mp4` (md5 `7be7d8b8702a019ac19f95100b9d285c`)
- Transcript: `work/EAR_TEST_V3_TRANSCRIPT.md` (faster-whisper `small`, `vad_filter=False`)
- Reader: fresh-context cold listen. **The cold read below was written from the transcript and audio forensics ONLY, before SCRIPT.md was opened.**

## VERDICT: EAR-TEST FAIL

---

## PART 1 — COLD READ (transcript + audio only, no script, no staging notes)

### (a) Does it make sense as spoken English? Can a first-time listener follow it?

Partially — and partial is not enough. A first-time listener can extract a skeleton:
a night desk somewhere with **ten beds and eleven names**; somebody wants "quiet" and
their name taken off the list; a man named **Elias** needs the bed or he "sleeps wet";
somebody wants the bed **sold**, and a man named **Peter** has cash. There is a rule
about a name being spoken and a bag being carried by "the same hands."

But the listener cannot say **what actually happened**:

- The count changes mid-episode with no spoken reason: "eleven names for ten beds"
  (×3) becomes "Ten names, ten beds. None mine." at 45.5s — then the closer at 55.2s
  goes back to "Eleven names, ten beds." Did someone get struck off, or not? The audio
  never plainly says.
- The outcome is never stated in plain words. Does Elias get the bed? Is the bed sold
  or kept? The resolution is encoded in aphorisms — "Money speaks, Peter doesn't."
  "Carrying hands hold no money." — and in repeated tallies, not in anything anyone
  says or decides out loud.
- Most of the dialogue is refrain-chant, not people talking to each other: "same
  hands" recurs four times, "eleven names, ten beds" three times, whole lines are
  re-recitations of the rule.

**Nonsense / unintelligible lines (as heard):**

- **[48.72s] "Drive-drive bed wanted, nothing carried."** — word salad as heard. A
  second, independent ASR pass over this span hears "dry dry bed wanted, nothing
  carry" with low word probabilities (0.42–0.49) — two passes cannot agree on the
  words, which means the delivery itself is mumbled/garbled at this point, not that
  the ASR is at fault. Even taken at face value, "bed wanted" is classified-ad
  shorthand, not a sentence a person says.
- **[43.26s] "Tight rope, same hands. Sleep tight."** — "tight rope(s)" comes back
  low-confidence (p≈0.27–0.39) in both passes; as heard it is a non-sequitur wedged
  between refrains.

### (b) Speakers and voice consistency

A transcript cannot certify timbre, so I ran a crude per-segment pitch (F0) proxy over
the extracted audio. It shows two registers alternating in blocks — a low voice
(~110–155 Hz) opening and closing the episode, a higher voice (~220–262 Hz) carrying
most of the middle segments — consistent with **two speakers**, and no segment shows
a voice changing identity mid-line. Voice consistency is **not** a failure point for
this master; the failures are in the words themselves.

### (c) Prompt-detail / stage-direction leakage

Yes — the episode's admission rule is spoken aloud as shorthand, twice:

- **[14.42s] "Door test, name spoken, bag carried, same hands."** Word-level ASR
  shows it is delivered as four separate checklist fragments — "Door test. / Names
  spoken. / Bag carried. / Same hands." — all at high word probability, i.e. clearly
  spoken, clearly a recited checklist. That is a staging rule / prompt detail read
  aloud, not a person telling another person anything.
- **[40.34s] "Elias, spoken, carried, same hands."** — the same checklist, compressed
  and repeated.
- **[2.12s] "Say it with me."** — an instruction to recite, closer to direction than
  dialogue.

### Cold-read score against the PASS bar

| PASS requirement | Result |
|---|---|
| Cold listener can follow the story from audio alone | **NO** — gist yes, outcome no; the 11→10→11 name count is unexplained in speech |
| Zero prompt-detail leakage | **NO** — the door-test checklist is spoken as fragments, twice |
| No nonsense lines | **NO** — [48.72s] unintelligible in two ASR passes; [43.26s] "tight rope(s)" likewise |
| Voices consistent per character | No evidence of failure (two-register pattern, no mid-line swaps) |

---

## PART 2 — SCRIPT COMPARISON (SCRIPT.md opened only after Part 1 was written)

The script (repair round v3, round 2) has 18 lines across 4 speakers: KEEPER,
LAURA, UNC, BLOB PRINCE. Compared line by line against the master's audio:

### Present and clean (12 lines)
Keeper's want ("I want quiet. My name off."), Laura's want ("Quiet? … I want it for
Elias."), the door test, Laura's stakes ("Without it, Elias sleeps wet."), UNC's want
("Wet. I want that bed sold."), Laura's U3 fact ("Outside too. Peter's never stood
here."), UNC's offer ("Want it sold? Peter's cash."), the money rule ("Carrying hands
hold no money."), UNC's slip ("These hands weren't at that board."), Laura's
counter-claim ("Board hands. Elias wants it. Money speaks, Peter doesn't."), Laura's
pass ("Elias, spoken, carried, same hands."), the count ("Held tight. Ten names, ten
beds. None mine."), and the closer ("Eleven names, ten beds. Desk tonight. Tomorrow
mine." — clean, high-confidence).

### Absent from the audio (3 scripted lines)
- **LAURA U1 opener — "You put him back on. Eleven names—" — NOT SPOKEN.** The line
  that sets up the whole episode (the struck name restored, the complaint) never
  reaches the listener.
- **KEEPER U2 ruling — "Unspoken. Bag outside." — NOT HEARD.** Nothing is audible in
  its slot (~20.0–22.4s). The Keeper's only ruling on Peter's claim is missing, so a
  listener never hears the claim graded.
- **BLOB PRINCE U2 — "Mine's outside. I want a dry bed." — NOT HEARD.** The invader,
  one of four scripted speakers, never audibly speaks at all. His want reaches the
  listener only through the Keeper's later restatement — the exact "invader who said
  and did nothing" failure the showrunner named on the previous episode.

### Garbled in delivery (2 lines)
- **KEEPER U5 teach — "Tight ropes, same hands: sleep tight."** The load-bearing
  phrase "tight ropes" is low-confidence (p≈0.27–0.39) in two independent ASR
  passes — mumbled below intelligibility. As heard: "Tight rope, same hands."
- **KEEPER U5 floor rule — "None mine — dry bed wanted, nothing carried: dry floor."**
  Heard as **"Drive-drive bed wanted, nothing carried."** The line's head ("None
  mine — dry") is garbled into word salad and its verdict words **"dry floor" are
  missing entirely** — the Blob Prince's settlement, the episode's second payoff,
  is never intelligibly spoken.

### Unscripted audio (the opening line)
The master's first spoken line (2.12s) is **"Desk takes the last bed, eleven names
for ten beds. Eleven names. Say it with me."** — none of this is in SCRIPT.md. It
(a) replaces Laura's scripted opener, (b) states the opposite of the story — the
Keeper takes *no* bed; his name comes *off* — and (c) contains "Say it with me," a
recitation instruction that is neither scripted dialogue nor anything a character
would say: direction leaking into the audio, exactly the failure class this gate
exists to catch.

### Speaker attribution
The script's four voices collapse to two pitch registers in the audio, and with the
Blob Prince's line absent, at most three characters are ever heard. No mid-line
voice swap was detected; attribution is not a scored failure — absence is.

### Effect on the cold read
The comparison strengthens every cold-read finding. On paper the count's arithmetic
is explained (Keeper strikes his own name, Peter is struck for Elias, the Keeper
re-files his claim for tomorrow) — but the audio drops the opener that sets up the
strike, drops the ruling, garbles the floor settlement, and opens with an unscripted
line that contradicts the premise. A listener with only the audio cannot reconstruct
the story the script tells. That is the definition of this gate's FAIL.

---

## FINAL VERDICT: **EAR-TEST FAIL**

THE NIGHT LIST E2 v3 does **not** ship on this master. It fails on nonsense in the
ear (the floor-rule line heard as "Drive-drive bed wanted, nothing carried," its
verdict words "dry floor" never spoken; "tight ropes" mumbled below intelligibility),
on prompt/direction leakage (the unscripted "Say it with me" opener; the door-test
checklist spoken as fragments, twice), and on story followability (scripted opener,
the Keeper's ruling, and the invader's only line all absent from the audio). The
paper gates passed this episode; the ear does not.
