# 05 — The project machine (product facts)

Sources: https://slop.cc/faq plus wiki guides scene-timeline, reference-bank,
firing-the-cannon, cannon-credits, make-films-with-an-agent (all 2026-09-30).
All items below [confirmed] unless tagged otherwise.

## The pipeline, end to end

1. INPUTS — song + people/visual references + idea; confirm rights once per
   project. You do not need to write prompts, split the song, know model
   settings, or prepare a shot list — the Producer helps.
2. PLAN — brainstorm with the Producer until the timed story and scene
   references feel right. "SLOPCANNON privately analyzes the song's timing
   and words to guide scene performance and editing. You can correct or
   ignore the detected words and disable mouth movement scene by scene."
3. GENERATE — review the exact credit total, fire the Cannon; ready scenes
   launch as one coordinated volley; finished clips attach to the timeline
   as they arrive; accepted jobs keep processing if the browser closes and
   recover on return, same device or another.
4. REVIEW — keep the hits: "Watch the timeline. Change and reroll only the
   scenes that missed; earlier takes stay available." Every scene keeps its
   take history; choose the version the cut uses; download any single clip.
5. ASSEMBLE — active takes trimmed into timeline order with the original
   song, optional captions, MP4 out. Assembly is included in the price.

## The scene timeline

- "The scene timeline is the song laid out as a film: numbered scenes, each
  tied to a passage of the track, with its own direction, references, words
  and takes. It is what lets you change scene 11 without touching scenes 1
  to 10."
- "The song sets the clock": cuts can land on the music, and a performance
  scene knows which line is being sung. Each scene keeps its own audio
  excerpt, "which is what the Cannon uses when it renders that scene."
- Plan rule: "A good scene asks for one clear action in one place, with the
  camera doing one thing. If a scene's direction needs the word 'then' more
  than once, it is probably two scenes. Splitting it costs nothing before
  the volley."
- Formats: landscape, square, portrait, vertical incl. 9:16. "Choose the
  format before the first pass, because every scene is composed for it."
- Common mistakes: scenes that ignore the song's structure so cuts land
  between beats; changing aspect ratio after the first pass; packing several
  actions into one short scene.

## Create mode vs Studio mode

- Create mode is the guided path: inputs, plan, generate, review, assemble.
- Studio mode reveals the scene timeline, reference assignments, prompts, word
  timing, take history, recovery tools, individual downloads.
- Both edit the same project; start simple, switch to precise controls only
  when needed.

## Credits [confirmed, exact numbers]

- "At launch, every generated clip uses Quality 2K at eight Cannon Credits per
  finished second. Standard packs therefore cost about $0.222 per finished
  second, or $13.33 per finished minute."
- "Before a volley or reroll, the interface shows the exact credits required.
  A first pass charges the exact saved timeline length; a reroll charges only
  the selected scene."
- "Status checks, recovery, downloads, caption changes, project editing, and
  a failed render with no deliverable do not create a lasting video-generation
  charge." A rejected or terminally failed render releases its credit hold.
- Short balance: "Nothing is submitted and nothing is deducted" — the app
  shows the shortfall and the smallest pack that covers it; the project is
  preserved; press the same button again after loading.
- Spending advice: "Most of a film's cost is decided by the plan, not the
  rerolls. Keep the timeline to the part of the song the story needs, read
  every scene before the first pass, and reshoot deliberately with a reason
  for each change."

## Captions [confirmed]

- "Optional closed captions are added during preview and final assembly; they
  are not drawn into the AI-generated footage." The captions guide adds: timed
  to every sung word, drawn in the chosen look, burned into the finished MP4.
  Twelve caption looks, karaoke sweep to one big word per beat.
- Consequence for WuBu: captions in post is not our workaround — it is the
  product's own architecture. Our zero-on-screen-text gate on generated takes
  plus captions in post matches Slopcannon exactly.

## Agents [confirmed]

- "SLOPCANNON provides documented agent-facing capabilities for project
  inspection and production workflows. Human confirmation remains required for
  content rights and paid generation actions."
- Three ways in: "The MCP server at https://api.slop.cc/mcp, for Claude,
  Claude Code, Claude Desktop and other MCP clients" (browser sign-in once);
  "the published agent skill, which teaches an agent the whole production
  workflow"; "the documented HTTP API, for your own tools and scripts."
- "An agent can do the production work, but some decisions stay human.
  Confirming the rights to uploaded media and approving paid generation
  require you, and tokens are scoped so an agent can only do what you
  granted it." An agent's project is an ordinary project, openable in the
  browser. The user-referenced `direction.md` is most plausibly this
  published agent skill (or part of it); it was NOT fetched this run — no URL
  was supplied. Open item: fetch via the agent guide's "SLOPCANNON for
  agents" link when wanted.
- Agent common mistakes (wiki): pasting a token into a chat or shared file;
  granting broader scopes than the job needs; letting an agent approve
  spending not reviewed.

## Start from your own footage (v2v) [index blurb]

- "Upload a video and SLOPCANNON restyles it scene by scene against your
  references, keeping the source's cuts and timing as the film's structure."
  Full guide not fetched this run; treat as a product claim, not a verified
  workflow detail.

## Rights gate [confirmed]

- "You must have the necessary rights or permission for the song, images,
  likenesses, logos, and other protected material you upload or ask
  SLOPCANNON to use. AI generation does not create those rights for you."
