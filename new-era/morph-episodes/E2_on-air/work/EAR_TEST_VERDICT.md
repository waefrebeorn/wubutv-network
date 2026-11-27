# EAR TEST — ON AIR E2 (finished master, cold listen)

**VERDICT: FAIL**

**Master under test:** `masters/ON_AIR_E2_MASTER.mp4`
**md5 verified before testing:** `9f2790f480e4d6b32850ad0a028981d1` (matches the
delivered master on record). 60.000s, 6 units × 10s.
**Method:** the finished master's own audio, transcribed cold — two independent
faster-whisper passes (large-v3-turbo + distil-large-v3, int8/CPU, beam 5, no VAD),
plus a third targeted pass (medium) over the U2 tail window (15–22s) and an RMS
energy audit of the gaps. The two main passes agree near word-for-word. Transcript:
`work/EAR_TEST_TRANSCRIPT.txt`. The cold read below was made from the transcript
BEFORE SCRIPT.md was opened; the script comparison followed it.
(Note: the Systran faster-whisper-large-v3 cache on this box is incomplete —
model.bin missing — so the large-v3 turbo/distil variants were used. All three
passes concur on every finding below.)

---

## COLD READ (transcript only, no script)

What a cold listener hears: people in a broadcast control room fighting over who
gets to be the singer. One wants a name taken off "the sheet," one wants the
advertiser renewed, one wants a quiet shift with his mouth shut, a challenger
claims "the singer's place is mine," a boss figure wants "billable truth," there
is an accusation ("You wrote this demo, Peter. The sheet never did."), a plea
("I don't know how. Show me how, Peter."), a rule ("Whoever sings here goes in
the next video and sheet"), a confession line ("A singer is just a mouth with
paperwork"), and then the turn, executed in speech: "Advertiser cancelled. Name
comes off." The quotable line repeats as the closer.

- **(a) Story sense:** the skeleton IS followable cold — a contest over the
  singer's place, a demonstration, a confession broadcast, a cancellation with
  consequences that are not revoked (U6 is silent). This is not the HOLD ON
  mishmash failure at full strength.
- **(b) Wants in plain words:** mostly yes — name off the sheet, advertiser
  renewed, one quiet shift, singer's place claimed, all stated as plain
  "I want…" lines. Exception: "I want billable truth" (heard twice) is jargon,
  not a plain-words want — cold, it does not say what should happen.
- **(c) Garble / leakage:** no staging or prompt vocabulary is spoken, and no
  line is word salad. One token is opaque: "Red means live, UN4." — heard
  identically by all three ASR passes (see Finding 3).
- **(d) Invader / secondaries:** Peter and Laura are named in dialogue and act
  in speech. The challenger, as heard, is a single disembodied claim — "The
  singer's place is mine" — with no name, no number, and no second line.
- **(e) Twined lines:** the designed twines mostly survive being heard (the
  "mouth shut" exchange parses as an argument; the repeated "mouth with
  paperwork" works as a refrain). Two scripted lines are weak as heard: the
  opener "This sheet knew yesterday" (a sheet cannot know; the conceit needs
  the picture) and "My mouth stays shut, mine." (the elliptical tail dangles
  cold). Both were delivered exactly as scripted — design nits, recorded as
  observations, NOT grounds for this verdict.

## SCRIPT COMPARISON (after the cold read)

12 scripted lines. 10 are present in the master verbatim and intelligible.
The failures:

### Finding 1 — ABSENT: the invader's identifying half-line
Scripted (CHAMPION, U2, [INVASION]): **"Number Four. The singer's place is mine."**
Heard (17.14–18.16): only **"The singer's place is mine."**
"Number Four." — the invader's name/rank announcement, the number-on-head
format's signature beat (rank announced aloud) — is not in the master audio.
All three ASR passes concur; the RMS audit shows the 16.5–19.5s band is fully
accounted for by the three heard lines packed back-to-back, with no unaccounted
speech window where the words could sit. As delivered, the invader never says
who he is. This is the NIGHT LIST v3 failure class (invader content missing
from the finished master), and against the msg-579 standard the invader is
left with half of one line and no spoken identity.

### Finding 2 — ABSENT: the Colonel's condition line (the payoff's cause)
Scripted (COLONEL, U2, intercom): **"I want billable truth. A false name and
I cancel the advertiser."**
Heard (18.34–19.44): only **"I want billable truth."**
"A false name and I cancel the advertiser." is not in the master audio (three
passes concur; the only unaccounted energy after 19.44 is a ~0.5s burst at the
U2→U3 joint — the aired segment coming in — far too short for the 8-word line).
This line is the stated condition that causes the U5 execution ("Advertiser
cancelled. Name comes off."). Without it, the cancellation lands in U5 with
its reason never spoken.

### Finding 3 — UNINTELLIGIBLE: the protagonist's name
Scripted (PETER, U2): "Red means live, **UNC**."
Heard by all three passes: "Red means live, **UN4**."
This is the only time the protagonist is named in the episode's speech, and as
spoken it does not land — a cold listener hears an unexplained code, not a
name. (Distinct from staging leakage: the script intended a name; the audio
fails to deliver it intelligibly.)

### Not counted
- Distil pass alone renders a faint "Thank you." at 59.52–60.00s (U6 is
  scripted silent). RMS in that window is 404 (peak 1454) against a music-bed
  RMS of 1779 — too quiet for real speech; classified as a probable ASR
  hallucination over the fading music tail, NOT unscripted dialogue.
- Voice/character match (msg 581) cannot be judged from an ASR transcript and
  was not assessed; this verdict rests on the transcript cold-read protocol.

## VERDICT

**FAIL.** Two scripted speech elements are absent from the finished master —
the invader's identifying half-line and the causal condition line for the
episode's payoff — and the protagonist's only spoken name-check is
unintelligible as delivered. Per the standing ear-test rule (msgs 579/581 and
the NIGHT LIST v3 precedent), a master whose own transcript is missing
scripted lines does not clear, whatever its paper gates say. The episode's
story skeleton, its stated wants, and its executed payoff are genuinely
stronger than the HOLD ON failure mode — but the gate is binary, and this
master does not pass it.
