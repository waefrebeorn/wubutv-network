# Source: @0xnicc0 X post 2118324011645997289 (2026-11-05) + linked seeco/@seeconvm article "Opus 5.5 Motion Design: What the Viral 'One-Prompt' Videos Are Hiding" (2026-10-02)
Extracted by the parent via live browser (read-only); this note written 2026-11-06 from the parent's extraction. Summary in WuBu's own words — not a reproduction.

## The post's thesis
"Opus 5.5 just replaced a whole film crew": 12 free repos framed as a complete film crew, each repo cast in a crew role — pre-production, concept, cast, sets, motion, sound, captions, final cut. The framing differs from the earlier stack posts: not a layer list but a **crew metaphor** — every stage of a real production has a named tool doing that job, driven by the agent.

## The 12 repos, mapped to WuBu's layers
| # | Repo | Crew role in their stack | WuBu layer mapping |
|---|---|---|---|
| 01 | Claude Skills | Teach the agent the pro workflow up front | **That is literally this mondo set** — corroboration of the architecture |
| 02 | Excalidraw | Storyboard sketches, shot by shot | **FENCED — note only** (see adjudication) |
| 03 | ComfyUI | Concept art + textures | **FENCED** (see adjudication) |
| 04 | Blender | Model + rig the cast | **Already ordered separately by the user** — Blender thread (see below) |
| 05 | Blender MCP | Lets the agent drive Blender | **Candidate follow-on** once base Blender is proven — nothing installed |
| 06 | Three.js | Sets + lights in the browser | Code-render 3D (Family G3) — already in the set via @flxrnc, UNVERIFIED on this VM |
| 07 | GSAP | Motion + moving titles | Kinetic type / motion engine — already in the set via @flxrnc, UNVERIFIED on this VM |
| 08 | SAM 2 | Cut any object out of footage, frame by frame | **FENCED — genuinely new capability** (see adjudication) |
| 09 | Chatterbox | Voice actor from text | **OUT for WuBu — see adjudication** |
| 10 | Tone.js | Score + SFX written in code | **FENCED** (see adjudication) |
| 11 | faster-whisper | Voiceover → captions | **Already ours** — the fw-venv ASR backbone of the swing tooling |
| 12 | FFmpeg | Final cut + export | Our assembly/delivery tool already — corroboration |

## The linked guide's methods (seeco/@seeconvm, summarized — mechanics only)
Thesis: **the model cannot output an MP4.** Every viral "one-prompt" clip is a program the model wrote, rendered frame by frame; the prompt is roughly a tenth of the result and the harness around it does the rest — the good ones started from a ~9,500-character brief, a skills folder, and long runs. The transferable machinery:

- **FRAME FUNCTION.** A deterministic `seek(t)` / `renderAt(t)` that paints exactly what second *t* shows; a headless browser calls it once per frame; ffmpeg assembles. No timers; seeded noise only. (Corroborates @flxrnc's renderAt(t) contract — second independent source for the same rule.)
- **THE RIG.** Coding agent + ffmpeg + headless browser (Playwright/Chromium) + a written render-contract file. Default shape: one HTML file + Playwright + ffmpeg, skipping Remotion/HyperFrames unless named. High effort settings for new films.
- **THE BRIEF.** A real production document — film, assets, visuals, hard lines, deliverables. Use real assets/screens; never invent them.
- **THE REFERENCE.** Supply a frame, clip, or folder of past work; distill `style_guide.md` + `shotlist.md` from it before building.
- **STATE LISTS.** A beat map with fixed windows (their example: Hook 0–2s, Problem 2–5s, Reveal 5–9s, Proof 9–13s, Close 13–16s) carried by **one morphing container** that transforms through the beats instead of cutting between scenes.
- **SPRINGS + SOUND ON ONE CLOCK.** Closed-form springs stacked per change; beats extracted (librosa → `beats.json`) so transitions lock to the music grid.
- **THE CRITIC.** The agent inspects its own work: contact sheet (2 fps, 6 across), strips, a phone test at 360px wide, a loop check, a determinism check; scores 1–10; fixes the worst 3 defects; repeats until every score is 8+.
- **THE SKILL.** Project-folder discipline — `brief.md`, `style_guide.md`, `shotlist.md`, `assets/`, `src/`, `reviews/`, `out/` — with six gates from asset approval to final formats.

## What WuBu takes from this (SLERM — mechanics, not their content)
1. **THE CRITIC is the highest-value transfer.** Our frame-audit doctrine (extract frames at onsets → inspect → fix → re-render) is the same loop unquantified. The Critic sharpens it into a procedure: a contact sheet at a stated density (2 fps, 6 across), named extra checks (phone-width legibility, loop, determinism), a 1–10 score per check, fix the **worst 3** defects only, and repeat until every score is **8+**. That gives the visual-slot QC a stopping rule instead of vibes. Folded into the Taxonomy's visual-slot QC.
2. **The harness-over-prompt thesis validates the mondo architecture.** "The prompt is a tenth; the brief, the skills folder, and the render contract do the rest" is exactly why this knowledge set exists as files instead of chat memory. Their project-folder discipline (`brief.md` / `style_guide.md` / `shotlist.md` / `assets/` / `reviews/` / `out/`, six gates) corroborates our per-project record + gated stages; the named gap worth adopting is a standing `reviews/` habit — audit artifacts filed per project, not scattered.
3. **State lists + one morphing container is a new form idea.** A fixed-window beat map (hook / problem / reveal / proof / close) carried by ONE container that morphs through the beats is a natural fit for hook sections and for Family I countdown/listicle pieces — the count itself becomes the container that transforms. Noted in the Taxonomy as a form note; any build still sits behind the Family G proof gate.
4. **Springs + sound on one clock ties two things we already own together.** We already produce a measured beat grid per project (the swing tooling's `beat_grid.json`); the guide's `beats.json` is the same artifact from the other direction. Rule going forward: code-rendered transitions and spring stacks key off the project's existing beat grid — one clock for picture and sound, never a second beat extraction.
5. **Corroboration, not novelty:** faster-whisper (our ASR backbone), FFmpeg (our assembly/delivery), Claude Skills (this set itself), Three.js/GSAP (in via @flxrnc). A third independent stack converging on the same backbone strengthens the stack-architecture principle.

## Honest applicability adjudication (what does NOT transfer, and why)
- **Chatterbox (TTS voice) — OUT.** Same standing law that excluded Bark (@renproton fold-in): generated audio is never a soundtrack; for MVs the user's song is the sole master audio, and station episodes are native-audio only, never TTS-dubbed. A voice-actor-from-text has no slot in either pipeline. Excluded, not deferred.
- **Tone.js (code-synthesized score/SFX) — FENCED.** For MVs the user's song is the sole master audio and is never replaced or supplemented as the track, so a code-written score has no MV slot. The only conceivable question — synthesized accents on our-own-material non-MV pieces — is unproven and no job is named. Do not reach for it without a named job and a ruling.
- **SAM 2 (object cutout / rotoscope) — FENCED.** Genuinely new capability: frame-by-frame object cutout would feed cutout/paper forms (Family E) directly. But it is a heavy model and CPU feasibility on this VM is unproven — it sits behind the Family G proof gate like every unverified renderer. Candidate, nothing installed.
- **ComfyUI (concept art / textures) — FENCED.** We already have image generation for concept stills and refs; a heavy local install to duplicate that is unproven value. Noted as the local-pipeline candidate if image-gen limits ever bite; nothing installed.
- **Excalidraw (storyboard sketching) — note only.** A web sketch tool; an alternative route to the storyboard/animatic discipline adopted from @renproton (Storyboarder), competing with Blender Grease Pencil boards on the Blender thread. No adoption decision — the discipline matters, the sketch tool is interchangeable.
- **Blender + Blender MCP — Blender thread, not this note's install.** The user has separately ordered Blender acquisition for the WuBu suite (graphics, animations, storyboards on CPU). This post corroborates that direction and adds one candidate: **Blender MCP** — the agent driving Blender directly — is the natural follow-on once base Blender rendering is proven on this VM. Recorded as a candidate; nothing installed by this fold-in.

Filed 2026-11-06; folded into SOURCES.md, the taxonomy (Critic loop in visual-slot QC, state-list/morphing-container form note, beat-grid tie-in), MONDO_INDEX.md and the visual-mv-forms skill map same day.
