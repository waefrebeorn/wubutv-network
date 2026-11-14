# MV-3 Volley 10 QC — 2 KEEP, 2 REJECTED, 0 failed

Volley 10 (final volley): S35 t2 (DELIVERY reroll) + S36 t2 (CHARACTER
reroll) + S38 t1 + S39 t1 (first attempts, outro + finale). All four
landed; no take failed to generate. Cap 6, 4 used — no volley 11 fired
from this document.

Method: faster-whisper base on take audio (RAW words, mishear classes
noted; numpy array input — the venv's av decode path is broken, see
qc10_analyze.py; NOTE: qc10_analyze.py originally shared one /tmp wav
across parallel runs and cross-contaminated two transcripts — fixed
mid-volley to per-take temp files, and the two affected takes (S36 t2,
S38 t1) were re-transcribed sequentially to confirm their own audio).
Frames at 2s/5s/8s in qc10/ (widened where the axis turned on the
face: S36 t2 and S38 t1 to full 1s–8s tiles). Motion from 160x90 gray
frame diffs.
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
One axis per reroll verdict. All four takes 1280x720/24fps, durations
measured. Mantra rule: L36 is a COUNTED line (x4 prompted), so the
S31–S33 thirds' content rule does not cover it; L40 carries no count
in the timeline, so its sequence test is correct mantra content
across the take, not a count (same class as S37's L38).

## S35 t2 — REJECTED, delivery (x2 of x4, repeat-drop again)

- Lyric sequence: FAIL (incomplete delivery). Prompted line is L36,
  "I am your dad" x4 (count prompted in the vehicle and the timeline).
  Full-clip Whisper heard only burst 1 (0.00–1.94); slice recheck of
  2.00–10.00 recovered burst 2 ("I am your dad." ~4.25–6.28) before
  any verdict, per the split-half rule. A further slice of
  6.00–10.00 heard only a "head." fragment (6.00–6.68, burst-2 tail),
  no third or fourth repeat. RMS confirms the two-burst structure
  cleanly (burst 1 ~0.25–1.94, flat 2.00–4.25, burst 2 ~4.25–6.25,
  flat after 6.50). Two repeats missing. This is the repeat-drop
  shape exactly as t1 and S25 t1 (x4→x2) — the delivery-wording
  change (four FULL repeats, none cut short) did not move the shape.
  The counted-line rule governs: the mantra-thirds content rule is
  NOT extended to L36.
- Ratio: slot 11.86s (L36 296.70–308.56) / line 6.28s = 1.89 — clear
  miss, moot — sequence gates first. NOTE: unlike S37, this slot IS
  fillable — a full-take ~9.5s x4 delivery lands ~1.25, in band — so
  a t3 would be meaningful. But no volley 11 is authorized in this
  task: t3 is owed in principle (t2 is only the first denied reroll)
  and falls to the parent — order a volley 11, or rule S35 structural
  (assembly-covered, master carries L36, same as S04/S05/S21/S24/S25/
  S30).
- G1 character: PASS. Ball head, small solid black oval eyes, no white
  showing, suit + cadmium tie; living-room set matches the plan.
- G2 text: PASS with note. Bookshelves/framed pictures blurred, no
  legible text anywhere.
- G4 performance window: PASS on staging (mouth open mid-mantra at
  2s/5s; 8s held smile is post-line rest, line ends 6.28) — the miss
  is delivery, not staging.
- Frame gate: PASS on motion. Word-window vocal mean diff 1.160;
  longest <0.5 run in vocal window 1f. The 36f full-take run at
  8.46–9.96s is post-line rest, disclosed.
- Specs: 1280x720/24fps, 10.000s, md5 39f77d6d4f00c5b7225775edb987d242.

## S36 t2 — KEEP (grey) — CHARACTER axis FIXED

- Lyric sequence: PASS. Full L37 exactly once, in order, 0.00–8.30:
  "All of you, every single one, I am your dad, you know it now."
  (Re-transcribed sequentially after the parallel-run temp-file
  contamination — confirmed its own audio.)
- Ratio: slot 11.56s (L37 309.88–321.44) / line 8.30s = 1.39 → GREY.
  Warp 1.11x to the 1.25 edge at assembly.
- G1 character: PASS — the CHARACTER axis is fixed. A full 8-sample
  tile (1s–8s) shows the big round ball head with large solid black
  OVAL eyes, wide open, no white, no lids, in every frame — never
  dots, never egg-shaped. The S30 t3 strengthened oval spec works a
  second time: t1's dot-eyes/egg-head variant is gone. Suit +
  cadmium tie, street-corner set. Arms open post-line at 5s–8s,
  matching the plan.
- G2 text: PASS. Plain corner walls, no shops, no signs, no legible
  text anywhere (red postbox and wall marks are objects, not text).
- G4 performance window: PASS. Facing camera, mouth open at speaking
  beats (1s/3s/5s/6s/8s); smiles between phrases are speaking
  rests, not stills.
- Frame gate: PASS with disclosure. Word-window vocal mean diff
  1.212; longest <0.5 run in vocal window 27f at 3.25–4.38s. That
  run sits in the inter-phrase gap between "one." (ends 3.30) and
  "I" (starts 4.50) — only ~1f touches the tail of a word — the
  S37 straddle class, not frozen motion during singing.
- Specs: 1280x720/24fps, 9.000s, md5 7f0e4eec9a20bea17cb020f61f86b4e0.

## S38 t1 — REJECTED, G1 eye drift (dot eyes, never ovals)

- Lyric sequence: PASS. Full L39 exactly once, in order, 0.00–7.14:
  "Say it back to me, I am your dad, say it to yourself."
  (Re-transcribed sequentially after the parallel-run temp-file
  contamination — confirmed its own audio; the first parallel pass
  had returned S36's words.)
- Ratio: slot 5.36s (L39 338.55–343.91) / line 7.14s = 0.75 → GREY.
  Warp 0.94x to the 0.80 edge at assembly — moot, character fails
  the take regardless.
- G1 character: FAIL — eye lock absent, design variant. A full
  8-sample tile (1s–8s) shows small round DOT eyes throughout the
  vocal window, never ovals, and the head elongated/egg-shaped and
  tilted — a visibly different face design from every kept take,
  consistent across the whole take (not a blink, not a transient).
  This is the S36 t1 failure class exactly, and the parent already
  upheld that FAIL in volley 9 (dots are not ovals; POSE_CARDS
  reconciled). S38 t1 used the standard vehicle, not the
  strengthened oval spec — a t2 carrying the S30 t3 strengthened
  spec (proven twice now: S30 t3, S36 t2) is the indicated reroll.
  But no volley 11 is authorized in this task: t2 is owed in
  principle (t1 is a first-attempt fail, not a denied reroll) and
  falls to the parent — order a volley 11, or rule S38 structural
  (assembly-covered call-and-response).
- G2 text: PASS. Street furniture, traffic lights, crosswalk, fire
  hydrant — objects, no legible text anywhere (background signs
  blurred beyond reading).
- G4 performance window: PASS. Point on the call (1s–4s), hand to
  ear post-line (5s–8s) — matches the plan exactly.
- Frame gate: PASS on motion. Word-window vocal mean diff 1.549;
  longest <0.5 run in vocal window 9f. The 34f full-take run at
  7.08–8.50s straddles the line end (7.14) into post-line rest —
  disclosed, post-line-hold class.
- Specs: 1280x720/24fps, 10.000s, md5 5d1ff4ab21c682c47fb3504c462aa883.

## S39 t1 — KEEP (mantra content PASS, ratio clear miss → assembly decision)

- Lyric sequence: PASS (mantra, no count). L40 carries no count in
  the timeline, so the test is correct mantra content across the
  take, not a count (S37 L38 class). Full-clip heard "I am your
  dad" 0.00–3.14; slice recheck of 3.00–9.00 heard only a "Yeah."
  fragment (3.00–3.62, burst tail), and fine slices of 5.50–9.00 /
  5.50–7.50 heard a soft non-lyric "ah" swell (5.50–7.18) / nothing
  — not a second mantra burst. RMS confirms the shape: strong
  vocal 0.25–3.75, low room tone 3.75–5.75, soft swell 5.75–7.00,
  low tone after. One full mantra burst, no wrong words, then the
  fade hold. The content is correct; the take does not invent
  lyrics or repeat the line wrongly.
- Ratio: slot 9.16s (L40 344.55–353.71) / line 3.14s = 2.92 — clear
  miss. ASSEMBLY DECISION (S37 class): the take stands as
  assemblable finale material — mantra burst + arms-open smile
  held for the fade — with bed-cut/loop or hold-cover at assembly
  time. DISCLOSURE, unlike S37: this slot IS fillable in principle
  (a ~9s delivery lands ~1.02), so a pacing reroll would be
  meaningful if the parent orders one. No volley 11 is authorized
  here; the KEEP stands unless the parent prefers the reroll.
- G1 character: PASS. Ball head, small solid black oval eyes, no
  white showing at 2s/5s/8s, suit + cadmium tie, street-corner set.
- G2 text: PASS. Brick wall, utility box, red pipe — objects, no
  legible text anywhere.
- G4 performance window: PASS. Facing camera, arms open, mouth open
  mid-mantra at 2s; 5s/8s held smile is the fade hold, not a
  still — the plan's final frame (smile held, rhyming with S01).
- Frame gate: PASS with disclosure. Word-window vocal mean diff
  0.725; longest <0.5 run in vocal window 14f (2.54–3.12s), under
  the 24f gate. The 57f full-take run at 2.54–4.92s straddles the
  line end (3.14) into post-line hold (only ~14f during the final
  word) — post-line-hold class, same as S22/S25/S37.
- Specs: 1280x720/24fps, 9.000s, md5 921b6d66b22908f8b380e9d1b9f7b342.

## Volley-10 tally

KEEP: S36 t2 (grey 1.39, character FIXED), S39 t1 (mantra content
PASS, ratio 2.92 clear miss → assembly decision, fillable-slot
disclosure). REJECTED: S35 t2 (delivery, x2 of x4 repeat-drop again
— t3 owed in principle, fillable slot, no volley 11 authorized),
S38 t1 (G1 eye drift, dot eyes + egg head across a full tile —
character reroll with the strengthened oval spec owed in principle,
no volley 11 authorized). UNFIRED: none — 4 attempts, 4 landed, 0
failed. No take was warped in this volley.

Active keeps now 30 (28 + S36 t2 + S39 t1). Structural set unchanged
pending parent decisions: S04, S05, S21, S24, S25, S30. S35 and S38
are REJECTED with rerolls owed in principle — the parent rules
whether they go structural (assembly-covered) or get a parent-ordered
volley 11. After those two rulings, all 39 scenes are resolved and
the build moves to assembly.

Pattern: the face-design variant class now has two confirmed members
(S36 t1, S38 t1 — dots + egg head, both on standard vehicles) and
two confirmed cures (S30 t3, S36 t2 — the strengthened oval spec
holds twice). Standard vehicles keep importing the variant on some
takes; the strengthened spec is the reliable shape for any future
character reroll. Second pattern: the repeat-drop class is now
three-for-three on counted lines (S25 t1, S35 t1, S35 t2 — x4→x2
every time, across two delivery wordings). Counted x4 lines do not
complete by generation wording alone; assembly coverage is the
reliable path if the parent declines a volley 11. Third pattern
(method note): parallel QC runs must never share a temp wav —
qc10_analyze.py now uses per-take temp files.
