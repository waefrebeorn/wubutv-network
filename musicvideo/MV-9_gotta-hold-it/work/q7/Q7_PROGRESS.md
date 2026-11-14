# MV-9 Q7 FIX BUILD — PROGRESS (coordinator: mv9-q7-fix)

Target: NEW v2 master `masters/mv9_gotta_hold_it_16x9_v2.mp4` + chat copy
`mv9_gotta_hold_it_16x9_v2_chat.mp4`. The APPROVED master
(`masters/mv9_gotta_hold_it_16x9.mp4`, md5 7eee36c4a381c3a86f9c2fa8ea430108)
is NEVER overwritten. No delivered flag, no commit — parent verifies/delivers.
Audit: research_notes/mv-improvement-program-2026-11-12/program.md §MV-9.

Pipeline (v1, reused): work/assembly_build.py (frame-indexed pieces →
CRF-14 segments, contracts sum 4416f) → work/build_kinetic.py (.ass) →
work/split_encode.py (two CRF-18 halves, split f2083) → work/mux.py →
work/gate_master.py. Q7 works in work/q7/ with v2 script copies so v1
intermediates stay untouched.

## Measured anchors (2026-11-13, this build)
- SONG S08b span: Inside,@78.16 | inside@79.46 | the@80.54 | portal,@81.00 |
  festival@81.62–83.96 (2.34s HOLD) | box@83.96–85.28.
- OLD s08b take: Festival@2.42–3.40 (0.98s), Box onset@3.40 → mapped 82.36,
  leads song box onset (83.96) by 1.60s. Confirmed the audit.
- SONG S12a pairs (Need onsets): 120.86 / 122.82 / 126.50 (long held "need"s:
  122.82–125.60, 126.50–129.22). TAKE s12a-t2 pairs: 0.00 / 1.88 / 3.74.
  V1 uniform map: pair2 123.95 (+1.13), pair3 127.00 (+0.50). Confirmed.
- S12b song block 134.42–145.72: mix ASR collapsed to one "to" — stem
  measurement owed (fix 5).
- S04b: song holds in phrase-2 window: 40.62 / 41.76 / 42.44 / 43.60 (4 pairs,
  last "it," runs 43.90–45.24 into S05's span). Take s04b sings 2 pairs
  (Gotta@5.38, hold@5.80, hold@6.92, ends 8.06). FULL-TAIL ASR of the 10s
  take (7.5–10.0s) run 2026-11-13: NO further words after 8.08 — the take
  has exactly 2 pairs; 4 cannot be manufactured without frame reuse
  (banned) or generation (out of fix-6 scope). PLAN: re-cut phrase 2 —
  piece take 5.38–8.06 → song 40.62–43.46 (gotta exact; pair2 lands 42.25,
  0.19s before song pair C 42.44; end exact at pair C's "it," end 43.46),
  then an 11f mouth-closed cutaway from the take's own UNUSED tail
  (8.08–8.54) covers 43.46–43.90. Pair D (43.60) plays over the cutaway —
  DISCLOSED. Gate: PARTIAL by construction (see gate log).

## Fix plan
1. S08b replacement take (GEN): sing "Inside the porta, festival box" with
   "festival" HELD ~2.3s. Event: 2.4 The Room Shrinks (porta walls breathe
   in on the held note; unused in USED_EVENTS). Pieces (song frames):
   A take[0..fest_onset] → f1876–1959 (78.16–81.62);
   B take[fest_onset..box_end] → f1959–2047 (81.62–85.28);
   C tail → f2047–2083 (85.28–86.80). GATE: Box onset within ±0.5s of 83.96.
2. S11a replacement take (GEN): water runs UPHILL. Event: 3.3 Reverse-Time
   Rebuild (stream climbs back into the tap; unused in USED_EVENTS).
   Montage slot, mouth closed; piece take window → f2625–2754 natural-ish.
   GATE: full-res eye read — water runs uphill.
3. OPTIONAL GEN (only if 1–2 land clean): S06 world-tilt take (event 6.6
   The World Rotates + doubled line); S15 door-swing take (event 11.5
   The Door Reveal — door swings shut as a distinct cut).
4. S12a re-warp (reassembly): pieces take 0–1.84 → f2901–2948 (speed 0.940),
   take 1.84–3.70 → f2948–3036 (0.507), take 3.70–5.20 → f3036–3106 (0.514).
   Splits sit in the take's inter-pair gaps (mouth closed). Predicted pair
   onsets: 120.86 exact / 122.91 (+0.09) / 126.58 (+0.08). GATE: ±0.5s.
   The 1.64x overall span warp stays (audit: ACCEPT; per-pair distribution
   is the fix). Gap-cover piece (take 6.94–10.00 → f3106–3226) unchanged.
5. S12b kinetic on stem times: MDX Voc_FT stem of the 128–152s span →
   faster-whisper (large-v3-turbo int8, threads=2, NO VAD) → true song
   word times in 134.42–145.72 → rebuild L16 in the .ass on stem times.
   GATE: kinetic words within ±0.25s of stem times; double-backslash
   audit 0 hits; full-res burned-frame reads.
6. S04b re-cut: see Measured anchors. Disclose either way.

## Volley outcome (6/6 cap spent: S08b ×4, S11a ×2 — S06/S15 optionals
## got NO slots; the cap went to the two priority fixes. Disclosed.)
- S08b fire 1 (q7-t1, a593b29f): REJECT — "port-a-sai" garble, 1.6s gap,
  shouted FESTIVAL (1.40s), NO "box".
- S08b fire 2 (q7-t2, 6bf2d095): REJECT — clean "Inside the Port-A-
  Festival" (festival 1.14s) but the line ENDS at festival; NO "box".
- S08b fire 3 (q7-t3, 95774de9): REJECT — "Portafestival" slur 2.02–6.06
  with eyes closed + non-articulating smile; detached "Box"@7.98 in a
  different, tighter shot with an "oo" pucker. Not assemblable.
- S08b fire 4 (q7-t4, 47237b0b): REJECT for the fix — sings "Inside the
  porta, inside the porta, box." (matches the song's performed doubling,
  and "box" is held 4.50–7.30) but contains NO "festival" at all;
  shipping it would mouth wrong words across the song's festival hold.
- => FIX 1 FALLBACK (reassembly, decided 2026-11-13): cap-edge re-warp
  of the ORIGINAL s08b-t1 take (which sings the exact line). Pieces:
  A take 0–2.42 → f1876–1959 (speed 0.700; festival onset lands 81.62
  exact); B take 2.42–3.40 → f1959–2006 (speed 0.5005 — festival held
  at the 2.0x cap edge, 1.96s vs song's 2.34s); C take 3.40–4.70 →
  f2006–2047 (speed 0.761; BOX onset lands 83.58 = −0.38s, INSIDE the
  ±0.5s gate; box end lands 85.28 exact); D take 4.70–6.20 → f2047–2083
  (speed 1.000, natural tail). Gate PASSES on its named terms with the
  correct words on the mouth throughout; the generation route failed
  4× and that is recorded, not hidden.
- S11a fire 1 (q7-t1, 17be8416): REJECT — tap pours DOWN in every
  sampled frame; only a transient jet off the phone (~3.5s) runs up.
- S11a fire 2 (q7-t2, b5d6940c): KEEP — a fountain column erupts UP
  out of the basin past his hands/face for the whole take (eye reads
  t1.5/3.5/5.5/7.0, one continuous push-in); dispensers plain (droplet
  pictogram, no lettering); mouth closed; crowd adults, hazy. NIT
  (disclosed): two thin tap trickles still pour down at frame-left —
  the fountain is the scene's water event and it runs UP. Assembly
  window: take 1.00–6.375 → f2625–2754 @1.00x. Event shipped:
  3.3 Reverse-Time Rebuild.

## S12b stem adjudication (fix 5) — MEASURED, changes the picture
- MDX Voc_FT stem of 128–152s + faster-whisper (raw + screened) + mix
  raw ASR + stem/mix RMS curves (work/q7/stem_words_raw.json,
  stem_words_128_152.json). FINDINGS: stem vocal RMS strong 129–136.75,
  then ~ZERO 137.00–141.75 (the song sings NOTHING resolvable there —
  the mix ASR agrees: no words 129.86–141.30; the famous 11.3s "to" was
  a whisper smear across a chant tail + a silent gap). Real words in
  the block: "Porta potty line" (stem For@141.56/the@142.40/party@
  142.70/line@143.04; mix agrees, "Pour" onset fuzzy 141.30–141.56),
  "Need to go" pair 1 (143.40, both agree), pair 2 (mix need@144.38
  p=0.90/to p=1.00/go p=1.00; stem partially ate it — stem RMS dips
  144.25–145.0 — times taken from mix, provenance logged).
- NEW L16 (SLAM, stem times, sheet labels, positional collapse as in
  build_kinetic): Porta 141.56–142.70, potty 142.70–143.04, line
  143.04–143.40, Need 143.40–143.66, to 143.66–143.78, go 143.78–
  144.28, Need 144.38–144.76, to 144.76–144.92, go 144.92–145.40.
  NO caption 134.42–141.56 (song sings nothing there; v1 captioned 3
  take-timed "Need to go" pairs across it — that was the flaw).
- DISCLOSED consequence: the S12b TAKE still chants 3 pairs visually
  across 134.42–145.72 (fix 5 is kinetic-only per the brief); during
  137–141.8 its mouths chant over a vocal-silent break. Flagged for
  the parent/user as a possible future visual re-fire (Q16 family).

## Stage log
- 2026-11-13 ~06:37 EST: intake read (program.md §MV-9, MV9_PROGRESS,
  LYRIC_TIMELINE, assembly_build/build_kinetic/split_encode/mux/gate
  scripts, assembly_notes, vehicles s06/s08b/s11a/s15, CHARACTER_LOCK).
  Measurements above locked. Volley design in progress.
- 2026-11-13 ~07:05 EST: stem separation + all ASRs done; volley
  complete (6/6); fix decisions locked (above). Build scripts next.
- 2026-11-13 ~07:20 EST: assembly_build_v2.py --analyze CLEAN (4416f,
  0 cap violations; slowest piece = S08b festival at speed 0.5004).
  Segments built: S04 (5d137b78), S08 (ea3cf87a), S11 (d774acc6),
  S12 (0a727a7a) — all at contract frames; the other 11 segments are
  BYTE-IDENTICAL copies of v1's (md5-verified against v1 manifest).
- 2026-11-13 ~07:25 EST: build_kinetic_v2.py run — 343 events, same
  count as v1; event diff vs v1 confined to L16 (13 events replaced)
  + L15's held "Need" caption extending 134.40→134.87 (emit caps at
  next-line start; L16 now starts 141.56 — disclosed, and truer: the
  stem shows the held need decaying to ~136.8). Double-backslash
  audit on mv9_kinetic_v2.ass: 0 hits.
- G7 records: s11a-q7t2 mechanical REJECT (overlap 0.0) — NOT
  APPLICABLE by design: wordless montage take (ASR hears only an
  "Ugh." grunt at 8.32, p=0.384, outside the used window; take audio
  is discarded at assembly; mouth closed throughout). s08b-q7t4 G7
  PASS (0.8) but rejected for the fix (no festival) — G7 pass is not
  fix pass; both facts logged in GATE_LOG_Q7.md.
- Split encode running.
- 2026-11-13 ~08:35 EST: split encode OK (2083f + 2333f; .ass split
  149/195 events, same as v1). Mux done: v2 house master md5
  345e658bea3c72dbcd6f89675c1390b4 (148,935,360 B, 4416f).
  gate_master.py: ALL GATES PASS (SEI crf=18.0 both halves,
  faststart moov@36, audio agreement min 0.9974 @175s — identical to
  v1's min, same encode path; the ≥0.998 shorthand does not hold at
  that one window and is reported exactly in the gate log).
- Motion audit: 1fps mean 42.51 / min 3.79 / median 39.61, no frozen
  seconds; festival-span + cutaway fine probes clean.
- Visual gate reads done on the master (work/q7/frames/master/):
  S08b 82.6/83.7, S11a 110.0, S12a 122.9, S12b 138.0/142.2/144.6,
  S04b 43.7 — all as designed; disclosures in VISUAL_GATE_Q7.md.
- Chat copy: mv9_gotta_hold_it_16x9_v2_chat.mp4 md5
  887c36a748d3d8cd19b55f4d330cbb1e, 43,208,222 B, 4416f, AAC copied
  (audio stream md5 identical to house master).
- Docs written: GATE_LOG_Q7.md, VISUAL_GATE_Q7.md (work/q7/);
  TAKE_LEDGER + assembly_notes + MV9_PROGRESS Q7 sections appended;
  USED_EVENTS.md gained the MV-9 v2 entry (S11a 3.3 shipped).
- BUILD COMPLETE. No delivered flag, no commit — parent verifies,
  flags, commits, delivers. Registry: mv9-q7-fix.
