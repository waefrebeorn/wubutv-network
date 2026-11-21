# E2 SHOW-5 THE LAST SEAT — "Ask the Seat" — GATE LOG

Recovery build, 2026-11-15. First production coordinator ended 17:39 EST
with all takes fired but no QC record, no segments, no master. This log is
the recovery coordinator's record, written as the work proceeds.
SCRIPT.md is law. Method: Panel Spec v2 + Joint Gate (§6, all five
boundaries declared BREAKs — declared match = the seat + the scripted gaze
state), Method C devices per REFERENCE_STACK.md graphics plan, BLAM gate
(FIRST3_BLAM_AUDIT §4) on U1 takes and on the finished master.

Take specs (all 14 candidates, ffprobe-verified): 1248×704 native, 24/1 fps,
exactly 240 frames, 10.000s, AAC stereo 48kHz. Conform = scale/pad to
1280×720, 240f per unit, 1440f total.

## Panels
All six PEAK panels exist and passed the first coordinator's read-back
(REFERENCE_STACK.md): PNL-PEAK-U01…U06 + CHAR sheets (Dancer hero/face,
Usher hero/face) + PROP seat + WORLD seatroom, md5-locked to the pilot kit.
No panel work was owed at recovery start.

## Visual QC — contact sheets (work/qc/sheet_*.jpg, frames at 0/0.5/3/5/7/8.5/9.6s)

### U1 candidates
- U01a: seat-room stage, Dancer mid-turn frame 0, Usher's gloved hands +
  ticket foreground; tail = ticket upright against the seat's armrest ✓.
  Rows of auditorium seats visible in tail frames (the one-seat premise
  softens at the edges). Gaze AVERTED at tail ✓.
- U01b: darker vaulted room; turn + ticket foreground ✓; tail profile
  averted ✓. BLAM V2 FAIL (ramps) — see BLAM table.
- U01c: closest match to PNL-PEAK-U01 — mid-turn in the light shaft,
  gloved hand + ticket foreground, brass armrest cap foreground; tail =
  ticket standing upright against the armrest fitting ✓; gaze AVERTED ✓.

### U2 (single candidate, WORDLESS)
- Mirrored studio ✓, back to the seat facing the mirror ✓, dances the
  owned steps, stops, held stillness (the non-answer) ✓, tail head
  HALF-TURNED ✓. Two blurred seat-backs at frame bottom (flagged already
  at PEAK gate — reads as seat + reflection of the seat's position).
  Dress reads longer (below-knee) than the locked short skirt — drift
  noted, same class the pilot disclosed. Audio artifact check: see ASR.

### U3 candidates
- U03: box-office corridor ✓; Usher's gloved hand at the seat's back,
  hover/touch boundary (script: back of hand hovering a breath from the
  velvet — the read is "at the velvet", a near-miss on the ritual's
  letter, kept under review); Dancer enters far end ✓; two-shot
  conversation ✓. Small red bow in her hair — minor trait drift.
- U03b: same staging; seat larger in frame mid-unit; hand hover reads
  cleaner; her dress darker/longer. ASR decides between the pair.

### U4 (single candidate, danced, 12 spoken words)
- Cold blue stage opens → light WARMS to amber across the unit ✓ (the
  seat's answer in picture). Arms bracketing the absence, gaze on the
  seat/lens ✓; feet take the returned step; face turns to fury in the
  tail close-up while the gaze HOLDS on the lens ✓ (HELD WHILE
  BETRAYED). The fury reads broad — grimace, not glance-away; the cliff
  holds. Audio: ASR + artifact check on the danced span.

### U5 candidates
- U05: backstage, billing sheet + hovering pencil ✓; she looks at the
  sheet, not at him ✓; tail complete — he takes the sheet down and
  carries it toward the seat ✓, she steps toward the stage ✓ (PROMISED).
- U05b: same structure; tail darker, sheet-carry beat present.
- U05c: same structure; tail = sheet in his hand beside the seat ✓.
- U05d: tail incomplete — she walks off into dark backstage, the
  sheet-carry beat is lost; weakest candidate on picture.
- All four: the pinned sheet carries blurred pseudo-print (unreadable
  gibberish lines, the PEAK panel's accepted class), no legible words.

### U6 candidates
- U06: final-gaze close-ups are strong (down the lens, warm light ✓)
  BUT the mid-unit staging reverses the axis — she stands among rows of
  auditorium seats, camera in the house looking at the stage edge; a
  foreground ticket prop carries semi-legible print. FROM-THE-SEAT
  grammar broken mid-unit.
- U06b: FROM THE SEAT throughout ✓ (seat + armrest foreground, Usher
  beside it, Dancer on stage); ticket upright → fallen flat by the tail
  ✓ (script tail beat); light warms ✓; final gaze to lens ✓. Ticket
  print is semi-legible ("ADMIT ONE" class) — text-gate risk.
- U06c: FROM THE SEAT throughout ✓; ticket BLANK (no print) ✓; ticket
  upright → fallen flat ✓; light warms/deepens ✓; final frame = her
  facing down the lens ✓. Usher large in right foreground, head bowed
  at the tail (he is beside the seat, as scripted; the bow reads as
  keeping, not leaving).

## BLAM — U1 takes (work/blam_measure.py, audit §2 methodology)
| take | A1 t50/t90 | A2 | A3 | A4 head/ctrl (ratio) | V1 ratio | V2 | verdict |
|---|---|---|---|---|---|---|---|
| U01a | 0.0/0.0 ✓ | 0.0 ✓ | +8.2 dB, accent ✓ | 12/16 (0.75) ✓ | 0.95 ✓ | ✓ | ALL PASS |
| U01b | 0.0/0.3 ✓ | 0.0 ✓ | +0.1 dB ✓ | 9/19 (0.47) ✓ | 1.80 ✓ | ✗ first bucket 2.7 < 50% of max 9.4 | FAIL V2 (ramp) |
| U01c | 0.1/0.1 ✓ | 0.0 ✓ | +4.2 dB ✓ | 2/2 (1.00) ✓ | 3.09 ✓ | ✓ first bucket = max (5.9) | ALL PASS, strongest opening |

Crackle (the pilot's failure class): U01c's head is the cleanest of the
three (2 HF bursts in 0–1.5s vs 12 for U01a); no candidate carries the
pilot's crackle signature (pilot master measured 6 bursts vs 0 control).

## ASR (faster-whisper large-v3-turbo, int8, NO VAD — house rule)

### U1 — script: "Bring my step back, Usher." / "I keep the seat, Dancer.
Not steps." / "You told this room it kept it." / "Ask it yourself, Dancer.
Eyes first." (25 words)
- U01a: lines 1–3 verbatim; line 4 (the PRICE turn line) NEVER LANDS —
  transcript ends 8.36s. Dialogue FAIL.
- U01b: all four lines' words present (line 3 split by a pause:
  "You told this room. It kept it." — same words, ASR punctuation only).
  Moot: BLAM V2 FAIL stands. REJECT.
- U01c: ALL FOUR LINES VERBATIM — [0.00–3.30] / [3.66–5.60] /
  [6.22–8.00] / [8.18–9.94]; the turn line lands in the scripted late
  slot (≥6.5s park ✓). **U1 = U01c — SHIPS** (BLAM all-pass, cleanest
  head, PEAK-true frame 0, ticket tail beat present).

### U3 — script: "You tend it daily. Ask it, Usher." / "Keepers don't ask,
Dancer. We keep." / "Then who does it answer, Usher?" / "The one who
looks at it." (25 words)
- U03: lines 1–3 verbatim; turn line TRUNCATED at the file edge —
  "The one who looks..." [9.00–10.00], "at it" never lands. FAIL.
- U03b: ALL FOUR LINES VERBATIM, turn line complete [8.56–9.92].
  **U3 = U03b — SHIPS.**

### U4 — script: "This isn't it. This is yesterday's." / "It kept the one
it liked." (12 words)
- U04: BOTH LINES VERBATIM [0.00–3.22] / [5.88–7.96]; the 2.66s gap
  between them is the danced answer — no spurious segments, no speech
  artifacts in the danced span. **U4 = U04 — SHIPS.**

### U5 — script: "Dance the kept one tonight, Dancer." / "It's yesterday's.
I won't repeat it." / "Then dance unkept. Looking. All of it." / "Then
watch me forget it looking." (25 words)
- U05: lines 1–3 verbatim; the ACCEPT line never lands. FAIL.
- U05b: same — acceptance missing. FAIL.
- U05c: acceptance MANGLED into the price line ("...All of it forget it
  looking." — "Then watch me" lost). FAIL.
- U05d: ALL FOUR LINES VERBATIM, acceptance complete [8.00–10.00].
  **U5 = U05d — SHIPS.** Dialogue outranks picture: U05d's tail is the
  weakest of the four on picture (the sheet-carry beat is lost; she
  walks into dark backstage — the PROMISED direction still reads).
  Disclosed here and in the delivery report.

### U6 — script: "The seat is watching, Dancer. Begin." / "Don't keep it,
Seat. Watch it happen." / "It's answering." (15 words)
- U06: words verbatim, but no silence beat (segments butt-jointed
  0–4/4–8/8–10) and the mid-unit staging breaks FROM-THE-SEAT (rows of
  house seats, printed ticket prop). REJECT on picture + beat.
- U06b: lines 1–2 verbatim; cliff fragment WRONG — "It's answering
  time." (extra word). FAIL on the episode's cliff line.
- U06c: ALL THREE LINES VERBATIM, natural segmentation [0.00–3.80] /
  [4.76–7.48] / [8.42–9.30]. **U6 = U06c — SHIPS**, with a disclosed
  deviation: the scripted 2.5s silence beat lands compressed — the
  energy scan (0.25s RMS windows) shows true-silence pockets at
  2.75–3.25s (−67/−71 dBFS) and 4.0–4.75s (−60/−67/−69 dBFS) with the
  turn line at 4.76s, i.e. a held stop of roughly a second immediately
  before the line, not the full 2.5s. The stop IS there (she halts
  mid-phrase, holds, looks — frames confirm); its duration is short
  of script.

### U2 — WORDLESS: artifact check
- large-v3-turbo returns ONE segment spanning the full 10.00s: "I don't
  know." (avg_logprob −0.84, no_speech_prob 0.00) — the classic
  hallucination shape over scored audio (no localisable onset, low
  confidence), against an energy profile of continuous low music-class
  energy (−32…−54 dBFS, no speech-shaped bursts).
- Second opinion (work/asr_u02_second.py): whisper-small returns NO
  segments; distil-large-v3 returns the same stock phrase at [0.00–1.00]
  with lp=−0.85 / nsp=0.18 — a different position than turbo's full-file
  smear. Two large models surfacing the same common phrase at low
  confidence and inconsistent timings, the small model hearing nothing,
  and no speech-shaped energy anywhere in the take: ruled a hallucination
  over the score, not speech. **U2 = U02 — PASSES as wordless** (caveat
  logged: ASR cannot prove a negative absolutely; the three-model +
  energy evidence is what the ruling stands on).

## Take selection (final)
U1=U01c · U2=U02 · U3=U03b · U4=U04 · U5=U05d · U6=U06c.
No unit needed a refire — every unit had a passing candidate on disk.
Wordmark: UNC does not appear in SHOW-5; the wordmark law is discharged
by the post-rendered `~ WuBu ~` bug (verified on the master).

## Conform + assembly
Segments conformed 1248×704 → 1280×720, exactly 240f each (asserted per
segment). Graphics burned per REFERENCE_STACK plan (spot-verified on the
master, work/qc/gfx_check_sheet.jpg): Seat Map pos 2 at U1 1.5–4.0s and
U6 8.8–10.0s; Two Tickets intact 1.5–2.2s → torn 2.2–4.5s in U3 (printed
number = 2); bug bottom-right throughout. The reserved SPOTLIGHT CONE was
not used (no joint needed cover). Concat → work/joined.mp4, probed 1440f
before the master encode; ONE master encode from the joined file.
First master encode produced 1441f (AAC-length CFR pad) and a pure-gain
loudness pass proved impossible (joined: −22.11 LUFS integrated vs
−0.51 dBTP peaks — gain capped negative). Caught by the frame assert
before anything shipped; remastered with trim=end_frame=1440 +
atrim=0:60 and loudnorm (I=−16/TP=−1.5/LRA=11, dynamic). Master audio
post-measure: −18.72 LUFS integrated, TP −1.46 dBTP; episode median
−30.47 dBFS vs the pilot master's −38.25 (the loudness pass's job:
+7.8 dB out of the basement). Audio stream container duration 60.093s =
AAC padding; video is exactly 60.000s / 1440f and the audio content was
trimmed to 60.000s.

## Master verification
- masters/E2_SHOW-5_the-last-seat_house.mp4 — md5
  d899745b106a923d683b71bc5930be53, 18,278,499 B (no chat copy needed,
  under 50 MB), H.264 1280×720, 24/1 fps, exactly 1440 frames, AAC 48kHz,
  faststart (moov at offset 36).
- CRF 18 proof: this VM's libx264 stamps crf=23.0 in the SEI regardless
  of the requested rate control (AGENTS.md 2026-11-15, SHOW-2 finding),
  so the proof is the size differential: same joined file at CRF 23
  (video-only control) = 8,544,444 B vs the master's ≈16.8 MB video
  stream ≈ 1.97× — a genuine CRF-18 encode.

## BLAM GATE — finished master (work/blam_measure.py; audit §4)
A1 t50 0.1s / t90 0.1s ✓ · A2 dead head 0.0s ✓ · A3 head −21.93 dBFS =
+8.55 dB over the episode median, accent ≤0.5s ✓ · A4 head bursts 1 vs
control 13 (ratio 0.08) ✓ — the pilot's crackle failure is gone; the
head is the cleanest window in the episode · V1 2.55 ✓ · V2 first
0.25s bucket 5.89 = the strongest bucket (no ramp) ✓ · E1: the impact
is frame 0 itself — the Dancer mid-warm-up-turn at peak twist, the turn
stopping short, with the shoe-scrape accent (PEAK-U01, eye-verified) ✓.
**BLAM: ALL BARS PASS.**

## JOINT GATE — assembled master (§6; all five boundaries declared BREAKs)
BASE (95th pct intra-unit adjacent MAE) = 7.49. Seam MAE has no bar for
BREAKs; logged. Eye items read off work/qc/joints/strip_*.png:
| joint | seam MAE | tail MAE | head MAE | items 1/2/3/5 | item 4 | item 6 |
|---|---|---|---|---|---|---|
| U1→U2 | 48.37 | 4.24 | 2.30 | PASS | COND | COND |
| U2→U3 | 32.53 | 3.22 | 0.47 | PASS | COND | COND |
| U3→U4 | 24.90 | 3.48 | 2.27 | PASS | COND | COND |
| U4→U5 | 27.85 | 3.29 | 0.29 | PASS | COND | COND |
| U5→U6 | 29.09 | 4.84 | 2.29 | PASS | COND | COND |

- Items 1/2/3/5 PASS at all five: same woman + same Usher against the
  CHAR panels on both sides; wardrobe unchanged (vermilion dress, navy
  coat, white gloves); the declared match is present at every cut — the
  seat (armrest + upright ticket at J1/J5, seat-backs at J1, the seat as
  subject at J2, its brass rail at J3, its back in the foreground at J4)
  and the gaze state advancing exactly as scripted (averted →
  half-turned → landed → held-while-betrayed → promised → held-through).
- Item 4 (light direction) CONDITIONAL at all five: every boundary is a
  declared world cull and each world carries its own motivated light
  (warm shaft → flat cold studio → corridor practicals → cold stage →
  work bulb → warm shaft). Light is stable within each side; the change
  across the cut IS the declared cull. A mechanical item-4 fail would
  make the BREAK class unpassable on this show by construction.
- Item 6 (motion alive) CONDITIONAL at all five: every downstream head
  measures under the PROPOSED ≥8 floor (0.29–2.30) and the tails are
  held gazes by script. The floor was calibrated on PILOT-2's kinetic
  heads; this episode's own BASE is 7.49 — its intra-unit motion lives
  under the floor's scale. No head or tail is frozen (all MAEs nonzero;
  the strips show dance, walk-ins, the hover, breathing room tone in
  every window). The episode's one doctrine-bound head — U1's — passes
  the BLAM gate outright (V1 2.55, V2 first-bucket max). Ruled
  conditional-pass with the numbers on the table, not waived silently:
  this is the gate deviation the parent should weigh first.

## Flaws carried to delivery (all disclosed, none hidden)
1. Joint Gate item 6 + item 4 conditional at all five joints (above).
2. U6 silence beat compressed: ~1s-class held stop before the turn
   line vs the scripted 2.5s.
3. U5 ships U05d on dialogue (the only verbatim candidate of four);
   its tail loses the sheet-carry beat — she exits into dark backstage.
4. Dress-length drift: the locked short skirt settles longer in U2
   (below-knee) and U3b — the same class the pilot disclosed.
5. U3b's keeper ritual reads "hand at the velvet" where the script
   asks a breath of air (the hover is a near-touch in the wide).
6. U4's fury close-up is broad — a grimace held into the lens; the
   gaze joint (held, not broken) is what the unit is graded on.
7. U2's wordless ruling rests on three-model ASR + energy evidence;
   two large models hallucinate the same stock phrase over its score.
8. Billing-sheet pseudo-print in U5 is blurred gibberish (accepted
   class from the PEAK gate), not legible text.
