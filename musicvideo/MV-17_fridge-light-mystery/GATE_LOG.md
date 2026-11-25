# MV-17 "Fridge Light Mystery" — GATE LOG (final, 2026-11-13)

## House master
- Path: `masters/mv17_fridge_light_mystery_16x9.mp4`
- **md5: 844dde83a366c412aed4268fb7c8dca4** — 105,680,219 B
- ffprobe: h264 1280×720 @ 24fps, **3908 frames**, duration **162.833s**
  (track 162.816s — inside ±0.5s), AAC 48k stereo, **faststart: yes**
  (moov before mdat), **x264 SEI crf=18.0** (verified by annexb extract;
  gates.py's own SEI parser missed it, direct extract reads crf=18.0).

## Correction on record (superseded encode)
The first completed master file (md5 959e42691be07ec70257da81f6791e7b,
233,797,743 B) probed at only **94.667s / 2272 frames** and was REJECTED —
never shipped. Cause: overlapping assembly runs — that encode was produced
by the earlier assembly pass reading a joined.mp4 that the next pass was
concurrently rewriting. The concat source itself was never short:
work/joined.mp4 probes 3908f / 162.833s, and all 34 segments verify on disk
at 3908 frames total (work/segments/segment_verify.json). The delivered
master above was encoded cleanly from that verified joined.mp4 in a single
uninterrupted pass and re-probed end to end.

## Gates (measured, work/analysis/gates.py + work/qc/gates.log)
- **Master-audio agreement** (master AAC vs track.mp3): global correlation
  **0.99885**, worst-10s window **0.99802** — the master audio IS the Suno
  track (AAC encode, never MP3-in-MP4).
- **Motion audit**: near-dup enumeration on the pre-grain master — **no
  performed line has a ≥24f near-dup run during its words** (PASS). Longest
  runs overall sit in the pre-vocal intro (0–3s, the slow door-crack open,
  max 36f) where no words play. ZOOM push-in repairs on S16/S19/S20 brought
  their in-line runs to 16f / 3f / 20f.
- **G7 wrong-lyric gate**: every shipped sung take scored overlap 1.0
  against its scene-plan words (take ASR in work/qc/, verdicts in
  TAKE_HISTORY.md).
- **Warp law**: phrase-level smooth warps only; slowest slowdown 0.548
  (cap 0.5); fastest speedup 1.60 (S12, grey-ceiling, disclosed).
- **Visual gate**: PASS with disclosed notes — VISUAL_GATE.md.

## Chat copy
- Path: `masters/mv17_fridge_light_mystery_16x9_chat.mp4`
- **md5: 80795f6e2603b14b2ca020b8d34c00bf** — 42,144,965 B (≤50 MB)
- Same cut: 3908 frames, 162.833s, h264 1280×720 @24, **AAC audio copied**
  from the house master, faststart. Bitrate-capped delivery encode
  (b:v 1900k / maxrate 2100k) — disclosed as such.

## Disclosed flaws (plain)
1. **S19 costume flaw**: he wears a plain blue pajama top for the whole
   3.82s scene — the 8.2 costume-snap event failed twice (generator renders
   the end-state costume throughout). Words land (warp 0.613); the scene
   plays as the count motif.
2. Grey-ceiling warps: S12 at 1.60, S32 at 1.483, S07 single-window 1.372
   (phrase 1's mouth finishes early inside it; he holds the knock pose).
3. Fridge-door crack texture inherited from the reference stack reads on
   the door through the crouch-shot takes.
4. S18 is an intentional one-scene palette break (The Spread event);
   S16/S20 are designed low-motion scenes (zoom-repaired, gate-verified);
   S22's string web reads lighter than planned.
