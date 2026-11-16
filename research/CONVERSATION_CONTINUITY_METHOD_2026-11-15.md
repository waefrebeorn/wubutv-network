# CONVERSATION + SERIAL CONTINUITY — METHOD BUILD B

**Commission:** user verdict on the first pilots, 2026-11-15 (Telegram
msg 440): *"the stories are good in a single shot but if you use the
subjects over and over, they're not gonna make a lot of sense and they'll
just repeat on themselves recursively — we need to actually have
conversation conversations and create better ways forward."*

**Scope:** writing method only. No generation, no refires. This document
proposes (a) a dialogue method that produces CONVERSATION inside the
10-second atom, and (b) a per-show continuity ledger that makes serial
state real, plus the rule that binds them: **a conversation turn is the
only legal way to change the ledger, and the ledger is the only memory a
returning subject has.** Where this method amends standing grammar it
says so openly (§9) — it does not silently override the show documents
or the FIRST_SECOND_DOCTRINE.

---

## §0 — THE HONEST VERDICT ON THE PILOT DIALOGUE LAW

The pilot law was: *one conversation chain per episode, every line a
speech act to a named addressee, ≤9 words, one unspent fact per unit,
nothing resolves.* Judged against the shipped pilots, it produced
**correspondence, not conversation.** Evidence:

- **Every pilot line is a first move; nothing is ever an answer.**
  PILOT-2's six lines — command → rule → report → counter-question →
  verdict → refusal — each responds to the *situation*, never to the
  previous line's actual words. The Watcher never answers "Hold this";
  the Courier never answers the rule she is told. In conversation-
  analysis terms (Sacks/Schegloff/Jefferson), every line is a first
  pair part and no second pair part ever lands — so no line ever
  *costs* its speaker anything, because nobody is ever caught by a
  reply.
- **The reply, when the chain format implies one, arrives a full unit
  later** — after a world-swap, addressed to a new situation. A
  10-second gap plus a rebuilt world dissolves the pressure a question
  exerts. Real conversation runs on conditional relevance: once a
  question is out, its answer is *noticeably absent* until it appears.
  The pilot format makes absence invisible.
- **Nothing changes between the speakers.** PILOT-4's Clerk and Counter
  end the episode in exactly the relation they started it: she dares,
  he counts. Six units, zero concessions, zero debts, zero knowledge
  transferred. The *count* moved (1000→1005); the *people* didn't.
  That is the recursion the user named: if lines respond to situations
  and situations are regenerated from the same premise, the same
  line-shapes recur forever, re-skinned.
- **The one accidental conversation in the pilots proves the point.**
  PILOT-2 U5's line arrived split — "You carried it to yourself."
  (2.26–3.72s), a long pause, then "Sign for it." (8.16–8.96s) — and
  PILOT-4 U6's cliff cuts the Counter mid-word. Both read as *more*
  conversational than the clean lines around them, because both imply
  a listener reacting in real time. The generator already knows how;
  the law never asked it to.

The show treatments' own chains (SHOW-1..5) are better than the pilots
— they are genuine 4-turn exchanges — but they spend one turn per unit,
so a 4-unit episode holds exactly one 4-turn conversation and each turn
still lands in a fresh world. The fix is not better lines. The fix is a
different atom: **the pair, not the line.**

---

## §1 — UNIT ECONOMICS (MEASURED, NOT ASSUMED)

Speech timings measured from PILOT-2's ASR transcripts
(GATE_LOG, faster-whisper large-v3-turbo, no VAD):

| Unit | Line | Words | ASR span | Duration | Rate |
|---|---|---|---|---|---|
| U1 | "Hold this. The street is leaving." | 6 | 5.60–8.14s | 2.54s | 2.36 w/s |
| U2 | "The street moves every ten seconds. The parcel doesn't." | 9 | 4.12–8.38s | 4.26s | 2.11 w/s |
| U3 | "This address doesn't exist anymore. The street moved." | 8 | 5.34–8.90s | 3.56s | 2.25 w/s |
| U4 | "Who do I give it to?" + "The name is mine." | 9 | 4.82–7.12s (two bursts) | ~1.96s speech | ~2.3s span |
| U5 | "You carried it to yourself." + "Sign for it." | 6 | 2.26–3.72 + 8.16–8.96s | ~2.26s speech | split delivery |
| U6 | "Then the next me signs it. Not me." | 8 | 5.44–8.26s | 2.82s | 2.84 w/s |

**Measured delivery rate: ~2.1–2.8 words/second** for generated speech
in this pipeline (consistent with natural conversational pace).
PILOT-4's gate log records exactness but not per-line spans; its lines
(5–7 words) all landed inside their units with room to spare.

**The 10s unit's budget, honestly drawn:**

- 0.0–1.5s — HOOK. Silent by doctrine (F4: sound-off legible). No line
  may start here.
- 1.5–4.0s — STATE. Picture only; the audience is reading the world.
- 4.0–9.0s — **the dialogue window: 5.0 seconds.**
- 9.0–10.0s — CLIFF. The handoff device (mouth onset / name / number /
  carry / gaze). A cliff *fragment* may live here; it is device, not
  dialogue, and is not charged to the pair budget.

**What fits in 5.0 seconds:**

| Shape | Composition | Speech time | Fits? |
|---|---|---|---|
| One full turn (old law) | 6–9 words | 2.5–4.3s | Yes — and wastes the window; the leftover silence is why pilots feel like monologues |
| **ONE PAIR (new standard)** | Turn 1 ≤7 words (~2.5–3.3s) + reaction gap 0.2–0.5s + Turn 2 ≤7 words (~2.5–3.3s) | 5.2–7.1s total incl. gap — turn 1 may start at 3.5s, riding the picture turn | **Yes, if turns are capped at 7 words** |
| Fragment chain | 3 turns × ≤4 words (~1.4–1.9s each) + 2 gaps | ~4.6–6.7s | Yes — for accusations, verdicts, counting fights |
| Pair + cliff fragment | Pair as above + device word at 9–10s | — | Yes — the fragment is the handoff, already budgeted |

Reaction gap: conversation analysis finds responses in natural talk
typically land within ~0.2s (Stivers et al. 2009, via CA summaries).
Write the gap as **0.2–0.5s of visible reaction** (a look, a stopped
hand) — never zero (turns mush together) and never >1s except for a
scripted dispreferred delay (§3, P6).

**Episode arithmetic:** a 6-unit episode at one pair per unit is **one
conversation of up to 12 turns** — the same turn-count as a full
STATION-era chain, but compressed so every turn is answered while its
pressure is still warm. A 3–4 unit episode is 6–8 turns. Either way:
ONE conversation per episode, designed as a single arc of pairs (§4),
not six monologues in a trench coat.

---

## §2 — THE PAIR LAW (PROPOSED GRAMMAR AMENDMENT)

This amends the show grammar's "exactly one spoken line per unit at
7–9s, ≤9 words." The amendment is flagged for adoption, not assumed
(see §9, Conflict 1).

1. **One exchange per unit.** A unit's dialogue is ONE adjacency pair
   (two turns, two speakers) or ONE fragment chain (three turns,
   ≤4 words each). The second turn must be a true *second pair part*:
   it answers, refuses, concedes, corrects, or counter-questions the
   first turn's actual words.
2. **Word caps.** Standard turn ≤7 words. A unit may run one long turn
   of ≤9 words only if its partner turn is a fragment of ≤3 words.
   Total spoken words per unit ≤16 (cliff device fragment excluded).
3. **Placement.** Turn 1 rides the picture TURN (start 3.5–6.0s). Turn
   2 is the doctrine line — it sits at 6.5–8.7s and does the reframing
   the FIRST_SECOND_DOCTRINE (L4) demands of "the line." All pairs
   close by 8.7s (8.5s in THE MACHINE — see §9, Conflict 4). The cliff
   stays clean.
4. **Every turn is a speech act with a named addressee and a named
   want** (doctrine L2, unchanged — now applied per turn, not per
   unit). One act per turn.
5. **No turn restates the hook fact** (doctrine L1, unchanged). Turn 1
   does something ABOUT the fact to the other character; turn 2 does
   something about turn 1.
6. **The narrator test binds every turn** (unchanged). A turn a
   narrator could say over the frame fails, whoever speaks it.

---

## §3 — THE EIGHT PAIR PATTERNS

The mechanics are sourced (CA, Johnstone, UCB, soap practice — see
Sources); the taxonomy and names are **house invention**, assembled for
this pipeline. Every pattern ends in a ledger-mappable state change
(§7) — a pattern that cannot name its delta may not be used.

**P1 — CLAIM → CHALLENGE → CONCESSION-WITH-A-PRICE.**
Turn 1 asserts a fact or a right. Turn 2 attacks the assertion's weak
joint (not the speaker — the joint). The concession lands as the next
unit's turn 1 or the same unit's fragment: the conceder gives the
thing *and names a price*. (Soap status negotiation + Johnstone's
see-saw: the price is what keeps the concession from being a status
collapse.) *Delta: a fact changes hands; an OWES entry is born.*

**P2 — THE MISDIRECTED ANSWER.**
Turn 2 answers a different question than the one asked — the more
dangerous one underneath it (the house SOAP move, formalized: the real
thing is never named directly; doctrine S3). The audience hears both
questions; the asker hears the dodge. *Delta: knowledge asymmetry
grows — the answerer is now recorded as KNOWING the unasked thing.*

**P3 — THE CALLBACK THAT RE-PRICES.**
A word, phrase, or number from an earlier unit/episode returns in
turn 2 with its value changed: the same words, a new price. (Doctrine
S6 callback budget: one per unit, and the unit must land without it.)
Re-pricing is not repetition — it is the anti-recursion move in its
purest form, because the audience watches the *same* material mean
something different. *Delta: a spent fact's status changes
(spent → re-priced); a relationship delta is recorded.*

**P4 — THE INTERRUPTED TURN.**
Turn 2 begins before turn 1 finishes — an entrance, a counter-command,
or the cull itself cutting a word. In this pipeline the interruption
is written into the vehicle (line A ends mid-phrase; line B starts on
the cut), and PILOT-4 U6's mid-word cliff proves the generator honors
a cut onset. *Delta: status see-saw flip — the interrupter takes the
floor and keeps it; the interrupted character's want is marked
CONTESTED.*

**P5 — THE COUNTER-QUESTION THAT CONCEDES.**
Turn 2 is a question that accepts turn 1's premise while attacking
its conclusion ("Then who kept me? I left."). CA: a counter-question
is a marked second part — it honors conditional relevance while
refusing the answer, and the refusal itself concedes the premise.
*Delta: the premise enters both characters' KNOWS lists as shared
ground; the fight moves to new ground.*

**P6 — THE DISPREFERRED SECOND, PLAYED.**
Refusals and disagreements in real talk arrive delayed, softened, and
accounted for (preference organization, Pomerantz 1984). Script the
delay: turn 2's speaker gets a visible beat of action (0.5–1.0s —
the stopped hand, the look at the wall) *before* the line, and the
line carries its account with it ("I can't. The ninth number isn't
mine anymore."). PILOT-2 U5's accidental split delivery is the
accidental proof. *Delta: a WANT is refused and marked CONTESTED;
the account plants a fact.*

**P7 — THE STATUS SEE-SAW.**
Every turn must move Johnstone's see-saw: raise-self, lower-other,
lower-self, or raise-other — named in the draft per turn. A turn that
moves nothing is texture, and texture lines are already banned
(doctrine §5.6). The gap should be minimal (Johnstone: status play
works at a *small* gap — colleagues, not hero/villain). *Delta: the
pair's STATUS field in both character cards.*

**P8 — REPAIR.**
A character mishears, misnames, or miscounts, and is corrected — or
corrects themselves. CA's repair machinery is native to this network:
THE MACHINE mishears its own song; THE COUNT miscounts; THE ROSTER
misreads names. Repair is the pattern where the world's wrongness
enters the conversation itself. *Delta: a fact is corrected in one
character's KNOWS (wrong → right, or right → doubted).*

---

## §4 — DRAFTING PROCEDURE AND TESTS

**The pair draft.** Every unit is drafted as five lines before any
vehicle is written:

```
TURN 1:  <speaker> → <addressee> | act: <speech act> | want: <named want>
         "<line, ≤7 words>"
PRESSURE: <what turn 1 makes conditionally relevant — the second part it demands>
TURN 2:  <speaker> → <addressee> | pattern: <P1–P8> | status move: <see-saw>
         "<line, ≤7 words>"
DELTA:   <the state change this pair banks — §7 classes>
```

**The episode conversation map.** Before units are drafted, the
episode's pairs are listed as one arc: pair 1 opens a pressure, each
subsequent pair inherits the previous pair's delta (a concession's
price is paid or refused; a contested want is pressed again or
abandoned *on record*), and the final pair ends with the conversation
in a different relation than it began — the cliff then spends the
device, not the relationship. If the pairs can be reordered without
loss, they are not one conversation. Rewrite.

**Four tests, applied to every pair:**

1. **Swap test.** Transplant turn 2 into another unit. If it still
   works, it was never a second pair part — it was a monologue that
   happened to be second. Rewrite until it breaks in transit: a true
   second part quotes, answers, or breaks turn 1 specifically.
2. **Cost test.** At least one speaker per pair pays: concedes a fact,
   loses status, takes on a debt, or is caught knowing something. A
   pair nobody pays for is filler.
3. **See-saw test.** Name each turn's status move (P7). If either
   turn's move cannot be named, the turn is texture.
4. **Silence test.** If turn 2 is a dispreferred second (refusal,
   disagreement, bad news), its delay must be written as a visible
   beat in the unit's STATE/TURN description — never left to the
   generator to find.

---

## §5 — THE CONTINUITY LEDGER (SPEC)

One file per show: `~/workspace/wubutv-network/new-era/shows/
SHOW-N_<slug>_CONTINUITY.md`. It is a **record, not a plan** (the
working-bible principle: a mismatch between draft and ledger means the
draft contradicts something the audience already knows). It is updated
**the same day an episode ships** — canon is what shipped, so the
ledger is written from shipped episodes, never from drafts. If the
ledger's last delta row is not the last shipped episode, the ledger is
STALE and no new episode may be drafted from it (pre-flight item 0).

### Sections

**0. Header.** Show, ledger version (v1, v2, … incremented per shipped
episode), last episode shipped, next episode's required reads
(auto: this whole file).

**1. Canon facts (append-only).** Numbered `F-###`, never renumbered,
never deleted. Each row:

| Field | Content |
|---|---|
| ID | F-001… |
| Fact | one clause, concrete |
| Established | episode + unit |
| How | SPOKEN / SHOWN / IMPLIED (a fact only implied is weaker canon — mark it) |
| Status | ACTIVE / SPENT / RE-PRICED / REPAIRED |

**2. Fact bank.** Two lists drawn from §1: **SPENT** (already used as
new information; may be called back per doctrine S6 but never
re-presented as new — R4) and **PLANTED** (seeded, unspent, each with
the episode that planted it and the thread it belongs to). The
doctrine's "one unspent fact per unit" stops being a vibe and becomes
an inventory.

**3. Character state cards.** One per character:

```
### <CHARACTER>
KNOWS:      F-###, F-### (fact IDs only — knowledge is per-character)
WANTS:      <current want, one clause> [since <episode>] [CONTESTED by <name>, <episode>]
OWES:       <character>: <what> (from <episode>)
IS OWED:    <character>: <what> (from <episode>)
STATUS:     vs <character>: UP / DOWN / LEVEL (as of <episode>)
LAST CHANGE: <episode> — <what moved>
HOME:       <this ledger> OR pointer → SHOW-N ledger (see shared-cast rule)
```

Shared-cast rule: UNC, LAURA, COLONEL, PETER, DISPATCHER and SUPER
NUMBER HEAD appear across shows. A shared character's card has ONE
canonical home (UNC, LAURA, COLONEL → SHOW-1; PETER → SHOW-3;
DISPATCHER → SHOW-2; SUPER NUMBER HEAD → SHOW-4); other ledgers carry
a one-line pointer, never a copy. Copies diverge; pointers don't.

**4. Relationship deltas.** Pair-wise rows: `A ↔ B | <episode> |
<what changed> | direction (A↑B↓ / B↑A↓ / both→debt / both→alliance)`.
This table is the anti-recursion instrument at the relationship
level: an episode whose central pair shows no new row has repeated
the relationship, whatever its plot did.

**5. World state (show-specific counters).** The fields the show's
premise makes countable:

- **THE MACHINE:** dropped/misheard words so far (list); fixes that
  did not hold (list); who sang last (cat / girl / voice); whether the
  machine has used a crew member's name yet, and whose.
- **THE TENTH SECOND:** current cull number; the chalk wall's current
  contents (verbatim — the wall is the show's memory); parcels
  outstanding (addressee, current carrier, signed? Y/N); doors that
  opened onto streets (count).
- **THE ROSTER:** names on the roster (in read order); names circled;
  names read aloud so far; the current reading position; who has been
  asked to erase, and the refusal state.
- **THE COUNT:** the current count value (canonical); the gap between
  the Counter's count and the Clerk's ledger (currently: her +1, and
  the one time they agreed); skipped numbers (known list — the count's
  central mystery is ledger data); who holds the count now.
- **THE LAST SEAT:** acts the seat KEPT (survived) vs acts CULLED;
  seat-signs log (warmth, light, sound — dated by episode); the
  Usher's knowledge of who sat last (what the Usher claims vs what is
  established — two fields, they may differ).

**6. Open threads.** `T-<ARC>-<n>` IDs, network-global (ARC-1/2/3 per
the lore bible): thread, arc tag, state (OPEN / DEVELOP /
PAYOFF-DUE), last moved (episode), the next question (copied from
the last cliff that touched it), passes used (see R5).

**7. Beat registry (anti-recursion).** Per shipped episode, one row:
opening-beat type · pair patterns used (P1–P8) · delta classes banked
(§7) · handoff-device variant · cliff type · motion motif. Windows
enforced at pre-flight (§6): no opening-beat type or pair pattern may
repeat in **consecutive** episodes; no pair pattern or delta class
may appear **3 times in any 5-episode window**. Shape alone is not
enough — the same *delta class* wearing new shapes is still recursion,
so deltas are registered too.

**8. Episode delta log.** One row per shipped episode, written at
ship time:

| Episode | Facts spent | Facts planted | State changes (field: before → after) | Beats used | Cliff question (→ thread ID) |
|---|---|---|---|---|---|

This log is the ledger's proof of work: R2 is verified here, not
asserted.

---

## §6 — GENERATION RULES AND PRE-FLIGHT

**The rules the ledger imposes on every new episode:**

- **R1 — READ FIRST.** No outline begins until the writer has read
  the show's ledger (and the home ledgers of any shared-cast
  characters appearing). The episode plan's header must cite what it
  consumes: fact IDs spent, fact IDs planted (new), thread ID moved,
  state changes promised. An uncited plan is an unledgered plan.
- **R2 — STATE CHANGE.** Every episode must change at least one field
  in EACH of two classes: (a) a character-state field (KNOWS / WANTS /
  OWES / STATUS) and (b) a world-state or thread field. "Change" means
  the delta log records before ≠ after. An episode whose forecast
  delta log is empty is not written.
- **R3 — NEW-FACT RETURN.** A returning subject — character, object,
  name, number, room — must return carrying at least one of: a new
  planted fact, a new want, or a changed relation to another subject.
  Same subject + same want + same relation = recursion, rejected at
  pre-flight however good the lines are.
- **R4 — NO RE-SPENT FACTS.** A SPENT fact may be called back (one
  callback per unit, doctrine S6) but may not be presented as new
  information to any character whose KNOWS list already holds it. If
  the scene is the one where a character *learns* a fact, the learning
  IS the state change and is logged as such.
- **R5 — THE CLIFF IS A LEDGER DEBT.** Every episode's final cliff
  question is written into Open Threads with an ID before the episode
  ships. The show's next episode must move that thread or record an
  explicit PASS (max 2 consecutive passes; a third means the thread
  must be moved or formally retired in the open, per canon discipline).

**Pre-flight check** (run by the episode's coordinator as a gate,
logged in the episode plan as LEDGER_CHECK, pass/fail per item —
failure rewrites the *plan*, never the ledger; a deliberate canon
change is made openly as a ledger revision, not smuggled):

0. **Freshness:** ledger's last delta row == last shipped episode.
1. **Citations:** plan header cites fact IDs spent/planted, thread ID
   moved, ≥2 promised state changes across the two R2 classes.
2. **Beat window:** opening-beat type and pair patterns differ from
   the previous episode's registry row; no pattern/delta class at
   3-in-5.
3. **Knowledge audit:** no line gives a character knowledge their
   KNOWS list lacks (unless this scene is the logged learning).
4. **Arithmetic audit:** show counters reconcile — THE COUNT's next
   number follows the ledger's canonical value; THE ROSTER's reading
   position and names match; THE TENTH SECOND's cull number and wall
   contents match.
5. **Delta forecast:** the promised deltas are written BEFORE lines
   are drafted; after ship, actual deltas are reconciled into the
   ledger the same day, and any forecast delta that didn't land is
   recorded as missed (a missed delta twice running on the same field
   is a method problem, surfaced — not quietly dropped).

---

## §7 — ONE SYSTEM: PAIR → DELTA → LEDGER

The dialogue method and the ledger are not two documents. **A pair is
a transaction; the ledger is its bookkeeping.** Each pattern banks a
recognizable delta class:

| Pattern | Delta class banked |
|---|---|
| P1 Concession-with-a-price | OWES entry created; fact changes hands (KNOWS ±) |
| P2 Misdirected answer | Knowledge asymmetry: answerer's KNOWS grows (marked: knows the unasked thing) |
| P3 Callback re-price | Fact status SPENT → RE-PRICED; relationship delta row |
| P4 Interrupted turn | STATUS flip; interrupted want marked CONTESTED |
| P5 Counter-question that concedes | Premise enters shared KNOWS for both; fight relocates (thread moves) |
| P6 Dispreferred second | WANT refused → CONTESTED; the account plants a fact |
| P7 Status see-saw | STATUS fields updated for the pair |
| P8 Repair | KNOWS corrected (wrong → right, or right → doubted) |

Drafting consequence: the pair draft's DELTA line (§4) is filled from
this table at draft time, and the episode's delta forecast (§6 item 5)
is just its pairs' DELTA lines collected. **A pair with no mappable
delta is texture — banned by the same law that already bans texture
lines.** The writer never faces a blank ledger at ship time, because
the ledger was being written, one delta at a time, since the first
draft.

---

## §8 — ILLUSTRATIVE FRAGMENTS

*The following fragments are ILLUSTRATIVE — method demonstrations
rewriting pilot material, not episode scripts and not canon.*

### ILLUSTRATIVE FRAGMENT 1 — THE COUNT, PILOT-4 U1 rewritten as a pair (P1 + P3)

*Shipped version: the Clerk's single line "Say the number between
ours, Counter." at 7–9s, then the cliff "One thousand one." Under the
pair law the same unit becomes:*

> **CLERK:** "Say the number between ours, Counter." *(turn 1 — dare;
> the doctrine line, moved up to ride the turn)*
> **COUNTER:** "There is no number between ours." *(turn 2 — refusal;
> dispreferred, flat: boards don't lie)*
> **CLERK:** "Then one of us invented one." *(fragment — the
> re-price: now somebody is a liar, and he must choose who)*
> **CLIFF (device):** **COUNTER:** "One thousand one." *(he speaks
> HER number — the concession. His board was wrong.)*

*Delta banked: STATUS flips (Clerk ↑); world state — the spoken count
follows the Clerk's ledger for the first time (gap field annotated);
OWES: the Counter owes the board an explanation he will not give.
Four spoken turns, ~13 words + the device fragment — inside the
measured budget.*

### ILLUSTRATIVE FRAGMENT 2 — THE TENTH SECOND, PILOT-2 U5 rewritten with interruption (P4 + P6)

*Shipped version: the Watcher's line arrived split across the unit —
"You carried it to yourself." … "Sign for it." — with the Courier
silent. Under the pair law the silence becomes her turn:*

> **WATCHER:** "You carried it to yourself." *(turn 1 — verdict)*
> **COURIER:** "Then I refuse delivery—" *(turn 2 begins — refusal,
> cut off mid-phrase)*
> **WATCHER:** "Sign for it, Courier." *(the interruption — he takes
> the floor back inside her turn; the command is now a second part,
> not a new speech)*
> *(beat: she takes the chalk from the parcel — her dispreferred
> second is an ACTION, delayed, per P6)*
> **CLIFF (device):** *the chalk hovers an inch above the paper,
> unsigned — as shipped.*

*Delta banked: OWES — the Courier owes a signature (to herself, which
is the show's whole wound, now ledgered); STATUS — the Watcher's
interruption held (Watcher ↑); her want (refuse) marked CONTESTED,
which is what U6's "Then the next me signs it" then answers — as a
true second part, one unit later, because the pressure was real.*

### ILLUSTRATIVE FRAGMENT 3 — THE ROSTER, SHOW-3 Chain R1-1 compressed into one unit (P2 + P8)

*Treatment version: four lines across four units. Under the pair law
the exchange lives inside one unit and the name handoff still closes
it:*

> **KEEPER:** "Who circled my name, UNC?" *(turn 1 — question)*
> **UNC:** "Read the next name, Keeper." *(turn 2 — the misdirected
> answer: a command instead of a name; it concedes the roster has an
> order while refusing the question)*
> **KEEPER:** "I asked who held the pen." *(repair — he names the
> dodge; the dodge is now on record, and it costs UNC: it can be
> quoted back)*
> **UNC:** "And the roster answered in order." *(he repeats the dodge
> as a claim — and accidentally plants a fact: the roster ANSWERS)*
> **CLIFF (device):** **KEEPER** *(reading)*: "Peter." *(the next
> name — spoken → next unit opens on it written)*

*Delta banked: PLANTED fact — "the roster answers in order" (F-new,
SHOWN/SPOKEN); Keeper's KNOWS gains "UNC's dodge is policy, not
ignorance"; thread ARC-2 moves OPEN → DEVELOP inside a single unit
instead of a whole chain.*

---

## §9 — CONFLICTS WITH THE DOCTRINE AND THE ATOM (NAMED, WITH RESOLUTIONS)

**Conflict 1 — One line per unit vs one exchange per unit.**
The show documents and standing grammar specify *exactly one spoken
line per unit at 7–9s, ≤9 words*; the FIRST_SECOND_DOCTRINE's L-rules
are written for that single line. The pair law cannot be satisfied
inside that grammar. **Resolution proposed:** amend the grammar to
"one exchange per unit" (§2), and read the doctrine's L-rules as
binding the *pair*: L2's "one act per line" becomes one act per turn;
L4's "the line reframes the turn" becomes turn 2's specific job. The
doctrine's intent (every word is a speech act; the late line reframes)
is preserved and strengthened; its letter (one line) is not. **This
amendment needs adoption by the parent/user — this report proposes,
it does not enact.**

**Conflict 2 — Cold arrivals vs an episode that opens mid-conversation.**
Doctrine S6/§5.9: every unit stands alone; the feed sends strangers.
A pair presumes a conflict already running (doctrine L3 wants exactly
that), but an episode's FIRST pair must not presume *knowledge* — a
cold viewer has none of the ledger. **Resolution:** episode-opening
pairs are restricted to self-evident pressures — demand/refusal,
dare/concession, question/misdirection — whose stakes read cold.
Callbacks (P3) and repairs of old facts (P8 on a ledger fact) are
banned from episode-opening pairs. The ledger governs what characters
may know and what may change; it never governs what a unit must
explain. Serial depth is a bonus for returners, never a tax on
strangers.

**Conflict 3 — The 10s atom vs natural pace (the tight one).**
Measured: a pair at cap (7+7 words, gap, reaction) consumes the whole
4.0–9.0s window, which means the picture TURN and turn 1 now share
the 4–7s band — the generator must act and speak simultaneously, and
PILOT-2's ASR already shows loose placement (lines landing at 5.6s,
spanning 4.1–8.4s, splitting unbidden). Two turns double the surface
for mush, overlap, and drift. **Resolution:** fragment chains for
dense units; per-turn ASR gate (BOTH turns must transcribe exact, not
just "the line"); roll the pair law out on the dialogue-forward shows
(THE ROSTER, THE COUNT) before THE MACHINE (Conflict 4). If two-turn
ASR fails repeatedly in production, fall back to pair-across-the-joint
(turn 2 as the next unit's first beat, pre-cliff) — named here as the
retreat position, not the plan.

**Conflict 4 — THE MACHINE's mouth handoff and song word-sync.**
SHOW-1 is cut like an MV: units end on a sung word's onset and the
next unit opens mid-word. A spoken pair that runs long eats the
handoff. **Resolution:** in THE MACHINE, pairs close by 8.5s (hard),
the cliff word is always SUNG, never dialogue, and pair turns are
written against the beat grid like everything else in that show —
the song remains the tempo gospel; conversation rides it or doesn't
ride at all.

**Conflict 5 — THE LAST SEAT's wordless units.**
SHOW-5 explicitly allows units carried by song or dance with no
spoken line. A spoken-pair law cannot bind them. **Resolution:** in
THE LAST SEAT a pair may be danced: the performer's phrase is turn 1;
the seat's answer — a light, a sound, a warmth, an act surviving — is
turn 2, and it must still bank a delta (act KEPT/CULLED is world
state). This is the loosest joint in the method and is flagged as
such: if danced pairs prove unreadable, THE LAST SEAT keeps spoken
pairs in its dialogue units and banks deltas only there.

**Conflict 6 — Serial state vs the "nothing resolves" pilot law.**
The pilot law held one unspent fact per unit and resolved nothing —
correct for 60s proofs, fatal as a series law (it is the recursion
engine wearing a doctrine's clothes: unspent forever = unchanged
forever). **Resolution:** the series law replaces it — every episode
SPENDS at least one planted fact and PLANTS at least one new one
(R2/R5 make this auditable). "Nothing resolves" survives only inside
the unit: a unit's pair may end contested; an episode's conversation
may not end unchanged.

---

## §10 — OPEN RISKS

1. **Two speakers per unit doubles the identity-anchor load.**
   PILOT-4's gate log shows the Clerk re-invented in every call that
   didn't carry her CHAR sheet — and pairs put both faces in speaking
   roles in *every* unit. The kit fix already recorded there (a
   combined two-character anchor per unit, or alternate which face is
   large) stops being optional under this method; it is a production
   prerequisite, and it belongs to the panel workflow, not this
   document — flagged for the parent.
2. **Ledger upkeep is a chore with a failure mode.** If the same-day
   update lapses, R1's read-first reads a stale record and pre-flight
   item 0 blocks drafting — by design, but it means a lapsed ledger
   halts the show, not just its paperwork. The ledger must stay small
   enough to update in minutes: facts are one clause, deltas one row.
   If a ledger grows past ~150 canon facts it needs a "cold storage"
   split (active facts vs archived), or upkeep will quietly stop.
3. **Recursion can migrate from shape to delta.** The beat registry
   counts patterns and delta classes, but a writer can still bank
   "status flip" forever via different patterns. The 3-in-5 window on
   delta classes is the mitigation; whether it is tight enough is an
   empirical question the first season answers.
4. **Cross-show threads vs per-show ledgers.** ARC-1/2/3 threads live
   in several shows at once; thread state is recorded in each show's
   ledger and can diverge. Mitigation: a thread's state is canonical
   in the ledger of the show that last moved it; other ledgers cite
   that episode. Divergence found at pre-flight is repaired in the
   open (canon discipline), never averaged.
5. **The generator may not honor written pauses.** P6's scripted delay
   and P4's interruption are vehicle-level instructions; PILOT-2 U5's
   split delivery shows the behavior exists, not that it is
   steerable. The first pair-law episodes are, in part, a steerability
   test — their gate logs should record per-turn placement against
   the §1 budget so the method can be revised on measurements, not
   impressions.
6. **Conversation density vs the maximalist visual doctrine.**
   The station's standing order is density — more events, more layers.
   A 5-second dialogue window is 5 seconds not spent on visual events.
   The method's answer (turn 1 rides the picture turn; the reaction
   gap is a visible beat) is a claim, not a measurement. If pair-law
   episodes read as talkier *and* thinner, the fragment chain — not
   the full pair — becomes the default shape.

---

## SOURCES

**House (primary evidence):**
- Pilot gate logs and scripts — PILOT-2_the-tenth-second (SCRIPT.md,
  GATE_LOG.md: ASR spans measured in §1) and PILOT-4_the-count
  (EPISODE_PLAN.md, GATE_LOG.md) — `~/workspace/wubutv-network/new-era/pilots/`
- FIRST_SECOND_DOCTRINE_2026-11-15 (L-rules, S-rules, banned failure
  modes) — `research/FIRST_SECOND_DOCTRINE_2026-11-15.md`
- DIALOGUE_LINES_RESEARCH_2026-10-27 (narrator test; SOAP/FRUIT/MEGA
  moves) — `research/DIALOGUE_LINES_RESEARCH_2026-10-27.md`
- SOAP_OPERA_ERA_RESEARCH_2026-10-22 (A5 one turn per part, A6 one
  withheld fact, A8 weave, B5 callback budget) —
  `research/SOAP_OPERA_ERA_RESEARCH_2026-10-22.md`
- WUBU_LORE_AND_LONG_ARCS_2026-10-27 (ARC-1/2/3, thread states, canon
  discipline) — `research/WUBU_LORE_AND_LONG_ARCS_2026-10-27.md`
- SHOW-1..5 treatments (cast, devices, chains) — `new-era/shows/`

**Web (mechanics, cited in text):**
- Sacks, Schegloff & Jefferson (1974), turn-taking; Schegloff &
  Sacks (1973), adjacency pairs and conditional relevance; Pomerantz
  (1984), preference organization; Stivers et al. (2009), response
  timing — via conversation-analysis summaries:
  https://sltinfo.com/ca101-adjacency-pairs/ and
  https://www.taalhammer.com/conversation-analysis-in-language-learning/
- Besser, Roberts & Walsh, *The Upright Citizens Brigade Comedy
  Improvisation Manual* — game of the scene; "if this is true, what
  else is true" — via https://www.scribd.com/document/812928247/UCB-Manual
  and Will Hines, "How To Play Game: Micro or Macro?",
  https://willhines.substack.com/p/how-to-play-game-micro-or-macro
- Keith Johnstone, *Impro* (status transactions, the see-saw
  principle, minimal status gap) — via
  https://fluidself.org/books/art/impro and
  https://scottfenstermaker.com/the-status-transaction/
- Series/character bibles as living continuity records; character
  bibles maintained by production staff tracking per-episode facts —
  https://scriptation.com/blog/tv-show-bible-and-character-bibles-guide/
- Bible continuity-check routine (freeze the reference; read for
  facts; mark spoken/shown/implied; deliberate change = bible
  revision; update the same day) —
  https://www.contd.app/blog/bible-continuity-check-for-tv-drafts
- Living continuity database; delta log instead of rewriting —
  https://storyloft.app/how-to-write-a-series-bible/ and
  https://www.laterpress.com/craft-of-writing/series-bible/

**House invention (unsourced, marked as such):** the eight-pattern
taxonomy (§3), the pair budget numbers (derived from measured pilot
ASR, §1), the ledger schema and field lists (§5), rules R1–R5 and
the pre-flight checklist (§6), the delta-class table (§7).

---

## ADDENDUM — msg 445, 2026-11-15: FILL THE TEN SECONDS + THE STORY SLATE

*Commissioned by the user's follow-up verdict (Telegram msg 445,
2026-11-15): "make sure we make more stories, and write better
conversations to fill 10 seconds if needed." What the main report
already covers, so this addendum does not repeat it: §1 measures the
delivery rate (~2.1–2.8 w/s) and draws the honest window (dialogue
4.0–9.0s, cliff 9.0–10.0s uncharged); §2 caps turns (≤7 words
standard, total spoken ≤16/unit) and already parks turn 2 late
(6.5–8.7s). What was missing, and is added here: a fill FLOOR to go
with the caps (the report said what may not be exceeded, not what
must be reached), an accounting of what counts as filled time, an
explicit rule against the generator's measured front-loading, and a
procedure that turns the ledger into the next stories.*

### A1 — FILL RANGES (the floor under §2's caps)

The caps keep a unit from overrunning; the ranges below keep it from
starving. Spoken-word targets per unit, at the measured 2.1–2.8 w/s
(so ~4–6s of the 5.0s window is voice when full):

| Fill class | Spoken words | When |
|---|---|---|
| **FULL** | 12–16 | The unit's pair is the beat — a concession, a verdict, a fight. The default for dialogue-forward shows (THE ROSTER, THE COUNT). |
| **STANDARD** | 9–12 | A pair plus picture: turn 1 rides the picture turn, turn 2 lands the reframe, and one filled beat (A2) covers the rest. The default everywhere else. |
| **SPARSE** | 5–8 | Deliberate only: a fragment chain, a held look, a world that is itself the event. A sparse unit must name its non-speech fill in the pair draft (A2) — sparse by accident is under-filled. |
| **UNDER-FILLED** | <5, or any class with >1.0s of unscripted dead air in the window | Fails drafting. Rewrite, or reclassify the unit as a declared wordless unit (THE LAST SEAT rule, §9 Conflict 5) with its fill carried by action/device. |

Coverage rule: **spoken words + filled beats (A2) must account for
≥4.0s of the 5.0s dialogue window.** The remaining ~1s is the
picture breathing — STATE spilling into the window's edges is
normal; a silent hole in the middle is not.

### A2 — WHAT COUNTS AS FILLED TIME

Not all silence is empty. These count toward the ≥4.0s coverage,
because each is a *second part the audience can read*:

- **Reaction gap, 0.2–0.5s** (§1) — the visible uptake before turn 2.
  Always present, always counted, never more than this unless P6.
- **The dispreferred delay, 0.5–1.0s** (P6) — a scripted visible beat
  (stopped hand, look at the wall) before a refusal or bad news. It
  is turn 2's first half, played in action.
- **Interruption overlap** (P4) — turn 2's onset lands inside turn
  1's final word or breath. Two voices, zero dead air: the overlap
  itself is filled time, and it is why a FULL unit can hold 16 words
  without rushing.
- **The reaction beat, 0.5–1.5s** — a visible response with story
  content after a turn lands: the chalk taken up, the number
  re-written, a hand withdrawn from the parcel. It must *do*
  something (change a prop's state, a position, a relation) — a
  character merely standing in frame while nothing changes is not a
  beat, it is the halted-photo failure wearing a dialogue costume.
- **The cliff fragment at 9.0–10.0s** stays device, not dialogue
  (§1) — it does not count toward coverage; the window must be full
  before the cliff arrives.

What does NOT count: unscripted pauses the generator invents,
settled tails (the deceleration zone belongs to the joint method,
not the dialogue window), and any silence the pair draft did not
assign to one of the beats above.

### A3 — THE ANTI-FRONT-LOAD RULE (front-load insurance)

**Measured problem (PILOT-5, delivered 2026-11-15):** the generator
front-loads quoted speech — PILOT-5's scripted lines landed inside
0–5.6s of their units regardless of where the script parked them.
A pair written to bloom at 6.5–8.7s may in fact be spent by 5.6s,
leaving the window's back half empty and the cliff standing in a
hole. PILOT-2's U5 split delivery ("You carried it to yourself." …
long pause … "Sign for it.") is the same behaviour read kindly.

**The rule: every unit is written to still play if all its speech
lands early.** Concretely, at pair-draft time:

1. **Two quoted blocks, never one.** Turn 1 and turn 2 are separate
   quoted blocks in the vehicle text, with the picture turn written
   between them — one merged paragraph of dialogue invites one
   merged early burst.
2. **A late beat is parked, on paper, at ≥6.5s.** Turn 2 (per §2.3),
   or — where turn 2 must land early for the pattern (P4) — a
   fragment or a scripted reaction beat (A2) is assigned to the
   6.5–8.7s band in the draft. The draft names it; "something will
   happen later in the unit" is not a late beat.
3. **The tail carries a speech-independent event.** The handoff
   completing, the device firing, a door state changing — something
   that reads with the sound off and survives total speech
   displacement. If the unit is unintelligible-but-pretty with its
   dialogue removed *and* front-loaded, it fails drafting.
4. **Turn 1 is written about what the picture shows late.** A first
   turn that references the unit's late visual state stays true
   whenever it lands; a first turn about the opening frame expires
   if displaced. (This is §2.5's "turn 1 does something ABOUT the
   fact" with a timing edge.)

If production ASR shows a show's lines consistently landing in the
0–5.6s band anyway, the drafting response is to move the *pair*
earlier on paper (turn 1 at the picture turn, turn 2 written as the
late fragment) — insurance first, surrender of the 6.5–8.7s slot
only on measurement, and logged when surrendered.

### A4 — THE STORY SLATE PROCEDURE ("make more stories" as procedure)

The ledger (§5) makes recursion visible; it does not by itself
produce the next story. This procedure does. It is a named
pre-flight step — **SLATE** — run once per show after each shipped
episode's ledger update (ship-day routine: reconcile ledger → run
SLATE → the chosen candidate becomes the next episode's R1 citation
base), and once at season planning.

**Inputs (all from the ledger, nothing from vibes):**

- §2 **PLANTED** facts — unspent, with their threads.
- §3 **WANTS** — especially CONTESTED wants and wants unchanged for
  2+ episodes (a want nobody has pressed is pressure stored).
- §6 **Open threads** — state PAYOFF-DUE or DEVELOP first; plus
  **arc pressure**: which of ARC-1/2/3 has moved least recently
  across the network (the starved arc gets weight — read across
  ledgers per §10 risk 4's canonical-home rule).

**Generation:** cross one planted fact × one pressed want × one
thread under pressure. That triple is a premise: the fact is what
the episode can spend, the want is who pays, the thread is what the
cliff will owe. Produce **exactly 3 candidates per show, one line
each**, each annotated in the slate with the fact ID, the want, and
the thread ID it would consume — R1's citations drafted at slate
stage, not reconstructed at outline stage.

**Screen (a candidate that fails any line is not a candidate):**

- Forecasts ≥2 state changes across the R2 classes.
- Obeys the §5.7 beat window (opening type, patterns, delta classes).
- Spends no SPENT fact as new (R4); a callback is marked as one.
- Names its pair patterns provisionally — a premise that cannot
  imagine its conversation is a plot, not an episode.

**Disposition:** the chosen candidate is marked on the slate and
carried into the episode plan. Unchosen candidates **stay on the
slate** — they are planted pressure, not waste — but they decay: a
candidate passed over at 3 consecutive slates is retired or
re-priced (its fact re-planted under a new want) and the retirement
is logged. The slate itself lives at the end of the show's ledger
file, under the delta log, so "what stories do we have?" is always
answerable from the same document that answers "what is true?"
