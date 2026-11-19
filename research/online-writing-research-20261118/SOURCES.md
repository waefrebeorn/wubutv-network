# SOURCES — Online Writing Research (2026-11-18)

Every source consulted for `REPORT.md`, with a one-line annotation
and the findings it carries. URLs copied verbatim from search
results. Grades: **official** (model vendor), **practitioner-tested**
(own test generations / documented production run), **practitioner
guide**, **vendor** (tool seller; format facts reliable, quality
claims weighted down), **press**.

## Angle 1 — prompt writing for dialogue scenes

- https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide
  — OpenAI's official Sora 2 prompting guide: Dialogue block below the prose, `Name: "line"` format, consistent speaker labels, alternating turns, per-duration exchange counts. [official] → P-1, C-2
- https://higgsfield.ai/blog/ai-short-film-youtube-guide
  — Higgsfield's own short-film prompt library: Soul ID character build, published turnaround-sheet prompt, worked dialogue prompts in `Name: "line"` form. [official] → P-1, C-5
- https://higgsfield.ai/blog/ai-short-film-pipeline
  — Higgsfield's full pipeline guide: script→scenes/shots first, Soul ID trained before any shot, storyboard sequences, per-scene audio. [official] → C-2, C-5
- https://lzyprompt.com/blog/ai-video-multi-character-scene-prompts/
  — Cross-model two-person direction guide: visual labels, one verb per character per sentence, per-model dialogue attribution (Veo quotes; Kling script line + tone parenthesis; Seedance quotes), listener-silence instruction, 2–3 character limit. [practitioner guide] → P-1, P-3, P-4, P-5, P-8
- https://www.ambienceai.com/tutorials/seedance-prompting-guide
  — Seedance 2.0 guide from the vendor's own test generations: ~20 words/15 s total, ~10 words/line, one sentence per quote, garbling tracks line length (21-word quote → phoneme soup). [practitioner-tested] → P-2
- https://hypernatural.ai/skill/hn/seedance-2-5-prompt-format
  — Seedance 2.5 prompt-format skill doc: `{}` line syntax after speaker + delivery, @Image/@Audio binding, timed spoken lines from an audio track, "never put a person's name outside {}" (renders as on-screen text). [practitioner skill doc] → P-1, P-6
- https://kreatorflow.ai/guides/seedance-2-5-prompt-guide
  — Seedance 2.5 guide tabulating BytePlus's official guidance vs third-party conventions: dialogue in curly braces per BytePlus, reference binding first, timestamped beats, continuity/constraint closing. [vendor, citing official] → P-1
- https://fal.ai/learn/tools/seedance-2-0-prompting-guide
  — fal.ai's Seedance 2.0 prompting guide: spoken line in double quotes lip-syncs and voices; keep lines short, split speeches across cuts. [vendor guide] → P-1
- https://www.dreamdrive.ai/learn/google-labs/veo-3-prompting-dialogue-and-sound/
  — Veo 3 prompting for dialogue/sound: layered prompt (shot, ambience, SFX, quoted line with speaker + delivery), 6–12 words per 8-s clip, remove other spoken text incl. signs/names to stop wrong words. [practitioner guide] → P-2, P-6, P-8
- https://magichour.ai/blog/how-to-prompt-for-speaking-in-veo-3
  — Veo 3.1 dialogue prompts: Google recommends quotation marks for specific dialogue; one visible speaker; formula [shot]+[speaker]+[action]+[exact dialogue]+[delivery]+[ambience]+[style]. [practitioner guide, citing official] → P-1
- https://useveo.ai/blog/the-veo-3-prompt-guide
  — Veo 3/3.1 prompt guide: dialogue layer = speaker + delivery + words in quotes; 8–12 words per 8-s clip; two speakers written in order. [practitioner guide] → P-2
- https://eastondev.com/blog/en/posts/ai/20251207-veo3-audio-generation-guide/
  — Tested Veo 3/3.1 audio guide: single-speaker lip sync ~80% vs multi-speaker <40% (one tester's figures); identical character description in every prompt or the voice changes; script blocks fail for two speakers — write scene flow, or one speaker per segment stitched in post; one line under 8 s. [practitioner-tested] → P-2, P-3, P-9, P-10, C-1
- https://www.gptunnel.ru/en/guide/veo3
  — Veo 3 guide: prompt formula with a Speech/Sound slot; "if you plan to have speech, the character can ONLY speak — no other actions at the same time"; monologue recommended over dialogue. [practitioner guide] → P-5
- https://blog.picassoia.com/kling-2-6-lip-sync-voice-control-audio-and-free-alternatives
  — Kling 2.6 native-audio guide: lines in quotes with delivery beside them; two speakers = practical ceiling, three+ breaks attribution; consistent speaker descriptors, avoid pronouns at speaker changes. [practitioner guide] → P-3
- https://openmicrodrama.com/models/kling
  — Kling 3.0 for micro-drama: Elements with bound voices (5–30-s recordings), word-for-word identical character descriptions, one line per beat (speaker + tone + quotes), speech inside the first 10 s, end on a reaction, lip-sync drift after ~10 s, lowercase-English fix for wrong words, silent shot + later voice when a line must be exact. [practitioner craft guide] → P-5, P-7, P-10, C-1, C-2
- https://flick.art/blog/kling-ai-lip-sync
  — Documented production (The Herder, 11 takes): line written word-for-word with punctuation/pauses before any audio; "Speak exactly the quoted lines only"; Eleven v3 voice-first + Kling Avatar route vs native-quote route compared on real takes. [practitioner-tested] → P-7, L-7
- https://quickveed.com/blogs/ai-video-prompts
  — General prompt guide: 6–8-s clip holds ~12–18 spoken words, one short sentence per clip, `Speaker says: "line"`, spell out numbers, no quotes inside the line. [practitioner guide] → P-2, P-7
- https://support.veed.io/en/articles/16893207-how-to-write-better-prompts-for-ai-video
  — VEED's official help: speech ≈2.5 words/sec (over-budget = rushed/garbled); turn prompt Enhance OFF for exact dialogue; "the model treats everything in your prompt as content to render" (stage directions become scene content); scene sentence + name-attributed lines format. [official help] → P-2, P-6, P-7
- https://www.magicboat.net/mobile/en/blog/ai-dialogue-image-video
  — Dialogue-scene workflow: master frame → derived coverage; speaking and reaction shots generated separately; published speaking prompt (inhale before, mouth closes, expression settles) and reaction prompt ("listens silently with her mouth closed"); one visible action per shot. [practitioner guide] → P-4, P-5, C-5
- https://www.prompt-architects.com/blog/310-dialogue-and-lip-sync-in-ai-video
  — Vendor-documented route taxonomy: native speech vs audio-driven vs replacement dialogue; "Pick the route first, because the prompt shape is different for each one"; Kling ships silent by default. [practitioner guide] → §4 (route-first confirmation)
- https://runway.com/resources/ai-lip-sync
  — Runway's official lip-sync overview: three approaches (prompt-to-video, audio+image, Act-Two performance transfer) — the route menu from a major vendor. [official] → §2 context
- https://aivideocreators.org/guides/ultimate-guide-to-lip-sync-in-ai-video-2026/
  — 2026 lip-sync workflow guide: best-practice baseline = write dialogue in short speaking beats, then record/generate the final voice with pauses and delivery, then drive picture. [practitioner guide] → L-7 context

## Angle 2 — line writing for AI short drama / soaps

- https://clippie.ai/ai-fruit-video-generator
  — Clippie's fruit-video product page: "Name: line" script input, each line one scene, acting tags [annoyed]/[whispers]/[gasps] performed not read, 6/11/20 lines per 30 s/1 min/2 min. [vendor — the tool's actual input contract] → L-1
- https://clippie.ai/blog/how-to-make-ai-fruit-videos
  — Clippie's full production guide: Characters Talk mode, @-mentions in script for consistency, per-character voice + style, scene instructions field, read-and-listen review before animating, "one-page character bible, two or three recurring conflicts, fix an episode length." [vendor guide] → L-1, C-5
- https://oakgen.ai/blog/how-to-write-a-micro-drama-script
  — Micro-drama script guide with template: five beats (hook 0–3 s … cliffhanger last 5–8 s on a face/object), one complication, 90–130 words/60 s from measured 152–170 wpm conversational rate, dialogue shot timed at ~2.5 wps + 1–2 s beat, ep-2+ setup pays the last cliffhanger, season arc before episode 1. [vendor guide] → L-2, L-4, P-2
- https://openmicrodrama.com/guides/writing-a-micro-drama-script
  — Micro-drama writing guide: season-first mapping, hook/friction/spike/button timing, Gigi M. Green's "no more than 10 lines an episode — write 20, then cut 10" and cliffhanger-first construction, "only describe things a video model can actually show." [practitioner craft guide] → L-2, L-3
- https://drama.so/en/blog/short-drama-hook-formula
  — 60-second hook formula: per-second beat sheet, "one line of want" as a demand ("I need this contract tonight"), cliffhanger swap test ("if the cliffhanger could be swapped onto another episode without rewriting the middle, it is decoration"). [vendor craft guide] → L-2, §4
- https://invideo.io/blog/ai-micro-drama-hooks-cliffhangers/
  — AI micro-drama hooks/cliffhangers: cold open = face reacting / shock line / reveal in motion, never an establishing shot; exactly one reversal per 60-s episode; cliffhanger types. [vendor craft guide] → L-2
- https://www.paintbrush.gg/blog/write-dialogue-for-ai-video
  — Dialogue writing for AI video: one bracketed delivery tag per line (1–5 words, performed not spoken), silent beats for reactions, one idea per line, one-breath lines, whole scene performed as ONE take with Eleven v4 Text to Dialogue — line-by-line generation named as the cause of robotic dialogue. [vendor guide describing its production pipeline] → L-5, P-8
- https://debutify.com/blog/make-ai-dialogue-scenes-natural-with-minimax-h3
  — Natural-dialogue study: root cause = "information without intention"; brief each character's want + what they're avoiding saying; naturalness from intent and constraint, not from asking for it; five-part reusable prompt structure. [practitioner-oriented craft article] → L-6
- https://www.hookstudio.ai/blog/frutinovelas
  — Frutinovela explainer with press citations: Fruit Love Island origin (@ai.cinema021, Mar 2026), William Rico / @frutystory, format facts and episode lengths across press sources; no line-level workflow disclosed. [vendor explainer, press-cited] → L-7, §5
- https://www.hookstudio.ai/blog/ai-fruit-videos
  — Hook Studio's priced recipes: fruit-drama episode = still first, one 5-s line per character, talking clips ≤8 s because voice drifts out of sync after that; three-character episode ≈ $4. [vendor recipe with real costs] → P-10, L-7
- https://www.wireflow.ai/blog/ai-fruit-videos
  — Fully disclosed fruit-drama run with every prompt and cost: one prompt + one line per fruit, voice lines <3 s (ElevenLabs v4), front-facing image → speech → Kling Avatar lip-sync, voices fixed across episodes. [vendor, practitioner-tested run] → L-7
- https://www.filmandpen.com/production/ai-sexy-fruits-filmmaking-ethical-crossroads
  — Fruit Love Island phenomenon essay citing NYT/Yahoo: the creator's process = hours per video of scriptwriting, scene planning, and constant redoing to correct generation errors; no workflow or lines published. [press] → L-7, §5
- https://www.freehumanizerai.com/blog/humanize-ai-youtube-script
  — Script-humanizing practice: one-breath sentences, contractions by default, spoken over formal words, read-aloud test marking stiff spots. [practitioner guide] → L-8
- https://blog.fanfun.ai/fix-robotic-tone-ai-character-voices/
  — Creator guide to robotic TTS tone: punctuation/phrasing steer cadence, phonetic respelling fixes mispronounced words, baked-in persona tone bounds the fix. [vendor creator guide] → L-8
- https://www.toolnova-ai.com/2026/06/ai-nutrition-videos-guide-2026.html
  — Talking-fruit Shorts guide (nutrition niche): workflow fact → script → consistent character → voice → animation → captions → human review; hook → reaction → fact → explanation → punchline script shape. [vendor guide; consulted, marginal] → not cited in findings
- https://ovideo.io/resources/ai-fruit-drama-video
  — oVideo fruit-drama generator page: paste a full script, characters designed once and kept the same, per-fruit voices. [vendor marketing; consulted, no line-level detail] → not cited in findings
- https://www.smew.ai/templates/ai-fruit-story
  — Smew AI fruit-story template page + format history (#fruitstory volumes, key accounts/dates). [vendor marketing; consulted for §5 gap check] → §5

## Angle 3 — character / voice consistency practice

- https://layerproof.app/blog/consistent-ai-character/
  — Character-consistency guide: one-page character bible (incl. Voice row: accent/pitch/pace/energy); identity block copied word-for-word in every prompt, never paraphrased ("Curly dark hair" vs "dark curly hair" differ); scripts written in the character's style reusing greetings/phrases/sign-offs. [practitioner guide] → C-1, C-4, C-5
- https://tellers.ai/blog/preserve_voice_consistency_in_ai_videos_2026-10-21
  — Voice-consistency guide: named voice reference files (Maya_voice_reference.wav), supported voice IDs, or a verbatim voice-description block (pitch range, texture, accent, pace, articulation) with stable traits separated from per-line emotion; worked prompt includes "Leo listens without speaking." [practitioner guide, capabilities checked 2026-10-21] → C-3, P-4, P-8
- https://www.media.io/video-tips/soul-id-character-consistency.html
  — Soul ID workflow: do NOT redescribe the face after selecting a trained identity; prompt = [Soul ID] + wardrobe + action + location + camera + lighting + continuity constraints; character bible of wardrobe names/colors/props/forbidden changes. [practitioner guide] → C-2
- https://aipromptgeneer.com/craft/cheatsheets/higgsfield/
  — Higgsfield cheat sheet quoting Higgsfield's own guides: same camera preset/lens/lighting wording across matching shots; Soul ID trained from ≥20 photos, "locks identity, not direction." [practitioner cheat sheet] → C-2 context
- https://www.auto-flow.studio/blog/autoflow-characters-same-face-voice
  — AutoFlow characters: saved once (portrait + name + voice), referenced by name in prompts, dialogue in quotes after the speaker; continuation prompts start from the previous clip's last frame. [vendor guide] → C-2
- https://skywork.ai/blog/ai-video/sora-2-audio-guide-for-cameo-and-import
  — Sora 2 audio/cameo guide: cameo carries face + actual voice; dialogue written after the cameo mention in quotes; specificity of sound description. [practitioner guide] → C-2 context
- https://docs.estuary-ai.com/docs/platform/persona-authoring
  — Estuary's Persona Authoring Cookbook: "Show the voice, don't describe it" — concrete speech patterns and example phrases over adjective lists; personality (how they speak) kept separate from background (what they know). [official platform docs] → C-4
- https://lunelle.ai/guides/keep-ai-characters-consistent/
  — Character-writing guide: voice shown in two or three sample lines; behavior over adjectives; most important lines first in the definition; persona drift research summary. [practitioner guide] → C-4
- https://documentation.act3ai.com/how-to/adding_voiceover_ai/
  — ACT3 AI docs: three voiceover routes compared; in-pipeline route generates speech from the script so speech length sets shot length and drives mouth shapes. [official docs; consulted for route context] → §2 context

## Searched, nothing usable found (dead ends)

- **clipcraft7 workflow / scripts / prompts** — no disclosure in any result; only format explainers and tool marketing. The banked hole stands.
- **Fruit Love Island / @frutystory line-level process** — press-level process only (scriptwriting, scene planning, redo loops); no scripts or prompts published.
- **Reddit / Discord practitioner threads** — searches surfaced guides and vendor docs, not forum threads; Discord is login-gated and was not attempted, per task rules.
