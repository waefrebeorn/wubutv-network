#!/usr/bin/env python3
"""Stage D part 1 — align app per-word output (work/gemini_song_words.json,
536 words) to SONG_WORDS.json (546 words) for the MV-5 v2 rebuild.

Banded Needleman-Wunsch: pairs are only allowed when |start diff| <= 4s
(both tracks are the same audio, so true matches are time-close; this stops
the DP from matching one 'Easy' to another 'Easy' 60s away in this very
repetitive song). Costs: exact match 0.25*|dt|, substitution 2.0+0.25*|dt|,
gap 1.2. Exact (word,start) duplicates in the app output are removed first
(the app lists 'Just two small sparks' twice at identical times, L73b).

Outputs work/gemini_song_words_aligned.json (new file; never overwrites
gemini_song_words.json). Prints alignment stats to stdout.
"""
import json, re, statistics

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
sw = json.load(open(f"{PROJ}/SONG_WORDS.json"))
app = json.load(open(f"{PROJ}/work/gemini_song_words.json"))
A = sw["words"]            # 546, v1 ground truth (Whisper + targeted decodes + sheet)
B_raw = app["words"]       # 536, Gemini app per-word output

# --- dedupe exact (word, start) duplicates in app output ---
seen, B, dups = set(), [], []
for x in B_raw:
    k = (x["word"], x["start"])
    if k in seen:
        dups.append(x)
    else:
        seen.add(k)
        B.append(x)
B.sort(key=lambda x: (x["start"], x["end"]))
print(f"app words raw={len(B_raw)} deduped={len(B)} exact-dupes-removed={len(dups)}")
for d in dups:
    print("  DUP removed:", d)

def norm(w):
    return re.sub(r"[^a-z0-9]", "", w.lower())

def edit_dist(a, b):
    """Levenshtein distance (small strings only)."""
    if a == b:
        return 0
    la, lb = len(a), len(b)
    prev = list(range(lb + 1))
    for i in range(1, la + 1):
        cur = [i] + [0] * lb
        for j in range(1, lb + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1,
                         prev[j - 1] + (0 if a[i - 1] == b[j - 1] else 1))
        prev = cur
    return prev[lb]

def close(a, b):
    """Words close enough that a substitution is the honest reading
    (same word with an STT confusable ending, a contraction split, or a
    hyphenation difference) — vs wholesale different words, which must be
    represented as drop + extra, never forced into a substitution.
    Requires a shared stem: edit distance <=2 needs a >=2-char common
    prefix; distance 3 needs a >=4-char common prefix. So
    replays/replaced (dist 3, prefix 'repla') stays a substitution, while
    hard/head (dist 2, prefix 'h') does not — the latter is an artifact
    of the app's duplicated 'And my whole head replaced' line at 113.4."""
    if a == b:
        return True
    if a.startswith(b) or b.startswith(a):
        return True
    n = 0
    for x, y in zip(a, b):
        if x == y:
            n += 1
        else:
            break
    d = edit_dist(a, b)
    if d <= 2 and n >= 2:
        return True
    if d <= 3 and n >= 4:
        return True
    return False

An = [norm(x["word"]) for x in A]
Bn = [norm(x["word"]) for x in B]
n, m = len(A), len(B)
INF = 1e9
BAND = 4.0
GAP = 1.2

# cost matrices
cost = [[INF] * (m + 1) for _ in range(n + 1)]
bt = [[None] * (m + 1) for _ in range(n + 1)]  # 'M' match/sub, 'D' drop song, 'I' extra app
cost[0][0] = 0.0
for i in range(n + 1):
    for j in range(m + 1):
        if i == 0 and j == 0:
            continue
        best, how = INF, None
        if i > 0 and j > 0:
            dt = abs(A[i - 1]["start"] - B[j - 1]["start"])
            if dt <= BAND:
                if An[i - 1] == Bn[j - 1]:
                    c = 0.25 * dt
                elif close(An[i - 1], Bn[j - 1]):
                    c = 2.0 + 0.25 * dt
                else:
                    c = 3.5 + 0.25 * dt  # dissimilar: drop+extra (2.4) wins
                v = cost[i - 1][j - 1] + c
                if v < best:
                    best, how = v, "M"
        if i > 0:
            v = cost[i - 1][j] + GAP
            if v < best:
                best, how = v, "D"
        if j > 0:
            v = cost[i][j - 1] + GAP
            if v < best:
                best, how = v, "I"
        cost[i][j] = best
        bt[i][j] = how

# traceback
ops = []
i, j = n, m
while i > 0 or j > 0:
    h = bt[i][j]
    if h == "M":
        ops.append(("M", i - 1, j - 1))
        i -= 1; j -= 1
    elif h == "D":
        ops.append(("D", i - 1, None))
        i -= 1
    else:
        ops.append(("I", None, j - 1))
        j -= 1
ops.reverse()

rows = []
stats = {"match": 0, "sub": 0, "dropped": 0, "extra": 0}
dts = []
for op, ai, bi in ops:
    if op == "M":
        a, b = A[ai], B[bi]
        st = "MATCH" if An[ai] == Bn[bi] else "SUBSTITUTED"
        stats["match" if st == "MATCH" else "sub"] += 1
        dt = b["start"] - a["start"]
        dts.append(abs(dt))
        rows.append({
            "song_idx": ai, "song_word": a["word"], "song_start": a["start"],
            "song_end": a["end"], "line": a["line"], "section": a["section"],
            "v1_owner": a["owner"], "app_word": b["word"],
            "app_start": b["start"], "app_end": b["end"],
            "app_speaker": b["speaker"], "status": st,
            "dt_start": round(dt, 2),
        })
    elif op == "D":
        a = A[ai]
        stats["dropped"] += 1
        rows.append({
            "song_idx": ai, "song_word": a["word"], "song_start": a["start"],
            "song_end": a["end"], "line": a["line"], "section": a["section"],
            "v1_owner": a["owner"], "app_word": None, "app_start": None,
            "app_end": None, "app_speaker": None, "status": "DROPPED",
            "dt_start": None,
        })
    else:
        b = B[bi]
        stats["extra"] += 1
        rows.append({
            "song_idx": None, "song_word": None, "song_start": None,
            "song_end": None, "line": None, "section": None, "v1_owner": None,
            "app_word": b["word"], "app_start": b["start"], "app_end": b["end"],
            "app_speaker": b["speaker"], "status": "EXTRA",
            "dt_start": None,
        })

print("alignment:", stats, "total cost:", round(cost[n][m], 1))
print("matched |dt_start|: median", round(statistics.median(dts), 2),
      "mean", round(statistics.mean(dts), 2),
      "p90", round(sorted(dts)[int(0.9 * len(dts))], 2),
      "max", round(max(dts), 2))

print("\n--- DROPPED song words (app heard nothing here) ---")
for r in rows:
    if r["status"] == "DROPPED":
        print(f"  #{r['song_idx']:3d} {r['line']:5s} {r['song_start']:7.2f} {r['song_word']} (v1 {r['v1_owner']})")

print("\n--- SUBSTITUTED pairs (different word, same slot) ---")
for r in rows:
    if r["status"] == "SUBSTITUTED":
        print(f"  #{r['song_idx']:3d} {r['line']:5s} {r['song_start']:7.2f} v1={r['song_word']!r} app={r['app_word']!r} {r['app_speaker']} dt={r['dt_start']}")

print("\n--- EXTRA app words (no song slot) ---")
for r in rows:
    if r["status"] == "EXTRA":
        print(f"  {r['app_start']:7.2f} {r['app_word']} {r['app_speaker']}")

# --- speaker agreement: app speaker vs v1 line owner on MATCHED words ---
agree = {"spk:0": {"CAT": 0, "GIRL": 0, "SPLIT": 0},
         "spk:1": {"CAT": 0, "GIRL": 0, "SPLIT": 0}}
for r in rows:
    if r["status"] in ("MATCH", "SUBSTITUTED") and r["app_speaker"] in agree:
        agree[r["app_speaker"]][r["v1_owner"]] += 1
print("\n--- app speaker vs v1 line owner (aligned words) ---")
for spk, c in agree.items():
    tot = sum(c.values())
    print(f"  {spk}: CAT-lines={c['CAT']} GIRL-lines={c['GIRL']} SPLIT-lines={c['SPLIT']} total={tot}")

# --- per-line speaker summary for contested lines ---
print("\n--- app speakers by line (contested / anchor lines) ---")
from collections import Counter
by_line = {}
for r in rows:
    if r["line"] and r["app_speaker"]:
        by_line.setdefault(r["line"], Counter())[r["app_speaker"]] += 1
for lid in ["L12", "L15", "L49", "L50", "L51", "L52", "L53", "L54", "L56",
            "L57", "L62", "L77", "L80", "L81", "L82", "L84", "L86", "L88",
            "L106", "L107", "L108", "L109", "L110", "I04", "I09"]:
    print(f"  {lid}: {dict(by_line.get(lid, {}))}")

out = {
    "method": "Banded Needleman-Wunsch on normalized word tokens (lowercase, punctuation stripped), "
              "band |dt_start|<=4.0s; match cost 0.25*|dt|, substitution 2.0+0.25*|dt|, gap 1.2. "
              "App words deduped on exact (word,start) first (2 dupes removed). "
              "Source: work/gemini_song_words.json (536 app words) vs SONG_WORDS.json (546 words). "
              "Gemini timestamps are model-generated, not CTC forced-aligned.",
    "counts": {"song_words": n, "app_words_raw": len(B_raw),
               "app_words_deduped": len(B), **stats},
    "duplicates_removed": dups,
    "dt_stats": {"median": round(statistics.median(dts), 3),
                 "mean": round(statistics.mean(dts), 3),
                 "p90": round(sorted(dts)[int(0.9 * len(dts))], 3),
                 "max": round(max(dts), 3)},
    "speaker_vs_v1_owner": agree,
    "rows": rows,
}
json.dump(out, open(f"{PROJ}/work/gemini_song_words_aligned.json", "w"), indent=1)
print("\nwrote work/gemini_song_words_aligned.json")
