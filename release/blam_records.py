#!/usr/bin/env python3
"""BLAM gate records: resolve an item's recorded FIRST-3 BLAM verdict
("pass" / "fail" / None) from evidence already on disk. Nothing here is
computed or inferred — every value traces to a gate record a production
run actually wrote:

  1. work/qc/blam_master.json (or work/blam_master.json) in the item's
     project dir — the machine-readable master gate run: every recorded
     sub-check true -> "pass"; any false -> "fail".
  2. GATE_LOG.md in the item's project dir — lines naming BLAM: any such
     line recording a FAIL -> "fail" (a failed sub-check that shipped
     under fail-once-then-ship is still a recorded fail); else any line
     recording PASS -> "pass".
  3. research/FIRST3_BLAM_AUDIT_2026-11-15.md §3/§5 verdict tables
     (AUDIT_VERDICTS below, copied verbatim from that document).

Items with no gate record resolve to None — an honest null, never a
guess. This module exists because metrics.jsonl's features.blam_class
was null in 74/74 rows: the harvest body copies features from the
item's inventory.json entry, and inventory never carried the field.
scan_inventory.py now stamps it from here."""
import glob, json, os, re

NET = os.path.expanduser("~/workspace/wubutv-network")

# FIRST3_BLAM_AUDIT_2026-11-15.md: §3 pilot table (BLAM? column) and
# §5 appendix table (BLAM? column), copied verbatim 2026-11-22.
AUDIT_VERDICTS = {
    "PILOT-1-THE-MACHINE": "fail",       # §3: NO
    "PILOT-2-THE-TENTH-SECOND": "pass",  # §3: YES
    "PILOT-3-THE-ROSTER": "fail",        # §3: NO
    "PILOT-4-THE-COUNT": "fail",         # §3: NO
    "PILOT-5-THE-LAST-SEAT": "fail",     # §3: NO (audio — A4 crackle)
    "MV-18": "fail",                     # §5: NO — E2 fail
    "MV-19": "fail",                     # §5: NO — A4 crackle head
    "MV-20": "pass",                     # §5: YES (E2 advisory only)
    "MV-21": "fail",                     # §5: NO — worst opening in the set
}

def _project_dir(item):
    """The item's project dir: the parent of its masters/ dir, when the
    catalogue path has that shape. None otherwise."""
    path = item.get("path") or item.get("house_path")
    if not path:
        return None
    parts = path.split(os.sep)
    if "masters" in parts:
        return os.sep.join(parts[:parts.index("masters")])
    return None

def _from_blam_json(item):
    proj = _project_dir(item)
    if not proj:
        return None
    for cand in (os.path.join(proj, "work", "qc", "blam_master.json"),
                 os.path.join(proj, "work", "blam_master.json")):
        if os.path.exists(cand):
            try:
                with open(cand) as f:
                    gate = (json.load(f) or {}).get("gate") or {}
            except (ValueError, OSError):
                return None
            if gate:
                return "pass" if all(gate.values()) else "fail"
    return None

def _from_gate_log(item):
    proj = _project_dir(item)
    if not proj:
        return None
    log = os.path.join(proj, "GATE_LOG.md")
    if not os.path.exists(log):
        return None
    try:
        with open(log, errors="replace") as f:
            lines = [ln for ln in f if "BLAM" in ln.upper()]
    except OSError:
        return None
    if any("FAIL" in ln.upper() for ln in lines):
        return "fail"
    if any("PASS" in ln.upper() for ln in lines):
        return "pass"
    return None

def blam_class_for(item):
    """item: an inventory/catalogue dict (uses id + path)."""
    for source in (_from_blam_json, _from_gate_log):
        v = source(item)
        if v:
            return v
    return AUDIT_VERDICTS.get(item.get("id"))

if __name__ == "__main__":
    # Self-check against the catalogue: print every resolved record.
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from catalogue import catalogue
    hits = {}
    for it in catalogue():
        v = blam_class_for(it)
        if v:
            hits[it["id"]] = v
    print(json.dumps(hits, indent=1))
    print(f"{len(hits)} items with a recorded BLAM verdict")
