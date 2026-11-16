# THE NIGHT LIST — E1 "The Sol Night" — REFERENCE STACK

Panel Spec v2, inherited from SHOW-3 E2 (the parent room's proven build) and
redressed per SLATE.md §§2/3/5: staging centres the BEDS and the doorway; the
board is the scoreboard; ALL handwriting is composited in post (PIL), never a
generation request. Script: SCRIPT.md (LAW). Room rulings: DECISION_LOG.md.

## Boundary classification

All five boundaries are JOINTs (one room, one night, continuous time). No
WORLD-SWAP anywhere — the swap is a spice this episode never fires; the room
refuses to change while the list does.

| Joint | Out of → Into | Handoff event (the cut lives inside it) | Carrier |
|---|---|---|---|
| J1 | U1 → U2 | Sol's look at the empty bed becomes Laura's look up from her chair — the room's refusal passes from the struck man to the witness | the look |
| J2 | U2 → U3 | The wet strike the Keeper stares at becomes the log page turned to camera — the name hands off to the paper | wet strike → page |
| J3 | U3 → U4 | The log's paper becomes UNC's receipt slips laid on the same desk — paper to paper | the desk |
| J4 | U4 → U5 | RE-ANCHOR (J7 slot): fresh PEAK, no chain — receipts down, chalk up; the Keeper crosses to the board | the crossing |
| J5 | U5 → U6 | The name just written on the board becomes the full board — writing hands off to the count | the board |

## Rotation (per unit: image 1 = joint/peak, image 2 = peak/anchor)

| Unit | Call shape | Image 1 | Image 2 |
|---|---|---|---|
| U1 | two-image journey | PNL-PEAK-U1 (strike landing, BLAM) | PNL-ANCH-U1 (wide entry) |
| U2 | chain | PNL-JOINT-U1 (U1 conformed frame 228) | PNL-PEAK-U2 |
| U3 | chain | PNL-JOINT-U2 | PNL-PEAK-U3 |
| U4 | chain | PNL-JOINT-U3 | PNL-PEAK-U4 |
| U5 | RE-ANCHOR | PNL-PEAK-U5 (single) | — |
| U6 | chain | PNL-JOINT-U5 | PNL-PEAK-U6 |

Joint frames are also harvested from U6's tail for the calibration record.
JOINT GATE per boundary, measured + logged: seam MAE (bar ≤58, 320×180 gray)
and head MAE vs the unit's own BASE; item 6 judged by visible motion in the
first second + logged as calibration data (the ≥8 floor sat above every E2
episode's own BASE — miscalibrated, do not gate on it).

## Panel table (all eye-read before use — ref-poisoning rule)

| Panel | md5 | Source / notes |
|---|---|---|
| PNL-CHAR-KEEPER-hero.png | 4cf35e2899c5ea2095b2f713b2d7f1bf | inherited E2_SHOW-3, md5-verified |
| PNL-CHAR-UNC-hero.png | 4e552aed3a50db19aa8496ef206d8562 | inherited, md5-verified |
| PNL-CHAR-LAURA-hero.png | 4c2159f63ca0b2d0645c0024a719f2fe | inherited, md5-verified |
| PNL-CHAR-DISPATCHER-hero.png | e6e6a05ff48369481abac93e0cd038d8 | inherited, md5-verified |
| PNL-CHAR-SOL-hero.png | 2837d1edb2f54612e63470c5d5b6cc82 | NEW — wet raincoat, grey sweater, duffel in hand; PASS |
| PNL-WORLD-night-desk.png | f5624cfc9a79523688e90a868aa06255 | NEW redress of the roster room: desk + lamp centre, blank board, beds through the door; keeps the inherited TELEVISION STATION CLOSED sign as set dressing |
| PNL-WORLD-roster-room.png | 136b5540e4356e188dce9e66fb303755 | inherited world ref (fallback) |
| PNL-PROP-board-blank.png | 0afd57d94a7bfa6a4db141f5a3bbc032 | NEW — frame-filling board, 11 ruled rows, blank; the PIL canvas |
| PNL-PROP-log-blank.png | 867af01b40727e3095f5d273a91b01cc | NEW — open log, blank ruled columns; the PIL canvas |
| PNL-PEAK-U1.png | 7894a1a6926069bc1f7ff6fdffe1058a | PIL plate: tight board, vermilion strike 65% across SOL, dust burst at the tip |
| PNL-ANCH-U1.png | 60f8e8455f4c37d17de8bc107946526c | NEW — Sol mid-stride in the rain arch, bag swinging, empty bed beside him, Keeper at desk |
| PNL-PEAK-U2.png | 1b0b08c5e2af1c012e2234f9dfa4e4ae | NEW — Laura in the corner chair, blanket + cup, mid-speech |
| PNL-PEAK-U3.png | def672af53017b98691981d99a592c17 | NEW — Dispatcher leaning over the desk, palm flat on the open log; the PIL noon entry survived conditioning and reads on the page |
| PNL-PEAK-U4.png | 7e8095aaf5240ed40aaadcfea17d1c5f | NEW + PIL: UNC in shadow at the right edge laying blank slips; the two slips at his hands marked BED 7 in post ink |
| PNL-PEAK-U5.png | fc13b7268fc83f98e5de3cb6bed1a585 | NEW — Keeper alone at the board, chalk raised at a middle row, Sol's wet bag by the open door |
| PNL-PEAK-U6.png | 78f351f51af44f30c387581183bf5cc0 | PIL plate (= work/gfx/board_stateB): full board, eleven names, SOL fresh bright, KEEPER at the bottom |

## Post plates (work/gfx/, deterministic PIL — make_plates.py / make_log.py / make_receipts.py)

- `board_stateA.png` — full board, SOL struck (U1 tail state / U2 reference / U5 start state).
- `board_stateB.png` — full board, SOL restored fresh (ships as PNL-PEAK-U6).
- `log_page.png` — the day page: NOON column carries "12:00 — SOL struck — U.", NIGHT column blank.
- Board roster, top→bottom (LEDGER §5): ANNA · MOSS · JUNE · COLE · RUTH · SOL · LAURA · EMMETT · TESS · HAROLD · KEEPER.
- U5 name reveal: progressive stroke-by-stroke composite on the take's tail if the board holds steady; fallback = board_stateB insert for the final ~1.5 s of U5 (the joint out IS the written name; U6 opens on the full board). Decided at QC, disclosed either way.
- Master overlays: vermilion strike completion + chalk snap accent at U1 0.0–0.5 s if the take's own strike falls short; question card WHOSE NAME COMES OFF? over the U6 freeze (final 2–3 s); "~ WuBu ~" corner bug bottom-right throughout.
