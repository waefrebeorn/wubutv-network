# Graphics Overlay Notes — kinetic type in POST (ffmpeg/ASS)

Built 2026-11-06. Tool: `tools/kinetic_ass.py` (plain python3, stdlib only).
Proof: `proof/kinetic_proof_16x9.mp4` — MV-5 take `takes/mv5_s01_t1.mp4`
(10.0s, 1280×720, 24fps) + words 0–10.2s of MV-5 `SONG_WORDS.json`, preset
MIXED (one preset per line, cycling), burned with
`ffmpeg -vf ass=...`. Proof md5 `570e4ffdca5077c31feb546483326eed`,
240 frames, 1,856,094 B, video-only. Per-preset .ass files sit beside it in
`proof/` (kinetic_SLAM/CASCADE/HIGHLIGHT/STACK.ass).

Doctrine: type and graphics are a POST layer, never generated inside clips.
The generator makes picture; this tool makes words fly on the song's own
word grid (tempo gospel — onsets come from SONG_WORDS.json, not from a
fixed interval).

## Motion, specified numerically (code-motion discipline)

Stagger is not a constant in any preset: **the stagger IS the song's
word-onset grid.** Each word's move starts at its measured onset, so
stagger values are whatever the singer sang (proof line I01 onsets:
1.66 / 2.22 / 2.78 / 2.96 s → staggers 0.56 / 0.56 / 0.18 s). Move
durations below are at 24 fps (1 frame = 41.7 ms).

| Preset | Move | Duration | Easing feel | Notes |
|---|---|---|---|---|
| SLAM | scale 300%→100% (`\fscx/\fscy`), alpha punch-in | 150 ms ≈ 3.6 f (alpha 0–60 ms, settle 60–150 ms), out-fade 90 ms | hard attack, fast decel settle — a "back-out"-style hit approximated in 2 segments | word holds to next onset; color alternates BONE/CADMIUM |
| CASCADE | `\move` 420 px horizontal into slot, alternating L/R by word index | 200 ms ≈ 4.8 f per word | linear slide with 60 ms fade head — reads as ease-out because distance is fixed and short | line builds cumulatively, all words hold to line end |
| HIGHLIGHT | active word scale 112%→100% (`\t`), CADMIUM over dim BONE line | pop 90 ms ≈ 2.2 f; dim layer fade-in 120 ms, out 150 ms | quick overshoot pop, no travel | full line present whole span; pop lands exactly on the sung word |
| STACK | scale 40%→100% + fade, one word per row | 130 ms ≈ 3.1 f per word; row pitch 67.5 px (1.25 × 54 pt) | soft grow-in | line builds downward; final word CADMIUM, rest BONE |
| Accent bar (all presets) | `\p1` rectangle, `\move` 260 px slide-in | 220 ms ≈ 5.3 f | linear slide | 7 px tall, width = line width (min 120 px), color cycles CADMIUM→VERMILION→COBALT→FOREST per line |

Palette (styles + accents): COBALT #1B3FD1, VERMILION #E23A1B, CADMIUM
#FFC61E, BONE #F4EEDC, INK #141414 (outline/shadow), FOREST #1E4D33.
Font: Noto Sans bold 54 pt at 1280×720, INK outline 4.

ASS tags used: `\move` (CASCADE travel, accent-bar slide), `\fscx/\fscy`
(SLAM/STACK/HIGHLIGHT scale), `\t(t1,t2,...)` timed transforms for every
settle, `\fad` in/out, `\pos` + `\an4/\an5/\an7` anchoring, `\alpha`,
`\1c` + `\p1...\p0` vector drawing for the accent bar, layered events
(0 = accent, 1 = dim line, 2 = words).

## Frame-verification (the audit loop)

Frames extracted at word onsets from the rendered proof and inspected —
extract → look → fix → re-render, twice:

- f_2.0 (SLAM, "Easy" @ onset 1.66): word visible lower-third, CADMIUM
  accent bar under it. PASS after fix 1.
- f_4.3 (CASCADE, "We ride"): both words landed in slots, VERMILION bar
  under. PASS.
- f_6.3 (HIGHLIGHT, "Easy now easy now"): "Easy" in CADMIUM exactly on
  its slot, remaining words dim BONE, COBALT bar under. PASS after fix 2.
- f_9.2 (STACK, "Till the morning comes"): four rows stacked, "comes" in
  CADMIUM, FOREST bar under. PASS.

Fixes the audit caught (both invisible without looking at frames):
1. Accent bar rendered at the TOP of frame — a `\pos(0,0)` on the drawing
   event fought its `\move`. Dropped the `\pos`; bar now sits at
   line_y + 34 as specified.
2. HIGHLIGHT garbled at line boundaries — (a) previous line's events
   bled 0.45 s into the next line, and (b) the CADMIUM overlay was
   positioned from a char-width estimate while the dim full line was
   laid out with real font metrics, so pops drifted off their words.
   Fixed by clamping every line's end to the next line's onset, and by
   rendering the dim line as per-word events at the same computed slots
   as the pops. Slot math is now self-consistent everywhere.

## Limits hit

- libass `\t` interpolation is a power curve (optional accel exponent),
  not GSAP-style named easings or springs — no overshoot/bounce physics.
  SLAM's "settle" is two linear segments faking a back-out. For true
  springs/eases, the road is a code-rendered layer (GSAP/Remotion-style)
  composited as video, with ASS for the high-volume word work.
- Char-width slot estimate (0.52 × fontsize per char) is approximate:
  inter-word spacing in HIGHLIGHT/CASCADE reads slightly wide vs real
  font metrics. Fine for bold display type; measure per-font before
  using small sizes.
- ASS has no per-letter animation, no rotation inertia, no blur trails.
  Kinetic ambition beyond slides/scales/pops belongs to the code layer.
- One proof take is a static framing; on moving footage the lower-third
  slot (y = 0.80 × H) can collide with faces/action — placement per
  scene belongs in the assembly plan, not the tool default.

## How this composes in a real MV assembly

Three layers, composited in POST in this order:

1. **Picture layer** — generated takes, placed and per-word time-warped
   per Slopcannon WORD-SYNC (song is the only audio; generated audio
   dropped). Sung lines get sung picture; covers stay closed-mouth.
2. **Type layer** — this tool. One .ass per section, preset chosen per
   section energy: HIGHLIGHT for lyrical passages (words support the
   singer, don't compete), SLAM for hook hits and downbeats, CASCADE
   for fast/rap passages (montage sections — words can fly because the
   picture is already cutting), STACK for list-like or building lines.
   Burned in the same ffmpeg pass as captions (or as its own pass when
   a section mixes caption + kinetic roles — keep the plain caption
   track for sung lines the type layer doesn't carry).
3. **Graphic accent layer** — the palette bar today; the same ASS
   drawing route extends to boxes, counters, HUD ticks. Anything
   richer (cards, 3D, shader motion) is a code-rendered video layer
   dropped between 1 and 2, timed on the same word/beat grid.

Assembly order of operations: place picture → generate type .ass from
SONG_WORDS.json with the section's preset map → burn → extract frames
at word onsets → audit (words visible, on the right word, no bleed
across lines) → fix → re-render → gate the master as usual.
