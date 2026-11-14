#!/usr/bin/env python3
"""Stamp a WuBuTV manifest with the PROVENANCE SPEC v1 blocks.

Reference behaviour for the Producer's build_manifest.py. Reads a manifest, adds
a `provenance` block per finished piece and a manifest-level `provenance_policy`,
and writes a NEW file. It never mutates its input.

The honest rule (notes/PROVENANCE_SPEC.md): a generator we cannot identify is
recorded as "unknown" with needs_backfill=true. A guessed provenance record is a
false statement about a regulated fact, so this tool refuses to guess.

Usage:
  python3 tools/provenance_stamp.py IN.json OUT.json [--date-field generated_at]
Output: the census it printed, plus the stamped manifest.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone

POLICY = {
    "version": 1,
    "effective": "2026-10-21",
    "disclosure_statement": (
        "Every piece in this dataset is AI-generated video with native generated "
        "audio. No piece is a re-voiced or dubbed performance."
    ),
}
BASIS = "eu_ai_act_art50+ca_sb942"


def blank_provenance() -> dict:
    return {
        "ai_generated": True,
        "generator": {"vendor": "unknown", "model": "unknown", "version": "unknown"},
        "prompt_ref": None,
        "generated_at": None,
        "disclosure": {"visible": True, "latent": False},
        "basis": BASIS,
        "needs_backfill": True,
    }


def stamp_piece(piece: dict) -> dict:
    """Attach provenance to one piece without inventing facts."""
    out = dict(piece)
    prov = blank_provenance()
    # Only what the piece itself attests can be trusted. A manifest that already
    # names a generator keeps it; nothing else is inferred.
    for key in ("generator", "prompt_ref", "generated_at"):
        if isinstance(out.get(key), (dict, str)) and out.get(key):
            prov[key] = out[key]
    if prov["generator"].get("model") == "unknown":
        prov["needs_backfill"] = True
    else:
        prov["needs_backfill"] = False
    prov["prompt_ref"] = prov["prompt_ref"] or _prompt_ref(out)
    out["provenance"] = prov
    return out


def _prompt_ref(piece: dict) -> str | None:
    """Hash whatever prompt text the record carries, else nothing."""
    txt = piece.get("prompt") or piece.get("premise") or ""
    if not isinstance(txt, str) or not txt.strip():
        return None
    return hashlib.sha256(txt.encode("utf-8")).hexdigest()


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        raise SystemExit(2)
    src, dst = sys.argv[1], sys.argv[2]
    man = json.load(open(src))

    counts = {"stamped": 0, "needs_backfill": 0, "sections": {}}
    for section, items in list(man.items()):
        if not isinstance(items, list) or not items:
            continue
        if not isinstance(items[0], dict):
            continue
        if "file" not in items[0]:
            continue  # docs / non-media sections
        man[section] = [stamp_piece(p) for p in items]
        counts["sections"][section] = len(man[section])
        counts["stamped"] += len(man[section])
        counts["needs_backfill"] += sum(
            1 for p in man[section] if p["provenance"]["needs_backfill"]
        )

    counts["prompt_ref_attached"] = sum(
        1 for s in counts["sections"]
        for p in man[s] if p["provenance"]["prompt_ref"]
    )
    policy = dict(POLICY)
    policy["backfill_state"] = {
        "stamped": counts["stamped"],
        "needs_backfill": counts["needs_backfill"],
        "prompt_ref_attached": counts["prompt_ref_attached"],
        "stamped_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    man["provenance_policy"] = policy
    json.dump(man, open(dst, "w"), indent=1)
    print(json.dumps({"out": dst, **counts}, indent=1))


if __name__ == "__main__":
    main()
