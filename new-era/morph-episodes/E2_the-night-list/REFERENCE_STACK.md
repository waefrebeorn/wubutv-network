# THE NIGHT LIST — E2 "The Keeper Night" — REFERENCE STACK

Panel Spec v2 + Strong Reference SR1–SR4. Script: SCRIPT.md (LAW, LOCKED).
Inherited identity panels are md5-identical to E1's (verified at copy).
ALL handwriting (board states, floor-rule sign, HELD tag) is composited
in post (PIL plates in work/gfx/), never a generation request.

## Boundary classification

All five boundaries are JOINTs (one hall, one night, continuous time).
No world-swap. Every unit is conditioned on the previous unit's actual
last frame (harvested at frame 228 of the conformed take) as image 1 —
the STRONG REFERENCE: same world state, wardrobe, positions, light.
Cohesion is EYE-verified per joint at QC and logged in work/GATE_LOG.md;
seam MAE is recorded as calibration only, never as the clearing test.

| Joint | Out of → Into | Handoff event (the cut lives inside it) | State carried |
|---|---|---|---|
| J1 | U1 → U2 | The struck name still wet on the board; Laura's bag at the door → UNC stepping into the lamplight with Peter's bag | board struck; Laura at door; rain |
| J2 | U2 → U3 | Peter's bag set outside by the Keeper's hand, blob's sack beside it → the same two bags, Laura looking at them | two bags outside; blob in the wet doorway corner |
| J3 | U3 → U4 | The envelope's edge in UNC's pocket, Keeper turning to the beds → UNC's hand closing on the envelope as he crosses to Bed 10 | Peter's bag alone at the stair foot |
| J4 | U4 → U5 | Laura turning from the door with Elias's bag → the same bag, the same hands, Laura speaking at the door | Bed 10 bare; envelope refused |
| J5 | U5 → U6 | The HELD tag on Bed 10, Elias's bag on the bed, board behind → the same tag, bag and board, held | Bed 10 made + HELD; Keeper desk-bound |

## Rotation (per unit: image 1 = joint/peak, image 2 = peak/anchor)

| Unit | Call shape | Image 1 | Image 2 |
|---|---|---|---|
| U1 | two-image journey | PNL-PEAK-U1 (PIL plate: strike landing on KEEPER, BLAM) | PNL-ANCH-U1 (wide: Keeper at board, Laura at door with the bag) |
| U2 | chain | PNL-JOINT-U1 (U1 conformed frame 228) | PNL-CHAR-BLOB-hero (the invader's entrance is the unit's event) |
| U3 | chain | PNL-JOINT-U2 | PNL-WORLD-night-desk |
| U4 | chain | PNL-JOINT-U3 | PNL-PEAK-U4 (envelope out, Bed 10 stripped) |
| U5 | chain | PNL-JOINT-U4 | PNL-ANCH-U1 (the door + bag composition, re-dressed by the chain) |
| U6 | chain | PNL-JOINT-U5 | PNL-PEAK-U6 (the final tableau) |

## Panel table (all eye-read before use — ref-poisoning rule)

| Panel | md5 | Source / notes |
|---|---|---|
| PNL-CHAR-KEEPER-hero.png | 4cf35e2899c5ea2095b2f713b2d7f1bf | inherited E1, md5-verified |
| PNL-CHAR-UNC-hero.png | 4e552aed3a50db19aa8496ef206d8562 | inherited E1, md5-verified |
| PNL-CHAR-LAURA-hero.png | 4c2159f63ca0b2d0645c0024a719f2fe | inherited E1, md5-verified |
| PNL-CHAR-DISPATCHER-hero.png | e6e6a05ff48369481abac93e0cd038d8 | inherited E1 (Dispatcher does not appear in E2; held unused) |
| PNL-WORLD-night-desk.png | f5624cfc9a79523688e90a868aa06255 | inherited E1, md5-verified |
| PNL-WORLD-roster-room.png | 136b5540e4356e188dce9e66fb303755 | inherited E1 (fallback) |
| PNL-PROP-board-blank.png | 0afd57d94a7bfa6a4db141f5a3bbc032 | inherited E1 — the PIL canvas |
| PNL-PROP-log-blank.png | 867af01b40727e3095f5d273a91b01cc | inherited E1 (unused in E2) |
| PNL-CHAR-BLOB-hero.png | 51311313bf595fb1d37bc1a79b78f081 | NEW — grey-green damp blob, one huge eye, bottle-cap crown slipping, soaked sack; eye-read PASS |
| PNL-ANCH-U1.png | (post-fix md5 in GATE_LOG) | NEW — Keeper at board chalk raised, Laura at door with carpet bag mid-accusation, beds beyond, rain windows; board roster PIL-corrected to canon (raw in work/gfx/ANCH-U1_raw.png) |
| PNL-PEAK-U4.png | a6cae07a80fe71657382cf858f10c4f1 | NEW — UNC holding the envelope out, "~ WuBu ~" glyph-exact in gold, Bed 10 stripped bare at right, sheet on the floor; eye-read PASS |
| PNL-PEAK-U6.png | 3b28b3242470a4b50b62eb936d203c63 | NEW — final tableau: Keeper turning to camera, Elias asleep on Bed 10 with his bag beside it, blob asleep under the stair on a mat, Peter in a wet tan coat outside the door turning away; eye-read PASS |
| PNL-PEAK-U1.png | (PIL plate, md5 in GATE_LOG) | PIL — tight board window, vermilion strike 65% across KEEPER at the foot, dust burst at the tip |

## Post plates (work/gfx/, deterministic PIL — make_plates_E2.py)

- `board_E2_open.png` — 11 names: ANNA · MOSS · JUNE · COLE · RUTH · SOL ·
  LAURA · EMMETT · TESS · HAROLD · KEEPER (foot), unstruck.
- `board_E2_struck.png` — KEEPER struck through in vermilion (U2–U4 state).
- `board_E2_held.png` — ELIAS fresh bright in the foot slot over the
  struck KEEPER ghost (U5 tail / U6 state).
- `board_E2_final.png` — held + KEEPER fresh, squeezed at the very foot
  below ELIAS (U6 freeze state).
- `sign_floor_rule.png` — the painted house sign: figure lying dry on a
  floor under a stair + STAYING AFTER REFUSAL EARNS DRY FLOOR — NO BED ·
  NO NAME.
- `held_tag.png` — the HELD tag card.
- Master overlays: "~ WuBu ~" corner bug bottom-right throughout; the
  chalk-snap accent at 0.25 s (BLAM A3 insurance, disclosed); board/sign/
  tag inserts ONLY if a take's own rendering falls short — decided at QC,
  disclosed either way.
- Disclosed plate nit: the freeze roster in LEDGER §1 omits HAROLD; the
  plates carry E1's board (HAROLD row included) per SCRIPT.md/F-014/
  F-017, which govern the build. The spoken counts are the contract.
