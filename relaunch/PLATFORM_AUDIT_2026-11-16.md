# PLATFORM AUDIT — 2026-11-16 (WuBuTV relaunch baseline)

Read-only audit. Nothing posted, deleted, or edited. Live checks run 2026-11-16 ~08:47–09:00 EST
via the Threads and Instagram connectors (both accounts @waefrebeorn, auth verified healthy today).
No TikTok connector exists — TikTok state is LEDGER-ONLY and marked as such.

## Catalogue (finished, on disk)

| Series | Total | Notes |
|---|---|---|
| E1M episodes | 60 | assembly/e1m_001–060 |
| E2M episodes | 59 | assembly/e2m_001–059 |
| ST station episodes | 79 | station/episodes/station_ep001–079 |
| New-era pilots | 5 | THE MACHINE, THE TENTH SECOND, THE ROSTER, THE COUNT, THE LAST SEAT (2026-11-15) |
| New-era E2s | 5 | one per show (2026-11-15) |
| Morph E1s | 5 | ON AIR, HOLD ON, THE NIGHT LIST, ONE SHORT, THE LAST SEAT (2026-11-16) |
| Music videos | 20 | MV-2 … MV-21, all delivered (MV-1 is intake-only, no video) |
| Bumpers | 1,123 files | bumpers/ on disk |
| Commercials | 344 files | commercials/ on disk |

## TikTok — @waefrebeorn (LEDGER-ONLY, no connector)

Ledger: `tiktok/TIKTOK_POSTS.md` — 294 posted rows, frozen at the 2026-11-08 shutter.

- E1M 60/60 posted · E2M 59/59 posted · ST 79/79 posted. **Episodes complete — 0 unposted.**
- Last posted item: ST-079, 2026-11-08 ~20:52 EST.
- Bumpers: 96 agent-posted rows (B-1…B-1227 subset). The user also hand-uploaded 500+ bumpers
  personally; TikTok Studio showed 442 total posts on 2026-11-08. The 500-vs-146 recon
  discrepancy was never fully resolved (closed by user override 2026-10-15). Episode series are
  unaffected — the ledger is complete for E1M/E2M/ST.
- Commercials: 0 posted (commercial uploads were off).
- MVs / new-era / morph: no rows — nothing posted per ledger. Hand-uploads by the user cannot
  be excluded (no live check possible).
- Double-posts: none in the ledger (all 294 rows unique IDs).

## Instagram — @waefrebeorn (ledger + live-verified)

Ledgers: `instagram/INSTAGRAM_EPISODES.md` (184 rows), `INSTAGRAM_POSTS.md` (48),
`INSTAGRAM_ADS.md` (7). Frozen 2026-11-08.

- E1M 60/60 posted · E2M 59/59 posted (unique) · ST 60/79 posted (ST-018…ST-077).
- **Unposted ST: 19** — ST-001…ST-017, ST-078, ST-079.
- Bumpers: 48 posted (B-1217…B-1301 subset). Ads: 7 posted. Last episode post 2026-11-08.
- Live check: account connected, professional/creator account, 777 total posts (personal +
  WuBuTV mixed). The `posts` census endpoint returned only a partial window (565 of 777), so
  absence from that window proves nothing; direct ID lookups are authoritative. Verified live
  by direct lookup today: both copies of all 3 double-posts (below), plus ST-052/059/060
  spot checks — all present. 50 ST posts also matched the ledger inside the census window
  with exact FBID agreement. No live WuBuTV-pattern post was found that the ledger lacks.
- RATE_LIMIT_UNTIL file says 2026-11-09T06:29:50Z — expired, not a current blocker.

## Threads — @waefrebeorn (ledger + live-reconciled)

Ledgers: `threads/THREADS_EPISODES.md` (167 rows), `threads/THREADS_POSTS.md` (29),
`threads/THREADS_ADS.md` (7) — 203 claimed post IDs. Frozen 2026-11-08. Profile live today:
264 posts total (includes the user's personal text posts/replies).

- E1M 60/60 posted · E2M 59/59 posted (unique) · ST 43/79 posted (ST-034…ST-076).
- **Unposted ST: 36** — ST-001…ST-033, ST-077, ST-078, ST-079.
- ST-077: no ledger row, and absent from the live account's newest media posts covering the
  Nov 6–9 station burst — consistent with the record (429 on 2026-11-08, never retried).
- Bumpers: 29 rows / 28 unique posted. Ads: 7 posted. Last ledger post: ST-076, 2026-11-08 03:35 EST (confirmed live).

### ⚠ Six live Threads posts NO ledger knows — MV promos, 2026-11-07 → 11-09

Found in the live profile-media scan (newest 24 media posts; 18 matched the ledger exactly,
these 6 did not). All carry the "i make ai slop music videos … slopcannon" caption form:

| Posted (EST) | Content |
|---|---|
| 2026-11-09 05:29 | MV-8 "Wipe and it's still there" promo |
| 2026-11-07 16:43 | "Futurama's finished" MV promo (unnumbered) |
| 2026-11-07 10:33 | MV-6 "Sell the Lemons" promo |
| 2026-11-07 10:31 | MV-5 "Easy now Easy Now" promo |
| 2026-11-07 09:59 | MV-7 "the nobody man" promo |
| 2026-11-07 09:50 | MV-2 "toll roads are dumb" promo |

**MV-2, MV-5, MV-6, MV-7, MV-8 must be treated as ALREADY POSTED on Threads** (promo form)
by any release plan. Deeper unledgered posts below the scanned window cannot be excluded,
but every ledger-era item spot-checked (18 individual ID lookups across Oct 18–Nov 8,
incl. all duplicate pairs) was live and matched.

## Double-posts — status verified live today

9 confirmed LIVE double-posts (both copies still up; removal is the user's in-app action —
nothing was deleted):

- **Instagram (3):** E1M-034 (2026-10-30 ×2), E2M-001 (2026-10-28 + 10-30), E2M-023 (2026-10-26 + 10-30) — all 6 post IDs verified live 2026-11-16.
- **Threads (6):** B-1293 (2026-10-23, two post IDs), E2M-053 (10-24 + 10-26), E2M-056 (10-24 + 10-30),
  E2M-009 (10-27 + 11-03), E2M-010 (10-27 + 11-02), E2M-019 (10-26 + 11-04) — all 12 post IDs verified live 2026-11-16.
- **Already handled:** Instagram E2M-049 and E2M-024 second copies are marked archived
  (2026-10-27 / 2026-11-03) — one live copy each, not live doubles.
- TikTok: none in ledger.
- Note: MEMORY.md says "exactly 10 known double-posts"; ledgers + the final dedup guard
  (2026-11-08 23:38 EST) support 9 live + 2 archived. The 1-count difference is not resolvable
  from the ledgers — likely an archived copy counted in the older figure.

## Unposted inventory — what the release plan can draw from (per platform)

| Content | TikTok | Instagram | Threads |
|---|---|---|---|
| E1M / E2M episodes | 0 | 0 | 0 |
| ST episodes | 0 | **19** | **36** (incl. ST-077, see blocker) |
| New-era pilots | 5 | 5 | 5 |
| New-era E2s | 5 | 5 | 5 |
| Morph E1s | 5 | 5 | 5 |
| Music videos (MV-2…MV-21) | 20* | 20 | **15** (MV-2/5/6/7/8 already promo-posted) + 1 unnumbered already posted |
| Bumpers unposted (of 1,123 files) | ~1,027 agent-side* | ~1,075 | ~1,095 |

\* TikTok figures are ledger-only; user hand-uploads may already cover some MVs/bumpers there.

## Blockers & cautions

1. **Threads ST-077** — hit a final 429 on 2026-11-08 and was never retried under a standing
   rule. Posting it now must be a deliberate plan decision, not a lane default.
2. **Threads PAUSE_FLAG** still sits in `threads/` and DAILY_COUNT files are stale
   (2026-11-08) on Threads/IG — lanes must be re-audited before re-enabling, not blindly restored.
3. **TikTok has no API/connector** — posting runs through a browser session (kickstand-nag was
   sole uploader, strict series order, 9/hr, 6-min floor). No live verification is possible;
   the user's hand-upload history (500+ bumpers, Studio total 442) is only partially reconciled.
4. **Instagram census caveat** — the connector's post-list endpoint returned a partial window
   (565/777, with a contiguous ST-052…061 gap that direct lookups proved live). Any future
   IG verification must use direct ID lookups, not list absence.
5. No account locks, no expired auth: Threads + Instagram connectors both authenticated and
   read live today. No current rate limit on either (IG's last limit expired 2026-11-09).

## Threads verdict

**SAFE TO POST — with the promo baseline applied.** No ledger-claimed Threads post was found
missing; the only conflicts are the 6 unledgered MV promos above, which are now part of the
baseline. Post nothing from {MV-2, MV-5, MV-6, MV-7, MV-8} to Threads as if new, and treat
ST-077 as a named exception.
