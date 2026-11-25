# MV-28 GATE LOG — "Pull Me Into Your Orbit"

## ✅ DELIVERED — 2026-11-21 (continuation coordinator, resumed on probe OPEN)

Generation reopened 2026-11-21T17:21:52Z (probe B-1345). The 16 owed
takes were fired in volleys 4R/5/6, plus 2 sheet-correction refires;
every scene S01–S23 reached KEEP coverage; assembly + master built
the same day.

### Deliverables
- House master: masters/mv28_pull-me-into-your-orbit_16x9.mp4 —
  124,317,595 B, md5 3fa1291a32a9d800f9224b71d7086781, **5760 frames
  (ffprobe -count_frames), 240.000s**, 1280×720 24fps h264 CRF 18,
  AAC LC 48kHz 192k from track.mp3 (re-encoded, never stream-copied),
  mov_text track + karaoke subtitles BURNED IN, faststart.
- Chat copy / release sibling (master >100MB):
  masters/mv28_pull-me-into-your-orbit_16x9_50mb.mp4 — 46,073,919 B,
  md5 7d4cb589bbb5f2e9b06c22712d38b372 (video 1350k capped, audio +
  mov_text copied from the house master).

### Gates
- FRAMES/DURATION: joined.mp4 asserted 5760f AND 239.998s before the
  master encode; every one of the 72 segments asserted frame-exact
  AND duration-exact at build (work/swing/build.log). Master probed
  5760f / 240.000s after encode.
- CRF 18 PROOF (size differential, never the SEI string): CRF-23
  encode of the same joined file = 64,170,322 B → ratio **1.94×**.
- FREEZEDETECT on joined.mp4: **zero** freeze starts.
- WORDMARK: "~ WuBu ~" gold bug eye-verified on master frames at
  t=2 / 100 / 140 / 200 / 230 / 239 — exact text, bottom-right.
- SUBTITLES: karaoke ASS (46 lines, 278 word events; sheet words on
  ASR slots where counts agree, syllable-split otherwise) burned in —
  eye-verified at t=100 (L14), t=140 (L26), t=200 (L34), t=230 (L40);
  mov_text track also present.
- WORD-SYNC: 38 of 40 sheet lines carry a matched singing take
  (phrase/chunk warps from SONG_WORDS.json slots). Zero reused
  picture (planner claim-ledger audit clean). L24/L36 are doubled
  vocals sharing L23/L35 spans — captioned once, no separate picture
  exists in the song.
- TAKE QC: every take ASR'd (house config) + G7 + eye-checked
  (adults only, motion at frame 0, zero on-screen text). Final
  primaries: 20 at G7 1.00, s03_t1 L01 exact (its L02 defective, see
  disclosures), s06_t2 0.91 banked.

### Disclosures (plain)
1. **S22 / L40 ships as a WORDLESS COVER.** The s22_t1 generation
   call failed at the tool-wrapper level (render reported ok
   server-side, no file saved locally, failed request not
   repeatable) — the MV-27 S06 lost-take class; NOT re-fired. The
   final "Pull me into your orbit" (225.08–232.30) plays over dawn
   cover from non-claimed spans of s23_t1 + s21_t1 at k=1.478, the
   line carried by the burned karaoke captions.
2. **S03 / L02 ships as a WORDLESS COVER.** The banked s03_t1 sang
   its vehicle's paraphrase ("Then you took the long way around the
   room") — a vehicle defect (the sheet line is "I take the long way
   past your door"). The sheet-corrected refire s03_t2 was REFUSED
   by the generator and was not re-attempted in altered form (house
   refusal rule). L02's span (34.06–37.48) is covered from s03_t1's
   non-sung spans + a 1.1s dome cutaway (s01_t2); captions carry it.
3. **S09 vehicle defect, fixed by refire.** The s09 vehicle also
   paraphrased its line ("Your jacket on the chair where you left
   it" vs sheet "Your jacket's hanging on my chair"). s09_t1 sang
   the paraphrase exactly (G7 0.80 vs sheet) → demoted to cover
   pool; s09_t2 fired with the sheet line, G7 1.00, primary.
4. **S17 refire.** s17_t1 sang only 4 of L30's 10 words (G7 0.83) →
   cover pool; s17_t2 is word-complete (G7 1.00), primary.
5. **Grey-zone warps** (outside the 0.80–1.25 band, all phrase-level,
   disclosed per house practice): S06 L07 k=0.76 · S07 L11 k=0.62 ·
   S07 L13 k=0.75 · S11 L19 k=0.80 (0.7958) · S13 L25 k=0.71 · S13
   L27 k=0.67 · S17 L29 k=1.36 · S18 L32 k=1.36 · S20 L37 k=0.71 ·
   S21 L39 k=0.57 (worst; the outro's slow held "Until the morning"
   — take phrase 3.52s over a 2.0s song span).
6. **Cover stretches:** S20 ad-lib head cover k=1.70 (the couple
   swaying, slow) · S21 fill k=1.45 · S22 manual cover k=1.478 ·
   S23 tail k=1.25 · wordless S14/S15/S16 k=1.03–1.04.
7. **Texture nits:** s12_t1's orrery throws a spark flare mid-take
   (reads as the perihelion ignition; kept) · dawn takes' HER hair
   reads longer/curlier than the night takes (s21_t1) · banked nits
   stand (s05_t1 neckline, s07_t1 HIM hair).
8. **Process incidents:** the first segment build was reaped by the
   runtime at seg045/72 and resumed cleanly from md5-verified
   segments; the first master encode was killed by a VM reboot at
   ~37MB and re-encoded in full under a fresh systemd unit. No
   picture was lost in either incident; joined.mp4 was asserted
   before every encode attempt.
9. Spend: **33/40 video calls + 1 generator refusal** (s03_t2).
   5 reference images (banked 2026-11-20). No 429s on resume day.

## ⛔ PRODUCTION HALTED — 429 HARD STOP (2026-11-20, volley 4)

Volley 4 (s09, s10, s11, s12_t1, s12_t2, s13_t1) returned
`video_daily_budget_exhausted` on all six calls: "This account has
reached its video limit for the last 24 hours." Per the brief, a
429 / budget-exhausted response is a HARD STOP — no retries were
made and none may be made until the account window reopens (the
parent's standing generation free-probe detects that). Spend at the
stop: **15 successful video calls of the 40-call budget** (+5
reference images). No master exists; MV28_DELIVERED.flag and
COMPLETION.json are deliberately NOT written — nothing is delivered.

### State at the stop (everything below is on disk and verified)
- Plan locked: MV_PREPRO_MV-28.md (23 scenes, frame-exact 5760f
  partition in work/scenes.json, beat grid work/swing/beat_grid.json
  141.5 BPM phase 0.080).
- MV-28's 23 events appended to USED_EVENTS.md (parent commits).
- Reference stack complete + eye-verified: REFERENCE_STACK.md
  (REF_HER / REF_HIM / REF_WORLD / REF_KEEPER / REF_DAWN, all
  2048×1152, zero legible text).
- Vehicles written for ALL 23 scenes (mv28_s01..s23 *_vehicle.txt).
- Takes banked: 15 (S01–S08 complete = song 0.00–97.00, plus S19 =
  194.46–204.71). Every banked take passed eye QC (adults only,
  zero legible text, mouth discipline) and G7/ASR (see
  TAKE_HISTORY.md — worst score 0.81 on a take demoted to cover
  pool; every primary take ≥0.91, eleven at 1.00).
- REMAINING WORK, in order: fire the 16 unfired takes listed in
  TAKE_HISTORY.md (vehicles ready) → take ASR + G7 + eye QC →
  adapt MV-27's plan_build/build_master/build_captions/
  encode_master pipeline (method fully specified in
  MV_PREPRO_MV-28.md: phrase-level smooth warp, setpts-then-fps,
  claim audit, 5760f assert, burned karaoke ASS with the alias map
  oven→orbit / fall→burn / Hold·We'll be→Pull me, CRF-18 size-
  differential proof, freezedetect, bug grabs) → CUTLIST.md,
  COMPLETION.json, MV28_DELIVERED.flag.

## Gates run so far (measured)

- G-plan: scene windows partition [0, 5760] frames exactly
  (asserted in work/scenes.json build). PASS.
- Hook timing adjudication: all five ASR-unmatched hook lines
  recovered from the ASR stream itself (work/swing/gap_analysis.txt):
  L11 68.84–71.10, L25 135.04–137.86, L32 192.12–194.46 (heavily
  garbled "No need to be above it"), L34 198.92–201.26, L37
  207.74–210.42. Ad-lib spans measured (65.70–68.84, 131.96–135.04,
  204.72–207.74) + outro backing 222.58–225.08 + patter 29.66.
- G7 per take: see TAKE_HISTORY.md. All primaries PASS (≥0.5 gate;
  actual ≥0.91). Wordless takes: screened sung sets empty. PASS.
- Eye QC per take: identity (HER face/hair/lipstick/gown hold in
  every take), HIM mouth closed in all two-shots, zero legible text
  at sheet + spot full-res, all figures grown adults. PASS with
  nits below.
- Refusals: 0. Lost takes: 0. 429s before the stop: 0.

## Disclosed flaws / nits (banked takes)
1. S19_t1 (pilot) garbles the L34 hook ("Pull me into your orbit"
   sung as "Pull me night, come rushing in"). Rerolled as S19_t2
   with paced line windows — t2 anchors all four S19 lines cleanly
   (G7 1.00). t1 is cover pool only; its garbled span must never be
   warped under a lexical line (BAD-WORD rule).
2. S05_t1: HER gown neckline drifts off-shoulder vs the REF_HER
   scoop neckline; face/hair/lipstick/pendant hold. Texture nit.
3. S07_t1: HIM's hair reads darker/less grey than REF_HIM in the
   two-shot; HER (the identity anchor) holds. Texture nit.
4. S03_t1: the background orrery reads as a tabletop instrument
   rather than the room-scale machine (the room's smaller orrery
   lamp); staging variance, disclosed.
5. S02_t2 / S01_t1: ASR junk fragments ("I", "so") on wordless
   takes — screened out by the house sung-screen (segment logprob /
   word prob), no words sung. Not a defect.
6. The orrery's scale varies between takes (tabletop instrument ↔
   room-scale machine) — a known generator variance across the
   batch's builds; the world, palette and machine design are
   consistent. Disclosed.
