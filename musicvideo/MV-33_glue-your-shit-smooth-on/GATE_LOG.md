# MV-33 GATE LOG — Assembly (2026-11-24)

"Glue Your Shit Smooth On, It Is Not Over" — THE ROCOCO RESTAGE.
Assembly coordinator build from the 30/30 KEEP takes. Method: take-audio
forced alignment (each take's own performed word timings), chunk before
warp, capped-QP warp renderer ONLY (MV-30 fix2 lineage; endpoint-exact
PCHIP retired), one assembly pass owning work/joined.mp4.

## Master

- File: `masters/mv33_glue-your-shit-smooth-on_16x9.mp4`
- md5 `9d2fb5c61089b9ac2eed75b3e47f17a1`, 131,524,332 bytes
- Probe (end to end, post-encode): h264 1280×720 24 fps, **4743 frames**;
  AAC 48 kHz stereo from track.mp3 (sole master audio, muxed as AAC);
  mov_text subtitle track, **66 cues**; duration 197.625 s; faststart
  (moov in first 200 KB) ✓
- Chat copy: `masters/mv33_glue-your-shit-smooth-on_16x9_50mb.mp4`,
  md5 `2513537d8c78e947150a6a0e0ac8e905`, 37,120,990 bytes (≤50 MB;
  bitrate-capped video encode, audio + subtitles copied)
- Joined intermediate: `work/joined.mp4` probed BEFORE the encode —
  4743 frames, 197.623 s vs the 197.611 s track (+12 ms container
  rounding) ✓. Single uninterrupted master encode; master re-probed
  end to end after.

## Gate 1 — Warp-slope histogram (PRE-ENCODE STRUCTURAL GATE): PASS

17,505 derivative samples across all 46 render maps (capped-QP maps and
constant-ratio cover/plain maps): **min 0.500, max 2.000, out-of-cap 0.**

| bin | samples |
|---|---|
| 0.50–0.60 | 4,089 |
| 0.60–0.70 | 1,755 |
| 0.70–0.80 | 1,147 |
| 0.80–0.90 | 1,348 |
| 0.90–1.00 | 1,521 |
| 1.00–1.10 | 959 |
| 1.10–1.25 | 1,510 |
| 1.25–1.50 | 766 |
| 1.50–1.75 | 414 |
| 1.75–2.00 | 1,034 |

Per-frame realized ratios in every segment render log also stayed
inside [0.500, 2.000] (work/assembly/maps/seg*_render.json).

## Gate 2 — Pacing law (measured on the final segment plan): PASS

46 edit units, 4743 frames (197.625 s). **Median shot 4.1 s, mean
4.3 s** (both ≥2.5 s). Sub-1 s shots: **2**, both named hits — seg08
S05b-c1 0.88 s (S05a tail beat into the doublet cover) and seg40
S25-c2 0.75 s (the take's inter-line breath beat inside the S25
doublet cover). Sub-0.5 s: **0**. Densest 30 s window: ~9 units
(≤15). One shot per sung line; warp sub-segments are render units
inside their line's shot; covers counted toward every cap.

## Gate 3 — Context rhythm (realized, from the render logs)

264 paired sung words measured at their realized output frames
(work/assembly/rhythm_table.json carries the full per-word table):

- **202 / 264 within ±120 ms** of the song onset
- **238 / 264 within ±250 ms**
- **210 / 264 land inside their song beat cell** (grid 115.0 BPM,
  period 0.5217 s, phase 0.27 s)

Worst 15 realized residuals — every one is a named, explained class
(see Disclosed residuals below):

| seg | word | song onset | error (ms) | in beat cell |
|---|---|---|---|---|
| 34 | is | 143.46 | +998 | no |
| 45 | on | 185.92 | -837 | no |
| 24 | is | 105.22 | +738 | no |
| 05 | glue | 23.54 | -665 | no |
| 34 | not | 144.16 | +507 | no |
| 24 | not | 105.60 | +483 | no |
| 20 | advised | 88.06 | -477 | no |
| 42 | is | 174.78 | +470 | no |
| 29 | the | 127.96 | +457 | no |
| 29 | your | 126.84 | +452 | no |
| 38 | it | 160.18 | -430 | no |
| 29 | cold, | 128.12 | +422 | yes |
| 05 | Smooth | 25.00 | +417 | no |
| 04 | coal | 13.64 | -390 | no |
| 26 | then | 120.46 | -377 | no |

## Gate 4 — CRF 18 proof (size differential; SEI never cited)

Same joined file, same filter chain: master (CRF 18, with audio)
131,524,332 B vs CRF-23 twin (video only) 69,069,828 B =
**1.904× differential** — CRF 18 proven. (This VM's ffmpeg stamps
crf=23.0 in the x264 SEI regardless of the requested rate control;
the differential is the valid proof, per the standing anomaly note.)

## Gate 5 — HUANG EXPRESSION LAW (S04): PASS

Take QC (V-09) recorded the Factor grave, mouth closed throughout,
never smiles, does not sing. Assembly's own eye check on the
extracted frames agrees: f_0024 (1.0 s, inside the sung span) —
mouth closed, grave, no smile; f_0072 (3.0 s) — the Factor from
behind at the doors (departure beat), face not visible. No breach
inside any sung span.

## Cover ledger (designed covers — never hero lines; picture only,
the doublet's words are sung by the track audio regardless)

| span (song) | line | picture source |
|---|---|---|
| 39.08–39.96 | S05b doublet L5 (piece 1) | S05a's own tail, take 4.45–5.00 (r≈1.59) |
| 39.96–42.76 | S05b doublet L6 (piece 2) | S02's performed tail, take 8.10–10.00 (r≈1.47) — the run-11 S02-tail precedent class |
| 67.90–71.97 | S11-scene doublet (L20–L21 span) | S11 take's post-line salute hold, take 6.85–10.00 (r≈1.29) — the take's flagged cover picture |
| 95.24–98.16 | S15-scene doublet (L28–L29 span) | S15 take's own excised wordless gap, take 1.85–5.00 (r≈0.93) — the take compressed the span out of its sung lines; the gap frames are the scene's own flagged picture (V-47), ledgered choice per the brief |
| 122.40–126.60 | S19-scene doublet (L41–L42 span) | S19 take's excised inter-line gap (4.42–6.22) + end-state bow-wave hold (8.46–10.00), r≈1.25 — the take's flagged bow-wave picture |
| 137.12–138.58 | Breakdown L4 "It is not over" | S20 take's chin-up hold tail, take 8.44–9.86 (r≈1.03) — inside S20's own span, per the brief |
| 138.58–140.12 | Breakdown L5 doublet (inferred) | S21 take's opening picture, take 0.00–1.06 (r≈0.68) — the take's flagged cover picture |
| 167.64–171.94 | S25-scene doublet (L59–L60 span) | S25 take's three wordless pieces: ovation head (0–0.78, r≈1.82), inter-line breath (4.48–4.90, r≈1.79 — the named sub-1 s hit), seated-court tail (8.85–10.00, r≈1.88) — the take's flagged ovation frames |

S05b's rejected paraphrase take (md5 `8329d906…`) was never used as
a sung take. Rejected takes S14 t1, S23 t1 were never used anywhere.

## Assembly adjudications (from the takes' own audio)

1. **S08 (HERO hook occ. 1) — modelled FA, disclosed.** ASR hears one
   5-word stream (repeat suppression), but the take's 100 ms RMS
   envelope shows two vocal bursts (0.3–1.75 s, 2.05–3.4 s) — both
   hook passes performed (V-07). Anchors modelled per pass:
   take [0.00, 1.85] → L14, [1.95, 3.45] → L15, seam anchor
   (1.95 → 57.80), per-pass word anchors proportional to the song
   lines' relative onsets at the bursts' measured scale. Realized
   worst +78 ms class — the model held.
2. **S26 L2 — distil checkpoint wins.** Large-v3's "It" at 3.78 s
   rides L1's reverb tail (RMS at ambient 4.4–6.9 s); distil's L2
   set matches the energy rise at 6.9 s. Scene rendered as two
   sub-segments split at the take's silent gap.
3. **S13 — paired from distil-large-v3 wholesale.** Large-v3's
   L24→L25 chunks are infeasible (0.39 / 2.88 — its "the" token
   absorbs the inter-line pause); distil's reads are uniformly
   feasible and the texts agree verbatim. Realized worst −105 ms.
4. **S12 — chunk-start 3.00 s** per the brief (clean pass 3.00–6.04;
   the false start at 1.14–2.90 is never shown).
5. **S27-A — performed pickup "And" trimmed at the chunk head**
   (render starts at take 0.06; the line's "Glue" onset is 0.10).
6. **S24 — centre-crop per parent ruling** (1152×768 → crop
   1152:648:0:60 → scale 1280×720 at conform; spot-checked on the
   master at t=163 — composition intact, nothing lost).
7. **Gap excisions (chunk-before-warp):** S15's wordless gap and
   S19's inter-line gap were excised at word edges and re-used as
   their scenes' doublet cover pictures; S23's 2.69 s inter-pass
   breath excised at the line boundary.
8. **Carried words:** only inside ≥1.0 s sustain-merge clusters
   (S16 is/not, S19b is, S21 is/not, S25 L62 is/not, S17 to) — the
   take sustains one token across the next word's space, so those
   words ride the map between their anchored neighbours.

## Chunk map (46 edit units; full machine record in
work/assembly/segment_plan.json + maps/)

| # | scene | kind | take | take span (s) | song span (s) | frames | method |
|---|---|---|---|---|---|---|---|
| 01 | S01-A1 | PLAIN | mv33_s01_a1_t1.mp4 | 0.00–4.21 | 0.00–4.21 | 101 | constant-ratio |
| 02 | S01-A2 | PLAIN | mv33_s01_a2_t1.mp4 | 0.00–4.21 | 4.21–8.42 | 101 | constant-ratio |
| 03 | S01-B | PLAIN | mv33_s01_b_t1.mp4 | 0.00–4.22 | 8.42–12.62 | 101 | constant-ratio |
| 04 | S02 | WARP | mv33_s02_t1.mp4 | 0.00–9.60 | 12.62–21.71 | 218 | capped warp |
| 05 | S03 | WARP | mv33_s03_t1.mp4 | 1.45–6.87 | 21.71–30.08 | 201 | capped warp |
| 06 | S04 | WARP | mv33_s04_t1.mp4 | 0.00–4.30 | 30.08–34.25 | 100 | capped warp |
| 07 | S05a | WARP | mv33_s05a_t1.mp4 | 0.00–4.42 | 34.25–39.08 | 116 | capped warp |
| 08 | S05b-c1 | COVER | mv33_s05a_t1.mp4 | 4.45–5.00 | 39.08–39.96 | 21 | constant-ratio |
| 09 | S05b-c2 | COVER | mv33_s02_t1.mp4 | 8.10–10.00 | 39.96–42.75 | 67 | constant-ratio |
| 10 | S06 | WARP | mv33_s06_t2.mp4 | 0.17–9.59 | 42.75–47.92 | 124 | capped warp |
| 11 | S07 | WARP | mv33_s07_t1.mp4 | 1.93–10.00 | 47.92–55.50 | 182 | capped warp |
| 12 | S08 | WARP | mv33_s08_t1.mp4 | 0.00–3.55 | 55.50–59.71 | 101 | chunk (already in cap) |
| 13 | S09 | WARP | mv33_s09_t1.mp4 | 0.17–3.81 | 59.71–61.71 | 48 | capped warp |
| 14 | S10 | WARP | mv33_s10_t1.mp4 | 0.00–7.87 | 61.71–67.92 | 149 | chunk (already in cap) |
| 15 | S11-cov | COVER | mv33_s11_t1.mp4 | 6.85–10.00 | 67.92–71.96 | 97 | constant-ratio |
| 16 | S11 | WARP | mv33_s11_t1.mp4 | 1.81–6.22 | 71.96–74.17 | 53 | capped warp |
| 17 | S12 | WARP | mv33_s12_t1.mp4 | 2.96–6.10 | 74.17–76.38 | 53 | chunk (already in cap) |
| 18 | S12-tail | PLAIN | mv33_s12_t1.mp4 | 6.10–9.78 | 76.38–79.88 | 84 | constant-ratio |
| 19 | S13 | WARP | mv33_s13_t1.mp4 | 0.00–7.11 | 79.88–86.62 | 162 | capped warp |
| 20 | S14 | WARP | mv33_s14_t2.mp4 | 0.00–10.00 | 86.62–95.25 | 207 | capped warp |
| 21 | S15-cov | COVER | mv33_s15_t2.mp4 | 1.85–5.00 | 95.25–98.17 | 70 | constant-ratio |
| 22 | S15a | WARP | mv33_s15_t2.mp4 | 0.00–1.77 | 98.17–100.00 | 44 | chunk (already in cap) |
| 23 | S15b | WARP | mv33_s15_t2.mp4 | 5.02–8.28 | 100.00–102.46 | 59 | capped warp |
| 24 | S16 | WARP | mv33_s16_t1.mp4 | 0.90–9.75 | 102.46–109.83 | 177 | capped warp |
| 25 | S17 | WARP | mv33_s17_t1.mp4 | 0.30–8.08 | 109.83–116.08 | 150 | chunk (already in cap) |
| 26 | S18 | WARP | mv33_s18_t1.mp4 | 0.00–9.61 | 116.08–122.42 | 152 | capped warp |
| 27 | S19-c1 | COVER | mv33_s19_t1.mp4 | 4.42–6.22 | 122.42–124.67 | 54 | constant-ratio |
| 28 | S19-c2 | COVER | mv33_s19_t1.mp4 | 8.46–10.00 | 124.67–126.58 | 46 | constant-ratio |
| 29 | S19a | WARP | mv33_s19_t1.mp4 | 0.00–4.60 | 126.58–129.00 | 58 | capped warp |
| 30 | S19b | WARP | mv33_s19_t1.mp4 | 6.18–8.59 | 129.00–130.71 | 41 | chunk (already in cap) |
| 31 | S20 | WARP | mv33_s20_t1.mp4 | 0.00–8.44 | 130.71–137.12 | 154 | capped warp |
| 32 | S20-cov | COVER | mv33_s20_t1.mp4 | 8.44–9.86 | 137.12–138.58 | 35 | constant-ratio |
| 33 | S21-cov | COVER | mv33_s21_t1.mp4 | 0.00–1.06 | 138.58–140.12 | 37 | constant-ratio |
| 34 | S21 | WARP | mv33_s21_t1.mp4 | 1.02–10.00 | 140.12–146.67 | 157 | capped warp |
| 35 | S22 | PLAIN | mv33_s22_t1.mp4 | 0.75–9.25 | 146.67–155.17 | 204 | constant-ratio |
| 36 | S23a | WARP | mv33_s23_t2.mp4 | 0.00–2.21 | 155.17–157.12 | 47 | capped warp |
| 37 | S23b | WARP | mv33_s23_t2.mp4 | 4.81–7.54 | 157.12–159.29 | 52 | capped warp |
| 38 | S24 | WARP | mv33_s24_t1.mp4 | 0.00–9.29 | 159.29–167.62 | 200 | capped warp |
| 39 | S25-c1 | COVER | mv33_s25_t1.mp4 | 0.00–0.78 | 167.62–169.04 | 34 | constant-ratio |
| 40 | S25-c2 | COVER | mv33_s25_t1.mp4 | 4.48–4.90 | 169.04–169.79 | 18 | constant-ratio |
| 41 | S25-c3 | COVER | mv33_s25_t1.mp4 | 8.85–10.00 | 169.79–171.96 | 52 | constant-ratio |
| 42 | S25 | WARP | mv33_s25_t1.mp4 | 0.74–8.80 | 171.96–176.29 | 104 | capped warp |
| 43 | S26a | WARP | mv33_s26_t1.mp4 | 0.00–3.70 | 176.29–179.17 | 69 | capped warp |
| 44 | S26b | WARP | mv33_s26_t1.mp4 | 6.56–8.85 | 179.17–181.62 | 59 | capped warp |
| 45 | S27-A | WARP | mv33_s27_a_t1.mp4 | 0.06–3.20 | 181.62–187.58 | 143 | capped warp |
| 46 | S27-B | PLAIN | mv33_s27_b_t1.mp4 | 0.00–10.00 | 187.58–197.62 | 241 | constant-ratio |

## Subtitles

- mov_text: 66 cues (65 sheet lines + the performed hook repeat after
  L47, captioned per performance) from lyrics.srt.
- Burned-in karaoke ASS: 324 word-step events, header copied verbatim
  from the shipped MV-28 file ([Events] Format includes Layer),
  bottom-center bold white on semi-transparent black bar, current
  word highlighted yellow. Display text is always the sheet
  (lyrics.txt). L49 (ASR-silent inferred doublet) timed by
  syllable-weight split across 138.58–140.12 — the only fallback.
- Spot-checked on the master: t=57.0 (hook, "smooth" highlighted),
  t=163.0 (S24, "on" highlighted), t=190.0 (finale hold, no caption —
  correct, past the last line).

## Disclosed residuals (named, not hidden)

1. **Carried sustain-cluster words** (S21 is +998 / not +507; S16 is
   +738 / not +483; S25 is +470): the takes sustain "It" for
   2.4–2.5 s where the track fires "It is not over" compactly. The
   capped map anchors both phrase edges (It and over land within
   ±115 ms in every case) and runs the cluster at the 0.50 floor;
   the two function words inside the held phrase land late. The
   mouth shape is preserved honestly — the alternative is breaking
   the warp cap, which standing law forbids.
2. **S27-A final "on" −837 ms:** the take sings the last line in
   ~2.5 s against the track's 5.96 s line with its 1.66 s "on"
   sustain; the map runs [1.774, 2.000] and the sustain plays over
   the heart-fold picture. The line's other four words land within
   ±175 ms.
3. **Performance-shape mismatches** the cap cannot close: S03 "glue"
   −665 / "Smooth" +417 (the take's Pray→glue gap is 0.56 s vs the
   song's 1.84 s); S14 "advised" −477; S19a head words ≈ +450
   (late line entry); S02 "coal" −390 (the take snaps "The" in
   0.32 s against the song's 1.0 s sustain); S24 "it" −430; S18
   "then" −377. All are single-word or head-of-line residuals with
   the surrounding anchors tight.
4. **S17 tube label legible "Smooth-On"** — correctly spelled
   diegetic lettering, sanctioned class (parent's call at take QC,
   V-50). S01 takes carry tube-print / "Gilded Seam" inscription
   flags of the same sanctioned class (V-01..V-03).
5. **S08's FA is modelled** (adjudication 1) — disclosed as such;
   realized residuals came out at chunk-method quality.

## Verdict

All structural gates PASS: warp-slope histogram (pre-encode),
pacing, joined probe, master probe, CRF differential, HUANG
EXPRESSION LAW, subtitle spec. The master is shipped to the parent
with the residuals above disclosed. No delivered flag, no delivery,
no commit — those are the parent's.
