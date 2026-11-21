# ANGLE 2 — Speech Reliability in Generated Video
## Recursive Improvement Pass 2 — 2026-11-18

**Scope:** Native-speech text-to-video for 60 s episodes built as 6 × 10 s units.
**Internal law under test (F-25 + Round-6 corollary):** ≤ ~30 spoken words and ≤ 2 speakers
per single generation; composites viable only with ≤ 1 spoken half; speech written as
colon-form blocks `NAME (trait, delivery): line`, no quotation marks anywhere in the prompt.
**Grades:** `VERIFIED` = primary vendor doc, or ≥2 independent sources converging, or a
benchmark / measured test. `INFERRED` = synthesis the evidence supports but no source states
in WuBu's exact form. `LEAD` = single practitioner claim / anecdote / unmethodologised number —
use as a test hypothesis, not as law.

---

## Headline verdict — read this first

1. **F-25's word cap is too loose by roughly 40–50%.** Every independent budget converges
   well below 30 words / 10 s: comfortable is **16–20 words total per 10 s**, hard ceiling
   **~20–25**, and that is for *one* speaker. A 2-speaker exchange needs a *lower* total, not
   the same total split in two, because it adds a turn gap. 30 words / 10 s = 180 wpm =
   reading-aloud speed with zero lead, pause, or tail. **[VERIFIED — §3.1]**
2. **F-25's speaker cap is right as a ceiling, wrong as a default.** ≤2 is the documented
   practical ceiling for Kling 2.6/3.0 and the outer limit everywhere else, but the
   practitioner consensus default for episodic work is **1 speaker per clip, cut together**.
   Two speakers in one generation is a *hero attempt*, not the template default. **[VERIFIED — §1, §2]**
3. **Colon-form / no-quotes is supported — for Veo-class models — and is NOT a universal law.**
   Google's *current* (10 Nov 2026) Cloud best-practice explicitly recommends
   `A woman says: My name is Clara.` and marks the quoted version *not recommended*, because
   quotes can make the model render the words on screen. But Seedance and Kling 3.0/4.0
   *require* quotes — quoted text is their spoken track. WuBu's rule is correct for a
   Veo-like / quote-leaking generator (which WuBu's own E2 evidence says theirs is); it must
   be recorded as **model-specific**, not as physics. **[VERIFIED, with a vendor self-contradiction — §3.2]**
4. **The "span law" is real, but it is mis-named. It is a container law, not a speech law.**
   A generation is a fixed-duration container. The model fills the container — by slowing
   delivery, by pausing, by trailing reaction/silence, and, documented for Kling, by
   **padding a too-short line with invented words**. So a spoken half generated as a full
   10 s take *is* a ~10 s span, whatever its word count. Two spoken halves = two containers
   = ~20 s of span for a 10 s slot. That is exactly Round 6's 9.7 s + 9.0 s ≈ 18.7 s.
   The corollary (composites only with ≤1 spoken half) therefore **stands**, and the fix is
   not "direct compression" — no source shows directed compression working — it is
   *generate the spoken half at the duration you actually need, or don't generate it spoken
   at all*. **[VERIFIED mechanism / INFERRED naming — §3.3]**
5. **The biggest practice WuBu lacks is not a word cap at all. It is per-line duration
   budgeting in seconds, measured from real audio (prelay / audio-first), plus explicit
   lead / internal-pause / turn-gap / tail budgeting.** Word count is only a first-draft
   proxy; every serious workflow found measures the line. **[VERIFIED — §4.1]**

---

## 1. Q1 — What current native-audio models and official guidance actually say

### 1.1 The model landscape (Nov 2026)

| Model | Native speech | Clip | Dialogue languages (vendor-stated) | Speaker handling (vendor-stated) |
|---|---|---|---|---|
| Veo 3.1 (Google) | Yes, always on in Gemini API | 4 / 6 / 8 s | English fully supported; others "not evaluated" | Multi-person dialogue in examples; no voice-selection control in API |
| Kling VIDEO 3.0 / 3.0 Omni (Kuaishou) | Yes | 3–15 s | Chinese, English, Japanese, Korean, Spanish + dialects; **other languages auto-translated to English** | Multi-character coreference claimed improved for 3+; Element voice binding |
| Kling VIDEO 2.6 | Yes (first Kling native audio) | 5 / 10 s | English, Chinese | Two speakers = practical ceiling in independent testing |
| Seedance 2.0 / 2.5 (ByteDance) | Yes, + audio-reference input | 4–15 s / 4–30 s | 8+ languages, phoneme-level lip-sync claimed | Quoted line = spoken track; accepts up to 3 (2.0) / 10 (2.5) audio refs |
| MiniMax H3 | Yes, stereo | 4–15 s | "Stable" in 11 languages | Audio refs accepted |
| Sora 2 (OpenAI) | Yes — **historical only** | 4–20 s in late API | — | Separate `Dialogue:` block, labelled alternating turns |
| Runway Gen-4 / 4.5 | **No native audio** | 5 / 10 s (4), 2–10 s (4.5) | — | Silent; dialogue via Act-Two / TTS + lip-sync tools in post |

- Native audio is now standard on the leading models, with the table above as the
  cross-vendor summary. **[VERIFIED]** — OpenMicroDrama model table, ToonlyAI model table,
  SeedDance comparison, each citing vendor pages.
- OpenAI shut down Sora 2 and its video API on 24 Sep 2026, so Sora guidance is a
  *design fossil* — still useful because its prompting guide was the most explicit about
  dialogue blocking, but it cannot be a production route. **[VERIFIED]** — ToonlyAI;
  OpenMicroDrama.
- Runway Gen-4 makes no sound at all; its own guide is a motion guide, and dialogue must be
  added afterwards. Any template borrowed from Runway tells you nothing about native speech.
  **[VERIFIED]** — Runway Gen-4 guide summary / GE Roundtable documentation-based guide.

### 1.2 Speaker counts per generation

- **Kling official (3.0 Omni):** "For multi-speaker scenes, identify the speaker plainly…
  Keep each speaker's line close to the character name." Its worked examples go to **four**
  speakers in one prompt (mother / father / boy / girl, one short line each) and a
  three-turn Korean exchange — but Kling gives **no word budget, no per-speaker budget, and
  no reliability rate** for those examples. They are capability demos, not production advice.
  **[VERIFIED that Kling claims it; LEAD that it is reliable at 3–4 speakers]**
- **Kling 2.6 independent testing:** "Kling 2.6 can handle dialogue between **two speakers**
  in a single clip… when three or more people talk in one scene, voice attribution tends to
  get confused and lines may be spoken by the wrong face"; "Three speakers in frame is where
  attribution slips." Atlas Cloud's 2.6 review says the same: 3+ = inconsistent attribution,
  stick to two-character exchanges. **[VERIFIED — two independent reviews converge]**
- **Veo:** Google's own DeepMind page notes natural-sounding speech is "still in active
  development" and to plan for re-rolls. Independent Veo guides converge on **one primary
  speaker per shot**; Magic Hour (summarising Google material): "Use one primary speaker per
  shot. Multi-person speech increases attribution and timing complexity… generate separate
  shots if the speakers or timing drift." **[VERIFIED]**
- **A widely repeated Veo number — single-speaker lip-sync ~80%, multi-speaker <40%,
  Chinese ~30% — appears in one guide with no test method, sample size, or prompt set.**
  Treat the *direction* (multi-speaker ≪ single) as corroborated and the *percentages* as
  unusable. **[LEAD]**
- **Sora 2 official prompting guide (OpenAI Cookbook):** "Keep lines concise and natural,
  and try to limit exchanges to a handful of sentences so the timing can match your clip
  length. For multi-character scenes, label speakers consistently and use alternating turns…
  a 4-second shot will usually accommodate one or two short exchanges, while an 8-second clip
  can support a few more. Long, complex speeches are unlikely to sync well." No numeric cap
  was ever published. **[VERIFIED]**
- **AVGen-Bench (Microsoft, 2026, arXiv:2604.08540)** is the only public joint audio-video
  benchmark found that scores Speech controllability separately. Even the top system
  (Seedance 2.0, total 72.07) and Veo 3.1-fast/quality (67.87 / 66.28) leave large headroom,
  and Face / Text controllability sit far below Speech for most systems — i.e. *who* is
  speaking and *what appears as text* fail before *whether something speech-like happened*.
  No vendor publishes a dialogue WER or speaker-attribution error rate for its video model.
  **[VERIFIED as a benchmark; INFERRED implication]** — and a genuine evidence gap: there is
  **no public "voice benchmark"** isolating pronunciation / attribution; leaderboards judge
  the whole clip. **[VERIFIED]** — AI Bibimbap comparison, stating this explicitly.

### 1.3 Line length — the vendor / practitioner budgets

No vendor publishes a words-per-clip spec. The budgets below are practitioner guides
built on the human speech rate (§3.1) — and they agree with each other to within a few words:

| Clip | Comfortable (target) | Approx. maximum | Source |
|---|---|---|---|
| 4 s | 6–8 words, 1 sentence | ~10 | ToonlyAI |
| 5 s | 7–9 words, 1 sentence | ~12 | Pippit; ToonlyAI (Kling 5 s) |
| 6 s | 10–12 words | ~15 | ToonlyAI |
| 8 s | 12–16 words, or 2 short lines | ~20 | Pippit (12–15); ToonlyAI (14–16); Prompt-Helper (≤16) |
| 10 s | **16–20 words, or a short 2-person exchange** | **~25** | Pippit (16–20); ToonlyAI (18–20) |

- "Keep spoken lines to roughly sixteen words or fewer for a short clip. Longer lines force
  Veo to compress the delivery, and compressed delivery is where lip-sync drifts."
  **[VERIFIED as practitioner consensus]** — note this directly predicts WuBu's internal
  finding that *directed* "compression" did not compress: the model either rushes (and sync
  drifts) or it doesn't comply.
- Kling 4.0 API docs (Runware): "An eight-second clip comfortably holds one or two short
  sentences." **[VERIFIED]**
- Seedance 6-speaker stunt (see §2, Camp D): the practitioner *self-imposed* ~65% of the
  theoretical word budget — 26 words used of a 45-word theoretical max for 15 s — explicitly
  to leave room for "pauses, reactions, head nods, beat changes." **[VERIFIED as reported practice]**

### 1.4 Prompt format for speech — quoted vs speaker-tagged is MODEL-SPECIFIC

This is the section where a single universal rule is actively harmful.

| Model | Format the current guidance prescribes | Evidence |
|---|---|---|
| **Veo 3.1 — current Google Cloud best practice (updated 10 Nov 2026)** | `A woman says: My name is Clara.` — **colon, NO quotation marks**. Quoted version explicitly marked *not recommended* | CapsAI's dated read of Google's pages; ToonlyAI; Ekly; AIPromptGeneer — all reporting the same current page |
| Veo 3.1 — Google's Oct 2025 prompting blog / Gemini API page | Dialogue **in quotation marks**: `A woman says, "We have to leave now."` | Google's own older guides — **the vendor contradicts itself across surfaces/dates** |
| **Seedance 2.0 / 2.5** | Line **in double quotes**; quoted text *is* the dialogue track, lip-synced phoneme-by-phoneme; name the language; add `EXACT, verbatim` clause | Frameliq (fal workflow guide); Cuty (ByteDance docs + community testing); Ekly ("Seedance, for one, wants quotes") |
| **Kling 3.0 / 4.0** | Speaker name + line + delivery **kept together**; official examples use curly quotes around the line; 4.0 API docs: "Whatever sits between them is what the character says, word for word" | Kling official Omni guide; Runware Kling 4.0 API guide |
| Kling 3.0 via fal (per OpenMicroDrama) | English speech in **lowercase**, capitals only for acronyms and names | **[LEAD]** — single secondary report of a fal model page; test before adopting |
| Sora 2 (historical) | Separate **`Dialogue:` block below the prose**, speakers labelled, alternating turns | OpenAI Cookbook prompting guide |

Universal across all of them (the part that *is* physics):
- Name / visibly describe the speaker **immediately before** their line; keep name, line,
  and delivery note **adjacent** — never describe all voices in one place and list all lines
  in another. **[VERIFIED]** — Kling official, ToonlyAI troubleshooting table ("Wrong
  character speaks → describe the speaker by a visible trait right before the line"),
  Sora guide.
- Delivery notes go **outside** the spoken words. Acting notes inside the line risk being
  spoken or garbling the lip-sync input, which must receive exactly the final words.
  **[VERIFIED]** — Pippit.
- WuBu's `NAME (trait, delivery): line` block is a *superset* of the Veo colon form and of
  Kling's name+line+delivery adjacency rule. Its structure is well supported. Only its
  **no-quotes clause** is model-dependent. **[INFERRED]**

### 1.5 Multi-speaker reliability — the named failure modes

Independent sources name the same four failures, in the same order WuBu hit them:

1. **Swap** — line spoken by the wrong face / voice. **[VERIFIED]** — OpenMicroDrama Veo
   guide ("Veo sometimes swaps or repeats lines between speakers"), Kling 2.6 reviews.
2. **Repeat / drop** — a line repeated, or a later line never spoken. **[VERIFIED as a
   reported mode]** — OpenMicroDrama lip-sync guide: two characters sharing a talky clip →
   "models swap lines, repeat them, or move both mouths."
3. **Both-mouths** — non-speaker's mouth moves too. Mitigation prescribed verbatim in Kling
   prompts: "Only the current speaker moves their lips," and by an H3 creator: let one
   character speak "while the other keeps their mouth closed." **[VERIFIED]**
4. **Voice drift across clips** — same character sounds like different people shot to shot.
   Mitigations: Kling Element voice binding / voice IDs, Seedance/H3 audio references, or
   post-hoc — run every line for a character through one voice in post. **[VERIFIED]**

No source found documents a *rotational* / *last-speaker-starved* pattern by name, and no
source documents speaker-order effects in video generation at all (see §4.4). WuBu's
11-attempt / last-speaker-starved observation is therefore **not contradicted** — it is
simply ahead of the public literature, which stops at "swap/repeat/drop." **[LEAD — WuBu's
own evidence is currently the strongest source on this specific pattern]**

---

## 2. Q2 — What working episodic creators actually do: four camps

### Camp A — Native multi-speaker in one generation
*Write all turns into one prompt; let the model perform the exchange.*
- Who: vendor demos (Kling's 4-speaker example), short-form / fruit-drama style pipelines
  (ToonlyAI's worked example is literally a two-character fruit-detective exchange in one
  Kling clip: `Lemon detective, low and unimpressed: … Banana, fast and squeaky: …`).
- Trade-off reported: fastest path, one generation, performance interaction is real —
  and it is the camp that produces swaps, repeats, both-mouths, and attribution loss at 3+.
- Verdict in the field: used for short, low-stakes exchanges; nobody found building a
  *serialised* show on Camp A alone. **[VERIFIED as practice; INFERRED verdict]**

### Camp B — Native, but ONE speaker per clip; cut the exchange together in the edit
*Each line gets its own generation; the conversation is an editing construct.*
- This is the **consensus reliability play** for episodic work:
  - OpenMicroDrama (micro-drama production guide): "**Use one speaker per clip.** When two
    characters share a talky clip, models swap lines, repeat them, or move both mouths. One
    Veo creator found a dull but reliable fix: give each character's line its own clip, then
    cut them together." Its Veo guide repeats it as shot grammar: "When two characters argue,
    make each side its own shot and cut between them. A TV editor would cover the scene that
    way anyway."
  - ClickPop dialogue guide: "Only one character should speak per clip. If two characters
    speak in the same generation, the model has to decide whose mouth moves when, and that
    is where things go wrong."
  - Skywork / Veo lip-sync guide: "the most reliable path is one sentence per clip… For
    two speakers: generate Speaker A's line as a [separate] clip…" and chain.
  - Magic Hour / Veo: one speaker + one or two short lines per clip as the reusable formula.
- Trade-offs reported: more generations per scene, you lose true in-take interaction /
  overlap, reaction must be directed separately (non-speaker mouth-closed, listening beat) —
  in exchange for attribution that survives, per-line re-rolls (fix one line without
  re-rolling the exchange), and clean joint points for last-frame→first-frame chaining.
- **[VERIFIED — four independent practitioner sources converge]**

### Camp C — Generate silent (or ambience-only) + separate TTS / voice pipeline + lip-sync in post
*Voice first or voice in post; picture never owns the words.*
- OpenMicroDrama's "Route 2": lock the performance in audio first (TTS or a human actor),
  generate the shot silent / background-only or from a still, then run a lip-sync model
  (Kling LipSync, sync. Lipsync 2.0, LatentSync, VEED, H3 Max Lip Sync, Wan 2.2 S2V —
  priced per second, all cheap relative to a re-rolled hero generation).
  Stated advantage, verbatim in substance: "you control every word, pause and retake, and
  you can reuse the same cloned voice for 80 episodes." Stated cost: slower, a round trip
  per shot.
- ACT3 AI's pipeline docs make the scaling argument explicitly: laying TTS under silent
  video "works for narration over B-roll, falls apart the moment a character's mouth is on
  screen"; post-hoc lip-sync is "three tools and two exports per shot — ten shots is an
  afternoon; two hundred shots is a month"; their answer is Camp D (§ below) inside one
  pipeline.
- Ekly on non-English Veo: the reliable move is exactly Camp C — generate the line with a
  dedicated speech model where pronunciation can be iterated cheaply, then lip-sync it on.
- ElevenLabs-voiceover workflow (AITasteBud): a separate voiceover "costs less than a cent
  a line and stays one voice across thirty shots. The price is sync" — so keep speaking
  faces off camera during voiceover, or send the pair through lip-sync.
- Trade-offs reported: total word/pause/voice control + series voice consistency + cheap
  line fixes (re-render audio, not picture) **vs** an extra pipeline stage, lip-sync
  artefacts in close-up (teeth/tongue smear; check `p/b/m` closures), and the need to keep
  non-speakers' mouths still in the silent plate.
- **[VERIFIED]**

### Camp D — Audio-first / prelay hybrid (the camp WuBu does not have yet)
*Build the finished audio track first — including multi-speaker tracks assembled line by
line — measure it, then generate picture to that track / duration.*
- Traditional animation's prelay, rediscovered: Hacker Noon practitioner report — after
  **nine failed generations** of the same 4 s line (clipped half a word early, or the shot
  ran 2 s past the last syllable), the fix was: say/record the line on a timer → generate
  or record the real audio → match clip tier to the *measured* duration → feed audio as a
  reference where the model accepts it → generate once against the locked track. A
  two-character exchange that kept failing silent-first rendered clean on attempt 2 once
  its scratch track was timed (just under 11 s) and the shot was built around that number.
- The 6-speaker Seedance case is Camp D at its limit: **six separate ElevenLabs voices**,
  assembled into **one 15 s track** with a protected **1.5 s silence before the punchline**,
  fed to Seedance 2.0 with **positional** speaker labels (`FRONT-CENTER-LEFT (navy jacket…)`,
  not "Guy 1") and explicit non-speaker "moving hold" rules. The author is explicit that
  numbered labels failed three generations ("the wrong character kept talking") and spatial
  labels fixed attribution. Note: this is **not** evidence native 6-speaker works — the
  voices, timing, and turn order were all locked *outside* the video model.
- ACT3's in-pipeline version: TTS runs per shot *from the script*, its duration **sets the
  shot length**, and the same audio drives the mouth — "you stop discovering timing
  mismatches after the render."
- Trade-offs: an audio stage before picture; needs a model/route that accepts audio
  reference (Seedance, Kling Elements, H3 do; Veo does not) or disciplined manual tier
  matching where it doesn't. In exchange, timing stops being a variable at generation time.
- **[VERIFIED as reported practice — two independent detailed write-ups + one pipeline doc]**

**Where WuBu sits:** Camp A with a word/speaker cap bolted on. The field's centre of gravity
for serialised work is **B as default, C/D for lines that must be exact, consistent, or
multi-speaker**. Camp A survives only as a budgeted exception (see Template Consequences).

---

## 3. Q3 — Attacking WuBu's calibration

### 3.1 Is ~30 words / ≤2 speakers per 10 s too loose, too tight, or right?

**Too loose — on words. Right as a ceiling, too loose as a default — on speakers.**

The arithmetic, from human speech first:
- Clear English delivery: **120–150 wpm** (2.0–2.5 words/sec); conversational average
  ~150 wpm; reading aloud ~183 wpm. **[VERIFIED]** — National Center for Voice and Speech
  figure via Baruch / VirtualSpeech; Brysbaert 2019 meta-analysis (183 wpm read-aloud);
  Cambridge conversation range 140–180 wpm via Pippit.
- 30 words in 10 s = **180 wpm sustained** — read-aloud speed, before any pause.
- A generated clip is not 10 s of speech window. Budget the non-speech time first
  **[VERIFIED — Pippit, with concrete numbers]**:
  - Lead silence: **0.3–0.5 s** (face settles; mouth must not be active on frame 1)
  - Internal pause at a meaning turn: **0.45–0.55 s**
  - Tail silence: **0.5–1.0 s** (mouth closes, expression settles, clean edit boundary;
    longer for a question, which needs a listening beat)
  - 2-speaker turn gap: at least one internal pause + a speaker change — budget **≥0.5 s**
- Remaining speech window in a 10 s unit: ~8.5 s (1 speaker) / ~8.0 s (2 speakers).
  At the *comfortable* AI-video planning rate of ~2.0 wps (Pippit: "allow about two words
  per second… use the lower end because facial settling, pauses, and the final mouth
  closure need room"): **~17 words (1 speaker) / ~16 words (2 speakers, total)**.
  At the *fill* rate of 2.5 wps: ~21 / ~20 words — with no margin for a long word, a name,
  a number, or an emotional delivery, all of which slow a line. **[VERIFIED inputs; INFERRED totals]**
- Cross-check against §1.3's independent tables: comfortable 10 s = 16–20 words;
  maximum ~25. WuBu's 30 sits **above every published maximum**, not at a comfortable point.
- WuBu's own measured ~0.3 s/word (≈200 wpm / 3.3 wps if taken literally as a *delivery*
  rate) cannot be a natural delivery rate — it is above read-aloud speed. Read it instead
  as evidence the model was **rushing/compressing or dropping** under overload, which is
  precisely the failure Pippit and Prompt-Helper predict for over-budget lines. If the
  0.3 s/word figure was instead a *span* measurement, see §3.3. Either way it does not
  support a 30-word budget. **[INFERRED — flag the measurement definition in the template]**

**Revised calibration (proposal, graded INFERRED from VERIFIED inputs):**

| Unit type (10 s generation) | Target | Hard cap | Per-line cap |
|---|---|---|---|
| 1 speaker | 14–17 words | 20 words | 20 (single line) / 10 per sentence, ≤2 sentences |
| 2 speakers, Camp A exception only | 14–16 words **total** | 18 words **total** | ≤9 words per turn, ≤2 turns, 1 turn change |
| 2 speakers, Camp B (default) | 2 separate generations, each budgeted as a 1-speaker unit at its *actual* generation duration | — | — |
| 3+ speakers | **Do not generate native multi-speaker.** Camp B or Camp D only | — | ≤6 words per turn in Camp D (cf. 26 words / 6 speakers / 15 s) |
| Silent / ≤1 spoken half composite | Spoken half budgeted at its *own* generation duration, never at the composite's slot duration | — | — |

Note the asymmetry the old cap missed: **adding a second speaker must *reduce* the total
word budget** (turn gap + attribution load), not leave it unchanged.

### 3.2 Is colon-form / no-quotes supported or cargo cult?

**Supported — narrowly, currently, and for Veo-class behaviour. Cargo cult only if it is
taught as model-independent.**

- For Veo: **[VERIFIED]** Google Cloud's video best-practice page, updated 10 Nov 2026,
  still teaches how "to prevent the model from rendering text in the video": write the line
  after a colon, leave out quotation marks; its example marks
  `A woman says: "My name is Clara."` as *not recommended* and
  `A woman says: My name is Clara.` as recommended. The mechanism is documented too: Veo
  was reported by MIT Technology Review (15 Jul 2025) to "often add nonsensical, garbled
  subtitles" to dialogue clips — one creative director estimated up to 40% of her dialogue
  scenes affected **[LEAD on the %]** — plausibly learned from training video with baked-in
  captions. The text is burned into the pixels; there is no caption track to switch off.
- The conflict is real and must be recorded: Google's Oct 2025 Veo 3.1 prompting guide and
  its Gemini API page **still show quotes**. Sources that simply repeat "Google says use
  quotes" are copying the older surface. Current-best-practice (Cloud, Nov 2026) wins for
  Veo, and "if text keeps appearing, drop the quotes first" is the documented triage.
- For Seedance / Kling, no-quotes would *break* the dialogue mechanism (§1.4): quotes are
  how those models know what is spoken vs what is a sign/subtitle. **[VERIFIED]**
- WuBu's additional local rule — *merged quoted blocks* dropped/garbled/invented lines in
  E2 — is consistent with the swap/repeat/drop literature, but no external source isolates
  "merged blocks" as the cause vs plain overload. Keep the rule; grade its mechanism
  **[LEAD / INFERRED]**.
- Practical consequence: keep no-quotes **for WuBu's current generator** (whose leak
  behaviour WuBu has directly observed — that local evidence outranks any vendor blog for
  that generator), but the template must carry a `MODEL SYNTAX` field so the rule flips
  deliberately if the generator changes, instead of being carried as superstition.
  Also: apostrophes/contractions inside the line are reported by one Veo guide to behave
  like quote marks for caption triggering **[LEAD]** — worth one controlled test, not a ban.

### 3.3 Is the span law a known behaviour or a local artifact?

**Known behaviour, three documented mechanisms, one local name.**

1. **Fixed container.** "AI video generation runs on fixed clip lengths, not on however
   long your line takes to say… You type a duration, or you pick a clip-length tier, and
   the model fills that window." If the line is short, "the shot pads itself with a beat of
   silence that reads as a mistake in the edit"; if long, it is "clipped mid-word."
   **[VERIFIED]** — Hacker Noon audio-first write-up; Pippit ("Filling all five seconds
   with speech makes the start and end feel clipped" — the inverse statement of the same law).
2. **Invented-word padding.** Kling 4.0 API docs, verbatim in substance: a line "much
   shorter than the clip **can be padded with invented words** to fill the time. For longer
   copy, raise `duration` rather than packing more words into the same clip."
   **[VERIFIED]** — this is the strongest single external corroboration of WuBu's
   "delivered speech expands" observation, and it explains *invented* lines, not just slow ones.
3. **Slow / stretched delivery + reaction tail.** Practitioner budgets universally assume
   the performance (speech + pauses + reaction + hold) occupies the whole take; the
   6-speaker case explicitly designs a SILENT BEAT and a HOLD as part of the take's span.
   **[VERIFIED as design practice]**

What is **not** documented anywhere found: a model deliberately *stretching a fixed word
count's phonemes* to exactly fill the take (true time-stretch), or a "compression"
instruction that reliably shortens a span. WuBu's "directed compression did not compress"
matches the literature's silence: **no source claims prompt-directed compression works.**
**[INFERRED]**

**Restated law for the template (replaces "span law"):**
> **CONTAINER LAW:** A generation's span is its requested duration, regardless of word
> count. Speech, pauses, invented padding, and reaction/hold distribute inside that
> container. Therefore: (a) never budget a composite from word counts — budget it from
> *generation durations*; (b) a spoken component generated at 10 s costs ~10 s of episode
> time even if it carries 8 words; (c) to get a 4 s spoken span, generate at 4–6 s (or
> generate silent + Camp C/D audio at a measured 4 s), never generate at 10 s and plan to
> use "the spoken part"; (d) the Round-6 corollary stands unchanged: composites viable
> only with ≤1 spoken half — and that half must itself be duration-budgeted.

This also retro-explains the 38-word / 4-speaker / 11-attempt failure without needing any
exotic mechanism: ~2× the word maximum, 2× the speaker ceiling, four turn gaps, and a
container that could not hold the turns — every documented failure mode stacked at once.

---

## 4. Q4 — Practices WuBu lacks entirely (or has only implicitly)

### 4.1 Per-line duration budgeting in SECONDS, from measured audio — the headline gap
- Workflow **[VERIFIED — Hacker Noon; Pippit; ACT3]**: write line → read it aloud on a
  timer *at performance pace* (performed dialogue runs **up to 30%+ longer** than silent
  reading) or generate a scratch TTS read → **log `duration_sec` next to the line** →
  choose the generation duration from that number (round *up*, never compress a longer
  line into a shorter tier) → only then generate picture.
- "The audio duration is the authority. Word count only helps you reach a workable first
  draft." — Pippit. WuBu's audit currently has no seconds field at all. **Add it (see §6).**
- Keep the scratch take attached to the shot record; it is reference data, not waste.

### 4.2 Explicit silence architecture
Lead (0.3–0.5 s), internal pause (0.45–0.55 s, placed at the *meaning turn*), turn gap
(≥0.5 s), tail (0.5–1.0 s; longer after a question). None of these appear as template
fields today; all are prescribed with numbers by Pippit. Also: protect a designed silence
before a punchline (1.5 s in the 6-speaker case) — silence is a budgeted item, not leftover.
**[VERIFIED]**

### 4.3 Non-speaker direction
Explicit lines WuBu's prompts lack: `Only the current speaker moves their lips.`
`[Listener] listens with mouth closed.` Plus a *moving hold* for listeners (breathing,
blinking, gaze shifts, micro-reaction) so Camp B reaction shots don't freeze into
mannequins — the single most-emphasised line in the 6-speaker prompt. **[VERIFIED]**

### 4.4 Speaker-order and labelling effects
- **Time-slotting turns:** Kling 4.0's documented conversation pattern assigns each turn a
  clock slot (`0–4 s: … 4–8 s: … 8–12 s: …`), states "only one person speaks at a time, with
  no overlapping dialogue" and "each person has a distinct voice" *outright in the prompt*.
  This is the only published mitigation that plausibly addresses last-speaker starvation:
  the last turn gets a reserved slot instead of whatever attention is left. **[VERIFIED as prescribed practice; LEAD that it fixes starvation specifically]**
- **Positional > nominal labels:** spatial labels (`front-center-left, in the navy jacket`)
  beat numbered/name-only labels for attribution, learned after repeated wrong-speaker
  failures. **[LEAD — single detailed practitioner report, but detailed and falsifiable]**
- **Prompt position:** Sora-era and Veo-era guides both note early prompt content carries
  more weight (first-~500-character primacy is claimed for Sora **[LEAD]**). No video-
  specific study of speaker order was found. **Gap recorded honestly:** WuBu should log
  speaker order + outcome per attempt (see audit field `speaker_order_outcome`) and become
  its own source, instead of importing an LLM-debate "first-speaker bias" result that does
  not transfer. **[Gap]**

### 4.5 Language / accent as a reliability variable
- Veo: English is the only *evaluated* language; non-Latin script in a quoted line +
  heavy performance language has been observed to trip the safety filter — transliteration
  fixed it in that report. **[VERIFIED limits; LEAD on the filter anecdote]**
- Kling: only CN/EN/JP/KR/ES are native; **any other language is auto-translated to
  English** — a silent failure mode if a brief ever calls for another language. Name the
  language *and* accent in the same sentence as the line; accents live in the delivery note.
  **[VERIFIED]**
- Seedance: name the language explicitly before any non-Chinese dialogue. **[VERIFIED as prescribed]**
- Consequence: the template needs `language` + `accent/dialect` per speaker, defaulting to
  an explicit `English` — never leave language implicit.

### 4.6 Audio-layer competition budgeting
Dialogue competes with music, SFX, and ambience inside one generated track. Prescribed
fixes: no music under dialogue clips (or one quiet ambience only), one SFX tied to a visible
action, delivery + ambience as separate sentences after the line. WuBu's briefs budget
*words* but not *audio layers*. Add an `audio_layers` count to the audit (dialogue + music +
SFX + ambience ≤ 3 in a spoken unit is the practitioner-shaped rule). **[VERIFIED problem; INFERRED cap]**

### 4.7 Framing for lip-sync
Medium close-up, speaker facing camera, mouth unobstructed, face large in frame; wide /
profile / turned-away speakers are a named cause of sync failure. Wider frames give more
pixels per face and fewer face-merging artefacts in multi-face frames. This belongs in the
unit's shot field as a check, not as lore. **[VERIFIED]**

### 4.8 Character-count / syllable load as a secondary meter
Word count hides load: long words, names, numbers, abbreviations, and tongue-twisting
clusters all slow or garble a line. Secondary meters used in the field: ~5.8 chars/word
average; respell hard names phonetically *for the voice* while keeping correct spelling
for captions; write numbers out as words. Add a `hard_words` flag to the audit rather than
a second cap. **[VERIFIED as practice]**

### 4.9 Voice identity as a bound asset, not a per-prompt adjective
Kling Elements bind a 5–30 s clean, single-speaker, moderate-pace audio sample to a
character; Seedance/H3 take audio references. Where no binding exists, the fallback is to
paste the *identical* voice description verbatim into every prompt for that character —
and, failing that, unify in post (Camp C). WuBu repeats visual descriptors for consistency
but has no equivalent voice-asset field. **[VERIFIED]**

### 4.10 Negative-prompt hygiene for text
Where a negative field exists, list the *things* (`subtitles, captions, on-screen text`) —
Google's guide advises against phrasing negatives as orders ("no… / don't…") in that field;
where no field exists, put a short negative in the prompt. Keep this separate from the
no-quotes rule: they stack, neither replaces the other. **[VERIFIED]**

---

## 5. Gaps and limits of this research (honest record)

- **No vendor publishes dialogue reliability numbers** — no WER, no attribution error rate,
  no per-speaker-count success rate for any current video model. All percentages in blogs
  (80% / 40% / 30%) are unmethodologised. WuBu's own attempt logs are, on this specific
  question, better data than the public literature — *if* they are logged in a comparable form.
- **Google's own Veo guidance contradicts itself across surfaces and dates** (quotes in the
  Oct 2025 guide / API page; no-quotes in the Nov 2026 Cloud best practice). This report
  follows the newer page and flags the conflict wherever the rule is cited.
- **Sora 2 is shut down** (24 Sep 2026). Its guide is cited only for dialogue-blocking design.
- Several model facts (Kling 4.0, Gemini Omni replacing Veo 3.1 Preview in the Gemini API,
  Seedance 2.5 30 s) come from Nov 2026 secondary pages reporting vendor docs; the vendor
  pages themselves were opened for Kling 3.0 Omni and AVGen-Bench, and read via dated
  secondary reports for Google Cloud best practice. No generation was run to test any claim.
- Speaker-order / last-speaker starvation, merged-block effects, and apostrophe-triggered
  captions remain **unverified externally** — they are WuBu-local findings awaiting the
  logging fields proposed below.

---

## SOURCES — URL + what it supports

- https://kling.ai/blog/kling-video-3-omni-native-lip-sync-audio-guide — Kling *official*:
  native audio, Element voice binding, name+line+delivery adjacency, simple grammar,
  5 languages, 3–15 s, 4-speaker demo example. (§1.1, §1.2, §1.4, §4.9)
- https://capsai.co/blogs/veo-3-gibberish-subtitles — Dated (11 Nov 2026) read of Google's
  own pages: current Cloud best practice = colon, no quotes, quoted example marked not
  recommended; Oct 2025 guide conflict; MIT Tech Review garbled-subtitles report; burned-in
  text, no caption switch. (§1.4, §3.2)
- https://www.toonlyai.com/blog/ai-video-with-sound — Veo/Kling word budgets by clip length
  (10 s ≈ 25 max / 18–20 comfortable), 2.5 wps rule, says-colon format, troubleshooting
  table (garbled / wrong speaker / subtitles / cut-off), Sora shutdown date. (§1.1, §1.3, §3.1)
- https://www.pippit.ai/blog/write-short-dialogue-fits-ai-video-clip — The seconds-based
  method: ~2 wps planning rate, lead 0.3–0.5 s / pause 0.45–0.55 s / tail 0.5–1.0 s with
  worked 5/8/10 s examples (7–9 / 12–15 / 16–20 words), delivery outside the line,
  "audio duration is the authority." (§1.3, §3.1, §4.1, §4.2)
- https://hackernoon.com/an-audio-first-workflow-for-ai-video-dialogue-shots — Audio-first /
  prelay workflow; 9-attempt failure → 2 attempts after timing the track; fixed-container
  mechanism; performed dialogue +30% vs silent reading. (§2 Camp D, §3.3, §4.1)
- https://runware.ai/docs/models/klingai-video-4-0/guides/dialogue-and-on-screen-text —
  Kling 4.0 API docs: quotes = verbatim spoken track; **short line "can be padded with
  invented words"**; 8 s = 1–2 short sentences; time-slotted 3-turn conversation pattern;
  "only one person speaks at a time / distinct voice" stated outright. (§1.4, §3.3, §4.4)
- https://openmicrodrama.com/guides/lip-sync-and-dubbing — Episodic production consensus:
  one speaker per clip, swap/repeat/both-mouths failures, Route 1 vs Route 2 (TTS +
  lip-sync) with tool prices, voice drift + fixes, 80-episode voice reuse. (§1.2, §1.5, §2 B/C)
- https://openmicrodrama.com/models/veo — Veo for micro-drama: one speaker + 1–2 short lines
  per clip, argue in shot/reverse-shot, burned-in captions + negative prompt. (§2 Camp B)
- https://arijiitdas.substack.com/p/how-i-got-six-ai-characters-to-talk — Camp D at the
  limit: 6 ElevenLabs voices → one assembled 15 s track, 26 words (≈65% of theoretical
  budget), 1.5 s protected silence, positional labels beat numbered labels, moving-hold
  rules. (§1.3, §2 Camp D, §4.3, §4.4)
- https://www.ekly.ai/guides/veo-prompting — Veo no-quotes syntax ("opposite convention
  from Seedance, which wants quotes"), fixed 4/6/8 s durations, non-English limits +
  transliteration report, decouple-audio recommendation. (§1.4, §2 Camp C, §4.5)
- https://www.frameliq.com/blog/seedance-2-guide-for-filmmakers — Seedance 2/2.5: no official
  ByteDance prompt guide; fal guidance = dialogue in double quotes, timed shot lists,
  4–15 s / 4–30 s, audio references. (§1.1, §1.4)
- https://www.cuty.ai/article/models/seedance-2-prompting-guide — Seedance quoting rules:
  quoted text engages the lip-sync pathway, name the language, `EXACT, verbatim` clause,
  8+ languages. (§1.4)
- https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/sora/sora2_prompting_guide.ipynb
  — OpenAI's Sora 2 guide: separate Dialogue block, labelled alternating turns, concise
  lines, 4 s = 1–2 short exchanges. Historical (model shut down). (§1.2, §1.4)
- https://microsoft.github.io/AVGen-Bench/ — Only public joint AV benchmark found scoring
  Speech controllability separately (Seedance 2.0 total 72.07; Veo 3.1-fast 67.87);
  Face/Text controllability lag Speech. (§1.2)
- https://www.media.io/creative-tips/kling-2-6-audio-prompts.html — Kling 2.6: small number
  of audible events, stable visual position/clothing to identify speakers, "only the
  current speaker moves their lips," official Audio User Guide exists. (§1.5, §4.3, §4.6)
- https://blog.picassoia.com/kling-2-6-lip-sync-voice-control-audio-and-free-alternatives —
  Kling 2.6: two speakers = practical ceiling, 3+ attribution confusion, quotes + delivery
  pattern, non-EN/CN speech translated to English, use dedicated lip-sync when you own the
  voice. (§1.2)
- https://www.atlascloud.ai/blog/tips/kling-2-6-review — Kling 2.6: 3+ speakers =
  inconsistent attribution, stick to two-character exchanges; speaker tags `[Character A]`;
  10 s recommended for dialogue stability. (§1.2)
- https://documentation.act3ai.com/how-to/adding_voiceover_ai/ — Three voice routes compared;
  in-pipeline TTS sets shot length and drives mouth; per-shot post round trips don't scale.
  (§2 Camps C/D, §4.1)
- https://clickpop.ai/guides/ai-video-with-dialogue — "Only one character should speak per
  clip"; native for short lines, post voice for exact voice / longer lines / consistency.
  (§2 Camp B)
- https://skywork.ai/blog/ai-video/how-to-prompt-lip-synced-dialogue-google-veo-3 — Veo:
  one sentence per clip, 3–6 s of speaking, chain clips for two speakers, external TTS if
  fine voice control is needed. (§2 Camp B)
- https://aipromptgeneer.com/craft/sound-in-ai-video/ — Four audio layers written on purpose
  or the model guesses; colon/no-quotes as Google's newest guidance, with the older-pages
  conflict noted. (§1.4, §4.6)
- https://imagera.ai/blog/ai-voiceover-for-video — Measured TTS timing: 67 words = 26.0 s /
  27.2 s in two voices (148–154 wpm); same words, 1.2 s apart — measure the file, not the
  script. (§3.1, §4.1)
- https://eastondev.com/blog/en/posts/ai/20251207-veo3-audio-generation-guide/ — Veo guide
  containing the 80% / <40% / ~30% lip-sync figures — cited **only** to grade them LEAD
  (no method published); also: write scene flow, not script blocks, for multi-character.
  (§1.2)
- https://prompt-helper.com/blog/veo-3-1-prompting-guide/ — Veo: ≤~16 words per short clip,
  longer lines → compressed delivery → lip-sync drift; burned-in subtitles negative. (§1.3)

---

## Template consequences — concrete, field-level changes for the production brief

Apply to the per-unit brief template and to F-25. Wording is drop-in.

### A. Replace the F-25 cap line
```
OLD: SPOKEN LOAD: ≤ ~30 words, ≤ 2 speakers per generation.
NEW: SPOKEN LOAD (10 s generation):
     - 1 speaker: target 14–17 words, HARD CAP 20.
     - 2 speakers: Camp B by default (separate generations). Camp A exception only
       with director note: target 14–16 words TOTAL, HARD CAP 18 TOTAL, ≤9 words/turn,
       ≤2 turns, 1 turn change. Adding a speaker REDUCES the word budget.
     - 3+ speakers: native multi-speaker FORBIDDEN. Camp B or Camp D only.
     - Composites: ≤1 spoken half (unchanged) AND that half is generated at the
       duration it will occupy (CONTAINER LAW), never at full-unit duration.
```

### B. Replace the per-unit spoken-load audit line with a budgeted audit block
Every spoken unit carries this block; a unit may not fire with any field blank:
```
SPOKEN-LOAD AUDIT — U<n>
  camp:            A (native multi) / B (1 speaker/clip) / C (silent+TTS+lip-sync) / D (audio-first)
  model_syntax:    veo-colon-noquotes / seedance-quotes / kling-quotes   [rule flips with this field]
  speakers:        <n>  [names]
  words_total:     <n>   words_by_speaker: <A: n / B: n>   chars_total: <n>
  hard_words:      none / list (names, numbers, long words — phonetic respelling noted)
  language_accent: <per speaker, explicit — never implicit>
  measured_sec:    <scratch/TTS read duration, performance pace>   [AUTHORITY — not estimated]
  silence_budget:  lead <0.3–0.5>s + internal_pause <0.45–0.55>s + turn_gap <≥0.5>s (if 2 spk)
                   + tail <0.5–1.0>s  =  <total>s
  speech_window:   generation_sec − silence_total = <n>s
  implied_rate:    words_total / speech_window = <n> wps   [PASS if ≤2.0 target, FAIL if >2.5]
  generation_sec:  <requested duration>   span_cost_sec: <same number — CONTAINER LAW>
  time_slots:      (Camp A/D only) 0.0–<n>s: <SPEAKER> / <n>–10.0s: <SPEAKER>
  non_speaker:     mouth-closed line present? Y/N · moving-hold line present? Y/N
  audio_layers:    dialogue + <music? SFX? ambience?> = <n>  [spoken unit: ≤3, no music under dialogue]
  framing_check:   speaker medium close-up / facing / mouth unobstructed? Y/N
  voice_asset:     <bound voice ID / audio ref, OR verbatim voice description pasted unchanged>
  negative_text:   subtitles, captions, on-screen text  [in negative field where one exists]
  verdict:         PASS / REWRITE (shorten, never "compress") / SPLIT TO CAMP B / MOVE TO CAMP C-D
```

### C. New standing rules to add beside F-25
1. **CONTAINER LAW** (text in §3.3) — replaces "span law" in all briefs; composites are
   budgeted in *generation seconds*, not words.
2. **MEASURE, DON'T COUNT** — no spoken unit fires on word count alone; `measured_sec`
   from a timed read / scratch TTS is the authority, and generation duration is chosen
   from it (round up). Silent reading is not a measurement (performed = +30%).
3. **SHORTEN, NEVER COMPRESS** — an over-budget line is cut or split to Camp B; the words
   "compress / faster / squeeze" are banned as delivery directions for an over-long line.
4. **DEFAULT CAMP B** — an exchange is shot/reverse-shot by default; Camp A is a noted
   exception with the reduced budget in (A); Camp D is required for any 3+ voice beat and
   recommended for any punchline beat that depends on a protected silence.
5. **SYNTAX FOLLOWS MODEL** — colon/no-quotes is stored under `model_syntax`, not as a
   universal prompt rule; on a quote-model (Seedance/Kling) the same brief must render
   lines quoted, with name+line+delivery still adjacent and delivery still outside the line.
6. **LOG THE ORDER EFFECT** — add to the attempt log: `speaker_order`, `turns_completed`,
   `dropped_speaker` (name or none), `invented_words` (Y/N + transcript), `span_sec`
   (measured first-to-last speech + hold). This is the dataset that will let WuBu confirm
   or kill the last-speaker-starvation and merged-block hypotheses with its own evidence,
   since no external source settles them.
7. **EAR GATE STAYS, WITH A NEW CHECK** — at Gate E / ear-test, also check: did any span
   exceed its `span_cost_sec` budget, and did any invented word appear? Both are automatic
   REWRITE verdicts, not nits — they are the two signatures of container-law violation.

### D. What does NOT change
- Colon-form block structure `NAME (trait, delivery): line` — kept for WuBu's current
  generator; it satisfies both the Veo colon rule and the universal adjacency rule.
- ≤1 spoken half in composites — kept, now justified by the Container Law rather than by
  a local span observation alone.
- Two designed speakers as the episode cast ceiling (E3 taste law) — untouched; this
  angle governs *per-generation* load, which is now stricter than the cast ceiling.
