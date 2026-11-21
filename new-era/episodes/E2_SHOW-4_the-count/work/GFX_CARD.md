# GFX CARD — SHOW-4 'THE COUNT', E2 "The Door Counts First"

Device family (Method C §2.4, accent FOREST): THE SPLIT TOTAL (2.4a, the
show's invariant), THE TALLY THAT RE-COUNTS ITSELF (2.4b, max one/episode),
THE n/? CHIP pattern folded into the Split Total's chips (2.4c behaviour:
values change only on naming beats, never between beats, never at frame 0).
Route P (PIL, deterministic — G8). Accent: FOREST green, kit value locked for
this build: #1F6B3A (no hex exists in the show kit; this card locks it).
Faces: board total = Noto Sans Black, lit-board white on INK; ledger total =
Noto Serif, ink on BONE. Furniture placement: bottom-left (the ~ WuBu ~ bug
owns bottom-right). The invariant RESTS ambient from frame 0 (sanctioned,
§3.5); its first EVENT fires at U1's TURN — no graphic event before ~1.5s in
unit 1, and no graphic event ever starts inside a spoken-line slot (G7).
Events are re-keyed to MEASURED event/speech times in the takes before
render; the times below are the plan skeleton.

## State table (board | ledger) — the arithmetic audit target
| Unit | Board | Ledger | Why |
|---|---|---|---|
| U1 | 1006 | 1007 | the desk beyond the door keeps her totals; she is one ahead |
| U2 | 1007→1008 | 1008 | threshold plate 1007 arrives; the board is revealed as her ledger's standing total 1008 |
| U3 | 1008→1009 | 1008 | the board advances ALONE at the bell strike |
| U4 | 1009 | 1009 | resting agreement — she clerked 1009 at U3's cliff |
| U5 | 1011 | 1010 | the desk leads; her book LOCKS at the clasp number 1010 |
| U6 | 1011→1012 | 1010 | the board ticks up in the closing gap; the book stays locked; he catches up by speaking 1012, unaudited |

Rule honoured: the two totals disagree by exactly one wherever they disagree;
the ledger chip advances only when the Clerk clerks a number; the board chip
advances only on the desk's own events. §3.4: the ledger values advance every
unit boundary or hold for a stated reason (U6: locked — the lock IS the plot).

## Event plan (one graphic event per unit + invariant ambience — density cap)
- U1 TURN: one digit migrates board→ledger across the chips (door opens itself).
- Joint U1→U2: the §3.1 named straddle — a Split Total digit mid-migration
  across the cut, completing in U2's hook (board 1006→1007, the threshold
  plate's number arriving).
- U2 TURN: board chip flips 1007→1008 (the reveal: it keeps her total exactly).
- U3 TURN: board chip 1008→1009 locked to the desk bell's self-strike.
- U4 TURN: THE TALLY THAT RE-COUNTS ITSELF (the episode's one use): a
  five-bar-gate cluster beside the chips un-draws one mark and re-draws it in
  the other ledger's style — the audit unit gets the audit device.
- U5 TURN: one digit migrates ledger→board (her side loses the lead as the
  book locks).
- U6 TURN: board chip 1011→1012 in the closing gap.
- Cliff ticks: a ~150ms settle pulse on the chip whose value equals the
  spoken cliff number, at the measured cliff line.

## Three-question audit (per device, §4)
- SPLIT TOTAL: (1) what does the viewer learn that the picture doesn't say?
  That two records of the same count disagree by exactly one — the episode's
  whole argument, never stated in dialogue. (2) could a caption do it? No —
  it is a persistent state, not a line. (3) does it move with the story? Yes —
  every change is a plot event (migration/flip/lock). PASS.
- TALLY RE-COUNT: (1) the desk's record corrects itself in the other book's
  hand — the audit made visible. (2) No. (3) Yes — fires once, at the audit
  unit's turn. PASS.

## Assembly (§5.5)
Joint Gate runs on the joined picture BEFORE any composite. Master encode:
joined picture + Split Total layer + Tally layer + bug = max load (two
graphic layers + bug). Graphic QC (§5.6) on the finished master: legibility
at phone size, arithmetic audit vs the state table above, frame-0 audit,
line-slot audit — all logged in GATE_LOG.md.
