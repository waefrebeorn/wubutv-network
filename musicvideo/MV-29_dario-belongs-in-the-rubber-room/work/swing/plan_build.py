#!/usr/bin/env python3
"""MV-29 assembly planner. Adapted from MV-28's plan_build.py.
 - Line song spans = LYRIC_TIMELINE.md (sheet text authority, ASR
   timing authority). Phrase-level chunk warps when take/song word
   counts agree, else whole-span warp. Warp caps per the ledger:
   grey phrases disclosed; nothing slows past 2x.
 - MANUAL dispositions from TAKE_HISTORY.md (assembly call sheet):
   * S04: generation BLOCKED twice -> manual cover: s03_t1 prop-swap
     span + s01_t1 bounce span, captions carry L07/L08.
   * S15/S19/S20: wordless cutaways placed on their tail spans
     (bloom culmination / Huang silhouette / bill hang live there).
   * S25: manual TB head + TA full (TA tail = calm dawn lean finish);
     mid-block cut between the two wordless takes per the ledger.
   * S01 L02 "Yeah": manual match on the take-tail Yeah (9.00-9.70),
     cut as its own sub-segment onto 2.32-2.92, trim no warp.
   * S16 L28: BAD-SPAN split — take "belong" stumble (4.98-5.80) is
     never warped: Dario-only seg, montage cover over the song's
     "belongs" span (bouncing-traders tail of the same take), then
     the correct "belongs..." phrase warped in.
   * S08 L14: FORCE_COVER — two pacing attempts hit the structural
     floor (1.68/1.72); L13 matches from t2, L14 span is a beat-cut
     montage cover from s08_t2/t1 non-sung complement spans only.
   * S24: ptr starts at the SECOND "Yeah" (the doubled head Yeah is
     trimmed, never used); L45 anchors on it per the ledger.
 - Take ASR screened at p>=0.10 so QC-cleared low-probability proper
   nouns (S07 "Huang" p=0.14, S13t2 "Spy" p=0.13) still match, while
   S21's p=0.00 defective "belong" token stays excluded.
 - Final audit: no picture span used twice (claim ledger).
Output: work/swing/plan.json + review table. Frame-exact per scene,
target 4445 frames."""
import json, os, re, subprocess
from collections import Counter

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FPS = 24
scenes = json.load(open(os.path.join(P, "work/scenes.json")))

# (line_id, sheet text, song_start, song_end) — LYRIC_TIMELINE.md
LINES = [
 ("L01","Rubber room",0.00,2.32),
 ("L02","Yeah",2.32,2.92),
 ("L03","Dario belongs in the rubber room",3.52,6.30),
 ("L04","Dario belongs in the rubber room",7.38,10.08),
 ("L05","Talks the doom then he takes the cash",10.08,13.28),
 ("L06","Dario belongs in the rubber room",13.28,16.98),
 ("L07","Huang is gone and the IPO flash",16.98,20.88),
 ("L08","Dario belongs in the rubber room",21.62,24.78),
 ("L09","Left the old team for the safety line",32.80,36.60),
 ("L10","Half the jobs gone in a short short time",36.60,40.48),
 ("L11","Law and finance, the white-collar fall",40.48,44.42),
 ("L12","Huang said only they should do it all",44.42,47.82),
 ("L13","Outrageous lie but the race stays hot",47.82,51.32),
 ("L14","China chips and the nuclear talk",52.24,57.36),
 ("L15","Dario belongs in the rubber room",58.76,62.12),
 ("L16","Dario belongs in the rubber room",62.12,66.00),
 ("L17","Talks the doom then he takes the cash",66.00,70.34),
 ("L18","Dario belongs in the rubber room",70.34,73.86),
 ("L19","Huang is gone and the IPO flash",73.86,77.90),
 ("L20","Dario belongs in the rubber room",77.90,81.82),
 ("L21","Pentagon call and the deal went cold",82.42,84.28),
 ("L22","No mass watch and the weapons hold",84.28,86.12),
 ("L23","Then the board met and the Huang went down",86.12,88.16),
 ("L24","Spy reports and the staff went round",88.16,90.02),
 ("L25","Outrageous lie but the race stays hot",90.02,94.10),
 ("L26","China chips and the nuclear talk",94.10,96.66),
 ("L27","Dario belongs in the rubber room",102.08,105.22),
 ("L28","Dario belongs in the rubber room",105.22,109.18),
 ("L29","Talks the doom then he takes the cash",109.18,113.30),
 ("L30","Dario belongs in the rubber room",114.10,116.98),
 ("L31","Huang is gone and the IPO flash",116.98,121.16),
 ("L32","Dario belongs in the rubber room",123.40,127.36),
 ("L39","Dario belongs in the rubber room",142.86,147.00),
 ("L40","Dario belongs in the rubber room",147.00,150.60),
 ("L41","Talks the doom then he takes the cash",150.60,154.58),
 ("L42","Dario belongs in the rubber room",154.58,158.22),
 ("L43","Huang is gone and the IPO flash",158.22,162.18),
 ("L44","Dario belongs in the rubber room",164.72,168.56),
 ("L45","Yeah",168.56,169.38),
 ("L46","Rubber room",169.38,172.78),
]
SCENE_LINES = {
 1:["L01","L02"], 2:["L03","L04"], 3:["L05","L06"],
 6:["L09","L10"], 7:["L11","L12"], 8:["L13","L14"],
 9:["L15","L16"], 10:["L17","L18"], 11:["L19","L20"],
 12:["L21","L22"], 13:["L23","L24"], 14:["L25","L26"],
 16:["L27","L28"], 17:["L29","L30"], 18:["L31","L32"],
 21:["L39","L40"], 22:["L41","L42"], 23:["L43","L44"],
 24:["L45","L46"],
}
LINE_MAP = {lid:(txt,s,e) for lid,txt,s,e in LINES}
SCENE_TAKES = {
 1:["s01_t1"], 2:["s02_t1"], 3:["s03_t1"], 5:["s05_t1"],
 6:["s06_t1"], 7:["s07_t1"], 8:["s08_t2","s08_t1"],
 9:["s09_t1"], 10:["s10_t2"], 11:["s11_t2"], 12:["s12_t1"],
 13:["s13_t2"], 14:["s14_t3"], 15:["s15_t1"], 16:["s16_t1"],
 17:["s17_t1"], 18:["s18_t1"], 19:["s19_t1"], 20:["s20_t1"],
 21:["s21_t1"], 22:["s22_t1"], 23:["s23_t1"], 24:["s24_t3"],
 25:["s25_ta","s25_tb"],
}
STEM_SCENE = {s: n for n, v in SCENE_TAKES.items() for s in v}
WORDLESS = {"s05_t1","s15_t1","s19_t1","s20_t1","s25_ta","s25_tb"}
FORCE_COVER = {(8, "L14")}
PTR_START_TIME = {"s24_t3": 0.5}
SKIP_SCENES = {4, 15, 19, 20, 25}
DONOR_OVERRIDE = {}
MISHEAR = {}
STOP = {"the","a","an","and"}
def norm(w):
    w = re.sub(r"[^a-z]","", w.lower().strip())
    return MISHEAR.get(w, w)
def content_of(text):
    return [t for t in (norm(w) for w in re.split(r"[\s,]+", text))
            if t and t not in STOP]

def take_words(stem, min_p):
    path = os.path.join(P, "work/qc", "mv29_" + stem + "_asr.json")
    if not os.path.exists(path): return []
    d = json.load(open(path))
    ws = []
    for seg in d["segments"]:
        for w in seg["words"]:
            if w.get("p", 0) < min_p: continue
            ws.append({"w": norm(w["w"]), "s": w["s"], "e": w["e"]})
    return ws
def take_dur(stem):
    f = os.path.join(P, "takes", f"mv29_{stem}.mp4")
    return float(subprocess.run(["ffprobe","-v","error","-show_entries",
        "format=duration","-of","csv=p=0", f], capture_output=True, text=True).stdout.strip())

ALL_STEMS = sorted({s for v in SCENE_TAKES.values() for s in v})
WORDS = {s: take_words(s, 0.10) for s in ALL_STEMS}
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
    plan.append({"scene": scene, "take": f"mv29_{stem}.mp4", "kind": kind,
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

# --- MANUAL LINES (computed from take ASR + song grid) ---------------
MANUAL_LINES = {}
# S01 L02: the "Yeah" isolated at the take tail -> own sub-segment.
_ye = [w for w in WORDS_ALL["s01_t1"] if w["w"] == "yeah" and w["s"] > 5.0]
assert _ye, "S01 tail Yeah missing from take ASR"
_y = _ye[0]
MANUAL_LINES[(1, "L02")] = [("s01_t1", _y["s"],
    (2.92 - 2.32) / (_y["e"] - _y["s"]), 2.32, 2.92)]
matchlog.append(f"S1 L02 <- MANUAL s01_t1 tail Yeah [{_y['s']:.2f}-{_y['e']:.2f}]")
# S16 L28: bad-span split around the "belong" stumble.
_ws16 = WORDS_ALL["s16_t1"]
_d2 = next(w for w in _ws16 if w["w"] == "dario" and w["s"] > 4.0)
_bl = next(w for w in _ws16 if w["w"] == "belong" and w["s"] > _d2["s"])
_bs = next(w for w in _ws16 if w["w"] == "belongs" and w["s"] > _bl["s"])
_room2 = next(w for w in _ws16 if w["w"] == "room" and w["s"] > _bs["s"])
_seg_end = _room2["e"]
_sw = [w for w in SONG if w["s"] >= 105.22 - 0.3 and w["e"] <= 109.18 + 0.3]
_sbel = next(w for w in _sw if w["w"] == "belongs")
_cov_len = _sbel["e"] - _sbel["s"]
assert _seg_end + _cov_len <= 10.02, "S16 cover span overruns take"
MANUAL_LINES[(16, "L28")] = [
 ("s16_t1", _d2["s"], (_sbel["s"] - 105.22) / (_bl["s"] - _d2["s"]),
  105.22, _sbel["s"]),
 ("s16_t1", _seg_end, 1.0, _sbel["s"], _sbel["e"]),
 ("s16_t1", _bs["s"], (109.18 - _sbel["e"]) / (_seg_end - _bs["s"]),
  _sbel["e"], 109.18),
]
for _s in MANUAL_LINES[(16, "L28")]:
    assert 0.5 <= _s[2] <= 2.0, f"S16 manual warp out of band: {_s}"
matchlog.append(f"S16 L28 <- MANUAL bad-span split: Dario [{_d2['s']:.2f}-{_bl['s']:.2f}] "
                f"k={MANUAL_LINES[(16,'L28')][0][2]:.2f} + cover [{_seg_end:.2f}+{_cov_len:.2f}] "
                f"over song 'belongs' [{_sbel['s']:.2f}-{_sbel['e']:.2f}] + phrase "
                f"[{_bs['s']:.2f}-{_seg_end:.2f}] k={MANUAL_LINES[(16,'L28')][2][2]:.2f}; "
                f"stumble [{_bl['s']:.2f}-{_bs['s']:.2f}] NEVER USED")

# --- MANUAL SCENES (pre-claimed before the scene loop) ---------------
# S04 cover by design: s03 prop-swap action + s01 room bounce.
add(4, "s03_t1", "C", 2.94, 1.0, 16.98, 20.34); claim("s03_t1", 2.94, 6.30)
add(4, "s01_t1", "C", 2.48, 1.0, 20.34, 25.28); claim("s01_t1", 2.48, 7.42)
matchlog.append("S04 L07/L08 <- MANUAL COVER s03_t1[2.94-6.30] + s01_t1[2.48-7.42] (generation blocked x2)")
# S15: tail span — the bloom culminates in the full padded tunnel.
add(15, "s15_t1", "C", 4.58, 1.0, 96.66, 102.08); claim("s15_t1", 4.58, 10.0)
matchlog.append("S15 <- MANUAL tail span s15_t1[4.58-10.00]")
# S19: tail span — Huang silhouette lives in the door window tail.
add(19, "s19_t1", "C", 2.36, 1.0, 127.36, 135.00); claim("s19_t1", 2.36, 10.0)
matchlog.append("S19 <- MANUAL tail span s19_t1[2.36-10.00]")
# S20: tail span — the bill hangs mid-air for the whole tail.
add(20, "s20_t1", "C", 2.14, 1.0, 135.00, 142.86); claim("s20_t1", 2.14, 10.0)
matchlog.append("S20 <- MANUAL tail span s20_t1[2.14-10.00]")
# S25: TB head (two-wall lineup) then TA full (dawn lean finish).
add(25, "s25_tb", "C", 0.0, 1.0, 172.90, 175.216); claim("s25_tb", 0.0, 2.316)
add(25, "s25_ta", "C", 0.0, 1.0, 175.216, 185.216); claim("s25_ta", 0.0, 10.0)
matchlog.append("S25 <- MANUAL s25_tb[0-2.316] + s25_ta[0-10] (TA primary finish)")

for sc in scenes:
    n = sc["n"]; w0, w1 = sc["win"]; tag = sc["tag"]
    if n in SKIP_SCENES: continue
    stems = SCENE_TAKES[n]
    if tag == "CUTAWAY":
        pool = sum(DURS[s] - sum(b - a for (a, b) in used.get(s, [])) for s in stems)
        k_cover = 1.0
        if (w1 - w0) > pool > 0:
            k_cover = min(1.45, (w1 - w0) / pool)
            warnings.append(f"S{n} cutaway cover stretch x{k_cover:.2f}")
        fill(n, stems, w0, w1, k_cover)
        continue
    ptr = {}
    for s in stems:
        t0 = PTR_START_TIME.get(s, 0.0)
        idx = [i for i, w in enumerate(WORDS[s]) if w["s"] >= t0]
        ptr[s] = idx[0] if idx else 0
    lines = [(lid, LINE_MAP[lid][0], LINE_MAP[lid][1], LINE_MAP[lid][2])
             for lid in SCENE_LINES[n]]
    matched, spans = {}, {}
    for li, (lid, txt, ls, le) in enumerate(lines):
        spans[lid] = (ls, le)
        if (n, lid) in MANUAL_LINES:
            matched[lid] = {"manual": MANUAL_LINES[(n, lid)]}
            for (stem, ts, k, o0, o1) in MANUAL_LINES[(n, lid)]:
                claim(stem, ts, ts + (o1 - o0) / k)
            matchlog.append(f"S{n} {lid} <- MANUAL (see header)")
            continue
        if (n, lid) in FORCE_COVER:
            matchlog.append(f"S{n} {lid} <- FORCE COVER (structural pacing floor)")
            continue
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
        if lid in matched and "manual" in matched[lid]:
            segs = matched[lid]["manual"]
            if segs[0][3] > cur + 0.02:
                fill(n, stems, cur, segs[0][3], k_cover, repeat_sig=scene_sigs)
            for (stem, ts, k, bo0, bo1) in segs:
                add(n, stem, "W", ts, k, bo0, bo1)
            cur = max(cur, segs[-1][4])
        elif lid in matched:
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
            rs = None if (n, lid) in FORCE_COVER else scene_sigs
            if s0 > cur + 0.02: fill(n, stems, cur, s0, k_cover, repeat_sig=rs)
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
print(f"segments: {len(final)}  total frames: {total} (target 4445)")
for ml in matchlog: print("MATCH:", ml)
for w in warnings: print("WARN:", w)
for b in audit_bad: print("AUDIT-OVERLAP:", b)
json.dump(final, open(os.path.join(P, "work/swing/plan.json"), "w"), indent=1)
for r in final:
    print(f"S{r['scene']:02d} {r['kind']} {r['take'][5:12]} ts={r['take_start']:6.2f} "
          f"k={r['k']:.3f} out {r['out'][0]:7.2f}-{r['out'][1]:7.2f} f{r['frames'][0]}-{r['frames'][1]}")
