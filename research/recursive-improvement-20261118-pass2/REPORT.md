# RECURSIVE IMPROVEMENT PASS 2 — audit the fix, then make the fix real

**Order:** Telegram msg 652 (2026-11-18) — "now do it again
recursively improve use online research." The "it" is the Pass 1
devil's-advocate audit (msg 642, 2026-11-18): three angles over the
production system for what was slipping, ending in a Revised
Reference + Prompt Design Protocol (AUDIT.md §5 A–F) that was
adopted as E3 law by declaration the same day, on top of the
ratified TASTE_GUIDE §8.

**Method:** three fresh online-research devil's-advocate angles
(full texts: `ANGLE1.md`, `ANGLE2.md`, `ANGLE3.md` in this
directory; every claim graded VERIFIED / INFERRED / LEAD with
primary sources where reachable) + one grep verification of the
real system (`VERIFICATION.md`) + one applied fix (the template,
below). Zero generations, zero postings.

---

## 1. The recursive verdict — the adoption did not land

Pass 1's core lesson was: *law that lives only in guide documents
does not reach the work* — in E2, zero vehicles carried the END
STATE / REFERENCE PRIORITY / OBJECTIVE / EYE TASK fields even
though the rules existed on paper. Pass 2's verification greps the
system for the ten fields the 2026-11-18 adoption (TASTE §8 +
AUDIT §5) was supposed to install, classifying every hit as
**T** (fill-in field in a reusable template), **V** (present in an
actual production artifact), or **G** (prose in a guide/law doc):

| # | Adopted field | T | V | G | Verdict |
|---|---|---|---|---|---|
| 1 | END STATE block | 0 | 0 as a block | F-22, AUDIT §5C | GUIDE-ONLY |
| 2 | REFERENCE PRIORITY block | 0 | 0 | F-24, AUDIT §5D | GUIDE-ONLY |
| 3 | OBJECTIVE/OBSTACLE/TACTICS | 0 | 0 as fields | F-23, AUDIT F9 | GUIDE-ONLY |
| 4 | EYE TASK | 0 | 0 (1 line in the whole new-era tree: the guide) | F-23 | GUIDE-ONLY |
| 5 | VOICE block on CHAR card | 0 | 0 (stacks carry LOOK only) | §3/F-15, AUDIT §5A | GUIDE-ONLY |
| 6 | UNIT LOAD line | 0 | partial precursor only (informal "(25w)" headers in 4/10 VEHICLES files) | F-25, AUDIT §5E.8 | GUIDE-ONLY |
| 7 | Hear-before-it-moves / Pass 3.5 sign-off | 0 | 0 (the writers-room method still runs Pass 1–7, no 3.5) | F-26, AUDIT F12 | GUIDE-ONLY |
| 8 | SEQUENCE GATE sign-off | 0 | 0 | AUDIT F8/§5B.5 | GUIDE-ONLY |
| 9 | Drift-taxonomy class field in GATE_LOG | 0 (no GATE_LOG template exists) | 0 as a field; drift narrated as free prose in all 20 logs | AUDIT F11/§5F | GUIDE-ONLY |
| 10 | Colon-form speech block, no quotes | 0 | 0 compliant — practice contradicts it: 52× `NAME says: "…"` in VEHICLES, 32× `NAME: "…"` in SCRIPTs, unison entries persist | §3/§7, AUDIT §5E.7 | GUIDE-ONLY |

**0 of 10.** And the structural fact underneath: **no standalone
production brief template existed anywhere in the repo** — the
wider find returns eight brief/template files, all MV/research/
sprint artifacts, zero under `new-era/`. Both law documents even
spelled out their own "template consequences" (F-22, F-24, F-25,
F-26 each name the field the vehicle template "gains"); nobody
built the template. The adoption repeated, within hours, the exact
failure it was adopted to fix.

Fairness caveat (from VERIFICATION.md): all production documents
predate adoption day, so V=0 is partly timing. The damning part is
timing-independent: T=0 — no template was created, the method was
not amended, no skill was touched. One contrast proves the system
*can* land a gate when it is an artifact: the master ear test,
which exists as verdict files, landed (4 EAR_TEST_VERDICT.md).
Gates that are files exist; gates that are paragraphs don't.

**The applied fix for this verdict is §5 below** — a template in
which every field is a greppable label, with a field-presence
checklist (§6 of the template) that is itself the gate.

---

## 2. Angle 1 — Cast consistency: three legs are not enough

Full text: `ANGLE1.md` (602 lines, 32 URLs).

**Identity.** The field has moved from re-describing characters to
*stored, bound assets*: Veo 3.1 Ingredients (≤3 reference images,
VERIFIED), Kling Elements (1 main + 3 supplementary refs,
VERIFIED), Runway References (≤3 named refs, INFERRED), and trained
identity at series scale (LoRA recipes of 15–40 curated images;
Higgsfield Soul ID from 20–80 photos, VERIFIED parameters).
Practitioner rules converge with ours: one canonical reference
reused byte-identically, never chain a drifted frame forward,
still-first then animate. The humbling number: the ConsisID / Face
Consistency Benchmark puts even state-of-the-art between-clip
ArcFace similarity at ~0.54–0.59 (VERIFIED) — a reference is not a
lock; the correct posture is generate → measure → re-roll.

**Voice — the weakest leg, structurally.** Only three real
architectures exist: (A) a pinned TTS voice ID; (B) voice bound
into the video model's character asset (Kling Omni: a 3–8s
character video or 5–30s clean speech file per element, VERIFIED);
(C) native speech from text — which re-rolls per shot, confirmed
by practitioners and a Nov 2026 listening test. Pass 1's VOICE
block is correct for route (A) and a **dead letter on the native
route**: the enrollment sample is never heard by the model, and
the "pinned engine" pins the wrong engine. Fix adopted: a
mandatory per-show `VOICE_ROUTE` declaration, route-specific card
fields, the spec text demoted to an honestly-labelled fallback,
and `NATIVE_TEXT_ONLY` invalid for recurring speakers without a
waiver.

**Persona — not theatre, but weak medicine.** Structured traits
beat unstructured prompting (CharacterGPT, NAACL 2025, VERIFIED),
yet persona instructions measurably drift within ~8 rounds (Li et
al. 2024, VERIFIED), trait adjectives often fail to change
behaviour, and models converge toward the conversation's style.
Persona acts on the *writing* model (hence per-unit re-injection)
and reaches the *video* model only through an explicit per-unit
translation into renderable posture/gesture/gaze/tempo. The card
shape changes accordingly: trait → observable behaviour + example
line + NEVER_DOES/NEVER_SAYS negatives.

**The attack lands: add three legs.** STATE (named wardrobe
states; per-episode open/close state covering props, knowledge,
relationships — every episodic guide found separates immutable
identity from versioned state), PERFORMANCE (a motion/gesture
signature in the voice-formula style; face-only identity ignores
body and gait), and MEASUREMENT as a gate leg (face + speaker
embedding tripwires feeding the ear test — precisely the detector
E2 lacked). Negative-reference sets have no generation-side
support anywhere in the field; they are adopted gate-side only,
as a REJECT_BANK, graded LEAD (our synthesis — pilot before law).

## 3. Angle 2 — Speech reliability: the cap was ~40–50% too loose

Full text: `ANGLE2.md` (656 lines, 25 sources).

**The cap.** Every independent published budget converges at
16–20 words comfortable / ~25 maximum per 10 seconds for *one*
speaker (ToonlyAI, Pippit, Prompt-Helper, Kling 4.0 docs). F-25's
~30 words is 180 wpm sustained — reading-aloud speed with zero
lead-in, pause, or tail. **Adopted: 1 speaker target 14–17 words,
hard cap 20; 2 speakers target 14–16 total, hard cap 18, ≤9
words/turn, ≤2 turns — adding a speaker reduces the total budget
(the turn gap costs time), it never leaves it unchanged.**

**The default.** ≤2 speakers per generation is right as a ceiling
(Kling 2.6 reviews: 3+ speakers = attribution confusion) but wrong
as a default. The episodic field's centre is **Camp B — one
speaker per clip, cut together** (OpenMicroDrama, ClickPop,
Skywork, Veo micro-drama guidance); native multi-speaker (Camp A,
where WuBuTV currently sits) survives as a budgeted exception;
silent+TTS+lip-sync (C) and audio-first/prelay (D) own the exact
and multi-speaker cases. The template now declares a camp per
unit, defaulting to B.

**The syntax.** Colon-form/no-quotes is *supported but
model-specific*: Google's current Cloud best practice (updated
10 Nov 2026) explicitly recommends `A woman says: My name is
Clara.` and marks quotes not recommended (quote-triggered
burned-in garbled subtitles are documented, MIT Tech Review, Jul
2025) — while Seedance and Kling *require* quotes as their spoken
track. The rule survives for our generator and moves under a
`MODEL_SYNTAX` field so it flips deliberately, per model, instead
of posing as a law of nature.

**The span law is real but mis-named: it is a Container Law.** A
generation is a fixed-duration container the model fills — by slow
delivery, by silence padding, and, documented verbatim in Kling
4.0 API docs, by *padding a short line with invented words*. That
single mechanism explains round 6 (two cap-compliant halves
delivering 9.7s + 9.0s), why directed "compression" never worked
(no source anywhere claims it does), and why the ≤1-spoken-half
corollary stands. Composites are now budgeted in generation
*seconds*, not words.

**The biggest missing practice** is per-line duration budgeting
from *measured* audio: prelay/audio-first pipelines time the track
before generating (a published case cut attempts from 9 to 2;
performed dialogue runs ~+30% over a silent read). The audit block
therefore carries `measured_sec` as the authority, an explicit
silence budget (lead 0.3–0.5s / pause 0.45–0.55s / turn gap ≥0.5s /
tail 0.5–1.0s), and an implied-rate check (words ÷ speech window:
PASS ≤2.0 wps, FAIL >2.5). Also new: time-slotted turns in Camp A
(the only published mitigation plausibly aimed at last-speaker
starvation), non-speaker mouth-closed + moving-hold lines, and
attempt-log fields (`speaker_order`, `dropped_speaker`,
`invented_words`, `span_sec`) — because last-speaker starvation
and merged-block effects have *no* external source; our own logs
are the best evidence, and now they will be collected as data.

## 4. Angle 3 — QC: two gates were half-theatre; one gate was missing

Full text: `ANGLE3.md` (315 lines, 50 URLs).

**Sequence Gate — our strongest gate, missing a clock.** Published
best practice matches the contact-sheet-as-set read; the better
method found adds an **animatic**: panels at real durations
against the dialogue timing track, watched once at speed, with
silent and audio-only reads. Only the timed pass catches
spoken-load and pacing failures before generation money moves.
Adopted as a co-blocking Animatic Gate.

**No automated drift score is gate-worthy.** ArcFace-style scoring
(FCB/VBench-2.0 method) is triage-only: verification thresholds
scatter 0.42–0.88 by dataset, hidden faces are silently skipped,
and *no benchmark exists for stylised/cartoon characters*. Worse,
CLIP/DINO consistency metrics preferred a frozen photo to a real
clip **25/25** in a Nov 2026 replication — gating on them rewards
exactly the halted-photo takes our motion law bans. And
pHash/PDQ/vPDQ/TMK/SSCD **do not fit drift scoring at all** (Meta's
own docs: syntactic copy detection, "same 2D source" by
definition) — their only legitimate use is verifying claimed
raster identity (chained frames, loops, dedup), which retires a
standing assumption in our finder research that F-31/F-28 might
grow into drift tools. Adopted: embedding/DINO scores as
flag-columns beside a dynamic-degree column, thresholds marked ◊
as local calibrations, and a calibration ledger that forces every
flag to eventually prove it catches something or be deleted.

**The ear test as designed was half-theatre.** "Two Whisper passes
concur" tests self-agreement, not truth: hallucination is
systematic over silence and music (Careless Whisper, FAccT 2024:
1.4% of 13,140 segments hallucinated, 38% of them harmful;
confident hallucinations defeat `no_speech_threshold`). The fix
stack is adopted wholesale: VAD-before-decode,
`condition_on_previous_text=False`, pass 2 from a *different
architecture* (Parakeet TDT as a disagreement generator — its
hallucination resistance is LEAD, no independent study found, so
it generates disagreements, never verdicts), and mechanical
word-timestamp checks — including **words-in-VAD-silence**, which
would have caught our hallucinated past-end-of-file tail
automatically. Transcript-reading alone is insufficient, a fact
our own history already proved (lines that matched ASR and were
nonsense when spoken).

**Diarization cannot carry the Voice Check.** pyannote community-1
DER runs 11.2% (VoxConverse) to 44.6–46.8% (AVA-AVD/Ego4D);
assume 20–45% on generated voices over music until measured
on-domain. The check is split into three separately-logged
instruments — diarization turns + the human-correction count (our
own DER proxy, logged every episode), ECAPA-TDNN embedding vs the
enrolled voice, and an honest outcome vocabulary that includes
`PASS-EAR-ONLY (too short/noisy for embedding)` — replacing both
the bare PASS (which hides which instrument judged) and the
already-banned "not assessed."

**The single highest-value addition: Gate (f), THE COLD RUN** —
one blind, timed, uninterrupted full-master watch+listen by a
non-maker, scored as a script diff; any missing, wrong, or extra
line blocks ship and re-runs on the repaired master. It is the
only check performed on the artefact the viewer actually
receives, and it subsumes every historical escapee class. It is
now the template's final ship blocker.

---

## 5. The applied fix — E3 PRODUCTION BRIEF TEMPLATE v2

`~/workspace/wubutv-network/new-era/E3_PRODUCTION_BRIEF_TEMPLATE.md`
(the verification's recommended home; no E3 template existed
anywhere before this pass). It extends/supersedes the de facto
E2 per-episode file pattern (SCRIPT + VEHICLES + REFERENCE_STACK +
work/GATE_LOG) and carries:

- **§0 header** — `VOICE_ROUTE`, `MODEL_SYNTAX`, `CONTINUITY_OWNER`,
  CAST_LOG reproducibility record.
- **§1 cast cards** — LOOK_PACK with named slots, `CANONICAL_FACE_REF`
  + hash + re-anchor rule, route-specific VOICE fields (pinned TTS
  IDs/settings/enrollment, or per-unit `VOICE_REF_CLIP` +
  bound-tone rule; spec text demoted to labelled fallback),
  behaviour-shaped PERSONA with negatives, `MOTION_SIGNATURE`,
  named `WARDROBE_STATES`, per-episode STATE_OPEN/STATE_CLOSE.
- **§2 room sign-offs** — Pass 3.5 hear-before-it-moves (reader
  named, stumbles logged) and Pass 4 load audit, as signature
  fields, not checklist prose.
- **§3 panel gates** — Sequence Gate (now with blind first look,
  odd-one-out + class, story-in-one-sentence) **and the new
  Animatic Gate**, both blocking, both signed.
- **§4 per-unit vehicle skeleton** — the full spoken-load audit
  block (camp, tightened caps, `measured_sec`, silence budget,
  implied-rate verdict, `span_cost_sec`), PREV END STATE quote,
  REFERENCE PRIORITY + positive overrides, `REFS_BOUND` /
  `PRIMARY_BOUND_CHARACTER`, `STATE_ASSERT`, per-unit persona
  injection + `PERSONA_TRANSLATION`, OBJECTIVE/OBSTACLE/TACTICS,
  EYE TASK, four-subfield END STATE, model-syntax speech block,
  blank-surface TEXT RULE with PIL plates as default.
- **§5 GATE_LOG sections** — four-class drift rows with kill rule
  and first/mid/last sampling, triage-only machine flags, the
  attempt log (order-effect dataset), tail-drift verdict, the
  three-instrument voice check, per-joint log with verdict enums,
  the rebuilt master transcription protocol + mechanical diff,
  ear-test sign-off, **Gate (f) Cold Run**, calibration ledger,
  REJECT_BANK.
- **§6 field-presence checklist** — the grep contract: the list of
  labels a gate checks. An amendment that adds a rule without
  adding its label here "does not exist" — the anti-decay clause
  this whole pass exists to install.
- **§7 amendment register** — 15 numbered changes vs the Pass 1
  protocol, each with its reason and angle (also summarized in §6
  below).

## 6. What changed in the protocol, and why (summary)

1. **F-25 tightened ~40–50%** (30 → hard 20 for one speaker; 18
   total for two) — published budgets converge at 16–20 words/10s;
   30 words leaves no room for the silence architecture every real
   take contains. (Angle 2)
2. **Span law → Container Law** — the mechanism (the model fills a
   fixed-duration container, up to inventing words) is documented
   externally; composites are budgeted in seconds. (Angle 2)
3. **Camps A/B/C/D; Camp B is the default** — the field's episodic
   centre is one speaker per clip; native multi-speaker becomes a
   noted, reduced-budget exception. (Angle 2)
4. **Speech syntax is a `MODEL_SYNTAX` field** — colon/no-quotes
   kept for our generator, quoted rendering specified for
   quote-models; the rule was model-specific all along. (Angle 2)
5. **`measured_sec` replaces word count as the load authority**,
   with silence budget + implied-rate PASS/FAIL. (Angle 2)
6. **`VOICE_ROUTE` is mandatory**; the text spec is demoted to
   fallback; enrollment becomes an input, not a filing-cabinet
   artifact. (Angle 1)
7. **STATE and PERFORMANCE legs added** to the character stack;
   persona reshaped to behaviour + example + negatives, injected
   per unit and translated per unit. (Angle 1)
8. **MEASUREMENT added as triage, never verdict** — with a
   calibration ledger so thresholds become ours or get deleted.
   (Angles 1+3)
9. **Animatic Gate** beside the Sequence Gate. (Angle 3)
10. **Ear test rebuilt** (VAD, no previous-text conditioning,
    cross-architecture pass 2, words-in-silence check). (Angle 3)
11. **Voice check split into three instruments** with an honest
    outcome vocabulary. (Angle 3)
12. **Gate (f) Cold Run** — the final ship blocker. (Angle 3)
13. **Copy-detection tools confined to raster identity** — vPDQ/
    SSCD are not drift instruments. (Angle 3)
14. **Vocabulary: bound vs carried** replaces "locked" for
    anything text-only. (Angle 1)

## 7. Ranked remaining gaps

1. **No E3 room has opened yet, so the template is unproven in
   production.** Its first real test is the first E3 episode
   (HOLD ON / ONE SHORT first per the standing order). The
   field-presence checklist must be run by someone other than the
   brief's author, or §6 becomes the next ritual.
2. **The native voice route problem is declared, not solved.**
   If our generator stays `NATIVE_TEXT_ONLY` for recurring
   speakers, voice consistency rests on spec text + ear — the
   weakest architecture in Angle 1. The real fix (pinned TTS or
   audio-reference binding) is a pipeline decision above this
   template's pay grade; the waiver field at least makes the
   choice visible and owned.
3. **No labelled calibration set exists.** Every ◊ threshold
   (ArcFace bands, ECAPA bands, diarization correction rate) is
   an imported starting guess. Building the per-character
   approved-vs-drifted labelled set from E1/E2 takes is cheap,
   unglamorous, and is the difference between measurement and
   theatre by episode 5.
4. **The resume/snapshot chaining test is still unrun** (Pass 1
   F7). The template forbids load-bearing on it, but the one-call
   lab test remains the standing cheapest experiment in the
   system.
5. **REJECT_BANK is LEAD-grade.** It is in the template as a
   pilot, explicitly not law; it needs one show's worth of
   evidence before it hardens.
6. **Camp B/C/D capacity is unbuilt.** The template can now
   *declare* one-speaker-per-clip, silent+TTS+lip-sync, or
   audio-first units, but the assembly and lip-sync workflow for
   C/D does not exist in our pipeline yet. Declaring a camp we
   cannot execute would be the next guide-only failure — rooms
   should treat C/D as unavailable until a workflow lands.
7. **Order-effect hypotheses remain open by design.** Speaker
   starvation and merged-block effects now have logging fields;
   they need a season of attempt logs before anyone rules on
   them again.

## 8. Honest limits of this pass

- Three vendor help-centre routes (Runway, ElevenLabs) resolved
  to secondary reviews in the fetcher; those claims are graded
  INFERRED in ANGLE1.md, not upgraded.
- No vendor publishes dialogue WER or speaker-attribution rates;
  blog percentages circulating for them are graded LEAD in
  ANGLE2.md and none were used.
- Parakeet's hallucination resistance is architectural reasoning +
  vendor-adjacent claims (LEAD); it is used in the protocol as a
  disagreement generator only.
- No benchmark exists for face-embedding drift on stylised/cartoon
  characters; all face thresholds are human-photo calibrations
  and are marked as such in the template.
- No published workflow found combines all of: set-level panel
  gate + animatic + cross-architecture master ear test + per-class
  drift log + cold run. The combination is ahead of the published
  field — which also means it has no external validation as a
  combination. Its validation set is our own ship/fail history,
  starting with E3 episode 1.

*Deliverables: this REPORT.md · ANGLE1.md · ANGLE2.md · ANGLE3.md ·
VERIFICATION.md · SOURCES.md · the template at
`wubutv-network/new-era/E3_PRODUCTION_BRIEF_TEMPLATE.md`, mirrored
into `wubutv-network/research/recursive-improvement-20261118-pass2/`.*
