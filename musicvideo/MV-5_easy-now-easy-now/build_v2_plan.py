#!/usr/bin/env python3
"""MV-5 v2 plan builder — work/assembly_fit_mv5_v2.json.

Starts from the v1 plan (work/assembly_fit_mv5.json) and changes ONLY the
scenes the audit (work/gemini_takes_verdicts.md + work/gemini_takes.json) and
the volley-12/13 QC amendments touch:
  S05  re-time from app per-line fits (scene fit for L09, 1 matched word)
  S06  L10/L11 from s06_t1 app fits; L12 from s06_t2 (qc_v12, warp 0.88)
  S07  L13/L14/L16 from s07_t1 app fits; L15 = donor cover (closed mouth)
  S12  L41/L43 from the SCENE fit (0.67) — L43's per-line fit (0.40) is
       illegal; L42/L44 donor cover (v1)
  S15  TWO ANCHORS (brief): head 0.3-2.5 -> 116.2-118.4 @1.0x;
       held tail 2.5-4.3 -> 118.4-120.2 @1.0x (replays covers 119.5)
  S21  interleaved: L82/L84/L86 structural covers (t8/t9/t10 closed-mouth
       tails); L83/L85 s21_t3 per-line (brief warps 0.79 / 0.605, grey);
       L87 donor; L88 s21_t7 (qc_v12, v1-grid, warp 0.89); L89 donor
  S26  tail-only cover: donor head, s26_t1 tail frames >=144 for L108
  S27  L109 s27_t1 head @1.0x; tail/donor fill; L110a s28_t1 CAT Till
       (warp 0.80, 201.0 onset)
  S28  structural: s28_t3 closed-mouth tail 3.0-5.0s + s28_t1 tail
All other scenes copy the v1 plan verbatim (parent scope decision).

Method per line piece: least-squares fit of take word STARTS -> song word
STARTS (app times, v2 grid); warp = fit slope; sf/ef from the take word
span (first start -> last end); dst0 = intercept + slope*(sf/24);
out = round((ef-sf)*warp). Fillers (1.0x, same take's inter-line frames
or donor tails) tile each scene to its v1 frame total (4954 overall).
Warps in [0.60, 1.60] are legal (grey outside [0.80, 1.25]); anything
outside is a GAP and is reported, never forced.
"""
import json, os, sys

PROJ = os.path.dirname(os.path.abspath(__file__))
V1 = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5.json")))
TAKES = json.load(open(os.path.join(PROJ, "work", "gemini_takes.json")))["scenes"]
FPS = 24

BOUNDS = V1["bounds"]
SCENES = V1["scenes"]
TARGET = {sc: sum(p["out"] for p in V1["plan"][sc]) for sc in SCENES}
assert sum(TARGET.values()) == 4954, sum(TARGET.values())

GAPS = []   # (scene, line, reason) — illegal placements, reported not forced
NOTES = []  # (scene, line, note) — disclosures

def ls_fit(pairs):
    """Least squares song = a + b*take over (take_start, song_start) pairs."""
    n = len(pairs)
    mt = sum(p[0] for p in pairs) / n
    ms = sum(p[1] for p in pairs) / n
    cov = sum((t - mt) * (s - ms) for t, s in pairs)
    var = sum((t - mt) ** 2 for t, s in pairs)
    b = cov / var if var else 0.0
    a = ms - b * mt
    res = [abs(s - (a + b * t)) for t, s in pairs]
    res.sort()
    return b, a, res[len(res) // 2], res[-1]

def words_of(scene, line):
    e = TAKES[scene]
    return sorted([w for w in e.get("words", []) if w["line"] == line],
                  key=lambda w: w["take_start"])

def line_piece(take, scene, line, slope, intercept, warp=None, dst0=None,
               kind="line", sf=None, ef=None):
    ws = words_of(scene, line)
    if sf is None:
        sf = round(ws[0]["take_start"] * FPS)
    if ef is None:
        ef = round(ws[-1]["take_end"] * FPS)
    w = warp if warp is not None else slope
    if not (0.60 <= w <= 1.60):
        GAPS.append((scene, line, f"warp {w:.3f} outside [0.60,1.60]"))
    d0 = dst0 if dst0 is not None else intercept + slope * (sf / FPS)
    out = round((ef - sf) * w)
    d1 = d0 + out / FPS
    # word placement report: placed onset vs song start
    placed = []
    for wd in ws:
        placed.append((wd["song_word"], wd["take_start"],
                       d0 + (wd["take_start"] - sf / FPS) * w,
                       wd["song_start_v2"]))
    return {"take": take, "sf": sf, "ef": ef, "warp": round(w, 4),
            "dst0": round(d0, 3), "dst1": round(d1, 3), "out": out,
            "kind": kind, "_placed": placed, "_line": line}

# ---- donor pool: established non-vocal tails (take -> [start, end) frames)
DONOR = {
    "mv5_s16_t4": [[172, 240]], "mv5_s16_t3": [[186, 240]],
    "mv5_s16_t1": [[212, 240]], "mv5_s09_t1": [[180, 240]],
    "mv5_s01_t1": [[223, 240]], "mv5_s10_t1": [[219, 240]],
    "mv5_s20_t1": [[68, 120]], "mv5_s21_t1": [[194, 240]],
    "mv5_s28_t1": [[85, 120]], "mv5_s03_t1": [[115, 120]],
    "mv5_s02_t1": [[206, 216]], "mv5_s18_t1": [[196, 216]],
    "mv5_s19b_t1": [[100, 120]], "mv5_s17_t1": [[233, 240]],
    "mv5_s04_t1": [[204, 240]], "mv5_s08_t2": [[205, 240]],
    "mv5_s12_t1": [[207, 216]], "mv5_s06_t1": [[194, 212]],
}

def alloc_donor(n, avoid=()):
    """Take n frames from the donor pool (longest range first)."""
    if n <= 0:
        return None
    best = None
    for take, ranges in DONOR.items():
        if take in avoid:
            continue
        for i, (a, b) in enumerate(ranges):
            if b - a >= n and (best is None or (b - a) > best[2]):
                best = (take, i, b - a)
    if best is None:
        # largest available range, caller pads the rest via tpad
        for take, ranges in DONOR.items():
            if take in avoid:
                continue
            for i, (a, b) in enumerate(ranges):
                if best is None or (b - a) > best[2]:
                    best = (take, i, b - a)
        if best is None:
            return None
        take, i, _ = best
        a, b = DONOR[take][i]
        del DONOR[take][i]
        return {"take": take, "sf": a, "ef": b, "warp": 1.0,
                "out": b - a, "kind": "donor-tail"}
    take, i, _ = best
    a, b = DONOR[take][i]
    if b - a == n:
        del DONOR[take][i]
    else:
        DONOR[take][i] = [a + n, b]
    return {"take": take, "sf": a, "ef": a + n, "warp": 1.0,
            "out": n, "kind": "donor-tail"}

def tile_scene(sc, pieces, take_for_gaps=None):
    """Tile pieces to [bound_start, bound_end) exactly (v1 frame total).
    pieces: ordered line/cover pieces with dst0/dst1 (seconds, from fits or
    line spans) and out (frames). Fillers (1.0x) are inserted for gaps >1f;
    gaps of <=1f are absorbed by starting the next piece at the running
    position (noted). The tail filler absorbs the rounding residual so the
    scene total is exact. dst0/dst1 are recomputed from the running frame
    position (the assembler concatenates in order; dst is documentation)."""
    start, end = BOUNDS[SCENES.index(sc)], BOUNDS[SCENES.index(sc) + 1]
    target = TARGET[sc]
    out_pieces = []
    pos = start  # running dst position (seconds)

    def add(p):
        nonlocal pos
        if "_multi" in p:
            for q in p["_multi"]:
                add(q)
            return
        p = dict(p)
        p.pop("_placed", None)
        p.pop("_line", None)
        p.pop("_fit_src", None)
        p.pop("_fit", None)
        p["dst0"] = round(pos, 3)
        p["dst1"] = round(pos + p["out"] / FPS, 3)
        out_pieces.append(p)
        pos = p["dst1"]

    first = pieces[0]
    head_n = round((first["dst0"] - pos) * FPS)
    if head_n > 1:
        add(filler_for_head(sc, first, head_n))
    elif head_n < -1:
        NOTES.append((sc, first.get("_line", "?"),
                      f"head overlap {-head_n}f: fit dst0 {first['dst0']} "
                      f"is before scene start {start}; piece starts at scene start"))
    for i, p in enumerate(pieces):
        if i > 0:
            prev = pieces[i - 1]
            gap_n = round((p["dst0"] - prev["dst1"]) * FPS)
            if gap_n > 1:
                add(filler_between(sc, prev, p, gap_n))
            elif gap_n < -4:
                GAPS.append((sc, p.get("_line", "?"),
                             f"overlap {-gap_n}f with previous piece"))
            elif gap_n < -1:
                NOTES.append((sc, p.get("_line", "?"),
                              f"fit overlap {-gap_n}f with previous piece; "
                              f"piece starts at running position "
                              f"(shift <= {abs(gap_n)}f, <=0.17s)"))
        add(p)
    tail_n = target - sum(q["out"] for q in out_pieces)
    if tail_n > 0:
        add(filler_for_tail(sc, pieces[-1], tail_n))
    elif tail_n < 0:
        GAPS.append((sc, "tail", f"pieces overrun scene by {-tail_n}f"))
    tot = sum(q["out"] for q in out_pieces)
    assert tot == target, f"{sc}: pieces sum {tot} != target {target}"
    return out_pieces

def filler_for_head(sc, first, n):
    take = first["take"]
    sf = first["sf"]
    if sf >= n:
        return {"take": take, "sf": sf - n, "ef": sf, "warp": 1.0,
                "out": n, "kind": "gap"}
    if sf > 0:
        # use the available pre-word frames, pad the rest by freezing frame 0
        return {"take": take, "sf": 0, "ef": 1, "warp": 1.0,
                "out": n, "kind": "freeze-leader"}
    d = alloc_donor(n)
    if d:
        d["kind"] = "donor-tail"
        return d
    return {"take": take, "sf": 0, "ef": 1, "warp": 1.0,
            "out": n, "kind": "freeze-leader"}

def filler_between(sc, prev, nxt, n):
    # same take's inter-line frames first
    if prev["take"] == nxt["take"]:
        avail = nxt["sf"] - prev["ef"]
        if avail >= n:
            return {"take": prev["take"], "sf": prev["ef"],
                    "ef": prev["ef"] + n, "warp": 1.0, "out": n, "kind": "gap"}
        if avail > 0:
            base = {"take": prev["take"], "sf": prev["ef"],
                    "ef": nxt["sf"], "warp": 1.0, "out": avail, "kind": "gap"}
            rest = alloc_donor(n - avail)
            if rest:
                # two fillers; caller handles list — flatten by returning
                # a combined marker the caller splits (handled below)
                return {"_multi": [base, rest]}
            # tpad-clone the last frame for the shortfall (<=3f ideally)
            base["out"] = n
            return base
    d = alloc_donor(n)
    if d:
        return d
    # last resort: hold the previous piece's last frame
    return {"take": prev["take"], "sf": prev["ef"] - 1, "ef": prev["ef"],
            "warp": 1.0, "out": n, "kind": "freeze-gap"}

def filler_for_tail(sc, last, n):
    take = last["take"]
    # same take's remaining frames
    import subprocess
    # take frame counts are known from the probe; hardcode the map here
    TAKE_FRAMES = {"mv5_s05_t1": 216, "mv5_s06_t1": 240, "mv5_s06_t2": 120,
                   "mv5_s07_t1": 240, "mv5_s12_t1": 216, "mv5_s15_t1": 120,
                   "mv5_s21_t3": 240, "mv5_s21_t7": 120, "mv5_s26_t1": 192,
                   "mv5_s27_t1": 144, "mv5_s28_t1": 120, "mv5_s28_t3": 120}
    total_f = TAKE_FRAMES.get(take, 240)
    avail = total_f - last["ef"]
    if avail >= n:
        return {"take": take, "sf": last["ef"], "ef": last["ef"] + n,
                "warp": 1.0, "out": n, "kind": "tail"}
    parts = []
    if avail > 0:
        parts.append({"take": take, "sf": last["ef"], "ef": total_f,
                      "warp": 1.0, "out": avail, "kind": "tail"})
        n -= avail
    while n > 0:
        d = alloc_donor(n)
        if d is None:
            # tpad-clone last frame
            parts.append({"take": take, "sf": total_f - 1, "ef": total_f,
                          "warp": 1.0, "out": n, "kind": "freeze-tail"})
            break
        parts.append(d)
        n -= d["out"]
    if len(parts) == 1:
        return parts[0]
    return {"_multi": parts}

def flatten(pieces):
    out = []
    for p in pieces:
        if "_multi" in p:
            out.extend(p["_multi"])
        else:
            out.append(p)
    return out

def build_scene_fit_pieces(sc, take, lines, use_scene_fit=False,
                             overrides=None):
    """Per-line pieces from app word pairs (line fit, or scene fit).
    overrides: {line: (slope, intercept)} — explicit fit (e.g. scene slope
    with a first-word-anchored intercept)."""
    e = TAKES[sc]
    sf_fit = e.get("fit") or {}
    pieces = []
    for ln in lines:
        ws = words_of(sc, ln)
        if overrides and ln in overrides:
            b, a = overrides[ln]
            src = "override"
        elif use_scene_fit or len(ws) < 2:
            b, a = sf_fit["slope"], sf_fit["intercept"]
            src = "scene fit"
        else:
            b, a, rm, rx = ls_fit([(w["take_start"], w["song_start_v2"])
                                   for w in ws])
            src = "line fit"
        p = line_piece(take, sc, ln, b, a)
        p["_fit_src"] = src
        p["_fit"] = (round(b, 3), round(a, 2))
        pieces.append(p)
    return pieces

def retrim(piece, ef):
    """Shorten a line piece to end_frame ef (cuts a word tail, not onset)."""
    piece["ef"] = ef
    piece["out"] = round((ef - piece["sf"]) * piece["warp"])
    piece["dst1"] = round(piece["dst0"] + piece["out"] / FPS, 3)
    return piece

# ---------------- per-scene builders ----------------
PLACEMENT = {}   # scene -> line -> [(word, take_start, placed_song, song_start)]

def save_placement(sc, pieces):
    PLACEMENT.setdefault(sc, {})
    for p in pieces:
        if "_placed" in p:
            PLACEMENT[sc][p.get("_line", p["kind"])] = p["_placed"]

def manual(take, sf, ef, warp, dst0, kind, line=None, placed=None):
    out = round((ef - sf) * warp)
    p = {"take": take, "sf": sf, "ef": ef, "warp": round(warp, 4),
         "dst0": dst0, "dst1": round(dst0 + out / FPS, 3), "out": out,
         "kind": kind}
    if line:
        p["_line"] = line
    if placed is not None:
        p["_placed"] = placed
    return p

def build_S05():
    ps = build_scene_fit_pieces("S05", "mv5_s05_t1",
                                ["L06", "L07", "L08", "L09"])
    # L09: include the split "half-zipped." (extras half 8.0-8.3, zipped. 8.3-8.7)
    l09 = ps[3]
    l09["ef"] = 209
    l09["out"] = round((209 - l09["sf"]) * l09["warp"])
    l09["dst1"] = round(l09["dst0"] + l09["out"] / FPS, 3)
    save_placement("S05", ps)
    return tile_scene("S05", ps)

def build_S06():
    # L11's per-line fit (0.584) is illegal (<0.60): use the SCENE slope
    # (0.621) anchored on the first word (You 3.4 -> 43.2).
    sc_fit = TAKES["S06"]["fit"]
    anchor_a = 43.2 - sc_fit["slope"] * 3.4
    ps = build_scene_fit_pieces("S06", "mv5_s06_t1", ["L10", "L11"],
                                overrides={"L11": (sc_fit["slope"], anchor_a)})
    # L12 from s06_t2 (qc_v12): single 0.88x warp; take words Yeah 0.0-0.54,
    # they 0.76-0.98, already 0.98-1.44, understand 1.44-2.6.
    placed = [("Yeah", 0.0, 44.58, 44.8), ("they", 0.76, 45.25, 44.9),
              ("already", 0.98, 45.44, 45.4),
              ("understand", 1.44, 45.85, 45.8)]
    t2 = manual("mv5_s06_t2", 0, 62, 0.88, 44.58, "line-L12", "L12", placed)
    ps.append(t2)
    save_placement("S06", ps)
    return tile_scene("S06", ps)

def build_S07():
    ps = build_scene_fit_pieces("S07", "mv5_s07_t1", ["L13", "L14", "L16"])
    # Trim word tails so the pieces end at the next line's start (the
    # per-line fits overlap by 2-3f): L13 "time" cut 0.17s early, L14
    # "fade" cut 0.12s early — onsets unaffected, L16 lands on its fit.
    retrim(ps[0], 68)
    retrim(ps[1], 122)
    # L15 donor cover (closed mouth): s08_t2 tail 205-237 (32f), 51.46-52.80.
    DONOR["mv5_s08_t2"] = [[237, 240]]
    cover = manual("mv5_s08_t2", 205, 237, 1.0, 51.46, "cover-L15", "L15")
    ps2 = [ps[0], ps[1], cover, ps[2]]
    save_placement("S07", ps)
    return tile_scene("S07", ps2)

def build_S12():
    # Scene fit (0.67) for both lines: L43's per-line fit (0.40) is illegal.
    ps = build_scene_fit_pieces("S12", "mv5_s12_t1", ["L41", "L43"],
                                use_scene_fit=True)
    save_placement("S12", ps)
    return tile_scene("S12", ps)

def build_S15():
    # TWO ANCHORS (brief): head 0.3-2.5 -> 116.2-118.4 @1.0x;
    # held tail 2.5-4.3 -> 118.4-120.2 @1.0x (replays covers 119.5);
    # donor-tail s21_t3 198-223 to 121.3.
    head = manual("mv5_s15_t1", 7, 60, 1.0, 116.2, "line-L56-head", "L56",
                  [("And", 0.3, 116.2, 116.2), ("my", 0.6, 116.5, 116.3),
                   ("whole", 1.0, 116.9, 116.4), ("head", 1.8, 117.7, 116.5)])
    tail = manual("mv5_s15_t1", 60, 103, 1.0, 118.4, "line-L56-tail", "L56b",
                  [("replays", 2.5, 118.4, 119.5)])
    don = manual("mv5_s21_t3", 198, 224, 1.0, 120.2, "donor-tail", "tail")
    save_placement("S15", [head, tail])
    return tile_scene("S15", [head, tail, don])

def build_S21():
    # L82 cover: t8 closed-mouth tail 3.5-4.5s (84-108).
    # L83: t3 per-line, brief warp 0.79. L84 cover: t9 tail 3.5-4.58s (84-110).
    # L85: t3 per-line, brief warp 0.605 (grey). L86 cover: t10 quiet gap
    # 2.79-3.33s (67-80) + post-repeat tail 3.96-4.46s (95-107).
    # L87 donor: s21_t1 tail 194-217. L88: t7, v1-grid, warp 0.89.
    # L89 donor: s21_t1 218-240 + s16_t3 186-201.
    DONOR["mv5_s21_t1"] = []  # fully used: L87 194-218 + L89a 218-240
    DONOR["mv5_s16_t3"] = [[202, 240]]
    ps = [
        manual("mv5_s21_t8", 84, 109, 1.0, 158.06, "cover-L82", "L82"),
        manual("mv5_s21_t3", 48, 82, 0.79, 159.10, "line-L83", "L83",
               [("We", 2.0, 159.10, 159.4), ("don't", 2.2, 159.26, 159.4),
                ("fold", 2.5, 159.50, 159.5), ("in", 3.0, 159.89, 159.6)]),
        manual("mv5_s21_t9", 84, 111, 1.0, 160.24, "cover-L84", "L84"),
        manual("mv5_s21_t3", 120, 163, 0.605, 161.36, "line-L85", "L85",
               [("Let", 5.0, 161.36, 161.6), ("the", 5.2, 161.48, 161.7),
                ("whole", 5.4, 161.60, 161.7), ("thing", 5.9, 161.91, 162.0),
                ("spin", 6.2, 162.09, 162.2)]),
        manual("mv5_s21_t10", 67, 80, 1.0, 162.46, "cover-L86a", "L86"),
        manual("mv5_s21_t10", 95, 108, 1.0, 163.01, "cover-L86b", "L86"),
        manual("mv5_s21_t1", 194, 218, 1.0, 163.58, "donor-L87", "L87"),
        manual("mv5_s21_t7", 0, 36, 0.89, 164.58, "line-L88", "L88",
               [("Nothing", 0.0, 164.58, 165.2), ("to", 0.5, 165.03, 165.5),
                ("prove", 0.9, 165.38, 165.6)]),
        manual("mv5_s21_t1", 218, 240, 1.0, 165.91, "donor-L89a", "L89"),
        manual("mv5_s21_t3", 186, 201, 1.0, 166.83, "donor-L89b", "L89"),
    ]
    # fix L89b dst0: it follows L89a (165.91 + 23/24 = 166.87); recompute below
    save_placement("S21", ps)
    return tile_scene("S21", ps)

def build_S26():
    # Head donor (190.42-194.1, 88f): s16_t4 217-240 + s16_t5 175-191 +
    # s20_t1 68-117. L108 window (194.1-197.58, 83f): s26_t1 tail 144-191
    # (mouth closed @6.0s) + s04_t1 204-239.
    DONOR["mv5_s16_t4"] = []
    DONOR["mv5_s16_t5"] = []
    DONOR["mv5_s20_t1"] = [[118, 120]]
    DONOR["mv5_s04_t1"] = []
    ps = [
        manual("mv5_s16_t4", 217, 240, 1.0, 190.42, "donor-head", "head"),
        manual("mv5_s16_t5", 175, 191, 1.0, 191.38, "donor-head", "head"),
        manual("mv5_s20_t1", 68, 117, 1.0, 192.04, "donor-head", "head"),
        manual("mv5_s26_t1", 144, 192, 1.0, 194.10, "cover-L108-tail", "L108"),
        manual("mv5_s04_t1", 204, 240, 1.0, 196.06, "donor-L108", "L108"),
    ]
    return tile_scene("S26", ps)

def build_S27():
    # L109 s27_t1 head @1.0x (take 3.6-4.9 -> 197.58-198.91); tail fill
    # s27_t1 118-143 + donor s16_t3 202-225; L110a s28_t1 CAT Till
    # (take 0.1-3.1 -> 201.0-203.42, warp 0.80).
    DONOR["mv5_s16_t3"] = [[227, 240]]
    ps = [
        manual("mv5_s27_t1", 86, 118, 1.0, 197.58, "line-L109", "L109",
               [("Easy", 3.6, 197.58, 196.6), ("now", 4.2, 198.18, 196.7)]),
        manual("mv5_s27_t1", 118, 143, 1.0, 198.91, "tail-L109", "L109"),
        manual("mv5_s16_t3", 202, 227, 1.0, 199.96, "donor-tail", "L109"),
        manual("mv5_s28_t1", 2, 74, 0.80, 201.0, "line-L110a", "L110a",
               [("Till", 0.1, 201.0, 201.0), ("the", 0.6, 201.40, 201.1),
                ("morning", 0.8, 201.56, 201.1),
                ("comes", 2.1, 202.60, 201.3)]),
    ]
    save_placement("S27", ps)
    return tile_scene("S27", ps)

def build_S28():
    # Structural: s28_t3 closed-mouth tail 3.0-5.0s (72-120) + s28_t1 tail
    # 4.0-4.96s (96-119, post-"Till", mouth closed).
    ps = [
        manual("mv5_s28_t3", 72, 120, 1.0, 203.42, "cover-L110b-a", "L110b"),
        manual("mv5_s28_t1", 96, 120, 1.0, 205.42, "cover-L110b-b", "L110b"),
    ]
    DONOR["mv5_s28_t1"] = [[85, 96]]
    return tile_scene("S28", ps)

BUILDERS = {"S05": build_S05, "S06": build_S06, "S07": build_S07,
            "S12": build_S12, "S15": build_S15, "S21": build_S21,
            "S26": build_S26, "S27": build_S27, "S28": build_S28}

def main():
    # Build the manual (hardcoded-donor) scenes FIRST so their donor ranges
    # are removed from the pool before the fit scenes allocate from it.
    # The plan dict itself stays in scene order.
    order = ["S15", "S21", "S26", "S27", "S28", "S05", "S06", "S07", "S12"]
    plan = {}
    for sc in order:
        plan[sc] = BUILDERS[sc]()
    for sc in SCENES:
        if sc not in plan:
            plan[sc] = V1["plan"][sc]
    total = sum(p["out"] for sc in SCENES for p in plan[sc])
    print(f"TOTAL frames: {total} (target 4954)")
    assert total == 4954
    out = {"total_frames": 4954, "fps": 24, "bounds": BOUNDS,
           "scenes": SCENES, "plan": plan,
           "scores": V1["scores"], "donor_used": V1["donor_used"]}
    json.dump(out, open(os.path.join(PROJ, "work", "assembly_fit_mv5_v2.json"),
                        "w"), indent=1)
    print("wrote work/assembly_fit_mv5_v2.json")
    print()
    print("=== GAPS (illegal placements — must be resolved, not shipped) ===")
    for g in GAPS:
        print("  ", g)
    if not GAPS:
        print("   none")
    print()
    print("=== NOTES / disclosures ===")
    for n in NOTES:
        print("  ", n)
    print()
    print("=== changed-scene piece tables ===")
    for sc in BUILDERS:
        print(f"-- {sc} target={TARGET[sc]} sum={sum(p['out'] for p in plan[sc])}")
        for p in plan[sc]:
            print(f"   {p['kind']:16} {p['take']:14} sf={p['sf']:3} ef={p['ef']:3} "
                  f"w={p['warp']:.3f} out={p['out']:3} dst={p['dst0']:.2f}-{p['dst1']:.2f}")
    print()
    print("=== word placement (placed onset vs song start, seconds) ===")
    for sc, lines in PLACEMENT.items():
        for ln, ws in lines.items():
            errs = [f"{w}:{pl - s:+.2f}" for w, _, pl, s in ws]
            print(f"  {sc} {ln}: " + " ".join(errs))

if __name__ == "__main__":
    main()
