# MV-8 Rebuild — LYRIC TIMELINE v2 (adjudicated)

Track: track.mp4 (187.2s, md5 8a4834d2e647fffce6782a3461baa936). Canonical word list:
`work/rebuild/SONG_WORDS_v2.json` (135 words, span 7.98–146.02).
Adjudication script: `work/rebuild/adjudicate_v2.py` (reproducible).

## Witnesses

| Pass | Model | Prompt | VAD | Words | Role |
|---|---|---|---|---|---|
| A (medium) | faster-whisper medium | none | no | 154 | BASE — strongest model, cleanest timing |
| B2 (small) | faster-whisper small | lyric sheet | no | 86 | Witness — sheet-prompted (bias note below) |
| v1 | faster-whisper small | none | no | 112 | Witness — heard the Verse/Hook 2/Final Hook first |
| tiny | faster-whisper tiny | none | no | — | Corroboration only (Hook 1 phrases 8.0–10.46, 12.32–14.16) |
| B (discarded) | small + sheet + VAD | sheet | yes | 10 | COLLAPSED — VAD kills the music-bed vocal, discarded |

**Prompt-bias note:** B2 was prompted with the lyric sheet, so where B2 agrees
with the sheet against the two unprompted passes, that agreement is weak
evidence (prompt echo). Medium (unprompted) is the timing authority; v1
(unprompted small) is the second timing witness.

**Systematic mishear corrections (applied in the canonical list):**
- Medium hears "White" for "Wipe" everywhere ("White and you're still there",
  "Endless white forever"). B2 + v1 both hear "Wipe" at those spots; "White"
  makes no lyric sense. Corrected to "Wipe"/"wipe".
- Medium hears "Fence" for "Phantom" ("Fence on residue stays"). Sheet lines
  are "Phantom residue stays" / "Phantom wiper never stops"; both passes garble
  the head word while the tails ("residue stays" p 0.80/0.82, "never stops"
  p 0.76/0.98) are solid. Corrected to "Phantom".
- v1's "in the stool" is its known mishear of "and it's still" (established in
  v1 analysis). v1's "water" = "wipe" in the same class.
- Zero-duration words in every pass are ASR boundary artifacts, dropped.

## Line list (performed vocal governs; sheet divergences flagged)

Onsets are the cut grid. "Sheet" = user's lyrics.txt.

### Hook 1 (5.97–34.40) — 7 lines, all multi-witness

| # | Line (performed) | Onset–end | Witnesses | Note |
|---|---|---|---|---|
| L1 | Wipe and it's still there | 7.98–11.70 | B2 7.98, tiny 8.0–10.46, medium 8.52 | Onset 7.98: B2+tiny agree; medium 8.52 (p=0.36) is the outlier. First word ~1.5s AFTER the groove-entry hit 6.44 — plan correction vs v1's ~6.4 inference |
| L2 | Wipe and it's still there | 11.70–16.12 | medium, B2 11.78–14.58 | Medium's "wipe, wipe" head is a doubled onset; line starts 11.70 |
| L3 | Paper comes back dirty (+ "dirty" echoes ×3) | 16.12–22.08 | medium (Paper p=0.36, core p≥0.96) | B2 onset 15.34 noted; medium's clean boundary (L2 ends 16.12) adopted |
| L4 | Brown brown brown brown brown | 22.08–24.74 | medium (p 0.41–0.97) | FIVE browns, not the sheet's two. B2's 20.94–23.14 (p 0.04/0.10) rejected; display's 18–20 was the dirty echoes |
| L5 | Wipe and it's still there | 24.74–27.74 | medium, B2 23.14–26.52 | |
| L6 | Wipe and it's still there | 28.62–29.98 | medium, B2 28.44–30.28 | Tail "still/there" zero-duration in medium; line ends ~29.98 |
| L7 | Phantom residue stays | 30.98–34.96 | medium, B2 31.70–34.36 | "residue stays" confirmed by both |

### Interlude (34.40–60.46) — NEW lyric anchor

| # | Line (performed) | Onset–end | Witnesses | Note |
|---|---|---|---|---|
| L8 | Brown brown brown brown brown | 36.90–41.84 | medium ONLY (p 0.58–0.97) | NEW. v1/B2 heard nothing here. Sheet's Hook-1-tail "Brown (Brown brown)" sits at this position — sheet-supported. Gives the Interlude a lyric anchor; 41.84–60.46 has no words (quiet 34.40–45.51 + instrumental build) |

### Verse (60.46–65.12)

| # | Line (performed) | Onset–end | Witnesses | Note |
|---|---|---|---|---|
| L9 | Sitting on the toilet | 60.46–63.30 | v1 60.46–62.20, medium 60.64–63.30 | Onset 60.46 (v1); medium "Sitting" p=0.02 |
| L10 | Wipe once, still brown | 63.00–65.00 | v1 63.00–65.12, medium 63.62–65.00 | Sheet's "(Phantom)" backing tag lands ~65.60–66.42 (medium's garbled "Fence on", p 0.02/0.04 — corrected to "Phantom", not a line) |

### Pre-Hook (65.12–67.26)

| # | Line (performed) | Onset–end | Witnesses | Note |
|---|---|---|---|---|
| L11 | Wipe, wipe again | 66.48–67.38 | medium, v1 66.38–67.26 | Singer doubles "wipe" vs sheet's single "Wipe again". Sheet's "Still there / (Never clean)" merges into L12 |

### Hook 2 (67.26–105.94)

| # | Line (performed) | Onset–end | Witnesses | Note |
|---|---|---|---|---|
| L12 | Wipe and it's still there (+ "Never clean") | 67.38–70.28 | medium, v1 67.26–68.90 | "(Never clean)" 69.36–70.28 (p 0.97/0.84) — sheet's parenthetical CONFIRMED as performed |
| L13 | Wipe and it's still there | 70.28–73.00 | medium, v1 71.00–72.90 | |
| L14 | Wipe and it's still there | 73.00–76.98 | medium, v1 frag 74.89–76.02 | Third hook line before "Endless" — the singer repeats more than the sheet (sheet has two) |
| L15 | Endless wipe forever | 76.98–81.08 | medium timing, v1 77.56–80.48 | Identity from sheet; medium's "white" corrected; v1's "And there's water" is its garble of the same line |
| L16 | Wipe and it's still there (truncated) | 81.66–83.74 | v1 ONLY (p 0.86–0.99) | **CONTESTED.** Sheet+B2 say "Brown brown (Still brown)" here. B2's probs ≈0.00 (prompt echo — the model assigned ~zero probability from audio). Medium hears silence. v1's high-prob hook words win, but single-witness: scene stages it as a hook-line repeat with a Brown-counter kinetic accent, which works under either reading |
| L17 | Wipe and you're still there | 85.98–88.98 | medium, v1 85.96–88.26, B2 85.96–88.26 | Performed "you're" variant (see below) |
| — | (gap) | 88.98–95.52 | — | v1's "Yeah" 90.66 (p=0.18) DROPPED — no second witness |
| L18 | Wipe and you're still there | 95.52–100.18 | medium, v1 frag 97.02–99.68 | Onset 95.52 (medium, p≥0.98 on 4/5 words); v1's 97.02 is late/weak (p=0.06) |
| L19 | Phantom wiper never stops | 102.34–105.98 | medium timing, v1 102.52–105.46 | Head words uncertain in BOTH passes (v1: "Santa, wipe, wipe"; medium: "And from wide one"); tail "never stop(s)" solid in both. Identity from sheet, flagged |
| — | Wipe (Drop shout) | 105.94–106.36 | v1 ONLY (p=0.43) | Single-word shout opening the Drop; no other witness (medium hears nothing in the Drop) |

Sheet's Hook-2-tail "Brown (Brown brown)" after L19 is NOT performed (no
witness; the Drop "Wipe" shout follows instead). Sheet's "Brown brown (Still
brown)" after L15 is the contested L16 window (above).

### Drop (105.94–120.40) — vocal gap

No lyric lines. Only the "Wipe" shout at 105.94. The sheet's half-bar silence
is NOT performed (level flat ~−16.5 dBFS); the "STILL THERE!" placement is the
hit pair at 112.25/112.72 (v1 inference, kept).

### Final Hook (120.40–146.00)

| # | Line (performed) | Onset–end | Witnesses | Note |
|---|---|---|---|---|
| L20 | Wipe and you're still there | 120.06–123.18 | medium, v1 120.40–122.80, B2 120.12–122.72 | |
| L21 | Wipe and it's still there | 124.68–127.18 | medium, B2 124.30–126.48 | Fills a v1 gap (v1 heard nothing here) |
| L22 | Paper comes back dirty (+ "Dirty" echo) | 127.18–132.14 | medium 127.18–130.53, v1 127.44–130.50 | Kills B2's repeated-hook reading at 127.68. Echo window 130.50–132.14 (v1) / 132.36–133.46 (medium) — one "Dirty" echo between Paper and the Browns |
| L23 | Brown brown brown brown brown | 133.46–136.40 | medium (p 0.82–0.99), v1 133.08–136.34 | Five browns again |
| L24 | Wipe and you're still there (+ "Still there, still there") | 136.40–140.14 | medium, v1 136.34–139.28 | Sheet's "(Still there)" tag is performed inside the line |
| L25 | Wipe and you're still there (+ "Still there") | 140.14–143.16 | medium, v1 139.28–142.00 | |
| L26 | (Phantom wipe) Endless wipe forever | 142.66–146.02 | medium + sheet | **v1's "The water in this pipe" RETIRED** — "water"="wipe" mishear class; medium+sheet agree on "Endless wipe forever". Core "Endless wipe forever" 144.18–146.02; "(Phantom wipe)" tag ~142.66–144.18 (medium's garbled 143.68 words) |

### Outro (146.00–187.20) — instrumental, NO lyric lines

No reliable words. Medium's 157.18–172.24 spans are zero-duration pile-ups
(p~0.00–0.12); B2's "Turn it. Turn it. Brown brown." 157.72–159.46 is the same
artifact class (tokens dumped at the 159.46 segment boundary); v1's "I'm gonna"
loop is a known hallucination. **The sheet's Outro "Brown" is sheet-only —
no performed witness with credible timing — so no lyric line is linked at the
true peak 159.435s.** The 171.44 "and you're" fragment (p 0.92/0.95, zero-duration
neighbours) is noted as uncorroborated, not a line. The true peak carries the
biggest VISUAL, not a lyric.

## The "you're" variant — performed deviation, flagged

Medium (unprompted) hears "you're" in the later hook lines — 87.16 (p=0.87),
125.46 (p=0.99), 140.72 (p=0.98) — while hearing "it's" in Hook 1 and early
Hook 2 (13.72 p=0.98, 25.48 p=0.99, 68.08, 72.24 p=1.00, 75.82 p=0.99).
B2 hears "it's" at 125.28 (p=0.98) but B2 is sheet-prompted (bias toward the
sheet's "it's"). v1's "in the" is its garble, no vote. The "baby" ad-lib
hypothesis is DEAD: v1's "baby" at 87.60/122.10/137.58/140.96 was its mishear
of "there" — B2 + medium both hear "there" at all four spots.

Reading: the singer switches to "Wipe and YOU'RE still there" in the later
hooks (L17, L18, L20, L24, L25). The line identity for scene planning is the
hook line either way; the variant is recorded here, not smoothed away.

## Divergences: sheet vs performed (complete)

1. Drop [Silence – half bar] NOT performed (level flat through the Drop).
2. Drop micro-sequence mostly sheet-only ("STILL THERE!" = hit pair 112.25/112.72, inferred).
3. Hook 2 back half: singer repeats the hook line MORE than the sheet (extra L14 at 73.00, extra L16 fragment at 81.66).
4. Sheet's Hook-2 "Brown brown (Still brown)" after "Endless wipe forever": contested (L16 window) — performed evidence favours a hook fragment.
5. Sheet's Hook-2-tail "Brown (Brown brown)" after "Phantom wiper": NOT performed.
6. Performed "you're" variant in later hooks (above).
7. Performed "Never clean" (L12) and "(Phantom)" tag (Verse tail) and "(Phantom wipe)" tag (L26) — sheet parentheticals confirmed as sung.
8. Interlude not on the sheet at all — but it HAS a performed Brown chant (L8, 36.90–41.84).
9. Performed Outro dwarfs the sheet's: sheet says "last two stabs, cut clean" with one "Brown"; performed Outro is 41.2s of instrumental with the track's true peak and loudest cluster, no reliable words.
10. Hook 1 "Brown brown" is performed as FIVE browns (L4, L23), not two.
11. First hook line starts ~7.98, not ~6.4 (groove-entry hit 6.44 precedes the first word by ~1.5s).
12. "Paper comes back dirty" gains three "dirty" echoes in Hook 1 (19.24–22.08) — sheet has one line, performed echoes it.

## Coverage statement (for the Stage 3 plan)

26 lyric lines (L1–L26) + 1 Drop shout. Every line is linked to a scene in
SCENE_PLAN_v2.md. Un-linkable: none among the lines. The Outro has no lines
to link; its scenes are staged on the crescendo map (true peak 159.435s,
loudest cluster 170.9–174.7s). Contested/flagged lines (L16, L19 head words,
L26 tag window) are staged so the visual works under either reading.
