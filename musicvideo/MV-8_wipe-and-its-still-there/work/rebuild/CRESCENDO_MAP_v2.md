# MV-8 Rebuild — CRESCENDO MAP v2

Track: track.mp4 (187.2s). Beat grid: `work/rebuild/beat_grid_v2.json`
(VERIFIED 2026-11-08 — v1 grid re-measured, not re-derived).
Lyric onsets: `work/rebuild/SONG_WORDS_v2.json` + `LYRIC_TIMELINE_v2.md`.
v1 audio facts carried over (track unchanged): 113 cut events (33 hit_major +
78 stab + 2 intro stabs); only silence in the track is the 0.00–0.50 leader.

## The grid

- **Tempo 123.05 BPM** (0.4876 s/beat; median inter-beat interval and
  beat_track agree; onset-autocorr witness 123.05). **368 beats**, first 5.968.
- **Downbeats INFERRED — weak phase margin 0.002** (phase scores 364.0 / 364.8 /
  327.9 / 351.8). Downbeat list in beat_grid_v2.json is a hint layer only.
- **Lyric onsets are NOT beat-locked** (median |dt| 0.133s, 44/112 within
  0.10s). **Lyric onsets are the primary cut grid in the rebuild**; the beat
  grid is the hint layer for montage cuts (cuts land ON beats, return cuts
  land ON word onsets — swing-keyframe method).
- **Frame-exact contract: 4493 frames (187.2s @ 24fps).** v1 ran 4497f (+4f) —
  that class of drift is a FAIL in the remake.

## Sections (v1 boundaries hold; lyric content is new)

| Section | Span | Character |
|---|---|---|
| Intro | 0.00–5.97 | Cold open, single brass stab beat 1, gated drum hit. No words. |
| Hook 1 | 5.97–34.40 | Full groove. 7 lyric lines (L1–L7). First word 7.98, ~1.5s after the groove-entry hit 6.44. |
| Interlude | 34.40–60.46 | NOT on the sheet. 26.1s. Brown chant L8 at 36.90–41.84 (NEW), then no words; quiet first half 34.40–45.51 has no tiered events. |
| Verse | 60.46–65.12 | Thinner arrangement. L9–L10. Strongest hit in the track: **63.32s**. |
| Pre-Hook | 65.12–67.26 | Rising drums. L11 + "(Phantom)" tag ~65.60–66.42. |
| Hook 2 | 67.26–105.94 | Denser, chant-covered back half. L12–L19 + Drop shout. |
| Drop | 105.94–120.40 | Vocal gap (only the "Wipe" shout 105.94). Sheet's half-bar silence NOT performed — level flat ~−16.5 dBFS. Hit pair **112.25/112.72** = the "STILL THERE!" placement. |
| Final Hook | 120.40–146.00 | Loudest section (mean −14.7 dBFS) but zero hit_majors. L20–L26. |
| Outro | 146.00–187.20 | 41.2s instrumental. **Holds the track's true peak and loudest window.** No lyric lines. |

## The peaks (what the plan must land on)

- **TRUE PEAK: 159.435s, −2.16 dBFS (re-measured exactly, VERIFIED).**
  Sits in the Outro. **The biggest visual in the video — the loop-the-loop —
  MUST land here, frame-verified.** v1 missed it (loop landed ~147–148.5s).
  No lyric line is linked at the peak (Outro is instrumental — see
  LYRIC_TIMELINE_v2.md); the peak carries the biggest visual, not a word.
- **Loudest window: 174.75s. Loudest cluster: 170.9–174.7s.** The Colossus
  finale lands here.
- **Strongest single hit: 63.32s** (Verse, inside L9 "Sitting on the toilet").
- **Final Hook is the loudest section** (mean −14.7 dBFS) — the victory-lap
  energy peaks here, but the single biggest moment is still the Outro peak.
- **Outro shape:** 146.00–159.435 builds to the true peak; 159.435–170.9
  sustains; 170.9–174.7 loudest cluster (Colossus); 174.7–187.20 release to
  the loop seam (final frame rhymes with F00, seam inside the flush vortex).

## Cut events (v1 measurements, track unchanged)

113 events: 33 hit_major + 78 stab + 2 intro stabs. Accents in the v2 grid:
1242 total, 313 strong. Montage cuts land on beats; lyric cuts land on the
word onsets in SONG_WORDS_v2.json. Every sung line's onset is a cut or a
camera move — never a frozen frame under a word.

## What changed vs v1's map

1. True peak re-measured EXACTLY (159.435s) and promoted to a hard plan
   requirement with frame-level verification stated in SCENE_PLAN_v2.md.
2. Lyric onsets are now the primary grid (v1 had no word times before 60.46s).
3. Interlude gains a lyric anchor (L8 Brown chant 36.90–41.84) — its quiet
   half is no longer two unanchored long holds.
4. The Drop's missing silence stays a visual-manufacture job (no audio gap
   to cut on — the hit pair 112.25/112.72 is the accent).
5. Outro is confirmed instrumental (no lyric lines) — its scenes are staged
   purely on this crescendo map.
