# MV-8 v3 — DETECTION GAPS v3

For the daily detection-research job (user order 2026-11-09 ~02:52
EST: "USE THE SONG AND FIND BETTER DETECTION METHODS EVERY DAY BY
RESEARCH PROJECTING ALL AVENUES NEW FINDERS"). These gaps BLOCKED a
verdict or a measurement during the v3 build. They are recorded here
so the research job can hunt methods — the build does NOT stall on
them (each gap lists the interim method used instead).

## GAP-1 — "Montage timing" has no direct metric (OPEN, recorded 2026-11-09)

- What we need: a measure of whether a montage cut FEELS locked to
  its beat — not just that the cut frame equals the beat frame
  (arithmetic, already exact), but that the incoming/outgoing shots'
  motion energy peaks ON the cut.
- Why it matters: the user's v2 verdict led with "bad montage
  timing". v2's cuts were placed on the grid and still read as badly
  timed — placement alone is not the percept.
- Interim method: cut frame = beat frame (±2f early allowed, C1);
  motion-energy check per segment (frame-diff mean in the 12f before
  and after each cut must both be non-trivial — a cut into or out of
  a still reads as a halt); eye review of the rendered master at 1x
  and 0.5x.
- Research avenues: motion-energy peak alignment (per-shot
  optical-flow / frame-diff curve vs beat grid); cut-point energy
  contrast metrics; existing MV edit-analysis tools; beat-tracking
  confidence per cut.

## GAP-2 — Singer-insert warp verification needs a mouth detector that works on warped renders (OPEN, recorded 2026-11-09)

- What we need: mouth-state read (open / transitional / closed) at
  word onsets on the WARPED insert render — not on the source take.
  Warping shifts mouth events; verifying the source take does not
  verify the insert.
- Why it matters: inserts are the only mouth-sung picture in v3;
  the user's verdict led with "bad lipsync timing". A wrong insert
  is worse than no insert (montage underneath is the fallback).
- Interim method: eye verification only (MV-7 precedent — all 56
  line lags re-measured by eye; mouth-openness DETECTORS are
  unreliable). Extract onset ±0.15s frames from the warped render,
  eye-read.
- Research avenues: lightweight lip-landmark tracking on warped
  renders (MediaPipe Face Mesh mouth landmarks, frame-to-frame mouth
  aspect ratio vs word onsets); audio-visual sync scorers that work
  on music-bed audio (SyncNet-class models, retrained/adapted);
  phoneme-free mouth-energy curves.

## GAP-3 — Motion audit across montage cuts is meaningless as frame-diff (OPEN, recorded 2026-11-09)

- What we need: a motion audit that treats cuts correctly — a cut
  is a 100% frame change by definition, so whole-master frame-diff
  flags every cut as "motion" and hides real freezes inside segments.
- Why it matters: "halted moments" was in the verdict. A freeze
  hiding inside a 3s montage segment between two cuts is invisible
  to a whole-master diff.
- Interim method: per-segment motion audit — split the master at
  cut points first, then require continuous frame-to-frame motion
  inside each segment (no frozen run ≥24f during words; mean diff
  floor per segment).
- Research avenues: shot-boundary detection + per-shot motion
  statistics as a single tool; optical-flow magnitude per shot;
  still-frame-run detection that respects cut boundaries.

## GAP-4 — "Vibes" match has no metric (OPEN, recorded 2026-11-09)

- What we need: any checkable proxy for whether the picture's
  energy matches the song's energy at a given moment (chant density,
  brass-stab punch, slap-bass groove, the 41s Outro build to the
  true peak) — beyond "cuts land on beats".
- Why it matters: the verdict says "you did not use the timing of
  the song properly or the song vibes". Beat-locking is necessary
  but not sufficient; v2 was beat-locked in places and still missed
  the vibes.
- Interim method: Critic loop (contact sheet → phone test → score
  1–10 → fix worst 3 → repeat to 8+) on every visual slot; parent
  ear/eye as the final judge; crescendo-map accents (63.32 hit,
  112.25/112.72 pair, 170.9–174.7 cluster, 159.435 peak) each get a
  named visual accent verified positionally on the master.
- Research avenues: audio-energy-envelope vs visual-motion-envelope
  correlation per section; onset-strength curve vs shot-change rate;
  "energy matching" metrics from MV/editing literature; learned
  audio-visual correspondence scorers.

## Closed gaps (for the record)

- (none yet — v3 gaps above are all open)
