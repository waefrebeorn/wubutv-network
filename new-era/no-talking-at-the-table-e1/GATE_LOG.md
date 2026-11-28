# NO TALKING AT THE TABLE — E1 GATE LOG
Title: "Who Loses His Chair First?" · Script LOCKED v1 (SCRIPT_E1.md)
Production: successor coordinator (reconciled from disk; predecessor's
anchors, peak stills and u1_t1 inherited, not regenerated).
Rule set: fail-once-then-ship; inverted ASR gate; 3 cap-exempt sound
events; chair-ledger eye checks per BRIEF.md.

## §1 Cast / look gate (anchors inherited, verified in use)
- BRUNO (refs/bruno_sheet.png + bruno_front.png): big broad man, tall
  white chef's hat, dark green jacket, grey stubble — consistent in
  every unit. PASS.
- KIP (refs/kip_sheet.png + kip_front.png): small slight man, messy
  dark hair, black bow tie, cream shirt, mahogany waistcoat —
  consistent U1–U6. PASS (wardrobe drift in the REJECTED u5_t2 only).
- MANGO (refs/mango_sheet.png + mango_front.png): glossy orange-gold
  mango man, green leaf sprout, wide white grin, deep green waistcoat
  — consistent. PASS (grin softens in places; see flaws).
- PEPPER (refs/pepper_sheet.png + pepper_front.png): tall red pepper
  man, green stem cap, long fingers — U6 only, as scripted. PASS.
- GRADE: warm candlelit tungsten, mahogany/cream/deep-green, brass
  sconces, 35mm grain held across all six units. The wall sign is a
  PICTURE (mouth + red circle + slash), no letters, in U1–U5. PASS.

## §2 Per-unit fire log (9 unit fires total: 1 predecessor + 8 successor)
- U1: t1 fired by predecessor. SHIPPED t1.
- U2: t1 fired → squeak unverifiable + beat order scrambled → refire
  t2 fired. SHIPPED t2.
- U3: t1 fired. SHIPPED t1.
- U4: t1 fired → HELLO unverified + end state unreadable → refire
  t2 fired. SHIPPED t2.
- U5: t1 fired (1152×768, wrong aspect; laugh present) → refire
  t2 fired (1280×720 but NO laugh event) → SHIPPED t1 (event wins
  over format; parent crop-conforms — see §4).
- U6: t1 fired, conditioned on shipped U5 t1's end frame
  (work/qc/u5_end_frame.png) + peak_u6 + 4 cast fronts. SHIPPED t1.
No 429/budget signal at any point; no outage retries consumed.

## §3 QC per shipped take (probe · dual ASR · sound event · ledger)
ASR method: asr_dual.py (large-v3-turbo + distil-large-v3) per take,
JSON in work/qc/<take>/asr.json; RMS profiles from the take's own
audio (work/qc/<take>/audio.wav). NOTE on ASR text: Whisper emits
stock hallucination phrases ("Thanks for watching!", "Thank you.",
the Russian subtitle-credit line) over score-only passages. These
are judged NON-SPEECH where (a) both checkpoints emit the stock
phrase over the same window, (b) segment RMS is score-level with no
vocal transient, and (c) no character is depicted speaking. Each
instance is disclosed below and in COMPLETION.json.

U1 t1 — 1280×720, 24fps, 240f, 10.000s, md5 a457c7799c259fe29714a50af3a7154d
- ASR: both checkpoints EMPTY. No speech. PASS (no event scripted).
- Eye: insult-mime opening (thumbs down, finger guns, tongues out),
  sign + saw + trophy blocks on wall, Mango enters with covered dish
  held high, zip-mouth mime, Bruno's three-point law mime, Kip's
  last insult + Bruno's warning finger. Chairs all whole/tall ✓.
  Rolls read ~2–3 hosts / 1 guest (pile small on screen).

U2 t2 — 1248×704, 24fps, 240f, 10.000s, md5 80bcd59add17ef7ca7bf6e5da894ce7a
- ASR: stock-hallucination class only (large-v3 Russian subtitle
  credit + distil "Thank you.", same 0.14–3.9s window, seg RMS
  0.041, score passage). No character speech. PASS.
- CAP-EXEMPT EVENT — KIP's tiny squeak: VERIFIED. RMS bump at
  2.9–3.2s (0.018 → 0.048–0.056) under Kip's clamp beat; band
  listen-check: 2.85–3.30s window high-band (2.5–6kHz) RMS −28.8 dB
  vs full-band −26.3 dB (energy concentrated high = tonal squeak),
  vs score-only control window 1.0–1.4s (band 15.3 dB BELOW full).
  A squeak does not transcribe as words; ASR silence on the event
  is expected.
- Eye: beat order correct — funny face (spoon on nose, cheeks out,
  eyes crossed) → clamp → Bruno saws Kip's chair leg on camera →
  block held up → Kip seated lower, tilted, furious. Ledger U2 end
  KIP −1 ✓. Rolls grow to ~5/1 ✓.

U3 t1 — 1248×704, 24fps, 240f, 10.000s, md5 563e8c4b7b9713d85162e2dc63a6609a
- ASR: stock-hallucination class only ("Thanks for watching!" /
  "Thank you.", 0.30–1.14s, seg RMS 0.019 = near-silence level).
- SILENT SCREAM: VERIFIED SILENT. Bruno's open-mouth scream frames
  (0.5–4.5s) sit over a flat RMS floor (0.013–0.028, no vocal burst;
  a real scream measures ≥0.10 on this scale, cf. U5 t1 laugh at
  0.116–0.19). The gag holds: mouth wide, zero sound.
- Eye: crab dangles from Bruno's raised finger by its claw, body
  rigid, hat trembling; spoon prise-off; finger held high; guests'
  applause; Mango's grin gone flat. Ledger: KIP still −1 ✓ (seated
  lower frame-right), rolls to 8/1 ✓.

U4 t2 — 1248×704, 24fps, 240f, 10.000s, md5 00b6b883eb37b0f4b4c3b1ae702669f3
- ASR: ONE segment only, both checkpoints agree: "Oh, hello."
  0.72–2.26s (large-v3) / 0.72–2.40s (distil), seg RMS ~0.031.
- CAP-EXEMPT EVENT — the phone's "HELLO!": VERIFIED. It is the
  episode's only word-shaped audio and it is the device voice, as
  scripted; no character speech anywhere else in the take. PASS.
- Eye: phone produced HIGH by Bruno (opening frames), guests point,
  Mango hands-up innocence, sawing beat on camera mid-take, roll
  avalanche late. Ledger U4 end MANGO −1: reads mid-take (Mango
  lower after the sawing); end tableau loose — see flaws.

U5 t1 — 1152×768 (3:2 — FORMAT DEVIATION, see §4), 24fps, 240f,
  10.000s, md5 1d2102f82e8b97a8e3d5e1f88c5733d0
- ASR: both checkpoints transcribe the laugh: "Ha ha ha ha"
  1.68–3.02s (large-v3) / 1.68–3.08s (distil), seg RMS 0.116.
- CAP-EXEMPT EVENT — KIP's "HA!": PRESENT BUT WRONG SHAPE. It is a
  ~1.3s multi-syllable laugh run placed mid-dance, not the scripted
  single huge "HA!" after the clamped build, and the held total
  silence after it is not clean. The refire t2 had NO laugh at all
  (ASR empty both checkpoints), so under fail-once-then-ship the
  take WITH the event ships. Disclosed in §4.
- Eye: Mango dances on the table (napkin blindfold, spoon in teeth,
  jelly dome untouched), room shaking silently, Kip purple and
  clamped before the burst; Bruno carries Kip's chair out on his
  shoulder inside the dining room; Kip ends standing, hands clamped.
  Ledger U5 end: chair CARRIED OUT ✓. Rolls frozen 12/1 ✓.

U6 t1 — 1248×704, 24fps, 240f, 10.000s, md5 16fddaae6c62a0469ad7f49ed8472d4f
- ASR: both checkpoints EMPTY. No speech, no vocal sound; Kip's
  laughter is silent (RMS score-level throughout; single 0.106
  transient at 7.3s = dish rattle / room sound class). PASS.
- Eye: Kip eats STANDING at the empty place (verified standing in
  every sampled frame 0.5–9.8s — he never sits); Mango's hip-wiggle
  cue → Kip's silent shake → self-clamp, eyes watering; Bruno's
  nod; PEPPER arrives in the doorway with the covered dish STEAMING,
  takes position beside Kip; final frames push in on Kip clamped,
  gaze to camera, Pepper beside him. Ledger U6: empty place held,
  KIP standing ✓. NEXT CHALLENGER button lands.

Non-shipped takes:
- u2_t1 (1248×704, md5 df4da7861e1eb7da5b3145c109b73651): beat order
  scrambled (punishment opens the take; funny-face/squeak elided);
  squeak NOT verifiable — band check on all candidate windows
  (0–0.5s, 3.4–3.8s, 6.8–7.5s, 8.5–8.9s) showed the high band
  8–17 dB below full band, i.e. no tonal squeak transient.
- u4_t1 (1248×704, md5 3e754c71dc0f9b8daa3dbcb459b7f251): HELLO not
  verified (both ASR checkpoints EMPTY — a loud device HELLO should
  transcribe); principals leave the frame for the final third; the
  MANGO −1 end state never reads.
- u5_t2 (1280×720, md5 52023757fef582ccbd0647ab5bf43099): NO laugh
  event (ASR empty both checkpoints; RMS max 0.091, score-level —
  Kip laughs silently in picture only); end-state room drift (the
  table and Mango leave the frame; plain-wall room); Kip wardrobe
  drift (tweed jacket replaces waistcoat in the final frames).

## §4 Disclosed flaws (all shipped takes)
1. U5 t1 is 1152×768 (3:2), NOT 16:9 — the only format-deviant
   shipped take. It ships because it alone carries the episode's
   turn (the laugh). PARENT ASSEMBLY: centre-crop to 1152×648 and
   scale to 1280×720, or pillarbox — coordinator's recommendation
   is the centre crop; the dance framing is centred and survives it.
2. U5's laugh is a ~1.3s "ha ha ha ha" run at 1.68–3.02s, not the
   scripted single "HA!" after silence; no clean held silence
   follows it inside the take.
3. U5 t1 final frame: Mango is not held frozen on the table (he is
   out of the closing frame); the chair-carry and Kip-clamped beats
   do read.
4. U2/U3 shipped takes carry Whisper stock-hallucination ASR text
   over score passages (documented in §3) — no audible speech;
   flagged so the parent's master ear-read is not surprised.
5. U4 t2: Bruno's chef hat is missing in the final third; the score
   dips to near-silence ~3.9–5.7s; the hosts' roll pile is already
   large in the opening frame (avalanche pre-spent); Mango is at
   the frame edge in the final frame and his grin-gone beat reads
   mid-take, not in the end tableau.
6. U1 t1: Mango's wide grin narrows to a closed smile in the final
   seconds; a duplicate small Mango figure appears briefly in the
   background doorway mid-take; the end-frame roll pile reads ~3/1
   against the scripted 2/1 (piles are small on screen).
7. U2 t2: the sawing is staged loosely in the mid frames (Bruno
   swings the saw standing before kneeling to the leg); roll counts
   are approximate at pile scale.
8. U3 t1: the guests' applause makes palm contact in the late
   frames (scripted: palms an inch apart, no contact); the platter
   carries several crabs, not one; Kip is under-framed mid-take.
9. U6 t1: Pepper's sit-on-nothing mime is not verifiable in sampled
   frames — he arrives with the steaming dish and stations beside
   Kip instead; an unoccupied chair back is visible at the table's
   far side in mid frames (diners' row — Kip himself never sits);
   a legible "PEPPER" name plaque hangs over the door (in-world
   text, designed-object class); the wall sign renders as a smaller
   framed picture rather than the big round sign (set drift);
   Bruno is cropped out by the push-in in the final third; closing
   roll piles read smaller than 12/1.
10. All successor-fired takes except u5_t2 arrived at 1248×704
    (the model's native raster; the predecessor's u1_t1 and u5_t2
    are true 1280×720). Parent conforms at assembly as usual.
No shipped take contains character speech → no silent-audio strip
copies were needed.

## §5 PARENT ASSEMBLY + DELIVERY (2026-11-27, parent by hand)

Assembly: ONE pass. Per-input conform in the filter-concat — U1
1280×720 native; U2/U3/U4/U6 1248×704 scaled; U5 t1 1152×768
centre-cropped to 1152×648 (crop y-offset 60) then scaled — all to
1280×720/24fps/yuv420p, audio resampled 48k, concat n=6 →
work/assembly/joined.mp4 (probed BEFORE the master encode: 1440
frames, video stream 60.125s — the known first-segment offset trap).
Master encode from joined: bug drawtext "~ WuBu ~" gold
bottom-right, then video setpts=N/(24*TB), audio atrim=end=60 +
asetpts=N/SR/TB, audio re-encoded (never copied).
MASTER: masters/no_talking_at_the_table_e1_16x9.mp4 — md5
71d6e9885eab83985e74ca6a772ec8a0, 25,765,966 B, 1280×720, 24fps,
1440 frames, BOTH streams exactly 60.000s, start_time 0.000, AAC
48k, faststart. CRF-18 proven by size differential: same-chain
CRF-23 control = 15,276,577 B → 1.69x (the SEI string is invalid
on this build, per the standing anomaly note).
Bug eye-verified on the 55s frame (work/qc/master_f55.png): gold
"~ WuBu ~" bottom-right, legible; the frame also confirms U6's
end state — Kip standing, clamping his own silent laugh, Mango
grinning beside him, PEPPER arrived with the steaming covered
dish, the PEPPER door plaque and the no-shouting sign on the wall.
MASTER SILENCE-READ (dual ASR, work/qc/master_asr.json + windowed
passes): NO character speech anywhere on the master. The full-file
pass returns only a 0.3s stock hallucination ("I wonder.", both
checkpoints, seg RMS 0.019 over the opening score — the documented
non-speech class). The two word-shaped events verified present ON
THE MASTER by windowed dual ASR: the phone's "Hello." at
31.9–32.5s (U4 window, both checkpoints, RMS 0.034) and Kip's
laugh run "Ha ha ha ha" at 42.0–43.5s (U5 window, both
checkpoints, RMS 0.116–0.124) — the laugh in its disclosed wrong
shape (a run, not the single scripted HA). The U2 squeak stands
verified at take level (RMS + band listen-check, GATE_LOG §3);
the master's 10–20s RMS profile (0.041/0.061) is consistent.
The U3 scream is silent on the master, as shipped.
DISCLOSED FLAWS AT DELIVERY: the full §4 list stands — headline
items: U5's laugh is a ~1.3s multi-syllable run mid-dance, not
the single HA after held silence, and its take was 3:2, crop-
conformed here; U5's closing frame loses Mango's frozen-on-table
beat; U4 loses Bruno's chef hat in the final third and its roll
pile is pre-grown in frame 1; U1 carries a brief duplicate small
Mango in a background doorway and its end grin narrows; U6's
Pepper sit-on-nothing mime is unverifiable and Bruno is cropped
out by the final push-in. Shipped under fail-once-then-ship;
the user's playback verdict is the authority above this log.
Catalogued NO-TALKING-AT-THE-TABLE-E1 (ARC-1).
