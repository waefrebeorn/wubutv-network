# PROMPTING AND COHESION — how the top brainrot / fruit-soap factories actually make it

**Lane:** LEARN DEEPLY (user order, Telegram msg 1249, 2026-11-27, STANDING):
"prompting like them and making like them is the way / learning frame
cohesion and reference proper usage."
**Written:** 2026-11-27, for the parent to fold into Slopcannon + the
episode pipeline. No SKILL.md was edited by this lane.
**Companion bank:** `deadsun-promptcraft-20261124/STUDY.md` already covers
one creator's prompt craft in depth (DeadSun — an MV maker, not a
factory); this report covers the *factories* and the tool-community
literature around them, and cross-references DeadSun only where he is
the control case.

## Evidence discipline — read this first

Four grades are used throughout, and they are not interchangeable:

- **PUBLISHED** — prompt text, a tutorial, or a stated method that a
  named source put on the public record and this lane read.
- **MEASURED** — counted from a published corpus of real prompts
  (the Flick canvas studies) or measured on our own tool (the
  video-api-mastery lab).
- **INFERRED** — reconstructed from the factories' finished artifacts
  (frames, consistency patterns, encode fingerprints) by our study
  waves. Labelled every time.
- **NOT KNOWABLE** — stated plainly where it applies (§5).

**The headline honest negative:** *no named factory in our corpus
publishes its prompts, tools, or workflow.* The clipcraft7 study
verified this as a negative (X bio/posts content-only, YouTube
descriptions empty, zero tutorial/prompt coverage of the account);
the overcookmyself study likewise documents no tools. FruitStudio,
thecontentlab01's factory, MemeBomba and Orange Cat Philosophy are
the same: silent. So "how they prompt" is known from three
directions that converge — (a) the tutorial industry that teaches
the genre's standard stack, (b) the tool communities' published
prompt corpora and guides for the same models, and (c) artifact
inference from our own frame-level studies. Where all three agree,
confidence is high. Where only (c) speaks, it says INFERRED.

---

## §1. PROMPTING

### 1.1 The production shape every source converges on

**Assets before generation → one clip per shot/setup → a short
behaviour prompt riding on the assets → voices, captions and score
finished in post.** This is the genre-standard stack as taught
(VdoBloom's fruit-drama walkthrough: design the character as a still,
make one starting frame per scene, animate it image-to-video with the
dialogue written into the prompt, join in CapCut; ToonlyAI's episode
guide: cast sheet → reference image per character → 3–4 clips of
6–10 s → stitch), it is the stack our overcookmyself study found the
genre's output *consistent with* (LEAD-LEVEL there, since that
creator documents nothing), and it is what artifact inference finds
inside the factories themselves: boss_bee_'s college soap reads as
"one generated clip per setup, image-to-video, with a short
motion/performance prompt" over character stills (§B.6/C of that
study), and clipcraft7's frutinovela reads as still-first I2V,
per-scene generation, loose assembly (INFERRED, high confidence).

Nobody in this economy writes one giant prompt per episode. The
episode is an *assembly* of per-shot generations.

### 1.2 Prompt structure — four documented forms

**(a) The fruit-drama tutorial form (PUBLISHED — VdoBloom, ToonlyAI,
Vmake genre guides).** Per clip: the character's full description
block, the scene, ONE line of dialogue, a style phrase. The cast
sheet's Look column is copied "word for word into each clip prompt"
(ToonlyAI). Google's own Veo guidance, quoted in the same guide:
name each character, give them a voice style, and **repeat the full
description unchanged in every prompt**. Sample master prompts in
the Vmake guide run ~35–45 words total: face/expression + quoted
line + scene + lighting + "4k". These are *short* prompts; the
description block is the only long part, and it is a constant, not
writing.

> ⚠ **FLAG F-08 (flag pass, 2026-11-27):** the "Google's own Veo
> guidance" attribution in (a) above is SECONDHAND — it reaches this
> packet quoted inside ToonlyAI's guide, not from Google's guide
> itself. The deep-research pass opened Google's actual Veo 3.1
> guide: it teaches the five-part formula and Ingredients (reference
> images carry identity) and does NOT instruct repeating the full
> description unchanged in every prompt. Read the repeat-verbatim
> practice as a genre-guide practice (ToonlyAI / VdoBloom), not a
> Google instruction. Full entry: brainrot-prompting-20261127/
> FLAG_PASS_LEARN_DEEPLY.md, F-08.

**(b) The Veo community form (PUBLISHED — PromptCrate's tested
guide; the 7-component Veo guide; Replicate's Veo guide).** Fixed
order: **camera first** (shot size, angle, one movement, lens feel —
"the model treats the first lines as its strongest instruction") →
**locked character block** (face, build, age as a number, costume,
one prop — copied verbatim into every shot) → **setting and light in
one line** → **one clear action, in order** → **dialogue** → **one
audio sentence** → **negatives list last**. The 7-component version
names the same skeleton: Subject / Action / Scene / Style / Dialogue
/ Sounds / Technical-negative.

**(c) The Seedance form (PUBLISHED — Higgsfield's official
Seedance Prompt Writer skill + director-skill repo, read in our
vibeeverything study; ByteDance grammar via the DeadSun study).**
Six-slot formula in fixed order: **Camera + Subject + Action +
Setting + Style + Lighting**. The fuller template: scene context →
references (by @name) → shot-by-shot action → lighting → **locks**
(end state, set-contents lock, heights, scale anchors). Multi-shot
work is written as **Shot 1 / Shot 2 / Shot 3** sequencing — precise
second timestamps are officially unstable on Seedance 2.0; assets
are bound by type and number (@Image1…). Long takes are beats in
prose order joined by *then / as*, one beat every 4–6 s, ending on a
visible state.

**(d) The LTX form (PUBLISHED — LTX's official prompting guide).**
One flowing present-tense paragraph, ~4–8 sentences: establish the
shot → set the scene → describe the action (front-loaded; "a bare
noun phrase returns a near-static clip") → characters → camera →
describe the audio, dialogue in quotation marks, language/accent
named. Emotion is written as physical cues, never abstract labels.

**The Flick corpus is the measured control for all four (MEASURED —
thousands of real, published prompts across 67 films):** Yao's
kept prompts open with the camera in 191 of 206; one look line is
reused word-for-word in 196 of 254 video prompts of one film;
Lifeguard's 69 prompts share a fixed anatomy — GLOBAL SETTINGS
header (duration, aspect, music negative, named ambient bed) →
start frame cited and ordered preserved → one job per reference →
camera lock → hex palette → one timed MOTION block. The forms
differ by vendor; the *invariants* do not: camera/framing early,
identity as a verbatim constant, one action, locks at the end (or
in the header), references cited by name.

### 1.3 Prompt length — where the words actually go

- **Hosted-model budgets are documented and small** (banked in
  video-api-mastery): Kling's own budgets run T2V 60–100 words,
  I2V **15–40 words of motion/camera only**. Seedance hosted routes
  cap around ~2,200 characters (2.0) / ~4,000 (2.5).
- **Requirement load, not word count, kills adherence** (PixVerse's
  tested guide, banked): the first sentence carries the most
  control; later details compete rather than reinforce.
- DeadSun's one verbatim published prompt is ~120 words, one
  paragraph — and his "thousands of words" Seedance practice is the
  outlier that lives on local/composer surfaces with section
  review; the DeadSun study already adjudicated it: *length
  transfers as a budgeting discipline, not a word count.*
- The fruit-drama tutorial prompts (§1.2a) are the shortest of all —
  because the still has already spent the identity words. **Length
  is inversely proportional to how much the references carry.**
  That, not a word target, is the law the factories run on.

### 1.4 Identity anchoring — three schools, and they contradict for a reason

1. **Verbatim text block** (fruit-drama tutorials; Google's Veo
   guidance; Atlas's Seedance MV guide: a 40–60-word character
   sentence "reused verbatim in every keyframe prompt — change a
   word and you risk casting a stranger"; anabology's *Escape
   Velocity*: identity lived in a **written canon in the prompt
   text because reference images drifted**). This is the school for
   text-led models and text-only serials.
2. **Reference-led, text silent** (Kling/Seedance reference-native
   workflows). RefVid's production A/B (PUBLISHED, dev.to, with
   test clips): same three scenes twice on Kling 3.0 Omni — prompt
   only with maximal description vs **no appearance words at all
   plus four reference photos**; only the reference set kept the
   same face. Their rule, verbatim in substance: *"once you attach
   references, stop describing the person in the prompt. When the
   words and the photos disagree, the model blends them, and the
   blend is exactly the drift you were trying to fix."*
3. **Hybrid registry** (Higgsfield/Seedance professional form):
   sheets + named elements carry identity; the prompt text carries
   *locks and current state* (end state, set contents, heights) —
   text stops describing what the character looks like and starts
   policing what must not change.

The contradiction between schools 1 and 2 is model-dependent, not a
disagreement about craft: on a text-led surface, unrepeated identity
is unanchored identity; on a reference-native surface, re-described
identity is a second, competing anchor. Our tool sits between the
two (strong conditioner, no role fields) — which is why our
compressed-vs-full vehicle question stays open until measured
(video-api-mastery flags it as the arbiter test).

### 1.5 Per-shot vs per-scene prompting

The universal unit is **one shot per prompt**: Veo doctrine is
"think in 8 seconds, not in 30 — one place, one moment, one action"
(PromptCrate); VdoBloom budgets one sentence of dialogue per 5–8 s
clip; boss_bee_ and clipcraft7 both read as per-setup/per-scene
generations (INFERRED). Multi-shot single generations exist —
Seedance 2.0's Shot 1/2/3 form, Kling 3.0's AI Director (up to six
specified cuts per 15 s generation), Techhalla's one-take-per-song-
section — but they are the *art-film and MV* wing's tool. The
serial factories' throughput (≈4.6 posts/day at clipcraft7;
1–3 finished episodes/day at overcookmyself) is built on small,
replaceable per-shot fires: a bad shot costs one clip, never a
scene.

### 1.6 Dialogue carriage — three routes in the wild

1. **Native, in-prompt** (the Veo 3 / Seedance serial mainstream):
   the line is written into the prompt. Format is surface-specific:
   `Name: line` with no quotes on one Veo surface, quoted lines on
   another (banked in video-api-mastery); budget ≈ **12–15 words
   per 8 s clip**, one line per shot, long speeches break lip-sync.
2. **Post voice + burned word captions** (boss_bee_, INFERRED from
   frames): mouths move in cartoon approximation, comprehension is
   carried by **word-by-word captions added in post** — "nothing in
   the frames requires native audio generation." clipcraft7's
   dominant text system is the same layer pushed further:
   **one-word karaoke narration**, burned in, carrying whole plots
   (≥9 of 19 posts in the refresh), plus in-world printed text
   (billboards, forehead numbers) doing exposition inside the frame.
3. **No dialogue at all** (Orange Cat Philosophy, via the xaiworlds
   study): wordless vignettes; story carried by costume tokens and
   one object's full journey per compilation. The only divorced
   audio/picture post in the Tier-3 batch (munnaqpj) is also the
   only one that flatlined — the corpus's standing negative proof
   that the audio and the picture must be the same story.

Our shows sit closest to route 1 with route 2's caption layer
(burned karaoke is already house law) — the factories say that
hybrid is legitimate, and that the caption layer is not garnish:
on the biggest accounts it *is* the comprehension system.

### 1.7 Negative prompting — what they actually exclude

- **"No background music" is the one near-universal negative**
  (MEASURED, Flick corpus: 173 of Yao's 217 prompts; **69 of 69**
  Lifeguard prompts — placed in the GLOBAL SETTINGS header, paired
  with a *named positive* ambient bed for the shot; drama corpus
  46%, Seedance reference-to-video corpus 79%). The score is added
  in the edit; the negative exists so the model doesn't invent one.
  Negative alone leaves a vacuum — Lifeguard's form pairs every
  negative with the named thing that replaces it.
- **Veo community form:** a closing list of 8–10 negatives (no
  on-screen text, no watermark, no face drift, no extra limbs, no
  morphing, no flicker, no duplicated characters, no UI, no logo),
  core list constant, 2–3 tailored per scene.
- **"No subtitles / no text"** because burned-in AI text misspells —
  captions are a post layer (VdoBloom, explicit).
- **Vendor reality check (banked):** Seedance's officially endorsed
  negatives are only for subtitles and BGM; Kling has a dedicated
  negative field that is *silently inert in image-to-image mode*;
  Runway supports no negative phrasing at all and warns it can
  invert. In-prose negation is the weakest exclusion mechanism on
  paper — and load-bearing by our own measurement (MV-14 G2). Both
  facts stand; the factories' practice suggests the resolution:
  negatives work as *house constants in a header/footer*, not as
  per-shot improvisation.

---

## §2. FRAME COHESION — how a serial holds together

Ranked by how much of a factory serial's cohesion each mechanism
actually carries, per the evidence:

1. **Character stills/sheets fed per shot (the load-bearing wall).**
   boss_bee_ (INFERRED from the consistency pattern): the lead's
   design — hair shape, tattoos, outfit, sock stripes — holds
   across 9 setups and 2 locations, "too stable for text-only
   prompting; this is reference-conditioned generation (character
   stills or a character sheet fed per shot)," while *background
   characters vary freely — they were prompted per shot, not
   referenced*. Surface detail re-renders slightly between setups;
   enumerated features don't drift — the signature of features
   fixed once, in a still, then carried by reference. Higgsfield's
   sheet discipline (PUBLISHED): 3-view sheet (full-body front,
   full-body back, frontal close-up) on neutral mid-grey — **with
   the faces on the full-body panels erased**, because "a character
   sheet with multiple faces confuses Seedance later — it doesn't
   know which face to lock onto, and your hero slowly drifts scene
   by scene." Yao (MEASURED): the knight's character sheet was used
   in **167 generations** — the single most-used image in the film —
   and *props get sheets too* (a cardboard box with every side
   annotated; a pistol sheet; a flare-gun sheet), each cited by
   exact name, variants as new named sheets, never overwrites
   (alanxiao corpus: 130 of 161 prompts cite a reference by name).
2. **Verbatim text locks.** One look line pasted unchanged into
   every prompt of a world (Yao: 196 of 254; Lifeguard: strict hex
   palettes with "no colours outside this palette" — and the
   palette switch *is* the world switch). Surreailist's variant is
   the extreme: **no start frame at all** — "strong prompt locks/
   stylisation plus references created in Midjourney," where the
   reference set is *scenography* (sets, figures, grade) that
   informs prompts without becoming first frames.
3. **Wardrobe / costume tokens as identity.** Orange Cat
   Philosophy's fat cat is findable in any fragment by checkered
   shorts + green belt + bare belly (xaiworlds study: "costume
   tokens survive the compilation cut"); mviews3's lioness soap
   holds identity with one red dress across a wordless episode.
   Identity is designed at the level generation is stable at —
   a garment, not a face (niceaunties study's formulation:
   continuity that is *categorical, not literal* — subject class +
   mascot props + named places + tone).
4. **Set constants.** Single-location-heavy staging by design
   (overcookmyself: kitchens, restaurants, streets, a hospital —
   "cheap staging"); clipcraft7's whole class story is one location
   pair, squalor vs mansion, reused.
5. **First/last-frame chaining — real, but a minority practice.**
   It exists as a first-class tool feature (Google Flow: Frames to
   Video with start+end frames; Scenebuilder's **Extend** continues
   from a clip's final frames, **Jump To** moves a character to a
   new setting preserving appearance; the documented join is "use
   the last frame of one clip as the first frame of the next").
   Yao used first+last-frame joining on 44 clips and pulled 20
   frames from finished clips to start the next shot (MEASURED).
   But no factory source treats chaining as a *law* — it is one
   joinery option among several, used where a continuous move is
   wanted, and skipped where a cut is fine.
6. **Seed reuse — the weakest leg, mostly marketing.** Vendor
   guides prescribe "generate a DNA check and lock the seed
   number" (Vmake), but our banked measurement stands: seeds are
   best-effort even where they exist, determinism is not
   guaranteed, and our tool has no seed field. No factory artifact
   shows seed discipline; their cohesion survives *without* it,
   carried by refs + locks + tokens.
7. **Voice/register cohesion.** overcookmyself's whole series is
   audio-logo'd by one exaggerated vernacular register and two
   carrier words ("cuh", "homie") — character consistency the
   audience hears. Flow and Kling both now bind a *voice* to the
   saved character asset (Flow Characters: 1–2 images + a voice,
   called by @Name; Kling voice binding from 5–30 s of audio) —
   the platforms have productised register-as-reference.

### Against our STRONG REFERENCE rule (msg 507)

Our rule: last-frame → first-frame conditions the next unit in
world, wardrobe, positions and light, with per-joint eye-verified
cohesion in every gate log (Slopcannon CONTINUITY METHOD, with
resume-chaining measured first-choice and portal-chain joints).

**Where we are THICKER than the factories — keep, do not dilute:**
- *Joint-level verification.* Nobody in the factory corpus
  eye-verifies joints. adi_8xx's Tung Sahur serial generates 17
  clips independently and "the wardrobe/world drift between them
  is simply tolerated" — our own study's verdict stands: our rule
  is strictly better, and load-bearing for dialogue shows where a
  face must survive a conversation, not just a vignette. Their
  drift tolerance is affordable because their identity is carried
  by tokens and design (§2.3); ours is carried by faces in
  dialogue. Different cargo, different hull.
- *Chaining as law vs chaining as option.* For sung/spoken
  continuity across a cut, our measured chain (resume MAE 45.24;
  two-image chain fallback) is more disciplined than anything the
  factories document.

**Where we are THINNER — the actual gaps this lane was ordered to find:**
1. **Asset permanence.** Their sheets/elements are *persistent,
   named, versioned assets reused across episodes and series*
   (Kling Element Library; Flow @Name characters; Higgsfield
   Elements; one sheet used 167 times). Our reference stack is
   per-project and rebuilt per build; panel sheets exist for
   likeness cast, but the shows' own casts have no cross-episode
   named-asset registry. We re-derive identity every build; they
   *file* it.
2. **Sheet geometry.** Our master reference is a composite panel
   sheet — the exact shape Higgsfield warns against (multiple
   faces confuse the lock) and our own video-api-mastery flags as
   *not equivalent* to the cross-vendor consistency unit of **3–4
   separate angle images, frontal first**. The panel-vs-separate-
   angles A/B is already queued in our bank as the highest-value
   open measurement. It is still unrun. The factories' literature
   has already voted.
3. **State carried in prompt text.** Their prompts carry the
   element's *current state* on every reference line and every
   shot's *end state* in prose — the vibeeverything study named it
   "the prompt-text twin of last-frame → first-frame." Our
   chaining is image-level; our vehicle text does not
   systematically state current/end state, so a chain break loses
   state the factories keep in words.
4. **Props are second-class here.** Their hero props get sheets
   and names (box, pistol, spyglass). Our stacks are
   character-centric; the plot-critical prop (a jar, a key, a
   stolen face) is re-described per vehicle instead of referenced.
5. **The look is paraphrased, not locked.** Surreailist's study
   flagged this in our practice on 2026-11-15 — "our LOOK block
   exists, but as description, not as a verbatim lock reused
   across every prompt of a piece" — and it is still true. Their
   look is ONE line, pasted; drift is what happens between prompts
   that each paraphrase it.
6. **No composition-only reference class.** Their sketch/blocking
   references decide framing while carrying *no identity to drift*
   (253 of Yao's 897 image generations consumed a sketch;
   simaypekcan's painted first frame = 3D block + character sheet +
   move). Our storyboards serve likeness builds; the episode
   pipeline has no per-shot composition reference that is
   deliberately identity-free.

---

## §3. REFERENCE USAGE — what they feed, how many, in what role

### Counts and roles (PUBLISHED vendor/community specs)

| Surface | Per-call image capacity | Role system |
|---|---|---|
| Google Flow (Veo) | ≤3 ingredients per prompt; start + optional end frame in Frames mode | Ingredients lock the *subject*; frames lock the *shot*. Combine: make a still with ingredients, use it as the start frame |
| Seedance 2.0 | ≤9 images, ≤3 videos, ≤3 audio (≤12 files mixed) | @Image/@Video/@Audio tags with stated jobs ("@Image 1 as the first frame, @Video 1 for camera language, @Audio 1 for music"); guide slot plans assign 1–3 face, 4–5 costume, 6–7 lighting/style |
| Kling 3.0 | Element = 1 frontal + up to 3 extra views (max 4); up to 7 reference characters per video generation; ≤3 elements bound alongside start/end frames | Element Library: persistent named assets (character / animal / item / costume / scene), called by @name; video elements (3–8 s) extract motion + voice |
| Flick-canvas practice | Sheets + storyboard frames, up to ~7 images (Techhalla) | **One job per reference**, verb-led: "sets the setting / sets the prop / is the character" — generalised from the corpus by Flick's own guide; media.io's Veo tutorial independently lands on the same rule ("three reference images only help when each one has a job": character / product / scene-style) |

Roles observed across all sources: **identity** (frontal face),
**identity-angles** (profile, back, detail — "front tells the model
the face; profile tells it the head shape"), **wardrobe** (the
outfit shown clearly or it cannot be held), **world/set**,
**composition** (sketch, blocking, storyboard frame), **motion**
(reference video — Kling "respects the timing of the video
reference beat-for-beat"; Seedance @Video for camera language),
**voice** (bound audio). And the reference-quality standard is
boringly consistent: frontal, sharp, evenly/neutrally lit, neutral
expression, clean background, outfit visible.

### Mapping to our tool and doctrine

- Our tool takes an ordered, interleaved text/image list with **no
  role fields and no @tokens**; house doctrine never mixes more
  than 2 images; frames and reference images are mutually
  exclusive on the vendor models our wrapper resembles, so a
  3+ image call must first prove every image is actually read.
- Measured on our tool: an image input is **a strong conditioner,
  not a frame source** (frame-0 MAE 43–52 vs refs; the lock
  dissolves by ~0.75 s); identity carries strongest, fine detail
  drifts; **prop singularity comes from the image, not the
  words**; text alone cannot reproduce a reference scene.
- The portable version of their @token system costs us nothing:
  **per-image role sentences** ("Image 1: mood; Image 2:
  character" is MiniMax H3's documented pattern) can ride in our
  interleaved text today — untested here, test already queued.
- **Stills-first adherence (msg 861) is exactly their practice.**
  Every source solves identity in the image stage (character still
  → scene still → animate); the factories' poster frames are
  finished key stills with the text already composed in. We are
  aligned here — the gap is not *whether* stills come first, it is
  *what happens to the still afterwards*: they file it as a named
  permanent asset and feed the same sheet on every shot of the
  series; we spend images per joint (chain frames, per-scene stack
  frames) and fewer on permanent identity.

---

## §4. TRANSPLANT — concrete method changes, each tied to its evidence

For Slopcannon and the episode pipeline. Ordered by leverage.

1. **A named permanent asset registry for show casts.** One
   canonical name per character, prop and set; a variant is a new
   named asset, never an overwrite; vehicles cite assets by name.
   The registry outlives any single build. *(Evidence: Higgsfield
   Elements discipline; alanxiao corpus — 130/161 prompts cite
   references by exact canvas name, variant sheets as distinct
   named objects.)*
2. **Run the queued panel-vs-angles A/B before the next cast lock,
   and default to separate angles meanwhile for new show casts:**
   frontal + profile + back/detail as *separate* images, frontal
   first. *(Evidence: Kling Elements spec; video-api-mastery's
   cross-vendor consensus — "the consistency unit is 3–4 SEPARATE
   angle images per character… NOT equivalent to a composite panel
   sheet"; the A/B is already our bank's highest-value open
   measurement.)*
3. **If panel sheets stay for likeness work, apply the sheet face
   rule:** exactly one face per sheet — blank/erase faces on the
   full-body panels, keep the single frontal close-up face.
   *(Evidence: Higgsfield tutorial, quoted §2.1.)*
   ⚠ **FLAG F-09 (flag pass, 2026-11-27):** this rule is SCOPED,
   not universal — it is Higgsfield's Seedance-ingestion
   discipline. InVideo's consistency method prescribes the opposite
   geometry: front, ¾, profile, back PLUS face and mid-angle
   close-ups on the sheet. Apply the one-face rule where
   Seedance-class sheet ingestion is in play; elsewhere, on-sheet
   close-ups are a legitimate alternative, not a violation. Full
   entry: brainrot-prompting-20261127/FLAG_PASS_LEARN_DEEPLY.md,
   F-09.
4. **One verbatim LOOK LINE per world, pasted unchanged into every
   vehicle of that world** — plus a hex palette object per world
   where worlds alternate, the palette switch carrying the world
   switch, one hex rhyming across worlds to bind them. *(Evidence:
   Yao 196/254 verbatim reuse; Lifeguard's two palettes; the
   Surreailist prompt lock.)*
5. **END STATE + CURRENT STATE in every vehicle.** The action
   block ends with the shot's end state in prose; every reference
   line states the element's current state (worn number, costume
   state, prop in hand, body-ledger state). This is the
   prompt-text twin of last-frame chaining, and it survives chain
   breaks. *(Evidence: Higgsfield END STATE discipline; Seedance
   2.5 guides — "a shot with no end tends to drift or cut early.")*
6. **A GLOBAL SETTINGS header on every vehicle** — duration,
   aspect, music negative *paired with the named ambient bed*,
   house exclusions — bookending the existing {END} footer, so
   the locks live where models read first *and* last. *(Evidence:
   Lifeguard 69/69 header discipline; PixVerse first-sentence
   weight; negative+positive pairing.)*
7. **Role sentences for every image entry** in interleaved calls
   ("Image 1: identity — [name]. Image 2: world — [set]."), one
   job per image, logged in take telemetry until the adherence
   effect is measured. *(Evidence: MiniMax H3's documented
   per-image role pattern; Flick's one-job-per-reference rule;
   media.io's Veo ingredients rule.)*
8. **Prop sheets for plot-critical props.** The jar, the key, the
   stolen face get their own reference sheets, cited by name
   whenever the prop appears — props are cast, not described.
   *(Evidence: Yao's cardboard-box and pistol sheets; the
   btc-shifty study's reference-set logic.)*
9. **A sketch-first composition reference class for problem
   shots:** a drawn/blocked composition image whose only job is
   framing — it carries composition and *no identity to drift*.
   Escalation for shots that keep failing on staging, not a
   default. *(Evidence: Yao — 253/897 image generations
   sketch-referenced, "prompt first, block only on failure";
   simaypekcan's painted first frame.)*
10. **Costume-token design rule for everyone except principals.**
    Background/invader cast gets identity by one permanent
    garment or mark, named in every prompt; principals get
    references, background gets tokens and is prompted per shot.
    *(Evidence: Orange Cat Philosophy's shorts+belt tokens;
    boss_bee_ — principals referenced, background prompted per
    shot.)*
11. **Register as a cited asset.** Each show's spoken register +
    carrier words are written on the cast card and cited in
    dialogue vehicles the way a reference is cited — audio
    cohesion is series identity, and the platforms now bind voice
    to the character asset itself. *(Evidence: overcookmyself's
    vernacular voice engine; Flow Characters and Kling voice
    binding.)*
12. **Two-speed spend, formalised.** Volume/coverage shots fire
    cheap (text-led, loose mode); hero shots fire the full
    stills-first stack; "rejected-energy" takes are recycled as
    tension/cutaway material instead of binned. *(Evidence:
    Techhalla's draft/finish split; VdoBloom — draft model for
    scenes, regenerate only the best on the stronger model.)*
13. **Keep the dialogue budget as a hard vehicle field** — one
    line per clip, ~13–15 words per 10 s unit (our F-25 already
    sits at the factories' measured budget; this ratifies it
    against outside evidence rather than changing it), spelled
    non-lexical sound included. *(Evidence: VdoBloom one sentence
    per 5–8 s clip; Veo guide 12–15 words per 8 s; DeadSun A1.)*

**Explicitly NOT transplanted:** seed-locking (no seed field;
best-effort where it exists); drift tolerance (their cargo allows
it, ours doesn't — §2); text-only identity for principals (school 1
is for text-led surfaces; our measured conditioner law says images
pin what words can't); multi-shot single generations as the serial
default (per-shot fires are the factories' replaceability economy).

---

## §5. What is NOT publicly knowable — said plainly

- **No factory prompt text exists in public.** Not one verbatim
  prompt from clipcraft7's sources, FruitStudio, thecontentlab01's
  factory, MemeBomba, or Orange Cat Philosophy was found by any of
  our study waves or this lane's searches. Anyone quoting "their
  prompt" is inventing it. All factory-side claims here are
  INFERRED from artifacts or are the tutorial industry's version of
  the genre stack.
- **MemeBomba's method is doubly unknown**: the name reaches us
  only as watermarks on another account's reposts (wapiliwatatu
  study) — the craft is attributable, the maker and method are
  not.
- **Tutorial platforms sell a workflow.** VdoBloom/ToonlyAI/Vmake
  guides are real and detailed, and their stack converges with
  artifact inference — which raises confidence — but they are the
  teaching industry's reconstruction, not the factories' disclosure.
- **Vendor prose overstates.** "Starts exactly on your picture,"
  "DNA check," "fixes consistency" — discounted throughout per our
  measured conditioner law (MAE 43–52, lock dissolving ~0.75 s).
- **DeadSun is the control, not a factory.** He is the only creator
  in the wider set with a verbatim published prompt and a stated
  method; he makes MVs. His evidence anchors §1's craft claims
  about *prompting*; it says nothing about factory throughput.

---

## Sources

**Our corpus (all under `~/workspace/research_notes/lilypads/`):**
deadsun-promptcraft-20261124/STUDY.md (DeadSun's verbatim prompt,
LTX/Seedance guides, length map) · bossbee-fakebody-20261124/STUDY.md
(per-shot I2V reconstruction, §B.6/§C) · clipcraft7-20261118/report.md
+ clipcraft7-20261127/BACKLOG_STUDY_2026-11-27.md (still-first I2V,
one-word karaoke narration, two-speed system, verified no-disclosure
negative) · overcookmyself-20261115/report.md (genre stack,
vernacular voice engine, repertory cast) · xaiworlds-20261127/
BACKLOG_STUDY_2026-11-27.md (costume tokens) · vibeeverything-
20261117/report.md (Higgsfield Seedance Prompt Writer: Elements,
sheet face rule, END STATE, cut-format ladder) · techhalla-20261115/
report.md (shot-list prompts, draft/finish split, ≤7 refs) ·
anabology-20261112/report.md (written canon over drifting refs) ·
genresuprcolide-20261122/STUDY.md (canon + signature triad,
corroboration) · surreailist-20261115/report.md (prompt lock, no
start frame) · owendoerr-20261119/report.md + alanxiao-20261120/
report.md + jaimeyao-20261121/report.md (Flick corpus counts:
headers, hex palettes, 167-use sheet, first/last-frame joining,
named citation) · simaypekcan-20261122/report.md (painted first
frame) · btc-shifty-shape-store-20261115/report.md (Seedance 2.5:
pinned start frame, ≤30 refs, saved characters) · adi8xx-
tungsahur-20261124/STUDY.md (unchained drift, tolerated) ·
niceaunties-20261115/report.md (categorical continuity) ·
thecontentlab01-20261122/STUDY.md (karaoke text systems) ·
miles-mazy-china-tactics-20261118/report.md (assets/world first —
CONFIRMS; no prompt-level craft in source, said so there too).

**Our doctrine read for the comparison:**
`~/workspace/custom-skills/video-api-mastery/SKILL.md` (conditioner
law, ≤2-image doctrine, frames/refs exclusivity, separate-angles
consensus, role sentences, Kling budgets) ·
`~/workspace/custom-skills/slopcannon/SKILL.md` (CONTINUITY METHOD
§265ff, CONFORMANCE + ADHERENCE §1296ff, panel sheets §1458ff).

**Web (read 2026-11-27):**
vdobloom.com/blog/how-to-make-ai-fruit-videos ·
toonlyai.com/blog/ai-fruit-drama-video · vmake.ai/blog/ai-fruit ·
vmake.ai/blog/seedance-2-0-character-consistency ·
promptcrate.pages.dev/guides/how-to-write-veo3-prompts ·
docsearch.algolia.com (Veo 3 prompting guide mirror) ·
replicate.com/blog/using-and-prompting-veo-3 ·
vofy.art/blog/seedance-2-consistent-character-advanced-guide ·
morphic.com/resources/models/seedance-2 ·
seedance-2.app/blog/seedance-2-0-character-consistency ·
kling.ai/blog/kling-3-subject-binding-character-consistency ·
kling.ai/quickstart/klingai-element-library-3-user-guide ·
layer3labs.io/guides/make-an-ai-series-with-character-photos ·
dev.to/ref_vid (Kling reference-to-video production A/B) ·
support.google.com/flow/answer/16353334 ·
blog.google/innovation-and-ai/products/flow-video-tips ·
media.io/video-tips/veo-3-1-ingredients-to-video.html ·
aiflowmatrix.com/google-flow-frames-vs-ingredients ·
meme.com/memes/ai-cat-stories-sad-meow-meow-song (AI cat story
formula; Orange Cat Philosophy itself documents nothing).
