#!/usr/bin/env python3
"""registry_backwrite.py — idempotent back-write of lifecycle dates into
~/workspace/wubutv-network/assembly/CLIP_REGISTRY.md.

Columns: Unit | File | Fresh | E1M-used | E2M-used | IG-posted | TT-posted | CDN-backed | Recycled
Only fills a '-' cell; never overwrites an existing date (idempotent).
Silent on unknown units / non-bumper files (commercials, assemblies have no rows).

Usage:
  registry_backwrite.py --column IG-posted --unit B-1267 [--date 2026-10-19]
  registry_backwrite.py --column CDN-backed --ok-list <media_list> --failed-list <failed_list> [--date 2026-10-19]
"""
import argparse, os, re, sys

REGISTRY = os.path.expanduser("~/workspace/wubutv-network/assembly/CLIP_REGISTRY.md")
# Column indexes in the '|' split: ['', 'Unit', 'File', 'Fresh', 'E1M-used',
# 'E2M-used', 'IG-posted', 'TT-posted', 'CDN-backed', 'Recycled', '']
COLIDX = {"IG-posted": 6, "TT-posted": 7, "CDN-backed": 8}
EXPECTED_HEADER = ["Unit", "File", "Fresh", "E1M-used", "E2M-used",
                   "IG-posted", "TT-posted", "CDN-backed", "Recycled"]


def unit_from_path(path):
    base = os.path.basename(path.strip())
    m = re.match(r"b(\d+)_", base, re.IGNORECASE)
    return f"B-{m.group(1)}" if m else None


def load_rows():
    with open(REGISTRY) as f:
        lines = f.readlines()
    header = None
    for ln in lines:
        if re.match(r"^\|\s*Unit\s*\|", ln):
            header = [c.strip() for c in ln.rstrip("\n").split("|")[1:-1]]
            break
    if header != EXPECTED_HEADER:
        raise SystemExit(f"registry header mismatch: {header}")
    row_idx = {}
    for i, ln in enumerate(lines):
        if ln.startswith("| B-") or ln.startswith("|B-"):
            unit = ln.split("|")[1].strip()
            row_idx[unit] = i
    return lines, row_idx


def set_cell(unit, col, date, lines, row_idx):
    i = row_idx.get(unit)
    if i is None:
        return False
    cells = lines[i].rstrip("\n").split("|")
    if len(cells) <= COLIDX[col]:
        return False
    if cells[COLIDX[col]].strip() == "-":
        cells[COLIDX[col]] = f" {date} "
        lines[i] = "|".join(cells) + "\n"
        return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--column", required=True, choices=list(COLIDX))
    ap.add_argument("--unit")
    ap.add_argument("--ok-list")
    ap.add_argument("--failed-list")
    ap.add_argument("--date", default=None)
    a = ap.parse_args()
    import datetime
    date = a.date or datetime.date.today().isoformat()

    lines, row_idx = load_rows()
    changed = 0

    if a.ok_list:
        failed = set()
        if a.failed_list and os.path.exists(a.failed_list):
            with open(a.failed_list) as f:
                failed = {ln.strip() for ln in f if ln.strip()}
        with open(a.ok_list) as f:
            paths = [ln.strip() for ln in f if ln.strip()]
        for p in paths:
            if p in failed:
                continue
            unit = unit_from_path(p)
            if unit and set_cell(unit, a.column, date, lines, row_idx):
                changed += 1
    elif a.unit:
        if set_cell(a.unit, a.column, date, lines, row_idx):
            changed = 1
    else:
        ap.error("need --unit or --ok-list")
        return 2

    if changed:
        with open(REGISTRY, "w") as f:
            f.writelines(lines)
    print(f"backwrite: {a.column} <- {date}: {changed} rows filled")
    return 0


if __name__ == "__main__":
    sys.exit(main())
