# LEDGER — SHOW-4 THE COUNT

## 0. Header

- **Show:** SHOW-4 — THE COUNT
- **Ledger version:** v2 — updated from the locked E2 script at its lock (resumed room session, 2026-11-15; see the episode's DECISION_LOG). v1 was seeded from the shipped pilot; no SHOW-4 continuity ledger existed before v1.
- **Last episode shipped:** PILOT-4 'The Number Between Ours' (E1). **Last episode locked:** E2 'The Door Counts First' — deltas below are written from the locked script per the room's lock procedure; they reconcile to ship state when E2 ships.
- **Freshness:** This ledger's last delta row (§8) is E2 (locked) over PILOT-4 (E1, last shipped). Pre-flight item 0 passes for E3 on the locked-script basis recorded here.
- **Canon source:** PILOT-4 EPISODE_PLAN.md (script) and GATE_LOG.md for E1; the locked E2 SCRIPT.md for E2. The show doc's treatment chains C1-1 / C1-2 / C1-3 are NOT shipped canon and are not ledgered as facts here.
- **Next required reads:** This whole file (Method B R1 — read first).

## 1. Canon facts (append-only)

| ID | Fact | Established | How | Status |
|---|---|---|---|---|
| F-001 | The board count and the Clerk's ledger disagree by exactly one, hers higher ("her +1"). | E1 U1 | SHOWN+SPOKEN | ACTIVE |
| F-002 | A number can arrive twice — two parcels both stamped 1001. | E1 U2 | SHOWN | ACTIVE (event SPENT) |
| F-003 | The Counter CLAIMED her ledger counted the parcel twice; she never conceded. | E1 U2 | SPOKEN | ACTIVE — CLAIMED / contested |
| F-004 | A counted digit can cull mid-count — chalked 1002 lost its last digit, the wall read 100_. | E1 U3 | SHOWN | ACTIVE (event SPENT) |
| F-005 | The Counter refused to write the missing digit. | E1 U3 | SHOWN | ACTIVE |
| F-006 | The Counter's chest tally stepped backward 1003→1002, then returned to 1003. | E1 U4 | SHOWN | ACTIVE (event SPENT) |
| F-007 | The Counter ordered the back-step kept secret ("Tell no one"); the Clerk wrote it in her ledger anyway — she holds his secret. | E1 U4 | SPOKEN+SHOWN | ACTIVE |
| F-008 | At 1004, board and ledger AGREED — the first agreement. | E1 U5 | SHOWN | ACTIVE |
| F-009 | A chair appeared in the row that neither counted; the total was wrong even in agreement. | E1 U5 | SHOWN | ACTIVE (event SPENT) |
| F-010 | The Clerk's stated position: when they agree, both are wrong. | E1 U5 | SPOKEN | ACTIVE |
| F-011 | Behind a chalked door at the hall's end, a second counting desk with its own board is counting without them; its board already read 1006. | E1 U6 | SHOWN | SPENT (confronted E2 U1/U3 — the desk was entered, found empty, and lost again behind the sealed door, E2 U6) |
| F-012 | The pilot's count ended mid-word — the Counter began "One thousand—" (1006) and was cut; last completed spoken number is 1005; 1006 is OWED. | E1 U6 | SPOKEN | SPENT (1006 completed aloud by the Counter, E2 U1 — a beat after the door moved first) |
| F-013 | The unattended desk's board showed 1008 — exactly the Clerk's ledger standing total (the count's leading edge +1). The desk keeps her totals. | E2 U2 | SHOWN | ACTIVE |
| F-014 | The desk's tally roll carries a written backward mark at 1003 — the Counter's back-step (F-006) recorded outside the Clerk's ledger, by a third party. | E2 U4 | SHOWN | ACTIVE |
| F-015 | The door at the hall's end opens and seals from the far side alone; no one was seen opening or closing it, either time. | E2 U1/U6 | SHOWN | ACTIVE |
| F-016 | The Clerk locked her ledger and withdrew the audit; reopening is priced at the Counter's concession that her book counts. He has not paid. | E2 U5 | SPOKEN+SHOWN | ACTIVE |

## 2. Fact bank

### SPENT

One-time events. Callable back (doctrine S6, one callback per unit), never re-presented as new.

- **F-002** — number arrived twice (two parcels stamped 1001), E1 U2.
- **F-004** — digit culled at 1002 (final digit), E1 U3.
- **F-006** — chest tally back-step 1003→1002, then returned to 1003, E1 U4. (Called back once in E2 U4 as a written record on the desk's tally roll — a record of the step, not a re-staging.)
- **F-009** — uncounted chair appeared at 1004, E1 U5.
- **F-011** — the second desk revealed behind the door, E1 U6; spent as confronted in E2 (entered, found empty, lost behind the sealed door).
- **F-012** — the owed 1006, E1 U6; spent in E2 U1 (completed aloud, late).

### PLANTED

Every plant carries planted-in / remind-in / payoff-in — no empty cells.

| Plant | What | Planted-in | Remind-in / Move-in | Payoff-in | Thread |
|---|---|---|---|---|---|
| PL-1 | The gap (her +1, from F-001) | E1 | REMINDED E2 U2 (the desk keeps her total — the gap is kept independently now) | E4 | T-ARC-3-2 |
| PL-2 | The second desk / the door (F-011) | E1 | MOVED E2 (entered U1, confronted U3, lost again U6 — the pilot cliff's ledger debt, R5, discharged) | E3 | T-ARC-3-1 |
| PL-3 | The back-step secret (F-007) | E1 | REMINDED E2 U4 (now recorded on the desk's roll, F-014 — no longer hers alone) | E3 | T-ARC-3-2 |
| PL-4 | The uncounted chair (F-009) | E1 | Remind E3 | E4 | T-ARC-3-3 |
| PL-5 | The other desk keeps the Clerk's totals (F-013) | E2 U2 | Remind E3 | E4 | T-ARC-3-2 |
| PL-6 | The door opens and seals from the far side alone (F-015) | E2 U1/U6 | Remind E3 | E3 | T-ARC-3-1 |

## 3. Character state cards

### SUPER NUMBER HEAD (the Counter)

```
KNOWS:      F-001, F-002, F-003, F-004, F-005, F-006, F-008, F-009, F-010,
            F-011, F-012; adds F-013 (the desk keeps her totals — learned
            E2 U2), F-014 (the back-step is recorded outside her ledger —
            learned E2 U4), F-015 (the door opens and seals from the far
            side alone), F-016 (the price of reopening). Of F-007 he knows
            his own order ("Tell no one"); since E2 U4 he also knows the
            step is written somewhere he cannot reach — whether he saw
            HER write it in E1 is still UNESTABLISHED.
WANTS:      The count to be his and true [since E1] — CONTESTED by the
            door and the desk, E2 U1 (he completed 1006 and disowned it
            in the same breath); the back-step never known [since E1] —
            the want now fails in fact: it IS known, by the desk (E2 U4)
OWES:       THE TALLY CLERK: the concession that her book counts — the
            price of reopening her locked ledger (born E2 U5, UNPAID).
            The 1006 debt is DISCHARGED (completed E2 U1).
IS OWED:    Nothing established
STATUS:     vs THE TALLY CLERK: DOWN (as of E2 — she holds the audit, the
            price, and the last word at the door)
LAST CHANGE: E2 U6 — conceded "It's counting without us" to the sealed
            door and spoke 1012 alone, unaudited
HOME:       This ledger
```

### THE TALLY CLERK

```
KNOWS:      F-001, F-002, F-003, F-004, F-005, F-006, F-007, F-008, F-009,
            F-010, F-011, F-012 — in full, including F-007 (she wrote it);
            adds F-013, F-014 (she read the desk's record of the back-step,
            E2 U4), F-015, F-016
WANTS:      The two counts reconciled — or his concession that her book
            is a count [since E1]. As of E2 U5 the concession is no longer
            only wanted: it is PRICED, as the cost of reopening her ledger.
OWES:       Nothing established. (Her book is locked by her own act,
            E2 U5; the reopening is hers to perform if the price is paid.)
IS OWED:    SUPER NUMBER HEAD: the concession that her book counts
            (from E2 U5, UNPAID). (Note: in E1 U1 her dare extracted his
            performed "One thousand one" — her number, spoken by him; in
            E2 U2 he spoke her number again, 1008, as the unit's cliff.)
STATUS:     vs SUPER NUMBER HEAD: UP (as of E2)
LAST CHANGE: E2 U6 — left the price standing at the sealing door
            ("Count alone, then. The price stands.")
HOME:       This ledger
```

### Pointer cards (shared cast — one line each, HOME elsewhere, never copies)

- **PETER** → SHOW-3 ledger. Has not appeared in THE COUNT yet.
- **UNC** → SHOW-1 ledger. Has not appeared in THE COUNT yet.
- **LAURA** → SHOW-1 ledger. Has not appeared in THE COUNT yet.
- **DISPATCHER** → SHOW-2 ledger. Has not appeared in THE COUNT yet.

## 4. Relationship deltas

| Pair | Episode | What changed | Direction |
|---|---|---|---|
| THE TALLY CLERK ↔ SUPER NUMBER HEAD | E1 | She dared and he performed her number; at 1004 they agreed and agreed they were both wrong; she now holds his back-step secret | both→debt |
| THE TALLY CLERK ↔ SUPER NUMBER HEAD | E2 | The desk's witness made her total a room fact; she locked her ledger and priced its reopening at his concession; he ended the episode counting alone and unaudited, the debt unpaid | Clerk ↑ / Counter ↓ — his debt, priced |

## 5. World state (THE COUNT counters)

- **Canonical count (Counter's, last completed spoken):** 1012 (spoken E2 U6, alone and unaudited)
- **Next number owed:** none outstanding in the count itself — the debt has moved: the door is sealed and the reopening is owed (see OWES, §3)
- **Clerk's ledger current total:** LOCKED at E2 U5 (clasp stamped 1010; her standing +1 unreconciled behind the lock)
- **The other desk's board:** 1012 (last seen in the closing light-gap, E2 U6 — still counting behind the sealed door)
- **The gap:** her +1, standing — and now kept independently by the desk (F-013); board/ledger agreed once, at 1004 (F-008)
- **Skipped numbers, known list:** NONE confirmed
- **Anomaly list:** digit culled at 1002 (final digit); tally back-step 1003→1002 (now also recorded on the desk's roll, F-014); number arrived twice (1001); uncounted chair at 1004; a door that opens and seals from the far side alone (F-015)
- **Who holds the count now:** THE DESK — behind the sealed door; the Counter holds only the speaking of it

## 6. Open threads

| Thread | Name | State | Last moved | Next question |
|---|---|---|---|---|
| T-ARC-3-1 | The count goes on without them (the door / second desk) | DEVELOP | E2 U6 | "What controls the desk — and what happens when the sealed door reopens?" (payoff owed E3: the desk's controller; the reopening) |
| T-ARC-3-2 | Her +1 (the gap; the secret she holds) | OPEN | E2 U4/U5 | "The back-step is written at the desk and her book is locked — what does the record buy whoever reads it?" (payoffs owed: PL-3 E3; PL-1 / PL-5 E4) |
| T-ARC-3-3 | The count does not match the world (the skipped number; totals that arrive wrong) | OPEN | E1 U5 | Not yet posed as a cliff question in a shipped episode (PL-4 remind E3) |

## 7. Beat registry

| Episode | Opening-beat type | Pair patterns | Delta classes banked | Handoff variants | Cliff types | Motion motifs |
|---|---|---|---|---|---|---|
| PILOT-4 (E1) | Disagreement tableau — two totals in one frame | None (pilot written under the pre-pair-law one-line grammar; line acts: dare / accusation / demand / refusal-with-secret / confession-dare / demand) | KNOWS asymmetry (she logs his back-step); STATUS leveling (the agreement); WORLD advance (count 1000→1005; a second counter exists) | Board digits → parcel stamp → chalk wall → chest tally badge → board+ledger frame → chalk door | Spoken number ×5; mid-word cut ×1 | Pressing / sliding / erasing / stepping-back / appearing / approaching |
| E2 | The owed number on a door that opens itself — single carrier, the handle turning under a still hand | P6 · P5 · P2 · P8 · P1 · P3 | KNOWS (he learns the desk keeps her totals; the back-step is recorded outside her book); STATUS (LEVEL → Clerk UP); WORLD (count 1005 → 1012 spoken; door unopened → opened → sealed; the desk holds the count); OWES (the concession, born U5); WANTS contested (his ownership of the count, U1) | Brass key tag → threshold plate → enamel sign → tally roll header → ledger clasp stamp → inner door face | Spoken number ×6 (alternating speakers; the last spoken alone, unaudited) | Turning / swinging / striking / unrolling / locking / sealing |

**Window watch (from DECISION_LOG G2 Check 4):** KNOWS, STATUS and WORLD each stand at 2-in-5 (E1 + E2). If E3 banks any one of them again it reaches the 3-in-5 ceiling and must be justified or redesigned at E3's board stage.

## 8. Episode delta log

| Episode | Facts spent | Facts planted | State changes | Beats used | Cliff question (→ thread ID) |
|---|---|---|---|---|---|
| PILOT-4 (E1) | F-002, F-004, F-006, F-009 | PL-1, PL-2, PL-3, PL-4 | World count 1000→1005; Clerk KNOWS gains the back-step secret; thread T-ARC-3-1 opened | See §7 registry row | → T-ARC-3-1 |
| E2 | F-012 (1006 completed), F-011 (desk confronted); F-006 called back once (record, U4) | PL-5, PL-6 (facts F-013–F-016 entered) | Canonical count 1005 → 1012 spoken; Counter KNOWS gains F-013, F-014; Counter OWES the Clerk the concession (born U5, unpaid), 1006 debt discharged; STATUS LEVEL → Clerk UP / Counter DOWN; Counter's WANT (the count his) CONTESTED; Clerk's ledger open → LOCKED; door unopened → opened → sealed; who holds the count: CONTESTED → THE DESK; T-ARC-3-1 OPEN → DEVELOP | See §7 registry row | "What controls the desk — and what happens when the sealed door reopens?" → T-ARC-3-1 |

## NEXT-EPISODE ANCHORS (for Episode 3 — written at the E2 lock)

1. The door is sealed from the far side; the desk behind it still counts and already holds 1012 — the count goes on without them, out of reach.
2. The Clerk's ledger is locked; reopening it costs the Counter one concession — that her book counts — and he has not paid.
3. The back-step is no longer hers alone to hold: the desk's tally roll has it written at 1003.

## STORY SLATE

**Inputs (from this ledger — Method B Addendum A4):**

- PLANTED facts: PL-1 (the gap, her +1), PL-2 (the second desk / the door), PL-3 (the back-step secret), PL-4 (the uncounted chair) — with threads and due dates per §2.
- WANTS: SUPER NUMBER HEAD — the count to be his and true; the back-step never known [since E1]. THE TALLY CLERK — the two counts reconciled, or his concession that her book is a count [since E1].
- Open threads under pressure: T-ARC-3-1 (OPEN, cliff debt — must MOVE in E2 per PL-2 / R5), T-ARC-3-2 (OPEN), T-ARC-3-3 (OPEN).
- Next-episode anchors for E2 (as consumed by this slate): the door unopened with her hand on its handle; the desk already counting 1006; the owed 1006 to be completed or answered in E2 U1. All three discharged in E2; the E3 anchors now stand at the head of §8.

**Candidates (run at the E2 slate — full record in the episode's DECISION_LOG):**

1. **CHOSEN for E2** — "The door opens from the far side and the desk beyond is already keeping the Clerk's total, pressing her want for a concession." [PL-2/F-011 · Clerk's want · T-ARC-3-1] — spent as E2's premise.
2. **Standing** — "The Counter tries to own the count by completing 1006 alone, but every total he reaches arrives already matched in her book." [PL-1 · Counter's want · T-ARC-3-2] — not chosen for E2; remains on the slate (its premise is partly re-priced by E2: the matching book is now the desk's, and hers is locked).
3. **Standing** — "A tally record from beyond the room threatens the back-step the Counter ordered buried." [PL-3 · Counter's want · T-ARC-3-2] — not chosen for E2; its record arrived inside E2 as a reminder (U4), so the candidate survives in sharpened form: the record is loose, and E3 owes PL-3's payoff.

_(The E2 anchors that stood here in v1 are discharged — all three were answered in E2 U1/U2 — and are replaced by the E3 anchors at the head of §8.)_
