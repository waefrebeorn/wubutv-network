# MV-11 "Water hit my balls" — LYRIC TIMELINE (measured)

Track: 172.42s. Working grid: **131.5 BPM, period 0.456s, phase 0.070s** (autocorrelation flat 129.5–131.5; IOI 0.46s confirms). Sources: `analysis/SONG_WORDS.json` (full-clip, 92 words) + `analysis/SONG_WORDS_RECHECK.json` (split-half recheck of 100–172s and 55–72s). Dadaspec map: `analysis/track.jpg`.
Confidence tags: [confirmed] measured word onsets · [inferred] section label / sheet-derived boundary · [smeared] Whisper merged the rapid chant, onset approximate.

## Sections

| Section | Span | Words | Notes |
|---|---|---|---|
| Intro — cold open, single brass stab | 0–13.76 | none | [confirmed] quietest 2s at 0s (−27.1 dB); first word 13.76 |
| Hook 1 | 13.76–38.94 | "Water hits my balls" x3 + "When I poop it splashes" + "Balls balls" + "Splash back on the balls" | [confirmed] |
| Gap — brass/string hits, no vocal | 38.94–45.18 | none | [confirmed] no words in either pass |
| Verse | 45.18–50.14 | "Sitting on the toilet / Water hits / My balls" | [confirmed] ("Sitting" ASR "Sipping" — corrected) |
| Gap — building snare | 50.14–55.26 | none | [confirmed] |
| Pre-Hook | 55.26–57.56 | "Water hits / My balls" | [confirmed] |
| Gap — instrumental, wordless | 57.56–70.66 | none | [confirmed] BOTH passes agree: full-clip found nothing here; 55–72s recheck found 0 words (its 55.26–57.56 edge loss is a window artifact — full-clip onsets stand). 13s of music with no vocal: montage/visual stretch, not a gap to paper over. |
| Hook 2 | 70.66–101.78 | "Water hits my balls" x5 + "When I poop it splashes" + "Balls balls" + "Splash back on the balls" | [confirmed] onsets; [smeared] "balls" 72.34–76.68 and "hits" 78.34–82.78 are Whisper merges, NOT held notes |
| Drop | ~102–111 | "Water..." then silence half-bar, then "BALLS!" | [inferred] dadaspec dark band ~107s = the silence; first recheck word "Water" 110.70; the BALLS! shout is buried in the degenerate loop below |
| Final Hook | ~111–155.06 | "Water hits my balls" (repeated) / "When I poop it splashes" / "Balls balls" | [confirmed] anchors below; [smeared] Whisper fell into a degenerate "water" repeat loop 110.7–130.7 — those 100+ "water" tokens are NOT real word times, they are model loop. Usable anchors only. |
| Outro — last two stabs, cut clean | 155.06–172.42 | "Balls" + stabs | [inferred] from sheet; NO measured words in this span (both passes blank). Final "Balls" sits here unmeasured; energy stays hot to ~170s then fades. |

## Measured line onsets (song word times — the assembly anchors)

### Hook 1 [confirmed]
- "Water hits my balls" 13.76 · 17.72 · 29.32 (third occurrence starts 29.32; "boss" at 30.58 = "balls")
- "When I poop it splashes" 21.78 ("our"→"I")
- "Balls balls" chant 26.08–29.32 (five hits; trailing "done" 29.04 is spurious, NOT a lyric word)
- "Water hits my balls" 31.02 · 33.04
- "Splash back on the balls" 34.94 ("Dash"→"Splash") · "Balls balls" 36.94–38.94

### Verse [confirmed]
- "Sitting on the toilet" 45.18 · "Water hits" 47.18 · "My balls" 48.64–50.14

### Pre-Hook [confirmed]
- "Water hits" 55.26 · "My balls" 56.18–57.56

### Hook 2 [confirmed onsets, smeared durations]
- "Water hits my balls" 70.66 · 76.68 · 85.40 · 90.98 · 93.01
- "When I poop it splashes" 87.36
- "Balls balls" 89.40–90.66
- "Splash back on the balls" 94.88 ("Splashes"→"Splash") · "Balls balls" 96.92–101.78

### Drop + Final Hook (recheck anchors — use THESE, not the loop)
- Drop "Water..." ~110.70 [confirmed-ish, prob 0.028 — low, but the loop starts here]
- "Splashes" 129.98–130.68 [confirmed] (the "(Splash back)" tag)
- "Balls balls" chant ~131.82–134.92 [inferred] (ASR heard "The walls" — mishearing of the backing "Balls balls")
- "Water hits my balls" ~138.42–139.86 [confirmed] ("hit my balls" 138.42, prob 0.82)
- "Water hits my balls" ~141.36–143.64 [confirmed] ("What"→"Water")
- "When I poop it splashes" ~145.40–147.98 [confirmed] ("I'll put"→"When I poop")
- "Balls balls" 153.60–155.06 [confirmed]

### Outro [inferred]
- Final "Balls" + two brass stabs somewhere in 155.06–172.42; place by the stab transients on the beat grid (131.5 BPM from phase 0.07), NOT by Whisper — both passes blank here.

## What the plan must respect

- The song is a CHANT, not a sung narrative: "Water hits my balls" repeats ~15 times. Every occurrence gets its OWN take/cover — no reuse across positions (standing rule).
- Two long wordless stretches are STRUCTURAL features, not gaps: 57.56–70.66 (13s instrumental) and the Drop silence (~107s). They are montage/visual slots, built for pure visuals timed to the song.
- Final Hook word times after ~111s are anchor-level only (the loop killed per-word precision). The coordinator's swing measurement re-measures take audio per word; the master gate reads VISIBLE MOUTH EVENTS, not these anchors, for any sung slot.
- New standing directives (2026-11-09 ~22:04 EST): LESS singing characters looking at camera; REPLACEMENT VISUALS PACK when timing is bad (don't wrestle the warp); pure visuals timed to song + singing beats a weird talky; musical vibes.
