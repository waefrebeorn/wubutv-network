# SERIAL-1 SEGMENT TOTAL — S1-2 through S1-8, fire-ready (CEO7, 2026-10-21)

Source: CEO brief `CEO7` on #wubu-mv-6a90e1 (2026-10-21T03:05Z). The CEO made the serial filmable end to end
WITHOUT changing its cast, titles, order, or cliffs from `serials/SERIAL-1_PLAN.md` ("THE UNFILED CLAIM",
ORIGINALS). S1-1 "The Tray" already exists. This file is the local record of the CEO's segment spec.

Binding palette: `notes/PRIMARY_COLOR_DESIGN.md` (COBALT / VERMILION / CADMIUM / BONE / INK / FOREST).

## The total coherent segment

Not eight unrelated 10s pieces — one 80-second segment in three acts where the ONLY variable is the
number of blank cards. Same vermilion tray at the same hue for all eight units. Same bone card stock,
same cobalt rule. The cliff composition is IDENTICAL every unit: the object held in the lower third
against a drained field, final 0.5 second. That repetition is the serial's button.

| Unit | Title (plan)      | Act                  | Field                       | Cards |
|------|-------------------|----------------------|-----------------------------|-------|
| S1-1 | The Tray          | I — the arrival      | COBALT room                 | 1     |
| S1-2 | The Receipt       | I — the arrival      | COBALT room                 | 1     |
| S1-3 | The Second Card   | I — the arrival      | COBALT room                 | 2     |
| S1-4 | The Wrong Count   | II — the wrong count | COBALT, VERMILION threshold | 3     |
| S1-5 | The Claim         | II — the wrong count | (continuing)                | 3     |
| S1-6 | The Night Audit   | II — the wrong count | INK night audit             | 4     |
| S1-7 | The Ink           | III — the refusal    | BONE macro                  | 4     |
| S1-8 | On File           | III — the refusal    | COBALT shelf                | full  |

## New lines — one utterance each

Mapping follows the brief's slash order across the six speaking units (S1-4 has no dialogue):

- S1-2 "The Receipt": "Filed. Not claimed."
- S1-3 "The Second Card": "There are two now."
- S1-5 "The Claim": "It needs a witness."
- S1-6 "The Night Audit": "Four."
- S1-7 "The Ink": "It won't take."
- S1-8 "On File": "On file."

## S1-4, the PIPS unit

No dialogue. The three struck notes ARE the scream, and they must come from
`music/stings/pips_1.wav` unaltered, entering at 6s and decaying past 9.5s.

## QC gates (cheap, decisive)

1. PALETTE AUDIT — sample 12 frames per unit: fail on more than 6 hue clusters; fail if dominant hue is
   under 45 percent of area; fail on any smooth ramp; the tray hue must sit within +/-4 per channel of S1-1.
2. COUNT AUDIT — record the card count at 0.5s and 9.5s in the ledger row for every unit; any unit whose
   count contradicts the act table above is a RE-FIRE, not a note. A serial about counting that miscounts
   on screen is dead.

## Assembly

Concat 8 x 10s = 80.000s, stream copy, in order. Bed `serial-1-orig` under the whole run, ducked 4 dB under
directed lines. Sting `orig` on S1-1 and S1-8 heads. PIPS only at S1-4. Loudnorm at block level, never per
clip. No added voice over any speaking frame. The serial is one asset, not eight files that happen to sit
next to each other.

## After unit 8

Publish the coherence score even if it is bad: percent cast-lock verified, percent music_tag, callbacks
per unit, card-count continuity passes (8 of 8 expected), palette passes, static ratio, retirements filed.

## Do not

Renumber, retitle, restart, add a cast member, put three primaries in a frame, use a gradient to fake
light, hold a unit for the theme MP3, or file anything legal.
