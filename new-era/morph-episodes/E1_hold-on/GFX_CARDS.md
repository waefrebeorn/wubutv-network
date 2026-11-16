# GFX CARDS — HOLD ON E1 "Write That He Owes Me"

Method C devices. One combined graphic layer (Class P, PIL
renderAt(t), 1440 RGBA frames at 1280×720/24fps) + the bug in the
master encode. Chalk is NEVER an overlay on moving picture — the
chalk beats are picture INSERTS cut into the segments (the wall
inserts below), because a guessed placement on a generated wall
is banned and the Split Total precedent is post-over-blank.

## DEVICE 1 — THE CULL CLOCK (the bell) — Class P overlay

The town's bell made visible; furniture-corner, sound-off
legible, never competes with speech. Geometry inherited from the
E2 SHOW-2 clock (same town furniture): segmented ring, 30
segments, outer radius 56px, stroke 9px, centre (1194, 86)
top-right. BONE chalk strokes with seeded jitter; the
currently-spent segment in CADMIUM. The ring empties over
exactly 10.0s (one segment per 8 frames) and SNAPS FULL on every
joint frame (full ring + 3-frame settle pulse 1.07→1.00 +
cadmium ghost ring) — the snap IS the bell the script stages.
U1 IGNITION: the ring draws itself on staggered over frames
5–19 (0.21–0.79s) as the key is snatched; frame 0 itself carries
NO graphic (the picture's own motion opens the episode).

## DEVICE 2 — THE CHALK INSERTS — Class P picture inserts

Base still: PNL-WALL-closeup-16x9 (blank brick, chalk-dust
ghosts). Rendered in PIL at 1280×720 with a hand-chalk texture
(seeded jitter, chalk-white with soft alpha), slow push-in
(1.00→1.06 zoompan). Cut INTO the segments picture-only; the
take's audio runs continuous underneath. Placements are scripted
beats, measured against ASR word timings at assembly:

- INS-U1 (~1.3s, after Rosa's "Write it: Bruno owes me three
  months." lands): the wall's left edge carries the older docket
  lines — small, weathered, numbered 1–9, faint (the feature is
  established here, per the script's staging note). In the main
  field, fresh chalk draws on over ~0.8s: **BR—** — and stops.
  The half-stroke stays unfinished all episode.
- INS-U5 (~2.0s, inside Rosa's scripted silent read, between
  "Line nine." and "Struck when your ring vanished."): same
  wall, same left-edge lines. Line nine sits in the main field,
  struck through with one hard chalk line:
  **BRUNO OWES ME THREE MONTHS** — and beside it the unfinished
  **BR—** from U1. The episode's whole argument in one frame.
- INS-U6 (~1.5s, at Laura's writing beat, after the ring is
  seen): fresh chalk draws on: **PAID. ASK HIS HAND.**

Chalk text style: DejaVuSans-Bold, chalk white (232,228,218)
with jittered alpha; older lines at 45% alpha, fresh lines at
95%. No other text appears anywhere in the episode.

## BUG

drawtext `~ WuBu ~`, DejaVuSans-Bold 26px, CADMIUM 0xFFCF3F,
black border, bottom-right (x=w−tw−22, y=h−th−18), full
duration — same expression as the E2 master.

## Loudness

Fixed gain to a −20 dBFS median target with a −1 dBFS limiter,
measured on the master (E2 recipe). No fade-in, ever.
