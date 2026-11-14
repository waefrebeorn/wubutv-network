# MV-3 QC — Volley 3 rows

Method: faster-whisper base on take audio (RAW words, mishear classes noted);
frames at 2s/5s/8s (widened where reads disagreed: S08 1s/1.5s/2.5s/3s for
the 2s half-closed-eye frame); motion from 160x90 gray frame diffs. Near-dup
threshold: mean abs diff <0.5. Frame gate: FAIL if vocal near-dup (<0.5) run
≥24f during vocal OR vocal mean diff <0.5. Ratio = song slot / take line
(first word onset to last word end). Usable 0.80–1.25; grey 0.60–0.80 /
1.25–1.60 (warp-rescue ≤1.5x to band edge at assembly only — no warping in
this volley); clear miss outside grey. Lyric-sequence gate FIRST (ratio is
not a lyric gate). A take sings its line exactly once — no part of it a
second time (repeat defect = sequence fail, per the MV-2 S22 t2 precedent).
Mishear classes on this track: game=dad, dogs=hooks, see=say. One axis per
reroll verdict.

## S04 t2 — REJECTED, slot STRUCTURAL (pacing axis exhausted, no third pull) [confirmed]
- Lyric sequence: FAIL (repeat defect). Line delivered 0.00–5.12 ("I've
  been here the whole time, kid, looking right at you"), then "looking"
  repeated 5.48–7.20 as a 1.72s tail — part of the line sung a second time.
  The take again smooths performed "I been" to "I've" (same one-word
  contraction variant as t1, noted, not a wrong line).
- Ratio: slot 3.56s (L03 32.16–35.72) / line span 7.20s = 0.49 → CLEAR MISS.
  Max 1.5x warp-rescue reaches only 0.74, still below the 0.80 band edge.
  (Even the clean first delivery alone, 5.12s, is 0.70 grey — the brisk
  prompt did not compress the line to ~4s; the repeat tail is what the
  model spent its extra time on.)
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; yellow hands, open palms.
- G2 text: PASS. Doorway, plain walls, no legible text anywhere.
- G4 performance window: PASS. 2s mouth open mid-line, lean + open palms;
  8s mouth closed to the painted smile, lean held.
- Frame gate: PASS. Vocal mean diff 2.273; longest <0.5 run 2f; <0.1 run 0f.
- Classification: STRUCTURAL per the pace-floor rule. Two pulls on PACING
  (t1 natural pace 7.58s, t2 brisk 7.20s with repeat) both missed the
  3.56s slot; the measured pace floor (~0.46–0.49x on this density class:
  11 words in 3.56s) is structural for this modality, not a prompting
  failure to be out-pulled. Assembly treatment (per the skill's coverage
  taxonomy, decided at assembly): cutaway / reaction cover while the
  untouched master audio carries L03 — never stretch beyond 1.5x, never
  freeze during words, never reuse another take's mouth for this slot.
  Recorded arithmetic: 0.49 x 1.5 = 0.74 < 0.80.

## S05 t1 — REJECTED, reroll axis PACING [confirmed]
- Lyric sequence: PASS. "Old man on the corner, old man in the room"
  0.00–6.92, exactly once.
- Ratio: slot 3.18s (L04 36.56–39.74; plan slot 3.44s) / line 6.92s = 0.46
  (0.50 on the plan slot) → CLEAR MISS, outside grey. Max 1.5x
  warp-rescue reaches only 0.69, still below the 0.80 band edge. Same
  density class as S04: 10 words in 3.18s; the take sang at natural pace
  despite the brisk window prompt (all ten words inside the first four
  seconds was requested; the model delivered in 6.92s).
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; yellow hands.
- G2 text: PASS. Quiet street corner, plain building walls, doorway, no
  shops, no signs, no neon, no legible text anywhere.
- G4 performance window: PASS. 2s/5s mouth open mid-line, mic on stand
  with hand on the stand (not handheld this time); 8s mouth closed to
  the painted smile post-line, held pose.
- Frame gate: PASS. Vocal mean diff 0.888; longest <0.5 run 5f; <0.1 run 0f.
- Reroll: PACING axis for volley 4 — prompt the 10-word line briskly
  (rapid-fire delivery, all words inside ~3.5s), performed wording
  verbatim. If the pacing reroll also misses, the slot goes STRUCTURAL
  per the pace-floor rule (assembly cover, no third pull).

## S06 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Both lines exactly once, in order, 0.00–8.10:
  "You walk by, you scroll by, you turn the radio on" 0.00–4.16, "And the
  voice in the speaker says the same thing all along" 4.16–8.10.
- Ratio: slot 7.54s (L05+L06 40.06–47.60) / line 8.10s = 0.93 → USABLE.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; wall speaker in frame behind him.
- G2 text: PASS. Hallway, plain walls, unbranded speaker, no legible
  text. (A noticeboard at the far right edge carries blurry rectangles,
  illegible at full resolution — same ruling as volley 2 S11's framed
  picture: illegible, not a fail.)
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s/8s, mid-shape at 5s; speaker gesture pre-line per the vehicle.
- Frame gate: PASS. Vocal mean diff 2.247; longest <0.5 run 0f; <0.1 run 0f.
- Notes: mic is handheld at 5s/8s (hand grips the mic, not the stand) —
  same disclosed nit class as volley 2 S02 t2, not a fail.

## S07 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Both lines exactly once, in order, 0.00–8.96:
  "I raised you in the dark, I raised you in the light, I raised every
  face that is listening tonight."
- Ratio: slot 7.02s (L07+L08 48.12–55.14) / line 8.96s = 0.78 → GREY
  (1.03x to 0.80 edge).
- G1 character: PASS. Ball head, small solid black oval eyes (white dots
  are specular highlights on black ovals, not sclera), no white showing;
  suit + cadmium tie.
- G2 text: PASS. Living room, warm lamp light, framed pictures and book
  spines all illegible, no legible text anywhere.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s/5s/8s (line ends 8.96); warm light present throughout the samples
  (the pre-line light rise itself is not sampled — not a gate).
- Frame gate: PASS. Vocal mean diff 0.899; longest <0.5 run 9f; <0.1 run 0f.
- Notes: mic is handheld in all samples — same disclosed nit class as
  volley 2 S02 t2, not a fail.

## S08 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. "You don't have to like it, you don't have to
  stay, but the words keep coming and they won't go away" 0.00–7.20,
  exactly once.
- Ratio: slot 7.06s (L09 55.14–62.20) / line 7.20s = 0.98 → USABLE.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; yellow hands, open palms. The 2s frame's
  half-closed eyes were widened (1s/1.5s/2.5s/3s all show full ovals):
  a single-frame mid-blink/speaking-beat artifact, same ruling as
  volley 2 S02 t2 — not drift.
- G2 text: PASS. Living-room doorway, plain walls, framed picture
  illegible, no legible text anywhere.
- G4 performance window: PASS. Lean + open palms through the line, mouth
  open mid-line at 2s/5s; 8s mouth closed to the painted smile post-line,
  shrug held.
- Frame gate: PASS. Vocal mean diff 2.097; longest <0.5 run 1f; <0.1 run 0f.

## S13 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Both lines exactly once, in order, 0.00–7.82:
  "You got your real one maybe, or maybe you don't" 0.00–4.72, "Matter
  to me, the message is the point" 5.00–7.82.
- Ratio: slot 8.34s (L14+L15 90.66–99.00) / line 7.82s = 1.07 → USABLE.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; lean + open palms.
- G2 text: PASS. Doorway, plain walls, no legible text anywhere.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s/5s; 8s mouth still open 0.18s after line end (7.82) — loose tail,
  assembly trims.
- Frame gate: PASS. Vocal mean diff 1.442; longest <0.5 run 7f; <0.1 run 0f.
- Notes: two disclosed nits, both color-rendering classes seen before,
  not fails — (1) mouth renders as full red lips vs the yellow/dark
  mouths of the other takes (stronger than volley 2 S11 t2's reddish-pink
  nit, same axis; face lock otherwise exact); (2) hands render
  flesh-toned vs yellow in other takes (same class as volley 2 S03's
  dark-hands nit). If the parent wants strict mouth/hand-color
  matching, this is the take to restage — but neither class has ever
  been a fail, and the face lock is exact in all samples.

## Volley-3 tally
KEEP: S06, S07, S08, S13. REJECTED: S04 t2 (ratio clear miss + repeat
defect → STRUCTURAL, pacing axis exhausted), S05 t1 (ratio clear miss →
PACING reroll owed, volley 4).
Pattern: the verse-1 density wall is real. S04 (11 words / 3.56s) and S05
(10 words / 3.18s) are the two densest lyric slots so far, and both
missed on pace despite brisk-window prompting — the tool's pace floor
(~0.46–0.49x on this class) holds across two different axes of attack
(natural pace, brisk prompt). S04 is now structural; S05 gets its one
pacing reroll. Everything else in the volley passed clean: no lyric
failures among the keeps, no frame-gate failures, no text failures,
no character drift (S08's 2s eye read resolved by widening, S13's color
nits disclosed, not failed).
