# TikTok Ideas Bank

Banked findings from the TikTok manager's Kevin Bacon research chains and the
recursive learning loop. Format: date — chain/findings — production note.

## Research findings

(none yet — first `tiktok-trend-research` run banks here)

## Learning-loop findings

### 2026-10-15 ~09:52 EDT — first performance check (5 posts, ages 1.4–6.4h)

Source: read-only pull via signed-in TikTok Studio + public post pages.
Per-post numbers live in `TIKTOK_METRICS.md` (this file carries the readouts).

1. **Distribution healthy, no suppression signal (replicated 3/3).** The three
   posts with For-You traffic data show 98.9% (B-501), 98.2% (B-502), 98.4%
   (B-503) FYP share. Policy §5's early-warning instrument fires on near-zero
   FYP across 2+ consecutive posts — we see the opposite at the onset of the
   6/day cadence. Readout: hold pacing steady, no park, no change. This is a
   hold-steady signal, NOT a green light to raise pacing (needs weeks of
   replication, not one check).
2. **Engagement baseline near zero — no tag/caption read possible yet.**
   1 like + 1 share total across 5 posts; each tag set (A/B/C/D) appears 1–2×
   and post ages differ (1.4–6.4h). Null result, banked honestly: no caption
   shape (2-beat / fragment pair / declarative) or hashtag set has replicated
   evidence either way. Revisit after videos mature ~7 days, comparing at
   equal ages.
3. **Velocity skews young — don't read per-hour rates naively.** B-964
   (~1.4h old, 90 views ≈ 64/h) leads the older posts (17–27/h), but that's
   the early-distribution window, not a bumper-quality signal. Next review:
   compare each post at the same age (~24h, ~7d).
4. **Loop data-quality notes:** on sub-7h videos Studio's engagement tabs show
   "being processed" — read likes/comments/shares from the post pages in
   early checks. Studio withholds the FYP traffic breakdown until 100 views
   (B-1/B-964 showed n/a). Studio view/share rows can lag the post page
   (B-501: Studio 0 shares vs post page 1). Keep source-per-row in the
   metrics log.
5. **First engagement event on record:** B-964 "The Tide Mark" received its
   first like ~09:51 EDT — baseline timestamp for future engagement-rate work.

Policy changes proposed this run: none. No finding replicates in a
change-demanding direction; pacing holds at 6/day per the standing rule
(no upward pacing change without replicated evidence).

### 2026-10-16 ~10:16 EDT — second performance check = first daily governor run at 9/hour (72 posts, ages 10min–30.7h)

Source: read-only pull via signed-in TikTok Studio (@waefrebeorn; 1.8K followers,
29K likes; Studio shows 217 posts total). Per-post numbers live in
`TIKTOK_METRICS.md`. This is daily run #1 of the 7-day governor series — and it
FIRED. Clean-day counter: 0.

1. **DISTRIBUTION COLLAPSE (replicated 48/48 consecutive posts).** Every one of
   the 48 posts from 2026-10-15 23:25 EDT through 2026-10-16 09:34 EDT sits at
   0–9 views (median 1). Governor comparison vs previous run: 106 → 1, ~99%
   drop, beating the 40% tripwire by a mile. Age-matched read (no confound):
   the 2026-10-15 5–6.4h-old cohort read 83/106/107/171 (median ~106); today's
   5h cohort (B-16…B-25) reads 0/0/0/0/0/0/0/1/1/1/1/5/6/9 (median ~0.5). The
   1.4–2.5h cohort: yesterday B-964 @1.4h = 90 views; today's equivalents =
   0/1/0/0/0/1/8 (median ~0.5). Meanwhile the 2026-10-15 evening cohort
   (18:09–21:35 EDT, 10–16h old at check) reached 47–193. The wall fell
   somewhere between 23:25 EDT (B-10: 0 views) and the morning batch. Cause
   unproven, but the signature matches the documented burst-suppression family:
   the 9/hour ramp did NOT trip instantly — it held clean through the evening
   (~40 posts at pace) and then fell off a cliff overnight, which reads as
   TikTok's paced response to sustained high volume rather than an instant
   burst flag. Separately, a captcha loop at 09:49 EDT today fired the §5
   hair-trigger park on its own — two independent tripwires in one morning.
   Governor actions: 48–72h park (upload_park.txt: resume ≥ 2026-10-18 09:49 EDT,
   auto-lift 2026-10-19 09:49 EDT), kickstand nag floor 6 → 30 min, review stays
   DAILY until 7 clean days at the new pace.
2. **For-You traffic %: unobservable, not near-zero (distinction matters).**
   Studio withholds the traffic-source breakdown until a video reaches 100
   views; NONE of the 14 newest posts reached it (max: B-1029 at 8). The
   governor's "2+ consecutive posts near-zero FYP" clause therefore cannot be
   evaluated this run — the views clause fired alone. Keep pushing for FYP% in
   the next review; the moment a post crosses 100 views it becomes the
   canary for the whole park-recovery phase.
3. **Top post so far: B-980 "The Pigeon" — 193 views / 3 likes (~14h old, tag
   set D, pair-shape caption).** Runner-up B-501 (265 views / 1 like, ~30h old,
   set A). Engagement is still near-zero channel-wide: 17 likes + 1 comment
   across all 72 posts (0.24 likes/post). No tag set (A/B/C/D), caption shape
   (2-beat/pair/decl), or post-hour effect has replicated evidence either way —
   the null bank from 2026-10-15 stands, and the collapse drowns any signal
   for now. Revisit tag/caption reads only AFTER distribution recovers and
   videos mature ~7 days at equal ages.
4. **Loop data-quality notes (new):** Studio's per-video analytics via
   /tiktokstudio/analytics/{video_id}/overview CAN disagree with the list
   table (B-1029: list 4 vs per-video 8 — per-video wins, it updates in real
   time). Studio's Posts list has NO Shares column; the per-video Engagement
   tab shows "Your video data is being processed" with no numeric values for
   any checked video — shares are n/a everywhere, not zero. Clicking a row in
   the Posts table opens the PUBLIC video page, not Studio analytics; the
   working route is the direct analytics URL pattern above.

Policy changes proposed this run: the governor duty is mechanical, not a
proposal — the 9/hour cadence is SUSPENDED (park 48–72h, then 30-min floor =
2/hour, rebuild 1–2 weeks, review stays daily until 7 clean days, no
re-tightening without replicated evidence). Logged in the policy changelog and
in §5, dated 2026-10-16.

### 2026-10-17 ~09:55 EDT — third performance check = daily governor run #2 at the 30-min floor (18 posts, ages 4.9–14.7h)

Source: read-only pull via signed-in TikTok Studio (@waefrebeorn; 1.8K followers,
29K likes; Studio shows 235 posts total). Per-post numbers live in
`TIKTOK_METRICS.md`. These 18 posts all went up at ~30–40 min spacing
2026-10-16 19:14 EDT → 2026-10-17 05:04 EDT, after the user lifted the first
governor park ~19:06 EDT. Governor verdict: NO ACTION — median views/post 1 → 9
(rise, not a >40% drop), FYP% healthy on all observable posts. Clean-day
counter: 1 (at the 30-min floor; review stays daily until 7 clean days).

1. **Partial distribution recovery at the 30-min floor (replicated 3/3 ≥100-view
   posts).** B-36 (116 views, 98.3% FYP), B-1062 (109, 97.3%), B-1053 (100,
   98.0%) — posted 19:14–20:58 EDT at ~35-min spacing — sit in the healthy
   baseline band with For-You shares matching the pre-collapse 98.2–98.9%
   exactly. Readout: the suppression LIFTED when spacing returned to ~30–40
   min; the collapse signature was pace-attributed, not account-attributed.
   Caveat, honestly held: the age-matched healthy-era cohort (10–15h, posted
   2026-10-15 evening) had median ~93 views vs this cohort's ~47.5 at the same
   ages — recovery is real but partial, and the mid-tail (12–57 views) is
   thinner than the 10-15 baseline. Also 15/18 posts are <100 views, so the
   FYP canary sample is only n=3.
2. **Age confound confirmed again — views scale with age, nothing else yet.**
   The 4.9–9.4h posts read 1–6 views; the 10–14.7h posts read 3–116. Same as
   the 10-15 finding. Next review: compare at matched ages only.
3. **Engagement null, third run running.** 18 likes + 4 comments across 18
   posts (1.0 likes/post vs 0.24/post on 10-16; the bump is mechanical — fewer
   zero-view posts, same ~1% view-to-like ratio). Medians by tag set at matched
   rough ages: A ~18 (n=3), B ~45 (n=3), C ~12 (n=9), D ~3.5 (n=2) — but age
   skews the sets (C posts skew young), n is small, and the null bank stands:
   no tag set or caption shape has replicated evidence either way. B-1053's
   100 views / 0 likes vs B-1062's 109 / 2 is the whole channel's engagement
   variance — do not read it as a caption-shape signal (decl vs pair with n=1
   each). Revisit only after videos mature ~7 days at equal ages.
4. **Data-quality notes:** Studio's Content list still has no Shares column
   (n/a everywhere). The direct /tiktokstudio/analytics/{video_id}/overview
   route confirmed per-video traffic sources this time — FYP 97.3–98.3%,
   profile 1.0–1.8%, search 0–1.0%, everything else <0.1%. B-43's view count
   moved 3 → 4 mid-read: treat single-digit views as ±1 noise. No captcha, no
   login challenge during this read.

Policy changes proposed this run: none. The governor did not fire, so pacing
is untouched (the kickstand nag stays at the user-reinstated 6-minute floor
while the 07:37 EDT target_blocked park is active). No re-tightening without
replicated evidence — the 30-min floor's partial recovery is evidence for
that floor, not evidence to change it.

