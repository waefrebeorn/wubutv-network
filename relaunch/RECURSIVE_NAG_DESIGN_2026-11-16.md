# RECURSIVE-NAG DESIGN — WuBuTV Relaunch Release Engine
2026-11-16 · Design + spec only (no crons created, nothing posted, no job bodies edited)
Authority: user decree 2026-11-16 (msg 516, confirmed in main chat + Telegram msg 518):
"never ask. setup nags to recursively learn and auto fire and use feedback — it is tv
station time, back to uploads as you make them, all rejected ones were accepted for
upload, check threads to not double post, i give you perms to post all things now,
plan and maximize to best use music videos release for lore." Plus msg 518's
REUSED-CONTENT GUARDRAIL (§4.3 — standing law, woven through §§1–3).

---

## 0. What already exists (the estate this design builds on)

- **MV nag ladder (LIVE):** kickstand 1m/5m/10m/15m/25m, delivery nag 1m, cannon-firing
  10m, volley-firing 1m, encode-size 5m, coordinator revive detector 5m, report watch
  10m, crosscheck 1h, meta-nag 1h, sprint heartbeat watch 5m + the 53-task
  `heartbeat_whitelist.json` registry. These watch PRODUCTION. None of them post.
- **Posting trees (ALL DISABLED at the 2026-11-08 shutter, bodies intact on disk):**
  - TikTok (goal `wubutv-tiktok-channel-operation`): kickstand-nag 1m (the sole steering
    job; browser-session uploader, strict series order, session lock, 30-min governor
    floor), performance-review daily (a proto-learning loop: reads metrics, throttles
    pace, could self-reschedule), post-verify 10m, ledger-audit 30m, dedup-recon 6h,
    crosspost-dedup-guard 1h, retry-hammer 3m + retry-escalation 1h (episodes-only decree
    killed these — see §2), episode-poster 2h, commercial-poster 4h (killed by decree).
  - Instagram (goal `instagram-reel-distribution`): reel-poster 30m (API, `post_next.sh`),
    episode-poster 1h, queue-feeder 15m, rate-guard 5m, post-verify 30m, ledger-audit 1h,
    pause-reset daily 00:05. Shared state: `instagram/DAILY_COUNT.json`, `PAUSE_FLAG`,
    `RATE_LIMIT_UNTIL` (bounded 6h backoff — the good pattern).
  - Threads (goal `wubutv-threads-video-distribution`): video-poster lanes A+B 1h offset
    30m (API, `post_next.sh`), episode-poster 1h, queue-feeder 30m, post-verify 1h,
    ledger-audit 2h, pause-reset daily. Shared state: `threads/DAILY_COUNT.json`,
    `PAUSE_FLAG` (present on disk right now, dated to the shutter — must be cleared by
    the relaunch audit, §5 step 0, not blindly).
- **Ledgers (the truth the old system already keeps):** `tiktok/TIKTOK_POSTS.md`,
  `instagram/INSTAGRAM_POSTS.md` + `INSTAGRAM_EPISODES.md`,
  `threads/THREADS_POSTS.md` + `THREADS_EPISODES.md`, per-MV `*_DELIVERED.flag` +
  GATE_LOG/TAKE_HISTORY under `musicvideo/MV-*/`, `assembly/ASSEMBLY_LOG.md`,
  `station/STATION_COLLECTION.md`. Frozen at the shutter: TikTok through ST-079
  (ST-078/ST-079 hand-posted 2026-11-12 at user request), IG/Threads through B-1266…B-1288
  (2026-10-23).
- **Lore source:** `research/WUBU_LORE_AND_LONG_ARCS_2026-10-27.md` — ARC-1 "The One
  Viewer" (6 chains, the spine), ARC-2 "The Roster That Keeps Everyone" (5 chains),
  ARC-3 "The Count" (5 chains); chains interleave in rotation, never two from one arc
  back-to-back; thread states OPEN → DEVELOP → PAYOFF; canon = what shipped.
- **Catalogue to release:** MV-2…MV-21 masters (MV-18/19/20 delivered, awaiting verdict;
  MV-21 approved 85%), the five morphed-show E1s (HOLD ON, ON AIR, ONE SHORT, THE NIGHT
  LIST, THE LAST SEAT — all delivered 2026-11-16), station canon ST-001…ST-079 posted,
  ST-080+ pieces + the 585-piece station archive, E1M/E2M 119/119 posted (complete).

---

## 1. THE FEEDBACK LOOP

### 1.1 Signals, where each lives, who writes it

| # | Signal | Source of truth | Recorded in | Written by |
|---|--------|-----------------|-------------|------------|
| S1 | Post attempted / verified-live (URL or post ID, caption as displayed, timestamp) | The platform itself, checked fresh | Platform ledger row (`*_POSTS.md`) + `release/posted_registry.json` | Poster lane (on verify only — never on attempt) |
| S2 | Post FAILED / uncertain (script non-zero, steer timeout) | Poster run output | `release/attempts.jsonl` (append-only) | Poster lane |
| S3 | Rate limit / lock / captcha (429, platform lock, challenge) | Platform response | `release/platform_state.json` (`backoff_until`, `consecutive_429`, learned floor) + existing `RATE_LIMIT_UNTIL`/`PAUSE_FLAG` files | Rate-guard / poster lane |
| S4 | Engagement: views, likes, comments, shares, completion where exposed | IG + Threads connectors (insights/media reads); TikTok via the signed-in Studio session (browser task — parent-owned, see §6) | `release/metrics.jsonl` (one row per post per harvest: 24h, 72h, 7d snapshots) | NEW: `release-metrics-harvest` (§3.2) |
| S5 | USER VERDICT (approve / reject / star rating / "great job" / corrections) | Chat + Telegram, as recorded in `~/MEMORY.md` and daily logs | `release/verdicts.jsonl` (item id, verdict, weight, date, source quote pointer) | NEW: `release-verdict-harvester` (§3.1) |
| S6 | New content landed (master delivered, episode flag written) | Disk: `*_DELIVERED.flag`, GATE_LOG, masters/ | `release/inventory.json` (rebuilt scan) | NEW: `release-inventory-scan` (§3.3) |
| S7 | Content identity (what a file actually IS, independent of its name) | The file bytes + picture | `release/inventory.json`: md5, duration, frame count, perceptual hash of sampled frames, audio fingerprint | `release-inventory-scan` (§4.3) |
| S8 | Lore position (arc, chain, thread state of an item) | Lore bible + per-show/episode docs | `release/inventory.json` lore fields + `release/arc_state.json` (next chain owed per arc) | Inventory scan seeds; Conductor (§3.4) advances |

### 1.2 How a nag consumes the signals — the ranking function

One file is the queue: **`release/release_queue.json`** — one entry per (item × platform),
each with a computed `score` and a `state` (`queued | held-verdict | held-guardrail |
held-backoff | posted | blocked-dup`). The **Release Conductor** (§3.4) recomputes scores
on every run; poster lanes only ever take the head entry for their platform whose state
is `queued`. Ranking, in strict priority order (higher rule wins outright, not weighted):

1. **User verdict (S5) outranks everything.** An item the user praised/approved jumps to
   the head of its platform queue; an item the user rejected is `held-verdict` UNLESS it
   clears the §4.3 reused-content guardrail, in which case it queues as an explicitly
   labeled alternate take. A one-star verdict (cf. HOLD ON E1, msg 513) demotes the item
   below all unrated new work but does not delete it — msg 516 accepted all rejected
   pieces for upload, so demotion ≠ exclusion.
2. **Lore-arc order (S8).** Among verdict-neutral items, the queue follows the lore
   bible's rotation: ARC-1 → ARC-2 → ARC-3 → ARC-1…, OPEN before DEVELOP before PAYOFF
   within an arc, and an arc's next chain may not post until its previous chain is posted
   on at least one platform. MVs slot into arcs by their lore function (the designated
   MV-show ON AIR carries MV premieres in-story; standalone MV releases are tagged to
   the arc whose current chain they thematically serve — the Conductor reads the tag
   from inventory, it does not invent tags).
3. **New work before catalogue.** A master delivered in the last 24h ("uploads as you
   make them") outranks backlog catalogue of equal verdict/arc standing.
4. **Engagement learning (S4) — the only metric input, and it is bounded.** Within the
   same verdict + arc tier, items sharing features with high performers (per
   `metrics.jsonl`: format, first-second BLAM class, tag set, post hour) rank up;
   features from two consecutive near-zero-FYP posts rank down. Metrics may ONLY reorder
   inside a tier — they can never promote an item over a verdict or an arc obligation,
   and never demote new work below catalogue. This is the TikTok performance-review
   governor generalized, with its evidence bar kept: a feature counts only after it
   replicates across ≥3 posts.
5. **Cadence state (S3).** A platform in backoff contributes no head entry at all
   (its queue waits; other platforms keep firing — reroute, never hammer).

Every score change writes its reason (`verdict | arc | new | metric:<feature> | backoff`)
into the queue entry, so any ranking is auditable after the fact. The queue file is
rewritten whole, via the standing JSON rule (§4.1).

---

## 2. AUTO-FIRE — revive vs rebuild, lane by lane

### 2.1 Revive as-is (bodies are correct; only `enabled` flips + a queue-source patch)
- **Instagram reel-poster 30m + episode-poster 1h** — API lanes, ledger-correct,
  bounded-backoff pattern already right. Patch: replace "newest unposted bumper" pick
  with "head of `release_queue.json` for instagram". Keep rate-guard 5m, post-verify
  30m, ledger-audit 1h, pause-reset daily.
- **Threads lanes A+B 1h** — same patch (head-of-queue pick). Keep post-verify 1h,
  ledger-audit 2h, pause-reset daily. **Threads is the double-post-critical platform**
  (user: "check threads to not double post"): lane A and B must both take the shared
  Threads session lock (new, §4.2) and both must pass the §4.2 pre-post platform check.
- **TikTok kickstand-nag 1m** — revive as the sole TikTok steering job, with three
  patches: (a) pick source becomes head-of-queue instead of strict STATION_COLLECTION
  order (the Conductor now owns ordering, lore-first); (b) the 30-min governor floor
  becomes a *learned* floor read from `platform_state.json` (floor may only widen on
  governor evidence, §3.5, and may narrow back only after 7 consecutive clean days —
  the old performance-review rule, kept verbatim); (c) the episodes-only restriction is
  lifted per msg 516 — MVs and show episodes are postable items; 10s bumpers remain
  unpostable as standalone uploads (they are CDN base clips; nothing in msg 516 reverses
  that, and posting them was never the lore play).

### 2.2 Rebuild (do NOT revive — their logic contradicts standing law)
- **tiktok-retry-hammer 3m + retry-escalation 1h** — built to hammer a failed upload
  every 3 minutes. Standing law now: 429/lock → back off and reroute, never hammer;
  ST-077's Threads 429 is never-retry. Their function is replaced by the Conductor's
  backoff state + the poster lanes' own single-retry-once rule. Leave disabled forever;
  note in their goal's state file that they are superseded.
- **commercial-poster lanes (TikTok 4h / IG 3h / Threads 3h)** — commercials were a
  shutter-era category; the relaunch queue treats every item uniformly by verdict + arc.
  Leave disabled; any commercial-format piece enters via inventory like everything else.
- **queue-feeder jobs (IG 15m / Threads 30m)** — they staged "newest unposted" into a
  staging dir; the Conductor + inventory scan replace staging entirely. Leave disabled.
- **tiktok-episode-poster 2h** — duplicates the kickstand-nag's steering role (two
  steerers = session collisions). Leave disabled; kickstand-nag is the only TikTok hand.

### 2.3 Fire conditions (the only ways a post happens)
A poster lane fires for its platform **iff all** of these hold at run start:
1. Head queue entry for the platform is `state: queued` (Conductor put it there).
2. Platform not in backoff (`backoff_until` < now; no `PAUSE_FLAG` unless the flag's
   recorded reason has expired — flags carry reason + expiry from now on).
3. **Pre-post platform check (fresh, this run):** the item has no live post on that
   platform — checked against the platform (connector read / Studio glance), not just
   the ledger. A "posted" cell without a ledger row, or a ledger row without a live
   post, is a discrepancy the Platform-Truth Auditor (§3.3) owns; the lane posts only
   when both agree the item is unposted. (Standing rule 2026-11-04.)
4. **Identity check:** the file's on-disk md5 equals the inventory/ledger md5 recorded
   for that item. Mismatch → no post, item flips to `held-guardrail`, Auditor alerted.
   (Never post a file whose bytes differ from its ledger row.)
5. **Reused-content check (§4.3):** if the item is a rejected/superseded/alternate
   version, its inventory entry must carry `different_enough: true` AND its caption
   must carry the alternate-take label. Either missing → hard block, no post, ever,
   until a human-grade inventory review flips the flag.
6. Session/lock free (TikTok session lock; new cross-lane lock for Threads A/B and for
   IG poster vs episode-poster).
On a verified post: ledger row + registry entry + queue state `posted`, in that order,
then the lock releases. On an uncertain failure: attempt logged (S2), NO ledger row,
item stays head-of-queue, platform check on the next run decides — this is what makes
a retry safe instead of a double-post.

---

## 3. THE NEW NAGS (genuinely new mechanisms, per the standing invent-new-checks order)

### 3.1 `release-verdict-harvester` — NEW NAG 1: the verdict ear (15m, goal: wubu-music-videos-from-suno-tracks)
No existing nag reads the user's reactions as data. This one scans the newest lines of
`~/MEMORY.md`, today's + yesterday's daily logs, and the Telegram inbox tail for verdict
language attached to a known item id/title (star ratings, "approved", "rejected",
"great job", named corrections), and appends structured rows to `release/verdicts.jsonl`:
`{item, verdict: praise|approve|reject|rating:n, ts, source}`. Dedupe by (item, source
line hash). It never interprets silence as a verdict, never upgrades a metric into a
verdict, and a later verdict for the same item supersedes an earlier one (latest wins,
history kept). This is the signal that outranks metrics in §1.2 — the loop's conscience.

### 3.2 `release-metrics-harvest` — NEW NAG 2: the engagement echo (1h, goal: instagram-reel-distribution)
The old TikTok performance-review read metrics but only to throttle. This harvester
reads IG + Threads insights via the connectors for every posted item at its 24h / 72h /
7d marks and appends to `release/metrics.jsonl`: views, likes, comments, shares,
completion/retention where the connector exposes it, plus the item's feature vector
(format, BLAM class, tag set, hour, arc, chain). TikTok metrics arrive via the parent's
Studio session reads (the harvester files a request row; the parent's browser-capable
run fulfils it — a generic cron cannot drive the live browser, §6). Below 3 posts
sharing a feature, the feature is recorded but inert (§1.2 rule 4's evidence bar).

### 3.3 `release-platform-truth-auditor` — NEW NAG 3: ledger-vs-platform-vs-disk (30m, goal: wubutv-threads-video-distribution — Threads-first, covers all three)
Extends the old crosscheck idea from ledger-vs-disk to ledger-vs-**platform**-vs-disk.
Every run, rotating one platform: (a) every ledger "posted" row must resolve to a live
post on the platform (connector/Studi
...[truncated 7718 chars]