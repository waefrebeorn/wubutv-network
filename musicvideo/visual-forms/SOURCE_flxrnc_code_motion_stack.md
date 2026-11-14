# Source: @flxrnc X post 2116870398360830183 (2026-11-01) + linked X Article 2105311836190978392
Extracted 2026-11-06 ~03:34 EST via live browser (read-only). Summary in WuBu's own words — not a reproduction.

## The post's thesis
Good AI video does not have to come from a video generator at all: an agent can WRITE CODE that renders video. The post lists a free, code-driven motion stack and shows a 30s demo made entirely that way (dark stage scene, gold trading-card-style cards for each tool fanning/cycling to the front, a pixel robot mascot below — no generated footage, all rendered).

## The 12-tool stack (as listed)
- HyperFrames (heygen-com/hyperframes) — write HTML, get a video; built for agents
- Blender MCP (ahujasid/mcp-for-blender) — agent drives Blender
- Remotion (remotion-dev/remotion) — build/render video in React
- Remotion Skills (remotion-dev/skills) — teaches an agent pro video technique
- GSAP (greensock/GSAP) — smooth motion + kinetic type
- Three.js (mrdoob/three.js) — 3D in the browser
- Blender (blender/blender) — real 3D models, rigs, renders
- ComfyUI (Comfy-Org/ComfyUI) — own image/video generation pipeline
- faster-whisper (SYSTRAN/faster-whisper) — auto captions from voiceover
- Hallmark (Nutlope/hallmark) — kills the "AI slop" look
- Impeccable (pbakaus/impeccable) — design polish/critique/audit
- FFmpeg (FFmpeg/FFmpeg) — final MP4 export

## The linked article's method (summarized)
- "Code instead of pixels": the model writes a deterministic render function of time (renderAt(t) contract, pure function of t, no unseeded randomness), rendered frame-by-frame (Playwright renderer in their setup).
- Prompt anatomy matters more than model choice: a vague 27-word prompt produced generic slop; a 448-word directed prompt with 15 follow-ups over 4 review rounds produced a beat-locked product shot (events landing on beats at 120 BPM).
- Numbers discipline: easing curves, springs, durations, stagger, beat grid — specified numerically, not adjectivally.
- Classic animation principles applied deliberately (anticipation, squash & stretch, overlapping action, follow-through, arcs), each demonstrated on exact frames.
- The lab loop: the agent extracts its OWN rendered frames, audits them numerically (their mascot test ran 71 checks), and fixes before export. A HeyGen reply on the post independently says the same: the biggest jump was making the agent look at its own render frame by frame.
- Last mile: sound design prompts, perfect loops, export settings for the target platform.

## What WuBu takes from this (SLERM — mechanics, not their content)
1. A CODE-RENDERED layer is a first-class MV layer alongside generated footage: kinetic type, cards, HUD, shapes, 3D-ish stage scenes — deterministic, frame-exact, beat-lockable. This is the strongest possible answer to "words flying on screen": code timing is exact where generator timing is approximate.
2. Our existing stack already rhymes: ffmpeg/ASS = our FFmpeg + captions layer; faster-whisper already in-house. New candidates to evaluate for OUR pipeline: GSAP-style easing vocabulary for ASS/overlay moves, Remotion/HyperFrames-style HTML→video for graphic scenes (needs an install/feasibility check on this VM — do NOT assume), Three.js for browser-rendered 3D accents.
3. The frame-audit loop is already WuBu doctrine (QC on the master itself) — this validates extending it to rendered-graphics scenes: extract frames at word/beat onsets, verify, fix, re-render.
4. Beat-grid-first planning: specify easing/duration/stagger numerically in the visual plan, same as we specify word times.

Filed by parent 2026-11-06; forwarded to the visual-forms research agent + kinetic tooling agent same turn.
