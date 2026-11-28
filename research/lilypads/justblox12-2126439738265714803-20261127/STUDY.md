# STUDY — @justblox12's "If you whistle it's comes back to you"

User order (Telegram msg 1291, 2026-11-28): study this post. Third
study of this account in one day — the immortal-snail post
(2126144561282224351) lives in the sibling folder
`justblox12-20261127/BACKLOG_STUDY_2026-11-27.md`, and the rust post
(2126333003949596699, "In this world if you touch water you rust")
was studied hours earlier in `justblox12-20261127/STUDY.md` (SOURCES
#146). This study is the whistle post only, read in full locally,
and its §C is written against the rust study: what is the same
grammar, and what is genuinely new.

Artefact: @justblox12 ("Just Blox", bio "Entertainment | Story
Teller", **1,434 followers at fetch** — 1,333 at the rust study's
fetch ~5 hours earlier; the account is compounding on these posts),
tweet text **"If you whistle it's comes back to you"** [sic —
the caption's grammar is the creator's own] (#Storytelling #roblox
#animation), posted **2026-11-27 22:15:15 UTC** — about seven hours
after the rust post. Metrics at study fetch (2026-11-28 ~02:53 UTC,
FxTwitter API): **63,716 views / 817 likes / 175 bookmarks /
34 reposts / 2 replies / 0 quotes** — ~44× the account's follower
count inside its first ~4.6 hours. Video: `video.mp4` in this
directory — md5 `35e8206d6eb65275bd04e12d39b60702`, 720×1280
vertical, 30 fps, 127.43 s, AAC 44.1 kHz.

Evidence labels used throughout: **PUBLISHED** (the post's own text
/metadata), **MEASURED** (frames, cuts, ASR from the downloaded
file), **INFERRED** (reconstruction from the artefact).

---

## A. RETRIEVAL HONESTY BOX

**Retrieved:**
- The full tweet object via the FxTwitter API
  (`api.fxtwitter.com/status/2126439738265714803`): text, author
  block, metrics, all video variants.
- The video itself, downloaded in full from the direct twimg MP4
  URL and read as: a 51-frame grid (1 frame / 2.5 s, `frames/f_*`,
  viewed as contact sheets), a scene-change count at threshold 0.4,
  and full-res frames at 20.5 / 83.0 / 95.5 / 126.5 s (`frames/key_*`).
- The audio, transcribed with the house dual-checkpoint ASR — with
  one documented deviation: **Checkpoint A (large-v3) was attempted
  three times (full file, then two halves) and was OOM-killed every
  time** under VM memory contention from concurrent production work
  (other agents' ASR jobs held ~2 GB each throughout the window).
  The transcript of record is therefore **Checkpoint B
  (distil-large-v3), run in its own process** (`asr_b.json`, merged
  into `asr.json`), **cross-validated against the creator's own
  burned-in word captions**, which are visible in every grid frame
  and matched the transcript at every sampled point (including the
  in-frame sign "SMALL ENOUGH TO CARRY" and the marker name "KOBI"
  on the shoe at 83.0 s). On this account's rust post the two
  checkpoints agreed near-verbatim, so a single-checkpoint read
  carries low wording risk; the two ASR garbles that remain are
  flagged in §E.

**Not retrieved:**
- Replies under the tweet (2) — not read; nothing about audience
  response is claimed beyond the public counts.
- No prompt text, tool disclosure or making-of exists for this
  video, and none is claimed. The artefact is Roblox-engine
  machinima (blocky in-engine avatars, in-engine camera), **not**
  AI generation — there is no prompt layer to reconstruct; §C
  studies the *writing and staging* layer, which is where this
  factory's craft lives.

---

## B. THE VIDEO READ

### B.1 What it is

A 127-second **first-person** narrated story animation in a Roblox
world built on **one law: anything with your name written on it
comes back to you when you whistle.** The narrator is the hero this
time — an older brother (his name, Kobi, is never spoken; it is
read off the things he has labeled, §B.4) whose criticised habit of
labeling everything he owns becomes the only tool that can save
his little sister Evie when she ends up hanging from a bolt
20 feet down a quarry wall. Where the rust post *priced* its law
(a two-rung cost ladder), this post *specifies* its law — three
written rules, stated in full by 18 seconds — and the entire third
act is the hero auditing those three rules, one by one, against
facts the story planted in the first two acts.

### B.2 Beat map (MEASURED — ASR segment times, Checkpoint B;
scene changes at threshold 0.4: 87 over 127.43 s ≈ one cut per
1.5 s, cuts landing on narration clauses)

| # | Time | Beat | The move |
|---|------|------|----------|
| 1 | 0.0–11.6 | **THE LAW, stated, demonstrated, spent** | Sentence 1 states the law; sentence 2 demonstrates it ("You write your name on a pencil, whistle, and it flies into your hand"); then the world re-spent in two strokes: "So lost property doesn't exist. Neither does stealing lunch." Proof by anecdote: last week a sandwich flew straight out of the headteacher's mouth back to a kid in year three. |
| 2 | 11.6–18.1 | **THE RULEBOOK** | "There are rules." All three, in plain words: (1) "Your name has to be on the actual thing. Not the box, not the wrapper." (2) "It has to be small enough for you to carry." (3) "And you have to write it yourself." The whole climax is already written here — the audience just doesn't know it yet. |
| 3 | 18.2–27.8 | **EVIE + THE TOLERANCE CLAUSE** | Little sister Evie is five; she can write three letters: "E, V, E. Her name wasn't E. But apparently, the magic didn't care about spelling." (Frame: the teddy's collar tag reads EVE.) Every night her teddy flies down the hallway when she whistles — "Usually into my face." The law's one stated exception is announced the first time the edge case appears, not invented at a payoff. |
| 4 | 27.8–37.6 | **THE FLAW + THE AMPLIFIER** | "Me? I labeled everything. Shoes, football, school bag." Mum called him lazy for whistling for the remote instead of getting up — "She was right." (The hero agrees with his own indictment.) For his birthday, Grandpa gives him a **red whistle**: "This one'll reach anything you own, he said." A range upgrade, planted with its spec spoken aloud. |
| 5 | 37.6–45.6 | **THE COST + THE CONFISCATION** | He tests the whistle outside: his school bag smashes through the kitchen window. The law's power is demonstrated destructively on his own property — and Mum keeps the whistle in a drawer. Amplifier: shown → confiscated. (The town's quarry and its lookout platform are introduced in the same breath.) |
| 6 | 45.6–52.1 | **THE PICNIC SETUP** | Sunday: the family picnics at the quarry lookout platform. Evie brings her teddy; he brings his football; and "because Mum finally trusted me again, I brought the whistle." Amplifier: re-earned. Every object that will matter is carried on screen by its owner. |
| 7 | 52.1–67.6 | **THE ACCIDENT** | He kicks the ball too hard; it hits a railing; the railing falls; the platform corner drops. Mum grabs Evie's sleeve — the sleeve tears. Evie slides under the broken rail. Her teddy falls all the way to the bottom. Evie doesn't: her backpack catches on a thick metal bolt in the quarry wall. "There she was. Hanging 20 feet below us." |
| 8 | 67.6–73.6 | **THE ADULTS FAIL + THE COUNTDOWN STARTS** | Dad lies flat and reaches down — too far. Mum calls the fire brigade (help is coming, but on its own clock). And the fabric around Evie's backpack straps starts ripping. The deadline is now a material state, not a number (§B.4). |
| 9 | 73.6–81.7 | **THE FAILED RESCUE** | He blows the whistle: his football shoots out of the bushes into his hands — the tool works, live, in front of everyone. Dad shouts for the obvious rescue: whistle her bag up. Evie tries — "Only air came out. She was crying too hard." And it would have failed anyway: "her name wasn't on it anyway. It was new." The obvious rescue is killed on **two independent grounds**, one per rule. |
| 10 | 81.8–95.8 | **THE AUDIT** | He sees her shoe: black marker along the white rubber — **KOBI** (verified in frame, key_83.0). He wrote his own name on her shoe that morning, during an argument about whose shoes could jump farther, "so I could whistle it back after throwing it." Mum made him stop, but the name stayed. Rule 1: name on the actual thing ✓. Rule 3: written by the whistler himself ✓. The strap rips another inch. Rule 2, remembered under pressure: "Small enough for you to carry" — "I carried Evie upstairs every time she fell asleep on the sofa." ✓. The climax is a checklist being ticked while fabric tears. |
| 11 | 95.8–114.0 | **THE RESCUE** | Instructions as dialogue-inside-narration: "Hold your foot! … Both hands. Don't let your shoe come off." Dad reaches over the edge. He blows. "The shoe jerked upward. Then her whole body." The backpack tears loose — "For one horrible second, she swung upside down over the quarry." Dad catches her coat; Mum grabs her arms; they drag her over the edge — "One shoe first." |
| 12 | 114.2–122.9 | **THE VICTIM USES THE LAW** | Nobody speaks. Evie looks down at the quarry: "My teddy." They wait until she stops shaking. Mum holds her on her lap. **And Evie whistled.** "A very dirty bear came flying up over the rail." (Final grid frames: the teddy alone on the wet quarry floor, then back in her world.) The rescued performs the mechanic herself, on her own loss, at her own scale. |
| 13 | 123.0–127.1 | **THE POLICY ENDING** | "That night, Mum handed me a marker and everybody's shoes. 'Inside the sole, she said. Small letters.'" The mother who confiscated the whistle and called him lazy now institutionalises his flaw as household safety policy. Narration ends at 127.1 s, 0.3 s before the file does. |

### B.3 How the law is PRINTED and RE-SPENT (MEASURED)

The rust post printed its law four ways (stated / shown / priced /
cured). This post prints its law as a **specification**: stated
(sentence 1), demonstrated (the pencil, sentence 2), world-spent
(no lost property, no lunch theft, the headteacher's sandwich),
then **bounded** — the three rules at 11.6–18.1 s are the law's
terms and conditions, and every later beat is either a rule being
exercised (Evie's misspelled tag, the labeled football, the drawer
confiscation) or a rule being *tested* (the new bag fails rule 1;
the shoe passes all three). The law is re-spent at least nine
times: pencil, sandwich, teddy-nightly (×implied), remote, bag
through the window, football at the quarry, the failed bag, the
shoe, the teddy again — and the final re-spend is administrative:
every shoe in the house gets labeled that night, so the premise
ends the episode as a *household system*, not just an event.

### B.4 The ledger mechanics (MEASURED)

- **The ledger is handwriting on objects.** Plot state in this
  world is literally written down — in marker, on the actual
  thing. KOBI on the blue school bag (grid frame ~30 s), KOBI on
  the white rubber of Evie's pink shoe (key frame 83.0 s, the
  single most important image in the piece: the rescue exists
  because of what is written on a shoe). Any frame containing a
  labeled object tells you what can move and who can move it.
- **The narrator's name is never spoken.** "Kobi" is read, not
  heard — the ASR transcript contains no instance of it; the
  audience learns the hero's name the way the magic does, by
  reading it off his property. (INFERRED as deliberate: the one
  name the law cares about is presented in the law's own medium.)
- **The countdown is a tearing material.** The backpack straps
  rip in stages — "started ripping" (73 s), "ripped another inch"
  (94 s), "tore loose" (107 s) — a damage state that worsens on
  schedule and is visible/audible in every rescue beat. It is the
  rust post's sound-graded rust (squeak → creak → freeze) rebuilt
  as a timer: not how much damage has happened, but how much
  *time is left*, carried on a body-adjacent object.
- **The exception's proof is a failure.** Evie's failed whistle
  (only air) plus the new bag (no name) prove the rules are real
  at the exact moment the audience most wants them bent. The law
  is never suspended for the hero's family — the rescue works
  *inside* the rules or not at all.
- **Scale is the law's unit of account.** Rule 2 prices everything
  in carry-weight: a pencil, a teddy, a football, a school bag —
  and one five-year-old, pre-certified as carryable by a domestic
  fact ("every time she fell asleep on the sofa"). The price
  ladder of the rust post (drop → bucket) is here a *weight
  ladder*, and the top rung is a person whose weight the story
  has already receipted.

### B.5 Audio, captions, dialogue (MEASURED)

- **One narrator voice, first person, wall-to-wall:** ASR segments
  run 0.0–127.1 s with no silent stretch; **594 words in 127 s
  ≈ 280 words/min**, 84 segments, mean segment ~2.4 s. Slightly
  denser than the rust post (541 words / 121 s ≈ 268 wpm) — the
  audit beat (81.8–95.8 s) is delivered as rapid short clauses,
  the narration's tempo doing the time pressure.
- **The narrator is a character.** Against the rust post's
  third-person voice, this narrator is the hero, in past tense,
  and he testifies against himself: "Mum called me lazy… She was
  right." The flaw is confessed by its owner before it is used.
- **Reported speech inside the narration:** Grandpa's spec ("This
  one'll reach anything you own"), Dad's shout at the failed
  rescue, the hero's own shouted instructions ("Hold your foot!…
  Don't let your shoe come off"), Evie's "My teddy.", and Mum's
  closing instruction ("Inside the sole… Small letters."). All
  carried by the single voice; there is no separately voiced
  dialogue track. The two lines that carry the ending — "My
  teddy." and "Small letters." — are the shortest in the piece.
- **Captions:** one word (occasionally a short phrase) at a time,
  bold white with black outline, bottom-centre, tracking the
  narration word-for-word — the account's standing caption
  discipline, unchanged.
- **Language:** the same aggressively ESL-simple register as the
  rust post — short single-clause sentences, concrete nouns, and
  a rulebook stated in words a five-year-old character could
  repeat. The most complex sentence in the piece is the rescue's
  conditional ("I could bring the shoe back. Could it bring Evie
  with it?") — and it is posed as a question the next ten seconds
  answer.
- **Joints:** audited segment by segment, the chain is therefore/
  but throughout — law → rules (therefore), rules → Evie's
  tolerance (but — an exception, announced), flaw → amplifier
  (therefore), amplifier → confiscation (but), trust re-earned →
  picnic (therefore), accident → adults fail (therefore), whistle
  works → bag fails (but), bag fails → the shoe (therefore — the
  audit), audit passes → rescue (therefore), rescue → Evie's own
  whistle → the policy (therefore). No and-then joints found.

### B.6 Model/production tells (MEASURED/INFERRED)

Roblox-engine machinima, same factory floor as the rust post:
blocky avatars with swapped face decals, flat-colour sets (street,
classroom, kitchen, hallway, bedroom, the quarry — the one
"location" set, built once and used for the whole third act),
camera staged per narration clause, 87 scene changes ≈ 1 per
1.5 s (rust: ~85 ≈ 1 per 1.4 s — the cutting tempo is a factory
constant). The production spends its precision where the story
lives: the handwritten names are legible at thumbnail size in
every frame they appear (marker texture on the shoe's rubber is
the climax's key prop and it reads), while the quarry is three
grey textures and a wooden platform. The teddy's flight is a
simple translate-with-light-streak (grid frame ~27 s) — the magic
has one cheap, consistent visual signature, reused for pencil,
sandwich, teddy, bag, football, shoe and girl, so the audience
learns the effect once and reads it instantly at the climax.

---

## C. CRAFT FINDINGS

1. **The law ships with its own rulebook, and the climax is an
   audit of it.** Three rules, all stated by 18 s, none of them
   decorative: the climax is the hero checking them one by one
   (name on the thing ✓ — but not hers, *his*; written by the
   whistler ✓ — that morning, for a petty reason; small enough
   to carry ✓ — receipted by the sofa fact) while the strap
   rips. Suspense here is not "will the magic work?" but "does
   the situation satisfy the spec?" — a question the audience can
   work on alongside the hero, because they were given the same
   rulebook. This is the rust post's price ladder generalised:
   the rust law was *priced* (two rungs); the whistle law is
   *specified* (three conditions). (MEASURED)
2. **The hero's criticised flaw is the rescue mechanism.** The
   labeling habit is introduced as a vice — Mum calls him lazy,
   he agrees ("She was right") — demonstrated as a nuisance
   (whistling for the remote), extended by a petty sibling
   argument (labeling *her* shoe so he could win a throwing
   game), and that exact petty act is the only reason a valid
   name exists on anything Evie is wearing. The story never gives
   the hero a new virtue; it re-prices the vice he already had.
   (MEASURED)
3. **The failed rescue runs first, and each failure names a
   rule.** The obvious save (whistle the bag) is attempted on
   screen and eliminated twice — she can't whistle (crying →
   only air) and the bag is new (no name → rule 1). By the time
   the shoe is spotted, the audience has re-learned the rulebook
   at maximum attention, and the working rescue feels earned
   rather than convenient. Failure is used as exposition.
   (MEASURED)
4. **The tolerance clause is stated when planted, not when
   spent.** "The magic didn't care about spelling" arrives at
   22 s, attached to a joke (the teddy in his face), a full 100 s
   before any rule-edge matters. When the climax later depends on
   rule-lawyering (whose name, whose handwriting), the audience
   already knows the law reads intent — so the audit reads as
   fair play, not as the author bending rules under pressure.
   (MEASURED)
5. **The amplifier prop runs a three-state trust arc.** Grandpa's
   red whistle: introduced with a spoken spec ("reach anything
   you own") → demonstrated destructively (bag through the
   kitchen window) → confiscated by the authority (the drawer) →
   re-earned ("because Mum finally trusted me again") → spent at
   the climax. The tool's availability is a relationship meter:
   each state change is a family verdict on the hero. (MEASURED)
6. **The ending is a repair, not a door — the account's second
   ending shape.** The rust post ended on a door (a new want,
   nothing resolved). This one closes every loop it opened: the
   teddy — lost in the accident, the one debt left — is recovered
   by *Evie herself*, whistling it up on her own (the victim
   performs the mechanic at her own scale, proving recovery and
   returning her agency in one beat); and the confiscating mother
   ends the episode by adopting the hero's flaw as policy
   ("Inside the sole. Small letters."). The law's final re-spend
   is administrative and loving. The factory therefore has (at
   least) two closers: open a door when the premise has somewhere
   to go; run a repair when the premise has something to heal.
   (MEASURED)
7. **First-person confession is a credibility device.** Because
   the narrator has already convicted himself ("She was right"),
   the audience trusts his audit at the climax — a narrator who
   reports his own failures is believed when he reports the rules
   are satisfied. The rust post's third-person voice had
   authority; this voice has *honesty*, and the story spends it
   at the audit. (MEASURED/INFERRED)
8. **Honest formula note:** the grammar underneath is identical
   to the rust post's — one-law world, single-voice narration,
   word captions, proof-by-experiment, the law re-spent through
   ordinary life, a body/object ledger, therefore/but joints, the
   same cutting tempo and caption discipline, posted the same
   day. What is new relative to the rust post: **the rulebook**
   (specification instead of a price ladder), **the flaw as the
   tool**, **the failed-rescue-first construction**, **the
   tolerance clause**, **the amplifier's trust arc**, **the
   first-person narrator-hero**, and **the repair ending**. Seven
   new mechanisms on one reused chassis, inside seven hours — the
   factory is not repeating a video, it is iterating a grammar.

---

## D. TRANSPLANTS — stated as rules, named targets

1. **STATE THE RULEBOOK IN UNIT 1; MAKE THE CLIMAX AN AUDIT OF
   IT** → slate-wide script rule for any law with conditions.
   State every condition of the episode's law in plain words in
   the first unit; plant exactly one fact per condition in the
   middle units; build the climax as the hero checking the
   conditions one by one while a visible countdown runs. SHE
   TOOK MY FACE: Madame Ora's law already carries conditions —
   E2's climax should be Nino auditing them (whose face, whose
   hand stamped it, what it cost) rather than receiving an
   explanation. NO TALKING AT THE TABLE: the cost ladder is
   already a two-rule book (almost-sound = an inch; full sound =
   the chair) — plant one fact per rule in units 2–4 so the
   final chair removal is an audit the audience can run ahead of
   the hosts.
2. **THE FLAW IS THE TOOL** → character rule, slate-wide. Give
   the hero one habit another character criticises in unit 1 —
   and have the hero *agree* with the criticism on the record.
   Plant the habit twice more (once as nuisance, once as petty
   self-interest). The climax must be solvable only by that
   habit; the hero gains no new virtue. MY LANDLORD IS A BABY
   already holds this shape in embryo: Elias's kept-back coin
   under the bath (E1's aside) is his flaw — a dishonesty toward
   the baby — and his only leverage; E2 should pay it off as the
   *tool* of the climax, not merely as a secret the baby finds.
   ONE MILLION PETALS: Lila's haggling is her criticised flaw;
   an E2 climax should be winnable only by haggling, not by
   honesty arriving on schedule.
3. **RUN THE FAILED RESCUE FIRST; LET EACH FAILURE NAME A
   RULE** → climax construction rule. Before the working save,
   attempt the obvious save on screen and kill it on stated
   grounds — one failure per rule the audience needs to
   re-learn. Never let the first plan work, and never let it
   fail for a reason the rulebook didn't publish. THE BIG JAR:
   the first attempt to settle the count should fail on the
   jar's own stated rule (a marked thing re-used doesn't count —
   the tile), teaching the rule at maximum attention before the
   cheat is priced in unit 4.
4. **ANNOUNCE THE TOLERANCE WHEN YOU PLANT THE EDGE CASE** →
   law-drafting rule. If a law's condition has an exception
   (spelling doesn't matter; a gift doesn't count as payment; a
   borrowed name works), state the exception in one line the
   first time the edge case appears — attached to a joke or a
   small beat — never at the payoff. An exception announced at
   planting is world-building; the same exception announced at
   the climax is a cheat. Applies to every slate law with
   conditions, and to the cannon's hook mechanics.
5. **THE VICTIM PERFORMS THE MECHANIC LAST** → endings rule.
   After any rescue, hand the episode's law back to the rescued
   character for one small, voluntary, safe use before the
   episode ends (Evie whistles her own teddy up). It proves
   recovery, returns agency, and re-prices the law from terror
   back to tool in a single beat. Audit every slate E1/E2 ending
   against it: LANDLORD — after the bed is paid, the baby should
   perform one small voluntary act with the night-light economy
   (he gives, unprompted, the one thing he was never asked for);
   NO TALKING — the saved diner should choose the episode's one
   permitted sound's *echo* himself (a deliberate, smiling knock
   on the table that costs nothing) rather than merely surviving
   in silence.
6. **THE COUNTDOWN IS A MATERIAL, NOT A CLOCK** → set/prop rule.
   When an episode needs a deadline, put it in a degrading
   object whose state is readable in every frame and worsens on
   a stated schedule: ripping straps here; rust's squeak →
   creak → freeze there. BIG JAR's painted line and PETALS'
   repainted board are static ledgers — where an episode needs
   *time pressure* rather than score, add one tearing/burning/
   melting prop whose damage the audience can grade at a glance
   (LANDLORD E2 candidate: the rent-book page the promise is
   written on, tearing a little further each time the baby
   refuses it — pairs with the promise-as-payment transplant
   banked from the Boss_Bee_ study).
7. **THE AMPLIFIER RUNS A TRUST ARC** → prop rule, slate and
   cannon. A hero tool with a spoken spec should change hands
   and states across the episode — shown → misused →
   confiscated → re-earned → spent — so its availability meters
   a relationship, not just a plot need. In the cannon: a hero
   prop/effect can carry the same three-state arc across a
   video's sections (introduced in the first verse with its
   "spec" visible, banned/broken at the bridge, returned for the
   final chorus) — the FIRST-3 BLAM promises the effect; the
   trust arc prices its return.
8. **CANNON (MV) — FIRST-PERSON CONFESSION AS A HOOK VOICE.**
   This account proves the one-law grammar carries a full rescue
   plot in first person, and that the narrator's early
   self-indictment ("She was right") is what makes the late
   rule-audit believable. For MV story-slots and show narration
   alike: when the teller is the hero, have him convict himself
   of the episode's flaw inside the first unit — the confession
   is cheap (one line) and it pre-pays the audience's trust for
   every later claim the narration makes.

---

## E. HONEST SCOPE

- **Transcript provenance:** Checkpoint B (distil-large-v3) is the
  transcript of record; Checkpoint A (large-v3) was attempted
  three times and OOM-killed each time under concurrent VM load
  (§A). Cross-validation is against the creator's burned-in word
  captions in the frame grid, which matched at every sampled
  point. Two Checkpoint B garbles are read contextually and
  flagged here: Dad's shout at 76.0–77.7 s ("Usel for your bag!")
  is read as **"Useless for your bag!"** (INFERRED — the bag is
  immediately explained as new and nameless); the whistle blow at
  104.2–104.4 s ("Blue!") is the narration's **"I blew"** with
  the pronoun cut by segmentation (INFERRED from the surrounding
  clauses "I raised the whistle. … The shoe jerked upward.").
  Beat structure is unaffected by either reading.
- **The narrator's name** ("Kobi") is INFERRED from the marker
  writing visible in frames (school bag, sheet_0 grid; the shoe,
  key_83.0) — it is never spoken in the transcript. Evie's name
  *is* spoken. The teddy's tag reading "EVE" is read from frames
  and matches the narration's "E, V, E."
- The video was watched as frames + full transcript, not screened
  in real time; performance-level claims (voice nuance, music)
  are limited to what ASR and the frame record show. The narration
  is a single flat TTS read (INFERRED from its uniform cadence
  and the account's prior posts); no music layer is separately
  credited or claimed.
- Metrics are the FxTwitter fetch at ~02:53 UTC on 2026-11-28,
  ~4.6 hours after posting; they will keep moving.
- Nothing about the creator's tools, revenue or workflow beyond
  the artefact is claimed — Roblox machinima has no prompt layer
  to reconstruct, and this study deliberately does not invent one.
- The account-level formula overlap with the rust post is stated
  in §C.8: the transplants above are the mechanisms this post
  adds or proves hardest, not a claim that the account invented
  them.
