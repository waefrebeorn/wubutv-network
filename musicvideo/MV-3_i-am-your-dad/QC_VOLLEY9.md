# MV-3 QC — Volley 9 rows

Method: faster-whisper base on take audio (RAW words, mishear classes noted;
numpy array input — the venv's av decode path is broken, see qc9_analyze.py);
frames at 2s/5s/8s in qc9/ (widened where reads disagreed: S36 t1 to a full
1s–8s tile for the eye design); motion from 160x90 gray frame diffs.
Near-dup threshold: mean abs diff <0.5. Frame gate: FAIL if vocal
near-dup (<0.5) run ≥24f during words OR vocal mean diff <0.5; runs
entirely in inter-repeat/inter-phrase gaps or post-line holds with
healthy word-window means PASS with disclosure (S22/S25 precedents).
Ratio = song slot (line-table span) / take line (first word onset to
last word end). Usable 0.80–1.25; grey 0.60–0.80 / 1.25–1.60
(warp-rescue ≤1.5x to band edge at assembly only — no warping in this
volley); clear miss outside grey. Lyric-sequence gate FIRST (ratio is
not a lyric gate). A take sings its line exactly once — no part of it
a second time, and no part of it missing (repeat defect = sequence
fail; incomplete delivery = sequence fail). Mishear classes on this
track: game=dad, dogs=hooks, see=say, word=words. Split-half rule: a
full-clip Whisper result that drops content is rechecked on slices
before any incomplete verdict (MV-2 S22 t4 precedent; volley 5 S22 save).
One axis per reroll verdict. All six takes 1280x720/24fps, durations
measured. Mantra rule for S35/S37: L36 is a COUNTED line (x4 prompted),
so the S31–S33 thirds' content rule does not cover it; L38 carries no
count in the timeline, so its sequence test is correct mantra content
across the take, not a count.

## S28 t3 — KEEP (grey) [confirmed]

- Lyric sequence: PASS. The PACING axis is fixed: BOTH lines exactly
  once, in order — L30 "I don't need a story, I don't need a name,
  just the one short claim that never changes" 0.00–5.26, then L31
  "You wake up tomorrow and the first thing you hear is the old man
  saying it crystal clear" 5.74–9.30. RMS confirms silence after 9.30
  (9.30–10.00 RMS 0.0122 → flat) and a clean break between lines
  (5.26–5.74 RMS 0.0083 → flat): no further content.
- Ratio: slot 14.58s (L30+L31 230.52–245.10) / line 9.30s = 1.57 →
  GREY. Warp 1.26x to the 1.25 edge at assembly. The PACING reroll
  moved the take from t2's 1.63 clear miss into grey — the axis is
  fixed, on its own numbers, no grey-rescue ruling needed. Note: the
  vehicle asked for a 10-second take (the line itself must exceed
  9.11s); the tool returned 10.000s, so the line fits.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing, suit + cadmium tie; bedroom-doorway set matches the plan
  (morning light, doorway), lean-in present (P-LEAN).
- G2 text: PASS. Bedroom, lamp, bedding blurred, no legible text
  anywhere.
- G4 performance window: PASS. Facing camera, lean held, mouth open
  mid-line at 2s/5s; 8s frame is mid-L31 ("saying" 7.86–8.30), mouth
  open as expected.
- Frame gate: PASS. Word-window vocal mean diff 0.892; longest <0.5
  run in vocal window 13f (5.00–5.54s). The 21f full-take run at
  9.08–9.96s straddles the line end into post-line rest (only ~5f of
  it falls during "clear.") — disclosed, under the 24f gate either way.
- Specs: 1280x720/24fps, 10.000s, md5 6df937cef902a407bd61ef5e767f212c.

## S30 t3 — REJECTED, delivery (middle phrase missing) — character FIXED [confirmed]

- Lyric sequence: FAIL (incomplete delivery). Prompted line is L33 in
  full. The take sings "I am your dad, you're hearing once" 0.00–5.20,
  then a 0.5s silence gap (5.20–5.78 RMS 0.001–0.01 → flat), then one
  slurred token, then "lives inside" 6.16–7.28. Three transcription
  passes agree on the shape and disagree only on the slurred token:
  full-clip "you're it", slice 4.50–8.50 "your wit", fine slice
  5.15–6.30 "you're with". The words "hearing" (second occurrence)
  and "now" are never recovered in any pass, and they cannot hide in
  the flat silence gap. The middle phrase "hearing twice, now" is
  missing — a dropped-middle delivery defect, same class as t1's
  dropped tail but a new shape (not a repeat-count defect).
- Ratio: slot 7.28s (L33 251.04–258.32) / line 7.28s = 1.00 → USABLE
  arithmetic, moot — sequence gates first.
- G1 character: PASS — the CHARACTER axis is fixed. All three samples
  show the big yellow ball head with two large solid black oval eyes,
  wide open, no white, no lids; suit + cadmium tie, mic on stand,
  corner set. The strengthened eye specification worked where restating
  the eye line alone (t2) did not. This take proves the eye spec CAN
  hold — the delivery broke instead.
- G2 text: PASS. Plain corner walls, no legible text anywhere.
- G4 performance window: PASS on staging (mouth open mid-line at 2s/5s;
  8s post-line rest smile) — the miss is delivery, not staging.
- Frame gate: PASS on motion. Word-window vocal mean diff 0.738;
  longest <0.5 run in vocal window 16f (4.62–5.29s). The 22f run at
  6.96–7.88s straddles the line end (7.28) into post-line rest —
  disclosed, under the 24f gate either way.
- Specs: 1280x720/24fps, 9.000s, md5 ad5fd1838a3eeaa754435c6b57a51ba7.
- Owed: PARENT ADJUDICATION, not a fixed axis. The parent's structural
  trigger for S30 was "if t3 fails character" — character PASSED, so
  that trigger is not met. But delivery, fixed on t2, broke on t3.
  Axis accounting: delivery t1 fail → t2 pass → t3 fail; character
  t2 fail → t3 pass. Options: (a) t4 DELIVERY reroll carrying the
  strengthened eye spec (delivery is proven fixable — t2 exists with
  the full line at 0.94 usable, only its eyes failed); (b) structural
  on axis churn (three takes, each breaking something different).
  QC recommends (a) — the failure shape is new (dropped middle, not
  the t1 tail), and t2 proves the line is singable — but the call is
  the parent's. Do NOT fire t4 from this document.

## S34 t1 — KEEP (usable) [confirmed]

- Lyric sequence: PASS. Full L35 exactly once, in order, 0.00–7.16:
  "I am your dad, I am your dad, just a low voice." The low-voice tail
  is heard clearly as words; register drop is a performance nuance,
  not a gate.
- Ratio: slot 8.20s (L35 287.80–296.00) / line 7.16s = 1.15 → USABLE.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing (tiny render eye-shine dots, not sclera), suit + cadmium
  tie; dim living-room set matches the plan (lamp, bookshelf).
- G2 text: PASS with note. Framed pictures and books blurred, no
  legible text anywhere.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s/5s; 8s post-line rest smile (line ends 7.16).
- Frame gate: PASS with disclosure. Word-window vocal mean diff 0.967;
  longest <0.5 run in vocal window 12f (4.21–4.71s). The 33f run at
  7.50–8.88s is entirely post-line rest — disclosed, same class as
  the S22/S25 post-line holds.
- Specs: 1280x720/24fps, 9.000s, md5 ed6fe01827c4792aeef29c25093d1bd9.

## S35 t1 — REJECTED, delivery (x2 of x4) [confirmed]

- Lyric sequence: FAIL (incomplete delivery). Prompted line is L36,
  "I am your dad" x4 (count prompted in the vehicle and the timeline).
  Full-clip Whisper heard only burst 1 (0.00–2.32); slice recheck of
  2.00–9.00 recovered burst 2 ("I am your dad." 3.54–6.28) before any
  verdict, per the split-half rule. RMS confirms the two-burst
  structure cleanly (burst 1 ~0.25–2.25, flat 2.75–4.00, burst 2
  ~4.25–6.25, flat after 6.50). Two repeats missing. This is the
  repeat-drop shape exactly as S25 t1 (x4→x2) — a counted line
  truncating at x2, not a mantra-third content case.
- Ratio: slot 11.86s (L36 296.70–308.56) / line 6.28s = 1.89 — clear
  miss, moot — sequence gates first. NOTE: unlike S37, this slot IS
  fillable — a full-take ~9.5s x4 delivery lands ~1.25, in band — so
  the reroll is meaningful.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing, suit + cadmium tie; living-room set matches the plan.
- G2 text: PASS with note. Bookshelves/framed pictures blurred, no
  legible text anywhere.
- G4 performance window: PASS on staging (mouth open mid-mantra at
  2s/5s; 8s held smile is post-line rest, line ends 6.28) — the miss
  is delivery, not staging.
- Frame gate: PASS on motion. Word-window vocal mean diff 0.909;
  longest <0.5 run in vocal window 5f. The 39f run at 2.46–4.08s is
  the inter-burst gap — disclosed, same class as S22/S25.
- Specs: 1280x720/24fps, 9.000s, md5 7938076e9cb1ac1141723d0addb9a375.
- Reroll: DELIVERY axis for volley 10 — all four repeats, in order.
  First attempt, so reroll budget is open.
- Disclosure for the parent: if the parent extends the S31–S33
  mantra-thirds content rule ("correct content, not a count") to
  breakdown mantras, this take's sequence verdict flips to PASS and
  its axis becomes PACING (ratio 1.89 clear miss). QC does not adopt
  that extension — L36 is a counted line, and the S25 t1 precedent
  (same count, same truncation) rules it a delivery fail.

## S36 t1 — REJECTED, G1 eye drift (dot eyes, never ovals) [confirmed]

- Lyric sequence: PASS. Full L37 exactly once, in order, 0.00–7.78:
  "All of you, every single one, I am your dad, you know it now."
- Ratio: slot 11.56s (L37 309.88–321.44) / line 7.78s = 1.49 → GREY.
  Warp 1.19x to the 1.25 edge at assembly — moot, character fails
  the take regardless.
- G1 character: FAIL — eye lock absent, design variant. An 8-sample
  tile (1s–8s) shows small round DOT eyes throughout the vocal
  window, never ovals; the head is egg-shaped rather than ball, and
  the mouth is a wide grin with drawn corner creases — a visibly
  different face design from every kept take, consistent across the
  whole take (not a blink, not a transient). This is not the S30 t2
  failure (human-like lidded eyes) — the dots are cartoon, lidless,
  no white — but the parent's lock definition is "small solid black
  oval eyes," and dots are not ovals. Note for the parent:
  POSE_CARDS.md says "two round dot eyes" while every vehicle says
  ovals — a doc discrepancy. If the parent rules dots acceptable,
  this take passes (delivery, ratio, motion all pass); QC verdict is
  FAIL on the vehicle/parent lock definition.
- G2 text: PASS. Plain corner walls, no shops, no signs, no legible
  text anywhere.
- G4 performance window: PASS on staging (lean present, mouth open
  mid-line at 2s/5s, arms open post-line at 8s, matching the plan) —
  the miss is character, not staging.
- Frame gate: PASS with disclosure. Word-window vocal mean diff 1.053;
  longest <0.5 run in vocal window 19f (3.50–4.29s), entirely inside
  the inter-phrase gap (3.58–4.62) — disclosed, under the 24f gate.
  The 31f run at 7.96–9.25s is entirely post-line rest (line ends
  7.78) — disclosed.
- Specs: 1280x720/24fps, 10.000s, md5 7613688c9b2bec3a7cc51d667d8454ab.
- Reroll: CHARACTER axis for volley 10 — same delivery, eye lock
  restated and strengthened toward OVALS (the S30 t3 strengthened
  spec is the proven vehicle shape: it produced open ovals). First
  attempt, so reroll budget is open.

## S37 t1 — SEQUENCE PASS, RATIO CLEAR MISS, SLOT NOTE (assembly decision, no reroll) [confirmed]

- Lyric sequence: PASS (mantra, no count). L38 carries no count in
  the timeline, so the test is correct mantra content across the
  take: "I am your dad" x2 in two bursts — burst 1 0.00–~2.25, burst 2
  4.00–5.82. Full-clip heard both bursts; slice recheck of 5.50–9.00
  recovered only an "and" tail artifact (5.50–6.14), not a third
  repeat. RMS confirms no third burst (low-level 0.02–0.04 room tone
  after 6.00, no burst). No wrong words. The burst-and-hold shape is
  the disclosed S31–S33 class.
- Ratio: slot 16.36s (L38 322.08–338.44) / line 5.82s = 2.81 — far
  outside grey. SLOT NOTE (S25 precedent): even a perfect full-take
  ~9.5s delivery gives 16.36/9.5 = 1.72, still a clear miss — no
  single take can fill this slot under the 1.5x warp cap. This is an
  ASSEMBLY decision (mantra bed-cut/loop or structural cover),
  independent of any reroll. No reroll is recommended: a pacing
  reroll cannot land in band, and the content is already correct.
- G1 character: PASS with disclosure. Ball head, small solid black
  oval eyes, no white showing at 2s/5s, suit + cadmium tie, street
  corner set matches the plan. The 8s frame shows eyes CLOSED — but
  the line ends 5.82, so 8s is ~2.2s post-line: a rest-beat eye
  close, not a vocal-window lock break (contrast S30 t2, where lids
  covered the whole vocal window).
- G2 text: PASS. Plain corner wall, no shops, no signs, no legible
  text anywhere.
- G4 performance window: PASS. Facing camera, mouth open mid-mantra
  at 2s/5s; 8s smile is post-line rest.
- Frame gate: PASS with disclosure. Word-window vocal mean diff 0.957;
  longest <0.5 run in vocal window 22f (1.58–2.50s), straddling the
  burst-1 tail into the inter-repeat gap — under the 24f gate. The
  26f full-take run at 5.33–6.42s straddles the line end (5.82) into
  post-line rest (only ~11f of it falls during the final word) —
  disclosed, same post-line-hold class as S22/S25.
- Specs: 1280x720/24fps, 9.000s, md5 090edb91e3542e5eb9917e1912d11445.
- Owed: NO REROLL. Parent/assembly decision on outro-mantra coverage
  (bed-cut/loop vs structural cover) at assembly time, same as the
  S25 slot note. This take stands as assemblable mantra material.

## Volley-9 tally

KEEP: S28 t3 (grey 1.57), S34 t1 (usable 1.15). REJECTED: S30 t3
(delivery, middle phrase missing — character FIXED, parent
adjudication owed), S35 t1 (delivery, x2 of x4), S36 t1 (G1 eye drift,
dot eyes never ovals). ASSEMBLY DECISION (no reroll): S37 t1 (mantra
content PASS, ratio 2.81 clear miss, slot unfillable by design).
UNFIRED: none — 6 attempts, 6 landed, 0 failed. No take was warped
in this volley.

Pattern: the axis-churn class — S30 now has three takes each breaking
something different (t1 delivery tail, t2 character eyes, t3 delivery
middle). The strengthened eye spec WORKS (t3 eyes pass), so character
is no longer the open question for S30; delivery is, in a new shape
(dropped middle, not dropped tail). Second pattern: the face-design
variant class — S36 proves a take can pass delivery, ratio, and motion
while presenting a different face (dot eyes, egg head). The lock
definition (ovals) is doing real work here; the POSE_CARDS "dot eyes"
wording should be reconciled with the vehicle "oval eyes" wording
before volley 10, or the S36 reroll vehicle will re-import the
ambiguity. Third pattern: the unfillable-slot class now has two
members (S25's 19.66s slot, S37's 16.36s slot) — both need assembly
coverage decisions, not more pulls.

Volley-10 arithmetic (for the parent, NOT fired here): S35 t2
(DELIVERY) + S36 t2 (CHARACTER) + S38 t1 + S39 t1 = 4 takes; plus
S30's parent decision (t4 DELIVERY reroll → 5 takes, or structural
→ 4 takes). S37 needs no slot. Do not fire volley 10 from this
document — parent decision first (S30 adjudication + S36 dot/oval
ruling if the parent disagrees with the FAIL).
