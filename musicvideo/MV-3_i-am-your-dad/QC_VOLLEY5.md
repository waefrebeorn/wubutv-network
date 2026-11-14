# MV-3 QC — Volley 5 rows

Method: faster-whisper base on take audio (RAW words, mishear classes noted);
frames at 2s/5s/8s (widened where reads disagreed: S18 1s/4s/5.5s/6s/7s for
the facing arc + hands timing; S20 6s/7s for late-line eyes + tail);
motion from 160x90 gray frame diffs. Near-dup threshold: mean abs diff
<0.5. Frame gate: FAIL if vocal near-dup (<0.5) run ≥24f during vocal OR
vocal mean diff <0.5. Ratio = song slot / take line (first word onset to
last word end). Usable 0.80–1.25; grey 0.60–0.80 / 1.25–1.60 (warp-rescue
≤1.5x to band edge at assembly only — no warping in this volley); clear
miss outside grey. Lyric-sequence gate FIRST (ratio is not a lyric gate).
A take sings its line exactly once — no part of it a second time, and no
part of it missing (repeat defect = sequence fail, per the MV-2 S22 t2
precedent; incomplete delivery = sequence fail). Mishear classes on this
track: game=dad, dogs=hooks, see=say. Split-half rule: a full-clip
Whisper result that drops content is rechecked on slices before any
incomplete verdict (MV-2 S22 t4 precedent). One axis per reroll verdict.

## S18 t2 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–7.70:
  "I am your dad, you're hearing once, you're hearing twice, now it
  lives inside."
- Ratio: slot 7.06s (L20 129.46–136.52) / line 7.70s = 0.92 → USABLE
  (t1 was 0.79 grey; the reroll landed inside the band).
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; mic on stand, hand on stand.
- G2 text: PASS. Plain walls, no legible text anywhere.
- G4 performance window: PASS on facing — the reroll axis is FIXED.
  Head front to camera in every sample (1s/2s/4s/5s/5.5s/6s/7s/8s);
  no head-turn arc, no profile, no three-quarter angle. Mouth open
  mid-line at 1s/2s/4s/5s/6s/7s; closed post-line at 8s.
- Frame gate: PASS. Vocal mean diff 0.59; longest <0.5 run 15f; <0.1
  run 0f. (Mean sits near the 0.5 floor but passes; run well under 24f.)
- Staging nit (disclosed, not a gate fail): hands reach the chest
  during the late vocal (by ~5.5s; line ends 7.70) rather than after
  the last word as directed. Same note class as t1's staging note:
  t1's G4 failed on facing alone, hands were a note — and this
  brief's fail condition was a facing miss, which did not occur.
  The end state is correct (hands to chest, mouth closed, facing
  camera at 8s).

## S19 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–8.12:
  "I am your dad, I am your dad, I am your dad, say it with me."
- Ratio: slot 7.28s (L21 136.52–143.80) / line 8.12s = 0.90 → USABLE.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; lean escalated as planned (close
  framing, leaning in).
- G2 text: PASS. Plain doorway, bare walls, no legible text anywhere.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s/5s/8s (8s is 0.12s before line end, still mid-line).
- Frame gate: PASS. Vocal mean diff 1.647; longest <0.5 run 1f; <0.1
  run 0f.
- Notes: no nits. Chorus 2 closes with the escalated lean as planned.

## S20 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–6.96:
  "I am your dad, you're hearing twice, now it lives inside."
- Ratio: slot 5.34s (L22 143.76–149.10) / line 6.96s = 0.77 → GREY
  (1.04x to 0.80 edge at assembly).
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie.
- G2 text: PASS. Plain doorway, bare walls, no legible text anywhere.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s/5s/6s; 7s shows a loose mouth tail just post-line (0.04s after
  line end), closed to the painted smile by 8s.
- Frame gate: PASS. Vocal mean diff 1.045; longest <0.5 run 3f; <0.1
  run 0f.
- Notes: loose mouth tail at 7s, assembly trims (same class as volley 4
  S14 t1's 0.48s tail). 8s half-closed eyes are post-line (blink/rest
  state — eyes open through the line at 2s/5s/6s/7s), not drift.

## S21 t1 — REJECTED, reroll axis DELIVERY [confirmed]
- Lyric sequence: FAIL (incomplete delivery). Prompted line is dad x3;
  the take sings dad x2 only, 0.00–6.82 ("I am your dad, I am your dad"),
  then holds a closed-mouth pose. Two vocal bursts (0–2.75, 5.0–6.75);
  tail RMS flat (~0.004) after 7.0s and the tail slice heard only an
  "and" fragment — no third repeat exists. The third repeat is
  missing, not quiet.
- Ratio: slot 9.20s (L23 150.30–159.50) / line 6.82s = 1.35 → GREY
  arithmetic, moot — sequence gates first.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; lamp set present (bridge contrast).
- G2 text: PASS. Bare room, plain walls, no legible text anywhere.
- G4 performance window: PASS on facing/mouth state (mouth open
  mid-line at 2s/5s, closed post-line at 8s) — the miss is delivery,
  not staging.
- Frame gate: PASS on motion. Vocal mean diff 1.204; longest <0.5 run
  1f; <0.1 run 0f.
- Reroll: DELIVERY axis for volley 6 — three repeats in full, do not
  stop after two; completeness wording ("all three times, in full").
  Pattern note: pure-repeat mantra lines can truncate (the model stops
  after two) — S19's tailed line (x3 + "say it with me") completed,
  while this tail-less x3 did not.

## S22 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, across two
  bursts: "I am your dad" 0.00–2.70 + "I am your dad" 4.00–6.32.
  Full-clip Whisper dropped the second repeat (single segment
  0.00–2.70, reproducibly); the split-half recheck recovered it —
  second-half slice word timestamps prove the second repeat
  (i 4.00–4.98, am 4.98–5.28, your 5.28–5.74, dad 5.74–6.32), and the
  5s frame shows the mouth wide open mid-second-repeat. Same save
  class as the MV-2 S22 t4 split-half precedent: never call a take
  incomplete on a full-clip decode alone.
- Ratio: slot 5.80s (L24 160.70–166.50) / line span 6.32s
  (0.00–6.32) = 0.92 → USABLE.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; leaning into the lamplight as planned.
- G2 text: PASS. Bare room + lamp, plain walls, no legible text
  anywhere.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s (burst 1) and 5s (burst 2); closed post-line at 8s.
- Frame gate: PASS with disclosure. Full-span vocal mean diff 1.211;
  word-window means 1.967 (burst 1) and 0.825 (burst 2) — motion
  healthy during every word. The longest <0.5 run, 27f, sits
  ENTIRELY in the inter-repeat gap (2.92–4.04s, no word plays
  there) — a held beat between repeats, not a freeze during words.
  Disclosed as a nit; the gate guards motion during words, which
  holds. (Post-line 59f still run from 6.50s is the held end pose,
  outside the vocal span.)
- Notes: bridge lamp set carries; lean reads in all three samples.

## S23 t1 — UNFIRED (generation failure, not a QC verdict)
- The S23 generation call failed with an integrity_check_failed error
  and was NOT retried in this volley, per the standing rule against
  repeating a failed media request. No take exists on disk; no QC row
  applies. S23 is HELD pending a parent decision: either a new
  request in a later volley, or a structural classification
  (assembly cover, no take). It is not counted as rejected and not
  counted against any reroll budget.

## Volley-5 tally
KEEP: S18 t2, S19, S20, S22. REJECTED: S21 t1 (incomplete delivery →
DELIVERY reroll owed, volley 6). UNFIRED: S23 (integrity failure, held
for parent decision — not retried, not rejected).
Pattern: chorus 2 closes clean (S18 facing fixed, S19/S20 usable/grey,
S22 saved by the slice recheck), while the bridge's first pure-repeat
mantra line truncated — repeat-drop is the new failure class to watch
on L23-style lines. The S22 save is the method working: a full-clip
drop is not an incomplete verdict until slices are checked.
