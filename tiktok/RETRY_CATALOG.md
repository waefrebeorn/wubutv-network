# TikTok Retry Catalog

The no-skip backlog. Every bumper that fails an upload attempt lands here with its failure history and gets retried every run until it posts. Nothing is ever skipped, nothing is ever dropped — the catalog is the librarian's hammer list.

Format: `| Bumper | Title | Failures | Last attempt (EDT) | Last reason | Status |`

Rules:
- A bumper enters on its first failed attempt (failures=1).
- Each failed retry increments Failures and updates Last attempt + Last reason.
- On a successful post, the row is DELETED (the ledger row is the proof of posting).
- Pick order each run: the oldest row whose Last attempt is >30 minutes old beats the fresh interleave pick. If no retry item is due, run the fresh pick.
- A row is never removed except by posting. No expiry, no giving up.

| Bumper | Title | Failures | Last attempt (EDT) | Last reason | Status |
| B-1112 | The Wall Clock | 7 | 2026-10-18 ~02:29 | target_blocked (tooling-side file grant refused, 7th attempt — in replacement window browser-task:e124174f, both "Select videos" and drag-and-drop targets; session signed in, no stuck B-1112 draft, no post created, no double-post risk) | retry-due |
| B-1205 | The New Datum | 3 | 2026-10-18 ~02:26 | target_blocked (tooling-side file grant refused, 3rd attempt — in replacement window 39695e52, incl. classic /upload route; no post created, no double-post risk; session healthy, signed in, B-1204 verified live) | retry-due |
| B-44 | Please Stand By | 1 | 2026-10-18 ~02:42 | Akamai edge "Access Denied" block on TikTok Studio upload page (hard-blocked across reloads/tabs; soft client-side block on 'Select videos' first, then the wall; 2 bot-challenge specialists failed to clear; network-route recovery refused by runtime — 'another window waiting for the user'); sign-in intact, other Studio surfaces load; nothing posted, file never uploaded, no double-post risk | retry-due |
| B-45 | The Card Trick | 1 | 2026-10-18 ~02:47 | Akamai edge "Access Denied" hard block on ALL of www.tiktok.com for this browser/route (Studio upload page + tiktok.com homepage, Reference IDs 18.52ed2c17…, no interactive puzzle/widget/retry control — no challenge to solve; 2 bot-challenge specialists failed; environment replacement refused by runtime — 'another window on this browser is waiting for the user'); fresh replacement window browser-task:608f5f9e held open as session, will retry when block clears; nothing posted, file never uploaded, no double-post risk | retry-due |
