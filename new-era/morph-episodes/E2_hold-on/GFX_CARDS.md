# GFX CARDS — HOLD ON E2 "Write That We're Married"

Method C devices. One combined graphic layer (Class P, PIL
renderAt(t), 1440 RGBA frames at 1280×720/24fps) + the bug in
the master encode. Chalk is NEVER an overlay on moving
picture — the chalk beats are picture INSERTS cut into the
segments (the wall inserts below), because a guessed
placement on a generated wall is banned and the Split Total
precedent is post-over-blank. The ROOMS sign is painted on
the PANELS in post before generation (the generator never
renders text); the takes inherit it from the panels.

## DEVICE 1 — THE BELL (the town clock) — Class P overlay

The E1 Cull Clock device, unchanged geometry (same town
furniture): segmented ring, 30 segments, outer radius 56px,
stroke 9px, centre (1194, 86) top-right. BONE chalk strokes
with seeded jitter; the currently-spent segment in CADMIUM.
The ring empties over exactly 10.0s (one segment per 8
frames) and SNAPS FULL on every joint frame (full ring +
3-frame settle pulse + cadmium ghost ring) — the snap IS
the bell the script stages (bells in U1, U2, U3, U5 and at
every joint). U1 IGNITION: the ring draws itself on
staggered over frames 5–19 as the hands slam; frame 0
itself carries NO graphic (the picture's own motion opens
the episode).

## DEVICE 2 — THE CHALK INSERTS — Class P picture inserts

Base still: PNL-WALL2-closeup-16x9 (blank brick in the E2
wall's own blue-grey tone, chalk-dust ghosts). Rendered in
PIL at 1280×720 with a hand-chalk texture (seeded jitter,
chalk-white with soft alpha), slow push-in (1.00→1.06
zoompan). Cut INTO the segments picture-only; the take's
audio runs continuous underneath. Placements are scripted
beats, measured against ASR word timings at assembly:

- INS-U1 (~1.3s, after June's "Write us married, or noon
  loses our room." lands): THE WEDDING WALL — the field of
  couples' names already chalked in two-hand spans (pairs
  of names, side by side, weathered chalk at 45% alpha —
  the wall's history). In the main field, one fresh span
  draws on over ~0.8s: **JUNE — ELI**, unmarked. The test
  the episode grades, established in chalk.
- INS-U5 (~2.0s, at the Watcher's chalking beat, after the
  verdict line "Hold held. Wall writes married."): the
  same wall, the same names field. Across **JUNE — ELI**
  the Watcher's chalk draws one long word in two-hand
  span: **MARRIED**. The episode's whole argument in one
  frame.
- INS-U6 (~1.2s, at the Courier's look-to-the-wall beat,
  after her moral lands — placement decided at assembly
  against ASR): the same wall again; **MARRIED** stands
  across the couple's names, finished chalk at 95%; the
  rest of the field unchanged. What the wall keeps.

Chalk text style: DejaVuSans-Bold, chalk white (232,228,218)
with jittered alpha; older names at 45% alpha, fresh work at
95%. No other text appears anywhere in the episode except
the panel-painted ROOMS sign and the bug.

## SIGN PAINT (post, on the panels — pre-generation)

The WORLD panel's hanging sign board — and any PEAK panel
where the board reads — gets **ROOMS** painted in PIL:
hand-painted lettering, warm ink (38,34,30) on the wood
board, grounded to the board's measured bbox in each panel.
Crops read back and verified legible. (DECISION_LOG: the
sign reads ROOMS again — E1's debt paid, the room open.)

## BUG

drawtext `~ WuBu ~`, DejaVuSans-Bold 26px, CADMIUM 0xFFCF3F,
black border, bottom-right (x=w−tw−22, y=h−th−18), full
duration — same expression as the E1 master.

## Loudness

Fixed gain to −20 dBFS median (100ms RMS windows) with a
−1 dBFS limiter, measured on joined.mp4 — same method as
E1. No fade-in (A2 dead head ≤0.2s).
