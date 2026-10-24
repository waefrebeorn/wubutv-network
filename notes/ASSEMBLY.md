# Outlet assembly spec (2026-10-12)

## Units
- **UNIT** = one finished 10s piece (episode, bumper, or commercial),
  1280x720, h264, native audio.

## Blocks
- **Episode block** = 75 consecutive units = **12.5 minutes**.
- **Commercial pod** = 15 commercials = **2.5 minutes**.
- **Outlet block** = episode block + commercial pod + episode block +
  commercial pod = **30 minutes** (180 units).

## Assembly method
- `ffmpeg -f concat -safe 0 -i <filelist> -c copy <out.mp4>` — stream copy,
  no re-encode, no quality loss.
- All units are already 1280x720/24fps/10.0s with matching codecs, so
  concat demuxer output decodes cleanly.
- Commercial pods: seeded at ~2/3 slots with bumpers until the AD inventory
  holds 15+ finished commercials; then full 15-commercial pods.
- Each assembly ships with a unit-list doc (`outlet/BLOCK_<X>_UNITS.md`)
  naming every unit file in order, plus duration and hash verification.

## Loudness
- Individual units ship at native levels (never loudnorm-boosted).
- Per-block normalization is applied at assembly time only, to a
  documented target, with the applied gain recorded in the unit-list doc.
- True-peak hot units are static-attenuated before concat; the pass is
  recorded.

## Block A (2026-10-12)
- `outlet/block_a_12m30s_episodes_v1.mp4` — 75 episode units in
  channel-rotation order (NEWS, ORIGINALS, SATIRE, LABS, MEDIA SCHOOL,
  PUBLIC ACCESS, PUPPET THEATER, NETWORK, ARCHIVE). Episodes only:
  no bumpers, no commercials.
- Unit list: `outlet/BLOCK_A_UNITS.md`.

## Chapter architecture (2026-10-13 — from the @clipcraft7 structural study)

All findings below are INFERRED FROM STRUCTURE, not observed practice:
@clipcraft7 publishes nothing about their workflow (no tools, prompts, or
process are public). What transfers is the shape, allegorically reworked
for WuBuTV's own tools:

- **Chapters, not unit sequences.** Every 75-unit episode block gets named
  chapters (e.g. "The Ledger Opens", "The Second Ask", "Hours: Never") —
  a block with chapter names navigates better than 75 anonymous units.
  Each chapter = one channel-rotation pass (9 units) or one lore beat.
- **Serialization with cliffhangers.** Numbered parts released as teasers;
  arcs continue rather than stand alone. The network already has the lore
  for this (the Kept Gap, the ledger, the Second Ask, UNC's unchanging
  stance); the move is deliberately planting continuations the way the
  network has been planting callbacks. Max one callback per bumper still
  holds; a continuation plant counts as the bit.
- **Teaser → compilation funnel.** Short clips up front, longer
  compilations as the destination. The 12.5-minute blocks are the "full
  story" versions of what's been running as tens; the 30-minute outlet
  block is the long-form destination.
- **Recurring named universes.** Same characters, new situations. The
  lore-accumulation work (canon compendium, CONTINUITY_WEB callbacks,
  the Colonel's codec arc) is the model — name it and lean into it.
- **Near-zero caption overhead.** The clip is the message. Already how
  the announcements run; no change.
- Explicit rejects from the study: licensed-clip repurposing, slop-volume
  without QC, engagement-bait CTAs, overlay caption/music templates,
  reply-guy tactics. None of these enter the pipeline.
