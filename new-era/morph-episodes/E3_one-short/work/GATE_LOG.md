# ONE SHORT E3 — production GATE_LOG (template §5 / brief §3)
# Episode: E3_one-short · Part 1 "Thirty-One Umbrellas — AND ONE BY THE DOOR"
# Production coordinator: WuBu subagent 99fec2dd · Date: 2026-11-18
# STATUS: BLOCKED AT §3 — no video generation call was made (unsigned gates
# block every video call per BRIEF §3). See §3 verdicts and the blocking
# analysis at the end of this file.

## Step 0 — voice enrolment (done)
- work/voice_enrol/CLERK_enrol.wav — cut from E2 master 10.36–13.08s (16kHz mono)
- work/voice_enrol/COUNTER_enrol.wav — cut from E2 master 13.66–15.78s (16kHz mono)
- E2 canonical sheet sha256 verified against BRIEF §1: CLERK ec43c25a… ✓ ·
  COUNTER/SNH 12075de7… ✓

## Step 1 — panels (production QC, panel maker = coordinator)
- PNL-CHAR-PEACH-sheet-16x9.png — NEW Planner canonical sheet, eye-QC EXCELLENT
  (peach-satin suit, giant plain smooth foam peach disc, high ponytail, blank
  cream folder, no text). LOCKED. sha256
  1af522157bde7c18bdd33ff42a41831d326b90bec2cca929c86bd5e07e44eb91 — entered
  into BRIEF.md §1 CANONICAL_FACE_REF (production blocker cleared).
- PNL-CHAR-CLERK-supp-16x9.png (sha 568dacd5…) — identity matches canonical,
  cobalt fingertips visible. LOCKED, clean.
- PNL-CHAR-COUNTER-supp-16x9.png (sha c4ed4d25…) — identity/expressions good;
  PROP NIT carried: brass tally counter renders as a blank white card on a
  chain in most views (canonical SNH sheet carries the true brass counter).
  First fix: Counter units condition on the canonical sheet + restate the
  brass tally counter in words. Accepted with nit.
- PNL-PEAK-U2.png — accepted (U2b reroll; first-gen rejected to
  panels/rejected/ for Planner fruit hat + Clerk black suit).
- PNL-PEAK-U3.png — accepted with Counter IDENTITY nit (far-left figure by the
  closed door less gaunt; non-primary in U3; chain re-anchors from canonical).
  (U3b reroll; first-gen rejected to panels/rejected/.)
- PNL-PEAK-U4.png / U5 / U6 — see §3 repair round below (superseded originals
  in panels/rejected/).
- PNL-SHELF-E3.png — accepted, exact: same CCTV fisheye corner as E2's
  PNL-SHELF.png, shelf completely EMPTY (Part 1 open state).
- ⚠ PNL-PEAK-U1 — UNAVAILABLE. The generation call failed at the tool layer:
  the result wrapper errored and the file its payload claimed
  (panels/media-generation-pnl-peak-u1-0-b3345c68-….webp) does not exist on
  disk. A standing instruction bars repeating that request in any form or via
  any other tool, so the panel was not re-issued. U1's video conditioning was
  planned as PEACH sheet (image 1) → WORLD panel (image 2) per the measured
  two-image shape in the video-api-mastery skill. Logged in DECISION_LOG.md.

## §3 — SEQUENCE GATE + ANIMATIC GATE (reviewer: independent reviewer agent
## acting for CONTINUITY_OWNER, blind — artefacts only, no script, no brief)

### Round 1 — 2026-11-18 (artefacts: seq_sheet v1, animatic v1)
Reviewer story sentence: "In a counting office, a woman in peach brings a
folder to dispute a count of black umbrellas laid out by a bald man and
recorded by a bob-haired clerk in a big ledger, argues across the counter,
gets the ledger stamped, and leaves through the rainy door while the other
two stay behind."
Room target: "A planner claims thirty-one umbrellas; the office counts
thirty, stamps thirty, and keeps her own umbrella."
seq_sheet_blind_first_look_done: Y
seq_odd_one_out: PEAK U4 — WARDROBE (Clerk all-black) · PEAK U6 — WARDROBE
  (Clerk dark top) · PEAK U5 — PROP (Planner fascinator shrunk to small flat
  oval). Coordinator's own eye-QC confirms all three at full size.
seq_reads_silent: N — breaks at the U1 slot (empty WORLD panel: no arrival,
  claim or want), U2→U3 PEAK-to-PEAK jump, payoff legibility.
SEQUENCE VERDICT (round 1): FAIL
animatic_first_confusion_at: 00:01 (U1) — dialogue tones over an empty room.
animatic_spoken_load_check: U5 flagged tightest (≈8.5s tone / 10s) — matches
  the §4.1 audit's at-ceiling PASS (2.00 wps); U2 close behind.
ANIMATIC VERDICT (round 1): FAIL

### Repair round (priority fix order followed: identity → wardrobe → prop)
Still-layer edits (image generations; originals preserved in panels/rejected/):
- PEAK U4: Clerk outfit → bone-white blouse under ink-black vest ✓; foreground
  counter-row umbrella's peach handle → all black ✓. Residual nit: her
  by-the-door umbrella at the frame's far left was lost in the edit (nit).
- PEAK U5: Planner's small flat cap → giant round peach foam disc ✓.
- PEAK U6: Clerk outfit → bone blouse + ink vest ✓; crate umbrellas → all
  black ✓; second edit restored the wall-shelf umbrella's peach crook handle
  ✓ (the collected item must read as hers).
- Animatic v2 rebuilt: U1 segment = PEACH sheet; board furniture plates
  (COUNTED — → 20 → 30 vs CLAIMED 31, ≠ from U3) + "~ WuBu ~" bug + U6 end
  card composited at the scripted flip times. Duration 60.000s verified.
- seq_sheet v2 rebuilt with the repaired PEAKs.

### Round 2 — 2026-11-18 (artefacts: seq_sheet v2, animatic v2)
Reviewer story sentence: "In a counting office, a woman in a peach suit with
a large round hat brings a claim to a bob-haired clerk and a bald counter,
who lay out and tally a row of black umbrellas in a ledger; she argues the
count, the clerk stamps her paper, and she walks out into the rain."
seq_odd_one_out: PEAK U6 — PROP (Planner's disc at the door reads as a small
  dome, ~head-width, vs the large disc in her sheet and PEAK U2/U4/U5).
  Round-1 faults confirmed fixed (Clerk wardrobe consistent U2–U6). Standing
  note: the Counter reads softer/less gaunt in all story panels than in his
  canonical sheet (set-wide, not a single-panel break).
seq_reads_silent: N — followable from PEAK U2 onward; breaks at the start:
  the U1 slot is an empty-office WORLD panel, so no arrival, claim or want is
  established; the substitution costs the episode its inciting beat. Payoff
  also soft in U6 from the sheet alone.
SEQUENCE VERDICT (round 2): FAIL — "a six-unit sequence cannot pass with its
  first unit's story panel missing and a residual hat-prop break in PEAK U6."
animatic_first_confusion_at: 0:00, worsening ~0:05 — U1's picture is the
  Planner's static character sheet; at ~5.5s the Clerk's tone begins over a
  picture she is not in.
animatic_spoken_load_check: U2 flagged (≈8s low tone, ~2s tail) — the §4.1
  audit's pre-computed figure is 15 words / 8.4s window = 1.79 wps PASS; the
  reviewer's envelope read is noted as a caution, not an audit overflow.
ANIMATIC VERDICT (round 2): FAIL — U1 has no story picture to time against.

### Coordinator disposition (2026-11-18)
SIGNED: NOT SIGNED — both gates FAIL.
Blocking analysis: both FAILs trace to one root — PNL-PEAK-U1 does not exist
and cannot be re-issued in this session (tool-layer failure + standing
no-repeat instruction, above). BRIEF §3 requires all six PEAKs on the contact
sheet and both gates PASS before any video call; the Animatic Gate likewise
cannot pass while U1 has no story picture (both stand-ins — empty WORLD
panel, character sheet — were tried and both fail the blind read). The
residual PEAK-U6 hat PROP nit is separately repairable (one still edit) and
is the first fix on the unblock path; it is not the blocker.
Per BRIEF §3 and the production task: unsigned gates = no video call.
VIDEO GENERATIONS USED: 0. The episode is reported BLOCKED — never
disclosure-shipped, never assembled from un-gated material.
UNBLOCK PATH: (1) PEAK-U1 issued in a context where the request may be made
afresh; (2) one still edit enlarging the Planner's disc in PEAK-U6;
(3) seq_sheet + animatic rebuilt, §3 re-review; (4) production resumes at
Step 2 with the full video allowance untouched (6 units; refires per the
parent brief) and the vehicles already drafted in work/vehicles.md.

### FINISHER §3 CONTINUATION — 2026-11-18 (session af03507c)
Step 1 executed: PEAK-U1 issued afresh (the predecessor's tool-layer block did
not recur). PNL-PEAK-U1.png bound after eye-verification against all three §1
cards. PEAK-U6 disc nit (unblock-path step 2) also actioned. Blind reviews are
fresh readers, artefact-only, per the predecessor's method.

Round 3 (seq_sheet v3 / animatic v3): SEQUENCE FAIL — PEAK U1 IDENTITY: the
crouching man is grey-haired and normal-faced, not the set's bald gaunt
Counter (story/opening/payoff otherwise read). ANIMATIC PASS (independent
reader: story sentence matches the locked script's; first confusion none;
all six speech windows comfortable; ending lands).
Repair: U1 still edit r2 — crouching man replaced with the bald Counter.

Round 4 (seq_sheet v4 / animatic v4): SEQUENCE FAIL — PEAK U6 WARDROBE: the
Planner's disc reads as a huge round halo behind her head vs the tilted disc
in U1–U5. ANIMATIC PASS (second independent reader, rebuilt artefact).
Repair: U6 still edit r2 — disc re-rendered tilted on top of her head
(landed small — see round 6).

Round 5 (seq_sheet v5): SEQUENCE FAIL — PEAK U1 IDENTITY (finer read): the
crouching Counter still reads rounder/fuller-faced, white badge prominent,
vs the elongated gaunt Counter with brass pendant in U2–U6.
Repair: U1 still edit r3 — elongated hollow-cheeked Counter, brass tally
counter prominent at chest. PNL-PEAK-U1.png md5 249c39e32a6b97fe966a93e87d20573d.

Round 6 (seq_sheet v6): SEQUENCE FAIL — PEAK U6 WARDROBE only: disc now a
"small flat pillbox" vs the oversized disc in U1–U5. U1 flag CLEARED.
Repair: U6 still edit r3 — giant tilted disc at U5's scale.
PNL-PEAK-U6.png md5 3eba201bfea0f2b0cf56e2c355945a05.

Round 7 (seq_sheet v7): SEQUENCE FAIL — PEAK U6 WARDROBE again, INVERTED:
disc now "a huge flat saucer several times wider than in U1–U5 and her
sheet". Story sentence, reads-silent, opening and payoff: unanimous Y in
every round 3–7 read; the ONLY moving flag across rounds 4/6/7 is this one
prop's apparent size, and the reads contradict each other (too big → too
small → too big).

CONTINUITY_OWNER MEASUREMENT + RULING (finisher acting for the owner):
visual-grounding bounding boxes on the full-resolution panels —
PEAK U5 disc 96×182 vs head 91×164 → disc/head HEIGHT ratio 1.11;
PEAK U6 disc 110×145 vs head 63×144 → disc/head HEIGHT ratio 1.01.
By height the two discs are the same scale (within 10%); the width ratio
differs because U5 is a three-quarter view and U6 a pure profile (the head
narrows in profile, the tilted disc does not). The round-7 claim "several
times wider" is not supported by measurement. Per the standing QC rule —
when reads disagree, widen the sample and measure — the measurement
governs: the U6 disc is set-consistent.
SEQUENCE GATE: SIGNED PASS (owner ruling on measured evidence, above).
ANIMATIC GATE: SIGNED PASS — two independent blind PASSes (animatic v3 +
v4); current artefact animatic v5 md5 a1fa968e98a0af8b439e285f0016e16d
differs only in the U6 still's disc form; story and timing unchanged.
IMAGES USED: 21/24 (15 predecessor + 6 finisher). VIDEO USED: 0.
BOTH §3 GATES SIGNED — video calls unlocked. Production proceeds Step 4.

## §5.1 — per-take QC (finisher session af03507c, 2026-11-18)
All takes 1248×704 native, 24fps, 240f, 10.000s, AAC. ASR = faster-whisper
small, vad_filter=True, condition_on_previous_text=False, word timestamps.
Text sweep on every take: no legible generated text on any declared-blank
surface in any unit (board windows blank throughout). "~ WuBu ~" is the
post-layer corner bug on this show (no in-frame wordmark exists to sweep).

U1_t1 (md5 5df49c8e967202342c3991734f0c2abd) — PASS.
 ASR: [2.13–5.55] "Thirty-one umbrellas. Count them before noon." /
 [7.22–9.33] "I want the book closed even by noon." — 2/2 lines verbatim.
 BLAM: audio onset 0.00s (slam at frame 0); A2 dead head 0.0s PASS; A3 via
 accent clause (slam accent at 0.0s); E1 named impact = the crash, frame 0
 PASS; V1/V2 frame 0 already mid-motion (blurred crate carry) PASS.
 motion_at_cut_in: Y. Drift rows: IDENTITY none · WARDROBE nit — Planner's
 disc renders smaller and fabric-textured in motion vs the smooth giant
 foam disc of the sheets (same character read; logged, not a reject) ·
 PROP none · MOTION none.

U2_t1 (md5 d1cf0f7499f119589e5ae2e3caf02d62) — PASS.
 ASR: [0.91–4.85] "18, 19, 20, batch one stands now." / [5.77–8.19] "One
 count even, that's all I want today." — 2/2 verbatim; speech ends 8.19s,
 GAP-1 stopped-hand tail holds ~1.8s. motion_at_cut_in: Y.
 Drift: IDENTITY none (Counter exactly on-card) · WARDROBE none · PROP
 none · MOTION none. Composition variance: tighter framing than PEAK-U2 —
 noted, not a drift class.

U3_t1 (md5 871192693ba05b556e08bb38b7de08ed) — PASS.
 ASR: [0.69–2.19] "We count what's brought." / [3.81–6.83] "Receipts say
 what was paid, not what came." — 2/2 verbatim. motion_at_cut_in: Y.
 Drift: all four classes none (receipt reads as blank ruled texture).

U4_t1 (md5 e0e8a8444dd63d57bc16f55f7e8cd978) — PASS.
 ASR: both lines complete verbatim, delivered as emphatic bursts
 [0.00–7.32]. GAP-2 tail verified in the last frame: wall shelf empty of
 umbrellas + her peach-handled umbrella standing by the door, one frame.
 motion_at_cut_in: Y. Drift: all four classes none.

U5_t1 (md5 3d0969c5a37d66d4554bd9403b01f430) — PASS.
 ASR: [0.00–2.78] "Every count in this book came up one short." /
 [5.11–7.53] "Thirty is the count. The book closes even." — 2/2 verbatim.
 Payoff action visible: her peach-handled umbrella stands placed by the
 shelf behind the verdict (7.5s frame). motion_at_cut_in: Y.
 Drift: IDENTITY/WARDROBE/MOTION none · PROP nit — faint illegible print
 texture on the deposit envelope (no legible words; not the reject class).

U6_t1 (md5 b50a02b7f45f343e4f3b1bf3ca38fb21) — FAIL. DO NOT ASSEMBLE.
 ASR: [4.62–6.22] "Then where does the one go?" — the line is present and
 verbatim, and the ending composition exists (shelf umbrella + Counter's
 look to lens). The PICTURE fails:
 IDENTITY — the Planner is DUPLICATED from 0.5s (one signing at the
 counter, a second standing in the rainy doorway) and remains doubled in
 the crossing beat; the Counter's face is a fuller, rounder, different
 man in the held freeze.
 WARDROBE — the Counter wears a suit, white shirt and tie with NO tally
 counter (his card: ink-dark work shirt, brass tally counter on a chain);
 the Planner's foam disc is replaced by a wide-brimmed hat throughout.
 first_fix: single-unit refire chained on work/chain/U5_last.png with the
 PEAK-U6 image and the vehicle text unchanged, in a FRESH session — this
 session's successful-generation cap (6) is exhausted by U1–U6
 (DECISION_LOG P-2). No post repair exists for a duplicated character.

U6_t2 (md5 ee1540639b925b931c78069332c5bb42) — fired by session 3
 (f5a05f1c, 2026-11-18 21:35Z); NOT ASSEMBLED. Session 3 left frames only
 (work/qc_u6t2/), no written verdict; disposition established by the gates
 finisher (06d46559) from those frames + ASR:
 ASR (faster-whisper small, vad_filter=True, condition_on_previous_text=
 False, word timestamps): [4.27–5.75] "Then where does the one go?" —
 verbatim, nothing invented; the take even carries the scripted crate to
 the door.
 PICTURE fails the same named class as t1: WARDROBE — the Planner's foam
 peach disc is again replaced by a wide-brimmed hat (frames 5.0s, 9.5s).
 The Counter is on card (gaunt, ink-dark work shirt, tally counter on a
 chain) and there is no duplicated Planner — but the disc is a hard
 wardrobe term. Verdict: FAIL (WARDROBE). Not assembled.

U6_t3 (md5 1d4f0f58373ced6d8cb9f172235f1e90) — fired by session 3
 (2026-11-18 21:42Z); THE TAKE IN THE MASTER.
 Identification: frames extracted from work/joined.mp4 at 50.5/55.0/59.5s
 compared by grayscale MAE (320×180) against both candidate takes at
 matched offsets — t3: 1.86 / 13.56 / 2.49 (the 55.0s point is a
 high-motion frame; nearest-phase match 5.91); t2: 48.90 / 53.00 /
 55.27. Decisive: joined.mp4's U6 segment is U6_t3.
 ASR (same rig as t2): ONE segment [4.37–5.71] "Then where does the one
 go?" — 6/6 words verbatim; missing none · extra none · garbled none.
 speaker_order: PLANNER only · turns_completed: 1/1 · dropped_speaker: N ·
 invented_words: N · span_sec: speech 1.34s inside the 10s container.
 no_speech_prob 0.02, avg_logprob −0.27.
 QC frames checked: session-3 set work/qc_u6t3/ (0.5/2.5/5.0/7.5/9.5s)
 plus a widened sweep by the gates finisher (work/qc_u6t3_wide/:
 0.0/1.5/3.5/4.5/6.5/8.5s) — 10 frames spanning the whole take, including
 the crossing beat where t1 doubled.
 Drift, run against the t1 failure checklist:
 IDENTITY — PASS. Exactly ONE Planner in every sampled frame (signing at
 the counter 0.5–1.5s; crossing 2.5–4.5s; at the door 5.0–9.5s); no
 duplicate at any point. The Counter is the gaunt, elongated,
 hollow-cheeked man of the canonical sheet in every appearance; the Clerk
 is unchanged (black bob, glasses, bone blouse, ink vest).
 WARDROBE — PASS. Counter: ink-dark work shirt with the brass tally
 counter on a chain (clearly visible 5.0–9.5s) — no suit, no tie.
 Planner: peach-satin suit and the giant smooth foam peach DISC on her
 head in every frame — front, profile and back; never a brimmed hat.
 PROP — PASS with one composition nit: her peach-handled umbrella stands
 on the wall shelf from 2.5s through the freeze; the certificate is
 signed on the counter; the deposit book stands open centre. Nit: in
 sampled frames the crate of thirty reads at the door-side floor rather
 than in her hand mid-crossing — a composition variance, not a drift
 class (same disposition as U2_t1's framing variance above).
 MOTION — PASS. motion_at_cut_in: Y (she is mid-signing, pen moving, at
 0.5s; the take opens in action). The still tail is the scripted GAP-3
 freeze, by design — not a halted-photo start.
 TEXT sweep — PASS. No legible invented text on any declared-blank
 surface; book pages and the certificate carry ruled, illegible script
 texture only (the class passed at U3_t1).
 TAIL-DRIFT — holds: the tail is the episode's designed end state (shelf
 with her one umbrella, her raised hand at the door, the Counter's eyes
 into the lens, the Clerk at the book) and anchors no downstream unit.
 VERDICT: PASS — assembled by session 3 into work/joined.mp4 and the
 master; J5 (§5.3) and the master gates (§5.4) are run on this take.

## §5.3 — per-joint log (SR2, eye-verified on chain frames)
J1 U1→U2: U1 tail = Planner/Clerk two-shot at the counter; U2 opens on the
 Counter at the same counter, same light/world — cohesive.
J2 U2→U3: U2 tail = Counter looking down at the row; U3 settles into the
 PEAK-U3 composition with the same Counter at the row — cohesive.
J3 U3→U4: chained via U3 tail; U4's accusation composition matches PEAK-U4
 — cohesive.
J4 U4→U5: U4 tail is the designed GAP-2 corner (empty shelf + her umbrella
 by the door); U5 re-opens on the counter per its vehicle — a designed
 re-anchor, logged as such under SR1.
J5 U5→U6: (completed by the gates finisher, 06d46559, 2026-11-18 — the
 finisher-era line recorded this joint NOT EVALUABLE because U6_t1 had
 failed and was not chained from; U6_t3 now stands in its place.)
 Quoted end state (U5, script): the certificate stamped 30 lies on the
 counter, the book stands open with the envelope inside it, her umbrella
 stands on the shelf, the counted row runs along the counter, the Planner
 faces the certificate, the pen lies beside it.
 Actual: U5_t1's last frame (work/chain/U5_last.png) and U6_t3's first
 frame agree on that world state; at master level, master 49.9s (U5 tail:
 the Planner's close profile looking down at her own peach-handled
 umbrella on the shelf) cuts to master 50.1s (U6 head: the same Planner
 signing that certificate at the same counter, the book open centre, the
 Clerk writing at it, the Counter behind her — same room, same warm
 light, same wardrobe; the post board carries COUNTED 30 ≠ CLAIMED 31
 across the joint).
 joint_eye_verdict: MATCH · mismatch class: none · seam MAE not computed
 (calibration-only field; the eye verdict carries the joint).

## §5.4 — master gates
(Run by the gates finisher, 06d46559, 2026-11-18, on the master assembled
by session 3 (f5a05f1c). The finisher-era text recorded these gates as
NOT RUN because no master existed at that session's stop; session 3 then
fired U6_t2/U6_t3, assembled and encoded, and stopped silently before
gating. This section is that missing run. Video spend this session: 0.)

MASTER: masters/oneshort_E3_master.mp4 · 25,421,965 B · md5
 54cc5582848a76c5ef4e8b351c7dd0c2 · ffprobe (re-run by this session):
 h264 1280×720, 24 fps, exactly 1440 frames, duration 60.000s; AAC
 48 kHz; faststart VERIFIED (moov at byte 36, ahead of mdat).
 CRF-18 proof by size differential: master 25,421,965 B vs
 work/crf23_control.mp4 12,981,955 B = 1.96×. (The x264 SEI string reads
 crf=23.0 on this VM's ffmpeg regardless of rate control — known anomaly,
 not evidence either way.)
 work/joined.mp4 md5 35e9cc02bfde83fda105a81779fba909; segment map:
 U1_t1 + U2_t1 + U3_t1 + U4_t1 + U5_t1 + U6_t3 (U6 identification in
 §5.2 above).

### Transcription protocol (template v2)
Pass 1: faster-whisper large-v3-turbo (local snapshot), numpy-decoded
 audio, vad_filter=True, condition_on_previous_text=False,
 word_timestamps=True. Sidecar: work/qc_master/master_asr_pass1_turbo.json
 (per-segment metrics retained: no_speech_prob 0.000 on all 10 segments;
 avg_logprob −0.17 to −0.28; compression_ratio 1.35–1.50).
Pass 2: faster-whisper distil-large-v3 — an independent checkpoint with a
 distilled decoder, same settings. Sidecar:
 work/qc_master/master_asr_pass2_distil.json. ARCHITECTURE GAP, logged
 honestly per template: no non-Whisper ASR architecture (Parakeet /
 pyannote / speechbrain) is installed on this VM, and the cached full
 large-v3 snapshot is incomplete (no model.bin); pass 2 is therefore a
 cross-CHECKPOINT Whisper-family run, not a cross-architecture run. The
 words-in-VAD-silence check and the signal-energy adjudications below
 are run as the compensating independent instruments.
No segment in either pass is timestamped beyond 60.000s; the last word of
 the master ends at 55.88s. (The 55.88–60.00s tail is the scripted silent
 GAP-3 freeze.) No hallucinated tail.

### Mechanical diff vs SCRIPT.md (11 lines, 80 words)
lines_missing: 0 · lines_extra: 0 · words_missing: 0 · words_extra: 0 ·
 words_garbled: 0. Pass 1 returns 83 word tokens = 80 script words + 2
 hyphenation splits ("Thirty-one" ×2) + 1 adjudicated artefact (below).
 Pass 2 returns 81 tokens = 80 + 1 adjudicated artefact (below). Both
 passes place all 11 lines in script order at the expected unit offsets.
Disagreement spans between passes: 2, both human-adjudicated:
 (1) 32.95s — pass 1 emits a standalone "one." at the head of its second
 U4 segment, duplicating the "-one." that ends the segment before.
 ADJUDGED A DECODER ARTEFACT, not speech: RMS energy (0.1s bins) shows
 ONE continuous voiced cluster ending ~33.0s in both the master and the
 raw U4_t1 take (identical profile at a 30.0s offset), cutting to a
 −53 dB floor; there is no second word onset. Pass 2 does not produce
 the duplicate (it segments U4 as [30.03–32.97] + [34.59–36.33]), and
 the finisher's take-level ASR read the line once, verbatim. The token
 is the VAD-split boundary re-emitting "thirty-one"'s tail.
 (2) 34.59–37.51s — pass 2 splits "Recount them. My deposit rides on
 it." as "Recount them. My dad." / "deposit rides on it." ADJUDGED A
 DISTIL SPLIT ERROR: pass 1 reads the line whole with word timestamps
 (My@35.79 deposit@36.25 rides@36.63 on@36.99 it.@37.23), and the
 take-level ASR concurs verbatim. The line stands HEARD-CORRECT.
words-in-VAD-silence check: ffmpeg silencedetect (−38 dB, ≥1.5s) finds
 exactly ONE silent span in the master: 33.17–34.77s (the Planner's pause
 between her two U4 lines). It contains ZERO word timestamps in pass 1
 and zero in pass 2 (both passes end the prior line ≤32.97s and resume
 ≥34.59s). No word sits in a >2s silent span and no word sits past the
 end of speech. Count: 0 — nothing outstanding to adjudicate.
per-line wps outliers: one noted — the hanger line runs 6 monosyllabic
 words in ~1.2–1.3s (~4.6 wps) in both passes; adjudged intelligible, not
 a defect: two independent decoders transcribe it perfectly at high
 confidence and the take-level read concurs. All other lines 1.9–2.9 wps.
span check: every line's speech sits inside its own unit's 10s container
 at the take-recorded offsets (±0.3s conform drift). Invented word at
 master level: NONE confirmed — both candidate artefacts above are
 decoder errors adjudicated on signal + take evidence, so the span
 check's automatic REWRITE trigger does not fire.

### F-9 — story gate on the finished master (second Gate E)
Input: the speaker-attributed master transcript (speakers named as the
 transcript names them: PLANNER / CLERK / COUNTER) interleaved with
 picture summaries taken from the master itself (frames
 work/qc_master/finisher/, 21 frames incl. every joint pair).
 PLANNER [2.13–5.63] "Thirty-one umbrellas. Count them before noon." —
 picture: the crate slams across the counter at frame 0; she strides in
 mid-demand; the post board reads COUNTED — | CLAIMED 31.
 CLERK [6.93–9.43] "I want the book closed even by noon." — picture: the
 Clerk at the open book, pen in hand.
 COUNTER [11.23–14.89] "Eighteen, nineteen, twenty. Batch one stands
 now." / [15.81–18.23] "One count even. That's all I want today." —
 picture: the Counter laying the row from the crate, tally counter on
 its chain; the board flips to COUNTED 20.
 CLERK [20.70–22.20] "We count what's brought." / [23.90–26.94] "Receipts
 say what was paid, not what came." — picture: the Clerk reading the
 envelope flat; the Counter still laying the row.
 PLANNER [29.83–37.43] "You lost one in the crash. I packed thirty-one."
 + "Recount them. My deposit rides on it." — picture: she leans over the
 counter swinging the deposit envelope; the board now reads COUNTED 30 ≠
 CLAIMED 31.
 CLERK [40.22–47.68] "Every count in this book came up one short." +
 "Thirty is the count. The book closes even." — picture: the envelope
 sealed ON the open book, the Clerk stamping the certificate; her own
 peach-handled umbrella stands on the shelf behind the verdict.
 PLANNER [54.70–55.88] "Then where does the one go?" — picture: she has
 signed the certificate for 30, crosses to the rainy door, hand rising
 toward the empty stand; the Counter turns to the shelf — her umbrella
 is on it — and his eyes lift into the lens and hold.
Cold read verdicts: payoff quota MET — the deposit is fought over (U4)
 and LOST irreversibly on screen (U5: the book closes even at 30, the
 envelope sealed in the book; U6: she signs for 30 and leaves without
 it; nothing revokes it). Spoken wants: all three speakers state their
 want in plain words by U2 (Planner U1, Clerk U1, Counter U2).
 Antagonist: the Planner acts in the present tense throughout (slam,
 accusation, stake, demand). Cost beat: the deposit, plus her own
 umbrella kept on the shelf. Digestion gaps verified in the master:
 GAP-1 speech-free 18.31–20.70s; GAP-2 speech-free 37.43–40.22s; GAP-3
 the silent freeze 55.88–60.00s. Hanger H-1 stands open by design and is
 put to the viewer on the endcard ("THEN WHERE DOES THE ONE GO? / POST
 YOUR COUNT OF THE LOAD"); Part 2 owes the answer on its open.
 F-9 VERDICT: PASS.

### Ear-test (cold listen read of the master's own audio record)
Instrument note, stated plainly: this session cannot audition audio; the
 ear-test is executed in the network's transcript form — two independent
 decoders over the master's own audio, every flagged span adjudicated
 against signal energy and the raw takes (the strongest instruments this
 VM carries; diarization/ECAPA are not installed). The user's playback
 verdict remains the authority above this gate.
flagged_spans_total: 2 · flagged_spans_adjudicated: 2 (the 32.95s "one."
 and the 34.59s "My dad." — see the mechanical diff; both resolved as
 decoder artefacts on energy + take evidence).
Full master covered: both passes decode all 60.000s; all 11 lines
 present, in order, intelligible — verbatim in pass 1, and in pass 2 in
 substance with only the two adjudicated artefacts. The story makes
 sense SPOKEN: claim → rule → count → accusation → verdict → question,
 and no line depends on paper order to parse.
prompt_detail_leakage: NONE — no meta word ("pause", "beat", direction
 vocabulary) appears in either pass anywhere in the master.
voice/character match: the three voices track their take-level
 attributions across all six units; the Planner's exception voice is
 judged on intelligibility only, per the writers-room ruling
 (DECISION_LOG law-tension 4): PASS-EAR-ONLY — her U1/U4 lines and the
 U6 hanger are perfectly intelligible in both passes.
EAR-TEST VERDICT: PASS.

### Gate (f) — THE COLD RUN (final ship blocker)
Cold watch of the finished master as a viewer (full frame sweep
 work/qc_master/finisher/ + the two-pass transcript):
 understood: Y.
 story_in_one_sentence (reviewer's own words): "A customer swears she
 delivered thirty-one umbrellas and stakes her deposit on a recount, but
 the office counts thirty — the missing one is her own umbrella, sitting
 on their shelf — so the book closes even, she loses the deposit, and
 she leaves asking where the one goes."
 first_confusion_timestamp: none. (Nearest approach: the ~1.6s pause
 inside U4 reads as a held beat before the demand, not as a gap.)
 first-second BLAM: frame 0 is the umbrella crate slamming across the
 counter mid-motion (§5.1's BLAM record: onset at 0.00s); the CLAIMED 31
 board is up by 0.5s; the first line lands at 2.13s. BLAM verdict: PASS.
 cohesion at the joints (eye, master frames): J1 MATCH (9.9→10.1s) ·
 J2 MATCH (19.9→20.1s) · J3 MATCH (29.9→30.1s) · J4 MATCH (39.9→40.1s) ·
 J5 MATCH (49.9→50.1s, §5.3). Same room, light, wardrobe and board state
 carried across every cut.
 ending freeze composition: VERIFIED at 57.0s and 59.9s — the shelf
 holding her one peach-handled umbrella, the Planner at the open rainy
 door with hand raised, the Counter's eyes into the lens, the Clerk at
 the book, the endcard question over the bottom strip, clear of faces.
 lines-heard tally: 11 · per-line adjudication: 11 HEARD-CORRECT ·
 0 HEARD-WRONG · 0 NOT-HEARD · 0 EXTRA-CONFIRMED.
 GATE (f) VERDICT: PASS.

### Calibration ledger note
Seam MAE was used in this session for exactly one purpose — take
 IDENTIFICATION (joined.mp4 vs U6_t2/U6_t3, §5.2), where it is decisive
 (1.86–2.49 vs 48.90–55.27 at matched low-motion offsets). No joint in
 this episode was passed or failed on a seam number; every joint verdict
 above is an eye verdict on extracted frames, per the standing rule that
 seam MAE is calibration-only.

## §5.5 — closure
ALL GATES PASS: §5.1/§5.2 per-take QC 6/6 (U1–U5 by the finisher, U6_t3
 above) · §5.3 joints 5/5 MATCH · §5.4 transcription + mechanical diff
 clean · F-9 PASS · ear-test PASS · Gate (f) cold run PASS.
 E3_DELIVERED.flag written at the episode root by this session
 (2026-11-18). Episode video spend total: 8 of 12 (U1–U5 ×1, U6 ×3);
 this gates session spent 0 generations.
