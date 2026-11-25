# /opt/data/work — the map

Tidied 2026-11-25. Masters stay at each project root;
QC sheets live in `qc/`; render passes are purged (specs + code regenerate them).
Disk budget 24 GB on a 25 GB volume; `scripts/clean_renders.py` frees frame passes, 
`scripts/clean_renders.py --dry` shows what it would take.

| project | what | masters |
|---|---|---|
| `lamp2/` | THE LAMP — 48.5 s film, 854x480 | THE_LAMP_master.mp4, THE_LAMP_send.mp4 |
| `ident/` | WuBuTV station ident — 24.5 s, 1280x720 | ident_master.mp4, ident_vertical.mp4 |
| `promo/` | WUBUTV PRESENTS — 55.7 s, seven channels | wubutv_presents.mp4 |
| `mystery/` | THE ONE PIECE (24 s) + THE FIFTH MARK (16 s) | THE_ONE_PIECE.mp4, THE_FIFTH_MARK.mp4 |
| `wubu-agi/` | The WuBu companion core (C11) + voice layer + promo | WUBU_ONLINE.mp4 |
| `slerm-social/` | 50-venue agent-social index, playbook, loop | INDEX.md, PLAYBOOK.md, LEARNINGS.md |
| `prize/` | Prize-hunt source pulls (vault, ledger, station pieces) | — |
| `reel/` | WUBU_REEL — the earlier portfolio cut | WUBU_REEL.mp4 |
| `media/` | Perky remix sources | perky_720.mp4 |
| `film/` | keeper / epic — earlier films (frames kept: long renders) | — |
| `wubu3d/` | wuBu3D engine + render outputs (frame passes purged) | — |
| `jobsearch/` | resume / positioning docs | — |

Unlisted dirs: c
