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
