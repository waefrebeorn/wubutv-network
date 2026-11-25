# BRIEF — HOLD ON E3 · PART 3: "Write His Name" (PRODUCTION)

Parent-written production brief, 2026-11-24. Source of truth:
SCRIPT_PART3.md (LOCKED v1, same dir — read it in full before
any work; its production notes are part of this brief). Cold
read: work/COLD_READ_PART3.md (PASS). Continuity:
RUNNING_BRIEF.md (updated at this lock: H-4 PAID inside this
episode; Laura's true lines 2 → 3).

## The episode in one breath

Last night the street voted YES on writing the Watcher's name.
Before dawn he scraped the tallies off the wall with his coat
sleeve and chalked THE STREET SAID NO. The Courier saw it. The
scraped vote is still on the Watcher's sleeve as chalk dust.
Laura names it; the Courier's unsigned box forces the sleeve
into the light; Laura chalks WATCHER — OWES THE STREET A TRUE
WALL and offers him the chalk. This time he takes it. End on
his face. NO freeze question.

## Format (hard spec)

- 6 units × 10s = exactly 1440 frames / 60.000s, 1280×720,
  24fps, h264 CRF 18 (proof = size differential vs a CRF-23
  encode of the same joined file — this VM's ffmpeg stamps
  crf=23.0 in the SEI regardless; never cite the SEI string),
  AAC 48kHz, faststart, ~ WuBu ~ corner bug head + tail.
- Speakers: LAURA (U2/U4/U6), THE COURIER (U1/U3/U5). The
  Watcher NEVER speaks. Camp B: one speaker per unit.
- 13 lines / 70 words total (U1 6, U2 17, U3 14, U4 18,
  U5 11, U6 4). FULL-TALK U2 + U4 (never adjacent in load —
  U3 QUIET sits between them). U6 = SILENCE-BEAT.
- LOAD-BEARING LINES (exempt from the fail-once cap — refire
  past the cap until the line lands verbatim):
  - U4 L1: "Your sleeve's been holding chalk all morning."
  - U6 L1: "Your name's up, Watcher."
- FAIL-ONCE-THEN-SHIP for every other line/unit: first take +
  ONE refire; a second failure ships the best take with the
  flaw disclosed in GATE_LOG_PART3.md. Structural fixes only
  past the cap (wrong duration/frames, missing/corrupt audio,
  unwatchable file).
- 502/503 = upstream outage, NOT a take failure — consumes no
  refire; wait ~10 min and retry the same fire in-run.
  429 = HARD STOP: end the run, write COMPLETION_PART3.json
  with the state reached, report. Never invent a daily cap.

## Staging law (from the locked script)

- The wall is generated BLANK in every unit. ALL chalk is a
  POST layer composited at assembly: Part 2's freeze question
  + YES tallies (U1, pre-scrape state), THE STREET SAID NO
  (U2 onward), MARTA PAID continuity (U2 background), the
  morning names, WATCHER — OWES THE STREET A TRUE WALL (U6).
  Any readable generated lettering in a take = flag it in the
  gate log (Part 2's U6_t3 was rejected for exactly this).
- U1's scrape is performed on a blank-wall take; the tallies'
  disappearance is a post-layer state change matched to the
  sleeve's passes (two wall states: pre- and post-scrape).
- The sleeve is a wardrobe constant: the Watcher's LEFT coat
  sleeve carries white chalk dust from U1's scrape onward —
  state it as a positive staging fact in every vehicle; the
  dusty arm is kept behind his back U2–U4, forced up into
  the light at U5, heaviest dust at U5.
- STRONG REFERENCE chaining: each unit's first frame is
  conditioned on the previous unit's last frame (world,
  wardrobe, positions, light); per-joint eye-verified
  cohesion recorded in the gate log.
- Dawn → sunrise grade shift at the U1→U2 joint ONLY.
- BLAM: U1 frame 0 is mid-scrape (motion + dust at frame 0).
- No world-swaps. One street, one wall, one morning. CARRY
  matches at every joint.
- Cast look: continue Part 2's accepted cast (Laura, the
  Watcher, the Courier, Marta in the queue) — use Part 2's
  accepted takes/panels in this dir as identity references.
- Vehicles: "at <place>" opens each; aspect stated in words
  "1280×720 landscape 16:9"; compact recipe (approved
  reference frame + short description paragraph); dialogue
  in the vehicle exactly as scripted (colon form in the
  script; the spoken lines verbatim in the prompt).

## Assembly + gates (all recorded in GATE_LOG_PART3.md)

- ONE assembly pass owns work/assembly_part3/joined_part3.mp4;
  ffprobe the joined file (1440f + 60.000000s audio, zero
  start offsets) BEFORE the master encode; re-probe the
  finished master end to end.
- F-9 on the MASTER's own audio: dual ASR
  (~/workspace/tools/lyrics-venv/bin/python
  ~/workspace/tools/asr_dual.py) — all 13 lines verbatim, in
  order, zero extra/missing; load-bearing lines checked
  separately and named.
- Ear-test (ASR-mediated cold read of the master), master
  Stranger Test (floor), Gate (f) cold run.
- Sleeve law check: dusty sleeve present U1–U6, behind his
  back U2–U4, up in the light at U5 — eye-verified per unit.
- Subtitles: mov_text (13 cues) + burned-in ASS at measured
  Checkpoint-A timings (house style: bottom-center bold
  white on semi-transparent black bar, current word yellow;
  the ASS [Events] Format header MUST include "Layer").
- Loudnorm two-pass to ≈ −18.6 LUFS / TP ≈ −2.3 (Part 2
  values). Poster frame from the master.
- Chat copy: if the master exceeds 50 MB, a bitrate-capped
  chat encode (audio copied); otherwise the master itself
  serves (Part 2 precedent: 21.9 MB, byte-identical).

## Deliverables (this dir)

- masters/E3_hold-on_part3_16x9.mp4 (+ chat copy if needed)
- masters/E3_hold-on_part3_poster.png
- GATE_LOG_PART3.md (every gate, every disclosed flaw)
- work/PROGRESS_PART3.md (running log), work/vehicles_part3/,
  takes_part3/, work/qc_part3/, work/assembly_part3/
- COMPLETION_PART3.json BEFORE your final report.

## NOT yours

- NO delivered flag, NO delivery to the user, NO commit —
  the parent verifies from disk, flags, commits, delivers.
- NO script changes. If a line cannot land as written after
  the cap (and is not load-bearing), ship the best take and
  disclose; never rewrite dialogue.
