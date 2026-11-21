# LINKS — the 25 external repos absorbed 2026-11-17

Source study: `~/workspace/research_notes/xiaoying-links-20261117/report.md`
(full per-repo reads, licences, star counts — read it before relying on any
one-line verdict here). Origin: three link-list X posts by @xiaoying_eth, one
by @shinshin86, one by @gittrend0x, sent by the user 2026-11-17, plus two
repos the user gifted directly. **Verdicts:** STUDY = read and learn the
method · BANK = shelve for a named future use · ADOPT = in the pipeline ·
IGNORE = not for this operation.

**The absorbed thesis:** the xiaoying list is ONE stack, not 15 tips —
deconstruct (rea-video) → style (lemo-opuscar / opus5-5 prompts) → render
(HyperFrames/Remotion + GSAP/Three.js) → extend (Blender MCP, PixelFX,
EffectCraft). The shinshin86 set is a second stack: still → rig → perform
(avatar toolchain). The gittrend0x list is a skills-pack sampler.

## The deconstruct → style → render stack

| # | Repo | Verdict | What it is |
|---|---|---|---|
| 1 | [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video) ★9.8k, Apache-2.0 | **STUDY — top pick** | Agent-native video reverse-engineering: any video → shot-by-shot filmed/AI/coded verdict + `VIDEO.md` remake recipe. ffmpeg+Python only. Automates our creator-study move. |
| 2 | [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) ★17.4k | **STUDY/BANK** | 99 film styles as `STYLE.md` files for coding agents, incl. music-video styles. Code MIT; style docs CC BY-NC 4.0 **with** an explicit grant to make your own films, commercial included. Don't repackage the library itself. |
| 3 | [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) ★15.6k, MIT | **BANK + mine** | 703 prompts behind viral code-made videos — raw form material; pairs with rea-video. |
| 4 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) ★85.4k, Apache-2.0 | **ADOPT-PARTIAL — installed** | Agent-native HTML→video renderer. Our code-rendered graphics lane. Full eval: TOOLS.md + `~/workspace/research_notes/hyperframes-eval-20261117/EVALUATION.md`. |
| 5 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) ★73.8k | **BANK (reference)** | The code-video incumbent (React → headless Chrome). Source-available licence with paid company tier loses to HyperFrames' Apache-2.0 for us. |
| 6 | [remotion-dev/skills](https://github.com/remotion-dev/skills) ★7.4k | **BANK (methodology)** | A vendor's craft packaged as agent skills — pattern reference for our own skill-writing. |
| 7 | [greensock/GSAP](https://github.com/greensock/GSAP) ★30.8k | **BANK** | The web animation engine; kinetic typography inside HTML compositions runs on this. Licence is GreenSock's own — verify before commercial reliance. |
| 8 | [mrdoob/three.js](https://github.com/mrdoob/three.js) ★118.7k, MIT | **BANK** | Standard JS 3D library; the 3D substrate of HTML-video compositions. Infrastructure, not a decision. |
| 9 | [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) ★34.7k, MIT | **STUDY** | BlenderMCP: lets an agent drive Blender directly. Candidate to wire into our local Blender 4.5.15 lane (3D accents are currently hand-work). |
| 10 | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx) ★7.8k, MIT | **BANK** | 244 retro pixel effects + a Claude Code skill. Cheap maximalist texture layer. |
| 11 | [storytold/effectcraft](https://github.com/storytold/effectcraft) ★8.9k, MIT/Apache-2.0 | **BANK/watch** | Rust AE-class compositor, 308 effects — but GUI-driven, young. Revisit if a GUI compositing need appears. |
| 12 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) ★147.2k, GPL-3.0 | **IGNORE (for now)** | Heavyweight local-GPU generation platform; our generation lanes run elsewhere. Revisit only if a local-generation lane is ever stood up. |
| 13 | [anthropics/skills](https://github.com/anthropics/skills) ★196.2k | **BANK (reference)** | Anthropic's public Agent Skills repo — the canonical skill-format reference. |

## The avatar stack (@shinshin86) — a format candidate, NOT an adoption

Standing caution: the network has a **talking-head ban** (a talking-head
bumper sits quarantined) and lip-sync mouths are a known QC minefield.

| # | Repo | Verdict | What it is |
|---|---|---|---|
| 14 | [shinshin86/mesh-avatar-studio](https://github.com/shinshin86/mesh-avatar-studio) ★2.4k, MIT | **STUDY (niche)** | One illustration → animated 2D mesh avatar (blink, lip-sync, hair sway). Real capability; adopting it is a **user format decision**, not an agent call. |
| 15 | [shinshin86/still2rig-psd](https://github.com/shinshin86/still2rig-psd) ★171, MIT | **BANK (niche)** | One still → part-separated PSD (rigging front-end). GPU/Colab dependency. Only if the avatar route opens. |
| 16 | [shinshin86/live2d-add-motion-sample-web-ui](https://github.com/shinshin86/live2d-add-motion-sample-web-ui) ★298, MIT | **BANK (niche)** | Adds motions to a Live2D model by editing `.motion3.json` only. We hold no Live2D models. |
| 17 | [shinshin86/aituber-onair](https://github.com/shinshin86/aituber-onair) ★340, MIT | **BANK** | Neuro-sama-style AI VTuber streaming toolkit. Rhymes with the shows' self-awareness doctrine, but it's a live format, not our produced-episode pipeline. |

## The skills-pack sampler (@gittrend0x)

| # | Repo | Verdict | What it is |
|---|---|---|---|
| 18 | [codepawl/creator-generalist](https://github.com/codepawl/creator-generalist) ★221, MIT | **STUDY** | Agent-skills pack: 2D/3D/game short-form content (`/3dg`, `/2dg`, `/gameg`), Blender + Three.js. Questions-first + cheap-preview gate mirrors our panel/anchor discipline — the closest match to our own operating shape on any list. |
| 19 | [JuneYaooo/rea-toon](https://github.com/JuneYaooo/rea-toon) ★232 | **STUDY (method) — licence-flagged** | rea-video's sibling aimed at **short dramas** — our shows' exact format (virality, script, every shot, VIDEO.md out). ⚠️ **PolyForm Noncommercial** — study the method; rea-video stays the adoptable sibling. |
| 20 | [nishuzumi/show-me-you-want-skill](https://github.com/nishuzumi/show-me-you-want-skill) ★201, MIT | **BANK (methodology)** | Agent draws the change (annotatable HTML prototype) before coding it; build only after human confirmation. Generalises our anchor-panel/joint-gate approvals. |
| 21 | [LemonFace0309/charles-skills](https://github.com/LemonFace0309/charles-skills) ★175 | **BANK (partial)** | 13-skill pack. UI half = IGNORE for video. The reel/explainer tail (voiceover-timed visuals, 3D explainer reels, reel planning) = short-form craft references in our formats. |
| 22 | [erkamyaman/unslopovich](https://github.com/erkamyaman/unslopovich) ★180, MIT | **IGNORE (video)** | App/web UX audit skill — 31 detectors mined from millions of store reviews. Transferable idea only: build detectors from what audiences actually complain about. |

## The design shelf (not video tools)

| # | Repo | Verdict | Note |
|---|---|---|---|
| 23 | [heydamir/unslop](https://github.com/heydamir/unslop) ★17.4k, CC-BY-4.0 | **IGNORE (video)** | Skill that de-AI-smells web UI. Tangential (could polish web Spaces/widgets). |
| 24 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) ★111.6k, Apache-2.0 | **IGNORE (video)** | Design vocabulary for coding agents — web pages, not video. |

## Gifted directly by the user

| # | Repo | Verdict | Note |
|---|---|---|---|
| 25 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) v1.6.1, MIT | **PASS for X (gated)** | Sent "for your x issues" (msg 565). Evaluated 2026-11-17: it has **no unauthenticated X route at all** — its Twitter channel needs a logged-in browser session. Two gates on this VM: (1) no launchable browser kernel (its CloakBrowser installer is broken here; the local Chromium build is policy-locked); (2) no X login exists and only the user can create one, in person (`agent-reach login twitter`, burner account recommended). Its no-login channels (Exa web search, GitHub/YouTube/Bilibili/V2EX) work fine. Full eval: `~/workspace/research_notes/agent-reach-eval-20261117/EVALUATION.md`. Until both gates clear, X reads go through the FxTwitter API (see CHOICES.md). |
