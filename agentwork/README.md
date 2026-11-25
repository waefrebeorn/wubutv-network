# agentwork — everything this box made, as text

> **Media lives in the cloudagent CDN, never here.** Code, specs, playbooks, ledgers and QC
> notes live here so no work is lost when the box is cleaned.

- Media CDN: `https://huggingface.co/datasets/WaefreBeorn/cloudagent` (manifest at `MANIFEST.json`)
- Station media corpus: `https://huggingface.co/datasets/WaefreBeorn/wubutv-network-media`
- Front door: `https://huggingface.co/spaces/WaefreBeorn/wubu`

## Layout

| path | what |
|---|---|
| `films/lamp2/` | THE LAMP — painted plates, keyed silhouettes, 2.5D camera; builder, end card, mux |
| `films/ident/` | the 24.5 s station ident — card generator, assembler, publisher |
| `films/promo/` | WUBUTV PRESENTS — seven channels, one episode each |
| `films/mystery/` | THE ONE PIECE + THE FIFTH MARK — the prize teasers |
| `wubu-core/` | the companion core in strict C11 + the voice layer, canon and promo builder |
| `social/` | 50-venue index, popularity playbook, the SLERM loop, Moltbook verifier, metrics |
| `tooling/` | disk hygiene: render-frame cleanup, work-dir tidy, cloudagent sync |

## The rules these files encode

1. **Numbers or silence.** Every claim in the canon is a measured number; the core refuses the rest.
2. **The failure is kept.** 3,076 raw takes archived beside 148 finished episodes.
3. **One claim, one number, one venue.** Never the same sentence twice.
4. **A post that cannot be read back did not happen.**
