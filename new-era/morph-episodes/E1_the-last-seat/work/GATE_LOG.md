# GATE LOG — THE LAST SEAT E1 "Night One: The Woman with the White Stub"

Production coordinator run, 2026-11-16. SCRIPT.md was law throughout.
Fires: **6 videos, 6 successes, 0 refires, no 429 / budget error.**
Every take used exactly once (t1 per unit). This run's video budget is
spent; the two candidate recovery refires are named at the bottom for the
parent's dispatch decision.

## MASTER

- `masters/E1_the-last-seat_MASTER.mp4` — **md5 0ce3002b252f3b499b9d23009df5e38b**,
  16,131,737 B, **1440 frames**, 60.000 s, 1280×720, 24 fps, h264,
  AAC 48 kHz stereo, faststart (moov at byte 36). ≤50 MB — no chat copy needed.
- Assembly law held: segments probed 240f each; joined.mp4 probed
  **1440f = segment sum BEFORE** the master encode; ONE uninterrupted
  master encode from the joined intermediate; master re-probed end to end.
- **CRF-18 proof = size differential** (the SEI string reads crf=23.0 on
  this ffmpeg regardless — not used): CRF-23 video-only control of the same
  chain = 8,315,036 B vs the master's ≈15.56 MB video stream — **≈1.87×**.
- Loudness: joined measured −26.01 LUFS / TP −3.81 dBTP → **pure gain
  +2.81 dB** (true-peak-capped, dynamics untouched) → master
  **−23.20 LUFS / TP −1.02 dBTP**. A quiet master — disclosed in FLAWS.

## TAKES (all 240f / 10.000 s native)

| Take | md5 | Native |
|---|---|---|
| e1s5_u01_t1 | 5c7c30cd0fda9579a8b8654cba4523f8 | 1248×704 |
| e1s5_u02_t1 | 7afc770892e6c7c2898bdee1896986a2 | 1248×704 |
| e1s5_u03_t1 | 3e78d564d1046c68196010fcb5212b1d | 1280×720 |
| e1s5_u04_t1 | c2572fd8c021038c4b5ed9df626c74d9 | 1248×704 |
| e1s5_u05_t1 | 0b1257fbcb20340b4723ed244df8b17a | 1248×704 |
| e1s5_u06_t1 | d217866484c2e0d230dec65644cf963e | 1248×704 |

Anchors per REFERENCE_STACK.md: image 1 = the unit's gated PEAK panel,
image 2 = CHAR per the rotation table. Panels: the six-piece kit carried
md5-identical from E2_SHOW-5; seven new panels generated + eye-gated
(CHAR-OCCUPANT + PEAK-U01…U06; PEAK-U01 v1 rejected on premise, v2 shipped).

## DIALOGUE GATE — PASS, clean sweep

ASR (faster-whisper large-v3-turbo, NO VAD) on every take and on the
master: **all 14 locked lines verbatim, correct speakers, correct order,
no unscripted speech anywhere.** Master timings: U1 0.00–7.76 · U2
13.68–17.02 · U3 20.68–28.20 · U4 30.00–39.46 · U5 40.12–49.66 · U6
55.54–58.96. (Whisper's segment timing on U6 was unstable across runs;
word-level timestamps settle the line at local 5.52–8.76 s. The master
ASR's hallucinated tail past 60 s is an instrument artifact on the
near-silent frozen tail — the take-level runs show no speech after 58.96 s.)

## BLAM GATE (master; U1 take reads identically)

- A1 onset t50 0.0 s / t90 0.0 s — **PASS** · A2 dead head 0.0 s — **PASS**
- A3 head −29.58 dB vs median −38.67, accent ≤0.5 s — **PASS** (accent clause)
- A4 head bursts 0 vs control 15 — **PASS**
- V1 opening motion ratio **0.26** (bar ≥0.6) — **FAIL**
- V2 first bucket 0.47 vs max 7.36 (ramp pattern) — **FAIL**
- E1 named impact ≤1.0 s — **PASS on the eye**: frame 0 IS the leap,
  mid-flight over the stage from behind the hat; she is still airborne at
  0.25 s and landing by 1.0 s (frames 0/6/12/24 eyed). The V1/V2 readings
  measure the leap's apex-hang + slow push — low frame-delta, not a held
  still — but the bars are the bars: both are logged FAIL.
- E2 — the "~ WuBu ~" bug is on screen from frame 0 (graphic at 0.0 s);
  the format is a serial chamber piece, not a montage format. PASS.

## JOINT GATE (all five boundaries declared BREAKs, per script note 8)

Episode BASE (95th-pct intra-unit adjacent MAE) = **6.50**. Seam MAE is
logged, not barred, at BREAKs. Declared matches **eyed PASS at all five**
(seat + gaze spine; the book carried across U3→U4 — strip read: U3 ends
on the book close-up, U4 opens on the reading, hat + lamp foreground).

| Joint | Seam MAE | Upstream tail | Downstream head |
|---|---|---|---|
| U1→U2 | 26.58 | 6.31 | 1.80 |
| U2→U3 | 26.33 | 2.43 | 1.33 |
| U3→U4 | 111.37 (close-up→wide scale change) | 12.57 | 1.20 |
| U4→U5 | 22.39 | 2.38 | 2.49 |
| U5→U6 | 35.60 | 3.38 | 2.72 |

Item 6 (downstream head ≥ 8 absolute): FAIL at all five — the floor
exceeds this episode's own BASE (6.50); it is the same miscalibration E2
found. Under the standing distribution-relative replacement the heads
read **LOW-MOTION class**: units open composed and build (the generator's
known head-settle, the same behaviour behind the V1/V2 readings).
Item 6 logged **CONDITIONAL**, not passed over in silence.

## DIGESTION GAPS (measured on master ASR timings)

- **GAP 1 — PASS.** Speech-free 17.02→20.68 s = **3.66 s** across the
  U2→U3 boundary: the non-applause, then the keeper fetching the book
  into the light before U3's first line.
- **GAP 2 — FAIL.** Speech-free 39.46→40.12 s = **0.66 s**. The held look
  exists inside U4, but the scripted 2–3 s of air after U4's peak turn is
  not there — U5's first line lands at 0.12 s of its unit. The episode's
  one failed structural gap.
- **GAP 3 — PARTIAL.** The freeze is built and verified: picture holds
  57.5–60.0 s (MAE 0.007 between 58.5 s and 59.9 s outside the card), the
  QUESTION card fades in at 57.7 s and holds (eyed at 59.5 s — legible,
  bone serif, gold rule). BUT the Occupant's line runs 55.5–58.8 s, so
  speech overlaps the freeze's first ~1.3 s and the speech-free frozen
  tail is **~1.2 s**, not the full 2–3 s.

## FACE / WORDMARK / TEXT LAWS

- **Occupant face law — PASS.** No frame in any take shows her face lit
  or front-on; hat, gloves, programme and the lamp carry every appearance
  (contact sheets + joint strips + master frames eyed). Two panels carry
  a shadowed profile sliver at the hat's edge (PEAK-U01 v2, PEAK-U04) —
  never front-lit; in the takes she reads as silhouette throughout.
- **Wordmark — PASS.** No UNC in this show (script). The "~ WuBu ~" bug
  is post-drawn, exact, bottom-right, every frame (eyed at 0 s and 59.5 s).
- **Generated text — PASS with texture disclosed.** No legible words
  anywhere in generation: the guest book carries illegible
  pseudo-handwriting texture (U3 close-ups), the programme carries print
  texture (U5/U6), the lease notice stays blurred (U1 tail). A guest book
  with handwriting texture is diegetically right; nothing reads.

## FLAWS — disclosed plainly

1. **BLAM V1/V2 FAIL** (apex-hang head; audio bars + E1 pass). See above.
2. **GAP 2 compressed to 0.66 s** (scripted 2–3 s).
3. **GAP 3 partial**: the last line overlaps the freeze head; silent
   frozen tail ~1.2 s.
4. **Dress drift** (the lineage's known tax): U2 mid-shot dress reads
   longer; U3 the Dancer wears a counter gown; U4's seated dress is long
   with thin straps; U6's closing frames wear a different floral/lace red
   dress. Vermilion + tight bun hold in every unit.
5. **U1 nits**: the Usher's aisle entrance wears a peaked cap (not in his
   locked look); mid-unit the Dancer briefly holds a book-like object
   (not scripted).
6. **U4 staging variant**: the Dancer delivers "She never claps" seated
   beside the seat rather than standing at the book — reads deliberately;
   the gaze spine (page→hat) still lands.
7. **U5 grade shift**: a red stage wash vs the episode's warm-shaft grade,
   and one near-black stretch at the dark-aisle beat.
8. **Master loudness −23.20 LUFS** — quiet (pure-gain law, TP-capped).
9. **U6 opening shoe** reads as a lace-up oxford at still scale (carried
   from the PEAK-U06 panel nit); the tap staging itself is big and singular.
10. **Joint item 6 CONDITIONAL** at all five boundaries (see JOINT GATE).

## CANDIDATE RECOVERIES (parent's call — not fired; budget spent)

- **U1 refire** aimed at V1/V2: prompt the leap already travelling at
  frame 0 (descent phase, not apex) — the only gate failures on the head.
- **U5 refire** aimed at GAP 2: hold the Dancer's first U5 line later in
  the unit (open on the house dropping to dark + the held look for ~3 s
  before she calls). Dialogue is verbatim in the current take; a refire
  trades a known-good take for a gap fix.

Everything else is closed: panels, takes, segments, joined, master,
control encode, graphics, gates — all on disk under this episode dir.
