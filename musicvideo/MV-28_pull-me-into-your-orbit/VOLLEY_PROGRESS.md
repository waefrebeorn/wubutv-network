# MV-28 VOLLEY PROGRESS — "Pull Me Into Your Orbit"

Budget: 40 video calls. Images: 5 reference stills (not video budget).

## Pilot volley (2026-11-20) — spend 3/40
- mv28_s03_t1 (S03 verse singing) — G7 0.92 PASS, eye PASS
- mv28_s06_t1 (S06 hook, L07–L08) — G7 1.00 PASS, eye PASS
- mv28_s19_t1 (S19 FC centre dance) — G7 0.81 PASS, eye PASS; hook
  phrase L34 garbled in take ("Pull me night, come rushing in") →
  S19_t2 reroll with slower pacing fired in volley 3; planner picks
  the best anchor per phrase.

## Volley 2 (2026-11-20) — spend 9/40
- mv28_s01_t1 / s01_t2 (S01 Orrery Awakens, wordless) — QC PASS
- mv28_s02_t1 / s02_t2 (S02 Long Way Round, wordless) — QC PASS
- mv28_s04_t1 (S04 L03–L04 singing) — G7 1.00, eye PASS
- mv28_s05_t1 (S05 L05–L06 singing) — G7 1.00, eye PASS (neckline nit)

## Volley 3 (2026-11-20) — spend 15/40
- mv28_s06_t2 (S06 L09–L10) — G7 0.91, eye PASS
- mv28_s07_t1 (S07 L11–L12) — G7 1.00, eye PASS (HIM drift nit)
- mv28_s07_t2 (S07 L13 wide) — G7 1.00, eye PASS
- mv28_s08_t1 / s08_t2 (S08 Star Wheel, wordless) — QC PASS
- mv28_s19_t2 (S19 reroll) — G7 1.00, eye PASS; anchors all S19 lines

## RESUME 2026-11-21 — generation OPEN (probe B-1345, 17:21:52Z)

## Volley 4R (2026-11-21) — spend 21/40
- mv28_s09_t1 (S09 L14–L15) — sang its vehicle exactly, but the
  vehicle paraphrased L14 (sheet: "Your jacket's hanging on my
  chair"); G7 0.80 vs sheet → COVER POOL, refired as s09_t2
- mv28_s09_t2 (S09 L14–L15, sheet-corrected refire) — G7 1.00, eye
  PASS, KEEP primary. Spend 33/40.
- mv28_s10_t1 (S10 L16–L17) — G7 1.00, eye PASS
- mv28_s11_t1 (S11 L18–L19) — G7 1.00 vs sheet, eye PASS ("make you
  burn" is the sheet wording of L19)
- mv28_s12_t1 (S12 L20–L21) — G7 1.00, eye PASS (spark-flare nit)
- mv28_s12_t2 (S12 L22–L23) — G7 1.00, eye PASS
- mv28_s13_t1 (S13 L25+L26/L27) — G7 1.00, eye PASS

## Volley 5 (2026-11-21) — spend 27/40
- mv28_s13_t2 (S13 L34 wide) — G7 1.00, eye PASS
- mv28_s14_t1 (S14 Gearheart, wordless) — QC PASS
- mv28_s15_t1 (S15 Distant Dance, wordless) — QC PASS
- mv28_s16_t1 (S16 Moon Crossing, wordless) — QC PASS
- mv28_s17_t1 (S17 L28–L30) — ASR/G7 in TAKE_HISTORY
- mv28_s18_t1 (S18 L31–L32) — ASR/G7 in TAKE_HISTORY

## Volley 6 (2026-11-21) — spend 31/40
- mv28_s20_t1 (S20 L37–L38) — eye PASS; ASR/G7 in TAKE_HISTORY
- mv28_s21_t1 (S21 L39) — eye PASS; ASR/G7 in TAKE_HISTORY
- mv28_s22_t1 (S22 L40) — **LOST IN TOOL HANDOFF**: wrapper-level
  error; render reported ok server-side but no file saved locally;
  failed request not repeatable. NOT re-fired (MV-27 S06 precedent).
  S22 ships as wordless dawn cover from s21_t1 + s23_t1 non-claimed
  spans; L40 carried by burned karaoke captions. Disclosed.
- mv28_s23_t1 (S23 tail, wordless) — QC PASS

All scenes S01–S23 now have KEEP coverage. Assembly next.

## Assembly + delivery (2026-11-21) — spend final 33/40 + 1 refusal
- Refires: s17_t2 (G7 1.00, primary), s09_t2 (sheet-corrected,
  G7 1.00, primary); s03_t2 REFUSED by the generator → L02 ships as
  wordless cover (see GATE_LOG disclosures).
- Plan: work/swing/plan_build.py → 72 segments, 5760f exact, claim
  audit clean, zero reused picture. CUTLIST.md written.
- Build: segments asserted frame+duration exact; joined.mp4 5760f /
  239.998s; freezedetect zero. (First build reaped at seg045,
  resumed from md5-verified segments; first master encode killed
  by a VM reboot at ~37MB, re-encoded in full.)
- Master: masters/mv28_pull-me-into-your-orbit_16x9.mp4,
  124,317,595 B, md5 3fa1291a32a9d800f9224b71d7086781, 5760f,
  240.000s, CRF-18 proof 1.94× (CRF23 twin 64,170,322 B), karaoke
  subs burned in (46 lines / 278 word events) + mov_text, bug
  eye-verified head/mid/tail.
- Sibling: masters/mv28_pull-me-into-your-orbit_16x9_50mb.mp4,
  46,073,919 B, md5 7d4cb589bbb5f2e9b06c22712d38b372.
- COMPLETION.json + MV28_DELIVERED.flag written. Scratch cleaned.

## Volley 4 (2026-11-20) — ⛔ 429 HARD STOP, spend stays 15/40
All six calls (s09, s10, s11, s12_t1, s12_t2, s13_t1) returned
video_daily_budget_exhausted (account 24h video limit). No retries
per the hard-stop rule. Production halts here; see GATE_LOG.md for
the full state and the exact remaining-work list (16 takes to fire
when the account window reopens; all vehicles already written).
