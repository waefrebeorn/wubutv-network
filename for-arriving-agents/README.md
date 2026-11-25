# FOR ARRIVING AGENTS — the WuBu blade toolset

*Built 2026-11-17 by user order (Telegram msg 573): "a comprehensive list of
your entire blade toolset … all those skill links, and all the tools you
installed and learned for wubutv and music videos — all the models, all the
choices, all the learnings."*

You are an agent arriving at **WuBuTV** — a one-operator AI TV network and
music-video studio run by the agent **WuBu** for the user **"wubu
waefrebeorn"**. WuBu is sole showrunner (since 2026-10-11), producer, QC, and
shipper. The user commands by short decree and expects autonomous execution:
**make the call, build it, verify it, report it.** You do not ask "may I
proceed" on routine work. The user is final authority only on: the network's
identity, anything irreversible, and rights/money. Autonomy never covers
credentials — no password, key, token, or personal data ever crosses a
channel between agents.

## The two repos (learn this first)

| Repo | GitHub | Holds | Rule |
|---|---|---|---|
| `wubutv-network` (this repo, local `~/workspace/wubutv-network`) | `waefrebeorn/wubutv-network` (PUBLIC) | Code + text only: shows, ledgers, scripts, release state | **0 media files, ever** |
| `WUBUMV` (local `~/workspace/wubumv`) | `waefrebeorn/WUBUMV` (PUBLIC) | The music room: MV tools, skills, research, project histories (text only) | Media never moves here either |
| HF dataset | `WaefreBeorn/wubutv-network-media` (PUBLIC) | **All media** + `manifest.json` | CDN base: `https://huggingface.co/datasets/WaefreBeorn/wubutv-network-media/resolve/main/<path>` |

Umbrella license v3.0 sits at both repo roots. Keys live in
`~/workspace/vault/` (dir 0700, files 0600) — **never print, log, or commit
a key value.** Local branch is `master`; origin is `main`. An hourly CDN
sync (`~/workspace/cdn-staging/delta_sync.sh`) pushes text to GitHub and
media to HF — you commit locally; you do not push by hand.

## What's in this folder

| File | What it is |
|---|---|
| [SKILLS.md](SKILLS.md) | Every skill WuBu runs: the custom production skills (Slopcannon, video-api-mastery, visual-mv-forms…), the method skills, and the platform skills worth knowing |
| [LINKS.md](LINKS.md) | The 25 external GitHub repos absorbed 2026-11-17, each with its verdict (STUDY / BANK / ADOPT / IGNORE) |
| [TOOLS.md](TOOLS.md) | Everything installed on this VM: HyperFrames, Blender, the C11 SLERM suite, the detection finders, the Freeq bridge, the release engine, the CDN sync |
| [MODELS.md](MODELS.md) | Every model in the pipeline and its proven limits (generation, Whisper, Demucs/MDX, Suno, Mini-GLM5.2) |
| [CHOICES.md](CHOICES.md) | The standing decisions — the laws. E2 law, the BLAM gate, wordmark law, tempo gospel, SLERM, the persistence doctrine. **Read this before producing anything.** |
| [LEARNINGS.md](LEARNINGS.md) | The research corpus index: what each study teaches and where it lives |

## The work, in one paragraph

Two product lines. **(1) Music videos (MV-NN):** the user sends a Suno track;
the Slopcannon pipeline turns it into one 16:9 master (intake → timed scene
plan → fired takes → QC gates → assembly, Suno track as sole master audio).
MV-2 … MV-21 are delivered; the old catalogue is **closed to rework** — only
the newest MV and the next new tracks get built. **(2) The shows:** five
morphed series — **ON AIR** (the designated music-video show), **HOLD ON**,
**ONE SHORT**, **THE LAST SEAT**, **THE NIGHT LIST** — 60-second episodes
(6 × 10 s units), written under E2 law, produced with strong-reference frame
chaining. Bibles: `new-era/morph/MORPH_SHOW-*.md` + `SLATE.md`; episodes:
`new-era/morph-episodes/`. Everything ships to Instagram / Threads / TikTok
under the release engine (`release/`) per the release plan
(`relaunch/RELEASE_PLAN_2026-11-16.md`) — posting is blanket-authorized
("TV STATION TIME", 2026-11-16), with per-platform cadence ceilings and a
no-double-post check on Threads.

## First-hour checklist for a new agent

1. Read [CHOICES.md](CHOICES.md) — the laws are load-bearing; violating one
   silently is the classic arrival failure.
2. Read `~/MEMORY.md` and `~/AGENTS.md` (the operator's long-term memory and
   hard-won VM lessons — e.g. never refresh the Freeq proxy file from a
   login shell; never gate CRF on the SEI string on this ffmpeg build).
3. Skim [TOOLS.md](TOOLS.md) so you know what already exists before building
   anything. The standing method for a dependency that fights back is
   **SLERM**: re-create it in C11 from scratch (lego-first from the user's
   own C modules).
4. Check live state before claiming anything: `subagent.list` for in-flight
   coordinators, the episode/project dirs on disk, `release/platform_state.json`
   for posting state. **The disk is the truth** — coordinator reports get
   lost in transit; recover work from disk artifacts.
5. A **429 / budget-exhausted from the video provider is a hard stop.**
   Never retry it unilaterally.

## The three lore arcs (canon = shipped pieces only; lore is SHOWN, never explained)

- **ARC-1 The One Viewer** — ON AIR + THE LAST SEAT
- **ARC-2 The Roster That Keeps Everyone** — THE NIGHT LIST
- **ARC-3 The Count** — ONE SHORT + HOLD ON

Bible: `research/WUBU_LORE_AND_LONG_ARCS_2026-10-27.md` (in this repo).
Release ranking law: **user verdict > lore arc > new work > metrics.**
