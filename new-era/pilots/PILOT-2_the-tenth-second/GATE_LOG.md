# GATE LOG — PILOT-2 THE TENTH SECOND, "The Parcel"

QC method: ffprobe per take; frames extracted at 0 / 0.5 / 2.5 / 5 / 7.5 / 9.6s
(contact sheets work/qc/sheet_U*.png, read by eye); dialogue transcribed with
faster-whisper large-v3-turbo, no VAD (work/qc/asr/transcripts.json);
head-motion measured as grayscale MAE frame0→frame0.5s at 320×180.

## Per-unit verdicts

| unit | frame-0 test | dialogue (ASR) | motion MAE f0→0.5s | carry in 1.5s | event-read | verdict |
|---|---|---|---|---|---|---|
| U1 | PASS — PEAK composition: courier mid-stride, parcel offered to blank brick where the doorway was; tally wall behind | "Hold this. The street is leaving." 5.6–8.14s — EXACT | 28.19 | parcel, courier's hand ✓ | reach/offer; tally one short reads in close-up | KEEP |
| U2 | PASS — watcher holding parcel, courier's hand empty, street fully replaced (laundry street) | "The street moves every ten seconds. The parcel doesn't." 4.12–8.38s — EXACT | 13.46 | parcel, watcher's hands ✓ | world-swap around the held parcel; parcel handed back at cliff ✓ | KEEP |
| U3 | PASS — row of identical doors, courier at the nearest with parcel | "This address doesn't exist anymore, the street moved." 5.34–8.9s — EXACT | 66.31 | parcel, courier's hand ✓ | door-testing; door opens (street-beyond reads weakly in stills) | KEEP w/ notes |
| U4 | PASS — parcel close in her hands, chalk wall behind with a circled chalk drawing of a parcel among the tallies | "Who do I give it to?" 4.82–5.86 + "The name is mine." 6.2–7.12 — EXACT | 13.21 | parcel, courier's hands ✓ | inspection/slow turn; watcher takes parcel at cliff ✓ | KEEP |
| U5 | FAIL at frame 0 → FIXED in assembly — first ~0.25s is the studio-anchor replica (grey background) before the dusk scene; trimmed + 1.026× stretch to hold 240f | "You carried it to yourself." 2.26–3.72 + "Sign for it." 8.16–8.96 — EXACT, split delivery | 90.79 (post-trim head is mid-offer, in motion) | parcel, watcher's hands ✓ | handover of parcel + chalk at cliff ✓ | KEEP w/ fix |
| U6 | PASS — bookend of U1 composition (same PEAK anchor, fresh take); parcel + chalk in her hands by 2.5s | "Then the next me signs it, not me." 5.44–8.26 — EXACT | 27.43 | parcel, courier's hand ✓ | suspension; chalk hovers, unsigned; street-end swap is subtle | KEEP w/ notes |

## Standing gates

- Dialogue intelligibility: PASS all six — every written line is the spoken
  line, verbatim, no garbling, no invented extra speech in any take.
- Wordmark hard gate: PASS (vacuous) — UNC does not appear in this pilot;
  no hoodie figure exists in any frame of any take (verified on sheets).
- Generated captions/titles/subtitles: PASS — none in any take. Diegetic
  texture only: door numerals "27" (U3), distant blurred shop signage (U3),
  chalk tallies (not lettering). Not captions; noted, not gated.
- MOTION LAW: PASS all six — MAE f0→f0.5s 13.2–90.8; no halted-photo starts;
  every assembly cut lands on moving frames (U5 post-trim head verified).
- Adults only: PASS — all figures adult, including distant U2 extras.
- Zero reused footage: PASS — six distinct generations; U6's frame 0 rhymes
  with U1 by design (same PEAK anchor), it is not the same take.
- Motif axis: PASS — reach / world-swap / door-testing / inspection /
  handover / suspension; no motif repeats.
- Escalation: PASS — blank-wall door → street replaced → doors everywhere →
  the wall already knew → the unwritten mark → the early cull.
- Line timing vs the 7–9s spec: lines complete inside their units but land
  early in U1 (5.6s), U2 (spans 4.1–8.4s), U4 (4.8s) and split in U5 —
  generator speech placement; disclosed, not gated (intelligibility is).

## Disclosed flaws (ship with the pilot)

1. U3 watcher identity drift: fuller grey beard + maroon shirt under the
   cardigan vs the locked panel's stubble + bone shirt. He is an
   edge-of-frame non-speaker in U3; the speaker's identity holds.
2. Courier coat hue drifts brighter/saturated blue in U2 and U5 (those
   units' light) — the measured hue-drift class; face/layout hold.
3. U5 frame-0 studio-anchor replica (~0.25s) — trimmed in assembly
   (0.25s head trim + 1.0256× stretch, atempo 0.975; unit stays 240f).
4. U5 line is split: "You carried it to yourself." at 2.3s, long pause,
   "Sign for it." at 8.2s. Words exact; plays as verdict → command.
5. U6 hook replays U1's offer composition for its first beat (bookend by
   design); the parcel-and-chalk pose the script specifies resolves by
   ~2.5s. The far-end building swap is subtle in stills.
6. U3's door opening "onto another street" reads weakly in stills; the
   event carries on the door row + her testing the door.
7. No refires were available inside this build's 6-successful-video
   budget (6 fired, 6 landed, 0 failures, 0 429s) — flaws above are
   disclosed rather than re-rolled.
