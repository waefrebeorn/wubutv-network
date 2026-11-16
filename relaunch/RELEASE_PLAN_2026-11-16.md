# RELEASE PLAN — WuBuTV Relaunch (2026-11-16)

Authority: user decree 2026-11-16 (msg 516, confirmed in main chat): TV station time —
uploads resume as content is made, blanket posting permission, all previously rejected
pieces accepted for upload **subject to the msg-518 reused-content rule** (a rejected /
superseded version posts only if it is different enough from the posted version not to
trip platform reused-content/spam rules, and it must be labeled as what it is).
Ranking law (from RECURSIVE_NAG_DESIGN_2026-11-16 §1.2): **user verdict > lore-arc
order > new work > bounded engagement metrics**. This plan is the concrete queue the
Release Conductor's `release_queue.json` is seeded from. Plan only — nothing here
posts by itself.

Sources: PLATFORM_AUDIT_2026-11-16 (posted/unposted baseline), CONTENT_INVENTORY_
2026-11-16 (asset + differentiation verdicts), RECURSIVE_NAG_DESIGN_2026-11-16
(ranking + fire conditions), WUBU_LORE_AND_LONG_ARCS_2026-10-27 (ARC-1 The One Viewer,
ARC-2 The Roster That Keeps Everyone, ARC-3 The Count; chains rotate ARC-1 → ARC-2 →
ARC-3, never two chains from one arc back-to-back; OPEN → DEVELOP → PAYOFF).

**Note on the design source:** the design file on disk ends mid-§3.3; §§3.4–6 are
absent. This plan relies on the ranking law and fire conditions as stated in its
§§0–2 (which are complete) and on the inventory's per-item verdicts for §4.3's
guardrail. If the design's missing sections surface, cadence numbers in §4 below
should be reconciled against its §3.5 governor text.

## Preconditions (before the first post, per the audit — re-audit, never blind restore)

1. Threads `PAUSE_FLAG` (shutter-dated) and the stale `DAILY_COUNT` files on Threads/IG
   are cleared by the relaunch lane re-audit, with reason + expiry recorded — not
   blindly deleted.
2. Every post passes the design's fire conditions: fresh pre-post platform check
   (ledger AND platform agree the item is unposted), on-disk md5 = inventory md5,
   reused-content check for any non-current version.
3. Instagram verification is by direct post-ID lookup only (the census endpoint
   returns partial windows — audit blocker 4).
4. TikTok has no connector: its column in this plan is **ledger-only**. The ledger
   shows zero MVs and zero show episodes posted, but the user hand-uploaded 500+
   bumpers personally and hand-uploads of MVs cannot be excluded. When the TikTok
   lane revives, its first Studio session glance verifies the MV/show titles before
   the lane treats any of them as a premiere; any title found already live is marked
   posted in the ledger and skipped, never re-posted.
5. The 9 live double-posts (IG: E1M-034, E2M-001, E2M-023; Threads: B-1293, E2M-053,
   E2M-056, E2M-009, E2M-010, E2M-019) are the user's in-app removal action. Nothing
   in this plan touches them, and no plan item re-posts any E1M/E2M episode anywhere
   (all 119 are already posted on all three platforms).

---

## PHASE 1 — THE PREMIERE WAVE

35 posts per platform on Instagram and TikTok (15 show episodes + 20 MV premieres);
30 on Threads (15 episodes + 15 MVs — see the Threads MV baseline below).

### 1.1 The fifteen show episodes (never posted anywhere)

Show-lines run in internal story order (pilot → new-era E2 → morph E1). Blocks run
pilots first, then E2s, then morph E1s; inside each block the order follows the lore
rotation ARC-1 → ARC-2 → ARC-3 with no arc repeated back-to-back (a block that runs
out of one arc yields to the next arc with an episode left).

Arc assignment of the show-lines (each line carries one arc through all three
generations):
- **ARC-1 · THE ONE VIEWER** — THE MACHINE → ON AIR (the station's machines watch;
  ON AIR is also the designated MV show and carries MV premieres in-story) and
  THE LAST SEAT (the one seat that is always occupied — the viewer, seated).
- **ARC-2 · THE ROSTER THAT KEEPS EVERYONE** — THE ROSTER → THE NIGHT LIST (the
  roster becomes the night list: names kept, beds decided, nobody erased quietly).
- **ARC-3 · THE COUNT** — THE COUNT → ONE SHORT (the count that is always one short)
  and THE TENTH SECOND → HOLD ON (the world restarts on the count of ten).

**Episode order (identical on all three platforms):**

| # | Episode | Arc · chain beat |
|---|---|---|
| 1 | PILOT-1 · THE MACHINE | ARC-1 · Chain 1 OPEN — the lobby monitor plays the station to an empty room |
| 2 | PILOT-3 · THE ROSTER | ARC-2 · Chain 1 OPEN — the circled name |
| 3 | PILOT-4 · THE COUNT | ARC-3 · Chain 1 OPEN — the count passes a round number |
| 4 | PILOT-5 · THE LAST SEAT | ARC-1 · DEVELOP — the seat that is always occupied |
| 5 | PILOT-2 · THE TENTH SECOND | ARC-3 · DEVELOP — the count that restarts the world |
| 6 | E2 SHOW-1 · THE MACHINE — "The Mouth That Moved First" | ARC-1 · DEVELOP |
| 7 | E2 SHOW-3 · THE ROSTER — "The Pass, Done Properly" | ARC-2 · DEVELOP |
| 8 | E2 SHOW-4 · THE COUNT — "The Door Counts First" | ARC-3 · DEVELOP |
| 9 | E2 SHOW-5 · THE LAST SEAT — "Ask the Seat" | ARC-1 · DEVELOP |
| 10 | E2 SHOW-2 · THE TENTH SECOND — "The Chalk Wall" | ARC-3 · DEVELOP |
| 11 | ON AIR E1 — "The Signed Folder" | ARC-1 · DEVELOP — the MV show premieres; MV catalogue posts ride this chain |
| 12 | THE NIGHT LIST E1 — "The Sol Night" | ARC-2 · DEVELOP |
| 13 | ONE SHORT E1 — "Thirty-One Umbrellas" | ARC-3 · DEVELOP — the count lands one short, on screen |
| 14 | THE LAST SEAT E1 — "Night One: The Woman with the White Stub" | ARC-1 · DEVELOP |
| 15 | HOLD ON E1 — "Write That He Owes Me" | ARC-3 · DEVELOP — placed last in the block per the verdict rule: its one-star verdict (msg 513) demotes it below all unrated new work (design §1.2 rule 1); demotion is not exclusion — msg 516 accepted it |

No episode in this wave is a PAYOFF: the arcs open and develop here. Payoffs are
later chains (morph E2s and beyond, §6) — a payoff never posts before its arc's
earlier chains are live on at least one platform (design §1.2 rule 2).

### 1.2 The MV catalogue premieres

Standalone MV posts are tagged to the arc whose open chain they thematically serve
(design §1.2 rule 2 — the tag is recorded in inventory, read by the Conductor).
Within the MV order, user-approved MVs lead their arc group (verdict rule), then
catalogue order. An MV post that follows an episode of the same arc is a
**chain-serving post** — part of that chain's beat, not a new chain — so the
rotation is counted between beats, not between individual posts.

**MV premiere order (Instagram + TikTok):**

| # | MV | Arc tag · why |
|---|---|---|
| 1 | MV-21 · "Wowie Pants That Fit" | ARC-1 — a projector loop performing for an empty room: the one viewer, literal. User-approved 85% (msg 437) — verdict head of the MV queue |
| 2 | MV-7 · "I'm the Nobody Man" | ARC-2 — the name that matches no employee |
| 3 | MV-14 · "CLIP IT" | ARC-3 — the count of clips. User-approved (msg 326) |
| 4 | MV-15 · "Unread DMs" | ARC-1 — broadcasts nobody reads. Approved, closed |
| 5 | MV-3 · "I Am Your Dad (HE IS NOT YOUR DAD, RUN)" | ARC-2 — a name claimed, a roster disputed |
| 6 | MV-9 · "Gotta hold it" | ARC-3 — holding the count. v2 approved, closed |
| 7 | MV-8 · "Wipe and it's still there" | ARC-1 — the thing in the seat is still there. Accepted, closed |
| 8 | MV-5 · "Easy now, easy now" | ARC-2 — v6 approved, closed |
| 9 | MV-10 · "Aging tropes" | ARC-3 — time, counted. Approved, closed |
| 10 | MV-16 · "Wrong for Years" | ARC-1 — the long watch. Approved, closed |
| 11 | MV-6 · "Sell the Lemons" | ARC-2 — Peter sells; the roster of goods |
| 12 | MV-12 · "Micro-soft lost the bet" | ARC-3 — the count as currency (ARC-3 Chain 4's question) |
| 13 | MV-4 · "This Time It's Real" | ARC-1 — this time the viewer is real |
| 14 | MV-19 · "Confused NPC" | ARC-2 — a person with no roster entry |
| 15 | MV-18 · "What's a Sigma? ~Mom" | ARC-3 — sigma is the sum sign: the count itself |
| 16 | MV-13 · "Movin' on Newton" | ARC-1 — motion, watched |
| 17 | MV-17 · "Fridge Light Mystery" | ARC-2 — the building knows (the Dispatcher's light) |
| 18 | MV-11 · "Water hit my balls" | ARC-3 — catalogue rotation fill |
| 19 | MV-20 · "Laundry Life" | ARC-1 — the everyday, broadcast |
| 20 | MV-2 · "Toll Roads Are Dumb" | ARC-2 — the first MV closes the catalogue wave |

**Threads MV baseline (audit — hard rule):** MV-2, MV-5, MV-6, MV-7 and MV-8 were
already promo-posted to Threads unledgered on 2026-11-07 → 11-09, plus one
unnumbered "Futurama's finished" promo. Threads therefore gets **15 MV premieres**:
the order above with MV-7, MV-8, MV-5, MV-6 and MV-2 removed (MV-21, MV-14, MV-15,
MV-3, MV-9, MV-10, MV-16, MV-12, MV-4, MV-19, MV-18, MV-13, MV-17, MV-11, MV-20).
The five promo-posted MVs are NOT re-posted to Threads as new in any phase; if one
is ever re-posted there it goes through Phase 3's label rule as a full-master post
("Full Master — promo previously posted"), which is a parent decision, not a
default of this plan.

### 1.3 The merged wheel (how episodes and MVs interleave)

The wheel alternates **episode → chain-serving MV → episode → MV**, episodes drawn
in §1.1 order, MVs drawn in §1.2 order, each MV following the most recent episode
of its own arc where the sequence allows (the Conductor's queue enforces the
arc-beat reading in §1.2). When the 15 episodes run out, remaining MVs post
solo in order. Phase 2 ST posts weave into this same wheel (§2.2) — the wheel is
one feed, not three dumps.

**The first ten posts (Instagram and TikTok, in order):**

1. PILOT-1 · THE MACHINE (episode · ARC-1 OPEN)
2. MV-21 · "Wowie Pants That Fit" (MV premiere · ARC-1 chain-serving, verdict head)
3. PILOT-3 · THE ROSTER (episode · ARC-2 OPEN)
4. MV-7 · "I'm the Nobody Man" (MV premiere · ARC-2 chain-serving)
5. PILOT-4 · THE COUNT (episode · ARC-3 OPEN)
6. MV-14 · "CLIP IT" (MV premiere · ARC-3 chain-serving, approved)
7. PILOT-5 · THE LAST SEAT (episode · ARC-1 DEVELOP)
8. MV-15 · "Unread DMs" (MV premiere · ARC-1 chain-serving)
9. PILOT-2 · THE TENTH SECOND (episode · ARC-3 DEVELOP)
10. MV-9 · "Gotta hold it" (MV premiere · ARC-3 chain-serving)

On Threads the wheel is identical except slot 4: MV-7 is baseline-posted there,
so the ARC-2 chain-serving MV at that beat is MV-3 (the next ARC-2 MV in the
Threads order), and the Threads MV sequence then continues MV-14, MV-15, MV-9, …

---

## PHASE 2 — THE ST BACKLOG (interleaved, never a dump)

The ST station episodes are the canon the lore bible was built from. On TikTok all
79 are already posted — TikTok has **no Phase 2**. The missing runs are premieres
for the Instagram and Threads audiences.

### 2.1 The lists (strict series order per platform)

- **Instagram — 19 posts:** ST-001, ST-002, …, ST-017, then ST-078, ST-079.
  (ST-018…ST-077 are already live on IG.)
- **Threads — 36 posts:** ST-001, ST-002, …, ST-033, then **ST-077 (named post,
  §2.3)**, then ST-078, ST-079. (ST-034…ST-076 are already live on Threads.)

### 2.2 Interleave rule

Phase 2 runs **inside** the Phase 1 window, not after it:
- Instagram: 1 ST post per day, on the §4 cadence, drawn in series order.
- Threads: 2 ST posts per day (its backlog is ~2× Instagram's), in series order.
- An ST post never displaces a premiere-wheel post; it fills the day's remaining
  cadence slots. When Phase 1 ends, the ST cadence continues unchanged until the
  backlog clears (~19 days IG, ~18 days Threads at the §4 ceilings).
- ST posts are captioned as canon (§5) and carry no arc-chain beat — they deepen
  the world the premieres are opening; chain advancement stays with Phase 1 / §6.

### 2.3 ST-077 on Threads — the named deliberate post

ST-077 hit a final 429 on 2026-11-08 and was never retried; that never-retry rule
was a **shutter-era** rule, written for a station that had been ordered dark. The
2026-11-16 decree supersedes the shutter: uploads are back on with blanket
permission, and ST-077 is named in this plan as **one deliberate fresh post
attempt**, scheduled in its series position (after ST-033, before ST-078) as a
standalone slot — not a lane default, not a bulk catch-up. Backoff discipline
applies in full: a single attempt; on a 429 the platform enters backoff per
`platform_state.json`, other platforms keep firing (reroute, never hammer), and
ST-077 may be attempted once more only after the backoff expires clean. If the
second attempt also 429s, ST-077 returns to held and is reported — it is never
hammered, and the old retry-hammer lanes stay disabled (design §2.2).

---

## PHASE 3 — THE ALTERNATE-TAKE TIER

Every rejected/superseded version the inventory marked **POSTABLE**, with the
inventory's exact label text. Rules for the whole tier:
- An alternate version posts **no sooner than 7 days after** the current master of
  the same MV on the same platform, and alternate versions of the same MV are
  spaced **≥7 days apart** from each other on a platform.
- **≤1 alternate-take post per platform per day**, in the day's last cadence slot.
- The caption's first line carries the label (§5.3). No label, no post (design
  §2.3 fire condition 5 — hard block).
- Phase 3 starts only once Phase 1's MV premieres are complete on that platform.

### 3.1 Postable items (label text is exact, from the inventory)

| Item | File | Label (exact) | Platforms |
|---|---|---|---|
| MV-2 viewing cut | `mv2_toll_roads_are_dumb_viewingcut_16x9.mp4` | Alternate Cut | IG · Threads · TikTok |
| MV-3 9:16 vertical | `mv3_i_am_your_dad_9x16.mp4` | Vertical Cut | TikTok only (one platform only — inventory risk note: reframe-only, some reused-content systems flag crops) |
| MV-3 9:16 recut | `mv3_i_am_your_dad_9x16_recut.mp4` | Vertical Cut — Recut | Instagram only (one platform only, same risk note) |
| MV-5 v1 | `mv5_easy_now_easy_now_16x9.mp4` | Alternate Take | IG · Threads · TikTok |
| MV-5 v2 | `mv5_easy_now_easy_now_16x9_v2.mp4` | Alternate Take | IG · Threads · TikTok |
| MV-5 v3 | `mv5_easy_now_easy_now_16x9_v3.mp4` | Alternate Take | IG · Threads · TikTok |
| MV-5 v4 | `mv5_easy_now_easy_now_16x9_v4.mp4` | Alternate Take | IG · Threads · TikTok |
| MV-5 v5 | `mv5_easy_now_easy_now_16x9_v5.mp4` | Alternate Take | IG · Threads · TikTok |
| MV-5 lyrics redo | `mv5_easy_now_easy_now_16x9_lyrics.mp4` | Alternate Take — Lyrics Version | IG · Threads · TikTok |
| MV-7 v1 (base) | `mv7_im_the_nobody_man_16x9.mp4` | Alternate Take | IG · TikTok (see exclusivity note) |
| MV-7 corrected | `mv7_im_the_nobody_man_16x9_corrected.mp4` | Alternate Take — Corrected Cut | Threads (see exclusivity note) |
| MV-7 otaku | `mv7_im_the_nobody_man_16x9_otaku.mp4` | Alternate Take — Otaku Cut | IG · Threads · TikTok |
| MV-8 v2 | `mv8_wipe_and_its_still_there_v2_16x9.mp4` | Alternate Take | IG · Threads · TikTok |
| MV-11 master #1 | `mv11_water_hit_my_balls_16x9.mp4` | Alternate Take | IG · Threads · TikTok |
| MV-11 master #2 | `mv11_water_hit_my_balls_rebuild_16x9.mp4` | Alternate Take | IG · Threads · TikTok |
| MV-16 wrong-take master | `mv16_wrong_for_years_16x9_wrongtake.mp4` | Alternate Suno Take | IG · Threads · TikTok — the only item that differs in BOTH audio and picture (a different Suno performance); postable as-is, label still carried so viewers know it is the alternate recording |

**MV-7 exclusivity (inventory note):** MV-7 v1 and MV-7 corrected are 0.910-similar
to *each other* — at most one of them per platform. This plan assigns v1 → IG +
TikTok, corrected → Threads, so both versions are used and no platform carries both.

**Phase 3 counts:** Instagram 14 · Threads 13 · TikTok 14.

### 3.2 HELD — MV-8 v1 (named, not queued)

`mv8_wipe_and_its_still_there_16x9.mp4` (label would be: Alternate Take) is marked
postable-with-label by the inventory **with a content flag**: it was rejected on
2026-11-08 in part for a **child subject in frame** — a content problem, not a
quality or reused-content problem. The msg-516 decree accepts rejected pieces for
upload, but the inventory explicitly requires a parent/user decision before this
one posts anywhere, decree or not. It is therefore **held out of the queue** and
named here so the decision is visible: it enters Phase 3 only on an explicit
user yes in chat. Nothing else in this plan is held.

### 3.3 EXCLUDED — TOO CLOSE (named, per the msg-518 rule; do not post anywhere)

Same audio and same/near-identical picture as a version already posted (SSIM
≥0.90 family, per the inventory's sampling):

- MV-2 v6 (`mv2_toll_roads_are_dumb_v6_16x9.mp4`, SSIM 0.946 vs v7)
- MV-2 v7 non-lyrics (`mv2_toll_roads_are_dumb_v7_16x9.mp4`, SSIM 0.987 — caption layer only)
- MV-3 base / old-caption (`mv3_i_am_your_dad_16x9.mp4`, SSIM 0.933–0.947)
- MV-3 corrected (`mv3_i_am_your_dad_16x9_corrected.mp4`)
- MV-3 recut (`mv3_i_am_your_dad_16x9_recut.mp4`, SSIM 0.971)
- MV-3 retimed (`mv3_i_am_your_dad_16x9_retimed.mp4`, SSIM 0.971)
- MV-3 q5 (`mv3_i_am_your_dad_16x9_q5.mp4`, SSIM 1.000 over the first 60s)
- MV-4 base / old-caption (`mv4_this_time_its_real_16x9.mp4`, SSIM 0.990 — caption layer only)
- MV-6 base / old-caption (`mv6_sell_the_lemons_16x9.mp4`, SSIM 0.978)
- MV-9 v1 (`mv9_gotta_hold_it_16x9.mp4`, SSIM 0.975 vs v2)
- MV-12 v1 (`mv12_micro_soft_lost_the_bet_16x9.mp4`, SSIM 0.999)
- MV-12 v2 (`mv12_micro_soft_lost_the_bet_v2_16x9.mp4`, SSIM 1.000)
- MV-13 v1 (`mv13_movin_on_newton_16x9.mp4`, SSIM 1.000 over the first 60s)

Also excluded, not uploadable at all: MV-2 v1 (rejected 2026-11-01 — **no file
exists on this VM**), MV-15's first/superseded master (**no file on disk**), the
8 MV-3 intermediate renders (assembly intermediates, not masters), and the E1M
duplicate re-encodes `e1m_028_the_power_hour_16x9_fixed.mp4` /
`e1m_036_the_snap_six_16x9_fixed.mp4` (ARCHIVE duplicates of episodes already
posted everywhere).

Out of scope for this plan (noted so they are not mistaken for omissions): the
bumper pool (10s bumpers are CDN base clips, not standalone uploads — design
§2.1), the Q3 factory episodes and Q4 STATION serial pieces in the archive tier
(207 Q3 files on disk with pre-shutter posted marks; 158 of 160 Q4 masters are
not on this VM at all). Either enters only via a future inventory pass with its
own double-post check.

---

## 4. CADENCE (per platform — ceilings, not targets)

Drawn from the old lanes' proven governors; every ceiling is subordinate to the
platform backoff state (design §1.2 rule 5: a platform in backoff contributes no
posts at all; other platforms keep firing).

| Platform | Lane lineage | Ceiling | Spacing floor | Daily ceiling |
|---|---|---|---|---|
| TikTok | kickstand-nag browser lane: 9 posts/hr, 6-min floor | 9 / hour | ≥6 min between posts (learned governor floor may only widen it) | 8 / day |
| Instagram | reel-poster 30m + episode-poster 1h, `DAILY_COUNT` governor | — | ≥2 h between posts | 4 / day (2 premiere-wheel + 1 ST + 1 flex/alternate) |
| Threads | lanes A+B 1h, offset 30m, `DAILY_COUNT` governor | — | ≥1 h between posts | 6 / day (premiere-wheel + 2 ST + flex) |

- At these ceilings Phase 1 + Phase 2 complete in roughly three weeks per
  platform; Phase 3's spacing rules stretch its 13–14 posts across at least two
  further weeks. That pace is the point: a relaunch that reads as a station
  broadcasting, not a backlog dump or a spam burst.
- Any 429 / lock / challenge: the platform's backoff engages (bounded, IG's
  6h-backoff pattern is the model), its queue waits, the other platforms reroute
  and continue. No lane ever retries inside a backoff window.
- Post hours follow the metrics loop once it has evidence (≥3 posts sharing a
  feature, design §1.2 rule 4); until then, posts spread across the waking day
  rather than clustering.

## 5. CAPTION & LABEL CONVENTIONS

### 5.1 Show episodes
`{SHOW} — "{Episode Title}" · {PILOT / E2 / E1} · [ARC-N · {ARC NAME} · {OPEN|DEVELOP}] · ~ WuBu ~`
- Pilots carry no episode title (none exists): `THE MACHINE — Pilot · [ARC-1 · THE ONE VIEWER · OPEN] · ~ WuBu ~`
- Example: `ON AIR — "The Signed Folder" · E1 · [ARC-1 · THE ONE VIEWER · DEVELOP] · ~ WuBu ~`

### 5.2 MV premieres
`MV-{N} — "{Song Title}" · [ARC-N · {ARC NAME}] · ~ WuBu ~`
- Example: `MV-21 — "Wowie Pants That Fit" · [ARC-1 · THE ONE VIEWER] · ~ WuBu ~`
- The wordmark line `~ WuBu ~` closes every caption, exact, tildes included.

### 5.3 Alternate takes (Phase 3 — the label is the first line, verbatim)
`{LABEL} — MV-{N} "{Song Title}" ({version}) · [ARC-N · {ARC NAME}] · ~ WuBu ~`
- Example: `Alternate Take — MV-5 "Easy now, easy now" (v5) · [ARC-2 · THE ROSTER THAT KEEPS EVERYONE] · ~ WuBu ~`
- Example: `Alternate Suno Take — MV-16 "Wrong for Years" (wrong-take master) · [ARC-1 · THE ONE VIEWER] · ~ WuBu ~`
- The label text is exactly the inventory's recommended label (§3.1) — never
  paraphrased, never dropped, never moved below the first line. This is the
  msg-518 compliance surface: same-audio pieces are always labeled as what they are.

### 5.4 ST backlog
`STATION — ep{NNN} (ST-{NNN}) · WuBuTV canon · ~ WuBu ~`

### 5.5 Hashtags
One standing set, kept small and constant so the metrics loop can read tag effects:
`#WuBuTV #aishow #aimusicvideo` on premieres; ST posts take `#WuBuTV #stationcanon`;
alternate takes take the premiere set plus no extra tags (the label does the work).

## 6. "UPLOADS AS YOU MAKE THEM" — THE NEW-WORK RULE (operational)

From the decree: new deliveries post as they are made. Concretely, for every
future delivery (morph E2s when they land, new MVs, any new episode):

1. The delivery's `*_DELIVERED.flag` / GATE_LOG landing is the trigger
   (inventory scan signal S6). The item enters `release_queue.json` at the
   **head of its platform queues**, ahead of all remaining Phase 1–3 backlog —
   design §1.2 rule 3 (new work before catalogue) — subject only to rule 1
   (a fresh user verdict on another item can still outrank it) and to the
   fire conditions (pre-post platform check + md5 identity check).
2. **Target: posted to all three platforms within 24h of delivery**, inside the
   §4 ceilings — a new delivery may spend a platform's flex slot, and if the
   day's ceiling is already spent it takes the first slot of the next day.
   TikTok rides the same rule via its lane, with the §0 ledger caveat.
3. The premiere wheel **pauses around it**: the new item posts, then the wheel
   resumes at its next beat. New work never waits for a phase boundary.
4. Arc handling: the inventory scan assigns the item its arc tag and chain
   state at intake. A morph E2 that advances an arc posts as that arc's next
   chain beat (DEVELOP, or PAYOFF when the show's arc reaches it) — chain
   order inside an arc is never violated by the new-work rule: if an arc's
   earlier chain is somehow still unposted, the new item waits for that chain
   and the pair posts in order.
5. A user verdict on the new item lands in `verdicts.jsonl` and re-ranks it
   immediately (praise → stays head; a one-star/reject verdict → demoted below
   unrated new work but still posted, per msg 516 + the §4.3 guardrail if it is
   ever superseded by a newer version of itself).

## Totals

| Phase | Instagram | Threads | TikTok (ledger-only) |
|---|---|---|---|
| 1 — premieres (episodes + MVs) | 15 + 20 = **35** | 15 + 15 = **30** | 15 + 20 = **35** |
| 2 — ST backlog | **19** | **36** (incl. the named ST-077 post) | 0 (complete) |
| 3 — alternate takes | **14** | **13** | **14** |
| **Plan total** | **68** | **79** | **49** |

Held outside the totals: MV-8 v1 (§3.2, awaiting an explicit user decision).
Excluded from the totals: the 13 TOO CLOSE versions and the not-on-disk /
not-a-master items in §3.3.
