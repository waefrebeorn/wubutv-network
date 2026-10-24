# 04 — THE NEW PRODUCTION GRAMMAR (replaces the esoteric canon)

Owner order, 2026-10-21: *"do not write any more esoteric slop … we are now in the
algo maxxing — each 10 seconds being story parts."* This is the CEO Director's
binding rewrite. Where it contradicts earlier doctrine documents, **this wins**.

## The kill list (retired, not deleted)

| Retired | Why it dies |
|---|---|
| Blank-card / unfiled-claim serial engine | nobody arriving cold understands it; zero hook in the first 1.5 s |
| Paperwork as the plot | a form changing is not a story event to a stranger |
| "Melodrama at full gravity over an object that doesn't deserve it" | clever once, then it is a smirk; it cannot carry a chain of parts |
| No-dialogue units | dialogue is native audio now on every major model; refusing it throws away the cheapest hook |
| Deadpan-only cast (UNC never reacts) | a cast with no reactions has no engine; Laura being *the only reactor* was a workaround, not a design |
| Abstract motifs (the Kept Gap, the Framed Blank) | unreadable at thumbnail size, unsearchable, unmemorable |
| Title cards / serial cards / slates on screen | a 10-second part has no room for a card; the card is the first thing that gets scrolled |

**Kept:** the words (`~ WuBu ~` wordmark), the ledger discipline, the coherence
contract, one callback max, native audio, cast lock, and the archive. Craft rules
survive; the sensibility changes.

## What a part is now

A **story part**, not a "bumper". Ten seconds, five beats, fixed grid:

```
0.0-1.5 s  HOOK FRAME   the single most legible image; a question the viewer
                        needs answered; no card, no fade, no wide
1.5-4.0 s  STATE        who wants what, where - shown in ONE action
4.0-7.0 s  TURN         the thing changes (object moves, person enters, count
                        is wrong, someone is caught)
7.0-9.0 s  LINE/SOUND   one utterance or one hard sound that reframes the turn
9.0-10.0 s CLIFF FRAME  the withheld fact, held; THIS FRAME IS THE NEXT PART'S
                        HOOK FRAME (first-frame chaining)
```

Non-negotiables that come from the retention data (see `03_ALGO_MAX_10S_STORY.md`):

1. **A visible change every 1.5 s.** The median retention curve loses 47% in the
   first 1.5 s; the part must already be moving.
2. **The hook frame works alone.** Cold-seeded viewers arrive mid-chain (Shorts
   seeding is 50–500 viewers, ~70% non-subscribers).
3. **Shipping unit = 3–4 parts = 30–45 s.** Ten seconds alone cannot clear a
   watch-time gate (≈65% AVD needed sub-30 s; 15 s Shorts collapsed in 2026).
4. **One withheld fact per part**, spent by the next.
5. **No part requires the previous part.** Continuity is a reward, never a toll.

## Visual system: BIG PRIMARY, kept but simplified

From `wuBuTV notes/PRIMARY_COLOR_DESIGN.md`, unchanged in palette, simplified in
use: **two primaries + bone + ink per frame**, flat fills, ink outline on every
edge. The palette now carries **story information**, not mood:

- **one character = one hue** (the moment a character owns a colour, a viewer can
  identify them at thumbnail size with no dialogue)
- **the antagonist's colour enters the frame before the antagonist does**
- **the cliff frame drains to one hue** so the chain reads as a chain

## The show: "THE STATION" (season 2 engine, replacing the serial line)

Accessible, funny, character-driven, and built on assets we already have. A
sitcom in a failing AI television station that must earn one viewer (and, not by
coincidence, one advertiser).

**Cast (fixed, all legacy, all now allowed to react):**

| Character | Job | Engine | Primary |
|---|---|---|---|
| **UNC** | station manager | deadpan is now a *choice* he uses under pressure, not a rule | INK + CADMIUM |
| **LAURA** | new hire, the audience's eyes | reacts, asks the dumb question the viewer needs asked | FOREST |
| **THE COLONEL** | anchor, on air forever, nothing to read | catastrophises | COBALT |
| **PETER** | sales, enthusiasm with no evidence | promises what the station cannot do | VERMILION |

**The engine of every part:** a promise is made, the station cannot keep it, and
the failure is funnier than the promise. That is a *sitcom* engine — repeatable
forever, legible in one frame, and it never needs the audience to know any lore.

**Season shape:** 12 pieces × 3 parts (36 parts) = 6 minutes of finished story,
shipped as 12 × 30 s Shorts/Reels plus one 6-minute cut. Every third part ends on
a cliff that the next piece's first frame answers.

## Prompt rules for the factory (delta from current practice)

- Dialogue is **expected**: one line per part, inside 7.0–9.0 s, written to be
  understandable with the sound off *and* funny with it on.
- **Negatives per model** (Higgsfield school): `NO fisheye, NO plastic skin, NO
  commercial gloss, NO on-screen text, NO title cards`.
- **Camera moves once per part**, named explicitly (push-in, whip pan, snap zoom,
  dolly left) — movement is part of the 1.5 s change rule.
- **Beat labels in the prompt** (`(0-1.5s) (1.5-4s) (4-7s) (7-9s) (9-10s)`) —
  Vidu-style labelling is the native way to get pacing from these models.
- **Reference frames**: the cliff frame of part N is passed as the **first-frame
  image** of part N+1. This is the continuity stack (Seedance/PixVerse/Hailuo all
  describe it) and it is what makes a chain look shot rather than sampled.

## What I am NOT doing

- I am not deleting the archive, the ledger, or the existing serial. They stay as
  catalogue. `SERIAL-1` finishes or is filed — the Producer decides which, on the
  record.
- I am not asking permission to change the sensibility. The owner ordered it.
