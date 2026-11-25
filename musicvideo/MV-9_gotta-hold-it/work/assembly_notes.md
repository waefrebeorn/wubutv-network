# MV-9 "Gotta hold it" — ASSEMBLY NOTES

Track: track.mp4 md5 `bad11958165dea267592643f185a15f8`, 184.0s.
Grid: measured 133 BPM, period 0.451s, phase 0.200s. Plan fully fired:
25 KEEP / 11 REJECT (V1–V7). Master target: `masters/mv9_gotta_hold_it_16x9.mp4`,
frame-exact 184.0s = **4416 frames** @24fps, 1280x720, CRF 18, AAC 48k stereo, faststart.
Method: MV-8 v3 assembly (segments CRF-14 → split-half final encode → capped-apad mux),
adapted. Builder: `work/assembly_build.py`. Kinetic: `work/build_kinetic.py`.

## Word-alignment analysis (measured, not assumed)

Take words from `work/qc/<scene>*/words.json` (all 36 exist, reused as-is — none
corrupt/missing, no Whisper re-run needed); song words from `analysis/SONG_WORDS.json`
(231 words). ASR mishearings (intake-adjudicated, AUDIO_ANALYSIS.md): "line" heard as
"light"; "porta" as "portal"/"pour the"; "Festival porta potty" as "festival party
party". The takes sing the SHEET line; the song's performed words are the sheet
words at the ASR times (positional mapping within each phrase). The plan's line
spans are onset-of-last-word; assembly anchors use last-word END (hence ratios
below differ slightly from the QC's onset-based ratios — same takes, correct ends).

Frame math: scene boundaries = round(song_seconds × 24), cumulative — so every
cut lands on the nearest frame to the true song time and the 15 scene contracts
sum to exactly 4416f. Per-piece warp = uniform over the piece's take window
(phrase-level smooth; per-word data places phrases, never per-word setpts steps).

## Scene treatments (piece list; factor = song_span / take_span; slow cap 2x)

- **S01** 0–340f. S01a-t2 take 0–7.071 (170f, 1.00x; hold starts 7.17s, avoided —
  verified by eye: t7.0 moving, t7.5 frozen). S01b-t2 take 0–2.6 (62f, 0.99x) +
  take 5.2–9.700 (108f, 1.00x); internal jump lands on beat 9.671s (k=21).
  S01b hold 2.67–5.17s skipped per ledger.
- **S02** 340–502f (162f). S02-t1 vocal take 0–4.80 → song 14.18–20.38 (149f,
  1.29x slow). Gap 20.38–20.90 (13f, no words): tail take 4.80–5.00 natural
  (5f) + **8f freeze of the last frame** (wordless window, MV-8 v3 precedent:
  H2-A 3f freeze; disclosed). QC's "slot 5.56s" was onset-of-"bad"; true word
  span 14.18–20.38 = 6.20s.
- **S03** 502–696f (194f). S03-t1. BAD-WORD REPAIR (ledger): extra "hold it"
  pair take 2.24–2.92s. Piece 1 take 0–2.24 → song 20.90–23.06 (51f, 0.95x);
  **16f montage cutaway take 5.76–6.44** (post-vocal tail, moving, mouth
  closed — verified by eye t6.0/7.0/8.0) → song 23.06–23.73 (17f, 1.04x);
  piece 2 take 2.92–5.76 → song 23.73–27.00 (78f, 1.14x) — take "gotta"
  lands song 23.73, 0.13s after the song's "gotta" onset (23.60), inside
  the 0.5s mouth-lead tolerance; take "line" lands 26.38 vs song 26.40.
  Gap cover take 6.44–8.46 → song 27.00–29.02 (48f, 0.99x; tail moves,
  probed mean diff 15.8).
- **S04** 696–1054f (358f). **CORRECTION to the ledger's S04a mapping:** the
  ledger stopped the vocal at take 6.48s, but the take words show "hold"
  6.76–7.12 + "it," 7.12–7.48 BEFORE the stray "line" 7.56–7.98 — the take
  sings the full 15-word line ("…Gotta hold it, hold it") + one stray word,
  matching the song's 15 words 29.02–36.34. So S04a = take 0–7.48 → song
  29.02–36.34 (176f, 0.98x), stray "line" trimmed; NO gap, NO tail piece.
  S04b = phrase-split (swing-keyframe, ledger intent: "'Gotta' lands 5.38s
  in take time vs 4.28s song position — swing-warp compresses the gap"):
  phrase 1 take 0–4.72 → song 36.34–39.98 (88f, 0.78x); gap take 4.72–5.38
  → song 39.98–40.62 (15f, 0.95x); phrase 2 take 5.38–8.06 → song
  40.62–43.90 (79f, 1.23x). "Gotta" lands exactly 40.62. (Ledger's "gap
  compressed to 0.24s" misreads the song gap — the song gap is 39.98–40.62
  = 0.64s, and the take gap 0.66s maps to it at 0.95x.) S04b's chant tail
  runs ~1 word out of phase by the end (take sings 2 "hold it" pairs where
  the song sings 4) — chant, mouth repetitive, disclosed.
- **S05** 1054–1368f (314f). Montage, natural. S05a-t2 take 0–7.714 (185f,
  1.00x; opens with a whip at frame 0, then a ~0.4s wristband hold — montage
  grammar, ledger-blessed). S05b-t1 take 3.96–9.346 (129f, 1.00x; starts
  after the 37f doorway hold 2.42–3.96s). Cut between them on beat 51.614s
  (k=114) — the plan's "~50.45s" is the scene midpoint, not a beat; 51.614
  is the nearest beat that lets S05b run as one continuous post-hold piece.
  DISCLOSED: S05b has a ~10f held blue-door detail shot at take ~6.45–6.87s
  (probed diffs 0.38–0.83, then a hard cut at 6.87s) — a held montage beat,
  same family as S05a's 0.4s hold.
- **S06** 1368–1591f (223f). S06-t1 take 0–9.28 natural (1.00x). Disclosed
  (ledger): line-doubling/fence-tilt beat NOT visible — psychedelic touch
  lands only via glow + look + grass; no re-fire (instrumental cover slot).
- **S07** 1591–1754f (163f). S07-t2 (5.000s, 0 words — visual slot, the song
  line "Door is open now" plays over the door event) uniform 1.36x slow of
  the whole take (in cap, disclosed — door swing in slow motion fits the
  dreamy moment). Door event verified by eye (t2.5: man in the doorway).
- **S08** 1754–2083f (329f). S08a-t1 vocal take 0–5.48 → song 73.10–77.64
  (109f, 0.83x); tail take 5.48–6.00 → song 77.64–78.16 (13f, 1.04x;
  verified moving by eye t5.5/5.9, before the 25f near-dup run at 7.3s).
  S08b-t1 vocal take 0–4.70 → song 78.16–83.96 (139f, 1.23x); tail take
  4.70–7.54 → song 83.96–86.80 (68f, 1.00x) — the tail EXTENDS past the
  scene's nominal end (85.28) to cover the 85.28–86.80 inter-scene gap
  (36f, no song words; the plan leaves it unassigned). Tail motion probed:
  mean diff 16.1, min 5.0 — moving throughout. DISCLOSED: S08b's "Box"
  leads the song by ~1.6s — the song holds "festival" 81.62–83.96 (2.34s)
  while the take's "Festival" is 0.98s; slowing it to match would be 2.39x,
  past the cap. The mouth is correct at "Inside" (78.16), "porta" (81.00),
  "festival" (81.62), and is closing from "Box" at the song's "box" onset
  (83.96).
- **S09** 2083–2442f (359f). S09a-t2 phrase-split (take has a 0.70s gap
  5.14–5.84 between "line" and "Gotta" where the song has 0.08s): phrase 1
  take 0–5.14 → song 86.80–91.25 (107f, 0.87x); phrase 2 take 5.84–7.98 →
  song 91.25–93.66 (58f, 1.13x) — "Gotta" lands 91.25, 0.03s before the
  song's "gotta" (91.28); the 0.70s take gap is cut (hard cut at a phrase
  boundary, mouth closed both sides). Tail take 7.98–8.42 → song 93.66–94.10
  (10f, 0.95x; smile end state, probed moving 19.1). S09b-t2 take 0–7.70 →
  song 94.10–101.74 (184f, 1.00x); extra two "hold it" pairs 7.70–8.78s drop
  with the tail per ledger.
- **S10** 2442–2625f (183f). S10a-t1 take 0–4.83 continuous (115f, 0.99x) —
  includes 4f (0.16s) of the 30f QR-phone hold, within the ledger's ≤0.5s
  sanction. S10b-t1 take 0–2.80 → song 106.56–109.36 (68f, 1.01x).
  **CORRECTION to the ledger's "uses 0–2.1s":** the take is one continuous
  drifting haze shot — frames at 0.5/1.5/2.1/2.8s show no cut, no defect,
  no content change at 2.1s (verified by eye). The full 2.80s span is used
  natural; the 2.1s figure has no visible basis.
- **S11** 2625–2901f (276f). S11a-t2 take 0–5.38 natural (129f, 1.00x);
  S11b-t1 take 0–6.125 natural (147f, 1.00x). Disclosed (ledger): S11a
  water runs DOWN not uphill (one psychedelic beat missed).
- **S12** 2901–3497f (596f). Final chorus, loudest section. S12a-t2 vocal
  take 0–5.20 (first three pairs) → song 120.86–129.40 (205f, **1.64x** —
  just past grey edge 1.60, within 2x cap, disclosed); extra 4th pair
  5.22–6.94s drops. Gap 129.40–134.42 (120f, no segmented song words —
  ASR holds "need" 129.98–134.42, unreliable): cover = S12a tail take
  6.94–10.00 → 120f at **1.63x** slow (crowd builds behind the smiling man,
  verified by eye t7.5/9.0 + probed moving 12.3; mouth closed). S12b-t2
  vocal take 0–7.02 → song 134.42–145.72 (271f, **1.61x** — just past grey
  edge, within cap, disclosed). S12a pair onsets drift (pair 2 +1.13s, pair
  3 +0.50s vs the song's uneven chant spacing) but land inside the song's
  long held "need" words — mouth on the right word, disclosed.
- **S13** 3497–3782f (285f). S13a-t1 vocal take 0–4.84 → song 145.72–150.50
  (115f, 0.99x; "Pull the party light, gotta hold it" ×4). S13b-t2 montage
  take 0.30–7.34 → song 150.50–157.60 (170f, 1.01x; head trimmed 0.3s —
  motion starts ~0.3s, verified by eye: speed lines appear at t0.3–0.5).
  Cut between them at song 150.50 (2f seam absorbed).
- **S14** 3782–4144f (362f). Visual peak, montage, natural. S14a-t1 take
  0–7.666 (184f, 1.00x); S14b-t1 take 0–7.414 (178f, 1.00x); cut between
  them on beat 165.266s (k=366; plan's "~165.14s" is not a beat).
- **S15** 4144–4416f (272f). S15-t2 (10.000s, 0 words, one continuous
  drifting line shot) uniform 1.13x slow of the whole take (disclosed).
  Disclosed (ledger): CUT 3 (door swinging shut) is not a distinct cut;
  other crowd members carry backpacks (ban was on OUR man only).

## No-reuse audit (each KEEP take used once; each frame at most once)

25 KEEP takes, all used; 0 REJECT takes in the cut. S01b-t2 split across its
60f hold (0–2.6 + 5.2–9.7, ledger-sanctioned); S03-t1 reordered around the
bad-word cutaway (frames 0–8.46 each used exactly once, in 4 ranges);
S09a-t2's 0.70s inter-phrase gap frames dropped (not reused); S12a-t2's
extra 4th pair (5.22–6.94) dropped; S09b-t2's extra pairs (7.70–8.78)
dropped; S02's 8f freeze is the take's own last frame (MV-8 v3 precedent,
not a second use). Generated tail speech ("Thanks for watching!",
"Subscribe to the channel!") is audio only — dropped; no take audio is used
as soundtrack (song is sole master audio).

## Kinetic layer (post, .ass — never in-clip text)

`work/build_kinetic.py` from `analysis/SONG_WORDS.json` (231 words) + the
sheet. Per-line presets (plan): HIGHLIGHT default; SLAM on hook hits
("Hold it" 20.90, "Need to go" 29.02 + 36.34 + 86.80 + 94.10 + 120.86 +
134.42, "Lock" 73.10, "Four squares" 158.20); CASCADE on the "Hold it"
chants (S05 45.24–52.00, S06 pickup 63.96–66.26, S13 "hold it" run
150.56–157.60); STACK on the lists (S10 102.16–106.56, S14 158.20–161.52).
Corner bug `~ WuBu ~` bottom-right, full duration (MV-8 v1 form).
Sheet-word corrections applied to ASR labels (times unchanged):
"light"→"line" (idx 24); "pull the party light"→"Porta potty line"
(idx 31–34, 112–115 — chorus only; idx 173–176 KEPT, S13a really sings
"Pull the party light"); "festival party party"→"Festival porta potty"
(idx 46–48, 127–129, 192–194); "portal,"→"porta," (idx 103);
"eating"→"heat" (idx 83); "I've extended near"→"Addicts standing near"
(idx 157–159). S12b block (134.42–145.72): the ASR collapsed the whole
block into one 11.3s "to" — unmeasurable, so the kinetic there follows the
take's warped word times (3 "Need to go" pairs, SLAM on the first), NOT
SONG_WORDS. Disclosed.

## Final encode (MV-8 v3 method)

Segments CRF-14 1280x720 → split-half final encode (video-only CRF 18,
kinetic .ass burned in; split at the S08/S09 boundary, song 86.80s =
frame 2083; half 1 = 2083f, half 2 = 2333f) → mux stream-copies halves +
track audio re-encoded AAC 48k stereo, `-af apad=whole_dur=184.0 -t 184.01`
(NEVER bare apad), faststart → `masters/mv9_gotta_hold_it_16x9.mp4`.
Chat copy ≤50 MB if the house master exceeds it (bitrate-capped re-encode,
AAC copied untouched, faststart).

## Gates (measured on the delivered master)

Exact 4416f; h264 1280x720 24fps; AAC 48k stereo (ffprobe the container);
x264 SEI crf=18.0; faststart (moov early); master-audio agreement vs
track.mp4 (5 windows, corr > 0.99); mouth state at line/hook onsets by eye
on the warped render; motion audit on the final cut. `work/gate_master.py`.

## Build log

- 2026-11-09 ~12:25 EST: assembly chained. Analysis done (take words reused
  from QC, no Whisper re-run). All 25 KEEP takes ffprobe-verified on disk
  (11× 1248x704, 14× 1280x720, all 24fps, 5.000/10.000s). Open gaps
  adjudicated by eye + motion probe (see treatments above).

## Build log
- 2026-11-09 ~12:42 EST: build_kinetic.py run 1 — 25 lines, 232 words, 333 events. CAUGHT: (a) first 4→3 remap deleted the "line," it had just set (L3 showed "light,"); (b) L4/L10/L11 tail words fell outside their windows (end-exclusive); (c) L1/L4/L7/L10/L11/L13/L17/L18/L20 lines >44 chars run off the 1280px frame at fontsize 54 (first word at x=-230).
- 2026-11-09 ~12:45 EST: build_kinetic.py fixed + run 2 — collapse_pull_party() helper (correct start/end per word, deletes the 4th ASR word), windows extended (L4→45.24, L10→94.10, L11→102.16), zero-duration artifact filter (dropped 5: idx 73/74/172/218/219), long HIGHLIGHT/CASCADE lines split into phrase sub-lines, L6 opening "Hold" reconstructed (63.70–63.96), first word of each line capitalized. FINAL: 37 lyric lines, 232 words, 343 events; off-screen check PASS (no negative x; widest lyric word x=1089; 1252 = the ~ WuBu ~ bug). Kinetic .ass at work/assembly/mv9_kinetic.ass.
- 2026-11-09 ~12:47 EST: split/mux/gate scripts written (work/split_encode.py, work/mux.py, work/gate_master.py — adapted from MV-8 v3; split at S08/S09 boundary 86.80s = frame 2083; halves 2083f + 2333f = 4416f).
- 2026-11-09 ~12:48 EST: assembly_build.py RUNNING (background session proc_b5751daf83a3). S01–S04 built + checkpointed by 18:19 UTC; S05.mp4 on disk. Awaiting completion.
- 2026-11-09 ~12:58 EST: assembly_build.py DONE (exit 0, ~9.4 min). All 15 segments ffprobe-verified: manifest frames == disk frames for every scene; TOTAL 4416f exactly. Segment md5s in assembly_manifest.json.
- 2026-11-09 ~13:06 EST: split_encode.py DONE (exit 0, ~6.9 min). Half 1 = 2083f (62,375,559 B), half 2 = 2333f (80,777,367 B). .ass split: part1 149 events, part2 195 events (344 = 343 + straddling ~ WuBu ~ bug in both).
- 2026-11-09 ~13:08 EST: mux.py DONE. Master masters/mv9_gotta_hold_it_16x9.mp4 — 4416f, 147,687,159 B, md5 e1cc0349b6953f4f409207244a5dc5d7.
- 2026-11-09 ~13:09 EST: gate_master.py ALL GATES PASS — h264 1280x720 24fps, 4416f, 184.000s, AAC 48k stereo, SEI crf=18.0 on BOTH halves (2 lines), faststart moov@36, audio agreement min 0.9974 (windows @5/45/90/135/175s, all >0.99).
- 2026-11-09 ~13:15 EST: MOUTH GATE (master, by eye) — 6 onsets checked (S02 need 18.82, S04a Need 29.02, S09a gotta 91.28, S12b need 134.42, S13a Pull 145.74, S15 need 178.64): mouth open at every sung onset; S13a mouth closes briefly between "Pull" and "the" (normal inter-word closure, open again on "light,"). S15 outro plays over the singer's BACK (no visible mouth) — deliberate visual slot per the plan (0-word take), disclosed.
- 2026-11-09 ~13:16 EST: KINETIC DEFECT FOUND on the master — at 145.99s the caption reads "goty": the L16 SLAM line's last word ("go,") sits at full opacity over L17a's "party". ROOT CAUSE: kinetic_ass.py SLAM branch gives the last word an event ending at w.end+0.4 and ignores lend (which the tool caps at next_start-0.02) — it violates the tool's own "never bleed into the next line's window" invariant. 6 back-to-back boundaries affected (L3->L4 36.34, L4->L5 45.24, L8->L9 78.16, L10->L11 94.10, L14->L15 129.98, L16->L17a 145.74). FIX: one-line change in visual-forms/tools/kinetic_ass.py — SLAM last word end = min(w.end+0.4, lend). .ass regenerated; all 6 events now end at next_start-0.02 (36.32, 45.22, 78.14, 94.08, 129.96, 145.72). Master must be re-encoded (halves + mux) — segments unaffected.
- 2026-11-09 ~13:24 EST: split_encode + mux + gates RE-RUN after the kinetic fix. New master md5 7eee36c4a381c3a86f9c2fa8ea430108, 147,677,665 B, 4416f. ALL GATES PASS again (SEI crf=18.0 both halves, faststart moov@36, audio agreement min 0.9974). The first master (md5 e1cc0349...) is SUPERSEDED — it carried the SLAM-bleed kinetic defect; do not deliver it.
- 2026-11-09 ~13:26 EST: KINETIC FIX VERIFIED ON THE NEW MASTER — 145.99s now reads "Pull the party light," clean (no "goty"); 36.50s shows L4 "Need" alone with no overlapping "it". Both fixed boundaries confirmed by eye at full res.
- 2026-11-09 ~13:28 EST: MOTION AUDIT (master, 1fps frame-diff) PASS — 184 frames, mean diff 37.57, min 4.89, median 35.52; NO frozen runs >=1s. Lowest-diff second 4.89 at 57s (instrumental gap — slow but moving).
- 2026-11-09 ~13:30 EST: CHAT COPY made (house 147.7 MB > 50 MB): masters/mv9_gotta_hold_it_16x9_50mb.mp4 — 44,234,154 B, md5 4119ea79c08f57b7831f6899b5b960b5, bitrate-capped 1750k video, AAC copied untouched. VERIFIED: 4416f, h264 1280x720 24fps, 184.000s, AAC 48k stereo, faststart moov@36, audio-stream md5 2c6c7cbc7519a74055fac77b46cabcd4 IDENTICAL to the house master.
- 2026-11-09 ~13:31 EST: ASSEMBLY COMPLETE. House master md5 7eee36c4a381c3a86f9c2fa8ea430108 (147,677,665 B, 4416f, 184.000s). All gates PASS. Disclosed flaws in final report. NO commit, NO delivered flag (parent writes them).

## Q7 FIX BUILD (2026-11-13) — v2 master

Ships as `masters/mv9_gotta_hold_it_16x9_v2.mp4` (md5
345e658bea3c72dbcd6f89675c1390b4, 4416f) + chat copy
`mv9_gotta_hold_it_16x9_v2_chat.mp4` (md5 887c36a748d3d8cd19b55f4d330cbb1e,
43.2 MB, AAC copied — audio stream md5 identical to the house master).
The APPROVED v1 master is untouched; v2 awaits the user's verdict.
Builder: work/q7/assembly_build_v2.py (segments S04/S08/S11/S12 rebuilt;
the other 11 segments are byte-identical copies of v1's, md5-verified).
Kinetic: work/q7/build_kinetic_v2.py → work/q7/assembly/mv9_kinetic_v2.ass.
Full record: work/q7/GATE_LOG_Q7.md + VISUAL_GATE_Q7.md + Q7_PROGRESS.md.

Changes vs v1 (everything else identical):
- **S08b re-warp** (4 fires for a pacing replacement all failed QC —
  ledger above): pieces take 0–2.42 → f1876–1959 (0.700; festival
  onset lands 81.62 exact), take 2.42–3.40 → f1959–2006 (speed
  0.5004 — festival held at the 2.0x cap edge, 1.96s), take 3.40–4.70
  → f2006–2047 (0.761; **Box onset lands 83.58, −0.38s** vs v1's
  −1.60s; box end 85.28 exact), take 4.70–6.20 → f2047–2083 (1.000).
- **S11a replaced** with s11a-q7t2 (fountain erupts UP out of the
  basin; window 1.00–6.375 @1.00x). Nit: thin tap trickles run down.
- **S12a per-pair re-warp**: take 0–1.84 → f2901–2948 (0.940),
  1.84–3.70 → f2948–3036 (0.507), 3.70–5.20 → f3036–3106 (0.514).
  Pair onsets on the render: 120.86 exact / 122.91 (+0.09, was
  +1.13) / 126.58 (+0.08, was +0.50).
- **S12b kinetic rebuilt on MDX-stem word times**: the song sings
  nothing resolvable 134.42–141.56 (stem RMS ≈0 at 137.00–141.75;
  mix ASR silent) — v1's 3 take-timed "Need to go" caption pairs
  removed. New L16: "Porta potty line" 141.56–143.40 + "Need to go"
  ×2 (143.40, 144.38; pair 2 timed from the mix — the stem partially
  ate it, provenance in the gate log). Side effect disclosed: L15's
  held "Need" caption now ends 134.87 (was capped 134.40).
  DISCLOSED: the S12b take still chants visually through the
  song's vocal-silent break — a future visual re-fire candidate.
- **S04b chant-tail re-cut**: phrase 2 take 5.38–8.06 → f975–1043
  (gotta exact 40.62; pair 2 lands 42.25 vs song pair C 42.44; ends
  exactly at pair C's "it," end 43.46 — v1 ended ~1 word out of
  phase) + 11f cutaway from the take's unused tail (8.10–8.56 →
  f1043–1054). The take sings only 2 pairs vs the song's 4
  (full-tail ASR: no more pairs exist) — count mismatch stands
  disclosed; phase error eliminated.
- NOT DONE: S06 doubling/tilt take, S15 door-swing take (volley cap
  spent on the priority fixes). S12a/S12b span warps unchanged
  (1.64x/1.61x overall, audit ACCEPT).
Gates: house gate ALL PASS (audio agreement min 0.9974 @175s —
identical to v1, same encode path; reported exactly). Motion audit
mean 42.51 / min 3.79, no frozen seconds; festival-span and cutaway
fine probes clean.
