# GFX CARDS — E2 SHOW-2 THE TENTH SECOND (Method C, accent CADMIUM)

All devices Class P (PIL renderAt(t) → RGBA sequence → one overlay
input in the master encode), deterministic, code in work/gfx/.
House law: max two graphic layers + bug per encode — this build
uses ONE combined graphic layer (clock + tally + stamp rendered
into a single sequence) + the bug. Joint Gate runs on the joined
picture BEFORE this composite (Method C §5.5). The `~ WuBu ~` bug
is drawn at the master encode exactly as the pilot's: DejaVuSans-
Bold 26px, CADMIUM 0xFFCF3F, black border, bottom-right
(x=w-tw-22, y=h-th-18), full duration.

## GFX-1 THE CULL CLOCK — invariant (§2.2a)
- Geometry: segmented ring, 30 segments, outer radius 56px,
  stroke 9px, centre (1194, 86) — top-right kit corner.
- Look: chalk texture — BONE strokes, per-segment edge jitter
  (seeded, fixed), chalk speckle; the segment currently being
  spent renders CADMIUM.
- Behaviour: empties over exactly the unit's 10.0s (one segment
  per 8 frames). On every joint frame (first frame of units
  2–6) it SNAPS FULL: full ring + a 3-frame settle pulse
  (scale 1.07→1.00, brightness pop) — the cull's punctuation,
  exactly on the cut (§3.2).
- Unit 1: no event at frame 0 (§3.5 — frame 0 stays the clean
  generated peak). IGNITION inside the first second per the
  BLAM fix menu: segments draw on staggered over frames 5–19
  (0.21–0.79s), arriving already at the count state for that
  instant; the ring then empties normally. Logged in GATE_LOG
  as the U1 graphic event alongside the picture impact.
- Ledger input: none (it is the atom itself).

## GFX-2 THE CHALK TALLY (§2.2c) — placement ruling
- The device's serial function (§3.4) is what ships: tally marks
  accumulating one per unit of the show's whole run. The literal
  wall position varies per generated take and a guessed mid-frame
  placement is banned (§2.2b risk rule), so the tally renders as
  a chalk cluster in the clock's furniture corner, directly
  beneath the ring — fixed geometry, deterministic, legible.
  Deviation from the device letter is logged here and in
  GATE_LOG; the serial arithmetic is exact.
- Look: five-bar-gate tally groups, BONE chalk strokes with
  jitter, group width ~26px, rows under the clock.
- Behaviour: the show's run count — pilot units 1–6 already
  banked. E2 unit k carries the count to 6+k: unit 1's mark
  draws on with the clock ignition (one shared event); units
  2–6 each draw on their mark over frames 5–16 of the unit.
  Unit 6's mark completes the count at 12.
- Ledger input: units elapsed in the show's whole run (6 + k).

## GFX-3 THE STAMP (§2.2b) — one firing
- Fires once: U6, on the carry's state change (the parcel is
  signed and changes hands). Slam timed to the handover frame
  located in QC (default: U6 t≈9.3s if the handover reads
  there; re-timed to the actual frame, never approximate).
- Look: rotated −12°, double-rule rectangular border, CADMIUM
  ink on transparent, tabular bold type: line 1 "CULL 423",
  line 2 "TO THE COURIER". Back-out spring: scale 1.35→1.00
  over 8 frames with a 2° settle; then it rests for the
  remaining frames (a stamp, once down, stays).
- Placement: bottom-left furniture corner (70, 556) — the
  fallback position (§2.2b): the take's parcel position at the
  handover is a two-hand close frame and a guessed on-parcel
  placement is banned.
- Ledger input: cull number 423 (E2 U6's cull; the episode runs
  culls 418–423, one per unit).

## Graphic audit rows (Method C §4.1/§5.6 — answered in GATE_LOG)
Per device: (1) the show's subject / world's instrument? (2)
would exist if nobody spoke? (3) out of the audio channel's
way? Plus: legibility at phone size, arithmetic vs ledger,
frame-0 audit (no event before the U1 ignition at 0.21s, which
is the BLAM-sanctioned early fire — §3.5 tension noted: the
audit's fix menu explicitly orders the device inside 0–1.0s on
U1; frame 0 itself carries no graphic), line-slot audit (no
event starts inside any 7–9s slot except the U6 stamp at the
cliff slot ≥9s, a §3 CLIFF-slot event).
