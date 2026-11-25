# ONLINE WRITING RESEARCH — How others write the prompts and the lines

**Authority:** user directive, Telegram msg 681 (2026-11-18 ~21:44 EST):
"bro look online at how others do it / like writing the prompts and
writing the lines, maybe online research is the way rn."

**Scope:** the open-web complement to the banked case-study mining
(`dialogue-method-rebuild-20261118/`, `case-study-writing-themes-20261118/`).
This report researches what the banked corpus does **not** contain:
how working creators and vendors actually format dialogue inside
generation prompts, what spoken-load budgets survive testing, how
micro-drama writers structure lines and episodes, and how persona /
voice consistency is practised in published workflows. Every claim
is tied to a source in `SOURCES.md`. Amendments proposed from this
research live in `AMENDMENTS_2.md`; nothing here edits the method.

**Evidence grading used below:** *practitioner-tested* = the source
describes its own test generations or a documented production run;
*official* = the model vendor's own published guide; *vendor
marketing* = a tool seller's guide whose workflow claims are
product-shaped (usable for format facts, weak for quality claims).

**The known hole, checked again:** clipcraft7 still discloses
nothing. Searches for its workflow, and for the Fruit Love Island /
frutinovela creators' line-level process, surfaced only format
explainers, press history, and tool marketing. The hole stands —
see §5.

---

## 1. ANGLE 1 — How pros write generation prompts that carry speech

### P-1. The field's rendering convention is label + colon + quoted line — and the wrapper is per-model

Every major native-audio model publishes (or is documented with) a
speaker-attribution format, and none of them is "bare line in a
script block":

- **Sora 2 (official, OpenAI):** "Dialogue must be described
  directly in your prompt. Place it in a block below your prose
  description so the model clearly distinguishes visual description
  from spoken lines," formatted as a `Dialogue:` block with lines
  like `- Detective: "You're lying. I can hear it in your
  silence."` — speaker label, colon, quoted line, in a block
  separated from the visual prose. "For multi-character scenes,
  label speakers consistently and use alternating turns."
  [OpenAI Sora 2 Prompting Guide, developers.openai.com — official]
- **Higgsfield's own short-film prompt library** writes dialogue
  the same hybrid way inside scene prompts: `Dave: "Little Kazakh
  spot on 5th. Plastic tables. Soup so hot it files a complaint."
  Adil: "Sounds nice!"` [higgsfield.ai prompt library — official]
- **Kling 3.0 (official format, via LzyPrompt's cross-model
  guide):** "a script line with a tone note in parentheses":
  `Mom (softly, in a surprised tone): Wow, I didn't expect this
  plot at all.` — label, parenthesised delivery, colon, line
  *unquoted*. [lzyprompt.com — practitioner guide]
- **Seedance 2.5 (official, BytePlus):** spoken lines in curly
  braces — `Mara says, teasing: {You remembered.}` — speaker and
  delivery first, line in `{}`. Seedance 2.0 takes double quotes
  instead. [KreatorFlow's Seedance 2.5 guide, tabulating BytePlus's
  official guide against third-party guides — vendor guide citing
  official]
- **Seedance 2.5 (Hypernatural skill doc):** "each line in its own
  `{}` right after its speaker and a short delivery, verbatim, in
  spoken order: `@Image2, in a bright, breathless voice, says:
  {Morning! Did I miss the eight-fifteen?}`."
  [hypernatural.ai — practitioner skill doc]
- **Veo 3 / 3.1 (Google guidance, via Magic Hour + Dreamdrive):**
  "Put exact speech in quotation marks. Google explicitly
  recommends quotation marks for specific dialogue," with the
  speaker named by visible description and delivery described
  separately: `She says, calmly: 'We should have left an hour
  ago.'` [magichour.ai; dreamdrive.ai — practitioner guides citing
  official]

**Read:** our colon form (F-16) is the *script's* form, and the
field agrees with it at that layer (see L-1: the genre's own tool
takes scripts as "Name: line"). At the *prompt* layer the line
additionally gets a model-specific wrapper — quotes, braces, or
Kling's bare line after a tone parenthesis — and the dialogue is
visually separated from scene prose. The wrapper is a MODEL_SYNTAX
fact, not a house style.

### P-2. Comfortable spoken-load budgets cluster BELOW our F-25 ceiling

Our caps (16–20 words per 10-s unit, one speaker) were set from our
own model's measured span behaviour. Test-based field guides
budget lower, because their clips also carry reaction and ambience:

- **Ambience AI's Seedance 2.0 guide** (built from its own test
  generations): "**About 20 spoken words per 15-second clip.** That
  is the comfortable total across all lines. **About 10 words per
  line.** … One sentence per quote." And the diagnostic: "garbled
  speech tracked line length rather than clip duration. A single
  21-word quote transcribed as clean speech for five seconds and
  then dissolved into phoneme soup for the rest of the clip."
  [ambienceai.com — practitioner-tested] (≈13 words/10 s.)
- **Dreamdrive's Veo 3 guide:** "A clip of 8 seconds … has room for
  one line of roughly six to twelve words. Two characters
  exchanging lines is possible but less reliable than one."
  [dreamdrive.ai — practitioner guide] (≈8–15 words/10 s.)
- **UseVeo's prompt guide:** "8 to 12 words fit an 8-second clip.
  Longer lines get rushed." [useveo.ai — practitioner guide]
- **QuickVeed:** "A 6 to 8 second clip holds about 12 to 18 spoken
  words"; "One short sentence per clip." [quickveed.com —
  practitioner guide] (the high end of the field range)
- **VEED's help docs** give the fit ceiling, not a comfort budget:
  "Speech runs at roughly **2.5 words per second**. If you write
  more dialogue than fits the clip, the model has no choice but to
  speed the audio up to fit, which is why generations come back
  sounding rushed or garbled." [support.veed.io — official help]
- **Oakgen's micro-drama writer** times a dialogue shot at "about
  2.5 words a second plus a beat of 1 to 2 seconds" — i.e. even at
  human conversational rate, the shot budget subtracts a reaction
  beat from the word count. [oakgen.ai — vendor guide]

**Read:** nobody credible budgets *above* our ceiling; the
test-based guides sit at roughly 60–75% of it. The disagreement is
about what the cap is *for*: ours is a fit ceiling (will the words
physically land), theirs is a comfort budget (will they land with
the reaction and the room tone still in the clip). Filed as a
flagged contradiction (X-1 / B-12), not smoothed over.

### P-3. One speaker per clip is the reliability consensus; two is the ceiling; three breaks attribution

- **Easton Dev's Veo 3 audio guide** (tested): "Single-speaker lip
  sync succeeds about 80% of the time; with multiple speakers it
  drops below 40%." Veo 3.1 improved turn-taking, but his
  recommendation stands: "letting only one person speak per
  segment, then stitch them together in post-production."
  [eastondev.com — practitioner-tested; the percentages are one
  tester's figures, not benchmarks]
- **Kling 2.6 voice-control guide:** "Kling 2.6 can handle dialogue
  between **two speakers** in a single clip. Research on the model
  points to two characters as the practical ceiling: when three or
  more people talk in one scene, voice attribution tends to get
  confused and lines may be spoken by the wrong face."
  [blog.picassoia.com — practitioner guide]
- **LzyPrompt's multi-character guide:** "Two or three named
  characters is the practical limit for a single clip. Anyone else
  becomes background … with no actions or lines of their own."
  [lzyprompt.com — practitioner guide]

**Read:** independent confirmation of Camp B and the two-designed-
speaker ceiling (F-14), from outside our own failure record.

### P-4. Tell the listener to be silent — in those words

Three independent sources prescribe an explicit listener-silence
instruction in any two-character frame, to stop the non-speaker's
mouth moving:

- LzyPrompt: "Tell the listener to be quiet. 'The man in grey
  listens silently, mouth closed' cuts down on both characters
  mouthing the same words." [lzyprompt.com]
- Tellers' voice-consistency guide, in a worked two-character
  prompt: "Leo listens without speaking." [tellers.ai]
- MagicBoat's dialogue-scene workflow publishes a reaction prompt
  verbatim: "Character A listens silently with her mouth closed.
  Her eyes tighten slightly, then she gives one restrained blink
  and a small exhale." Its speaking prompt ends "…then the mouth
  closes and the expression settles." [magicboat.net]

### P-5. Speaking is the action: one verb per character per beat

- **GPTunnel's Veo 3 guide:** "CRITICAL: if you plan to have
  speech, the character can ONLY speak (says/sings) — no other
  actions at the same time!" [gptunnel.ru — practitioner guide]
- **LzyPrompt:** "One verb per character per sentence. 'The dog
  barks. The man in the blue shirt jumps back.' Two sentences, two
  subjects." The named failure is shared action: "'the dog barks
  and the man jumps back' … you get a man who barks, or a dog that
  jumps." [lzyprompt.com]
- **MagicBoat:** "Break the exchange into shots defined by one
  visible action"; generate speaking shots and reaction shots as
  different clips. [magicboat.net]
- **OpenMicroDrama's Kling guide:** "Give dialogue one line per
  beat. … Keep speech inside the first 10 seconds of a clip, and
  end on a reaction or action." [openmicrodrama.com]

### P-6. Names and stray text inside a prompt get rendered or spoken

- **Hypernatural's Seedance 2.5 skill doc:** "Never put a person's
  name or a handle in the prompt outside `{}`: Seedance renders it
  as on-screen text." Speakers are cited by reference label
  (`@Image2`) or noun phrase; "Never a name before a line."
  [hypernatural.ai]
- **Dreamdrive's Veo guide**, troubleshooting wrong words: "Shorten
  the line and put it in quotation marks on its own sentence.
  Remove any other spoken text from the prompt, including signs or
  names." [dreamdrive.ai]
- **VEED help:** "The model treats everything in your prompt as
  content to render. Stage directions and instructions aimed at
  the AI get interpreted as part of the scene." Leave out stage
  directions; include "the exact lines you want spoken."
  [support.veed.io — official help; the vendor-side statement of
  our speaking-the-fence failure class]

### P-7. Exact-line protection is a named step

- **VEED:** prompt-enhancement/rewriting must be OFF when the
  prompt carries exact dialogue: "the rewrite can change or drop
  your lines. If your prompt contains dialogue you want spoken
  word for word, switch Enhance off." [support.veed.io]
- **Flick's documented production** (Jaime Yao's *The Herder*):
  the Kling 3.0 Pro / Seedance takes quote the line exactly, with
  the instruction "Speak exactly the quoted lines only. Do not add
  any extra words." — and the line is written "word for word, with
  its punctuation and pauses, before you make any audio, so the
  voice take and the video prompt both work from the same script."
  [flick.art — practitioner-tested production record]
- **QuickVeed:** "Avoid quotation marks inside the line, and spell
  out numbers." [quickveed.com]
- **OpenMicroDrama** (citing fal's docs): if a word comes out
  wrong, "writing English in lowercase, with capitals only for
  acronyms and names" is the suggested fix; "When a line has to be
  exact, make the shot silent and add the voice later."
  [openmicrodrama.com]

### P-8. Delivery is a short tag attached to the line — stable voice traits live elsewhere

Across models, per-line delivery is 1–5 words attached to the line
itself: Kling's `(softly, in a surprised tone):` parenthesis
[lzyprompt.com]; Veo's "says, calmly:" [dreamdrive.ai]; Seedance's
"in a bright, breathless voice, says: {…}" [hypernatural.ai].
Tellers' guide states the separation explicitly: describe "the
qualities that distinguish the speaker: pitch range, vocal
texture, accent, pace and articulation. Separate those stable
qualities from the emotion of an individual line." [tellers.ai]
The stable block is saved and reused verbatim (see C-3); the tag
varies per line.

### P-9. On Veo-class models, a pasted two-speaker script block is a documented failure mode

Easton Dev tested the obvious approach on Veo 3 — a script block
(`Man: "…" / Woman: "…"`) — and reports: "The result was
disastrous. Either only one person had sound, or both dialogues
didn't match the visuals. The correct approach: **Don't write
dialogue scripts, write scene flow**" — prose describing the
argument and the two performances, letting the model decide who
speaks when — or one speaker per segment, stitched. [eastondev.com
— practitioner-tested] OpenAI's Sora 2 guide publishes the
opposite artefact (the Dialogue block, P-1) for its own model.
**Read:** dialogue syntax in the vehicle is an empirical per-model
property. Any house habit of pasting the script's block form into
every model's prompt is contradicted for Veo-class models and
confirmed for Sora-class models — which is what MODEL_SYNTAX
exists to record (filed as B-9).

### P-10. Talking clips have a sync-drift ceiling around 8–10 seconds

- **Hook Studio's fruit-drama recipe** (a disclosed, priced
  production recipe): "A talking clip uses its own voice, in one
  step, and stays at 8 seconds or less because the voice drifts
  out of sync after that." [hookstudio.ai — vendor recipe with
  real costs]
- **OpenMicroDrama on Kling 3.0:** "Several creators say lip sync
  drifts after about 10 seconds, even though the model can make
  15." [openmicrodrama.com]
- **Easton Dev on Veo 3:** "Keep dialogue short, one line, under
  8 seconds … Veo 3's sync capability for long dialogue isn't
  stable enough." [eastondev.com]

**Read:** our 10-s unit container sits at the top of the field's
drift range. This does not by itself indict the container (our
span law was measured on our model), but any unit whose speech
runs to the container's edge is spending its last seconds in the
drift zone on every model the field has tested.

---

## 2. ANGLE 2 — How writers write lines for AI short drama and soaps

### L-1. The genre's own factory tool publishes its script format: "Name: line", one line per scene, bracketed acting tags

Clippie — a talking-fruit factory tool — publishes a full
production guide (Nov 2026) describing exactly how scripts enter
its pipeline:

- "paste a script in 'Name: line' form. **Each line becomes one
  scene.**" Worked specimens are the same starter exchange our
  banked study transcribed: `Strawberry: You told me you were at
  the farmers' market.` / `Banana: I was. With Cherry.`
- "Add [annoyed], [whispers] or [gasps] where a line needs
  acting"; the tags "**are performed, not read out**". Scene
  setting lives in a separate field: "Use **scene instructions**
  (up to 2,000 characters) to set locations."
- Characters are referenced with **@** in the script "so they stay
  consistent across scenes"; each character is assigned a voice
  and a style (Dramatic, Warm, Energetic, Eerie) before lines are
  animated; the review step is "Read and listen, fix anything,
  then turn each scene into a talking clip."
- Pacing: the writer drafts "about 30 seconds, 1 minute or 2
  minutes (**6, 11 or 20 lines**)" — ≈5.5 seconds per line,
  reaction included; a story can run to 40 scenes.
- Series planning, verbatim: "Plan an AI fruit drama like a TV
  writers' room: pick a small cast, **write a one-page character
  bible**, choose **two or three recurring conflicts**, and fix an
  episode length."

[clippie.ai product page + "How to Make AI Fruit Videos in 2026"
guide — vendor marketing for the tool, but the format facts are
the product's actual input contract; the strongest line-level
disclosure the genre has published]

**Read:** the colon form is not our invention or our error — it is
the genre's literal script format at its biggest disclosed tool.
What Clippie adds that our method lacks: the bracketed per-line
acting tag as part of the script's surface (performed, not read),
and @-binding of characters inside the script itself.

### L-2. Micro-drama beat discipline: one complication, one reversal, cliffhanger on a face

- **Oakgen's script guide** (vendor, citing measured speaking
  rates): a 60–90-s episode needs five beats — "a hook in the
  first 3 seconds, a short setup, one escalation, a turn, and a
  cliffhanger in the last few seconds"; the escalation carries
  "**One complication, not three**"; the cliffhanger ends "on a
  face or an object, not on a resolved line"; on episode 2 onward
  the setup "is where you pay off the last cliffhanger"; "write
  the season arc before episode 1." [oakgen.ai]
- **InVideo's AI micro-drama craft piece:** "Between the cold open
  and the cliffhanger, a 60-second episode has room for exactly
  **one reversal** — one moment where the situation flips"; the
  cold open must be "a face reacting, a shock line of dialogue, or
  a reveal already in motion. Never an establishing shot."
  [invideo.io — vendor craft guide]
- **Drama.so's hook formula:** the cliffhanger is "a *new*
  question, not the answer to the old one," and it must be
  load-bearing: "If the cliffhanger could be swapped onto another
  episode without rewriting the middle, it is decoration. Write a
  new last five seconds." Its model want-line is a demand under
  time pressure: "'I need this contract tonight' is a want. 'She
  had a difficult childhood' is a pamphlet." [drama.so — vendor
  craft guide]

**Read:** the swap test is a checkable form of our hanger law —
filed as B-11. The one-reversal cap sharpens our five-beat sheet
(escalation = one complication) without changing it.

### L-3. Draft double, cut half

OpenMicroDrama's script guide, citing working vertical-drama
writers: "Gigi M. Green's rule of thumb is **no more than 10 lines
an episode. Write 20, then cut 10**." And on construction order:
"Gigi M. Green suggests **writing the cliffhanger first, then
working backward**." The same guide states the AI-specific script
rule: "If you're making the footage with AI, your script is also
your production plan. So only describe things a video model can
actually show." [openmicrodrama.com — practitioner craft guide]

**Read:** our banter-first pass drafts loose, but nothing in the
method sets an expected cut ratio; the field's rule makes the
harvest a halving, not a selection. Filed as B-8.

### L-4. Human-rate word budgets do NOT transfer to generated speech

Oakgen budgets "about **90 to 130 words of dialogue per 60
seconds**," built from measured conversational English (152–170
wpm, Yuan/Liberman/Cieri 2006). That is a budget for *human
actors* in live-action micro-drama. Every AI-native source in §1
budgets generated speech lower (P-2), because the model must also
render the reaction, the room, and the drift margin. Rooms citing
micro-drama word budgets for AI episodes would over-load units by
~1.5×. Recorded here so the number is never imported naked.

### L-5. On the TTS route, the scene is performed as ONE take — line-by-line generation is the named cause of robotic dialogue

Paintbrush's dialogue-writing guide (the tool performs scripts
with ElevenLabs Eleven v4 "Text to Dialogue"):

- Script form: "short lines. Give every line a named speaker and
  open it with **one delivery tag in brackets**, like [whispers]
  or [dry, quietly pleased]. … One to five words that describe how
  the voice sounds." Sound-effect tags are banned ("The video
  model supplies ambience").
- "Put what the audience watches without speech into **silent
  beats**. … A look, a pause, a hand on a shoulder."
- "Why perform the whole scene as one take? Most text-to-speech
  tools read one line at a time. Each line sounds fine alone, but
  **nobody is listening to anybody**. Every reply lands with the
  same gap, and a shout gets a calm answer. … Every voice hears
  the others." Their answer to "why does my AI dialogue sound
  robotic?": "Usually because each line was generated alone.
  Perform the whole scene as one take, give each line a specific
  tag, and add pauses."
- Line rules: "A line you cannot say in one breath makes a long
  shot"; "**One idea per line.** If a line makes a point and then
  changes the subject, make it two lines."

[paintbrush.gg — vendor guide describing its own production
pipeline; the one-take claim is its product's premise, but the
diagnosis (per-line generation kills reaction) is stated as craft,
and it matches our D-6 no-contact diagnosis from the audio side]

### L-6. Naturalness is briefed as intention + the withheld line, never requested as a quality

Debutify's natural-dialogue study (worked MiniMax H3 examples):

- "The root cause is **information without intention**. A model
  produces words that fit, but nothing underneath them wants
  anything. Real dialogue has a goal in every line: to persuade,
  to deflect, to comfort, to win. Without that subtext, every
  sentence lands with the same weight, and same weight is what
  reads as fake."
- The prompt fix: "describe the situation, **what each character
  wants, and what they are avoiding saying**" — "you get
  naturalness by describing intent and constraint, not by asking
  for naturalness."
- Its reusable prompt structure has five parts: "The setting and
  its pressure. Who each character is in one phrase each. What
  each one wants from the exchange. The length each line may
  take. And [the ending state]."

[debutify.com — practitioner-oriented craft article] **Read:** our
vehicles already carry objective/obstacle/tactics (ratified E3
law); the field's addition is the *withheld* line — what the
character is avoiding saying — as a named brief element. Filed as
B-7.

### L-7. What the original factories actually disclose: process, not lines

- **Fruit Love Island** (@ai.cinema021): press reporting (NYT via
  Film and Pen) records the creator's own account: "hours went
  into each video, involving **scriptwriting, scene planning, and
  constant redoing to correct AI generation errors**." No script,
  prompt, or line specimen from the account has been published.
  [filmandpen.com, citing NYT/Yahoo reporting — press]
- **Frutinovelas / @frutystory** (William Rico): Hook Studio's
  sourced explainer documents the format's history and the
  creator's stated origin (a parody of *La Isla de las
  Tentaciones*), episode lengths of 30 s–3 min across press
  sources, and a cliffhanger per part — but no writing workflow.
  [hookstudio.ai — vendor explainer with press citations]
- **Hook Studio's own disclosed recipe** for a fruit-drama
  episode: still first ("a still first, a clip only from a still
  you like"), one 5-second line per character, three characters =
  3 stills + 3 talking clips ≈ $4/episode; talking clips ≤8 s
  (P-10). [hookstudio.ai]
- **Wireflow's fully disclosed run** (every prompt and cost
  published): "One prompt and one line per fruit, two lip-synced
  clips and a captioned cut"; the pipeline is "Make a front-facing
  fruit image, **turn the line into speech, then give both to a
  lip-sync model**" — voice lines under 3 seconds each (ElevenLabs
  v4), lip-sync via Kling AI Avatar. [wireflow.ai — vendor,
  practitioner-tested run with costs]

**Read:** the disclosed factory-style pipelines converge on the
shape our banked studies found — still first, one line per clip,
fixed voice per character — and the voice-first variant (TTS →
lip-sync) is at least as common in disclosed runs as native audio.

### L-8. The spoken-surface rules converge with our plainness pass

Script-humanizing practice (for human-voiced scripts, but the
surface rules are identical): shorten to one breath, contractions
by default, swap formal words for spoken ones, read aloud and mark
where you stumble. [freehumanizerai.com — practitioner guide]
FanFun's creator guide adds the TTS-specific surface: punctuation
and phrasing steer cadence; phonetic respelling is the fix when a
word "sounds unnatural in your generation"; a character's baked-in
persona tone bounds what punctuation can fix. [blog.fanfun.ai —
vendor creator guide] Neither source repairs *toward* formality —
independent confirmation of Pass 3.5's direction.

---

## 3. ANGLE 3 — Character & voice consistency as actually published

### C-1. On routes without a persistent identity, the identity block is pasted verbatim — paraphrase is the named failure

- **LayerProof's character-consistency guide:** "Split every
  prompt into two parts. The identity part never changes. The
  scene part changes for each clip. … **Do not paraphrase the
  identity block. 'Curly dark hair' and 'dark curly hair' can
  produce different results.** Keep the wording identical, even
  when it feels repetitive." Its one-page character bible carries
  a Voice row: "Accent, pitch, pace, energy." [layerproof.app —
  practitioner guide]
- **Easton Dev (Veo):** "use the same character description every
  time. Like 'a woman in a red coat with short black hair'—this
  description must be identical in every prompt, or the AI will
  generate different characters **with different voices**."
  [eastondev.com] — the description carries the voice, not only
  the face.
- **OpenMicroDrama (Kling):** "Keep each character's description
  exactly the same in every prompt of an episode, word for word."
  [openmicrodrama.com]

### C-2. On routes WITH a persistent identity, the rule inverts: stop redescribing the face

- **Media.io's Soul ID workflow guide:** "**Do not repeatedly
  redescribe the face after selecting a trained identity.** Use
  the prompt for scene variables and stable production details."
  Its scene formula: "[selected Soul ID] + [wardrobe] + [action]
  + [location] + [camera and composition] + [lighting] +
  [continuity constraints]", plus "Keep a character bible
  containing wardrobe names, colors, props, age, hair, makeup and
  forbidden changes." [media.io — practitioner guide]
- **Higgsfield's pipeline guide:** Soul ID is "training a
  persistent face from reference photos once and carrying it
  across every model on the platform" (20+ photos); the shot
  prompt then works from the storyboard frame + parameters, not a
  face description. Its character step publishes a verbatim
  turnaround-sheet prompt (four full-body views + three portrait
  close-ups, "Maintain perfect identity consistency across every
  panel"). [higgsfield.ai — official]
- **Kling Elements (OpenMicroDrama):** "make each lead an Element
  from one clean front-facing image plus two or three more angles
  … Bind a voice from a clean 5–30 second recording."
  [openmicrodrama.com]
- **AutoFlow's character system:** a character is "saved once — a
  portrait, a name and a voice — and attached to the clip itself,
  so the face comes from the portrait and the voice from the
  character"; prompts then just name the character.
  [auto-flow.studio — vendor guide]
- **Sora 2 (official):** uploaded characters are referenced by ID
  (up to two per generation) — identity by reference, not by
  description. [developers.openai.com]

**Read:** C-1 and C-2 are both field law, on different routes.
Our reference law (verbatim look blocks, REFERENCE PRIORITY) is
written for the C-1 route and does not currently distinguish the
C-2 case. Filed as a flagged contradiction (X-4 / B-13).

### C-3. The voice-consistency toolkit, in the field's portability order

Tellers' guide lays out the options as a ladder:

1. **A named voice reference file per character** — "a clean clip
   with one speaker and name it after the character:
   `Maya_voice_reference.wav`"; the model generates a new
   performance guided by the sample. (Seedance 2.5 supports audio
   references; Gemini Omni Flash adds voice references.)
2. **A supported voice ID / registered voice** — Kling's voice
   library and user-created voices; Elements bind a voice from a
   5–30-s recording (C-2).
3. **A precise voice description reused verbatim** — "the most
   portable approach": pitch range, vocal texture, accent, pace,
   articulation, with stable qualities separated from per-line
   emotion (P-8). "Save that character block and reuse it
   verbatim."

[tellers.ai — practitioner guide, capabilities checked 2026-10-21]

### C-4. Show the voice, don't describe it: specimen lines on the card

Persona-authoring craft (from the character-chat world, where the
card *is* the production document) converges on example dialogue
over adjectives:

- **Estuary's Persona Authoring Cookbook:** "**Show the voice,
  don't describe it.** Adjective lists produce generic characters.
  Concrete speech patterns and example phrases produce distinctive
  ones." Its field discipline: `personality` = *how* they speak
  and behave; `background` = *what* they know — "Keeping them
  separate produces noticeably more consistent characters."
  [docs.estuary-ai.com — official platform docs]
- **Lunelle's character-writing guide:** a definition needs "A
  voice: how they talk, **shown in two or three sample lines**";
  "describe what the character does instead of listing
  adjectives"; "Put the most important lines first, because apps
  tend to give the top of a definition the most weight."
  [lunelle.ai — practitioner guide]
- **LayerProof:** "Write scripts in the character's style. Reuse
  their typical greeting, phrases, and sign-off." [layerproof.app]

**Read:** our SPEECH_RULE is a rule *statement* ("speaks in
questions when hurt"). The persona craft adds 2–3 *specimen lines*
in the character's voice on the same card — the grain the banter
is checked against. Filed as B-5.

### C-5. The character bible / reference sheet is the universal first artefact

Every published pipeline starts there: LayerProof's one-page bible
(name/role, look, voice, behavior) written "before you generate a
single image" [layerproof.app]; Clippie's one-page bible + 2–3
recurring conflicts (L-1); Higgsfield's turnaround reference sheet
+ Soul ID training before "a single shot" [higgsfield.ai];
OpenMicroDrama's "Build your cast before you shoot"
[openmicrodrama.com]; MagicBoat's master frame from which all
coverage is derived [magicboat.net]. This confirms our cast-card /
combined-anchor practice and adds one artefact we don't produce:
the *turnaround sheet* (multi-view single generation) as the
canonical look source, per Higgsfield's published prompt.

---

## 4. ANGLE 4 — Contradictions and tensions with our current method

**X-1. ⚠ CONTRADICTS (application of F-25).** Test-based comfort
budgets sit at ~60–75% of our spoken-load ceiling (P-2): Ambience's
Seedance tests (~20 words/15 s, garbling tracking *line* length),
Dreamdrive's Veo budget (6–12 words/8 s), Hook Studio's ≤8-s
talking clip (P-10). Fit-ceiling sources (VEED, Oakgen, ~2.5 wps)
support our arithmetic as a *maximum*. The contradiction is real
but narrow: it argues the ceiling should be *budgeted against*
when a unit also carries a REACTION beat or a second voice — not
that the arithmetic is wrong. → B-12, flagged for parent ruling,
in the A-13 pattern.

**X-2. ⚠ CONTRADICTS (one vehicle habit).** A pasted two-speaker
script block fails on Veo 3 in practitioner testing (P-9) while
being OpenAI's published form for Sora 2. Any single house syntax
for dialogue-in-prompt is therefore wrong somewhere; the fix is
evidence inside MODEL_SYNTAX, not a new house form. → B-9.

**X-3. ⚠ TENSION (Camp B vs one-take performance).** Camp B
generates one speaker per *video clip*. Paintbrush's production
evidence says one-speaker-per-*audio take* is precisely what makes
exchanges robotic (L-5): on the voice-first route, the scene's
audio should be performed whole and cut, while the video stays
Camp B. The two rules operate on different layers and can both
hold — but our VOICE_ROUTE declaration doesn't currently state
performance granularity, so a room could satisfy Camp B on both
layers and ship dead exchanges. → B-6.

**X-4. ⚠ CONTRADICTS (unqualified verbatim-redescription).** On
trained-identity routes, pasting the full face block is the named
mistake (C-2); on plain routes, *not* pasting it verbatim is the
named mistake (C-1). Our reference law states the C-1 rule without
the C-2 exception. → B-13, flagged for parent ruling.

**Checked and NOT contradicted:** the want-announcement ban (the
closest field specimen, drama.so's "I need this contract tonight,"
is a demand spoken to the counterparty under time pressure — a
move, not a declaration; no source endorses "I want X" filings);
the Stranger Test (no field source operates a stronger
plausibility gate; the field's QA is captions-vs-script, per the
banked clone census); fact spend, proof objects, payload-last,
colon form at the script layer (L-1 confirms it as the genre's own
input format).

---

## 5. Gaps and dead ends (stated, never filled)

- **clipcraft7:** no workflow, script, prompt, or line specimen
  found anywhere online this pass. The banked hole is total.
- **The original factories' writing process:** Fruit Love Island
  and @frutystory are documented only at press level
  (scriptwriting + scene planning + redo loops; format history).
  No line-level evidence exists in the open record found here.
- **Practitioner forums:** searches aimed at Reddit/Discord
  surfaced guide sites and vendor docs, not forum threads;
  Discord is login-gated and out of scope under the task rules.
  The practitioner voice in this report comes from tested guides
  and documented production runs instead.
- **Vendor marketing weight:** Clippie, oVideo, Oakgen, Hook
  Studio, InVideo and Paintbrush all sell the workflow they
  describe. Their *format* facts (input contracts, syntax) are
  reliable; their *quality* claims were used only where a second,
  independent source converges.
- **Single-tester numbers:** eastondev's ~80% / <40% lip-sync
  success rates and Ambience's word budgets are one test bench
  each. They are cited as practitioner evidence, not benchmarks,
  and B-12 is flagged rather than asserted for exactly this
  reason.
- **Not researched (out of the brief's scope):** caption/title
  grammar online (wave 1's A-11/A-12 covered the banked record);
  non-English frutinovela line craft beyond format facts (the
  Spanish-language sources found were press explainers, not
  writing guides).

*End of report.*
