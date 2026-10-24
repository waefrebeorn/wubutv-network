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
