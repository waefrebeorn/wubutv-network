# Character takes on a talking rig — anticipation, pop, settle

Source read in full this run: School of Motion, *How to Animate Character "Takes"*
(schoolofmotion.com/blog/how-to-animate-character-takes, the Mogran rig article;
cross-read the animation-comedy chapter excerpt, Jean Ann Wright, *Write Your Way
into Animation and Games* ch. 5, and DigiCel's timing note "a held pose before a
movement can show thought"). Read 2026-11-28.

## The law

A **take** is an extreme reaction built from FOUR poses, not one expression:

1. **Start** — after the character has seen/heard/realised something (neutral).
2. **Anticipation** — the *opposite* of the pose to come: head DOWN, shoulders up,
   eyes closing. Anticipation is a smaller movement in the opposite direction.
3. **Accent** — the most exaggerated version of the new expression. In punchy
   animation the audience *feels* this pose more than sees it, because it is popped
   into and out of in a single frame.
4. **Settle** — a less exaggerated version of the accent. **This is the pose the
   viewer actually reads** as the new attitude; it is the one that holds.

Timing, two published formulas at 24 fps:

| variant | start→anticipation | anticipation→accent | accent→settle |
|---|---|---|---|
| Basic | ~90% ease IN, **4 frames** | linear, **7 frames** | ~70% ease IN, **7 frames** |
| Warner Bros | ~90% ease IN, **6 frames** | **pop, 1 frame** | ~70% ease IN, **7 frames** |

Two variations worth keeping: "anticipation to the anticipation" (an extra pose that
absorbs the news before the take starts) and "holding the accent" (a moving hold on
the accent, better for fear/anger than a 1-frame pop).

## What this changed on the clean rig

`make_audio_cartoon.py` now writes `take: [a0, a1, a2]` (anticipation start, pop
frame, settle reach) and `clean_render.py` renders the four poses: head group
translation `-0.024 → +0.042 → +0.026` world (4.0 → 7.1 → 4.4 px at 540x960), eye
plate closed to a slit on the dip and reopened on the pop, brow lift at
`BROW_LIFT*BROW_POP` (0.022*2.4) on the accent relaxing to 0.60 of that in the
settle. Bob is multiplied by 0.25 inside the take so the pop is not cancelled by
breathing.

- **The take must eat into the authored stillness.** First build bound `a0 =
  max(still_end, button-6)` and the still ended ON the button, so the anticipation
  had **one frame** and no read (`TAKE frames [306, 307, 314]`). Correct form: keep
  >= 0.35 s of hold, then hand the last 6 frames of the pause to the dip
  (`still [287,300]`, `take [300,307,314]`). Freeze -> dip -> pop is one continuous
  beat, and the dip is the movement *out* of the freeze, not a second action.
- **Measured on the shipped 350-frame clip** (Suno cut, 14.6 s): brow band 218-228
  at rest -> 220-230 at the end of the dip (eyes closed to slits at f305) -> 203 at
  the pop (f308) -> 207 settled through f340. Net +15 px up at the pop, +11 px
  settled, all vertical translation; the brow bar never rotates.
- `FRAME_TO` was added to `clean_render.py` so a take window can be rendered and
  measured (40 frames, ~30 s) before committing the full pass. `take_measure.py`
  prints brow rows / eye-plate pixels / mouth band per frame.

## The still window: ramps belong OUTSIDE it

`STILL_REST` (jaw eased to a rest contact during the word-gap hold) was logged last
run as "fixes the hold, breaks the sync gate". Both halves are measurable and the
resolution is where the ramp lives:

| build | session r_ex | still vs speech (face box) |
|---|---|---|
| no clamp | 0.962 | — (jaw keeps singing) |
| rest 0.18, 3-frame ramp INSIDE the window | 0.948 | 38.6 % FAIL |
| rest 0.28, ramp 4 frames BEFORE / 2 after | 0.950 | 0.0 % PASS |
| rest 0.40, ramp outside | 0.960 | — |

A 3-frame ease in and out *inside* the "still" is 6 of 13 frames of motion, which is
why the hold measured 38.6% of speech motion even though the pose was authored
frozen. Settle the jaw before the window opens and release it after it closes and
the interior is byte-identical between frames (face-box mean |diff| exactly 0.000
over 11 frame pairs). Whole-frame `beat_qc` then read still 0.013 vs speech 0.070 =
19% PASS (was 83% FAIL).

Residual, stated rather than hidden: at rest 0.18 the clamp costs the correlation
gate (session r_ex 0.930, encoded r_x would sit near the 0.90 line), because the
band envelope is loud through an instrumental fill while nobody sings. Shipped at
0.28, where encoded r_ex = 0.921 and the mouth visibly shuts (23 px -> 12 px). The
instrument conflict is the real story: `qc_cartoon` scores the pause against the
music bed, not the vocal.

## Reusable rules

- A take is four poses; drawing only the accent leaves the viewer with a face change
  and no performance.
- The anticipation is the opposite pose and it is what makes the pop read.
- Use the Warner Bros 6/1/7 timing when the accent must be *felt*; the 4/7/7 basic
  timing when the reaction is subtle.
- Bind the take to the frame where the pause ends (the first loud frame after the
  authored still), never to a word index: ASR stamps drift 0.2-0.5 s.
- The settle holds to the end of the clip; the take is the last thing the viewer
  sees, so it must not be interrupted by a blink (last 8 frames already suppress it).
