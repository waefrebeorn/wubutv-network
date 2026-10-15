# Production wheel — operations (2026-10-12)

## Quadrants
- **Q0 ideas-research** — hourly `:00`. Kevin Bacon six-degree chains,
  3+/run, multiple sources. Banks 6–10 items to `ideas/IDEAS_BANK.md`
  (6 `[READY]`). Standing studies: the art of 10 seconds; meme literacy.
  World-expansion quotas per run: 3+ outside-cluster settings, 2+ plot
  spines (want/obstacle/turn), 1+ lore item, 1+ motif candidate,
  verb-driven action beats.
- **Q1 pre-production** — hourly `:15`. Drafts 12 FIRE-READY 10s bumper
  prompts + episode voice stages into `slate/PREPRO_<ts>.md` from oldest
  `[READY]` bank items (FIFO). Reads `LEARNING_LOG.md` FIRST. Max 4/12
  from any one setting cluster. Prompts omit character labels
  (never render as diegetic text).
- **Q2 bumper factory** — every 15 min. 3 bumpers/run = 12/hr, continuous,
  no cap. Numbers claimed FIRST via `slate/CLAIM_<ts>.json` (runs overlap).
- **Q3 episode factory** — every 2h `:45`. 3 single-take 10s episodes/run.
  Continuous past 100 (user ruling 2026-10-12).
- **Commercial cadence** — AD-series 10s spots drafted to
  `slate/AD_SLATE_<date>.md`, fired on the factory wheel between bumper
  batches.

## QC gates (every piece, before acceptance)
1. 10.0s, 1280x720, zero decode errors.
2. Footage verified against its scene description (O-7 lesson).
3. Hoodie wordmark `~ WuBu ~` glyph-by-glyph — HARD FAIL on drift;
   re-fire once; if the re-fire drifts, do not ship.
4. Corner bug `~ WuBu ~`/`WuBuTV`, plain white, bottom-right, every frame.
5. UNC never reacts (nod counts). Mouth moves only on directed lines.
6. Native audio; peaks > −1 dB get ONE static attenuation pass.
7. Honest nits in the ledger; never ship a rule-break silently.

## Ledger rules
- A number with a finished clip behind it is a fact — never renumber,
  never re-shoot.
- Rows: BUMPERS.md (bumpers), EPISODE_LEDGER.md (episodes), adNNN ledger
  (commercials — `slate/BUMPERS.md`-style rows in COMMERCIALS notes).
- Unshot-with-cause numbers return to the pool; re-fires not burned by
  pipeline denials are restaged, never blindly retried (B-426 rule).
- CLAIM files are deleted when the run completes.

## Recursive loop
- Factories append one line per lesson to `LEARNING_LOG.md`.
- Pre-production reads it before drafting. The loop is the learning.
- Be the best, be the loop, be the learning.
