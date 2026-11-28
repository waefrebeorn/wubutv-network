# ONE MILLION PETALS — E1 PRODUCTION BRIEF (parent → coordinator)

Script: SCRIPT_E1.md in this folder (LOCKED v1, parent-written).
Read it in full before firing anything. Bible:
new-era/shows/ONE_MILLION_PETALS.md.

## Job
Produce the six units as takes in `takes/u<N>_t<1|2>.mp4` under
fail-once-then-ship (TV shows): each unit gets its first take plus
ONE refire; if the refire also fails, ship the better take with
flaws disclosed. Do NOT assemble a master — the parent assembles.
Write GATE_LOG.md (§1 cast/look gate, §2 per-unit fire log, §3 QC,
§4 disclosed flaws) and COMPLETION.json (shipped takes + md5s +
per-unit line verification + non-shipped takes with reasons +
full disclosed-flaw list) in this folder before reporting done.

## Standing production rules (all shows)
- Every vehicle: aspect stated in words "1280x720 landscape 16:9",
  duration exactly 10 seconds, one continuous shot unless the
  script says otherwise, native audio only, no subtitles/captions,
  no on-screen text or logos beyond the script's designed objects
  (the banner and the tally board are designed objects — their
  painted text is the show's ledger, not a defect; the ~ WuBu ~
  bug is added at assembly, never in a vehicle).
- Cine fold: open each vehicle with the locked GRADE BLOCK (warm
  gold daylight, petal-pink/cream, deep garden green accent, black
  point in the chain shadow, 35mm film, fine grain, halation on
  the banner letters — verbatim from the script's GLOBAL LOOK),
  one lighting sentence (source + direction + quality + colour),
  lens as number + visible consequence, one camera move per unit,
  physics phases (anticipation → action → recovery) on the unit's
  big action (the petal rain U1, the melt U2, the dip U5, the
  drop U6).
- Reference discipline: build cast anchor stills first (LILA, OLD
  PETT, MOSS, PIA, PIO, DORO — one sheet each, faces graded at
  the still stage; the twins must read as two distinct people in
  matching scarves), grade them in GATE_LOG §1, and condition
  every unit on its anchors + the previous unit's end frame where
  the script names a joint (U5's collection mirrors U2's sale
  framing; U6 conditions on U5's end state — hat back on, sack
  heavy).
- State-in-prompt-text: every vehicle carries the board/garment
  state for its unit verbatim (see the script's GLOBAL LOOK
  states + each unit's STATE IN / END STATE) and the exact board
  number for the unit.
- Per-take QC: ffprobe (1280×720 / 24fps / 240f / 10.000s — the
  model's native 1248×704 raster is acceptable and conformed at
  assembly; any other aspect, e.g. 3:2, is a format defect to
  weigh at ship), frame strips + crops under `work/qc/<take>/`,
  dual ASR (`~/workspace/tools/lyrics-venv/bin/python
  ~/workspace/tools/asr_dual.py <take> <out.json>`), board/garment
  eye check, identity eye check (red coat + hat state, PETT's
  white moustache, the twins' scarves, DORO's garland).

## This episode's special gates
- DIALOGUE IS THE GATE: dual ASR on every take must find the
  unit's scripted lines, in order, spoken by the right character.
  A missing or wrong-speaker line = refire reason. Judge by the
  take's own ASR plus the RMS/segment evidence; Whisper stock
  hallucinations over score-only passages are non-speech —
  document any instance, do not let one fail a take by itself.
- CAP-EXEMPT LINES (missing one spends the unit's refire):
  U2 LILA's bet — "Every petal in my sack is real by sunset —
  or the coat is yours. For nothing." · U5 LILA's demand —
  "Open the box, Pett." Both must land FULL and verbatim.
- THE BOARD IS THE LEDGER (eye-verified per take; a wrong or
  unreadable board number = refire reason): U1 12 · U2 end 62 ·
  U3 end 31 REAL · U4 end 31 REAL — 19 FAKE (painted by LILA) ·
  U5 end 231 · U6 end 231 + tomorrow's chalk line. Painted-number
  garble that still reads as the right number = designed-object
  class, disclose; a number that reads as a DIFFERENT number
  fails.
- THE GARMENT LEDGER (eye-verified per take; contradiction =
  refire reason): hat ON U1–U2 sale · hat in PETT's hand from
  U2 end through U4 · hat BACK on LILA from U5 collection on ·
  coat ON in every unit (the coat is only ever AT STAKE, never
  paid in E1) · sack near-empty U1, growing U2, smaller U3–U4,
  heavy U5–U6.
- THE MELT IS THE PROOF: U2's petal must visibly melt/drip in
  LILA's palm in front of the witnesses; U5's dip must melt
  PETT's crown petal ON CAMERA and the witnesses' THREE FACES
  (MOSS shock, PIA shock, PIO delight) must be readable BEFORE
  the collection beat. A take where the melt happens off-frame
  or the faces don't read = refire reason.
- U3's PICTURED WISH: the dream insert (gate open, garden
  flowered, LILA inside in coat + hat, sack full) must hold the
  SAME composition as the unit's waking wide — grab both frames
  into work/qc/u3_t<N>/ and note the match in GATE_LOG; this
  composition is the season finale's target frame.
- DORO appears U1 (inside the garden, hanging the garland),
  U3 (second garland + his taunt line), U6 (the black petal +
  his line). He never leaves the garden in E1.

## Budget/outage rules
- A 429 / budget-exhausted signal is a HARD STOP: write
  COMPLETION.json with what exists, report BLOCKED, do not retry.
- A 502/503/500-upstream error is an outage, not a take failure:
  wait ~5 min, retry the same fire, ≤3 tries, and it consumes no
  refire.
- Fire order: U1 first (cast/look gate), then in order; U5 and
  U6 are a conditioned pair — U6's vehicle conditions on the
  shipped U5 take's end frame.
