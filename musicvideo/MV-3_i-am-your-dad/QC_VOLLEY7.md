# MV-3 QC — Volley 7 rows (RECOVERY — original agent died in daemon restart after firing, before writing records)

Method: faster-whisper base on take audio (RAW words, mishear classes noted);
frames at 2s/5s/8s (the dead agent's qc7/ grabs, reused — no read
disagreements, no widening needed); motion from 160x90 gray frame diffs.
Near-dup threshold: mean abs diff <0.5. Frame gate: FAIL if vocal
near-dup (<0.5) run ≥24f during words OR vocal mean diff <0.5. Ratio =
song slot (line-table span) / take line (first word onset to last word
end). Usable 0.80–1.25; grey 0.60–0.80 / 1.25–1.60 (warp-rescue ≤1.5x
to band edge at assembly only — no warping in this volley); clear miss
outside grey. Lyric-sequence gate FIRST (ratio is not a lyric gate).
A take sings its line exactly once — no part of it a second time, and no
part of it missing (repeat defect = sequence fail; incomplete delivery =
sequence fail). Mishear classes on this track: game=dad, dogs=hooks,
see=say, word=words. Split-half rule: a full-clip Whisper result that
drops content is rechecked on slices before any incomplete verdict
(MV-2 S22 t4 precedent; volley 5 S22 save). One axis per reroll verdict.
All six takes 1280x720/24fps, durations measured.

## S23 t1 — REJECTED, pacing (ratio clear miss) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–8.00:
  "You can close your eyes, you can plug your ears, the words still
  bounce around inside your head" ("word" for "words" is a trivial
  plural mishear, same word — not a fail).
- Ratio: slot 13.36s (L25 168.76–182.12) / line 8.00s = 1.67 → ABOVE
  the 1.60 grey top → CLEAR MISS. Slot-fill arithmetic (S25-style):
  1.67 > 1.5 cap, so the take cannot fill its slot even warped.
  Disclosure for the parent: warp to the 1.25 edge needs only 1.34x
  (within cap), and non-word held-tail energy runs 8.00–8.75 (slice
  7.75–9.00 heard no words there) — if the tail counted, line 8.75s
  → ratio 1.53 grey. Method verdict stands on Whisper word
  timestamps (8.00s); the parent may alternatively rule grey-rescue.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie.
- G2 text: PASS. Bare room, plain walls, no legible text anywhere.
- G4 performance window: PASS. Facing camera at 2s/5s, mouth open
  mid-line; 8s post-line rest with the hands-near-head beat as
  prompted (hand beside the head, never covering the mouth).
- Frame gate: PASS. Word-window vocal mean diff 1.232; longest <0.5
  run 7f at 3.58–3.88s, during "ears" but far under the 24f gate.
- Notes: red-lip mouth color class disclosed, not failed (S13
  precedent); 8s eyes-closed post-line rest (same class as volley 6
  S25 t1's post-line blink).
- Reroll: PACING axis for volley 8 — prompt the line slower, spread
  across the ~13s slot. First attempt, so reroll budget is open.

## S24 t2 — REJECTED, delivery fail (2nd denial → structural recommendation) [confirmed]
- Lyric sequence: FAIL (incomplete delivery). Prompted line is dad x7
  accelerating with explicit counted sequencing; the take sings dad x3
  only, in three bursts ~0.50–2.25, ~4.25–5.75, ~6.00–7.75, then
  silence. Full-clip Whisper heard bursts 1–2; slice recheck of
  5.75–8.00 recovered burst 3 ("I am your dad" 5.75–7.45). Gaps
  RMS-flat (2.25–4.25, 5.75–6.00). Four repeats missing. Counted
  sequencing moved the count x2 → x3 but did NOT close to x7.
- Ratio: slot 8.88s (L26 183.06–191.94) / line 7.75s = 1.15 → USABLE
  arithmetic, moot — sequence gates first.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; push-in tightens framing as planned
  (8s frame much closer than 2s).
- G2 text: PASS. Bare room, plain walls, single lamp, no legible
  text anywhere.
- G4 performance window: PASS on staging (mouth open at 2s burst 1
  and 5s burst 2, resting smile post-line at 8s) — the miss is
  delivery, not staging.
- Frame gate: PASS on motion. Vocal mean 1.181; longest <0.5 run 5f.
- Reroll budget: EXHAUSTED. t1 (volley 6, x2) + t2 (volley 7, x3) =
  two denied delivery rerolls. Per QC_VOLLEY6's stated rule ("if this
  reroll also truncates, S24 goes structural") and the S21 precedent,
  NO third pull is recommended — parent structural decision owed
  (assembly cover: mantra beat-cut or cutaway/reaction while master
  audio carries L26).

## S25 t2 — REJECTED, delivery fail (2nd denial → structural recommendation) [confirmed]
- Lyric sequence: FAIL (incomplete delivery). Prompted line is dad x4
  with explicit counted sequencing; the take sings dad x2 only,
  IDENTICAL to t1, in two bursts ~0.25–2.25 and ~4.75–7.25, then
  silence. Full-clip Whisper heard burst 1 only; slice recheck of
  4.50–7.50 recovered burst 2 ("I am your dad" 4.50–6.82). Gap
  RMS-flat (2.25–4.75). Counted sequencing did NOT move the count
  at all. Two repeats missing.
- Ratio: slot 19.66s (L27 195.24–214.90) / line 7.25s = 2.71 — far
  outside grey, moot — sequence gates first. NOTE FOR PARENT (carried
  from volley 6): even a perfect x4 take (~10s max) cannot fill a
  19.66s slot under the 1.5x warp cap (19.66/10 = 1.97). S25's slot
  coverage is an assembly decision (mantra beat-cut per the
  timeline's mantra-block rule, or structural cover) independent of
  this reroll.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie.
- G2 text: PASS with note. Busy study set (books, globe, framed
  pictures, papers) but no legible text at frame resolution — same
  note class as t1.
- G4 performance window: PASS on staging (mouth open mid-burst at 2s
  and 5s; resting smile post-line at 8s) — the miss is delivery,
  not staging.
- Frame gate: PASS with disclosure. Vocal mean 0.712; longest <0.5
  run 52f at 2.125–4.29s sits entirely in the inter-burst gap
  (2.25–4.75, no word plays there) — same disclosure class as
  volley 5's S22 inter-repeat-gap run. Motion during words holds.
- Reroll budget: EXHAUSTED. t1 (volley 6, x2) + t2 (volley 7, x2) =
  two denied delivery rerolls, failing identically. Per the S21
  precedent, NO third pull is recommended — parent structural
  decision owed.

## S28 t1 — REJECTED, delivery (second line missing) [confirmed]
- Lyric sequence: FAIL (incomplete delivery). Prompted lines are
  L30 + L31, both exactly once, in order. The take sings L30 only,
  exactly once, 0.00–6.60: "I don't need a story, I don't need a
  name, just the one short claim that never changes". L31 ("You wake
  up tomorrow and the first thing you hear is the old man saying it
  crystal clear") is NOT sung — slice recheck of 6.00–9.00 heard
  only the "changes." tail (6.00–6.62); RMS flat after 6.75. The
  second line is missing, not quiet.
- Ratio: slot 14.58s (L30+L31 230.52–245.10) / line 6.60s = 2.21 —
  far outside grey, moot — sequence gates first.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; lean held (P-LEAN); morning light.
- G2 text: PASS. Bedroom doorway, plain walls, framed pictures
  blurred out, no legible text anywhere.
- G4 performance window: PASS on staging (mouth open mid-L30 at 2s
  and 5s; resting smile post-line at 8s) — the miss is delivery,
  not staging.
- Frame gate: PASS on motion. Vocal mean 1.778; longest <0.5 run 0f.
- Notes: red-lip mouth color class disclosed, not failed (S13
  precedent).
- Reroll: DELIVERY axis for volley 8 — both lines in full, in order.
  First attempt, so reroll budget is open.

## S29 t1 — KEEP (active) [confirmed]
- Lyric sequence: PASS. Full line exactly once, in order, 0.00–8.38:
  "I am your dad, I am your dad, say it with me."
- Ratio: slot 5.60s (L32 245.10–250.70) / line 8.38s = 0.67 → GREY
  (1.20x to 0.80 edge at assembly).
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; point at viewer held (P-POINT).
- G2 text: PASS. Plain street-corner walls, no legible text anywhere.
- G4 performance window: PASS. Facing camera, point held through the
  line at 2s/5s/8s; mouth open mid-line at 2s/5s, closing on the
  final "me." at 8s.
- Frame gate: PASS with disclosure. Word-window vocal mean diff
  0.814; longest <0.5 run 23f at 3.08–4.04s during the held "I"
  (2.92–4.72) — 1f under the 24f gate, knife-edge, disclosed.
  Motion during words otherwise holds.
- Notes: no nits. Last chorus opens with the widest point as planned.

## S30 t1 — REJECTED, delivery (tail phrase missing) [confirmed]
- Lyric sequence: FAIL (incomplete delivery). Prompted line is L33
  in full; the take sings "I am your dad, you're hearing once,
  you're hearing twice" 0.00–6.56 and stops. The tail phrase "now
  it lives inside" is NOT sung — slice recheck of 6.25–9.00 heard
  only the "twice" tail garbled as "Wines." (6.25–6.77); RMS flat
  after 6.75. Four words missing. Same stop-early shape as the
  repeat-drop class, on a non-repeat line.
- Ratio: slot 7.28s (L33 251.04–258.32) / line 6.56s = 1.11 → USABLE
  arithmetic, moot — sequence gates first.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing; suit + cadmium tie; mic on stand (P-CROON).
- G2 text: PASS. Plain corner wall, no legible text anywhere.
- G4 performance window: PASS on staging (mouth open mid-line at 2s
  and 5s; resting smile post-line at 8s) — the miss is delivery,
  not staging.
- Frame gate: PASS on motion. Vocal mean 1.033; longest <0.5 run 2f.
- Notes: no nits. Hand grips the mic stand shaft (stand mic, not
  handheld — no nit).
- Reroll: DELIVERY axis for volley 8 — the full line including "now
  it lives inside". First attempt, so reroll budget is open.

## Volley-7 tally
KEEP: S29 t1. REJECTED: S23 t1 (pacing, ratio 1.67 clear miss →
PACING reroll volley 8), S24 t2 (incomplete delivery x3 of x7, 2nd
denial → parent structural decision, no third pull recommended),
S25 t2 (incomplete delivery x2 of x4, 2nd denial → parent
structural decision, no third pull recommended), S28 t1 (L31 missing
→ DELIVERY reroll volley 8), S30 t1 (tail phrase missing → DELIVERY
reroll volley 8). UNFIRED: none — 6 attempts, 6 landed, 0 failed.
Pattern: COUNTED SEQUENCING IS NOT A RELIABLE FIX. It moved S24
x2 → x3 but did not close to x7, and did not move S25 at all (x2 →
x2). Tail-less repeat lines still truncate; the stop-early shape
also hit two non-repeat first attempts (S28's second line, S30's
tail phrase). The repeat-drop class now reads: the model sings what
it sings, holds, and stops — counted sequencing buys at most one
extra repeat. S24/S25 close by the two-denial rule, not by a third
pull.
