# MV-8 Rebuild — SCENE PLAN v2 (17 scenes, 0.00–187.20, 4493f)

Governing brief: `MV8_REBUILD_BRIEF_2026-11-08.md`. Lyric onsets:
`work/rebuild/SONG_WORDS_v2.json` (135 words). Timeline:
`work/rebuild/LYRIC_TIMELINE_v2.md`. Crescendo:
`work/rebuild/CRESCENDO_MAP_v2.md`. Beat grid:
`work/rebuild/beat_grid_v2.json` (123.05 BPM, 368 beats, first 5.968).
Stills: `work/rebuild/stills/` (F00–F21 v2; F00_v2 + F16_v2 pending re-fire).
Asset bank: `work/rebuild/ASSET_BANK_v2.md`.

## Global contract (rebuild law)

- **4493 frames exactly** (187.200s @ 24fps). Frame counts below are the
  contract; assembly must land on 4493f — v1's +4f drift is a FAIL.
- **Adults only, everywhere.** Champion = adult woman (F_HERO_TEST_v2 anchor).
  Squire = adult man. Crowds = adults. No children in any frame, ever.
- **Every lyric line is SINGING:** Champion facing camera, mouth open on the
  line, performance-window staging; per-word warp anchors on VISIBLE mouth
  events (never take-audio words). A sung line gets a SUNG picture — never
  another character's mouth, never a closed-mouth cover (bad-word rule: fast
  cut on the nearest beat to montage for exactly the bad span, back at the
  next good word anchor).
- **Motion in every shot.** No frozen lead-in, no held-photo opening that
  snaps into motion, no designed held shot (v1's D-B precedent is DEAD).
  Every take must show continuous motion from its first frame.
- **Cuts on lyric onsets (primary grid) and beats (hint layer).** Montage cuts
  land ON beats; return cuts land ON word onsets.
- **Lilypad techniques, named per scene** (@pixhell: loose-prompt + strong
  curation, CRADLE SHOT; visual-forms: Critic loop, kinetic type, montage /
  collage, code-rendered counters, visualizer forms). One loose-prompt slot
  per volley (designated: H2-B). Critic loop runs on every visual (non-sung)
  slot: contact sheet → phone test → score 1–10 → fix worst 3 → repeat to 8+.
- **Two-image calls:** never lead with a 3:2 still (aspect lesson — output
  follows the FIRST image's aspect). Prefer single-anchor or 16:9-first order.
  1248x704 is the pipeline's near-16:9 plate.
- **Wardrobe lock (Stage 4 watch item):** full breastplate + long trousers /
  skirt in EVERY vehicle. The two-piece (F16/F20 v1) is NOT the lock.
- **F12 pupil-glyph watch item:** any take where the pupil reflection resolves
  into readable letters FAILS QC.
- **Kinetic layer (assembly, never generated in-clip text):** WIPE counter
  (WIPE 001…347, resets to WIPE 001 — CLEAN at ~183s in O-C); STILL THERE!
  slam at 112.25/112.72; sung-line words as kinetic type keyed to song word
  times. Star Guitar rule: each musical element gets a visual object.
- **Loop close:** final frame rhymes with F00; seam inside the flush vortex.

## Scene table

Frames are 0-indexed starts; end frame = start of next scene. True-peak frame:
159.435s × 24 = **frame 3826**.

| # | Scene | Span (s) | Frames | Type | Lyric lines (onset) | Anchors | Lilypad technique |
|---|---|---|---|---|---|---|---|
| 1 | IN-A "The Loop" | 0.00–5.97 | 0–143 (143f) | JOURNEY | — (instrumental) | F00→F01 | Cradle-establishing drift; code-rendered counter opens at WIPE 001 |
| 2 | H1-A "Still There" | 5.97–22.08 | 143–530 (387f) | SINGING | L1 7.98, L2 11.70, L3 16.12 + dirty echoes to 22.08 | F01→F02 | Performance-window; kinetic type on each line; brass-stab camera punches |
| 3 | H1-B "Brown Brown" | 22.08–34.96 | 530–839 (309f) | SINGING | L4 Browns 22.08, L5 24.74, L6 28.62, L7 30.98–34.96 | F02→F03 | Performance-window; Brown chant = visualizer-form pulse (5 browns = 5 pulses) |
| 4 | I-A "Inside the Sheet" | 34.96–45.51 | 839–1092 (253f) | SINGING→JOURNEY | L8 Browns 36.90–41.84, then no words | F03→F04 | Macro-world hold WITH ambient motion (fibre drift, never frozen); Brown chant = counter tick |
| 5 | I-B "The Gate" | 45.51–60.46 | 1092–1451 (359f) | JOURNEY | — | F04→F07 via F05/F06 | Montage/collage river flight; one whip per hit in the storm cluster 45.51–48.88; gate approach ends ON 60.43 |
| 6 | V-0 "Sitting on the Toilet" | 60.46–65.12 | 1451–1563 (112f) | SINGING | L9 60.46, L10 63.00 | F07→F08 | Performance-window, Champion seated on the porcelain throne at the gate, singing to camera; strongest hit 63.32s = throne-slam beat |
| 7 | PH-A "Wipe Again" | 65.12–67.26 | 1563–1614 (51f) | SINGING | L11 66.48 + "(Phantom)" tag ~65.60 | F08→F09 | Arming montage begins — pieces land on the five hits 65.25/65.74/66.21/66.70/67.07; kinetic "WIPE AGAIN" slam |
| 8 | H2-A "The Quest Begins" | 67.26–81.08 | 1614–1946 (332f) | SINGING | L12 67.38 + "Never clean" 69.36, L13 70.28, L14 73.00, L15 76.98–81.08 | F09→F11 via F10 | Performance-window; arming completes (F10 full armour + adult Squire), mounted departure; Critic loop on the departure shot |
| 9 | H2-B "World-Hop Reprise" | 81.08–93.00 | 1946–2232 (286f) | SINGING | L16 fragment 81.66 (contested), L17 85.98 | F11→F14 via F12/F13 | **LOOSE-PROMPT + STRONG CURATION slot** (one per volley); eye→pupil-canal journey; F12 glyph watch item ACTIVE |
| 10 | H2-C "Unclogging Quests" | 93.00–105.94 | 2232–2543 (311f) | SINGING | L18 95.52, L19 102.34–105.98 | F14→F16 via F15 | Performance-window; plunger-in-clog quest (F15), palace-gate quest (F16 v2); L19 head words uncertain — stage on the "never stops" tail |
| 11 | D-A "The Vortex Duel" | 105.94–112.25 | 2543–2694 (151f) | JOURNEY | Drop shout "Wipe" 105.94 (v1-only) | F16→F17 | **CRADLE SHOT** transition into the duel; serpent has NO goggles (rival-flyer read banned); continuous motion, no held shot |
| 12 | D-B "STILL THERE!" | 112.25–120.06 | 2694–2881 (187f) | JOURNEY | — (hit pair 112.25/112.72 = the "STILL THERE!" placement) | F17→F18 | Kinetic STILL THERE! slam on the hit pair; camera push on the serpent close — **motion throughout, v1's designed-held-shot precedent is DEAD** |
| 13 | FH-A "The Synchronised Flush" | 120.06–133.46 | 2881–3203 (322f) | SINGING | L20 120.06, L21 124.68, L22 127.18 + "Dirty" echo ~130.50–133.46 | F18→F20 | Performance-window; synchronised flush (F20) as the section's visual rhyme; loudest section energy |
| 14 | FH-B "The Brown Deep" | 133.46–146.00 | 3203–3504 (301f) | SINGING | L23 Browns 133.46, L24 136.40, L25 140.14, L26 142.66–146.02 | F20→F04 | Performance-window; pipe-flight victory lap (F04 reused deliberately); Brown chant = 5-pulse visualizer; L26 "(Phantom wipe)" tag ~142.66–144.18, core "Endless wipe forever" 144.18–146.02 |
| 15 | O-A "The Return Flight" | 146.00–163.00 | 3504–3912 (408f) | JOURNEY | — (instrumental) | F11→F02 | **CRADLE SHOT** into the vortex; **THE LOOP-THE-LOOP — biggest visual in the video — apex ON frame 3826 (159.435s, true peak −2.16 dBFS)**; see verification below |
| 16 | O-B "The Last Stand at the Cistern" | 163.00–180.00 | 3912–4320 (408f) | JOURNEY | — (instrumental) | F19→F20 | Colossus finale on the loudest cluster 170.9–174.7s (hits 170.92/171.85/173.77/174.24/174.72); district-by-district clean reveals on the stab run 177.11–180.56 |
| 17 | O-C "The Ghost Wipe + Loop Close" | 180.00–187.20 | 4320–4493 (173f) | JOURNEY | — (instrumental) | F21→F00 | Ghost Wipe reveal (F21); **WIPE 001 — CLEAN counter reset ~183s**; final frame rhymes with F00; seam inside the flush vortex |

Frame-count check: 143+387+309+253+359+112+51+332+286+311+151+187+322+301+408+408+173
= **4493f** ✓. Spans tile 0.00–187.20 with no gaps ✓.

## True-peak landing (O-A) — the hard requirement

- The loop-the-loop apex MUST be on screen at **frame 3826 (159.435s)**,
  322 frames into O-A (13.42s into the 17.00s scene).
- v1's failure, not repeated: v1's loop landed ~147–148.5s, 11–12s early.
- Stage 4 firing note for O-A: the take's internal timing must place the loop
  apex at 13.42s into the take (10s take → the take covering 146.00–156.00
  holds the approach; the take covering 156.00–163.00 holds the apex at
  3.435s in — OR a single 17s-equivalent assembled from two 10s takes with
  the cut placed so the apex lands on 3826; the firing coordinator chooses
  the split, the apex frame is non-negotiable).
- **Verification (assembly gate, stated here so Stage 4/assembly cannot miss
  it):** extract frame 3826 from the assembled master and eye-check that the
  loop apex is on screen; extract frames 3826±12 (±0.5s) and confirm the apex
  is the local motion extreme (frame-diff peak within the ±12f window centred
  on 3826, not offset). If the apex is off by more than ±6f (±0.25s), the
  O-A assembly is re-cut — no exceptions.
- Secondary peaks for the same treatment: strongest hit 63.32s (V-0, frame
  1520) and the loudest-cluster hits 170.92–174.72 (O-B) — verify by the same
  frame-extraction method at assembly; the true peak is the only one that is
  a hard gate.

## Lyric-link coverage (every line linked, or listed un-linkable)

All 26 lines L1–L26 + the Drop shout are linked above. **Un-linkable: none.**
Notes on the flagged lines and how the plan stages them:
- **L16 (81.66–83.74, contested):** staged as a hook-line repeat (Champion
  singing, H2-B) with a Brown-counter kinetic accent — works under either
  reading (hook fragment per v1, or "Brown brown (Still brown)" per sheet+B2).
- **L19 head words uncertain:** staged on the solid tail ("never stops",
  104.60–105.98); the take's mouth work is judged on the tail words.
- **L26 tag window (142.66–144.18):** staged as the "(Phantom wipe)" tag —
  a half-second Phantom-wipe flourish (Ghost Wipe flicker) before the
  "Endless wipe forever" core.
- **Outro (146.00–187.20):** no lyric lines exist to link; O-A/O-B/O-C are
  staged purely on the crescendo map (true peak, loudest cluster, loop seam).
  The sheet's Outro "Brown" is sheet-only, not performed — no line is
  invented for it.

## Casting decision (for parent review)

- **Champion = the adult woman of F_HERO_TEST_v2** (late-20s, braid, defined
  cheekbones/jaw, mouth open mid-song). She IS the voice made visible: every
  SINGING scene is her, facing camera, mouth open on the line. Identity anchor
  passed FIRST in every Stage 4 call showing her.
- **Squire = tall lanky grown man** (paper-white tabard). v1's small round
  TP-roll creature is RETIRED (reads young).
- **Crowds = adults only** (pipe-citizens, hooded canal figures, palace staff).
- **Mount "Sir Swirl"** (giant brown turd) and **Brown Ribbon Serpent**
  (no goggles) and **Clog Colossus** carried from v1, unchanged.
- **Worlds W1–W9 + props P1–P9** carried from v1 (see ASSET_BANK_v2.md).

## Timing contract (restated for Stage 4)

Master exactly 4493f / 187.200s. Cuts on lyric onsets (primary) + beat grid
(123.05 BPM, hint layer). True peak 159.435s = loop apex, frame 3826,
verified at assembly. No frozen-lead-in takes. Adults only. No generated
in-clip text. No licensed material.

## Stage 4 firing order (parent-approved order, once the plan is reviewed)

1. **Volley 1 (proof of look):** H1-A (the hook scene — SINGING proof) +
   IN-A + D-B (motion proof — the anti-held-shot scene).
2. Then journey order: H1-B, I-A, I-B, V-0, PH-A, H2-A, H2-B (loose slot),
   H2-C, D-A, FH-A, FH-B, O-A (true-peak scene — fire early enough to
   re-fire if the apex misses), O-B, O-C.
3. O-A's apex is verified per-take BEFORE assembly (take-level frame check
   at 13.42s into the O-A take) so a miss is caught at firing time, not
   at assembly.
