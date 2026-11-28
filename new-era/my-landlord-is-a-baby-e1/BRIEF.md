# MY LANDLORD IS A BABY — E1 PRODUCTION BRIEF (parent → coordinator)

Script: SCRIPT_E1.md in this folder (LOCKED v1, parent-written).
Read it in full before firing anything. Bible:
new-era/shows/MY_LANDLORD_IS_A_BABY.md.

## Job
Produce the six units as takes in `takes/u<N>_t<1|2>.mp4` under
fail-once-then-ship (TV shows): each unit gets its first take plus
ONE refire; if the refire also fails, ship the better take with
flaws disclosed. Do NOT assemble a master — the parent assembles.
Write GATE_LOG.md (§1 cast/look gate, §2 per-unit fire log, §3 QC,
§4 disclosed flaws) and COMPLETION.json (shipped takes + md5s +
per-unit line/act verification + non-shipped takes with reasons +
full disclosed-flaw list) in this folder before reporting done.

## Standing production rules (all shows)
- Every vehicle: aspect stated in words "1280x720 landscape 16:9",
  duration exactly 10 seconds, one continuous shot unless the
  script says otherwise, native audio only, no subtitles/captions,
  no on-screen text or logos beyond the script's designed objects
  (the rent book's "ONE MONTH EARLIER" page, the calendar page,
  the black slip are designed objects; the ~ WuBu ~ bug is added
  at assembly, never in a vehicle).
- Cine fold: open each vehicle with the locked GRADE BLOCK (warm
  lamplight, honey/cream, deep teal shadows, black point in the
  baby's corner, 35mm film, fine grain — verbatim from the
  script's GLOBAL LOOK), one lighting sentence (source +
  direction + quality + colour), lens as number + visible
  consequence, one camera move per unit, physics phases
  (anticipation → action → recovery) on the unit's big act (the
  growth U2, the shrink + pillow drag U3, the bed drag U5).
- Reference discipline: build cast anchor stills first (ELIAS,
  BABY BOSS at his three sizes, THE COLLECTOR — sheets graded at
  the still stage; BABY BOSS's hat + teething-ring crown must be
  identical at every size — the size changes, the tokens don't),
  grade them in GATE_LOG §1, and condition every unit on its
  anchors + the previous unit's end frame where the script names
  a joint (U6 re-shoots U1's exact composition — condition U6 on
  U1's shipped take frames, not on a fresh still).
- State-in-prompt-text: every vehicle carries the size/glass/
  room state for its unit verbatim (see the script's GLOBAL
  LOOK states + each unit's STATE IN / END STATE).
- Per-take QC: ffprobe (1280×720 / 24fps / 240f / 10.000s — the
  model's native 1248×704 raster is acceptable and conformed at
  assembly; any other aspect is a format defect to weigh at
  ship), frame strips + crops under `work/qc/<take>/`, dual ASR
  (`~/workspace/tools/lyrics-venv/bin/python
  ~/workspace/tools/asr_dual.py <take> <out.json>`), size/glass
  eye check, identity eye check (ELIAS's cardigan; the baby's
  hat + crown at every size; the COLLECTOR's grey hat).

## This episode's special gates
- NARRATION IS THE ONLY SPEECH: dual ASR on every take must
  find ELIAS's scripted narration lines, in order, in ELIAS's
  voice. BABY BOSS and THE COLLECTOR NEVER SPEAK — any baby
  speech or babble-with-words in a take = refire reason (a
  baby's wordless cry in U5 is an act, not speech: it must be
  SILENT crying as scripted — shoulders shaking, no sound; an
  audible wail is a flaw to disclose, and in U5 it also breaks
  the beat, so weigh it as a refire reason). Whisper stock
  hallucinations over quiet passages are non-speech — document
  any instance.
- CAP-EXEMPT LINES (missing one spends the unit's refire):
  U1 "My landlord took everything. It started with one coin."
  · U6 "One coin left. Tomorrow he comes for the bath."
  BIBLE-PROTECTED LINE (same footing): U4 THE ASIDE — "I keep
  one coin under the bath. He does not know." — delivered
  QUIETLY, to camera only.
- THE EXCHANGE RULE IS THE QC: every narration sentence must
  be ANSWERED BY AN ACT in the same shot (growth, shrink,
  point, taking, the book opened, the sleeping hand). A take
  where a sentence lands and the baby does nothing = refire
  reason. Verify per sentence in GATE_LOG §3.
- THE SIZE LEDGER (eye-verified per take; contradiction =
  refire reason): U1 HUGE · U2 DOLL-SMALL → KNEE-HIGH (growth
  ON CAMERA, mid-take, after the coin changes hands) · U3
  KNEE-HIGH → DOLL-SMALL (shrink ON CAMERA after the refusal)
  · U4 COLLECTOR doll-small only · U5 DOLL-SMALL → KNEE-HIGH
  (growth while dragging the bed) · U6 HUGE. A take where the
  size is merely different between frames with no visible
  grow/shrink moment for U2/U3/U5 = refire reason.
- THE GLASS LEDGER (eye-verified per take): U1 EMPTY · U2
  six coins → five · U3 five · U4 five · U5 five · U6 ONE.
  Coin counts that read approximately at shelf distance =
  disclose; a glass that reads FULL in U1 or EMPTY in U2's
  opening = refire reason.
- U2's PICTURED WISH: the dream insert must hold the SAME
  composition as the unit's waking wide — grab both frames
  into work/qc/u2_t<N>/ and note the match in GATE_LOG; this
  composition is the season finale's target frame.
- U4's TELL: the wrong detail is IN THE BOOK'S DRAWING (the
  little hat on the wrong side) and the camera must push in
  until it reads. A take where the book never opens or the
  drawing doesn't read = refire reason. The COLLECTOR's own
  grey hat is a casting tell for the audience, not the
  in-story proof — both must be present.
- THE BABY IS A BABY: checked sleep suit, hat, crown — plain
  storybook staging only, nothing else. No exceptions, no
  innuendo in any vehicle, ever.
- THE TAKEN-THINGS PILE (study transplant, boss_bee_ lilypad
  2026-11-27, SOURCES #147 — staging only, changes no line):
  in U1 and U6 the HUGE baby sleeps in his corner ON/AMONG the
  taken things — the pillow under his head, the bed's blanket
  over him — so the destination frame carries BOTH ledgers:
  Elias's side of the room empty, the baby's corner visibly
  full of what the rent took. In U5's doorway beat, the baby
  drags the bed out with its blanket trailing. Keep the pile
  readable in the U1/U6 wide frames and note it in GATE_LOG.

## Budget/outage rules
- A 429 / budget-exhausted signal is a HARD STOP: write
  COMPLETION.json with what exists, report BLOCKED, do not retry.
- A 502/503/500-upstream error is an outage, not a take failure:
  wait ~5 min, retry the same fire, ≤3 tries, and it consumes no
  refire.
- Fire order: U1 first (cast/look gate — it also banks the
  composition U6 must re-shoot), then in order.
