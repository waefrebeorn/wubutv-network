# THE WRITERS ROOM — standing method for the WuBuTV new-era shows

**Status:** standing operating spec, adopted 2026-11-15. This is the ORG
document: who writes, in what order, through which gates, and who owns
what. It synthesizes two research reports — real TV room process
(`research_notes/writers-room-craft-20261115/`) and dialogue craft +
serial continuity + AI rooms (`research_notes/writers-room-dialogue-
20261115/`) — and integrates with **Method B** (`research_notes/
conversation-continuity-method-20261115/`), which remains the authority
on dialogue grammar (the Pair Law, §2; the eight pair patterns, §3) and
on the continuity ledger's format (§5) and rules R1–R5 (§6).

**Division of authority, stated once:**

- **Method B** says what a conversation *is* (pairs, patterns, deltas)
  and what the ledger *contains*.
- **This document** says how a room full of agents *produces* one:
  roles, session flow, the canonical pass order, the gates between
  passes, and the failure-mode guards.
- Where the two research reports and Method B disagree, §7 of this
  document names the conflict and the resolution. The resolutions here
  are the standing ones until the parent revises them.

**Format reminder:** five shows, 60-second episodes, 6 units × 10s.
One episode = ONE conversation (Method B §1). The room exists because
the pilot law produced correspondence, not conversation (Method B §0),
and because subjects reused without state change repeat recursively —
the two failures the user named on 2026-11-15.

---

## §0 — THE ROOM IN ONE PAGE

Seven roles. **One agent-instance per role per episode** — a role is
never split across two instances mid-episode, and the separations
marked ✕ below are hard: they exist because the research shows merged
roles are where the failure modes live.

| Role | Who | Owns | May never |
|---|---|---|---|
| **Showrunner** | The parent agent, always | Premise, tone, final approval of every beat and line; the LOCK | Delegate the lock |
| **Room-runner** | A coordinator agent, instantiated per episode | Running the session: spawn order, gate enforcement, the episode scratchpad; declares an episode *pipeline-complete* | Approve a board; declare a lock (✕ showrunner's alone) |
| **Storyliner** | One agent per show per episode | Plot: premise choice, board, beat sheets, plants/payoffs. The soap head-writer/breakdown tier | Write dialogue (✕ ≠ Dialogue Writer) |
| **Dialogue Writer** | One agent per show per episode, fresh instance | Words: the pair drafts, tactics, timing budget. Writes units **serially, in order** | Touch the board or the ledger; draft units in parallel (✕ documented Dramatron failure) |
| **Continuity Editor** | One agent per show (standing across its episodes) | The production bible / continuity ledger; the continuity edit pass | Rewrite dialogue (✕ — returns the unit with the ledger line quoted; the Dialogue Writer rewrites) |
| **Critic** | Fresh-context agent, shared pool across shows | The cold read + located, gate-cited objections | Rewrite anything; file generic feedback ("tighten this" is rejected unread); exceed **2 rounds** |
| **Script Coordinator** | Shared function across shows | The decision log, version sequence, board archive, episode scratchpad hygiene | Be the episode's writer; pitch |

**Why the separations are load-bearing (research, in one line each):**

- Storyliner ≠ Dialogue Writer is the soap machine's core split —
  different crafts, different hires (craft report §4.4).
- A critic anchored to checklists and located objections measurably
  helps; a critic asked "is this good?" about fresh output measurably
  does not — generic feedback collapses the gain to ~zero (dialogue
  report §4.5, Self-Refine ablation; Huang et al.). Hence: located
  objections only, max two rounds, no rewrites.
- The Continuity Editor checks against *artifacts*, never taste
  (dialogue report §5, Pass 5) — and a named single owner is what
  keeps a continuity record from decaying (craft report §4.3).
- The decision log is written by an agent that did not pitch — the
  writers'-assistant principle: the room's memory of *what was chosen
  and why* is never the pitcher's own account (craft report §6-A4).

**The episode scratchpad.** One shared document per episode carries
every intermediate artifact — board, beat sheets, pair drafts, unsaid
sentences, tactic maps, timing counts, continuity checklist, critic
objections, decision log — in pass order. (The Agents' Room pattern:
planning agents write to a scratchpad, writing agents read it;
dialogue report §4.1.) Nothing about an episode lives only in an
agent's context. If it isn't in the scratchpad, it didn't happen.

---

## §1 — STANDING DOCUMENTS PER SHOW

Five documents per show, plus two room-level archives. Each has ONE
owner. A document with no owner decays; that is a finding of the
research, not a preference (craft report §4.3).

**1. The pitch bible (static).** Written once per show, revised
rarely and only by the Showrunner. Contents: premise; the story
engine (the mechanism that generates problems without manufactured
coincidence); tone; world rules; and per principal character —
**Want / Flaw / Relationships / Arc** (beginning → end), plus voice
notes (vocabulary, sentence-length habits, dominant emotion) and the
character's **full trait set** (the anti-Flanderization reference,
§4). The founding treatments (`new-era/shows/SHOW-N_*.md`) are the
seed of each pitch bible.

**2. The production bible = the continuity ledger (living).** Format
is Method B §5, unchanged: canon facts (append-only, F-###), fact
bank (SPENT / PLANTED), character state cards (KNOWS / WANTS / OWES /
IS OWED / STATUS / LAST CHANGE), relationship deltas, world-state
counters, open threads, beat registry, episode delta log — plus the
story slate at the end of the file (Method B Addendum A4). One file
per show: `new-era/shows/SHOW-N_<slug>_CONTINUITY.md`. **Owner: the
show's Continuity Editor.** Updated from the *locked script* the same
day the episode ships — never from drafts or plans, because a bible
updated from plans becomes fiction about the show (dialogue report
§3.1). Shared-cast characters keep ONE canonical home ledger per
Method B's shared-cast rule; other ledgers carry pointers, never
copies.

**3. The season projection + episode grid.** Written before episode
breaking begins, owned by the Showrunner, updated at every lock.
Contents: where each character starts and ends the season; the
season's final image; the midseason turn; and the grid — one row per
episode: logline + one line "how the arc moves here" + end-hook.
Deliberately firm for the next 2–3 episodes and loose beyond (the
soap "good bail-out position," craft report §4.4): the destination
disciplines choices; the looseness keeps a working story extendable
and a failing one escapable.

**4. The open-seeds table (plant & payoff).** Lives inside the ledger
(Method B §5.2 PLANTED list, §5.8 delta log) and obeys one hard rule
imported from the dialogue research: **no empty payoff cells.** Every
plant carries — at the moment it is planted — a planted-in episode, a
remind-in episode, and an assigned payoff episode. A detail with no
assigned payoff is not planted; at the storyline pass it is either
assigned or cut. Payoffs are chosen before plants (write the payoff
first, plant backward — dialogue report §3.3).

**5. Next-episode anchors.** Written at LOCK time, stored at the head
of the ledger's delta log: the 1–2 facts/lines the *next* episode
needs in the viewer's working memory. The next episode's first unit
spends its opening line(s) on them as in-character re-anchoring —
soap-style, inside the conversation, never as a recap card (dialogue
report §3.4: a 20s recap would eat a third of a 60s episode; soaps
re-anchor in dialogue, and so do we).

**Room-level archives (owner: Script Coordinator):**

**6. The decision log** — per episode, inside the scratchpad: what was
pitched, what was chosen, why, and what was killed. This is the room's
memory and the anti-repetition check's second source (§4).

**7. The board archive** — every episode's board file, kept after
production. The archive *is* the repetition detector: a new board is
checked against the shapes of the old ones, not against anyone's
recollection (craft report §6-E19).

---

## §2 — THE BREAKING SESSION

Story is broken on a board before anyone writes a word of dialogue.
No stage may be skipped, and **no unit may be generated from a card
alone** (craft report §6-B8).

**The board file.** One per episode, `BOARD.md` in the episode's
scratchpad, laid out as six columns (Unit 1 … Unit 6). Each column
holds one card per beat. Rules:

- **Card text ≤ 7 words.** The card states an *indispensable* beat:
  if removing the card changes nothing, delete the card (Gilligan
  room discipline, craft report §2.2).
- **The Gilligan line.** Under each card, one line answering: *"What
  is [character] thinking/feeling right now?"* A card that can't
  answer it is plot machinery, not story (craft report §2.3).
- **Lettered storylines.** Beats are tagged A/B/C by storyline and
  units are rationed across them (e.g., A gets 3 units, B gets 2, C
  gets 1) so no storyline loops in place and every episode advances
  more than one thread (soap structurer practice, craft report §4.4).
  In a 6-unit episode built on one conversation, the letters track
  which thread each pair is spending.
- **Anti-repetition pre-check.** Before the board goes to the
  Showrunner, the Script Coordinator searches the production bible,
  the used-events ledger, and the board archive for the board's
  beats/events (§4). A beat matching a prior episode's must be
  justified in the decision log or replaced — at board stage, where
  replacement is cheap.

**The pipeline of documents.** Board → **beat sheet** (one line per
beat, in order) → **outline** (scene-by-scene prose, scaled: ~1 short
paragraph per unit) → **script** (the pair drafts of §3). Each stage
is a separate artifact in the scratchpad; each is the next stage's
only input. The test of a finished break, from the room that codified
it: anyone who reads the board could go off and write that episode.

**Breaking is the expensive step — budget it that way.** In human
rooms, breaking costs more hours than drafting (craft report §2.3).
Room rule: **at least half of an episode's agent calls happen before
the dialogue draft exists** — board drafting, board review, the
anti-repetition search, the beat sheet, the outline. A room that
spends its calls on redrafting dialogue has inverted the economics
that make the pipeline work.

**Approval gate.** The Room-runner may fill the board; only the
Showrunner approves it. No beat sheet is written from an unapproved
board.

---

## §3 — THE PASS PIPELINE (CANONICAL ORDER)

One order, binding on every episode of every show:

> **Storyline → Breakdown → Dialogue → Timing Verification →
> Continuity Edit → Critic → Showrunner Lock** (+ ledger update and
> next-episode anchors, which are part of the lock, not an afterthought).

A pass may only fix its own layer. A dialogue problem noticed during
the storyline pass is logged in the decision log, not fixed there
(craft report §6-C10). The craft report's classic taxonomy maps onto
this pipeline without remainder: its *story pass* is Pass 1; its
*structure / character / scene passes* are executed inside Pass 2
(the board's columns are the structure check, the Gilligan line is
the character check, the beat sheet is the scene check); its
*dialogue pass* is Pass 3, kept separate and late; its *polish* is
absorbed into the Showrunner's lock pass. Passes 4–6 (timing,
continuity, critic) are the layers the classic taxonomy assigns to
roles rather than passes — the script coordinator's continuity duty,
the table read — and this room runs them as explicit passes because
an AI room has no hallway where such checking happens by itself
(see §7, Conflict 5).

### Pass 1 — STORYLINE (Storyliner)

Inputs: the ledger (R1 — read first; the plan header must cite what
it consumes: fact IDs spent, fact IDs planted, thread ID moved, state
changes promised), the season projection row, the story slate
(Method B A4), the next-episode anchors from the previous lock.

1. Run/refresh **SLATE** if the previous lock didn't: cross one
   PLANTED fact × one pressed want × one thread under pressure;
   exactly 3 candidates, screened per Method B A4.
2. If a payoff is due within 2 episodes, choose the episode's payoff
   *first* and plant backward from it.
3. Write the six unit summaries. **Gate A — the connector test:**
   the summaries must read as one sentence joined only by
   *but / therefore*. Any "and then" joint fails the pass
   (Parker & Stone rule, dialogue report §2.1).
4. Per unit, declare opening value → closing value and the turn.
   **Gate B:** if open = close for any unit, redesign that unit now,
   not in dialogue (McKee's turn law, dialogue report §1.4).
5. Forecast the episode delta log (Method B §6 item 5): ≥2 state
   changes across the two R2 classes, or the episode is not written.

Output: board file (§2) + unit summaries + delta forecast, into the
scratchpad. Showrunner approves the board before Pass 2.

### Pass 2 — BREAKDOWN (Storyliner)

Per unit, a beat sheet of **3–5 beats**. Each beat is one
action/reaction pair labeled with **(tactic verb, Δinfo or Δpower)**.
**Gate C:** a beat with no tactic verb or no Δ annotation is cut or
merged — it is a repeated beat wearing a costume (dialogue report
§§1.2, 2.2). The breakdown also marks, per unit:

- the **silence beat**, if any: at most one, 2–3s, placed
  *immediately before the turn line* (dialogue report §2.4);
- any **scripted interruption points** (essential spans marked;
  interruptions land only on sacrificial edge words — §3 Pass 3,
  and dialogue report §1.5);
- which **plant** is planted / reminded / fired here;
- the pair pattern (Method B P1–P8) the unit's exchange will run,
  checked against the beat-registry windows (Method B §5.7);
- the fill class (Method B A1: FULL / STANDARD / SPARSE) and, for a
  SPARSE unit, its named non-speech fill (A2).

### Pass 3 — DIALOGUE (Dialogue Writer, serially, unit 1 → 6)

The Dialogue Writer receives: the approved breakdown, the pitch
bible's voice notes, the previous episode's final unit, and the
next-episode anchors. Units are drafted **in order, never in
parallel**, under the **carry-forward rule**: unit *n*'s final line
and the state it leaves are pasted verbatim into unit *n+1*'s context
before drafting (soap adjacent-breakdown practice + Dramatron's
documented parallel-dialogue failure; dialogue report §§3.2, 4.2).

Per unit, the draft is Method B's five-line pair draft (§4 of Method
B: TURN 1 / PRESSURE / TURN 2 / DELTA), extended with the research
room's requirements:

1. **The unsaid sentence.** Before drafting, write for each speaker
   the sentence they will not say, and confirm each has a *cost of
   saying it plain*. If there is no cost, the unit plays it straight
   — directness becomes the tactic (dialogue report §1.3).
2. **Word budget.** Draft to the budget; counting is mechanical and
   is re-verified in Pass 4.
   - Full-talk unit: **22–25 words** total spoken.
   - Unit carrying its silence beat: **15–18 words**.
   - **Hard ceiling: 28 words** — beyond it, generated speech is
     being asked to run at subtitle-ceiling speed.
   - Inside those totals, Method B's per-turn shape caps bind the
     pair itself (standard turn ≤7 words; one long turn ≤9 only with
     a ≤3-word fragment partner; cliff device fragment uncharged).
     How the two budget systems compose is §7, Conflict 2.
3. **Tactic labels.** Every line carries its tactic verb in the
   margin. **Gate D:** no repeated tactic verb consecutively for one
   speaker; the final tactic ≠ the opening tactic (dialogue report
   §2.3). Every turn also names its speech act, addressee, and want
   (Method B §2.4) and its status move (P7 see-saw).
4. **Anti-front-load construction** (Method B A3, mandatory):
   turn 1 and turn 2 are separate quoted blocks with the picture
   turn written between them; a late beat is parked on paper at
   ≥6.5s; the unit's tail carries a speech-independent event.
5. **Punch-up by volume.** For any line meant to land (the turn line,
   the cliff set-up), the Dialogue Writer drafts ~10 alts, logs them
   all in the scratchpad, and the Showrunner picks at lock. Nobody
   defends a single first idea (craft report §6-C12).

### Pass 4 — TIMING VERIFICATION (Room-runner, mechanical)

No judgment in this pass — arithmetic only.

1. Recount every unit's words against its budget class. Don't trust
   the draft's claim.
2. Read-aloud check at 140 wpm equivalent: a full-talk unit's
   dialogue must time out at **9–11s**. Under 9s = under-filled:
   return to Pass 2 for another beat — **never stretch lines**.
   Over 11s = trim edge words first (edges are sacrificial by
   design, dialogue report §1.5).
3. Pair units are gated on Method B's coverage arithmetic instead
   (spoken words + A2 filled beats ≥ 4.0s of the 5.0s dialogue
   window; fill-class floors per A1). Which gate applies is declared
   per unit in the breakdown. See §7, Conflict 2.
4. Confirm the silence beat's seconds are *in* the unit plan and the
   word budget was reduced for them.

### Pass 5 — CONTINUITY EDIT (Continuity Editor, checklist only)

Method B's pre-flight (§6), run as a pass on the draft. The Editor
answers yes/no per item, **citing the ledger line** for each answer:

- Freshness: the ledger's last delta row == last shipped episode.
- No line contradicts a state card (knowledge, possessions,
  obligations). Knowledge audit: no character knows what their KNOWS
  list lacks, unless this scene is the logged learning.
- Every plant fired here exists in the plant table with an earlier
  plant episode; every plant planted here has been added with a
  payoff episode assigned (no empty payoff cells).
- Names, relations, world rules match the pitch bible.
- Arithmetic audit: the show's counters reconcile (THE COUNT's next
  number follows the canonical value; THE ROSTER's reading position
  matches; THE TENTH SECOND's cull number and wall contents match).
- Voice check: the **cover-the-names test** per unit (dialogue
  report §1.6).

Any "no" returns the unit to Pass 3 with the specific ledger line
quoted. **The Editor does not rewrite.** A deliberate canon change is
made openly as a ledger revision, never smuggled through a draft.

### Pass 6 — CRITIC (fresh context, constrained)

The Critic receives the locked breakdown, the dialogue draft, and
the checklists — *not* the drafting history. Two instruments, in
this order:

1. **The cold read** (the table-read substitute, craft report
   §6-C13): read the episode cold and report only — lines it
   stumbled on, characters it couldn't tell apart, beats it couldn't
   follow. Located by construction.
2. **Located objections:** each must name unit + line, state the
   failure, and cite the gate it invokes (Gate A–D, word budget,
   connector test, legibility test, Method B's four pair tests).
   The Critic also runs the **legibility test**: state each
   speaker's unsaid sentence from the dialogue alone; a mismatch
   with Pass 3's recorded unsaid sentences is a located objection
   (dialogue report §1.3).

Generic feedback is rejected by the Room-runner unread. **Maximum
two critique rounds.** The Critic never rewrites; the Dialogue
Writer rewrites, and Pass 4's counts are re-run on any rewritten
unit.

### Pass 7 — SHOWRUNNER LOCK (the parent)

1. The Showrunner reads the full scratchpad, picks punch-up alts,
   and performs the final pass — the single-voice edit every soap
   head writer performs on every script (craft report §4.4).
2. Lock is declared only when Gates A–D, the timing gate, and the
   continuity checklist all pass. Only the Showrunner locks; a lock
   is what makes an episode canon-eligible.
3. **At lock, the Continuity Editor updates the ledger from the
   locked script** (state-card deltas, plant-table changes, beat
   registry row, one-line episode log), reconciles forecast vs
   actual deltas (a missed delta is recorded as missed — Method B §6
   item 5), and writes the **next-episode anchors**.
4. The Script Coordinator archives the scratchpad and board, files
   the decision log, and advances the version sequence.

---

## §4 — FAILURE-MODE GUARDS

Checks, not intentions. Each guard has an owner, a moment in the
pipeline, and a mechanical test. (Sources: craft report §5; Method B
§§5–6.)

**G1 — Anti-Flanderization.** *Owner: Continuity Editor, at Pass 5.*
The pitch bible records each character's full trait set. The Editor
flags any episode where a character uses only their single most-used
trait, or where one trait's share of the character's beats rises
across three consecutive episodes. A flagged episode returns to
Pass 1 with the flag attached — flattening is a story problem, not a
line problem.

**G2 — Anti-repetition.** *Owner: Script Coordinator, at board
stage (§2), re-checked by the Continuity Editor at Pass 5.* Three
registers are searched before a board is approved: the production
bible, the used-events ledger, and the board archive. On top of the
search, Method B's beat-registry windows bind as hard rules:

- No opening-beat type or pair pattern repeats in **consecutive**
  episodes.
- No pair pattern or **delta class** appears **3 times in any
  5-episode window** — the same delta wearing new shapes is still
  recursion (Method B §10, risk 3).

A beat that matches a prior episode's must be justified in the
decision log or replaced.

**G3 — Plant discipline.** *Owner: Storyliner proposes, Continuity
Editor enforces, reviewed at every lock.* The open-seeds table is
reviewed at each season-projection update and each lock: every seed
is paid off, kept open *deliberately* (with the reason logged), or
retired on record. No seed is forgotten silently. No payoff without
a ledger plant; no plant without an assigned payoff (§1.4).

**G4 — Continuity at every draft, not at delivery.** *Owner:
Continuity Editor.* A contradiction found in a first draft costs a
line; the same one found at delivery costs an episode (craft report
§4.3). The checklist runs at Pass 5 on every episode, and any
deliberate contradiction is logged with the draft that made it and
the downstream episodes it ripples into.

**G5 — Periodic full-room re-pitch.** *Owner: Showrunner. Cadence:
every 5 episodes per show, and at every season boundary.* All roles
re-pitch the upcoming slate in one session — the Simpsons story
retreat / soap structurer-brainstorm pattern (craft report §§2.4,
4.4) — with the explicit job of killing duplicate or stalled
storylines *before* they are written, and of re-examining the season
projection's loose band: what is working gets more room; what is
stalling gets a bail-out while one still exists.

**G6 — Recursion watch at the relationship level.** *Owner:
Continuity Editor, read off the ledger's §4 relationship-delta
table.* An episode whose central pair shows no new relationship-delta
row has repeated the relationship whatever its plot did (Method B
§5.4). Two consecutive no-delta episodes on the same pair escalate
to the Showrunner at the next re-pitch, early if the pair is the
show's spine.

---

## §5 — HOW THE PARENT RUNS A ROOM SESSION

One episode of one show, as a spawn sequence. The parent is the
Showrunner throughout; every other role is a spawned agent instance
with a defined input packet and a defined return. All returns land
in the episode scratchpad.

| # | Spawn | Gets | Returns |
|---|---|---|---|
| 0 | **Continuity Editor** (the show's standing instance) | Ship state of the show | Freshness verdict (Method B pre-flight item 0) + ledger digest: state cards, open plants due ≤2 eps, contested wants, slate status |
| 1 | **Storyliner** (per-show) | Ledger digest, pitch bible, season projection row, slate candidates, next-episode anchors | Premise choice + board file + 6 unit summaries (Gate A/B self-checked) + delta forecast |
| 2 | **Script Coordinator** (shared) | Board + Storyliner's pitch notes | Formalized board file, decision-log entries (pitched / chosen / why / killed), anti-repetition search result (G2) |
| — | **Showrunner gate** (parent, no spawn) | Board + decision log + G2 result | Approve, or return with notes to step 1. *No beat sheet before this gate.* |
| 3 | **Storyliner** (same instance, follow-up) | Approved board | Beat sheets, 3–5 beats/unit, Gate C applied; silence beats, interruption points, plant marks, pair patterns, fill classes declared |
| 4 | **Dialogue Writer** (fresh instance, per-show) | Approved breakdown, voice notes, previous episode's final unit, anchors | Full pair-draft script, serially, with unsaid sentences, tactic margins, alts for landing lines |
| 5 | **Room-runner** (mechanical; parent or checker instance) | Draft | Pass 4 timing sheet: per-unit word counts vs budget, read-aloud timings, gate verdicts. Failures loop to 3 (under-filled) or 4 (over-long) |
| 6 | **Continuity Editor** | Draft + ledger | Pass 5 checklist, yes/no per item with ledger lines cited. Failures loop to 4 with the quoted lines |
| 7 | **Critic** (fresh context, shared pool) | Locked breakdown, draft, checklists — never the drafting history | Cold-read report + located objections. Max 2 rounds; rewrites loop to 4, counts re-run at 5 |
| 8 | **Showrunner lock** (parent) | Complete scratchpad | Final pass, alt picks, LOCK declaration |
| 9 | **Continuity Editor** + **Script Coordinator** | Locked script | Ledger updated from the script; next-episode anchors written; scratchpad + board archived; version sequence advanced |

**Call budgeting.** Steps 0–3 (breaking) must consume at least half
the session's agent calls (§2). If steps 4–7 are consuming the
session, the board was under-broken — that is logged in the decision
log as a process finding, not just absorbed.

**What is shared across the five shows, and what is not:**

- **Per-show, never shared: Storyliner and Dialogue Writer.** Story
  knowledge and voice are show-specific; a Dialogue Writer shared
  across shows is a voice-flattening machine (the cover-the-names
  test would start failing *across* shows). Each show's room keeps
  its own instances.
- **Per-show: Continuity Editor.** It owns one show's ledger.
  Exception: shared-cast characters have one canonical home ledger
  (Method B shared-cast rule) — when a guest appearance touches a
  shared character's state, the *home* show's Continuity Editor
  arbitrates the fact, and cross-show thread state is canonical in
  the ledger of the show that last moved the thread (Method B §10,
  risk 4).
- **Shared: Critic pool.** Fresh context is the Critic's whole
  value; a shared pool instantiated fresh per episode is both
  cheaper and *less* captured by any one show's habits. The pool is
  shared; an instance never is.
- **Shared: Script Coordinator.** One archive discipline across all
  five shows — one decision-log format, one version sequence, one
  board archive — because the anti-repetition check and the
  cross-show threads both read across shows.
- **Shared by definition: Room-runner function and Showrunner.**
  The Room-runner is instantiated per episode as the session's
  coordinator; the Showrunner is the parent, and there is one
  network, so there is one final pass.

---

## §6 — WORKED MICRO-EXAMPLE (THE COUNT, one unit through the pipeline)

> **EXAMPLE — illustrative only.** What follows runs ONE unit of THE
> COUNT through §§2–3 in miniature to prove the spec is usable. It is
> not an episode script, not canon, and plants nothing. Ledger state
> is taken from Method B's record of the shipped pilot: canonical
> count **1005**; the Clerk's ledger disagrees by exactly one — hers
> reads **1006** (the standing gap: "her +1"); the gap is an open
> plant from the pilot, payoff assigned, not yet fired.

**Context.** Hypothetical Episode 2, Unit 3. The unit opens on 1005
already shown — chalked on the counting board (the show's number
handoff: last unit's cliff spoke it, this unit shows it).

**Board card** (≤7 words — 6):

> **Clerk shows her ledger: one ahead**
> *Gilligan line — the Counter is thinking: "If her book is right, I
> skipped. I don't skip."*

**Beat sheet** (Pass 2; 5 beats, each with tactic + Δ):

| # | Beat | Tactic | Δ |
|---|---|---|---|
| 1 | The Clerk lays her ledger open at **1006** beside his board | PRESENT | Δinfo — the gap is visible, not alleged |
| 2 | The Counter counts the ledger's *pages* with a tapping finger, saying nothing | DEFLECT | Δpower — the subject stays paper, not arithmetic |
| 3 | **SILENCE BEAT, 2.0s** — his finger stops mid-page; the room tone drops | — (scripted) | placed immediately before the turn line; word budget reduced for it |
| 4 | The Counter refuses, with an account (Turn 2) | REFUSE | Δinfo — he claims her book invented a number; logged as his *position*, contested |
| 5 | The Clerk dares him to perform his own number (fragment) | DARE | Δpower — if he says it on her demand, the spoken number is the floor's number |

**Pair draft** (Pass 3; Method B five-line format, extended):

```
UNSAID:  CLERK — "You skipped one, and you're afraid of which one."
         COUNTER — "If I stop counting to argue, the count stops
         being true."  (Both carry a cost of saying plain. ✓)
TURN 1:  CLERK → COUNTER | act: present | want: make him look at
         the gap | tactic: PRESENT | status: raise-self
         "My book calls this one six."            (6 words)
PRESSURE: the gap is on the table; silence or a wrong answer both
         concede it. Reaction gap 0.3s, then the silence beat (2.0s)
         — his dispreferred delay, played in action.
TURN 2:  COUNTER → CLERK | pattern: P6 (dispreferred second, played)
         + P1 (her claim challenged at its joint) | status:
         lower-other | tactic: REFUSE
         "Your book counts one I never said."      (7 words)
FRAGMENT: CLERK | tactic: DARE
         "Say five aloud."                        (3 words)
CLIFF (device, uncharged): COUNTER — "One thousand five."
         (Next unit opens on 1005 stamped on a parcel.)
DELTA:   STATUS — Clerk ↑ (she extracted a performed number on her
         demand); KNOWS — the Counter's claim enters his card as
         CLAIMED/contested, not canon; WORLD — the gap plant is
         REMINDED, payoff cell unchanged.
```

Word count: 6 + 7 + 3 = **16 spoken words** — at Method B's pair cap
(§2.2) and inside the silence-beat budget band of 15–18 (§3, Pass 3).

**Timing verification** (Pass 4, mini): mechanical count 16 ✓.
Coverage per Method B A1/A2: 16 words at the pipeline's measured
2.1–2.8 w/s, turn 1 riding the picture turn, + 0.3s reaction gap +
2.0s scripted silence accounts for the full dialogue window. The
unit is pair-gated, not full-talk-gated (§7, Conflict 2).

**Continuity edit** (Pass 5, mini — yes/no with citations):

- Arithmetic audit — **yes**: 1005 matches the ledger's world-state
  canonical value; her 1006 matches the standing gap field (her +1).
- Knowledge audit — **yes**: the Clerk cites only her own ledger;
  the Counter claims only his own count. Neither knows anything
  their KNOWS list lacks.
- Plant table — **yes**: the gap plant is reminded, not fired; its
  payoff cell remains assigned; no payoff is claimed without a plant.
- Cover-the-names — **yes**: only the Clerk would cite "my book";
  only the Counter would phrase a refusal as an arithmetic claim.
- Beat window — **yes**: P6 as spine differs from the previous
  episode's registered pattern for this slot; the delta class
  (STATUS flip via performed concession) is not at 3-in-5.

**Result: PASS**, with one note carried to the ledger at lock —
Turn 2's claim is recorded as the Counter's *position* (CLAIMED,
contested), not as a canon fact. The room has now spent one unit,
one pair, and banked a status delta, a contested claim, and a
reminded plant — which is the whole job.

---

## §7 — CONFLICTS WITH EXISTING DOCTRINE, NAMED WITH RESOLUTIONS

**Conflict 1 — One line per unit vs one exchange per unit.**
The founding treatments (e.g., SHOW-4: "exactly one spoken line per
unit at 7–9s, ≤9 words") and the pilot grammar specify a single line;
the Pair Law cannot be satisfied inside that grammar (Method B §9,
Conflict 1). **Resolution:** the Pair Law is adopted. Method B
proposed the amendment; this room method enacts it as standing
procedure — the treatments' one-line grammar is superseded *for
dialogue units*, and the treatments remain canon for premise, cast,
and world. Single-line units survive as declared SPARSE or fragment
shapes (§3, Pass 2 fill classes); wordless units survive under
Conflict 4. *Flagged for parent/user ratification, as Method B
required — the room writes to the pair law from adoption, and the
flag stays on record.*

**Conflict 2 — Two word budgets.**
Method B caps the pair (turn ≤7 words, total spoken ≤16/unit) from
ASR measured in this pipeline; the dialogue research budgets the
unit (22–25 words full-talk, 15–18 with a silence beat, hard ceiling
28, gated at 9–11s at 140 wpm) from general screen norms. Both
cannot be the same gate. **Resolution — layered budgets.** Method
B's per-turn shape caps always bind: they are what makes a pair a
pair. Unit totals are gated by class, declared in the breakdown:
*pair units* are gated on Method B's fill classes and coverage
arithmetic (Pass 4.3); units declared **FULL-TALK** (fragment
chains, counting fights, overlapping argument — shapes whose word
totals the house has not yet measured) are gated on the research
budget and the 9–11s check. Where the two collide head-on — one pair
asked to fill a unit by words alone — **Method B wins**: measured
house data outranks imported norms. And under neither budget may a
line be stretched to fill time; under-fill is fixed at Pass 2 with
another beat.

**Conflict 3 — Word budgets vs the generator's front-loading.**
Measured on PILOT-5: the generator front-loads quoted speech (lines
land at 0–5.6s regardless of where the script parks them), so a pair
budgeted and placed for 6.5–8.7s may be spent by 5.6s. **Resolution:
the budget governs the script; placement is a production behavior.**
Pass 4 measures the script read aloud — a drafting gate, passed or
failed on paper. The generated take's placement is handled by
Method B A3's construction rules (two quoted blocks, never one; a
late beat parked on paper at ≥6.5s; a speech-independent tail event)
and measured at production QC, which is outside this document. If a
show's ASR shows lines consistently landing in the 0–5.6s band, the
drafting response is to move the pair earlier on paper and log the
surrender of the late slot (A3) — the room never "fixes"
front-loading by rewriting the budget, because the budget was never
the thing that moved.

**Conflict 4 — The Pair Law vs single-speaker and wordless units.**
THE MACHINE is cut like an MV (sung handoffs, word-sync) and THE
LAST SEAT licenses wordless units; a spoken-pair law cannot bind
either as written (Method B §9, Conflicts 4–5). **Resolution:** the
Pair Law binds *dialogue units*. In THE MACHINE, pairs close by
**8.5s hard**, the cliff word is always SUNG, never dialogue, and
turns are written against the beat grid — the song remains the tempo
gospel; conversation rides it or doesn't ride at all. In THE LAST
SEAT, a pair may be **danced** (the performer's phrase is turn 1;
the seat's answer — a light, a sound, an act KEPT or CULLED — is
turn 2) and must still bank a delta. Declared wordless units are
exempt from the Pass 3–4 word gates but **not** from the delta
requirement (Method B R2): a unit with no pair and no delta is
texture, and texture is cut.

**Conflict 5 — The craft pass taxonomy vs the seven-pass pipeline.**
The craft report's order (story → structure → character → scene →
dialogue → polish) has no continuity or critic pass; the dialogue
report's seven passes do. **Resolution:** mapping, not contradiction
(§3 intro). The classic taxonomy assigns continuity to a *role*
(the script coordinator checks every draft) and the read to an
*event* (the table read); an AI room has no ambient layer where
either happens by itself, so this room runs both as explicit passes
(5 and 6) owned by those same roles. The Continuity Editor is a role
that owns a pass; the Critic is the table read, formalized.

**Conflict 6 — Who may declare the episode locked.**
The dialogue report's Orchestrator "is the only role that can
declare the episode locked"; the craft report gives final approval
of every beat and draft to the showrunner. **Resolution:** the verb
is split. The Room-runner (this room's orchestrator function)
declares an episode **pipeline-complete** — every gate passed, every
checklist closed. Only the Showrunner **locks** — the lock is the
canon act, and it is the parent's alone. Pipeline-complete is
paperwork; locked is the show.

**Conflict 7 — Season-first breaking vs the per-episode slate.**
The craft report breaks the season backward from its ending before
episode one; Method B's SLATE generates candidates after each
episode ships. **Resolution:** two cadences, both binding. The
season projection is written once, backward from the final image,
and updated at every lock; SLATE runs inside it after each lock.
The projection is firm for the next 2–3 episodes (the bail-out
position); a slate candidate that contradicts the firm band loses,
and a candidate in the loose band may amend the projection — at the
re-pitch (G5), in the open, never silently.

**Conflict 8 — Soap many-hands dialogue vs serial drafting.**
Soaps split dialogue across many writers and circulate adjacent
breakdowns; Dramatron's professional users documented continuity
inconsistencies from *parallel* dialogue generation. **Resolution:**
one Dialogue Writer per episode, drafting serially under the
carry-forward rule. The soap's adjacent-context practice survives as
the writer's input packet (previous unit verbatim, previous
episode's final unit, next-episode anchors) — the context is
supplied structurally, exactly as the soaps supply it, but the hands
are one pair, in order.

**Conflict 9 — Cold arrivals vs an episode that opens
mid-conversation.** The feed sends strangers; a first pair must not
presume knowledge (Method B §9, Conflict 2). **Resolution:**
episode-opening pairs are restricted to self-evident pressures —
demand/refusal, dare/concession, question/misdirection. Callbacks
(P3) and repairs of ledger facts (P8 on a canon fact) are banned
from opening pairs. The ledger governs what characters may know and
what may change; it never governs what a unit must explain. Serial
depth is a bonus for returners, never a tax on strangers.

---

## SOURCES AND DEBTS

This document is a synthesis; its evidence lives in the three
documents it merges, and their source lists govern:

- `research_notes/writers-room-craft-20261115/report.md` — room
  roles and hierarchy, the Gilligan board method, pass taxonomy,
  soap pipeline (projection → breakdown → dialogue → single-voice
  edit), bible ownership, Flanderization and repetition guards.
- `research_notes/writers-room-dialogue-20261115/report.md` —
  lines as speech acts, tactic rotation, subtext and the legibility
  test, timing math (§1.7), plant-and-payoff ledger discipline,
  Agents' Room / Dramatron / FilmAgent evidence, Self-Refine and
  Huang et al. on critique loops (§4.5).
- `research_notes/conversation-continuity-method-20261115/report.md`
  (Method B) — the Pair Law, the eight pair patterns, the ledger
  spec (§5), rules R1–R5 and pre-flight (§6), fill ranges and the
  anti-front-load rule (Addendum A1–A3), the story slate (A4).
- `new-era/shows/SHOW-4_the-count.md` — THE COUNT's cast, gap canon,
  and number-handoff device, used in §6.

Nothing in this document overrides the FIRST_SECOND_DOCTRINE's
first-second law: the hook stays silent and legible with the sound
off, and every rule above operates inside the 10-second atom the
doctrine defines.


---

## AMENDMENTS ADOPTED 2026-11-15 (from the talking-story-creators research, user msg 470)

The full amendment text lives at research/talking-story-creators-20261115/amendments.md and is ADOPTED as part of this method from Episode 3 onward: A1 revised word budgets (episode total 80-90 words, cap 95; per-unit ceiling 20) REPLACE the §3 Pass 3 budgets; A2 three scripted digestion gaps at fixed placements REPLACE the one-silence-beat rule; A3 Gate E (cold-reader story legibility + relatability clause) is a NEW lock gate; A4 character-intelligence beats (the questioning job, character cards, one shared wrong belief) are a NEW Pass 2 requirement; A5 supporting rules (plot-pattern letters, one-talker default, shared task, scratch-read timing, clippable line, repetition audit, coverage note) are adopted. Micro-drama density is explicitly rejected.
