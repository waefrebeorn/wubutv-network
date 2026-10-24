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

### 2026-10-23 ~19:55 EDT — fourth performance check = daily governor run #3, first post-resume (2 posts, ages ~130h)

Source: read-only pull via signed-in TikTok Studio (@waefrebeorn; 1.8K followers,
29K likes; Studio shows 239 posts total). Per-post numbers live in
`TIKTOK_METRICS.md`. First check after the 5-day user-ordered stop
(2026-10-18 ~02:47 → 2026-10-23 ~19:42 EDT); both measured posts are the
pre-stop tail — the first near-7-day maturity read. Governor verdict:
NO ACTION — median views 9 → 254 (rise, not a >40% drop), FYP healthy on 2/2.
Clean-day counter: 1 (unchanged — it resumes building on new-regime posts).
Review stays DAILY; no pacing change.

1. **Distribution fully healthy on mature posts (replicated 2/2).** B-1227:
   333 views / 7 likes, 99.4% FYP — the highest For-You share of any
   agent-posted video to date, above the pre-collapse 98.2–98.9% band.
   B-1204: 175 / 3, 98.3% FYP. Both at ~130h old sit above the healthy-era
   24–31h cohort's 47–265-view band at much older ages: the collapse-era
   suppression is not lingering, and the 5-day stop produced no decay signal.
2. **Engagement-rate bests, with an age caveat honestly held.** B-1227's 7
   likes is the most any agent-posted video has received (prior best: B-980's
   3); view-to-like 2.1% and 1.7% vs the historical ~1%. Caveat: these are
   the oldest measured posts (130h), so part of the bump is accumulation
   time, not necessarily caption/tag superiority. No tag set (A vs B, n=1
   each) or caption shape (pair vs 2-beat, n=1 each) replicates — the null
   bank stands. And do not read this as a bumper formula: the bumper era is
   ending; the relaunch queue is 1-min/2-min soap episodes, a different
   format whose performance baseline starts at zero.
3. **Shares are now measurable (n=2, both 0).** First check where the
   Engagement route returned real share counts instead of "being processed"
   — 0 shares on both at ~130h. That zero is the honest starting baseline
   for the soap era.
4. **Data-quality notes:** per-video analytics header icons now carry
   likes/comments/shares totals even when the Engagement tab shows no
   totals — use them before falling back to public pages. Studio's post
   count grew 235 → 239 (+4) since the 2026-10-17 check with only 2 new
   ledger rows — two Studio posts have no ledger row; open question for
   tiktok-dedup-recon. B-1204's single search-driven view came from the
   query "b.1204" — noise, not signal. No captcha, login wall, or
   rate-limit during this read.

Policy changes proposed this run: none mechanical (the governor did not fire;
the review stays daily, no pacing change). One standing calibration note for
the soap era, logged as a changelog line rather than a section change: all
bumper-era pacing and distribution findings (the 30-min floor evidence, this
run's healthy mature read) attach to 10-second bumpers. The 1-min/2-min soap
episodes have no performance baseline yet — the first new-regime review should
treat them as a fresh calibration cohort and must not inherit bumper numbers.


### 2026-10-24 ~09:50 EDT — fifth performance check = daily governor run #4, first new-regime review (21 posts, ages 0.5–14.1h)

Source: read-only pull via signed-in TikTok Studio (@waefrebeorn; Studio shows 261 posts total, 0 drafts). Per-post numbers live in `TIKTOK_METRICS.md`. Governor verdict: NO ACTION on the age-matched read — clean-day counter 1 → 2 (first clean day on new-regime posts). Review stays DAILY; no pacing change, no park.

1. **The raw median "collapse" is an age/format confound, not a distribution event — and the matched-age read is healthy.** Raw median 51 vs the previous run's 254 (−79.9%) looks like a governor trip, but the previous median was 2 bumper posts at ~130h old and this cohort is 21 posts at 0.5–14.1h old in the new 1-minute episode format. The loop's standing rule (compare at matched ages only) is what keeps this from being a false firing: the 10–14.1h subset (n=18) has median 53, inside the healthy-era 10–15h band (47–193) and above the 2026-10-17 partial-recovery median (~47.5). The 2026-10-16 collapse, by contrast, was confirmed at matched ages (5h cohort 106 → ~0.5) — this run has no such matched-age collapse anywhere. Lesson banked explicitly so a future run does not fire the park on a raw cross-age number: the governor compares medians, but a median across different ages/formats is not a comparison.
2. **For-You health holds at the top of the record — on a sample of one.** B-1205 (bumper tail, 14.1h, 180 views) reads 99.5% For You, the highest share of any agent-posted video to date (above B-1227's 99.4%). Every other post is <100 views so its FYP share is withheld by Studio — withheld, not near-zero, per the 2026-10-16 precedent. The FYP clause therefore cannot fire, and the one observable post points the healthy way. The FYP canary sample for the episode format itself is still n=0 (no episode has reached 100 views yet) — the next run's first 100-view episode is the real episode-format canary.
3. **Episodes open in the healthy band, with two watch items, not a pattern.** Episode median 51 (n=17); the 10h+ episodes run 25–72 views, squarely in the bumper healthy band for those ages — the format change itself shows no distribution penalty at these ages. Watch items: E1M-015 at 0 views / 7.3h (overnight 02:30 post — single-post zero, re-check at maturity) and E1M-008 at 13 / 11.5h (low outlier vs siblings). E1M-016/017 zeros at 1.2h/0.5h are young enough to be Studio lag. None of these is a consecutive-post pattern, so none touches the governor.
4. **Engagement null, fourth run running — and the format gives no new lever yet.** 14 likes / 0 comments / 0 shares across 21 posts (0.67 likes/post). All 17 episode captions share one shape ("WuBuTV 1-minute episode." declarative), so no caption-shape comparison exists for the new format; tag-set medians (A 54, B 33, C 53, D 32) are age-skewed with n=4–5. The null bank stands: no tag set or caption shape has replicated evidence either way. Shares at 0 across all 21 extends the honest 0-share baseline.
5. **Data-quality notes:** Studio's list search does not filter on typed text (B-1205/B-1112 confirmed via direct per-video analytics URLs instead). List-table and per-video figures agreed on every double-checked video; no counts moved mid-read. Studio count +22 vs 21 newly measured rows leaves ~1 additional unledgered Studio post this interval, plausibly E1M-018 if it landed before the 09:47 read — the standing unledgered-post question for dedup-recon persists. No captcha, login wall, or rate-limit during this read.

Policy changes proposed this run: none. The governor did not fire on the matched-age read, so pacing is untouched (the kickstand nag stays at the user-ordered 6-minute floor under the episodes-only decree). No re-tightening or loosening without replicated evidence — the first episode-format FYP canary (first episode ≥100 views) is the next decision-grade datum, not this run's withheld shares.
