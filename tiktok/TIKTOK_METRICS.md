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

## 2026-10-25 ~10:05 EDT (daily governor run #5 — PROXY READ, formal Studio comparison incomplete; account @waefrebeorn)

GOVERNOR: NO ACTION on proxy evidence; NO clean-day credit. Three signed-in TikTok Studio browser tasks were run read-only (task ids browser-task:07930aed…, browser-task:621946ac…, plus a re-ask of the first) and each worked through Studio pages (Content list, then per-video analytics pages up to E1M-034 and back to the list), but none of their final result messages ever arrived in this run's context — the windows closed with no table delivered. Rather than report no data, the cohort was re-read from the public post pages (browser.open on the ledger's verbatim video URLs, ~10:03–10:05 EDT). Those figures are public-page PLAYS, not Studio views, and carry no For-You % — so the governor's two formal inputs (Studio median views/post, FYP %) are both unavailable this run. What the proxy does show is no collapse signal: raw public-play median 61 (n=21) vs the previous run's Studio median 51, and the age-matched 10–24h band (E1M-018…026, n=9) median 65 vs the previous run's 10–14.1h Studio median 53. Instruments differ, so this is directional only — it does not fire, and it does not certify, the governor. FYP clause cannot fire: no post reaches 100 plays (max 96), so even a Studio read would withhold every FYP breakdown; withheld is not near-zero. Clean-day counter HOLDS at 2 (not advanced on a proxy read). Review stays DAILY; no pacing change, no park. The Studio-result delivery failure is itself the run's blocker to report — the next run must obtain a Studio read before any clean-day credit or throttle decision.

| Post | Title | Age at check | Tag set | Plays (public page) | Likes | Comments | Shares | Saves | Source |
|--------|-------|--------------|---------|---------------------|-------|----------|--------|-------|--------|
| E1M-018 | The Forge Six | ~22.6h | B | 34 | 0 | 0 | 0 | 0 | Public post page |
| E1M-019 | The Picked Pressure | ~15.1h | C | 38 | 1 | 0 | 0 | 0 | Public post page |
| E1M-020 | The Cargo Turn | ~14.4h | D | 69 | 1 | 0 | 0 | 0 | Public post page |
| E1M-021 | The Fresh Six | ~13.0h | A | 66 | 1 | 0 | 0 | 0 | Public post page |
| E1M-022 | The Six Strike | ~11.7h | B | 65 | 0 | 0 | 0 | 0 | Public post page |
| E1M-023 | The Rapid Swing | ~11.0h | C | 71 | 1 | 0 | 0 | 0 | Public post page |
| E1M-024 | The Swift Six | ~10.8h | D | 19 | 0 | 0 | 0 | 0 | Public post page |
| E1M-025 | The Drop Six | ~10.3h | A | 64 | 0 | 0 | 0 | 0 | Public post page |
| E1M-026 | The Coil Six | ~10.1h | B | 68 | 0 | 0 | 0 | 0 | Public post page |
| E1M-027 | The Toast Six | ~9.4h | C | 25 | 0 | 0 | 0 | 0 | Public post page |
| E1M-028 | The Power Hour | ~6.5h | D | 35 | 0 | 0 | 0 | 0 | Public post page |
| E1M-029 | The Variant Minute | ~6.3h | A | 15 | 0 | 0 | 0 | 0 | Public post page |
| E1M-030 | The Speed Six | ~6.1h | B | 96 | 2 | 2 | 0 | 0 | Public post page |
| E1M-031 | The Gag Six | ~5.9h | C | 39 | 1 | 0 | 0 | 0 | Public post page |
| E1M-032 | The Jab Six | ~5.7h | D | 61 | 0 | 0 | 0 | 0 | Public post page |
| E1M-033 | The Cutaway Six | ~5.6h | A | 23 | 0 | 0 | 0 | 0 | Public post page |
| E1M-034 | The Rapid Fire | ~5.4h | B | 65 | 1 | 0 | 0 | 0 | Public post page |
| E1M-035 | The Slam Six | ~3.8h | C | 68 | 0 | 0 | 0 | 0 | Public post page |
| E1M-036 | The Snap Six | ~3.6h | D | 73 | 2 | 0 | 0 | 0 | Public post page |
| E1M-037 | The Grip Six | ~2.4h | A | 0 | 0 | 0 | 0 | 0 | Public post page, re-fetched unchanged |
| E1M-038 | The Held Open Six | ~1.4h | B | 2 | 0 | 0 | 0 | 0 | Public post page, re-fetched unchanged |
| E1M-008 | The Punch Clock | ~35.7h | D | 22 | 0 | 0 | 0 | 0 | Public post page (re-check; was Studio 13 at 11.5h) |
| E1M-015 | The Returned Six | ~31.6h | C | 61 | 1 | 0 | 0 | 0 | Public post page (re-check; was Studio 0 at 7.3h) |
| E1M-016 | The Quick Draw | ~25.5h | D | 75 | 1 | 0 | 0 | 0 | Public post page (re-check; was Studio 0 at 1.2h) |
| E1M-017 | The Trade Six | ~24.7h | A | 36 | 0 | 0 | 0 | 0 | Public post page (re-check; was Studio 0 at 0.5h) |

Data notes:
- New-cohort totals: 10 likes, 2 comments (both on E1M-030), 0 shares, 0 saves across 21 posts. E1M-030's 2 comments are the first comments on any episode-format post in this log.
- Shares stay at 0 across all 25 reads, extending the 0-share baseline from the 2026-10-23/24 runs.
- Watch items: E1M-037 at 0 plays / 2.4h and E1M-038 at 2 / 1.4h are consecutive youngest posts, but both ages carry the established young-post lag precedent (E1M-015/016/017 all read 0 young and now read 61/75/36) — a watch, not a consecutive-post pattern for the governor, and FYP is unobservable here anyway. E1M-024 (19 at 10.8h) is the cohort's low outlier against 10h+ siblings at 34–71. E1M-008 stays a confirmed slow grower (13 → 22 from 11.5h to 35.7h, instrument change noted).
- E1M-039 has no ledger row and EPISODE_COLLECTION still shows it "queued" at check time — the 09:18 EDT upload steer had not landed a post by ~10:05 EDT.
- Tag-set medians on public plays (A 23, B 65, C 39, D 61; n=5–6) are age-skewed (A holds the 0-play youngest post; B holds the 96-play high) — the null bank stands, no tag inference.
- Public-page plays track the previous run's Studio views in the same order of magnitude at matched ages (e.g. E1M-020 69 plays at 14.4h vs E1M-001 72 Studio views at 13.1h), which is why the proxy is usable as a collapse check but not as a governor-grade median.

## 2026-10-25 ~10:07 EDT — LATE STUDIO CORROBORATION (correction to the proxy read above; formal governor verdict)

The signed-in Studio browser task's report arrived after the proxy section was banked (Studio read 09:44–09:53 EDT, 2026-10-25). It confirms the proxy read almost exactly and upgrades this run to a formal Studio verdict. Studio totals at read start: 282 posts, 0 drafts, 1.8K followers, 29K likes. Per-video analytics agreed with the list table on every video; shares 0 on all 25.

- Studio median for the 21 new posts = 61 (sorted: 0, 1, 15, 19, 23, 25, 34, 35, 38, 39, 61, 64, 65, 65, 66, 68, 68, 69, 71, 71, 96) vs the previous run's Studio median 51 — a RISE, not a >40% drop. Age-matched 10–24h band (E1M-018…026) Studio median 65 vs the previous run's 10–14.1h Studio median 53 — also a rise.
- FYP % withheld on ALL 25 posts (none reached 100 views; max E1M-030 at 96) — withheld, not near-zero, so the FYP clause cannot fire.
- GOVERNOR FORMAL VERDICT: NO ACTION, and this run DOES earn clean-day credit — clean-day counter 2 → 3. Review stays DAILY (7 needed before weekly). No pacing change, no park.
- Value differences vs the public-page proxy are time progression, not contradiction: Studio read 09:44–09:53, proxy fetched ~10:03–10:05. E1M-036 Studio 71 → public 73 (+2 views in the gap); E1M-038 Studio 1 → public 2 (+1). All other 23 values identical across instruments. Prefer the Studio values for the governor record.
- New anomaly (Studio-only, not visible on public pages): E1M-020's per-video analytics page shows "Your video is unavailable to some audiences" even though the posts list shows privacy "Everyone" — banked as a watch item for the next run; its view count (69) is in the healthy band, so no action now.
- Studio delta check: 261 → 282 posts (+21) against exactly 21 new ledger rows this interval, so no NEW unledgered post this interval; the cumulative +1 unledgered post from the earlier interval persists (E1M-039 was not live at the 09:53 final check and is not the extra post).
- E1M-037/E1M-038 per-video pages noted "Your video data is being processed" for retention/search data only; their counts were shown.

## 2026-10-25 ~10:10 EDT — ADDENDUM: second Studio list-table read (duplicate delivery, one data-quality correction)

A duplicate delivery of both Studio reports arrived after the correction above. The second report (Studio Content list, ~10:03 EDT, totals 282 posts / 0 drafts) adds no new verdict information — E1M-039 still not live, no post at 100 views — but it corrects one explanation in the correction above: at ~10:03 EDT the Studio list table shows E1M-036 at 71 views while the public page at ~the same time showed 73. That 2-view gap is therefore an instrument difference (list table vs public page), NOT time progression. E1M-038's 1→2 is still consistent with time progression (per-video 09:44–09:53 = 1, list 10:03 = 2, public ~10:04 = 2). Governor verdict unchanged: Studio median 61, clean-day counter 3, review stays DAILY, no pacing change.

## 2026-10-26 ~10:05–10:14 EDT (daily governor run #6 — PROXY READ; account @waefrebeorn)

GOVERNOR: NO ACTION on a proxy read, NO CLEAN-DAY CREDIT (precedent of run #5:
a public-page proxy is not governor-grade; clean-day counter HOLDS at 3).
Studio browser task (browser-task:acaaf5c4…) worked through Studio — its
window was seen on a per-video analytics page — but closed with no result
delivered to this run. If a Studio report arrives late, it supersedes this
proxy section as a correction, as in run #5. FYP % unobservable on every post
(public pages carry no traffic source; all 26 posts are <100 plays, so Studio
would withhold the breakdown anyway) — withheld is NOT near-zero FYP, and the
FYP clause cannot fire on this read.

Raw proxy median 36 (n=26) vs run #5's proxy/Studio median 61 is a −41.0% raw
move, but it does NOT fire the governor: the loop's matched-age rule governs,
and the matched band is flat — the 10–14h subset (E1M-039…050, n=12) has median
66 vs run #5's 10–24h band median 65. The raw drop is an age-mix artifact:
this cohort's tail is much younger (E2M-004 is ~1.6h old at check) than run
#5's cohort. Within-cohort age gradient: evening band (039–050, ~10–13h) 59–78
except two lows; overnight band (051–057, ~8–10h) median 25; early-morning band
(058–E2M-004, ~2–7h) median 0. That gradient matches the established slow-start
pattern (run #5: E1M-037 0 plays at 2.4h → 63 at ~27h; E1M-038 2 → 64), so the
young tail is a WATCH item, not a decay verdict — tomorrow's check, at ~24h+,
is the one that can call it.

| Post | Title | Age at check | Tag set | Caption shape | Plays (proxy) | Likes | Comments | Shares | For-You % | Source |
|--------|-------|--------------|---------|---------------|-------|-------|----------|--------|-----------|--------|
| E1M-039 | The Floodlight Six | ~13.3h | C | decl (1-min) | 67 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-040 | The Checked Six | ~13.1h | D | decl (1-min) | 59 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-041 | The Spare Minute | ~12.7h | A | decl (1-min) | 66 | 1 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-042 | The Quick Hits | ~12.5h | B | decl (1-min) | 64 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-043 | The Six Punches | ~12.0h | C | decl (1-min) | 68 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-044 | The Punchline Six | ~11.6h | D | decl (1-min) | 78 | 1 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-045 | The Held Round | ~11.4h | A | decl (1-min) | 60 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-046 | The Second Beat | ~11.2h | B | decl (1-min) | 8 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-047 | The Rapid Six | ~11.0h | C | decl (1-min) | 40 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-048 | The Coin Six | ~10.8h | D | decl (1-min) | 69 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-049 | The Six Turns | ~10.6h | A | decl (1-min) | 66 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-050 | The Hooked Six | ~10.3h | B | decl (1-min) | 71 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-051 | The Twist Six | ~9.6h | C | decl (1-min) | 37 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-052 | The Counter Six | ~9.4h | D | decl (1-min) | 11 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-053 | The Filed Six | ~8.7h | A | decl (1-min) | 36 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-054 | The Time Six | ~8.6h | B | decl (1-min) | 8 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-055 | The Utility Six | ~8.2h | C | decl (1-min) | 25 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-056 | The Wound Six | ~8.0h | D | decl (1-min) | 21 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-057 | The Locked Six | ~7.8h | A | decl (1-min) | 36 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-058 | The Property Six | ~6.5h | B | decl (1-min) | 0 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-059 | The Theatre Six | ~6.3h | C | decl (1-min) | 1 | 1 | 0 | 0 | unobservable (public page) | Public post page |
| E1M-060 | Six Punches | ~6.2h | D | decl (1-min) | 0 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-001 | The Longer Cut | ~5.5h | A | decl (2-min) | 0 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-002 | The Harbor Ledger | ~4.7h | B | decl (2-min) | 0 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-003 | The Kept Rooms | ~2.9h | C | decl (2-min) | 1 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-004 | The Gathered Dark | ~1.6h | D | decl (2-min) | 0 | 0 | 0 | 0 | unobservable (public page) | Public post page |

Re-checks (same proxy read): E1M-020 69 plays / 1 like (unchanged from Studio
69 — the "unavailable to some audiences" banner cannot be seen from a public
page, so it stays an open Studio-only watch item); E1M-024 48 plays (was 19
proxy at run #5 — low outlier resolved upward); E1M-037 63 plays (was 0 proxy
at run #5 — slow start resolved); E1M-038 64 plays / 1 like (was 2 proxy at
run #5 — slow start resolved). Prior watch items E1M-037/E1M-038/E1M-024 are
all RESOLVED. New watch items: E1M-058, E1M-060, E2M-001, E2M-002 (0 plays at
~5–7h) and the whole 058–E2M-004 segment (median 0 at ~2–7h); E1M-046 (8 plays
at ~11h) and E1M-052/E1M-054 (11 / 8 plays at ~9h) as secondary lows.
Engagement: 3 likes total across 26 new posts, 0 comments, 0 shares — the
episode-comment drought continues (no episode comments since E1M-030).
No Studio totals available on this read (window closed without a report).

## 2026-10-26 ~09:54 EDT — LATE STUDIO CORROBORATION (correction to the proxy read above; formal governor verdict)

The Studio browser task's report (per-video reads 09:44–09:54 EDT, totals
re-confirmed on the Posts page at 09:54 EDT) arrived after the proxy section
above was banked. It matches the proxy on ALL 30 values — every Studio view
equals the public-page play count, and likes/comments/shares are identical —
so the proxy read is fully corroborated, not merely consistent. Formal
governor verdict on Studio numbers: median 36 vs previous Studio 61 (−41.0%
raw) does NOT fire, because the matched-age rule governs and the 10–14h
subset median is 66 vs run #5's 10–24h band median 65 (flat-to-rising); the
raw move is an age-mix artifact. FYP withheld on all 30 posts (every post
<100 views; Studio shows "Data will show when video views reach 100") —
withheld, not near-zero, so the FYP clause cannot fire. GOVERNOR NO ACTION
and clean-day credit APPLIES: counter 3 → 4. Review stays DAILY. No pacing
change, no park. Studio totals 308 posts / 0 drafts: +26 vs run #5's 282,
exactly the 26 new ledger rows — no new unledgered post this interval.
One Studio-only confirmation the proxy could not give: E1M-020's "Your video
is unavailable to some audiences" banner is CONFIRMED still present (appeared
on the refreshed analytics view; Posts-list privacy still Everyone) — it
moves from open watch item to confirmed standing anomaly, still with healthy
69 views, so watch, not action. No "Content under review" banner on any
checked post. Shares are real zeros (0) on all 30 posts, not withheld.

## 2026-10-28 ~09:45 EDT (daily governor run #8 — PROXY READ; account @waefrebeorn)

GOVERNOR (proxy-grade): NO ACTION, NO CLEAN-DAY CREDIT. New-post proxy median 26 (13 posts, ages 3.3–23.9h) vs run #7's Studio median 1 is a rise on paper but an age-mix artifact (run #7's cohort was mostly ≤6.8h). The matched-age rule governs: 10–14h proxy median 46 (E2M-034…038: 43/55/26/46/66) vs run #7's Studio 10–14h median 44 = +4.5%, flat-to-rising, far under the >40% drop tripwire. FYP % unobservable on public pages (no traffic source) and would be withheld in Studio anyway (max proxy plays 79 < 100) — withheld, not near-zero, so the FYP clause cannot fire. No park, no pacing change, upload_park.txt stays absent. Clean-day counter HOLDS at 4 (no credit on a proxy read, per runs #5/#6 precedent). Review stays DAILY. If the signed-in Studio browser task (browser-task:0f283c5d…) delivers a report after this banking, it supersedes this entry as a correction, as in runs #5/#6.

| Episode | Title | Age at check | Tag set | Caption shape | Plays | Likes | Comments | Shares | For-You % | Source |
|---------|-------|--------------|---------|---------------|-------|-------|----------|--------|-----------|--------|
| E2M-032 | The Sealed Hour | ~23.9h | D | decl (2-min) | 76 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-033 | The Weather Hours | ~22.2h | A | decl (2-min) | 42 | 1 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-034 | The Quiet Inventory | ~14.0h | B | decl (2-min) | 43 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-035 | The Unclaimed Hour | ~13.3h | C | decl (2-min) | 55 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-036 | The Spare Hour | ~12.5h | D | decl (2-min) | 26 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-037 | The Late Rounds | ~12.3h | A | decl (2-min) | 46 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-038 | The Numbered Gap | ~12.0h | B | decl (2-min) | 66 | 2 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-039 | The Kept Rounds | ~9.2h | C | decl (2-min) | 9 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-040 | The Kept Watch | ~9.0h | D | decl (2-min) | 4 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-041 | The Kept Order | ~8.2h | A | decl (2-min) | 7 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-042 | The Quiet Hour | ~6.9h | B | decl (2-min) | 1 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-043 | The Kept Ledger | ~3.4h | C | decl (2-min) | 0 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-044 | The Returned Hour | ~3.3h | D | decl (2-min) | 0 | 0 | 0 | 0 | unobservable (public page) | Public post page |

Re-checks (same proxy read, run #7's young tail now at ~24–31h): E2M-018 23 plays / 0 likes (was 0–1 at ≤6.8h — resolved); E2M-019 71 / 1; E2M-020 59 / 1; E2M-021 16 / 0; E2M-022 31 / 0; E2M-023 45 / 1; E2M-024 50 / 0; E2M-025 66 / 0; E2M-026 51 / 0; E2M-027 36 / 0; E2M-028 19 / 0; E2M-029 67 / 0; E2M-030 79 / 2; E2M-031 5 / 0 — UNRESOLVED, first slow-start non-resolution in the series (13/14 resolved; re-check median 47.5). E2M-031 is the run #9 watch item (re-check at ~48h+ before any verdict). Young tail E2M-039…044 (0–9 plays at 3–9h) is a WATCH item, not a verdict, per the standing rule. Engagement: 3 likes total across 13 new posts, 0 comments, 0 shares — the episode-comment drought continues (no episode comments since E1M-030). Studio-only flags NOT resolvable on this read: the unledgered second E2M-006 post and E1M-020's "unavailable to some audiences" banner remain open pending a Studio report. Context: no new ledger rows after E2M-044 (2026-10-28 06:29 EDT) at check time; the kickstand nag showed 7 consecutive failures with last success 06:34 EDT — an upload stall, not a governor signal, and not this review's remit.

## 2026-10-28 ~09:49 EDT — LATE STUDIO CORROBORATION (correction to the proxy read above; formal governor verdict)

The Studio browser task's report (read 09:44–09:49 EDT, totals re-confirmed on the Posts page at 09:49 EDT) arrived after the proxy section above was banked. It matches the proxy on ALL 27 values — every Studio view equals the public-page play count, and likes/comments are identical — so the proxy read is fully corroborated, not merely consistent. Formal governor verdict on Studio numbers: median 26 vs run #7's Studio median 1 is an age-mix artifact; matched-age 10–14h median 46 vs run #7's 44 (+4.5%, flat-to-rising, under the >40% tripwire); FYP withheld on all 27 posts (max 79 views < 100) — withheld, not near-zero, so the FYP clause cannot fire. GOVERNOR NO ACTION and clean-day credit APPLIES: counter 4 → 5. Review stays DAILY (5 of 7 clean days; no weekly switch). No pacing change, no park. Studio totals 349 posts / 0 drafts: +13 vs run #7's 336, exactly the 13 new ledger rows — no NEW unledgered post this interval. Studio-only confirmations the proxy could not give: (a) the unledgered second E2M-006 "The Steady Count" (2026-10-26 21:35 EDT, 60 views) is STILL present beside the ledgered 21:51 EDT post (62 views, both unchanged from run #7) — dedup-recon still owes a video-ID verification before any ledger action; (b) E1M-020's "Your video is unavailable to some audiences" banner is CONFIRMED a fourth time (Everyone privacy, 69 views / 1 like / 0 comments / 0 shares, unchanged) — standing anomaly, watch not action; its per-video analytics also show average watch time 4.06s, watched-full-video 0%, total play time 0h:04m:48s, 0 new followers (single-post detail, not a channel signal). Shares are NOT in the Studio list table — proxy shares (0 on all 27) stand as the public-page values; only E1M-020's Studio shares (0) are Studio-confirmed. Minor discrepancy: Studio shows E2M-044 posted 6:28 AM vs the ledger's 6:29 AM — 1 minute, no action.

## 2026-10-29 ~09:45 EDT (daily governor run #9 — PROXY READ; account @waefrebeorn)

GOVERNOR (proxy-grade): NO ACTION, NO CLEAN-DAY CREDIT. No new ledger rows
since E2M-044 (2026-10-28 06:29 EDT) — a 27.3h gap at check time — so this run
measures NO new-post cohort: it re-checks E2M-031...044 at 27-49h. The signed-in
Studio browser task (browser-task:5831c320...) was still in flight when this
section was banked; a late Studio report supersedes this entry as a correction,
as in runs #5/#6/#8. Re-check median 62.5 (n=14) vs run #8's new-post proxy
median 26 is NOT a governor comparison (different ages, different cohort type);
the governor test here is per-post progression plus the consecutive-post rule:
12/14 posts grew, 2 flat, 0 declined, and only ONE post (E2M-031) sits near
zero — isolated, not consecutive, so neither governor clause fires. FYP %
unobservable on public pages and would be withheld in Studio anyway (max 78
plays < 100) — withheld, not near-zero, so the FYP clause cannot fire. No park,
no pacing change, upload_park.txt stays absent. Clean-day counter HOLDS at 5
(no credit on a proxy read, per runs #5/#6/#8 precedent). Review stays DAILY.
Context, not a governor signal: the upload window has been steering E2M-045
"The Marked Ledger" since 07:55 EDT through three replacement spawns
(07:55 / 08:27 / 09:27 EDT) without a ledger row landing, and KICKSTAND_STATE
shows a 07:09 EDT "no-post-over-6h-nag-blocked" alert — an upload stall for
the kickstand nag's remit, not this review's.

| Episode | Title | Age at check | Tag set | Caption shape | Plays | Likes | Comments | Shares | For-You % | Source |
|---------|-------|--------------|---------|---------------|-------|-------|----------|--------|-----------|--------|
| E2M-031 | The Claimed Letters | ~48.7h | C | decl (2-min) | 5 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-032 | The Sealed Hour | ~47.9h | D | decl (2-min) | 78 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-033 | The Weather Hours | ~46.2h | A | decl (2-min) | 42 | 1 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-034 | The Quiet Inventory | ~38.1h | B | decl (2-min) | 43 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-035 | The Unclaimed Hour | ~37.3h | C | decl (2-min) | 59 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-036 | The Spare Hour | ~36.5h | D | decl (2-min) | 63 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-037 | The Late Rounds | ~36.3h | A | decl (2-min) | 68 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-038 | The Numbered Gap | ~36.0h | B | decl (2-min) | 71 | 2 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-039 | The Kept Rounds | ~33.2h | C | decl (2-min) | 53 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-040 | The Kept Watch | ~33.0h | D | decl (2-min) | 17 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-041 | The Kept Order | ~32.2h | A | decl (2-min) | 62 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-042 | The Quiet Hour | ~30.9h | B | decl (2-min) | 64 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-043 | The Kept Ledger | ~27.4h | C | decl (2-min) | 63 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-044 | The Returned Hour | ~27.3h | D | decl (2-min) | 68 | 1 | 0 | 0 | unobservable (public page) | Public post page |

Progression vs run #8 (proxy, ~24h earlier): E2M-031 5 -> 5 (FLAT);
E2M-032 76 -> 78; E2M-033 42 -> 42 (flat); E2M-034 43 -> 43 (flat);
E2M-035 55 -> 59; E2M-036 26 -> 63; E2M-037 46 -> 68; E2M-038 66 -> 71;
E2M-039 9 -> 53; E2M-040 4 -> 17; E2M-041 7 -> 62; E2M-042 1 -> 64;
E2M-043 0 -> 63; E2M-044 0 -> 68. Run #8's young tail (E2M-039...044) is
RESOLVED 6/6 at maturity (53-68 plays), the same slow-start resolution pattern
as runs #5/#6/#7/#8. Engagement: 4 likes total across 14 re-checks, 0 comments,
0 shares — the episode-comment drought continues (no episode comments since
E1M-030). Studio-only flags NOT resolvable on this read: the unledgered second
E2M-006 post, E1M-020's "unavailable to some audiences" banner, and whether
E2M-031 carries any Studio banner — all pending the Studio report.

## 2026-10-29 ~09:54 EDT — LATE STUDIO CORROBORATION (correction to the proxy read above; formal governor verdict)

The Studio browser task's report (per-video reads 09:47-09:50 EDT, totals
re-confirmed on the Posts page at 09:54 EDT) arrived after the proxy section
above was banked. It matches the proxy on ALL 14 values — every Studio view
equals the public-page play count, and likes/comments are identical — so the
proxy read is fully corroborated, not merely consistent. Shares are now
Studio-confirmed 0 on all 14 posts (the proxy shares were also 0). Formal
governor verdict on Studio numbers: NO ACTION. The re-check median is 62.5
(Studio views), FYP withheld on all 14 (max 78 views < 100; Studio shows "Data
will show when video views reach 100") — withheld, not near-zero, so the FYP
clause cannot fire; only E2M-031 sits near zero, isolated, not consecutive.
Studio totals 349 posts / 0 drafts: UNCHANGED vs run #8's 349 — zero new posts
this interval, which corroborates the upload stall (no E2M-045 post exists yet;
an E1M-045 "The Held Round" entry is a different series). Studio-only
confirmations: (a) the unledgered second E2M-006 "The Steady Count" persists
(2026-10-26 21:35 EDT, 60 views, unchanged; ledgered 21:51 EDT post 62 views,
unchanged; video IDs 7701155158876589342 / 7701159376391769375) — dedup-recon
still owes a video-ID verification before any ledger action; (b) E1M-020's
"Your video is unavailable to some audiences" banner is CONFIRMED a fifth time
(Everyone privacy, 69 views / 1 like / 0 comments / 0 shares, unchanged) —
standing anomaly, watch not action. (c) E2M-031's possible Studio banner was
NOT checked: the Studio task's checklist covered only the E2M-006 duplicate
and the E1M-020 banner, so whether E2M-031 carries a banner stays an open
run #10 watch item — do not read the Studio report as clearing it. Minor
discrepancy carried over from run #8: Studio shows E2M-044 posted 6:28 AM vs
the ledger's 6:29 AM — 1 minute, no action.
CLEAN-DAY CREDIT: WITHHELD, counter HOLDS at 5 — and this supersedes the
proxy section's alternative credit test ("re-check median holding the 60s
band"). A day with zero new posts exercises no pace at all, so it cannot
certify pace health: Studio totals are flat at 349 because uploads stalled,
not because distribution held at pace. The run #10 credit test is a NEW-POST
cohort (once uploads resume) with a matched-age median flat/rising vs 46.
Review stays DAILY (5 of 7 clean days; no weekly switch). No pacing change,
no park.

## 2026-10-30 ~09:45 EDT (daily governor run #10 — PROXY READ; account @waefrebeorn)

GOVERNOR (proxy-grade): NO ACTION, NO CLEAN-DAY CREDIT. First new-post cohort
since the 27h+ stall: 15 posts E2M-045...059 (2026-10-30 04:05-07:13 EDT, ages
2.5-5.7h at check). The signed-in Studio browser task
(browser-task:d5052ed1-1a7d-5438-b32d-c54b55fd7f6a) was still in flight when
this section was banked; a late Studio report supersedes this entry as a
correction, as in runs #5/#6/#8/#9. New-cohort proxy median 28 (n=15) vs run
#9's mature re-check median 62.5 is NOT a governor comparison (different ages
— the exact cross-age error runs #4-#9 corrected); the matched-age rule
governs and NO 10-14h band exists this run (the whole cohort is under 6h),
so no matched-age drop can be computed. The honest young-cohort test points
the other way: vs prior young tails (run #7 at <=6.8h: 0-1 plays; run #8 at
3.3-9h: 0-9 plays), this cohort at 2.5-5.7h reads 5-66, median 28 — markedly
stronger early distribution, and the within-cohort age gradient is intact
(oldest five E2M-045...049, 4.8-5.7h: median 59; youngest five E2M-055...059,
2.5-3.3h: median 16), consistent with slow-start maturation, not decay.
FYP % unobservable on public pages and would be withheld in Studio anyway
(max 66 plays < 100) — withheld, not near-zero, so the FYP clause cannot fire.
Consecutive near-zero clause: only E2M-059 (5 plays, age 2.5h — too young to
judge) and the isolated E2M-031 flatline (5, ~72.7h) sit near zero; they are
not consecutive posts, so the clause cannot fire. Mature re-check median
holds at 62.5 (n=14, identical to run #9). No park, no pacing change,
upload_park.txt stays absent. Clean-day counter HOLDS at 5 (no credit on a
proxy read, per runs #5/#6/#8/#9 precedent — and a sub-6h cohort cannot
certify pace health at matched ages in any case). Review stays DAILY (5 of 7;
no weekly switch).

| Episode | Title | Age at check | Tag set | Caption shape | Plays | Likes | Comments | Shares | For-You % | Source |
|---------|-------|--------------|---------|---------------|-------|-------|----------|--------|-----------|--------|
| E2M-045 | The Marked Ledger | ~5.7h | A | decl (2-min) | 66 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-046 | The Returned Count | ~5.5h | B | decl (2-min) | 65 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-047 | The Long Tally | ~5.2h | C | decl (2-min) | 40 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-048 | The Still Beacon | ~5.0h | D | decl (2-min) | 57 | 1 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-049 | The Kept Rooms | ~4.8h | A | decl (2-min) | 59 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-050 | The Quiet Objects | ~4.6h | B | decl (2-min) | 24 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-051 | The Uncounted Hours | ~4.4h | C | decl (2-min) | 20 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-052 | The Dock Lamps | ~4.1h | D | decl (2-min) | 21 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-053 | The Count's Ledger | ~3.9h | A | decl (2-min) | 42 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-054 | The Kept Passages | ~3.5h | B | decl (2-min) | 62 | 1 | 1 | 0 | unobservable (public page) | Public post page |
| E2M-055 | The Slow Ledger | ~3.3h | C | decl (2-min) | 14 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-056 | The Crossed Thresholds | ~3.1h | D | decl (2-min) | 19 | 1 | 1 | 0 | unobservable (public page) | Public post page |
| E2M-057 | The Deep Signals | ~2.9h | A | decl (2-min) | 16 | 1 | 1 | 0 | unobservable (public page) | Public post page |
| E2M-058 | The Night House | ~2.7h | B | decl (2-min) | 28 | 1 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-059 | The Late Transmission | ~2.5h | C | decl (2-min) | 5 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-031 | The Claimed Letters | ~72.7h | C | decl (2-min) | 5 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-032 | The Sealed Hour | ~71.9h | D | decl (2-min) | 78 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-033 | The Weather Hours | ~70.2h | A | decl (2-min) | 42 | 1 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-034 | The Quiet Inventory | ~62.1h | B | decl (2-min) | 43 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-035 | The Unclaimed Hour | ~61.3h | C | decl (2-min) | 59 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-036 | The Spare Hour | ~60.5h | D | decl (2-min) | 63 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-037 | The Late Rounds | ~60.3h | A | decl (2-min) | 68 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-038 | The Numbered Gap | ~60.0h | B | decl (2-min) | 71 | 2 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-039 | The Kept Rounds | ~57.2h | C | decl (2-min) | 53 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-040 | The Kept Watch | ~57.0h | D | decl (2-min) | 17 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-041 | The Kept Order | ~56.2h | A | decl (2-min) | 62 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-042 | The Quiet Hour | ~54.9h | B | decl (2-min) | 64 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-043 | The Kept Ledger | ~51.4h | C | decl (2-min) | 63 | 0 | 0 | 0 | unobservable (public page) | Public post page |
| E2M-044 | The Returned Hour | ~51.3h | D | decl (2-min) | 69 | 1 | 0 | 0 | unobservable (public page) | Public post page |

Progression vs run #9 (proxy/Studio, ~24h earlier): E2M-031 5 -> 5 (FLAT,
third consecutive flat check — confirmed flatline at ~72.7h); E2M-032 78 ->
78 (flat); E2M-033 42 -> 42 (flat, third consecutive flat check — plateau
persists in-band); E2M-034 43 -> 43 (flat, third consecutive flat check);
E2M-035 59 -> 59 (flat); E2M-036 63 -> 63 (flat); E2M-037 68 -> 68 (flat);
E2M-038 71 -> 71 (flat); E2M-039 53 -> 53 (flat); E2M-040 17 -> 17 (flat —
soft low persists); E2M-041 62 -> 62 (flat); E2M-042 64 -> 64 (flat);
E2M-043 63 -> 63 (flat); E2M-044 68 -> 69 (+1). Mature cohort 13/14 flat,
re-check median 62.5 unchanged — maturation flattening at 51-73h, not decay
(the run #9 interval showed growth because that cohort was 27-49h; a flat
second interval at 51-73h is the expected curve, and the median did not move).
Engagement: 5 likes across 15 new posts; 3 new posts show 1 comment each
(E2M-054, E2M-056, E2M-057) — first episode comment counts since E1M-030 by
count, but comment CONTENT is unread on public pages, so the drought is NOT
yet declared over; the Studio report must corroborate before any such claim.
Shares 0 everywhere (public-page values). Studio-only flags NOT resolvable
on this read: Studio totals, any unledgered 2026-10-30 post, the unledgered
second E2M-006 post, E1M-020's banner (6th check pending), and whether
E2M-031 carries any Studio banner — all pending the Studio report.

## 2026-10-30 ~10:12 EDT — LATE STUDIO CORROBORATION (correction to the proxy read above; formal governor verdict)

The Studio browser task's report (per-video analytics reads 09:59-10:07 EDT,
totals re-confirmed on the Posts page at 10:08, 10:10 and 10:11 EDT) arrived
after the proxy section above was banked. It matches the proxy on all 14
re-checks exactly and on the new cohort within live-tick drift (Studio views
run 0-6 above the ~09:45 proxy plays on 11 of 15 new posts — e.g. E2M-049
59 -> 65, E2M-056 19 -> 23, E2M-059 5 -> 7 — and the Posts list at 10:08-10:10
already showed E2M-056 at 25 and E2M-055 at 16, above their analytics reads;
treat the Studio table as a snapshot at the stated read times, not frozen
totals). Likes/comments are identical to the proxy on all 29 posts; shares
are now Studio-confirmed 0 on all 29 (per-video analytics Overview, which is
where shares live — the Posts list table has no shares column). Formal
governor verdict on Studio numbers: NO ACTION. New-cohort Studio median 28
(n=15, ages ~3-6.5h at read) equals the proxy median; FYP withheld on all 29
(max 66 views < 100; Studio shows "Data will show when video views reach
100") — withheld, not near-zero, so the FYP clause cannot fire; only E2M-059
(7, young) and the isolated E2M-031 flatline (5) sit near zero, not
consecutive posts. CLEAN-DAY CREDIT: WITHHELD, counter HOLDS at 5 — the
Studio grade removes the proxy caveat, but no matched-age band exists to
certify pace health (the whole cohort is sub-6.5h), so this run still cannot
count toward the 7 clean days; the run #11 credit test stands (this cohort's
re-check at ~24h+ with a matched-age median flat/rising vs 46). Review stays
DAILY (5 of 7; no weekly switch). No pacing change, no park.
Studio totals 364 posts / 0 drafts: growth +15 equals exactly the 15 new
ledger rows — NO unledgered post this interval (newest post E2M-059 07:13
EDT, followed in order down to E2M-045). Studio-only findings: (a) E2M-031
carries NO banner on its per-video analytics Overview (re-opened 10:07 EDT
— no "unavailable to some audiences," no "under review," no
limited-distribution notice); the flatline is therefore NOT explained by a
Studio flag on that page, and its retention data points elsewhere: average
watch time 3.91s, "Most viewers stopped watching at 0:03," watched-full-video
0%, total play time 0h:00m:19s — viewers bail at 3 seconds, a hook/retention
read on this one post, not a suppression verdict. (b) E1M-020's
"unavailable to some audiences" banner is GONE on its per-video analytics
Overview (opened 10:09 EDT — no banner, under-review, or limited-distribution
notice anywhere on that page; views still 69, likes 1, comments 0, shares 0)
— the standing anomaly clears on this check (scope: analytics Overview
only); it leaves the watch list. (c) The unledgered second E2M-006 "The
Steady Count" PERSISTS (Oct 26 21:35 EDT, 60 views; ledgered 21:51 EDT post
62 views; both privacy Everyone) — dedup-recon still owes a video-ID
verification before any ledger action. (d) Comment counts Studio-confirmed:
1 each on E2M-054/056/057 — the episode-comment drought ends BY COUNT (first
episode comments since E1M-030); comment contents remain unread, so no read
on what viewers said. (e) Loose end, not assumed away: the Studio home
page's "Last 7 days" key metrics showed Shares 1, yet all 29 videos checked
show 0 shares each — that single share belongs to another post or to the
rolled-up account metric, not to any of these 29. Minor discrepancies
carried over: Studio shows E2M-050 posted 05:08 vs the ledger's ~05:09 and
E2M-044 at 06:28 vs the ledger's 06:29 — 1 minute each, no action.

| Episode | Title | Views (Studio) | Likes | Comments | Shares | For-You % | Source |
|---------|-------|----------------|-------|----------|--------|-----------|--------|
| E2M-045 | The Marked Ledger | 66 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:07 EDT) |
| E2M-046 | The Returned Count | 65 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:07 EDT) |
| E2M-047 | The Long Tally | 43 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:06 EDT) |
| E2M-048 | The Still Beacon | 58 | 1 | 0 | 0 | withheld <100 | Studio analytics (read 10:06 EDT) |
| E2M-049 | The Kept Rooms | 65 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:06 EDT) |
| E2M-050 | The Quiet Objects | 24 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:06 EDT) |
| E2M-051 | The Uncounted Hours | 21 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:06 EDT) |
| E2M-052 | The Dock Lamps | 22 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:05 EDT) |
| E2M-053 | The Count's Ledger | 45 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:05 EDT) |
| E2M-054 | The Kept Passages | 63 | 1 | 1 | 0 | withheld <100 | Studio analytics (read 10:05 EDT) |
| E2M-055 | The Slow Ledger | 15 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:03 EDT) |
| E2M-056 | The Crossed Thresholds | 23 | 1 | 1 | 0 | withheld <100 | Studio analytics (read 10:03 EDT) |
| E2M-057 | The Deep Signals | 19 | 1 | 1 | 0 | withheld <100 | Studio analytics (read 10:03 EDT) |
| E2M-058 | The Night House | 28 | 1 | 0 | 0 | withheld <100 | Studio analytics (read 10:02 EDT) |
| E2M-059 | The Late Transmission | 7 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:02 EDT) |
| E2M-031 | The Claimed Letters | 5 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:07 EDT) |
| E2M-032 | The Sealed Hour | 78 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:02 EDT) |
| E2M-033 | The Weather Hours | 42 | 1 | 0 | 0 | withheld <100 | Studio analytics (read 10:02 EDT) |
| E2M-034 | The Quiet Inventory | 43 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:02 EDT) |
| E2M-035 | The Unclaimed Hour | 59 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:01 EDT) |
| E2M-036 | The Spare Hour | 63 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:01 EDT) |
| E2M-037 | The Late Rounds | 68 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:01 EDT) |
| E2M-038 | The Numbered Gap | 71 | 2 | 0 | 0 | withheld <100 | Studio analytics (read 10:00 EDT) |
| E2M-039 | The Kept Rounds | 53 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:00 EDT) |
| E2M-040 | The Kept Watch | 17 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:00 EDT) |
| E2M-041 | The Kept Order | 62 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 09:59 EDT) |
| E2M-042 | The Quiet Hour | 64 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 09:59 EDT) |
| E2M-043 | The Kept Ledger | 63 | 0 | 0 | 0 | withheld <100 | Studio analytics (read 10:07 EDT) |
| E2M-044 | The Returned Hour | 69 | 1 | 0 | 0 | withheld <100 | Studio analytics (read 10:07 EDT) |

## 2026-10-31 ~09:44 EDT (daily governor run #11 — PROXY READ; account @waefrebeorn)

No new ledger rows since E2M-059 (2026-10-30 07:13 EDT). Re-check of E2M-045...059 at ~26.5-29.6h plus E2M-031, from public post pages (plays, not Studio views) while the signed-in Studio browser task (browser-task:2f0b9e03...) was still in flight. Run #10 young reads shown for delta; run #10 Studio values used as the young baseline (Studio median 28 = proxy median 28).

| Episode | Title | Plays (proxy) | Run #10 young | Likes | Comments | Shares | For-You % | Source |
|---------|-------|---------------|---------------|-------|----------|--------|-----------|--------|
| E2M-045 | The Marked Ledger | 70 | 66 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-046 | The Returned Count | 67 | 65 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-047 | The Long Tally | 62 | 43 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-048 | The Still Beacon | 62 | 58 | 1 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-049 | The Kept Rooms | 73 | 65 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-050 | The Quiet Objects | 63 | 24 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-051 | The Uncounted Hours | 75 | 21 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-052 | The Dock Lamps | 56 | 22 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-053 | The Count's Ledger | 68 | 45 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-054 | The Kept Passages | 67 | 63 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-055 | The Slow Ledger | 97 | 15 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-056 | The Crossed Thresholds | 62 | 23 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-057 | The Deep Signals | 53 | 19 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-058 | The Night House | 72 | 28 | 1 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-059 | The Late Transmission | 63 | 7 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |
| E2M-031 | The Claimed Letters | 5 | 5 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EDT) |

Cohort median 67 (n=15), all 15 up from run #10. Tag medians: A 69, B 67, C 69, D 62. Likes 6, comments 4, shares 0.

## 2026-10-31 ~09:53 EDT — LATE STUDIO CORROBORATION (correction to the proxy read above; formal governor verdict)

Studio read 09:43-09:53 EDT, totals 364 posts / 0 drafts (flat — no new posts this interval). Studio matches the proxy on all 16 values exactly; shares Studio-confirmed 0 on all 16; saves 0 on all 15 re-checks. Formal verdict: NO ACTION (median 67 vs run #9 mature 62.5, rise; FYP withheld on all 15). Clean-day credit STILL WITHHELD (counter holds at 5): zero new posts means the day exercised no pace. Studio-only findings: no post newer than E2M-059; unledgered second E2M-006 persists (21:35 EDT, 60 views; ledgered 21:51 EDT post 62 views); E2M-031 banner-free on Posts row, analytics page, and public page (5 views, Everyone); home "Last 7 days" (window Oct 23-29): video views 6.9K (+44.1%), profile views 24 (+84.6%), likes 67 (+15.5%), comments 4 (-55.6%), shares 0 (-1, -100.0%) — the run #10 unattributed share has rolled out of the window. Minor: Studio shows E2M-050 at 05:08 vs ledger ~05:09.

## 2026-11-01 ~09:44 EST (daily governor run #12 — PROXY READ; account @waefrebeorn)

No new ledger rows since E2M-059 (2026-10-30 07:13 EDT). Re-check of E2M-045...059 at ~50.5-53.6h plus E2M-031, from public post pages (plays, not Studio views) while the signed-in Studio browser task (browser-task:8cc522b2...) was still in flight. Run #11 reads shown for delta (run #11 proxy = Studio, corroborated).

| Episode | Title | Plays (proxy) | Run #11 | Likes | Comments | Shares | For-You % | Source |
|---------|-------|---------------|---------|-------|----------|--------|-----------|--------|
| E2M-045 | The Marked Ledger | 71 | 70 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-046 | The Returned Count | 67 | 67 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-047 | The Long Tally | 63 | 62 | 1 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-048 | The Still Beacon | 62 | 62 | 1 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-049 | The Kept Rooms | 73 | 73 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-050 | The Quiet Objects | 63 | 63 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-051 | The Uncounted Hours | 76 | 75 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-052 | The Dock Lamps | 57 | 56 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-053 | The Count's Ledger | 69 | 68 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-054 | The Kept Passages | 67 | 67 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-055 | The Slow Ledger | 97 | 97 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-056 | The Crossed Thresholds | 62 | 62 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-057 | The Deep Signals | 53 | 53 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-058 | The Night House | 72 | 72 | 1 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-059 | The Late Transmission | 64 | 63 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-031 | The Claimed Letters | 5 | 5 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |

Cohort median 67 (n=15), flat vs run #11's 67; 6 up (+1 each), 9 flat, 0 down. Tag medians: A 70, B 67, C 70, D 62. Likes 7, comments 4, shares 0, saves 0.

## 2026-11-01 ~09:49 EST — LATE STUDIO CORROBORATION (correction to the proxy read above; formal governor verdict)

Studio report (task ran 09:43-09:49 EST; the report's own 09:50 re-confirmation timestamp runs one minute past the harness-measured end — values unaffected). Studio totals 364 posts / 0 drafts (flat — no new posts this interval). Studio matches the proxy on all 16 values exactly; shares Studio-confirmed 0 on all 16; FYP withheld on all 15 re-checks plus E2M-031 (max 97 < 100). Formal verdict: NO ACTION (median 67 flat vs run #11's 67; FYP withheld, not near-zero). Clean-day credit STILL WITHHELD (counter holds at 5): Studio totals are flat at 364 because NO new posts landed this interval, so the day exercised no pace and cannot certify pace health (same distinction as the run #9 and run #11 corrections). Review stays DAILY (5 of 7; no weekly switch). No pacing change, no park. Studio-only resolutions: no post newer than E2M-059; unledgered second E2M-006 persists (21:35 EDT, 60 views; ledgered 21:51 EDT post 62 views); E2M-031 banner-free on its Posts row and analytics detail page (5 views, Everyone) — flatline stays a hook read; no banner or "Content under review" badge on any of the 16 checked videos, all Everyone. Studio home "Last 7 days": video views 7.7K (+134.6%), profile views 24 (+118.2%), likes 61 (+1.7%), comments 8 (+14.3%), shares 0 (-100.0%). Minor: Studio shows E2M-050 at 05:08 vs ledger ~05:09 (carried over).

## 2026-11-02 ~09:44 EST (daily governor run #13 — PROXY READ; account @waefrebeorn)

No new ledger rows since E2M-059 (2026-10-30 07:13 EDT). Re-check of E2M-045...059 at ~75.5-78.6h plus E2M-031, from public post pages (plays, not Studio views) while the signed-in Studio browser task was still in flight. Read 09:44-09:46 EST.

| Episode | Title | Plays (proxy) | Run #12 | Likes | Comments | Shares | For-You % | Source |
|---------|-------|---------------|---------|-------|----------|--------|-----------|--------|
| E2M-045 | The Marked Ledger | 71 | 71 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-046 | The Returned Count | 67 | 67 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-047 | The Long Tally | 63 | 63 | 1 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-048 | The Still Beacon | 62 | 62 | 1 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-049 | The Kept Rooms | 74 | 73 | 1 | 0 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-050 | The Quiet Objects | 63 | 63 | 0 | 0 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-051 | The Uncounted Hours | 76 | 76 | 0 | 0 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-052 | The Dock Lamps | 57 | 57 | 0 | 0 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-053 | The Count's Ledger | 69 | 69 | 0 | 0 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-054 | The Kept Passages | 67 | 67 | 1 | 1 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-055 | The Slow Ledger | 97 | 97 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-056 | The Crossed Thresholds | 62 | 62 | 1 | 1 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-057 | The Deep Signals | 53 | 53 | 1 | 1 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-058 | The Night House | 72 | 72 | 1 | 0 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-059 | The Late Transmission | 65 | 64 | 0 | 0 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-031 | The Claimed Letters | 7 | 5 | 1 | 0 | 0 | withheld <100 | public post page (read 09:46 EST) |

Cohort median 67 (n=15), flat vs run #12's 67; 2 up (+1 each: E2M-049, E2M-059), 13 flat, 0 down. Tag medians: A 70, B 67, C 70.5, D 62. Likes 8, comments 4, shares 0, saves 0.

## 2026-11-02 ~09:56 EST — LATE STUDIO CORROBORATION (correction to the proxy read above; formal governor verdict)

Studio report (task ran 09:46-09:56 EST). Studio totals 364 posts / 0 drafts (flat — no new posts this interval). Studio matches the proxy on all 16 values exactly; shares Studio-confirmed 0 on all 16; saves 0 on all 16; FYP withheld on all 16 (max 97 < 100). Formal verdict: NO ACTION (median 67 flat vs run #12's 67; FYP withheld, not near-zero). Clean-day credit STILL WITHHELD (counter holds at 5): Studio totals are flat at 364 because NO new posts landed this interval, so the day exercised no pace and cannot certify pace health (same distinction as the run #9/#11/#12 corrections). Review stays DAILY (5 of 7; no weekly switch). No pacing change, no park. Studio-only resolutions: no post newer than E2M-059; unledgered second E2M-006 persists (Oct 26, 9:35 PM, 60 views, 0 likes, 0 comments, Everyone; ledgered 9:51 PM post 62 views); E2M-031 banner-free on its analytics overview (7 views, 1 like, Everyone) — flatline stays a hook read; no banner or "Content under review" badge on any of the 16 checked videos, all Everyone. Studio home "Last 7 days": video views 6.7K (+155.3%), profile views 22 (+120.0%), likes 44 (-10.2%), comments 8 (+14.3%), shares 0 (-100.0%).

## 2026-11-03 ~09:45 EST (daily governor run #14 — PROXY READ; account @waefrebeorn)

No new ledger rows since E2M-059 (2026-10-30 07:13 EDT). Re-check of E2M-045...059 at ~99.5-102.7h plus E2M-031, from public post pages (plays, not Studio views) while the signed-in Studio browser task (browser-task:bca979cc-40ea-58a3-9599-6daa4352be90) was still in flight. Read 09:44-09:46 EST.

| Episode | Title | Plays (proxy) | Run #13 | Likes | Comments | Shares | For-You % | Source |
|---------|-------|---------------|---------|-------|----------|--------|-----------|--------|
| E2M-045 | The Marked Ledger | 71 | 71 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-046 | The Returned Count | 67 | 67 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-047 | The Long Tally | 63 | 63 | 1 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-048 | The Still Beacon | 62 | 62 | 1 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-049 | The Kept Rooms | 74 | 74 | 1 | 0 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-050 | The Quiet Objects | 63 | 63 | 0 | 0 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-051 | The Uncounted Hours | 76 | 76 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-052 | The Dock Lamps | 57 | 57 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-053 | The Count's Ledger | 69 | 69 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-054 | The Kept Passages | 67 | 67 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-055 | The Slow Ledger | 97 | 97 | 0 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-056 | The Crossed Thresholds | 63 | 62 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-057 | The Deep Signals | 53 | 53 | 1 | 1 | 0 | withheld <100 | public post page (read 09:44 EST) |
| E2M-058 | The Night House | 73 | 72 | 1 | 0 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-059 | The Late Transmission | 65 | 65 | 0 | 0 | 0 | withheld <100 | public post page (read 09:45 EST) |
| E2M-031 | The Claimed Letters | 7 | 7 | 1 | 0 | 0 | withheld <100 | public post page (read 09:44 EST) |

Cohort median 67 (n=15), flat vs run #13's 67; 2 up (+1 each: E2M-056, E2M-058), 13 flat, 0 down. Tag medians: A 70, B 67, C 70.5, D 62. Likes 8, comments 4, shares 0, saves 0.

## 2026-11-03 ~09:50 EST — LATE STUDIO CORROBORATION (correction to the proxy read above; formal governor verdict)

Studio report (task ran 09:43-09:50 EST; Analytics Overview figures read 09:45-09:47 EST, Posts list re-checked 09:48-09:49 EST). Studio totals 364 posts / 0 drafts (flat — no new posts this interval). Formal verdict: NO ACTION. Clean-day credit STILL WITHHELD (counter holds at 5): Studio totals are flat at 364 because NO new posts landed this interval, so the day exercised no pace and cannot certify pace health (same distinction as the run #9/#11/#12/#13 corrections). Review stays DAILY (5 of 7; no weekly switch). No pacing change, no park.

Unlike runs #5/#6/#8/#11/#12/#13, the Studio report does NOT match the proxy on all 16 values — two discrepancies, both disclosed, neither governor-relevant:
- E2M-058 "The Night House": proxy 73 plays, Studio Posts list 09:49 EST 73, but its Analytics Overview figure (read 09:45-09:47 EST) was 66. The overview figure reads as stale/lagging, not a real drop — the Posts list corroborates the proxy. Using overview figures the cohort median is 66; using the Posts-list figure it is 67, exactly the proxy median. Either way flat vs run #13's 67 (at most -1.5%), far from the >40% tripwire.
- E2M-057 "The Deep Signals": proxy 1 like / 1 comment, Studio Analytics Overview 0 / 0 (views agree at 53). First likes/comments mismatch in the proxy-vs-Studio series; the overview count may lag the public page, or the public count may include something the overview does not. Totals affected by at most 1 like and 1 comment; no verdict rests on them. Shares/saves Studio-confirmed 0 on all 16.
FYP withheld on all 16 (max 97 < 100; Studio note: "Data will show when video views reach 100") — withheld, not near-zero, so the FYP clause cannot fire.

Studio-only resolutions: no post newer than E2M-059 (Posts list top E2M-059 Oct 30 7:13 AM, then E2M-058 7:03 AM); unledgered second E2M-006 persists (Oct 26, 9:35 PM, 60 views, 0 likes, 0 comments, Everyone; Analytics Overview video ID 7701155158876589342, distinct from the ledgered 9:51 PM post) — dedup-recon now has its video ID; E2M-031 banner-free on its analytics overview (7 views, 1 like, Everyone) — flatline stays a hook read; no banner or "Content under review" badge on any of the 16 checked videos, all Everyone. Studio home "Last 7 days": video views 5.4K (+94.9%), profile views 17 (+54.5%), likes 33 (-36.5%), comments 8 (+300.0%), shares 0 (-100.0%).

## 2026-11-04 ~09:55 EST — daily governor run #15, STUDIO READ IN-RUN (first STATION cohort)

Signed-in Studio browser task ran 09:44–09:53 EST (378 posts, 0 drafts); individual Studio analytics overview pages for all 14 ST posts, read 09:46–09:50 EST. No proxy read needed — the first in-run Studio report since run #7.

| Episode | Title | Views (Studio) | Likes | Comments | Shares | For-You % | Source |
|---------|-------|---------------|-------|----------|--------|-----------|--------|
| ST-001 | The Late Announcement / The Overheard Promise | 69 | 0 | 0 | 0 | withheld <100 | Studio analytics (read ~09:46 EST, age ~4.9h) |
| ST-002 | The Demand / The Second Warmth | 62 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~4.8h) |
| ST-003 | The Third Word, Read / The First Watch | 66 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~4.6h) |
| ST-004 | The First Reading / The Third Reading | 95 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~4.4h) |
| ST-005 | The Fifth Reading / The First Precedent | 87 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~4.3h) |
| ST-006 | The First Settlement / The First Recount | 96 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~2.3h) |
| ST-007 | The Keeper'S Hearing / The First Standing | 44 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~2.1h; Posts list 45 at 09:50 EST, live tick) |
| ST-008 | The Heard Guest'S First Telling / The First Holding | 54 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~1.8h) |
| ST-009 | The First Seating In The Gallery / The First Filing | 52 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~1.6h) |
| ST-010 | The Returned Hearing / The Sealed Question | 57 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~1.4h) |
| ST-011 | The Return Nobody Sent For / The Coat Worn Inside Out | 62 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~1.2h) |
| ST-012 | The Slip The Pocket Kept / The Third Mark That Returned Its Maker | 35 | 1 | 0 | 0 | withheld <100 | Studio analytics (age ~1.0h) |
| ST-013 | The Fifth Mark That Kept Its Secret / The Seventh Mark That Returned Its Counter | 28 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~0.8h; Posts list 29 at 09:50 EST, live tick) |
| ST-014 | The Ninth Wave That Framed Its Field / The Eleventh Letter That Returned Its Sender | 15 | 0 | 0 | 0 | withheld <100 | Studio analytics (age ~0.5h; Posts list 18 at 09:52 EST, live tick) |
| E2M-055 | The Slow Ledger | 97 | 0 | 0 | 0 | withheld <100 | Studio analytics re-check (09:46 EST) |
| E2M-031 | The Claimed Letters | 7 | 1 | 0 | 0 | withheld <100 | Studio Posts list re-check (09:51 EST) |

Cohort median 59.5 (n=14); oldest-five median 69, youngest-five median 35 — age gradient intact. Tag medians: A 60.5, B 59.5, C 62, D 54. Likes 1, comments 0, shares 0 across 14 new posts. Governor: NO ACTION, NO clean-day credit (see policy changelog 2026-11-04 entry). Studio totals 378 = 364 + 14 exactly; no post newer than ST-014; unledgered second E2M-006 persists (60 views, Everyone). Studio home "Last 7 days": video views 4.1K (+151, +3.8%), profile views 14 (+1), likes 29 (-29), comments 6 (+3), shares 0 (-1).

## 2026-11-05 ~09:50 EST — daily governor run #16, PROXY READ (GOVERNOR FIRED — distribution collapse; Studio report pending)

GOVERNOR: FIRED. New cohort ST-015…064 (n=50, ages 2.9–23.6h) median plays/post 13.5 vs previous run's 59.5 (−77.3% raw). The matched-age rule confirms it: the 17–24h band (ST-015…059, n=45) median 12 vs the ST-001…014 re-check median 63.5 at ~24–29h (−81.1%). The age mix biases this comparison the other way (the new cohort is OLDER than run #15's 0.5–4.9h cohort), so the drop is not an age artifact. FYP % unobservable on all 66 posts (max 98 plays < 100) — withheld, not near-zero, so the FYP clause does not fire on its own; the median clause fires decisively. Actions taken this run: (1) 48–72h park written to upload_park.txt (resume ≥ 2026-11-07 ~09:50 EST, auto-lift 2026-11-08 ~09:50 EST); (2) kickstand nag pacing floor widened 6 → 30 min via cron.update (2/hour on resume); (3) both logged in the policy changelog. Clean-day counter RESETS to 0 at the 30-min floor (was 5); review stays DAILY until 7 consecutive clean days at the new pace. No re-tightening without replicated evidence.

Public-page proxy read (plays, not Studio views), all 66 pages crawled fresh ~09:44–09:47 EST. Signed-in Studio browser task (browser-task:0190a6ea…) was still in flight at bank time — a late Studio report supersedes this entry as a correction, as in runs #5/#6/#8/#9/#10/#11/#12/#13/#14. Profile cross-check: video_count 428 = 378 (run #15 Studio total) + 50 new rows exactly; followers 1794, total likes 28.8K.

### Re-checks (ST-001…014 at ~24–29h; E2M-055, E2M-031)

| Episode | Title | Plays (proxy) | Likes | Comments | Shares | Saves | For-You % | Source |
|---------|-------|--------------|-------|----------|--------|-------|-----------|--------|
| ST-001 | The Late Announcement / The Overheard Promise | 71 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~28.9h; was 69, +2) |
| ST-002 | The Demand / The Second Warmth | 63 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~28.8h; was 62, +1) |
| ST-003 | The Third Word, Read / The First Watch | 72 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~28.6h; was 66, +6; first like) |
| ST-004 | The First Reading / The Third Reading | 95 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~28.4h; was 95, flat) |
| ST-005 | The Fifth Reading / The First Precedent | 88 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~28.3h; was 87, +1) |
| ST-006 | The First Settlement / The First Recount | 98 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~26.2h; was 96, +2) |
| ST-007 | The Keeper'S Hearing / The First Standing | 53 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~26.1h; was 44, +9) |
| ST-008 | The Heard Guest'S First Telling / The First Holding | 55 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~25.8h; was 54, +1) |
| ST-009 | The First Seating In The Gallery / The First Filing | 56 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~25.6h; was 52, +4) |
| ST-010 | The Returned Hearing / The Sealed Question | 61 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~25.4h; was 57, +4) |
| ST-011 | The Return Nobody Sent For / The Coat Worn Inside Out | 64 | 1 | 0 | 0 | 1 | withheld <100 | public post page re-check (~25.2h; was 62, +2; first ST save) |
| ST-012 | The Slip The Pocket Kept / The Third Mark That Returned Its Maker | 57 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~25.0h; was 35, +22) |
| ST-013 | The Fifth Mark That Kept Its Secret / The Seventh Mark That Returned Its Counter | 70 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~24.8h; was 28, +42) |
| ST-014 | The Ninth Wave That Framed Its Field / The Eleventh Letter That Returned Its Sender | 63 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~24.5h; was 15, +48) |
| E2M-055 | The Slow Ledger | 97 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (6th consecutive check at 97) |
| E2M-031 | The Claimed Letters | 7 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (6th flat check; solved hook case) |

Re-check median 63.5 (n=14), all 14 up or flat vs run #15 — the ST cohort's first matched-age anchor. Slow-start resolution replicates again (ST-013 28→70, ST-014 15→63, ST-012 35→57).

### New cohort ST-015…064 (n=50)

| Episode | Title | Plays (proxy) | Likes | Comments | Shares | Saves | Tag | Age |
|---------|-------|--------------|-------|----------|--------|-------|-----|-----|
| ST-015 | The Thirteenth Letter That Kept Its Family / The Fifteenth Letter That Returned Its Reader | 53 | 0 | 0 | 0 | 0 | C | ~23.6h |
| ST-016 | The Shift That Kept Its Keeper / The Night With Two Keepers | 58 | 0 | 0 | 0 | 0 | D | ~23.3h |
| ST-017 | The Keeper Who Returned Twice / The Name The Buyer Collected | 58 | 0 | 0 | 0 | 0 | A | ~23.2h |
| ST-018 | The Buyer Who Came Back / The Answer That Arrived First | 52 | 0 | 0 | 0 | 0 | B | ~23.0h |
| ST-019 | The Fruit The Count Would Not Take / The Paycheck The Building Signed | 75 | 3 | 0 | 0 | 0 | C | ~22.8h |
| ST-020 | The Tower That Answered Back / The Name The Building Kept | 6 | 0 | 0 | 0 | 0 | D | ~22.7h |
| ST-021 | The Hand Nobody Recognized / The Look That Followed | 9 | 0 | 0 | 0 | 0 | A | ~22.5h |
| ST-022 | The Door That Kept Her Place / The Step The Dispatcher Took | 7 | 0 | 0 | 0 | 0 | B | ~22.3h |
| ST-023 | The Seventh The Stranger Stamped / The Sixth Sum | 28 | 0 | 0 | 0 | 0 | C | ~22.1h |
| ST-024 | The Hall That Kept Walking / The Name The Stamp Hired | 2 | 0 | 0 | 0 | 0 | D | ~22.0h |
| ST-025 | The Count The Tower Claimed / The Doorway That Took Its Next Stander | 5 | 0 | 0 | 0 | 0 | A | ~21.8h |
| ST-026 | The Hand That Hovered / The Fruit The Tower Counted | 2 | 0 | 0 | 0 | 0 | B | ~21.6h |
| ST-027 | The Chair The Keeping Settled On / The Hand That Was Pushed | 7 | 0 | 0 | 0 | 0 | C | ~21.4h |
| ST-028 | The Tick That Stayed / The Sitter The Chair Watched | 1 | 0 | 0 | 0 | 0 | D | ~21.2h |
| ST-029 | The Hand That Lifted / The Tick That Ticked Alone | 5 | 0 | 0 | 0 | 0 | A | ~21.1h |
| ST-030 | The Doorway The Chair Left / The Hand That Witnessed | 2 | 0 | 0 | 0 | 0 | B | ~20.9h |
| ST-031 | The Third Tick Nobody Paid For / The Keeping One Leaving Late | 55 | 0 | 0 | 0 | 0 | C | ~20.7h |
| ST-032 | The Witness Replaced / The Fourth Tick Nobody Owes | 3 | 0 | 0 | 0 | 0 | D | ~20.5h |
| ST-033 | The Chair That Watched Him Sit / The Slip The Claimant Signed | 17 | 0 | 0 | 0 | 0 | A | ~20.3h |
| ST-034 | The Tick The Station Paid / The Chair That Watched Her Sit | 56 | 0 | 0 | 0 | 0 | B | ~20.1h |
| ST-035 | The Book The Manager Reached For / The Sixth Tick The Machine Spoke | 43 | 0 | 0 | 0 | 0 | C | ~19.8h |
| ST-036 | The Third Sit The Head Refused / The Name The Book Kept Twice | 6 | 0 | 0 | 0 | 0 | D | ~19.6h |
| ST-037 | The Seventh Tick That Named The Fruit / The Chair Nobody Sat In | 47 | 1 | 0 | 0 | 0 | A | ~19.4h |
| ST-038 | The Pocket The Page Kept / The Fruit The Tower Owed | 29 | 0 | 0 | 0 | 0 | B | ~19.2h |
| ST-039 | The Doorway The Head Kept / The Hand The Page Would Not Match | 6 | 0 | 0 | 0 | 0 | C | ~19.1h |
| ST-040 | The Eighth Tick The Coin Became / The Man The Head Chose | 0 | 0 | 0 | 0 | 0 | D | ~18.9h |
| ST-041 | The Book That Outranked The Manager / The Fruit The Tick Would Not Buy | 6 | 0 | 0 | 0 | 0 | A | ~18.7h |
| ST-042 | The Chair The Head Kept / The Manager The Book Hired | 0 | 0 | 0 | 0 | 0 | B | ~18.6h |
| ST-043 | The Ninth Tick The Tower Took / The Sitter The Chair Unwatched | 18 | 0 | 0 | 0 | 0 | C | ~18.4h |
| ST-044 | The Card That Hired Nothing / The Eleventh Tick The Tower Charged | 4 | 0 | 0 | 0 | 0 | D | ~18.1h |
| ST-045 | The Doorway The Watcher Unwatched / The Name Left Bare | 8 | 0 | 0 | 0 | 0 | A | ~17.9h |
| ST-046 | The Thirteenth Tick The Leaving Paid / The Sitter The Chair Watched Past | 15 | 0 | 0 | 0 | 0 | B | ~17.7h |
| ST-047 | The Two Names Left Bare / The Fifteenth Tick The Second Hand Paid | 16 | 0 | 0 | 0 | 0 | C | ~17.5h |
| ST-048 | The Head That Turned To The Doorway / The Card That Came Back | 6 | 0 | 0 | 0 | 0 | D | ~17.3h |
| ST-049 | The Seventeenth Tick The Removal Paid / The Chair The Watcher Left | 20 | 0 | 0 | 0 | 0 | A | ~17.1h |
| ST-050 | The Card That Changed Its Name / The Eighteenth Tick The Leaving Paid | 21 | 0 | 0 | 0 | 0 | B | ~17.0h |
| ST-051 | The Figure That Came To The Edge / The Name That Faded Through The Broadcast | 30 | 0 | 0 | 0 | 0 | C | ~16.8h |
| ST-052 | The Nineteenth Tick The Return Paid / The Hand That Passed The Glass | 19 | 0 | 0 | 0 | 0 | D | ~16.6h |
| ST-053 | The Name The Slip Refused To Sign / The Twentieth Tick The Fruit Paid | 12 | 0 | 0 | 0 | 0 | A | ~16.5h |
| ST-054 | The Third Hand The Chair Refused / The Witness The Desk Refused | 4 | 0 | 0 | 0 | 0 | B | ~16.3h |
| ST-055 | The Price Peter Refused To Name / The Watcher The Hall Watched | 0 | 0 | 0 | 0 | 0 | C | ~16.0h |
| ST-056 | The Strike The Room Refused / The Seat The Glass Filled | 27 | 0 | 0 | 0 | 0 | D | ~15.8h |
| ST-057 | The Tick The Keeper Paid / The Strike The Room Undid | 57 | 0 | 0 | 0 | 0 | A | ~15.5h |
| ST-058 | The Fruit The Tower Took / The Answer The Monitor Gave | 8 | 0 | 0 | 0 | 0 | B | ~15.3h |
| ST-059 | The Name The Slip Doubled / The Fruit The Tower Refused | 42 | 0 | 0 | 0 | 0 | C | ~15.1h |
| ST-060 | The Watcher That Rose / The Name The Broadcast Spoke | 60 | 0 | 0 | 0 | 0 | D | ~14.9h |
| ST-061 | The Coin The Machine Spent / The Chair Laura Sat In | 28 | 0 | 0 | 0 | 0 | A | ~14.7h |
| ST-062 | The Name The Dispatcher Struck / The Padlock The Hallway Kept Locked | 71 | 0 | 0 | 0 | 0 | B | ~14.5h |
| ST-063 | The Crate The Lot Counted As A Van / The Shelf The Archive Built Too Tall | 1 | 0 | 0 | 0 | 0 | C | ~9.0h |
| ST-064 | The Shutter The Hallway Lowered At Noon / The Shelf The Archive Sank Below Its Floor | 3 | 0 | 0 | 0 | 0 | D | ~2.9h |

Cohort median 13.5 (n=50, mean 22.2); 24/50 at ≤9 plays; 3 at 0 plays (ST-040, ST-042, ST-055); 10/50 at ≥50. Band medians: ST-015…019 58 (healthy, ~23h); ST-020…029 5.5; ST-030…039 23; ST-040…049 7; ST-050…059 20; ST-060…062 60 (healthy, ~15h). Likes 4 (ST-019 3, ST-037 1), comments 0, shares 0, saves 0 across 50 new posts. The collapse is NOT uniform: the morning batch (10:10–10:57 AM) and the evening batch (6:54–7:16 PM) read healthy, while the 11:07 AM–~6:00 PM window is depressed with wide per-post variance (2 vs 55 within the same hour) — partial suppression, not the uniform 0–9 of the 2026-10-16 collapse. Cause unproven; the signature matches the burst-suppression family (63 posts in ~27h at ~10–12 min spacing, ~4–5/hour sustained) rather than a per-post quality read — the same titles/caption template/tag rotation as the healthy batches. ST-063 (1 play / 9.0h) and ST-064 (3 / 2.9h) are young-tail watch items for the next run, not verdicts: run #15's slow starts resolved 0→63 / 2→64 in this same format.

## 2026-11-05 ~09:57 EST — LATE STUDIO CORROBORATION (correction to the run #16 proxy read; formal governor verdict)

Formal Studio verdict on the 09:44–09:56 EST read (428 posts, 0 drafts): Studio matches the proxy on ALL 66 values exactly — views, likes, comments, and both re-checks. The proxy is fully corroborated; the governor verdict stands unchanged and is now Studio-grade: new-cohort median 13.5 vs previous run 59.5 (−77.3% raw; −81.1% matched-age), park 48–72h and nag floor 6 → 30 min already in force. Clean-day counter stays RESET at 0. No pacing change beyond the throttle already applied.

Studio-only confirmations: no post newer than ST-064 (Nov 5, 6:52 AM, 3 views); no banner or "Content under review" / "unavailable to some audiences" badge on any ST row or on the E2M-055/E2M-031 analytics pages, all Privacy Everyone; unledgered second E2M-006 persists (Oct 26, 9:35 PM, 60 views; ledgered 9:51 PM post 62 views); E2M-055 holds 97 views / 0 likes (Shares 0, Saves 0, avg watch 3.99s, 0% full-watch); E2M-031 holds 7 views / 1 like (Shares 0, Saves 0, avg watch 9.14s, 0% full-watch). Shares/Saves spot-checks on ST-062 (71 views), ST-019 (75), ST-006 (98) all 0/0; avg watch 2.9s / 2.36s / 6.45s (ST-006 highest, 2% full-watch). The proxy's ST-011 save (1) was NOT opened in Studio Analytics, so it stands uncontradicted as the public-page value. Studio home "Last 7 days": video views 2.8K (−47.0%), profile views 7 (−65.0%), likes 28 (−50.9%), comments 6 (+100.0%), shares 0 (−100.0%) — down sharply vs run #15's 4.1K (+3.8%), consistent with the collapse.

Data-reliability note (new): Studio served INCONSISTENT data within minutes — the first Posts-list pass (09:44–09:45) showed ST-037…062 with later times (5:01–11:00 PM Nov 4) and views mostly 1–5; after a reload (09:47) the same 26 posts showed the ledger times and the proxy's values (0–71). The second pass was cross-checked against the public profile grid, video-page "14h ago", recommended-videos list, and per-video Analytics (ST-062 = 71) and is the authoritative set; the first-pass figures are discarded, recorded only in the browser report. The proxy (read ~09:44–09:47, matching the second pass exactly on all 26) was never the wrong instrument — Studio's first render was. Next run: if a Studio pass disagrees with the proxy, reload and cross-check before trusting either.

Title-collision note (ledger-confirmed): E2M-029 is also titled "The Slow Ledger" (ledger, 2026-10-27 ~07:48 AM EDT), the same title as E2M-055 — a duplicate title in the episode catalog, not a duplicate post. (Studio lists E2M-029 at 1:38 PM Oct 27 vs the ledger's approximate ~07:48 AM; time discrepancy noted, not resolved.)

## 2026-11-05 ~11:12 EST — daily governor run #17, PROXY READ (PARK HOLDS — no recovery, no further decay; Studio report pending)

GOVERNOR: NO NEW ACTION — the park fired by run #16 is already in force (resume ≥ 2026-11-07 ~09:50 EST, auto-lift 2026-11-08 ~09:50 EST) and this re-check gives no reason to lift, shorten, or extend it. The collapsed cohort is FLAT, not recovering and not decaying further: new-cohort ST-015…064 median plays/post 13.5, identical to run #16's 13.5 (mean 22.2, identical; 24/50 at ≤9 plays, identical; 3 at 0 plays, identical; 10/50 at ≥50, identical). Exactly ONE of 66 re-read values moved in ~1.4h: ST-054 4→5 (+1). The ST-001…014 re-check median is 63.5, identical to run #16, all 14 flat or up. The matched-age picture is unchanged: the cohort is now ~19–26h old and its median sits exactly where run #16 left it. FYP % unobservable on all 67 posts (max 98 plays < 100) — withheld, not near-zero, so the FYP clause does not fire. Clean-day counter stays RESET at 0: no clean day can be certified during a park, and the one post that did land in the interval went out through the park, not under the new pace. Review stays DAILY until 7 consecutive clean days at the new pace. No re-tightening without replicated evidence.

PARK LEAK (new fact, recorded not adjudicated): ST-065 posted 2026-11-05 ~10:49 AM EST — 59 minutes AFTER the park was written — because the kickstand nag body contains no park-file gate (the enforcement gap flagged to the user ~09:58 EST, decision still pending). The nag picked up the freshly shipped soap episode 065 and posted it at the 30-min floor. The post is live and ledgered; the governor does not un-post. The park still holds for everything after ST-065: no further uploads are due before the resume time (the station queue is otherwise empty — no ST-066 exists yet), and the 30-min floor remains the operative throttle on resume. ST-065 reads 0 plays at ~0.4h — a fresh post, not a verdict; its ~24h re-check is the next run's watch item.

Public-page proxy read (plays, not Studio views), all 67 pages crawled fresh ~11:10–11:14 EST via the repo's new proxy script (goals/wubutv-tiktok-channel-operation/hidden_files/tiktok_proxy_crawl.py; method validated against run #16: ST-062 page reads playCount 71, exactly the run #16 value). Signed-in Studio browser task (browser-task:543014d7…) was still in flight at bank time — a late Studio report supersedes this entry as a correction, as in runs #5/#6/#8/#9/#10/#11/#12/#13/#14/#16. Profile cross-check: video_count 429 = 428 (run #16 Studio total) + ST-065 exactly; followers 1794 (flat); total likes 28.8K (flat).

### Re-checks (ST-001…014 at ~26–30h; E2M-055, E2M-031)

| Episode | Title | Plays (proxy) | Likes | Comments | Shares | Saves | For-You % | Source |
|---------|-------|--------------|-------|----------|--------|-------|-----------|--------|
| ST-001 | The Late Announcement / The Overheard Promise | 71 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~30.4h (was 71, flat)) |
| ST-002 | The Demand / The Second Warmth | 63 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~30.2h (was 63, flat)) |
| ST-003 | The Third Word, Read / The First Watch | 72 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~30.0h (was 72, flat)) |
| ST-004 | The First Reading / The Third Reading | 95 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~29.9h (was 95, flat)) |
| ST-005 | The Fifth Reading / The First Precedent | 88 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~29.7h (was 88, flat)) |
| ST-006 | The First Settlement / The First Recount | 98 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~27.7h (was 98, flat)) |
| ST-007 | The Keeper'S Hearing / The First Standing | 53 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~27.5h (was 53, flat)) |
| ST-008 | The Heard Guest'S First Telling / The First Holding | 55 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~27.2h (was 55, flat)) |
| ST-009 | The First Seating In The Gallery / The First Filing | 56 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~27.0h (was 56, flat)) |
| ST-010 | The Returned Hearing / The Sealed Question | 61 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~26.8h (was 61, flat)) |
| ST-011 | The Return Nobody Sent For / The Coat Worn Inside Out | 64 | 1 | 0 | 0 | 1 | withheld <100 | public post page re-check (~26.6h (was 64, flat)) |
| ST-012 | The Slip The Pocket Kept / The Third Mark That Returned Its Maker | 57 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~26.4h (was 57, flat)) |
| ST-013 | The Fifth Mark That Kept Its Secret / The Seventh Mark That Returned Its Counter | 70 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~26.2h (was 70, flat)) |
| ST-014 | The Ninth Wave That Framed Its Field / The Eleventh Letter That Returned Its Sender | 63 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~25.9h (was 63, flat)) |
| E2M-055 | The Slow Ledger | 97 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (7th consecutive check at 97 (was 97, flat)) |
| E2M-031 | The Claimed Letters | 7 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (7th flat check; solved hook case (was 7, flat)) |

Re-check median 63.5 (n=14), all 14 flat vs run #16 — the ST cohort's matched-age anchor holds. No slow-start movement in this interval: the anchor posts have stopped growing at ~26–30h (their growth happened between run #15 and run #16, not since).

### Cohort ST-015…065 (n=51: the run #16 cohort re-read + ST-065, posted through the park)

| Episode | Title | Plays (proxy) | Likes | Comments | Shares | Saves | Tag | Age |
|---------|-------|--------------|-------|----------|--------|-------|-----------|-----|-----|
| ST-015 | The Thirteenth Letter That Kept Its Family / The Fifteenth Letter That Returned Its Reader | 53 | 0 | 0 | 0 | 0 | C | ~25.0h |
| ST-016 | The Shift That Kept Its Keeper / The Night With Two Keepers | 58 | 0 | 0 | 0 | 0 | D | ~24.8h |
| ST-017 | The Keeper Who Returned Twice / The Name The Buyer Collected | 58 | 0 | 0 | 0 | 0 | A | ~24.6h |
| ST-018 | The Buyer Who Came Back / The Answer That Arrived First | 52 | 0 | 0 | 0 | 0 | B | ~24.4h |
| ST-019 | The Fruit The Count Would Not Take / The Paycheck The Building Signed | 75 | 3 | 0 | 0 | 0 | C | ~24.2h |
| ST-020 | The Tower That Answered Back / The Name The Building Kept | 6 | 0 | 0 | 0 | 0 | D | ~24.1h |
| ST-021 | The Hand Nobody Recognized / The Look That Followed | 9 | 0 | 0 | 0 | 0 | A | ~23.9h |
| ST-022 | The Door That Kept Her Place / The Step The Dispatcher Took | 7 | 0 | 0 | 0 | 0 | B | ~23.7h |
| ST-023 | The Seventh The Stranger Stamped / The Sixth Sum | 28 | 0 | 0 | 0 | 0 | C | ~23.6h |
| ST-024 | The Hall That Kept Walking / The Name The Stamp Hired | 2 | 0 | 0 | 0 | 0 | D | ~23.4h |
| ST-025 | The Count The Tower Claimed / The Doorway That Took Its Next Stander | 5 | 0 | 0 | 0 | 0 | A | ~23.2h |
| ST-026 | The Hand That Hovered / The Fruit The Tower Counted | 2 | 0 | 0 | 0 | 0 | B | ~23.1h |
| ST-027 | The Chair The Keeping Settled On / The Hand That Was Pushed | 7 | 0 | 0 | 0 | 0 | C | ~22.8h |
| ST-028 | The Tick That Stayed / The Sitter The Chair Watched | 1 | 0 | 0 | 0 | 0 | D | ~22.6h |
| ST-029 | The Hand That Lifted / The Tick That Ticked Alone | 5 | 0 | 0 | 0 | 0 | A | ~22.5h |
| ST-030 | The Doorway The Chair Left / The Hand That Witnessed | 2 | 0 | 0 | 0 | 0 | B | ~22.3h |
| ST-031 | The Third Tick Nobody Paid For / The Keeping One Leaving Late | 55 | 0 | 0 | 0 | 0 | C | ~22.1h |
| ST-032 | The Witness Replaced / The Fourth Tick Nobody Owes | 3 | 0 | 0 | 0 | 0 | D | ~21.9h |
| ST-033 | The Chair That Watched Him Sit / The Slip The Claimant Signed | 17 | 0 | 0 | 0 | 0 | A | ~21.7h |
| ST-034 | The Tick The Station Paid / The Chair That Watched Her Sit | 56 | 0 | 0 | 0 | 0 | B | ~21.5h |
| ST-035 | The Book The Manager Reached For / The Sixth Tick The Machine Spoke | 43 | 0 | 0 | 0 | 0 | C | ~21.2h |
| ST-036 | The Third Sit The Head Refused / The Name The Book Kept Twice | 6 | 0 | 0 | 0 | 0 | D | ~21.0h |
| ST-037 | The Seventh Tick That Named The Fruit / The Chair Nobody Sat In | 47 | 1 | 0 | 0 | 0 | A | ~20.8h |
| ST-038 | The Pocket The Page Kept / The Fruit The Tower Owed | 29 | 0 | 0 | 0 | 0 | B | ~20.6h |
| ST-039 | The Doorway The Head Kept / The Hand The Page Would Not Match | 6 | 0 | 0 | 0 | 0 | C | ~20.5h |
| ST-040 | The Eighth Tick The Coin Became / The Man The Head Chose | 0 | 0 | 0 | 0 | 0 | D | ~20.3h |
| ST-041 | The Book That Outranked The Manager / The Fruit The Tick Would Not Buy | 6 | 0 | 0 | 0 | 0 | A | ~20.1h |
| ST-042 | The Chair The Head Kept / The Manager The Book Hired | 0 | 0 | 0 | 0 | 0 | B | ~20.0h |
| ST-043 | The Ninth Tick The Tower Took / The Sitter The Chair Unwatched | 18 | 0 | 0 | 0 | 0 | C | ~19.8h |
| ST-044 | The Card That Hired Nothing / The Eleventh Tick The Tower Charged | 4 | 0 | 0 | 0 | 0 | D | ~19.6h |
| ST-045 | The Doorway The Watcher Unwatched / The Name Left Bare | 8 | 0 | 0 | 0 | 0 | A | ~19.4h |
| ST-046 | The Thirteenth Tick The Leaving Paid / The Sitter The Chair Watched Past | 15 | 0 | 0 | 0 | 0 | B | ~19.1h |
| ST-047 | The Two Names Left Bare / The Fifteenth Tick The Second Hand Paid | 16 | 0 | 0 | 0 | 0 | C | ~18.9h |
| ST-048 | The Head That Turned To The Doorway / The Card That Came Back | 6 | 0 | 0 | 0 | 0 | D | ~18.8h |
| ST-049 | The Seventeenth Tick The Removal Paid / The Chair The Watcher Left | 20 | 0 | 0 | 0 | 0 | A | ~18.6h |
| ST-050 | The Card That Changed Its Name / The Eighteenth Tick The Leaving Paid | 21 | 0 | 0 | 0 | 0 | B | ~18.4h |
| ST-051 | The Figure That Came To The Edge / The Name That Faded Through The Broadcast | 30 | 0 | 0 | 0 | 0 | C | ~18.2h |
| ST-052 | The Nineteenth Tick The Return Paid / The Hand That Passed The Glass | 19 | 0 | 0 | 0 | 0 | D | ~18.1h |
| ST-053 | The Name The Slip Refused To Sign / The Twentieth Tick The Fruit Paid | 12 | 0 | 0 | 0 | 0 | A | ~17.9h |
| ST-054 | The Third Hand The Chair Refused / The Witness The Desk Refused | 5 | 0 | 0 | 0 | 0 | B | ~17.7h |
| ST-055 | The Price Peter Refused To Name / The Watcher The Hall Watched | 0 | 0 | 0 | 0 | 0 | C | ~17.4h |
| ST-056 | The Strike The Room Refused / The Seat The Glass Filled | 27 | 0 | 0 | 0 | 0 | D | ~17.2h |
| ST-057 | The Tick The Keeper Paid / The Strike The Room Undid | 57 | 0 | 0 | 0 | 0 | A | ~16.9h |
| ST-058 | The Fruit The Tower Took / The Answer The Monitor Gave | 8 | 0 | 0 | 0 | 0 | B | ~16.7h |
| ST-059 | The Name The Slip Doubled / The Fruit The Tower Refused | 42 | 0 | 0 | 0 | 0 | C | ~16.5h |
| ST-060 | The Watcher That Rose / The Name The Broadcast Spoke | 60 | 0 | 0 | 0 | 0 | D | ~16.3h |
| ST-061 | The Coin The Machine Spent / The Chair Laura Sat In | 28 | 0 | 0 | 0 | 0 | A | ~16.1h |
| ST-062 | The Name The Dispatcher Struck / The Padlock The Hallway Kept Locked | 71 | 0 | 0 | 0 | 0 | B | ~15.9h |
| ST-063 | The Crate The Lot Counted As A Van / The Shelf The Archive Built Too Tall | 1 | 0 | 0 | 0 | 0 | C | ~10.4h |
| ST-064 | The Shutter The Hallway Lowered At Noon / The Shelf The Archive Sank Below Its Floor | 3 | 0 | 0 | 0 | 0 | D | ~4.3h |
| ST-065 | The Chair The Break Room Kept Warm / The Parcel The Roof Sent Down Early | 0 | 0 | 0 | 0 | 0 | A | ~0.4h (posted through the park 10:49 EST) |

Cohort ST-015…064 median 13.5 (n=50, mean 22.2); 24/50 at ≤9 plays; 3 at 0 plays (ST-040, ST-042, ST-055); 10/50 at ≥50. Band medians identical to run #16: ST-015…019 58 (healthy, ~25h); ST-020…029 5.5; ST-030…039 23; ST-040…049 7; ST-050…059 20; ST-060…062 60 (healthy, ~17h); ST-063…064 2. Likes 4 (ST-019 3, ST-037 1), comments 0, shares 0, saves 0 across the 50 — identical to run #16. The depressed window is frozen in place: not one post in ST-020…059 moved a single play in ~1.4h, including the 0-play posts. That freeze is the throttle still holding, not a recovery — a recovering cohort would show scattered +1s and +2s across the window, and the only +1 in the whole read sits at ST-054, at the window's edge. ST-063 (1 play / ~10.5h) and ST-064 (3 / ~4.4h) are still young-tail watch items: no slow-start resolution yet at these ages, and the run #16 rule (a young post is a watch item until its ~24h re-check) still governs — their verdict comes at the next run's re-check, not this one.

## 2026-11-05 ~11:23 EST — LATE STUDIO CORROBORATION (correction to the run #17 proxy read; formal governor verdict)

Formal Studio verdict on the 11:09–11:22 EST read (429 posts, 0 drafts): Studio matches the proxy on ALL 67 values exactly — views, likes, comments, and both re-checks. The proxy is fully corroborated; the governor verdict stands unchanged and is now Studio-grade: park holds, no new action (cohort median 13.5 flat vs run #16; ST-054 4→5 the only mover; ST-065 0 at ~0.4h, posted through the park). Clean-day counter stays RESET at 0. No pacing change beyond the throttle already applied.

Studio-only confirmations: no post newer than ST-065 (Nov 5, 10:49 AM, 0 views); no banner or "Content under review" / "unavailable to some audiences" badge on any ST row or on the E2M-055/E2M-031 analytics pages, all Privacy Everyone; unledgered second E2M-006 persists (Oct 26, 9:35 PM, 60 views; ledgered 9:51 PM post 62 views); E2M-055 holds 97 views / 0 likes (Shares 0, Saves 0, avg watch 3.99s, 0% full-watch); E2M-031 holds 7 views / 1 like (Shares 0, Saves 0, avg watch 9.14s, 0% full-watch). Shares/Saves spot-checks on ST-062 (71 views), ST-019 (75), ST-006 (98) all 0/0; avg watch 2.9s / 2.36s / 6.45s (ST-006 highest, 2% full-watch). The proxy's ST-011 save (1) was NOT opened in Studio Analytics, so it stands uncontradicted as the public-page value. Studio home "Last 7 days": video views 2.4K (−62.9%), profile views 2 (−91.7%), likes 21 (−68.2%), comments 6 (+100.0%), shares 0 (−100.0%) — down further vs run #16's 2.8K (−47.0%), consistent with the collapse plus the park (no new posts in the window except ST-065, which posted into the park).

Data-reliability note (replicates run #16): Studio served INCONSISTENT data within minutes — the first Posts-list pass (~11:09 AM, confirmed by an immediate reload) showed ST-060 at 7 views, ST-059 at 0, ST-058 at 2, with ST-024…ST-046 times shifted 1–29 minutes later than the ledger; after three fresh navigations (~11:12, ~11:17, ~11:20 AM, all agreeing) the same posts showed the proxy's values (ST-060 60, ST-059 42, ST-058 8, ledger times), cross-checked against the public profile grid, public video pages ("16h ago" / "23h ago"), and per-video Analytics. The first-pass figures are discarded, recorded only in the browser report. The proxy (read ~11:10–11:14, matching the corrected pass exactly on all 67) was never the wrong instrument — Studio's first render was stale, twice in a row now. Next run: if a Studio pass disagrees with the proxy, reload and cross-check before trusting either. Caveat carried from the browser report: within the ST-024…ST-046 minute-shift band, only ST-026 was directly arbitrated by a public page; the rest of that band is trusted by extension of the same corrected render.
## 2026-11-06 ~09:45 EST — daily governor run #18, PROXY READ (PARK HOLDS — young tail resolved, depressed window still frozen; 3 more park leaks; Studio report pending)

GOVERNOR: NO NEW ACTION — the park fired by run #16 is already in force (resume ≥ 2026-11-07 ~09:50 EST, auto-lift 2026-11-08 ~09:50 EST) and this re-check gives no reason to lift, shorten, or extend it. New-cohort ST-015…064 median plays/post 17.5 vs run #16/#17's 13.5 (+29.6%) — a RISE, not the >40% drop the governor fires on, and it is driven by the young tail resolving (ST-063 1→86, ST-064 3→92, ST-065 0→95), not by the depressed window recovering: the mid-window bands ST-020…029 (median 6.0) and ST-040…049 (7.5) are still depressed, 22/50 posts at ≤9 plays, and the same 3 posts sit at 0 (ST-040, ST-042, ST-055 — now ~43h old, confirmed flatlines). FYP % unobservable from public pages on all 70 posts (max 113 plays; ST-066 at 113 is the first ST post over 100 and the first STATION-format FYP% candidate — the Studio report must read it). Clean-day counter stays RESET at 0: no clean day can be certified during a park, and the three posts that landed in the interval went out through the park, not under the new pace. Review stays DAILY until 7 consecutive clean days at the new pace. No re-tightening without replicated evidence.

PARK LEAK (continuation, recorded not adjudicated): THREE more posts landed through the park since run #17 — ST-066 (2026-11-05 ~3:03 PM EST), ST-067 (~6:54 PM EST), ST-068 (2026-11-06 ~4:48 AM EST) — because the kickstand nag body still contains no park-file gate (enforcement gap flagged to the user 2026-11-05 ~09:58 EST, decision still pending). The nag keeps picking up freshly shipped soap episodes as they arrive. The posts are live and ledgered; the governor does not un-post. The leak count is now 4 (ST-065…068). The park still holds for everything after ST-068: the station queue is otherwise empty (no ST-069 exists yet — the master pool is dry, ep069 waits on the next Q4 master), so no further leak is possible before the resume time unless a new episode ships.

Public-page proxy read (plays, not Studio views), all 70 pages crawled fresh ~09:44–09:48 EST via the repo's proxy script (goals/wubutv-tiktok-channel-operation/hidden_files/tiktok_proxy_crawl.py; snapshot review_2026-11-06_0943_proxy.json). Signed-in Studio browser task (browser-task:6437af09-…) still in flight at bank time — a late Studio report supersedes the proxy numbers as a correction, as in runs #5/#6/#8/#9/#10/#11/#12/#13/#14/#16/#17. Profile cross-check: video_count 432 = 429 (run #17 Studio total) + ST-066/067/068 exactly; followers 1794 (flat); total likes 28.8K (flat).

### Re-checks (ST-001…014 at ~50–54h; E2M-055, E2M-031)

| Episode | Title | Plays (proxy) | Likes | Comments | Shares | Saves | For-You % | Source |
|---------|-------|--------------|-------|----------|--------|-------|-----------|--------|
| ST-001 | The Late Announcement / The Overheard Promise | 71 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~52.9h (was 71, flat)) |
| ST-002 | The Demand / The Second Warmth | 63 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~52.7h (was 63, flat)) |
| ST-003 | The Third Word, Read / The First Watch | 72 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~52.6h (was 72, flat)) |
| ST-004 | The First Reading / The Third Reading | 95 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~52.4h (was 95, flat)) |
| ST-005 | The Fifth Reading / The First Precedent | 88 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~52.2h (was 88, flat)) |
| ST-006 | The First Settlement / The First Recount | 99 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~50.2h (was 98, +1)) |
| ST-007 | The Keeper'S Hearing / The First Standing | 53 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~50.0h (was 53, flat)) |
| ST-008 | The Heard Guest'S First Telling / The First Holding | 55 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~49.7h (was 55, flat)) |
| ST-009 | The First Seating In The Gallery / The First Filing | 56 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~49.5h (was 56, flat)) |
| ST-010 | The Returned Hearing / The Sealed Question | 61 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~49.3h (was 61, flat)) |
| ST-011 | The Return Nobody Sent For / The Coat Worn Inside Out | 64 | 1 | 0 | 0 | 1 | withheld <100 | public post page re-check (~49.1h (was 64, flat)) |
| ST-012 | The Slip The Pocket Kept / The Third Mark That Returned Its Maker | 57 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~49.0h (was 57, flat)) |
| ST-013 | The Fifth Mark That Kept Its Secret / The Seventh Mark That Returned Its Counter | 70 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~48.7h (was 70, flat)) |
| ST-014 | The Ninth Wave That Framed Its Field / The Eleventh Letter That Returned Its Sender | 63 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~48.5h (was 63, flat)) |
| E2M-055 | The Slow Ledger | 97 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~171.3h (was 97, flat)) |
| E2M-031 | The Claimed Letters | 7 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~240.7h (was 7, flat)) |

Re-check median 63.5 (n=14), identical to run #16/#17 — the ST cohort's matched-age anchor holds; the anchor posts have fully plateaued (only ST-006 moved, 98→99, +1). No slow-start movement left in this band: their growth happened between run #15 and run #16, not since.

### Cohort ST-015…068 (n=54: the run #16 cohort re-read + ST-065…068, all posted through the park)

| Episode | Title | Plays (proxy) | Likes | Comments | Shares | Saves | Tag | Age |
|---------|-------|--------------|-------|----------|--------|-------|-----------|-----|-----|
| ST-015 | The Thirteenth Letter That Kept Its Family / The Fifteenth Letter That Returned Its Reader | 53 | 0 | 0 | 0 | 0 | C | ~47.6h |
| ST-016 | The Shift That Kept Its Keeper / The Night With Two Keepers | 58 | 0 | 0 | 0 | 0 | D | ~47.3h |
| ST-017 | The Keeper Who Returned Twice / The Name The Buyer Collected | 58 | 0 | 0 | 0 | 0 | A | ~47.1h |
| ST-018 | The Buyer Who Came Back / The Answer That Arrived First | 52 | 0 | 0 | 0 | 0 | B | ~47.0h |
| ST-019 | The Fruit The Count Would Not Take / The Paycheck The Building Signed | 75 | 3 | 0 | 0 | 0 | C | ~46.8h |
| ST-020 | The Tower That Answered Back / The Name The Building Kept | 6 | 0 | 0 | 0 | 0 | D | ~46.6h |
| ST-021 | The Hand Nobody Recognized / The Look That Followed | 9 | 0 | 0 | 0 | 0 | A | ~46.5h |
| ST-022 | The Door That Kept Her Place / The Step The Dispatcher Took | 7 | 0 | 0 | 0 | 0 | B | ~46.3h |
| ST-023 | The Seventh The Stranger Stamped / The Sixth Sum | 28 | 0 | 0 | 0 | 0 | C | ~46.1h |
| ST-024 | The Hall That Kept Walking / The Name The Stamp Hired | 2 | 0 | 0 | 0 | 0 | D | ~45.9h |
| ST-025 | The Count The Tower Claimed / The Doorway That Took Its Next Stander | 6 | 0 | 0 | 0 | 0 | A | ~45.8h |
| ST-026 | The Hand That Hovered / The Fruit The Tower Counted | 2 | 0 | 0 | 0 | 0 | B | ~45.6h |
| ST-027 | The Chair The Keeping Settled On / The Hand That Was Pushed | 7 | 0 | 0 | 0 | 0 | C | ~45.4h |
| ST-028 | The Tick That Stayed / The Sitter The Chair Watched | 1 | 0 | 0 | 0 | 0 | D | ~45.2h |
| ST-029 | The Hand That Lifted / The Tick That Ticked Alone | 5 | 0 | 0 | 0 | 0 | A | ~45.0h |
| ST-030 | The Doorway The Chair Left / The Hand That Witnessed | 2 | 0 | 0 | 0 | 0 | B | ~44.8h |
| ST-031 | The Third Tick Nobody Paid For / The Keeping One Leaving Late | 55 | 0 | 0 | 0 | 0 | C | ~44.6h |
| ST-032 | The Witness Replaced / The Fourth Tick Nobody Owes | 3 | 0 | 0 | 0 | 0 | D | ~44.5h |
| ST-033 | The Chair That Watched Him Sit / The Slip The Claimant Signed | 17 | 0 | 0 | 0 | 0 | A | ~44.2h |
| ST-034 | The Tick The Station Paid / The Chair That Watched Her Sit | 56 | 0 | 0 | 0 | 0 | B | ~44.0h |
| ST-035 | The Book The Manager Reached For / The Sixth Tick The Machine Spoke | 43 | 0 | 0 | 0 | 0 | C | ~43.8h |
| ST-036 | The Third Sit The Head Refused / The Name The Book Kept Twice | 6 | 0 | 0 | 0 | 0 | D | ~43.6h |
| ST-037 | The Seventh Tick That Named The Fruit / The Chair Nobody Sat In | 47 | 1 | 0 | 0 | 0 | A | ~43.4h |
| ST-038 | The Pocket The Page Kept / The Fruit The Tower Owed | 29 | 0 | 0 | 0 | 0 | B | ~43.2h |
| ST-039 | The Doorway The Head Kept / The Hand The Page Would Not Match | 7 | 0 | 0 | 0 | 0 | C | ~43.1h |
| ST-040 | The Eighth Tick The Coin Became / The Man The Head Chose | 0 | 0 | 0 | 0 | 0 | D | ~42.9h |
| ST-041 | The Book That Outranked The Manager / The Fruit The Tick Would Not Buy | 6 | 0 | 0 | 0 | 0 | A | ~42.7h |
| ST-042 | The Chair The Head Kept / The Manager The Book Hired | 0 | 0 | 0 | 0 | 0 | B | ~42.5h |
| ST-043 | The Ninth Tick The Tower Took / The Sitter The Chair Unwatched | 19 | 0 | 0 | 0 | 0 | C | ~42.3h |
| ST-044 | The Card That Hired Nothing / The Eleventh Tick The Tower Charged | 4 | 0 | 0 | 0 | 0 | D | ~42.1h |
| ST-045 | The Doorway The Watcher Unwatched / The Name Left Bare | 8 | 0 | 0 | 0 | 0 | A | ~41.9h |
| ST-046 | The Thirteenth Tick The Leaving Paid / The Sitter The Chair Watched Past | 15 | 0 | 0 | 0 | 0 | B | ~41.7h |
| ST-047 | The Two Names Left Bare / The Fifteenth Tick The Second Hand Paid | 18 | 0 | 0 | 0 | 0 | C | ~41.5h |
| ST-048 | The Head That Turned To The Doorway / The Card That Came Back | 7 | 0 | 0 | 0 | 0 | D | ~41.3h |
| ST-049 | The Seventeenth Tick The Removal Paid / The Chair The Watcher Left | 20 | 0 | 0 | 0 | 0 | A | ~41.1h |
| ST-050 | The Card That Changed Its Name / The Eighteenth Tick The Leaving Paid | 21 | 0 | 0 | 0 | 0 | B | ~41.0h |
| ST-051 | The Figure That Came To The Edge / The Name That Faded Through The Broadcast | 31 | 0 | 0 | 0 | 0 | C | ~40.8h |
| ST-052 | The Nineteenth Tick The Return Paid / The Hand That Passed The Glass | 20 | 0 | 0 | 0 | 0 | D | ~40.6h |
| ST-053 | The Name The Slip Refused To Sign / The Twentieth Tick The Fruit Paid | 12 | 0 | 0 | 0 | 0 | A | ~40.4h |
| ST-054 | The Third Hand The Chair Refused / The Witness The Desk Refused | 5 | 0 | 0 | 0 | 0 | B | ~40.2h |
| ST-055 | The Price Peter Refused To Name / The Watcher The Hall Watched | 0 | 0 | 0 | 0 | 0 | C | ~39.9h |
| ST-056 | The Strike The Room Refused / The Seat The Glass Filled | 27 | 0 | 0 | 0 | 0 | D | ~39.7h |
| ST-057 | The Tick The Keeper Paid / The Strike The Room Undid | 57 | 0 | 0 | 0 | 0 | A | ~39.5h |
| ST-058 | The Fruit The Tower Took / The Answer The Monitor Gave | 8 | 0 | 0 | 0 | 0 | B | ~39.2h |
| ST-059 | The Name The Slip Doubled / The Fruit The Tower Refused | 42 | 0 | 0 | 0 | 0 | C | ~39.0h |
| ST-060 | The Watcher That Rose / The Name The Broadcast Spoke | 60 | 0 | 0 | 0 | 0 | D | ~38.9h |
| ST-061 | The Coin The Machine Spent / The Chair Laura Sat In | 30 | 0 | 0 | 0 | 0 | A | ~38.7h |
| ST-062 | The Name The Dispatcher Struck / The Padlock The Hallway Kept Locked | 71 | 0 | 0 | 0 | 0 | B | ~38.5h |
| ST-063 | The Crate The Lot Counted As A Van / The Shelf The Archive Built Too Tall | 86 | 1 | 0 | 0 | 0 | C | ~32.9h |
| ST-064 | The Shutter The Hallway Lowered At Noon / The Shelf The Archive Sank Below Its Floor | 92 | 0 | 0 | 0 | 0 | D | ~26.9h |
| ST-065 | The Chair The Break Room Kept Warm / The Parcel The Roof Sent Down Early | 95 | 0 | 0 | 0 | 0 | A | ~22.9h |
| ST-066 | The Crate The Dock Signed Twice / The Exit The Lot Logged Before The Entry | 113 | 0 | 0 | 0 | 0 | B | ~18.7h |
| ST-067 | The Fire The Lobby Burns For Nobody / The Tower That Named Its Own Builder | 87 | 0 | 0 | 0 | 0 | C | ~14.8h |
| ST-068 | The Letter The Mail Room Sent To A Missing Number / The Viewer The Contract Cannot Name | 92 | 1 | 0 | 0 | 0 | D | ~5.0h |

Cohort ST-015…064 median 17.5 (n=50, mean 25.9); 22/50 at ≤9 plays; 3 at 0 plays (ST-040, ST-042, ST-055); 12/50 at ≥50. Band medians vs run #17: ST-015…019 58 (healthy, unchanged); ST-020…029 6.0 (was 5.5); ST-030…039 23.0 (unchanged); ST-040…049 7.5 (was 7); ST-050…059 20.5 (was 20); ST-060…062 60 (healthy, unchanged); ST-063…064 89.0 (was 2 — the young tail resolved). 12 of 67 re-read values moved since run #17 (~22.5h): the three big movers are all young-tail resolutions (ST-063 +85, ST-064 +89, ST-065 +95); the other nine are +1/+2 drift (ST-006, ST-025, ST-039, ST-043, ST-047, ST-048, ST-051, ST-052, ST-061). Likes 6 on the 54 (ST-019 3, ST-063 1, ST-068 1, ST-037 1, plus re-check likes), comments 0, shares 0, saves 1 (ST-011, unchanged). The depressed window is frozen in place at maturity: its posts are now ~42–48h old and have gained at most +2 plays in ~22.5h. That is a flatline at maturity, not a slow start — the park's 48–72h is the mechanism that lets it clear, and the first recovery read lands at the resume, not before.

Post-park cohort ST-065…068 median 93.5 (95, 113, 87, 92 — all ≥50, none ≤9): posts landing AFTER the collapse window perform in the healthy band, the same band as the pre-collapse morning batch (58) and the ST-001…014 anchor (63.5). This is the fourth data point for the time-windowed reading of the collapse (not account-level): the suppression hit the 11:07 AM–~6:00 PM Nov 4 window and did not follow the account into Nov 5–6. Caveat: these four posted into a parked channel at the 30-min floor with no competing volume, so they are not a clean pace signal — they test the channel's distribution state, not the 9/hour pace.

### Process note

The first proxy-crawl invocation this run passed the episode list space-separated; the script takes ONE comma-separated argument, so it crawled ST-001 only and overwrote the run #17 snapshot file (review_2026-11-05_1100_proxy.json) with a 1-row partial. The partial was renamed to review_2026-11-06_0943_proxy_PARTIAL_ST001_ONLY.json; run #17's full data survives in this file's run #17 tables, so no values were lost. The script's hardcoded snapshot path (still pointing at the run #17 filename) was fixed this run to a run-stamped filename, so a future run cannot clobber a prior snapshot.

### Correction (Studio report arrived ~10:05 EST)

Formal Studio verdict on the 09:44–10:03 EST read (432 posts, 0 drafts): Studio matches the proxy on ALL 70 values exactly — views, likes, comments, and both re-checks. The proxy is fully corroborated and the governor verdict stands unchanged, now Studio-grade: park holds, no new action (cohort median 17.5 vs 13.5; young tail resolved; depressed window frozen). Clean-day counter stays RESET at 0. No pacing change beyond the throttle already applied.

Studio-only confirmations: no post newer than ST-068; no banner/badge on any ST row or on E2M-055/E2M-031 (all Everyone); unledgered second E2M-006 persists (9:35 PM, 60 views; ledgered 9:51 PM, 62 views); E2M-055 97 views / 0 likes (avg watch 3.99s, 0% full-watch); E2M-031 7 views / 1 like (avg watch 9.14s, 0% full-watch). Shares Studio-confirmed 0 (16 per-video Analytics headers read individually + home "Last 7 days" Shares 0 corroborates the rest); saves 0 except ST-011's 1 (spot-check basis for the unopened zero-like rows, per the browser report's method note). Studio home "Last 7 days": video views 2.4K (−62.9%), profile views 2 (−91.7%), likes 21 (−68.2%), comments 6 (+100.0%), shares 0 (−100.0%) — identical to run #17's home figures, consistent with the park (no new posts in the window except the three leaks, which posted into it).

FIRST STATION FYP% READING: ST-066 (113 views) — For You 93.8%, Following 3.5%, Search 1.8%, Other 0.9%, DM <0.1%, profile <0.1%; avg watch 5.87s; 0% full-watch; most viewers stopped at 0:02. FYP traffic is healthy on the first post that crossed the 100-view threshold — the FYP clause does not fire, and the post-park cohort's healthy views are For You-driven, not follower-driven. E2M-055 stays just below threshold (97) with no breakdown. Spot-check avg watch: ST-068 6.47s / 1.1% full-watch, ST-067 2.68s / 0%, ST-065 5.43s / 0%, ST-063 6.43s / 0%, ST-003 7.68s (1 new follower — the only follower gain in the spot-checks), ST-001 6.2s / 2.7%.

Discrepancies: ST-068 posted Nov 6, 4:47 AM in Studio vs ~4:48 AM in the ledger — 1 minute, trivial, ledger time stands as approximate. Data-reliability note (new this run): Studio's AGGREGATE surfaces lag the Posts list by ~2 days — the home video-views chart's last point is Nov 4, and Analytics > Content "top posts (last 7 days)" lists E2M-055 (97) as #1 and omits ST-066 (113) and every other Nov 5–6 ST video; "Most likes" omits ST-019 (3 likes) and ST-068. The home "Last 7 days" video-views total (2.4K) also does not reconcile with the summed ST-range views (2,647, all inside the window). The Posts-list figures are the current ones — never use the top-posts rankings or the home chart as a cross-check. No stale first render this run (top-five figures identical across four renders 9:44–10:03 AM) — the stale-render pattern of runs #16/#17 did not repeat. Also ledger-confirmed duplicate titles in E2M: E2M-029 = "The Slow Ledger" (same as E2M-055), E2M-010/E2M-017 = "The Kept Hours", E2M-003/E2M-049 = "The Kept Rooms" — duplicate titles, not duplicate posts. Studio Posts-list search box does not filter (typed queries left the list unfiltered) — a UI quirk, not a data issue.

## 2026-11-07 ~09:43 EST — daily governor run #19, PROXY READ (PARK REACHES 48h RESUME POINT — no new action; new cohort healthy at the 30-min floor; depressed window frozen at ~72h; 4 more park leaks; Studio report pending)

GOVERNOR: NO NEW ACTION — the park fired by run #16 reaches its 48h resume point at this run (resume ≥ 2026-11-07 ~09:50 EST, auto-lift 2026-11-08 ~09:50 EST) and nothing in this read extends, shortens, or re-fires it. The new cohort ST-069…072 (posted 2026-11-06 ~12:51 PM – 2026-11-07 ~02:52 AM EST, all four through the park at the 30-min floor) reads median plays/post 94.0 vs run #18's post-park cohort ST-065…068 median 93.5 (+0.5%) — flat-to-rising, not the >40% drop the governor fires on. The re-check cohort ST-015…064 median 17.5 is identical to run #18, and the ST-001…014 anchor median 63.5 is identical — no decay anywhere. FYP % unobservable from public pages on all 74 posts (max 122 plays; ST-066 at 122 is now the second ST post over 100, and run #18's Studio correction already read its FYP at 93.8% — healthy, so the FYP clause does not fire from this read; the Studio report must confirm the new cohort's FYP%). Clean-day credit WITHHELD (counter stays RESET at 0): no credit on a proxy read, per runs #5/#6/#8 precedent — if the late Studio report corroborates these numbers, credit applies as a correction (clean day 1 at the 30-min floor). Review stays DAILY until 7 consecutive clean days at the new pace. No re-tightening without replicated evidence.

PARK LEAK (continuation, recorded not adjudicated): FOUR more posts landed through the park since run #18 — ST-069 (2026-11-06 ~12:51 PM EST), ST-070 (~6:55 PM EST), ST-071 (~10:50 PM EST), ST-072 (2026-11-07 ~02:52 AM EST) — because the kickstand nag body still contains no park-file gate (enforcement gap flagged to the user 2026-11-05 ~09:58 EST, decision still pending). The nag keeps picking up freshly shipped soap episodes as they arrive. The posts are live and ledgered; the governor does not un-post. The leak count is now 8 (ST-065…072). All four leaked posts predate this run's 09:50 EST resume point, so they are leaks, not post-park posts; the first post landing after ~09:50 EST today is the first genuinely post-park post. The park file itself is not deleted by this run: its 48–72h window runs to the 2026-11-08 ~09:50 EST auto-lift, and the 30-min floor it imposed stays operative either way.

Public-page proxy read (plays, not Studio views), all 74 pages crawled fresh ~09:44–09:51 EST via the repo's proxy script (goals/wubutv-tiktok-channel-operation/hidden_files/tiktok_proxy_crawl.py; snapshot review_2026-11-07_1449_proxy.json). Signed-in Studio browser task (browser-task:ff24f9f5-4fcd-5fc1-b6b2-1a6439af735a) still in flight at bank time — a late Studio report supersedes the proxy numbers as a correction, as in runs #5/#6/#8/#9/#10/#11/#12/#13/#14/#16/#17/#18. Profile cross-check: video_count 436 = 432 (run #18 Studio total) + ST-069/070/071/072 exactly; followers 1794 (flat); total likes 28.8K (flat).

### Re-checks (ST-001…014 at ~77.0–72.5h; E2M-055, E2M-031)

| Episode | Title | Plays (proxy) | Likes | Comments | Shares | Saves | For-You % | Source |
|---------|-------|--------------|-------|----------|--------|-------|-----------|--------|
| ST-001 | The Late Announcement / The Overheard Promise | 71 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~77.0h (was 71, flat)) |
| ST-002 | The Demand / The Second Warmth | 63 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~76.8h (was 63, flat)) |
| ST-003 | The Third Word, Read / The First Watch | 72 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~76.7h (was 72, flat)) |
| ST-004 | The First Reading / The Third Reading | 95 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~76.5h (was 95, flat)) |
| ST-005 | The Fifth Reading / The First Precedent | 88 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~76.3h (was 88, flat)) |
| ST-006 | The First Settlement / The First Recount | 99 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~74.3h (was 99, flat)) |
| ST-007 | The Keeper'S Hearing / The First Standing | 53 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~74.1h (was 53, flat)) |
| ST-008 | The Heard Guest'S First Telling / The First Holding | 55 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~73.8h (was 55, flat)) |
| ST-009 | The First Seating In The Gallery / The First Filing | 56 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~73.6h (was 56, flat)) |
| ST-010 | The Returned Hearing / The Sealed Question | 61 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~73.4h (was 61, flat)) |
| ST-011 | The Return Nobody Sent For / The Coat Worn Inside Out | 64 | 1 | 0 | 0 | 1 | withheld <100 | public post page re-check (~73.2h (was 64, flat)) |
| ST-012 | The Slip The Pocket Kept / The Third Mark That Returned Its Maker | 57 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~73.0h (was 57, flat)) |
| ST-013 | The Fifth Mark That Kept Its Secret / The Seventh Mark That Returned Its Counter | 70 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~72.8h (was 70, flat)) |
| ST-014 | The Ninth Wave That Framed Its Field / The Eleventh Letter That Returned Its Sender | 63 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~72.5h (was 63, flat)) |
| E2M-055 | The Slow Ledger | 97 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~194.4h (was 97, flat)) |
| E2M-031 | The Claimed Letters | 7 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~263.8h (was 7, flat)) |

Re-check median 63.5 (n=14), identical to run #16/#17/#18 — the ST cohort's matched-age anchor holds; the anchor posts have fully plateaued (no value moved). E2M-055 holds at 97 plays for a ninth consecutive check — still 3 short of the 100-view FYP threshold; a post can stall 3 short indefinitely. E2M-031 holds at 7 plays / 1 like (9th flat check, solved hook case).

### Cohort ST-015…072 (n=58: the run #16 cohort re-read + ST-065…072, all posted through the park)

| Episode | Title | Plays (proxy) | Likes | Comments | Shares | Saves | For-You % | Source |
|---------|-------|--------------|-------|----------|--------|-------|-----------|--------|
| ST-015 | The Thirteenth Letter That Kept Its Family / The Fifteenth Letter That Returned Its Reader | 53 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~71.7h (was 53, flat)) |
| ST-016 | The Shift That Kept Its Keeper / The Night With Two Keepers | 58 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~71.4h (was 58, flat)) |
| ST-017 | The Keeper Who Returned Twice / The Name The Buyer Collected | 58 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~71.2h (was 58, flat)) |
| ST-018 | The Buyer Who Came Back / The Answer That Arrived First | 52 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~71.0h (was 52, flat)) |
| ST-019 | The Fruit The Count Would Not Take / The Paycheck The Building Signed | 75 | 3 | 0 | 0 | 0 | withheld <100 | public post page re-check (~70.9h (was 75, flat)) |
| ST-020 | The Tower That Answered Back / The Name The Building Kept | 6 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~70.7h (was 6, flat)) |
| ST-021 | The Hand Nobody Recognized / The Look That Followed | 10 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~70.5h (was 9, +1)) |
| ST-022 | The Door That Kept Her Place / The Step The Dispatcher Took | 7 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~70.3h (was 7, flat)) |
| ST-023 | The Seventh The Stranger Stamped / The Sixth Sum | 28 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~70.2h (was 28, flat)) |
| ST-024 | The Hall That Kept Walking / The Name The Stamp Hired | 2 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~70.0h (was 2, flat)) |
| ST-025 | The Count The Tower Claimed / The Doorway That Took Its Next Stander | 6 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~69.8h (was 6, flat)) |
| ST-026 | The Hand That Hovered / The Fruit The Tower Counted | 2 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~69.7h (was 2, flat)) |
| ST-027 | The Chair The Keeping Settled On / The Hand That Was Pushed | 7 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~69.5h (was 7, flat)) |
| ST-028 | The Tick That Stayed / The Sitter The Chair Watched | 1 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~69.3h (was 1, flat)) |
| ST-029 | The Hand That Lifted / The Tick That Ticked Alone | 5 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~69.1h (was 5, flat)) |
| ST-030 | The Doorway The Chair Left / The Hand That Witnessed | 2 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~68.9h (was 2, flat)) |
| ST-031 | The Third Tick Nobody Paid For / The Keeping One Leaving Late | 55 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~68.7h (was 55, flat)) |
| ST-032 | The Witness Replaced / The Fourth Tick Nobody Owes | 3 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~68.5h (was 3, flat)) |
| ST-033 | The Chair That Watched Him Sit / The Slip The Claimant Signed | 17 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~68.3h (was 17, flat)) |
| ST-034 | The Tick The Station Paid / The Chair That Watched Her Sit | 56 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~68.1h (was 56, flat)) |
| ST-035 | The Book The Manager Reached For / The Sixth Tick The Machine Spoke | 43 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~67.9h (was 43, flat)) |
| ST-036 | The Third Sit The Head Refused / The Name The Book Kept Twice | 6 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~67.7h (was 6, flat)) |
| ST-037 | The Seventh Tick That Named The Fruit / The Chair Nobody Sat In | 47 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~67.5h (was 47, flat)) |
| ST-038 | The Pocket The Page Kept / The Fruit The Tower Owed | 29 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~67.3h (was 29, flat)) |
| ST-039 | The Doorway The Head Kept / The Hand The Page Would Not Match | 7 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~67.2h (was 7, flat)) |
| ST-040 | The Eighth Tick The Coin Became / The Man The Head Chose | 0 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~67.0h (was 0, flat)) |
| ST-041 | The Book That Outranked The Manager / The Fruit The Tick Would Not Buy | 6 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~66.8h (was 6, flat)) |
| ST-042 | The Chair The Head Kept / The Manager The Book Hired | 0 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~66.6h (was 0, flat)) |
| ST-043 | The Ninth Tick The Tower Took / The Sitter The Chair Unwatched | 19 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~66.4h (was 19, flat)) |
| ST-044 | The Card That Hired Nothing / The Eleventh Tick The Tower Charged | 4 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~66.2h (was 4, flat)) |
| ST-045 | The Doorway The Watcher Unwatched / The Name Left Bare | 9 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~66.0h (was 8, +1)) |
| ST-046 | The Thirteenth Tick The Leaving Paid / The Sitter The Chair Watched Past | 15 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~65.8h (was 15, flat)) |
| ST-047 | The Two Names Left Bare / The Fifteenth Tick The Second Hand Paid | 18 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~65.6h (was 18, flat)) |
| ST-048 | The Head That Turned To The Doorway / The Card That Came Back | 7 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~65.4h (was 7, flat)) |
| ST-049 | The Seventeenth Tick The Removal Paid / The Chair The Watcher Left | 20 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~65.2h (was 20, flat)) |
| ST-050 | The Card That Changed Its Name / The Eighteenth Tick The Leaving Paid | 21 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~65.0h (was 21, flat)) |
| ST-051 | The Figure That Came To The Edge / The Name That Faded Through The Broadcast | 31 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~64.8h (was 31, flat)) |
| ST-052 | The Nineteenth Tick The Return Paid / The Hand That Passed The Glass | 20 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~64.7h (was 20, flat)) |
| ST-053 | The Name The Slip Refused To Sign / The Twentieth Tick The Fruit Paid | 12 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~64.5h (was 12, flat)) |
| ST-054 | The Third Hand The Chair Refused / The Witness The Desk Refused | 6 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~64.3h (was 5, +1)) |
| ST-055 | The Price Peter Refused To Name / The Watcher The Hall Watched | 0 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~64.0h (was 0, flat)) |
| ST-056 | The Strike The Room Refused / The Seat The Glass Filled | 27 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~63.8h (was 27, flat)) |
| ST-057 | The Tick The Keeper Paid / The Strike The Room Undid | 57 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~63.5h (was 57, flat)) |
| ST-058 | The Fruit The Tower Took / The Answer The Monitor Gave | 8 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~63.3h (was 8, flat)) |
| ST-059 | The Name The Slip Doubled / The Fruit The Tower Refused | 42 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~63.1h (was 42, flat)) |
| ST-060 | The Watcher That Rose / The Name The Broadcast Spoke | 60 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~62.9h (was 60, flat)) |
| ST-061 | The Coin The Machine Spent / The Chair Laura Sat In | 30 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~62.8h (was 30, flat)) |
| ST-062 | The Name The Dispatcher Struck / The Padlock The Hallway Kept Locked | 71 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~62.6h (was 71, flat)) |
| ST-063 | The Crate The Lot Counted As A Van / The Shelf The Archive Built Too Tall | 86 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~57.0h (was 86, flat)) |
| ST-064 | The Shutter The Hallway Lowered At Noon / The Shelf The Archive Sank Below Its Floor | 93 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~51.0h (was 92, +1)) |
| ST-065 | The Chair The Break Room Kept Warm / The Parcel The Roof Sent Down Early | 95 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~47.0h (was 95, flat)) |
| ST-066 | The Crate The Dock Signed Twice / The Exit The Lot Logged Before The Entry | 122 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~42.8h (was 113, +9)) |
| ST-067 | The Fire The Lobby Burns For Nobody / The Tower That Named Its Own Builder | 89 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~38.9h (was 87, +2)) |
| ST-068 | The Letter The Mail Room Sent To A Missing Number / The Viewer The Contract Cannot Name | 99 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~29.0h (was 92, +7)) |
| ST-069 | The Roster Read Aloud / The Count Peter Sold As An Audience | 94 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~21.0h (new this run)) |
| ST-070 | The Double the Control Room Seated / The Chamber the Stairwell Opened Twice | 87 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~14.9h (new this run)) |
| ST-071 | The Buyer the Street Seated Early / The Caller the Switchboard Never Answers | 94 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~11.0h (new this run)) |
| ST-072 | The Fruit the Boiler Room Ripens for Nobody / The Ticket the Box Office Sold to the Tomb | 99 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~7.0h (new this run)) |

Cohort ST-015…064 median 17.5 (n=50, mean 25.9); 21/50 at ≤9 plays; 3 at 0 plays (ST-040, ST-042, ST-055); 12/50 at ≥50. Band medians vs run #18: ST-015…019 58 (healthy, unchanged); ST-020…029 6.0 (unchanged); ST-030…039 23.0 (unchanged); ST-040…049 8.0 (was 7.5); ST-050…059 20.5 (unchanged); ST-060…062 60 (healthy, unchanged); ST-063…064 89.5 (was 89.0). Only 7 of 74 re-read values moved since run #18 (~24.1h): ST-066 113→122 (+9), ST-068 92→99 (+7), ST-067 87→89 (+2), ST-064 92→93 (+1), ST-021 9→10 (+1), ST-045 8→9 (+1), ST-054 5→6 (+1) — all drift on healthy posts, none in the depressed window. Likes 9 on the 74 (ST-019 3, ST-003/ST-011/ST-012/ST-037/ST-063/ST-068/ST-069 1 each, E2M-031 1), comments 0, shares 0, saves 1 (ST-011, unchanged). The depressed window is frozen in place at maturity: its posts are now ~66–72h old and have gained at most +1 play in ~24h. That is a permanent flatline at maturity, not a slow start — the park's 48–72h has now run its course without any late recovery in the window.

New cohort ST-069…072 median 94.0 (94, 87, 94, 99 — all ≥50, none ≤9): posts landing AFTER the collapse window perform in the healthy band, the same band as the pre-collapse morning batch (58), the ST-001…014 anchor (63.5), and the post-park cohort ST-065…068 (93.5). This is the fifth data point for the time-windowed reading of the collapse (not account-level): the suppression hit the 11:07 AM–~6:00 PM Nov 4 window and did not follow the account into Nov 5–7. Caveat, carried forward: these four posted into a parked channel at the 30-min floor with no competing volume, so they test the channel's distribution state, not a pace — they are the first cohort that can start certifying the 30-min floor once Studio corroborates, because they did land at that floor.

### Correction (Studio report arrived ~09:52 EST)

Formal Studio verdict on the 09:44–09:51 EST read (436 posts, 0 drafts): Studio matches the proxy on 72 of 74 values exactly — the proxy is corroborated and the governor verdict stands unchanged, now Studio-grade, with one new data-reliability note below. GOVERNOR NO ACTION, and clean-day credit APPLIES: counter 0 → 1 (clean day 1 at the 30-min floor) — the new cohort ST-069…072 matches exactly (94, 87, 94, 99; median 94.0 vs run #18's post-park 93.5, flat-to-rising, Studio-grade). Review stays DAILY (1 of 7 clean days; no weekly switch).

Studio-only confirmations: no post newer than ST-072; no banner/badge on any of the 74 checked videos (all Everyone); E2M-055 97 views / 0 likes (avg watch 3.99s, total play 0h:06m:27s, 0% full-watch, traffic source "-%" — no breakdown below 100); E2M-031 7 views / 1 like (avg watch 9.14s, total play 0h:01m:04s, 0% full-watch, all 7 views on Oct 27 — confirms the flatline, no views since Oct 27); ST-055 0 views (avg watch 0s — genuine, not stale). Shares Studio-confirmed 0 on the checked videos; home "Last 7 days": video views 3.2K (−53.1%), profile views 5 (−79.2%), likes 25 (−62.7%), comments 6 (+100%), shares 0. Sum of the 72 ST Posts-list views = 3,085.

FIRST PROXY-vs-STUDIO MISMATCH in this series: ST-011 reads 81 in Studio's Posts list vs 64 on its public page, and ST-012 reads 82 vs 57. At run #18, Studio matched the proxy on both (64/57), so the two videos genuinely gained +17/+25 views in ~24h while their public pages still served the old counts — the public page can lag Studio by a day for individual videos. The proxy's flat 64/57 for these two across runs #18/#19 was a stale-cache artifact, not a real plateau. Direction matters: Studio is HIGHER, so the anchor median rises 63.5 (proxy) → 70.5 (Studio) and no verdict weakens. The governor's key numbers (new-cohort median 94.0, ST-015…064 median 17.5, depressed bands) match exactly. Next run: a proxy-vs-Studio gap on an old video now reads as public-page cache lag, and the anchor median must be re-derived from Studio figures when they differ.

SECOND STATION FYP% READING: ST-066 (122 views) — For You 94.3%, Following 3.3%, Search 1.6%, Other 0.8%; avg watch 5.93s; 0% full-watch; most viewers stopped at 0:02. FYP traffic is healthy on the second post over 100 (first reading 93.8% in run #18) — the FYP clause does not fire, and the post-park cohort's healthy views are For You-driven. Only ST-066 is ≥100 in the Posts list; ST-068 (99) and ST-072 (99) are the next FYP% candidates if they cross 100. Unledgered second E2M-006 was not re-verified individually this run; it persists by total count (436 = 432 + ST-069…072 exactly, no new unledgered post).

## 2026-11-08 ~09:43 EST — daily governor run #20, PROXY READ (PARK AUTO-LIFTS TODAY — no new action; new cohort healthy; 5 more park leaks; Studio report pending)

GOVERNOR: NO NEW ACTION — the new cohort ST-073…077 (posted 2026-11-07 ~10:50 EST – 2026-11-08 ~08:49 EST, all five through the park at the 30-min floor) reads median plays/post 90.0 vs run #19's ST-069…072 median 94.0 (−4.3%) — flat-to-rising, not the >40% drop the governor fires on. Age-matched: ST-073 at ~22.9h reads 99 vs ST-069…072's ~21h median 94 — flat-to-rising. ST-077 at 41 plays / ~0.9h is a young-tail watch item, not a verdict (run #18/#19 young tails resolved 0→95 and 1→86 by ~24h). FYP % unobservable from public pages on all 18 posts read (max 122 plays; ST-066's FYP already read 94.3% healthy in run #19's Studio correction) — withheld, not near-zero, so the FYP clause cannot fire; the Studio report must confirm the new cohort's FYP%. Clean-day credit WITHHELD (counter holds at 1): no credit on a proxy read, per runs #5/#6/#8 precedent — if the late Studio report corroborates these numbers, credit applies as a correction (clean day 2 at the 30-min floor). Review stays DAILY until 7 consecutive clean days at the new pace. No re-tightening without replicated evidence.

PARK: the run #16 park auto-lifts at ~09:50 EST today (72h), seven minutes after this run's read. The park file stays in place through the auto-lift, per run #19's note; the 30-min floor it imposed stays operative. No new park is written by this run. The first post landing after ~09:50 EST today is the first genuinely post-park post.

PARK LEAK (continuation, recorded not adjudicated): FIVE more posts landed through the park since run #19 — ST-073 (2026-11-07 ~10:50 EST), ST-074 (~6:41 PM EST), ST-075 (2026-11-08 ~02:45 EST), ST-076 (~03:19 EST), ST-077 (~08:49 EST) — because the kickstand nag body still contains no park-file gate (enforcement gap flagged to the user 2026-11-05 ~09:58 EST, decision still pending). The leak count is now 13 (ST-065…077). All five leaked posts predate today's ~09:50 EST auto-lift, so they are leaks, not post-park posts; the leak window closes at this run's auto-lift. The posts are live and ledgered; the governor does not un-post.

Public-page proxy read (plays, not Studio views), 18 pages crawled fresh ~09:44 EST (5 new + 13 spot re-checks; the full-cohort re-check rides on the Studio task this run). Signed-in Studio browser task (browser-task:ad163b94-9eb3-53bc-934c-7940089a97ae) still in flight at bank time — a late Studio report supersedes the proxy numbers as a correction, as in runs #5/#6/#8/#9/#10/#11/#12/#13/#14/#16/#17/#18/#19.

### New cohort ST-073…077 (n=5)

| Episode | Title | Plays (proxy) | Likes | Comments | Shares | Saves | For-You % | Source |
|---------|-------|--------------|-------|----------|--------|-------|-----------|--------|
| ST-073 | The Reel the Tape Library Plays for Its Nurse / The Coat Too Big for the Check | 99 | 1 | 0 | 0 | 0 | withheld <100 | public post page (~22.9h; tag set A) |
| ST-074 | The Uniform the Laundry Room Washes for Nobody / The Lamp the Projection Booth Burns for Nobody | 108 | 0 | 0 | 0 | 0 | withheld (public page) | public post page (~15.0h; tag set B) |
| ST-075 | The Ledger the Archive Vault Begins Nowhere / The Tone the Signal Room Sings to Sleep | 89 | 1 | 0 | 0 | 0 | withheld <100 | public post page (~7.0h; tag set C) |
| ST-076 | The Pass the Gatehouse Sent Back Signed / The Poster the Print Room Sent Back Starring | 90 | 0 | 0 | 0 | 0 | withheld <100 | public post page (~6.4h; tag set D) |
| ST-077 | The Map That Came Back With A Road / The Email the Courtyard Pinned to Its Board | 41 | 0 | 0 | 0 | 0 | withheld <100 | public post page (~0.9h; tag set A) |

New cohort ST-073…077 median 90.0 (99, 108, 89, 90, 41 — four of five ≥50, none ≤9 except the 0.9h-old ST-077): posts landing AFTER the collapse window perform in the healthy band, the same band as the pre-collapse morning batch (58), the ST-001…014 anchor (63.5 proxy / 70.5 Studio), and the post-park cohorts ST-065…068 (93.5) and ST-069…072 (94.0). This is the sixth data point for the time-windowed reading of the collapse (not account-level). ST-074 at 108 plays is the highest ST post yet and the first of this cohort over 100 — a new FYP% candidate pending Studio. Likes 2, comments 0, shares 0, saves 0 on the five.

### Spot re-checks (ST-066/068/069/070/071/072, ST-011/012, ST-040/042/055, E2M-055, E2M-031)

| Episode | Title | Plays (proxy) | Likes | Comments | Shares | Saves | For-You % | Source |
|---------|-------|--------------|-------|----------|--------|-------|-----------|--------|
| ST-066 | The Crate The Dock Signed Twice / The Exit The Lot Logged Before The Entry | 122 | 0 | 0 | 0 | 0 | withheld (public page) | public post page re-check (~66.8h (was 122, flat)) |
| ST-068 | The Letter The Mail Room Sent To A Missing Number / The Viewer The Contract Cannot Name | 101 | 1 | 0 | 0 | 0 | withheld (public page) | public post page re-check (~53.0h (was 99, +2)) |
| ST-069 | The Roster Read Aloud / The Count Peter Sold As An Audience | 95 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~45.0h (was 94, +1)) |
| ST-070 | The Double the Control Room Seated / The Chamber the Stairwell Opened Twice | 88 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~38.9h (was 87, +1)) |
| ST-071 | The Buyer the Street Seated Early / The Caller the Switchboard Never Answers | 94 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~35.0h (was 94, flat)) |
| ST-072 | The Fruit the Boiler Room Ripens for Nobody / The Ticket the Box Office Sold to the Tomb | 106 | 0 | 0 | 0 | 0 | withheld (public page) | public post page re-check (~31.0h (was 99, +7)) |
| ST-011 | The Return Nobody Sent For / The Coat Worn Inside Out | 64 | 1 | 0 | 0 | 1 | withheld <100 | public post page re-check (~97.2h (was 64, flat)) |
| ST-012 | The Slip The Pocket Kept / The Third Mark That Returned Its Maker | 57 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~97.0h (was 57, flat)) |
| ST-040 | The Eighth Tick The Coin Became / The Man The Head Chose | 0 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~91.0h (was 0, flat)) |
| ST-042 | The Chair The Head Kept / The Manager The Book Hired | 0 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~90.6h (was 0, flat)) |
| ST-055 | The Price Peter Refused To Name / The Watcher The Hall Watched | 0 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~88.0h (was 0, flat)) |
| E2M-055 | The Slow Ledger | 97 | 0 | 0 | 0 | 0 | withheld <100 | public post page re-check (~218.4h (was 97, flat)) |
| E2M-031 | The Claimed Letters | 7 | 1 | 0 | 0 | 0 | withheld <100 | public post page re-check (~287.8h (was 7, flat)) |

Spot re-checks: ST-068 (99→101) and ST-072 (99→106) both crossed 100 since run #19 — three ST posts are now FYP% candidates pending Studio (ST-074 108, ST-072 106, ST-068 101), with ST-066 (122, FYP 94.3% read) as the control. ST-069…071 drift +1/flat at ~35–45h — the run #19 cohort matures in band. ST-011/ST-012 read 64/57 flat on their public pages for the third consecutive check while Studio read 81/82 at run #19 — the public-page cache lag persists (proxy undercounts; Studio is authoritative). The depressed window's three 0-play posts (ST-040/042/055) are still at 0 at ~88–91h — permanent flatlines, no late recovery even after the full 72h park. E2M-055 holds at 97 plays for a tenth consecutive check — still 3 short of the 100-view FYP threshold. E2M-031 holds at 7 plays / 1 like (10th flat check, solved hook case). Likes 5, comments 0, shares 0, saves 1 (ST-011, unchanged) across the 13 spot re-checks.

### Correction (Studio report arrived ~09:56 EST)

Formal Studio verdict on the 09:44–09:54 EST read (441 posts, 0 drafts): Studio matches the proxy on ALL 18 values exactly on the main pass — the proxy is fully corroborated and the governor verdict stands unchanged, now Studio-grade. GOVERNOR NO ACTION, and clean-day credit APPLIES: counter 1 → 2 (clean day 2 at the 30-min floor). Review stays DAILY (2 of 7 clean days; no weekly switch). No pacing change, no park change. The park auto-lifted ~09:50 EST today on its own terms; the 30-min floor stays operative.

Studio-only confirmations: no post newer than ST-077; 441 = 436 + ST-073…077 exactly, no new unledgered post; no banner/badge on any video (all Everyone); unledgered second E2M-006 persists (Oct 26, 9:35 PM, 60 views; ledgered 9:51 PM post 62 views; both views all occurred Oct 26, 0 since); E2M-055 97 views / 0 likes (avg watch 3.98s, 0% full-watch); E2M-031 7 views / 1 like (avg watch 9.14s, all 7 views Oct 27). Shares Studio-confirmed 0 on the 13 Analytics overviews opened; home "Last 7 days": video views 3K (−60.4%), profile views 8 (−66.7%), likes 19 (−68.9%), comments 5 (+25.0%), shares 0.

THREE NEW FYP% READINGS — the FYP sample triples: ST-074 (108 views) — For You 100.0%; ST-072 (106) — 99.1%; ST-068 (101) — 98.0%. With ST-066's 94.3%, all four ST posts over 100 are 94–100% For You — the post-park healthy band is For You-driven four times over, and the FYP clause does not fire. Avg watch 5.05–6.24s, full-watch 0–1%, most viewers stop at 0:02 (ST-068 the lone 1% full-watch). Next FYP candidates did NOT cross 100: ST-073 99, ST-006 99, ST-076 90–94 (still climbing), ST-075 89.

LIVE-TICK NOTE: ST-077 read 41 (main pass 09:44), 52 (Analytics 09:50), 56 (Posts 09:52); ST-076 read 90, then 91, then 94 — the young tail is resolving in real time inside the read window. On the latest figures the new-cohort median would be 94.0 (56/89/94/99/108), not 90.0; the run figures stay the main-pass values per the run rule, and the resolution is banked for run #21.

NEW DATA-RELIABILITY NOTE — Studio's own Posts-list figures for ST-011/ST-012 do NOT replicate across runs: run #19's Studio read showed 81/82, this run's Studio read (twice-verified second pass, ST-001–ST-069) shows 64/57, matching the public pages exactly on both runs. The 81/82 figures are retracted as a Studio-side anomaly, not real gains — the anchor median on Studio figures reverts to 63.5 (not 70.5). No verdict weakens: the governor's key numbers (new-cohort median 90.0, depressed bands) match exactly on every instrument. Two further +1 drifts vs run #19's proxy (ST-027 7→8, ST-058 8→9) read as genuine small gains. No stale 1–5-view first render this run (two full passes agreed). E2M supplementary rows (second pass): E2M-058 73 — matches the proxy, resolving run #14's Analytics-overview lag note (overview 66 vs Posts list 73); E2M-030 83 views / 3 likes / 1 comment; E2M-057 54 / 1 / 1; E2M-059 65; E2M-056 64 / 1 / 1; E2M-054 67 / 1 / 1. Eight E2M rows were not captured in this pass (E2M-046/045/036/035/026/025/016/015).
