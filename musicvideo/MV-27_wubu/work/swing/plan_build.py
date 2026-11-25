#!/usr/bin/env python3
"""MV-27 assembly planner v4.
 - Word streams: song (SONG_WORDS.json) + takes (work/qc/*_asr.json).
   Singing matching uses p>=0.25 words; chant matching uses all words.
 - Line->take windows anchored on the first content token, shortest
   window reaching >=88% content coverage, extended over adjacent
   name tokens (the chant prefix is part of the performance).
 - SINGING: vocal blocks = song word spans, chunk-tiled warps
   (chunks split at >0.8s gaps in either stream; inter-chunk gaps
   warped by their own k or cover-filled when the take gap ~0).
 - CHANT/MIXED: natural placement on timeline/inferred onsets.
 - Fills: cover sub-cuts (complements, name-only phrases, same-line
   repeats in gaps), even per-scene cover-stretch when the pool is
   short, last-resort stretch <=1.85x, donors ONLY from earlier
   scenes' takes (claims final) — never future scenes' material.
 - Micro-gaps <=0.3s closed by stretching the previous segment.
 - Final audit: no picture span used twice (claim ledger).
Output: work/swing/plan.json + review table. Frame-exact per scene.
"""
import json, os, re, subprocess
from collections import Counter

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FPS = 24
scenes = json.load(open(os.path.join(P, "work/scenes.json")))

LINES = [
 ("L01","WuBu WuBu",None,None), ("L02","Let's go",6.34,8.00),
 ("L03","WuBu WuBu, say the name",None,None), ("L04","WuBu WuBu, in the game",None,None),
 ("L05","Clip it up, clip it up",None,None), ("L06","More and more, never stop",22.74,27.32),
 ("L07","Let's go",47.86,48.98),
 ("L08","Long nights I stay on the line",48.98,51.98), ("L09","Pay the rent, keep the lights on mine",51.98,55.88),
 ("L10","Work till the moon is bright in the sky",55.88,59.52),
 ("L11","Then I take my two days and I go live",59.52,63.90), ("L12","Tired eyes but I keep the promise",64.50,66.68),
 ("L13","I keep moving, I keep it honest",66.68,68.54),
 ("L14","Bills on the desk and a dream in my hand",None,None), ("L15","WuBu makes the way, does what he can",None,None),
 ("L16","When the week gets heavy",72.26,73.70), ("L17","I hear my people call",74.22,76.02),
 ("L18","When the week gets heavy",76.02,77.46), ("L19","I give my all",77.58,80.32),
 ("L20","WuBu WuBu, say the name",None,None), ("L21","WuBu WuBu, in the game",None,None),
 ("L22","Clip it up, clip it up",None,None), ("L23","More and more, never stop",85.50,87.12),
 ("L24","WuBu WuBu, hear it loud",None,None), ("L25","WaefreBeorn, say it proud",None,None),
 ("L26","WuBu WuBu, keep it going",None,None), ("L27","WuBu WuBu, keep it growing",99.06,103.40),
 ("L28","Couple days free, I stream for the crew",109.84,112.44), ("L29","Not the usual crowd, but I still see you",112.44,116.30),
 ("L30","Warehouse shows to the underground night",116.30,118.50),
 ("L31","Old tapes in the box, the signal stays tight",118.50,122.02), ("L32","I send it out where the echoes go",122.02,123.68),
 ("L33","Backroom glow and the world should know",123.68,125.62), ("L34","Audience rare, audience true",125.62,127.36),
 ("L35","Every face means something to WuBu too",127.36,129.44),
 ("L36","When the backlog grows",129.44,130.18), ("L37","I keep the fire on",131.00,132.94),
 ("L38","When the backlog grows",132.94,134.02), ("L39","We move it on",135.26,136.90),
 ("L40","WuBu WuBu, say the name",None,None), ("L41","WuBu WuBu, in the game",None,None),
 ("L42","Clip it up, clip it up",None,None), ("L43","More and more, never stop",142.86,144.50),
 ("L44","WuBu WuBu, hear it loud",None,None), ("L45","WaefreBeorn, say it proud",None,None),
 ("L46","WuBu WuBu, keep it going",None,None), ("L47","WuBu WuBu, keep it growing",None,None),
 ("L48","WuBu WuBu",None,None), ("L49","Say the name",170.04,171.46),
 ("L50","Keep it going",173.90,175.30), ("L51","Keep it growing",177.72,178.62),
 ("L52","Say the name",187.86,189.64),
 ("L53","Keep it going",199.20,201.14), ("L54","Keep it growing",201.14,202.54),
 ("L55","Say the name",None,None), ("L56","Keep it going",None,None), ("L57","Keep it growing",None,None),
 ("L58","WuBu",None,None), ("L59","WuBu",None,None),
 ("L60","WuBu WuBu, say the name",None,None), ("L61","WuBu WuBu, in the game",None,None),
 ("L62","Clip it up, clip it up",None,None), ("L63","More and more, never stop",None,None),
 ("L64","WuBu WuBu, hear it loud",None,None), ("L65","WaefreBeorn, say it proud",None,None),
 ("L66","WuBu WuBu, keep it going",None,None), ("L67","WuBu WuBu, keep it growing",None,None),
 ("L68","One more time",204.76,207.04), ("L69","WuBu WuBu",None,None),
 ("L70","Stay with me",208.62,210.86), ("L71","New things coming, wait and see",210.86,214.44),
 ("L72","WuBu WuBu",246.16,248.36), ("L73","WuBu WuBu",None,None),
]
SCENE_LINES = {
 1:["L01","L02"], 2:["L03","L04","L05"], 3:["L06"], 4:["L07"],
 5:["L08","L09","L10"], 6:["L11","L12","L13"], 7:["L14","L15"],
 8:["L16","L17","L18","L19"], 9:["L20","L21","L22","L23"],
 10:["L24","L25","L26"], 11:["L27"], 12:["L28","L29","L30"],
 13:["L31","L32","L33","L34","L35"], 14:["L36","L37","L38","L39"],
 15:["L40","L41","L42","L43","L44","L45","L46","L47"],
 16:["C16a","C16b","C16c"],
 17:["L48","L49","L50","L51"], 18:["L52","L52b","L52c","L52d"],
 19:["L53","L54","L55","L56","L57","L58","L59"],
 20:["L68","L69","L70","L71"], 21:["L60","L61","L62","L63"],
 22:["L64","L65","L66","L67","L67b"], 23:["L72","L73"],
}
LINE_MAP = {lid:(txt,s,e) for lid,txt,s,e in LINES}
LINE_MAP.update({
 "C16a":("Keep it going",158.30,160.70), "C16b":("Keep it growing",163.02,164.10),
 "C16c":("Keep it growing",166.90,167.96),
 "L52b":("WuBu WuBu, in the game",None,None), "L52c":("Clip it up, clip it up",None,None),
 "L52d":("More and more, never stop",None,None), "L67b":("WuBu WuBu",None,None)})
SCENE_TAKES = {
 1:["s01_t1"], 2:["s02_t1","s02_t2"], 3:["s03_t1"], 4:["s04_t1","s04_t2"],
 5:["s05_t1"], 6:["s06c_t1"], 7:["s07_t1"], 8:["s08_t1"],
 9:["s09_t1"], 10:["s10_t1"], 11:["s11_t1"], 12:["s12_t1"],
 13:["s13_t1","s13_t2"], 14:["s14_t1"], 15:["s15_t1","s15_t2","s15c_t1"],
 16:["s16_t1","s16_t2"], 17:["s17_t1"], 18:["s18_t1","s18_t2"],
 19:["s19_t1"], 20:["s20_t1"], 21:["s21_t1","s21_t2"],
 22:["s22_t1","s22_t2"], 23:["s23_t1"],
}
STEM_SCENE = {s: n for n, v in SCENE_TAKES.items() for s in v}
WORDLESS = {"s04_t1","s06c_t1","s18_t1"}
NAME_TOK = {"wubu","waefrebeorn","woo","boo","wooboo","woobo","wubuu","wabu",
            "wup","wu","bu","wo","oh","whoa","waif","wayfra","bayorn","bayon",
            "wudu","wubub","bub","wupawupa","wupa","wupawup","wuuboo","wubo","wubbu"}
MISHEAR = {"days":"nights","feels":"bills","blow":"glow",
           "click":"clip","live":"clip","glimmin":"clip","log":"backlog",
           "rolls":"grows","real":"rare"}
STOP = {"the","a","an","and"}
def norm(w):
    w = re.sub(r"[^a-z]","", w.lower().strip())
    return MISHEAR.get(w, w)
def content_of(text):
    return [t for t in (norm(w) for w in re.split(r"[\s,]+", text))
            if t and t not in NAME_TOK and t not in STOP
            and not re.fullmatch(r"(a+h+|o+h+|u+h+)", t)]

def take_words(stem, min_p):
    path = os.path.join(P, "work/qc", stem + "_asr.json")
    if not os.path.exists(path): return []
    d = json.load(open(path))
    ws = []
    for seg in d["segments"]:
        for w in seg["words"]:
            if w.get("p", 0) < min_p: continue
            ws.append({"w": norm(w["w"]), "s": w["s"], "e": w["e"]})
    return ws
def take_dur(stem):
    f = os.path.join(P, "takes", f"mv27_{stem}.mp4")
    return float(subprocess.run(["ffprobe","-v","error","-show_entries",
        "format=duration","-of","csv=p=0", f], capture_output=True, text=True).stdout.strip())

ALL_STEMS = sorted({s for v in SCENE_TAKES.values() for s in v})
WORDS = {s: take_words(s, 0.25) for s in ALL_STEMS}       # singing-grade
WORDS_ALL = {s: take_words(s, 0.0) for s in ALL_STEMS}    # chant-grade
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
        have = Counter(); j = i
        while j < len(ws) and j - i < need + 7:
            t = ws[j]["w"]
            if t not in NAME_TOK and t not in STOP: have[t] += 1
            j += 1
            cov = sum((want & have).values())
            if cov >= thresh and have.get(last, 0) >= want[last]:
                break
            if cov >= thresh and j < len(ws) and ws[j]["w"] == next_first:
                break
        else:
            continue
        if sum((want & have).values()) < thresh: continue
        a = i
        while a > i0 and ws[a - 1]["w"] in NAME_TOK and ws[a]["s"] - ws[a - 1]["e"] < 0.6 and i - a < 4: a -= 1
        b = j
        while b < len(ws) and ws[b]["w"] in NAME_TOK and ws[b]["s"] - ws[b - 1]["e"] < 0.6 and b - j < 2: b += 1
        return (a, b)
    return None

def match_take_line(ptr, stems, line_text, chant=False, next_first=None):
    want = content_of(line_text)
    src = WORDS_ALL if chant else WORDS
    for stem in stems:
        if stem in WORDLESS: continue
        ws = src[stem]
        if not want:
            i = ptr[stem]
            while i < len(ws):
                if ws[i]["w"] in NAME_TOK:
                    j = i
                    while j + 1 < len(ws) and ws[j + 1]["w"] in NAME_TOK and ws[j + 1]["s"] - ws[j]["e"] < 1.2 and j - i < 3: j += 1
                    ptr[stem] = j + 1
                    return {"take": stem, "i": i, "j": j + 1}
                i += 1
            continue
        r = find_window(ws, ptr[stem], line_text, next_first)
        if r:
            ptr[stem] = r[1]
            return {"take": stem, "i": r[0], "j": r[1]}
    if not want:
        for stem in stems:
            if stem in WORDLESS: continue
            ws = src[stem]
            for i, w in enumerate(ws):
                if w["w"] in NAME_TOK and span_free(stem, w["s"], w["e"]):
                    j = i
                    while j + 1 < len(ws) and ws[j + 1]["w"] in NAME_TOK and ws[j + 1]["s"] - ws[j]["e"] < 1.2 and j - i < 3: j += 1
                    if span_free(stem, ws[i]["s"], ws[j]["e"]):
                        return {"take": stem, "i": i, "j": j + 1}
    return None

def song_window(ptr, line_text, lo, hi, next_first=None):
    want = content_of(line_text)
    if not want: return None
    first = want[0]; last = want[-1]
    wantc = Counter(want); need = sum(wantc.values())
    thresh = max(1, round(0.75 * need))
    ws = SONG
    for i in range(ptr[0], len(ws)):
        if ws[i]["w"] != first or ws[i]["s"] < lo - 0.5 or ws[i]["s"] > hi + 0.5: continue
        have = Counter(); j = i
        while j < len(ws) and j - i < need + 7:
            t = ws[j]["w"]
            if t not in NAME_TOK and t not in STOP: have[t] += 1
            j += 1
            cov = sum((wantc & have).values())
            if cov >= thresh and have.get(last, 0) >= wantc[last]:
                break
            if cov >= thresh and j < len(ws) and ws[j]["w"] == next_first:
                break
        else:
            continue
        if sum((wantc & have).values()) < thresh: continue
        ptr[0] = j
        return (ws[i]["s"], ws[j - 1]["e"], i, j)
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
    plan.append({"scene": scene, "take": f"mv27_{stem}.mp4", "kind": kind,
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
        try_cands(cover_candidates(stems, scene, donors=True))
        try_stretch()
    if rem > 0.03:
        warnings.append(f"S{scene} fill {o0:.2f}-{o1:.2f} SHORT by {rem:.2f}s")
        return False
    return True

for sc in scenes:
    n = sc["n"]; w0, w1 = sc["win"]; tag = sc["tag"]
    chant = tag != "SINGING"
    stems = SCENE_TAKES[n]
    ptr = {s: 0 for s in stems}
    sptr = [0]
    lines = [(lid, LINE_MAP[lid][0], LINE_MAP[lid][1], LINE_MAP[lid][2])
             for lid in SCENE_LINES[n]]
    matched, songspans = {}, {}
    for li, (lid, txt, ls, le) in enumerate(lines):
        nf = content_of(lines[li + 1][1])[0] if li + 1 < len(lines) and content_of(lines[li + 1][1]) else None
        m = match_take_line(ptr, stems, txt, chant=chant, next_first=nf)
        if m:
            matched[lid] = m
            tw = (WORDS_ALL if chant else WORDS)[m["take"]]
            claim(m["take"], tw[m["i"]]["s"], tw[m["j"] - 1]["e"])
            matchlog.append(f"S{n} {lid} <- {m['take']} "
                            f"[{tw[m['i']]['s']:.2f}-{tw[m['j']-1]['e']:.2f}] "
                            f"'{' '.join(w['w'] for w in tw[m['i']:m['j']])}'")
        elif n != 6: warnings.append(f"S{n} {lid} '{txt}' UNMATCHED")
        if tag == "SINGING" and ls is not None:
            sw = song_window(sptr, txt, ls, le, next_first=nf)
            if sw: songspans[lid] = sw
    # infer unanchored spans
    spans = {}; seq = [(lid, ls, le) for lid, txt, ls, le in lines]
    i = 0; cursor = w0
    while i < len(seq):
        lid, ls, le = seq[i]
        if ls is not None:
            spans[lid] = (ls, le); cursor = le; i += 1
        else:
            j = i
            while j < len(seq) and seq[j][1] is None: j += 1
            nxt = seq[j][1] if j < len(seq) else w1
            group = seq[i:j]
            ws = []
            for (gid, _, _) in group:
                if gid in matched:
                    mm = matched[gid]; tw = (WORDS_ALL if chant else WORDS)[mm["take"]]
                    ws.append(max(0.8, tw[mm["j"] - 1]["e"] - tw[mm["i"]]["s"]))
                else: ws.append(1.4)
            # degenerate block (anchor sits at the cursor): borrow time
            # from the following anchored line's span, weighted together
            if j < len(seq) and nxt - cursor < 0.6 * sum(ws):
                aid, als, ale = seq[j]
                aw = 1.4
                if aid in matched:
                    mm = matched[aid]; tw = (WORDS_ALL if chant else WORDS)[mm["take"]]
                    aw = max(0.8, tw[mm["j"] - 1]["e"] - tw[mm["i"]]["s"])
                group = group + [seq[j]]; ws = ws + [aw]
                nxt = ale; j += 1
            tot = sum(ws); t = cursor
            for (gid, _, _), wt in zip(group, ws):
                d = (nxt - cursor) * wt / tot
                spans[gid] = (t, t + d); t += d
            cursor = nxt; i = j
    # cover stretch estimate
    vocal_len, pool_len = 0.0, 0.0
    for lid, txt, ls, le in lines:
        if lid in matched:
            mm = matched[lid]; tw = (WORDS_ALL if chant else WORDS)[mm["take"]]
            vocal_len += (tw[mm["j"] - 1]["e"] - tw[mm["i"]]["s"]) if chant else (spans[lid][1] - spans[lid][0])
    for stem in stems: pool_len += DURS[stem]
    pool_len -= sum(((WORDS_ALL if chant else WORDS)[m["take"]][m["j"] - 1]["e"] -
                     (WORDS_ALL if chant else WORDS)[m["take"]][m["i"]]["s"])
                    for m in matched.values())
    need_cover = (w1 - w0) - vocal_len
    k_cover = 1.0
    if need_cover > pool_len > 0:
        k_cover = min(1.45, need_cover / pool_len)
        if k_cover > 1.02:
            warnings.append(f"S{n} cover stretch x{k_cover:.2f} (pool {pool_len:.1f}s < need {need_cover:.1f}s)")

    scene_sigs = [content_of(txt) for lid, txt, ls, le in lines]
    if tag == "SINGING":
        cur = w0
        for lid, txt, ls, le in lines:
            s0, s1 = spans[lid]
            if lid in matched:
                mm = matched[lid]; tw = WORDS[mm["take"]]
                twords = tw[mm["i"]:mm["j"]]
                tstart, tend = twords[0]["s"], twords[-1]["e"]
                if lid in songspans:
                    ss, se, si, sj = songspans[lid]
                    swords = SONG[si:sj]
                else:
                    ss, se = s0, s1; swords = None
                if ss > cur + 0.02: fill(n, stems, cur, ss, k_cover, repeat_sig=scene_sigs)
                segs = []
                if swords and len(swords) == len(twords):
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
                    k = (se - ss) / (tend - tstart)
                    segs.append((mm["take"], tstart, k, ss, se))
                    if not (0.6 <= k <= 1.7):
                        warnings.append(f"S{n} {lid} warp k={k:.2f}")
                first = True
                for (stem, ts, k, bo0, bo1) in segs:
                    if stem is None:
                        fill(n, stems, bo0, bo1, k_cover, repeat_sig=scene_sigs)
                    else:
                        if first and bo0 < cur - 0.02:  # trim overhang into previous line
                            ts = ts + (cur - bo0) / k; bo0 = cur
                        add(n, stem, "W", ts, k, bo0, bo1)
                    first = False
                cur = max(cur, se)
            else:
                if s0 > cur + 0.02: fill(n, stems, cur, s0, k_cover, repeat_sig=scene_sigs)
                fill(n, stems, s0, s1, k_cover, slot=True)
                cur = max(cur, s1)
        if cur < w1 - 0.02: fill(n, stems, cur, w1, k_cover, repeat_sig=scene_sigs)
    else:
        intervals = []; cur = w0
        for lid, txt, ls, le in lines:
            s0, s1 = spans[lid]
            if s0 > cur + 0.02: intervals.append((cur, s0, None))
            intervals.append((s0, s1, lid)); cur = s1
        if cur < w1 - 0.02: intervals.append((cur, w1, None))
        elif intervals: intervals[-1] = (intervals[-1][0], w1, intervals[-1][2])
        for (o0, o1, lid) in intervals:
            need = o1 - o0
            if need <= 0.02: continue
            if lid and lid in matched:
                mm = matched[lid]; tw = WORDS_ALL[mm["take"]]
                tstart, tend = tw[mm["i"]]["s"], tw[mm["j"] - 1]["e"]
                dur = min(tend - tstart, need)
                add(n, mm["take"], "N", tstart, 1.0, o0, o0 + dur)
                if need - dur > 0.05:
                    fill(n, stems, o0 + dur, o1, k_cover, repeat_sig=content_of(txt))
            elif lid:
                fill(n, stems, o0, o1, k_cover, slot=True)
            else:
                fill(n, stems, o0, o1, k_cover, repeat_sig=scene_sigs)

# micro-gap closure (<=0.3s): stretch previous segment, recompute k
plan.sort(key=lambda z: z["out"][0])
for idx in range(1, len(plan)):
    prev, cur = plan[idx - 1], plan[idx]
    gap = cur["out"][0] - prev["out"][1]
    if 0 < gap <= 0.3 and prev["scene"] == cur["scene"]:
        take_len = (prev["out"][1] - prev["out"][0]) / prev["k"]
        prev["out"][1] = cur["out"][0]
        prev["k"] = round((prev["out"][1] - prev["out"][0]) / take_len, 4)
for sc in scenes:  # tail micro-gap
    items = [p for p in plan if p["scene"] == sc["n"]]
    if items:
        last = max(items, key=lambda z: z["out"][1])
        gap = sc["win"][1] - last["out"][1]
        if 0 < gap <= 0.3:
            take_len = (last["out"][1] - last["out"][0]) / last["k"]
            last["out"][1] = sc["win"][1]
            last["k"] = round((last["out"][1] - last["out"][0]) / take_len, 4)

# hole check + frame partition (merge <3f into previous)
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
# overlap audit on the claim ledger
audit_bad = []
for stem, ivs in used.items():
    ivs = sorted(ivs)
    for a in range(1, len(ivs)):
        if ivs[a][0] < ivs[a - 1][1] - 0.15:
            audit_bad.append(f"{stem} {ivs[a-1]} x {ivs[a]}")
print(f"segments: {len(final)}  total frames: {total} (target 6048)")
for ml in matchlog: print("MATCH:", ml)
for w in warnings: print("WARN:", w)
for b in audit_bad: print("AUDIT-OVERLAP:", b)
json.dump(final, open(os.path.join(P, "work/swing/plan.json"), "w"), indent=1)
for r in final:
    print(f"S{r['scene']:02d} {r['kind']} {r['take'][5:12]} ts={r['take_start']:6.2f} "
          f"k={r['k']:.3f} out {r['out'][0]:7.2f}-{r['out'][1]:7.2f} f{r['frames'][0]}-{r['frames'][1]}")
