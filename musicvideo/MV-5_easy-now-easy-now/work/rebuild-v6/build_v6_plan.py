#!/usr/bin/env python3
"""MV-5 v6 fit builder v3 — text-derived grid sequences, cursor-ordered
DP alignment, onset-anchored warps, tiling layout with tail absorption,
global src clamp. Emits assembly_fit_mv5_v6.json."""
import json, glob, os
from difflib import SequenceMatcher

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
V6 = PROJ + "/work/rebuild-v6"
grid = json.load(open(PROJ + "/work/lyrics-redo/grid_merged.json"))
LINES = {l["id"]: l for l in grid["lines"]}
GWORDS = grid["words"]
FPS = 24

BOUNDS = [0.0, 10.0417, 18.625, 22.0, 31.5, 40.4583, 47.625, 57.5,
          67.0417, 76.7917, 85.1667, 93.7917, 102.1417, 111.9167,
          119.1458, 121.2917, 130.7917, 140.5, 148.7083, 155.7083,
          158.0417, 167.5, 168.72, 176.0417, 182.7917, 190.4167,
          193.0, 203.8333, 206.4167]
SCENES = [f"S{i+1:02d}" for i in range(28)]

def norm(w):
    w = w.lower().strip(".,!?\"'“”")
    w = w.replace("-", "").replace("’", "'")
    if w.endswith("s") and len(w) > 3:
        w = w[:-1]
    return w.replace("grey", "gray")

def sim(a, b):
    return SequenceMatcher(None, norm(a), norm(b)).ratio()

def text_seq(lid):
    """Grid word dicts for a line, derived from its TEXT: each token takes
    the time of the nearest unused grid word in the line window."""
    l = LINES[lid]
    toks = l["text"].replace(",", " ").replace("  ", " ").split()
    pool = [w for w in GWORDS if l["start"] - 0.05 <= w["start"] < l["end"] + 0.12]
    used = set()
    out = []
    for t in toks:
        best, bi = 0.6, -1
        for i, w in enumerate(pool):
            if i in used:
                continue
            s = sim(t, w["word"])
            if s > best:
                best, bi = s, i
        if bi >= 0:
            used.add(bi)
            out.append(pool[bi])
        else:  # interpolate a placeholder between neighbours
            out.append(None)
    # fill placeholders by interpolation (rare; keeps indices aligned)
    res = []
    for i, w in enumerate(out):
        if w is not None:
            res.append(w)
        else:
            prev = next((out[j] for j in range(i - 1, -1, -1) if out[j]), None)
            nxt = next((out[j] for j in range(i + 1, len(out)) if out[j]), None)
            a = prev["end"] if prev else l["start"]
            b = nxt["start"] if nxt else l["end"]
            mid = (a + b) / 2
            res.append({"word": toks[i], "start": mid, "end": mid + 0.1})
    return res

TAKEW, TAKEDUR = {}, {}
for p in glob.glob(V6 + "/qc/words/*.json"):
    d = json.load(open(p))
    TAKEW[os.path.basename(p)[:-5]] = d["words"]
    TAKEDUR[os.path.basename(p)[:-5]] = d["take_dur"]

CURSOR = {}
def align_phrase(take, grid_seq, after=None, min_match=None):
    """DP-align grid_seq to the take stream (words at/after `after`).
    First grid word must match; up to 1 trailing grid word may miss.
    Returns (src_a, src_b, warp, offsets, matched_grid_words)."""
    if after is None:
        after = CURSOR.get(take, 0.0)
    tw_all = TAKEW[take]
    off0 = 0
    tw = tw_all
    if after > 0:
        tw = [w for w in tw_all if w["end"] >= after - 0.02]
        off0 = len(tw_all) - len(tw)
    n, m = len(grid_seq), len(tw)
    if n == 0 or m == 0:
        return None
    NEG = (-10**9, 0)
    dp = [[NEG] * (m + 1) for _ in range(n + 1)]
    bk = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = (0, 0)
    for i in range(n + 1):
        for j in range(m + 1):
            cur = dp[i][j]
            if cur[0] <= NEG[0] // 2:
                continue
            if j < m:
                v = (cur[0], cur[1] - 1)
                if v > dp[i][j + 1]:
                    dp[i][j + 1] = v; bk[i][j + 1] = ("T", i, j)
            if i < n:
                v = (cur[0], cur[1] - 1)
                if v > dp[i + 1][j]:
                    dp[i + 1][j] = v; bk[i + 1][j] = ("G", i, j)
            if i < n and j < m and sim(grid_seq[i]["word"], tw[j]["word"]) >= 0.45:
                v = (cur[0] + 1, cur[1])
                if v > dp[i + 1][j + 1]:
                    dp[i + 1][j + 1] = v; bk[i + 1][j + 1] = ("M", i, j)
    best_j, best = -1, NEG
    for j in range(m + 1):
        if dp[n][j] > best:
            best, best_j = dp[n][j], j
    matched = best[0]
    need = min_match if min_match else int(0.8 * n + 0.999)
    if matched < max(1, need):
        return None
    pairs = []
    i, j = n, best_j
    while (i, j) != (0, 0):
        step = bk[i][j]
        if step is None:
            break
        kind, pi, pj = step
        if kind == "M":
            pairs.append((pi, pj))
        i, j = pi, pj
    pairs.reverse()
    if not pairs or pairs[0][0] != 0:
        return None
    if n - 1 - pairs[-1][0] > 1:
        return None
    gw = [grid_seq[a] for a, _ in pairs]
    twm = [tw[b] for _, b in pairs]
    if len(gw) >= 2 and gw[-1]["start"] - gw[0]["start"] > 0.15:
        warp = (twm[-1]["start"] - twm[0]["start"]) / (gw[-1]["start"] - gw[0]["start"])
    else:
        warp = (twm[-1]["end"] - twm[0]["start"]) / max(0.05, gw[-1]["end"] - gw[0]["start"])
    src_a = max(0.0, twm[0]["start"] - 0.06)
    if pairs[-1][0] == n - 1:
        src_b = min(TAKEDUR[take], twm[-1]["end"] + 0.05)
    else:  # trailing grid word unmatched: project its end through the warp
        span = grid_seq[-1]["end"] - grid_seq[0]["start"]
        src_b = min(TAKEDUR[take], twm[0]["start"] + span * warp + 0.05)
    offs = []
    for g, t in zip(gw, twm):
        pred = gw[0]["start"] + (t["start"] - twm[0]["start"]) / warp
        offs.append(round(pred - g["start"], 3))
    CURSOR[take] = src_b
    return src_a, src_b, warp, offs, gw, (twm[0]["start"], twm[-1]["end"])

def align_near(take, grid_seq, expected_src, tol=2.75):
    """Align a short grid seq near an expected src position (span offsets)."""
    tw = TAKEW[take]
    lo = max(0.0, expected_src - tol)
    hi = expected_src + tol + 2.0
    sub = [w for w in tw if lo <= w["start"] <= hi]
    if not sub or not grid_seq:
        return None
    n = len(grid_seq)
    best = None
    for i in range(len(sub) - n + 1):
        sc = sum(sim(grid_seq[k]["word"], sub[i + k]["word"]) for k in range(n)) / n
        if best is None or sc > best[0]:
            best = (sc, sub[i]["start"])
    if best and best[0] >= 0.75:
        return best[1]
    return None

# ---- spec ---------------------------------------------------------------
SPEC = {
 "S01": [("F", "mv5_v6_s02_ride", 0.5, 3.0, True),
         ("P", "mv5_v6_s01_cat", [("I01", None)]),
         ("P", "mv5_v6_s01_cat", [("I02", None)]),
         ("P", "mv5_v6_s01_cat", [("I03", None)]),
         ("P", "mv5_v6_s01_cat", [("I04", None)])],
 "S02": [("F", "mv5_v6_s02_ride", 3.5, 6.0, True),
         ("P", "mv5_v6_s02_girl", [("I05", None)]),
         ("SX", "mv5_v6_s02_girl", ["I08"])],
 "S03": [("SX", "mv5_v6_s03_girl", ["I09"])],
 "S04": [("P", "mv5_v6_s04_cat", [("L01", None)]),
         ("PX2", "mv5_v6_s04_cat", 1.81, 3.04, 22.96, 25.24),
         ("P", "mv5_v6_s04_cat", [("L03", None)]),
         ("P", "mv5_v6_s04_cat", [("L04", None)]),
         ("PX2", "mv5_v6_s04_cat2", 0.0, 2.66, 30.10, 31.48)],
 "S05": [("F", "mv5_v6_s02_ride", 6.0, 6.5, True),
         ("P", "mv5_v6_s05_cat", [("L06", None)]),
         ("P", "mv5_v6_s05_cat", [("L07", None)]),
         ("P", "mv5_v6_s05_cat", [("L08", None)]),
         ("F", "mv5_v6_s01_cat", 9.0, 10.0, False)],
 "S06": [("F", "mv5_v6_s02_ride", 9.2, 10.0, True),
         ("P", "mv5_v6_s06_cat", [("L10", None)]),
         ("F", "mv5_v6_s11_cat", 0.0, 1.65, False),
         ("P", "mv5_v6_s06_cat", [("L12", None)])],
 "S07": [("P", "mv5_v6_s07_girla", [("L13", (0, 2))]),
         ("P", "mv5_v6_s07_cat", [("L13", (2, 6)), ("L14", None)]),
         ("P", "mv5_v6_s07_girla", [("L15", None)]),
         ("P", "mv5_v6_s07_girlb", [("L16", None)])],
 "S08": [("F", "mv5_v6_s02_girl", 9.35, 9.65, True),
         ("SX", "mv5_v6_s08_duet", ["L17", "L18", "L19", "L20", "L21", "L22"])],
 "S09": [("SX", "mv5_v6_s09b_duet", ["L23", "L24", "L25", "L26", "L27", "L28",
                                    "L29", "L30", "L31", "L32"])],
 "S10": [("F", "pilot_p2_cat", 3.2, 5.0, True),
         ("P", "mv5_v6_s10_cat", [("L33", None)]),
         ("P", "mv5_v6_s10_cat", [("L34", None), ("L35", None)]),
         ("P", "mv5_v6_s10_cat", [("L36", None)])],
 "S11": [("F", "mv5_v6_s03_girl", 8.5, 10.0, True),
         ("P", "mv5_v6_s11_cat", [("L37", None)]),
         ("P", "mv5_v6_s11_cat", [("L38", None)]),
         ("P", "mv5_v6_s11_cat", [("L39", None)]),
         ("P", "mv5_v6_s11_cat", [("L40", (0, 5))]),
         ("P", "mv5_v6_s11_girl", [("L40", (5, 9))])],
 "S12": [("P", "mv5_v6_s12_cat", [("L41", None)]),
         ("P", "mv5_v6_s12_cat", [("L42", None)]),
         ("P", "mv5_v6_s12_girl", [("L43", None)]),
         ("PX", "mv5_v6_s12_cat", 6.30, 9.65, "L44")],
 "S13": [("P", "mv5_v6_s13_cat", [("L45", (0, 3))]),
         ("PX2", "mv5_v6_s13_girl", 0.0, 1.95, 103.54, 105.18),
         ("P", "mv5_v6_s13_cat", [("L47", None)]),
         ("P", "mv5_v6_s13_cat", [("L48", None)]),
         ("F", "mv5_v6_s13_boombox", 0.5, 9.5, True),
         ("P", "mv5_v6_s13_girl", [("L50", None)]),
         ("F", "mv5_v6_s13_spin", 3.40, 4.55, False),
         ("P", "mv5_v6_s13_girl", [("L52", None)])],
 "S14": [("P", "mv5_v6_s15_girl", [("L53", (0, 2))]),
         ("P", "mv5_v6_s15_cat2", [("L53", (2, 5))]),
         ("P", "mv5_v6_s15_cat2", [("L54", (0, 4))]),
         ("PX2", "mv5_v6_s15_girl", 1.36, 1.64, 114.6, 114.9),
         ("P", "mv5_v6_s15_cat2", [("L55", None)]),
         ("P", "mv5_v6_s15_girl", [("L56", None)])],
 "S15": [("F", "mv5_v6_s15_girl", 7.6, 9.9, True)],
 "S16": [("SX", "mv5_v6_s16_duet", ["L57", "L58", "L59", "L60", "L61", "L62",
                                    "L63", "L64"])],
 "S17": [("SX", "mv5_v6_s17_duet", ["L65", "L66", "L67", "L68", "L69", "L70",
                                    "L71", "L72"])],
 "S18": [("SX", "mv5_v6_s18_girl", ["L73a", "L73b", "L73d"]),
         ("F", "mv5_v6_s18_girl", 7.7, 9.9, True)],
 "S19": [("F", "mv5_v6_s02_girl", 9.7, 10.0, True),
         ("SX", "mv5_v6_s19_bridge", ["L74", "L75", "L76", "L77", "L78", "L79"])],
 "S20": [("P", "mv5_v6_s20_bridge", [("L80", None)]),
         ("PX2", "mv5_v6_s20_cat2", 0.0, 1.80, 157.02, 157.94)],
 "S21": [("P", "mv5_v6_s21_all2", [("L82", None)]),
         ("PX", "mv5_v6_s21_all2", 2.77, 3.75, "L83"),
         ("PX", "mv5_v6_s21_all2", 3.80, 4.67, "L84"),
         ("P", "mv5_v6_s21_all2", [("L85", None)]),
         ("F", "mv5_v6_s21_spin", 3.90, 4.40, True),
         ("P", "mv5_v6_s21_all2", [("L86", None)]),
         ("PX2", "mv5_v6_s21_girl2", 0.0, 2.0, 163.66, 164.88),
         ("P", "mv5_v6_s21_all2", [("L88", None)]),
         ("P", "mv5_v6_s21_walk", [("L89", None)])],
 "S22": [("F", "mv5_v6_s21_walk", 8.9, 10.0, True)],
 "S23": [("SX", "mv5_v6_s23_duet", ["L91", "L92", "L93", "L94", "L95", "L96"])],
 "S24": [("SX", "mv5_v6_s24_duet", ["L98", "L99", "L100", "L101", "L102"])],
 "S25": [("P", "mv5_v6_s25_cat2", [("L104", None)]),
         ("PT", "mv5_v6_s25_girl", "easy now easy now", 185.02, 186.46),
         ("PT", "mv5_v6_s25_girl", "just two small sparks", 186.46, 188.04)],
 "S26": [("F", "mv5_v6_s26_chain", 2.5, 5.2, True)],
 "S27": [("F", "mv5_v6_s26_chain", 0.0, 1.2, True),
         ("SX", "mv5_v6_s27_chant", ["L108"]),
         ("P", "mv5_v6_s27_cat2", [("L109", None)])],
 "S28": [("PX", "mv5_v6_s28_cat2", 0.0, 2.35, "L110")],
}
OBJECT_ONLY = {"mv5_v6_s26_chain", "mv5_v6_s13_ice", "mv5_v6_s02_ride",
               "mv5_v6_s13_boombox"}

# ---- resolve --------------------------------------------------------------
errors, disclosed, notes = [], [], []

def grid_seq_for(parts):
    seq = []
    for lid, sl in parts:
        ws = text_seq(lid)
        if sl:
            ws = ws[sl[0]:sl[1]]
        seq.extend(ws)
    return seq

def part_window(parts):
    a, b = parts[0], parts[-1]
    la, lb = LINES[a[0]], LINES[b[0]]
    wa, wb = text_seq(a[0]), text_seq(b[0])
    start = la["start"] if (a[1] is None or a[1][0] == 0) else wa[a[1][0]]["start"]
    end = lb["end"] if (b[1] is None or b[1][1] >= len(wb)) else wb[b[1][1] - 1]["end"]
    return start, end

resolved = {}
for sc in SCENES:
    out = []
    for item in SPEC[sc]:
        kind = item[0]
        if kind in ("P", "PH"):
            _, take, parts = item
            if kind == "PH":
                parts = [(lid, None) for lid in parts]
            seq = grid_seq_for(parts)
            r = align_phrase(take, seq, min_match=2 if kind == "PH" else None)
            if r is None:
                errors.append(f"{sc} PHRASE NOT FOUND {take} {[p[0] for p in parts]} "
                              f"'{' '.join(w['word'] for w in seq)}'")
                continue
            src_a, src_b, warp, offs, _, core = r
            sa, sb = part_window(parts)
            out.append(dict(kind="phrase", take=take, src_a=src_a, src_b=src_b,
                            sung_a=src_a, sung_b=src_b, warp=warp,
                            core_a=core[0], core_b=core[1],
                            song_a=sa, song_b=sb, lines=[p[0] for p in parts],
                            offsets=offs))
        elif kind in ("PX", "PX2"):
            if kind == "PX":
                _, take, sa_, sb_, lid = item
                wa, wb = LINES[lid]["start"], LINES[lid]["end"]
                lids = [lid]
            else:
                _, take, sa_, sb_, wa, wb = item
                lids = ["PX2"]
            CURSOR[take] = max(CURSOR.get(take, 0.0), sb_)
            out.append(dict(kind="phrase", take=take, src_a=sa_, src_b=sb_,
                            sung_a=sa_, sung_b=sb_, core_a=sa_, core_b=sb_,
                            warp=(sb_ - sa_) / (wb - wa),
                            song_a=wa, song_b=wb, lines=lids, offsets=[], px=True))
        elif kind == "PT":
            _, take, text, sa, sb = item
            toks = text.split()
            tw = [w for w in TAKEW[take] if w["end"] >= CURSOR.get(take, 0.0) - 0.02]
            found = None
            for i in range(len(tw) - len(toks) + 1):
                if all(sim(toks[k], tw[i + k]["word"]) >= 0.6 for k in range(len(toks))):
                    found = (tw[i]["start"], tw[i + len(toks) - 1]["end"])
                    break
            if found is None:
                errors.append(f"{sc} PT NOT FOUND {take} '{text}'")
                continue
            src_a = max(0.0, found[0] - 0.06)
            src_b = min(TAKEDUR[take], found[1] + 0.06)
            CURSOR[take] = src_b
            out.append(dict(kind="phrase", take=take, src_a=src_a, src_b=src_b,
                            sung_a=src_a, sung_b=src_b, core_a=src_a, core_b=src_b,
                            warp=(src_b - src_a) / (sb - sa),
                            song_a=sa, song_b=sb, lines=["PT:" + text], offsets=[]))
        elif kind in ("S", "SX"):
            _, take, lids = item
            sa, sb = LINES[lids[0]]["start"], LINES[lids[-1]]["end"]
            tw = TAKEW[take]
            if not tw:
                errors.append(f"{sc} SPAN TAKE HAS NO WORDS {take}")
                continue
            first = align_phrase(take, text_seq(lids[0])[:3])
            src_a = first[0] if first else max(0.0, tw[0]["start"] - 0.06)
            last = align_phrase(take, text_seq(lids[-1])[-3:])
            if last:
                src_b = min(TAKEDUR[take], last[1] + 0.9)
            else:
                src_b = min(TAKEDUR[take], tw[-1]["end"] + 1.2)
            warp = (src_b - src_a) / (sb - sa)
            CURSOR[take] = src_b
            offs = []
            for lid in lids:
                lw = text_seq(lid)
                if not lw:
                    continue
                exp_src = src_a + (lw[0]["start"] - sa) * warp
                got = align_near(take, lw[:2], exp_src)
                if got is not None:
                    pred = sa + (got - src_a) / warp
                    offs.append((lid, round(lw[0]["start"] - pred, 3)))
            out.append(dict(kind="span", take=take, src_a=src_a, src_b=src_b,
                            sung_a=src_a, sung_b=src_b, core_a=src_a, core_b=src_b,
                            warp=warp,
                            song_a=sa, song_b=sb, lines=lids, offsets=offs,
                            span_off=True, sx=(kind == "SX")))
        elif kind == "F":
            _, take, sa_, sb_, ex = item
            CURSOR[take] = max(CURSOR.get(take, 0.0), sb_)
            out.append(dict(kind="fill", take=take, src_a=sa_, src_b=sb_,
                            sung_a=sa_, sung_b=sb_, core_a=sa_, core_b=sb_,
                            warp=None, song_a=None,
                            song_b=None, lines=[], offsets=[],
                            exempt=ex or take in OBJECT_ONLY))
    resolved[sc] = out

# ---- layout -----------------------------------------------------------------
for idx, sc in enumerate(SCENES):
    lo, hi = BOUNDS[idx], BOUNDS[idx + 1]
    pieces = resolved[sc]
    for p in pieces:
        if p["kind"] != "fill":
            if p["song_a"] < lo:
                notes.append(f"{sc} clip head {lo - p['song_a']:.2f}s {p['lines']}")
                p["song_a"] = lo
            if p["song_b"] > hi:
                notes.append(f"{sc} clip tail {p['song_b'] - hi:.2f}s {p['lines']}")
                p["song_b"] = hi
    fixed = sorted([p for p in pieces if p["kind"] != "fill"],
                   key=lambda p: p["song_a"])
    ordered, fi = [], 0
    for p in pieces:
        if p["kind"] == "fill":
            ordered.append(p)
        else:
            ordered.append(fixed[fi]); fi += 1
    cursor, prev, work, pending = lo, None, [], []
    for p in ordered:
        if p["kind"] == "fill":
            pending.append(p)
            continue
        if pending:
            tot = sum(f["src_b"] - f["src_a"] for f in pending)
            c = cursor
            for f in pending:
                share = (f["src_b"] - f["src_a"]) / tot if tot else 1
                f["song_a"] = c
                f["song_b"] = c + (p["song_a"] - c) * share
                c = f["song_b"]
                work.append(f)
            pending = []
            cursor = p["song_a"]
            prev = work[-1] if work else None
        elif p["song_a"] > cursor + 0.04:
            gap = p["song_a"] - cursor
            if prev is not None and prev["kind"] in ("phrase", "span"):
                prev["song_b"] = p["song_a"]
                prev["src_b"] = min(TAKEDUR[prev["take"]],
                                    prev["src_b"] + gap * prev["warp"])
            elif prev is not None:
                prev["song_b"] = p["song_a"]
            else:
                # head gap: extend first piece backward
                need = gap * p["warp"]
                if p["src_a"] >= need:
                    p["src_a"] -= need
                    p["sung_a"] = p["src_a"]
                    p["song_a"] = cursor
                    notes.append(f"{sc} head gap {gap:.2f}s absorbed backward "
                                 f"into {p['take']}")
                else:
                    errors.append(f"{sc} HEAD GAP {gap:.2f}s uncovered "
                                  f"({p['take']} src_a {p['src_a']:.2f})")
                    p["song_a"] = cursor
        elif p["song_a"] < cursor - 0.01:
            ov = cursor - p["song_a"]
            if prev is not None and ov <= 0.75:
                prev["song_b"] = p["song_a"]
                notes.append(f"{sc} overlap clip {ov:.2f}s on prev {prev['lines']}")
            elif ov > 0.75:
                errors.append(f"{sc} SONG OVERLAP {ov:.2f}s {p['lines']}")
            cursor = p["song_a"]
        work.append(p)
        cursor = max(cursor, p["song_b"])
        prev = p
    if pending:
        tot = sum(f["src_b"] - f["src_a"] for f in pending)
        c = cursor
        for f in pending:
            share = (f["src_b"] - f["src_a"]) / tot if tot else 1
            f["song_a"] = c
            f["song_b"] = c + (hi - c) * share
            c = f["song_b"]
            work.append(f)
        cursor = hi
    elif hi > cursor + 0.04:
        if prev is not None:
            gap = hi - cursor
            prev["song_b"] = hi
            if prev["kind"] in ("phrase", "span"):
                prev["src_b"] = min(TAKEDUR[prev["take"]],
                                    prev["src_b"] + gap * prev["warp"])
            cursor = hi
        else:
            errors.append(f"{sc} EMPTY SCENE")
    resolved[sc] = work

# ---- gates --------------------------------------------------------------------
for sc in SCENES:
    for p in resolved[sc]:
        if p["kind"] in ("phrase", "span"):
            if p["warp"] > 2.0 or p["warp"] < 0.5:
                errors.append(f"{sc} WARP {p['warp']:.3f} FAIL {p['take']} {p['lines']}")
            if p.get("span_off"):
                for lid, off in p["offsets"]:
                    if p.get("sx"):
                        if abs(off) > 0.5:
                            disclosed.append(f"{sc} SX span onset offset {off:+.2f}s {lid} "
                                             f"({p['take']}) — disclosed (continuous-shot span)")
                    elif abs(off) > 1.0:
                        errors.append(f"{sc} SPAN OFFSET {off:+.2f} FAIL {lid}")
                    elif abs(off) > 0.5:
                        disclosed.append(f"{sc} span onset offset {off:+.2f}s {lid} "
                                         f"({p['take']}) — disclosed")
            else:
                mx = max((abs(o) for o in p["offsets"]), default=0)
                if mx > 0.5:
                    disclosed.append(f"{sc} phrase word offset max {mx:.2f}s "
                                     f"{p['take']} {p['lines']} — disclosed")
        else:
            d = p["song_b"] - p["song_a"]
            if d > 0:
                p["warp"] = (p["src_b"] - p["src_a"]) / d
                if not (0.35 <= p["warp"] <= 2.6):
                    notes.append(f"{sc} fill warp {p['warp']:.2f} {p['take']} (warn)")

# ---- src clamp ------------------------------------------------------------------
usage = {}
for sc in SCENES:
    for p in resolved[sc]:
        usage.setdefault(p["take"], []).append((p["src_a"], p["src_b"], sc, p))
for take, spans in usage.items():
    spans.sort(key=lambda x: x[0])
    for (a1, b1, s1, p1), (a2, b2, s2, p2) in zip(spans, spans[1:]):
        if a2 < b1 - 0.01:
            # trim p1's trailing pad/tail down toward its core end
            new_b1 = max(p1["core_b"], min(b1, p2["core_a"] - 0.01))
            if new_b1 < b1:
                notes.append(f"clamp: {take} {s1} src_b {b1:.2f}->{new_b1:.2f} for {s2}")
                p1["src_b"] = new_b1; b1 = new_b1
            if a2 < b1 - 0.01:
                new_a2 = min(p2["core_a"], b1)
                if new_a2 > a2:
                    notes.append(f"clamp: {take} {s2} src_a {a2:.2f}->{new_a2:.2f} for {s1}")
                    p2["src_a"] = new_a2; a2 = new_a2
            if a2 < b1 - 0.01:
                errors.append(f"SRC REUSE {take} [{a1:.2f},{b1:.2f}] {s1} vs "
                              f"[{a2:.2f},{b2:.2f}] {s2}")

# ---- cover word overlap -----------------------------------------------------------
for sc in SCENES:
    for p in resolved[sc]:
        if p["kind"] != "fill" or p.get("exempt"):
            continue
        tw = TAKEW[p["take"]]
        gw = [w for w in GWORDS if p["song_a"] - 0.01 <= w["start"] < p["song_b"]]
        for w in tw:
            if p["src_a"] - 0.01 <= w["start"] and w["end"] <= p["src_b"] + 0.01:
                mapped = p["song_a"] + (w["start"] - p["src_a"]) / p["warp"]
                for g in gw:
                    if sim(w["word"], g["word"]) >= 0.6 and abs(mapped - g["start"]) < 0.20:
                        errors.append(f"COVER WORD OVERLAP {sc} {p['take']} "
                                      f"'{w['word']}' ~ '{g['word']}' @{g['start']:.2f}")

# ---- out frames + emit --------------------------------------------------------------
plan = {"total_frames": 4954, "scenes": {}}
tot = 0
for idx, sc in enumerate(SCENES):
    target = round((BOUNDS[idx + 1] - BOUNDS[idx]) * FPS)
    acc = 0
    for p in resolved[sc]:
        p["out"] = round((p["song_b"] - p["song_a"]) * FPS)
        acc += p["out"]
    residue = target - acc
    if abs(residue) > 3:
        errors.append(f"{sc} OUT SUM off by {residue}f")
    elif residue and resolved[sc]:
        resolved[sc][-1]["out"] += residue
        notes.append(f"{sc} residue {residue:+d}f absorbed by last piece")
    pcs = []
    for p in resolved[sc]:
        pcs.append(dict(kind=p["kind"], take=p["take"],
                        src=[round(p["src_a"], 3), round(p["src_b"], 3)],
                        song=[round(p["song_a"], 3), round(p["song_b"], 3)],
                        out=p["out"],
                        warp=round(p["warp"], 3) if p["warp"] else None,
                        lines=p["lines"],
                        offsets=p["offsets"] if not p.get("span_off")
                                else [list(o) for o in p["offsets"]]))
        tot += p["out"]
    plan["scenes"][sc] = dict(start=BOUNDS[idx], frames=target, pieces=pcs)
plan["computed_frames"] = tot
plan["disclosed"] = disclosed
plan["notes"] = notes
json.dump(plan, open(V6 + "/assembly_fit_mv5_v6.json", "w"), indent=1)
print(f"scene frames 4954 | plan frames {tot}")
print(f"ERRORS {len(errors)}")
for e in errors:
    print("  E:", e)
print(f"DISCLOSED {len(disclosed)}")
for d in disclosed:
    print("  D:", d)
for n in notes:
    print("  N:", n)
