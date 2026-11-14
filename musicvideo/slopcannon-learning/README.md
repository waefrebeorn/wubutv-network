# Slopcannon Learning Folder

Scraped 2026-11-01 from slop.cc (Director's Wiki + FAQ). This is WuBu's study
library for the Slopcannon engine — mechanics only, SLERM-transformed, never
copied. Slop.cc's own guides carry this caveat on every page: the references
support definitions and technical context; the example directions and production
advice are Slopcannon's editorial synthesis, and "available controls and results
depend on the workflow." That caveat is the whole reason file 08 exists.

## Contents

- `01-wiki-index.md` — the full 134-guide inventory, shelves, and the
  Inside-the-Cannon shelf in detail.
- `02-lip-sync.md` — lip-sync, phonemes/visemes, and AV-sync diagnosis,
  distilled from three guides.
- `03-prompting.md` — AI video prompting: one readable event, one factor at
  a time, audio direction separate from visible action.
- `04-consistency-and-bank.md` — character consistency + the reference bank.
- `05-project-machine.md` — the product itself: Create vs Studio, timeline,
  volley, credits, rerolls, agents, own-footage, captions.
- `06-music-video-craft.md` — music-video + performance-video guides: visual
  proposition, section mapping, recurring vocabulary, restraint.
- `07-bone-posts-and-claims.md` — the user-supplied sauce (bone's posts as
  relayed), with verification status per claim.
- `08-wubu-transfer.md` — what transfers to WuBu's prompt-only pipeline, what
  does not, and what is downgraded to staging hygiene.
- `sources.md` — every URL fetched, when, and its page status.

## How this folder relates to the engine

The engine at `~/workspace/custom-skills/slopcannon/` already encodes the
transferable rules (timeline-first, performance-window staging, keep-hits,
diagnose-before-reroll, captions in post, no peak-tween ever). This folder is
the evidence behind those rules and the place new learning lands. When a new
Slopcannon source arrives, distill it here first, then patch the skill — never
the other way round.

## Confidence tags used throughout

- [confirmed] — stated on a fetched slop.cc page or in the FAQ.
- [index blurb] — stated only in the wiki index summary line, full page not
  fetched this run.
- [user-supplied] — from the sauce text the user relayed; not independently
  located on 2026-11-01.
- [unverified] — claimed somewhere, no supporting source found this run.
- [does-not-transfer] — true of Slopcannon's product, false of WuBu's
  prompt-only media tool; see file 08.
