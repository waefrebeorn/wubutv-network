# RECURSIVE VERIFICATION — Pass 2 (2026-11-18)

**Question:** Did the 2026-11-18 adoption — devil's-advocate AUDIT.md §5
"Revised Reference + Prompt Design Protocol" (adopted as E3 law) and
TASTE_GUIDE §8 ratification (F-22 END STATE pin, F-24 REFERENCE
PRIORITY, F-23 objective/eye task, F-25 unit load cap, F-26
hear-before-it-moves) — land in **working artifacts**, or only in
guide documents?

**Method:** read-only grep over the real system. Classification per hit:

- **(T)** fill-in template field in a reusable template / brief skeleton
- **(V)** present in an actual episode vehicle / production doc
- **(G)** prose in a guide / law document only

**Corpus searched:**

| Tree | Files |
|---|---|
| `~/workspace/wubutv-network/new-era/` (morph bibles, episodes/, morph-episodes/ E1+E2, pilots/, research/) | 217 `.md` — incl. 10 `VEHICLES.md`, 20 `GATE_LOG.md` |
| `~/workspace/wubutv-network/research/` (incl. `WRITERS_ROOM_METHOD_2026-11-15.md`, `devils-advocate-audit-20261118/AUDIT.md`, `slerm-their-shows-20261118/`) | all `.md` |
| `~/workspace/custom-skills/` | all `.md` |
| `~/workspace/wubutv-network/` (whole repo) | `find` for `*brief*` / `*template*` filenames |

**Timing caveat, stated once and applied throughout:** every production
artifact in the corpus is pilot / E1 / E2 era (produced 2026-11-15→17);
the adoption is dated 2026-11-18 and **no E3 episode directory exists**
(`new-era/` contains only `pilots/`, `episodes/` = pre-morph E2,
`morph-episodes/` = E1+E2; every "E3" string in a working doc is an
Episode-3 *story debt*, e.g. "payoff due E3" in
`new-era/episodes/E2_SHOW-1_the-machine/LEDGER.md`). So "(V) = 0" alone
would be partly excusable. What is **not** excusable — and is the actual
finding — is **(T) = 0 everywhere**: no template was created, the
writers-room method was not amended, and no skill was updated, even
though both law documents spell out the template changes in so many
words (TASTE_GUIDE: "Template consequence: the vehicle template gains a
mandatory END STATE block…"; AUDIT §5 is written as fill-in fields with
checkboxes and owners). This is the Pass-1 failure repeating exactly:
law in guides, nothing in the machinery the work is actually made from.

---

## Verdict table

| # | Adopted field | T | V | G | Verdict |
|---|---|---|---|---|---|
| 1 | END STATE block | 0 | 0 as a block (joint prose only) | TASTE F-22; AUDIT §5C | **GUIDE-ONLY** |
| 2 | REFERENCE PRIORITY block | 0 | 0 | TASTE F-24; AUDIT §5D | **GUIDE-ONLY** |
| 3 | OBJECTIVE / OBSTACLE / TACTICS fields | 0 | 0 as fields (Gate-E analysis prose only) | TASTE F-23; AUDIT F9/§5E.5 | **GUIDE-ONLY** |
| 4 | EYE TASK field | 0 | 0 | TASTE F-23 (1 line); AUDIT F9/§5E.5 | **GUIDE-ONLY** |
| 5 | VOICE block on CHAR card (age·accent·pitch·pace·texture + enrollment + engine) | 0 | 0 | TASTE §3/T-6 + F-15; AUDIT §5A.2 | **GUIDE-ONLY** |
| 6 | UNIT LOAD line (words/speakers vs cap) | 0 | 0 as the line; informal word-count headers in 4/10 VEHICLES | TASTE F-25; AUDIT §5E.8 | **GUIDE-ONLY** (partial precursor in V) |
| 7 | Hear-before-it-moves / Pass 3.5 sign-off | 0 | 0 | TASTE F-26; AUDIT F12/§5F | **GUIDE-ONLY** |
| 8 | SEQUENCE GATE sign-off | 0 | 0 | AUDIT F8/§5B.5/§5F only | **GUIDE-ONLY** |
| 9 | Drift-taxonomy class field (IDENTITY/WARDROBE/PROP/MOTION) in GATE_LOG | 0 (no GATE_LOG template exists) | 0 as a field; drift narrated as free prose in all 20 logs | AUDIT F11/§5F | **GUIDE-ONLY** |
| 10 | Colon-form speech block (`NAME (trait, delivery): line`, no quotation marks) | 0 | 0 in compliant form; dominant practice is the opposite convention | TASTE §3/§7; AUDIT §5E.7 | **GUIDE-ONLY; practice contradicts it** |

**Score: 0 of 10 fields exist as (T). 0 of 10 exist in compliant (V)
form. 10 of 10 exist as (G).**

---

## Evidence per field

Counts are matching **lines** from `grep -r -i '<pattern>' --include='*.md' <tree>`
unless noted. Short paths below are relative to `~/workspace/wubutv-network/`
(`NE/` = `new-era/`, `RES/` = `research/`, `CS/` = `~/workspace/custom-skills/`).

### 1. END STATE block — GUIDE-ONLY

Commands:

```
grep -r -i -c 'END STATE' --include='*.md' NE/            → 11 lines total
grep -r -i 'END STATE' --include='VEHICLES.md' NE/        → 0
grep -r -i 'END STATE' --include='GATE_LOG.md' NE/        → 2 (prose, see below)
```

All 11 new-era hits:

- **(G)** `NE/research/TASTE_GUIDE_2026-11-17.md:927,930,939` — F-22 itself:
  "Every unit's vehicle carries a written **END STATE** block… *Template
  consequence:* the vehicle template gains a mandatory END STATE block".
- **(G-adjacent)** `NE/research/E2_SPEECH_AND_STORY_ADDENDUM_2026-11-16.md:78`
  — episode-level before/after prose ("end state equals the start state…"),
  not a per-unit vehicle block.
- **Working-doc hits are episode-outcome prose, not the pin:** Gate-E verdicts
  (`morph-episodes/E2_on-air/GATE_E.md:122`, `E2_hold-on/GATE_E.md:107`,
  `E2_the-night-list/GATE_E_MASTER2.md:88`, `E2_hold-on/work/GATE_E_F9_REPAIR_VERDICT.md:10`),
  a BOARD premise line (`E2_the-last-seat/BOARD.md:28`), and the only two
  GATE_LOG hits — joint-outcome prose inside take rows:
  `E2_the-last-seat/work/GATE_LOG.md:47` "…J4 end state missed" and `:50`
  "…(J5 end state broken at the exact payoff joint)".

The working system's real continuity device is the older one: SCRIPT.md
joint prose — `E2_on-air/SCRIPT.md:111,244,281,328,370`
("**Joint U1→U2 (last frame → first frame):** last frame — …") and
`E2_the-last-seat/SCRIPT.md:158,240,293,384` ("**JOINT NOTE J1…:** Last
frame: …") — plus image chaining (`img1 = U1 take last frame` in
VEHICLES). No vehicle opens by quoting a previous END STATE verbatim;
no GATE_LOG verifies a quoted pin against the outgoing last frame.
The F-22 block, as specified, exists in **zero** of 10 VEHICLES.md.

### 2. REFERENCE PRIORITY block — GUIDE-ONLY

```
grep -r -i 'REFERENCE PRIORITY' --include='*.md' NE/      → 3 lines, all one file
grep -r -i 'REFERENCE PRIORITY' --include='VEHICLES.md' NE/ → 0
grep -r -i 'REFERENCE PRIORITY' --include='REFERENCE_STACK.md' NE/ → 0
```

The 3 lines are `NE/research/TASTE_GUIDE_2026-11-17.md:963,964,976`
(F-24, incl. "REFERENCE PRIORITY is a mandatory block in the vehicle
template"). The exact fill-in format —
`IDENTITY: <panel> · GEOMETRY: <panel> · WARDROBE: <panel>` — appears
only in `RES/devils-advocate-audit-20261118/AUDIT.md` (§5D; 7
"REFERENCE PRIORITY" lines in that file). Vehicles do name their
images (`IMAGES: u1_last.png…, PNL-PEAK-U2.png` in
`E2_on-air/VEHICLES.md:56,85,110…`) but no vehicle adjudicates which
reference owns identity vs geometry vs wardrobe, and no known-defect
override block exists anywhere in production docs.

### 3. OBJECTIVE / OBSTACLE / TACTICS fields — GUIDE-ONLY

```
grep -r -i 'OBJECTIVE' --include='*.md' NE/   → 3 lines, all TASTE_GUIDE (F-23: :943,945,958)
grep -r -i 'OBJECTIVE' --include='VEHICLES.md' NE/ → 0
grep -r -i 'OBSTACLE'  --include='*.md' NE/   → 45 lines (see below — not the field)
grep -r -i 'TACTICS'   --include='*.md' NE/   → 5 lines
```

The 45 "obstacle" hits are a **different artefact**: Gate-E cold-join
*story analysis* — e.g. `morph-episodes/E2_on-air/GATE_E.md:76,165,232`,
`E2_the-last-seat/GATE_E.md:66,149,215`, `E2_the-night-list/GATE_E.md:63,66,149…`
("Obstacle — recoverable: UNC does not know how…"), plus DECISION_LOG
retrospectives. That is the room analysing a finished script's want/
obstacle; it is not a per-character field on a CHAR card or a per-scene
`OBJECTIVE: <verb> · OBSTACLE: <…> · TACTICS: <move 1 → move 2>` line in
a vehicle (AUDIT §5E.5 format). "TACTICS" working hits are incidental:
`NE/morph/MORPH_SHOW-5.md:103` ("now as tactics in…") and
`E1_one-short/SCRIPT.md:353` ("Gate C (breakdown tactics/Δ)") — Pass-2
beat-sheet vocabulary, not the F-23 field. Morph bibles
(`NE/morph/MORPH_SHOW-1..5.md`) carry persona **prose** cards
(Identity / Personality / Backstory per rule C1, e.g. MORPH_SHOW-1:145)
— a real precursor for the PERSONA leg — but no OBJECTIVE / OBSTACLE /
TACTICS fields.

### 4. EYE TASK field — GUIDE-ONLY

```
grep -r -i 'EYE TASK' --include='*.md' NE/   → 1 line in the entire tree
grep -r -i 'EYE TASK' --include='*.md' CS/   → 0
```

The single new-era line is the law itself:
`NE/research/TASTE_GUIDE_2026-11-17.md:950` (F-23: "Every close take
carries an explicit **EYE TASK**"). Remaining hits are AUDIT.md
(F9 fix + §5E.5) in the research tree. Zero vehicles, zero gate logs,
zero skills carry an EYE TASK on any close take.

### 5. VOICE block / voice spec on a character card — GUIDE-ONLY

Law text: `TASTE_GUIDE:453-462` ("### The voice spec (lives on the CHAR
panel)… `VOICE: [age range] · [accent/region] · pitch [low/mid/…] ·
… texture …`"), `:81` (spec contents incl. enrollment), `:362,442,745-751`
(enrollment-sample comparison, per-take voice QC); AUDIT §5A.2
("**VOICE block** — … + enrollment sample file path + pinned engine").

Working artifacts:

```
grep -r -i -E 'voice|accent|pitch|pace|texture|enroll' --include='VEHICLES.md' NE/ → 33 lines, all prose
grep -r -i -E 'voice|accent|pitch' --include='REFERENCE_STACK.md' NE/               → 13 lines, all false positives / prose
grep -r -i 'VOICE CHECK' --include='GATE_LOG.md' NE/                               → 0 (the AUDIT §5F per-take line)
```

- REFERENCE_STACKs carry **LOOK blocks only** — verified directly in
  `morph-episodes/E2_hold-on/REFERENCE_STACK.md:44` ("## LOOK blocks
  (verbatim in every vehicle)") + panel inventory at `:101-121`
  (CHAR hero/face panels, md5, no voice data). This matches the audit's
  own census (AUDIT.md:61-63: "`grep -i voice` over all five E2
  REFERENCE_STACKs returns **0 hits in every file**").
- The 33 VEHICLES "voice" hits are scene prose ("An older man's voice
  crackles from the desk phone speaker, voice only…" —
  `E2_on-air/VEHICLES.md:71-72,243-244,367-368…`), never a structured spec.
- Morph bibles' `Voice:` label is a **different field**:
  `MORPH_SHOW-4.md:185,197,230` — "*Voice:* Response Style **Short /
  Medium** (C6)" = dialogue-length register, not age·accent·pitch·pace·
  texture. No enrollment sample path and no pinned engine appear in any
  working doc.
- "Voice check" in working docs = the cover-the-names dialogue test
  (`RES/WRITERS_ROOM_METHOD_2026-11-15.md:338`; `E1_the-night-list/DECISION_LOG.md:198`),
  not the AUDIT's per-take `VOICE CHECK: <char> — match / flag / re-fire`
  against an enrollment sample (0 hits in any GATE_LOG).

### 6. UNIT LOAD line — GUIDE-ONLY (partial precursor in V)

```
grep -r -i 'UNIT LOAD' --include='*.md' NE/   → 0
grep -r -i 'UNIT LOAD' --include='*.md' RES/  → 4 lines, all AUDIT.md (:447, :783 + §5F :790)
grep -r -i 'UNIT LOAD' --include='*.md' CS/   → 0
```

The field name itself was coined by the audit (§5E.8: "**UNIT LOAD
line** at the vehicle's head: words / speakers counted against the
~30-word / ≤2-speaker cap before firing"). TASTE F-25
(`TASTE_GUIDE:980-998`) states the cap and assigns the audit to Pass 4,
but the string never entered a working doc.

What *does* exist in production — the honest partial credit:

- **Informal word counts in unit headers, 4 of 10 VEHICLES.md, 22 header
  lines:** `E1_hold-on/VEHICLES.md:12,28,42,55,68,80` ("## U1 — FULL-TALK
  (18w)…"), `E1_the-night-list/VEHICLES.md:17,27,35,43,51,58` ("(15
  words)…"), `E2_the-night-list/VEHICLES.md:21,29,45,53` ("(27 words)…"),
  `E2_hold-on/VEHICLES.md:16,39,60,81,100,120` ("(25w)…"). Words only —
  **no speaker count, no cap, no pass/fail against F-25** — and absent
  from the other 6 files (e.g. `E2_on-air/VEHICLES.md:28,54,83…` headers
  are bare "## U1 vehicle").
- **The cap as retrospective lesson prose:** `E2_on-air/DECISION_LOG.md:660,684`
  and `E2_on-air/work/GATE_LOG.md:701` ("a 10s unit's spoken load is
  capped at ~30 words / ≤2 speakers…") — recorded *after* the U2
  38-word/4-speaker failure, in the repair log, not printed per vehicle.
- `WRITERS_ROOM_METHOD` Pass 4 does count words — against the **old**
  budgets (2026-11-15 amendments: per-unit ceiling 20, episode 80–90),
  not F-25's per-generation ~30 words / ≤2 speakers.

### 7. Hear-before-it-moves / Pass 3.5 sign-off — GUIDE-ONLY

```
grep -r -i -E 'Pass 3\.5|hear.before' --include='DECISION_LOG.md' --include='BOARD.md' NE/ → 0
grep -r -i 'hear.before' --include='*.md' NE/ → 5 lines, all TASTE_GUIDE (:26, :1021-1042 = F-26)
grep -n -i -E 'Pass 3\.5|hear.before|END STATE|…' RES/WRITERS_ROOM_METHOD_2026-11-15.md → 0
```

F-26 (`TASTE_GUIDE:1021-1042`) defines the gate and its template
consequence verbatim: "the one-page room checklist gains a Pass 3.5
line — *hear-before-it-moves run, stumbles returned*". **No one-page
room checklist file exists** (every "checklist" hit in working docs is
the Pass-5 continuity checklist embedded in DECISION_LOGs), and the
writers-room pipeline still runs Pass 1–7 with **no Pass 3.5**
(`WRITERS_ROOM_METHOD:195-368`). No DECISION_LOG names a cold reader or
logs a single returned stumble.

Contrast that proves the machinery *can* land a gate: the master-stage
ear test (F-13) **did** land as (V) — `EAR_TEST_VERDICT.md` files exist
for `E2_on-air`, `E2_one-short`, `E2_the-last-seat`, `E2_the-night-list`
(work/ dirs). The script-stage twin (F-26 / Pass 3.5) produced no file,
no field, and no sign-off anywhere. (All other "3.5" hits in working
docs are false positives: graphics-method §3.5 references and
timestamps.)

### 8. SEQUENCE GATE sign-off — GUIDE-ONLY

```
grep -r -i 'SEQUENCE GATE' --include='*.md' NE/  → 0
grep -r -i 'SEQUENCE GATE' --include='*.md' RES/ → 3 lines, all AUDIT.md (:581 F8 fix, :734 §5B.5, :790 §5F)
grep -r -i 'SEQUENCE GATE' --include='*.md' CS/  → 0 true hits (slopcannon SKILL.md:906 "lyric-sequence gate" is the MV warp gate — unrelated)
```

No GATE_LOG records a sequence sign-off. Panel QC in the logs is
per-panel prose — e.g. `E2_hold-on/work/GATE_LOG.md:20-31` ("Panel
verification (parent pre-pro, eye-checked this build): PNL-WORLD-…
(✓) · PNL-PEAK-U1-… (✓) · PNL-CHAR-… (✓)") lists panels individually;
there is no contact-sheet set read (cast consistency / relative size /
prop ownership as a set) and no sign-off line before the first video
call. The companion §5B.4 **DESTINATION** panel label is likewise
absent: `grep -r -i 'DESTINATION' --include='*.md' NE/` returns only
story-prose uses ("destination spoken (U4)") and one "destination
composition" phrase (`E2_on-air/VEHICLES.md:9`) — never a panel label.

### 9. Drift-taxonomy class field in GATE_LOG — GUIDE-ONLY

Prescription: AUDIT F11 + §5F — "**DRIFT CHECKLIST (printed in the
GATE_LOG template):** every take's QC classifies drift as IDENTITY /
WARDROBE / PROP / MOTION (or NONE), and a drift note is incomplete
without its class and the class's first fix attempted."

Reality:

```
find NE/ -iname '*template*' -o -iname '*brief*'   → (none — no GATE_LOG template exists)
grep -r -i -E 'IDENTITY|WARDROBE|drift' --include='GATE_LOG.md' NE/ → 50+ lines, all free prose
```

Drift is *everywhere* in the logs — as narrative, in five different
prose styles, exactly as the audit charged: pilots
(`PILOT-2/GATE_LOG.md:43-47` "watcher identity drift… the measured
hue-drift class"; `PILOT-3/GATE_LOG.md:64,130` "Prop identity:
FAIL/PASS"), E2 show logs (`E2_SHOW-4/work/GATE_LOG.md:69` joint table
with free-text "wardrobe: Counter gains a black tie in U2 (nit,
logged)"; `:152` "**Wardrobe/prop nits:**…"), morph logs
(`E2_hold-on/work/GATE_LOG.md:34-38` "tail drifts from the scripted palm
close-up…; the Peach drifts toward a crowned pink-princess design").
The words identity/wardrobe/prop occur constantly; the **four-class
field with a first-fix mapping occurs never** — no column, no
`DRIFT: <class>` line, no class counts ledger in any of the 20
GATE_LOG.md files, and no template file exists for the checklist to be
"printed in".

### 10. Colon-form speech block — GUIDE-ONLY; practice contradicts it

Rule: TASTE §3/§7 (speech block isolated, colon form, "no quotation
marks" — `TASTE_GUIDE:762` and §3) and AUDIT §5E.7: "`NAME (visible
trait, delivery): line` — colon form, **no quotation marks anywhere in
the prompt**; no unison entries".

Practice, counted:

```
grep -r -E 'says:' --include='VEHICLES.md' NE/                 → 52 lines: NAME says: "line"  (quoted)
grep -r -E '^[> ]*[A-Z][A-Z ]+: "' --include='SCRIPT.md' NE/   → 32 lines: NAME: "line"       (quoted)
grep -r -E '\([A-Za-z ]+, [A-Za-z ]+\):' --include='VEHICLES.md' NE/ → 12 lines, of which true speech instances ≈ 5, all still quoted
```

- The dominant vehicle convention is `NAME says: "…"` —
  e.g. `E2_SHOW-2/VEHICLES.md:51-54` (`LAURA says: "The wall started my
  name, Courier."`), `E2_hold-on/VEHICLES.md` speech blocks
  (`JUNE says: "Write us married, or noon loses our room."` etc.).
  Scripts use `NAME: "…"` (`E2_hold-on/SCRIPT.md:84,88,95…`).
- The only colon-*shaped* speech lines are pilot-era and still carry
  quotation marks, violating the rule's second half:
  `pilots/PILOT-3_the-roster/VEHICLES.md:16` `UNC (flat, one word):
  "VASQUEZ."`, `:88-89,103` (`KEEPER (quiet, cliff): "KEEPER."`).
  (The other regex hits are headers: "LOOK (all units, verbatim):",
  "Dialogue (exact words, in order):", "TEXT 1 (both halves,
  unchanged):".)
- Banned unison entries persist in the newest vehicles:
  `E2_hold-on/VEHICLES.md` U2 — "THE PEACH AND THE LIME say together:
  …" (cf. SCRIPT.md:147 "PEACH AND LIME (in unison): …").

Zero vehicles use the adopted format in compliant form.

---

## Cross-cutting checks

**Custom skills — nothing landed there either.**
`grep -r -i -E 'END STATE|REFERENCE PRIORITY|EYE TASK|UNIT LOAD|SEQUENCE GATE|hear.before|Pass 3\.5' --include='*.md' CS/`
(excluding `recovered-skill-notes/`) returns exactly 3 lines, all false
positives in the MV skill `slopcannon/SKILL.md`: `:761` "End state +
reinforcement: 'After the final word the mouth closes…'" (an MV
mouth-close instruction) and `:906` "lyric-sequence gate" (a warp QC
gate). `video-api-mastery` and `visual-mv-forms` contain none of the ten
fields. (The 7 `OBJECTIVE` hits in custom-skills are `objective_id:
skill_improvement` YAML in `recovered-skill-notes/` — unrelated.)

**Writers-room method — unamended.**
`WRITERS_ROOM_METHOD_2026-11-15.md` (742 lines): 0 hits for END STATE,
REFERENCE PRIORITY, EYE TASK, UNIT LOAD, SEQUENCE GATE,
hear-before-it-moves, Pass 3.5, VOICE block, drift taxonomy. Its pass
pipeline is still Pass 1–7 (storyline / breakdown / dialogue / timing /
continuity / critic / lock) with Pass-4 word budgets from the
2026-11-15 amendments — i.e. the room that would run E3 has no slot
where any adopted field could be filled in.

**Where the law actually lives (complete list):**
`NE/research/TASTE_GUIDE_2026-11-17.md` §8 (F-22 :927-941, F-23
:943-961, F-24 :963-978, F-25 :980-1019, F-26 :1021-1042) and §3 voice
spec (:453-486); `RES/devils-advocate-audit-20261118/AUDIT.md` §5
(:696-800) + fixes F1/F4/F8/F9/F11/F12; second-order guide references in
`RES/slerm-their-shows-20261118/THE_SAUCE.md:36` and `RETOOL_PLAN.md:14`
(both prose summaries of the same law). Every one of these is a (G)
document. No working artifact cites F-22…F-26 or AUDIT §5 as a filled
field.

---

## Template existence — direct answer

**No. A standalone E3 production brief template does not exist anywhere
in `~/workspace/wubutv-network`.**

Evidence:

```
find ~/workspace/wubutv-network -type f \( -iname '*brief*' -o -iname '*template*' \) -not -path '*/takes/*'
→ 8 files, none of them a show/E3 production brief:
  musicvideo/MV-18_whats-a-sigma-mom/work/vehicles/TEMPLATE.md   (MV singing-vehicle macros: {SON}/{MOM}/LOOK BLOCK/SINGING CLAUSE — no E3 fields)
  musicvideo/MV-19_confused-npc/work/vehicles/TEMPLATE.md        (same MV template, copied)
  musicvideo/MV-20_laundry-life/work/vehicles/TEMPLATE.md        (same MV template, copied)
  musicvideo/MV-7_the-nobody-man/MV7_OTAKU_REBUILD_BRIEF_2026-11-07.md  (one-off rebuild brief)
  musicvideo/MV-7_the-nobody-man/MV7_REBUILD2_BRIEF_2026-11-07.md       (one-off rebuild brief)
  musicvideo/MV-8_wipe-and-its-still-there/MV8_REBUILD_BRIEF_2026-11-08.md (one-off rebuild brief)
  musicvideo/detection-research/SPRINT_BRIEF_TEMPLATE.md         (C11 sprint-coordinator skeleton — code sprints, not episodes)
  research/CRAFT_POACH_BRIEF_2026-10-27.md                        (research brief)

find ~/workspace/wubutv-network/new-era -type f \( -iname '*brief*' -o -iname '*template*' \)
→ (none)   ← confirms the Pass-1 find, re-verified wider
```

**Closest existing artifacts a v2 template would supersede/extend:**

1. **The de facto per-episode file set** (the real "template" today —
   copied by imitation, never skeletonised):
   `new-era/morph-episodes/E2_<show>/` = `SCRIPT.md` + `VEHICLES.md` +
   `REFERENCE_STACK.md` + `BOARD.md` / `LEDGER.md` / `DECISION_LOG.md` +
   `work/GATE_LOG.md`. Most complete instance:
   `new-era/morph-episodes/E2_hold-on/` (all of the above +
   `VEHICLES_REPAIR.md`, `GFX_CARDS.md`). A v2 template extends *this*
   set: END STATE / REFERENCE PRIORITY / UNIT LOAD / OBJECTIVE-block /
   EYE TASK fields in VEHICLES.md; VOICE + PERSONA blocks in
   REFERENCE_STACK.md's CHAR cards; DRIFT CHECKLIST + SEQUENCE GATE +
   per-joint END-STATE verification in `work/GATE_LOG.md`.
2. **The room-side skeleton:** `research/WRITERS_ROOM_METHOD_2026-11-15.md`
   — needs the Pass 3.5 insertion and F-25 Pass-4 audit to match the law
   it claims to implement.
3. **The spec to encode:** TASTE_GUIDE §8's five "Template consequence"
   sentences + AUDIT §5 A–F (cast-sheet data, panel/sequence gate,
   END STATE chain, reference priority lines, prompt-assembly order,
   pre-flight sign-offs). The spec is complete and field-level; only the
   artefact is missing.

**Where the template should live:**
`~/workspace/wubutv-network/new-era/E3_PRODUCTION_BRIEF_TEMPLATE.md`
— the `new-era/` root, beside the slate-level standing material
(`morph/SLATE.md` pattern), so every E3 room (which will open as
`new-era/morph-episodes/E3_<show>/` on the E1/E2 pattern) copies it as
its first act; the GATE_LOG skeleton belongs in the same file or as
`new-era/E3_GATE_LOG_TEMPLATE.md`. (Second-best home, if it must sit
with the law: `new-era/research/` beside `TASTE_GUIDE_2026-11-17.md` —
but that is precisely the guides-only failure mode this pass is
verifying against.)

---

## Bottom line

The 2026-11-18 adoption is, as of this grep, **declarative only**.
TASTE §8 and AUDIT §5 are unusually implementable law — they name the
field, the format string, the owner, and the checkbox — and still:
no template file was created, the writers-room method gained no
Pass 3.5, no skill was touched, and the newest production docs
(E2, completed 2026-11-17/18) run entirely on the pre-adoption
machinery (LOOK-only stacks, `says: "…"` quoted speech, prose drift,
per-panel QC). Two fields have genuine precursors worth building on
rather than discarding — the VEHICLES word-count header habit (field 6)
and the SCRIPT joint/last-frame prose + Gate-E want/obstacle analysis
(fields 1, 3) — but in adopted form, **0/10 fields reached the work**.
Pass 1's lesson stands unrepaired: until a field exists as a fill-in
line in a template that a room must copy to start an episode, it does
not exist in production.

*Verification run 2026-11-18, read-only; sole write is this file.*
