# CLAIM WINDOW — Episode 2: "The Bus Pass" — BRIEF (template v6, filled)

## §0 Episode header
SHOW: CLAIM WINDOW            EPISODE: 2 (follows the pilot, "Very Umbrella")
TITLE: "The Bus Pass"
ORDER: Telegram msg 735 (2026-11-19) — pilot praised ("so much better"),
second episode ordered, "get better and better."
REGISTER: dry municipal deadpan (counter-speak) vs fruit melodrama — same
as pilot; June's flatness cracks once, late, small (the stamp handover).
GENERATOR: media.generate_video (Muse video pipeline), image-conditioned
text-to-video, 10s units, one clip per unit; dialogue block LAST in the
prompt and isolated; character names only inside speech-block speaker
labels or as bound reference labels (B-4 name hygiene).
VOICE_ROUTE: NATIVE_TEXT_ONLY — no TTS of any kind (tiny-voca hold,
msg 730). Voices carried by VOICE_SPEC_TEXT + dual-checkpoint ASR + ear
gates; drift is a disclosed-flaw class under the fail-once cap.
BUDGETS: video ≤12 total (6 first takes + at most ONE refire per unit —
FAIL-ONCE-THEN-SHIP, msg 714/716); images ≤3 (hero panels are REUSED from
the pilot, copied into panels/ with md5s matching the pilot's canonical
refs — they cost 0; the ≤3 covers an optional peak panel). A 429 /
video_daily_budget_exhausted is a HARD STOP — do not retry, report.
DELIVERABLES: masters/CLAIM_WINDOW_E2_16x9.mp4 (house master) ·
masters/CLAIM_WINDOW_E2_chat.mp4 (chat copy, ≤50 MB) ·
masters/CLAIM_WINDOW_E2_poster.png · GATE_LOG.md + COMPLETION.json in
this directory · EP2_DELIVERED.flag written only after the master passes
the gates below.

## §1 Cast (cards carried from the pilot BRIEF, unchanged except states)
SHOW_OFF: THE PEACH.
JUNE — canonical face: panels/PNL-CHAR-JUNE-hero.png md5
3559721269a323bdd7565f9ad3a2ce26 (pilot canonical, reused).
LOOK_BLOCK_VERBATIM: "a woman in her forties with dark hair in a low
knot, wearing a plain grey station cardigan over a white shirt, sleeves
pushed to her elbows, seated behind a lost-and-found claim counter, a
rubber stamp and a stack of paper claim forms at her right hand,
umbrella shelves behind her"
VOICE_SPEC: 40s · dry, low, unhurried · never raises her voice.
RIZZ: carriers "again / the form / noted" · catchphrase "Describe it
again." · tell: stamp thunk-thunk before unbelieved answers · brag:
"Nobody's ever gotten anything out of this window they couldn't
describe."
STATE_OPEN: the morning after; she has pinned yesterday's claim form on
the wall behind her (she never keeps forms — deviation plant).
STATE_CLOSE: she has handed her stamp to a claimant and let it stamp
its own form — trust, on screen.

THE PEACH — canonical face: panels/PNL-CHAR-PEACH-hero.png md5
b0b34a709fb9601ec1f12569073e94e8 (pilot canonical, reused).
LOOK_BLOCK_VERBATIM: "a peach character with a bent-flat leaf stem,
wearing a yellow rain slicker two sizes too big, standing at a
lost-and-found claim window, hands always moving"
WARDROBE NOTE: slicker DRY today (dry morning); closed umbrella under
its arm in U1 only, never opened.
VOICE_SPEC: bright, round, theatrical · fast, pleading · drops the act
for one plain line (U4).
RIZZ: carriers "technically / okay so / mine" · catchphrase "Okay so
technically—" (lands clean in U4 — one unit earlier than the pilot) ·
tell: small squeak before each lie · brag: "I have never lost anything
I didn't find louder."
STATE_OPEN: lost the bus pass that was taped under its mother's
umbrella; performed panic. STATE_CLOSE: describes the pass perfectly,
unprompted, in June's own form of words; holds the stamp.

## §2 Room gates (parent-locked in SCRIPT_E2.md — recorded, not re-run)
PETTY_WANT: the Peach wants its mother's bus pass back before its bus.
STATUS_CHANGE: Bluffer (pilot) → Habitual bluffer who tells the truth
early and describes perfectly by U6; June: Rule-breaker (pilot) →
Trusting (hands over the stamp).
FACE_AT_RISK: the Peach's (lying now out of habit, not need) and
June's (yesterday's broken rule is becoming a reputation).
QUOTABLE: "That's not a description — that's a habit."
STANDALONE_BEAT: U3 — the coat lined with dozens of pinned bus passes.
HOOK (U1): PAIN — "It's gone! The pass is gone!" at frame 0.
FLOOR_CHECK + TASTE_TEST: PASS at script lock (SCRIPT_E2.md rulings).

## §3 Panels / sequence
Panels: the two pilot hero panels, copied (md5-verified above). Reuse
them as the identity anchors for every unit — RE-ANCHOR RULE: never
chain a drifted frame; if a take's last frame drifts (esp. June's hair
colour/parting), re-anchor the next unit to the canonical hero panel.
Optional: ONE peak panel for U1 or U3 inside the image budget.
SEQUENCE GATE: build a contact sheet (2 panels + per-unit chained
frames), eye-read before assembly; seq_story_in_one_sentence must
read: "A peach that lost its bus pass bluffs, confesses, and gets it
back at the lost-and-found window."

## §4 Per-unit vehicles (build work/vehicles/U1.txt … U6.txt)
Three-loci law placement (header / cast-action / closing Final block),
verbatim LOOK blocks, speech block last and isolated, blank-surface
assertions ×3, name hygiene (action prose: "the woman" / "the peach
character").
- U1: Camp A exception (hook exchange IS the unit; 12 words, ≤6/turn) ·
  HEAD-SPEECH assertion instead of head-silence: the Peach is mid-shout
  at frame 0, mouth open, first line immediate · PROOF_OBJECT: the
  closed umbrella under its arm · BIT: none · KEEP_LIST: "Yesterday lied."
- U2: Camp B · June + REACTION (Peach scribbles) · 16 words ·
  PROOF_OBJECT: the claim form (BLANK) · BIT: THE FORM readback ·
  KEEP_LIST: the quotable, whole.
- U3: Camp A (11 words) · PROOF_OBJECT: the coat lined with coloured
  pass cards (NO letters/words on any card — shapes only) · BIT: THE
  PULL #2 · KEEP_LIST: "First honest answer today."
- U4: Camp B · Peach · 13 words · PROOF_OBJECT: the new form in June's
  hand as she stands · BIT: catchphrase earned early · KEEP_LIST: whole
  line.
- U5: Camp B · June · 13 words · PROOF_OBJECT: the yellow bus pass
  (photo = simple peach shape, NO text, NO face detail; torn corner) ·
  BIT: June describes · KEEP_LIST: "Driver handed this in at seven."
- U6: Camp A (12 words) · PROOF_OBJECTS: the yellow pass + the stamp in
  the Peach's hand · BIT: THE STAMP handed over · KEEP_LIST: "Now it's
  a description."

## §5 Gates (all recorded in GATE_LOG.md)
Per-take QC (identity / wardrobe / prop-continuity incl. BELL CHECK /
motion-at-cut-in / text check — any legible generated word is a take
flaw, disclosed per the cap) · dual-checkpoint ASR vs script (Whisper
large-v3-turbo + Rumble-2-Flash adjudication; ~/workspace/tools pattern
from the pilot's work/qc/rumble_check.py — copy it in) · head check on
U1 (first-word time measured and reported; target ≤0.5s) · per-joint
cohesion log (world, wardrobe, positions, light, bell/stamp/form-stack
presence, June hair check) · master gates: F-9 on the MASTER's audio,
ear-test (cold listen), Gate (f) cold run, Quote-Back on the master,
BLAM measured on the master (A1 first-word time is a headline number
this episode) · structural: exactly 1440 frames / 60.000s, 1280×720,
24fps, AAC 48kHz, faststart, corner bug head+tail · CRF 18 proven by
size differential vs a CRF-23 encode of the same joined.mp4 (never the
SEI string) · ONE assembly pass owns joined.mp4; probe joined =
segment sum BEFORE the master encode; re-probe the master end to end.
Takes generate at 1248×704 — conform scale+pad to 1280×720 in assembly
(pilot method).
FAIL-ONCE CAP: at the cap, gates DISCLOSE rather than block; only
structural failures (wrong duration/frames, missing/corrupt audio,
unwatchable file) may stop a ship.
CAPTION: from the QUOTABLE or EMPTY — "That's not a description —
that's a habit."

## §6 Improvements over the pilot (BINDING — the user ordered "better
and better"; each maps to a disclosed pilot flaw)
I-1 BLAM: U1 speech from frame 0; report the master's first-word time.
I-2 PROP CONTINUITY: brass bell, stamp, form stack named in every
vehicle's prop list and checked at every joint.
I-3 FRAMING: one locked medium two-shot for U1–U4 and U6 (counter
frame-bottom, June frame-left seated, Peach frame-right); U5 at the
shelves uses the pilot's U5 geography. No recompose at joints.
I-4 IDENTITY: re-anchor every unit to the canonical hero panels;
June's hair (dark, low knot, centre colour) checked per joint.
I-5 NO weather effects indoors; Ep2 is a dry morning — windows dry.
I-6 TEXT: no legible words anywhere; the words "Lost Property" are
banned by name in vehicles; passes/forms/signage = coloured shapes.
I-7 Umbrella closed and upright/under-arm only; never opened indoors
or over the counter in this episode.

## §7 Completion record
Write COMPLETION.json in this directory BEFORE your final report
(paths + md5s, spend vs budgets, gate verdicts, disclosed flaws), and
GATE_LOG.md with the full per-take and per-joint record. Disk is the
truth — a lost report must not lose the episode.
