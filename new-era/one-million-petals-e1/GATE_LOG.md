# ONE MILLION PETALS — E1 GATE LOG
Title: "How Many Petals Are Fake?" · Script LOCKED v1 (SCRIPT_E1.md)
Production: production coordinator (parent-assembled later; no master
in this log). Rule set: fail-once-then-ship; dialogue-is-the-gate
(dual ASR per take); 2 cap-exempt lines (U2 bet, U5 demand);
board-ledger + garment-ledger eye checks per BRIEF.md.

## §1 Cast / look gate (anchors built by coordinator, graded at still stage)
- LILA (refs/lila_sheet.png + lila_front.png): woman ~30, strong
  stubborn chin, dark hair in a bun, long red coat over cream dress,
  small red hat, cloth petal sack on a strap, wooden tally-board tag
  at the hip — identical across all 3 sheet views. PASS. NOTE: the
  separately generated front was a DIFFERENT woman (loose wavy hair,
  softer face) — rejected as an anchor (kept as lila_front_gen.png);
  the canonical lila_front.png is a crop of the sheet's front panel,
  identity-exact.
- OLD PETT (refs/pett_sheet.png + pett_front.png): big broad man
  ~60, large white moustache, ruddy face, rolled sleeves, brown
  waistcoat + canvas apron, wooden cart with a mountain of pink
  petals — identical across sheet views; front (arms spread,
  showman's welcome) is the same man. PASS.
- MOSS (refs/moss_sheet.png + moss_front.png): kind slow-faced
  baker ~50, soft round face, grey-brown hair, flour-dusted white
  apron, bread stall with loaves — consistent sheet + front. PASS.
- PIA (refs/pia_sheet.png + pia_front.png): young woman ~22, long
  dark braid, cream blouse, rust-red skirt, red-and-cream striped
  scarf — consistent; front's face reads slightly younger/rounder
  than the sheet's, same person class, braid + scarf exact. PASS
  (minor front drift noted).
- PIO (refs/pio_sheet.png + pio_front.png): young man ~22, short
  dark hair, bright grin, cream shirt, brown trousers, the SAME
  red-and-cream striped scarf as Pia — clearly a distinct person
  from Pia (male twin), scarf match exact. PASS.
- DORO (refs/doro_sheet.png + doro_front.png): smooth man ~35,
  slicked dark hair, sly calm face, deep-green velvet jacket, cream
  shirt, garland of pink/white flowers at his neck, inside the
  garden at the chain-link gate — identical across sheet views.
  PASS. NOTE: the separately generated front was a DIFFERENT man —
  rejected (kept as doro_front_gen.png); canonical doro_front.png
  is a crop of the sheet's front panel, identity-exact.
- GRADE: warm gold late-afternoon daylight, petal-pink/cream
  palette, deep garden-green accents, 35mm grain — held across all
  twelve anchors. PASS.
- LILA's tally board renders in the anchors as a small plain wooden
  board/tag at her hip (no numbers) — numbers are carried by the
  peak stills and vehicles, per unit state.
- PEAK STILLS (panels/peak_u1..u6.png, 16:9 crops *_169.png used as
  first-frame conditioners): U1 banner reads exactly "1,000,000
  PETALS = THE GARDEN", board 12 legible, petal rain, Doro at the
  gate (twins read as young boys in the wide — noted); U2 melt
  tableau with board 62 + hat in Pett's hand (twins read as two
  girls — noted); U3 the waking wide (board 31, bowl, gate, Doro);
  U4 bowl of pink water + board "31 REAL — 19 FAKE" exact; U5 the
  three faces (shock / shock / delight) with the dip below; U6
  dusk gutter, board 231 + chalk line, heavy sack (black petal not
  clearly visible in the peak's garland — noted).

## §2 Fire log (fail-once-then-ship; 10 fires total)
- U1 t1 FIRED (peak_u1_169 + lila/pett/doro/moss fronts) → SHIPPED.
- U2 t1 FIRED → failed: cap-exempt bet truncated ("For nothing."
  absent), "Done!"/"Shake on it." absent, hat back on Lila's head
  mid-take. REFIRE t2 (one-hat discipline + paced turns) → SHIPPED.
- U3 t1 FIRED → failed: dream insert broke composition (second
  Lila, new camera, no snap-back) though dialogue was perfect.
  REFIRE t2 (in-place dream, one-woman rule) → SHIPPED.
- U4 t1 FIRED → failed: Pett's refusal line absent (tail loss).
  REFIRE t2 (all lines inside 8s, silent board-paint ending) →
  SHIPPED.
- U5 t1 FIRED → SHIPPED (cap-exempt landed; see §3). A refire t2
  was still fired for the garment contradiction (hat worn from
  frame 1 + duplicate hat in the box); t2 fixed the garment but
  LOST the cap-exempt demand entirely → t1 ships, t2 not shipped.
- U6 t1 FIRED (conditioned on shipped U5 t1's end frame
  work/qc/u5_t1/end_frame.png + peak_u6_169 + fronts) → SHIPPED.

## §3 QC per shipped take (ffprobe + frame strips in work/qc/<take>/ + dual ASR)
All shipped takes: 10.000s, 240 frames, 24fps (U1–U5 1248×704
native; U6 1280×720). Board + garment eye checks per frame strip.
- U1 t1 (md5 ec09f52229f426fb3a2ab169685e93aa): ASR both
  checkpoints, all 4 lines in order, right speakers (Pett call
  0.2–2.7 / Lila 12-petals 2.9–5.4 / Pett coat 5.6–7.4 / Lila
  refusal 7.6–9.6). Board 12 legible f_0.5; banner exact; hat ON,
  coat ON, sack small; Pett's eyes land on her hat in the closing
  two-shot. PASS.
- U2 t2 (md5 da6a752d421edb6008b2e0dec624fdbf): ASR both
  checkpoints: Pett's price, Lila's hat offer, "Done.", and the
  CAP-EXEMPT BET COMPLETE through "For nothing." — with "by
  sunset" slurred to "and set" on both checkpoints (see §4).
  "Shake on it." absent on ASR in both takes (handshake lands
  visually, f_9.7). MELT ON CAMERA: petal goo-stretch f_5.0,
  melted drip f_8.0. Board 62 chalked, reads at f_0.5 (small,
  part-cropped). Hat: single hat with Pett from the sale on;
  Lila bare-headed after the opening frames.
- U3 t2 (md5 e3f7323741289584631793cbc6465291): ASR: Doro taunt
  verbatim both checkpoints; Lila's answer lands as "My guy
  garden. I am buying it back." (see §4). PICTURED WISH: waking
  wide work/qc/u3_t2/f_0.5.png vs dream frame f_6.0/f_7.0.png —
  SAME locked composition (table frame-left, gate frame-right);
  the dream transforms in place: gate open, garden flowered,
  hat on, sack full and round, she smiles — composition match
  VERIFIED. Board "31 REAL" written in the closing close-up
  f_9.7. Sack flat in waking frames, full in dream frames.
- U4 t2 (md5 bf3f28d5746dcacc1256702a91362590): ASR both
  checkpoints: "Look. Your petals. Pink water." / "Bad luck!
  Nineteen new petals. Free!" / "My hat back. And real petals.
  All nineteen." all verbatim; Pett's refusal lands as "No."
  only (8.9–9.4s, low level) — the rest of the line absent in
  both takes (see §4). Board "31 REAL — 19 FAKE": reads across
  f_8.0/f_9.7 with the "19" partly under the painting hand at
  the final frame (mid-paint occlusion, designed-object class).
  Hat hugged to Pett's chest f_5.0/f_6.5; Lila bare-headed.
- U5 t1 (md5 a5bef2c525bfddfe5a3c7e938acaeaa0): ASR both
  checkpoints: "Moss. Pia. Pio. Watch his best petal." verbatim;
  CAP-EXEMPT "Open the box, Pett." spoken in full at 4.7–5.8s —
  both checkpoints transcribe the name as its homophone "pet"
  (phonetically identical; the line is landed, see §4 note);
  Pett's payoff "The hat and 200 real." (leading pause
  compressed). THE DIP + THREE FACES: f_2.0 — Moss shock, Pia
  shock, Pio delight, all large and readable BEFORE the
  collection; the crown petal in Lila's hand at the bowl.
  "231" reads engraved on the coin-box lid f_5.5 (wrong object —
  see §4).
- U6 t1 (md5 a331d7121681e20125924fc9b808331b): ASR both
  checkpoints: Doro's "One black petal, Lila, for your garden."
  (name ASR-rendered "Leela", see §4) + Lila's "Tomorrow I buy
  more." Board 231 + fresh chalk line legible f_2.0/f_5.0; hat
  ON, heavy sack, kept petal dropped — floats in the stream
  f_8.0. Doro at the gate with the garland + one black petal
  f_0.5. Dusk grade holds.

## §4 Disclosed flaws (ship-with-flaws, fail-once-then-ship)
1. U2 cap-exempt bet: complete in structure and wording except
   "by sunset" performed slurred — both ASR checkpoints read
   "real and set". The line's tail "For nothing." lands (it was
   absent in t1). Disclosed as a one-phrase pronunciation slur
   on a cap-exempt line.
2. U2 "Shake on it." is not heard in either take; the handshake
   itself lands visually at the close of both.
3. U2 opening frames (~0–2s) show two red hats (peak-tableau
   bleed: one in Lila's hand, one already in Pett's) and the
   board already reads 62 at 0.5s; from the sale onward the
   single-hat state is correct. U2's twins read as two young
   girls (peak inheritance), not the anchored adult Pia + Pio.
4. U3 Lila's line lands as "My guy garden. I am buying it
   back." on both checkpoints ("garden" preceded by a slurred
   "guy" — the scripted "My garden." is not clean).
5. U3's dream never snaps back: the unit ends inside the
   bloomed frame (closing push-in on Lila, hat on, writing
   "31 REAL"). The composition-match gate passes; the return
   to the chained-gate waking frame does not occur.
6. U3 + U6: Doro's face drifts from his anchor (reads as a
   different, long-faced man in the green velvet jacket; U1's
   Doro matches the anchor). Costume, place and actions correct.
7. U4 Pett's refusal line lands as "No." only in the shipped
   take and is absent entirely in t1; "The hat is mine. Take
   the nineteen." is not heard in either take. The refusal is
   carried visually (hat hugged to his chest, head shake).
8. U4 board: the "19" is partly occluded by Lila's painting
   hand/brush at the final frame; the full "31 REAL — 19 FAKE"
   reads across the closing frames.
9. U5 garment: Lila wears the red hat from the first frame of
   the shipped take (peak still carried the hat), and a second
   hat is visible inside the open coin box at the payoff — the
   on-camera hat return the script stages does not read. The
   refire fixed this but lost the cap-exempt line, so the
   flawed take ships per the cap-exempt priority.
10. U5 Pett's face wobbles balder mid-take (f_4.5/f_5.5) vs his
    anchor; "231" is engraved on the coin-box lid instead of
    painted on Lila's tally board (number correct, object
    wrong); Pett's payoff line loses its leading pause.
11. U5 cap-exempt note: "Open the box, Pett." — both ASR
    checkpoints transcribe the name as "pet" (homophone). The
    line is judged landed: spoken in full, in place, by the
    right speaker; no refire can change a homophone.
12. U6: the black petal on Doro's garland is small and dark in
    frame (visible f_0.5, not prominent); "Lila" is pronounced
    / ASR-rendered "Leela" in Doro's line.
13. Cross-unit: the twins read younger than their anchors in
    U1/U2 (peak inheritance); from U5 they read as the anchored
    young adults. Lila's tally board is a small hip board in
    U1–U3 and a large painted board at the cart in U4–U5 (prop
    scale drift, numbers always correct per unit).
14. U1: Pett's closing eye-line lands on Lila's face/hat area
    in a tight two-shot rather than an isolated hat beat.


## 5. PARENT ASSEMBLY + MASTER GATES (parent, 2026-11-27 ~21:47 EST)

- Takes verified against COMPLETION.json (all six md5s match).
  Joined: filter-concat, scale-conformed (U6 1280x720 -> 1248x704
  chain), probed 1440 frames; video stream 60.125s / audio 60.16s
  with start_time 0.000 (the known native-offset pattern).
- ASSEMBLY DEFECT CAUGHT + FIXED: the first two master encodes read
  1441 frames / 60.0417s video (audio exact 60.000s). Diagnosis by
  null-mux: every take is exactly 240f, the joined file is exactly
  1440f, and the full filter chain (bug + setpts + trim) outputs
  exactly 1440f — the extra frame was duplicated by the output
  `-r 24` vsync at the encode stage. Corrected encode drops `-r 24`
  (the setpts grid carries the timing): master now probes EXACTLY
  1440 frames, video 60.000s, audio 60.000s, start_time 0.000 both
  streams, AAC 48k, faststart.
- Master: masters/one_million_petals_e1_16x9.mp4
  md5 717f668f50f172c6361b953d9e840251, 32,390,095 B.
  CRF-18 proven by size differential: CRF-23 control of the same
  joined file = 18,739,435 B -> 1.73x (the SEI string is not a valid
  proof on this ffmpeg build).
- Bug eye-verified on the 55s frame: "~ WuBu ~" gold, bottom-right,
  exact wordmark. The frame also confirms the U6 disposal staging
  (Lila at the canal, petal in hand over the water, tally board
  reading 231 at frame-left).
- MASTER EAR-READ (dual-checkpoint ASR on the finished master,
  work/qc/master_asr.json): PASS. Both checkpoints agree closely.
  Every scripted line is present: U1 4/4 (the haggle opens clean);
  U2 the count and the hat price land, "Done." lands, and the
  CAP-EXEMPT bet lands complete — "Every petal in my sack is real
  and set. Or the coat is yours. For nothing." — with the disclosed
  "by sunset" -> "and set" slur; "Shake on it." absent (disclosed
  §4.6-class). U3 Doro's boast lands; Lila's answer lands with the
  disclosed "My guy garden" insertion. U4 the dip verdict, the
  count-back and the demand land; Pett's refusal lands as "No."
  only (39.1-39.5s), carried visually per §4.7. U5 the witness call
  lands ("Moss, Pia, Pio, watch his best petal."), the CAP-EXEMPT
  "Open the box, Pett." lands in full (ASR renders the name as the
  homophone "pet" on both checkpoints — judged landed, §4.11), and
  the payoff "The hat and 200 real." lands. U6 Doro's gift line and
  Lila's "Tomorrow I buy more." both land.
- Disclosed flaws: the 14 production flaws in §4 stand as the
  delivery disclosure (headline: U4 refusal reduced to "No."; U3
  dream never snaps back; U5 hat worn from frame 1 + duplicate hat
  in the coin box; U3/U6 Doro face drift; twins read young in
  U1/U2). Shipped under fail-once-then-ship; the user's playback
  verdict is the authority above this master.
