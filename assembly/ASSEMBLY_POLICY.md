# WuBuTV Episode Assembly Policy

Long-form WuBuTV episodes are assembled from the 10-second network-native units
(bumpers, commercials, episodes) by the concat platform (`assemble.sh`).
No re-encode: every unit ships h264 + aac, 1280x720, ~10.0s, so assembly is a
stream copy — fast, lossless, one frame-accurate seam per unit.

## Formats and numbering

| Code | Duration | Units | Filename prefix |
|------|----------|-------|-----------------|
| E1M  | 1 minute | 6     | `e1m_<NNN>_<slug>_16x9.mp4` |
| E2M  | 2 minutes| 12    | `e2m_<NNN>_<slug>_16x9.mp4` |

Numbers run E1M-001, E1M-002, ... and E2M-001, E2M-002, ... independently.
The ledger (`ASSEMBLY_LOG.md`) is the source of truth; a number with a finished,
QC-passed file behind it is a fact.

## Title format

`"<Slug phrase>" — WuBuTV <N>-minute episode. ~ WuBu ~`

Example: `"The Shifted Weights" — WuBuTV 1-minute episode. ~ WuBu ~`
The title is embedded as the mp4 `title` metadata tag.

## Sequencing rules (binding)

1. **Alternate energy.** No two adjacent units may carry the same mood register
   (e.g. two slow paperwork beats back-to-back). Order units by contrast:
   UNC-beat, lore object, comedy turn, UNC-beat, ...
2. **No same-subject adjacency.** No two adjacent units with the same subject
   type (two clocks, two doors, two lamps). If the pool forces it, insert a
   commercial as a buffer.
3. **Commercials can bookend.** A 2-minute episode may open or close with a
   commercial (AD series) — never sandwich one between two bumpers of the same
   setting.
4. **Episodes open cold.** A 1-minute episode opens on a bumper, not a commercial.
5. **UNC identity carries.** At least half the units in any assembly must pass
   the UNC wordmark rule at their own QC — the `~ WuBu ~` hoodie must read
   through the whole minute.
6. **Never licensed material.** All inputs are WuBuTV-native (bumpers/,
   commercials/, network/). No third-party footage, no licensed meme templates.

## Destination platforms (user ruling 2026-10-18)

E1M and E2M episodes post to **Instagram Reels** (supports up to 3 min) and
**TikTok** (supports up to 10 min). No YouTube — the long-form effort serves
the two short-form platforms' longer slots. Same 16:9, same specs, same
`~ WuBu ~` identity.

## The two editorial identities (user ruling 2026-10-18)

The 1-minute and 2-minute episodes are NOT the same style of clips. Each has
its own queue, its own reserved units, its own editorial voice:

- **E1M — THE RAPID MINUTE** (queue: `assembly/E1M_QUEUE.md`): punchy,
  high-contrast, comedy-forward. Six units, sixty seconds, no breathing room.
  Every unit lands a beat or a turn. Built for scrollers.
- **E2M — THE SLOW BUILD** (queue: `assembly/E2M_QUEUE.md`): lore-heavy,
  atmospheric, sustained mood. Twelve units, two minutes, one unbroken
  atmosphere. Units accumulate like chapters. Built for watchers.

## No-reuse rule (registry-enforced, user ruling 2026-10-18)

A 10-second unit is NEVER used in more than one assembly. The clip registry
(`assembly/CLIP_REGISTRY.md`) is the enforcer: E1M-used and E2M-used are
mutually exclusive columns. Assemblers MUST check the registry before firing —
a unit with either column dated is ineligible, full stop.
(E1M-001/E2M-001 are grandfathered: they share 6 units from before this rule.)

## Queues are the source of units

Assemblies pull units ONLY from `E1M_QUEUE.md` / `E2M_QUEUE.md` — never ad-hoc.
Each queue holds reserved B-numbers in assembly order. The assembler consumes
from the top (6 for E1M, 12 for E2M) and refills from the freshest unposted
bumpers, excluding: registry-flagged units (E1M/E2M-used), IG/TT-posted units,
and anything reserved in the OTHER queue.

## Recycle (user ruling 2026-10-18)

A unit's hot-storage life ends when it is IG-posted AND CDN-backed (both dates
in the registry). The daily recycle sweep moves those files to `recycle/`
(filesystem move, not copy), updates the registry's Recycled column and File
path. Queued/reserved units are never recycled. TT-posted is a bonus, not a
requirement.

## Assembly cadence

- New assemblies draw from the newest unassembled bumpers (straight down the
  new end, no interleave) so long-form platforms always carry fresh material.
- One assembly run = one ledger row. Assemblies never consume unit numbers —
  units keep their own identity in the source-units column.

## QC checklist (every assembly)

- [ ] All inputs verified: 1280x720, ~10s, h264+aac (assemble.sh fails loudly otherwise)
- [ ] Output duration: 60.0s ±0.5 (E1M) or 120.0s ±0.5 (E2M)
- [ ] Output resolution 1280x720, audio stream present, no decode errors
- [ ] Sequence follows rules 1–6 above
- [ ] Title metadata embedded
- [ ] Ledger row appended (ASSEMBLY_LOG.md)
- [ ] File announced + delivered as a chat attachment ("just send it")

## Changelog

- 2026-10-18: platform created; E1M/E2M numbering adopted.
