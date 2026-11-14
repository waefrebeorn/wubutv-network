# Source: @renproton X post 2118392436863201677 (2026-11-05) + quoted @beamnxw guide "Motion Engineering with Opus 5.5" (2026-10-09)
Extracted by the parent via live browser (read-only); this note written 2026-11-06 from the parent's extraction. Summary in WuBu's own words — not a reproduction. The beamnxw article's pricing/sales content is deliberately NOT imported — irrelevant to the MV pipeline.

## The post's thesis
A complete motion-design studio without After Effects, assembled from 16 free open-source repos, driven by an agent (their framing: Opus 5.5) from brief to finished video. Pipeline framing: **Brief → storyboard → motion → sound → render → launch.** The post's 15s demo reel shows the stack as floating tool cards plus a 3D physics demo (Three.js + cannon-es + Effekseer thumbnails, code panel visible) — the stack itself is the subject.

## The 16 repos, mapped to WuBu's layers
| # | Repo | Job in their stack | WuBu layer mapping |
|---|---|---|---|
| 01 | Remotion | Build videos with React | Code-render layer (Family G) — already in the set via @flxrnc |
| 02 | Storyboarder | Plan shots, create animatics | **NEW — pre-production / planning discipline (see below)** |
| 03 | Anime.js | Animation timelines, easing control | **NEW candidate — Family G/A motion engine (UNVERIFIED)** |
| 04 | Flubber | Smooth shape morphing | **NEW candidate — Family A/D shape-morph moves (UNVERIFIED)** |
| 05 | Pixelorama | Pixel art, animated sprites | **NEW — Family E stills-in-motion / pixel plates candidate** |
| 06 | Three.js | 3D scenes, lighting, cameras | Code-render 3D (Family G3) — already in the set via @flxrnc |
| 07 | PlayCanvas | Real-time 3D worlds | **NEW candidate — 3D worlds, overlaps Three.js's job (UNVERIFIED)** |
| 08 | cannon-es | 3D physics, collisions | **NEW candidate — physics layer for rendered scenes (UNVERIFIED)** |
| 09 | Sverchok | Procedural geometry inside Blender | **NEW — Blender-side procedural geometry (Blender thread, see below)** |
| 10 | Effekseer | Stylized particle effects | Effects layer (Family H1) — already in the set via @Mnilax |
| 11 | twigl | Live shader coding, GIF loops | **NEW candidate — shader/loop plates, Family E2/G (UNVERIFIED)** |
| 12 | Bark | Voice and sound generation | **OUT for WuBu — see adjudication** |
| 13 | Pedalboard | Audio FX (reverb, compression) | **Unproven/optional, narrow boundary — see adjudication** |
| 14 | OBS Studio | Screen capture / recording | **No current MV use — see adjudication** |
| 15 | Shotcut | Timeline editor, finish the cut | **Superseded by our ffmpeg pipeline — see adjudication** |
| 16 | FFmpeg | Encode, compress, deliver | Our assembly/delivery tool already — corroboration |

## The quoted guide's method (@beamnxw, summarized — mechanics only)
A five-step loop for building a short clip from a brief:
1. **Capture reference** — a ~20s reference video, named screenshots, the copy.
2. **Shot brief** — opening / product reveal / action / feature / closing, one brief per shot.
3. **Single JSON timeline deck** — one shot per slide, stated fps (24/30/60), **one action per frame**.
4. **Render** in a browser-based stage.
5. **Review single frames against the brief** — the deliverable is reviewable frame by frame.
Motion rules: **one motion per shot; if it moves, say why; copy readable on frame 30 and frame 60 alike; vary mass, colour and timing rather than just speed.** Acceptance test (the **stranger test**): a stranger watches once and can name the product and one benefit.

## What WuBu takes from this (SLERM — mechanics, not their content)
1. **The storyboard/animatic step is the highest-value transfer.** Their stack puts Storyboarder + a shot brief + an animatic BEFORE any motion work. WuBu's plans (MV_PREPRO rows) are text contracts; adding a cheap storyboard/animatic pass — boards or generated stills cut to the song grid as a timed animatic — would let the frame-audit doctrine bite BEFORE generation spend, not after. This extends, not replaces, the plan gate.
2. **The five-step loop corroborates and sharpens our frame-audit doctrine.** Reference → brief → JSON timeline deck → render → review single frames against the brief is the same shape as our plan → render → onset-frame audit → fix loop, with two upgrades worth adopting: the timeline as ONE machine-readable deck (our per-project JSON already does this for words; extend the habit to visual-form sections), and review frames checked **against the brief**, not just against the song.
3. **The motion rules sharpen ours.** "One motion per shot; if it moves, say why" is the graphics-layer twin of our "accents are punctuation, not wallpaper." "Readable on frame 30 AND frame 60" is a harder legibility check than our rest rule (it tests legibility mid-flight, not only at rest). "Vary mass/colour/timing, not just speed" is a new axis for move specs. The stranger test becomes a hook/legibility check: a stranger watches the hook once and can say what the song/section is about.
4. **Corroboration, not novelty:** Remotion, Three.js, Effekseer and FFmpeg were already in the set (flxrnc/Mnilax). A second independent stack naming the same four strengthens the stack-architecture principle — one tool per layer, agent-driven.
5. **New candidates stay behind the Family G proof gate.** Anime.js, Flubber, twigl, PlayCanvas, cannon-es, Pixelorama are plausible layer tools (easing/morph engines, shader loops, physics, pixel plates) but **none is verified on this VM** — same status as Remotion/GSAP/Three.js. No plan may promise a scene from them until a 10s proof render passes here.

## Honest applicability adjudication (what does NOT transfer, and why)
- **Bark (voice/sound generation) — OUT.** WuBu never generates a soundtrack: the user's track is the sole master audio, generated audio is dropped, and station episodes use native audio only (never TTS-dub). A TTS/voice generator has no slot in either pipeline. Not adopted, not "someday" — excluded by standing law.
- **OBS Studio (screen capture) — no current MV use.** Nothing in the MV pipeline is a screen recording; our footage is generated or code-rendered. Noted for completeness only.
- **Shotcut (timeline editor) — superseded.** Our timeline editing IS the ffmpeg pipeline (scripted, frame-exact, reproducible). A GUI editor would be a step backwards in determinism. Not adopted.
- **Pedalboard (audio FX) — unproven/optional, narrow boundary.** It could only ever matter as post audio FX on **our own** material (e.g. a code-rendered sting or our own recorded voice), never on the master song: the song is never time-stretched, re-processed, or used as anything but the untouched timing/audio authority. Flagged unproven — no current need identified; do not reach for it without a named job.
- **Sverchok — Blender thread, not this note's install.** Procedural geometry inside Blender; the user has separately ordered Blender acquisition for the WuBu suite. Recorded here as the Blender-side candidate to evaluate when that lands. Nothing installed by this fold-in.

Filed 2026-11-06; folded into SOURCES.md, the taxonomy (storyboard step + motion-rule sharpenings), the kinetic playbook (legibility/stranger-test additions), MONDO_INDEX.md and the visual-mv-forms skill map same day.
