#!/usr/bin/env python3
"""MV-5 v4 plan builder.

Method correction vs v3 (per-word swing warps, 249 pieces):
- Anchors are VISIBLE mouth events (work/mouth_events_v4.json), not take-audio
  word times (hints only - mouth-lag doctrine + refrain blindness).
- PHRASE-LEVEL SMOOTH WARPS ONLY: one setpts factor per sung phrase.
- Chorus scenes run their chorus take CONTINUOUSLY (no donor slices at
  onsets). S16 (Chorus 2 head) has no singing take among s16_t1-t6, so its
  four hooks use the sanctioned montage-insert exception (s24_t2/t3 active
  singing heads, otherwise unused); inter-lines stay on s16_t1.
- Intro hooks I05/I07 (cutaway take s02_t1) use montage inserts from
  s06_t1's unused articulating tail.
- Cover scenes with no gated onsets (S03, S10, S13, S14, S18, S19a, S28)
  keep v3 pieces verbatim, except donor swaps where v3 borrowed frames
  that v4 now uses at their home positions (s27_t1 out of S13/S14,
  s21_t3 out of S15/S17 donors -> its own scene S22).
- S26/S27 boundary moved 197.58 -> 193.00 so s27_t1's own performance
  (L108 passage + hook decoded at take 3.6s) anchors L109 at the app
  onset 196.6 (audio bible: L109 'Easy now' 196.4-197.0 GIRL).
Output: work/assembly_fit_mv5_v4.json (same schema as v3pw).
"""
import json, math, os

PROJ = os.path.dirname(os.path.abspath(__file__))
FPS = 24

v3 = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5_v3pw.json")))
V3PLAN = v3["plan"]

# Scene frame totals from v3 (verified against its bounds), with the
# S26/S27 boundary move: S26 172f -> 62f, S27 140f -> 250f (sum unchanged).
SCENE_FRAMES = {}
for sc, pieces in V3PLAN.items():
    SCENE_FRAMES[sc] = sum(p["out"] for p in pieces)
SCENE_FRAMES["S26"] = 62
SCENE_FRAMES["S27"] = 250

BOUNDS_S = [0, 10.04, 18.64, 22.00, 31.48, 40.44, 47.76, 57.52, 67.06,
            76.80, 85.16, 93.80, 102.40, 111.90, 116.00, 121.30, 130.78,
            140.52, 148.70, 152.36, 155.72, 158.06, 167.50, 169.16, 176.04,
            182.78, 190.42, 193.00, 203.42, 206.4167]
SCENE_IDS = list(V3PLAN.keys())  # S01..S28 in order (S19a/S19b separate)

# cumulative dst (seconds) per scene id
DST0 = {}
acc = 0.0
bounds_frames = []
for i, sc in enumerate(SCENE_IDS):
    DST0[sc] = BOUNDS_S[i]
assert abs(BOUNDS_S[-1] - 206.4167) < 1e-6

def piece(take, sf, warp, out, kind, ef=None):
    if ef is None:
        ef = sf + math.ceil(out / warp)
    return {"take": f"mv5_{take}", "sf": sf, "ef": ef, "warp": round(warp, 4),
            "out": out, "kind": kind}

def verbatim(scene, swaps=None):
    """Copy v3 pieces; swaps: {(old_take, sf): new_take}."""
    out = []
    for p in V3PLAN[scene]:
        q = dict(p)
        if swaps and (q["take"], q["sf"]) in swaps:
            q["take"] = swaps[(q["take"], q["sf"])]
        out.append(q)
    return out

PLAN = {}

# S01: freeze leader (as v3) + one phrase, mouth/audio fit
PLAN["S01"] = [
    piece("s01_t1", 0, 1.0, 40, "leader-freeze", ef=1),
    piece("s01_t1", 5, 0.9315, 201, "phrase-I01-I04"),
]
# S02: cutaway base + sanctioned montage inserts on hooks I05/I07
PLAN["S02"] = [
    piece("s06_t1", 150, 1.0, 27, "insert-I05"),
    piece("s02_t1", 27, 1.0, 101, "cutaway-I06"),
    piece("s06_t1", 189, 1.0, 27, "insert-I07"),  # gate fix: +3f, onset lands on the open run
    piece("s02_t1", 156, 1.0, 51, "cutaway-I08"),
]
PLAN["S03"] = verbatim("S03")
# S04: gate fix - split at L02 (its onset landed closed under the single fit);
# P2 starts at f63 (where P1's consumption ends; inside the take's verified
# open run f60-f72), so L02's onset lands open-mouthed
PLAN["S04"] = [
    piece("s04_t1", 0, 0.964, 60, "phrase-L01"),
    piece("s04_t1", 63, 0.9492, 168, "phrase-L02-L05"),
]
# S05: one phrase, warp 1.0
PLAN["S05"] = [piece("s05_t1", 0, 1.0, SCENE_FRAMES["S05"], "phrase-L06-L09")]
# S06: s06_t1 (L10-L11) + s06_t2 (L12, GIRL per ear verdict)
PLAN["S06"] = [
    piece("s06_t1", 2, 0.933, 118, "phrase-L10-L11"),
    piece("s06_t2", 0, 1.23, 57, "phrase-L12"),
]
# S07: s07_t1 (L13-L14) + s07_t2 (L15) + s07_t1 tail (L16, stretched phrase)
PLAN["S07"] = [
    piece("s07_t1", 2, 0.738, 89, "phrase-L13-L14"),
    piece("s07_t2", 0, 0.5234, 32, "phrase-L15"),
    piece("s07_t1", 150, 1.2556, 113, "phrase-L16"),
]
# S08: Chorus 1; gate fix - split at L21 (L21/L22/L23 landed closed under the
# single fit); P2 re-anchored on the take's open frame f144. Re-gate fixes:
# P2's tail landed L24 closed, and an s09_t1 insert also landed closed (that
# take's tail is calm - full-res verified). L24 is a CAT inter-line, so it
# gets s06_t1's free f129-150: full-res verified CAT articulation in every
# frame (the cat sings while the girl holds the keys)
PLAN["S08"] = [
    piece("s08_t2", 7, 1.03, 129, "phrase-L17-L20"),
    piece("s08_t2", 144, 1.1111, 76, "phrase-L21-L23"),
    piece("s06_t1", 129, 1.1429, 24, "insert-L24"),
]
# S09: Chorus 1b continuous; proportional hook fit setpts 1.447
PLAN["S09"] = [piece("s09_t1", 0, 1.447, SCENE_FRAMES["S09"], "phrase-chorus1b")]
PLAN["S10"] = verbatim("S10")
# S11: one phrase
PLAN["S11"] = [piece("s11_t4", 0, 0.8884, SCENE_FRAMES["S11"], "phrase-L37-L40")]
# S12: one phrase (take is exactly 216f)
PLAN["S12"] = [piece("s12_t1", 0, 0.9583, SCENE_FRAMES["S12"], "phrase-L41-L44")]
# S13/S14: v3 cover pieces; donors whose frames v4 uses at home are swapped
# to filler takes (s27_t1 -> s16_t5; s04_t1/s06_t1/s19b_t1 -> s13_t6;
# s16_t1 -> s16_t5). Swap value = (new_take, new_sf); new ef keeps the span.
def verbatim_swaps(scene, swapmap):
    out = []
    for p in V3PLAN[scene]:
        q = dict(p)
        key = (q["take"], q["sf"])
        if key in swapmap:
            nt, nsf = swapmap[key]
            span = q["ef"] - q["sf"]
            q["take"], q["sf"], q["ef"] = nt, nsf, nsf + span
        out.append(q)
    return out

PLAN["S13"] = verbatim_swaps("S13", {
    ("mv5_s27_t1", 114): ("mv5_s16_t5", 114),
    ("mv5_s04_t1", 204): ("mv5_s13_t6", 0),
    ("mv5_s06_t1", 194): ("mv5_s13_t6", 40),
    ("mv5_s19b_t1", 100): ("mv5_s13_t6", 60),
    ("mv5_s28_t1", 85): ("mv5_s13_t6", 70),
})
PLAN["S14"] = verbatim_swaps("S14", {
    ("mv5_s27_t1", 85): ("mv5_s16_t5", 85),
    ("mv5_s16_t1", 151): ("mv5_s16_t5", 150),
})
# S15: s15_t1's whole L56 performance stretched over the scene; no donor tail
PLAN["S15"] = [piece("s15_t1", 0, 1.2330, SCENE_FRAMES["S15"], "phrase-L56")]
# S16: s16_t1 base (CAT inter-lines) + montage inserts on the 4 hooks
PLAN["S16"] = [
    piece("s24_t2", 0, 1.0, 31, "insert-L57"),
    piece("s16_t1", 96, 1.0, 34, "base-L58"),
    piece("s24_t2", 31, 1.0, 25, "insert-L59"),
    piece("s16_t1", 130, 1.0, 30, "base-L60"),
    piece("s24_t2", 60, 1.0, 26, "insert-L61"),
    piece("s16_t1", 160, 1.0, 19, "base-L62"),
    piece("s24_t3", 70, 1.0, 36, "insert-L63"),
    piece("s16_t1", 179, 1.0, 27, "base-L64"),
]
# S17: Chorus 2; gate fix - L69/L70 land in the take's wide/profile passage
# (mouth closed at both onsets), so that span becomes sanctioned inserts:
# L69 (GIRL hook) from s09_t1's singing tail; L70 (CAT inter-line) from
# s28_t1 f57 - full-res verified open-mouth beat (tongue out at f57, tip at
# f60; the take's only articulation, mouth closes after ~0.2s - disclosed in
# the notes; sunset cutaway 3s before the sunset act). An s06_t1 f216 insert
# was tried first and landed closed (that tail is a smug slow-blink).
# P1/P2 keep the original fit's mapping exactly
PLAN["S17"] = [
    piece("s17_t1", 38, 1.23, 123, "phrase-L65-L68"),
    piece("s09_t1", 185, 1.0, 26, "insert-L69"),
    piece("s28_t1", 57, 1.2083, 29, "insert-L70"),
    piece("s17_t1", 183, 1.23, 55, "phrase-L71-L72"),
]
PLAN["S18"] = verbatim("S18")
PLAN["S19a"] = verbatim("S19a")
# S19b: one phrase (complete decode fit, setpts 0.762)
PLAN["S19b"] = [piece("s19b_t1", 0, 0.762, SCENE_FRAMES["S19b"], "phrase-L77-L79")]
# S20: one phrase
PLAN["S20"] = [piece("s20_t1", 0, 0.6333, SCENE_FRAMES["S20"], "phrase-L80-L81")]
PLAN["S21"] = verbatim("S21")
# NOTE: no S21 slice shift - the plan's actual L85 slice is s21_t13 sf82-108
# (not sf0 as the v3 notes suggested), and the bridge's app/v1 onset grids
# disagree by ~1 line in this rapid section; the montage stays exactly as v3
# per the repair brief, and L85 reads transitional->open at +0.15.
# S22: s21_t3 sings this scene's own lines - moved home from donor duty
PLAN["S22"] = [piece("s21_t3", 8, 1.0, SCENE_FRAMES["S22"], "phrase-L90")]
# S23: hooks phrase (fit on decoded hooks 0.2->169.2, 3.5->174.0) + L96 phrase
PLAN["S23"] = [
    piece("s23_t1", 4, 1.4545, 143, "phrase-L91-L95"),
    piece("s23_t1", 144, 0.9167, 22, "phrase-L96"),
]
# S24: active heads of s24_t1 (L97-L100) + s24_t3 (L101-L102)
PLAN["S24"] = [
    piece("s24_t1", 0, 0.88, 102, "phrase-L97-L100"),
    piece("s24_t3", 0, 0.9375, 60, "phrase-L101-L102"),
]
# S25: hooks phrase (0.6->183.0, 2.1->184.68) + L106 on s28_t3's singing head
PLAN["S25"] = [
    piece("s25_t1", 10, 1.12, 88, "phrase-L103-L105"),
    piece("s28_t3", 0, 1.759, 95, "phrase-L106"),
]
# S26: cover, shortened by the boundary move (profile section of s26_t1)
PLAN["S26"] = [piece("s26_t1", 120, 1.0, SCENE_FRAMES["S26"], "cover-L108-zone")]
# S27: s27_t1 home phrase (hook 3.6s -> 196.6) + instrumental interlude
# (s16_t6 clouds, no words) + L110a phrase (s28_t1)
PLAN["S27"] = [
    piece("s27_t1", 0, 1.0351, 118, "phrase-L108-L109"),
    piece("s16_t6", 60, 1.0, 74, "interlude-instrumental"),
    piece("s28_t1", 0, 1.0357, 58, "phrase-L110a"),
]
PLAN["S28"] = verbatim("S28")

# fill dst0/dst1 + validate
total = 0
for sc in SCENE_IDS:
    pieces = PLAN[sc]
    ssum = sum(p["out"] for p in pieces)
    assert ssum == SCENE_FRAMES[sc], f"{sc}: pieces sum {ssum} != scene {SCENE_FRAMES[sc]}"
    t = DST0[sc]
    for p in pieces:
        p["dst0"] = round(t, 4)
        t += p["out"] / FPS
        p["dst1"] = round(t, 4)
    total += ssum
assert total == 4954, f"total {total} != 4954"

# banned takes must never appear
blob = json.dumps(PLAN)
for banned in ("mv5_s28_t5", "mv5_s07_t3", "mv5_s21_t7"):
    assert banned not in blob, banned

# overlap check: same take may not reuse the same frames at two positions.
# Exempt: S21's verbatim bridge montage - v3 disclosed a 3-frame overlap
# inside s21_t13 (f36-39 in both the L83 and L87 slices); montage-internal.
used = {}
for sc in SCENE_IDS:
    for p in PLAN[sc]:
        key = p["take"]
        for (a, b, where) in used.get(key, []):
            if sc == "S21" and where == "S21":
                continue
            assert p["ef"] <= a or p["sf"] >= b, \
                f"frame reuse: {key} [{p['sf']},{p['ef']}) in {sc} overlaps [{a},{b}) in {where}"
        used.setdefault(key, []).append((p["sf"], p["ef"], sc))

out = {"plan": PLAN, "total_frames": total, "bounds": BOUNDS_S, "scenes": SCENE_IDS,
       "note": "MV-5 v4: phrase-level smooth warps on visible mouth events; see work/V4_ASSEMBLY_NOTES.md"}
with open(os.path.join(PROJ, "work", "assembly_fit_mv5_v4.json"), "w") as f:
    json.dump(out, f, indent=1)
n_pieces = sum(len(v) for v in PLAN.values())
print(f"v4 plan OK: {n_pieces} pieces, {total} frames")
for sc in SCENE_IDS:
    for p in PLAN[sc]:
        print(f"  {sc:5} {p['kind']:24} {p['take']:12} sf={p['sf']:3} ef={p['ef']:3} "
              f"w={p['warp']:.4f} out={p['out']:3}f dst {p['dst0']:.2f}-{p['dst1']:.2f}")
