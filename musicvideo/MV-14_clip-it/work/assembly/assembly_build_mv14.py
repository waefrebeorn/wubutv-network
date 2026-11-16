#!/usr/bin/env python3
"""MV-14 ASSEMBLY builder (assembly coordinator, 2026-11-12).

Pattern: MV-13 assembly_build_mv13.py (trim + setpts=PTS-STARTPTS +
setpts={factor}*PTS + fps=24; per-segment CRF-14 intermediates scaled
1280x720; manifest with md5/frames). MV-14 DIFFERS from MV-13 in the
warp method: MV-13 was uniform 1.000 everywhere (almost no mouth
events); MV-14 has ~40 singing scenes with visible mouths, and a
uniform span warp leaves per-word landing errors up to 0.66s. So MV-14
uses SWING-KEYFRAME + PER-WORD warping: keyframes on word onsets
(take word start -> song word start), sub-segments between keyframes
warped individually, each checked inside [0.5x, 2.0x]. A sub-segment
that cannot land in caps has its bounding keyframe dropped (the word
onset is then interpolated); if no keyframe set works, the scene falls
back to the uniform span warp and is logged.

Contract: 65 segments, boundaries = plan slot starts (with the five
adjudicated moves). Total = round(161.60*24) = 3878f (telescoping —
no drift). Video duration 3878f = 161.5833s; track audio 161.600s
(mux pads the 0.0167s tail, capped apad — see mux_mv14.py).

Special scenes (hand-built, see MV14_PROGRESS.md / ledger):
  S37 MOUTH ANCHOR: uniform f=1.000, a=0 (take audio lags its own
      mouth ~0.88s; the visual line is take 0-1.40, mouth wide open
      at frame 0; audio word times are NOT the sync authority).
  S38 PER-WORD DEGENERATE: take holds "Help" 1.34s vs song 0.18s — the
      keyframe dropper removes all word keyframes, leaving one
      sub-segment at 0.661x (the effective span warp). "Help" lands
      0.22s early; mouth-open at take 0.71s lands on "me" — disclosed.
  S39 BAD-WORD: "Clip" take [0,0.54] -> song [86.24,87.36] = 2.08x
      (4% past the 2x cap — DISCLOSED, mouth moving throughout, not
      frozen); "it" 7.45x UNWARPABLE -> fast cut to the take's own
      closed-mouth hands-working tail [0.76,0.93] for 87.36-87.54.
  S40 THREE-PART: S39-take tail [0.93,2.76] f=1.0 covers 87.54-89.38,
      then S40 take "Post" [3.78,4.30] -> 89.38-89.64 = 0.50x (at the
      floor), "it." [4.30,4.56] -> 89.64-89.90 = 1.17x.
  S43 UNIFORM line + tail: the take's three "No"s run long-short-medium
      vs the song's short-medium-long — no in-cap per-word warp exists
      (0.28x / 2.67x). Uniform span 0.857x for the line; the "No"s land
      ~0.4s late (DISCLOSED, mouth-open lands on the third "No").
      Tail take [1.44,3.57] stretched 1.53x to fill 95.24-98.50 —
      DISCLOSED: that span includes the take's repeat "No"x3 at
      1.6-3.06s, so the Editor visibly mouths three extra silent "No"s
      during the wordless gap (take audio is muted; head-shakes read
      as emphasis).
  S51 PER-WORD (dropper): the "it" keyframe drops, merging "post"+"it"
      into one 0.67x sub-segment; "it" onset lands 0.09s late.
  S55 PER-WORD (dropper): the "Don't" keyframe drops; the first 2.08s
      of take compress at 0.50x (at the floor). "Don't" lands 0.12s
      early (a clamps at 0); "overthink" lands 0.41s late — disclosed.
  S28 PER-WORD DEGENERATE: the take sings the line in 1.20s vs the
      song's 2.34s with the words bunched at the front; no in-cap
      per-word warp exists (first gap needs 4.67x). One sub-segment
      at 1.93x; all words land ~0.3s early — disclosed.
  S49: the song "it" (113.40-113.64) straddles the S49/S50 boundary at
      113.46; the keyframe dropper merges it into the previous
      sub-segment (onset lands ~0.11s early — disclosed).
  S22: two sub-segments land exactly at the caps (0.50x / 2.00x) —
      at the caps, not past them.

Usage: python3 work/assembly/assembly_build_mv14.py [--analyze] [--scene S33]
"""
import glob
import hashlib
import json
import os
import subprocess
import sys

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-14_clip-it"
TAKES = f"{BASE}/takes"
ASM = f"{BASE}/work/assembly"
SEG = f"{ASM}/seg"
MANIFEST = f"{ASM}/assembly_manifest.json"
TOTAL_FRAMES = 3878
FPS = 24

TABLE = json.load(open(f"{ASM}/scene_table.json"))
SONG = json.load(open(f"{ASM}/mv14_kinetic_words.json"))["words"]
TAKEW = json.load(open("/tmp/mv14_take_words.json"))
KEEPS = json.load(open("/tmp/mv14_keeps.json"))

# plan line spans: scene -> ((song_ls, song_le), (take_ts, take_te))
# (plan_mv14.py loads relative paths, so exec it from BASE)
_SRC = open(f"{ASM}/plan_mv14.py").read()
_NS = {}
_cwd = os.getcwd()
os.chdir(BASE)
try:
    exec(_SRC.split("def contract")[0], _NS)
finally:
    os.chdir(_cwd)
LINES, SLOTS = _NS["LINES"], _NS["SLOTS"]

FLOOR, CAP = 0.5, 2.0
EPS = 0.002  # rounding tolerance on the caps


def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def frames_of(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
         "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", path])
    return int(out.strip())


def contract_of(ss, se):
    return round(se * FPS) - round(ss * FPS)


def take_key(scene):
    t = KEEPS[scene]["take"]
    return scene if t == "t1" else scene + t.upper()


def resolve_takes():
    by_md5 = {}
    for p in glob.glob(os.path.join(TAKES, "*.mp4")):
        by_md5[md5_file(p)] = p
    missing = []
    for s, keep in KEEPS.items():
        if keep["md5"] not in by_md5:
            missing.append((s, keep["md5"]))
    assert not missing, f"takes missing for md5: {missing}"
    print(f"all 65 KEEP takes resolved by ledger md5 ({len(by_md5)} mp4s hashed)")
    return by_md5


def fr(t):
    """seconds -> nearest frame index"""
    return int(round(t * FPS))


def subseg_warps(keys):
    """keys = [(take_t, song_t), ...] sorted; returns list of
    (take_f0, take_f1, song_f0, song_f1, f) or None if any degenerate."""
    out = []
    for (t0, s0), (t1, s1) in zip(keys, keys[1:]):
        tf0, tf1 = fr(t0), fr(t1)
        sf0, sf1 = fr(s0), fr(s1)
        if tf1 <= tf0 or sf1 <= sf0:
            return None
        out.append((tf0, tf1, sf0, sf1, (sf1 - sf0) / (tf1 - tf0)))
    return out


def plan_perword(scene, ss, se, contract):
    """Per-word keyframe plan for a singing scene. Returns
    (subsegments, method, notes) where subsegments = list of
    (take_path_key, take_f0, take_f1, song_f0, song_f1, f)."""
    (ls, le), (ts, te) = LINES[scene]
    sw = [w for w in SONG if ls - 0.01 <= w["start"] < le]
    tw = [w for w in TAKEW.get(take_key(scene), [])
          if ts - 0.01 <= w["start"] < te]
    notes = []
    if not tw or not sw:
        return None, "uniform", ["no words in line span"]
    if len(tw) > len(sw):
        return None, "uniform", ["take words > song words (%d>%d)"
                                 % (len(tw), len(sw))]
    f_span = (le - ls) / (te - ts)
    a = ts - (ls - ss) / f_span
    a = max(0.0, a)
    # b: line ends at/after the segment end -> window ends at the take line end
    if sw and sw[-1]["end"] >= se - 0.02:
        b = tw[-1]["end"] if tw else a + contract / FPS / f_span
    else:
        b = a + contract / FPS / f_span
    keys = [(a, ss)]
    for w1, w2 in zip(sw, tw):
        if w2["start"] > a and w1["start"] > ss:
            keys.append((w2["start"], w1["start"]))
    if tw and sw and tw[-1]["end"] < b - 1e-9 and sw[-1]["end"] < se - 0.02:
        keys.append((tw[-1]["end"], sw[-1]["end"]))
    keys.append((b, se))
    # dedupe identical (take, song) pairs, keep order
    ded = []
    for k in keys:
        if not ded or ded[-1] != k:
            ded.append(k)
    keys = ded
    # greedy keyframe dropping until every sub-segment is in caps
    dropped = []
    while True:
        subs = subseg_warps(keys)
        if subs is None:
            # degenerate keyframe pair (same take or song frame) — drop the
            # middle keyframe that creates it (never the segment endpoints)
            for j in range(len(keys) - 1):
                if fr(keys[j + 1][0]) <= fr(keys[j][0]) or \
                   fr(keys[j + 1][1]) <= fr(keys[j][1]):
                    if j + 1 == len(keys) - 1:
                        if len(keys) <= 2:
                            return None, "uniform", [
                                "degenerate keyframes, no drop found"]
                        dropped.append(keys[j])
                        del keys[j]
                    else:
                        dropped.append(keys[j + 1])
                        del keys[j + 1]
                    break
            else:
                return None, "uniform", ["degenerate keyframes, no drop found"]
            continue
        bad = [(i, s) for i, s in enumerate(subs)
               if s[4] < FLOOR - EPS or s[4] > CAP + EPS]
        if not bad:
            break
        if len(keys) <= 2:
            return None, "uniform", ["caps unfixable (%d bad sub-segments)"
                                      % len(bad)]
        # drop the interior keyframe bounding the worst violation; try both
        # sides, keep the one whose merged warp lands in caps (closer to 1.0)
        i, worst = max(bad, key=lambda p: max(FLOOR - p[1][4], p[1][4] - CAP))
        best = None
        for j in (i, i + 1):
            if j == 0 or j == len(keys) - 1:
                continue
            trial = keys[:j] + keys[j + 1:]
            tsubs = subseg_warps(trial)
            if tsubs is None:
                continue
            merged = tsubs[i if j == i + 1 else i - 1]
            score = abs(merged[4] - 1.0)
            ok = FLOOR - EPS <= merged[4] <= CAP + EPS
            if best is None or (ok and not best[0]) or \
               (ok == best[0] and score < best[1]):
                best = (ok, score, j)
        if best is None:
            return None, "uniform", ["no droppable keyframe fixes the caps"]
        dropped.append(keys[best[2]])
        del keys[best[2]]
    subs = subseg_warps(keys)
    assert subs is not None
    assert sum(s[3] - s[2] for s in subs) == contract, \
        f"{scene}: sub-segments sum != contract"
    out = [(scene, s[0], s[1], s[2], s[3], round(s[4], 4))
           for s in subs]
    if dropped:
        notes.append("dropped keyframes: %s"
                     % ", ".join(f"take {d[0]:.2f}/song {d[1]:.2f}"
                                 for d in dropped))
    for s in subs:
        if abs(s[4] - FLOOR) < 0.01 or abs(s[4] - CAP) < 0.01:
            notes.append(f"at-cap warp {s[4]:.3f}x "
                         f"(take f{s[0]}-{s[1]} -> song f{s[2]}-{s[3]})")
    return out, "per-word", notes


def plan_uniform(scene, ss, se, contract, f_span, a_span):
    """Single sub-segment from the scene table's span warp."""
    tf0 = fr(a_span)
    take_frames = int(round(contract / f_span))
    tf1 = tf0 + take_frames
    f = contract / take_frames
    sf0, sf1 = fr(ss), fr(se)
    assert tf1 <= 240, f"{scene}: take window past 240f"
    assert FLOOR - EPS <= f <= CAP + EPS, f"{scene}: span warp {f:.3f} out of caps"
    return [(scene, tf0, tf1, sf0, sf1, round(f, 4))]


def plan_scene(scene):
    row = next(r for r in TABLE if r["scene"] == scene)
    ss, se, contract = row["ss"], row["se"], row["frames"]
    assert contract == contract_of(ss, se)
    f_span, a_span = row["f"], row["a"]
    if scene == "S37":
        return (plan_uniform(scene, ss, se, contract, 1.0, 0.0),
                "uniform-mouth-anchor",
                ["take audio lags mouth ~0.88s; visual line take 0-1.40"])
    if scene == "S39":
        subs = [("S39", 0, fr(0.54), fr(86.24), fr(87.36), 0),
                ("S39", fr(0.76), fr(0.93), fr(87.36), fr(87.54), 0)]
        subs = [(k, t0, t1, s0, s1, round((s1 - s0) / (t1 - t0), 4))
                for k, t0, t1, s0, s1, _ in subs]
        return subs, "special-bad-word", [
            '"Clip" 2.077x (4% past the 2x cap — DISCLOSED, mouth moving '
            'throughout, not frozen)',
            '"it" 7.45x UNWARPABLE -> fast cut to take tail [0.76,0.93]']
    if scene == "S40":
        subs = [("S39", fr(0.93), fr(2.76), fr(87.54), fr(89.38), 0),
                ("S40", fr(3.78), fr(4.30), fr(89.38), fr(89.64), 0),
                ("S40", fr(4.30), fr(4.56), fr(89.64), fr(89.90), 0)]
        subs = [(k, t0, t1, s0, s1, round((s1 - s0) / (t1 - t0), 4))
                for k, t0, t1, s0, s1, _ in subs]
        return subs, "special-three-part", [
            'S39-take tail covers 87.54-89.38 at 1.0x; "Post" 0.50x (at '
            'the floor); "it." 1.17x']
    if scene == "S43":
        subs = [("S43", 0, fr(1.44), fr(94.02), fr(95.24), 0),
                ("S43", fr(1.44), fr(3.57), fr(95.24), fr(98.50), 0)]
        subs = [(k, t0, t1, s0, s1, round((s1 - s0) / (t1 - t0), 4))
                for k, t0, t1, s0, s1, _ in subs]
        return subs, "special-uniform+tail", [
            'line uniform 0.857x — "No"s land ~0.4s late (take rhythm '
            'long-short-medium vs song short-medium-long; mouth-open '
            'lands on the third "No")',
            'tail 1.53x includes the take\'s repeat "No"x3 at 1.6-3.06s — '
            'Editor visibly mouths three extra silent "No"s in the gap']
    if scene in LINES:
        subs, method, notes = plan_perword(scene, ss, se, contract)
        if subs is not None:
            return subs, method, notes
        notes = ["per-word unworkable: " + "; ".join(notes),
                 "falling back to uniform span warp %.3fx" % f_span]
        return (plan_uniform(scene, ss, se, contract, f_span, a_span),
                "uniform-fallback", notes)
    return (plan_uniform(scene, ss, se, contract, f_span, a_span),
            "uniform-wordless", [row["note"]] if row["note"] != "wordless" else [])


def analyze():
    total = 0
    methods = {}
    for row in TABLE:
        s = row["scene"]
        subs, method, notes = plan_scene(s)
        total += sum(x[4] - x[3] for x in subs)
        methods[method] = methods.get(method, 0) + 1
        worst = max(x[5] for x in subs)
        print(f"{s} {row['ss']:6.2f}-{row['se']:6.2f} {row['frames']:3d}f "
              f"{method:20} {len(subs)} sub-seg, slowest {worst:.3f}x")
        for n in notes:
            print(f"     - {n}")
        for x in subs:
            if x[5] > CAP + EPS:
                print(f"     *** OVER CAP: {x}")
    print(f"TOTAL FRAMES: {total} (expect {TOTAL_FRAMES})")
    print("methods:", methods)
    assert total == TOTAL_FRAMES, f"total {total} != {TOTAL_FRAMES}"
    print("CONTRACT OK")


def build_scene(scene, by_md5, force=False):
    row = next(r for r in TABLE if r["scene"] == scene)
    contract = row["frames"]
    dst = os.path.join(SEG, f"{scene}.mp4")
    if not force and os.path.exists(dst):
        n = frames_of(dst)
        if n == contract:
            print(f"{scene}: exists {n}f — skipping")
            return {"scene": scene, "song": [row["ss"], row["se"]],
                    "frames": n, "path": dst, "md5": md5_file(dst),
                    "built": True}
        print(f"{scene}: exists {n}f != {contract}f — rebuilding")
    subs, method, notes = plan_scene(scene)
    assert sum(x[4] - x[3] for x in subs) == contract
    parts = []
    labels = []
    for i, (tkey, tf0, tf1, sf0, sf1, f) in enumerate(subs):
        take_path = by_md5[KEEPS[tkey]["md5"]]
        parts.append(
            f"[{i}:v]trim=start_frame={tf0}:end_frame={tf1},"
            f"setpts=PTS-STARTPTS,setpts={f:.6f}*PTS,fps=24[v{i}]")
        labels.append(f"[v{i}]")
    fc = ";".join(parts)
    if len(subs) > 1:
        fc += f";{''.join(labels)}concat=n={len(subs)}:v=1:a=0[vc]"
        vlabel = "[vc]"
    else:
        vlabel = "[v0]"
    fc += (f";{vlabel}scale=1280:720:flags=lanczos,setsar=1,"
           f"trim=end_frame={contract}[v]")
    inputs = []
    for tkey, *_ in subs:
        inputs += ["-i", by_md5[KEEPS[tkey]["md5"]]]
    cmd = ["ffmpeg", "-y", "-v", "error"] + inputs + [
        "-filter_complex", fc, "-map", "[v]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "14",
        "-pix_fmt", "yuv420p", "-r", "24", "-frames:v", str(contract),
        "-an", dst]
    subprocess.run(cmd, check=True)
    n = frames_of(dst)
    assert n == contract, f"{scene}: built {n}f != {contract}f"
    print(f"{scene}: built {n}f ({method}, {len(subs)} sub-seg) "
          f"md5 {md5_file(dst)[:12]}...")
    return {"scene": scene, "song": [row["ss"], row["se"]], "frames": n,
            "path": dst, "md5": md5_file(dst), "built": True,
            "method": method, "notes": notes,
            "subsegments": [{"take": k, "take_frames": [t0, t1],
                             "song_frames": [s0, s1], "warp": f}
                            for k, t0, t1, s0, s1, f in subs]}


def main():
    os.makedirs(SEG, exist_ok=True)
    only = sys.argv[sys.argv.index("--scene") + 1] if "--scene" in sys.argv else None
    if "--analyze" in sys.argv:
        analyze()
        return
    by_md5 = resolve_takes()
    man = []
    if os.path.exists(MANIFEST):
        man = json.load(open(MANIFEST))
    done = {e["scene"]: e for e in man}
    for row in TABLE:
        s = row["scene"]
        if only and s != only:
            continue
        e = build_scene(s, by_md5)
        done[s] = e
        json.dump([done[r["scene"]] for r in TABLE if r["scene"] in done],
                  open(MANIFEST, "w"), indent=1)
    tot = sum(done[r["scene"]]["frames"] for r in TABLE if r["scene"] in done)
    print(f"segments done: {len(done)}/65, frames {tot} (expect {TOTAL_FRAMES})")
    if len(done) == 65:
        assert tot == TOTAL_FRAMES
        print("ALL SEGMENTS BUILT — total exactly 3878f")


if __name__ == "__main__":
    main()
