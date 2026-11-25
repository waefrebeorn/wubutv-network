# SLERM — THE VIDEO METHOD

*The reusable playbook for SLERMing a video format, written 2026-11-18 under user order msg 635: "slerm can mean more than code — we are slerming them."*

*SLERM (the user's standing definition, from the code work): take someone's full work and make your own version FROM SCRATCH — a ground-up reimplementation, not a fork, not a copy. This playbook extends the method from software to formats. It is written so a future agent can run it on a new target format without re-deriving it: the worked example throughout is the 2026-11-18 run (fruit-gen factories + Cantina + clipcraft7 → THE_SAUCE.md → RETOOL_PLAN.md), but no step depends on that example.*

---

## 0. The analogy — why the code method transfers

| Code SLERM | Video-format SLERM |
|---|---|
| Read the dependency's *behavior* (what it computes, its edge cases) | Read the format's *artifacts* (episodes, poster frames, titles, cadence) — what it does to a viewer, beat by beat |
| Write a spec of the behavior, in your own words | Write a mechanics spec (THE SAUCE for that target) — structure, economy, devices, cadence, hooks — in your own words |
| Discard the source code entirely | Discard the IP surface entirely (characters, names, looks, text) — quarantine list, written down |
| Reimplement from the spec, in your stack | Rebuild from the spec, with your cast, world, tools, and law |
| Test against the original's *behavior* (does it pass the same cases?) | Verify by cold-watch gates (does it produce the same *effects* — legibility, retention, the hanger pulling — on a cold viewer?) |
| Ship your implementation; the dependency is gone | Ship your show; the target is a citation in a research note, not a credit on the work |

The discipline that makes both work: **you may study the original as closely as you like; you may not carry any of it across except the behavior, restated in your own words.**

---

## 1. Step 0 — Pick the target; name the prize

- A SLERM target is a *format that demonstrably works* — evidenced by audience numbers, a clone ecology forming around it, or a platform productizing it. If nobody is copying it and nobody is watching it, there is no prize.
- **Name the prize in one sentence before studying**: the mechanic you believe is doing the work ("the worn countdown is the plot," "the vault triples the value of every scene"). The study tests that sentence; it does not go shopping.
- Record the IP boundary up front (our standing ruling, msg 486): what ships is our cosplay/parody original. The target's characters, names, looks, titles, and text are never inputs to production — they are evidence in a study.

## 2. Step 1 — Study the artifacts, not the marketing

- **Primary evidence is the work itself**: episodes/posts (lengths, cadence, captions or their absence), poster frames read directly, title grammar catalogued, platform split (where the audience is vs where the archive is). In the worked example, the decisive facts were all artifact-level: parts of 79–257s, two 6.5M-view posts with *empty* captions, a compilation every 2–3 days.
- **Workflow disclosures are usually absent — treat that as normal.** The genre's biggest creator publishes no workflow anywhere. Reconstruct the pipeline from the artifact fingerprint instead: resolution variance across posts (per-scene generation, loose assembly), composed stills with clean in-image text (still-first, image-to-video), the same scenes appearing in three products (triple monetization). Grade every claim: VERIFIED (read directly) / INFERRED (fingerprint) / LEAD (single secondary source). Never let a LEAD carry a design decision.
- **Study the clone ecology, not just the originator.** When sixteen products converge on one checklist, the checklist is the genre's de-facto spec — and convergence is stronger evidence than any single creator's habits. Map who copied whom from *shared artifacts* (identical copy, shared feature checklists), not vibes.
- **Read the tools' published doctrine.** Factories print their method in guides and FAQs (line economy, beat map, review gates, drift taxonomies). It is the cheapest research in the space: the method is given away; only the machinery is sold.
- Deliverable of this step: a study report (per target) + sources file, in `research_notes/`, with honest negatives recorded (what could not be read, and why).

## 3. Step 2 — Extract the mechanics into a spec (the sauce document)

Write the target's recipe as **pure mechanics**, each claim cited to a study section. The spec has eight shelves; a target that can't fill a shelf gets an explicit "absent" note, which is itself a finding:

1. **Episode structure** — the beat spine; where the reveal sits; what the evidence is made of; how escalation is itemized.
2. **Line economy** — words per line, speakers per unit, the atomic unit's shape; the dialogue format the models are fed.
3. **Serialization** — how parts chain (in-platform mechanics, not intentions); hanger discipline; numbering and title patterns; recap form.
4. **The worn stake** — the readable state on a body/board that the plot bargains against; how it is stated and challenged aloud.
5. **Funnel / vault architecture** — how the same scenes are used more than once; what points at what; the compilation lag and shape.
6. **Cadence** — posts per day, compilations per week, planning horizon (how many episodes are pre-written).
7. **Engagement hooks** — what the frame does alone; what the title does alone; what the viewer is asked to do, and what their doing changes.
8. **The consistency stack** — how the cast persists: look, voice, persona; the drift failure classes and their fixes.

Plus a ninth section, always: **the gap list** — what the target and its whole field do *not* do. The gaps are where your version wins; a SLERM that only matches the target has wasted the study.

**The noun test**: the finished spec must be statable without any of the target's proper nouns — no character names, no show titles, no branded terms. If a mechanic can't be said without their nouns, it isn't extracted yet; it's still surface. (Worked example: "a lifespan countdown worn on the body that eating shortens" passes; the target's device name and look do not appear.)

## 4. Step 3 — The discard pass (quarantine the surface)

Before any rebuilding, write the quarantine list explicitly:

- **Characters** — names, species/persona concepts as *designed* (a genre's broad archetypes are folk material; a specific cast is surface).
- **Looks** — art direction, signature props as designed objects, costume identifiers.
- **Titles and text** — title strings, catchphrases, any written line.
- **World IP** — named places, institutions, lore terms.

Rules: nothing on the list enters a bible, a prompt, a vehicle, or a title — even "as a homage," even renamed. Renaming is not discarding; the test is whether a viewer who knows the target would say "that's *their* X with a new label." If yes, it goes back.

What legitimately crosses: mechanics (Step 2), folk skeletons (public-domain story shapes — the shape is borrowed, the telling is ours), and *grammatical slots* (a title grammar's slots, filled with our nouns).

## 5. Step 4 — Rebuild from scratch, with our assets and our law

- **Start from our cast cards, not from their cast.** Each rebuilt show's characters are written Identity / Personality / Backstory from our world's materials first; the spec's mechanics are then *assigned* to them (who holds the stake, who delivers the authority reveal). If a mechanic has no natural holder in our cast, the mechanic is adapted or dropped — the cast is never bent into a reskin of theirs.
- **Write the retool as a bible amendment, not a vibe**: per show — mechanics absorbed (cited to the spec), what changes vs the bible (section-level), what stays ours, and the first episode's unit-by-unit skeleton under the retooled format (skeleton only; dialogue belongs to the writers room).
- **Our law governs the rebuild, not the target's constraints.** Their format's limits (9:16, talking heads, 60-second ceilings, credit metering) are *their* pipeline's shape, not the mechanic's. Check each absorbed mechanic against standing law — Gate E, BLAM, the ear-test, the spoken-load cap, base lore — and where a mechanic fights a show's premise or the law, **say so plainly in the retool and refuse that layer** (worked example: THE LAST SEAT absorbs the serialization/stake/vault layer and refuses the line layer, on the record). A forced fit is a failed SLERM: it means the spec was surface after all.
- **Design the differentiators in.** The gap list (Step 2, shelf 9) is applied at bible stage: serialization device, vault plan, worn stake, poster-frame discipline — named per show, or the bible is a factory-format bible and does not open (F-28 completeness check).

## 6. Step 5 — Verify by cold-watch gates

A code SLERM is verified against the original's behavior. A format SLERM is verified against the original's *effects*, on cold viewers, with our own gates — never by resemblance:

1. **Gate E cold read** — from the premise alone, a cold viewer states who wants what, what blocks them, what changes — no lore terms, none of theirs either.
2. **The EMPTY CAPTION test** — the poster frame pitches the episode alone, zero copy. (The target's own evidence sets this bar: its biggest posts carried no caption at all.)
3. **Hear-before-it-moves** — the locked script read aloud cold before any vehicle is written; stumbles return to dialogue pass.
4. **The ear-test on the finished master** — the cold listen; no paper gate substitutes. This is the gate the entire target field lacks — it is the verification layer that makes our version *better*, not just ours.
5. **Cold-join test** — a viewer joining at any unit is oriented within ten seconds (worn continuity + stated wants do this; check it, don't assume it).
6. **Hanger-ledger audit** — every hanger booked with a due episode; the chain pays on schedule.
7. **The reskin check** — the final, SLERM-specific gate: show the episode to the quarantine list. If any item on the list is recognizable in the episode — a character, a look, a device-as-designed, a title — the build fails and returns to Step 4, no matter how well it scored elsewhere.

## 7. Step 6 — Bank it, so the next SLERM is cheaper

- The study reports, the sauce spec, the retool plan, and this method live in `research_notes/` and are mirrored into the network repo (`wubutv-network/research/`) — text only, committed. An uncommitted SLERM is a rumor.
- The retool is **done when a second show can be retooled from the documents alone** — when a future agent, given a new target and this playbook, needs no conversation with the original researcher. If they would, the spec is missing a shelf; write it.
- Record the standing directive in memory: SLERM covers formats now, not just code (msg 635). Future "study this creator/format" orders default to this playbook's shape: study → sauce → discard → retool → gates.

## 8. Failure modes (each observed or named in the worked example)

- **Copying the surface.** The clone ecology's own bottom layer does this (a landing page copied near-verbatim, store shells sharing description text). It produces a worse copy and an IP problem. The discard pass exists because this is the default failure.
- **Mistaking the tool for the recipe.** The factories are wrappers over a public recipe the tutorial layer gives away free. SLERM the *recipe*; never adopt the app (its constraints become yours).
- **Importing their constraints as if they were mechanics.** 9:16 talking-head monoculture is a metering artifact, not a genre law. Check every "rule" of the target for whether it serves the viewer or the vendor.
- **Forcing the fit.** A show whose premise fights a layer of the sauce must refuse that layer on the record. The honest flag is a deliverable, not an embarrassment.
- **Skipping the gates because the study felt conclusive.** The study proves the *target* works. Only the cold-watch gates prove *ours* does — the ear-test exists because our paper gates once passed a master the user rejected on first listen.
- **Letting a LEAD carry a decision.** Unverifiable claims (view counts from marketing pages, unsourced statistics in guides) are recorded as claims. Design decisions cite VERIFIED and INFERRED evidence only.

---

*End of SLERM_VIDEO_METHOD.md. Worked example: THE_SAUCE.md + RETOOL_PLAN.md, same directory. Standing method from 2026-11-18: any dependency — code or format — that matters gets re-created from scratch rather than worked around or copied.*
