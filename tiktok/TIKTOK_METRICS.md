# TikTok Metrics Log

Time-series record of the weekly `tiktok-performance-review` checks. One entry
per check. Views/likes/comments/shares are per-post as returned; engagement
figures from Studio vs the public post page are kept separate when they differ.
A missing value is unknown, never zero. Post ages are computed from the
ledger's "Posted (local)" column against the check timestamp (America/New_York).

Tag sets: A=#WuBuTV #deadpan #skit #absurdist · B=#WuBuTV #dryhumor
#originalseries #weird · C=#WuBuTV #deadpancomedy #shortfilm #surreal ·
D=#WuBuTV #comedy #indiefilm #strange. Caption shapes: 2-beat (two short
sentences), pair (two fragments), decl (single declarative).

## 2026-10-15 ~09:52 EDT (first check; account @waefrebeorn, 1796 followers, 28.6K likes)

| Bumper | Title | Age | Tag set | Caption shape | Views | Likes | Comments | Shares | For-You % | Source |
|--------|-------|-----|---------|---------------|-------|-------|----------|--------|-----------|--------|
| B-501 | The Tarp Pull | ~6.4h | A | 2-beat | 171 | 0 | 0 | 1 (post page; Studio showed 0) | 98.9% | Studio views+FYP; post page engagement |
| B-502 | The Newspaper Box | ~5.7h | B | pair | 106 | 0 | 0 | 0 | 98.2% | Studio views+FYP; post page engagement |
| B-503 | The Returned Ladder | ~5.6h | C | decl | 107 | 0 | 0 | 0 | 98.4% | Studio views+FYP; post page engagement |
| B-1 | Ident | ~5.0h | D | decl | 83 | 0 | 0 | 0 | n/a (<100 views) | Studio views; post page engagement |
| B-964 | The Tide Mark | ~1.4h | C | pair | 90 | 1 | 0 | 0 | n/a (<100 views) | Studio views+like; post page engagement |

Data notes:
- Studio engagement tabs showed "Your video data is being processed" for all
  five — likes/comments/shares came from the public post pages, not Studio.
- B-501 share discrepancy (Studio 0 vs post page 1, verified twice on the page)
  is treated as Studio processing lag; the post-page value is recorded.
- Studio withholds the For-You traffic-source breakdown until a video reaches
  100 views (hence B-1 and B-964 show n/a).
- B-964 received its first like (~09:51 EDT, a like notification arrived during
  the check) — earliest engagement event on the channel's agent-posted videos.
- No video showed 0 views; no distribution anomaly observed.

## 2026-10-17 ~09:55 EDT (daily governor run #2 at 30-min floor; account @waefrebeorn, 1.8K followers, 29K likes, 235 posts in Studio)

GOVERNOR: NO ACTION. This run's median views/post = 9 (18 posts, ages 4.9–14.7h) vs previous run's median = 1 — a rise, not a >40% drop. For-You % healthy on all 3 observable posts (97.3–98.3%, matching the pre-collapse 98.2–98.9% band). The FYP-decay clause cannot fire: 15/18 videos are below 100 views, where Studio withholds the breakdown (unknown, never zero). Distribution is partially recovered at the 30-minute floor; the 9/hour reinstatement (user order 2026-10-17 06:53 EDT) has posted nothing yet — the operation has been parked since 07:37 EDT on the B-1112 target_blocked hair-trigger. Clean-day counter: 1 (at the 30-min floor; review stays daily until 7 clean days).

| Bumper | Title | Age at check | Tag set | Caption shape | Views | Likes | Comments | Shares | For-You % | Source |
|--------|-------|--------------|---------|---------------|-------|-------|----------|--------|-----------|--------|
| B-43 | The Parade | ~4.9h | A | 2-beat | 4 | 1 | 0 | n/a | withheld (<100 views) | Studio list table |
| B-1113 | The Prop Shelf | ~5.6h | C | decl | 5 | 1 | 0 | n/a | withheld (<100 views) | Studio list table |
| B-42 | The Election | ~6.6h | D | decl | 6 | 1 | 0 | n/a | withheld (<100 views) | Studio list table |
| B-1114 | The Closed Stacks | ~7h | C | decl | 6 | 1 | 0 | n/a | withheld (<100 views) | Studio list table |
| B-41 | The Market Update | ~7.6h | B | 2-beat | 1 | 1 | 1 | n/a | withheld (<100 views) | Studio list table |
| B-1110 | The Lunchbox | ~8.2h | C | decl | 1 | 1 | 0 | n/a | withheld (<100 views) | Studio list table |
| B-39 | The Emergency Broadcast | ~8.7h | D | 2-beat | 1 | 1 | 1 | n/a | withheld (<100 views) | Studio list table |
| B-1093 | The Flour Scoop | ~9.4h | C | decl | 1 | 1 | 0 | n/a | withheld (<100 views) | Studio list table |
| B-40 | The Moment of Silence | ~10h | A | 2-beat | 3 | 1 | 0 | n/a | withheld (<100 views) | Studio list table |
| B-1086 | The Boot Jack | ~10.6h | C | decl | 12 | 1 | 0 | n/a | withheld (<100 views) | Studio list table |
| B-37 | The Penny, Part 2 | ~11.5h | B | 2-beat | 45 | 1 | 0 | n/a | withheld (<100 views) | Studio list table |
| B-1076 | The Lightning Rod | ~11.6h | C | 2-beat | 16 | 1 | 0 | n/a | withheld (<100 views) | Studio list table |
| B-38 | The Coffee | ~12h | C | 2-beat | 50 | 1 | 1 | n/a | withheld (<100 views) | Studio list table |
| B-1070 | The Snack Drop | ~12.7h | B | 2-beat | 57 | 1 | 0 | n/a | withheld (<100 views) | Studio list table |
| B-36 | The Traffic Report | ~13h | A | 2-beat | 116 | 1 | 0 | n/a | 98.3% | Studio list table; per-video traffic sources |
| B-1062 | The Wound Clock | ~13.5h | C | decl | 109 | 2 | 0 | n/a | 97.3% | Studio list table; per-video traffic sources |
| B-35 | The Stapler | ~14.1h | D | 2-beat | 18 | 1 | 1 | n/a | withheld (<100 views) | Studio list table |
| B-1053 | The Couched Sheet | ~14.7h | C | pair | 100 | 0 | 0 | n/a | 98.0% | Studio list table; per-video traffic sources |

Data notes:
- All 18 posts went up at ~30–40 min spacing (the 30-min floor) between 2026-10-16 19:14 EDT and 2026-10-17 05:04 EDT, after the user lifted the first governor park ~19:06 EDT 10-16.
- Shares: Studio's Content list has no Shares column — n/a everywhere, never zero. Engagement tabs on the per-video pages were reachable this time; search-queries section showed "being processed."
- Per-video traffic sources for the 3 ≥100-view posts: For You 97.3–98.3%, Personal profile 1.0–1.8%, Search 0–1.0%, everything else <0.1%. No distribution anomaly on these.
- B-43 moved 3 → 4 views during the read (real-time fluctuation). No captcha, no login challenge, nothing changed on the account (read-only).
- Posted timestamps are Studio's displayed times (EDT); ages computed against check ~09:55 EDT.

---

## 2026-10-16 ~10:16 EDT (first daily governor run; account @waefrebeorn, 1.8K followers, 29K likes, 217 posts in Studio)

GOVERNOR FIRED: median views/post 106 → 1 (~99% drop vs 2026-10-15 run; 40% tripwire beaten). 48 consecutive posts at 0–9 views. 9/hour cadence SUSPENDED: 48–72h park (resume ≥ 2026-10-18 09:49 EDT), then 30-min floor. Review stays DAILY until 7 consecutive clean days at the new pace.

| Bumper | Title | Age at check | Tag set | Caption shape | Views | Likes | Comments | Shares | For-You % | Source |
|--------|-------|--------------|---------|---------------|-------|-------|----------|--------|-----------|--------|
| B-34 | The Breaking News Sounder | ~0.4h | A | decl | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1023 | The Tide Table | ~0.7h | C | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-33 | The Phone Call | ~0.9h | A | decl | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1024 | The Laundry Line | ~1.1h | C | decl | 1 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-32 | The Interview | ~1.3h | B | pair | 2 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1025 | The Change Cup | ~1.5h | A | decl | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-31 | The Replay | ~1.7h | D | pair | 1 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1026 | The Opening Time | ~2h | C | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-30 | The Halftime | ~2.2h | D | decl | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1027 | The Boarding Bell | ~2.6h | C | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-29 | The Sports Desk | ~2.7h | B | pair | 1 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1029 | The Stamped Ticket | ~2.9h | C | pair | 8 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-28 | The Commercial Break | ~3.1h | D | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1030 | The Covered Statue | ~3.3h | C | pair | 1 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-27 | The MEGA Vault | ~3.5h | D | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1032 | The Parked Bicycle | ~3.7h | A | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-26 | The Storage Unit | ~4.2h | B | pair | 1 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1033 | The Latched Field Gate | ~4.4h | C | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-24 | The Microphone | ~4.6h | D | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1034 | The Rooftop Antenna | ~4.8h | C | pair | 1 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-23 | The Applause Sign | ~5h | D | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1035 | The Hourglass | ~5.2h | C | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-25 | The Curtain | ~5.3h | B | pair | 6 | 1 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1036 | The Kneaded Dough | ~5.8h | C | pair | 5 | 2 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-22 | The Orb Staff | ~6h | A | pair | 1 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1038 | The Bailed Dinghy | ~6.3h | C | pair | 9 | 1 | 1 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-21 | The Audience | ~6.4h | B | pair | 1 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1039 | The Drawn Pail | ~6.6h | D | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-20 | The Podium | ~6.8h | C | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1042 | The Turned Compost | ~6.9h | C | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-19 | The Envelope | ~7.1h | D | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1040 | The Split Log | ~7.3h | C | pair | 1 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-18 | The Drum Roll | ~7.5h | A | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1037 | The Stropped Razor | ~7.6h | ? | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-17 | The Spotlight | ~7.8h | B | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1031 | The Set-Down Crate | ~8h | D | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-16 | The Penny Ledger | ~8.2h | C | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1028 | The Forgotten Umbrella | ~8.5h | C | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-14 | The Vending Machine | ~8.7h | A | pair | 1 | 1 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-15 | Unit 47 | ~9h | B | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1021 | The Booth Window | ~9.2h | D | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-13 | After These Messages | ~9.6h | B | decl | 1 | 1 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1015 | The Filled Pitcher | ~9.7h | C | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-12 | Station Identification | ~9.8h | A | pair | 6 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1012 | The Anemometer | ~10h | C | pair | 1 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-11 | Please Adjust Your Set | ~10.3h | B | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1006 | The File Drawer | ~10.5h | D | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-10 | Sign-Off | ~10.7h | B | pair | 0 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1003 | The Bay Door | ~10.9h | C | pair | 48 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1001 | The Floor Indicator | ~11h | A | pair | 64 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1000 | The Paid Lot | ~11.1h | ? | pair | 69 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-993 | The Shelved Weight | ~11.4h | ? | pair | 84 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-9 | Intermission | ~12.6h | D | pair | 102 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-988 | The Sundial | ~13h | C | pair | 101 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-8 | Test Pattern | ~13.3h | C | decl | 102 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-985 | The Sandwich Board | ~13.5h | B | pair | 119 | 1 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-7 | Sign-On | ~13.8h | A | pair | 76 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-980 | The Pigeon | ~14h | D | pair | 193 | 3 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-6 | The Scoreboard | ~14.4h | A | pair | 85 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-978 | The Turned Pike | ~14.6h | C | pair | 106 | 1 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-5 | We'll Be Right Back | ~14.8h | D | pair | 47 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-975 | The Cast Slug | ~15h | C | pair | 113 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-4 | Stay Tuned | ~15.1h | D | pair | 85 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-973 | The Fed Doves | ~15.3h | C | pair | 171 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-3 | News Next | ~15.5h | D | pair | 133 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-963 | The Toll Bar | ~16h | B | pair | 163 | 1 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-2 | Nobody Won | ~21.6h | A | pair | 124 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-964 | The Tide Mark | ~25.8h | C | pair | 126 | 2 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-1 | Ident | ~29.4h | D | decl | 91 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-503 | The Returned Ladder | ~30h | C | decl | 122 | 0 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-502 | The Newspaper Box | ~30.1h | B | pair | 119 | 1 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |
| B-501 | The Tarp Pull | ~30.7h | A | 2-beat | 265 | 1 | 0 | n/a | n/a (<100 views, withheld) | Studio list table; per-video analytics for B-1029 |

Data notes:
- Posted timestamps are Studio's displayed times (EDT); ages computed against check ~10:13 EDT.
- Shares: Studio's Posts list has no Shares column; per-video Engagement tab shows "being processed" with no numeric values — n/a everywhere, never zero.
- For-You %: withheld by Studio below 100 views; none of the 14 newest (the governor-relevant set) reached 100, so the FYP clause of the governor rule could not be evaluated.
- B-1029: list table showed 4 views, per-video analytics showed 8 — per-video value preferred (real-time). All other newest-14 rows matched.
- Caption shapes derived from the ledger's "Caption used" column: pair = two fragments, decl = single declarative, 2-beat = two short sentences.

## 2026-10-23 ~19:55 EDT (daily governor run #3 — first post-resume check; account @waefrebeorn, 1.8K followers, 29K likes, 239 posts in Studio)

GOVERNOR: NO ACTION. This run's median views/post = 254 (2 posts, ~130h old) vs previous run's median = 9 — a rise, not a >40% drop. For-You % healthy on both observable posts (99.4%, 98.3% — the 99.4% is the highest FYP share recorded for any agent-posted video). The near-zero-FYP clause cannot fire: both posts are ~99%. Both posts are the pre-stop tail (posted 2026-10-18 ~01:22/02:13 EDT, ~5.3 days before this check) — the first near-7-day maturity read. No new-regime posts exist yet (operation resumed ~19:42 EDT today, minutes before this check). Clean-day counter: 1 (unchanged — it resumes building on new-regime posts).

| Bumper | Title | Age at check | Tag set | Caption shape | Views | Likes | Comments | Shares | For-You % | Source |
|--------|-------|--------------|---------|---------------|-------|-------|----------|--------|-----------|--------|
| B-1227 | The Cone at Half | ~130.5h | B | pair | 333 | 7 | 0 | 0 | 99.4% | Studio list table + per-video analytics |
| B-1204 | The Unit's Click | ~129.7h | A | 2-beat | 175 | 3 | 0 | 0 | 98.3% | Studio list table + per-video analytics |

Data notes:
- The Engagement tab rendered its graph with no totals this run — likes/comments/shares came from the per-video analytics header icons, which matched the list table for views/likes/comments. Shares returned real zeros (0), not "being processed": first run where shares were measurable rather than withheld — a share baseline of 0 at ~130h is the honest starting point.
- B-1227's "Content under review" + auto-"Only me" anomaly at publish left no residue: privacy Everyone, no badge, 333 views, 99.4% FYP.
- B-1204's traffic-source page named "b.1204" as its top search query (100% of its 0.6% search share — ~1 view). Noise, not signal.
- Studio post count grew 235 → 239 (+4) since the 2026-10-17 check with only 2 new ledger rows (B-1227, B-1204) — two Studio posts have no ledger row. Open question for tiktok-dedup-recon.
- No captcha, login wall, or rate-limit encountered during this read; nothing uploaded, posted, edited, or changed. Public-page fallback not needed.

---

## 2026-10-24 ~09:50 EDT (daily governor run #4 — first new-regime review; account @waefrebeorn, 261 posts in Studio, 0 drafts)

GOVERNOR: NO ACTION — on the age-matched read. Raw median views/post = 51 (21 posts) vs previous run's 254 — a −79.9% raw drop that does NOT fire the governor, because the previous median was 2 bumper posts at ~130h old and this cohort is 21 posts at 0.5–14.1h old in a different format (1-min soap episodes). Per the loop's standing matched-age rule, a cross-age, cross-format raw comparison is not a distribution signal. Age-matched: the 10–14.1h subset (n=18) has median 53, inside the healthy-era 10–15h band (47–193, median ~93) and above the 2026-10-17 partial-recovery median (~47.5). FYP clause cannot fire: only 1 post reached 100 views and it reads 99.5% For You (a channel record, above B-1227's 99.4%); all others are withheld (<100 views), which is not near-zero FYP. Clean-day counter: 1 → 2 (first clean day on new-regime posts). Review stays DAILY; no pacing change, no park.

| Post | Title | Age at check | Tag set | Caption shape | Views | Likes | Comments | Shares | For-You % | Source |
|--------|-------|--------------|---------|---------------|-------|-------|----------|--------|-----------|--------|
| B-1205 | The New Datum | ~14.1h | D | pair | 180 | 2 | 0 | 0 | 99.5% | Per-video analytics |
| B-1112 | The Wall Clock | ~13.9h | C | decl | 77 | 1 | 0 | 0 | withheld (<100 views) | Per-video analytics |
| B-44 | Please Stand By | ~13.6h | A | 2-beat | 45 | 1 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| B-45 | The Card Trick | ~13.4h | B | 2-beat | 52 | 1 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-001 | The Long Minute | ~13.1h | A | decl | 72 | 1 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-002 | The Rapid Six | ~12.9h | B | decl | 61 | 1 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-003 | The Short Count | ~12.7h | C | decl | 55 | 0 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-004 | The Quick Cut | ~12.5h | D | decl | 51 | 1 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-005 | The Hard Minute | ~12.3h | A | decl | 57 | 0 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-006 | The Craft Six | ~12.0h | B | decl | 36 | 0 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-007 | The Honed Six | ~11.8h | C | decl | 51 | 2 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-008 | The Punch Clock | ~11.5h | D | decl | 13 | 0 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-009 | The Sharp Six | ~11.3h | A | decl | 41 | 1 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-010 | The Punch Line | ~10.9h | B | decl | 30 | 1 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-011 | The Snap Count | ~10.6h | C | decl | 59 | 0 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-012 | The Quick Turn | ~10.2h | D | decl | 64 | 1 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-013 | The Quick Six | ~10.0h | A | decl | 54 | 0 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-014 | The Night Shift | ~9.8h | B | decl | 25 | 1 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-015 | The Returned Six | ~7.3h | C | decl | 0 | 0 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-016 | The Quick Draw | ~1.2h | D | decl | 0 | 0 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |
| E1M-017 | The Trade Six | ~0.5h | A | decl | 0 | 0 | 0 | 0 | withheld (<100 views) | Studio list table + per-video analytics |

Data notes:
- Read via signed-in TikTok Studio, 09:47–09:53 EDT (browser task, read-only). No login wall, no captcha, nothing uploaded/posted/edited/changed. List-table figures matched per-video analytics figures for every video checked both ways; no counts moved mid-read. Studio list search did not filter on typed text, so B-1205/B-1112 were confirmed via their direct per-video analytics pages.
- Shares are real numeric 0s from per-video analytics headers this run (not "being processed") — 0 shares on all 21 posts, extending the 0-share baseline from the 2026-10-23 run. Comments 0 on all 21. Likes total 14 across 21 posts (0.67/post).
- B-1205's traffic breakdown: For You 99.5%, Other 0.5%. No "Content under review" badge and no Only-me privacy seen; checked rows showed Privacy "Everyone".
- Watch items (not triggers): E1M-015 at 0 views / 7.3h (overnight 02:30 post — re-check at maturity; a single-post zero, not a consecutive-post pattern); E1M-008 at 13 views / 11.5h (low outlier vs 10h+ siblings at 25–77); E1M-016/017 zeros at 1.2h/0.5h (young enough that Studio lag is plausible — re-check next run).
- Studio count 261 (+22 since the 2026-10-23 run's 239) vs 21 newly measured rows: the standing unledgered-post question persists — this interval's delta suggests ~1 additional Studio post with no ledger row, plausibly E1M-018 if it landed before the 09:47 read (the upload window was steering E1M-018 ~09:30). Verify next run; do not assume.
- Episode captions share a single shape ("WuBuTV 1-minute episode." declarative) in this cohort, so no caption-shape comparison is possible yet; tag-set medians (A 54, B 33, C 53, D 32) are age-skewed (A holds the oldest episode, D the youngest) with n=4–5 — the null bank stands.
