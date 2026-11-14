#!/usr/bin/env python3
"""MV-5 v3 plan: copy the v2 fit plan, replace only S07 (L15) and S21 (bridge).

- S07: cover-L15 piece -> s07_t2, uniform warp 1.34/2.56 = 0.5234375
  (playback 1.91x, DISCLOSED out-of-band warp — parent decision; L15 is
  structural for per-line generation and a closed-mouth cover under a sung
  line is banned by the user's 2026-11-06 law).
- S21: all v2 pieces -> 9 beat-matched montage pieces (warp 1.0), cuts on
  the v2 line boundaries, GIRL-first alternation per the user's ear.
- Everything else copies v2 verbatim. Total frames must stay 4954.
- L15 word-start offsets are computed here from the QC JSON take word
  starts and the aligned song starts — not taken on trust from the brief.
"""
import copy, hashlib, json, os

PROJ = os.path.dirname(os.path.abspath(__file__))
V2 = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5_v2.json")))
QC15 = json.load(open(os.path.join(PROJ, "work", "qc_v15", "qc_v15_results.json")))
SONG = json.load(open(os.path.join(PROJ, "work", "gemini_song_words_aligned.json")))["rows"]

def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

# --- verify the new takes on disk ---
EXPECTED = {
    "mv5_s07_t2": "39ba0cf638d31f165accd2101ef487e8",
    "mv5_s21_t11": "4b91522f554a2893fa3f164197c14873",
    "mv5_s21_t12": "f2de5e0d8bb254dd5be590b92226457a",
    "mv5_s21_t13": "479a404a34c327ccf57088882f670599",
    "mv5_s21_t14": "3d047b2b662dafa6820f13adbc62f904",
    "mv5_s21_t15": "be27fe25d38dd0a5da532b6064469d66",
    "mv5_s21_t16": "c60c1e452c116fa0ee27582add1fe5f7",
}
for take, want in EXPECTED.items():
    got = md5(os.path.join(PROJ, "takes", take + ".mp4"))
    assert got == want, f"{take} md5 {got} != {want}"
    print(f"{take} md5 OK")
# s28_t5 must never appear in the plan
assert "mv5_s28_t5" not in json.dumps(V2), "v2 plan already contains s28_t5?!"

plan = copy.deepcopy(V2)

# --- S07: replace cover-L15 with the warped s07_t2 line piece ---
s07 = plan["plan"]["S07"]
cover = [p for p in s07 if p["kind"] == "cover-L15"]
assert len(cover) == 1, f"expected exactly 1 cover-L15 piece, got {len(cover)}"
assert cover[0]["out"] == 32 and cover[0]["dst0"] == 51.468, cover[0]
warp = 1.34 / 2.56  # 0.5234375; playback 1.91x
assert round(61 * warp) == 32, round(61 * warp)
idx = s07.index(cover[0])
s07[idx] = {"take": "mv5_s07_t2", "sf": 0, "ef": 61, "warp": warp,
            "out": 32, "kind": "line-L15-warped",
            "dst0": 51.468, "dst1": 52.801}
assert sum(p["out"] for p in s07) == 234, sum(p["out"] for p in s07)
print("S07 total 234f OK")

# --- L15 word-start offsets, computed from sources ---
take_words = QC15["s07"]["word_times"]  # [word, start, end] x5
song_l15 = [r for r in SONG if r.get("line") == "L15"]
assert len(song_l15) == 5, len(song_l15)
offsets = []
for (tw, ts, _te), sr in zip(take_words, song_l15):
    assert tw.lower().strip() == sr["song_word"].lower().strip("."), (tw, sr)
    placed = ts * warp
    song_rel = sr["song_start"] - 51.46
    offsets.append({"word": tw, "take_start": ts, "placed_start": round(placed, 4),
                    "song_start_rel": round(song_rel, 4),
                    "offset": round(placed - song_rel, 4)})
print("L15 offsets (placed - song, s):")
for o in offsets:
    print(f"  {o['word']:6} take {o['take_start']:.2f} -> placed {o['placed_start']:.4f} "
          f"vs song {o['song_start_rel']:.4f}  offset {o['offset']:+.4f}")
import statistics
print(f"  max |offset| = {max(abs(o['offset']) for o in offsets):.3f}s; "
      f"median |offset| = {statistics.median(abs(o['offset']) for o in offsets):.3f}s")
assert max(abs(o["offset"]) for o in offsets) <= 0.50, "L15 offset outside working band!"
plan["scores"]["L15_warped_offsets"] = offsets
plan["scores"]["L15_warp"] = warp

# --- S21: replace all v2 pieces with 9 montage pieces ---
# (take, sf, ef, out, kind, dst0, dst1) — dst boundaries = v2 line boundaries
# REVISION 2026-11-06 ~03:40 EST (gate on build 1): the first montage used
# t14 156-182 for L85 and t15 84-108 for L87, but frame checks on the
# built master showed the GIRL visibly singing through both fragments
# (t14 girl mouth open 5.5-7.5s; t15 girl mouth open 3.5-4.5s) — wrong
# singer under CAT lines, the exact defect class v3 exists to fix.
# Both CAT lines now come from t13 (strongest cat-singing close-up,
# mouth verified open at f36-48 and f82-108). The four CAT lines need
# 99f from t13's 96f cat window (12-108), so ONE 3-frame overlap is
# unavoidable: t13 f36-39 appears in both L83 (12-39) and L87 (36-60),
# ~5.3s apart inside 1.1s montage cuts — imperceptible, disclosed.
MONTAGE = [
    ("mv5_s21_t12", 12, 37, 25, "montage-L82-GIRL", 158.06, 159.102),
    ("mv5_s21_t13", 12, 39, 27, "montage-L83-CAT", 159.102, 160.227),
    ("mv5_s21_t16", 12, 39, 27, "montage-L84-GIRL", 160.227, 161.352),
    ("mv5_s21_t13", 82, 108, 26, "montage-L85-CAT", 161.352, 162.435),
    ("mv5_s21_t11", 12, 38, 26, "montage-L86-GIRL", 162.435, 163.519),
    ("mv5_s21_t13", 36, 60, 24, "montage-L87-CAT", 163.519, 164.519),
    ("mv5_s21_t15", 132, 164, 32, "montage-L88-GIRL", 164.519, 165.852),
    ("mv5_s21_t13", 60, 82, 22, "montage-L89-CAT", 165.852, 166.769),
    ("mv5_s21_t14", 12, 30, 18, "tail", 166.769, 167.519),
]
# slice-window audit: every slice inside a QC-noted window, no slice reused
WINDOWS = {
    "mv5_s21_t11": [(12, 108), (132, 228)],   # girl 0.5-4.5s; two-shot 5.5-9.5s
    "mv5_s21_t12": [(0, 240)],                # girl throughout
    "mv5_s21_t13": [(12, 108)],               # cat 0.5-4.5s
    "mv5_s21_t14": [(12, 108), (156, 204)],   # wide 0.5-4.5s; cat 6.5-8.5s
    "mv5_s21_t15": [(84, 108), (132, 228)],   # cat 3.5-4.5s; girl 5.5-9.5s
    "mv5_s21_t16": [(12, 156)],               # girl 0.5-6.5s (cat 0.5-4.5s inside)
}
seen = set()
for take, sf, ef, out, kind, d0, d1 in MONTAGE:
    assert (ef - sf) == out, (take, sf, ef, out)
    assert any(a <= sf and ef <= b for a, b in WINDOWS[take]), (take, sf, ef)
    assert (take, sf, ef) not in seen, f"slice reused: {take} {sf}-{ef}"
    seen.add((take, sf, ef))
    assert abs((d1 - d0) * 24 - out) <= 1, (kind, d0, d1, out)
plan["plan"]["S21"] = [
    {"take": t, "sf": sf, "ef": ef, "warp": 1.0, "out": out, "kind": k,
     "dst0": d0, "dst1": d1}
    for t, sf, ef, out, k, d0, d1 in MONTAGE
]
assert sum(p["out"] for p in plan["plan"]["S21"]) == 227, \
    sum(p["out"] for p in plan["plan"]["S21"])
print("S21 total 227f OK")

# --- totals + forbidden-take audit ---
total = sum(p["out"] for sc in plan["scenes"] for p in plan["plan"][sc])
assert total == 4954, total
blob = json.dumps(plan)
assert "mv5_s28_t5" not in blob, "s28_t5 leaked into v3 plan!"
assert "mv5_s07_t3" not in blob, "s07_t3 leaked into v3 plan!"
assert "mv5_s21_t7" not in blob, "s21_t7 leaked into v3 plan!"
print(f"total frames {total} OK; s28_t5 / s07_t3 / s21_t7 absent from plan")

json.dump(plan, open(os.path.join(PROJ, "work", "assembly_fit_mv5_v3.json"), "w"), indent=1)
print("wrote work/assembly_fit_mv5_v3.json")
