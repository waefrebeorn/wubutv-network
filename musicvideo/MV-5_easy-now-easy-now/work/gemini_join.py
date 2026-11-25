"""Stage B join: every SONG_WORDS line vs the Gemini segments that overlap it.

Mapping (Stage A): spk_0 -> CAT, spk_1 -> GIRL, spk_2 -> GIRL (diarization
split of the same voice — see work/gemini_speakers.md). Gemini segments have
integer-second boundaries; zero-length segments (e.g. 122-122) are treated
as 1s windows [start, start+1).

Agreement classes (time overlap only — words are adjudicated by hand in
gemini_diff.md, because Gemini's text differs from v1 in places):
  agree    — every overlapping Gemini segment maps to the v1 owner
             (SPLIT lines always agree: both voices are expected inside)
  conflict — at least one overlapping segment maps to a different owner
  dropped  — no Gemini segment overlaps the line window at all
  coarse   — (modifier) the overlapping segment is >3x the line duration,
             so its single label cannot adjudicate this line alone
Output: work/gemini_line_join.json
"""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(BASE, "work")
MAP = {"spk_0": "CAT", "spk_1": "GIRL", "spk_2": "GIRL"}

sw = json.load(open(os.path.join(BASE, "SONG_WORDS.json")))
gem = json.load(open(os.path.join(WORK, "gemini_song.json")))
f0 = {x["id"]: x for x in json.load(open(os.path.join(WORK, "gemini_line_f0.json")))}

segs = []
for s in gem["segments"]:
    e = s["end"] if s["end"] > s["start"] else s["start"] + 1.0
    segs.append({**s, "end_eff": e})

out = []
for ln in sw["lines"]:
    ls, le = ln["start"], ln["end"]
    ov = []
    for s in segs:
        a, b = max(ls, s["start"]), min(le, s["end_eff"])
        if b > a:
            ov.append({"speaker": s["speaker"], "owner": MAP[s["speaker"]],
                       "seg_start": s["start"], "seg_end": s["end"],
                       "overlap_s": round(b - a, 2),
                       "text": s["text"][:60]})
    f = f0.get(ln["id"], {})
    if not ov:
        verdict = "dropped"
    elif ln["owner"] == "SPLIT":
        verdict = "agree"
    elif all(o["owner"] == ln["owner"] for o in ov):
        verdict = "agree"
    else:
        verdict = "conflict"
    coarse = any((o["seg_end"] - o["seg_start"] if o["seg_end"] > o["seg_start"] else 1.0)
                 > 3 * (le - ls) for o in ov)
    out.append({"id": ln["id"], "section": ln["section"], "text": ln["text"],
                "start": ls, "end": le, "v1_owner": ln["owner"],
                "v1_confidence": ln.get("confidence"),
                "pyin_median": f.get("pyin_median"),
                "pyin_cat_frac": (f.get("pyin_bands") or {}).get("cat_97_160"),
                "pyin_girl_frac": (f.get("pyin_bands") or {}).get("girl_200_330"),
                "pyin_bass_frac": (f.get("pyin_bands") or {}).get("bass_lt80"),
                "aubio_median": f.get("aubio_median"),
                "gemini_overlap": ov, "coarse": coarse,
                "agreement": verdict})

json.dump(out, open(os.path.join(WORK, "gemini_line_join.json"), "w"), indent=1)

from collections import Counter
print("lines:", len(out))
print(Counter(x["agreement"] for x in out))
print("coarse flags:", sum(1 for x in out if x["coarse"]))
print("\nCONFLICT lines:")
for x in out:
    if x["agreement"] == "conflict":
        labs = [(o["speaker"], o["overlap_s"]) for o in x["gemini_overlap"]]
        print(f"  {x['id']} v1={x['v1_owner']} pyin_med={x['pyin_median']} "
              f"cat={x['pyin_cat_frac']} girl={x['pyin_girl_frac']} aubio={x['aubio_median']} overlap={labs}")
print("\nDROPPED lines:")
for x in out:
    if x["agreement"] == "dropped":
        print(f"  {x['id']} {x['start']}-{x['end']} v1={x['v1_owner']} :: {x['text']}")
print("\nAGREE lines where Gemini segment is coarse (label cannot adjudicate alone):")
for x in out:
    if x["agreement"] == "agree" and x["coarse"]:
        print(f"  {x['id']} v1={x['v1_owner']} :: {x['text'][:40]}")
