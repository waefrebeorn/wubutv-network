#!/usr/bin/env python3
"""Match one take's whisper words to song words (pipeline tool).

Same method as the original MV-2 v3 match, hardened: vehicle window +-12s,
LCS sequence alignment (not greedy-earliest), no reuse. Whisper mishears normalized via an
explicit map (never silent guessing beyond the map). Unmatched take
words get song=None and are swept by the assembler.

Usage: match_take.py <scene> <take_words.json> <veh_lo> <veh_hi>
Prints the anchor list; writes masters_work_v3/match_<scene>.json.
The caller merges it into WORD_MATCH_V3.json (backing the original up).
"""
import json
import re
import sys
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
MISHEAR = {
    "done": "dumb", "toe": "toll", "tall": "toll", "told": "toll",
    "plasers": "plazas", "rex": "wrecks", "dine": "dime",
    "your": "you", "watchin'": "watching", "weavein'": "weave",
    "$1": "dollar",
}


def norm(w):
    w = w.strip().lower().strip(".,!?;:'\"()")
    w = re.sub(r"'$", "", w)
    return MISHEAR.get(w, w)


def main():
    scene, take_json, lo, hi = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
    take = json.load(open(take_json))["words"]
    song = json.load(open(PROJ / "SONG_WORDS_BASE.json"))
    lo, hi = max(0.0, lo - 12), hi + 12
    # Sequence alignment (LCS) between take words and song words in the
    # window, degenerate song words excluded. Greedy-earliest FAILS here:
    # S21's take opens "The road gets meaner..." (whose song 'the' is a
    # zero-duration burst word) and later sings "The wrecks..."; greedy
    # gives the first 'The' to the wrecks line's 'The' (205.20) and then
    # strands every later word (3/21 anchored, two of them wrong). LCS
    # maximizes total matches, so it leaves the burst head unmatched and
    # anchors the dense passage instead (15/21 for S21).
    cand = [(i, sw) for i, sw in enumerate(song)
            if lo <= sw["t0"] <= hi and sw["t1"] > sw["t0"]]
    n, m = len(take), len(cand)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if norm(take[i]["word"]) == norm(cand[j][1]["word"]):
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    pair = {}
    i = j = 0
    while i < n and j < m:
        if norm(take[i]["word"]) == norm(cand[j][1]["word"]) and \
                dp[i][j] == 1 + dp[i + 1][j + 1]:
            pair[i] = cand[j]
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    anchors = []
    for k, tw in enumerate(take):
        if k in pair:
            idx, sw = pair[k]
            anchors.append({"take": {"t0": tw["start"], "t1": tw["end"],
                                     "word": tw["word"]},
                            "song": {"t0": sw["t0"], "t1": sw["t1"],
                                     "word": sw["word"]},
                            "song_idx": idx})
        else:
            anchors.append({"take": {"t0": tw["start"], "t1": tw["end"],
                                     "word": tw["word"]},
                            "song": None, "song_idx": None})
    out = {"window": [0.0, 10.0], "anchors": anchors}
    dest = PROJ / "masters_work_v3" / f"match_{scene}.json"
    json.dump(out, open(dest, "w"), indent=1)
    n = sum(1 for a in anchors if a["song"])
    print(f"{scene}: {n}/{len(anchors)} anchored -> {dest}")
    for a in anchors:
        if a["song"]:
            print(f"  take {a['take']['t0']:5.2f} {a['take']['word']:>10} "
                  f"-> song {a['song']['t0']:7.2f} {a['song']['word']}")
        else:
            print(f"  take {a['take']['t0']:5.2f} {a['take']['word']:>10} -> None")


if __name__ == "__main__":
    main()
