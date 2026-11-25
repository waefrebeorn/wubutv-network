# PILOT-5 THE LAST SEAT — gate log

Gates per unit: frame-0 test · dialogue (transcript == written line) ·
wordmark (n/a on takes — UNC absent; bug verified on master) · no
generated text · MOTION LAW (cut lands on a moving frame) · adults
only · zero reuse · event-read + motif.

## U01 — THE LEAP (takes/U01.mp4, 240f, 10.000s, 1248×704 native)
- Frame-0: PASS. Frame 0 = dancer mid-leap over the stage toward the
  seat, white-gloved hands + two tickets in the foreground corners.
  Frame sentence reads sound-off: "the stage from the seat's view, and
  the dancer already mid-leap toward the one viewer." Already moving
  at the cut — motion law satisfied at the episode's first frame.
- Identity: PASS. Same woman as PNL-CHAR-DANCER (bun, face, vermilion
  dress) at 0s / 3s / 5s / 8.5s / 9.6s. Stage light runs redder than
  the PEAK panel — measured hue-drift class, not an identity fail.
- Gaze joint: PASS. She dances down the aisle to the seat, stops at
  ~8s, and the final frames are a held down-lens gaze, face large —
  the gaze is TAKEN exactly on the cliff.
- Deviation (noted, accepted): the camera drifts/pushes in during the
  last seconds instead of staying perfectly locked; the seat's POV is
  never broken (hands/tickets persist, eyeline is down the lens), and
  the push serves the cliff. Bible line amended in practice: the seat
  may lean in; it may not leave.
- Text: PASS. No captions/titles; the foreground tickets carry only
  blurred pseudo-print, unreadable at any frame checked.
- Dialogue: PASS on words, DEVIATION on placement. Transcript (whisper
  large-v3-turbo, no VAD): [0.00–2.58] "You kept her step." /
  [4.06–5.58] "She dances it tonight." — the written line verbatim, no
  other speech, male voice off-screen as directed. But the generator
  front-loaded the line into 0–5.6s instead of the 7–9s grammar slot.
- Refire U01b (explicit "no speech for the first seven seconds"
  phrasing): REJECT — frame 0 fails outright (dancer small, back to
  camera, standing on stage; the leap and the PEAK composition gone).
  Measured lesson: this generator front-loads quoted speech and the
  first-frame lock is the scarcer asset — U01 ships, the line-timing
  deviation is disclosed, and U2–U6 prompts are designed so the line
  reads correctly wherever it lands while the visual cliff carries
  the 9–10s slot.
- VERDICT: U01 = KEEP (ships as unit 1).

## First volley U02–U06 (CHAR-hero anchored) — ALL REJECTED on frame 0
The control experiment of the build. With only a CHAR panel as the
image anchor, the generator rebuilt the panel instead of the unit:
- U02: frame 0 = the hero panel re-rendered (dancer standing still on
  a plain dark ground) — no ballroom, no chairs, halted-photo start.
- U03: world built and composition strong, but the lobby is covered in
  legible generated signage ("Platform 3", "DEPARTURES") = text-gate
  FAIL, and the text-only Dancer was re-costumed into a long-sleeved
  gown (identity drift on the unanchored character).
- U04: forest built, dress correct, but frame 0 is a static standing
  profile — halted-photo start; the turn never reads at the cut.
- U05: same collapse as U02 — plain ground, standing still, no tower.
- U06: frame 0 = empty red stage, dancer a sliver at the edge (an
  establishing shot — banned shape #1); final gaze goes off-lens.
Transcripts of the rejected takes (run for the record): every line
was spoken verbatim in all five — the dialogue recipe was never the
problem; the first frame was. (U04's line even spread 0–9.6s.)
FIX APPLIED: PEAK panel per unit (PNL-PEAK-U02..U06, gated stills —
see REFERENCE_STACK.md), refire on the PEAK anchor, the U1 recipe.

## Refire volley (PEAK-anchored) — visual verdicts
- U02b: frame 0 = PEAK composition held (ballroom of chairs, mid-
  falter, seat backs in foreground); ends on her face close, gaze
  straight down the lens, waiting. PASS.
- U03b: frame 0 = PEAK held (blank lobby, zero text, Usher mid-stride
  large, Dancer small in the light square, correct dress); ends on
  the Usher's face huge, gaze down the lens. PASS.
- U04b: frame 0 = mid-turn in the clearing, skirt flaring, leaves in
  the air; ends close on her face to camera, wonder played bright
  (broader than house deadpan — noted). PASS.
- U05b: frame 0 = the tower slide, exact PEAK. Widened sample settles
  the mid-unit question: the "hover" frame is a railing vault (hand
  on the rail at 5.5s), landing a lower ledge (6.5s), then a full
  leap at the lens (7.5s, motion-blurred) — the travel resolves into
  the scripted spring. PASS with staging variant disclosed.
- U06b: frame 0 = mid-descent, exact PEAK; landing reads (deep crouch,
  3.0s); the kept step reads in the body (6.0s). Deviations: the
  final gaze goes UP to the shifting spotlight instead of into the
  lens — the last joint is a refusal, not a return (disclosed); the
  dress settles longer than the locked short skirt in the back half
  of U05b/U06b (disclosed).
- Dialogue verdicts for the b-takes: PASS, all five lines verbatim
  (whisper large-v3-turbo, no VAD): U02b "Teach me the step the seat
  liked, Usher." / U03b "You didn't forget it, Dancer. The seat kept
  it." / U04b "I asked. The seat answered in steps, not words." /
  U05b "Then dance the answer, Dancer. The seat is watching." /
  U06b "Keep this one too, Seat. I'll forget it." — U06b's ASR
  spelled the homophone as "one-two"; too/two are exact homophones,
  the spoken line is the written line (G7 logged hand-check note).
  Placement: lines land early/spread rather than in the 7–9s grammar
  slot — the same measured generator behaviour as U1, disclosed once
  for the whole episode; the words are exact everywhere.

## Master verification (end to end, on the finished file)
- masters/PILOT-5_the-last-seat_house.mp4 — md5
  9bb12bc04d8c1c0ce078757e133775c6, 20,193,246 B.
- 1440 frames, 1280×720, 24fps, h264 + AAC, 60.005s container
  (video exactly 60.000s; 5ms audio tail).
- x264 SEI reads crf=18.0. Faststart: moov at byte 36, before mdat.
- Wordmark: UNC does not appear in this show; the post-production
  corner bug was read off the finished master at 0s and 35s — reads
  exactly "~ WuBu ~" in gold, bottom-right. PASS.
- Joined file probed BEFORE the master encode: 1440f exactly.
- Chat copy: house master is already ≤50 MB, so the chat file is the
  same encode (identical md5). A bitrate-capped test encode came out
  larger (39.5 MB) than the CRF-18 master and was discarded.
- Zero reused footage: six distinct generations; no frame, take, or
  panel output is reused across units. Adults only throughout.
