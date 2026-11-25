# GATE LOG — PILOT-4 THE COUNT

QC method: ffprobe on every take; frames extracted at 0.0/2.5/5.0/7.5/9.8 s
(+ denser where a beat needed isolating) and read back; dialogue verified by
faster-whisper transcription of every take (qc/transcripts.json) against the
written script. Panel QC per spec §4.5 is in REFERENCE_STACK.md.

## Dialogue gate (written line must be the spoken line) — PASS, all units

- U1: "Say the number between ours, counter." + cliff "1,001" ✓
- U2: "Your ledger counted that parcel twice." + "One thousand two." ✓
- U3: "Write the missing digit, Counter. Now." (ASR hears "Right" for
  "Write" — base-model mis-hear; word shape and the rest of the line exact)
  + "One thousand three." ✓
- U4: "It went back one. Tell no one." (ASR prefixes a spurious "If") +
  "One thousand four." ✓
- U5: spoken recount murmur ("One, two, three, four, five, six.") +
  "We agree, Counter. So we're both wrong." + "One thousand five." ✓
- U6: "Open it, Clerk. It's counting without us." + cliff "One thousand…"
  trailing off unfinished — the count never completes, as scripted ✓
Line always precedes its cliff; order correct in all six units.

## Per-unit verdicts

**U1 — PASS.** Frame 0 is the doctrine image: board 1000 + ledger 1001
legible in one frame, Counter mid-press. Identities exact vs CHAR sheets.
Note: the take push-ins to the speakers instead of holding the locked wide
(camera law said no move in the first 12 f — the opening IS the locked
frame, motion begins after; logged as a deviation, not a fail).

**U2 — CONDITIONAL PASS (major flaws disclosed).**
- Clerk identity FAIL: unanchored in this call (WORLD + SNH panels only),
  she renders as a different, older woman in a green cardigan and pearls;
  late in the take a second, bobbed figure appears at frame right —
  a duplicated clerk. The locked Clerk is absent from her own unit.
- Frame-0 number PARTIAL: the parcel stamp is small and hand-covered at
  0.0 s; "1001" is legible mid/late take inside "POST OFFICE" stamp ovals
  (pseudo-text around the digits — in-world prop printing).
- World: the hall is fully re-dressed (green room, notice board) rather
  than swapped inside the anchor frame.
- SNH identity PASS; dialogue PASS; the double-parcel event reads.

**U3 — PASS with notes.** "1002" is body-occluded by the Counter at frame
0 and fully legible by mid-take; the missing-digit state therefore reads
at the open and the smear plays in reverse (write/complete, not erase).
Whole-frame grade shifts cold fluorescent blue — beyond the playbook's
one-foreign-colour allowance; motivated in-script as the rebuilt world.
Identities PASS; dialogue PASS.

**U4 — CONDITIONAL PASS.** The chest-tally close-up reads exactly 1003,
huge and legible — the unit's event lands. The backward step is PARTIAL:
split-flap turnover is visible in the close-up, but no clean held "1002"
frame could be isolated in samples. Clerk identity FAIL again (elderly
woman, mustard cardigan — same unanchored-invention failure as U2; she
appears only in the tail two-shot). Take arrived 3:2 (1152×768) despite
the aspect steer — conformed by crop in assembly (CUTLIST). SNH PASS;
dialogue PASS.

**U5 — PASS with notes.** Board 1004 and ledger 1004 both present (the
agreement reads; the ledger total is small on the page). Counter wardrobe
drift: brown tweed jacket replaces the locked ink-black suit (face/head/
tally chain all hold). The appearing-chair beat could not be isolated in
sampled frames. Clerk PASS (anchored); dialogue PASS incl. the recount.

**U6 — PASS after the assembly head-trim.** Raw take opens on ~0.75 s of
empty hall (the banned establishing opener) — removed in the cutlist;
the unit opens mid-walk with the chalked 1005 door in frame, conformed
at 0.925× to hold exactly 240 f. Chalk 1005 legible on the door glass.
The through-window second board reading 1006 does NOT read (dim room
behind glass, no legible digits) — the turn lands on the door itself.
Clerk wardrobe drift (green knit, skirt) though her bob/glasses/face
hold — she was unanchored in this call too. Dialogue PASS, cliff trails
off unfinished as scripted.

## Standing gates

- **Frame-0 / first-second:** PASS U1 (exact doctrine beat), U4, U5;
  PARTIAL U2 (number small), U3 (number occluded), U6 (fixed by trim).
- **Wordmark (`~ WuBu ~` hoodie):** NOT TRIGGERED — UNC is not in this
  pilot's cast (brief cast: Counter + Clerk). The master carries the
  network corner bug instead. Logged so the gate is not silently skipped.
- **Generated text:** PASS — no captions, titles, subtitles or overlays
  in any take. All writing is in-world pictured subject (board digits,
  ledger totals, parcel stamps, chalk) — the allowed exception class.
- **Motion law:** PASS — every cut in the assembled master lands on a
  frame already moving (joint frames verified post-assembly); no
  halted-photo starts after the U6 head-trim.
- **Adults only:** PASS — all figures adult.
- **Zero reused footage:** PASS — six original takes, no repeats, no
  stock.
- **Event-read + motif axis:** PASS — press / slide / write / flip /
  appear / approach are six distinct motion motifs; each unit's named
  event reads on screen (U4's back-step and U5's chair at PARTIAL,
  above).
- **Count arithmetic:** PASS — 1000 (board) / 1001 (ledger) → 1001 →
  1002 → 1003 → 1004 (agreed) → 1005, exactly one increment per unit,
  every cliff spoken and every next number shown.

## Pattern finding (for the show kit)

The Clerk holds identity ONLY in calls that carried her CHAR sheet
(U1/U3/U5) and is re-invented — older, cardiganed — in every call that
didn't (U2/U4/U6). The Counter, anchored in 4 of 6 calls and text-held
in the rest, never fully broke. With the 2-image fire cap, a two-hander
unit cannot anchor both faces plus the world; future episodes should
either build a combined two-character PEAK-style anchor per unit or
alternate which face is large. Recorded in the kit notes.

## Closing note on refires

The build's video budget was one volley of 6 and it is spent; U2/U4's
identity flaws are therefore shipped disclosed rather than refired.
If the parent orders a second volley, U2 and U4 are the refire queue,
in that order, with the Clerk's CHAR sheet in both calls.
