# MV-3 QC — Volley 1 rows

Method: faster-whisper base on take audio (RAW words, mishear classes noted);
frames at 2s/5s/8s (widened where reads disagreed); motion from 160x90 gray
frame diffs. Near-dup threshold stated: mean abs diff <0.5 = near-duplicate
frame (a <1.0 threshold counts slow MCU motion as duplication and was
rejected after inspection — S10's 59f <1.0 run is visible mouth motion at
0.4–0.9 diff, not a freeze). Frame gate: FAIL if vocal near-dup (<0.5) run
≥24f during vocal OR vocal mean diff <0.5. Ratio = song slot / take line
(first word onset to last word end). Usable 0.80–1.25; grey 0.60–0.80 /
1.25–1.60 (warp-rescue ≤1.5x to band edge at assembly); clear miss outside grey.

## S09 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order: dad 0.00–2.24,
  dad 3.20–5.10, "Say it with me" 6.08–7.58.
- Ratio: slot 5.36s / line 7.58s = 0.707 → GREY (warp-rescue: 1.13x to 0.80 edge).
- G1 character: PASS. Yellow ball head, dot eyes, dark suit, cadmium tie —
  matches the lock; single character, facing camera. ANCHOR P-POINT.
- G2 text: PASS. Background shop signs are illegible blur in all 3 samples.
- G3 licensed: PASS. Original monster man; no licensed material.
- G4 performance window: PASS. 2s + 5s: face-to-camera, mouth wide open,
  point held; 8s: post-line held pose, mouth closed to painted smile.
- Frame gate: PASS. Vocal mean diff 4.177; longest <0.5 run 2f; <0.1 run 0f.
- Notes: vocal fills 0–7.58 of 9.000s; 1.42s held-pose tail trims cleanly.

## S01 t1 — REJECTED, reroll axis TEXT [confirmed]
- Lyric sequence: PASS. "Listen, all of you." 0.00–4.90, exactly once.
- Ratio: slot 6.18s / line 4.90s = 1.26 → GREY (barely; 1.01x to band edge).
- G1: PASS. Ball head, dot eyes, suit, tie; lean + open palms as posed.
- G2: FAIL. Legible neon "OPEN" sign in the left background at 2s and 5s.
- G4: PASS. 2s mouth open mid-line, facing; 5s "o" viseme at line tail.
- Frame gate: PASS. Vocal mean 1.175; longest <0.5 run 20f (<24f).
- Reroll: same vehicle + plain background (no shops, no signs, no neon).

## S02 t1 — REJECTED, reroll axis TEXT (+CHARACTER noted) [confirmed]
- Lyric sequence: PASS. "You already know I am your dad" 0.00–6.50, once.
- Ratio: slot 9.02s / line 6.50s = 1.39 → GREY (1.11x to 1.25 edge).
- G1: FAIL. Eyes are large white-sclera cartoon eyes, not the lock's dot
  eyes, and not the S09 anchor's eyes. Face drift.
- G2: FAIL. Legible neon "OPEN"/"PEN" at the left edge at 2s and 5s.
- G4: PASS (facing + open mouth at 2s and 5s). Mic is handheld, not stand —
  disclosed NIT class, not a fail.
- Frame gate: PASS. Vocal mean 1.225; longest <0.5 run 5f.
- Reroll: text axis first (plain background, identity block verbatim). If
  the reroll's eyes still drift, the next reroll is CHARACTER.

## S10 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–7.70.
- Ratio: slot 7.14s / line 7.70s = 0.93 → USABLE band. Cleanest take of the volley.
- G1: PASS. Dot eyes, ball head, suit, tie — matches S09 anchor. ANCHOR P-CROON.
- G2: PASS. Background signage illegible blur in both samples.
- G4: PASS. 2s + 5s face-to-camera, mouth open; hand moves to chest
  mid-line as posed (slightly early, not a fail).
- Frame gate: PASS. Vocal mean 1.044; longest <0.5 run 5f; <0.1 run 0f.
  (The 59f <1.0 run is slow-motion mouth movement, not a freeze — see Method.)

## S11 t1 — REJECTED, reroll axis CHARACTER [confirmed]
- Lyric sequence: PASS. Full line exactly once, 0.00–9.18.
- Ratio: slot 6.62s / line 9.18s = 0.72 → GREY (1.11x to 0.80 edge).
- G1: FAIL. White-sclera cartoon eyes (2s, 8s) vs the lock's dot eyes and
  the S09 anchor. (5s shows closed eyes mid-blink — not itself a fail.)
- G2: PASS. Doorway background: framed pictures illegible, no text.
- G4: PASS. All 3 samples face-to-camera with visible, open mouth.
- Frame gate: BORDERLINE. Longest <0.5 run 24f — exactly at the ≥24f gate.
  Visual samples show continuous mouth-shape change (open → "o" → open),
  so the run is judged a slow passage, not a freeze; the take fails G1
  regardless, so the borderline does not change the verdict.
- Reroll: character axis — eye line strengthened to "small solid black oval
  eyes, no white showing", referencing the S09 anchor.

## S12 t1 — REJECTED, reroll axis TEXT [confirmed]
- Lyric sequence: PASS. "I am your dad." twice (0.00–2.96, 3.86–6.54) =
  the full line exactly once, with a between-phrase gap.
- Ratio: slot 4.58s / line span 6.54s = 0.70 → GREY (1.14x to 0.80 edge).
- G1: PASS. Dot eyes matching the anchor; mic on stand; arms open post-line.
- G2: FAIL. Legible neon "OPEN" sign in the left background at 2s, 5s, 8s.
- G4: PASS. 2s + 5s facing + open mouth; 8s arms-open held pose, mouth closed.
- Frame gate: PASS. Vocal means 2.068 / 2.743; longest <0.5 run 0f.
- Reroll: same vehicle + plain background (no shops, no signs, no neon).

## Volley-1 tally
KEEP: S09, S10. REJECTED: S01 (G2), S02 (G1+G2), S11 (G1), S12 (G2).
Pattern: street-corner vehicles default to signed storefronts (3 G2 fails);
"dot eyes" alone drifts to white-sclera eyes (2 G1 fails). Both fixed in the
vehicle template for volley 2 (see VOLLEY_PROGRESS.md). No take failed the
lyric-sequence gate; no take was a clear ratio miss; no structural (pace-floor)
classifications this volley.
