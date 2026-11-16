# MV-6 ASSEMBLY NOTES — "Sell the Lemons" · v4 method · ONE 16:9 master
Track: track.mp3 md5 aa7e65560f1b765d156755844eb57aa7 · 228.8s · 152.0 BPM (beat 0.3947s, first beat 0.163s)

## STAGE 1 — SONG ANCHOR TABLE (word-measured; base SONG_WORDS.json + small-model head pass A)
Line onsets (first-word onset) used for segment anchoring. Timeline segment spans were coarse — word onsets govern where they differ (notably V1: L5 onset 31.90 not 32.9; S03/S04 boundary = 31.90).

| Slot | Song onsets (s) | Notes |
|---|---|---|
| Intro line | 2.72 | "Bacon head on the stand…" ends ~5.32 |
| Intro hook #1 | 6.88 | ends ~8.34 |
| Intro hook #2 | 9.92 | ends ~11.60 |
| Intro hook #3 | 15.70 | ends ~18.00 — NO singing take covers it (see Stage 3) |
| V1 L1–L4 | 19.86 · 22.98 · 25.72 · 28.94 | L4 words: Click 28.94, button 29.84, watch 30.00, cash 31.00, climb 31.34–31.70 |
| V1 L5–L8 | 31.90 · 34.82 · 38.02 · 41.14 | section ends 44.2 |
| C1 L1–L4 | 45.00 · 47.50 · 50.58 · 53.78 | L3 lemons ends 53.78 = L4 click onset |
| C1 L5–L8 + tail | 57.02 · 58.44 · 61.04 · 64.36 · tail 67.52 · 70.10 | montage slot (S06) |
| V2 L1–L3 | 73.32 · 76.24 · 80.10 | |
| V2 L4–L6 | 82.58 · 86.02 · 88.90 | Joe line L4 82.58 |
| V2 L7–L8 | 92.06 · 95.14 | ends 98.58 |
| C2 L1–L4 | 98.58 · 100.88 · 104.12 · 107.14 | L3 lemons ends 107.14 = L4 click onset |
| C2 L5–tail | 110.30 · 111.86 · ~113.64 · 117.04 | montage slot (S11) |
| Bridge chants | 121.00 · 124.08 | "Click, sell, upgrade, sell" ×2 — montage (S12) |
| Bridge lines | 126.84 · 129.90 | "Automate…" / "Bacon head dancing…" — montage |
| S13 chants ×4 span | 133.00 · 137.46 · 142.20 (+ phrase onsets 134.32/135.72, 138.98/141.00, 143.40) | STRUCTURAL — montage cover per parent decision 1 |
| V3 L1–L4 | 145.90 · 148.94 · 152.14 · 155.14 | |
| V3 L5–L8 | 158.52 · 160.80 · 163.80 · 166.66 | L8: Sell 166.66–167.94, keep 168.12, high ends 170.46 |
| FC L1–L4 | 173.38 · 176.28 · 179.52 · 182.66 | DSP "Don't stop…" 184.06–185.20 |
| FC mantra | 185.74 · 188.80 · 199.72 · 204.48 (+never-gonna-stop 189.54, 205.52) | montage slot (S17) |
| Outro | BH/sell 218.46 · sell 220.38 · sell 224.70 · sell 226.62 | clicks 212.2–218.46 cover first |

## TAKE INVENTORY (KEEP pool, word tables from QC)
- S02 t1: line 0.00–~2.6, phrases 3.32 / 5.34, words end ~6.9, closed hold tail
- S03 t2: L1 0.00 · L2 2.12 · L3 4.88 · L4 7.78, words end 9.44, tail to 10
- S04 t2: L5 0.00 · L6 2.36 · L7 5.02 · L8 7.46, words end 9.46, tail to 10
- S05 t1: L1 0.00 · L2 2.44 · L3 5.86, words end 7.96, closed hold 8–10 (NO L4 in any hook take — L4s are chant-class → montage+kinetic, prepro S06/S11/S17 design)
- S07 t2: L1 0.00 · L2 3.80 · L3 7.24, words end ~9.4
- S08 t3: L4 0.00 · L5 3.42 · L6 6.24, words end 8.66, tail to 10
- S09 t1: L7 0.90 · L8 5.70, words end 8.92 (pre-vocal jetpack settle 0–0.9)
- S10 t1: L1 0.00 · L2 1.98 · L3 5.60, words end 8.38, tail to 10 (camera drifts — cuts respect moving frame)
- S14 t1: L1 0.00 · L2 2.66 · L3 5.42 · L4 7.86, words end 9.66, tail to 10
- S15 t2: L5 0.00 · L6 2.86 · L7 5.22 · L8-tail keep 7.60, words end 8.9 (L8 HEAD never sung)
- S15 t1 (REJECTED, L8 evidence only): L8 Sell@8.90, keep@9.62, truncated 10.0; signage surrounds subject on all sides at 9.3s frame (left planter signs, right stall placards, "…rld 2" text center-background) — no clean punch-in exists; head-phrase warp would need (168.12−166.66)/(9.62−8.90) = 2.03× > 2× slow cap. BOTH grounds fail → parent decision-2 fallback: montage + kinetic for L8 head 166.66–168.12.
- S16 t1: L1 0.00 · L2 2.64 · L3 5.48, words end 7.84, closed hold tail; raster 1168×640 → upscale in slot
- S18 t1: BH 0.00–1.96 · chant1 3.60 · chant2 6.76, words end ~8.9, set-down in final second
- Plates: S01 t2 (windows 0–2 + 5–10 only), S06 t1 (0–6s only), S11 t1, S12 t1, S17 t1 (mouths closed, QC-verified)

## STAGE 2 — MOUTH-EVENT MAP (4fps face-crop strips read cell-by-cell, work/assembly/strips/; fine 12fps strip for S03 L4)
Mouth onsets (take-time, first visible open after the line's audio onset; ±0.12s):
- S02: line 0.12 · phrase#a 3.37 · phrase#b 5.00 (activity ends ~6.1; closed lemon-raised hold after — maps onto the song's 11.60–15.70 wordless gap ✓)
- S03 t2: L1 0.00 (open at frame 0) · L2 2.00 · L3 4.90 · L4 7.80 — 12fps fine strip CONFIRMS L4 articulates: opens ≈7.82 (Click), 8.23 (button), 8.48–8.65 (watch), 8.82–8.98 (cash/climb); the 4fps strip had under-sampled it. L4 proceeds as a normal sung segment (parent decision 4: least-bad = onset-anchored phrase warp, below).
- S04 t2: L5 0.45 · L6 2.25 · L7 5.15 · L8 7.30 (lags vs take-audio onsets +0.45/−0.11/+0.13/−0.16 — mixed, so mouth onsets govern)
- S05: L1 0.12 · L2 2.44 · L3 5.90 (activity to ~7.9, closed hold 8–10)
- S07 t2: L1 0.40 · L2 3.60 · L3 7.20 (activity to ~9.0)
- S08 t3: L4 0.00 · L5 3.30 · L6 6.20 (face exits crop after ~7.5 as portal fills frame; Joe's mouth closed in all cells where visible + QC full-res)
- S09: L7 1.85 (face not framed until ~1.0 — jetpack settle; first clear open 1.75–2.0) · L8 6.10 (activity sparse in L8 tail, small open at 8.50)
- S10: L1 0.00 (open at 0) · L2 2.40 · L3 5.50 (activity to ~8.3)
- S14: L1 0.15 · L2 2.60 · L3 5.30 · L4 7.60
- S15 t2: L5 0.15 · L6 2.60 · L7 5.40 · L8-tail 7.90 (activity 8.0–8.5 only — brisk tail)
- S16: L1 0.15 · L2 3.00 · L3 5.90 (activity to ~7.9)
- S18: NEAR-STILL throughout — micro-opens at 1.25 / 1.75 / 3.50 only; chant spans show closed smirk (decision-3 handling + disclosure in Stage 5)
- S01 t2: mouth CLOSED in both flagged windows ✓ (window B front-facing from ~6.5; 5.0–6.5 is a head-turn — fine under no-words/kinetic spans)
- S15 t1 L8 head (8.90–9.65): mouth CLOSED in every fine-strip cell → punch-in route dead on mouth grounds as well (third ground; see Stage 1)

## STAGE 3 — SLOT MAP + WARP TABLE (phrase-smooth warps; factor = song span ÷ take span; speed = 1/factor)
Segments tile 0.00–228.80 contiguously. take_in = mouth onset − ~0.12 pre-roll (0 where the onset cell is already open).

| # | Take | in–out | → Song | Factor | Note |
|---|---|---|---|---|---|
| 1 | S01 t2 | 0.00–2.00 | 0.00–2.72 | 1.360 | clicks, empty stand |
| 2 | S02 | 0.12–3.25 | 2.72–6.88 | 1.329 | intro line |
| 3 | S02 | 3.31–4.94 | 6.88–9.92 | 1.865 | hook #1 — DISCLOSE (>1.5× slow) |
| 4 | S02 | 4.94–10.00 | 9.92–15.70 | 1.142 | hook #2 + closed hold over gap |
| 5 | S01 t2 | 5.00–9.16 | 15.70–19.86 | 1.000 | hook #3 = KINETIC over cover (no singing take exists; prepro S01 design carries the intro echo by post type) |
| 6 | S03 t2 | 0.00–2.00 | 19.86–22.98 | 1.560 | L1 — DISCLOSE |
| 7 | S03 t2 | 2.00–4.78 | 22.98–25.72 | 0.986 | L2 |
| 8 | S03 t2 | 4.78–7.66 | 25.72–28.94 | 1.118 | L3 |
| 9 | S03 t2 | 7.66–10.00 | 28.94–31.90 | 1.265 | L4 (decision 4 outcome: fits INSIDE caps once measured against word-level song span 28.94–31.90 = 2.96s and the take's full tail; internal drift ≤0.53s on cash/climb — flagged) |
| 10 | S04 t2 | 0.38–2.13 | 31.90–34.82 | 1.669 | L5 — DISCLOSE |
| 11 | S04 t2 | 2.13–5.03 | 34.82–38.02 | 1.103 | L6 |
| 12 | S04 t2 | 5.03–7.18 | 38.02–41.14 | 1.451 | L7 |
| 13 | S04 t2 | 7.18–10.00 | 41.14–44.20 | 1.085 | L8 |
| 13b | S06 chunk | 0.00–0.79 | 44.20–45.00 | ~1.0 | pre-chorus breath (no words) |
| 14 | S05 | 0.12–2.32 | 45.00–47.50 | 1.136 | C1 L1 |
| 15 | S05 | 2.32–5.78 | 47.50–50.58 | 0.890 | C1 L2 |
| 16 | S05 | 5.78–7.96 | 50.58–53.78 | 1.468 | C1 L3 |
| 17 | S06 chunks ×9 | (see script) | 53.78–73.30 | 0.70–1.00 | C1 L4 + L5–L8 + echo tail — MONTAGE + kinetic (prepro S06 design) |
| 18 | S07 t2 | 0.28–3.48 | 73.32–76.24 | 0.913 | V2 L1 |
| 19 | S07 t2 | 3.48–7.08 | 76.24–80.10 | 1.072 | V2 L2 |
| 20 | S07 t2 | 7.08–9.10 | 80.10–82.58 | 1.228 | V2 L3 (activity-span factor, tail trimmed) |
| 21 | S08 t3 | 0.00–3.18 | 82.58–86.02 | 1.082 | V2 L4 (Joe line) |
| 22 | S08 t3 | 3.18–6.08 | 86.02–88.90 | 0.993 | V2 L5 |
| 23 | S08 t3 | 6.08–10.00 | 88.90–92.06 | 0.806 | V2 L6 |
| 24 | S09 | 1.73–5.98 | 92.06–95.14 | 0.725 | V2 L7 (speed 1.38×) |
| 25 | S09 | 5.98–10.00 | 95.14–98.58 | 0.856 | V2 L8 |
| 26 | S10 | 0.00–2.28 | 98.58–100.88 | 1.009 | C2 L1 |
| 27 | S10 | 2.28–5.38 | 100.88–104.12 | 1.045 | C2 L2 |
| 28 | S10 | 5.38–8.48 | 104.12–107.14 | 0.974 | C2 L3 |
| 29 | S11 chunks ×5 | (see script) | 107.14–121.00 | 0.75–0.93 | C2 L4–tail — MONTAGE + kinetic |
| 30 | S12 chunks ×5 | (see script) | 121.00–133.00 | 0.88–1.12 | bridge chants+lines — MONTAGE + kinetic (rap rule) |
| 31 | S12/S17/S11 chunks ×6 | (see script) | 133.00–145.90 | ~1.0 | S13 STRUCTURAL cover (decision 1) + breath tail to 145.90 |
| 32 | S14 | 0.03–2.48 | 145.90–148.94 | 1.241 | V3 L1 |
| 33 | S14 | 2.48–5.18 | 148.94–152.14 | 1.185 | V3 L2 |
| 34 | S14 | 5.18–7.48 | 152.14–155.14 | 1.304 | V3 L3 |
| 35 | S14 | 7.48–10.00 | 155.14–158.52 | 1.341 | V3 L4 |
| 36 | S15 t2 | 0.03–2.48 | 158.52–160.80 | 0.931 | V3 L5 |
| 37 | S15 t2 | 2.48–5.28 | 160.80–163.80 | 1.071 | V3 L6 |
| 38 | S15 t2 | 5.28–7.90 | 163.80–166.66 | 1.092 | V3 L7 |
| 39 | S12 chunk | 2.00–3.46 | 166.66–168.12 | ~1.0 | V3 L8 HEAD — montage + kinetic (decision 2 fallback; machine plate = the line's own subject) |
| 40 | S15 t2 | 7.78–10.00 | 168.12–170.50 | 1.072 | V3 L8 tail ("keep the machine running high") |
| 40b | S17 chunk | 0.00–2.88 | 170.50–173.38 | 1.000 | FC swell (no words) |
| 41 | S16 | 0.15–2.88 | 173.38–176.28 | 1.062 | FC L1 (upscale 1168×640→1280×720) |
| 42 | S16 | 2.88–5.78 | 176.28–179.52 | 1.117 | FC L2 (upscale) |
| 43 | S16 | 5.78–8.05 | 179.52–182.66 | 1.383 | FC L3 (upscale; activity-span factor) |
| 44 | S17/S11 chunks ×15 | (see script) | 182.66–212.20 | 0.67–1.00 | FC L4 + DSP + mantra layers — MONTAGE + kinetic (prepro S17 design) |
| 45 | S12 chunks ×2 | (see script) | 212.20–218.46 | 0.80–0.87 | outro clicks — machine winding down |
| 46 | S18 | 0.00–1.96 | 218.46–220.38 | 0.980 | outro "Bacon head…" (soft — see disclosure) |
| 47 | S18 | 1.96–6.76 | 220.38–224.70 | 0.900 | outro chant 1 |
| 48 | S18 | 6.76–10.00 | 224.70–228.80 | 1.265 | outro chants 2+3 — chant 3 (226.62) carried by rhyme visual + kinetic (decision 3); set-down lands at the end, final frame rhymes with S01 |

All factors within caps (≤2.0 slow, speedups unrestricted). Disclosed ≥1.5× slows: seg 3 (1.865), seg 6 (1.560), seg 10 (1.669). No segment slower than 0.5× speed.
Montage plate re-use: S06 chunks repeat inside C1's 19.5s slot (its only plate; beat-sliced at varied trims/speeds + kinetic phrases); S17 chunks repeat inside FC's 29.5s slot (same treatment); S12 appears in bridge, S13 cover, L8-head sliver and outro clicks at distinct trims.


---

## Stage 4 — Build record + GATE 1 (2026-11-06)

Build: 86 pieces (41 sung-phrase segments + 45 montage chunks) rendered phrase-smooth
(setpts factor per phrase, tpad + exact frame caps), concat -c copy = **5491 frames**
(228.8s × 24, drift −2f auto-corrected on the last piece). Captions = lyrics.txt verbatim
(69 events) + kinetic post layer (SLAM/CASCADE/HIGHLIGHT, 189 events) in one .ass, burned
at the final encode; audio = track.mp3 stream-copied.

GATE 1 master: md5 d369ea15f4cf59365c8b2f012b737dea, 149,441,951 B, 1280×720, 24fps, 228.816s.
- Specs: PASS.
- Audio identity: container round-trip md5 differs (ffmpeg extraction wrapper), but decoded
  PCM is BIT-EXACT vs track.mp3 over the full 10,982,400 samples (max abs diff 0.0; the
  extracted stream carries +815 trailing padding samples from the MP4 edit list). PASS by PCM.
- Motion audit: freezedetect (n=0.003, d≥1.2s) found exactly ONE near-freeze, 13.71–15.71s,
  wholly inside the wordless click gap (11.60–15.70). No frozen frames under any sung words. PASS.
- Judder: every segment boundary sits on a song line/phrase boundary by construction; the only
  mid-line boundary is the sanctioned S15 L8 head→tail join at 168.12 (word boundary "keep").
- Onset reads (tiles: onset−1f / onset / onset+4f, fine strips where the tile was closed):
  59 of 68 PASS as built. 9 sung onsets LATE (mouth-lag phrases, measured on the master):
  intro hook #a +0.38 · V1 L3 +0.21 · V1 L7 +0.60 · C1 L3 +0.95 · V2 L5 +0.30 · C2 L3 +0.63 ·
  V3 L1 +0.25 · FC L3 +0.38 — all re-anchored (below). Outro "Bacon head…" onset closed
  (take's micro-opens land mid-phrase) — disclosed, no better picture exists (S18 is the only
  outro take). Outro chant 2 (224.70) still-mouth wide → kinetic SLAM added (decision-3
  treatment, same as chant 3). C1 L7's montage chunk showed S05's closed face under the onset
  → chunk swapped to an S06 money plate.

GATE-1 FIXES (phrase-smooth re-anchors on the measured visible opens; same frame counts):
| piece | take | new window | new factor | open lands |
|---|---|---|---|---|
| 002 | S02 t1 | 3.44–5.02 | 1.925 | hook #a +0.13 |
| 007 | S03 t2 | 4.90–7.66 | 1.162 | V1 L3 +0.08 |
| 011 | S04 t2 | 5.37–7.18 | 1.727 | V1 L7 +0.12 |
| 015 | S05 t1 | 6.35–8.60 | 1.426 | C1 L3 +0.11 |
| 020 | S08 t3 | 3.41–6.08 | 1.077 | V2 L5 +0.08 |
| 026 | S10 t1 | 5.95–8.48 | 1.186 | C2 L3 +0.09 |
| 027 | S14 t1 | 0.16–2.48 | 1.311 | V3 L1 +0.09 |
| 037 | S16 t1 | 5.99–8.05 | 1.517 | FC L3 +0.11 |
| 045 | S06 t1 (was S05) | 3.90–5.90 | 0.896 | C1 L7 chunk swap |
Plus .ass: SLAM line "o2" added at outro chant 2 (224.70). Rebuilt concat = 5491 frames;
master re-encoded (gate 2 below).

## Stage 5 — GATE 2 (re-gate of the 10 changed onsets)

Gate-2 master: md5 b6e28a43bbe327805a49840c84ccfdda, 149,948,955 B, 228.816s.
Re-reads: V1 L3 ✓ open at +4f · V1 L7 ✓ · C1 L3 ✓ open ON the onset (wide O) · C1 L7 ✓
(S06 plate + slam) · V2 L5 ✓ small open at +4f · C2 L3 ✓ · V3 L1 ✓ wide O at +4f ·
FC L3 ✓ · outro chant 2 ✓ kinetic slam lands. **Intro hook #a still late**: parting at
+0.25, wide at +0.34 (improved from +0.38 but outside the +0.17 window — the take's true
first parting measures 3.57 take-time, not the 3.51 estimated from the gate-1 strip).
One more iteration: piece 002 re-anchored to take 3.53–5.11 (f 1.925) → parting predicted
+0.08, wide +0.17. Concat re-verified 5491 frames; master re-encoded (gate 3 below).

## Stage 6 — GATE 3 (final) + DISCLOSURES

FINAL MASTER: masters/mv6_sell_the_lemons_16x9.mp4
md5 **600925eb6fb1cebdd02d16ebb8ae8598** · 149,924,753 B · 1280×720 · 24fps · 5491 frames · 228.816s.
- Hook #a re-read: mouth WIDE OPEN on the onset frame itself (gate-3 strip, work/gate_final/gate2/h1_check_g3.png). ✓
- Audio: decoded PCM bit-exact vs track.mp3 over all 10,982,400 samples (+815 trailing
  padding samples from the MP4 edit list; container round-trip md5 differs by the extraction
  wrapper only). ✓
- Motion: freezedetect final — single near-freeze 13.71–15.71s, inside the wordless click
  gap; nothing frozen under sung words. ✓
- FINAL ONSET TALLY: 67 of 68 onsets open/articulating at onset (or kinetic-carried for the
  sanctioned montage class). The one soft onset: outro lead-in "Bacon head…" (218.46) —
  S18's mouth is closed at the onset frame and its micro-opens land mid-phrase; disclosed,
  no alternative picture exists in the pool.

DISCLOSURES (complete):
- Warp extremes: slowest = S02 hook #a ×1.925 slow-down (0.52× speed, inside the 0.5× cap);
  other ≥1.5× slows: S03 L1 ×1.560 (original build), S04 L5 ×1.669 (original build),
  S04 L7 ×1.727 (gate fix), S16 L3 ×1.517 (gate fix). Fastest: S09 L7 ×0.725 (1.38× speedup).
- Montage-covered sung spans (sanctioned, prepro + parent decisions 1–3): all chorus L4s
  ("Click, upgrade, sell…"), chorus L5–L8 echo phrases + tails (kinetic SLAM over S06/S11
  plates), bridge chant lines + the S13 chant groups ×3 (decision 1 — S13 structural),
  V3 L8 head phrase (decision 2 fallback — kinetic over the S12 machine plate, the line's
  own subject; S15 t1 punch-in impossible: signage on all sides + closed mouth + 2.03× warp),
  FC L4–end mantra stack (S17/S11 celebration plates), outro chants 2+3 (kinetic over the
  S18 rhyme visual, decision 3). Intro hook #3 (15.70) has no singing take in the pool —
  kinetic type over S01 cover per MV_PREPRO_MV-6.md's own S01 design note.
- S03 L4 (decision 4): fits inside caps on word-level times; internal drift ≤0.53s on
  cash/climb — the take's articulation verified at 12fps.
- Outro (decision 3): S18 near-still throughout (micro-opens only); chant 1 lands on an
  open mouth; chants 2–3 kinetic-carried; lead-in soft as disclosed above.
- Plate re-use: S06 chunks repeat inside C1; S17 chunks repeat inside FC; S12 at distinct
  trims in bridge / S13 cover / L8 sliver / outro clicks. One FC chunk (idx83) is a 1-frame
  sliver from chunk-plan rounding — invisible in motion.
- S16 upscaled 1168×640 → 1280×720 in-slot (decision 5). S11 flag stands (distant
  pseudo-glyph signage, none readable). Prepro's C1 numeric counters not implemented —
  kinetic phrases + accent bars carry the escalation instead (minor deviation).
- Gate history: gate 1 = 59/68 clean, 8 mouth-lag phrases measured + re-anchored, 1 chunk
  swap, 1 kinetic addition → gate 2 = 9/10 verified → gate 3 = hook #a on-onset. PASS.

## CORRECTION 2026-11-06 ~10:05 EST — silent on phones (user report, verified)

The delivered master carried the song as a raw MP3 stream stream-copied into the MP4
container. ffmpeg decodes it (PCM gate passed, bit-exact), but iPhone's player renders
MP3-in-MP4 silent — same failure class as MV-2 on 2026-11-02. FIXED in place at the
canonical path: video stream copied untouched (streamhash identical,
649a8064192ece7f110c57e00594d5bc), audio transcoded to AAC 48 kHz stereo 195.9 kbps +
faststart. New master md5 6f980697fb6b742c33dd59585f49b72c, 150,428,904 B, 228.817s.
Re-verified: audio lag 0, corr 0.9981 vs track.mp3; mean volume −17.2 dB, max −1.3 dB
(original MP3-stream copy: −17.1 / −1.3). Original file preserved at
work/fix_2026-11-06/mv6_master_ORIGINAL_mp3-in-mp4.mp4. Gate lesson written into the
Slopcannon skill: the master gate ffprobes the audio codec — aac or it does not ship.

## FORMAT CORRECTION 2026-11-06 ~11:50 EST — house encode (user report, verified)

User verdict #2 (~10:50 EST): "i cannot load or view this — use the exact format
used for all the other mv." Container/stream comparison against MV-2/MV-3/MV-4/MV-5
masters showed ONE divergence: the x264 encode. All other MV masters are CRF 18;
MV-6 alone was CRF 15 (5.06 Mbps video, 150.4 MB file). Everything else already
matched (h264 High avc1 L3.1, yuv420p, 1280x720, 24 fps, isom, faststart, AAC-LC
48 kHz stereo). A first re-encode attempt was stopped by the user ~10:53 EST
(partial deleted, master untouched); resumed on the user's go ~11:41 EST.

FIX: video re-encoded from the AAC-corrected master with libx264 preset medium
CRF 18 (MV-5 v4's exact recipe — its SEI options are the preset-medium defaults
with crf=18.0), audio copied bit-exact (-c:a copy), +faststart. Swapped into
masters/ at the canonical path. NEW master md5 206ee9b07b85e9731708d96eec67e927,
111,261,800 B, 228.817s. Verified on the delivered file: SEI crf=18.0 (x264 core
164 r3108, same as MV-5 v4), 5491 frames, audio streamhash deab9cc34c6c29f431d1153707d4c6f0
identical to the AAC-corrected master (audio untouched), moov before mdat.
Pre-swap versions preserved in work/fix_2026-11-06/: mv6_master_AAC_crf15.mp4
(md5 6f980697fb6b742c33dd59585f49b72c) and mv6_master_ORIGINAL_mp3-in-mp4.mp4
(md5 600925eb6fb1cebdd02d16ebb8ae8598). House-encode rule (x264 CRF 18 + SEI
gate read) written into the Slopcannon skill alongside the AAC law.

## 50MB DELIVERY COPY 2026-11-06 ~12:18 EST (user order: "you have to send a 50mb or under master")

The CRF-18 house master (111 MB) is too big to send in chat. Delivery copy
`masters/mv6_sell_the_lemons_16x9_50mb.mp4` — md5 b835c5212138e449a7ea9d2a4cabd9bf,
47,197,553 B, 5491f, 228.817s, 1280x720 24fps, h264 1,448,816 bps (2-pass,
target 1450k, maxrate 2200k), AAC 195,910 bps copied untouched from the house
master (audio streamhash identical on both files), faststart (moov offset 36).
Same cut, same timing — video bitrate only. House master (CRF 18,
206ee9b07b85e9731708d96eec67e927) stays the canonical master on disk and on
the CDN; the 50MB file is the chat-sendable copy. Encode log + script in
work/fix_2026-11-06/ (encode_50mb.sh, encode_50mb.log, encode_50mb.done rc=0).
Standing rule from this order: chat-sent masters must be 50 MB or under —
if a house master exceeds that, send a bitrate-capped delivery encode of the
same cut with the audio copied, and say so.
