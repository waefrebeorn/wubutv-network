# MV-8 — Crescendo Map (the edit's cut map)

Machine-readable version: `work/crescendo_map.json` (all 113 events with per-hit section tags, the full 0.5 s energy curve, per-section stats). Beat grid: `work/beat_grid.json`. Line times: `LYRIC_TIMELINE.md`.

## Headline numbers

- **Duration 187.200 s · tempo 123.05 BPM** (0.4876 s/beat, 368 beats, first beat 5.968 s)
- **113 cut events**: 33 **hit_major** + 78 **stab** (beat-quantized onset tiers) + 2 intro stabs
- **True peak: −2.16 dBFS @ 159.435 s** · **Loudest 0.5 s window: 174.75 s (−12.03 dBFS RMS)** — both in the instrumental Outro zone
- **Silence: only the 0.00–0.50 s leader.** The sheet's Drop [Silence – half bar] was **not performed** (see LYRIC_TIMELINE Dispute 1)

## Method

Onset envelope via librosa `onset_strength` (hop 256 @ 22050 Hz, uncapped — an earlier capped pass destroyed the ranking in loud sections and was discarded). Peaks clustered ≤0.12 s, then beat-quantized against the measured grid: **hit_major** = strength ≥ p90 (1.073) AND |Δbeat| ≤ 0.10 s AND local peak ≥ −6 dBFS; **stab** = strength ≥ p75 (0.804) AND |Δbeat| ≤ 0.12 s. Energy = RMS in 0.5 s windows, 0.25 s hop, over the track mp3 (dBFS). A prominence-based cross-check pass collapsed in loud sections and was discarded; a vocal-band phrase pass was unusable (brass saturates the vocal band).

**Caveats for the edit:** (1) tiering is beat-locked by design — in the loud 80–120 s stretch, off-grid stabs exist that fell below tier; if a cut point is needed there, the raw 679-event onset list is in `work/crescendo_raw.json`. (2) hit_major requires peak ≥ −6 dBFS, so quiet sections (Hook 1) structurally produce few majors — their stabs are real, just quieter; use the stab tier there. (3) Downbeats are [inferred] (weak phase margin) — cut on beats/hits, not bars.

## Macro energy curve (10 s block mean RMS, dBFS)

| 0 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 | 110 | 120 | 130 | 140 | 150 | 160 | 170 | 180 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| −25.2 | −21.0 | −19.6 | −19.5 | −16.9 | −15.7 | −16.1 | −16.9 | −16.3 | −17.9 | −17.2 | −16.4 | −14.9 | −14.6 | −14.7 | −17.7 | −16.7 | −14.7 | −23.0 |

One long build with local dips: the track gets louder almost monotonically from the Intro to the Final Hook plateau (120–150 s), dips at 150–160, peaks again 170–180, then decays. Section means tell the same story: Hook 1 −20.3 → Hook 2 −17.1 → Final Hook **−14.7** (loudest section mean).

## Sections — energy and hit density

| Section | Span | Mean RMS | Max RMS | Hits | Majors |
|---|---|---|---|---|---|
| Intro | 0.00–5.97 | −28.0 | −19.4 | 3 | 0 |
| Hook 1 | 5.97–34.40 | −20.3 | −18.1 | 16 | 3 |
| Interlude | 34.40–60.46 | −17.0 | −14.5 | 21 | 6 |
| Verse | 60.46–65.12 | −15.5 | −13.9 | 9 | 4 |
| Pre-Hook | 65.12–67.26 | −16.2 | −15.1 | 5 | 4 |
| Hook 2 | 67.26–105.94 | −17.1 | −15.4 | 12 | 5 |
| Drop | 105.94–120.40 | −16.5 | −15.0 | 5 | 0 |
| Final Hook | 120.40–146.00 | −14.7 | −13.7 | 14 | 0 |
| Outro (instrumental) | 146.00–187.20 | −17.3 | −12.0 | 28 | 11 |

Notable: the **Verse + Pre-Hook is the hit-densest chant passage** (14 events in 6.8 s, 8 majors) — the arrangement explodes exactly where the lyric gets specific. The **Final Hook has zero hit_majors** despite being the loudest section: its hits are big but sit slightly off the quantized grid (raw peaks −3.5 to −5 dBFS at 170–175 belong to the Outro cluster). Cut the Final Hook on the stab tier + RMS swells, not majors.

## The ramps

- **Intro build (0.5–5.97):** after the beat-1 stab (0.546), level climbs ≈ −33 → −20 dBFS steadily into the groove-entry pair 5.96/6.44. A true crescendo — the journey's launch ramp.
- **Pre-Hook build (60.46–67.26):** the sheet's [Building Snare] is real but modest in level (+~1.3 dB window means; the build is textural — snare + hit density: 9 events in the Verse alone). Don't expect a swell; expect thickening.
- **Drop strip (105.94–120.40): NOT a strip.** Level is flat (~−16.5 dBFS) start to finish — Suno kept the full groove running under the vocal gap. The only events: "Wipe…" 105.94, hit pair **112.25 / 112.72** ([Orchestral Hit] + "STILL THERE!" [inferred]), then quiet-until-Final-Hook at the hit cluster 121.42/121.78. If the edit wants a drop, it must manufacture it visually — the audio won't do it.
- **Outro decay (184.0–187.2):** −22.9 → −42.3 dBFS after the last stabs (~183.3). The track's only fade.

## Top hit_majors (strongest 15 of 33)

| t (s) | Strength | Peak dBFS | Section |
|---|---|---|---|
| 63.32 | 1.907 | −5.1 | Verse |
| 48.40 | 1.880 | −5.6 | Interlude |
| 46.46 | 1.787 | −5.4 | Interlude |
| 47.91 | 1.783 | −5.6 | Interlude |
| 63.81 | 1.701 | −5.1 | Verse |
| 64.76 | 1.655 | −5.4 | Verse |
| 173.77 | 1.609 | −4.6 | Outro |
| 171.85 | 1.598 | −4.8 | Outro |
| 61.87 | 1.554 | −5.8 | Verse |
| 48.88 | 1.546 | −5.4 | Interlude |
| 66.21 | 1.506 | −4.7 | Pre-Hook |
| 174.24 | 1.500 | −4.5 | Outro |
| 66.70 | 1.450 | −4.0 | Pre-Hook |
| 174.72 | 1.412 | −3.5 | Outro |
| 170.92 | 1.300 | −4.4 | Outro |

The single loudest stab-cluster in the track is **170.9–174.7** (Outro) — five majors in 4 s around the loudest window (174.75). The Interlude's 46.5–48.9 cluster is the other surprise peak. Full 113-event list with tiers and sections: `work/crescendo_map.json`.
