# WuBuTV — network repository

**Identity:** WuBuTV. **"B — A Foundation."**
**Conceit:** the room was real, the crowd was generated, and this is the paperwork.
**Flagship:** @WuBuOriginals.

The whole network runs on one unit of time: **ten seconds**. Every piece —
bumper, episode, commercial — is one genuine 10-second scene, 1280x720,
16:9, with native audio only. Never dubbed, never re-encoded when stitched.

Sole showrunner: **WuBu**. (MovieAgent, former co-producer, went dark
2026-10-06; WuBu has directed, generated, QC'd, assembled, and shipped
everything solo since 2026-10-11.)

## The 10-second doctrine

One piece = one beat. Setup and payoff inside 10s. The beat lands at 4–6s.
The premise reads from a silent frame. One directed line maximum.
UNC never reacts: no smile, laugh, nod, head shake, eyebrow raise,
double-take, or shock. **A nod counts.**

## Standing rules

- 10s scene, 16:9, 1280x720. Native audio only — never dub TTS over
  native speech. Commentary is editing, never overdub.
- Quiet room tone ships at native levels; never loudnorm-boost to −14 LUFS.
  If true peak exceeds −1 dB, apply one static attenuation pass only.
- Real motion only. No licensed characters, footage, or meme templates.
- Diegetic text only, spelled exactly. Never put version tokens, slate
  numbers, or character labels in prompts.
- `INF:0` / `∞:0` stays stable and legible in every wide.
- UNC = heavyset Black man, large rounded afro, thick mustache/goatee,
  BLACK hoodie with the wordmark `~ WuBu ~` in YELLOW/GOLD letters.
  **The tildes are the wordmark.** Missing/changed tildes, respelling,
  restyling, or dimming = HARD QC FAIL: re-fire once; if the re-fire
  also drifts, the piece does not ship.
- Colonel = stocky, grey/white beard, navy dress uniform, news desk,
  grave and composed. The irony lives in the words; deadpan is wrong for him.
- Corner bug on every bumper/commercial: `~ WuBu ~` over `WuBuTV`.
- Shipped numbers are facts; a number with a finished clip behind it is
  never renumbered and never re-shot.
- Verify footage against its scene description before acceptance.
- Ship honest nits in the ledger; never ship a rule-break silently.

## The nine channels

1. NEWS — @WuBuNews. Straight-faced deadpan news. (The Colonel's world:
   ∞:0 is real to him, meaningless to the viewer.)
2. ORIGINALS — @WuBuOriginals. Flagship. Dread, lore, paperwork. (H-1 is
   an Originals horror ident.)
3. SATIRE — @WuBuSatire. Administration. Satire's UNC does the
   paperwork; Originals' UNC does the dread.
4. LABS — @WuBuLabs. Experiments, measurement, ritual.
5. MEDIA SCHOOL — Media School. Instruction in the deadpan craft.
6. PUBLIC ACCESS — caller-driven lore. (Laura is the only non-deadpan
   character: she reacts; the contrast is the engine.)
7. PUPPET THEATER — skeletons, the rink, the coach.
8. NETWORK — channel idents, the codec series, scoreboard.
9. ARCHIVE — the ninety days, the shelved, the mis-shelved.

There is no tenth channel. The Control Voice is network furniture, not a channel.

## Coherence contract

The network's public checkable promise — Era II, effective 2026-10-21:
[COHERENCE_CONTRACT.md](COHERENCE_CONTRACT.md). Native audio only, never
dub, one callback max, cast lock, wordmark gate on every UNC frame,
retirement is filing, a number with a finished clip behind it is a fact.
Scored per outlet block, published even when the number is bad.

## Production wheel

Four quadrants, running without human input (cron schedules):

- **Q0 research** (hourly, `:00`) — Kevin Bacon six-degree associative
  research into `ideas/IDEAS_BANK.md`. Standing studies: the art of 10
  seconds; meme literacy. World-expansion quotas: new settings, plot
  spines, lore, motifs, verb-driven action.
- **Q1 pre-production** (hourly, `:15`) — drafts 12 FIRE-READY 10s bumper
  prompts + episode voice stages into `slate/PREPRO_<ts>.md` from the
  `[READY]` bank (FIFO), reading `LEARNING_LOG.md` first.
- **Q2 bumper factory** (every 15 min) — fires 3 bumpers/run (12/hr),
  continuous, no cap. Claim files (`slate/CLAIM_*.json`) prevent
  overlapping runs from double-shooting.
- **Q3 episode factory** (every 2h, `:45`) — fires 3 single-take 10s
  episodes/run. Continuous past 100 (user ruling 2026-10-12).

Plus a **commercial cadence** on the factory wheel: AD-series 10s spots for
network-native fictional sponsors (see `notes/COMMERCIALS.md`).

## Directory layout

```
wubutv-network/
  README.md                this file
  EPISODE_LEDGER.md        episode ledger (row per shipped episode)
  LEARNING_LOG.md          recursive lessons (factories append; pre-pro reads)
  slate/                   BUMPERS.md (bumper ledger), PREPRO_*.md drafts,
                           AD_SLATE_*.md commercial drafts, CLAIM_*.json
  ideas/                   IDEAS_BANK.md (banked research)
  notes/                   CANON.md COMMERCIALS.md ASSEMBLY.md PRODUCTION_WHEEL.md
  bumpers/                 shipped bumper masters bNNN_slug_16x9.mp4
  commercials/             shipped commercial masters adNNN_slug_16x9.mp4
  news/ originals/ satire/ labs/ mediaschool/ publicaccess/
  puppet/ network/ archive/  — shipped episode masters per channel
  outlet/                  assembled outlet blocks + unit lists
  takes/                   raw intermediates (git-ignored)
  masters/ qc/ audio/ rules/ continuity/ — legacy production dirs
```

## Assembly spec (outlet)

- **UNIT** = one 10s piece.
- **Episode block** = 75 units = **12.5 minutes**.
- **Outlet block** = [12.5-min episode block] + [2.5-min commercial pod = 15
  commercials] + [12.5-min episode block] + [2.5-min commercial pod] = **30 min**.
- Assembly via `ffmpeg` concat demuxer (stream copy, no re-encode).
- Loudness normalized per block at assembly time to the documented target.
- Spec details: `notes/ASSEMBLY.md`. Block A: `outlet/`.

## Backup / GitHub

This repo is push-ready. It has no remote yet; to publish:

    git remote add origin <url>
    git push -u origin main

Videos are the network's masters and ARE tracked (deliberately — this is
the backup). Only `takes/` (raw intermediates) is ignored.
