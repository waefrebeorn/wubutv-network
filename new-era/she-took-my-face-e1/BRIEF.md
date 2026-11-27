# SHE TOOK MY FACE — E1 PRODUCTION BRIEF (coordinator)

Parent-written script: SCRIPT_E1.md in this folder (LOCKED v1). Bible:
new-era/shows/SHE_TOOK_MY_FACE.md. Approved story:
new-era/SHE_TOOK_MY_FACE_E1_PLAIN_STORY_DRAFT.md. Follow the script
exactly; production/script-level calls inside the script are yours to
execute, not to re-plot.

## The job

Produce the 6 units of E1 as shipped takes in takes/ (u1_t1.mp4 …
u6_t1.mp4, plus a refire u<N>_t2.mp4 only where the cap allows), QC
each, and write COMPLETION.json + GATE_LOG.md in this folder. The
PARENT assembles the master — do NOT assemble.

## Standing production law

- FAIL-ONCE-THEN-SHIP (TV shows): each unit gets its first take plus
  ONE refire. If the refire also fails a gate, ship the better take
  and disclose the flaw in GATE_LOG.md + COMPLETION.json. No third
  takes, no repair loops.
- CAP-EXEMPT lines (may justify the refire on their own; must land
  full): ORA's law (U1) "One smile, one face. Stamped. Sold. Legal." ·
  NINO's aside (U4) "Then watch me peel it back." · ORA's revocation
  (U6) "Two smiles. One face. My stamp is wrong."
- Dialogue total target: 16 scripted lines; count landed lines per
  take from dual-checkpoint ASR (Checkpoint A large-v3-turbo is the
  authority; B adjudicates): ~/workspace/tools/lyrics-venv/bin/python
  ~/workspace/tools/asr_dual.py <take> <out.json> — one at a time.
- Every take: 10.000s, 24fps, 240 frames, landscape 16:9 (native takes
  may arrive 1248×704 or 1280×720 — either is fine, the parent
  conforms). Native audio only; no TTS, no added music.
- Camp B default: one speaker per clip where the script allows;
  exchanges may share a clip when the script stages them together,
  but keep spoken load ≤ ~15 words per speaker per 10s.
- STRONG REFERENCE joints: condition each unit's generation on the
  previous unit's world (characters, wardrobe, light) — carry the
  look verbatim in prompt text; where the tool accepts image refs,
  use the previous unit's landed frame as world reference.
- FIRST-3 (U1): frame 1 mid-flash, the theft visible in the first
  frame (two smiles vs no mouth), first line is ORA's law.

## Cast look lines (verbatim in every vehicle that shows the character)

- NINO: an adult man with a smooth flat face and NO mouth at all —
  an unbroken surface where a mouth would be; dark hair; a wedding
  suit; a bright red scarf at his neck (the scarf is in every shot
  he is in). He speaks in a flat quiet voice; his face never moves.
  (State the no-mouth positively and plainly; do not describe a
  mouth for him anywhere.)
- VELLA: a fruit woman with glossy plum-purple skin and a small green
  leaf in her dark hair, wearing TWO wide smiles one above the other
  on her face; a saleswoman's bright dress and apron. Her spare smile
  is NINO's — same shape on her labels.
- MADAME ORA: an older woman, grey hair in a bun, glasses on a chain,
  a studio apron, carrying a heavy brass stamp.
- TOMI: a young boy, NINO's little brother, plain home clothes.
- The bottles: cream jars whose labels are printed with one wide
  smile (the same smile VELLA wears second).

## Known risk classes (log honestly; do not burn the cap fighting them)

- In-world text (the certificate's SOLD — LEGAL, the shop sign) will
  garble in generation. It is a designed object, not a gate: accept
  the best take's rendering and disclose. Never refire solely for
  text garble.
- The mouthless face and the double smile are the episode's identity
  mechanics: a take where NINO grows a mouth, or VELLA drops to one
  smile in a unit that needs two, is a real QC fail (identity break)
  — that is what the one refire is for.
- U2 is SCORE ONLY: no dialogue, no speech-like audio. If a take
  arrives with speech artifacts, cut its audio silent in the take
  file you ship and disclose (native-audio rule: speech-like artifacts
  never ship).
- U5's laugh is a sound event, not a line: it must read as the SMILE
  laughing while VELLA's own expression fights it; her clamped-hands
  beat and her line to the smile close the unit.

## Files + records

- Takes: takes/u<N>_t<1|2>.mp4 in this folder.
- QC per take: work/qc/<take>/ (ASR json, contact sheet or frame grabs).
- GATE_LOG.md: per-unit verdicts, ASR line counts, joint notes, flaws.
- COMPLETION.json BEFORE your final report: shipped take per unit
  (path + md5), lines landed per unit, cap-exempt line status, the
  full disclosed-flaw list, and the assembly recipe note "parent
  assembles: conform 1280×720/24fps, concat U1..U6, bug + CRF-18
  master, CRF-23 control".
- Budget discipline: the generation tool's own 429/budget signal is a
  hard stop — checkpoint and report BLOCKED, never retry around it.
  502/503/500-upstream is an outage, not a take failure: wait ~5 min,
  retry the same fire, ≤3, then checkpoint BLOCKED.
