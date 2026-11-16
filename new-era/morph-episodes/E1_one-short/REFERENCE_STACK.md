# REFERENCE STACK — ONE SHORT, E1 "Thirty-One Umbrellas"

Inherited LOCKED from E2_SHOW-4 (md5s verified identical on copy-in,
2026-11-16); new panels generated for the shopfront office (the morph moved
the show from the counting hall to the shop) and eye-QC'd before firing.

| Panel | md5 | Source | Status |
|---|---|---|---|
| PNL-CHAR-CLERK-sheet.png (3:2) | f5fe1aedcd466530c69d53f85c559572 | E2_SHOW-4 kit, LOCKED inherited | LOCKED |
| PNL-CHAR-CLERK-sheet-16x9.png | 18f9e8fbae905b870d9bc267cdd20e62 | local pad of the locked sheet | LOCKED (derived) |
| PNL-CHAR-SNH-sheet.png (3:2) | 99b701477a2246caf9c8c8857e0a404f | E2_SHOW-4 kit, LOCKED inherited | LOCKED |
| PNL-CHAR-SNH-sheet-16x9.png | 0ccd7f8786c12be8873bf2c49433af14 | local pad of the locked sheet | LOCKED (derived) |
| PNL-WORLD-office.png | 191737d7ed6e81d25fa32dc8865dcd85 | generated E1: text only | LOCKED after eye QC |
| PNL-CHAR-PLANNER-sheet.png | b4b54a89da49cdbc0ef119f8b42e1c0d | generated E1: text only | LOCKED after eye QC |
| PNL-CHAR-PLANNER-sheet-16x9.png | 28d8999afb2f187cbc131858e03a8673 | local pad of the new sheet | LOCKED (derived) |
| PNL-PEAK-U1.png | 236f77446885b45ef70b403d08afc680 | generated E1: WORLD + 3 sheets + text | LOCKED after eye QC |
| PNL-PEAK-U2.png | 097d8427f95680a05885fc5191eca90d | generated E1: WORLD + 3 sheets + text | LOCKED after eye QC |
| PNL-PEAK-U3.png | 8465b608ccbe0b55742ac3565714afe4 | generated E1: WORLD + 3 sheets + text | LOCKED after eye QC |
| PNL-PEAK-U4.png | f945ca4aec5468e688f6016d7048b291 | generated E1: WORLD + 3 sheets + text | LOCKED after eye QC |
| PNL-PEAK-U5.png | a94499acb5ca70578307a61f623d1fd0 | generated E1: WORLD + 3 sheets + text | LOCKED after eye QC |
| PNL-PEAK-U6.png | c1056f71a4cf38cb5f6b65e815ce8fde | generated E1: WORLD + 3 sheets + text | LOCKED after eye QC |
| PNL-SHELF.png | d1406b43f36fb9e7fe2536426cef52ee | generated E1: WORLD + text (CCTV) | LOCKED after eye QC |
| PNL-JOINT-U1..U5 | (logged in TAKE_HISTORY.md) | harvested per J4 from conformed segments | at assembly |

## Panel eye-QC notes
- WORLD: bone counter, ink wood, door + brass bell left, big ledger on stand,
  shelves, warm practicals, cadmium lamp accent; the in-world board body reads
  as two dark blank shuttered windows over the counter — blank ✓. No text ✓.
- PLANNER sheet: three views consistent with the locked sheets' format;
  rust-red coat, tight bun, folder, flat deadline face. Caption strip baked
  into the sheet margins (conditioning only; never a video input).
- PEAK-U1 = the BLAM frame: door mid-slam, bell swinging, umbrellas crashing
  across the counter, Clerk looking up (cobalt fingertips visible), Counter
  catching a sliding umbrella by the handle. Rain-wet load.
- PEAK-U2: rows laid, Planner's palm on a BLANK receipt, Counter mid-count.
- PEAK-U3: Counter laying batch two; Planner leaning in mid-accusation;
  Clerk at frame right, cobalt fingertips on the counter.
- PEAK-U4: recount — both pairs of hands in the rows; Clerk centered, severe.
- PEAK-U5: book close angle — Clerk's cobalt fingertips flat on the closed
  book; Planner's hands laying the paper down; Counter's head at frame edge.
  Nit: the paper shows faint illegible marks (face-down intent imperfect;
  illegible at phone size — logged, not a gate).
- PEAK-U6: Clerk centered, open book, facing camera (the freeze target);
  Counter turned to the shelf, finger raised; ONE black umbrella standing on
  the shelf, handle up, legible ✓ (matches LEDGER §5 shelf state).
- SHELF: CCTV fisheye corner angle; exactly ONE black umbrella standing on
  the long shelf, handle up; no people, no text ✓.

## Combined-anchor compliance (script law + slate flag)
Every unit is anchored on a combined panel: PEAK-U1 and PEAK-U5 are combined
three-character panels and ride the two fresh calls together with the Clerk's
CHAR sheet (16:9). Chain units (U2/U3/U4, U6) inherit all faces through the
resume chain from combined-anchored parents; each also has its own gated
PEAK panel as design anchor and refire fallback. The Clerk's sheet rides
every fresh call (inside a resume call there is no image slot — the sheet
rides the chain through the parent take, E2 precedent).

## Joint classification (J1 — all five boundaries)
All JOINT. One continuous space (the shopfront office), one continuous cast,
continuous carry (the umbrella load, the rows, the receipt, the book, the
count itself). No BREAKs; no dissolves (institutional realism). The U4 tail
carries GAP 2 as a designed CCTV shelf insert INSIDE the U4 segment (the
script's named gap carrier), cut on the recount's end — an intra-unit insert,
not a joint.

## Generation routes (J3/J7)
- U1: fresh two-image chain — image 1 = PNL-PEAK-U1 (combined),
  image 2 = PNL-CHAR-CLERK-sheet-16x9.
- U2: resume from U1's snapshot_id.
- U3: resume from U2's snapshot_id.
- U4: resume from U3's snapshot_id. (Chain U1→U2→U3→U4 = J7 max.)
- U5: RE-ANCHOR fresh — image 1 = PNL-PEAK-U5 (combined),
  image 2 = PNL-CHAR-CLERK-sheet-16x9.
- U6: resume from U5's snapshot_id.
Serial discipline: a unit fires only after its upstream take passes QC
(J4: never chain from a rejected take).

## Wordmark gate
UNC is not in this show's cast. E2 ruling carried: NOT TRIGGERED, logged —
the network corner bug (bottom-right, gold, post) carries the wordmark.

## The board (Method C, post)
The count-along promise is carried by the POST board (PIL, deterministic,
FOREST accent, furniture bottom-left), never by generated piles: flips keyed
to MEASURED speech — CLAIMED 31 on the U1 slam (~0.3s) → COUNTED 20 at the
U2 cliff → COUNTED 30 at the U3 tail → U4 recount re-flap stops at 30 →
settle COUNTED 30 | CLAIMED 31 in U6. The U6 cliff question also ships as a
post card over the freeze (script B11).
