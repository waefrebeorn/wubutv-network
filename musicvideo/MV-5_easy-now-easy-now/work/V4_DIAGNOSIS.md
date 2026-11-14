# MV-5 V4 DIAGNOSIS — why v3 fails on playback (measured on the v3 master)

Written 2026-11-06, before any v4 assembly. Master under test:
masters/mv5_easy_now_easy_now_16x9_v3.mp4, md5 e13f17fc3a1e130ff1bfcd865a0c0ed1
(build 3, per-word swing warps, 249 pieces). User verdict 2026-11-06 ~05:16 EST:
"none of the easy now easy now is lining up and also the jumps are misaligned
and bad jarring cuts." Verdict outranks the v3 gate (which measured PLACEMENT —
right take frame at the song time by pixel diff — not perceived mouth sync).

## 1. Hook mouth audit — 24 of 30 "Easy now" onsets land closed / transitional / unreadable

Method: for every "Easy now" occurrence (SONG_WORDS.json, first 'Easy' onset),
frames extracted from the v3 master at onset−0.10s, onset, +0.15s, +0.30s
(work/diag_v4/hooks/, sheets work/diag_v4/sheets/hooks_01..08.png) and the
SINGER's mouth read visually (CAT for intro, GIRL for choruses per the
ear-verdict ownership). "Open" = clearly open singing mouth at the onset frame.

| # | Line | Onset (s) | Singer | Picture at onset (v3 piece) | Mouth at onset | Mouth +0.15s |
|---|------|-----------|--------|------------------------------|----------------|--------------|
| 1 | I01 | 1.66 | CAT | s01_t1 line-pw | OPEN | open |
| 2 | I03 | 5.98 | CAT | s01_t1 line-pw | CLOSED | closed (opens ~+0.30) |
| 3 | I05 | 10.04 | CAT | s02_t1 cutaway (wide) | UNREADABLE (cat tiny, girl closed) | unreadable |
| 4 | I07 | 15.40 | CAT | s02_t1 cutaway (wide) | UNREADABLE | unreadable |
| 5 | L17 | 57.52 | GIRL | s08_t2 refrain-pw | OPEN | transitional |
| 6 | L19 | 59.90 | GIRL | s20_t1 donor-tail | TRANSITIONAL (lips parted) | transitional |
| 7 | L21 | 62.52 | GIRL | s20_t1 donor-tail | CLOSED | closed |
| 8 | L23 | 64.92 | GIRL | s08_t2 refrain-R4 | TRANSITIONAL (barely parted) | transitional (opens +0.30) |
| 9 | L25 | 66.82 | GIRL | s08_t2 tail | CLOSED | closed |
| 10 | L27 | 69.20 | GIRL | s09_t1 refrain-R2 (cat close-up) | CLOSED (singer small behind, cat shut) | closed |
| 11 | L29 | 71.34 | GIRL | s10_t1 donor (wide) | UNREADABLE | unreadable |
| 12 | L31 | 74.02 | GIRL | s09_t1 refrain-pw | CLOSED | OPEN (opens ~0.1s late) |
| 13 | L57 | 121.26 | GIRL | s21_t3 donor (S15 tail) | CLOSED (profile) | transitional |
| 14 | L59 | 124.00 | GIRL | s16_t2 cover | CLOSED | closed |
| 15 | L61 | 126.30 | GIRL | s16_t2 cover | CLOSED | closed |
| 16 | L63 | 128.18 | GIRL | s16_t3 cover (profile) | CLOSED | closed |
| 17 | L65 | 130.44 | GIRL | s17_t1 refrain-R1 (static portrait) | CLOSED | closed |
| 18 | L67 | 132.94 | GIRL | s16_t1 donor | CLOSED | OPEN (opens ~0.15s late) |
| 19 | L69 | 135.02 | GIRL | s16_t1 donor | CLOSED | closed |
| 20 | L71 | 137.30 | GIRL | s16_t1 donor | CLOSED | closed |
| 21 | L91 | 169.16 | GIRL | s23_t1 refrain-pw | OPEN | open |
| 22 | L93 | 171.16 | GIRL | s16_t3 donor | CLOSED | closed |
| 23 | L95 | 173.30 | GIRL | s16_t3 donor | CLOSED | closed |
| 24 | L97 | 176.04 | GIRL | s24_t1 cover | OPEN | open |
| 25 | L99 | 178.24 | GIRL | s24_t1 cover | CLOSED | closed |
| 26 | L101 | 180.28 | GIRL | s24_t3 cover | CLOSED | closed |
| 27 | L103 | 182.52 | GIRL | s24_t2 cover | OPEN | open |
| 28 | L105 | 184.68 | GIRL | s16_t4 donor | CLOSED | closed (opens after donor ends) |
| 29 | L107 | 192.06 | GIRL | s20_t1 donor-head | TRANSITIONAL (lips parted) | transitional |
| 30 | L109 | 197.58 | GIRL | s27_t1 line-L109 | OPEN | open |

**Count: 6/30 land clearly OPEN at the onset (I01, L17, L91, L97, L103, L109).
24/30 land CLOSED, TRANSITIONAL, or UNREADABLE — the number v4 must drive to
zero.** (L31 and L67 open ~0.1–0.15s late — the mouth-lag signature in
miniature. L107 is a grid-suspect occurrence: two Gemini runs + the audio
bible hear NO sung words at 187–194.1s; the v1 'tail' decode stamp is likely
an artifact — v4 treats it as a non-sung slot, reported here for completeness.)

### Where the failures live (structural, not random)
- **Donor/cover picture sits exactly on the onset** in 13 of the failures
  (L19, L21, L29, L57, L67, L69, L71, L93, L95, L105 donors; L59, L61, L63
  S16 cover; L99, L101 S24 cover). The v2/v3 scene plans interleave refrain
  slices with donor tails fitted to take-audio, and the song's line onsets
  fall inside the donor slices. Placement checks passed because the donor
  frame at the onset is "a frame of some take near the right time" — the
  singer's mouth is simply not open in it.
- **Chorus 2's first half (L57–L63) is not the chorus take at all** — it is
  rejected-take tails (s16_t2/s16_t3) used as cover, closed-mouthed at every
  onset. S17's chorus take only enters at L65 — and its R1 group is a
  near-static portrait with a closed mouth (L65).
- **Final Chorus is a patchwork**: s23_t1 refrain slices alternate with
  s16_t3/s16_t4 donor slices; the donors carry L93, L95, L105's onsets, all
  closed. S24 (L97–L102) is entirely rejected-take cover — L97/L103 happen
  to land open, L99/L101 closed.
- **Per-word warping can place a closed-mouth interval on an onset** (I03):
  the take's audio word and its visible mouth disagree by the standing
  mouth-lag (~0.5–1s class); warping the audio swing curve faithfully
  reproduces the lag in the picture.

## 2. Judder audit — 89 adjacent-interval steps >1.35× inside sung phrases

From work/assembly_fit_mv5_v3pw.json: for consecutive pieces of the same
take inside a sung phrase, playback factor = 1/setpts. **89 adjacent steps
exceed a 1.35× ratio** (101 counting cross-take pw adjacencies). Every one is
a visible speed lurch at a word boundary — the "jarring jumps."

Worst 10:
| Ratio | Scene | Playback step | At song time |
|-------|-------|---------------|--------------|
| 14.09× | S15 | 9.50× → 0.67× | 116.42→116.50 |
| 8.93× | S08 | 4.67× → 0.52× | 57.90→58.02 |
| 5.14× | S06 | 2.57× → 0.50× | 44.61→44.90 |
| 4.86× | S20 | 4.86× → 1.00× | 155.72→156.01 |
| 4.13× | S23 | 3.33× → 0.81× | 169.16→169.28 |
| 4.00× | S12 | 1.00× → 4.00× | 97.51→97.59 |
| 3.77× | S19b | 0.63× → 2.37× | 152.36→153.49 |
| 3.64× | S04 | 0.71× → 2.60× | 25.42→25.71 |
| 3.50× | S15 | 1.00× → 3.50× | 116.00→116.21 |
| 3.50× | S08 | 1.33× → 4.67× | 57.52→57.90 |

By scene: S04 11, S12 10, S07 10, S01 10, S05 10, S06 9, S11 9, S19b 6,
S15 3, S17 3, S08 2, S20 2, S23 2, S09 1, S25 1. (Full table computed from
the plan JSON; method: same-take consecutive sung pieces, ratio of playback
factors.)

## 3. Consequence for v4 (method correction, per the repair brief)
- Anchors come from VISIBLE mouth events (work/mouth_events_v4.json), not
  take-audio word times.
- Phrase-level smooth warps only — one factor (or one linear ramp) per sung
  phrase; per-word data chooses takes and verifies, never chops.
- Chorus scenes run their chorus take CONTINUOUSLY across the lines (no
  donor slices interleaved at onsets); donors survive only where no sung
  line onset lands on them.
- Every hook gets its own mouth-verified anchor.
