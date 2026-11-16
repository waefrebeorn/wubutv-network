# 01 — THE AI-SHOW PLATFORM MATRIX (fetched 2026-10-21)

What exists right now, what it generates, and how a 10-second story part is
actually produced on each. Sources are the pages saved verbatim in `web/`.

## A. Networks that are already AI-generated, running live

**aitvlist.com** tracks **29 AI-generated TV channels live right now** (page
capture 2026-10-21). Named channels and their engines:

- **Slop TV** — an **open-source 24/7 YouTube stream**: chat comments are expanded
  by an LLM into prompts and rendered with **MiniMax H3**. Source: GitHub
  `shuttie/SlopTV`. This is the single most important precedent in this whole
  corpus: a live channel whose *audience writes the prompts*.
- **fal.live** channels (line-up tracked, some 404 or password-gated as of the
  capture): a 90s-style **magical girl anime** with chat supplying each mishap; a
  **1940s black-and-white film-noir mystery** steered by chat (password-protected,
  i.e. not publicly watchable); a **claymation-style animals game show** with
  chat voting.
- Engines in use across the list: **MiniMax H3 / H3 Max, Veo 3, Agora-1, Athene,
  GPT, GPT+Unity, GPT-4 + PlayHT**, plus a live model column showing per-channel
  render engines.

Takeaway #1: the network form is real and already running, and the winning
interaction is **chat-driven generation** (vote-driven / prompt-driven), not
pre-rendered episodes.

## B. Platforms built to make *shows*, not clips

| Platform | What it is | Show-specific affordances |
|---|---|---|
| **Showrunner / Fable** (`showrunner.xyz`, `showrunnerstudio.com`; Amazon-backed) | "generate your own TV show" streaming platform — the "Netflix of AI" framing | AI showrunning: write/voice characters, generate episodes; public library of user shows |
| **Runway — Microdramas** (`runway.com/use-cases/microdramas`) | vertical microdrama production lane inside Runway | their own words: *"Vertical episodes with a recurring cast, locations that stay put and a hook every sixty seconds. Cast the show once, then generate the season."* Also ships title cards, cold opens, **cliffhanger stingers**, vertical cover art; season = **60+ episodes** of **1–2 minutes** |
| **Google Flow + Veo 3 / 3.1** (`blog.google`, `deepmind.google/models/veo`) | AI filmmaking tool for shot-by-shot construction | prompt guide structures prompts as **subject → action → camera/framing → lighting → audio**, with explicit audio description alongside visuals |
| **OpenAI Sora 2** | prompt-first video with style templates | official-style guidance splits **style / camera direction & framing / subject / action / technical** |
| **LTX Studio** (`ltx.io`, `docs.ltx.io`) | story-first studio; API prompting guide is unusually explicit | single continuous shot = **4–8 sentences**; multi-shot = **2–4 shots per generation**; LTX-2.5 **duration predictor sizes the clip to the action described** |
| **MiniMax Hailuo** | image-to-video dominant | in I2V the **source image carries appearance and composition**; the prompt is for **motion, camera, and what stays stable** |
| **Kling** | general video | guidance is "repeatable prompt workflows", strong/weak example pairs |
| **Higgsfield** | cinematic camera-control models | prompt style includes explicit **gear/lens spec** and **negative clauses** ("NO fisheye, NO plastic skin, NO commercial gloss") |
| **Seedance 2.0 / 2.5** (ByteDance) | multimodal reference video | **assign every asset a role**: `@image1` = appearance, `@video1` = action + camera rhythm, `@audio1` = emotional progression; single pass reportedly ~30 s |
| **Wan 2.2 / 2.5** (Alibaba) | open-weight | explicit formula: **Subject + Scene + Motion + Camera Language + Atmosphere + Styling** |
| **PixVerse V5.6 / V6** | multi-shot single generation | V6: 1080p to ~15 s, three anchors — **character sheet, precise reference image, strictly fixed keyword order**; **first-frame chaining** for continuity |
| **Vidu Q3** | native audio-video | **16 s of native audio+video = one complete narrative unit** (setup/development/turn/resolution), with beats labelled `(0-4s)(4-10s)(10-16s)` |

Takeaway #2: the market has converged on **vertical, recurring-cast, 1–2 minute
episodes with a hook at least every 60 seconds** — and, in Vidu's case, on
**beat-labelled prompts** as the native way to get pacing.

## C. Money in the lane

- Global investment in short-form / micro-drama content: **$8.4B in 2025, +162%
  vs 2022** (Vitrina, citing industry figures).
- Microdrama platform economics (from the DA-25 run, same week): ReelShort on pace
  for **$1.05B revenue** in 2026; DramaBox **$530M gross IAP** in 2025; short-drama
  apps **850M+ downloads in Q1 2026** (Sensor Tower).
- Episode length consensus: **60–120 s**, engagement sweet spot **90–100 s**
  (invideo); creator playbooks say 30–90 s or 2–5 min and tell you to pick ONE
  (charisma.cloud).

## D. What this means for us (CEO Director call)

1. **SlopTV is the model to beat and to learn from**: chat → LLM → prompt →
   render → live channel. We already have the render factory and a catalogue; we
   do not have the interactive loop. That is the cheapest differentiator available
   to us and it costs no new spend.
2. **Runway's microdrama spec is our format**: recurring cast, fixed locations,
   hook every 60 s, 60+ episodes a season, 1–2 minutes each. A 10-second unit is
   the *atom*, not the episode: **six 10-second story parts = one 60-second
   episode**.
3. Nothing in the platform landscape rewards the deadpan-paperwork canon. The
   catalogue stays; the *new* output changes (see `04_PRODUCTION_GRAMMAR.md`).
