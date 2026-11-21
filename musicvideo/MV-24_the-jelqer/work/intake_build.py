#!/usr/bin/env python3
"""Intake build v2 (clustering): ocr_raw.json -> work/rows_draft.json +
lyrics_draft.txt. Sightings of the same display row across frames are
clustered (time-contiguous, fuzzy), variants voted, scroll garble dropped.
Mid-word wraps rejoined (ASR-confirmed); cross-occurrence merges applied.
Usage: intake_build.py PROJ
"""
import difflib, json, os, re, sys
from collections import Counter

PROJ = sys.argv[1]
WORK = os.path.join(PROJ, "work")

def norm(s):
    s = s.lower().replace("’", "'").replace("‘", "'")
    s = re.sub(r"[^a-z0-9'\[\]\(\) ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def ratio(a, b):
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()

def fuzzy_eq(a, b):
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return False
    if na == nb or na in nb or nb in na:
        return True
    return ratio(na, nb) >= 0.82

with open(os.path.join(WORK, "ocr_raw.json")) as f:
    frames = json.load(f)
with open(os.path.join(PROJ, "SONG_WORDS.json")) as f:
    asr = json.load(f)
asr_vocab = set()
for w in asr:
    t = norm(w["word"]).replace(" ", "")
    if t:
        asr_vocab.add(t)

# ---------- cluster sightings ----------
clusters = []  # {variants, sightings, first_t, last_t, width, last_j}
for fr in frames:
    rows = [r for r in fr["rows"] if r["text"].strip()
            and "made with suno" not in r["text"].lower()]
    for j, r in enumerate(rows):
        best, bestscore = None, 0.0
        for c in clusters:
            if fr["t"] - c["last_t"] > 3:
                continue
            if abs(j - c["last_j"]) > 1:
                continue
            rep = c["variants"].most_common(1)[0][0]
            if fuzzy_eq(rep, r["text"]):
                sc = ratio(norm(rep), norm(r["text"]))
                if sc > bestscore:
                    best, bestscore = c, sc
        if best is not None:
            best["variants"][r["text"]] += 1
            best["sightings"] += 1
            best["last_t"] = fr["t"]
            best["last_j"] = j
            best["width"] = max(best["width"], r["width"])
        else:
            clusters.append({"variants": Counter({r["text"]: 1}),
                             "sightings": 1, "first_t": fr["t"],
                             "last_t": fr["t"], "width": r["width"],
                             "last_j": j})

for c in clusters:
    c["text"] = sorted(c["variants"].items(),
                       key=lambda kv: (kv[1], len(kv[0])), reverse=True)[0][0]

# ---------- drop scroll garble ----------
kept, dropped = [], []
for c in clusters:
    n = norm(c["text"])
    toks = n.split()
    bad_toks = [t for t in toks if t.strip("[]()") not in asr_vocab]
    if (c["sightings"] <= 2 and len(n) <= 7 and bad_toks
            and not n.startswith("[")):
        dropped.append(c["text"])
    else:
        kept.append(c)
clusters = kept

# order by first appearance, then row position
clusters.sort(key=lambda c: (c["first_t"], c["last_j"]))

# ---------- split section tags ----------
lines = []
for c in clusters:
    m = re.match(r"^\s*\[([^\]]+)\]\s*(.*)$", c["text"])
    if m:
        lines.append({"kind": "tag", "text": f"[{m.group(1).strip()}]",
                      "width": c["width"], "sightings": c["sightings"]})
        rest = m.group(2).strip()
        if rest:
            lines.append({"kind": "lyric", "text": rest, "width": c["width"],
                          "sightings": c["sightings"]})
    else:
        lines.append({"kind": "lyric", "text": c["text"], "width": c["width"],
                      "sightings": c["sightings"]})

# ---------- rejoin mid-word wraps ----------
def tokens(s):
    return norm(s).split()

joined, wrap_joins = [], []
i = 0
while i < len(lines):
    cur = lines[i]
    if cur["kind"] == "lyric" and i + 1 < len(lines) and lines[i + 1]["kind"] == "lyric":
        nxt = lines[i + 1]
        ct, nt = tokens(cur["text"]), tokens(nxt["text"])
        if ct and nt:
            concat = (ct[-1] + nt[0]).strip("'")
            if concat in asr_vocab and (ct[-1] not in asr_vocab or len(nt[0]) <= 2):
                cur_raw = re.findall(r"\S+", cur["text"])
                nxt_raw = re.findall(r"\S+", nxt["text"])
                head = cur["text"][:cur["text"].rfind(cur_raw[-1])]
                tail = nxt["text"][nxt["text"].find(nxt_raw[0]) + len(nxt_raw[0]):]
                cur = dict(cur)
                cur["text"] = (head + cur_raw[-1] + nxt_raw[0] + tail).strip()
                wrap_joins.append(f"{ct[-1]}+{nt[0]} -> {concat}")
                joined.append(cur)
                i += 2
                continue
    joined.append(cur)
    i += 1
lines = joined

# ---------- cross-occurrence merge ----------
singles = {norm(l["text"]) for l in lines if l["kind"] == "lyric"}
merged, cross = [], []
i = 0
while i < len(lines):
    if (i + 1 < len(lines) and lines[i]["kind"] == "lyric"
            and lines[i + 1]["kind"] == "lyric"
            and norm(lines[i]["text"] + " " + lines[i + 1]["text"]) in singles):
        cur = dict(lines[i])
        cur["text"] = lines[i]["text"] + " " + lines[i + 1]["text"]
        cross.append(cur["text"])
        merged.append(cur)
        i += 2
    else:
        merged.append(lines[i])
        i += 1
lines = merged

with open(os.path.join(WORK, "rows_draft.json"), "w") as f:
    json.dump({"lines": lines, "dropped_garble": dropped,
               "wrap_joins": wrap_joins, "cross_merges": cross}, f, indent=1)
with open(os.path.join(PROJ, "lyrics_draft.txt"), "w") as f:
    for l in lines:
        f.write(l["text"] + "\n")
print(f"DRAFT {PROJ}: {sum(1 for l in lines if l['kind']=='lyric')} lyric rows, "
      f"{sum(1 for l in lines if l['kind']=='tag')} tags, dropped {len(dropped)} garble, "
      f"wrap-joins {len(wrap_joins)}, cross-merges {len(cross)}", flush=True)
