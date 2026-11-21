# ON AIR E2 "Show Me How" — GATE LOG

**Provenance:** production coordinator 1 fired all six units
(takes/U*_take1.mp4, fire log in VEHICLES.md), ran frame/ASR QC
and wordmark sweeps, and died on a runtime transport error
(sqlx pool timeout) mid-QC — newest artifact work/qc/wm/
u3_drift_*.png ~01:50 EST 2026-11-17. No segments, no master,
no gate log. This log is completed by the REPLACEMENT
coordinator from the disk state: coordinator 1's QC artifacts
re-adjudicated by eye, hard-gate failures refired once each
under the replacement brief's 8-call allowance, then segments,
assembly, master gates, F-9.

## TAKE PROBES (take1 set, as inherited)

All six takes: 1248×704, 24fps, 240 frames, 10.000s, AAC
audio. (Generator native raster; segments upscale to
1280×720 per the E1 recipe.)

## DIALOGUE GATE (ASR vs SCRIPT.md) — take1 set

- U1: 19/19 lines present. Two ASR-ambiguous tokens ("sheep"
  p=0.52 for "sheet"; "wanted" p=0.00 for "want") — recognizer
  artifacts, E1 precedent (cf. E1 U2 "Strips"). PASS.
- U2: 28/38 — FAIL. UNC line exact; PETER line exact ("UNC"
  ASR-rendered "UN4"); CHAMPION line TRUNCATED — "Number
  Four." missing (the number announced aloud is an F-3 story
  beat, not decoration); COLONEL intercom line TRUNCATED —
  "A false name and I cancel the advertiser." missing. Both
  wants survive, both tails are locked-script content.
  → REFIRE (dialogue hard gate).
- U3: 17/17 EXACT. PASS on dialogue (fails wordmark, below).
- U4: 19/19 EXACT. PASS on dialogue (fails picture, below).
- U5: 17/17 EXACT — direct address + Colonel execution line
  verbatim. PASS.
- U6: 0 scripted dialogue; the cat's sung line ("A singer is
  just a mouth with paperwork", ASR 1.06–5.42s) is the designed
  U6 content. PASS.

## WORDMARK GATE (full-span sweep, coordinator 1's frames
## re-adjudicated by eye)

- U1: `~ WuBu ~` exact wherever legible (f_0.0 confirmed).
  PASS.
- U2: main glyphs intact where visible, BUT flaw F-b
  confirmed by eye at f_3.0: a line of small prompt-echo print
  ("'prominently printed pr…") sits under the wordmark during
  the badge action. Text artifact on the chest. → covered by
  the U2 dialogue refire; re-swept on the new take.
- U3: FAIL — DRIFT. Zoom + drift strip (work/qc/wm/
  u3_t3_zoom.png, u3_drift_b.png): the chest reads
  "~~ WuEu ~~" / "~~ WuBu ~~" — DOUBLE tildes both sides
  persistently across ~2–6s, B intermittently rendered as E.
  Hard QC fail under the standing wordmark ruling.
  → REFIRE (exactly one, per the ruling).
- U4: glyphs exact in the tail frames (f_7.0/f_9.9 read
  `~ WuBu ~`). PASS on glyphs (fails picture, below).
- U5: `~ WuBu ~` exact (f_0.0, f_9.9). PASS.
- U6: `~ WuBu ~` exact (f_3.0, f_9.9). PASS.

## PICTURE GATE — take1 set

- U1: PASS. Frame 0 is the scripted BLAM tableau: ON AIR lit,
  monitor mid-video at full sound (cat singing), LAURA up with
  the sheet, PETER wheeling the stand in, mic red light glowing
  foreground. Correct UNC (grey-stubbled), correct cast.
- U2: badge beat lands (~3s, PETER lifts the badge; tray on
  desk); CHAMPION at the glass ~6s; tail is the scripted GAP-1
  held close frame — OUT tray + badge + red light (u2_last.png
  eye-confirmed). Picture PASS apart from F-b (above).
- U3: tray→pullback opens as scripted; UNC stands, page face
  up; mouth handoff IN lands — aired segment full-frame cat in
  the crystal layer-stack world (f_8.0 eye-confirmed). Handoff
  OUT does not land inside U3 (the E1 shape; exit carried into
  U4's opening). Room renders brighter/more papered than
  U1/U2's — noted. Picture PASS apart from wordmark.
- U4: FAIL — flaw F-c confirmed and worse than logged. The
  demonstration plays (costumed PETERs on the stack, cat on
  the desk), but across the second half UNC's face drifts to
  a DIFFERENT, younger man, and the GAP-2 held reaction — the
  scripted carrier is UNC's deadpan face, "the grin he does
  not have" — is that wrong man LAUGHING broadly (f_7.0,
  f_9.9 eye-confirmed). Identity break + deadpan break on a
  named structural beat. → REFIRE (cohesion/picture hard
  gate).
- U5: payoff staging lands (f_9.9: COLONEL with the torn
  invoice, stamp on desk, LAURA at the fader, UNC seated with
  badge restored, PETER staring at the flickering monitor).
  Dialogue exact. Caveat: UNC's face is the drifted younger
  man inherited from U4's anchor — carried, disclosed (F-c2).
  PASS with disclosure.
- U6: freeze tableau lands (ON AIR, PETER staring, cat on the
  monitor, torn invoice + sheet on the desk). The cat sings
  with a CAT's fanged mouth, not PETER's human mouth — the
  composite gag does not read (same class as E1 flaw F1).
  PETER's face is a third variant (curly-haired) — disclosed.
  PASS with disclosures.

## REFIRE PLAN (replacement brief allowance: 8 calls)

Chained in anchor order, each exactly ONE refire, vehicles
from VEHICLES.md with the noted reinforcements:
1. U2 take2 — dialogue tails. Anchor: work/qc/u1_last.png
   (unchanged) + PNL-PEAK-U2.png.
2. U3 take2 — wordmark. Anchor: NEW U2 last frame +
   PNL-PEAK-U3.png. Vehicle adds the exact-glyph clause.
3. U4 take2 — identity/deadpan. Anchor: NEW U3 last frame
   (inside the segment; pull-back-out per the take1 amended
   vehicle) + PNL-PEAK-U4.png. Vehicle adds the identity +
   deadpan clause ("grey-stubbled man in his fifties; he
   never smiles — the grin he does not have").
U5/U6 stay take1 regardless (dialogue exact / designed);
the U4→U5 seam is already a reframing cut in take1, so a
restored UNC in U4's tail is adjudicated at the joint gate.

## REFIRE OUTCOMES

- **U2 take2 (refire 1/8) — fired, ASR'd, NOT shipped.**
  Probe: 1248×704, 240f, 10.000s ✓. Picture: correct UNC,
  wordmark clean at f_3.0 (no F-b prompt-echo line), badge
  action + OUT tray present. ASR: UNC 10/10 exact, PETER
  10/10 exact ("UNC" rendered correctly this time), CHAMPION
  8/8 COMPLETE ("Number four, the singer's place is mine."),
  but COLONEL 0/10 — his entire intercom line dropped.
  Take1 vs take2: both 28/38, different losses. Take1 keeps
  all four speakers' wants spoken in U2 (F-3 architecture
  intact: Champion's want + Colonel's want both present);
  its losses are the Champion's spoken number (carried
  visually by the foam FOUR, on screen ~6s) and the Colonel's
  cancel condition (whose execution plays on screen in U5).
  Take2 restores the number but deletes a whole speaker and
  his want. **Verdict: take1 SHIPS; flaw F-a stands as
  disclosed and goes to F-9 with honest summaries.** The
  one-refire discipline is spent for U2 — no third roll.

- **U3 take2 (refire 2/8) — fired, PASSES, SHIPS.** Probe:
  1248×704, 240f, 10.000s ✓. Wordmark `~ WuBu ~` exact —
  single tildes, correct glyphs at f_3.0 and f_5.0 (eye).
  ASR 17/17 EXACT. Tray→pullback opens as scripted; correct
  grey UNC stands at the mic; PETER rolls his sleeves at the
  tail of the room portion; mouth handoff IN lands — the
  take ends inside the segment on the full-frame singing cat
  (u3t2_last.png), the E1 shape. Take1 is retired for U3
  (wordmark drift).

- **U4 take2 (refire 3/8) — fired, PASSES, SHIPS.** Probe:
  1248×704, 240f, 10.000s ✓. ASR 19/19 EXACT (desk rule +
  quotable line verbatim). Opens inside the segment on the
  singing cat (frame-matched to U3 take2's last frame);
  pull-back-out lands; the demonstration plays at full
  maximalist density (costumed PETERs harmonizing across the
  stack, cat duetting on the console, rundown sheets raining
  — f_5.0). GAP-2 carrier RESTORED: the held tail is the
  correct grey-stubbled UNC, face flat and deadpan — the
  grin he does not have (f_7.0, f_9.9). Wordmark exact.
  Take1 is retired for U4 (identity drift + laughing hold).
  Nit: the desk mic's flag reads "ON AIR" in the generator's
  render, not the scripted RED MEANS LIVE — broadcast
  furniture, legible, and the rule is carried by dialogue +
  the red light; disclosed, not composited over.

**FINAL TAKE SET: U1 take1 · U2 take1 · U3 take2 · U4 take2 ·
U5 take1 · U6 take1.** Refires used: 3 of 8. The U4→U5 seam:
U5 take1 was anchored on take1's (laughing, drifted) U4 tail
and opens on a reframed medium shot; the shipped U4 take2
tail restores the correct UNC, so the seam now also carries
the face correction — adjudicated at the joint gate below.

## ASSEMBLY + JOINT GATE

Segments: seg_u1..u6 = shipped takes scaled 1280×720, CRF 15,
each 240f / 10.026s format (AAC priming). seg_u6 carries the
Method C call-sheet composite (below). ONE concat pass →
work/joined.mp4: 1280×720, 24fps, **1440 frames counted**,
video 60.000s (audio stream 60.178s from AAC priming across
segments — trimmed in the master pass).

Joint gate (E1's jointgate, 320×180 gray seam MAE; bands
PASS ≤58 / CONDITIONAL ≤75 / FAIL >75) + EYE verdicts on
±6-frame strips (work/qc/joints/strip_U*.png):

| Joint | MAE | Head motion | Eye verdict |
|---|---|---|---|
| U1→U2 | 2.4 PASS | 24.4 | PASS — same tableau, PETER's stand gesture flows across the cut; positions/wardrobe/light identical |
| U2→U3 | 2.0 PASS | 37.3 | PASS — the GAP-1 tray hold itself bridges the seam; pull-back begins inside U3 |
| U3→U4 | 6.5 PASS | 49.3 | PASS — seam inside the aired segment; same full-frame cat, same crystal world (E1 shape) |
| U4→U5 | 40.9 PASS | 24.1 | **CONDITIONAL** — MAE passes, but the eye sees a reframing cut to a wider desk angle and UNC's face is the younger variant on the U5 side (U5 take1 was anchored on take1's drifted U4 tail). World, wardrobe, light and story state continuous; the face-variant seam is the episode's one non-continuous joint (E1's F4 class) |
| U5→U6 | 10.6 PASS | 25.4 | PASS — locked wide tableau continuous across the cut; the monitor's cat→colour-bars flicker is the scripted picture event inside the held frame |

## METHOD C GRAPHICS

- Singer credit / payoff paper (seg_u6, from 6.5s): printed
  call-sheet composite, bottom-right above the strip —
  "CALL SHEET — TOMORROW / SINGER: PETER / NUMBER FIVE:
  CHAMPION" (work/gfx/callsheet_u6.png; eye-verified legible
  in work/qc/seg_u6_sheet.png). This is the episode's singer
  credit — post, per the brief; the take's own desk sheet
  reads only "Call Sheet".
- Broadcast Strip + `~ WuBu ~` corner bug: master pass
  (below).

## MASTER PASS — FRAME-COUNT FIX

Master v1 (E1's filter verbatim) probed **1436 frames**:
timestamp gaps inherited from the segment encodes at the
f480/f960/f1200 seams became dropped frames in the overlay
framesync (3 double-steps located by pts scan; first frame
offset 0.041s). Fix: `setpts=N/(24*TB)` renumbering on both
the main video and the strip stream, strip cloned-padded and
trimmed to exactly 1440 frames (work/qc/master_filter_e2.txt).
Master v2 supersedes v1 (same filename; v1 never delivered).

## MASTER RECORD

**masters/ON_AIR_E2_MASTER.mp4** — md5
9f2790f480e4d6b32850ad0a028981d1, 30,719,181 bytes.
Video: H.264 1280×720, 24 fps, **1440 frames counted
end-to-end, first pts 0.0, zero irregular steps** (v2 video;
the final container carries v2's video stream bit-exact).
Audio: AAC 48 kHz stereo (2814 frames). Duration **60.000s**
exact. Faststart (moov at byte 36). Under 50 MB — no separate
delivery encode needed.

- **CRF 18 proof (size differential, per the standing
  ruling):** identical chain at CRF 23 = 17,500,480 B;
  master = 30,706,231 B at the same chain → **1.75×** ✓.
  (The SEI string reads crf=23.0 on this VM's ffmpeg
  regardless of rate control — not used as evidence.)
- **Broadcast Strip:** cobalt 0x0047AB waveform band,
  frame-bottom, driven by the episode's own audio advanced
  +0.4s. Present throughout; head amplitude honestly low for
  the first frames (the E1 strip-head class) and fully live
  by the U1 dialogue — eye-verified master_f0/master_f58.
- **Corner bug:** `~ WuBu ~`, cadmium 0xF2C230, top-right,
  full duration ✓ (eye, master_f0 + master_f58).
- **Loudness:** joined measured −16.86 LUFS / TP +0.49 /
  LRA 7.40 → loudnorm (dynamic; linear impossible against
  the −1.5 TP ceiling) → master **−16.51 LUFS / TP −1.49 /
  LRA 5.80** ✓.

## BLAM GATE (master; E1's measure.py, work/qc/blam_master.json)

As encoded, U1 take1's audio opened ~14 dB under the episode
median (generator mixed the already-airing song low), failing
A1/A3. Repair, mastering-only (no words or pictures changed;
a refire of U1 was rejected — it passed every unit gate and
carries the episode's best joint, U1→U2 MAE 2.4): a +13 dB
head lift decaying to 0 at 2.5s ahead of the loudnorm,
restoring the scripted "song already airing at frame 0"
level; video stream untouched. A stronger second variant
(+16.5 dB flat) was tested and rejected — the dynamic
loudnorm rode the whole episode quieter (median −24.3).

| Item | Bar | Result | Verdict |
|---|---|---|---|
| A1 t50 | ≤0.5s | 0.0s | PASS |
| A1 t90 | ≤1.5s | 1.8s | **FAIL — disclosed** (set by U1's own performance: the song bed sits low and LAURA's line builds; two envelope variants moved t50/A3 but not t90; further gain is undone by the loudnorm's dynamic ride) |
| A2 dead head | ≤0.2s | 0.0s | PASS |
| A3 head level | within 6 dB of median (−21.6) or accent ≤0.5s | head buckets −25.3/−26.3/−29.0/−26.8/−16.4/−18.8 — first bucket within 6 dB at ≤0.5s | PASS |
| A4 HF bursts | ≤2× control | 0 head vs 10 control | PASS |
| V1 opening motion | ≥0.6× baseline | ratio 0.99 | PASS |
| V2 no ramp-from-rest | — | first 0.25s bucket low (0.84); full motion (5.03 ≥ baseline 2.97) by 0.25–0.5s | PASS with note |
| E1 named impact ≤1.0s | — | frame 0 IS the BLAM tableau: monitor mid-song, stand being locked, sheet up, red light lit (master_f0) | PASS |
| E2 first cut/graphic ≤3.0s | — | Broadcast Strip + bug from frame 0; first hard cut 10.0s (unit format) | PASS |

## DISCLOSED FLAWS CARRIED TO DELIVERY

1. **F-a (U2 dialogue, take1 shipped):** the CHAMPION's
   spoken "Number Four." and the COLONEL's "A false name
   and I cancel the advertiser." are truncated in the audio.
   All four wants ARE spoken in U2 (F-3 intact); the number
   is carried visually by the foam FOUR; the cancel executes
   on screen in U5. The one permitted refire (take2) restored
   the number but dropped the COLONEL's whole line — take1
   retained as the more complete.
2. **F-c residue (U5/U6 face variants):** UNC's younger face
   variant persists through U5 take1 and U6 take1 (both
   inherited it from take1's drifted U4 tail anchor); the
   U4→U5 joint is CONDITIONAL on the eye for this reason.
   U6's PETER is a third (curly-haired) variant. Faces are
   disclosed; world/wardrobe/light/state are continuous.
3. **Cat's mouth (U6):** the cat sings the payoff line with
   a cat's fanged mouth, not PETER's human mouth (script's
   mouth-arithmetic lands in voice + credit; same class as
   E1's disclosed F1).
4. **BLAM A1 t90 = 1.8s** vs the 1.5s bar (above).
5. **Mic flag text (U4 take2):** the desk mic's flag reads
   "ON AIR" in the generator's render, not the scripted RED
   MEANS LIVE; the rule is carried by dialogue + the red
   light throughout.
6. **U2 prompt-echo (take1, F-b):** a fragment of prompt
   text ('prominently printed pr…') is printed under the
   wordmark at ~3.0s, small, during the badge action. The
   wordmark itself is exact everywhere it appears.

## F-9 — SECOND GATE E ON THE FINISHED MASTER

Fresh-context cold reader (subagent, no script/bible access),
input = transcript + picture summaries of the SHIPPED takes
(work/GATE_E2_INPUT.md), full record work/GATE_E2_VERDICT.md.

**VERDICT: PASS.** The reader reconstructed, with citations:
all five wants (Laura — name off the sheet; UNC — a quiet
shift; PETER — advertiser renewed via UNC live; COLONEL —
billable truth; CHAMPION — the singer's place); the complete
win/loss ledger (name crossed off and NOT undone; badge taken
in U2 and restored in U5; advertiser cancelled against
PETER's want; the showman's claim defeated); and the payoff's
causation in four cited steps — PETER's own desk rule (U4)
catches PETER because HE performed, live (fader locked open,
U5), so the printer names SINGER: PETER (U6). The reader's
"does not make sense" list is the designed texture layer
(prophetic sheet, the FOUR/FIVE numbering, the cat — shown,
never explained, per the msg-524 doctrine and the invasion
law) plus two edge nits it honestly flagged: "billable
truth" is never defined, and the "confession" link must be
guessed. Neither breaks the want/win-loss/ending chain. The
reader also confirmed the F-a truncation did not cost
comprehension: every want survived in the shipped U2 take1,
validating the take1-over-take2 call.

## DELIVERY

All gates complete: dialogue (above), wordmark (exact on
every shipped take), joints (4 PASS + 1 CONDITIONAL on the
eye, all MAE PASS), BLAM (7 PASS, A1-t90 FAIL disclosed,
V2 PASS-with-note), loudness, CRF-18 differential, frame
count/duration exact, F-9 PASS. E2_DELIVERED.flag raised.
Master: masters/ON_AIR_E2_MASTER.mp4 (md5
9f2790f480e4d6b32850ad0a028981d1).

---

## EAR-TEST REPAIR ATTEMPT (2026-11-17 ~23:00 EST) — BLOCKED AT GENERATION

The delivered master FAILED the post-delivery ear-test
(work/EAR_TEST_VERDICT.md): three findings, all in U2 —
(1) CHAMPION's identifying half-line "Number Four." ABSENT;
(2) COLONEL's condition "A false name and I cancel the
advertiser." ABSENT (the U5 payoff's spoken cause);
(3) PETER's "Red means live, UNC." unintelligible as
delivered ("UN4" in three ASR passes). A bounded repair was
authorized: refire U2 ONLY (allowance 2 generation calls),
take-level ASR gate before any assembly, fresh master
filename, re-ear-test after assembly.

- **Attempt (U2 take3):** fired 2026-11-18T04:00Z. Vehicle =
  the production U2 vehicle (VEHICLES.md, repair entry) with
  completeness reinforcements aimed at the three findings:
  unhurried dialogue, every speaker finishes their complete
  sentence; PETER says UNC's name slowly and clearly; the
  CHAMPION shouts his number first, loud and clear; the
  COLONEL's intercom line comes last and is spoken complete
  to the end; exact-glyph hoodie clause plus a no-other-print
  clause (F-b guard). Anchors (SR1): work/qc/u1_last.png +
  panels/PNL-PEAK-U2.png, as production.
- **Result: media.generate_video returned an internal error
  (downstream status 500).** No video landed — the only
  artifact is the 540-byte error receipt
  (takes/media-generation-u2-take3-repair-1794974441.json).
  Whether the request changed any external state is unknown.
  Per the runtime instruction attached to this failure, the
  request was NOT repeated; the contingency call was not
  spent on a retry.
- **No assembly performed.** masters/ON_AIR_E2_MASTER.mp4 is
  untouched — md5 re-verified after the attempt:
  9f2790f480e4d6b32850ad0a028981d1. No
  masters/ON_AIR_E2_MASTER_v2.mp4 exists. work/joined.mp4
  untouched (cff998f1d03d13a72f3234cd74d0f446).
- **Status: the ear-test FAIL stands, UNREPAIRED.** The
  resume path is fully specified and ready: re-fire U2 with
  the take3 vehicle; ASR-gate the take (all four U2 lines
  complete — "Number Four." AND "A false name and I cancel
  the advertiser." AND a clean "UNC"); build seg_u2 (CRF 15,
  1280×720, 240f) and ONE assembly pass with seg_u1 +
  seg_u3–seg_u6; master via work/qc/master_filter_e2.txt
  with loudnorm re-measured on the new joined and the
  +13 dB head lift (linear decay to 0 at 2.5s, ahead of the
  loudnorm — shape forensically confirmed this session by
  joined-vs-delivered envelope comparison: +16.38 dB total
  at t=0 over a +3.09 dB loudnorm base, decaying to base by
  2.5s); fresh filename masters/ON_AIR_E2_MASTER_v2.mp4;
  re-probe 1440f/60.000s; re-ear-test
  (work/EAR_TEST_VERDICT_v2.md).

---

## EAR-TEST REPAIR RESUME (2026-11-17 ~23:30 EST) — BLOCKED AT ASR GATE

Fresh session (job on-air-e2-u2-repair-resume), fresh
2-call allowance, resuming the repair blocked at
generation in the attempt above. Both calls landed this
time; both takes were ASR-gated BEFORE any assembly, per
the work order; both failed the gate; no assembly was
performed and no failing take was shipped.

- **U2 take3** (takes/U2_take3.mp4, 4,699,840 B) — the
  take3 vehicle fired verbatim. ASR (distil-large-v3;
  work/qc/u2t3/asr_distil.json): UNC and PETER complete,
  "Red means live, UNC." clean (Finding 3 element ✓);
  CHAMPION complete — "Number four, the singer's place
  is mine." (Finding 1 element ✓); COLONEL starts at
  8.12s and is CLIPPED by the 10s boundary mid-word —
  "...a false name and I can't..." (word ends exactly at
  10.00s, p=0.696); "cancel the advertiser" absent.
  **GATE FAIL** on Finding 2.
- **U2 take4** (takes/U2_take4.mp4, 4,415,234 B) — one
  contingency refire; vehicle amended by a single pacing
  sentence (brisk start, final speaker finishes well
  before the picture ends — full record in VEHICLES.md).
  ASR, two independent concurring passes (distil-large-v3
  + medium; work/qc/u2t4/): "Number four" ✓; "UNC" heard
  by both ✓; CHAMPION's "place" garbled/absent in both;
  COLONEL's line now ENDS complete ("...and I cancel the
  advertiser.") but its head is garbled in both passes —
  "Bill of All's name" / "Bill of Ulth's name" for
  "I want billable truth. A false name" — the word
  "false" is absent in both passes. **GATE FAIL** on
  Finding 2 (the condition line is not intelligibly
  complete), with a secondary CHAMPION nit.
- **No assembly performed.** masters/ON_AIR_E2_MASTER.mp4
  untouched (md5 re-verified after both attempts:
  9f2790f480e4d6b32850ad0a028981d1); work/joined.mp4
  untouched (cff998f1d03d13a72f3234cd74d0f446); no
  masters/ON_AIR_E2_MASTER_v2.mp4 exists; no EAR_TEST_
  VERDICT_v2 (no new master to test). Joint eye-
  verification (SR2) not reached — it is gated behind
  the ASR pass.
- **Status: BLOCKED AT ASR GATE. The ear-test FAIL on
  the delivered master stands, UNREPAIRED.** Failure
  pattern across take1–take4 (see VEHICLES.md): the
  COLONEL's two-sentence condition line is the
  persistent casualty of a 4-speaker / ~41-word / 10s
  unit — dropped whole, tail-dropped, tail-clipped, or
  head-garbled in every attempt. Any further repair
  needs a fresh allowance and should treat the line's
  front half ("I want billable truth. A false name...")
  as the at-risk element, not only its tail.

---

## EAR-TEST REPAIR ROUND 3 (2026-11-18 ~00:05 EST) — BLOCKED AT ASR GATE (R3)

Fresh session (job on-air-e2-u2-repair-r3), fresh
2-call allowance, REDESIGNED vehicle per the round-3
brief: front three speakers brisk and finished by
~4.5s, a full beat of silence, the COLONEL last and
alone — slow, separately enunciated, finished by
~8.5s, silent hold to the end; his line written with
emphasis spacing ("A FALSE NAME — and I cancel the
advertiser."); the CHAMPION directed to land "place"
in full. Same anchors (work/qc/u1_last.png +
panels/PNL-PEAK-U2.png), dialogue words exactly as
scripted. Both calls landed; both takes were
ASR-gated BEFORE any assembly; both failed; no
assembly was performed and no failing take shipped.

- **U2 take5** (takes/U2_take5.mp4, 4,312,308 B) —
  ASR, two independent concurring passes
  (distil-large-v3 + medium; work/qc/u2t5/): UNC
  10/10; PETER 10/10 with a clean "UNC"; CHAMPION
  COMPLETE — "Number four, the singer's place is
  mine." with "place" at p=0.999 — Findings 1 and 3
  fully satisfied for the first time in any take.
  But the brisk direction did not compress the front
  speakers (CHAMPION ends 7.72s), and the COLONEL
  (7.94–9.88s) compressed his head into ~0.6s: both
  passes hear "Bill's name and I cancel the
  advertiser." — "I want billable truth. A false
  name" collapsed, the word "false" absent in both
  passes. **GATE FAIL** — Finding 2, head-garbled
  class (as take4).
- **U2 take6** (takes/U2_take6.mp4, 5,305,765 B) —
  one further delivery adjustment: the COLONEL's
  delivery rebuilt as two slow beats through a loud,
  close, distortion-free phone speaker, starting
  ~4.5s, with a full second of silence between "I
  want billable truth." and a stress-stamped "A
  FALSE NAME — and I cancel the advertiser." ASR,
  two concurring passes + per-second RMS audit
  (work/qc/u2t6/): UNC ✓, PETER ✓ clean "UNC",
  CHAMPION complete with "place" — and the
  COLONEL's line ENTIRELY ABSENT: no speech after
  the CHAMPION's 8.92s in either pass; 9–10s RMS
  641 (room tone) vs 2,000–3,400 in speech windows.
  **GATE FAIL** — Finding 2, whole-line-dropped
  class (as take2).
- **No assembly performed.** masters/ON_AIR_E2_
  MASTER.mp4 untouched — md5 re-verified after both
  attempts: 9f2790f480e4d6b32850ad0a028981d1.
  work/joined.mp4 untouched (cff998f1d03d13a72f323
  4cd74d0f446). No masters/ON_AIR_E2_MASTER_v2.mp4
  exists; no EAR_TEST_VERDICT_v2 (no new master to
  test). Joint eye-verification (SR2) not reached —
  gated behind the ASR pass.
- **Status: BLOCKED AT ASR GATE (R3). The ear-test
  FAIL on the delivered master stands, UNREPAIRED.**
  Six-attempt pattern (VEHICLES.md): Findings 1+3
  are solved — the redesigned vehicle lands "Number
  Four." + "place" + clean "UNC" reliably (take5
  AND take6). The COLONEL's two-sentence intercom
  line has now failed in every mode: tail-dropped,
  whole-dropped (×2), tail-clipped, head-garbled
  (×2). The unit's structure — four speakers, the
  densest line last, delivered by an off-screen
  voice — is the binding constraint, not the
  wording of any single vehicle tried so far. Any
  further repair needs a fresh allowance and a
  structurally different idea (e.g. a vehicle that
  gives the COLONEL the FIRST slot, or splits U2's
  dialogue load), not another pacing adjective.

## EAR-TEST REPAIR ROUND 4 (2026-11-18) — BLOCKED AT ASR GATE (R4)

Fresh session (job on-air-e2-u2-repair-r4), fresh
2-call allowance, SCRIPT AMENDMENT applied first:
under the user's 2026-11-18 directive ("never ask me
you decide"), the showrunner amended U2's line order
— COLONEL first, UNC and PETER in their current
relative order, CHAMPION's line closing the unit;
every line verbatim, order only (SCRIPT.md header +
U2 amendment note; DECISION_LOG.md 2026-11-18 entry;
VEHICLES.md round-4 section). Both calls landed; both
takes were ASR-gated BEFORE any assembly; both
failed; no assembly was performed and no failing
take shipped.

- **U2 take7** (takes/U2_take7.mp4, 4,419,191 B) —
  ASR, two independent concurring passes
  (distil-large-v3 + medium; work/qc/u2t7/): COLONEL
  COMPLETE for the first time in any take — "I want
  billable truth, a false name and I cancel the
  advertiser." (0.00–4.06s), "false" at p=0.999 /
  0.998. Finding 2 SOLVED by the amendment. UNC ✓,
  PETER ✓ with clean "UNC" — Finding 3 stands
  solved. But the CHAMPION's line is ABSENT ENTIRE:
  no "Number Four.", no "The singer's place is
  mine." in either pass; heard speech accounts for
  0–9.94s with no window for it. **GATE FAIL** —
  Finding 1, whole-line-dropped class, now in the
  last slot (the CHAMPION's).
- **U2 take8** (takes/U2_take8.mp4, 4,054,996 B) —
  one delivery adjustment: room directed "VERY quick
  and tight... done by five and a half seconds", a
  silence beat, CHAMPION at ~6s. ASR, two concurring
  passes (work/qc/u2t8/): COLONEL COMPLETE again
  (0.00–4.00s, "false" p=0.998/0.999); UNC ✓; PETER
  ✓ clean "UNC" (to 9.48–9.50s); CHAMPION ABSENT
  ENTIRE again. The compression direction did not
  take — the room ran 4.34–9.50s, near-identical to
  take7. **GATE FAIL** — Finding 1, whole-line-
  dropped class.
- **No assembly performed.** masters/ON_AIR_E2_
  MASTER.mp4 untouched — md5 re-verified at round
  end: 9f2790f480e4d6b32850ad0a028981d1.
  work/joined.mp4 untouched (cff998f1d03d13a72f323
  4cd74d0f446). No masters/ON_AIR_E2_MASTER_v2.mp4
  exists; no EAR_TEST_VERDICT_v2 (no new master to
  test). Joint eye-verification (SR2) not reached —
  gated behind the ASR pass.
- **Status: BLOCKED AT ASR GATE (R4). The ear-test
  FAIL on the delivered master stands, UNREPAIRED.**
  Eight-attempt pattern (VEHICLES.md): the reorder
  amendment solved its target — Findings 2+3 now
  pass together (COLONEL complete with "false"
  intelligible in both round-4 takes; clean "UNC").
  The failure moved with the slot: whoever speaks
  LAST in this four-speaker unit is dropped whole —
  the Colonel in rounds 1–3, the CHAMPION in round
  4 (×2). Compression direction has now failed to
  compress in two separate rounds; the room's
  argument expands to fill the unit. The binding
  constraint is U2's four-speaker dialogue load in
  10 seconds. Any further repair needs a fresh
  allowance AND a structurally different idea
  (split the dialogue load across the unit boundary,
  or carry one line by picture/post), not another
  order or pacing change.

## EAR-TEST REPAIR ROUND 5 (2026-11-18) — BLOCKED AT ASR GATE (R5)

Fresh session (job on-air-e2-u2-repair-r5), fresh
3-call allowance, METHOD CHANGE: SPLIT-TAKE COMPOSITE
(showrunner decision under the user's 2026-11-18
"never ask me you decide" directive; full design in
VEHICLES.md round-5 section and DECISION_LOG.md).
TAKE A = the room (COLONEL intercom first, UNC, PETER;
≤3 speakers); TAKE B = the glass (CHAMPION alone);
one motivated internal picture cut at the glass beat;
each span keeps its own take's audio; total 240f.
SCRIPT unchanged (round-4 amended order stands).

- **U2 take9A** (takes/U2_take9A.mp4, 3,979,102 B) —
  ASR, two concurring passes (distil-large-v3 +
  medium; work/qc/u2t9a/) + per-second RMS audit:
  COLONEL COMPLETE (0.00–4.40s, "false" p=0.999 both
  passes); UNC present (medium verbatim incl.
  "mine."); clean "UNC" (p=0.83). **GATE FAIL** —
  PETER's first sentence "Your mouth shut pays
  nobody." is ABSENT in both passes (only "Red means
  live, UNC." heard, 8.34–9.76s), and the RMS audit
  leaves no unaccounted speech window (true silence
  7.75–8.25s). Secondary: room dialogue ran to 9.76s,
  not the designed ~6s — no silent drift tail.
- **U2 take9B** (takes/U2_take9B.mp4, 3,314,320 B) —
  ASR, two concurring passes (work/qc/u2t9b/):
  "Number four. The singer's place is mine."
  COMPLETE in both ("place" p=0.998/0.999). **GATE
  PASS on its elements** — but the delivery spans
  1.36–7.86s (a ~2.3s internal pause inside the
  shout), so its minimum composite window is ~6.5s,
  not the designed ~4s.
- **Composite arithmetic (blocking):** A-span floor
  ~8.5s for three complete room lines + B-span
  ≥6.5s = ~15s > the unit's 10.00s/240f. No single
  refire repairs both defects (refire A → B's span
  still blocks; refire B → A still gate-failed, and
  a failing half is never assembled). **Call 3
  deliberately UNSPENT** — no outcome of it could
  produce an assemblable pair. NO assembly
  performed; joint eye-verification (SR2) not
  reached — gated behind assemblable halves.
- **No assembly performed.** masters/ON_AIR_E2_
  MASTER.mp4 untouched — md5 re-verified at round
  end: 9f2790f480e4d6b32850ad0a028981d1.
  work/joined.mp4 untouched (cff998f1d03d13a72f323
  4cd74d0f446). No masters/ON_AIR_E2_MASTER_v2.mp4
  exists; no EAR_TEST_VERDICT_v2 (no new master).
- **Status: BLOCKED AT ASR GATE (R5). The ear-test
  FAIL on the delivered master stands, UNREPAIRED.**
  Ten-attempt pattern (VEHICLES.md): every element
  is individually proven landable; the unit's total
  dialogue load exceeds one 10s generation AND the
  landed split spans. The untried lever is the load
  split itself (2+2 speakers across the halves) or
  a script-level trim of U2 — a future showrunner
  call, not another vehicle variation.

## EAR-TEST REPAIR ROUND 6 (2026-11-18) — BLOCKED AT SPAN GATE (R6) — FINAL ROUND

Fresh session (job on-air-e2-u2-repair-r6), fresh
4-call allowance, SCRIPT AMENDMENT + METHOD CHANGE
(showrunner decisions under the user's 2026-11-18
"never ask me you decide" directive; SCRIPT.md header
+ U2 round-6 notes; DECISION_LOG.md round-6 entry;
VEHICLES.md round-6 section): PETER's first sentence
"Your mouth shut pays nobody." CUT from U2 (33 words;
episode 105); 2+2 SPLIT-TAKE COMPOSITE — TAKE A =
COLONEL (intercom, first) + UNC; TAKE B = PETER (at
the glass) + CHAMPION (one continuous breath). Gates:
completeness in two concurring ASR passes per half
PLUS the span gate (usable spans from word
timestamps must sum to <= 240f). Both calls landed;
both halves were gated BEFORE any assembly.

- **U2 take10A** (takes/U2_take10A.mp4, 3,662,983 B)
  — ASR, two concurring passes (distil-large-v3 +
  medium; work/qc/u2t10a/): **COMPLETENESS PASS** —
  COLONEL complete ("false" p=0.993/0.999), UNC
  complete incl. "mine." But the Colonel ran
  0.86–5.68/5.96s and UNC to 9.58/9.68s: A-span
  ≈ 9.6–9.8s.
- **U2 take10B** (takes/U2_take10B.mp4, 3,783,082 B)
  — ASR, two concurring passes (work/qc/u2t10b/):
  **COMPLETENESS PASS** — PETER's trimmed line with
  a clean "UNC" (both passes; the Finding 3 garble
  is gone); CHAMPION complete ("place" p=0.999
  both). But Peter ends 2.94/3.06s, the Champion
  runs 4.10–8.86/4.60–9.10s with a residual internal
  pause: B-span ≈ 8.9–9.1s.
- **SPAN GATE: FAIL.** A-span ~9.7s + B-span ~9.0s
  ≈ 18.7s > the unit's 10.00s/240f. No cut point
  exists. Calls 3–4 (per-half refires) deliberately
  UNSPENT — no single refire brings the sum inside
  240f (best-case single-refire sums ≈ 15.5s and
  ≈ 13.2s), and the joint floor (~10.0s) assumes
  both halves simultaneously hit all-rounds-best
  rates with zero lead-in or tail, contradicted by
  this round's landed rates. NO assembly performed;
  joint eye-verification (SR2) not reached — gated
  behind assemblable halves.
- **No assembly performed.** masters/ON_AIR_E2_
  MASTER.mp4 untouched — md5 re-verified at round
  end: 9f2790f480e4d6b32850ad0a028981d1.
  work/joined.mp4 untouched (cff998f1d03d13a72f323
  4cd74d0f446). No masters/ON_AIR_E2_MASTER_v2.mp4
  exists; no EAR_TEST_VERDICT_v2 (no new master to
  test).
- **Status: BLOCKED AT SPAN GATE (R6). FINAL ROUND —
  THE U2 REPAIR ENDS. The ear-test FAIL on the
  delivered master stands, UNREPAIRED.** Eleven-
  attempt pattern (VEHICLES.md): round 6 solved
  completeness — the trim + 2+2 split landed every
  scripted element in two concurring passes per
  half, a first across all eleven attempts — and
  isolated the true binding constraint: delivered
  speech RATE. At 0.3–0.45s/word with incompressible
  pauses, the unit's words occupy ~18.7s of span
  across two generations against a 10s unit. The
  standing lesson is recorded in DECISION_LOG.md:
  a 10s unit's spoken load is capped at ~30 words /
  2 speakers per generation at the observed
  non-compressible rate — and span, not just
  completeness, is a gate quantity from the start.
