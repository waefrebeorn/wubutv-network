# MV-7 OTAKU REBUILD — notes (2026-11-07)

User rejected the hobo build completely 2026-11-07 ~05:47 EST ("creepy and no timing").
Rebuilt from zero per MV7_OTAKU_REBUILD_BRIEF_2026-11-07.md: THE NOBODY MAN as a bright
weeb otaku (mid-20s, round glasses, cadmium front streak, cobalt star hoodie, cat-ear
headphones at neck) in a bright cozy fan room; the small flame = tiny glowing star lamp;
eras A→B→C (room fills; final chorus = screen-wall kingdom, final frame rhymes with first).

## Deliverables
- masters/mv7_im_the_nobody_man_16x9_otaku.mp4 — house master, CRF 18, 1280×720, 24fps,
  4493 frames, 187.2s, AAC 48kHz sole audio = user track.mp3 (md5 c660e81b0811cf2240c0e33992b03aa7),
  kinetic HIGHLIGHT lyric layer burned in post. md5 c89c4757928a31b95ada25928d498020, 70,748,889 B.
- masters/mv7_im_the_nobody_man_16x9_otaku_50mb.mp4 — chat copy, video bitrate-capped,
  AAC copied untouched. md5 7b3de18be0ead36b2b752838f10f0a98, 45,326,972 B (≤50 MB).

## Build
- 3 era anchor stills (refs/otaku_eraA/B/C.webp) generated + visually verified (identity,
  star lamp, generic figures, plain spines, abstract posters, zero readable text).
- Plan: MV7_OTAKU_PLAN.md — 40 units U01–U40, line-level (1–2 lines/take, every hook fresh).
- 46 generations total: 40 t1 takes + 6 completeness rerolls (t2 for U01/U19/U24/U34/U35/U39,
  whose t1 takes missed a line or the ×2 chant). All takes ffprobe-verified on disk by the
  coordinator (child-reported md5s proved unreliable twice; disk governs).
- Assembly (work/otaku_assemble.py): per-unit phrase-smooth warp of the take's measured sung
  span onto the song's sung span; tails at natural speed or held (word-free by construction);
  bridge U28–U30 = beat-region montage takes; kinetic layer from SONG_WORDS.json via
  visual-forms/tools/kinetic_ass.py (HIGHLIGHT, cadmium pop 2 frames before each onset).
- Warp extremes: slowest 0.785 (U37), fastest 1.742 (U06) — speedups disclosed, no interval
  slowed past the 0.5 floor. One fallback anchor: U33 (take truncates the final word "ma-").

## Gate on the rendered master (work/otaku_gate/)
- ffprobe: h264 1280×720 24fps, 4493 frames exact; audio AAC 48kHz; x264 SEI crf=18.0. PASS.
- Kinetic audit: cadmium highlight present at 24/24 sampled word onsets; clean before/after
  rise on 18/24 (the other 6 are mid-line words whose predecessor's highlight was still up).
- Mouth gate (visual read of onset sheets at onset / +0.167s / +0.33s, 61 sung line onsets;
  6 bridge montage onsets excluded): open/transitional at the exact onset frame 30/61;
  by +0.167s 39/61; by +0.33s 48/61. DISCLOSED RESIDUAL: 13 onsets stay closed through
  +0.33s — concentrated in the held-note chant takes (U01 start, U02, U15, U16, U17) where the
  performer smile-holds sustained "Nobody Man" notes, plus hooks in U24/U27/U35/U37/U39 and
  U31's settle line. Anchors are measured take-audio word times; visible mouth events lag
  them in those takes. This is the build's known weakness, stated plainly — the user's
  playback verdict governs, and a mouth-event correction pass (MV-3 method) is the fix if ordered.
- Motion gate: one 32-frame near-dup run at ~75.5s, inside U17's held final chant note
  (overlaps the song's sustained "man", 72.34–75.84s). All other word spans pass (<24f). DISCLOSED.
- Content gate: identity/room/no-text verified on take sheets + master onset sheets across
  all three eras; no stubble/thinning/tired/creepy traits; no licensed characters; star lamp
  present in all eras; Era C screen wall with one brighter light.

## Other disclosures
- U20's take is guitar/room close-ups with no face — its two lines (V2.5/V2.6) are carried by
  the kinetic layer over a cover shot, not a sung mouth.
- U40's take returned 5.04s against the 10s request; the word-free outro tail is held/slowed
  to fill the 8.9s unit (no words after 183.24s).
- Take aspect drift (1248×704, 1152×768, some 1280×720) — all segments scale/cropped to 1280×720.
- FC.10 lyric ("Yeah, I turn the small things grand") follows the lyric sheet; the timeline
  marks it [uncertain] — kinetic text uses the sheet wording.
- Era stills: eye colour drifts (brown A/C, blue B) — accepted nit.
