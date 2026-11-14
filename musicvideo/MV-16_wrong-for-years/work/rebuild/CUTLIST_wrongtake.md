# MV-16 'Wrong for Years' — CUTLIST (assembly of record)

Master: 28 segments back-to-back, tiling 0–183.20s at 24fps
(4,396 conformed frames + 1 cloned tail frame = 4,397).
Per-chunk source/target/factor table: work/segments/conform_log.json
(final patch state) + work/segments/conform_run.log (full v2 run).
Method: phrase-level chunk warps — chunks tile each scene window by
grid line starts; take word groups come from take-ASR JSONs on disk;
words/gap sub-chunk splits compress take dead air harder than sung
words. Reorder scenes permute chunks to the song's line order.

| Scene | Window | Take | Lines | Notes |
|-------|--------|------|-------|-------|
| S01 | 0.00–5.24 | s01_t3 | L1–L3 | Hook. L3 warp 2.06× (take sustains "me") — softest sync in C1. Frame 0 = fist-up peak. |
| S02 | 5.24–11.74 | s02_t1 | L4–L6 | Friends nod, mouths closed. |
| S03 | 11.74–19.28 | s03_t1 | L7–L9 | CHUNK REORDER (take sang WFY/still/WFY). Head pocket filled from take tail. One gap chunk at 6.18× (8-frame nod burst). |
| S04 | 19.28–26.04 | s04_t2 | L10–L12 + Hey | HEAD TRIM 0.30s (closed-mouth pose) → trio warps 0.94–1.05. Hey pocket = shout span (head back, 2.16×). Disco ball grows overhead. |
| S05 | 26.04–31.86 | s05_t3 | L14–L16 | Re-fire: t2 sang the friends' lines (generator drift, caught at conform) — t3 delivers "Belted the whole chorus in the car / Like I wrote it / (yeah)" (rode=wrote homophone). Season flip leg 1 (summer). |
| S06 | 31.86–38.14 | s06_t2 | L17–L19 | Season flip completes (summer→autumn→snow). Second (what) unused. |
| S07 | 38.54–47.92 | s07_t2 | L20–L23 | Karaoke quatrain (performed text). SCREEN window installs (post layer). |
| S08 | 48.94–54.10 | s08_t2 | L24–L27 | PC1 performed stack (wrong×2/kept×2). L25 chunk 3.00× (short song line, leisurely take). Room shrinks. |
| S09 | 54.10–59.46 | s09_t1 | L28–L30 | PEEL 1 (bowling→hawaiian) on "decade" — frame-verified. |
| S10 | 59.46–65.84 | s10_t1 | L31–L34 | Personal weather: cloud rains only on HOST (frame-verified). (oh-oh-oh) = 2 take words. Trio phrase-compressed (take spreads it). |
| S11 | 65.84–73.40 | s11_t1 | L35–L38 | CUSTOM chunk map (take fused the (oh) inside WFY + extra still group unused): L35←oh tail, L36←clean WFY, L37←WFY+oh, L38←still. Factors 0.62–1.91. 1 tpad frame at tail. |
| S12 | 73.40–77.90 | s12_t2 | L39–L41 | C2 entry. L40 2.28×. 1 tpad frame. |
| S13 | 77.90–86.66 | s13_t1 | L42–L45 | POST gang chant (staged exception: friends chant). WORD CHASE assembles hook words on the blank wall (post). Tail gap drifts slow (0.31×) across the breath pocket — deliberate. 1 tpad frame. |
| S14 | 86.66–90.38 | s14_t2 | L46–L48 | Mic stand leans the mic to him. L47 forced split: words 2.00× + 0.29s gap burst 11.5× (7-frame head-bob into the (yeah), 2.13×). |
| S15 | 90.38–96.38 | s15_t2 | L49–L53 | L51 (what) omitted by take → merged into L52's span (BAD-WORD rule: no re-fire for a background ad-lib). Chaos behind / calm front. |
| S16 | 96.38–100.06 | s16_t2 | L54–L56 | L54 (uh) merged into L55 (same ad-lib rule). THE TURN on "Ten years deep". |
| S17 | 100.06–104.78 | s17_t2 | L57–L60 | PC2 stack. Prop swap mic→tambourine→maraca→trophy. |
| S18 | 104.78–110.08 | s18_t1 | L61–L63 | PEEL 2 (hawaiian→gold glitter jacket) — frame-verified (jacket on by 8.6s, tee blank). |
| S19 | 111.16–116.48 | s19_t2 | L64–L66 | Runaway lyric sheet; SIDEYE dives. |
| S20 | 118.04–124.02 | s20_t1 | L67–L69 | CHUNK REORDER. Scatter & reform. |
| S21 | 124.02–132.24 | s21_t2 | L70–L72 | Room zero-G. L71 slow chunk repaired with HOLD-FILL (words 0.62× + take-tail hold fills the song's breath). |
| S22 | 132.24–140.10 | s22_t2 | L73–L76 | Medium swap: paper cut-out room, GUY full colour. |
| S23 | 140.10–145.08 | s23_t2 | L77–L78 | Impossible bend. (yeah) chunk 0.47× — slow bend reads as slow-motion, kept deliberately. |
| S24 | 145.08–152.46 | s24_t1 | L79–L82 | FC entry. Palette snap to concert gold. NSM double inside. |
| S25 | 152.46–158.98 | s25_t1 | L83–L86 | They build the set around him. NSM doubles. |
| S26 | 158.98–164.90 | s26_t1 | L87–L89 | CHUNK REORDER. WORN GRAPHICS: kinetic words drawn on the blank tee in post. |
| S27 | 164.90–172.84 | s27_t2 | L90–L92 | Clone handoff (sings into his double's mic). |
| S28 | 174.10–182.80 | s28_t2 | L93–L97 | L94 (oh) merged into L95 (ad-lib rule); merged chunk 0.48× (marginal floor brush, outro wide shot). Day–night flip; final frame rhymes S01's fist-pump. 1 tpad frame. |

Post layers (work/mv16_kinetic.ass, 1,387 events):
- Kinetic per-word HIGHLIGHT on every performed line (display text
  from the corrected grid; ASR supplies timing only, mapped
  proportionally — no ASR slip can reach the screen).
- SLAM style on every "Wrong for years" entry + FC NSM doubles.
- S13 word chase (cumulative words on the stage's blank wall).
- S26 worn graphics (words on the blank tee, red highlight).
- SCREEN PiP (lower-right): installs S07, steady + glitch bars C1–C2,
  beat-pulse POST, dark BR, gold equalizer FC, fade-out OUT. The box
  never shows a second lyric set (bank rule B7) — the screen-vs-singer
  gag is carried by reaction + the kinetic layer.
- `~ WuBu ~` bug, bottom-right, full runtime.
