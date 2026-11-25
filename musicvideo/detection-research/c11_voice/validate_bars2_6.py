#!/usr/bin/env python3
"""Sprint 8 validation bars 2-6 (no librosa needed except numpy).
Mirrors c11_voice.c make_bounds exactly; verifies mirror vs C output,
scores boundaries vs sprint-6 ref, sweeps thresholds, checks bars 4/5/6."""
import json, math, itertools
import numpy as np

DR = "/home/hatch/workspace/wubutv-network/musicvideo/detection-research"
V = DR + "/c11_voice"
REF = json.load(open(DR + "/c11_mir/hpss_mv14_ref.json"))["segments"]
HPSS = json.load(open(DR + "/c11_mir/hpss_mv14_validation.json"))["bounds"]

def load_curve(p):
    d = json.load(open(p))
    f = d["frames"]
    return (np.array([x["t"] for x in f]),
            np.array([x["voicing"] for x in f]),
            np.array([x["cpp_db"] for x in f]),
            np.array([x["hnr_db"] for x in f]),
            np.array([x["voiced"] for x in f], dtype=bool),
            np.array([x["pyin_voiced"] for x in f], dtype=bool),
            np.array([x["f0_hz"] for x in f]),
            np.array([x["f0_yin"] for x in f]))

def split_long(start, end, vc, out):
    if end - start <= 30.0:
        out.append((start, end)); return
    a, b = int(start*100), int(end*100)
    q = a + int(np.argmin(vc[a:b]))
    mid = q*0.01
    if mid - start < 2.0 or end - mid < 2.0:
        mid = (start+end)/2.0
    split_long(start, mid, vc, out); split_long(mid, end, vc, out)

def make_bounds(voiced, vc, track_len=161.6):
    n = len(voiced); runs = []; t = 0
    while t < n:
        if not voiced[t]: t += 1; continue
        s = t
        while t < n and voiced[t]: t += 1
        runs.append([s, t])
    merged = []
    for r in runs:
        if merged and (r[0]-merged[-1][1])*0.01 < 1.0:
            merged[-1][1] = r[1]
        else:
            merged.append(list(r))
    segs = []
    for r in merged:
        s, e = r[0]*0.01, r[1]*0.01
        if e - s < 0.5: continue
        split_long(s, e, vc, segs)
    out = []
    for s, e in segs:
        s2 = max(0.0, s-0.3); e2 = min(track_len, e+0.3)
        out.append((math.floor(s2*100+0.5)/100, math.floor(e2*100+0.5)/100))
    return out

def boundary_match(ref_b, c_b, tol=0.5):
    m = 0; offs = []
    for rb in ref_b:
        if not c_b: break
        d = min(abs(rb-cb) for cb in c_b)
        if d <= tol: m += 1; offs.append(d)
    return m, len(ref_b), (float(np.median(offs)) if offs else float("nan")), offs

def score(segs, label):
    rs = [s["start"] for s in REF]; re_ = [s["end"] for s in REF]
    cs = [s[0] for s in segs]; ce = [s[1] for s in segs]
    ms, ts, meds, soffs = boundary_match(rs, cs)
    me, te, mede, eoffs = boundary_match(re_, ce)
    cms, _, _, _ = boundary_match(cs, rs); cme, _, _, _ = boundary_match(ce, re_)
    print(f"{label}: C {len(segs)} segs | starts ref->C {ms}/{ts} med|off|={meds:.3f} | "
          f"ends ref->C {me}/{te} med|off|={mede:.3f} | OVERALL {(ms+me)}/24 "
          f"({100*(ms+me)/24:.1f}%) | C->ref starts {cms}/{len(cs)} ends {cme}/{len(ce)}")
    return {"starts_matched": ms, "starts_total": ts, "starts_median_offset_s": meds,
            "ends_matched": me, "ends_total": te, "ends_median_offset_s": mede,
            "overall_pct": 100*(ms+me)/24, "c_segments": len(segs),
            "c_to_ref_starts_matched": cms, "c_to_ref_ends_matched": cme,
            "start_offsets": soffs, "end_offsets": eoffs}

mix = load_curve(V+"/voice_mv14.json")
stem = load_curve(V+"/voice_mv14_stem.json")
mix_bounds = json.load(open(V+"/voice_bounds_mv14.json"))["segments"]
stem_bounds = json.load(open(V+"/voice_bounds_mv14_stem.json"))["segments"]

# --- mirror check at defaults (0.7/0.5/8.0) ---
for name, cur, cb in (("mix", mix, mix_bounds), ("stem", stem, stem_bounds)):
    t, vc, cpp, hnr, voiced, pyv, f0, f0y = cur
    gate = (vc >= 0.7) & (cpp >= 0.5) & (hnr >= 8.0)
    print(f"{name}: gate voiced frames {int(gate.sum())}/{len(gate)}; saved voiced {int(voiced.sum())}; gate==saved: {bool((gate==voiced).all())}")
    m = make_bounds(gate, vc)
    c = [(s["start"], s["end"]) for s in cb]
    print(f"{name}: mirror {len(m)} segs vs C {len(c)}; EXACT MATCH: {m==c}")
    if m != c:
        for i,(a,b) in enumerate(itertools.zip_longest(m,c)):
            if a!=b: print("  first diff", i, a, b); break

print("\n--- BAR 2/3: boundary scores (tol +/-0.5s, ref = 12 hand-marked sung spans) ---")
mix_score = score([(s["start"], s["end"]) for s in mix_bounds], "MIX  gate 0.7/0.5/8.0")
stem_score = score([(s["start"], s["end"]) for s in stem_bounds], "STEM gate 0.7/0.5/8.0")
print(f"HPSS (sprint 6, same ref): vocal-stem starts {HPSS['segments_vocal']['starts_matched']}/12 "
      f"ends {HPSS['segments_vocal']['ends_matched']}/12 overall {HPSS['segments_vocal']['overall_pct']:.1f}% ; "
      f"full-mix starts {HPSS['segments_full']['starts_matched']}/12 ends {HPSS['segments_full']['ends_matched']}/12 "
      f"overall {HPSS['segments_full']['overall_pct']:.1f}%")

# --- threshold sweep on mix + stem (150 combos: 6 voicing x 5 cpp x 5 hnr) ---
print("\n--- SWEEP (150 combos, mix) ---")
t, vc, cpp, hnr, voiced, pyv, f0, f0y = mix
best = []
for vthr in (0.3,0.5,0.6,0.7,0.8,0.9):
    for cthr in (0.5,2.0,4.0,6.0,8.0):
        for hthr in (None,0.0,4.0,8.0,12.0):
            g = (vc>=vthr)&(cpp>=cthr) if hthr is None else (vc>=vthr)&(cpp>=cthr)&(hnr>=hthr)
            segs = make_bounds(g, vc)
            rs=[s["start"] for s in REF]; re_=[s["end"] for s in REF]
            ms,_,_,_ = boundary_match(rs,[s[0] for s in segs])
            me,_,_,_ = boundary_match(re_,[s[1] for s in segs])
            best.append((ms+me, ms, me, vthr, cthr, hthr, len(segs)))
best.sort(key=lambda b: (b[0], b[1], b[2]), reverse=True)
for b in best[:8]:
    print(f"  total {b[0]}/24 starts {b[1]}/12 ends {b[2]}/12  voicing>={b[3]} cpp>={b[4]} hnr>={b[5]} segs={b[6]}")
print(f"  combos reaching >=80% (20/24): {sum(1 for b in best if b[0]>=20)}")
# pyin_voiced-only diagnostic on mix
py_segs = make_bounds(pyv, vc)
print("--- pyin_voiced-only segments (diagnostic, mix) ---")
score(py_segs, "MIX  pyin_voiced only")

# stem sweep best
print("\n--- SWEEP (150 combos, stem) top 5 ---")
t, vc, cpp, hnr, voiced, pyv, f0, f0y = stem
best2 = []
for vthr in (0.3,0.5,0.6,0.7,0.8,0.9):
    for cthr in (0.5,2.0,4.0,6.0,8.0):
        for hthr in (None,0.0,4.0,8.0,12.0):
            g = (vc>=vthr)&(cpp>=cthr) if hthr is None else (vc>=vthr)&(cpp>=cthr)&(hnr>=hthr)
            segs = make_bounds(g, vc)
            rs=[s["start"] for s in REF]; re_=[s["end"] for s in REF]
            ms,_,_,_ = boundary_match(rs,[s[0] for s in segs])
            me,_,_,_ = boundary_match(re_,[s[1] for s in segs])
            best2.append((ms+me, ms, me, vthr, cthr, hthr, len(segs)))
best2.sort(key=lambda b: (b[0], b[1], b[2]), reverse=True)
for b in best2[:5]:
    print(f"  total {b[0]}/24 starts {b[1]}/12 ends {b[2]}/12  voicing>={b[3]} cpp>={b[4]} hnr>={b[5]} segs={b[6]}")
print(f"  combos reaching >=80% (20/24): {sum(1 for b in best2 if b[0]>=20)}")

# --- BAR 4: CPP/HNR separation, mix curve, sung = ref segments ---
print("\n--- BAR 4: sung vs instrumental medians (mix curve) ---")
t, vc, cpp, hnr, voiced, pyv, f0, f0y = mix
sung = np.zeros(len(t), dtype=bool)
for s in REF:
    sung |= (t >= s["start"]) & (t < s["end"])
print(f"sung frames {int(sung.sum())} instrumental {int((~sung).sum())}")
for nm, arr in (("cpp_db", cpp), ("hnr_db", hnr), ("voicing", vc)):
    ms_ = float(np.median(arr[sung])); mi = float(np.median(arr[~sung]))
    print(f"  {nm}: sung median {ms_:.3f} | instrumental median {mi:.3f} | diff {ms_-mi:+.3f} (bar: +3 dB for cpp/hnr)")

# --- BAR 5: 5 early-snap errors ---
print("\n--- BAR 5: snapper early-snap errors (1-based indices 34,56,60,112,162) ---")
snap = json.load(open(DR+"/c11_mir/snap_mix_mv14.json"))["words"]
for idx in (34,56,60,112,162):
    w = snap[idx-1]
    a, b = w["asr_start"], w["asr_end"]
    inspan = (t >= a) & (t < b)
    nv = int(voiced[inspan].sum())
    # snapped-position check: voicing at snapped_start frame
    si = int(round(w["snapped_start"]/0.01))
    print(f"  #{idx} '{w['word']}' ASR {a:.2f}-{b:.2f} snapped {w['snapped_start']:.3f} "
          f"(corr {w['correction_s']:+.3f}) | voiced frames in ASR span: {nv}/{int(inspan.sum())} "
          f"| voiced at snapped pos: {bool(voiced[min(si,len(voiced)-1)])}")

# --- BAR 6: unsung spans ---
print("\n--- BAR 6: unsung/ambiguous spans (mix curve; pass = voiced fraction < 0.15) ---")
for label, a, b in (("intro 0.00-14.14 (confirmed wordless lead-in)", 0.0, 14.14),
                    ("gap 95.24-98.50 (wordless gap before bridge)", 95.24, 98.50),
                    ("tag 153.50-153.60 ('We\\'ll be right back.' ASR hallucination)", 153.50, 153.60),
                    ("outro 128.20-161.60 (33.4s wordless ride-out, supporting)", 128.20, 161.60)):
    m = (t >= a) & (t < b)
    vf = float(voiced[m].mean())
    print(f"  {label}: voiced {vf*100:.1f}% of {int(m.sum())} frames -> {'UNVOICED' if vf<0.15 else 'VOICED?'}")

json.dump({"mix_score": {k:v for k,v in mix_score.items() if k not in ("start_offsets","end_offsets")},
           "stem_score": {k:v for k,v in stem_score.items() if k not in ("start_offsets","end_offsets")},
           "mix_start_offsets": mix_score["start_offsets"], "mix_end_offsets": mix_score["end_offsets"],
           "stem_start_offsets": stem_score["start_offsets"], "stem_end_offsets": stem_score["end_offsets"],
           "sweep_mix_top8": [list(b) for b in best[:8]],
           "sweep_mix_ge80": sum(1 for b in best if b[0]>=20),
           "sweep_stem_top5": [list(b) for b in best2[:5]],
           "sweep_stem_ge80": sum(1 for b in best2 if b[0]>=20)},
          open("/tmp/c11_voice_val/bars2_3.json","w"), indent=1)
print("\nWROTE /tmp/c11_voice_val/bars2_3.json")
