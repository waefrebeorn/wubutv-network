# Banger proof examples — WORK NOTES (incremental, 2026-11-06)

Goal: two NEW 10 s proofs (1280×720, 24 fps, 16:9) in this dir.
Kinetic-type proof already exists/delivered — NOT redone.

## Shared setup
- Song/grid: MV-6 "Sell the Lemons", `MV-6_sell-the-lemons/work/beat_grid.json`
  (152.0 BPM, beat 0.3947 s, measured — tempo gospel, one clock).
- Window: Chorus 1, W = 44.489 s (first downbeat ≥ 44.2), 10.0 s slice.
  Beats in window: 26. Downbeats (rel s): 0, 1.556, 3.135, 4.691, 6.270,
  7.849, 9.405. Accents carry `strength` + `strong` flags.
- Audio: source `track.mp3` slice ONLY (never generated audio), muxed AAC.
- Renderer: Python PIL 10.2 + numpy, deterministic `renderAt(t)` per frame
  (Family G discipline), PNG sequence → ffmpeg. Scripts land in `../tools/`.
- Palette: COBALT #1B3FD1 · VERMILION #E23A1B · CADMIUM #FFC61E ·
  BONE #F4EEDC · INK #141414 · FOREST #1E4D33. Font: Noto Sans
  Bold/Black (house display family, same as kinetic proof).

## Proof 1 — Family B (audio-reactive visualizer / graphic system)
File: `visualizer_proof_16x9.mp4`
- B1: real spectrum bars + waveform computed from the track slice itself
  (numpy STFT on decoded PCM — sync intrinsic, picture IS the audio).
- B2: beat-reactive rings keyed to the measured grid — ring peak ON the
  beat frame; downbeat = larger ring + accent-colour cycle
  CADMIUM→VERMILION→COBALT→FOREST; sparks on `strong` accents.
- Status: PLANNED

## Proof 2 — Family I (countdown / listicle)
File: `countdown_proof_16x9.mp4`
- Lemon-empire top-5 countdown. Items land ON downbeats (rel s):
  5 @0.000 · 4 @1.556 · 3 @3.135 · 2 @4.691 · 1 @6.270 (holds to 10.0).
  5 ONE LEMON, ONE STAND / 4 JUICER DOUBLES THE TAKE / 3 CRATES BY THE
  DOZEN / 2 LIME LABS OPENS ITS DOORS / 1 $1.243 OCTOVIGINTILLION.
- Number slams with a real back-out spring (code type, G2 flavour);
  milestone label + palette accent bar per item; progress counter
  "n / 5" ticks ON each item onset; counted chips accumulate along the
  bottom; drawn lemon glyph pops on each increment. Base = slow
  procedural gradient drift (H2) — pixels move every frame.
- All type/graphics post-layer code render — zero generated text.
- Status: PLANNED

## Critic loop log
- (pending first renders)
