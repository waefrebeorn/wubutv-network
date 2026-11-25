# MV-19 — VOLLEY PROGRESS

Plan: 36 scenes (SCENE_PLAN.md). Pilot = S01/S09/S11 (template test).
Then volleys of ≤6: V1 S02–S06+S08 · V2 S07+S10+S12–S14 · V3 S15–S20 ·
V4 S21–S26 · V5 S27–S31 · V6 S32–S36. Spares/refires as QC rules.

## PILOT — fired 2026-11-14, QC DONE
- S01 t1 KEEP (G7 1.0, motion PASS, G2 clean).
- S09 t1 REJECT — JUN leaked in from ref_flat edge. LESSON: ref_flat
  vehicles must stage JUN explicitly or the scene goes on ref_kit.
- S11 t1 REJECT (motion) — idle too subtle (run 66f). LESSON:
  "standing" vehicles need amplified whole-body motion in the text.
- Refires S09 t2 (ref_kit, solo) + S11 t2 (amplified idle) ride with
  Volley 1.

## VOLLEY 1 — QC DONE: S09t2 KEEP · S11t2 KEEP* (zoom-lift) ·
S02 KEEP · S03 REJECT (motion, refire t2 with Volley 3) · S04 KEEP ·
S05 KEEP. Coverage: 7/36 (S01, S02, S04, S05, S09, S11 + S03 owed).

## VOLLEY 2 — QC DONE: S06 KEEP* (zoom-lift) · S08 KEEP · S07 KEEP ·
S10 KEEP · S12 KEEP · S13 KEEP for L16 only (L17 not sung → scene
split, S13B created). Coverage: 12/37 scenes (S01, S02, S04–S13,
S13B owed, S03 owed).

## VOLLEY 3 — QC DONE: S03t2 KEEP · S14 KEEP · S15 REJECT (G2
"Milk" label + 79f plant; refire t2 in Volley 4) · S16 KEEP ·
S17 KEEP · S13B KEEP. Coverage: 17/37 (S15 owed).

## VOLLEY 4 — QC DONE: S15t2 KEEP · S18 KEEP · S19 REJECT (held
shrug, refire t2 in Volley 6) · S20 KEEP · S21 KEEP* (push-in) ·
S22 KEEP. Coverage: 22/37 (S19 owed).

## VOLLEY 5 — QC DONE: S23 REJECT (event miss + JUN leak; restaged
Spawn Pop) · S24 KEEP · S25 KEEP L31 only (split → S25B) ·
S26 KEEP · S27 KEEP* (fragment-chunk conform) · S28 KEEP L35+L36
(split → S28B). Coverage: 27/39 (S19, S23, S25B, S28B owed).

## VOLLEY 6 — QC DONE: S19t2 KEEP L22 only (split → S19B) ·
S23t2 REJECT (plant; refire t3 continuous arc) · S25B KEEP ·
S28B KEEP · S29 KEEP* (push-in) · S30 KEEP.
Coverage: 33/40 (S19B, S23 owed).

## VOLLEY 7 — QC DONE: S19B KEEP · S23t3 KEEP* · S31 REJECT (cast:
4 copies + male teal figure) · S32 KEEP · S33 KEEP* · S34 REJECT
(motion: exits too slow).
## VOLLEY 8 — QC DONE: S35 KEEP · S36 KEEP.
Coverage: 38/40 (S31, S34 owed).

## VOLLEY 9 (pickups) — QC DONE: S34t2 KEEP (poster flaw disclosed);
S31 needed t3 (REJECT cut/cast), t4 (REJECT cast/motion), t5 KEEP
(marching trio on ref_kit).
**COVERAGE COMPLETE: 40/40 scenes.** Generation closed — 41 video
fires + 3 image fires, zero 429s. Next: conform → assembly → gates.

## BUILD COMPLETE — 2026-11-14
Conform: 93 chunks, 40 segments, 3686 frames exact.
Assembly: single pass; joined.mp4 probed 3686f before encode.
House master: masters/mv19_confused_npc_16x9.mp4 md5
42877939fa568a630e1dee9ac6a0ceea (3686f / 153.600s, CRF 18 SEI
verified, AAC 48k, faststart). Chat copy:
masters/mv19_confused_npc_chat.mp4 md5 b56d551f37b433771659b991190a7ee5
(46,105,391 B). Gates: audio agreement 0.99927 / worst-10s 0.99872;
zero-still PASS (worst run 3f); G7 all shipped ≥0.89. Full detail:
GATE_LOG.md, CUTLIST.md, MUSIC_VIDEO_LEDGER.md. Awaiting parent
delivery (flag + commit are the parent's).
