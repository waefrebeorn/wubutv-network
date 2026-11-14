#!/usr/bin/env python3
"""Score the G7 validation fixture (loop 7).

Inputs: fixture.json + work/asr/<id>.json (from transcribe_set.py).
Outputs: validation_results.json (here and in the loop-07-g7 report dir)
plus a console summary.

Cross-pair strata (classified on the two scenes' PLANNED sets, in this
priority order):
  undefined_empty_planned - other scene is wordless; recall is undefined,
                            excluded from the bar and counted.
  quarantine_identical    - planned sets identical (the spec's provenance
                            quarantine for identical choruses).
  near_identical          - Jaccard(plannedA, plannedB) >= 0.5.
  subset                  - one planned set strictly contains the other
                            (chant granularity: 'post it' is a whole scene
                            and also half of three other scenes' lines).
  discriminating          - everything else; the bar's real test.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g7_check  # noqa: E402
from g7_check import overlap, word_sets  # noqa: E402

REPORT_DIR = os.path.expanduser(
    "~/workspace/research_notes/slopcannon-improvement-loop/loop-07-g7")


def dist(scores):
    if not scores:
        return {"n": 0}
    s = sorted(scores)
    n = len(s)

    def q(p):
        return s[min(n - 1, max(0, int(round(p * (n - 1)))))]
    return {"n": n, "min": round(s[0], 3), "p25": round(q(0.25), 3),
            "median": round(q(0.5), 3), "p75": round(q(0.75), 3),
            "max": round(s[-1], 3),
            "n_below_0.5": sum(1 for x in s if x < 0.5),
            "hist": {"0-0.25": sum(1 for x in s if x < 0.25),
                     "0.25-0.5": sum(1 for x in s if 0.25 <= x < 0.5),
                     "0.5-0.75": sum(1 for x in s if 0.5 <= x < 0.75),
                     "0.75-1.0": sum(1 for x in s if 0.75 <= x < 1.0),
                     "1.0": sum(1 for x in s if x >= 1.0)}}


def jaccard(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a | b else 1.0


def main():
    fixture = json.load(open(os.path.join(HERE, "fixture.json")))["items"]
    data = {}
    for it in fixture:
        segs = json.load(open(os.path.join(
            HERE, "work", "asr", it["id"] + ".json")))["segments"]
        screened, raw = word_sets(segs)
        data[it["id"]] = {**it, "segments": segs, "screened": screened,
                          "raw": raw,
                          "asr_text": " ".join(s["text"] for s in segs).strip()}

    mv14 = [d for d in data.values() if d["project"] == "MV-14"]

    # ---- own pairs -----------------------------------------------------------
    own = []
    for d in mv14:
        own.append({
            "scene": d["scene"], "take": d["take"], "id": d["id"],
            "wordless": not d["planned_primary"],
            "asr_text": d["asr_text"],
            "asr_screened": sorted(d["screened"]),
            "asr_raw": sorted(d["raw"]),
            "planned_primary": d["planned_primary"],
            "planned_grid": d["planned_grid"],
            "overlap_primary_screened": round(overlap(d["screened"], d["planned_primary"]), 4),
            "overlap_primary_raw": round(overlap(d["raw"], d["planned_primary"]), 4),
            "overlap_grid_screened": round(overlap(d["screened"], d["planned_grid"]), 4),
        })
    own_sung = [o for o in own if not o["wordless"]]
    own_wordless = [o for o in own if o["wordless"]]

    # ---- cross pairs ---------------------------------------------------------
    strata = {}
    breaches = []
    for a in mv14:
        pa = set(a["planned_primary"])
        for b in mv14:
            if a["scene"] == b["scene"]:
                continue
            pb = set(b["planned_primary"])
            if not pb:
                stratum = "undefined_empty_planned"
            elif pa == pb:
                stratum = "quarantine_identical"
            elif jaccard(pa, pb) >= 0.5:
                stratum = "near_identical"
            elif pb < pa or pa < pb:
                stratum = "subset"
            else:
                stratum = "discriminating"
            ov = overlap(a["screened"], pb)
            ov_raw = overlap(a["raw"], pb)
            strata.setdefault(stratum, []).append(ov)
            if stratum == "discriminating":
                strata.setdefault("discriminating_raw", []).append(ov_raw)
            if ov >= 0.5 and stratum != "undefined_empty_planned":
                breaches.append({"take": a["id"], "vs_scene": b["scene"],
                                 "stratum": stratum, "overlap": round(ov, 4),
                                 "take_asr": sorted(a["screened"]),
                                 "vs_planned": b["planned_primary"]})

    # ---- MV-2 real positives ---------------------------------------------------
    positives = []
    for pid in ("mv2_s04_t3", "mv2_s21_t1"):
        d = data[pid]
        row = {"id": pid, "asr_text": d["asr_text"],
               "asr_screened": sorted(d["screened"]),
               "asr_raw": sorted(d["raw"]),
               "planned_primary": d["planned_primary"],
               "overlap_screened": round(overlap(d["screened"], d["planned_primary"]), 4),
               "overlap_raw": round(overlap(d["raw"], d["planned_primary"]), 4)}
        if "alt_segment_words" in d:
            row["alt_segment_words"] = d["alt_segment_words"]
            row["overlap_vs_alt_segment_screened"] = round(
                overlap(d["screened"], d["alt_segment_words"]), 4)
        positives.append(row)

    results = {
        "own_pairs": own,
        "own_sung_dist_screened": dist([o["overlap_primary_screened"] for o in own_sung]),
        "own_sung_dist_raw": dist([o["overlap_primary_raw"] for o in own_sung]),
        "own_sung_dist_gridvariant": dist([o["overlap_grid_screened"] for o in own_sung]),
        "own_wordless": own_wordless,
        "own_wordless_false_rejects_screened": sum(
            1 for o in own_wordless if o["overlap_primary_screened"] < 0.5),
        "own_wordless_false_rejects_raw": sum(
            1 for o in own_wordless if o["overlap_primary_raw"] < 0.5),
        "cross_strata": {k: dist(v) for k, v in sorted(strata.items())},
        "cross_breaches_ge_0.5": breaches,
        "mv2_positives": positives,
    }
    for path in (os.path.join(HERE, "validation_results.json"),
                 os.path.join(REPORT_DIR, "validation_results.json")):
        json.dump(results, open(path, "w"), indent=1)

    print("OWN-PAIRS, sung scenes (n=%d), screened:" % len(own_sung),
          results["own_sung_dist_screened"])
    print("OWN-PAIRS, sung scenes, raw:", results["own_sung_dist_raw"])
    print("OWN-PAIRS, sung scenes, grid-planned variant:",
          results["own_sung_dist_gridvariant"])
    print("OWN-PAIRS, wordless scenes (n=%d): false REJECTs screened=%d raw=%d"
          % (len(own_wordless),
             results["own_wordless_false_rejects_screened"],
             results["own_wordless_false_rejects_raw"]))
    print("CROSS-PAIR STRATA:")
    for k, v in results["cross_strata"].items():
        print(" ", k, v)
    print("CROSS BREACHES (>=0.5, non-undefined):", len(breaches))
    for b in breaches:
        print("  ", b)
    print("MV-2 POSITIVES:")
    for p in positives:
        print(" ", p["id"], "overlap_screened=", p["overlap_screened"],
              "raw=", p["overlap_raw"],
              ("vs-alt-segment=" + str(p["overlap_vs_alt_segment_screened"]))
              if "overlap_vs_alt_segment_screened" in p else "",
              "asr=", p["asr_text"])


if __name__ == "__main__":
    main()
