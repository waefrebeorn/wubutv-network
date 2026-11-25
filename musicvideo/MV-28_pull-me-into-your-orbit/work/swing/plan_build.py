#!/usr/bin/env python3
"""MV-28 assembly planner. Adapted from MV-27's plan_build.py.
 - Line song spans are the ADJUDICATED spans (LYRIC_TIMELINE.md +
   gap_analysis.txt): unmatched hooks L11/L25 and inferred L32/L34/L37
   carry their adjudicated spans; L24/L36 are doubled vocals sharing
   L23/L35 spans (no separate picture).
 - Singing lines matched to take ASR windows (p>=0.25) by content
   words; phrase-level chunk warps when take/song word counts agree,
   else whole-span warp. BAD-WORD rule is enforced upstream by QC:
   every matched take sings its lines exactly (s09_t1/s17_t1/s19_t1
   defective spans are cover pool only — their sung phrases never
   match a line's content, so the matcher cannot claim them).
 - S22 (L40) has NO take (lost in tool handoff): manual cover from
   non-claimed spans of s23_t1 + s21_t1 ONLY, pre-claimed before the
   scene loop so S21/S23 plan around them.
 - Fills: complement spans of the scene's own takes, cover stretch
   when the pool is short, donors from earlier scenes as last resort.
 - Final audit: no picture span used twice (claim ledger).
Output: work/swing/plan.json + review table. Frame-exact per scene,
target 5760 frames."""
import json, os, re, subprocess
from collections import Counter

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FPS = 24
scenes = json.load(open(os.path.join(P, "work/scenes.json")))

# (line_id, sheet text, song_start, song_end) — adjudicated spans
LINES = [
 ("L01","You set your glass beside the phone",30.64,34.06),
 ("L02","I take the long way past your door",34.06,37.48),
 ("L03","A little smile, a raised eyebrow",37.48,40.76),
 ("L04","We both know what we're waiting for",40.76,44.34),
 ("L05","Come a little closer, let the whole room turn",44.34,48.10),
 ("L06","Say it with your eyes and let me make you burn",48.10,51.12),
 ("L07","Pull me into your orbit",52.86,55.16),
 ("L08","Keep me right where the sparks begin",55.16,58.26),
 ("L09","Pull me into your orbit",59.62,62.20),
 ("L10","Let the night come rushing in",62.20,65.70),
 ("L11","Pull me into your orbit",68.84,71.10),
 ("L12","Don't let go until the morning",71.10,75.50),
 ("L13","Don't let go until the morning",75.50,79.02),
 ("L14","Your jacket's hanging on my chair",97.00,100.58),
 ("L15","My lipstick marks the porcelain",100.58,103.64),
 ("L16","You tell a story, lose your place",103.64,107.78),
 ("L17","I catch you looking once again",107.78,110.90),
 ("L18","Come a little closer, let the whole room turn",110.90,114.48),
 ("L19","Say it with your eyes and let me make you burn",114.48,117.52),
 ("L20","Pull me into your orbit",118.40,121.54),
 ("L21","Keep me right where the sparks begin",121.54,124.66),
 ("L22","Pull me into your orbit",126.18,128.48),
 ("L23","Let the night come rushing in",128.48,131.96),
 ("L25","Pull me into your orbit",135.04,137.86),
 ("L26","Don't let go until the morning",137.86,141.68),
 ("L27","Don't let go until the morning",141.68,145.20),
 ("L28","One step back, then you draw me near",176.18,179.42),
 ("L29","A quiet promise only I can hear",179.42,182.70),
 ("L30","Say it again, no need to hurry, no need to pretend",183.58,186.14),
 ("L31","I'll take the long way around again",186.14,190.70),
 ("L32","Pull me into your orbit",190.70,194.46),
 ("L33","Keep me right where the sparks begin",194.46,197.62),
 ("L34","Pull me into your orbit",197.62,201.26),
 ("L35","Let the night come rushing in",201.26,204.72),
 ("L37","Pull me into your orbit",207.74,210.42),
 ("L38","Don't let go until the morning",210.42,214.40),
 ("L39","Until the morning",215.96,217.96),
 ("L40","Pull me into your orbit",225.08,232.30),
]
SCENE_LINES = {
 3:["L01","L02"], 4:["L03","L04"], 5:["L05","L06"],
 6:["L07","L08","L09","L10"], 7:["L11","L12","L13"],
 9:["L14","L15"], 10:["L16","L17"], 11:["L18","L19"],
 12:["L20","L21","L22","L23"], 13:["L25","L26","L27"],
 17:["L28","L29","L30"], 18:["L31","L32"],
 19:["L33","L34","L35"], 20:["L37","L38"], 21:["L39"],
}
LINE_MAP = {lid:(txt,s,e) for lid,txt,s,e in LINES}
SCENE_TAKES = {
 1:["s01_t1","s01_t2"], 2:["s02_t1","s02_t2"], 3:["s03_t1"],
 4:["s04_t1"], 5:["s05_t1"], 6:["s06_t1","s06_t2"],
 7:["s07_t1","s07_t2"], 8:["s08_t1","s08_t2"],
 9:["s09_t2","s09_t1"], 10:["s10_t1"], 11:["s11_t1"],
 12:["s12_t1","s12_t2"], 13:["s13_t1","s13_t2"], 14:["s14_t1"],
 15:["s15_t1"], 16:["s16_t1"], 17:["s17_t2","s17_t1"],
 18:["s18_t1"], 19:["s19_t2","s19_t1"], 20:["s20_t1"],
 21:["s21_t1"], 23:["s23_t1"],
}
STEM_SCENE = {s: n for n, v in SCENE_TAKES.items() for s in v}
WORDLESS = {"s01_t1","s01_t2","s02_t1","s02_t2","s08_t1","s08_t2",
            "s14_t1","s15_t1","s16_t1","s23_t1"}
MISHEAR = {"needs":"need","oven":"orbit"}
STOP = {"the","a","an","and"}
def norm(w):
    w = re.sub(r"[^a-z]","", w.lower().strip())
    return MISHEAR.get(w, w)
def content_of(text):
    return [t for t in (norm(w) for w in re.split(r"[\s,]+", text))
            if t and t not in STOP]

def take_words(stem, min_p):
    path = os.path.join(P, "work/qc", "mv28_" + stem + "_asr.json")
    if not os.path.exists(path): return []
    d = json.load(open(path))
    ws = []
    for seg in d["segments"]:
        for w in seg["words"]:
            if w.get("p", 0) < min_p: continue
            ws.append({"w": norm(w["w"]), "s": w["s"], "e": w["e"]})
    return ws
def take_dur(stem):
    f = os.path.join(P, "takes", f"mv28_{stem}.mp4")
    return float(subprocess.run(["ffprobe","-v","error","-show_entries",
        "format=duration","-of","csv=p=0", f], capture_output=True, text=True).stdout.strip())

ALL_STEMS = sorted({s for v in SCENE_TAKES.values() for s in v} | {"s21_t1","s23_t1"})
WORDS = {s: take_words(s, 0.25) for s in ALL_STEMS}
WORDS_ALL = {s: take_words(s, 0.0) for s in ALL_STEMS}
DURS = {s: take_dur(s) for s in ALL_STEMS}
SONG = [{"w": norm(w["word"]), "s": w["start"], "e": w["end"]}
        for w in json.load(open(os.path.join(P, "SONG_WORDS.json")))]

used = {}
def span_free(stem, a, b):
    return all(not (a < y - 0.15 and x + 0.15 < b) for (x, y) in used.get(stem, []))
def claim(stem, a, b): used.setdefault(stem, []).append((a, b))
def first_free(stem, a, b, need):
    cur = a
    for (x, y) in sorted(used.get(stem, [])):
        if y - 0.15 <= cur: continue
        if cur + need <= min(b, x + 0.15): return cur
        cur = max(cur, y - 0.15)
    return cur if cur + need <= b + 0.02 else None

def phrases_of(stem):
    ws = WORDS_ALL[stem]
    if not ws: return []
    phr, cur = [], [ws[0]]
    for w in ws[1:]:
        if w["s"] - cur[-1]["e"] > 0.7: phr.append(cur); cur = []
        cur.append(w)
    phr.append(cur)
    return [{"start": c[0]["s"], "end": c[-1]["e"],
             "sig": content_of(" ".join(w["w"] for w in c))} for c in phr]
PHRASES = {s: phrases_of(s) for s in ALL_STEMS}

def find_window(ws, i0, line_text, next_first=None):
    want = Counter(content_of(line_text))
    if not want: return None
    first = content_of(line_text)[0]
    last = content_of(line_text)[-1]
    need = sum(want.values())
    thresh = max(1, round(0.75 * need))
    for i in range(i0, len(ws)):
        if ws[i]["w"] != first: continue
        have = Counter(); j = i; fallback = None
        while j < len(ws) and j - i < need + 7:
            t = ws[j]["w"]
            if t not in STOP: have[t] += 1
            j += 1
            cov = sum((want & have).values())
            if cov >= thresh and have.get(last, 0) >= want[last]:
                return (i, j)
            if fallback is None and cov >= thresh and j < len(ws) and ws[j]["w"] == next_first:
                fallback = (i, j)
        if fallback: return fallback
    return None

def match_take_line(ptr, stems, line_text, next_first=None):
    for stem in stems:
        if stem in WORDLESS: continue
        ws = WORDS[stem]
        r = find_window(ws, ptr[stem], line_text, next_first)
        if r:
            ptr[stem] = r[1]
            return {"take": stem, "i": r[0], "j": r[1]}
    return None

def cover_candidates(stems, scene_n, repeat_sig=None, donors=False):
    repeat_sigs = []
    if repeat_sig is not None:
        repeat_sigs = repeat_sig if isinstance(repeat_sig, list) else [repeat_sig]
    out = []
    if donors:
        src = [s for s in ALL_STEMS if STEM_SCENE[s] < scene_n]
    else:
        src = stems
    for stem in src:
        dur = DURS[stem]
        if stem in WORDLESS:
            out.append((stem, 0.0, dur)); continue
        prev = 0.0
        for ph in sorted(PHRASES[stem], key=lambda z: z["start"]):
            if ph["start"] - prev > 0.25: out.append((stem, prev, ph["start"]))
            prev = max(prev, ph["end"])
        if dur - prev > 0.25: out.append((stem, prev, dur))
        for ph in PHRASES[stem]:
            if not ph["sig"]: out.append((stem, ph["start"], ph["end"]))
            elif any(Counter(ph["sig"]) == Counter(rs) for rs in repeat_sigs):
                out.append((stem, ph["start"], ph["end"]))
    return out

plan, warnings, matchlog = [], [], []
def add(scene, stem, kind, ts, k, o0, o1):
    plan.append({"scene": scene, "take": f"mv28_{stem}.mp4", "kind": kind,
                 "take_start": round(ts, 3), "k": round(k, 4),
                 "out": [round(o0, 4), round(o1, 4)]})
    return plan[-1]

def fill(scene, stems, o0, o1, k_cover=1.0, repeat_sig=None, slot=False):
    rem = o1 - o0; placed_any = []
    def try_cands(cands):
        nonlocal rem
        while rem > 0.03:
            placed = False
            for (stem, a, b) in cands:
                avail = b - a
                if avail < 0.2: continue
                base = min(rem / k_cover, avail)
                if base < 0.2: continue
                st = None
                for frac in (1.0, 0.6, 0.35, 0.22):
                    take_len = base * frac
                    if take_len < 0.18: continue
                    st = first_free(stem, a, b, take_len)
                    if st is not None: break
                if st is None: continue
                seg = add(scene, stem, "C", st, k_cover, o1 - rem, o1 - rem + take_len * k_cover)
                claim(stem, st, st + take_len)
                placed_any.append((seg, take_len))
                rem -= take_len * k_cover; placed = True; break
            if not placed: break
    def try_stretch():
        nonlocal rem
        if rem <= 0.03 or not placed_any: return
        seg, take_len = placed_any[-1]
        new_out = (seg["out"][1] - seg["out"][0]) + rem
        new_k = new_out / take_len
        if new_k <= 1.85:
            seg["out"][1] = round(o1, 4); seg["k"] = round(new_k, 4)
            warnings.append(f"S{scene} fill stretch k={new_k:.2f} on {seg['take']}")
            rem = 0
    try_cands(cover_candidates(stems, scene, None if slot else repeat_sig))
    try_stretch()
    if rem > 0.03:
        if scene in DONOR_OVERRIDE:
            dstems = DONOR_OVERRIDE[scene]
            if dstems:
                try_cands(cover_candidates(dstems, scene, donors=False))
                try_stretch()
        else:
            try_cands(cover_candidates(stems, scene, donors=True))
            try_stretch()
    if rem > 0.03:
        warnings.append(f"S{scene} fill {o0:.2f}-{o1:.2f} SHORT by {rem:.2f}s")
        return False
    return True

# --- S22 manual cover (L40 lost take): pre-claim dawn spans ----------
# Outro pool arithmetic (dawn takes s21_t1 + s23_t1 = 20s for 25.58s of
# outro output): S21 fill takes ~1.25s of s23 as donor, S22 takes
# s23[1.57-4.68] + s21[7.5-10] at uniform k=1.478, S23 keeps
# s23[4.68-10] = 5.32s at k=1.45 for its own 7.71s window.
K22 = (232.29 - 224.00) / (3.11 + 2.5)
add(22, "s23_t1", "C", 1.57, K22, 224.00, 224.00 + 3.11 * K22)
claim("s23_t1", 1.57, 4.68)
add(22, "s21_t1", "C", 7.5, K22, 224.00 + 3.11 * K22, 232.29)
claim("s21_t1", 7.5, 10.0)
matchlog.append("S22 L40 <- MANUAL COVER s23_t1[1.57-4.68] + s21_t1[7.5-10] (take lost)")
DONOR_OVERRIDE = {21: ["s23_t1"], 23: []}

for sc in scenes:
    n = sc["n"]; w0, w1 = sc["win"]; tag = sc["tag"]
    if n == 22: continue
    stems = SCENE_TAKES[n]
    if tag == "CUTAWAY":
        pool = sum(DURS[s] - sum(b - a for (a, b) in used.get(s, [])) for s in stems)
        k_cover = 1.0
        if (w1 - w0) > pool > 0:
            k_cover = min(1.45, (w1 - w0) / pool)
            warnings.append(f"S{n} cutaway cover stretch x{k_cover:.2f}")
        fill(n, stems, w0, w1, k_cover)
        continue
    ptr = {s: 0 for s in stems}
    lines = [(lid, LINE_MAP[lid][0], LINE_MAP[lid][1], LINE_MAP[lid][2])
             for lid in SCENE_LINES[n]]
    matched, spans = {}, {}
    for li, (lid, txt, ls, le) in enumerate(lines):
        spans[lid] = (ls, le)
        nf = content_of(lines[li + 1][1])[0] if li + 1 < len(lines) and content_of(lines[li + 1][1]) else None
        m = match_take_line(ptr, stems, txt, next_first=nf)
        if m:
            matched[lid] = m
            tw = WORDS[m["take"]]
            claim(m["take"], tw[m["i"]]["s"], tw[m["j"] - 1]["e"])
            matchlog.append(f"S{n} {lid} <- {m['take']} "
                            f"[{tw[m['i']]['s']:.2f}-{tw[m['j']-1]['e']:.2f}] "
                            f"'{' '.join(w['w'] for w in tw[m['i']:m['j']])}'")
        else:
            warnings.append(f"S{n} {lid} '{txt}' UNMATCHED")
    # cover stretch estimate
    vocal_len, pool_len = 0.0, 0.0
    for lid, txt, ls, le in lines:
        if lid in matched:
            vocal_len += spans[lid][1] - spans[lid][0]
    for stem in stems: pool_len += DURS[stem]
    pool_len -= sum(sum(b - a for (a, b) in used.get(stem, [])) for stem in stems)
    need_cover = (w1 - w0) - vocal_len
    k_cover = 1.0
    if need_cover > pool_len > 0:
        k_cover = min(1.45, need_cover / pool_len)
        if k_cover > 1.02:
            warnings.append(f"S{n} cover stretch x{k_cover:.2f} (pool {pool_len:.1f}s < need {need_cover:.1f}s)")
    scene_sigs = [content_of(txt) for lid, txt, ls, le in lines]
    cur = w0
    for lid, txt, ls, le in lines:
        s0, s1 = spans[lid]
        if lid in matched:
            mm = matched[lid]; tw = WORDS[mm["take"]]
            twords = tw[mm["i"]:mm["j"]]
            tstart, tend = twords[0]["s"], twords[-1]["e"]
            swords = [w for w in SONG if w["s"] >= s0 - 0.3 and w["e"] <= s1 + 0.3]
            segs = []
            if len(swords) == len(twords) and len(swords) > 1:
                cuts = [0]
                for a in range(1, len(swords)):
                    if swords[a]["s"] - swords[a-1]["e"] > 0.8 or twords[a]["s"] - twords[a-1]["e"] > 0.8:
                        cuts.append(a)
                cuts.append(len(swords))
                for c in range(len(cuts) - 1):
                    a0, a1 = cuts[c], cuts[c + 1]
                    sw0, sw1 = swords[a0]["s"], swords[a1 - 1]["e"]
                    tw0, tw1 = twords[a0]["s"], twords[a1 - 1]["e"]
                    segs.append((mm["take"], tw0, (sw1 - sw0) / (tw1 - tw0), sw0, sw1))
                    if a1 < len(swords):
                        gw_s = swords[a1]["s"] - sw1; gw_t = twords[a1]["s"] - tw1
                        if gw_s > 0.05 and gw_t >= 0.1:
                            segs.append((mm["take"], tw1, gw_s / gw_t, sw1, swords[a1]["s"]))
                        elif gw_s > 0.05:
                            segs.append((None, 0, 1.0, sw1, swords[a1]["s"]))
                for (_, _, kk, _, _) in segs:
                    if kk and not (0.6 <= kk <= 1.7):
                        warnings.append(f"S{n} {lid} chunk warp k={kk:.2f}")
            else:
                k = (s1 - s0) / (tend - tstart)
                segs.append((mm["take"], tstart, k, s0, s1))
                if not (0.6 <= k <= 1.7):
                    warnings.append(f"S{n} {lid} warp k={k:.2f}")
            if segs and segs[0][3] > cur + 0.02:
                fill(n, stems, cur, segs[0][3], k_cover, repeat_sig=scene_sigs)
            first = True
            for (stem, ts, k, bo0, bo1) in segs:
                if stem is None:
                    fill(n, stems, bo0, bo1, k_cover, repeat_sig=scene_sigs)
                else:
                    if first and bo0 < cur - 0.02:
                        ts = ts + (cur - bo0) / k; bo0 = cur
                    add(n, stem, "W", ts, k, bo0, bo1)
                first = False
            cur = max(cur, min(s1, segs[-1][4]) if segs else s1)
        else:
            if s0 > cur + 0.02: fill(n, stems, cur, s0, k_cover, repeat_sig=scene_sigs)
            fill(n, stems, s0, s1, k_cover, slot=True)
            cur = max(cur, s1)
    if cur < w1 - 0.02: fill(n, stems, cur, w1, k_cover, repeat_sig=scene_sigs)

# micro-gap closure (<=0.3s)
plan.sort(key=lambda z: z["out"][0])
for idx in range(1, len(plan)):
    prev, cur = plan[idx - 1], plan[idx]
    gap = cur["out"][0] - prev["out"][1]
    if 0 < gap <= 0.3 and prev["scene"] == cur["scene"]:
        take_len = (prev["out"][1] - prev["out"][0]) / prev["k"]
        prev["out"][1] = cur["out"][0]
        prev["k"] = round((prev["out"][1] - prev["out"][0]) / take_len, 4)
for sc in scenes:
    items = [p for p in plan if p["scene"] == sc["n"]]
    if items:
        last = max(items, key=lambda z: z["out"][1])
        gap = sc["win"][1] - last["out"][1]
        if 0 < gap <= 0.3:
            take_len = (last["out"][1] - last["out"][0]) / last["k"]
            last["out"][1] = sc["win"][1]
            last["k"] = round((last["out"][1] - last["out"][0]) / take_len, 4)

# hole check + frame partition
final = []
for sc in scenes:
    n = sc["n"]; f0, f1 = sc["frames"]
    items = sorted([p for p in plan if p["scene"] == n], key=lambda z: z["out"][0])
    t = sc["win"][0]
    for it in items:
        if it["out"][0] > t + 0.05: warnings.append(f"S{n} HOLE {t:.2f}-{it['out'][0]:.2f}")
        t = max(t, it["out"][1])
    if t < sc["win"][1] - 0.05: warnings.append(f"S{n} TAIL HOLE {t:.2f}-{sc['win'][1]:.2f}")
    bounds = [f0] + [round(it["out"][1] * FPS) for it in items]
    bounds[-1] = f1
    rows = []
    for i, it in enumerate(items):
        if bounds[i + 1] - bounds[i] < 3 and rows:
            rows[-1]["frames"][1] = bounds[i + 1]
            rows[-1]["out"][1] = it["out"][1]
            continue
        it["frames"] = [bounds[i], bounds[i + 1]]
        rows.append(it)
    if rows: rows[-1]["frames"][1] = f1
    final.extend(rows)
total = sum(r["frames"][1] - r["frames"][0] for r in final)
audit_bad = []
for stem, ivs in used.items():
    ivs = sorted(ivs)
    for a in range(1, len(ivs)):
        if ivs[a][0] < ivs[a - 1][1] - 0.15:
            audit_bad.append(f"{stem} {ivs[a-1]} x {ivs[a]}")
print(f"segments: {len(final)}  total frames: {total} (target 5760)")
for ml in matchlog: print("MATCH:", ml)
for w in warnings: print("WARN:", w)
for b in audit_bad: print("AUDIT-OVERLAP:", b)
json.dump(final, open(os.path.join(P, "work/swing/plan.json"), "w"), indent=1)
for r in final:
    print(f"S{r['scene']:02d} {r['kind']} {r['take'][5:12]} ts={r['take_start']:6.2f} "
          f"k={r['k']:.3f} out {r['out'][0]:7.2f}-{r['out'][1]:7.2f} f{r['frames'][0]}-{r['frames'][1]}")
