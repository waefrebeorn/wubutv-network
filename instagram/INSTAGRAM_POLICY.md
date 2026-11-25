# WuBuTV Instagram Operation Policy

## Channel
- Account: @waefrebeorn (Instagram, professional account, connected via Meta Accounts Center)
- user_fbid: 17841400684652688
- Format: 16:9 landscape bumpers posted as-is (user order 2026-10-17: "Yes, post 16:9 as-is")

## Publishing route
- `instagram-cli post-feed` — official Content Publishing API. No browser, no file picker.
- Every reel needs: --file (mp4 under ~/workspace/), --cover (jpg/png under ~/workspace/), --caption
- Files must be under ~/workspace/ (copy from wubutv-network before posting, never /tmp paths)

## Rate
- 48 posts/day = 1 per 30 minutes (user order 2026-10-17 23:12 EDT: "maximize the cadence" / "most posting per minute or hour")
- API cap is 50/24h rolling (conservative documented figure); we sit just under it — maximum sustainable velocity
- On 429: STOP ALL instagram-cli calls immediately (connector rule), park 24h, report
- Never retry a publish automatically — uncertain results get looked up first (no duplicates)

## Caption format (Instagram-optimized)
- `B-<N> "<Title>" — <tagline>. ~ WuBu ~` + 3 hashtags max
- Hashtag rotation (3 per post, never repeat the same block twice in a row):
  - Set A: #WuBuTV #deadpan #skit
  - Set B: #WuBuTV #dryhumor #comedy
  - Set C: #WuBuTV #absurdist #shortfilm
  - Set D: #WuBuTV #surreal #indiefilm
- 10s runtime hits Instagram's 7-15s viral sweet spot natively

## Order
- New end first (highest unposted B-number), straight down — no interleave on Instagram (fresh channel, no backlog asymmetry to manage)
- Skip any bumper already posted to Instagram (check INSTAGRAM_POSTS.md ledger)

## Ledger
- INSTAGRAM_POSTS.md: | B-number | Title | Post time (EDT) | Media FBID | Caption | Hashtag set | Status |
- DEDUP: a B-number with a ledger row is posted. Never re-post.

## Virality notes (research 2026-10-17)
- 60%+ of Reel views come from non-followers — Reels are the discovery engine
- First 3 seconds decide distribution; completion rate is the #1 ranking factor
- Originality Score rewards original content (ours is all original, no watermarks)
- Consistency beats volume for per-post reach — we trade per-post reach for catalog velocity by user order
- Trial Reels / new features: evaluate when Meta ships them
