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
