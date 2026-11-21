# PILOT-1 THE MACHINE — PROGRESS

- 2026-11-15 ~08:25 EST — Build started. All five source docs read (SHOW-1
  treatment, FIRST_SECOND_DOCTRINE, POPPING_VISUALS_TV_PLAYBOOK, panel spec
  report, lore bible). Frame count locked: 1440f (6 units × 240f).
- Script written (SCRIPT.md): Chain M1-1 spine extended to 6 units, doctrine
  frame 0 adopted verbatim, mouth handoff at every joint, all lines ≤9 words.
- NEXT: panel kit (WORLD → CHAR UNC/LAURA → PROP → PEAKs), lock, then fire.
- Panel kit LOCKED: 12/12 panels (WORLD, CHAR UNC hero+face, CHAR LAURA
  hero+face, PROP headphones, PEAK U1–U6) — all read back, md5-logged in
  REFERENCE_STACK.md. UNC wordmark exact on first generation.
- NEXT: fire volley 1 (U1, U2, U3), QC, volley 2 (U4, U5, U6), assembly.
- Volleys complete: 6/6 takes landed, zero 429s, zero refusals. All takes
  exactly 10.000s / 24fps / 1248×704 (scaled to 1280×720 in segments).
- Frame QC done on all six (0.5/5.0/9.5 + joint frames): anchors held;
  mouth handoff present at every joint; motion-at-start MAE 13.4–20.2 on all
  units (no halted starts). Two assembly fixes: U5 black tail from ≈9.13s
  (trim to 219f + stretch), U6 cliff beat plays at ≈8.5s (trim to 210f +
  stretch) — see CUTLIST.md.
- Dialogue transcription running (faster-whisper large-v3-turbo, no VAD).
- NEXT: segment build → joined probe (1440f) → master encode → chat copy.
- [2026-11-15 finisher] Dialogue gate run on the SHIPPED segment audio
  (large-v3-turbo, no VAD): U1–U5 exact-word PASS; U6 initially FAILED —
  the CUTLIST 210f window amputated the final word "anyway" (take speaks
  it fully at 8.60–8.90s). Fixed in assembly: U6 window widened to 216f,
  re-transcribed PASS (full line, "anyway" 9.56–9.80s p=0.957).
- [2026-11-15 finisher] Second assembly fix: full-decode scan found a
  black tail on U2 (take frames 235–239) that spot probes missed; U2
  rebuilt from frames 0–234 stretched to 240f, line re-verified exact.
- [2026-11-15 finisher] joined.mp4 rebuilt via concat FILTER (stream
  copy skewed timestamps; demuxer join duplicated frame 0). Full-decode
  verified: exactly 1440 frames, zero black, zero exact duplicates.
- [2026-11-15 finisher] MASTER ENCODED: masters/pilot1_the-machine_16x9.mp4
  md5 847091dfde8da850229e747038c5bf50, 19,825,048 B, 1440f/60.010s,
  CRF 18 (SEI crf=18.0), AAC 48k stereo, faststart, ~ WuBu ~ bug.
  Chat copy: masters/pilot1_the-machine_chat.mp4 md5
  b638badd0389cb3241da33bbd78a249c, 19,877,856 B.
- [2026-11-15 finisher] Master eye pass PASS: doctrine frame 0, mouth
  handoff at every joint, wordmark exact (f1300 full-res), final frame
  holds the bridge cliff, no captions, no black frames.
  PILOT_DELIVERED.flag written. Disclosed flaws in GATE_LOG (U3 eye
  colour nit; dialogue onsets ≈5–6.4s vs scripted 7–9s slot; U6 final
  frame UNC mouth only slightly parted; three units time-stretched).
