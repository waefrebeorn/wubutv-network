# V6 timing adjudication — triple devil's advocate, 2026-11-02

Sources: research report + devils-advocate.md in
`~/workspace/research_notes/video-generation-timing-methods-20261103-0233/`.
Full cut plan: MV-2 project `V6_10S_CUT_PLAN.md`.

- Pacing words: directional only. No 2-3.4x compression evidenced.
  Volley 1 is a selection test, not a promised fix.
- Word timing inside one T2V shot: model-internal (narrow claim
  stands). Shot/beat steering exists elsewhere (Kling multi-shot,
  Seedance 2.5 timestamps, Pikaframes transitions); true word
  timing needs audio-driven lip-sync or performance capture —
  escalation only, with user go-ahead.
- Line band survives for clear misses (<0.60x / >1.60x).
  Grey zone 0.60-0.80x / 1.25-1.60x: forced-align against
  lyrics.txt before calling a miss. Never QC on raw Whisper alone.
- Motion gate is primary: frozen/halted motion is visible with
  no transcript and is what the user rejected.
- 10s-fit + proper cuts: no segment over 10s, hard cut on a
  word/line boundary, split >10s lines at phrase/breath
  boundaries before generation. MV-2's only >10s line is S06
  (12.70s), split into S06a 57.92-63.60 and S06b 65.02-70.62.
