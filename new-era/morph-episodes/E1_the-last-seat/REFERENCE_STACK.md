# REFERENCE STACK — THE LAST SEAT E1 "Night One: The Woman with the White Stub"

Declared BEFORE firing, per bible §6 + Panel Spec v2 + the pilot/E2 lessons.
SCRIPT.md is law; this stack implements it. Joints are declared BREAKs at
production, as E2 ran them (script production note 8).

## KIT — carried from E2_SHOW-5 (md5-locked, verified byte-identical 2026-11-16)

| Panel | md5 | Role |
|---|---|---|
| PNL-CHAR-DANCER-hero.png | 31a99dcbe7384e01aab4e4cb4547868e | Dancer identity (hero) |
| PNL-CHAR-DANCER-face.png | 51317c369344a215d76a84e8ce59ecf8 | Dancer identity (face) |
| PNL-CHAR-USHER-hero.png | 0aaca18f385d3ab8988261ac4bae039b | Usher identity (hero) |
| PNL-CHAR-USHER-face.png | 22be47a3d3c03903f56f26429e8d47f0 | Usher identity (face) |
| PNL-PROP-seat.png | 9a5e660a77943c6125413145a9b1a2b9 | THE seat — the house's constant |
| PNL-WORLD-seatroom.png | b44bbe1dbf3deb27c97fd0cb3d3f6386 | House world (carried, not fired this episode) |

## NEW THIS EPISODE (generated + eye-gated 2026-11-16)

| Panel | md5 | Gate read |
|---|---|---|
| PNL-CHAR-OCCUPANT.png | 6b99de741aa13c7c4568a6ce69879436 | PASS — back/side silhouette in the seat: wide hat, dark coat, black gloves, programme, brass reading lamp on the arm; face fully shadowed, never visible. The identifier anchor that makes the rotating stranger castable. |
| PNL-PEAK-U01.png | 21de722fc056b9202a51f8846c9c225d | PASS (v2) — from behind the hat: the Occupant IN the lamp seat, programme in gloved hands, lamp lit; the Dancer mid-split-leap in the shaft. v1 REJECTED (occupant sat beside an empty lamp seat — premise violation), kept at work/stills/PNL-PEAK-U01-v1-rejected.png. Nit: a shadowed sliver of her profile at the hat's edge — never front-lit; disclosed. |
| PNL-PEAK-U02.png | 4b90fc81d5410a9c4e95143d2b979103 | PASS — blank white stub large on the brass armrest (foreground perspective; phone-legible), Occupant seated with programme, Dancer mid-phrase on stage, Usher crossing soft-focus with white gloves, lamp dark. |
| PNL-PEAK-U03.png | bb5d6db62f9d2b4b2ec97e73da69f070 | PASS — box-office counter: Usher's white gloves turning the huge book's page in the lamplight, Dancer leaning in; pages blank. |
| PNL-PEAK-U04.png | 9877dcb255a84755006169bc31020518 | PASS — Usher reading the book aloud in the light; Dancer turned toward the house; the hat in the foreground seat, lamp glowing warm. Nits: Dancer stands in the aisle rather than at his shoulder; a shadowed profile sliver under the hat. Disclosed. |
| PNL-PEAK-U05.png | 56765067cad68b96fb8a9c467f6004c9 | PASS — the Dancer's proud opening pose in the shaft, gaze out at the seat; the Occupant's silhouette with programme half-lowered, lamp warm. |
| PNL-PEAK-U06.png | 214d021c7b00a2b168df4f79a154e054 | PASS — the tell staged BIG and singular (slate §5): brass cap large in frame, shoe raised mid-tap above it, gloved hand spread conducting, programme edge in the other hand, lamp warm, Dancer blurred beyond. Nit: the shoe reads as a lace-up oxford at still scale; disclosed. |

## LOOK BLOCKS (verbatim in every prompt)

- THE DANCER — adult woman in her late twenties, dark hair in a tight bun,
  deep vermilion sleeveless stage dress with a SHORT swirling skirt, soft
  dance shoes, athletic build, focused expression. (SCRIPT-locked look;
  supersedes the E2 gown drift.)
- THE USHER — tall thin man in his late fifties, slicked-back grey-streaked
  dark hair, long ink-navy usher's coat with brass buttons, white gloves,
  thin deadpan face, calm unsmiling expression.
- THE OCCUPANT — a woman in the front-row critic's seat, seen only in
  shadow: wide dark hat, dark elegant coat, gloved hands, a theatre
  programme; her face is NEVER shown or front-lit — hat, gloves, programme
  and the seat's reading lamp are her identifiers.
- THE SEAT — one old cinema seat, faded vermilion velvet, brass armrest
  caps, worn, with a small reading lamp on its arm.
- UNC does not appear in this show (script). The "~ WuBu ~" wordmark rides
  as a post corner bug only — no in-generation text anywhere; the book,
  programme, stub and lease notice all stay blank/unreadable by prompt law.

## ROTATION (image 1 = the unit's PEAK panel — the anchor; image 2 = CHAR)

| Unit | Image 1 (PEAK) | Image 2 (CHAR) | Declared joint-in |
|---|---|---|---|
| U1 | PNL-PEAK-U01 | PNL-CHAR-DANCER-hero | — (frame 0 IS the leap, from behind the hat) |
| U2 | PNL-PEAK-U02 | PNL-CHAR-DANCER-face | BREAK — declared match: the seat + the Occupant's gaze on the stage |
| U3 | PNL-PEAK-U03 | PNL-CHAR-USHER-face | BREAK — declared match: the book, carried from the aisle to the counter light |
| U4 | PNL-PEAK-U04 | PNL-CHAR-USHER-hero | BREAK — declared match: the seat + the Dancer's gaze page→hat |
| U5 | PNL-PEAK-U05 | PNL-CHAR-DANCER-hero | BREAK — declared match: the seat + her gaze held on the hat |
| U6 | PNL-PEAK-U06 | PNL-CHAR-OCCUPANT | BREAK — declared match: the seat, the brass cap, the lamp warm |

## POST GRAPHICS (Method C, per script — the only graphics this episode)

1. "~ WuBu ~" corner bug, bottom-right, every frame (PIL-drawn, as E2).
2. THE QUESTION card at the U6 freeze: "WHO IS THE WOMAN IN SEAT ONE?"
   bone-white serif, centre frame, faded in over the frozen final frames
   of U6 (the freeze is GAP 3's carrier — built in post by holding the
   take's frame from ≈57.5s; card fades in ≈57.7s and holds to 60.0s).

## GAP CARRIERS (script §A2 — verified at master QC, disclosed as measured)

- GAP 1 (after U2's turn): the non-applause — U3's head at the counter
  before its first line; the held wide nobody applauds into.
- GAP 2 (after U4's peak turn): the held look — U5's head: the house
  dropping to dark and the Dancer beginning, before her U5 call.
- GAP 3 (final 2–3s of U6): the freeze + the question card (post-built,
  above — the one gap whose carrier is guaranteed by construction).
