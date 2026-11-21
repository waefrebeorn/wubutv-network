# MV-3 CORRECTION AUDIT + PLAN (2026-11-06)

Method: MV-5 v4 correction. Mouth state read on the RETIMED master at every
line onset and every mantra onset (99 unique sample times = 40 line onsets +
97 mantra stamps incl. the "game" variant), each at t and t+0.17s, from
extracted frames (`work/audit_frames/`, sheets in `sheets_retimed/`).
Reads: `work/mouth_events_retimed.json`. States: O = open at onset,
o = closed at onset, open by +0.17, T = transitional/parted at onset,
C = closed at onset AND +0.17. For every C in a mouth scene, a probe strip
(frames every 3–4f for 2s) found the actual mouth-open time
(`work/audit_frames/probes/`). Audio cross-check offsets
(`work/audio_offsets_retimed.json`, from placement_crosscheck_retimed.json)
are HINTS only — mouth evidence governs (mouth-lag doctrine).

## Headline numbers (retimed base)
- 99 onsets read: **O 62 · T 13 · o 9 · C 15**
- C in cover/structural scenes (disclosed, no sync claimed): 7
  (S21 150.30, S24 183.06 + 191.48, S25 209.28, S31 268.16, S37 331.02, S39 351.55)
- C in MOUTH scenes (the fixable failures): **8** —
  S02 9.32, S09 62.64, S10 68.36, S13 90.66, S14 99.68, S27 220.64,
  S28 238.24, S29 245.10
- Late-open (o) in mouth scenes: 6 — S08 55.14, S12 82.92, S18 129.46,
  S19 136.52, S34 291.42, S38 338.55 (all open by +0.17; micro-shift class)

## Probe evidence (mouth-open time after onset, retimed base)
| scene | onset | mouth opens | audio hint (mean off) | reading |
|---|---|---|---|---|
| S02 | 9.32 | +0.75s (take 0.60s) | −0.55 (early) | take holds closed smile through "you"; opens for "already". Mouth lags take audio ~1.2s at the head. Alternate take s02_t1 is REJECTED (G1 sclera eyes + G2 neon text) — banned. |
| S09 | 62.64 | +0.25–0.38s | +0.64 late, drift +0.88 | classic mouth lag ~0.3s on mantra 1; mantra 2 (64.70) reads O |
| S10 | 68.36 | parts +0.17, open +0.33–0.50 | +0.21, tight | gradual opening inside long "i"; mouth lag ~0.35 |
| S13 | 90.66 | NO opening in 2.0s strip | span-only, med 1.77 | take's mouth is a near-static painted red-lip smile at the head; first parting near L15 (98.50, T). Only s13 take in existence (t1). |
| S14 | 99.68 | +0.67–0.83s | −0.81 early, agree 0.481 DOUBT | mouth opens ~0.75 late; take-audio hint conflicts (unreliable match) — mouth governs |
| S27 | 220.64 | +0.50s (head turns to camera) | +0.80 phrasing hump | head-turn + open lands ~0.5 late |
| S28 | 238.24 (L31) | parts +0.33, open +0.50 | −0.73 (tail artifact) | pout-style articulation, first open ~0.45 late; L30 onset (230.52) reads O |
| S29 | 245.10 | +0.50–0.62s | +0.78 late | mouth lag ~0.55 on mantra 1; mantra 2 (247.10) reads O |

## Corrections (pure assembly; base = retimed SCENES; mechanics of assemble_mv3_recut)
SHIFT = raise the piece head trim sf by N take-frames (events move earlier
by N·w/24 s; tail-loop absorbs the end). REWARP-SPLIT = split one piece at a
word boundary, one warp factor per phrase. Playback floor 0.5× respected
everywhere (slowest = S02 piece A at 0.71×).

| scene | verdict | change | evidence → expected result |
|---|---|---|---|
| S01 | OK | — | T at 2.82 is the sanctioned leader boundary; opens immediately after |
| S02 | REWARP-SPLIT | piece A: take[13f:96f] w=1.4096 (spans 9.32–14.22); piece B: take[96f:FULL] w=0.825 (14.22–18.34) | mouth-open (take 0.60s) lands at master +0.08; mantra "i" attack (take 4.0s) lands exactly at 14.22 (was 14.32, read O). Trade-off disclosed: "already" attack lands ~10.73 vs song ~10.2 (mid-line, no onset sampled there); piece A playback 0.71× |
| S03 | OK (cutaway) | — | no face by design |
| S04 | STRUCTURAL-COVER | — | partial take, disclosed in base; onset reads T |
| S05 | STRUCTURAL-COVER | — | partial take, disclosed in base; onset reads T |
| S06 | OK | — | WORKING SYNC (med 0.08); profile T at 40.06, O at 44.26 |
| S07 | SHIFT | sf += 5f (δ 0.21s) | onset frame is the take's fade-from-black; audio +0.39 late. Removes black head, lands articulation at onset |
| S08 | SHIFT | sf += 4f (δ 0.16s) | late-open o at 55.14 → parting at onset |
| S09 | SHIFT | sf += 9f (δ 0.30s) | probe: opens +0.25–0.38 → opens at onset; mantra 2 stays open |
| S10 | SHIFT | sf += 9f (δ 0.35s) | probe: open +0.33–0.50 → parting at onset, open by +0.15 |
| S11 | OK | — | O at 76.28 and 77.88 |
| S12 | SHIFT | sf += 4f (δ 0.13s) | late-open o at 82.92; mantra 85.04 reads O |
| S13 | STRUCTURAL-COVER (new) | — | probe: no mouth opening exists in the head window of the only take; cannot be created by shift/warp. L14 onset stays CLOSED — disclosed, parent eyeball. L15 onset reads T |
| S14 | SHIFT | sf += 12f (δ 0.61s) | probe: opens +0.67–0.83 → parting at ~+0.06–0.22. DOUBT-scene audio hint conflicts; mouth governs |
| S15 | OK | — | O at 108.92 (WORKING) |
| S16 | OK | — | O at 116.14 + 120.36 (retime already fixed) |
| S17 | OK | — | O at 123.74 + 125.90 (WORKING) |
| S18 | SHIFT | sf += 4f (δ 0.16s) | late-open o at 129.46 |
| S19 | SHIFT | sf += 4f (δ 0.15s) | late-open o at 136.52; mantras 138.58/141.06 read O |
| S20 | OK | — | T at 143.76 (parted at onset, wide open +0.17); disclosed in base |
| S21 | STRUCTURAL-COVER | — | lemon-head partial, disclosed in base; mantras 152.34/156.54 read O, L23 onset C disclosed |
| S22 | OK | — | O at 160.70 + 164.42 |
| S23 | OK | — | O at 168.76 (span-only audio hint; mouth governs) |
| S24 | STRUCTURAL-COVER | — | egg-head partial, disclosed; mixed reads (O at 184.70/188.42/190.60, C at 183.06/191.48) |
| S25 | STRUCTURAL-COVER | — | two partial takes, disclosed; mixed reads (O at 201.54/211.40/211.86, C at 209.28) |
| S26 | OK | — | O at 215.40 (WORKING) |
| S27 | SHIFT | sf += 12f (δ 0.57s) | probe: head-turn open +0.50 → open at ~onset. Phrasing hump mid-line remains (disclosed in base) |
| S28 | SHIFT | sf += 8f (δ 0.42s) | probe (L31): open +0.50 → parting at onset. L30 onset must stay O — gate verifies (take articulates continuously there) |
| S29 | SHIFT | sf += 16f (δ 0.53s) | probe: opens +0.50–0.62 → opening at ~+0.02; mantra 2 stays open; audio hint (+0.78 late) agrees |
| S30 | STRUCTURAL-COVER | — | disclosed in base; onset reads O anyway |
| S31 | COVER | — | mantra-slice montage, disclosed; reads O except 268.16 C / 268.42 o |
| S32 | COVER | — | mantra-slice montage, disclosed; reads O |
| S33 | COVER | — | pile-up montage (171 words/30s — unfilmable as lip-sync), disclosed; sampled reads O/T |
| S34 | SHIFT | sf += 4f (δ 0.15s) | L35 onset O (287.80); second mantra late-open o at 291.42 → centered |
| S35 | STRUCTURAL-COVER | — | repeat-drop structural, disclosed; reads mostly O (296.70 o) |
| S36 | OK | — | O at 309.88 + 317.08 (mouth governs over grey audio hint) |
| S37 | COVER | — | hold-loop montage remainder, disclosed; mixed reads (O at 322.08/323.32/325.22/333.08) |
| S38 | SHIFT | sf += 4f (δ 0.13s) | late-open o at 338.55; mantras read O |
| S39 | COVER | — | whole-slot montage cover (ratio 0.573), disclosed; final mantra 351.55 reads C — the outro's last "dad" has no articulation in the cover take (disclosed; caption reads "dad" ✓, ASR "dead" rejected) |

## Captions
`captions_16x9_corrected.ass` = base captions with ONE proven fix: the L02
events (9.32–18.34, 7 Dialogue lines) now read "You already know, I am your
**game**" (the song's performed word; two Whisper passes + LYRIC_TIMELINE).
"dead" count in captions = 0 ✓ (outro reads "dad"). No other caption changes.
Note: take s02_t2 itself sings "dad" — a take-level mismatch inherited from
the base build; not fixable without generation (barred this run).

## Eye-spec conflict (per brief)
POSE_CARDS.md says "two round dot eyes"; the governing spec in every vehicle
is "small solid black oval eyes, no white showing." Ovals govern. (Several
takes visibly drift to dot eyes — S10/S31/S37 reads show small round eyes —
inherited from the base build; no new generation this run to fix them.)

## Gate (on the corrected master, work/gate_corrected/)
(a) audio identity vs track.mp3 (decoded-PCM md5);
(b) mouth state re-read at all 99 onsets — mantra onset CLOSED in a mouth
scene = FAIL (fix + re-gate); cover-scene onsets reported as
DISCLOSED-COVER;
(c) judder audit — zero in-phrase warp steps by construction (one factor
per phrase; S02 has exactly one step at the 14.22 phrase boundary) +
cut-point reads (no closed↔open pops at scene cuts);
(d) motion audit — no frozen run ≥24f during words; no vocal mean-diff <0.5
(reuse master_motion_spotcheck method).
