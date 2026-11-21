# BIG PRIMARY COLOR — the Era II design language

Owner order 2026-10-21: *"use big primary color designs."* This file is the
binding interpretation. Every Era II prompt carries it as a **STYLE IS
LOAD-BEARING** clause, the same way the wordmark gate is carried.

## The principle

The frame must read as a **flat colour diagram** before it reads as a picture.
If you squint and the image turns to mush, the frame is wrong. Colour is
**information**, not decoration: a hue that changes means an object changed, and
in a serial an object changing is a plot event.

## The palette — six colours, no more

| Name | Hex | Job |
|---|---|---|
| **COBALT** | `#1B3FD1` | architecture: set walls, doors, the desk body, the ledger cover |
| **VERMILION** | `#E23A1B` | the object under dispute: the tray, the stamp pad, the second card's edge |
| **CADMIUM** | `#FFC61E` | light, authority and the wordmark: UNC's `~ WuBu ~`, the stamp handle, the pool of light |
| **BONE** | `#F4EEDC` | paperwork: cards, forms, pages. The blank is bone — never pure white |
| **INK** | `#141414` | line work, UNC's hoodie, all typography |
| **FOREST** | `#1E4D33` | **Laura only** — cast lock exception, the single non-primary note in the palette |

FOREST is the one permitted exception and it exists because the canon already
locks it (Laura's unlettered forest-green hoodie). It is not a licence to add a
seventh colour. Anything else in frame must be one of the five above.

## Composition rules

1. **Two primaries maximum per frame**, plus BONE and INK. Never three.
2. **60/30/10 weight:** one dominant field, one supporting field, one accent.
   A frame with equal areas of cobalt and vermilion is a failed frame.
3. **Flat fills only.** No gradients, no glow, no bloom, no pastel, no neon, no
   photographic shading, no film grain, no lens flare. The only permitted
   gradients are the two-step (not smooth) shadow bands on painted surfaces.
4. **Ink outlines on every edge**, constant weight. Colour never substitutes for
   a line.
5. **Backgrounds are colour fields, not rooms with props.** A wall is a cobalt
   plane; a doorway is a vermilion rectangle. Detail is earned by the beat, never
   sprinkled.
6. **No colour drift within a serial.** The tray is the same vermilion in unit 1
   and unit 8 to the hex. Colour continuity is a QC gate (frame-diff the sampled
   hue, tolerance ±4 per channel), the same class of check as the wordmark gate.

## Character and prop keys (fixed for the whole serial)

| Element | Colour key |
|---|---|
| UNC | INK hoodie, CADMIUM wordmark `~ WuBu ~` and CADMIUM stamp handle in hand |
| LAURA | FOREST hoodie, bare hands, CADMIUM pool of light on her side of the frame |
| THE PIPS | CADMIUM only — it may never appear in any other hue |
| The lost-and-found tray | VERMILION body, INK rim |
| The blank cards | BONE, COBALT rule line, no lettering unless the allowlist says otherwise |
| The stamp | COBALT body, CADMIUM handle, VERMILION pad |
| The ledger / file box | COBALT cover, BONE pages |
| Set walls (ORIGINALS desk) | COBALT |
| Doorways and thresholds | VERMILION |

## What the palette is FOR in a soap opera

The fruit-soap engine is **status anxiety about an object**. Big primaries make
status legible at thumbnail size, which is where this content actually lives:
- The **count** is the only thing that changes across the arc, so the cards are
  the only repeated BONE shapes — the audience learns to count them subconsciously.
- Every escalation gets a **new colour field** (Act 1 cobalt room, Act 2 the
  vermilion threshold, Act 3 the ink-black night audit) so a viewer who dropped in
  at unit 6 knows where they are in the story from the colour alone.
- The **cliff** is always the same composition: the object held in the lower
  third against a drained field, 0.5 s. Recognisable as this serial's button.

## QC gates (added to the standing unit gates)

- Palette audit per unit: sample 12 frames, count distinct hues; **fail if more
  than six clusters** or if any hue is outside tolerance of the six above.
- Dominant-field check: the top hue covers ≥45% of frame area.
- Tray hue constant vs unit 1 within ±4/channel.
- No-gradient check: reject a take whose flat region shows a smooth ramp (a
  because-there-was-light gradient is a re-fire, not a note).
