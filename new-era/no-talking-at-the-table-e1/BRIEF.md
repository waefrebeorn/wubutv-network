# NO TALKING AT THE TABLE — E1 PRODUCTION BRIEF (parent → coordinator)

Script: SCRIPT_E1.md in this folder (LOCKED v1, parent-written).
Read it in full before firing anything. Bible:
new-era/shows/NO_TALKING_AT_THE_TABLE.md.

## Job
Produce the six units as takes in `takes/u<N>_t<1|2>.mp4` under
fail-once-then-ship (TV shows): each unit gets its first take plus
ONE refire; if the refire also fails, ship the better take with
flaws disclosed. Do NOT assemble a master — the parent assembles.
Write GATE_LOG.md (§1 cast/look gate, §2 per-unit fire log, §3 QC,
§4 disclosed flaws) and COMPLETION.json (shipped takes + md5s +
per-unit sound-event status + non-shipped takes with reasons +
full disclosed-flaw list) in this folder before reporting done.

## Standing production rules (all shows)
- Every vehicle: aspect stated in words "1280x720 landscape 16:9",
  duration exactly 10 seconds, one continuous shot unless the
  script says otherwise, native audio only, no subtitles/captions,
  no on-screen text or logos (the ~ WuBu ~ bug is added at assembly,
  never in a vehicle).
- Cine fold: open each vehicle with the locked GRADE BLOCK (warm
  tungsten, mahogany/cream/deep-green, 35mm film, fine grain,
  halation on candle flames — verbatim from the script's GLOBAL
  LOOK), one lighting sentence (source + direction + quality +
  colour), lens as number + visible consequence, one camera move
  per unit, physics phases (anticipation → action → recovery) on
  the unit's big action.
- Reference discipline: build cast anchor stills first (BRUNO, KIP,
  MANGO — one sheet each, face graded at the still stage), grade
  them in GATE_LOG §1, and condition every unit on its anchors +
  the previous unit's end frame where the script names a joint
  (U5→U6 must hold the empty place; other joints may be
  conditioned resets).
- State-in-prompt-text: every vehicle carries the chair ledger
  state for its unit verbatim (see the script's GLOBAL LOOK chair
  states + each unit's FRAME/END STATE) and the roll-pile counts.
- Per-take QC: ffprobe (1280×720 / 24fps / 240f / 10.000s), frame
  strips + crops under `work/qc/<take>/`, dual ASR
  (`~/workspace/tools/lyrics-venv/bin/python
  ~/workspace/tools/asr_dual.py <take> <out.json>`), chair-ledger
  eye check, identity eye check (chef hat / bow tie / mango leaf
  + grin; MANGO's grin never leaves; PEPPER only in U6).

## This episode's special gates
- AUDIO IS INVERTED: there is NO dialogue. Both ASR checkpoints
  must return no character speech in every shipped take. The only
  permitted word-shaped audio is the phone's "HELLO!" in U4 (a
  device voice). Character speech in a take = identity-class
  break → refire; speech in both takes of a unit → ship the
  better picture with its audio SILENT (strip the audio track on
  a copy in takes/, note it in COMPLETION.json) and disclose.
- CAP-EXEMPT SOUND EVENTS (missing one spends the unit's refire,
  exactly like a missing cap-exempt line): U2 KIP's tiny squeak ·
  U4 the phone's "HELLO!" · U5 KIP's one huge "HA!". Verify each
  on the take's own ASR/audio (a squeak or HA may not transcribe
  as words — judge by ASR markers plus an RMS listen-check on the
  segment; record how you verified it in GATE_LOG).
- U3's scream must be SILENT: a take where Bruno audibly screams
  fails the gag — refire reason.
- CHAIR LEDGER (eye-verified per take; contradiction = refire
  reason): U1 all whole · U2 end KIP −1 inch · U3 KIP still −1 ·
  U4 end MANGO −1 too · U5 end KIP's chair carried OUT · U6 the
  empty place, KIP standing.
- The wall sign is a PICTURE (mouth + red circle + slash), no
  letters. Incidental garbled text elsewhere = designed-object
  class, disclose only.

## Budget/outage rules
- A 429 / budget-exhausted signal is a HARD STOP: write
  COMPLETION.json with what exists, report BLOCKED, do not retry.
- A 502/503/500-upstream error is an outage, not a take failure:
  wait ~5 min, retry the same fire, ≤3 tries, and it consumes no
  refire.
- Fire order: U1 first (cast/look gate), then in order; U5 and U6
  are a conditioned pair — U6's vehicle conditions on the shipped
  U5 take's end frame.
