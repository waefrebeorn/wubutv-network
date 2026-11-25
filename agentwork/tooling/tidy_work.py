#!/usr/bin/env python3
"""Tidy /opt/data/work: QC images into qc/, keep masters and code at the root, write the index."""
import os
import shutil
import sys
from datetime import datetime, timezone

ROOT = "/opt/data/work"
DRY = "--dry" in sys.argv
QC_PREFIX = ("chk_", "still_", "sheet", "qc_", "card_check", "check", "endcard_check", "src_sheet",
             "algo_sheet", "fifth_sheet", "mid_")


def plan():
    moves = []
    for proj in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, proj)
        if not os.path.isdir(p):
            continue
        for f in os.listdir(p):
            if os.path.isfile(os.path.join(p, f)) and f.lower().endswith((".png", ".jpg")) and f.startswith(QC_PREFIX):
                moves.append((os.path.join(p, f), os.path.join(p, "qc", f)))
    return moves


MASTERS = {
    "lamp2": ("THE LAMP — 48.5 s film, 854x480", ["THE_LAMP_master.mp4", "THE_LAMP_send.mp4"]),
    "ident": ("WuBuTV station ident — 24.5 s, 1280x720", ["ident_master.mp4", "ident_vertical.mp4"]),
    "promo": ("WUBUTV PRESENTS — 55.7 s, seven channels", ["wubutv_presents.mp4"]),
    "mystery": ("THE ONE PIECE (24 s) + THE FIFTH MARK (16 s)", ["THE_ONE_PIECE.mp4", "THE_FIFTH_MARK.mp4"]),
    "wubu-agi": ("The WuBu companion core (C11) + voice layer + promo", ["WUBU_ONLINE.mp4"]),
    "slerm-social": ("50-venue agent-social index, playbook, loop", ["INDEX.md", "PLAYBOOK.md", "LEARNINGS.md"]),
    "prize": ("Prize-hunt source pulls (vault, ledger, station pieces)", []),
    "reel": ("WUBU_REEL — the earlier portfolio cut", ["WUBU_REEL.mp4"]),
    "media": ("Perky remix sources", ["perky_720.mp4"]),
    "film": ("keeper / epic — earlier films (frames kept: long renders)", []),
    "wubu3d": ("wuBu3D engine + render outputs (frame passes purged)", []),
    "jobsearch": ("resume / positioning docs", []),
}


def main():
    moves = plan()
    if DRY:
        print(f"{len(moves)} QC images would move into qc/")
        return
    for src, dst in moves:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
    print(f"moved {len(moves)} QC images into qc/")

    lines = ["# /opt/data/work — the map", "",
             f"Tidied {datetime.now(timezone.utc).strftime('%Y-%m-%d')}. Masters stay at each project root;",
             "QC sheets live in `qc/`; render passes are purged (specs + code regenerate them).",
             "Disk budget 24 GB on a 25 GB volume; `scripts/clean_renders.py` frees frame passes, ",
             "`scripts/clean_renders.py --dry` shows what it would take.", "",
             "| project | what | masters |", "|---|---|---|"]
    for proj, (what, files) in MASTERS.items():
        present = [f for f in files if os.path.exists(os.path.join(ROOT, proj, f))]
        lines.append(f"| `{proj}/` | {what} | " + (", ".join(present) if present else "—") + " |")
    extra = sorted(p for p in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, p)) and p not in MASTERS)
    if extra:
        lines += ["", "Unlisted dirs: " + ", ".join(extra)]
    open(os.path.join(ROOT, "WORK_INDEX.md"), "w").write("\n".join(lines) + "\n")
    print("wrote WORK_INDEX.md")


if __name__ == "__main__":
    main()
