# Volley 17 + S04a volley — gap coverage record (2026-11-04)

Format matches VOLLEY14/15/16_GAP_COVERAGE.md. No commit, no ledger edit,
no announcement, no posting, no chat delivery — the parent verifies,
commits, and delivers. This record covers the last generation fired for
MV-2 v6; everything after this is assembly.

## Cap accounting

Task cap: at most 6 new videos total, including retries. Used in this
task: 3 (S07, S21, S04a). Retries burned: 0. Remaining cap: 3, unused —
no further volley is planned: every remaining slot is either covered by a
candidate below, covered by a re-gated existing take (§4), or a
structural assembly cover that generation already failed twice.

## Vehicles

All three prompts follow the 55-rule construction in order: framing +
identity lock first sentence (medium close-up, locked-off steady camera,
THE VOICE: slicked dark hair, clean shave, INK suit, BONE shirt, CADMIUM
pocket square, chrome mic on stand, blank paper ticket), performance
window with a local whole/half-second bracket, exact lyric in quotes at
least twice, articulation clause, no other visible character (silent
mouths moot — single performer), action only before the first word or
after the last word, closed-mouth hold + stable end pose, no
whisper/mumble/hushed/softly language, one singer, open-road
structure-free staging (no plaza/booths/signage/text), forbidden
checklist at the end.

- S07: window "from 1.0 to 8.0 seconds", lyric "We've been slamming the
  danger roads, toll roads are dumb", 9-second clip.
- S21: window "from 0.5 to 9.5 seconds", lyric "The wrecks just come, pay
  to go faster, the rest of us slow", 10-second clip.
- S04a: window "from 0.0 to 9.5 seconds", lyric "Now they got the fast
  lanes, the rich ones fly on by, while the rest of us crawl, watching
  money flash by" (21 words INCLUDING the "Now they got" lead, so a pass
  also closes the GAP-A micro-gap), 10-second clip.

All three landed on the first attempt; 0 server failures.

## Gate order (as in volleys 14–16)

Lyric sequence FIRST, ratio second (usable 0.80–1.25; grey 0.60–0.80 /
1.25–1.60 with warp-rescue only ≤1.5x to band edge and gates re-run),
frame gate third (FAIL if vocal near-dup run ≥24f during vocal OR vocal
mean diff <0.5), character gate, exactly-once check including beat-word
subsequence repeats, split-half recheck on zero-word decodes. Mishear
classes normalized for matching only (raw kept): tall/told/toe=toll,
done=dumb in hook, paid=pay, plasers=plazas, comin'=coming, tell=sell.

## Per-take results

### S07 — CANDIDATE (slot COVERED)

- Raw: `takes/media-generation-mv2-s07-v6final-t1-0-ab879823-028d-485f-b78d-a8bb79742c38.mp4`
- Canonical: `takes/mv2_s07_v6final_t1.mp4`, md5
  `f3b4f97ec32270b8c00a719fc1ab9807`, 1280x720/24fps/10.000s.
- Lyric: all 10 words exactly once (we've, been, slamming, the, danger,
  roads, toll [raw "told"→toll class], roads, are, dumb 7.66–8.18).
  Vocal span 0–8.18s vs song 8.50s → ratio 1.039 IN BAND.
- Drift: median −3.6f (range −32.7 to +21.8). Disclosed drift nit: the
  "toll" word is held long and arrives ~1.4s early on that one word;
  remaining hook words align within ~0.2s.
- Sub-repeats: empty. Singles: empty.
- Frame: PASS (mean 0.54, near-dup run 13, frozen run 1).
- Character: PASS (2s/5s/8s frames: same THE VOICE face, face-to-camera,
  mouth open mid-vocal, mic on stand, blank ticket, CADMIUM square).
- Text: PASS (no legible words).
- VERDICT: CANDIDATE — S07 slot COVERED (words 118–127). Ear-decision
  dependency applies: this take sings the PERFORMED line ("we've been
  slamming the danger roads"); captions use performed words. If the
  user's ear hears "weaving" instead, the take itself would need
  revisiting — captions alone cannot fix a mouth. Flagged, not resolved.

### S21 — CANDIDATE with disclosed micro-gap (slot COVERED)

- Raw: `takes/media-generation-mv2-s21-v6final-t1-0-f0e214bb-1e81-42ee-bb74-070d1425cd44.mp4`
- Canonical: `takes/mv2_s21_v6final_t1.mp4`, md5
  `f8f80a6a2ea511b66d7702ae94bc6d38`, 1280x720/24fps/10.000s.
- Lyric: dictated 13 words; CORRECTED beat is 14 words ("the wrecks
  just come pay to go faster TO the rest of us slow") — the take drops
  song word "to" 211.18–212.60 (take goes "faster" 4.62–5.46, gap, then
  "the" 6.30; "paid"→pay class for "pay"). The initial QC script's beat
  string omitted the second "to"; the saved JSON was corrected with a
  note (13/14, minor class) — do NOT re-derive 13/13 from the old beat.
- Vocal span 0–8.14s vs song 9.24s → ratio 1.135 IN BAND.
- Drift: median +10.9f (range +5.0 to +21.5).
- Sub-repeats/singles: empty.
- Frame: PASS (mean 0.71, run 5).
- Character: PASS (5s frame: face-to-camera, mouth open, mic on stand,
  blank ticket, CADMIUM square).
- Text: PASS.
- VERDICT: CANDIDATE with disclosed micro-gap (dropped "to") — same
  minor single-word drop class as S06b t1 / R1 t3, which are counted as
  candidates. S21 slot COVERED.
- Trim alternative REJECTED on evidence: S21 t2's mantra-only portion
  (take 3.84–9.18, 5.34s) vs song 9.24s → ratio 1.73, outside band.
  Trimming the wrong-line take does not pass; the fresh take was the
  correct path.
- Phantom-token finding (assembly-relevant, discovered at caption
  build): SONG_WORDS_BASE words 333–339 ("the road gets meaner every
  single time.") all carry the identical zero-duration stamp 205.2–205.2
  — a transcription echo of the S17 line, not words sung at 205.2. The
  real S21 line is words 340–353 ("The wrecks just come. Pay to go
  faster to the rest of us slow."), which is exactly what this take
  sings. The 7 phantom tokens are EXCLUDED from captions (not sung,
  not mouthed, not captioned). This does not change the take's verdict:
  its ratio/drift were computed against the real line words 340–353.

### S04a — CANDIDATE via warp-rescue (slot COVERED, GAP-A lead closed)

- Raw: `takes/media-generation-mv2-s04a-v6final-t1-0-110283e5-c80f-4985-aa57-e1d928d86a5b.mp4`
  (2,281,360 B).
- Canonical: `takes/mv2_s04a_v6final_t1.mp4`, md5
  `c95e644beb35eb0bcb1ca1571b4439f3`, 1280x720/24fps/10.000s.
- Lyric: all 21 prompted words matched in sequence (now, they, got,
  the, fast, lanes, the, rich, ones, fly, on, by, while, the, rest, of,
  us, crawl, watching, money, flash, by). Note: the take sings "fast
  lanes" (2 words) where the song transcription has the single token
  "flaselines" — same phrase, not a mismatch. Vocal span 0–9.18s vs
  song 6.74s (34.56–41.30) → ratio 0.734 GREY.
- Frame (unwarped): PASS (mean 0.62, near-dup run 7, frozen run 1).
- Warp-rescue: whole-clip warp 1.0899x (within the ≤1.5x cap) →
  `takes/mv2_s04a_v6final_t1_warped.mp4`, md5
  `6c6dd183d26dd2f6fdc1a5b53d4cfd36`. Warped dictation: all 21 words,
  vocal 0–8.44s; measured ratio 0.799, scaled ratio 0.800 (S09
  precedent: assembly uses the scaled span 8.423s at factor 1.2497).
  Warped frame gate: PASS (mean 0.64, run 6).
- Character: PASS (2s/5s/8s frames: face-to-camera, mouth open mid-vocal,
  mic on stand, blank ticket, CADMIUM square, open-road staging).
- Text: PASS (no legible words).
- VERDICT: CANDIDATE (warp-rescued) — S04a slot COVERED, and because
  the prompt included the "Now they got" lead, the GAP-A micro-gap
  ("Now they got" 34.56–34.96) closes with it.
- Fallback NOT needed: the fresh take passed via the sanctioned
  warp-rescue path, so the warped S04 t1 (profile/facing FAIL — side
  view throughout, different pale render, mouth not readable) stays
  unused. Warped t1 md5 `be954eae922e6ab52d05e0247f590d26` remains on
  disk as a superseded asset, never assembled.

## §4 — Re-gated existing takes (NO new videos, NO cap consumed)

Two hook slots convert from cover to mouth-sung by re-gating existing
takes against the LONGER second-hook spans of their own scenes' lines.
Each take covers exactly one hook occurrence within its own scene's
line (the take's single hook delivery); the other occurrence stays
covered. This is within-scene assignment to matching words, same rule
as the S07-tail anchor — not cross-scene reuse.

### C1-hook2 (54.22–56.46) — MOUTH via warped S05 t6

- Take: `takes/mv2_s05_t6.mp4` (volley-3, frames/text clean). Warped
  1.30x → `takes/mv2_s05_t6_warped.mp4`, md5
  `05e321a9e02e2a223e64ce117da1cf1e`.
- Lyric: all 4 hook words exactly once (toll [raw "tall"→toll], roads,
  are, dumb), warped vocal 0–2.82s; measured ratio 0.794 / scaled 0.800
  (S09 signature). Assembly uses scaled span 2.80s at factor 1.25.
- Frame (warped vocal): PASS (mean 0.61, near-dup run 12, frozen run 2).
- Character/text: PASS (warped 1.5s frame: face-to-camera, mouth open,
  mic on stand, blank ticket; booth panels blank).
- Previous status: S05 t6 was a clear miss (0.54x) against the 1.92s
  opener span and frame-poor by the old changed-fraction bar. Against
  the 2.24s second-hook span it is grey → warp-rescuable, and the
  refined vocal-window frame gate passes it. The old verdict is
  superseded for this span only.

### C2-hook2 (125.16–128.12) — MOUTH via S13 t3

- Take: `takes/mv2_s13_t3.mp4` (volley-1; sequence clean: hook exactly
  once, tall→toll class).
- Ratio vs the 2.96s second-hook span: 0.813 IN BAND (factor 1.230).
  Previous status was a clear miss (0.42x) against the 1.52s first-hook
  span — superseded for this span only.
- Frame (vocal 0–3.64): PASS (mean 0.97, near-dup run 11, frozen run 1).
- Character: PASS (2s/3s frames: face-to-camera, mouth open mid-vocal,
  mic on stand, blank ticket, CADMIUM square).
- Text: PASS (booth panels blank, no legible words).
- C2-hook1 (122.92–124.44) stays COVERED (hook-floor: no in-band take;
  S13 t3 cannot cover both occurrences).

## Tally

- COVERED by this volley: S07, S21, S04a (+ GAP-A lead).
- COVERED by re-gate (no new video): C1-hook2, C2-hook2.
- Remaining slots are assembly covers, not generation targets:
  structural four (GAP-B, S12 middle line, S11 lexus + money phrases,
  S02 "baby, make"), C2-hook1, S18-tail hook, S08-gap words, S12-tail
  words, and the disclosed micro-gaps (see V6_ASSEMBLY_MAP_2026-11-04.md).
- Total new videos this task: 3 of 6. No retries used.

## Files

- `TAKE_WORDS_V6_VOLLEY17.json` (S07, S21 + frames record)
- `TAKE_WORDS_V6_VOLLEY17_S04A.json` (S04a unwarped + warped)
- `V6_SUPPLEMENTAL_QC2.json` (S05 warped, S13 t3 frame gate)
- `VOCAL_WINDOW_V6V17.json` (S07, S21 vocal windows)
- `qc_frames_v6v17/` (S07/S21/S04a/S13t3/S05w frames)
- Takes: `mv2_s07_v6final_t1.mp4`, `mv2_s21_v6final_t1.mp4`,
  `mv2_s04a_v6final_t1.mp4`, `mv2_s04a_v6final_t1_warped.mp4`,
  `mv2_s05_t6_warped.mp4`
- No commit, no ledger edit, no announcement, no posting, no delivery
  performed by this record. Assembly follows in
  `masters_work_v6/` + `V6_ASSEMBLY_MAP_2026-11-04.md`.
