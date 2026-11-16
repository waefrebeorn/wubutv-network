# PILOT-3 THE ROSTER — progress

- 2026-11-15 ~08:27 EST — build opened. All governing docs read (show
  treatment, first-second doctrine, TV playbook, panel spec, lore
  bible ARC-2, video-api-mastery).
- Script written: SCRIPT.md — 6 units × 10s, 1440f locked, one name
  (the Keeper's) across the episode, name-handoff at every joint.
- Panel kit COMPLETE: 6 panels generated, 6 LOCKED, 0 rejects
  (WORLD room, CHAR KEEPER/UNC/LAURA, PROP roster page, PEAK U1).
  UNC wordmark read-back exact "~ WuBu ~" on first generation.
  Two panels (PROP, LAURA) centre-cropped 3:2 → 16:9 and re-read.
  Full inventory: REFERENCE_STACK.md.
- Stage: VOLLEY — firing U1 + U2 first as pilot pair, then U3–U6.
- Volley 1 complete (6 takes). QC: U4_t1 KEEP; U1/U2 REJECT
  (wordmark), U3 REJECT (line doubled), U5 REJECT (page layout +
  event), U6 REJECT (cliff image + palette). Full verdicts:
  GATE_LOG.md. ASR via house G7 config on every take.
- Refire volley complete: U2_t2, U3_t2, U5_t2, U6_t2 all KEEP
  (visual gates verified frame-by-frame; refire ASR confirming).
  Wordmark law measured: glyph-spelled prompt + UNC at a shadowed
  edge/background renders "~ WuBu ~" exactly; large/lit/central
  UNC garbles it.
- **U1_t2 BLOCKED**: the prescribed wordmark refire was fired once;
  the media tool failed internally, produced NO file, and its
  recovery instruction barred repeating the request in this run.
  U1_t1 stands rejected. The exact refire vehicle is preserved in
  VEHICLES.md; assembly is fully specified in CUTLIST.md.
- Stage: PARKED at 5/6 units gate-passed. Remaining work for the
  finisher: (1) fire U1 refire verbatim, QC, save takes/U1_t2.mp4;
  (2) run the CUTLIST assembly recipe (~10 min); (3) flag + deliver.
  PILOT_DELIVERED.flag is NOT set — no master exists yet.
- 2026-11-15 (finisher run) — U1 REFIRE FIRED + KEEP: the preserved
  VEHICLES.md vehicle produced takes/U1_t2.mp4 on the first fire
  (snapshot 65933a1c-…:s6i3cf). All gates PASS — wordmark exactly
  "~ WuBu ~" in every readable frame, dialogue ASR verbatim +
  "Vásquez." cliff, frame-0 = PEAK, motion, no captions. Full
  verdicts: GATE_LOG.md.
- ASSEMBLED + MASTER VERIFIED: CUTLIST recipe run; joined probed
  at 1440f before the encode; master
  masters/pilot3_the-roster_16x9.mp4 — 1280×720, 24fps, 1440f,
  video exactly 60.000s, CRF 18 (SEI crf=18.0), AAC 48k,
  faststart, ~ WuBu ~ bug; md5 67c7fa105e13c3443b3f03c7892155a7,
  18,561,759 B. Chat copy = straight copy (≤50 MB), same md5.
  Full-master eye pass done (NAME visible at every joint; final
  frame held on WREN). Disclosed in GATE_LOG: audio container
  duration reads 60.110s (AAC tail padding; picture exact); a
  first `-t 60` encode clipped 4 frames and was discarded.
- Stage: DELIVERED TO DISK. PILOT_DELIVERED.flag set. Parent
  delivers to chat. Episode-level disclosures for delivery are
  in GATE_LOG (cast identity drift is the headline).
