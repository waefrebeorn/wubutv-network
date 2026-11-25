# MV-3 QC — Volley 2 rows

Method: faster-whisper base on take audio (RAW words, mishear classes noted);
frames at 2s/5s/8s (widened where reads disagreed: S02 4s/6s for the 5s
closed-eye frame, S03 1s/3.5s for the hand-tone read, S11 9.5s end-state);
motion from 160x90 gray frame diffs. Near-dup threshold: mean abs diff <0.5.
Frame gate: FAIL if vocal near-dup (<0.5) run ≥24f during vocal OR vocal mean
diff <0.5. Ratio = song slot / take line (first word onset to last word end).
Usable 0.80–1.25; grey 0.60–0.80 / 1.25–1.60 (warp-rescue ≤1.5x to band edge at
assembly only — no warping in this volley); clear miss outside grey.
Lyric-sequence gate FIRST (ratio is not a lyric gate). Mishear classes on
this track: game=dad, dogs=hooks, see=say. One axis per reroll verdict.

## S01 t2 — KEEP (active) [confirmed]
- Lyric sequence: PASS. "Listen, all of you" 0.00–4.54, exactly once.
- Ratio: slot 6.18s / line 4.54s = 1.36 → GREY (1.09x to 1.25 edge).
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie match the lock. TEXT-axis fix held.
- G2 text: PASS. Plain building walls in all samples; no legible text.
  The volley 1 "OPEN" neon is gone.
- G4 performance window: PASS. 2s mouth open mid-line, lean + open palms;
  8s mouth closed to the painted smile, lean held.
- Frame gate: PASS. Vocal mean diff 1.626; longest <0.5 run 9f; <0.1 run 0f.
- Notes: 5s frame shows a small "o" mouth 0.46s after line end — loose
  tail, closed by 8s. Disclosed nit, not a fail; assembly trims the tail.

## S02 t2 — KEEP (active) [confirmed]
- Lyric sequence: PASS. "You already know, I am your dad" 0.00–6.94,
  exactly once.
- Ratio: slot 9.02s / line 6.94s = 1.30 → GREY (1.04x to 1.25 edge).
- G1 character: PASS. Small solid black oval eyes in 2s/4s/6s/8s samples;
  the 5s closed eyes are a mid-blink (widened sample: eyes open at 4s and
  6s), not drift — same ruling as volley 1 S11 t1. TEXT axis fixed and the
  noted CHARACTER concern is closed: no white sclera anywhere.
- G2 text: PASS. Plain walls + doorway in all samples; no legible text.
  The volley 1 "OPEN"/"PEN" neon is gone.
- G4 performance window: PASS. Facing camera, mouth open through the line
  (2s/4s/6s); 8s post-line held pose.
- Frame gate: PASS. Vocal mean diff 1.083; longest <0.5 run 4f; <0.1 run 0f.
- Notes: two disclosed nits, both repeat classes from volley 1 — (1) mic
  is handheld, not on the stand, in all samples; (2) 8s frame shows the
  mouth still open in a held smile 1.06s after line end (Whisper hears no
  words after 6.94, so no lyric spills past the line). Assembly trims
  the tail.

## S11 t2 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–8.48.
- Ratio: slot 6.62s / line 8.48s = 0.78 → GREY (1.03x to 0.80 edge).
- G1 character: PASS. Eyes exactly as the S09 anchor: small solid black
  oval eyes, no white showing, in 2s/5s/9.5s samples. The CHARACTER axis
  is fixed — no white sclera anywhere. Ball head, suit, cadmium tie match.
- G2 text: PASS. Doorway background; framed picture illegible, no text.
- G4 performance window: PASS. 2s + 5s face-to-camera, mouth open mid-line;
  9.5s mouth closed to the painted smile, lean held.
- Frame gate: PASS. Vocal mean diff 1.565; longest <0.5 run 7f; <0.1 run 0f.
- Notes: lip color renders reddish-pink in this take vs the yellow/dark
  mouths of the other takes. Disclosed nit, not a fail — the face lock
  (ball head + oval eyes + suit + tie) is exact.

## S12 t2 — KEEP (active) [confirmed]
- Lyric sequence: PASS. "I am your dad." twice (0.00–2.68, 3.50–6.80) =
  the full line exactly once, with a between-phrase gap.
- Ratio: slot 4.58s / line span 6.80s = 0.67 → GREY (1.19x to 0.80 edge).
- G1 character: PASS. Small solid black oval eyes, no white showing;
  mic on stand with hand on the stand (not handheld this time).
- G2 text: PASS. Plain walls in all samples; no legible text. The volley 1
  "OPEN" neon is gone.
- G4 performance window: PASS. 2s mouth open mid-line; 5s arms opening
  into the post-line pose; 8s arms-open held pose, mouth closed to the
  painted smile.
- Frame gate: PASS. Vocal mean diff 1.175; longest <0.5 run 14f (<24f);
  <0.1 run 0f.
- Notes: hand tone renders dark in shadow at 8s (same lighting variation
  as S03). Disclosed nit, not a fail — face lock exact.

## S03 t1 — KEEP (active, CUTAWAY) [confirmed]
- Lyric sequence: N/A (instrumental cutaway). Whisper hears only "music"
  7.18–8.58 — generated ambient audio, not a sung line. Mouth is closed
  to the painted smile at 1s/2s/3.5s/5s/8s, including inside the
  "music" span, so no lyric is performed on camera.
- Ratio: N/A (no vocal to cover; assembly places the 10.000s walk under
  the 13.82s instrumental slot with the song as master audio).
- G1 character: PASS on the face lock — ball head, small solid black
  oval eyes, suit, cadmium tie, exact in all samples. Walk delivered:
  far at 1s, mid-stride at 2s/3.5s, near at 5s/8s; wall speaker planted
  in frame throughout (carry into V1).
- G2 text: PASS. Plain walls, unbranded speaker, no legible text anywhere.
- G4 performance window: N/A (cutaway — no singing pose). Motion mean
  5.28 over the clip confirms continuous walking movement, not a freeze.
- Frame gate: N/A (no vocal window). No freeze anywhere in the walk.
- Notes: hands render dark rather than yellow, consistently across
  1s/2s/3.5s samples (a within-take rendering choice, not a one-frame
  artifact). Disclosed nit, not a fail — the face lock is exact and the
  cutaway's job (walk + speaker plant) is delivered. If the parent
  wants strict hand-color matching, this is the take to restage.

## S04 t1 — REJECTED, reroll axis PACING [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–7.58
  ("I've been here the whole time, kid, looking right at you" — the
  take smooths the performed "I been" to "I've"; one-word contraction
  variant, noted, not a wrong line).
- Ratio: slot 3.56s (L03 32.16–35.72; plan slot 3.84s) / line 7.58s = 0.47
  (0.51 on the plan slot) → CLEAR MISS, outside grey. Max 1.5x
  warp-rescue reaches only 0.71, still below the 0.80 band edge — this
  is a generation miss, not an assembly rescue. The song sings 11 words
  in 3.56s; the take delivers them at natural pace in 7.58s.
- G1 character: PASS. Ball head, small solid black oval eyes, suit,
  cadmium tie; doorway, no text (G2 PASS); facing camera, mouth open
  mid-line at 2s (G4 PASS).
- Frame gate: PASS. Vocal mean diff 1.682; longest <0.5 run 6f.
- Reroll: PACING axis for volley 3 — prompt the 11-word line briskly
  (rapid-fire delivery, all words inside ~4s), performed wording
  verbatim ("I been here…", not "I've"). If the pacing reroll also
  misses, the slot goes STRUCTURAL per the pace-floor rule (assembly
  cover, no third pull).

## Volley-2 tally
KEEP: S01, S02, S11, S12, S03 (cutaway). REJECTED: S04 (ratio clear miss).
Pattern: the volley 1 template fixes WORKED — all three TEXT axes fixed
(no neon in any reroll) and both CHARACTER concerns closed (no white
sclera in any reroll). The new miss is pacing, not look: S04's 11-word
line in a 3.56s slot is the fastest lyric density so far, and the take
sang it at natural pace. No take failed the lyric-sequence gate; no
take failed the frame gate; no structural classifications this volley
(S04 is a first-attempt pacing miss, not yet structural).
