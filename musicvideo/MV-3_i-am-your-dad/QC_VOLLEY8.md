# MV-3 QC — Volley 8 rows

Method: faster-whisper base on take audio (RAW words, mishear classes noted);
frames at 2s/5s/8s in qc8/ (widened where reads disagreed: S23 t2 to
2s/3s/4s/5s/6s/7s/8s for the mid-take eye narrowing; S30 t2 to a full
1s–8s tile for the eye lock); motion from 160x90 gray frame diffs.
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
measured. Mantra rule for S31–S33: L34 is cut on beats, not repeats
at assembly, and no repeat count was prompted for the thirds — the
sequence test for a mantra third is correct mantra content delivered
across the take, not a count; inter-repeat holds are disclosed, not
failed, per the S22/S25 gap precedents.

## S23 t2 — KEEP (grey) [confirmed]

- Lyric sequence: PASS. Full L25 exactly once, in order, 0.00–8.78:
  "You can close your eyes, you can plug your ears, the words still
  bounce around inside your head" ("word" for "words" is a trivial
  plural mishear, same word — not a fail, same as t1). RMS confirms
  silence after 8.78 (8.75–9.00 0.0056 → flat): unlike t1, this take
  carries NO non-word held-tail energy past the last word, so the
  line is words-only at 8.78s with no grey-rescue ambiguity.
- Ratio: slot 13.36s (L25 168.76–182.12, LYRIC_TIMELINE.md [confirmed])
  / line 8.78s = 1.52 → GREY. Warp 1.22x to the 1.25 edge at assembly.
  The PACING reroll moved the take from t1's 1.67 clear miss into
  grey — the axis is fixed.
- G1 character: PASS with disclosed nit. Ball head, suit, cadmium tie
  throughout. Eyes narrow intermittently mid-take (3s, 5s, 6s samples)
  but return to open small solid black ovals at 2s/4s/7s/8s and NEVER
  show white sclera — a speaking squint pattern, not a lock break.
  The 3s mouth-closed smile is a word-boundary still ("plug"
  2.98–3.28), not a deadpan break.
- G2 text: PASS. Bare room, plain walls, no legible text anywhere.
- G4 performance window: PASS. Facing camera at 2s/5s/8s, mouth open
  mid-line; hands-near-head beat present at 8s (never covering the
  mouth).
- Frame gate: PASS. Word-window vocal mean diff 1.789; longest <0.5
  run 5f (4.25–4.46s).
- Specs: 1280x720/24fps, 10.000s, md5 e5cfc9aff82190325866f4a04db8d012.

## S28 t2 — REJECTED, pacing (ratio clear miss) [confirmed]

- Lyric sequence: PASS. The DELIVERY axis is fixed: BOTH lines exactly
  once, in order — L30 "I don't need a story, I don't need a name,
  just the one short claim that never changes" 0.00–5.26, then L31
  "You wake up tomorrow and the first thing you hear is the old man
  saying it crystal clear" 5.46–8.92. RMS confirms silence after 8.92
  (9.00–9.25 0.0157 → flat): no further content.
- Ratio: slot 14.58s (L30+L31 230.52–245.10, combined span per the
  volley-7 method) / line 8.92s = 1.63 → ABOVE the 1.60 grey top by
  0.03 → CLEAR MISS. The take rushes L31 in particular (3.46s sung
  against a 6.86s song span). Disclosure for the parent: warp to the
  1.25 edge needs only 1.31x (within cap) — the parent may rule
  grey-rescue, but the method verdict stands (same discipline as the
  S23 t1 ruling, where the parent upheld the band verdict).
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing, suit + cadmium tie; bedroom-doorway set matches the plan
  (morning light, doorway), lean-in present (P-LEAN).
- G2 text: PASS. Framed pictures on the wall carry no legible text.
- G4 performance window: PASS. Facing camera, mouth open mid-line at
  2s/5s/8s.
- Frame gate: PASS. Word-window vocal mean diff 1.063; longest <0.5
  run 8f (1.46–1.79s).
- Specs: 1280x720/24fps, 10.000s, md5 6da841cd6dae294dc6e0caaf3e92e397.
- Owed: PACING reroll (t3) — both lines slower, spread across the full
  take. A line of ≥9.11s lands grey (a full-take ~9.5s delivery gives
  ~1.53). This is the first reroll on the pacing axis; delivery is
  proven and is not re-opened.

## S30 t2 — REJECTED, G1 eye drift [confirmed]

- Lyric sequence: PASS. The DELIVERY axis is fixed: full L33 exactly
  once, in order, 0.00–7.74, INCLUDING the tail phrase t1 missed —
  "I am your dad, you're hearing once, you're hearing twice, now it
  lives inside." RMS tail check confirms no extra words (decaying tail
  to ~8.50, flat after).
- Ratio: slot 7.28s (L33 251.04–258.32) / line 7.74s = 0.94 → USABLE.
- G1 character: FAIL — eye lock absent. An 8-sample tile (1s–8s)
  shows half-lidded, human-like eyes throughout the vocal window
  (1s/2s/3s/4s/5s/6s/7s) and closed eyes at 8s (post-line smile);
  small solid black ovals NEVER appear. This is not a blink — the
  widened sample never resolves to the lock, unlike S23 t2's
  intermittent narrowing, which returns to open ovals. Ball head,
  suit, cadmium tie, mic and corner set are all correct; the eyes
  alone fail the take. The reroll fixed delivery but broke character.
  Restating the eye line in the vehicle did not hold the lock here.
- G2 text: PASS. Plain corner walls, no legible text anywhere.
- G4 performance window: mic + corner set match the plan (P-CROON),
  mouth open mid-line — but G1 fails the take regardless.
- Frame gate: PASS on motion. Word-window vocal mean diff 1.406;
  longest <0.5 run 0f. The failure is character, not motion.
- Specs: 1280x720/24fps, 9.000s, md5 1c3bd992955306cda830db033ddfae99.
- Owed: CHARACTER reroll (t3) — same delivery, eye lock restated and
  strengthened. Parent may alternatively rule disclosed-keep (MV-2 v6
  precedent: a disclosed character inconsistency shipped at assembly),
  but the QC verdict is REJECT. If t3 fails character again, the
  character axis has two denials and S30 goes structural — parent
  adjudication at that point.

## S31 t1 — KEEP (grey) [confirmed]

- Lyric sequence: PASS (mantra third — see method note). Mantra
  delivered, correct content, 3 repeats in three bursts: burst 1
  0.00–1.74, burst 2 2.58–4.54, burst 3 4.92–6.30 full-clip, with the
  slice recheck (6.00–9.00) recovering only the "dad" tail to 6.58.
  RMS flat after ~6.75: no further repeats. No wrong words, no
  count defined or missed.
- Disclosure (honest shape note): the take does NOT roll continuously
  to the take's end as the vehicle asked — it chants x3 in bursts
  with inter-repeat holds (gaps ~2.25–3.00, ~4.75–5.00) and stops
  ~2.4s before the 9s take ends. The gaps are disclosed-pass class
  per the S22/S25 precedents, and motion never near-stills through
  them (longest <0.5 run 0f) — the performer stays alive in the
  holds. Assembly cuts this third on beats, not repeats; the take
  supplies 6.58s of mantra material for the 10.18s third.
- Ratio: slot 10.18s (258.32–268.50) / line 6.58s = 1.55 → GREY. Warp
  1.24x to the 1.25 edge at assembly.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing, suit + cadmium tie; doorway set matches the plan; held
  smile at 8s is the post-line rest beat (line ends 6.58).
- G2 text: PASS. Doorway, plain walls, no legible text anywhere.
- G4 performance window: PASS. Mouth open mid-mantra at 2s/5s.
- Frame gate: PASS. Word-window vocal mean diff 1.316; longest <0.5
  run 0f.
- Specs: 1280x720/24fps, 9.000s, md5 9effd40a9553d26c2ac5374c2dc5c985.

## S32 t1 — KEEP (grey) [confirmed]

- Lyric sequence: PASS (mantra third). Mantra delivered, correct
  content, 3 repeats in three bursts. Full-clip Whisper heard only
  burst 1 (0.00–1.82) and dropped bursts 2–3 — slice rechecks
  recovered both before any verdict: burst 2 "I AM YOUR DAD"
  3.50–5.54 (slice 3.50–6.25; RMS burst ~3.75–6.00), burst 3 "I am your
  dad." 6.00–7.68 (slice 6.00–9.00; RMS burst ~6.25–8.25). RMS shows the
  three-burst structure cleanly. No wrong words.
- Disclosure (same shape note as S31): bursts with inter-repeat holds
  (gaps ~2.25–3.75, ~6.00–6.25), stops 1.32s before the 9s take ends —
  not a continuous roll. Gaps are disclosed-pass class (S22/S25).
- Ratio: slot 10.00s (268.50–278.50) / line 7.68s = 1.30 → GREY. Warp
  1.04x to the 1.25 edge at assembly.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing, suit + cadmium tie; speaker wall set matches the plan,
  lean-in present (P-LEAN).
- G2 text: PASS. Speaker grille/knobs carry no legible text.
- G4 performance window: PASS. Mouth open mid-mantra at 2s/5s; 8s
  open-mouth smile is the post-line rest beat (line ends 7.68).
- Frame gate: PASS with disclosure. Word-window vocal mean diff
  1.063; longest <0.5 run 12f (2.42–2.92s), entirely inside the
  inter-burst gap, under the 24f gate.
- Specs: 1280x720/24fps, 9.000s, md5 5c349aca13242a9b460bf02a0c1d8340.

## S33 t1 — KEEP (grey) [confirmed]

- Lyric sequence: PASS (mantra third). Mantra delivered, correct
  content, 3 repeats in three bursts. Full-clip Whisper heard only
  burst 1 (0.00–1.86) and dropped bursts 2–3 — slice rechecks
  recovered both before any verdict: burst 2 "I am your dad"
  3.50–5.62 (slice 3.50–6.25; RMS burst ~3.75–6.00), burst 3 "I am your
  dad." 6.00–7.22 (slice 6.00–9.00; RMS burst ~6.00–7.50, decaying tail
  to ~8.50, flat after). No wrong words.
- Disclosure (same shape note as S31/S32): bursts with inter-repeat
  holds (gaps ~2.25–3.75, ~5.62–6.00), last word 7.22 of a 10s take —
  not a continuous roll. Gaps are disclosed-pass class (S22/S25).
- Ratio: slot 9.30s (278.50–287.80) / line 7.22s = 1.29 → GREY. Warp
  1.03x to the 1.25 edge at assembly.
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing, suit + cadmium tie; living-room set matches the plan;
  held smile at 8s is the post-line rest beat (line ends 7.22).
- G2 text: PASS. Living room, no legible text anywhere.
- G4 performance window: PASS. Mouth open mid-mantra at 2s/5s.
- Frame gate: PASS with disclosure. Word-window vocal mean diff
  0.789; longest <0.5 run 20f (2.13–2.96s), entirely inside the
  inter-burst gap, under the 24f gate.
- Specs: 1280x720/24fps, 10.000s, md5 16d7bd942c808553fd3fe8613c811536.

## Volley-8 tally

KEEP: S23 t2 (grey), S31 t1 (grey), S32 t1 (grey), S33 t1 (grey).
REJECTED: S28 t2 (pacing, ratio 1.63 clear miss → PACING reroll t3),
S30 t2 (G1 eye drift → CHARACTER reroll t3). UNFIRED: none — 6
attempts, 6 landed, 0 failed. No take was warped in this volley.

Pattern: the burst-and-stop shape now covers all three mantra first
attempts (S31/S32/S33 each chant x3 in bursts, hold, stop) — the same
deterministic model shape as the repeat-drop class, now on lines with
no count at all. Continuous-roll / counted wording does not change
it; the model sings in bursts and stops. The mantra thirds are kept
grey because assembly cuts L34 on beats, not repeats, and the takes
supply assemblable mantra material — but the parent should know the
thirds will show hold-beats between repeats. If the parent prefers
strict continuous-roll delivery, S31–S33 fail together and the volley
arithmetic below changes. Second pattern: the eye lock is not held by
restating the eye line — S30 t2 proves a reroll can fix delivery and
break character in the same take.

Volley-9 arithmetic (for the parent, NOT fired here): owed work is
S28 t3 (PACING) + S30 t3 (CHARACTER) + S34–S39 first attempts = 8
takes over the 6-cap. Fits only if the parent rules S28 grey-rescue
(1.31x warp, within cap) and/or S30 disclosed-keep, or by splitting
across two volleys (e.g. volley 9 = S28 t3 + S30 t3 + S34–S37, volley
10 = S38–S39). Do not fire volley 9 from this document — parent
decision first.
