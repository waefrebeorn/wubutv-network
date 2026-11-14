# MV-3 QC — Volley 4 rows

Method: faster-whisper base on take audio (RAW words, mishear classes noted);
frames at 2s/5s/8s (widened where reads disagreed: S18 1s/4s/6s/7s/9s for
the head-turn arc); motion from 160x90 gray frame diffs. Near-dup threshold:
mean abs diff <0.5. Frame gate: FAIL if vocal near-dup (<0.5) run ≥24f during
vocal OR vocal mean diff <0.5. Ratio = song slot / take line (first word
onset to last word end). Usable 0.80–1.25; grey 0.60–0.80 / 1.25–1.60
(warp-rescue ≤1.5x to band edge at assembly only — no warping in this
volley); clear miss outside grey. Lyric-sequence gate FIRST (ratio is not
a lyric gate). A take sings its line exactly once — no part of it a
second time (repeat defect = sequence fail, per the MV-2 S22 t2 precedent).
Mishear classes on this track: game=dad, dogs=hooks, see=say. One axis per
reroll verdict.

## S05 t2 — REJECTED, slot STRUCTURAL (pacing axis exhausted, no third pull) [confirmed]
- Lyric sequence: FAIL (repeat defect). Line delivered 0.00–4.72 ("Old man
  on the corner, old man in the room"), then "in the room" re-sung
  5.42–7.06 as a 1.64s tail — part of the line sung a second time.
  Repeat confirmed real, not a Whisper artifact: RMS in the repeat
  window (0.2019) matches first-delivery level (0.2281), vs post-line
  0.0687.
- Ratio: slot 3.18s (L04 36.56–39.74) / line span 7.06s = 0.45 → CLEAR
  MISS. Max 1.5x warp-rescue reaches only 0.68, still below the 0.80
  band edge. (Even the clean first delivery alone, 4.72s, is 0.67 grey
  — the rapid-fire prompt did not compress the line to ~3.5s.)
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; yellow hands, mic on stand (hand on the
  stand, not handheld this time).
- G2 text: PASS. Plain walls, no legible text anywhere.
- G4 performance window: PASS. 2s mouth open mid-line; 5s mouth closed
  to the painted smile in the gap between deliveries (a between-delivery
  beat, not a break); 8s mouth closed post-line, pose held.
- Frame gate: PASS. Vocal mean diff 0.704; longest <0.5 run 5f; <0.1 run 0f.
- Classification: STRUCTURAL per the pace-floor rule. Two pulls on PACING
  (t1 natural pace 6.92s, t2 rapid-fire 7.06s with repeat) both missed
  the 3.18s slot; the measured pace floor (~0.45–0.46x on this density
  class: 10 words in 3.18s) is structural for this modality, not a
  prompting failure to be out-pulled. Assembly treatment (per the
  skill's coverage taxonomy, decided at assembly): cutaway / reaction
  cover while the untouched master audio carries L04 — never stretch
  beyond 1.5x, never freeze during words, never reuse another take's
  mouth for this slot. Recorded arithmetic: 0.45 x 1.5 = 0.68 < 0.80.

## S14 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–7.52:
  "I walk through the speakers, brass hits on the one and the three."
- Ratio: slot 9.24s (L16 99.68–108.92) / line 7.52s = 1.23 → USABLE.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; speaker wall behind him throughout.
- G2 text: PASS. Unbranded speaker wall, grilles carry no legible text
  anywhere.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s/5s; 8s mouth still open 0.48s after line end (7.52) — loose tail,
  assembly trims (same class as volley 3 S13 t1's 0.18s tail).
- Frame gate: PASS. Vocal mean diff 2.277; longest <0.5 run 0f; <0.1 run 0f.
- Notes: no nits. The performed L16 middle ("I sit in the beast that
  they sound" in raw Whisper) is a garble of the sheet slot; the take
  sings the timeline's performed line, which is what the plan prompts.

## S16 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–8.40:
  "Short words, easy words, the kind that sticks fast, I am your dad,
  and the song will last." Whisper hears "will last", matching the
  plan (not the raw-segment "will lead" variant).
- Ratio: slot 7.26s (L18 116.14–123.40) / line 8.40s = 0.86 → USABLE.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; mic on stand.
- G2 text: PASS. Plain walls, no legible text anywhere.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s/5s/8s (line ends 8.40, so 8s is mid-line).
- Frame gate: PASS. Vocal mean diff 1.012; longest <0.5 run 1f; <0.1 run 0f.
- Notes: no nits.

## S17 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.88–6.10:
  "I am your dad, I am your dad, say it with me."
- Ratio: slot 5.16s (L19 123.74–128.90) / line span 5.22s
  (0.88–6.10) = 0.99 → USABLE.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; point at viewer held at 2s/5s, hand
  lowered by 8s post-line.
- G2 text: PASS. Plain walls, no legible text anywhere.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s/5s (2s is a small round "o" speaking-beat shape, 5s the wide
  smile-mouth open); 8s mouth closed to the painted smile post-line.
- Frame gate: PASS. Vocal mean diff 2.166; longest <0.5 run 4f; <0.1 run 0f.
- Notes: no nits. Chorus 2 opens with the escalated point as planned.

## S18 t1 — REJECTED, reroll axis FACING [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–8.94:
  "I am your dad, you're hearing once, you're hearing twice, now it
  lives inside."
- Ratio: slot 7.06s (plan 129.46–136.52; timeline L20 ends 135.80) /
  line 8.94s = 0.79 → GREY (1.01x to 0.80 edge).
- G1 character: PASS on the lock itself. Ball head, small solid black
  oval eyes in the front-facing frames, suit + cadmium tie; mic on
  stand. The 7s frame's half-closed eyes are a blink/speaking beat
  (eyes full ovals at 6s/8s/9s), not drift.
- G2 text: PASS. Plain walls, no legible text anywhere.
- G4 performance window: FAIL (facing). The take plays a head-turn
  arc: 1s/2s/4s/5s all show the head turned away from camera in
  three-quarter-to-profile (far eye foreshortened to a dot), turning
  to front only around 5.5–6s; front-facing with open mouth only at
  6s/7s/8s. The standard 2s/5s/8s samples give 1 of 3 face-to-camera,
  below the 2-of-3 bar — the first ~5.5s of an 8.94s vocal are
  side-angle. Staging noted with the facing miss: both hands come to
  the chest during the vocal (by 6s, inside "twice"/"now") rather
  than after the last word as the vehicle staged it.
- Frame gate: PASS. Vocal mean diff 1.248; longest <0.5 run 1f; <0.1 run 0f.
- Reroll: FACING axis for volley 5 — front, static MCU, head to camera
  for the whole line (no head-turn arc), hands to chest only after
  the last word. If the facing reroll also misses, the slot goes to a
  fresh restage (not a third same-vehicle pull).

## S15 t1 — UNFIRED (generation failure, not a QC verdict)
- The S15 generation call failed with an integrity_check_failed error
  and was NOT retried in this volley, per the standing rule against
  repeating a failed media request with changed arguments. No take
  exists on disk; no QC row applies. S15 is HELD pending a parent
  decision: either a revised vehicle fired as a new request in a later
  volley, or a structural classification (assembly cover, no take).
  It is not counted as rejected and not counted against any reroll
  budget.

## Volley-4 tally
KEEP: S14, S16, S17. REJECTED: S05 t2 (ratio clear miss + repeat defect
→ STRUCTURAL, pacing axis exhausted), S18 t1 (facing miss → FACING
reroll owed, volley 5). UNFIRED: S15 (integrity failure, held for
parent decision — not retried, not rejected).
Pattern: the verse-1/verse-2 density wall now has two structural slots
(S04, S05 — both ~0.45x on 10–11 words in ~3.2–3.6s), while the
longer verse-2 lines (S14/S16/S17, 7–9s slots) all passed clean: no
lyric failures among the keeps, no frame-gate failures, no text
failures, no character drift. The volley's only look miss is S18's
head-turn staging, a first-attempt FACING miss, not a lock failure.
