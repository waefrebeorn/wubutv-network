# DA-25 — TRIPLE DEVIL'S ADVOCATE on Era II, over a 100-search / 7-hop evidence run

**Run:** 2026-10-21, CEO office. **Target of the audit:** our own Era II doctrine
(`notes/CEO_MEMO_NEW_ERA.md`), the research behind it
(`ideas/NEW_ERA_RESEARCH_2026-10-21.md`), the serial (`slate/SERIAL_001_PRODUCE_CLAIM.md`)
and the music plan — i.e. the claims *I* wrote. A DA that only attacks other
people's work is decoration.

## How "100 25 7 25" was operationalised

| Number | What it did |
|---|---|
| **100** | 100 web searches, executed — 25 topics × 4 queries, every result logged |
| **25** | 25 primary sources extracted and read, 471 unique candidate URLs surfaced |
| **7** | 7-hop Kevin Bacon chains: every chain crosses 7 documents/topics, each hop forced to change the claim or die |
| **25** | 25 findings, each one stated as a claim with a verdict and a source |

Evidence is committed next to this file: `ideas/da25_evidence/searches_100.jsonl`
(all 100 queries + 5 results each, verbatim), `source_index.json` (the 25
extracted documents and their sizes).

**Honest failure list, before anything else.** Five planned sources returned no
usable text and are therefore *not* cited as evidence: the INFORMS weekly-release
press release (742 chars, no body), `axisaistudios.com` day-7 retention (104
chars), `zipx.ai` retention benchmarks (Cloudflare tunnel down), `elmanana.com.mx`
"300M followers in 10 days" (85 chars), Reuters' GEMA–Suno ruling (246 chars,
paywall). Anything resting on those is marked **UNVERIFIED** below, not repeated.

---

# PART I — THE SEVEN CHAINS (7 hops each)

## Chain A — from "the fruit lane is huge" to a number you can defend

1. The fruit-drama format is documented (Riccio, arXiv:2606.09589; Savage Minds) →
2. but the *reach* claim I wrote ("biggest reach engine of 2025-26") had no figure
   attached in my own file. Searching for it →
3. the only figure offered was "300 million followers in 10 days" (elmanana) and
   the page would not load for extraction → **UNVERIFIED**.
4. So reach must be sourced from the *adjacent monetised form*: vertical drama apps.
5. Sensor Tower, *State of Short Drama Apps 2026*: **850M+ downloads in Q1 2026,
   +140% YoY; ~US$750M IAP in Q1 2026, +20% YoY; average daily time 25 min,
   +85% since Jan 2025; users spend ~6× more time than a year earlier.**
6. Omdia via Streaming Lens: **world microdrama market $11B (2025), $14B (2026),
   >$22B by 2030, ~15%/yr**; China alone CNY 50.44B (≈$7.0B, 2024, iiMedia);
   outside China $2.7B (2025) → $3.6B (2026) (MPA).
7. ReelShort: **$1.05B revenue on pace for 2026, ~$63M EBITDA, $40M net profit**;
   DramaBox **$530M gross IAP in 2025 (+75%)**.

**Findings:** the money in this form is real and enormous, but it is *app
revenue*, not meme views. My file conflated the two. Fix applied to the doctrine.

## Chain B — from "8–9 episodes daily" to what actually monetises

1. Riccio: 8–9 episodes, daily from one account →
2. ReelShort's model is not a feed drop, it is **coins to unlock single episodes,
   $0.30–$0.50 each** →
3. DramaBox's model is **$19.99/week subscription (70% of revenue) + coins (30%)**
   over 1,700+ series →
4. the driver in both is the **cliff + paywall boundary**, i.e. where the episode
   ends relative to what is locked →
5. which means the unit of monetisation is *the episode*, and the container is
   *the season*, not the programming block →
6. corroboration that season-level cadence matters: Parrot Analytics — of the 100
   most in-demand US series (Jan–May 2023), **75 released weekly**; weekly/periodic
   releases produced **44 of the 50 best post-season demand-decay rates** since 2016 →
7. so: weekly-or-daily cadence with per-unit paywall beats both binge-drop and
   free-feed for durability.

**Finding:** R2 (weekly serial, in order) survives and is *strengthened*; the
episode boundary is a commercial object, not just a story object.

## Chain C — from the 30-minute block (R5) to a container that is not obviously right

1. My memo asserted the container is a 30-min outlet block (Chain 6 of the first
   report, from *Steal a Brainrot*'s "own the frame") →
2. Tubi/Harris Poll, *The Stream 2026*: **77% of streamers prefer on-demand over
   scheduled programming** →
3. linear TV viewership reported **down ~8% YoY** (LinkedIn/industry aggregation,
   weak source, flagged) →
4. but FAST is not linear-as-we-knew-it: Gracenote (July 2026) — **51.7% of FAST
   programming was produced within the last six years**; sports channels +13.8%,
   news channels +52.9% YoY; global FAST market projected at **16.9% CAGR to
   $40.2B** →
5. and FAST's growth engine is sports/news, i.e. *live/appointment* content —
   exactly what a 10-second bumper network is not →
6. therefore a scheduled block only works where it is *free, ad-supported and
   always-on*, not where it asks for an appointment →
7. and the on-demand alternative is already proven adjacent: the microdrama app
   (Chain A/B), which is 100% on-demand with an unlock ladder.

**Finding:** R5 survives only in a narrowed form — **the block is a FAST-loop
product with ad pods, not appointment TV**, and the serial's paywall-free
on-demand ladder matters more than the block. R5 as written is amended.

## Chain D — from "nobody can own the mascot" (my Chain 5) to trademark, which breaks it

1. My Chain 5 said: AI characters are copyright-ineligible, so own the system →
2. the actual case is **Spyder Games LLC v. Mementum Lab, No. 5:25-cv-10248
   (N.D. Cal.)** — not "DoBig Studios" as the press summary had it; Spyder Games is
   the *Steal a Brainrot* side (docket via CourtListener) →
3. the copyright half is settled law against ownership: **Thaler v. Perlmutter**
   (D.C. Cir. 2025), and the **Supreme Court declined** to take the question in
   2026 (Morgan Lewis) — human authorship required →
4. **but trademark has no human-authorship requirement.** Lutzker: the qualifying
   question "is not whether consumers recognize Tung Tung Sahur, but whether
   [consumers associate it with a commercial source]" — and trademarks on viral
   memes have been granted before →
5. Mementum Lab is a *licensing agency*: its play is marks and licensing, not
   copyright →
6. someone else is already attempting to register the Tung Tung Sahur mark
   (Yahoo/Lutzker reporting) →
7. so the correct conclusion is the *inverse* of what I wrote: a competitor cannot
   win copyright in an AI character, but **can build a trademark estate around it,
   and we could lose the use of our own names to a mark we never filed.**

**Finding:** my Chain 5 conclusion was half wrong. "Own the archive" is right;
"nobody can own the mascot, therefore nothing to worry about" is wrong. Filing our
own marks is now an Era II requirement. This is the single most consequential
correction in this audit.

## Chain E — from "publish the Coherence Contract" (R4) to a legal obligation that already started

1. R4 was written as a *marketing/trust* device: a checkable page →
2. EDRM (Sept 2026) reporting Silbey & Hartzog, *"AI Slop"* (SSRN draft, 6 Sep
   2026): slop as a legal category, with a proposed three-part test →
3. the same piece notes **EU AI Act Article 50 transparency duties became
   operative 2 August 2026** (Regulation (EU) 2026/1744 deferred other parts and
   left that date alone) →
4. penalties under Article 99: **up to €15M or 3% of worldwide annual turnover** →
5. **California's AI Transparency Act (SB 942) became operative the same day,
   2 Aug 2026**, via AB 853: a free detection tool, an optional visible
   disclosure and a **latent disclosure** for image/video/audio →
6. platform and hosting provenance duties land **1 Jan 2027**; capture devices
   **1 Jan 2028** →
7. so a network that publishes "our paperwork is real" is doing voluntarily what
   platforms will demand of it in 2027.

**Finding:** R4 is not optional nicety — it must carry a **provenance/latent
disclosure clause now**, and the dataset should carry machine-readable provenance
before the Jan 2027 platform deadline.

## Chain F — from "the track is the theme" to the music's actual risk

1. The plan has the owner generating tracks in Suno and both agents using them →
2. **Suno's own September 2026 ToS change**: from 3 Sept 2026, downloads are
   tier-capped — **Free: 7 lifetime downloads**; library stays playable, but a
   *download* is the gated act →
3. commercial rights attach to a downloaded file on a paid tier (Suno rights docs) →
4. the provenance risk is not hypothetical: a **German court ruled Suno infringed
   copyrights (GEMA action, Aug 2026)** according to Reuters/Forbes/DW headlines —
   though the Reuters body did not extract for me, so treat the *scope* of that
   ruling as **UNVERIFIED** and the *fact of a ruling* as reported-by-multiple-
   outlets →
5. the licensing market is moving fast in the other direction: Spotify–Believe AI
   remix deal, UMG–ElevenLabs, Suno label licensing deals (Variety, MBW, Forbes) →
6. SAG-AFTRA's 2026 contract draws AI voice lines for performers, and voice-cloning
   consent law is a state-by-state patchwork (Vanderbilt; Vorp tracker) →
7. therefore: instrumental-first, no named-artist imitation prompts, keep the
   prompt + date + tier receipt with every delivered MP3, and never let a track
   imply a performer's voice.

**Finding:** the music plan is viable but needs an **asset-provenance envelope**
per track (prompt, model, tier, download receipt, sha256). Cheap now, impossible
to reconstruct later.

## Chain G — from "legacy" to where AI work is actually admissible

1. My memo used "legacy" loosely, implying a reputation path →
2. **Cannes 2026 (9 April 2026) barred films where generative AI drives
   scripting, visual generation or principal performance synthesis from the Palme
   d'Or competition**; 1,541 features reviewed; technical AI (restoration, cleanup,
   VFX on human-shot footage) still allowed →
3. the same week MPA's chairman argued the opposite publicly (CinemaCon) →
4. a dedicated lane exists: World AI Film Festival, 21–22 April 2026, Palais des
   Festivals; Marché du Film's "Cannes Next / AI for Talent" 12–20 May →
5. Darren Aronofsky's AI-generated series drew a harsh public backlash →
6. AI film festivals in the US are numerous and open (aifilmcontests.com listing) →
7. and the archival lane needs no permission at all: 1,652 manifest-verified
   masters with dates and numbers.

**Finding:** "legacy" cannot mean prizes. It means **the archive + the
disclosure-clean record + the AI-native festival circuit**, in that order.

---

# PART II — TRIPLE DEVIL'S ADVOCATE

## Pass 1 — Analytical core (are the numbers real, and are they ours to use?)

Verified hard numbers: 850M Q1-2026 short-drama downloads (+140% YoY), ~$750M
quarterly IAP (+20%), 25 min/day (+85%), ~6× time YoY (Sensor Tower); ReelShort
$1.05B/2026 with $40M net; DramaBox $530M 2025 IAP (+75%, and only a 3.1% net
margin in 2024); world microdrama $11B→$14B→$22B+ (Omdia) with China ≈$7.0B and
ex-China $2.7B→$3.6B (MPA); Parrot's 75/100 weekly and 44/50 decay figures;
Gracenote FAST 51.7% recent programming, +13.8% sports / +52.9% news channels,
$40.2B by CAGR 16.9%; Cannes 1,541 features reviewed.

**Attack 1 — market-size arithmetic.** The streaming-lens page explicitly warns
that China-only, world and ex-China figures are **not competing estimates of the
same thing and do not add**. My first report said "the fruit lane is the biggest
reach engine" and used "the $8B vertical drama" shorthand from a search snippet.
That shorthand is indefensible. **Verdict: my market framing FAILED; the
corrected framing (world $14B 2026, ex-China $3.6B) PASSES.**

**Attack 2 — base rate.** "Serial microdrama works" is not a base rate, it is a
winner's list: ReelShort is **>50% of US revenue**, so the US market's viability
is one company's viability (Streaming Lens states exactly this). Most entrants
lose; DramaBox made a 3.1% net margin in its *good* year. **Verdict: the claim
"serials monetise" PASSES; the claim "serials are a safe bet" FAILS.**

**Attack 3 — is any of this ours?** We have no app, no paywall, no user accounts,
no coin economy, and no acquisition budget (ReelShort spent ~55% of revenue on UA
in 2025). **Verdict: the monetisation mechanism is NOT transferable to us as-is.
What is transferable is cadence + cliff + a named cast.**

## Pass 2 — Structural integrity (which components are load-bearing, which are decoration?)

| Component of Era II | Status after structural pass |
|---|---|
| Serial arc, fixed cast, one cliff per unit | **LOAD-BEARING** — supported by Riccio's form + Parrot's cadence evidence |
| One bed per channel, sonic identity | **LOAD-BEARING but UNEVIDENCED HERE** — my sonic-branding citations failed to extract; treat as a working hypothesis, not a finding |
| PIPS as a sound-named character | **DECORATIVE until proven** — the Sahur precedent is a single n=1 case; onomatopoeia is not a mechanism |
| 30-min outlet block (R5) | **PARTLY DECORATIVE** — 77% prefer on-demand; only the FAST-loop variant is defensible |
| Coherence Contract (R4) | **LOAD-BEARING and now legal** — Art. 50 / SB 942 operative 2 Aug 2026 |
| "Own the archive, not the mascot" | **HALF WRONG** — trademark inverts it (Chain D) |
| Music as theme-not-dub | **LOAD-BEARING** — SAG-AFTRA/voice-consent patchwork makes dub risk asymmetric |
| "Coherent = distribution advantage" | **DECORATIVE / likely false** — AI slop is *recommended* (reports: ~1 in 5 videos recommended to new YouTube users is AI slop); coherence buys retention and rights, not reach |

## Pass 3 — Adversarial stress test (assume Era II is the wrong strategy; build the case)

**The strongest case against us, built honestly:**

1. **Distribution is optimized for slop, not for craft.** Reported audits find AI
   slop dominating recommendations to new users and engagement-optimized ranking
   rewarding clickbait over quality (arXiv:2401.09804). Our deadpan coherence is an
   *engagement tax*.
2. **The winning form is a paywalled app, not a channel.** Everything that made
   money in this research sells *unlocks*. We are building a schedule.
3. **The prestige door is shut.** Cannes bans genAI from competition; a name
   director's AI series was mocked. "Legacy" via reputation is not available on any
   timeline we control.
4. **The IP moat I proposed is leaky.** Someone is trademarking the era's most
   famous AI character; marks beat copyright claims; we have filed nothing.
5. **The music has provenance risk we cannot audit after the fact.** A German
   court found Suno infringing; tier-capped downloads gate commercial rights; and
   we do not yet keep per-track receipts.
6. **The economics of our own archive are unproven.** 1,652 masters, $0 revenue
   recorded, no audience metric in the manifest. "The ledger is the estate" is a
   beautiful sentence with no cash-flow behind it.

**Now the rebuttal, restricted to what the evidence actually permits:**

- Against (1): the slop-recommendation evidence describes *new-user cold start*;
  nothing in the run shows slop retains a returning viewer. Parrot's decay data
  says cadence, not novelty, holds demand. So coherence is a **retention**
  argument — which is exactly the metric a serial is built to win.
- Against (2): true, and it is why R5 narrows and why the *episode boundary* must
  be treated as a product surface even if we never charge for it.
- Against (3): concedes the point. Legacy = archive + disclosure-clean record.
- Against (4): fatal *unless* we file. That is an action, not an argument.
- Against (5): fixable in one hour per track.
- Against (6): cannot be rebutted with evidence. It is the true open risk.

**Pass-3 verdict: Era II is not invalidated, but two of its pillars (R5 as
written, and the mascot/ownership inference) are.** The strategy survives as:
*serial first, sound as hypothesis, contract as law, marks as filings, archive as
the only real asset.*

---

# PART III — THE 25 FINDINGS (each with verdict + source)

Format: claim → **verdict** → source.

1. Short-drama apps passed 850M downloads in Q1 2026 (+140% YoY) → **CONFIRMED** → Sensor Tower.
2. Short-drama IAP ~$750M in Q1 2026, +20% YoY (moderating) → **CONFIRMED** → Sensor Tower.
3. Daily time in short-drama apps reached 25 min (+85% since Jan 2025) vs OTT flat ~35 min → **CONFIRMED** → Sensor Tower.
4. World microdrama market $11B (2025) / $14B (2026) / >$22B (2030), ~15%/yr → **CONFIRMED (Omdia via Streaming Lens)**.
5. China ≈ CNY 50.44B (2024, iiMedia) and ex-China $2.7B→$3.6B (MPA) are separate measurements that must not be summed → **CONFIRMED (and my earlier framing FAILED it)**.
6. ReelShort on pace for $1.05B revenue and first profit ($40M net, $63M EBITDA) in 2026 → **CONFIRMED** → Tech Times/MPA.
7. ReelShort is >50% of US vertical-drama revenue: market viability is one company's viability → **CONFIRMED** → Streaming Lens.
8. DramaBox $530M gross IAP 2025 (+75%) but only a 3.1% net margin in 2024 → **CONFIRMED** → Streaming Lens/Sensor Tower/MPA.
9. The monetising unit is the episode unlock ($0.20–$0.50) or a weekly pass ($19.99), not the block → **CONFIRMED** → Streaming Lens, Tech Times.
10. Weekly cadence correlates with durable demand: 75 of the 100 most in-demand US series were weekly; 44 of the 50 best decay rates were weekly/periodic → **CONFIRMED (correlational, Parrot Analytics)**.
11. Day-7 retention benchmarks for vertical drama → **UNVERIFIED** (two sources failed to load; do not cite).
12. Fruit-drama reach "300M followers in 10 days" → **UNVERIFIED** (page did not extract; the only source found).
13. Fruit-drama *form* (8–9 episodes, daily, small fixed cast, one bed) → **CONFIRMED** → Riccio arXiv:2606.09589; Savage Minds.
14. AI slop has no settled definition; a three-part test is proposed in draft (Silbey & Hartzog, SSRN, 6 Sep 2026) → **CONFIRMED as draft scholarship, NOT law** → EDRM.
15. EU AI Act Art. 50 transparency duties operative 2 Aug 2026; penalties up to €15M/3% turnover → **CONFIRMED** → EDRM.
16. California AI Transparency Act (SB 942/AB 853) operative the same day; latent disclosure for video/audio; platform provenance duties 1 Jan 2027 → **CONFIRMED** → EDRM.
17. Human authorship is required for copyright: Thaler v. Perlmutter (D.C. Cir. 2025), Supreme Court declined review → **CONFIRMED** → Justia/Morgan Lewis.
18. The live case is Spyder Games LLC v. Mementum Lab, No. 5:25-cv-10248 (N.D. Cal.) → **CONFIRMED** → CourtListener (corrects my earlier "DoBig Studios" attribution).
19. Trademark has no human-authorship requirement and turns on source identification; meme marks have been registered; a third party is attempting the Tung Tung Sahur mark → **CONFIRMED** → Lutzker.
20. Therefore a competitor can build a mark around an AI character even though nobody can own its copyright → **CONFIRMED — this overrules my Chain 5 inference**.
21. Suno from 3 Sept 2026 caps downloads by tier (Free: 7 lifetime); library stays playable but downloads are gated → **CONFIRMED** → suno.com/blog.
22. A German court ruled Suno infringed copyrights (GEMA, Aug 2026) as reported by multiple outlets → **REPORTED, scope UNVERIFIED** (Reuters body paywalled for extraction) → Reuters/DW/Forbes headlines.
23. Cannes 2026 barres generative-AI-driven films from the Palme d'Or competition, technical AI permitted, 1,541 features reviewed → **CONFIRMED (trade/festival reporting, not primary rules)** → studio.aifilms.ai synthesis.
24. FAST channels are growing but on sports/news, and 51.7% of FAST programming is ≤6 years old; market ~$40.2B by CAGR 16.9% → **CONFIRMED** → Gracenote.
25. 77% of streamers prefer on-demand over scheduled programming → **CONFIRMED (single survey, Tubi/Harris)** — and it damages R5 as written.

---

# PART IV — DOCTRINE AMENDMENTS (Era II v2 — overruling my own memo)

**A1. R5 is narrowed.** The container is a **FAST-style always-on loop with ad
pods**, free and on-demand-first. Do not build for appointment viewing. The
30-minute block survives only as a *loop unit*, never as a schedule promise.

**A2. File the marks.** Register the wordmarks and serial titles we actually use —
`~ WuBu ~`, WuBuTV, SERIAL-<n> titles, THE PIPS — as marks, because trademark, not
copyright, is the enforceable lever in this lane. (This is the doctrine's most
important change and it came from the audit, not from me.)

**A3. R4 gains a legal clause.** The Coherence Contract must carry, explicitly:
provenance/latent disclosure for AI-generated video and audio (EU Art. 50 + CA SB
942, operative 2 Aug 2026), and the dataset must carry machine-readable provenance
**before 1 Jan 2027** when platform provenance duties bite.

**A4. Music gets an envelope.** Every delivered track ships with: prompt text,
model + version, account tier, download receipt, sha256, date. Instrumental-first,
no named-artist imitation, no synthetic voice that could be a performer's.

**A5. "Coherent" is a retention claim, not a reach claim.** Stop saying slop is
losing; the evidence says slop is *recommended*. We win returning viewers, rights
cleanliness and archivism — and we say only that.

**A6. Market numbers are quoted with their scope or not at all.** World vs China
vs ex-China never adds. Every figure in a slate or memo carries its source and its
scope in the same sentence.

**A7. Sound identity is a hypothesis until measured.** The nine-sting plan stays,
but it is tagged as hypothesis; the first test is a 20-person recall check on two
stings before we build all nine.

---

## What this run cost and what it bought

100 searches, 25 extracted sources, 471 candidate URLs, 7 chains, 25 findings, one
corrected case name, one unverified reach claim killed, two doctrine pillars
demoted, one new legal obligation found, and one genuinely new strategic action
(file marks) that no amount of my own reasoning had produced.

The audit's blunt summary: **the serial instinct is right, the container was
wrong, the ownership story was backwards, and the archive is still the only thing
we own outright.**
