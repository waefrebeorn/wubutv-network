# TALKING-STORY CREATORS — research for the writers-room fix

**Order:** user, Telegram msg 470 (2026-11-15), verdict on SHOW-3 E2
"The Pass, Done Properly": the characters are *"talking every single
breathing second… no downtime and no gap for anything to be digested…
we're microwaving the viewers"*; *"I don't really see a story coming
out of this… esoterically babbling about nonsense and numbers… they
can get a little bit smarter… aware of the environment, questioning
it"*; *"research more creators that actually have engaging generated
content with stories where they're talking"*; visuals praised — *"it's
really just the writing and the script writing."* (The same message's
motion/jump-cut directive is a separate workstream, not covered here.)

**Method:** three parallel research lines — (A) AI series/stream
creators with talking characters, (B) AI short-film/studio craft,
(C) dialogue-pacing science + the AI micro-drama industry. Labels:
**EVIDENCED** = stated in a cited source; **LEAD-LEVEL** = self-report,
secondary summary, or transfer inference. Nothing below invents a
workflow or a number; §6 lists what could NOT be evidenced.

---

## §1. The diagnosis, in arithmetic (the budget itself is the bug)

Our current writers-room budget is 22–25 words per full-talk 10s unit
(hard ceiling 28), with **at most one** scripted silence beat (2–3s)
per 60s episode. At the documented conversational articulation rate
of ~150 wpm = 2.5 words/sec (National Center for Voice and Speech
figure), 22–25 words = **8.8–10.0 seconds of actual speaking inside a
10-second unit**. Six such units = **88–100% of the episode's runtime
spent speaking**, leaving 0–1.2s per unit for every turn gap,
reaction, action and silence combined. Wall-to-wall talk is not a
performance failure by the rooms; it is what the budget mathematically
produces.

Every independent evidence route lands in the same other place:

- **Stephen Follows, 61,517-film subtitle study:** dialogue share of
  runtime fell from 60% (1940) to 35.6% (2005) and sits now at **just
  under 50%**; the median gap between spoken lines is **1.9s in
  comedies, 3.7s in war films** — gaps are the normal rhythm, not an
  event. (EVIDENCED)
- **Pavlik script dataset (via RedShark):** the average feature
  carries ~9,000 dialogue words ≈ **82–100 words per runtime minute**
  — i.e. ~55–65% speech fraction. A narration-heavy annotated film
  (*Forrest Gump*, F1000Research) measures ~113 words/runtime-minute.
  (EVIDENCED / measured)
- **Subtitle absorption standards:** Netflix caps at 20 chars/sec;
  BBC targets **160–180 wpm** reading speed; the educational DCMP
  standard — the one designed for viewers who must also learn from
  the picture — drops to **130–160 wpm**. Eye-tracking (Szarkowska &
  Gerber-Morón, PLOS ONE 2018) shows 20 CPS is a *coping* ceiling, not
  a comfort target; caption research shows dense text cannibalises
  picture-watching (~84% of gaze on captions in the Jensema study
  population). Our shows' product IS the picture. (EVIDENCED)
- **Veo-era per-clip guides:** a 10s generated clip holds ~25 words
  max, **18–20 comfortable**, and an 8s clip really holds **one line
  of 6–12 words**. (Practitioner, consistent across guides)

**Converged target: ~80–95 spoken words per 60s episode (50–60%
speech fraction)** — roughly a 40% cut from the current 132–150,
achieved by converting units, not by thinning every unit equally:
the hook and peak units stay dense; the middle converts to mixed and
quiet. Full budget table in `amendments.md`.

## §2. Creators studied

### The directly transferable

**@BigYowie / Bigfoot vlogs (Seiji, TikTok, Veo 3, 2025).**
250k+ followers, 35M views in 20 posts; the format's first video did
6.3M plays in 3 weeks. The Kapwing creator interview is the most
useful craft document in this study (EVIDENCED): *"The hardest part
of making a video is script writing."* His order per scene: outline
**the major actions / the emotional shift / which lines need to
land** — then prompt. **One character per scene** (multi-character
action takes 50+ prompts and may not be possible; a close-up talking
shot takes 5–10). Personality is designed as **one verbal sentence**
("dry, casually destructive", Australian register) + **one visual
anchor repeated in every prompt** (the "YOWIE" cap). His
self-awareness gag engine: Bigfoot complains about *how the world
treats him* — trail cams, blurry photos — awareness of his own image,
in plain modern words. He credits storyboarding and the 180-degree
rule, not prompting, for coherence.

**Neural Viz / Monoverse (Josh Kerrigan, YouTube/TikTok).** A
one-person AI TV network (mockumentary, cop show, ghost-hunting
parody) with recurring characters and cross-episode subplots;
hundreds of thousands to millions of views per piece (profile-level
EVIDENCED; no audited subscriber count found). Method (EVIDENCED):
**full TV-format script first** — slug lines, action, dialogue,
blocking — then a storyboard still per shot with lighting/sight-lines
locked; **he acts every line himself** and maps the performance
(timing, head turns, pauses) onto the characters (Runway Act-One).
The world is designed around the tool's strength ("AI is good at
talking heads, so the Monoverse is mostly aliens talking to a
camera"), graded as worn VHS so flaws read as style. **"Smart" =
dramatic irony:** his glurons confidently misread vanished human
culture; the viewer always knows more than the expert on screen. A
generation glitch (a stretched vowel) was kept as a character's
signature cadence; a Sora skin change was written in-world as the
character "metamorphosizing" — **the fiction absorbs production
reality instead of hiding it.**

**AI Presidents Gaming (YouTube/TikTok, 2023– ).** Human-written,
voice-cloned presidents bantering over games/tier lists; clips at
1.6M likes in 4 days, 6M+ views (EVIDENCED via Know Your Meme /
InsideHook). Creator Regular Pat (EVIDENCED): the dialogue is
*written to interrupt* — overlaps, "uhs", stutters — and it works
because the cast dynamic is pre-known ("well-understood characters
to almost everyone"). The structural lesson: **a shared visible task
with a finish line** (rank the games, finish the match) gives every
line a referent the camera can show, gives pauses a job (someone is
deciding/moving something), and gives the scene a built-in ending.
Viewers call the result "comforting" — low-stakes conflict, no plot
to track.

**AI historical POV vlogs (@timetravellerpov et al., TikTok, 2025).**
329k followers / 5.7M likes in weeks (Fast Company); single videos at
21.8M views (Dexerto); an arXiv dataset counts 5,565 such videos,
average 35.9s. The form is a **fixed template** (EVIDENCED): "POV:
You wake up in [place, disaster year]" — title-as-contract before
line 1 — spoken hook inside 3s, escalation, cliffhanger/punchline
ending, built from 4–8 short clips. Crucially, much of the form has
**little or no performed dialogue**: legibility is carried by caption
+ place + **one ordinary physical action** (waking, walking, giving
bread to a beggar, visiting a sick mother), narrated in modern
vlogger register. Feelings scale better than facts; accuracy errors
did not stop the views.

**Dave Clark (Promise studio).** Traditional director; AI shorts
*Borrowing Time* (viral, 3 min), *Battalion*, *Tairell Isn't Real*
(Runway AIF 2026 Honoree). Craft (EVIDENCED): the relatability
anchor is **a true story statable in one sentence** (his father's
1960s story, flipped into one impossible chance to fix it); *"The
technology itself isn't emotional. The emotion comes from the context
you bring to it."* He **performed the voices himself** because his
plain read "sounded better… the natural pauses" — pauses are
performed, not generated. On pacing: *"Editing is where tension is
actually created. How long you stay on a face. When you cut. When you
don't cut"* — and he deliberately varies shot lengths (1s and 8s in
the same film) to break uniform clip rhythm. His *Tairell* premise —
an influencer who unravels when the internet decides he isn't real —
is the "character questioning his own existence" beat as a whole
film.

**The Dor Brothers (Berlin AI studio).** Viral satire + brand work;
view counts are studio self-report (LEAD-LEVEL: "500M views across
300+ projects"; trade reports put their biggest single video at
17–50M). Craft (EVIDENCED across interviews): the work is
**selection, not generation volume** — "I generate 50 clips… maybe
select two", sometimes hundreds of versions; the model is a crew you
sift, not a shoulder you sit on. Satire rule: *"keep it classic…
digestible, like eating a truffle"* — one clear idea per piece.
Legibility comes from **borrowed context** (the audience already
knows the news/public figures; zero exposition spent). And a limit
worth respecting: he **turned down $3M to make a 90-minute AI movie**
— "come back when the tech is ready" — long-form AI legibility is
not claimed as solved even by its most successful studio.

**Waymark, *The Frost* (2023).** Human-written 12-min AI narrative
(MIT Technology Review premiere). Lessons (EVIDENCED): **one
environment for the whole film** (snow forgives every continuity
drift; "inside would be a whole different ball of wax"); the **first
dialogue line is an object + action** ("Pass me the tail", cut to the
wrong object) — dread and story in seconds, no exposition; character
continuity via **archetype, not identity** (the mad-scientist
silhouette holds while faces change); shot/reverse-shot conversation
was the hardest thing they did — coverage is mined iteratively, not
assumed.

**Runway Gen:48 / AI Film Festival winners (2024–2026).** The
pattern across winners (EVIDENCED as reviews/listings): **every
winner is built on an idea you can say in a sentence, containing a
question** (*The Well*: a sharp-witted hare investigates a dead wolf
— the questioning character as premise). Narration and workarounds
beat wall-to-wall dialogue: *Voids* gives characters TVs for heads
with the words on screen ("painfully relatable"); *RUPU-KK* repeats
one workplace loop with a change until the viewer is invested;
*Beatrice* (Grand Prix, 1:56) is carried by narration over small
moments. The counter-proof: Best Craft winner *Honu* was flawless
and the reviewer still noted "there is not much of a story" — the
exact praised-visuals/weak-story split the user is flagging in us.

**Curious Refuge (AI filmmaking school).** Public curriculum only —
lesson content is paywalled, so **no dialogue numbers are
attributable to them** (honest gap). What is public (EVIDENCED as
curriculum): Module 1 is story/script/character/world **before a
single frame is generated**; the Module 2 deliverable is a
**30-second trailer** — legibility tested at trailer length before
the short is finished. Their own viral proof was a borrowed-context
collision (Wes Anderson × Star Wars) legible in under 3 seconds.

### The cautionary evidence

**Nothing, Forever (Mismatch Media, 2022– ).** The AI Seinfeld
stream peaked at ~47k followers / ~11k concurrent in days
(EVIDENCED) — as **ambient viewing** ("leave it on… even when you
are asleep"). Its pacing secret is **segment rotation**: sitcom
scenes alternate with stand-up, channel-surfing and weather segments
— dialogue is never continuous. Its failures are documented too:
setups orphaned, conversations never followed up, plans forgotten.
And its famous "dead air" (Larry frozen at the mic) became a gag
*by accident*. Lesson: it held an audience precisely because nobody
had to follow a 60-second story. We do. Borrow the segment rotation
and the scripted reaction pause; do not borrow the amnesia.

**ai_sponge (2023).** 26k Twitch followers in a month, ~221k YouTube
subs (EVIDENCED, Wikipedia) — on **audience-supplied topics** and
**single clippable lines** ("12 August 2036, the heat death of the
universe") that travelled as clips, plus "Some Time Later" time
cards as dialogue-free joints. Unfiltered density ended in repeated
bans. Lesson: design lines that can be clipped alone, and let a
visual card — not a line — make at least some joints.

**Sunspring (2016) + Solicitors (2020).** The negative control for
AI-written dialogue (EVIDENCED): Sunspring's generated script
"repeats sentence constructs without any logic", one phrase 4× in 4
pages, plot non-existent; it played at all because **actors'
performance supplied the legibility the text lacked**. Solicitors,
with a human-pre-written scenario and half the runtime, held a basic
three-act shape. Conclusion in the analyses: machines can draft
*within* a scene; humans must hold the thread *between* scenes, and
repetition-without-a-turn is the #1 incoherence tell.

**Fable SHOW-1 / Showrunner (2023 paper).** No audience evidence
exists (honest gap) — a systems source only. Three transferable
mechanisms (EVIDENCED as the paper's design): (1) **plot-pattern
alternation** — scenes lettered A/B/C and alternated (ABABC);
downtime for one storyline is literally the other storyline;
(2) **character cards before dialogue** — a simulation supplies each
character's history, goals and emotions *before* any line is
generated, the paper's explicit fix for context-free babble;
(3) **dramatic operators** (reversal, foreshadowing, cliffhanger)
injected procedurally by rule, not left to the writer's instinct.
Also its named warning, aimed exactly at our repetition problem:
the **"10,000 bowls of oatmeal"** — unlimited generation converges
to sameness and engagement decays. Note the one thing NOT to copy:
SHOW-1 buffered voice clips to engineer pauses *out*; its pacing
came from alternation alone.

## §3. The pacing evidence (numbers, graded)

| # | Finding | Grade |
|---|---|---|
| 1 | Articulation ~150 wpm (2.5 wps) conversational — a rate *while speaking*, not a runtime budget | documented standard |
| 2 | Film dialogue share ≈50% of runtime today; median inter-line gap 1.9s (comedy) – 3.7s (war) — Follows, 61,517 films | measured study |
| 3 | Average feature ≈82–100 dialogue words per runtime minute (Pavlik); narration-heavy outlier 113 | measured study |
| 4 | Absorption ceilings: Netflix 20 CPS max; BBC 160–180 wpm; DCMP 130–160 wpm where the picture must also be learned from; 20 CPS is coping, not comfort (eye-tracking) | documented standards |
| 5 | Natural turn gap ≈200 ms (Stivers et al., PNAS) — so a 2–3s silence is 10–15× natural and reads as *meaning* (shock/refusal/grief); spend it rarely, on turns | measured study |
| 6 | Segmented presentation with pauses measurably improves absorption vs continuous (Mayer segmenting principle, d≈0.34 transfer) — instructional domain, transfer by analogy | measured study, flagged |
| 7 | Micro-drama event cadence: hook ≤3s, ONE event / one value change per episode, mini-reversal ~20–25s, cliffhanger in final 3–15s; 65% of viewers who watch 3s stay ≥10s (Sprout data) | practitioner / trade |
| 8 | Micro-drama counter-models: ~12–18 sentences per 90s episode, **≤12 words per line**, "leaves room for looks, inserts and the beat after the last line" (HotPlot; WaveSpeed; Dawnwood) | practitioner |
| 9 | Practitioner film guides converge: one line max per shot (Graver); "leave silence somewhere — one genuinely quiet moment makes every loud moment louder"; done-test = "watch it start to finish without wanting to explain anything" (Domer) | practitioner |
| 10 | Comedy pause ≈1s before a punchline, set in the edit (micro-drama comedy craft) | practitioner |

## §4. What NOT to copy

- **The micro-drama industry's dialogue density.** Its own format
  guides specify 180–360 spoken words per 60–120s episode at an
  assumed 3 words/sec — speech filling ~100% of runtime *by
  construction*, under an explicit "no dead air" rule. That is a
  paywall-retention technology (the money event is the episode 10–12
  tap-through), it reproduces exactly the "microwaved" effect the
  user reported, and its outcomes argue against it: of ~61k AI
  comic-dramas launched in China in 2025, **96 (0.16%) passed 100M
  views** and ~64% never reached 1M (Daxue/DataEye synthesis,
  trade-press). Borrow only its *event* cadence (Finding 7), never
  its word density.
- **Nothing, Forever's amnesia.** Ambient tolerance for orphaned
  setups is a property of infinite streams, not of 60s episodes.
- **SHOW-1's pause removal.** Alternation is a real pacing tool;
  engineering out the within-scene breath is the opposite of the
  fix the user ordered.
- **"Pattern interrupt every X seconds."** No citable measured basis
  exists (vendor blogs analysing undisclosed data); a mechanism
  counter-argument (habituation of the orienting response) is at
  least as strong. Do not build a rule on it.

## §5. The rules (consolidated; each tied to evidence)

1. **Budget the episode, not just the unit.** ~80–90 spoken words per
  60s (hard cap 95), speech fraction ≤60%, target 50–57%. (§1, all
  routes converge.)
2. **One line that must land per unit.** Outline order per unit:
  action → emotional shift → the line. Everything else is action,
  reaction, or silence. (Big Yowie; Graver one-line-max; Veo guides.)
3. **Three digestion gaps, placed on the turns.** 2–3s of no dialogue
  after U2's turn, after U4's peak turn, and as the final 2–3s hold
  after U6's cliff line; plus a ~1s reaction hold after any
  punchline/reveal. (Follows gaps; Stivers markedness; micro-drama
  event cadence; comedy-pause craft.)
4. **Alternate segment jobs and cast.** Letter the six units
  (e.g. A B A C A B) on the board; vary who talks, where, doing what.
  No six consecutive same-cast/same-room dialogue units. (SHOW-1;
  Nothing, Forever rotation.)
5. **One talker by default.** Two-handers are the expensive,
  failure-prone exception — spend them on the episode's tensest unit
  only. (Big Yowie production economics; also rhymes with the user's
  msg-467 calibration: reserve the big device for tenser moments.)
6. **Title-as-contract in U1.** Place + person + want/danger in
  picture and plain words before the first line is spent; **first
  line = a visible object + action**, never a lore term. (POV
  template; The Frost.)
7. **One ordinary physical action per unit** that carries story with
  the sound off; dialogue comments on the action, never replaces it.
  Where the format allows, one **shared visible task with a finish
  line** per episode — its completion is the ending. (POV actions;
  AI Presidents.)
8. **Smart = dramatic irony + a questioning job.** The cast holds
  one shared wrong belief the viewer can see through; ONE character
  is assigned the questioning job — notices by U2, names it in one
  short line by U4, acts on it in U6. Awareness is dramatised, never
  explained. (Neural Viz; The Well; Tairell.)
9. **Character cards before dialogue.** Three lines per speaker —
  history / this-episode goal / entering emotion — pasted into the
  dialogue pass. No card, no lines. (SHOW-1.)
10. **Performed timing.** The dialogue pass includes a scratch read
    aloud with pauses; a line with no natural breath in performance
    is cut, not crammed. Timing comes from the read, not only from
    counts. (Neural Viz; Dave Clark; Domer.)
11. **Coverage, not masters.** Write speaker MCU → insert
    (object/hand) → listener reaction (silent) inside units instead
    of 10s two-person dialogue masters. (Graver; The Frost.)
12. **One clippable line per episode** — a complete, strange,
    quotable sentence that needs no context. If none exists, the
    episode has no hook. (ai_sponge; Bigfoot.)
13. **Repetition audit.** Any phrase or information repeated across
    units without a change of meaning is cut. Repetition *with* a
    difference (a loop revisited, one detail wrong) is story;
    repetition without is the incoherence tell. (Sunspring;
    RUPU-KK; SHOW-1 oatmeal warning.)
14. **Cold story test before lock.** A reader who has never seen the
    show states, from the summaries and again from the locked draft:
    who wanted what, what blocked them, what changed, and why anyone
    outside the lore should care. Needing a lore term = fail; the
    fix is cutting/replacing lines and adding visible action, never
    adding explanation. (Domer done-test; festival one-sentence
    pattern; Clark one-sentence stake.)

## §6. Honest gaps

- No published study directly reports "% of runtime that is speech"
  for film/TV; the fraction targets here are derived from words-per-
  runtime-minute ÷ articulation rate, cross-checked three ways.
- No platform (ReelShort/DramaBox/Chinese) publishes a dialogue spec;
  all micro-drama numbers are practitioner/trade tier.
- Curious Refuge publishes no dialogue/pacing numbers publicly.
- SHOW-1 has no audience/retention evidence at all.
- Editing literature is unanimous on holding reactions but offers no
  measured pause-length standard; the 2–3s gap rests on the Follows
  gap distribution + Stivers markedness, not on an editing study.
- Neural Viz engagement figures are profile-level, not audited.

## Sources (principal)

Follows dialogue study — stephenfollows.com/p/has-the-way-movies-use-dialogue-changed ·
Follows shots study — stephenfollows.com/p/how-many-shots-are-in-the-average ·
Pavlik via RedShark — redsharknews.com/lets-talk-about-dialogue ·
Forrest Gump annotation — f1000research.com/articles/10-54 ·
Subtitle standards — meetwave.io/blog/subtitle-reading-speed ·
Szarkowska & Gerber-Morón — researchgate.net/publication/325864139 ·
Stivers et al. summary — webridgeai.com/blog/voice-ai-turn-taking ·
Kapwing Bigfoot interview — kapwing.com/resources/what-it-takes-to-make-viral-ai-video-content-we-asked-bigfoot ·
Know Your Meme (Bigfoot/POV/Presidents) — knowyourmeme.com ·
Fast Company POV — fastcompany.com/91280871 · Dexerto — dexerto.com/tiktok/tiktoks-viral-ai-history-pov-trend-lets-you-go-back-in-time-in-first-person-sort-of-3137127 ·
arXiv POV dataset — arxiv.org/html/2606.23300v1 ·
Neural Viz profiles — thedaringcreatives.com/creator-stories/neural-viz-ai-tv-universe · scalebytech.com/neural-viz-filmmaker-josh-crafts-ais-first-cinematic-universe ·
Nothing, Forever — tvtropes.org/pmwiki/pmwiki.php/WebAnimation/NothingForever · pipedot.org/article/68EZR ·
ai_sponge — en.wikipedia.org/wiki/Ai_sponge ·
AI Presidents — inverse.com/gaming/youtube-ai-presidential-gaming-debates · insidehook.com/internet/presidents-ranking-video-games-ai ·
SHOW-1 paper — fablestudio.github.io/showrunner-agents ·
Dor Brothers — thedaringcreatives.com/creator-stories/the-dor-brothers-fifty-clips-keep-two · creativebloq.com/ai/fear-is-the-mind-killer-how-the-dor-brothers-are-redefining-ai-filmmaking ·
Dave Clark — thedaringcreatives.com/creator-stories/dave-clark-borrowing-time-ai-short-film · nofilmschool.com/dave-clark-interview-adobe-max ·
Curious Refuge — caleb-ward-toc4.squarespace.com/ai-filmmaking · motionhatch.com/podcast/ep-107 ·
The Frost — cognitiverevolution.ai/ai-powered-filmmaking-with-waymarks-stephen-parker-and-josh-rubin ·
Gen:48/AIF — nerdly.co.uk/2024/10/20/winners-announced-for-the-3rd-annual-ai-runway-gen48-short-film-festival · aicinema.substack.com/p/from-gentle-to-feast-in-ai-cinema ·
Sunspring — screencraft.org/blog/a-i-writes-a-screenplay-screenwriters-breathe-a-sigh-of-relief · filmscalpel.com/sunspring ·
Graver — aiwritersstudio.substack.com/p/how-to-write-a-script-ai-can-read ·
Domer — domer.io/blog/ai-storytelling-short-film-workflow ·
Veo guides — dreamdrive.ai/learn/google-labs/veo-3-prompting-dialogue-and-sound · toonlyai.com/blog/ai-video-with-sound ·
Micro-drama — microdrama.id/en/academy/short-drama-foundations · shortdramaalliance.medium.com/how-to-write-a-short-drama-hooks-pacing-and-paywall-basics-171c811fac84 · scenemixer.com/guides/vertical-short-drama-script-format · hotplot.net/learn/phone-dialogue · wavespeed.ai/blog/ai-guides/write-a-vertical-ai-short-drama-script-that-ends-on-a-cliffhanger ·
AI drama scale — daxueconsulting.com/ai-in-entertainment-and-media-industry
