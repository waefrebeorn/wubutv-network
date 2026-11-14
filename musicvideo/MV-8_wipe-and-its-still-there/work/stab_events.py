#!/usr/bin/env python3
"""Refine raw onsets into stab/hit events: cluster onsets <=0.15s apart (a stab's
multi-transient attack = one event), then require neighborhood prominence —
a stab must stand out from the groove around it (+-2s median strength)."""
import json
import numpy as np

raw = json.load(open("work/crescendo_raw.json"))
onsets = raw["onsets"]

# cluster
events = []
cur = [onsets[0]]
for o in onsets[1:]:
    if o["t"] - cur[-1]["t"] <= 0.15:
        cur.append(o)
    else:
        events.append(cur); cur = [o]
events.append(cur)
ev = []
for c in events:
    m = max(c, key=lambda o: o["strength"])
    ev.append({"t": m["t"], "strength": m["strength"], "peak_dbfs": max(o["peak_dbfs"] for o in c),
               "n_sub": len(c)})

# neighborhood prominence
strengths = np.array([e["strength"] for e in ev])
times = np.array([e["t"] for e in ev])
for i, e in enumerate(ev):
    mask = (np.abs(times - e["t"]) <= 2.0) & (np.arange(len(ev)) != i)
    med = float(np.median(strengths[mask])) if mask.sum() >= 3 else float(np.median(strengths))
    e["prominence"] = round(e["strength"] / max(med, 0.05), 2)
    if e["strength"] >= 0.85 and e["peak_dbfs"] >= -6.0 and e["prominence"] >= 1.6:
        e["class"] = "orchestral_hit"
    elif e["strength"] >= 0.55 and e["prominence"] >= 1.5:
        e["class"] = "brass_stab"
    elif e["strength"] >= 0.40 and e["prominence"] >= 1.8:
        e["class"] = "accent"
    else:
        e["class"] = "groove"
    e["med_nbhd"] = round(med, 3)

hits = [e for e in ev if e["class"] in ("orchestral_hit", "brass_stab", "accent")]
json.dump({"n_events": len(ev), "n_hits": len(hits), "hits": hits, "all_events": ev},
          open("work/crescendo_events.json", "w"), indent=1)
from collections import Counter
print("events:", len(ev), "hits:", len(hits), Counter(e["class"] for e in hits))
for e in hits:
    print(f'{e["t"]:8.3f}  {e["class"]:15s} str {e["strength"]:.2f} prom {e["prominence"]:.2f} peak {e["peak_dbfs"]:.1f} sub {e["n_sub"]}')
