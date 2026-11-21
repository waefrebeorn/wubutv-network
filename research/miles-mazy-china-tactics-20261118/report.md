# CHINA TACTICS — lilypad study: 哲导 (Director Zhe) via @miles_mazy

**User order:** Telegram msg 688, 2026-11-18 22:21 EST — "more sauce
from CHINA / this one is TACTICS AND BIG CHINA", with the link
https://x.com/miles_mazy/status/2122939676780548494

**What the link actually is:** Miles Ma's tweet is an *amplification*,
not the source. His caption (Chinese): "卧槽，这篇绝对价值4位数 —
现在哲导免费开源出来，赶紧收藏学起来" ("Damn, this piece is
absolutely worth four figures — Director Zhe has now open-sourced
it for free; hurry, bookmark it and learn"). It quote-posts
@Formulasearch, whose tweet is a bare link to an X long-form
article. The article's author signs himself 阿哲Phil — and
@Formulasearch's own display name *is* 阿哲Phil. **The sharer and
the author are the same person**: 哲导 ("Director Zhe") posted his
own article; Miles Ma (42.5K followers) carried it to the user's
timeline.

**The article:** 《独立制作AI商业广告片全流程分享①：如何从编导思维开始？》
— "Making AI Commercial Films Solo: The Full Process, Part 1 — How
to Start from a Writer-Director Mindset" (X article
2122612968370094081, carried by @Formulasearch tweet
2122893489885397274, 2026-11-18 03:23 UTC; 80,664 views, 1,059
bookmarks, 551 likes on the carrier tweet; Miles's amplification:
62,794 views, 992 bookmarks, 843 likes — a bookmark-to-like ratio
above 1 on both, the save-to-learn signature). Full Chinese text
secured on disk as `source_article_zh.txt` in this directory;
tweet JSONs alongside for provenance.

**Series status:** this is part ①, the *mindset* stage. The author
promises later parts on the practice stage (character/scene
assets, image generation, AI-video shot joins, real UI + code
animation, music/sound). Parts ②+ were **not findable** through
the permitted routes in reasonable effort: FxTwitter has no
profile-timeline route (404 on both profile paths tried), and the
author's site rzcthink.top ("Phil / Formula") returns garbled
text extraction with no article listing exposed. **Leads for
②+:** the author's X account @Formulasearch, his site
rzcthink.top, and the Feishu (飞书) document linked inside the
article. Recorded, not stalled on.

---

## A. Translation — the article's full substance, section by section

### Preface (untitled)

The author opens by refusing the genre he is publishing into: this
article offers no "one-click generation" skill and no
essay-style prompt packs, and he cannot teach anyone to make
high-quality video quickly — behind it sits a necessary process of
large time and money spent practising and trial-and-erroring. He
states outright disgust for the timeline's low-quality,
case-free, clickbait-stacked articles. Creation is continuous work
that cannot be rushed; no method gets you there in one step. As AI
gets more convenient, "using your brain" (动脑子) matters more:
before touching tools, first cultivate your own abilities as a
screenwriter and director. His full-process toolkit: ideation in
Claude (Opus), video generation via Seedance / GPT Image /
Midjourney, music and sound via ElevenLabs / Minimax / Suno,
motion design in Remotion, editing in 剪映 (CapCut). This part
covers only the thinking stage; cases are presented mostly as
拉片 (frame-strip analysis) images, with the films themselves on
his website / Feishu doc. The article's six questions: (1) division
of labour — where is effort best spent on a solo commercial? (2)
understanding the product — does the audience know you, what
should the film say first? (3) choosing the film type; (4) the
script — what does each type fix *before* writing? (5) building a
system — how do one product's several films cooperate? (6) review —
how do you know the finished film said it clearly? He advises
reading it yourself rather than tossing it to your AI.

### §一 — How to divide labour with AI (怎么与AI分工)

AI's execution power is strong: mechanical, technical work can all
be handed to it; creativity stays with your own brain. Spend your
own energy on exactly these things: make sure you have personally
used the product and truly understand the product and the brand;
conceive the creative; orchestrate the workflow; judge quality and
call for revisions; and actively go find cases and materials to
feed the AI — only then can you steer it to work faster and better.

### §二 — Before the script: understand the brand and the product

Before writing, establish how much the audience already knows
about the product. If they don't know it yet, the film must first
explain clearly what it is and what it does; if they already know
it well, spend the energy on brand story and attitude. New brands
are mostly the first case; big brands mostly the second. Worked
example — Knockin', an AI networking assistant ("like an AI
customer-service rep of your own: it answers visitors' messages for
you and filters out the opportunities that genuinely need you
personally"; tagline "Get Discovered. Never Miss an Opportunity").
Knockin' is unknown, so the film must first explain what it is,
then introduce features. Red Bull, Volvo, Apple need no
explanation, so their films can go straight to brand narrative and
concept — what he calls "raising the brand's B格" (its prestige
altitude): Red Bull's 2012 Stratos jump never introduces the drink
at all; it tells the extreme spirit the brand has always run on.

**The five questions to answer before scripting** (this step can
be delegated to AI: have it use the product, read the site and
docs, organise features and audiences, and sweep the brand fonts,
colours and UI components into a material library). For Knockin':
1. **What is the product, what can it do?** — It generates an AI
   business card from your experience and work that answers
   visitors' questions for you: answers only from your own
   materials, hands decisions back to you, can book meetings
   directly. Site line: "Your bio can finally answer back."
2. **Who needs it most, in what situation?** — Freelancers and
   consultants who take client work. A prospect enquires while
   you're away; the opportunity can be missed. Site line:
   "Present, even when you aren't."
3. **What does the audience know, lack, and fear?** — They know
   replying promptly matters, but have never seen this kind of
   product, and they fear the AI will say the wrong thing on their
   behalf. Positioning: "Not a chatbot. A trusted stand-in."
4. **Where does it publish, and what should the viewer do after
   watching?** — English-language social media; afterwards, go to
   knockin.info and build their own AI card.
(The fifth question is the core-value question developed in §四.1:
what should the audience remember — see the core-message formula
there.)

### §三 — Choose the film type (选择片子类型)

Commercial films come in several common types; the article
develops the three most representative: the **long product PR
film** (长篇产品PR片), the **scene short** (场景短片), and **Motion
animation** (Motion动画). Type is chosen before scripting, and
each type has its own script logic (§四).

### §四.1 — Product PR film: fix the core first, then the concept

**Core information** = the product value the audience should
remember after watching, written in the form **"who, in what
situation, because of it gains what"** (谁，在什么情况下，因为它得
到什么). **Creative concept** = the device that delivers the core
information — a worldview, a metaphor, or a storyline — with every
feature placed inside it. Knockin''s demo film: core = *[the user]
[while living their real-world life], [the assistant handles the
daily work affairs online for them]*; concept = **personify the
"assistant"**.

Software products are invisible and untouchable; shoot the
interface and recite features and the audience feels nothing. But
"assistant" is a word that already carries an image, so film it as
a character. Everyone knows what an assistant does — watch it
receive guests and book meetings for its master and no explanation
is needed. Once the concept and image are fixed, the product's
operations translate into interactions between characters: a
visitor asking a question = someone calling at the door, the
assistant receives them; a decision that's the owner's to make =
the assistant goes back and asks the master; searching someone's
card = your assistant goes out to find the person. The virtual
world then forms its own worldview and can keep generating stories
from it — nearly all of Knockin''s shorts use this thinking, as do
its IP character design and its live-action character conception.
**The creative concept should grow out of a concept the product
already carries, not be bolted on from outside.**

For agent/assistant products, turning an abstract program into a
visible figure is common across the industry — an embodiment menu:
- **A character:** xAI's Grok Bot launch film made each bot a small
  round ball with two eyes that blinks and hops; Meta's Muse and
  OpenAI's Dots also give their agents cartoon figures; the ancient
  example is Office's paperclip assistant (Clippy).
- **A cursor:** for computer-operating agents, the demo often shows
  only a cursor moving and clicking by itself — when OpenAI's Dots
  takes over the computer, the frame holds only its cursor at
  work, and the audience knows the agent is working because the
  cursor moves.
- **An ambient signal:** Apple Intelligence's Siri is no longer a
  small orb at the screen's bottom but a ring of light along the
  screen's edge — when the light comes on, the user knows Siri, or
  the whole phone, has been woken.

### §四.2 — Scene short: one short films one selling point

An ad short is only tens of seconds — enough to make exactly one
feature clear. Inside those seconds it must do three things,
following classic AIDA (Attention → Interest → Desire → Action):

**1. Grab attention — the first 3 seconds decide whether the
viewer swipes away.** Four hook types, each with his own Knockin'
short as the case:
- **Curiosity (猎奇):** an unusual image that makes you want to
  know what happens next. *《试试看》* ("Try It and See") opens with
  Mia picking up her own AI card — "Can I really trust it?" — she
  decides to test it: sunglasses on, posing as a client, she sends
  "Half price. Do as I say." The frame freezes: how will the AI
  reply?
- **Pain point (痛点):** directly stage a trouble the audience
  knows. *《只需要出面》* ("You Only Need to Show Up") opens with a
  man scheduling a meeting — "See you at 2?" "Sorry, back to 2?"
  "Then 4?" — the time bounces back and forth until he collapses
  into his chair. Everyone has lived the scheduling shuffle.
- **Contrast (反差):** first show what an ordinary person (or a bad
  product) does, then show it done with the product. First a "dumb
  AI" agrees to everything — "No problem, half price" — then cut
  to Knockin''s assistant showing professional boundary-keeping.
  *《信任的助手》* ("The Trusted Assistant") uses this contrast set.
- **Result first (结果先行):** give the result, then rewind to how
  it happened. *《面试替身》* ("The Interview Stand-In") opens with
  the hero getting a call: "Alex, can you start work Monday?" He
  freezes: "But I never interviewed." The caller: "You did
  interview — sort of." Then rewind: the hiring side had scanned
  his card, and the one interviewed was his Knockin'.

**2. Make it understood — selling points are almost all
adjectives, and adjectives can't be filmed.** Convert them into
visible action, change, or comparison:
- **Extreme demonstration (极限演示):** put the product under the
  most extreme conditions. In *《试试看》*, Mia tests her AI in four
  outfits — a haggling client, a reporter fishing for quotes, a fan
  pressing questions, a gossiping mother. Four times it doesn't
  answer recklessly; what must go back to the owner goes back.
  Final score: 4/4.
- **Comparison (对比):** shoot the same scene twice — one version
  agrees to everything, one holds the boundary. *《信任的助手》* is
  exactly this pair.
- **Designed contrast (反差):** *《看看我的》* ("Look at Mine") is
  about assistant customisation — a refined, gentle person paired
  with a screaming parrot.
- **Metaphor (隐喻):** one image replaces the concept.
  *《名片的厚度》* ("The Thickness of a Business Card") is about
  "the card is too thin": a paper card of three lines thickens
  layer by layer until it becomes a phone — implying that a
  person's whole context can be concentrated in their AI card.

**3. Leave the impression:** the ending makes the viewer remember
the product and the selling point, and act (buy? register?).

### §四.3 — Motion (code) animation: low-cost creation

Use animation software or code to animate interface, text and
graphics — also called Motion or MG animation. It relies on
neither filming nor generation; every frame is drawn by code, so
reusability and accuracy are guaranteed. **Advantages:** *Accurate*
— reuse the product's real front-end UI components directly,
eliminating AI video/image blur and deformation. *Easy to change*
— product revision or feature update: swap the component and
re-render, no re-shooting and no re-rolling generations (重抽卡);
landscape, vertical, English versions come out in batches by
changing parameters. *Clear* — operating steps, data flows, how
the back end works: processes that can't be filmed can be drawn as
diagrams and explained step by step. *Controllable* — how long
each frame stays and when it appears can be matched precisely to
narration and music. **The short board:** Motion animation is not
good at emotion and scene expression; when you want the audience
to feel something, hand it to AI video or live action.

**Recipes by video type:** *Functional demo* — in real operating
order: problem → solution → how to use → result → call to action.
*Talking-head B-roll* — wherever the narration goes, the picture
follows with diagrams, data and interface. *Explainer animation* —
draw principles, processes and data as diagrams, step by step.
*With AI image generation* — generate characters, scenes and
illustrations with AI first, then use code for layout and motion
effects into a stylised film. *With AI video* — AI performs the
people, code animation explains the interface: in the AI shot a
person picks up a phone, next shot cuts to a code-made interface
close-up; or overlay interface cards, annotations and subtitles
onto the AI picture; title cards, end cards (落版) and logos are
also made in code, guaranteeing every film's brand fonts and
colours match. *With real material* — real screenshots, screen
recordings or live footage as the base, code overlays interface,
annotations, subtitles and transitions.

### §五 — Build assets and a system (构建资产和体系)

One film released burns hot and cools fast, but a product must
stay warm: every feature update should ship a post or a film. But
products iterate too fast to spend days conceiving each one. So
**design the assets and the worldview first**: fixed setting,
characters and art style, directly reusable afterwards; similar
scripts already used can be lightly adjusted and re-shot. The
payoffs: *Audience impression* — the same actors/characters/key
elements recur, and next time the audience instantly knows who it
is. *Accumulating impression* — each film continues the previous
one, and brand impression builds bit by bit. *Faster production*
— for a new feature, just extend the existing materials and
worldview; no conceiving from zero. Longevity cases: Duolingo's
owl Duo plus a fixed group of friends — the same cast in the app,
the ads and the socials; Headspace's orange smiling face, used
from the app to brand publicity; GEICO's gecko, the US insurer's
mascot, first appeared 1999 and still headlines its ads;
Michelin's tyre man, born over a century ago, among the oldest
brand figures still in use in the world.

### §六 — The review (检验)

After the film is done, and during production, keep asking:
*Content* — Can you say in one sentence what this film is about?
Do the first three seconds grab attention? With sound and
subtitles off, can the audience still understand it? Is there
causality between shots — do they connect front to back?
*Product and brand* — Is the product interface accurate? Are the
characters, fonts and colours consistent with the brand language?
*Ending and release* — After watching, can the viewer think of
what to do next? Is the cover attractive enough?

**Next-part preview:** the practice stage — character & scene
assets, image generation, joining AI-video shots, real interface
and code animation, music and sound. Sign-off: "I'm 阿哲Phil,
focused on AI content creation and sharing; co-founding an
AI-native content growth studio; open to commissions."

---

## B. Tactics — the reusable moves, numbered

Each tactic is stated as a rule a room can run, tied to its
article section. (Numbered Z- for Zhe, to avoid colliding with
the TASTE guide's T- rules.)

- **Z-1. Delegate the mechanical, keep the creative.** AI takes
  execution; the human keeps creativity and judgment. (Preface/§一)
- **Z-2. The director's five jobs.** Personally use/know the
  product; conceive the creative; orchestrate the workflow; judge
  quality and direct revisions; actively hunt cases and materials
  to feed the AI. (§一)
- **Z-3. Craft before tools; no one-click exists.** Train
  screenwriting/directing ability before tool skill; quality is
  bought with time-and-money trial and error. (Preface)
- **Z-4. The audience-awareness gate.** Before scripting, declare
  what the audience already knows: unknown → explain what it is
  first; known → skip explanation, spend on story and attitude
  (raise the B格). (§二)
- **Z-5. The five pre-script questions.** What is it/does; who
  needs it, in what situation; what does the audience know, lack,
  fear; where does it publish and what should the viewer do after;
  what is the one value they should remember. (§二, §四.1)
- **Z-6. Outsource the research leg to AI — and bank a brand
  material library.** AI uses the product, reads site/docs,
  organises features/audiences, and sweeps brand fonts, colours
  and UI components into a reusable material library. (§二)
- **Z-7. Type before script.** Choose the film type first (long PR
  film / scene short / Motion animation); each type has its own
  pre-writing fix-list. (§三)
- **Z-8. Core message in the who/when/gain form.** The remembered
  value is written "who, in what situation, because of it gains
  what" — before any concept work. (§四.1)
- **Z-9. Grow the concept from the product's own concept.** Never
  bolt an external concept on; the product's built-in word
  ("assistant") is the seed. (§四.1)
- **Z-10. Personify, then translate operations into interactions.**
  Make the abstraction a character; map every system operation to
  a social interaction (visit → guest received; escalation → ask
  the master; search → go find the person). The world then
  generates stories by itself and powers the whole series. (§四.1)
- **Z-11. The embodiment menu for invisible systems.** Character /
  cursor / ambient signal — three sanctioned ways to make an
  invisible agent visible. (§四.1)
- **Z-12. One short, one selling point, AIDA spine.** Tens of
  seconds carry exactly one feature through attention → interest
  → desire → action; the ending names the next step. (§四.2)
- **Z-13. First 3 seconds + the four-hook taxonomy.** CURIOSITY /
  PAIN POINT / CONTRAST / RESULT-FIRST — every opening is one of
  the four, and the first 3 seconds decide the swipe. (§四.2.1)
- **Z-14. Adjectives can't be filmed — four conversion devices.**
  EXTREME DEMO (stress-test, scored: 4/4) / COMPARISON (same scene
  shot twice, two behaviours) / DESIGNED CONTRAST (persona
  mismatch) / METAPHOR (one image replaces the concept). (§四.2.2)
- **Z-15. Code animation for whatever must be exact.** Real UI
  components (no AI deformation), re-render on change, batch
  variants by parameter, diagram the un-filmable, frame-exact
  timing. Weak at emotion — hand feeling to AI video/live action.
  (§四.3)
- **Z-16. The hybrid recipe list.** Demo in operating order;
  B-roll that follows narration; explainer step-by-step; AI stills
  + code layout; AI acts people / code shows interface (or code
  cards over AI footage); real base + code overlays; title cards,
  end cards and logos always in code for brand consistency.
  (§四.3.2)
- **Z-17. Assets and world first, then the treadmill.** Fixed
  setting/characters/style designed once and reused; similar
  scripts micro-adjusted and re-shot; payoff = instant
  recognition, accumulating impression, faster production. (§五)
- **Z-18. Mascot longevity is the asset proof.** Duolingo's cast,
  Headspace's orange face, GEICO's gecko (1999– ), the Michelin
  Man (100+ years) — fixed figures compound. (§五)
- **Z-19. The nine-question review, run during and after.** One
  sentence? First 3 seconds? Muted *and* subtitle-less still
  legible? Shot-to-shot causality? Interface accurate? Characters/
  fonts/colours on-brand? Next step thinkable? Cover attractive?
  (§六)

---

## C. Mapping against WuBuTV doctrine

Doctrine sources cited: TASTE = `new-era/research/TASTE_GUIDE_2026-11-17.md`;
DM = `research_notes/dialogue-method-rebuild-20261118/DIALOGUE_METHOD.md`.

| Tactic | Verdict | Ground |
|---|---|---|
| Z-1 division of labour | **CONFIRMS** | Our whole architecture is this split: parent/showrunner holds judgment, coordinators execute. His one-human version is the same shape at smaller scale. |
| Z-2 director's five jobs | **CONFIRMS** | "Judge quality, direct revisions" = the gate stack's job; "hunt cases/materials to feed the AI" is literally the lilypad program this study belongs to. His "personally use the product" maps to knowing the show's bible/world first-hand before scripting. |
| Z-3 craft before tools | **CONFIRMS** | TASTE §1 T-2 ("If the generating came first and the thinking came after, it's slop"); the TASTE guide itself exists because tool fluency outran craft. |
| Z-4 audience-awareness gate | **ADDS** | Our cold gates (Gate E; DM §3 Stranger Test) test whether a *script* reads cold. Nothing declares, before scripting, what a cold viewer already knows walking into this part of a serial. The RUNNING_BRIEF (DM Pass 3.4) tracks who-knows-what *inside* the fiction, not the audience's knowledge state. New field, not a new philosophy. |
| Z-5 five questions | **ADDS** | Q1–Q3 sharpen premise work (cf. TASTE §1 T-1/T-30), but Q4 — where it publishes and what the viewer should *do* after — has no home in our briefs. Our captions close with the wordmark; no per-piece intended action is declared anywhere in the release system. |
| Z-6 AI research leg + brand library | **CONFIRMS + ADDS** | Research waves and the vault confirm the research leg. The add: his fonts/colours/UI sweep is a *standing brand-asset library per product*; ours exists only in fragments (wordmark law, the HyperFrames lane). |
| Z-7 type before script | **CONFIRMS + ADDS** | Our slate already runs types (episode / MV / bumper) with type-specific law. The add is his explicit selection step — which type carries *this* message — which we perform implicitly at intake, never as a declared choice with the rejected types named. |
| Z-8 core in who/when/gain form | **CONFIRMS** | A fill-in sharpening of TASTE §1 T-1 (one idea, sayable in one sentence) and T-30 (one want, one obstacle, one turn). His formula is better form design for the same law. |
| Z-9 concept from the product's own concept | **CONFIRMS** | TASTE §1 T-5 (specificity from our own world; the first idea is everyone's first idea; banned defaults) — the same law reached from the ad side. |
| Z-10 personify + operations-as-interactions | **ADDS** | We have no named worldbuilding step that translates a system's operations into social interactions between characters. This is a story-generation engine: define the mapping once and episodes suggest themselves. Directly applicable to our system-driven shows (the count office, the broadcast race) and to the occupation lore — an invader's "operations" in the home world are already interactions; naming the mapping makes them writable on purpose. |
| Z-11 embodiment menu | **ADDS** | THE ALGO (TASTE §6) is our central invisible system and has no sanctioned visual embodiment — L-4 forbids explaining it, so it is currently shown only by its effects. A CURSOR/signal treatment is a *showing* device fully compatible with L-4: the system's hand, never its face, never a lecture. |
| Z-12 one point + AIDA | **CONFIRMS + ADDS** | One-idea-per-piece is TASTE §1 T-1; our 10-second bumpers are the only format that has ever performed for us, and they are ad-format. The add is AIDA's tail: his shorts must land Desire → Action (the viewer knows the next step); our bumpers end on the brand beat with no declared next step. |
| Z-13 four hooks / first 3 s | **CONFIRMS + ADDS** | The FIRST-3 BLAM gate already measures opening impact (onset, dead-head, motion) — but it measures *that* the opening hits, not *which move* it makes. His taxonomy names the move. RESULT-FIRST in particular is a structure (cold-open the outcome, rewind) our U1 design does not currently choose among. |
| Z-14 adjective conversion devices | **CONFIRMS + ADDS** | Confirms DM Pass 3.1's proof-object law (conflict shown on an object, never reported) and acting-as-objective (TASTE §8). Adds two named scene constructions we don't carry: the EXTREME DEMO (a claim stress-tested on screen, with a score) and COMPARISON (the same scene shot twice with two behaviours) — the second is a natural staging for home-vs-invader in the occupation lore. |
| Z-15 code animation for exactness | **CONFIRMS** | Our HyperFrames ruling was ADOPT-PARTIAL on exactly his boundary: code-rendered graphics lane yes, footage renderer no; his "weak at emotion, hand feeling to AI video" is the same line drawn from the other side. |
| Z-16 hybrid recipes | **CONFIRMS + ADDS** | Method C / HyperFrames practice confirms the hybrids. The add: code-made end cards as a *system* — we run a corner bug; he runs full title/end cards in code so every piece's brand surface is identical by construction. |
| Z-17 assets/world first | **CONFIRMS** | Bibles, cast cards, RUNNING_BRIEF, reference stacks, quote-chained serialization and the FULL STORY vault (TASTE §8) are this tactic already institutionalised. His §五 is our §8 stated from the ad side, including the re-shoot-with-micro-adjustments clause our outtakes/alternate-takes practice mirrors. |
| Z-18 mascot longevity | **CONFIRMS** | Evidence for the fixed-cast strategy (UNC and the recurring home cast) — the compounding-recognition argument is why a stable cast outranks novelty casting in our rooms. |
| Z-19 nine-question review | **CONFIRMS + ADDS** | One-sentence = T-1; muted watch = TASTE §5 K-4 (his version is stricter — subtitles off too); shot causality = K-2 joint audit; cover = THE EMPTY CAPTION poster-frame test banked from clipcraft7. The adds: interface/product accuracy (for us: the count board, the wall, the props must be *right*, a QC question our gates ask only via proof objects) and the next-step question (counted under Z-5). Writer≠judge (K-5) is the one review principle he lacks — see tensions. |

**Verdict tally (19 tactics):** CONFIRMS 8 (Z-1, Z-2, Z-3, Z-8,
Z-9, Z-15, Z-17, Z-18) · CONFIRMS+ADDS 7 (Z-6, Z-7, Z-12, Z-13,
Z-14, Z-16, Z-19) · ADDS 4 (Z-4, Z-5, Z-10, Z-11) ·
**CONTRADICTS 0.**

**Two tensions, recorded honestly (not contradictions of any
single rule):**
1. **Where judgment lives.** His system concentrates quality
   judgment in one human director who knows the product first-hand
   (§一, Z-2). Ours deliberately distributes and *separates* it —
   writer ≠ judge (TASTE §5 K-5), cold readers, gates the room
   cannot self-administer — because our "director" is an agent
   network whose self-judgment has demonstrably failed before.
   His model presumes a person; ours presumes fallible agents.
   Nothing to adopt or reject — but any future "just let the maker
   judge it" proposal argues against K-5, not against Zhe.
2. **Brand-first vs fiction-first scope.** His order of work grows
   the world out of the *product's* concept (Z-9/Z-10). That maps
   cleanly onto the MV show, bumpers and promos — the station's
   ad-surfaces — and only partially onto the fiction shows, whose
   worlds grow from lore (TASTE §6) under a shown-never-explained
   law. The personification engine (Z-10) still transfers; the
   brand-first *order* does not, and shouldn't be imported whole.

---

## D. Liftables — concrete changes, with landing spots

1. **AUDIENCE-KNOWLEDGE declaration (from Z-4/Z-5).** Add a field
   to the E3 brief template's storyline declarations, beside
   `AUDIENCE_SECRET`: *a cold viewer walking into this part knows
   X / has never seen Y / fears or expects Z* — written before
   dialogue, checked at Gate E. Lands in:
   `new-era/E3_PRODUCTION_BRIEF_TEMPLATE.md` §2 + template §6 grep
   contract.
2. **Intended-action line (from Z-5 Q4 / Z-12).** Every brief and
   every delivery declares the viewer's next step (watch Part
   N+1, vote in the comments, count along, follow the vault). Lands
   in the template's delivery section and the release caption
   rules (A-12 CAPTION_RULE gains a next-step slot).
3. **The personification pass (from Z-10/Z-11).** When a show's
   engine is an invisible system, its bible names the embodiment
   (CHARACTER / CURSOR / AMBIENT SIGNAL) and writes the
   operations→interactions mapping once, as a story generator.
   First candidates: THE ALGO as CURSOR-class presence (effects
   only, L-4-safe); ON AIR's broadcast system. Lands in the show
   bibles (`new-era/morph/MORPH_SHOW-*.md`) at their next storyline
   pass.
4. **Hook-type declaration for U1 (from Z-13).** U1's BLAM beat
   declares its hook — CURIOSITY / PAIN / CONTRAST / RESULT-FIRST —
   in the brief, and the GATE_LOG records which was fired. Lands
   in template §4 (U1 block) beside the existing BLAM fields.
5. **Two named scene devices (from Z-14).** EXTREME DEMO and
   COMPARISON enter the scene-construction vocabulary beside the
   proof object: a claim may be stress-tested on screen with a
   visible score, and a scene may be shot twice with two
   behaviours where the contrast *is* the argument. Lands in the
   writers-room method + DM Pass 3.1's neighbourhood as drafting
   devices (not gates).
6. **Zhe questions merged into the master checklist (from Z-19).**
   Gate (f)/delivery checklist gains two named questions: *is the
   world's working surface accurate?* (boards, counts, props —
   the interface-accuracy question) and *is the next step
   legible?* The muted test is tightened to his form: sound off
   **and** subtitles off. Lands in template §5.4 beside Gate (f).
7. **A standing brand-asset library (from Z-6/Z-16).** One
   harvested folder per show — fonts, colours, wordmark, code
   end-card — built once and reused by construction, extending
   the HyperFrames lane from bumpers to episode end cards. Lands
   in `wubutv-network` tooling/docs at the next production pass.
8. **Series watch (from the article's own preview).** When parts
   ②+ of Zhe's series appear (practice stage: assets, image gen,
   shot joins, UI + code animation, music/sound), they get the
   same study treatment — part ① contains no prompt-level tactics
   at all, and the practice parts are where his Seedance workflow
   will either confirm or challenge our vehicle law.

---

## E. Form ideas (lilypad pattern)

- **THE CURSOR** — an invisible system shown only as its cursor or
  signal moving through the world: a light that travels the docket
  wall, a highlight that picks who speaks next. THE ALGO's hand,
  never its face — occupation you can see happening, fully inside
  L-4's shown-never-explained law.
- **THE STAND-IN** — a character whose job is being someone else:
  answers for them, takes their meetings, holds their line — and
  the drama is what it refuses to answer. (Knockin''s assistant,
  reworked into our world: the night clerk's stand-in, the count
  office's second who only ever says "that's his to decide.")
- **THE STRESS TEST** — an episode built as an extreme demo: the
  world's rule pushed to its hardest case in escalating tries,
  with the score kept on screen (the count office handed something
  uncountable; the bell rung mid-sentence four times). The 4/4 is
  the plot.
- **FOUR TRIES** — one claim tested four ways by one sceptic in
  four disguises (Mia's structure, generalised): each try is a
  unit, the tally is the hanger.

---

## F. Gaps — what the article does NOT disclose (stated, never filled)

- **No prompt-level craft at all.** Part ① contains zero prompts,
  zero generation parameters, zero per-shot workflow. His Seedance
  practice is entirely in the unpublished/unfound later parts.
- **No numbers.** No view counts, conversion data, budgets, or
  timelines for the Knockin' films; the tactics are argued from
  craft reasoning, not performance evidence. Miles's "worth four
  figures" is an endorsement, not a measurement.
- **The films themselves were not reviewed.** Cases are presented
  as 拉片 frame-strips inside the article; the playable films live
  on his website / Feishu doc, which the permitted routes could
  not extract (site crawl returned garbled text).
- **No dialogue craft.** His formats are narration/demo-driven ad
  forms; nothing here speaks to two-character spoken scenes — the
  territory our dialogue method governs. The mapping above never
  pretends otherwise.
- **Client-case bias.** The worked example is one product
  (Knockin') from his own practice, plus brand-name cases (Red
  Bull, Duolingo, GEICO) cited at headline level only.
- **Miles Ma himself is a thin node so far.** The evidence shows
  an amplifier with a save-worthy radar (bookmark ratios >1 on
  both tweets), not a practitioner of this material; his own
  field is enterprise AI/FDE. One data point, treated as one.

---

## G. People notes

- **哲导 / 阿哲Phil (@Formulasearch)** — the author. Display name
  阿哲Phil; bio "AI Builder & Visual Designer — Creating
  AI-generated videos & motion graphics"; 12,538 followers;
  joined 2025-11-30; site rzcthink.top ("Phil / Formula");
  co-founding an "AI Native 内容增长工作室" (AI-native content
  growth studio) per the article's sign-off. 哲导 is his directing
  persona ("Director Zhe"). The article is a *give-away of paid-tier
  craft*: his framing is openly anti-guru — no one-click skills, no
  prompt packs, contempt for case-free clickbait — which is itself
  the credibility signal Miles was amplifying.
- **Miles Ma (@miles_mazy)** — the amplifier and the user's actual
  send. See the people file `~/memory/people/miles-mazy.md`.
- **@Formulasearch gets no separate people file** — he *is* the
  author above; one node, two names, recorded here to keep the
  chain of custody straight.

*Study compiled 2026-11-18. Sources: source_article_zh.txt +
tweet JSONs in this directory (FxTwitter captures, 2026-11-18);
doctrine cites to TASTE_GUIDE_2026-11-17.md and
DIALOGUE_METHOD.md as read on disk the same day.*
