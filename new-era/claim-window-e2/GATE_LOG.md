# CLAIM WINDOW — Episode 2 "The Bus Pass" — GATE_LOG

Production: template v6 · FAIL-ONCE cap (first take + ≤1 refire per unit) ·
VOICE_ROUTE: NATIVE_TEXT_ONLY (no TTS of any kind, msg 730 hold).
RECOVERY NOTE: the production coordinator ended without a report after
firing all six first takes and starting QC (frame grabs for all units,
ASR for U1–U3). The recovery finisher resumed from disk 2026-11-19/20:
verified every pre-existing artifact on disk before use, completed QC
for U4–U6, assembled, and ran the master gates. ZERO refires were used
in the whole episode — every unit ships its first take.

## CAST_LOG / panels (verified on disk by the finisher)
- panels/PNL-CHAR-JUNE-hero.png — md5 3559721269a323bdd7565f9ad3a2ce26
  (pilot canonical, reused — matches BRIEF §1).
- panels/PNL-CHAR-PEACH-hero.png — md5 b0b34a709fb9601ec1f12569073e94e8
  (pilot canonical, reused — matches BRIEF §1).
- panels/PNL-PEAK-E2-U1.png — md5 cf109c21062ed2ff7ddbbef64165069e
  (the one image generation of this episode).
- CANONICAL_FACE_REFs: the two hero panels above (BRIEF §1).

## SEQUENCE GATE (BRIEF §3)
- contact sheet: work/sequence_sheet.png (built by the first
  coordinator) + per-unit chained frames eye-read by the finisher.
- seq_story_in_one_sentence: "A peach that lost its bus pass bluffs,
  confesses, and gets it back at the lost-and-found window." — matches
  the brief's required sentence. PASS.

## §5.1 PER-TAKE QC

### TAKE U1_t1 — UNIT U1 — file takes/U1_t1.mp4
- md5 3173b2de3cb6015e02676e645c1be879 · 3,356,376 B · 1248×704 · 24 fps ·
  240 frames · 10.000 s (assembly conforms to 1280×720 — see assembly note)
- qc_frames_checked: 0.0s / 0.3s / 5.0s / 8.0s / last — all eye-read.
- DRIFT ROWS:
  - qc.identity: PASS — June (dark hair, low knot, grey cardigan, white
    shirt) matches the canonical hero panel; the Peach (leaf stem,
    yellow slicker) matches its panel.
  - qc.wardrobe: PASS — the slicker is DRY (Ep2 dry morning); windows
    dry throughout (I-5).
  - qc.prop: PASS — brass counter bell on the counter between them ✓ ·
    rubber stamp at June's hand ✓ · blank form stack ✓ · the closed
    umbrella is under the Peach's arm, crook handle up, NEVER opened
    (I-7 ✓; it appears in U1 only, as scripted).
  - qc.motion: PASS — motion_at_cut_in: Y (frame 0: the Peach mid-shout,
    mouth wide open, leaning in; June seated, unimpressed).
  - text check: wall notice and clock carry texture only; no legible
    generated words anywhere.
- ASR-VS-SCRIPT DIFF (dual Whisper checkpoints, work/qc/U1_t1_asr.json):
  - large-v3: "It's gone! The pass is gone!" 0.0–2.2 · "You left with
    it yesterday." 4.34–5.84 · "Yesterday lied!" 7.82–8.94 — all three
    scripted lines verbatim, correct speakers by picture; missing
    none · extra none · garbled none.
  - distil-large-v3: identical three lines verbatim.
- HEAD CHECK (I-1): the unit carries a head-SPEECH assertion and it
  lands — first spoken word at 0.0s in BOTH checkpoints (target
  ≤0.5s): PASS. head RMS 0–1.7s = 0.1884; ambient 0–0.5s = 0.1593
  (the shout itself). This is the episode's headline improvement over
  the pilot's 1.17s.
- END-STATE vs pin: Peach leaning in, hands on the counter/sill edge ✓ ·
  June seated, unimpressed, bell and stamp in place ✓ — MATCH.
- TAIL-DRIFT: last frame (work/qc/U1_lastframe.png) may anchor U2: Y.
- VERDICT: **KEEP t1.** Refire not used. Spend so far: video 1/12 ·
  images 1/3.

### JOINT J1: U1 → U2
- joint_end_state_quoted: "Peach leaning in, both hands on the counter
  edge; June seated, unimpressed, bell and stamp in place."
- joint_actual_last_frame: work/qc/U1_lastframe.png
- joint_next_first_frame: work/qc/U2_t1_f_0.2.png (0.2s)
- joint_eye_verdict: MATCH — identical framing, set, positions,
  wardrobe and warm light; the Peach's head-down lean carries straight
  into U2's scribble beat; June is mid-line at the cut.
- joint_mismatch_class: none.

### TAKE U2_t1 — UNIT U2 — file takes/U2_t1.mp4
- md5 153c1b5a52e3520ca8e3b6134cc1bde1 · 3,120,210 B · 1248×704 · 24 fps ·
  240 frames · 10.000 s
- qc_frames_checked: 0.2s / 4.0s / 8.0s / last + form zoom
  (work/qc/U2_form_zoom.png) — all eye-read.
- DRIFT ROWS:
  - qc.identity: PASS — June and the Peach consistent with U1 and the
    canonical panels (I-4: June's hair dark, low knot, unchanged).
  - qc.wardrobe: PASS.
  - qc.prop: PASS — form slid, scribbled head-down (the picture answer
    lands), held up for the readback ✓ · bell ✓ · stamp ✓ (in June's
    hand at the open, on the counter for the readback) · form stack ✓.
  - qc.motion: PASS — motion_at_cut_in: Y (continuous out of U1's lean).
  - text check (I-6, PARTIAL — disclosed): the held form carries
    printed-form texture — ruled lines, small print-like marks,
    hexagonal stamp logos, and one small "A4"-like mark (see the zoom).
    NO legible words anywhere: the header line is an unreadable smudge
    and the Peach's "writing" is pure scribble, which is what the bit
    requires. Same disclosed-NIT class as the pilot's U2 form texture;
    NOT the reject class (no large/centred legible words; the words
    "Lost Property" appear nowhere in the episode).
  - performance: June's readback is flat and dry (an improvement on the
    pilot's more animated U2 readback).
- ASR-VS-SCRIPT DIFF (work/qc/U2_t1_asr.json):
  - large-v3: "The form, colour, photo, what's stuck underneath?"
    0.0–4.2 · "Very pass. That's not a description, that's a habit."
    5.52–9.18 — both scripted June lines complete and verbatim
    (modulo punctuation); the QUOTABLE lands whole.
  - distil-large-v3: identical content ("colour" spelled as scripted).
  - The Peach is silent throughout: PASS (Camp B — the scribble is the
    picture answer).
- HEAD CHECK: speech (line 1) begins at 0.0s as the form beat opens;
  nothing precedes it; no extra words.
- END-STATE vs pin: form held up between them ✓ · Peach's pen down
  (a pen rests on the form stack) ✓ · Peach head bowed over folded
  arms — MATCH.
- TAIL-DRIFT: last frame (work/qc/U2_lastframe.png) may anchor U3: Y.
- VERDICT: **KEEP t1.** Refire not used. Spend: video 2/12 · images 1/3.

### JOINT J2: U2 → U3
- joint_end_state_quoted: "the form on the counter between them,
  Peach's pen down, June holding the form up."
- joint_actual_last_frame: work/qc/U2_lastframe.png
- joint_next_first_frame: work/qc/U3_t1_f_0.2.png (0.2s)
- joint_eye_verdict: MATCH with a GEOMETRY note — U3's head frame is
  wider (the full umbrella rack reads at frame-left) while June ducks
  behind the counter; by 4.0s the framing settles back to the locked
  two-shot. The widen is the named event (THE PULL) beginning, not
  drift of world, wardrobe or light.
- joint_mismatch_class: GEOMETRY (minor, disclosed).

### TAKE U3_t1 — UNIT U3 — file takes/U3_t1.mp4
- md5 7659909ffa76871de4e4043979c5022c · 2,997,011 B · 1248×704 · 24 fps ·
  240 frames · 10.000 s
- qc_frames_checked: 0.2s / 4.0s / 8.0s / last — all eye-read.
- DRIFT ROWS:
  - qc.identity: PASS — June (dark low knot) and the Peach consistent;
    the Peach reads face-on here (it was downcast in U1/U2) — same
    character design.
  - qc.wardrobe: PASS.
  - qc.prop: PASS with note — THE PULL lands: June ducks at the open
    and hauls out the long coat; its inside is lined with DOZENS of
    pinned bus passes — coloured cards with simple shapes (circles,
    dots, small glyphs), NO letters or words on any card (I-6 ✓ for
    the proof object). June's hand ends flat on the coat ✓. NOTE
    (I-2): the bell, stamp and form stack are all present on the
    counter in the head frames (0.2s) and are then OCCLUDED by the
    coat — the unit's named proof object — for the rest of the unit.
    Presence in the unit: confirmed; occlusion disclosed.
  - qc.motion: PASS — motion_at_cut_in: Y (June mid-duck at 0.2s).
  - text check: wall notices texture only; the pass cards are shapes
    only. No legible words.
- ASR-VS-SCRIPT DIFF (work/qc/U3_t1_asr.json):
  - large-v3: "Collector's edition. Yours?" 1.78–3.62 · "I wish it
    was." 4.0–5.1 · "First honest answer today." 6.9–8.78 — all three
    lines verbatim, correct speakers; missing none · extra none ·
    garbled none.
  - distil-large-v3: identical content ("Collectors" = ASR spelling).
- HEAD CHECK: no speech before line 1 (first onset 1.78s, as the coat
  lands); head RMS 0–1.7s = 0.0085 (a quiet room — the pull is a
  picture beat before the line).
- END-STATE vs pin: the coat draped over the counter between them,
  coloured pass cards visible ✓ · Peach staring at it ✓ · June's hand
  flat on the coat ✓ — MATCH.
- TAIL-DRIFT: last frame (work/qc/U3_lastframe.png) may anchor U4: Y.
- VERDICT: **KEEP t1.** Refire not used. Spend: video 3/12 · images 1/3.

### JOINT J3: U3 → U4
- joint_end_state_quoted: "the coat draped over the counter between
  them, coloured pass cards visible; Peach staring at it; June's hand
  flat on the coat."
- joint_actual_last_frame: work/qc/U3_lastframe.png
- joint_next_first_frame: work/qc/U4_t1_f_0.2.png (0.2s)
- joint_eye_verdict: REPAIR (disclosed, no action — fail-once
  discipline): U4 recomposes to a counter-side angle (the service
  glass panel reads prominently at frame-right) and the coat is gone
  across the cut — its removal is an off-screen state change, as with
  the pilot's umbrella. World, wardrobe, positions and light hold,
  and — the improvement over the pilot's J3 — ALL the I-2 props are
  present in U4 (bell, stamp, form stack), so the break is geometry
  only. The take's performance and end-state are correct (see U4);
  a refire was judged more likely to harm than help (the pilot's U4
  refire produced a world swap with legible text) and was NOT used.
- joint_mismatch_class: GEOMETRY — disclosed at the master gate.

### TAKE U4_t1 — UNIT U4 — file takes/U4_t1.mp4
- md5 c388576164c589a13fc70fcdedc1fd75 · 2,500,433 B · 1248×704 · 24 fps ·
  240 frames · 10.000 s
- qc_frames_checked: 0.2s / 4.0s / 8.0s / last — all eye-read.
- DRIFT ROWS:
  - qc.identity: PASS — June's hair dark, low bun (I-4 ✓); the Peach
    consistent.
  - qc.wardrobe: PASS.
  - qc.prop: PASS (I-2) — brass bell ✓ (foreground; NIT: a second bell
    reads on the back desk in the head frame — prop duplication,
    minor) · rubber stamp ✓ prominent on the counter · form stack ✓ ·
    the new form ends in June's hand ✓ (the unit's proof object).
  - qc.motion: PASS — motion_at_cut_in: Y. Framing recomposed (see
    J3) — the episode's one I-3 deviation, disclosed.
  - performance: the growth beat plays — the Peach's hands are clasped
    and STILL on the counter (head bowed at the open), and June ends
    standing, turning toward the back shelves with the form.
  - text check: wall notices texture only; no legible words.
- ASR-VS-SCRIPT DIFF (work/qc/U4_t1_asr.json + Rumble adjudication
  work/qc/U4_t1_rumble.txt):
  - large-v3: "Okay, so technically, mum's photo on it, torn corner."
    2.16–6.52 · "I need that bus." 8.34–9.32 — the one scripted line
    complete and verbatim ("mum's" = ASR spelling of "Mom's", as in
    the pilot).
  - distil-large-v3: the same line complete, verbatim.
  - Rumble-2-Flash (checkpoint B, non-Whisper): "Okay, so technically,
    mum's photo on it, torn corner. I need that bus." — third
    architecture agrees in full. No adjudication needed.
  - June silent throughout: PASS (Camp B). The catchphrase lands clean
    in U4 — one unit earlier than the pilot, as scripted.
- HEAD CHECK: no speech before the line (onset 2.16s — the bus-brake
  beat and the Peach gathering itself; head RMS 0–1.7s = 0.1167 is
  ambient/brake, word-free in both checkpoints).
- END-STATE vs pin: Peach's hands still on the counter ✓ · June
  standing, turning toward the back shelves, the new form in her
  hand ✓ — MATCH.
- TAIL-DRIFT: last frame (work/qc/U4_lastframe.png) may anchor U5: Y
  (June already at the shelves side, form in hand).
- VERDICT: **KEEP t1.** Refire not used. Spend: video 4/12 · images 1/3.

### JOINT J4: U4 → U5
- joint_end_state_quoted: "Peach's hands still on the counter for
  once; June standing, turning toward the back shelves, the new form
  in her hand."
- joint_actual_last_frame: work/qc/U4_lastframe.png
- joint_next_first_frame: work/qc/U5_t1_f_0.2.png (0.2s)
- joint_eye_verdict: MATCH — June's turn to the shelves flows straight
  into U5's intake-tray geography (the brief's declared U5 exception);
  world, wardrobe and light hold; the Peach stays bowed at the window.
- joint_mismatch_class: none.

### TAKE U5_t1 — UNIT U5 — file takes/U5_t1.mp4
- md5 4fbf4f38d8091bfffbc16c6af88e4905 · 2,279,227 B · 1248×704 · 24 fps ·
  240 frames · 10.000 s
- qc_frames_checked: 0.2s / 4.0s / 8.0s / last — all eye-read.
- DRIFT ROWS:
  - qc.identity: PASS — June consistent (dark bun); the Peach
    consistent.
  - qc.wardrobe: PASS.
  - qc.prop: PASS (I-2) — bell ✓ (foreground) · stamp ✓ on the
    counter · form stack ✓ · PROOF OBJECT: June lifts the YELLOW bus
    pass out of the morning intake tray — the pass carries a small
    simple peach icon (no face detail) and texture print only, NO
    legible text (I-6 ✓). NIT: the pass's torn corner is not clearly
    readable at QC resolution (the spoken inventory carries it).
  - qc.motion: PASS — motion_at_cut_in: Y (June mid-search in the
    tray at 0.2s).
  - performance: June DESCRIBES, properly, the way she demands — the
    mirror beat lands. NIT: the Peach's hands rest on the sill rather
    than pressed to the glass as the pin words it (minor).
  - text check: wall notices texture only; no legible words; no
    weather effects (I-5 ✓ — dry light, blinds).
- ASR-VS-SCRIPT DIFF (work/qc/U5_t1_asr.json + work/qc/U5_t1_rumble.txt):
  - large-v3: "Driver handed this in at 7." 1.94–3.44 · "Torn corner."
    6.30–7.14 · "Little peach in the photo." 7.68–9.14 — both scripted
    lines complete and verbatim ("7" = ASR rendering of "seven").
  - distil-large-v3: "Driver handed this in at seven. Torn corner.
    Little peach in the photo." — verbatim.
  - Rumble: "Driver handed this in at 7. Torn corner. Little peach in
    the photo." — third architecture agrees. No adjudication needed.
  - The Peach silent throughout: PASS (Camp B).
- HEAD CHECK: quiet head (head RMS 0–1.7s = 0.0182); first speech
  1.94s as June lifts the pass; nothing precedes it.
- END-STATE vs pin: June at the shelves holding the yellow pass up ✓ ·
  Peach at the window, head bowed, hands on the sill (pin: pressed to
  the glass — minor deviation, above) — MATCH with NIT.
- TAIL-DRIFT: last frame (work/qc/U5_lastframe.png) may anchor U6: Y.
- VERDICT: **KEEP t1.** Refire not used. Spend: video 5/12 · images 1/3.

### JOINT J5: U5 → U6
- joint_end_state_quoted: "June at the shelves holding the yellow pass
  up; Peach at the window, hands pressed to the glass."
- joint_actual_last_frame: work/qc/U5_lastframe.png
- joint_next_first_frame: work/qc/U6_t1_f_0.2.png (0.2s)
- joint_eye_verdict: MATCH — U6 opens on the identical state: June
  standing, holding the pass up, examining it; the Peach bowed at the
  window; same framing family, wardrobe, props and light. (The
  pilot's J5 recompose does NOT recur.)
- joint_mismatch_class: none.

### TAKE U6_t1 — UNIT U6 — file takes/U6_t1.mp4
- md5 00cb480a474d53b714aa0697444ce3f5 · 2,943,097 B · 1248×704 · 24 fps ·
  240 frames · 10.000 s
- qc_frames_checked: 0.2s / 4.0s / 5.0s / 6.0s / 8.0s / last — all
  eye-read (5.0s and 6.0s grabbed by the finisher to verify the stamp
  beat).
- THE PAYOFF LANDS: June hands the pass over FIRST (4.0s — the Peach
  holds the pass as June reaches for the stamp). Then the stamp is
  slid across, and at 5.0s THE PEACH GRIPS THE STAMP WITH BOTH HANDS
  AND PRESSES IT onto its own form — the red smudge is on the form
  under the stamp (work/qc/U6_t1_f_5.0.png). June's audible tell,
  trusted into the claimant's hands, on screen, irreversible. At 8.0s
  the Peach holds the pass up, delighted; June watches with the
  scripted small smile. In the last frame the Peach has turned for
  the bus (a sliver of yellow at frame-right) — mid-consequence, as
  pinned.
- DRIFT ROWS:
  - qc.identity: PASS — June's hair stays dark and low-knotted in
    every checked frame (I-4 ✓ — the pilot's U6 hair-lightening does
    NOT recur); the Peach consistent.
  - qc.wardrobe: PASS.
  - qc.prop: PASS (I-2) — bell ✓ · stamp ✓ (slid, gripped, pressed;
    ends resting on the form stack beside its red smudge) · form
    stack ✓ · the yellow pass ✓ (held up at 8.0s; a second small card
    reads on the counter by the Peach's hand).
  - qc.motion: PASS — motion_at_cut_in: Y (continuous out of U5).
  - performance NIT (disclosed): June's smile in the FINAL frame is a
    broad laugh as the Peach exits — broader than the scripted "one
    small smile" (the restrained version is present at 8.0s, the
    poster frame). Same class as the pilot's U6 smile nit.
  - text check: wall notices texture only; the pass and forms carry
    texture/icon only; NO legible words anywhere (I-6 ✓); the words
    "Lost Property" appear nowhere in the episode.
- ASR-VS-SCRIPT DIFF (work/qc/U6_t1_asr.json + work/qc/U6_t1_rumble.txt):
  - large-v3: "Describe it again." 2.48–3.36 · "Yellow." 3.50–3.84 ·
    "Mum's photo." 5.12–6.02 · "Torn corner." 6.66–7.34 · "Now it's a
    description." 7.52–8.78 — all three scripted lines complete and
    verbatim, correct speakers by picture (June / Peach / June).
  - distil-large-v3: identical lines verbatim.
  - Rumble: "Describe it again. Yellow. Mum's photo. Torn corner. Now
    it's a description." — third architecture agrees in full.
  - The KEEP-LIST line "Now it's a description." lands clean.
- HEAD CHECK: quiet head (head RMS 0–1.7s = 0.0095) — June's return
  with the pass is a picture beat; first speech 2.48s; nothing
  precedes it, no extra words.
- END-STATE vs pin: Peach holding the pass up, delighted ✓ · the
  stamped form on the counter ✓ · the stamp used by the Peach's own
  hands ✓ (it rests on the stack in the final frame) · June watching
  with one small smile ✓ at 8.0s (final-frame laugh broader — NIT
  above) · yesterday's form on the wall behind her: wall notices
  present as texture, not individually verifiable · the Peach turns
  for the bus ✓ — MATCH with NITs.
- VERDICT: **KEEP t1.** Refire not used (the payoff performance is the
  episode's landing; remaining flaws are disclose-class).
  Spend: video 6/12 · images 1/3.

## §5.2 VOICE CHECK (per speaker, whole episode — native route)
- diar/adjudication method: dual Whisper checkpoints (large-v3 +
  distil-large-v3) per take and on the master, Rumble-2-Flash as the
  non-Whisper adjudicator (U4/U5/U6 takes + full master), RMS spans
  as ground truth.
- JUNE: PASS-EAR-ONLY (native generated voice, no enrollment exists
  on the NATIVE_TEXT_ONLY route) — dry, low, unhurried in U1/U2/U3/
  U5/U6; silent in U4 as scripted. No voice mismatch in the
  transcript evidence; drift class disclosed in BRIEF §0.
- THE PEACH: PASS-EAR-ONLY — bright and theatrical U1–U3, plain and
  quiet for the U4 truth line (the scripted register deviation
  lands), delighted U6. No voice mismatch.
- EAR_TEST (per unit, from take ASR + picture): U1 PASS · U2 PASS ·
  U3 PASS · U4 PASS · U5 PASS · U6 PASS. Master ear test below.

## ASSEMBLY RECORD
- Kept takes, in order: U1_t1 · U2_t1 · U3_t1 · U4_t1 · U5_t1 · U6_t1
  (each 240f @ 1248×704). Rejected takes: NONE. Outtakes: none.
- ONE assembly pass owns work/assembly/joined.mp4: per-segment conform
  scale 1248×704 → 1280×720 (non-uniformity <0.3%), setsar, fps 24;
  audio aresample 48kHz, mono→stereo pan, per-segment atrim 0:10
  (removes the ~27ms/take AAC overhang). joined.mp4 probe BEFORE the
  master encode: 1280×720 · 24 fps · video 1440 frames / 60.000s ·
  audio 60.000s ✓ (= the 6×240f segment sum exactly).
- Master encode: single uninterrupted pass from joined.mp4, bug
  overlay (work/assembly/bug.png, full-frame 1280×720, eof_action=
  repeat), audio atrim 0:60, libx264 CRF 18 preset medium, AAC 160k
  48kHz, faststart. (One earlier encode was discarded before delivery:
  its audio stream probed 60.010s; the shipped encode bounds the
  audio to exactly 60.000s and probes clean end to end below.)
- MASTER PROBE (end to end): masters/CLAIM_WINDOW_E2_16x9.mp4 —
  h264 1280×720 · 24/1 fps · 1440 frames (counted) · video 60.000s ·
  AAC 48kHz stereo, audio stream 60.000s · format duration 60.000s ·
  19,278,015 B · md5 16026b2d85aebb44b634aaf2525de565 · faststart ✓
  (moov at byte 36, before mdat).
- CRF-18 PROOF (size differential; the SEI string on this VM always
  reads 23.0 and is not evidence): CRF-23 encode of the same
  joined.mp4 (same bug overlay + audio bound) = 10,331,653 B →
  master/CRF23 = 1.87×. CRF 18 confirmed.
- Chat copy: masters/CLAIM_WINDOW_E2_chat.mp4 — byte copy of the
  master (19,278,015 B ≤ 50MB), md5 identical
  16026b2d85aebb44b634aaf2525de565.
- Poster: masters/CLAIM_WINDOW_E2_poster.png (master t=58.0s — the
  Peach holding its pass up, June's small smile, the stamp and its
  red smudge on the form stack), md5 3de6337d8d6a97690a4b79d643188fce.

## §5.4 MASTER GATES
MASTER TRANSCRIPTION PROTOCOL: asr_take.py on the master's own audio —
faster-whisper large-v3 + distil-large-v3, float32-array feed,
vad_filter=True, condition_on_previous_text=False, word_timestamps=True
(work/qc/master_asr.json) + Rumble-2-Flash (non-Whisper architecture)
full-master pass (work/qc/master_rumble.txt) + RMS adjudication.

F-9 SPEAKER-ATTRIBUTED TRANSCRIPT (master's own audio; picture
summaries interleaved; speakers attributed from the picture record):
- U1 (0–10s) [the Peach bursts in mid-shout at the window, closed
  umbrella under its arm; June seated, unimpressed]
  PEACH 0.00–2.48: "It's gone! The pass is gone!"
  JUNE 4.86–6.16: "You left with it yesterday."
  PEACH 8.08–9.32: "Yesterday lied!"
- U2 (10–20s) [June slides the form; the Peach scribbles head-down;
  June holds the form up and reads it back]
  JUNE 10.28–14.46: "The form, colour, photo, what's stuck
  underneath?"
  JUNE 15.54–19.40: "Very pass. That's not a description, that's a
  habit."
- U3 (20–30s) [June ducks and hauls the coat lined with dozens of
  pinned bus passes onto the counter; the Peach stares]
  JUNE 22.08–23.82: "Collector's edition. Yours?"
  PEACH 24.12–25.40: "I wish it was."
  JUNE 26.94–28.94: "First honest answer today."
- U4 (30–40s) [the Peach, hands clasped and still for once, drops the
  act; June stands and turns to the shelves with the new form]
  PEACH 32.16–39.56: "Okay, so technically, Mom's photo on it. Torn
  corner. I need that bus."
- U5 (40–50s) [June at the intake tray lifts the yellow pass out and
  describes it; the Peach waits at the window]
  JUNE 42.32–43.64: "Driver handed this in at seven."
  JUNE 46.70–47.30: "Torn corner."
  JUNE 48.26–49.34: "Little peach in the photo."
- U6 (50–60s) [June hands the pass over FIRST; slides the stamp
  across; the Peach stamps its own form, then holds the pass up]
  JUNE 52.92–53.48: "Describe it again."
  PEACH 53.74–57.42: "Yellow. Mom's photo. Torn corner."
  JUNE 58.04–58.98: "Now it's a description."
MECHANICAL DIFF:
  diff_script_lines_total: 14
  diff_lines_missing_in_asr: none
  diff_lines_extra_in_asr: none
  diff_words_in_vad_silence: 0 — large-v3 merges segments across
    joints over the room tone (the pilot's known VAD behaviour), but
    distil-large-v3 segments every line inside its own unit and no
    word is timestamped inside a scripted silence.
  diff_disagreement_spans: NONE. All three architectures (large-v3,
    distil-large-v3, Rumble-2-Flash) return the same 14 lines in the
    same order on the master's own audio; Rumble's full-master
    transcript is verbatim line-for-line. The only variations are
    ASR spellings ("mum's" for "Mom's", "7" for "seven"), as in the
    pilot. Nothing required adjudication.
  diff_per_line_wps_outliers: none (all lines within the §4 budgets
    and their measured spans; no span exceeds its 10s container).
EAR TEST SIGN-OFF: ear_flagged_spans_listened: 0/0 (no disagreement
  spans exist to flag) · ear_full_master_listened_at_speed: the full
  master transcript was read cold against the picture record in
  sequence · ear_reviewer: recovery finisher (the standing
  machine-ear protocol for the NATIVE_TEXT_ONLY route:
  triple-checkpoint transcript + RMS adjudication on the master's own
  audio) · ear_verdict: PASS · ear_fail_lines: none.
GATE (f) — THE COLD RUN: cold_reviewer: recovery finisher, working
  from the master's transcript + muted frame record only ·
  cold_pass1_at_speed_no_pause: Y · cold_understood: Y ·
  cold_story_in_one_sentence: "A peach that lost its bus pass bluffs
  out of habit, confesses early, and gets it back at the lost-and-
  found window — and the clerk trusts it with her stamp." ·
  cold_first_confusion_at: none at story level ·
  cold_lines_heard: 14/14 · cold_verdict: SHIP.
ZHE CHECKS: zhe_surface_accuracy: Y — the counts agree across the
  episode: one pass lost (U1), one bluffed form (U2), dozens of other
  people's passes (U3), the truth's two facts (U4: mom's photo, torn
  corner) are exactly what June finds (U5: torn corner, peach in the
  photo) and exactly what the Peach repeats back (U6: yellow, mom's
  photo, torn corner) · zhe_next_step_legible: Y — the episode closes
  mid-consequence (the Peach turns for its bus; June's trust is the
  open debt Part 3 would collect) · zhe_muted_test: Y — sound off,
  the story reads from the frames alone: shout → form → coat of
  passes → bowed confession → the shelves → the yellow pass → the
  stamp in the Peach's hands → the pass held up.
POSTER FRAME: frame_one_still: work/qc/master_head.png (0.2s — the
  Peach mid-shout at the window, umbrella under its arm, June
  stone-faced) · poster_pitch_read: the frame alone pitches the
  episode — a furious peach demanding, a clerk refusing ·
  poster_frame_verdict: PASS. (Shipped poster is the t=58.0s payoff
  frame — see Assembly Record.)
FLOOR CHECK (STRANGER) — MASTER: Q1 want-recovery: PEACH → get its
  mother's bus pass back (enacted: panic, bluff, confession — never
  announced); JUNE → run the window by description, and protect
  yesterday's broken rule from becoming a habit (enacted: procedure,
  then trust) · Q2 exchange scoring: every exchange answered or
  topped, including the U2 picture answer · stage_lines: 0 · Q4
  gossip retell matches the locked story · stranger_master_verdict:
  PASS.
TASTE TEST (MASTER) — QUOTE-BACK: taste_master_reader: recovery
  finisher, from the master's own transcript · quote_back_line:
  "That's not a description — that's a habit." (15.54s on the master;
  also quotable: "Yesterday lied." and "Now it's a description.") ·
  show_off_named: THE PEACH — signature "Okay so technically—",
  landing clean in U4, one unit earlier than the pilot, exactly as
  the growth beat was scripted · gossip_attitude: "The peach came
  back the next morning and lied out of pure habit about a bus pass,
  then told the truth a whole scene earlier than last time — it's
  learning, and the clerk knows it, because she let it stamp its own
  form." — judgment word: habitual · taste_master_verdict: PASS.
BLAM (master): I-1 HEADLINE — first spoken word at 0.00s on the
  master (target ≤0.5s): PASS — the pilot's 1.17s fail is fixed ·
  E1 named impact — the Peach's shout lands at frame 0 (mid-shout,
  mouth open, speech onset 0.0s) ≤1.0s: PASS · A2 dead head — none:
  head RMS 0–0.2s = 0.1488 against a quiet-room floor, speech from
  frame 0: PASS · A3 head level — head RMS 0–0.5s = 0.2247 vs the
  whole-master per-second median 0.0840: the head is hot (the shout),
  no quiet ramp or crackle: PASS · V1 opening motion — head 0–2s
  mean abs frame diff 3.17 vs whole-file mean 3.02 = 1.05× (≥0.6×):
  PASS (the file's motion peak is U3's coat pull, 7.19–9.30 per 2s
  window — the head is not compared against the peak) · A1
  cumulative-energy form — t50 0.80s / t90 2.35s against the ≤0.5s /
  ≤1.5s thresholds: FAIL, DISCLOSED. The metric is computed over the
  first 3s, which contain U1 line 1 (0–2.2s) and the scripted pause
  before line 2 (4.34s, outside the window); both numbers improve
  sharply on the pilot (t50 1.89s / t90 2.71s), and the brief's own
  I-1 first-word requirement passes at 0.00s. Recorded honestly;
  shipped under the fail-once disclosure rule.
WORDMARK: "~ WuBu ~" bug eye-verified PRESENT in gold, bottom-right,
  on the head frame (0.2s, work/qc/master_head.png) and the tail
  frame (59.5s, work/qc/master_tail.png): PASS.
STRUCTURAL: PASS — 1440f / 60.000s / 1280×720 / 24fps / AAC 48kHz /
  faststart, probed end to end.
IMPROVEMENTS I-1..I-7 (master-level roll-up): I-1 PASS (0.00s) ·
  I-2 PASS (bell + stamp + form stack present in every unit; U3
  occluded by the coat after its head frames) · I-3 PARTIAL (locked
  two-shot holds U1–U2 and U3's body; U3's head frame widens for the
  duck; U4 recomposes; U5 is the brief's declared shelves exception;
  U6 is continuous with U5 and does NOT recompose at the joint — the
  pilot's J5 flaw fixed, its J3 flaw repeated in geometry only) ·
  I-4 PASS (June's hair dark and low-knotted in every unit; the
  pilot's U6 lightening does not recur) · I-5 PASS (dry morning, no
  weather effects anywhere) · I-6 PARTIAL (no legible words anywhere
  and "Lost Property" never appears — the pilot's two text flaws are
  fixed; U2's form carries print texture + one small "A4"-like mark,
  disclosed) · I-7 PASS (umbrella closed under the Peach's arm in U1
  only, never opened).

## §5.5 DELIVERY — CAPTION STEP
CAPTION_RULE: form TORN_FRAGMENT (from the QUOTABLE) — caption:
  "That's not a description — that's a habit."
INTENDED_ACTION: watch Episode 3 / follow the show.

## SPEND (final)
- video generations: 6/12 — U1_t1, U2_t1, U3_t1, U4_t1, U5_t1, U6_t1.
  ZERO refires used (the first episode of the show to need none).
  No 429s; budget never exhausted. (First coordinator fired the 6
  takes + the peak panel; the finisher fired nothing.)
- image generations: 1/3 — PNL-PEAK-E2-U1 (the two hero panels were
  reused from the pilot at zero cost, md5-verified).

## DISCLOSED FLAWS (consolidated — everything the gates found)
1. BLAM A1 energy-form FAIL: t50 0.80s / t90 2.35s vs the ≤0.5s /
   ≤1.5s thresholds — while the binding I-1 first-word target PASSES
   at 0.00s (pilot: 1.17s) and E1/A2/A3/V1 all pass.
2. I-3 partial / J3: U4 recomposes to a counter-side angle (glass
   panel prominent) and U3's head frame widens during the duck; the
   coat's removal across J3 is an off-screen state change. All I-2
   props survive into U4 (the pilot's prop loss does not recur), and
   J5 — the pilot's other recompose — is a clean MATCH here.
3. I-6 partial / U2: the held claim form carries printed-form texture
   (ruled lines, print-like marks, stamp logos, one small "A4"-like
   mark). No legible words anywhere in the episode; "Lost Property"
   never appears.
4. U3: the bell, stamp and form stack are occluded by the coat after
   the unit's head frames (present in the unit; the coat is the
   named proof object).
5. U4: a second, duplicate bell reads on the back desk in the head
   frame (prop duplication, minor).
6. U5: the Peach's hands rest on the sill rather than pressed to the
   glass as the end-state pin words it; the yellow pass's torn corner
   is not clearly readable at QC resolution (its spoken inventory is
   exact in U4/U5/U6).
7. U6: June's smile in the final frame is a broad laugh as the Peach
   exits — broader than the scripted "one small smile" (the
   restrained smile is present at 8.0s / the poster frame).
8. Takes generate at 1248×704 and were scale-conformed to 1280×720
   in assembly (<0.3% non-uniformity, invisible in practice).
9. One master encode was discarded before delivery (audio stream
   60.010s); the shipped master probes exactly 60.000s video /
   60.000s audio / 1440 frames.
