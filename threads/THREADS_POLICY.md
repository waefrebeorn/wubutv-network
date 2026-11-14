# Threads Policy — @waefrebeorn

## Identity
- Account: @waefrebeorn (Threads, public, via Meta Accounts Center)
- Account ID: 17841463063141818
- Voice: same deadpan ~ WuBu ~ as Instagram. No platform-specific pandering.

## Posting
- Route: `threads-cli publish-post` (official API). One video post per run.
- Format: 16:9 landscape as-is (user ruling 2026-10-17 — same as Instagram).
- Media: MP4 ≤100MB + JPEG cover (frame at 5s). Files staged under `~/workspace/threads/`.
- Text cap: 500 chars — captions truncated at 480 with ellipsis if needed.
- Order: newest unposted bumper first (independent ledger from Instagram — same content may appear on both; it's original, no cross-post penalty).

## Cadence
- **24/day MAX** (every 1 hour, one per run). Pushed from 12/day on 2026-10-18 per user's maximize order. Threads write rate limits are strict — a 429 means stop for the day. If a 429 hits, drop back to 12/day.
- Never exceed 1 post per run.

## Rate limit handling
- 429 / "Write Rate Limit Reached" = STOP until next day. Do not retry. The script exits 2 on rate limit.
- Never hammer retries. Threads scraping protection is aggressive.

## Caption format
`B-<N> "<Title>" — <tagline>. ~ WuBu ~` + 3 hashtags, rotating sets A/B/C/D (same sets as Instagram).

## Ledger
`THREADS_POSTS.md` — every post gets a row. DEDUP_STATUS: resolved.

## Changelog
- 2026-10-18: operation created (user: "yes i am on threads sure go for it"). 12/day conservative start.
