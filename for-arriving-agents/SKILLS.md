# SKILLS — the blades WuBu carries

Skills are reproducible playbooks. The custom ones live in
`~/workspace/custom-skills/` (and are mirrored into `~/workspace/wubumv/skills/`
for the three MV skills). Read a skill's `SKILL.md` in full before using it —
the headers below are orientation, not substitutes.

## Custom production skills (ours, hand-built)

| Skill | Path | What it does / when to use it |
|---|---|---|
| **slopcannon** | `~/workspace/custom-skills/slopcannon/SKILL.md` | THE music-video pipeline: Suno track in → intake (audio analysis is a required step) → timed scene plan → fired scene volleys (≤6 videos per batch) → QC gates (wordmark hard gate, zero on-screen text, no licensed material) → assembly with the Suno track as master → one 16:9 master → chat delivery. SLERM-built by WuBu; NOT a copy of slop.cc. Boundary: never use the user as a copy-paste relay to Slopcannon. |
| **video-api-mastery** | `~/workspace/custom-skills/video-api-mastery/SKILL.md` | Measured behaviour of the media generation tools: image-ref conditioning, duration/aspect text steering, audio reality. Read BEFORE planning any generation call that uses image refs, a specific duration/aspect, or multi-image journeys. Lab evidence: `~/workspace/wubutv-network/musicvideo/video-api-lab/` (the lab file wins over the skill where they disagree). |
| **visual-mv-forms** | `~/workspace/custom-skills/visual-mv-forms/SKILL.md` | Visual-first MV forms beyond singing takes: kinetic typography, visualizers, montage/collage, graphic systems, stills in motion, non-singing performance, code-rendered graphics, countdown forms. The decision layer for every MV slot that is NOT a mouth-sung take. Full specs: `~/workspace/wubutv-network/musicvideo/visual-forms/VISUAL_FORMS_TAXONOMY.md`. |
| **creator_study_cross_platform** | `~/workspace/custom-skills/creator_study_cross_platform/SKILL.md` | How to study a creator across platforms: enumerate every platform they plausibly publish on, search by exact handle AND name, record which routes returned openable work, and pivot when one platform blocks you — a blocked route is one failed route, never the end of the study. (Lesson paid for: a study that stops at an X block loses to one that triangulates.) |
| **persistent_browser_session** | `~/workspace/custom-skills/persistent_browser_session/SKILL.md` | Keep ONE browser task alive across repeated actions (shared login state, drafts, page context): open with `task_id: "new"`, write the returned id to a pointer file with the operation's working files, read the pointer before every later action, steer the same session. |
| **delegated_work_recovery** | `~/workspace/custom-skills/delegated_work_recovery/SKILL.md` | Recover delegated work from its disk artifact when its report never arrives. A missing report is missing evidence, not proof of running work: set a checkpoint when delegating (what artifact proves completion, where, how long you'll wait), then check disk state before waiting longer or refiring. Transport/DB failures kill report channels while the work itself finished on disk — this has happened repeatedly. |
| **recovered-skill-notes** | `~/workspace/custom-skills/recovered-skill-notes/` | Archive of earlier local learning. Possibly stale — compare against current skills before use; promote useful methods into the relevant skill and retire the entry. |

## Method documents that act as skills (show production)

These live in the repo and bind production exactly like skills do:

| Method | Path | Governs |
|---|---|---|
| Writers Room Method + msg-470 amendments | `research/WRITERS_ROOM_METHOD_2026-11-15.md` (repo root `research/`) | Role-separated rooms (Storyliner ≠ Dialogue Writer; Continuity Editor never rewrites; fresh-context Critic, max 2 rounds), pass order, plant & payoff table, three scripted digestion gaps |
| E2 Speech & Story Addendum | `new-era/research/E2_SPEECH_AND_STORY_ADDENDUM_2026-11-16.md` | The one-star repair kit: skeleton menu S0–S9, speech-twining rules (shuffle test), character meaning/agency checks — adopted in full as E2 law (see CHOICES.md) |
| Method A — joint cohesion | `research/JOINT_COHESION_METHOD_2026-11-15.md` + Panel Workflow Spec v2 | Frame-joint cohesion between units; last-frame → first-frame strong reference (SR1–SR4) |
| Method B — conversation + continuity | `research/CONVERSATION_CONTINUITY_METHOD_2026-11-15.md` | Pair law, continuity ledger, eight pair patterns |
| Method C — dynamic graphics | `research/DYNAMIC_GRAPHICS_METHOD_2026-11-15.md` | G1–G8 graphic devices per show — now rendered via HyperFrames (see TOOLS.md) |
| First-Second Doctrine | `research/FIRST_SECOND_DOCTRINE_2026-11-15.md` | Every video lands an impact in the first second; the BLAM gate numbers live in CHOICES.md |

## Platform skills on this VM (system, `/opt/muse/skills/`)

The full set is large; the ones this operation actually leans on:

- **social-publishing** — plan/publish/schedule social posts (the release lanes do the posting; this is the general playbook).
- **documents** — read/write/revise docs, PDFs, spreadsheets, decks.
- **transcribe-recordings** — chunked transcription with resume (Whisper work).
- **image-search** — web image search for references and feeds.
- **media-library** — search the user's photo library.
- **music-discovery**, **spoken-audio**, **generate_podcast** — audio lanes.
- **custom-connector-setup** — build a connector/skill for a service Muse doesn't bundle (the template route for new reusable workflows).
- **wide-research**, **knowledge-organization**, **task-management**, **goals**, **scheduling**, **email-management**, **messaging** — general operations.

## External skill repos

The 25 GitHub repos absorbed on 2026-11-17 (agent-skills packs, code-video
stacks, avatar toolchain) are listed with verdicts in [LINKS.md](LINKS.md).
Two are already mirrored locally as research:
`~/workspace/wubumv/research/hyperframes-eval-20261117/` and
`~/workspace/wubumv/research/agent-reach-eval-20261117/`.
