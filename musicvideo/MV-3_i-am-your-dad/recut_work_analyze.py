#!/usr/bin/env python3
"""MV-3 re-cut stage 1 analysis: per-scene ratio / warp / verdict.

Warp rule (documented choice, parent may overrule):
  ratio = song line span / take line span (first word start -> last word end)
  usable [0.80, 1.25]  -> w = ratio (full alignment)
  grey-fast (1.25, 1.60] -> w = 1.25 (warp factor capped at band edge)
  grey-slow [0.60, 0.80) -> w = 0.80 (warp factor capped at band edge)
  outside [0.60, 1.60]  -> COVER (no mouth claim)
Placement: take clip trimmed at first-word time, placed at segment start,
so take first word lands on song first word. Warped take span vs song
span gives the end residual (positive = mouth ends late).
"""
import json, os

PROJ = os.path.dirname(os.path.abspath(__file__))
MEAS = os.path.join(PROJ, "recut_work", "measure")

def load_take(fn):
    d = json.load(open(os.path.join(MEAS, fn.replace(".mp4", ".json"))))
    words = [[w, t0, t1] for w, t0, t1 in d["words"]]
    sl = os.path.join(MEAS, fn.replace(".mp4", "_slice.json"))
    if os.path.exists(sl):
        sd = json.load(open(sl))
        words += [[w, t0, t1] for w, t0, t1 in sd["words"]]
        words.sort(key=lambda x: x[1])
    return words

SONG = json.load(open(os.path.join(PROJ, "SONG_WORDS.json")))["words"]

def song_words(lo, hi):
    return [(w, t0, t1) for w, t0, t1 in SONG if lo - 0.05 <= t0 < hi]

# (scene, seg_start, seg_end, take_file or None, song_span or None,
#  treatment, line_label)
SCENES = [
    ("S01", 2.82, 9.32, "mv3_s01_t2.mp4", (2.82, 9.00), "mouth", "L01"),
    ("S02", 9.32, 18.34, "mv3_s02_t2.mp4", (9.32, 18.34), "mouth", "L02"),
    ("S03", 18.34, 32.16, "mv3_s03_t1.mp4", None, "cutaway", "instr"),
    ("S04", 32.16, 36.56, "mv3_s04_t1.mp4", (32.16, 35.72), "structural", "L03"),
    ("S05", 36.56, 40.06, "mv3_s05_t1.mp4", (36.56, 39.74), "structural", "L04"),
    ("S06", 40.06, 48.12, "mv3_s06_t1.mp4", (40.06, 47.60), "mouth", "L05+L06"),
    ("S07", 48.12, 55.14, "mv3_s07_t1.mp4", (48.12, 54.38), "mouth", "L07+L08"),
    ("S08", 55.14, 62.64, "mv3_s08_t1.mp4", (55.14, 62.20), "mouth", "L09"),
    ("S09", 62.64, 68.36, "mv3_s09_t1.mp4", (62.64, 67.90), "mouth", "L10"),
    ("S10", 68.36, 76.28, "mv3_s10_t1.mp4", (68.36, 75.48), "mouth", "L11"),
    ("S11", 76.28, 82.92, "mv3_s11_t2.mp4", (76.28, 82.90), "mouth", "L12"),
    ("S12", 82.92, 90.66, "mv3_s12_t2.mp4", (82.92, 87.50), "mouth", "L13"),
    ("S13", 90.66, 99.68, "mv3_s13_t1.mp4", (90.66, 99.76), "mouth", "L14+L15"),
    ("S14", 99.68, 108.92, "mv3_s14_t1.mp4", (99.68, 108.92), "mouth", "L16"),
    ("S15", 108.92, 116.14, "mv3_s15_t1.mp4", (108.92, 115.90), "mouth", "L17"),
    ("S16", 116.14, 123.74, "mv3_s16_t1.mp4", (116.14, 123.40), "mouth", "L18"),
    ("S17", 123.74, 129.46, "mv3_s17_t1.mp4", (123.74, 128.90), "mouth", "L19"),
    ("S18", 129.46, 136.52, "mv3_s18_t2.mp4", (129.46, 135.80), "mouth", "L20"),
    ("S19", 136.52, 143.76, "mv3_s19_t1.mp4", (136.52, 143.80), "mouth", "L21"),
    ("S20", 143.76, 150.30, "mv3_s20_t1.mp4", (143.76, 149.10), "mouth", "L22"),
    ("S21", 150.30, 160.70, "mv3_s21_t2.mp4", (150.30, 159.50), "structural", "L23"),
    ("S22", 160.70, 168.76, "mv3_s22_t1.mp4", (160.70, 166.50), "mouth", "L24"),
    ("S23", 168.76, 183.06, "mv3_s23_t2.mp4", (168.76, 182.12), "mouth", "L25"),
    ("S24", 183.06, 195.24, "mv3_s24_t2.mp4", (183.06, 191.94), "structural", "L26"),
    ("S25", 195.24, 215.40, None, (195.24, 214.90), "structural", "L27"),
    ("S26", 215.40, 220.64, "mv3_s26_t1.mp4", (215.40, 220.64), "mouth", "L28"),
    ("S27", 220.64, 230.52, "mv3_s27_t1.mp4", (220.64, 230.00), "mouth", "L29"),
    ("S28", 230.52, 245.10, "mv3_s28_t3.mp4", (230.52, 245.10), "mouth", "L30+L31"),
    ("S29", 245.10, 251.04, "mv3_s29_t1.mp4", (245.10, 250.70), "mouth", "L32"),
    ("S30", 251.04, 258.32, "mv3_s30_t3.mp4", (251.04, 258.32), "structural", "L33"),
    ("S31", 258.32, 268.50, "mv3_s31_t1.mp4", (258.32, 268.50), "mantra-slice", "L34a"),
    ("S32", 268.50, 278.50, "mv3_s32_t1.mp4", (268.50, 278.50), "mantra-slice", "L34b"),
    ("S33", 278.50, 287.80, "mv3_s33_t1.mp4", (278.50, 287.80), "mantra-slice", "L34c"),
    ("S34", 287.80, 296.70, "mv3_s34_t1.mp4", (287.80, 296.00), "mouth", "L35"),
    ("S35", 296.70, 309.88, None, (296.70, 308.56), "structural", "L36"),
    ("S36", 309.88, 322.08, "mv3_s36_t2.mp4", (309.88, 321.44), "mouth", "L37"),
    ("S37", 322.08, 338.55, "mv3_s37_t1.mp4", (322.08, 338.55), "decision", "L38"),
    ("S38", 338.55, 344.55, "mv3_s38_t2.mp4", (338.55, 343.91), "mouth", "L39"),
    ("S39", 344.55, 354.816, "mv3_s39_t1.mp4", (344.55, 353.71), "decision", "L40"),
]

def warp_for(ratio):
    if 0.80 <= ratio <= 1.25:
        return ratio, "usable"
    if 1.25 < ratio <= 1.60:
        return 1.25, "grey-rescue (fast, band edge)"
    if 0.60 <= ratio < 0.80:
        return 0.80, "grey-rescue (slow, band edge)"
    return None, "COVER (outside caps)"

rows = []
for sc, ss, se, fn, span, tr, lab in SCENES:
    seg = se - ss
    if tr == "cutaway":
        rows.append((sc, tr, fn, "—", "—", "—", "—", "—", "slow-mo 1.382x fills instrumental window (no words)"))
        continue
    if tr == "structural":
        rows.append((sc, tr, fn or "s25_t1+s25_t2 / s35_t1+s35_t2", "—", "—", "—", "—",
                     "video cover only; master audio carries the line"))
        continue
    tw = load_take(fn)
    tf, tl = tw[0][1], tw[-1][2]
    tspan = tl - tf
    if tr == "mantra-slice":
        sspan = seg  # paced to segment, not individual repeats
        ratio = sspan / tspan
        w, verdict = warp_for(ratio)
        rows.append((sc, tr, fn, f"{tf:.2f}–{tl:.2f} ({tspan:.2f}s)",
                     f"segment {ss:.2f}–{se:.2f} ({sspan:.2f}s)", f"{ratio:.3f}",
                     f"w={w}" if w else "COVER", verdict +
                     "; bursts paced to segment, individual song repeats NOT matched (song ~0.74s/repeat vs take ~2.2s/burst)"))
        continue
    if tr == "decision" and sc == "S37":
        # take x2 bursts vs first two song repeats (323.32-327.54)
        sw = song_words(323.32, 327.54)
        sspan = 327.54 - 323.32
        ratio = sspan / tspan
        w, verdict = warp_for(ratio)
        rows.append((sc, tr, fn, f"{tf:.2f}–{tl:.2f} ({tspan:.2f}s)",
                     f"first two repeats 323.32–327.54 ({sspan:.2f}s)", f"{ratio:.3f}",
                     f"w={w}" if w else "COVER", verdict +
                     "; opening bursts mouth-synced to first two repeats, remainder = own-hold loop montage cover"))
        continue
    if tr == "decision" and sc == "S39":
        # take single mantra vs song first repeat (344.55-346.35)
        sspan = 346.35 - 344.55
        ratio = sspan / tspan
        w, verdict = warp_for(ratio)
        rows.append((sc, tr, fn, f"{tf:.2f}–{tl:.2f} ({tspan:.2f}s)",
                     f"first repeat 344.55–346.35 ({sspan:.2f}s)", f"{ratio:.3f}",
                     f"w={w}" if w else "COVER", verdict +
                     "; single mantra cannot land on any song repeat within caps -> whole slot montage cover (take video + tail, captions song-timed)"))
        continue
    # mouth scenes
    s0, s1 = span
    sspan = s1 - s0
    ratio = sspan / tspan
    w, verdict = warp_for(ratio)
    # per-word offsets after warp (order-matched, only if counts equal)
    sw = song_words(s0, s1)
    pw = ""
    if w and len(sw) == len(tw):
        offs = []
        for (tw_, t0, t1), (sw_, st0, st1) in zip(tw, sw):
            placed_end = (t1 - tf) * w  # seconds after segment start
            song_end = st1 - s0
            offs.append(placed_end - song_end)
        mx = max(abs(o) for o in offs)
        pw = f"per-word max|off| {mx:.2f}s (n={len(tw)})"
    elif w:
        pw = f"per-word: count mismatch take={len(tw)} song={len(sw)} (span-level only)"
    else:
        pw = "per-word: n/a (cover)"
    end_res = (tspan * w - sspan) if w else None
    rows.append((sc, tr, fn, f"{tf:.2f}–{tl:.2f} ({tspan:.2f}s)",
                 f"{s0:.2f}–{s1:.2f} ({sspan:.2f}s)", f"{ratio:.3f}",
                 f"w={w:.4f}" if w else "COVER",
                 verdict + (f"; end residual {end_res:+.2f}s" if end_res is not None else "") +
                 f"; seg {seg:.2f}s; {pw}"))

print(f"{'sc':4} {'treat':13} {'take':18} {'take span':22} {'song span':24} {'ratio':7} {'warp':10} verdict")
for r in rows:
    print(" | ".join(str(x) for x in r))
json.dump([{"scene": r[0], "treatment": r[1], "take": r[2], "take_span": r[3],
            "song_span": r[4], "ratio": r[5], "warp": r[6], "verdict": r[7]}
           for r in rows], open(os.path.join(PROJ, "recut_work", "analysis.json"), "w"), indent=1)
