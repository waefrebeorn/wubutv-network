# MV-9 Q7 FIX BUILD — GATE LOG (2026-11-13)

Build: `masters/mv9_gotta_hold_it_16x9_v2.mp4` — md5
`345e658bea3c72dbcd6f89675c1390b4`, 148,935,360 B, 4416f, 184.000s.
Chat copy: `masters/mv9_gotta_hold_it_16x9_v2_chat.mp4` — md5
`887c36a748d3d8cd19b55f4d330cbb1e`, 43,208,222 B (≤50 MB), 4416f,
AAC stream-copied (audio stream md5 `2c6c7cbc7519a74055fac77b46cabcd4`,
IDENTICAL to the house master and to v1's).
The approved v1 master (`7eee36c4…`) is untouched. NO delivered flag
written (parent delivers). Q7 scripts: work/q7/{assembly_build_v2,
build_kinetic_v2, split_encode_v2, mux_v2}.py; segments S04/S08/S11/S12
rebuilt, the other 11 byte-identical to v1 (md5-verified vs v1 manifest).

## House gates (work/gate_master.py on the v2 master) — ALL PASS
h264 1280x720 24fps · frames exactly 4416 · duration 184.000s · AAC
48k stereo · x264 SEI crf=18.0 on BOTH halves · faststart moov@36 ·
audio agreement (5 windows): @5s 0.9981, @45s 0.9980, @90s 0.9981,
@135s 0.9979, @175s 0.9974 → min 0.9974, mean 0.9979.
NOTE on the ≥0.998 figure: the min window (0.9974 @175s) is BELOW
0.998 — and it is IDENTICAL to the approved v1 master's min, because
the audio path is the same deterministic AAC encode of the same
track. Reported exactly; not rounded up.

## Motion audit (v2 master, 1fps frame-diff, v1 method)
183 diffs: mean 42.51, min 3.79, median 39.61; NO second below 2.0
(no frozen runs ≥1s). Fine probes: S08b festival span (81.5–83.7s,
0.125s steps) — no near-dup step (the cap-edge slow piece keeps
moving); S04b cutaway span (43.35–43.85s, 0.1s steps) — no near-dup.
MOTION LAW: PASS.

## The six named fix gates

### Fix 1 — S08b "Box" — PASS via cap-edge re-warp (generation route FAILED 4×, recorded)
Named gate: "Box" lands within ±0.5s of 83.96; final warp inside caps.
- Generation (4 fires, all REJECTED at QC — full log in Q7_PROGRESS):
  t1 a593b29f garble+gap+shout, no box · t2 6bf2d095 clean line
  truncated before "box" · t3 95774de9 slurred blend + closed eyes +
  detached tail "Box" in a different shot · t4 47237b0b "Inside the
  porta ×2 + held box" but NO "festival" (G7 PASS 0.8 — not a
  wrong-lyric take — yet unusable for this fix: it would mouth wrong
  words across the song's festival hold).
- Fallback shipped: re-warp of the ORIGINAL s08b-t1 take (sings the
  exact line). Pieces: A take 0–2.42 → f1876–1959 (speed 0.700;
  festival onset lands 81.62, exact) · B take 2.42–3.40 → f1959–2006
  (speed 0.5004 — the festival stretched at the 2.0x cap edge; hold
  now 1.96s vs the song's 2.34s and v1's 1.21s) · C take 3.40–4.70 →
  f2006–2047 (speed 0.761) · D take 4.70–6.20 → f2047–2083 (1.000).
- MEASURED: Box onset lands at f2006 = 83.58s → error −0.38s
  (v1: −1.60s). INSIDE ±0.5s. All speeds ≥0.5004 (inside the 2x cap).
  GATE: PASS, with the method disclosed — the audit's proposed means
  (a pacing replacement take) was tried 4 times and failed; the gate
  is met by the fallback with the correct words on the mouth
  throughout. Nit: the take's articulation is soft/smug (see visual
  gate) — the same performance the approved master carries, re-timed.

### Fix 2 — S11a uphill water — PASS
Named gate: full-res eye read — water runs uphill.
- Fire 1 (17be8416) REJECTED: tap pours DOWN in every sampled frame.
- Fire 2 (b5d6940c) SHIPPED: a fountain column erupts UP out of the
  basin past his hands/face for the whole take (eye reads at take
  t1.5/3.5/5.5/7.0 + master t110.0/112.5). Assembly window take
  1.00–6.375 → f2625–2754 @1.000x. Event shipped: 3.3 Reverse-Time
  Rebuild. GATE: PASS.
- NIT (disclosed): two thin tap trickles still pour down at
  frame-left in the wider frames. The scene's water EVENT — the
  fountain at his hands — runs up; v1's take had NO upward water.
- G7: mechanical REJECT (overlap 0.0) recorded as NOT APPLICABLE —
  the take is a by-design wordless montage cover (mouth closed; its
  ASR hears only an "Ugh." at 8.32s, p=0.384, outside the used
  window; take audio is discarded at assembly). The scene's line is
  carried by the visual + kinetic HIGHLIGHT, as designed in v1.

### Fix 3 — S06 / S15 optional takes — NOT FIRED (no volley room)
The 6-generation cap went to the two priority fixes (S08b ×4,
S11a ×2), per the brief's priority order ("only if 1–2 land clean
first" — S08b never landed clean). S06 keeps v1's take (line-
doubling/fence-tilt still not visible; glow+look+grass carry it,
as disclosed in v1). S15 keeps v1's take (CUT 3 door-swing still
not a distinct cut, as disclosed in v1). Both items stay open for
a future volley.

### Fix 4 — S12a pair-drift re-warp — PASS
Named gate: pair onsets within ±0.5s of song times.
Per-pair pieces (splits in the take's inter-pair gaps, mouth closed):
take 0–1.84 → f2901–2948 (speed 0.940) · take 1.84–3.70 → f2948–3036
(0.507) · take 3.70–5.20 → f3036–3106 (0.514). All inside the cap.
MEASURED pair onsets on the render: pair 1 = 120.86 (exact, was
exact) · pair 2 = 122.91 vs song 122.82 → +0.09s (was +1.13s) ·
pair 3 = 126.58 vs song 126.50 → +0.08s (was +0.50s). GATE: PASS.
Master frame at 122.9s confirms the mouth at the pair-2 attack.
The span's overall 1.64x slow is unchanged (audit: ACCEPT); only
its distribution across pairs changed.

### Fix 5 — S12b kinetic on stem times — PASS
Named gate: kinetic words within ±0.25s of stem word times; double-
backslash audit 0 hits; full-res burned-frame reads.
- Measurement: MDX Voc_FT stem of 128–152s (work/q7/span_vocals.wav)
  + faster-whisper large-v3-turbo int8, NO VAD, raw + screened;
  mix ASR cross-check; stem/mix RMS curves. The song sings NOTHING
  resolvable 134.42–141.56 (stem vocal RMS ≈0.000 at 137.00–141.75;
  mix ASR silent 129.86–141.30). v1 captioned 3 take-timed "Need to
  go" pairs across that span — removed.
- Rebuilt L16 (SLAM) on measured times (sheet labels, positional
  collapse as house doctrine): Porta 141.56–142.70 · potty 142.70–
  143.04 · line 143.04–143.40 · Need 143.40–143.66 · to 143.66–
  143.78 · go, 143.78–144.28 · Need 144.38–144.76 · to 144.76–
  144.92 · go 144.92–145.40. Every word sits ON its measured time
  (error 0.00 by construction; the underlying measurement carries
  ±0.05–0.15s ASR jitter, inside the ±0.25s gate). Provenance: words
  1–6 from the STEM (mix agrees ≤0.04s); pair 2 (words 7–9) from the
  MIX — the stem partially ate it (stem RMS dips 144.25–145.00) while
  the mix hears it at p=0.90/1.00/1.00. Logged, not hidden.
- .ass diff vs v1: 343 events both; changes confined to L16's 13
  events + L15's held "Need" caption extending 134.40→134.87 (the
  emit caps at next-line start; disclosed — and truer: the stem
  shows the held need decaying to ~136.8s).
- Double-backslash audit on mv9_kinetic_v2.ass: 0 hits. Burned-frame
  reads on the master: t138.0 NO caption (correct silence) · t142.2
  "Porta" · t143.5 "Need" · t144.6 "Need" (pair 2) — all clean, no
  bleed into L17a (the MV-13 v1 "goty" class does not recur).
  GATE: PASS.
- DISCLOSED consequence: the S12b TAKE still chants 3 pairs visually
  across the block; during 137–141.8 its mouths chant over the
  song's vocal-silent break (master t138.0 read confirms). Fix 5 is
  kinetic-only per the brief; a visual re-fire for S12b is a future
  item (Q16 family) if the user wants it.

### Fix 6 — S04b chant tail — PARTIAL (re-cut shipped, pair count cannot match)
Named gate (audit): pair count matches the song's 4.
- Measured: the song sings 4 hold onsets in the phrase-2 window
  (40.62/41.76/42.44/43.60); the take sings exactly 2 pairs and its
  full 10s tail was ASR'd — NO further pairs exist after 8.06s.
  Four pairs cannot be shown without frame reuse (banned) or
  generation (out of fix-6 scope). The count gate is therefore
  UNMEETABLE by re-cut; what the re-cut fixes is the PHASE error.
- Shipped re-cut: piece take 5.38–8.06 → f975–1043 ("Gotta" exact
  at 40.62; take pair 2 lands 42.25, −0.19s vs song pair C 42.44;
  the piece ends EXACTLY at pair C's "it," end, 43.46 — v1 drifted
  ~1 word out of phase by the phrase end) + 11f cutaway from the
  take's own UNUSED tail (take 8.10–8.56 → f1043–1054; post-line
  grin settling, not articulating — eye-verified) covering
  43.46–43.90. Song pair D (43.60) plays over the cutaway, and its
  "it," (43.90–45.24) over S05's chant montage, as in v1.
  GATE: PARTIAL — phase error eliminated; pair count 2-shown vs
  4-sung stands disclosed.
