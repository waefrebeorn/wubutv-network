# ANGLE 1 — Cast Consistency, State of the Art
## Recursive Improvement Pass 2 — 2026-11-18

**Scope:** WuBuTV 60s episodes = 6 units × ~10s, text-to-video generator, native speech in-clip.
Pass 1 adopted a three-leg stack: LOOK / VOICE / PERSONA. In E2, VOICE and PERSONA
effectively did not exist in a checkable form, voices mismatched characters, and no gate
could detect it. This pass asks what the field actually does now, and attacks the stack.

**Grading key — read this before trusting anything below**
- **VERIFIED** — primary source read in this pass (vendor help/docs as returned, paper
  abstract/full text as returned, official product guide excerpt).
- **INFERRED** — synthesis across ≥2 secondary/practitioner sources that agree, or a
  vendor claim relayed by a secondary source that checked the vendor docs. Directionally
  reliable, not independently benchmarked here.
- **LEAD** — single practitioner claim, marketing claim, or proposed-but-untested workflow.
  Treat as a hypothesis to test on one unit, not as law.

**Honest gaps:** Direct page opens of some vendor help centres resolved to secondary
reviews in the fetcher (Runway, ElevenLabs). Where that happened the claim is graded
INFERRED, not VERIFIED, and the secondary's own "checked against vendor docs on [date]"
statement is the provenance. No hands-on generation was done in this pass (per brief).

---

## Executive verdict (5 lines)

1. The field has moved from "repeat the description" to **stored, reusable identity
   assets**: a named reference set / Element / trained identity that is *bound* to every
   generation, not re-described per shot. Text-only identity is now the known-weak route.
2. **Voice is being bound to the same asset as face** in the newest systems (Kling
   Elements, Seedance audio references) — or taken *out* of the video model entirely and
   owned by a pinned TTS voice ID. Nobody serious relies on a text voice description
   inside a native-speech video prompt as the lock. That is exactly what E2 did.
3. Persona cards are **not theatre, but they are weak medicine**: structured traits beat
   unstructured traits in the one controlled comparison found, yet persona instructions
   measurably drift within ~8 dialogue rounds and trait adjectives often fail to change
   behaviour. A persona leg only earns its place if it is written as *observable
   behaviour + example lines* and *re-injected per unit*, not filed once per series.
4. Three legs are **not enough**. The field's working stacks have at least two more:
   **(4) STATE** — wardrobe / injury / prop / relationship / knowledge state, versioned
   per episode with a start-state and end-state; and **(5) PERFORMANCE** — motion,
   gesture and delivery signature, increasingly supplied by a driving performance or a
   motion reference rather than adjectives. A sixth, **MEASUREMENT**, is not a creative
   leg but a gate leg: embedding-based face and speaker scoring, which is mature,
   cheap, and precisely the detector E2 lacked.
5. **Weakest leg as specified: VOICE.** LOOK has a real mechanism (reference images
   condition the model). PERSONA has a weak-but-real mechanism (the writing model reads
   it). VOICE as specified — a structured text spec + an enrollment sample + a pinned
   engine — has *no mechanism at all* if the shipped audio is the video model's native
   speech: the spec is a suggestion the sampler re-rolls per unit, and the enrollment
   sample is never heard by that model. See §2.3.

---

## 1. IDENTITY / LOOK — how it is actually locked now

### 1.1 The three mechanisms, in order of strength

**Claim 1.1a — Reference images are now the default mechanism, offered natively by
every major video model, with small hard caps.** Veo 3.1 "Ingredients to Video" /
reference-images mode accepts **up to 3 images of a single person, character or
product** to preserve appearance; Runway Gen-4 References accepts **up to 3 tagged
references** called in-prompt as `@name`; Kling Elements take **1 main + up to 3
supplementary** images per element; Seedance 2.0's `@` system takes up to 9 images /
3 video / 3 audio in the secondary comparisons found.
— **VERIFIED** for Veo (Google AI docs excerpt: "up to three reference images…
preserve the subject's appearance") and for Kling (official Element Library guide
excerpt: "at least 2… up to 4 reference images (1 main + 3 supplementary)").
— **INFERRED** for Runway caps and Seedance caps (secondary guides checking vendor docs).

**Claim 1.1b — Trained identity (LoRA / Soul ID-style) is the stronger, series-scale
mechanism, and it is a *different job* from a reference sheet.** Practitioner consensus
in the sources read: a per-character LoRA holds *identity* (face, hair) across episodes;
a locked reference sheet holds *clothing and look*; neither does the other's job.
The working recipe is convergent across independent guides: **15–40 curated images,
varied in angle / expression / lighting / outfit, captioned for everything *except*
identity, unique trigger word, ruthless culling of any drifted training image.**
Higgsfield Soul ID is the hosted version of the same idea: train once on **20–80
photos (≥20 required, ≥960px, varied angles/expressions, ≥1 full-height, no
sunglasses/heavy shadow)**, reuse the trained identity across its image family and
into Seedance video as an Element; one Soul ID = one person, and it is explicitly
"clearly the same person, not an exact copy."
— **VERIFIED** for Soul ID parameters (Higgsfield help-centre excerpt, updated
2026-11-11). **INFERRED** for the LoRA recipe (multiple independent practitioner
guides agree on ranges; no controlled study found). **LEAD** for "use both, score
them separately" — that specific A/B protocol was posted as *proposed, not tested
at series scale* by its own author. Copy the honesty, not just the protocol.

**Claim 1.1c — Native multi-shot generation is the third, newest mechanism:** Kling
VIDEO 3.0 Multi-Shot generates up to ~6 connected shots in one 3–15s generation with
element references preserving face/clothing across the internal cuts. This moves the
consistency problem *inside* one generation for short sequences — relevant to WuBuTV
only as a benchmark: a 10s unit with an internal cut is safer than two 5s generations
stitched, all else equal.
— **INFERRED** (vendor guide as summarised in an evidence-led review of Kling's
official guides; claim is vendor positioning, not independently benchmarked there).

### 1.2 What practitioners say actually works / fails

- **One canonical reference, reused byte-identically, beats fresh uploads.**
  "Pick exactly one face reference and one optional body reference… use the exact same
  reference image across every clip" — one testing blog reports ~30% fewer drift
  incidents vs. re-uploading varied images, and diminishing returns after 2 references
  on Runway. — **LEAD** (single-source, self-reported benchmark, no methodology
  published). The *direction* (don't churn references) is **INFERRED** — it recurs in
  Veo, Kling and episodic-series guides independently.
- **Never chain a drifted frame forward.** Multiple guides give the same rule in
  almost the same words: if a render drifted and you feed its frame back as the next
  reference, the drift becomes the new baseline. Always re-anchor to the *original*
  approved source. First-frame→last-frame chaining is for *adjacent continuity*,
  not for identity storage. — **INFERRED** (convergent practitioner rule; also the
  logical consequence of Claim 1.4's between-clip numbers).
- **Reference quality spec is convergent:** front or ¾ view, even neutral lighting,
  neutral expression, clean background, face large in frame. Runway's help guidance
  (relayed) and Kling's and Higgsfield's guides all specify essentially this.
  Non-frontal references are not a soft weakness — see Claim 1.4. — **INFERRED**,
  with the non-frontal penalty **VERIFIED** as a reported benchmark result (§1.4).
- **Prompt discipline:** keep the identity block *verbatim* across units; change only
  action / camera / location per shot; if the prompt re-describes appearance in new
  words, text and reference fight and drift follows. Several guides state explicitly
  that when drift occurs you should *remove* redundant appearance adjectives and let
  the reference carry identity. — **INFERRED**.
- **Still-first, then animate** is the dominant episodic workflow: resolve identity,
  wardrobe, blocking and partner placement in approved *stills* (where LoRA/reference
  control is strongest and re-rolls are cheap), then animate the approved still.
  Generating a fresh keyframe per shot from LoRA + sheet beats asking one first frame
  to carry identity across cuts. — **INFERRED** (HF forum practitioner + episodic
  guides + Runway References workflow all describe the same shape).

### 1.3 The reference set the field builds (vs. "locked reference panels")

Episodic-series guides converge on a **character bible / reference pack of 8–12
images**: front, profile, back, ¾, full-body, close-up, **3–5 expressions**, action
poses, lighting variants, and **≥2 named outfits** — plus a separate *expression
library that is frozen once built* (episodes call it; they do not redraw it).
One animator case study claims this stack held one face from episode 1 to 10.
— **INFERRED** for the pack composition (two independent episodic guides agree in
detail). **LEAD** for the ep-1-to-10 claim (single creator case study, vendor-blog
hosted, no independent verification).

**Gap vs. Pass 1:** a "locked reference panel" that is a single hero image, or a
panel with no expression set and no profile/back, is *below* the field's minimum.
Video models fail first exactly where the pack is thin: profile, head-turns,
occlusion recovery, and wide shots (body proportions have no anchor in a face crop).

### 1.4 The numbers: identity is measured, and the numbers are humbling

- **ConsisID (CVPR 2025, Peking University et al.)** formalised identity-preserving
  T2V evaluation: **FaceSim-Arc = cosine similarity of ArcFace embeddings** between
  reference and generated frames, plus FaceSim-CLIP and temporal consistency. Its
  headline result (~0.58–0.67 FaceSim-Arc vs. 0.32–0.36 for prior open methods) shows
  even a SOTA research system sits far from 1.0. — **VERIFIED** (paper, arXiv/CVPR
  open access).
- **Face Consistency Benchmark (2025):** within a *single* generated clip, face drift
  is **2.1×–5.7× worse than real footage** (ArcFace cosine distance 0.0843 real vs.
  0.1734 best model / 0.4843 worst). — **VERIFIED** as reported in the benchmark
  paper's abstract/framework as returned; relayed figures via a secondary page that
  cites it are consistent.
- **Between clips is the real number, and it is ~0.54–0.59 ArcFace similarity** for
  reference-conditioned methods in the ContextAnyone comparison (relayed), and
  **non-frontal reference images drop identity scores by >50%** on the strongest
  published baseline in the FaithfulFaces result (relayed). — **LEAD/INFERRED**:
  relayed by one unusually source-careful vendor page that names its sources and
  disclaims having run the benchmark itself. Treat the magnitudes as planning
  figures, not as measurements of WuBuTV's generator.
- **Full-body identity is the open frontier:** WildActor (2026 preprint) argues
  face-encoder-based methods "overemphasize discriminative facial cues… while
  ignoring the body," and proposes body-level benchmarks. I.e., a face-score gate
  alone will pass takes whose *body, gait and silhouette* have changed. — **VERIFIED**
  (preprint abstract as returned).

**Planning consequence:** at ~0.55 between-clip similarity for the *best published*
reference methods, "the reference guarantees consistency" is false for every tool
on the market. The correct production posture is **generate → measure → re-roll the
keyframe**, with the reference as the largest single lever, not as a lock.

---

## 2. VOICE — how it is actually locked

### 2.1 The three real architectures (only three exist)

**Architecture A — Pinned TTS voice ID, video model muted / lip-driven.**
Each character owns a *saved voice object* — an ElevenLabs library voice, a Voice
Design result saved to the account, or a clone — addressed by a stable **voice ID**,
with pinned model + pinned settings. All lines for that character, in every episode,
are generated through that ID. This is the architecture behind e.g. ACT3 AI's
"Voice Profile per digital actor" (ElevenLabs generates all of the actor's dialogue;
the video side syncs lips to it). — **INFERRED** (production-platform docs page +
convergent creator workflows).

**Architecture B — Voice *bound into* the video model's character asset.**
Kling 3.0 Omni Elements: a character element built from a 3–8s character video
(extracting appearance **and native voice**) or from 2–4 images **plus a 5–30s
clean single-speaker speech file** (clean background, moderate speed, neutral,
consistent emotion) — the voice is then bound to the element and reused with the
face; Kling's own guidance adds: *if the element already has a bound voice tone,
do not re-specify tone in every prompt* (conflicting instructions degrade it).
Seedance offers the looser version: up to 3 audio references per generation, tagged
in-prompt. — **VERIFIED** for Kling's mechanism and file specs (official Element
Library guide + VIDEO 3.0 guides as returned/summarised). **INFERRED** for Seedance
limits (secondary comparisons).

**Architecture C — Native video-model speech from a text description.**
This is Veo-style: the model invents the voice per generation from whatever vocal
description is in the prompt. **This is not a lock, and the practitioner literature
says so in plain language.** See §2.2.

### 2.2 Failure modes practitioners report (native speech)

- **Per-generation voice re-roll:** "same character, same visual prompt, same scene —
  completely different voice… a 20-year-old streamer, then a 50-year-old narrator,
  then robotic." Cause named by practitioners: no audio seed parity in consumer
  interfaces; the voice description only narrows a distribution the sampler re-draws.
  A 5-part descriptive formula (Age → Gender → Timbre → Tone → Pacing, placed
  *before* the dialogue, verbatim every time) is offered as a *drift reducer* —
  with timbre called the strongest term — not as a fix. — **INFERRED** (practitioner
  guide; mechanism explanation is plausible and consistent with the OneInfer test
  below, but the guide is a vendor blog).
- **Cross-shot voice change confirmed in a listening test:** a Nov 2026 studio test
  of the same two-person scene across models found, for models using *their own*
  voices (Veo 3.1, Grok, Kling 4.0 class): "good speech within a single clip; a
  character's voice could change from one shot to the next," and its summary rule:
  "a model that speaks a language well in one clip doesn't keep a character's voice
  across clips; **that takes a fixed voice**." With each character's voice supplied
  *as a reference*, the same models kept the voices (with word-level errors in some
  languages). — **INFERRED** (single studio's published test, small n, but it is an
  actual listen-and-check test, not a feature list — the strongest practitioner
  evidence found for this exact question).
- **Room tone / ambience discontinuity:** each native-audio generation arrives with
  its own room tone, level and ambience, so cuts are *audible* even when voices
  roughly match; the standard fix is to strip generated ambience and lay one
  continuous bed. Speech level is "quiet and inconsistent between runs." — **INFERRED**.
- **Lip-sync is not enforced in native generation:** mouth and sound are generated
  from the same prompt with nothing forcing frame agreement; error grows with line
  length; multi-speaker shots degrade sharply (one guide cites single-speaker
  success ~80%, multi-speaker <40% — **LEAD**, unsourced figures in that guide).
  The *structural* point (no frame-level constraint; dedicated lip-sync inverts the
  pipeline by driving mouth from fixed audio) is **INFERRED** and uncontested in
  the sources read.
- **TTS-side failure modes (Architecture A is not magic):** ElevenLabs' own guidance
  as relayed: voice choice matters most, model second, sliders least; **Stability**
  trades emotional range against variation between generations (too low → erratic /
  too fast; too high → monotone), **Similarity** too high on a poor source reproduces
  its noise/artefacts; defaults ≈ Stability 50 / Similarity 75 / Style 0. Instant
  clones: >2–3 min of source gives little improvement and *can reduce stability*;
  Professional clones want 30 min–3 h of clean, single-speaker, same-mic,
  same-tone audio. Voice Design (text→voice) is called **experimental** by
  ElevenLabs itself, which recommends a Professional Voice Clone "when one voice
  must stay the same across a project." — **INFERRED** (secondary guides that quote
  and cite the official docs, checked Oct–Nov 2026; direct doc open failed in this
  pass — see Gaps). The *shape* — a designed voice is a starting lottery ticket,
  a saved/cloned voice ID is the lock — is consistent across all sources.

### 2.3 Verdict on WuBuTV's VOICE leg as specified

The Pass-1 spec (structured text spec: age·accent·pitch·pace·texture·trait·breaks
+ enrollment sample + pinned engine) is a correct spec **for Architecture A** and a
**dead letter for Architecture C**. If episodes ship with the video model's native
speech:
- the text spec is, at best, the §2.2 drift-reducer (worth keeping — verbatim, before
  the line, timbre-first in importance);
- the enrollment sample does nothing (the video model never receives it, unless the
  specific route accepts audio references — in which case the sample must be an
  actual *per-unit input field*, not a bible attachment);
- the "pinned engine" pins the wrong engine (the TTS engine is not the thing talking).

**Therefore the template must force an explicit per-show `VOICE_ROUTE` declaration:**
`PINNED_TTS` (voice ID + model + settings are the lock; native audio muted/stripped)
or `AUDIO_REFERENCE` (enrollment clip attached to every speaking unit) or
`NATIVE_TEXT_ONLY` (knowingly unlocked — permitted only for non-recurring voices,
with the ear-test gate carrying the full load). E2 effectively ran the third route
while documenting the first. That mismatch — not the spec's wording — is the failure.

### 2.4 Voice measurement exists too

Speaker-recognition embeddings (x-vector / ECAPA-TDNN / WavLM-SV; 192–512-d,
cosine similarity vs. an enrollment embedding, threshold set by EER on your own
material) are the standard, production-mature way to score "same speaker?"
automatically, and the same cosine-distance method is used to *evaluate* zero-shot
TTS similarity in the research literature. Caveat from that literature: recognition
embeddings reused for TTS evaluation do not rank systems identically to human
listening (H/ASP beat ECAPA in one controlled YourTTS comparison) — so use the
score as a **tripwire** (flag outliers for the ear-test), never as the verdict.
— **VERIFIED** (Springer/arXiv study abstracts as returned).

---

## 3. PERSONA — practice evidence, or theatre?

### 3.1 What the evidence actually says

- **Structured > unstructured, in the one controlled comparison found.**
  CharacterGPT (NAACL 2025 Industry): GPT-4 assistants given *structured* character
  traits (extracted chapter-wise, incrementally updated — "Character Persona
  Training") preserved persona consistency and answered character-knowledge
  questions substantially more correctly than the same system given unstructured
  traits, where "key personality traits or background knowledge are omitted,
  leading to degraded persona coherence." — **VERIFIED** (paper as returned).
  Note what "structured" means there: *discrete, retrievable trait/knowledge items*,
  not a better-written paragraph.
- **But persona instructions decay fast.** Li et al. (Harvard, 2024), *Measuring and
  Controlling Instruction (In)Stability in Language Model Dialogs*: in self-chats
  between two persona-prompted bots, **significant instruction drift within 8 rounds**,
  attributed to attention decay — the system prompt's share of attention shrinks as
  context grows; the effect occurs even at temperature 0 (per secondary analyses).
  A 2026 follow-up line of work (Luz de Araujo et al., EACL 2026, as summarised in
  a research-grounded guide) found persona fidelity falling over 100+ rounds with
  outputs converging toward the *no-persona* baseline. — **VERIFIED** for Li et al.
  (arXiv full text as returned); **INFERRED** for the 2026 extension (secondary
  summary with citations).
- **Trait adjectives are the weakest form.** Zakazov et al. (2024, as summarised):
  models given personalities purely as trait adjectives often did **not** behave in
  line with them, across every model family tested; a counter-study found plain
  trait instructions moved *questionnaire scores* more than example dialogues —
  i.e. adjectives can change what the model *says about itself* more reliably than
  what it *does in scene*. PERSIST (2025, 25 models, 2M+ responses): detailed
  persona instructions produced **mixed** stability effects, and question reordering
  alone shifted personality measurements ~20% of scale. — **INFERRED** (research-
  grounded secondary synthesis + PERSIST abstract as returned).
- **Style convergence is a named failure:** in a 16-model study (Blevins et al.,
  as summarised), models "strongly converge to the conversation's style" — in
  production terms: in a two-hander, both characters drift toward *each other's*
  register, and toward the scene's dominant tone, whatever their cards say.
  — **INFERRED**.
- **Position matters:** *Lost in the Middle* (Liu et al. 2024) — information at the
  start and end of a long input is used more reliably than the middle. A persona
  block buried mid-brief is structurally the least-read text in the brief.
  — **INFERRED** (well-established result, cited in the guide as returned).
- **Practitioner convergence (chatbot/roleplay world, the largest live persona-card
  user base):** the guides that cite the research land on the same recipe —
  define the character by **behaviour and example dialogue, not adjectives**;
  include what the character *does* under pressure / *never does*; keep the card
  short enough to be re-sent whole; **re-inject / restate** rather than assuming a
  long context retains it; test the character before a long run and repair drift
  by restating, not by lengthening. — **INFERRED**.

### 3.2 Verdict for video production specifically

No study found measures persona cards' effect on *video-generator* output — the
video model does not read the backstory; it reads the unit prompt. So for WuBuTV
the persona leg has exactly **two** real points of action, and the template should
name them instead of implying a third:

1. **On the writing model** (script/dialogue generation): real but decaying —
   hence per-unit re-injection (§3.1), behaviour-form entries, example lines.
2. **On the unit prompt, via translation:** persona only reaches the picture/sound
   when a human/agent *translates* it into per-unit observable fields — posture,
   gesture habit, gaze, tempo, the specific line reading. A persona card that is
   not translated is, for the video model, literally theatre.

Pass 1's form (Identity / Personality / Backstory + secret + RENT line, rewritten
per scene) is better than the field's average card in one respect — the per-scene
rewrite is exactly the re-injection the drift research demands — and weaker in
two: it is adjective/paragraph-shaped rather than behaviour+example-shaped, and it
has no *negative* entries (what this character never does/says), which are the
entries that catch the style-convergence failure in a two-hander.

---

## 4. ATTACK — is three legs enough?

**No. The field's working stacks, and the failure list from E2 itself, require
three additions and one demotion.**

### 4.1 Missing leg 4: STATE (continuity of things that *change*)

Every episodic guide found separates **immutable identity** from **versioned state**
and treats conflating them as the classic error:
- **Wardrobe states as named, dated assets:** "everyday / work / rain / injured /
  formal," each with its own references, with the episode+moment where the state
  *starts* recorded; wardrobe "breaks continuity before faces do," and must be tied
  to story time, not re-described ("a black jacket" is not a state). — **INFERRED**
  (two independent episodic guides, near-identical prescriptions).
- **Episode continuity brief:** before boarding, state per character at *opening
  and close*: character version, wardrobe, physical condition, **knowledge,
  emotional state, props held, location history, relationships**. The close-state
  of episode N is the open-state of N+1; changes are *versioned deliberately*
  ("create a new approved version and record where the change begins"), never
  improvised per unit. — **INFERRED**.
- WuBuTV translation: the "worn stake" and hanger ledger already track *plot*
  state; nothing tracks *visible* state. A character can end U3 holding the
  invoice / wearing the wet coat / with a cut hand and start U4 clean, dry and
  empty-handed, and no current leg owns that check. **STATE is the leg that owns it.**

### 4.2 Missing leg 5: PERFORMANCE (motion & delivery signature)

- Identity in the research is already escaping the face: WildActor's premise is
  that production needs "full-body identities across dynamic shots, viewpoints and
  motions," and face-only methods produce "copy-paste artifacts / pose locking."
  Viewers recognise characters by **silhouette, gait, gesture vocabulary, posture
  and tempo** — none of which LOOK (stills) or PERSONA (text) specifies in a form
  a video model can use. — **VERIFIED** (premise, preprint as returned).
- The tooling answer that exists *now* is a **driving performance**: Runway Act-Two
  transfers head/face/body/hand movement, expression *and audio* from a driving
  video onto a character image/video (≤30s, gesture control with image inputs);
  Kling Motion Control does the analogous motion-reference transfer. Where a
  driving performance is not available, the fallback is a *written motion
  signature in observable terms* (e.g. "leads with shoulders, small steps, touches
  the brim before speaking") repeated verbatim — the motion analogue of the voice
  formula, with the same "reduces drift, does not lock" status. — **VERIFIED** for
  Act-Two's mechanism (Runway help article as returned); **INFERRED** for the
  written-signature fallback.
- Delivery signature belongs here too, not in VOICE: *how* lines are played
  (pauses before answering, talks over, whispers the stake line) is performance;
  VOICE should own only *what the voice is*.

### 4.3 Missing leg 6: MEASUREMENT (the gate leg)

E2's deepest failure was not drift — drift is universal (§1.4) — it was that **no
gate could see drift**. The mature, cheap detectors exist and are standardised:
- **Face:** sample frames at start / middle / end + just after any occlusion or
  head-turn (the HF practitioner's cheap protocol, extended by its own author),
  ArcFace/SFace cosine vs. the canonical reference, scored *per character, per
  unit*, face / wardrobe / style scored **separately** (they drift separately).
  OpenCV SFace with a published same-person threshold (~0.363) was used exactly
  this way in the LoRA guide found. — **INFERRED** (protocol), **VERIFIED**
  (metric standardisation, ConsisID/FCB).
- **Voice:** speaker-embedding cosine vs. the enrollment sample per speaking unit,
  used as a tripwire feeding the (human/agent) ear-test, per §2.4. Plus the
  zero-tech checks the guides insist on: *check face and voice independently* —
  a consistent face does not prove a consistent voice.
- **Negative-reference sets** (the one attack item with *no* field support found):
  no vendor feature or practitioner workflow found uses "this is NOT her" image
  sets as conditioning. Negative *prompt* text exists everywhere but is generic.
  The productive form of the idea is therefore **gate-side, not generation-side**:
  keep a **reject bank** — approved stills of *known drift modes* (the age-shifted
  face, the wrong-jaw render, the other character's voice) — and score new takes
  against the reject bank too: a take closer to a reject exemplar than to canon
  fails even if its absolute canon score passes. — **LEAD** (this pass's synthesis;
  no source claims it — flagged as ours to test).

### 4.4 Which leg is weakest, ranked

1. **VOICE — weakest, structurally** (§2.3): no mechanism on the native route.
2. **PERSONA — second weakest**: real mechanism, fast decay, wrong shape
   (adjectives/paragraph vs. behaviour/examples/negatives), and no translation
   step into unit prompts.
3. **LOOK — strongest of the three, still under-specified**: mechanism is real,
   but a single panel is below the field minimum (§1.3), there is no state split
   (§4.1), and without §4.3 it is a hope rather than a checked condition.

### 4.5 Two further attacks the brief did not list

- **Two-character scenes are the worst case for every leg simultaneously:**
  multi-speaker native dialogue degrades (§2.2), persona style-convergence pulls
  both voices/registers together (§3.1), and reference systems have hard per-shot
  element limits (Kling Motion Control: *one* facial element per shot; Higgsfield
  Soul: one identity per generation). The existing E3 law (≤2 speakers, F-25 load
  cap) is directionally right; the template consequence is to require, per
  two-character unit, *which* character is reference-bound and which is
  prompt-carried — never assume both are locked. — **INFERRED/VERIFIED mix**
  as cited per item above.
- **Seed/parameter pinning is mostly folklore for hosted video models:** episodic
  guides prescribe "lock the seed," but hosted Veo/Kling/Runway routes do not
  expose a reliable cross-generation seed for video+audio (§2.2's "no audio seed
  parity" is the audio case). Record every parameter the route *does* expose in
  the unit log (model version, mode, reference IDs, settings) — reproducibility
  bookkeeping is achievable; seed-lock as a consistency strategy is a **LEAD**
  that should not be load-bearing in the template.

---

## SOURCES

- https://kling.ai/quickstart/klingai-element-library-3-user-guide — Kling official Element Library guide (as returned): elements from 1 main + up to 3 supplementary images or character video; 3.0 Omni voice binding to character elements; element binding in image-to-video. Supports §1.1a, §2.1B.
- https://aistudio.google.com/docs/veo?hl=he — Google AI Veo 3.1 docs (as returned): up to 3 reference images to preserve a person/character/product's appearance; first/last-frame modes. Supports §1.1a.
- https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-create-and-use-a-soul-id-character — Higgsfield help centre: Soul ID training set (≥20, up to 80 photos, ≥1 full-height, varied angles), one identity per Soul ID, carries into Seedance as an Element, not exportable. Supports §1.1b, §4.5.
- https://higgsfield.ai/blog/keep-ai-character-consistent — Higgsfield blog: Soul ID mechanics, 3–5 min training, reference-vs-trained distinction. Supports §1.1b.
- https://help.runwayml.com/hc/en-us/articles/42311337895827-Performance-Capture-with-Act-Two — Runway help: Act-Two driving performance + character image/video, gesture control, ≤30s, environmental motion added for image inputs. Supports §4.2. (Search-result excerpt read; direct open resolved to a secondary review — mechanism also corroborated there.)
- https://arxiv.org/html/2411.17440 — ConsisID (CVPR 2025): frequency-decomposition identity preservation; FaceSim-Arc/FaceSim-Cur definitions and results. Supports §1.4, §4.3.
- https://openaccess.thecvf.com/content/CVPR2025/papers/Yuan_Identity-Preserving_Text-to-Video_Generation_by_Frequency_Decomposition_CVPR_2025_paper.pdf — ConsisID published version. Supports §1.4.
- https://arxiv.org/html/2505.11425v1 — Face Consistency Benchmark for GenAI Video: ArcFace/FaceNet/SFace embedding framework, within-clip drift vs. real footage. Supports §1.4, §4.3.
- https://arxiv.org/html/2603.00586v1 — WildActor preprint: full-body identity, face-centric methods neglect body, pose-locking artefacts. Supports §1.4, §4.2.
- https://arxiv.org/html/2402.10962v4/ — Li et al. 2024: instruction/persona drift within 8 rounds, attention decay, split-softmax. Supports §3.1.
- https://aclanthology.org/2025.naacl-industry.24.pdf — CharacterGPT (NAACL 2025): structured traits + incremental persona training beat unstructured traits for persona consistency. Supports §3.1.
- https://lunelle.ai/guides/keep-ai-characters-consistent/ — Research-citing guide: drift studies (Li 2024; Luz de Araujo 2026; Blevins; Zakazov), Lost-in-the-Middle placement, behaviour-vs-adjective guidance. Supports §3.1 (secondary synthesis).
- https://askaillex.com/guides/train-a-character-lora/ — Practitioner LoRA recipe: 20–40 images, vary everything except identity, caption-except-identity, unique trigger, cull drift. Supports §1.1b.
- https://www.promptus.ai/blog/train-lora-consistent-character-comfyui — Practitioner LoRA run with SFace scoring (0.363 same-person threshold), strength 0.35 vs 1.0 failure, picture-LoRA→video via first frame. Supports §1.1b, §4.3.
- https://discuss.huggingface.co/t/keeping-a-character-consistent-across-a-multi-episode-series-once-images-go-to-video-lora-reference-images-or-both/191085/2 — Practitioner answer (self-flagged as proposed, AI-agent-posted): LoRA for identity + sheet for wardrobe, fresh keyframe per shot, last-frame chaining only for direct continuations, mid-frame cheap check. Supports §1.1b, §1.2, §4.3.
- https://aiunpacking.com/blog/consistent-ai-characters-video-workflows/ — 2026 survey-style guide: Veo Ingredients, Runway References, Kling Elements, multi-shot, Sora cameo shutdown. Supports §1.1 (secondary corroboration).
- https://genmagic.co/blog/consistent-characters-ai-video — 2026 guide: cross-shot degradation, per-model reference caps table, four identity tools. Supports §1.1a, §1.4 (secondary).
- https://www.hackaigc.com/blog/ai-video-character-consistency-workflow-2026 — Self-reported 200+ clip testing: one canonical face reference, diminishing returns after 2, ~30% fewer drift incidents with identical reference reuse. Supports §1.2 (LEAD-grade).
- https://kingy.ai/news/kling-3-0-review-a-serious-step-toward-ai-video-as-a-production-system/ — Evidence-led review of Kling's official VIDEO 3.0 / Omni guides: Multi-Shot, voice-bound elements (3–8s character video; 5–30s speech file specs), "don't re-specify bound tone," mode-dependent native-audio limits. Supports §1.1c, §2.1B.
- https://www.vidau.ai/veo-3-voice-consistency-proven-formula-for-better-results/ — Practitioner: native Veo voice re-roll, no audio seed parity, 5-part voice formula (age/gender/timbre/tone/pacing) as drift reducer. Supports §2.2.
- https://studio.oneinfer.ai/blog/ai-video-in-indian-languages — Studio listening test (Nov 2026): model-native voices change across shots; fixed cast voices / voice-as-reference keep character voices. Supports §2.2, §2.3.
- https://videoaigenerator.ai/ai-video-generator-with-sound — Native-audio analysis: per-generation room tone/level inconsistency, lip-sync not frame-enforced, strip-and-lay-one-bed fix. Supports §2.2.
- https://www.aicreatoru.com/blog/kling-ai-lip-sync — Seedance audio-reference mode specs (≤3 clips, 2–15s), Kling native dialogue, mode exclusivity (audio-reference vs first/last-frame). Supports §2.1B.
- https://www.linkmodel.ai/blog/seedance-2-0-vs-kling-3-0 — Comparison: Seedance @ reference system (9 img / 3 vid / 3 audio), joint audio-video generation. Supports §1.1a, §2.1B (secondary).
- https://aiproductivity.ai/guides/elevenlabs-audio-quality-optimization/ — ElevenLabs settings per official docs: Stability ~50 / Similarity ~75 / Style 0 defaults, slider trade-offs, v4 setting availability. Supports §2.2 (TTS).
- https://aiproductivity.ai/guides/elevenlabs-voice-cloning-tutorial/ — ElevenLabs cloning per official docs: IVC ≤~3 min guidance, PVC 30 min–3 h, clean consistent source rule. Supports §2.2 (TTS).
- https://www.ivanm.dev/vault/voice-design-description/ — Voice Design prompt order per ElevenLabs docs; note that ElevenLabs calls Voice Design experimental and recommends PVC for cross-project consistency. Supports §2.2 (TTS).
- https://link.springer.com/chapter/10.1007/978-3-032-02548-7_8?error=cookies_not_supported&code=a7966032-29d8-4402-bf67-38fc18c13afa — ECAPA-TDNN / x-vector / H/ASP comparison in zero-shot TTS: objective cosine-distance evaluation, recognition embeddings ≠ TTS ranking. Supports §2.4.
- https://ciaro.pro/answers/make-ai-episodic-series — Episodic workflow: character bible with wardrobe states + voice + behaviour, reference pack (front/profile/¾/full-body/expression/action/lighting), episode continuity brief (open/close state), versioned changes, continuity-log review. Supports §1.3, §4.1.
- https://www.lollipop.im/blog/creator-story-character-bible/ — Animator case study: 8–12-image bible, frozen expression library, anchor + seed protocol, per-episode spot-checks. Supports §1.3 (composition INFERRED, longevity claim LEAD).
- https://www.techloy.com/how-to-maintain-character-consistency-across-an-ai-microdrama-series/ — Microdrama continuity system: series source of truth, identity vs. state separation, wardrobe-as-continuity, locked-vs-shot prompt split, previous-shot chaining. Supports §4.1, §1.2.
- https://documentation.act3ai.com/features/elevenlabs/ — ACT3 AI production docs: per-actor ElevenLabs Voice Profile, all dialogue via that profile, clone from 5–10 min sample in their workflow. Supports §2.1A.

---

## Template consequences

Concrete field-level changes recommended for the production brief template.
(Fields are named so they can be pasted into the brief schema.)

### LOOK — replace the single "reference panel" with a pack + binding record
1. `LOOK_PACK` (per character, series-level, frozen): required slots —
   `front_neutral`, `three_quarter`, `profile`, `full_body`, `close_up`,
   `expression_set[3–5 named]`, `back_or_silhouette`. A character may not enter
   production with any slot empty; wide-shot-heavy shows require `full_body`
   to be a *video-tested* still, not only a generated portrait.
2. `CANONICAL_FACE_REF` — exactly one file, named + hashed, designated as the
   scoring anchor and the only permitted re-anchor source. Add explicit rule
   field: `REANCHOR_RULE: never chain a drifted frame; re-anchor to CANONICAL_FACE_REF`.
3. `LOOK_BLOCK_VERBATIM` — the identity sentence(s) pasted byte-identically into
   every unit prompt; brief lint: any unit whose look block differs from canon
   fails pre-flight. Appearance adjectives *outside* the block are forbidden
   (they fight the reference).
4. Per unit: `REFS_BOUND` — list which pack slots / element IDs are actually
   attached to *this* generation (not "available in the bible"). Unbound units
   are flagged as text-only and get a stricter gate.
5. Per two-character unit: `PRIMARY_BOUND_CHARACTER` — which character carries
   the reference/element binding this unit; the other is declared prompt-carried.

### VOICE — force the route declaration; make the lock a real object
6. `VOICE_ROUTE` (per show, mandatory, one of): `PINNED_TTS` /
   `AUDIO_REFERENCE` / `NATIVE_TEXT_ONLY`. `NATIVE_TEXT_ONLY` is invalid for a
   recurring speaking character unless the brief carries an explicit waiver line.
7. If `PINNED_TTS`: `VOICE_ID`, `TTS_MODEL_ID`, `VOICE_SETTINGS{stability,
   similarity, style, speed}`, `ENROLLMENT_FILE` (path + duration + sha).
   Changing any of these mid-season requires a version bump + note, like a
   recast. Native generated audio on speaking units: `NATIVE_AUDIO: STRIP`.
8. If `AUDIO_REFERENCE`: `VOICE_REF_CLIP` becomes a **per-unit input field**
   (5–30s, clean, single-speaker, neutral) attached to every speaking unit —
   and a rule field: `BOUND_TONE_RULE: do not re-describe tone in the prompt
   when a voice is bound` (per Kling guidance).
9. Keep the structured spec, rename it `VOICE_SPEC_TEXT` and mark it in the
   template as *fallback / drift-reducer only — not a lock*. Order fixed:
   age · gender · timbre · pace · accent · trait · breaks, placed **before**
   the dialogue line in every unit prompt, verbatim.
10. Per speaking unit: `SPEAKER_EMBED_SCORE` (cosine vs. enrollment) recorded
    in the gate log as a tripwire + `EAR_TEST: PASS/FAIL` as the verdict field.
    A unit may not ship on embedding score alone, nor on ASR transcript alone.

### PERSONA — change the shape, add negatives, add translation
11. Rewrite persona entries from adjectives to behaviour: each trait becomes
    `TRAIT → OBSERVABLE_BEHAVIOUR` + `EXAMPLE_LINE` (a line only this character
    would say, in their words) + `NEVER_DOES / NEVER_SAYS` (≥2 entries —
    the anti-convergence check for two-handers).
12. `PERSONA_INJECTION: PER_UNIT` — the brief must restate the character's
    behaviour entries inside *each unit's* writing block (top or tail of the
    unit block, never buried mid-brief), not once at episode head. This is the
    drift-research consequence; a series-level-only persona is non-compliant.
13. New mandatory per-unit field: `PERSONA_TRANSLATION` — 1 line converting
    persona into what the video model can actually render this unit: posture /
    gesture habit / gaze / tempo / line-reading. If this field is empty, the
    persona leg is declared decorative for that unit in the gate log.
14. Keep `SECRET` and `RENT` — but RENT must be restated in the unit where it
    is *paid or refused*, not only in the character header.

### STATE — new leg, new fields (per character, per episode)
15. `STATE_OPEN{wardrobe_state_id, condition, props_held, knowledge, emotion,
    relationship_delta}` and `STATE_CLOSE{...same fields}` per character per
    episode; `STATE_CLOSE` of Ep N must equal `STATE_OPEN` of Ep N+1 or carry
    a `STATE_CHANGE_NOTE` (when/why the change begins on screen).
16. `WARDROBE_STATES` (series-level): named states, each with its own reference
    still(s); units reference a state ID, never a free-text clothing description.
17. Per unit: `STATE_ASSERT` — one line: "at unit start, [character] is in
    wardrobe state X, holding Y, condition Z" — checked at the joint gate
    alongside last-frame/first-frame cohesion.

### PERFORMANCE — new leg
18. `MOTION_SIGNATURE` (per character, verbatim across units): 3–5 observable
    entries — gait/posture lead, gesture habit, stillness behaviour, tempo —
    written like the voice formula (observable, not adjectives).
19. `PERFORMANCE_SOURCE` per speaking/acting unit: `DRIVING_CLIP` (path) /
    `MOTION_REF` / `TEXT_ONLY`. `TEXT_ONLY` units inherit the stricter gate.
20. `DELIVERY_NOTE` per line (in PERFORMANCE, not VOICE): pause/overlap/whisper
    etc. — separates *what the voice is* from *how this line is played*.

### MEASUREMENT — new gate fields (in every GATE_LOG)
21. `FACE_SCORE` per character per unit: ArcFace/SFace cosine of sampled frames
    (start / mid / end / post-occlusion) vs. `CANONICAL_FACE_REF`, with
    `WARDROBE_SCORE` and `STYLE_SCORE` as separate human/agent verdicts —
    three scores, never one blended "consistency" mark.
22. `REJECT_BANK` (series-level, growing): stills/clips of known drift modes per
    character; gate rule — a take nearer a reject exemplar than canon fails
    regardless of its absolute score. *(LEAD-grade innovation, ours: test on
    one show before making it law.)*
23. `CAST_LOG` per episode (the reproducibility record): model + version, mode,
    reference/element IDs bound, voice route + IDs, settings — everything a
    future agent needs to re-create the cast exactly. Seed recorded if the
    route exposes one, but never cited as the consistency mechanism.

### Deletions / demotions
24. Delete any template language implying a text description "locks" a voice or
    a face. Replace "locked" throughout with "bound (asset attached) /
    carried (text only)" — the template's vocabulary should make the E2 failure
    (documented as locked, actually carried) impossible to write down.
25. Demote `BACKSTORY` from the per-episode brief to the series bible; per
    episode keep only `BACKSTORY_ACTIVE_FACT` (the one fact this episode uses).
    Long mid-brief backstory is the least-read, most-diluting text in the brief.
