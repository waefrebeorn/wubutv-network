# MV-3 QC — Volley 6 rows

Method: faster-whisper base on take audio (RAW words, mishear classes noted);
frames at 2s/5s/8s (no widening needed — no read disagreements);
motion from 160x90 gray frame diffs. Near-dup threshold: mean abs diff
<0.5. Frame gate: FAIL if vocal near-dup (<0.5) run ≥24f during words OR
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

## S15 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.72–7.82:
  "You try to skip it, but you try to change the song, but the phrase
  comes back and it doesn't take long."
- Ratio: slot 6.98s (L17 108.92–115.90) / line 7.10s (0.72–7.82) = 0.98
  → USABLE.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; point at viewer held (P-POINT).
- G2 text: PASS. Plain street-corner walls, no legible text anywhere.
- G4 performance window: PASS. Facing camera, point held through the
  line at 2s/5s, hand lowered by 8s; mouth open mid-line at 2s/5s,
  resting smile post-line at 8s.
- Frame gate: PASS with disclosure. Word-window vocal mean diff 1.791;
  longest <0.5 run 27f at 7.50–8.62s, but only its first ~8f overlap the
  final word's tail (mouth closing on "long", 7.36–7.82); the rest is
  the post-line held pose. Motion during words holds — same disclosure
  class as volley 5's S22 inter-repeat-gap run.
- Notes: no nits. First attempt lands clean after the volley-4
  infrastructural failure.

## S21 t2 — REJECTED, delivery fail (2nd denial) [confirmed]
- Lyric sequence: FAIL (incomplete delivery). Prompted line is dad x3;
  the take sings dad x2 only, in two bursts 0.00–2.48 and 5.72–8.00,
  with a ~3.2s silent gap between them. Slice recheck of 2.0–6.5s
  heard only the tail of burst 1 ("and") and the onset of burst 2
  ("I"); gap RMS flat (0.047 → 0.002), and the 5s frame shows the
  painted smile held, not a mouthed repeat — no middle repeat exists.
  The third repeat is missing, not quiet. Completeness wording
  ("ALL THREE TIMES IN FULL") did NOT fix the defect: t1 and t2 fail
  identically (repeat, hold, repeat, stop).
- Ratio: slot 9.20s (L23 150.30–159.50) / line 8.00s = 1.15 → GREY
  arithmetic, moot — sequence gates first.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; lamp set present.
- G2 text: PASS. Bare room, plain walls, no legible text anywhere.
- G4 performance window: PASS on staging (mouth open mid-burst at 2s
  and 8s, painted smile held through the gap at 5s) — the miss is
  delivery, not staging.
- Frame gate: PASS on motion. Burst means 1.02 / 1.20; longest <0.5
  run 15f; <0.1 run 1f.
- Reroll budget: EXHAUSTED. t1 (volley 5) + t2 (volley 6) = two denied
  delivery rerolls. Per the prepro retirement rule and the S04/S05
  precedent, NO third pull is recommended — parent structural
  decision owed (assembly cover, no take).

## S24 t1 — REJECTED, reroll axis DELIVERY [confirmed]
- Lyric sequence: FAIL (incomplete delivery). Prompted line is dad x7
  accelerating; the take sings dad x2 only, in two bursts 0.00–2.36
  and 5.14–6.50, then silence. Slice recheck of 2.0–6.0s heard only
  garbage ("And I'd...") over the silent gap (RMS 0.015 → 0.004);
  no middle repeats exist. Five repeats missing. The accelerating
  instruction did not produce acceleration — the model sang one slow
  repeat, held, sang one more, and stopped.
- Ratio: slot 8.88s (L26 183.06–191.94) / line 6.50s = 1.37 → GREY
  arithmetic, moot — sequence gates first.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; push-in tightens framing as planned
  (8s frame much closer than 2s).
- G2 text: PASS. Bare room, plain walls, single lamp, no legible
  text anywhere.
- G4 performance window: PASS on staging (mouth open at 2s burst 1
  and 5s burst-2 onset, resting smile post-line at 8s) — the miss is
  delivery, not staging.
- Frame gate: PASS on motion. Burst means 1.21 / 1.66; longest <0.5
  run 1f; <0.1 run 0f.
- Reroll: DELIVERY axis for volley 7 — seven times in full, with
  explicit counted sequencing (first … seventh) plus completeness
  wording; the volley-6 accelerating instruction alone did not hold.
  Caution: S21's completeness wording failed twice on x3 — if this
  reroll also truncates, S24 goes structural (two denied rerolls).

## S25 t1 — REJECTED, reroll axis DELIVERY [confirmed]
- Lyric sequence: FAIL (incomplete delivery). Prompted line is dad x4
  (mantra lead); the take sings dad x2 only, in two bursts 0.00–2.38
  (dad held to ~3.16) and 5.00–6.32. Full-clip Whisper dropped burst
  2; the split-half recheck recovered it (second-half slice words
  i 0.00–0.22, am 0.22–0.46, your 0.46–0.76, dad 0.76–1.32, local
  times = absolute 5.00–6.32) — the save class works, but the saved
  total is still x2, not x4. Two repeats missing.
- Ratio: slot 19.66s (L27 195.24–214.90) / line 6.32s = 3.11 — far
  outside grey, moot — sequence gates first. NOTE FOR PARENT: even a
  perfect x4 take (~10s max) cannot fill a 19.66s slot under the 1.5x
  warp cap (19.66/10 = 1.97). S25's slot coverage is an assembly
  decision (mantra beat-cut per the timeline's mantra-block rule, or
  structural cover) independent of this reroll.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie. Red-lip mouth color class disclosed,
  not failed (S13 precedent).
- G2 text: PASS with note. Busy study set (books, globe, framed
  pictures, papers) but no legible text at frame resolution — book
  spines and papers blur out, nothing readable.
- G4 performance window: PASS on staging (mouth open mid-burst at 2s
  and 5s; eyes closed at 8s is post-line rest, line ended 6.32 —
  same class as volley 5 S20's post-line blink) — the miss is
  delivery, not staging.
- Frame gate: PASS on motion. Burst means 0.70 / 0.89; longest <0.5
  run 12f; <0.1 run 0f.
- Reroll: DELIVERY axis for volley 7 — four times in full, explicit
  counted sequencing plus completeness wording. Same repeat-drop
  class as S21/S24: tail-less repeat lines truncate at x2.

## S26 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–6.54:
  "They study the hooks, they study the loops, they say simple words"
  ("hooks" heard correctly, not the "dogs" mishear).
- Ratio: slot 5.24s (L28 215.40–220.64) / line 6.54s = 0.80 → USABLE
  (band edge).
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; lean over the desk held (P-LEAN).
  Red-lip mouth color class disclosed, not failed (S13 precedent).
- G2 text: PASS with note. Busy study set (bookshelves, green lamp,
  papers) but no legible text at frame resolution.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s/5s, resting smile post-line at 8s (eyes slightly narrowed at
  8s is post-line rest, line ended 6.54).
- Frame gate: PASS with disclosure. Word-window vocal mean diff
  0.876; phrase means 1.338 / 0.92 / 0.748 — motion healthy during
  every phrase. Longest <0.5 run 46f at 6.12–8.04s, but only its
  first ~10f overlap the final word's tail ("words" 5.82–6.54); the
  rest is the post-line held pose. The 19f run at 3.67–4.46s sits in
  the inter-phrase gap (3.78–4.64, no word plays there). Motion
  during words holds — same disclosure class as volley 5's S22.
- Notes: no nits beyond the disclosed color class and busy set.

## S27 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–8.16:
  "Make the brain stay true, repeat the same, I make it easy to sing,
  and the mind can play it on its own string" (all 24 words).
- Ratio: slot 9.36s (L29 220.64–230.00) / line 8.16s = 1.15 → USABLE.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie. Red-lip mouth color class disclosed,
  not failed (S13 precedent).
- G2 text: PASS. Plain study wall + bookshelf edge, no legible text
  anywhere.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s ("true") and 5s ("easy"), still shaping the final word
  ("string" 7.78–8.16) at 8s.
- Frame gate: PASS. Word-window vocal mean diff 1.674; longest <0.5
  run 11f; <0.1 run 0f.
- Notes: no nits beyond the disclosed color class. Conducting hand
  not visible in the 2s/5s/8s samples (staging note only, not a gate).

## Volley-6 tally
KEEP: S15 t1, S26 t1, S27 t1. REJECTED: S21 t2 (incomplete delivery x2
of x3, 2nd denial → parent structural decision, no third pull
recommended), S24 t1 (incomplete delivery x2 of x7 → DELIVERY reroll
volley 7), S25 t1 (incomplete delivery x2 of x4 → DELIVERY reroll
volley 7). UNFIRED: none — 6 attempts, 6 landed, 0 failed.
Pattern: REPEAT-DROP CONFIRMED as a failure class. Tail-less repeat
lines truncate at x2 across three scenes (S21 x3→x2 twice despite
completeness wording, S24 x7→x2, S25 x4→x2), while tailed lines
(S19 x3 + "say it with me") and asked-x2 lines (S22) complete. The
model's repeat behavior is: sing one, hold, sing one more, stop.
Volley-7 rerolls need explicit counted sequencing, not just
completeness wording — and if they truncate again, the scenes go
structural.
