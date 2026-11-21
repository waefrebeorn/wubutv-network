# PILOT-1 THE MACHINE — GATE LOG

## Panel gate (spec §4.5) — 2026-11-15
All 12 panels read back after generation (no panel locked sight-unseen).
- Identity/detail vs LOOK: PASS all. UNC wordmark on PNL-CHAR-UNC-hero reads
  exactly `~ WuBu ~`, bold yellow-gold, chest, no border/box/emblem — PASS
  (hard gate). LAURA identity consistent hero↔face. Singer (cat) consistent
  across PEAK-U1/U2/U3/U6: black, red collar, gold bell, blue eyes.
- Aspect: PASS all after centre-crop of the two 3:2 generations to 16:9
  (framing only). All panels 1920×1080 or 2048×1152.
- Type gates: CHAR hands empty ✓ · WORLD empty of characters ✓ · PROP exactly
  one pair of headphones ✓ · PEAK one-glance legibility ✓ (U1 = doctrine frame
  sentence verbatim) · no captions/titles/readable text in any panel ✓
  (corkboard sheets blank or illegible set dressing).
- Disclosed panel nits: (1) PEAK-U3 shows LAURA's worn headphones + the desk
  stand pair from the WORLD plate — two pairs, both motivated and consistent
  with the room plate; (2) PEAK-U4 crops a sliver of gold lettering at UNC's
  chest edge — partial, not a displayed wordmark; (3) PEAK-U6 puts the
  wordmark on UNC's back (he faces the monitor) — text exact `~ WuBu ~`,
  placement differs from the CHAR hero's chest print; video prompt for U6
  restates the chest wordmark as the invariant trait.

## Take gates — completed by finisher pass, 2026-11-15

### Dialogue gate (transcription vs SCRIPT.md line table)
Method: faster-whisper large-v3-turbo (int8, NO VAD), house G7 config
(g7_check.transcribe), run on the SHIPPED segment audio (the exact audio in
joined/master). Raw ASR JSON: work/qc/dialogue_gate_asr.json; driver:
work/qc/transcribe_segments.py.

| Unit | Scripted line | ASR of shipped audio | Verdict |
|---|---|---|---|
| U1 | The mouth moved, UNC. Nothing came out. | "The mouth moved UNC. Nothing came out." (words 5.12–8.80s, all p≥0.51, key words ≥0.98) | PASS — exact words (ASR drops the comma) |
| U2 | Cut to the mouth, Laura. Mouth is the record. | exact, 5.08–8.76s, p≥0.86 | PASS |
| U3 | It sang a word that isn't written, UNC. | exact words, p high | PASS |
| U4 | File it under the singer. Singer's the record. | exact | PASS |
| U5 | It fixed a take we haven't broken yet. | exact, 4.96–7.22s, p≥0.83 | PASS |
| U6 | It knows our names now. Cut it anyway. | exact AFTER finisher correction #1 (see below); before it, the final word was truncated mid-word ("Cut it and…", stub p=0.23) | PASS as shipped |

Placement note (disclosed): lines land earlier than the script's 7–9s grid
slot in U1/U2/U5 (onsets ≈5.0s) — words are exact everywhere; the generator
front-loads speech. No line is garbled or unintelligible in the shipped cut.

### Finisher assembly corrections (2026-11-15, assembly only — no refires)
1. **U6 window widened 210f → 216f.** The CUTLIST's 210f trim amputated the
   final word of U6's line: the raw take speaks "anyway" at 8.60–8.90s
   (p=0.968, verified on the take), but the 210f window ends at 8.75s.
   Segment rebuilt: take frames 0–215 stretched ×240/216 (setpts 1.111111,
   atempo 0.900, audio window 0–9.0s). Re-transcribed: full line lands,
   "anyway" complete 9.56–9.80s p=0.957. Final frames still hold the
   open-mouth bridge cliff (beat closes ≈9.25s take time; last shipped
   frame = take 8.96s, mouth open, eye-verified on master f1439).
2. **U2 black tail found + fixed (same defect class as U5, missed by the
   original QC's 0.5/5.0/9.5 probes).** Full-decode frame scan: U2 take
   frames 235–239 are pure black (mean-gray 0.0; frame 234 = 59.44).
   Segment rebuilt: take frames 0–234 stretched ×240/235 (setpts 1.021277,
   atempo 0.979167, audio window 0–9.7917s). U2's line ends at 8.76s —
   untouched. Re-transcribed exact; segment tail now ends on the cat
   profile ECU, mouth open.
3. **joined.mp4 rebuilt with the concat FILTER (not stream copy, not the
   concat demuxer).** The stream-copy join had skewed timestamps (broke
   -ss seeking) and the demuxer+re-encode join duplicated frame 0
   (1441 decoded frames, f0==f1 MAE 0.0). Concat-filter join verified by
   full decode: exactly 1440 frames, zero black frames, zero exact
   duplicate frames. Segments remain CRF 12 intermediates per CUTLIST;
   joined is a CRF 12 intermediate; the CRF 18 law is applied at the
   master encode.

### Master gate — 2026-11-15
- House master: masters/pilot1_the-machine_16x9.mp4 — md5
  847091dfde8da850229e747038c5bf50, 19,825,048 B, 1440 frames / 60.010s
  (video exactly 60.000s; +10ms AAC tail), 1280×720 @24fps, x264 SEI
  verified crf=18.0, AAC 48kHz stereo (copied from joined), faststart,
  `~ WuBu ~` bug bottom-right (drawtext, DejaVu Sans Bold, #FFC400).
- Chat copy: masters/pilot1_the-machine_chat.mp4 — md5
  b638badd0389cb3241da33bbd78a249c, 19,877,856 B (≤50 MB), 1440f,
  video capped ≤2.7 Mbps, audio copied from house master.
- work/joined.mp4 md5 3bf766317e7e6d2b38fa11238699fb7d.
- Eye pass on the master (frames extracted by number): f0 = doctrine
  frame verbatim (monitor cat mouth wide in silence, LAURA headphone at
  frame edge) ✓ · mouth handoff present at every joint (f239/240,
  f479/480, f719/720, f959/960, f1199/1200) ✓ · f479 = cat profile ECU
  mouth open (no black) ✓ · f1199 = giant open mouth (U5 fix holds) ✓ ·
  f1439 = monitor mouth open + UNC in profile (bridge cliff) ✓ · UNC
  back wordmark at f1300 reads exactly `~ WuBu ~`, gold — hard gate
  PASS ✓ · bug exact on f0 crop ✓ · no generated captions anywhere ✓ ·
  motion at every cut (no halted starts; coordinator MAE 13.4–20.2
  stands, finisher dup/black scans clean) ✓.

### Disclosed flaws (ship-as-is, stated plainly)
1. U3 singer's eyes read yellow-green vs blue in U1/U2 (came in with
   PEAK-U3; logged in TAKE_HISTORY at fire time).
2. Dialogue placement: lines onset ≈5.0–6.4s instead of the scripted
   7–9s slot in U1/U2/U5/U6 (words exact; generator front-loads speech).
3. U6's final frame: the monitor-mouth half of the bridge cliff is
   unmistakable; UNC's own mouth in profile reads only slightly parted
   in the very last frame.
4. Three units ship time-stretched (U2 ×1.021, U5 ×1.096, U6 ×1.111)
   per the assembly fixes — inside house warp practice, logged here.
5. Panel nits carried from the panel gate: two headphone pairs visible
   in U3's world (both motivated by the WORLD plate); PEAK-U4's sliver
   of gold lettering at UNC's chest edge (partial, not a displayed
   wordmark); U6's wordmark is the back print (exact text) rather than
   the CHAR hero's chest print.
