# MV-7 "I'm The Nobody Man" — COMPLETE REDESIGN v2 (2026-11-06)

Ordered by the user 2026-11-06 ~13:30 EST ("make better prompts and make
better designs — complete redesign in case") while the video pipeline's
safety service is down. v1 (MV_PREPRO_MV-7.md + mv7_s*_vehicle.txt +
refs/nobody_man_canonical.webp) stays on disk untouched as the fallback.
v2 is the build we fire first when video generation returns; the S07
hook test fires with the v2 vehicle + v2 Era A still.

Song, timeline, lyrics, structure are UNCHANGED: LYRIC_TIMELINE.md
(103.36 BPM, hook chant opening, 24 scenes S01–S24, same in/out points).
This redesign is design + prompts only.

## What was wrong with v1 (the honest list)

1. ONE canonical still for all 24 scenes. The choruses ask a sparse-room
   still to become a spark wall — the image conditioning fights the text.
   Identity drifts or the wall never grows.
2. Prompts are long and overloaded: full identity lock + full prop list +
   long negative stack in every vehicle. The signal drowns.
3. Every lyric line is written TWICE in the performance entry ("sings the
   exact words X" + "He sings the line exactly once: X"). Repetition in
   the prompt invites repetition/invention in the take (a defect class we
   have already shipped and QC'd on MV-5/MV-6).
4. Every scene is the same shot: static MCU, locked-off, same desk, same
   glow. Three minutes of one composition. The design has no progression
   except "more sparks" said in words.
5. The character is described generically — "ordinary man, unremarkable
   kind face." A generator cannot hold "unremarkable." Nothing distinctive
   = identity drifts take to take.

## The v2 design — "THE DESK ACROSS THE YEARS"

One room, one man, one candle — but time visibly passes. The video is
the years of posting made visible: the room fills, the candle burns
down, the wall wakes up. The song's escalation (sparks) becomes the
room's aging.

### Character v2 — memorably ordinary

THE NOBODY MAN: a man in his mid-40s, heavy-lidded kind eyes, a crooked
tired grin (left corner lifts higher), two-day stubble, short dark hair
thinning at the crown, a worn charcoal crewneck sweater with a small
frayed patch on the left shoulder, ink-stained fingertips.

Five hard anchors the generator can actually hold: crooked grin (left
side higher) · heavy-lidded eyes · thinning crown · frayed left-shoulder
patch · ink-stained fingertips. Still nobody famous, still no UNC, no
hoodie, no wordmark on him — but now he is SOMEONE specific. The grin is
his signature; the patch is his continuity check in QC tiles.

### The candle is the clock

THE SMALL FLAME stays the motif, but now it MEASURES the years:
- Era A: candle tall and new.
- Era B: candle burned halfway down.
- Era C: candle a low stub — still burning.
A viewer can read the whole story off the candle. QC checks candle
height per era like a continuity prop.

### Three eras, three canonical stills (one per era, not one per video)

- **ERA A — THE BARE ROOM** (S01–S10: intro chant, V1, PC1, C1): bare
  dark wall, one monitor, tall candle, folder stacks low. He is a man
  with a desk and a habit.
- **ERA B — THE FILLING ROOM** (S11–S19: V2, PC2, C2, Bridge): cork strip
  crowded with blank receipt slips, draft drawer half open, first
  clusters of tiny glowing screens on the wall, candle at half height.
  The habit has become a life's work.
- **ERA C — THE KINGDOM** (S20–S24: Final Chorus): the whole wall behind
  him is a field of hundreds of tiny glowing screens like sparks, ONE
  steady light among them a touch brighter (the one viewer), candle a
  low stub still burning on the desk. Quiet triumph, no swell.

Every vehicle is conditioned on ITS era's still. The chorus escalation
is now carried by the image, not begged from the text.

### Camera design v2 — one composition per passage (verses still sustained)

Singing passages stay sustained (edit rule stands: one continuous
picture per passage, warp don't cut) — but each passage owns ONE
composition instead of all sharing one:

- Intro chant (S01–S02): FACE IN THE DARK — tight close-up, phone glow
  from below, room barely there. The chant comes out of the dark.
- Verse 1 (S03–S04): DESK LEAN — the v1 MCU, kept, now Era A.
- Pre-Chorus 1 (S05–S06): MAN + MONITOR — slightly wider; the glowing
  monitor sits in frame like the other half of a duet. First spark
  lights on the wall in S06.
- Chorus 1 (S07–S10): SLOW PUSH-IN — camera creeps a few inches closer
  across the chorus while the first sparks glow behind him.
- Verse 2 (S11–S12): DESK LEAN, Era B — same framing as V1 so the
  room's change reads against his sameness. S12 hand near the flame
  (PC-3) kept.
- Pre-Chorus 2 (S13–S14): MAN + MONITOR, Era B.
- Chorus 2 (S15–S17): SLOW PUSH-IN, Era B — wall clearly filling.
- Bridge (S18–S19): montage as before (hands posting, receipt pinning,
  cable roots, flame carried) + one new shot: OVERHEAD DESK — the desk
  from directly above, years of paper in rings around the keyboard,
  like a tree's rings.
- Final Chorus (S20–S23): THE REVEAL — the one medium-wide of the
  video (Era C, PC-6). S22 holds on the one brighter light.
- Outro (S24): SLOW PULL-BACK to the opening composition — candle +
  phone glow + man at desk, spark wall behind him. Frame rhyme kept.

### Light design v2 (one sentence, every vehicle)

Warm candle amber low from desk level + cool monitor glow across his
face, deep shadow behind him. Two sources, always the same two — the
flame and the screen. That IS the song: the small real light and the
endless posted light.

## Prompt format v2 — leaner and stronger

Three entries per vehicle, same as v1, but cut hard:

- **ENTRY 1 (framing, ≤70 words — the mandated opener + five-anchor lock + light sentence alone run ~56, so 60 proved impossible without dropping a required element):** "16:9 landscape, exactly 10
  seconds." + composition name + the SHORT character lock (the five
  anchors only, one clause) + era tag in words ("bare dark room, tall
  candle" / "cork strip crowded, candle half-burned" / "wall of tiny
  glowing screens, candle a low stub") + the one light sentence.
- **ENTRY 2 (image):** the ERA still (A/B/C), not the single v1 still.
- **ENTRY 3 (performance, ≤70 words):** window (0.5–9.5s) + the line
  stated ONCE + articulation in one clause ("clear open mouth shapes,
  visible jaw, no whispering") + end state in one clause ("mouth
  closes on the last word, held in the crooked grin") + exactly three
  negatives: "No readable text or logos. No other people. No morphing."

Rules: the lyric appears exactly once per vehicle. No prop inventory
(the era still carries the props). No repeated identity essay (the
still + five anchors carry it). Montage vehicles (S18/S19) carry no
singing window — "no face sings in this shot" where faceless.

## QC additions for v2

- Continuity checks per era: candle height (tall/half/stub), patch on
  the LEFT shoulder, grin crookedness. A take in the wrong era state is
  a REJECT, not a note.
- Hook test unchanged in purpose: S07 (v2 vehicle, Era A still) is the
  first fire when the video pipeline returns.

## Files

- redesign_v2/REDESIGN_V2.md — this document.
- redesign_v2/vehicles/mv7v2_s01_vehicle.txt … mv7v2_s24_vehicle.txt —
  all 24 scenes rewritten in the v2 format.
- refs/nobody_man_v2_eraA.webp / eraB / eraC — the three era stills.
- v1 files untouched everywhere else in the project.
