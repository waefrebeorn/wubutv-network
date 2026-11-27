#!/usr/bin/env python3
"""G8 MEASURED SYNC — Tier B v1 (MAR-primary master sync gate).

Spec: research_notes/lipsync-fix-20261122/AGGREGATE.md section 4 + L25-L31.
Measures per-word mouth-anchor error e = t_mouth - t_song ON THE FINISHED
MASTER. Mouth anchor = MAR (mouth aspect ratio) rising edge, from MediaPipe
Face Mesh RAW landmark geometry (landmarks 13/14 over 61/291). Blendshape
coefficients are never used (L31). Openness only, never frame-diff
(MOUTH-OPENNESS RULE).

REPORT-ONLY: this gate is under validation (Phase 0-2). It blocks nothing.

Inputs:
  --master     finished master mp4
  --words      SONG_WORDS.json (any house format: {words:[{word,start,end}]},
               [{word,start,end}], [{t0,t1,word}], or {lines:[{words:[[w,t0,t1,..]]}]})
  --segments   normalized inserts JSON: [{label,start,end,kind: sing|cover}]
               (optional; fallback = lyric-line grouping, all scored as sing)
  --e0         house zero in FRAMES (calibrated on positives; default 0)
  --bands      optional JSON overriding FAIL/WARN band lines (recalibration)
  --out        sync_gate.json output path
  --text-out   GATE_LOG-ready markdown section path
  --mar-cache  .npz cache for the MAR/presence series (reused on re-runs)

Tier 2 (windowed SyncNet) is NOT in v1: the window-jump statistic is computed
from MAR line-window medians instead and labelled source=mar_windows.
The envelope cross-check uses the master mix audio (no Demucs stem cached
for the validation corpus); labelled source=mix_envelope.
"""
import argparse, json, math, os, subprocess, sys
import numpy as np

FPS_DEFAULT = 24.0

BANDS = {
    # statistic: (pass_max, warn_max) for |value|-style stats; shares in [0,1]
    "bias_f":        (1.0, 2.0),    # |median e'|
    "late_share":    (0.10, 0.25),  # frac e' > +1f
    "early_share":   (0.10, 0.25),  # frac e' < -3f
    "scatter_f":     (1.0, 1.5),    # MAD of e'
    "drift_f":       (1.0, 2.0),    # |drift| end-to-end
    "gap_score":     (0.80, 0.65),  # PASS >= 0.80, WARN >= 0.65 (higher better)
    "jump_f":        2.0,           # any window step >= this = FAIL
    "cov_full":      0.80,          # coverage >= -> scored
    "cov_warn":      0.60,          # coverage >= -> scored capped WARN; below -> INCONCLUSIVE
}

# ---------------------------------------------------------------- words ----
def load_words(path):
    d = json.load(open(path))
    words = []
    if isinstance(d, dict) and "words" in d and isinstance(d["words"], list) and d["words"] and isinstance(d["words"][0], dict):
        for w in d["words"]:
            words.append((str(w.get("word", "")).strip(), float(w["start"]), float(w["end"])))
    elif isinstance(d, dict) and "lines" in d:
        for ln in d["lines"]:
            for w in ln.get("words", []):
                words.append((str(w[0]).strip(), float(w[1]), float(w[2])))
    elif isinstance(d, list):
        for w in d:
            if "start" in w:
                words.append((str(w.get("word", "")).strip(), float(w["start"]), float(w["end"])))
            else:
                words.append((str(w.get("word", "")).strip(), float(w["t0"]), float(w["t1"])))
    words = [w for w in words if w[2] > w[1]]
    words.sort(key=lambda x: x[1])
    return words

# ------------------------------------------------------------- segments ----
def load_segments(path, words):
    """Return (inserts, source). inserts: [{label,start,end,kind}] sorted."""
    if path:
        raw = json.load(open(path))
        ins = [{"label": s.get("label", f"S{i+1:02d}"), "start": float(s["start"]),
                "end": float(s["end"]), "kind": s.get("kind", "sing")}
               for i, s in enumerate(raw)]
        ins.sort(key=lambda s: s["start"])
        return ins, "segment_map"
    # fallback: lyric-line grouping (gap >= 0.9 s between word end and next start)
    ins, cur = [], None
    for (w, s, e) in words:
        if cur is None or s - cur["end"] >= 0.9:
            cur = {"label": f"L{len(ins)+1:02d}", "start": s, "end": e, "kind": "sing"}
            ins.append(cur)
        else:
            cur["end"] = max(cur["end"], e)
    return ins, "line_grouping_fallback"

def assign_words(inserts, words):
    """Each word goes to the insert containing its onset; else nearest insert
    whose span is within 0.35 s of the onset; else unassigned."""
    out = {i: [] for i in range(len(inserts))}
    unassigned = []
    for wi, (w, s, e) in enumerate(words):
        hit = None
        for i, ins in enumerate(inserts):
            if ins["start"] - 1e-9 <= s < ins["end"]:
                hit = i; break
        if hit is None:
            best, bd = None, 0.35
            for i, ins in enumerate(inserts):
                d = max(ins["start"] - s, s - ins["end"], 0.0)
                if d < bd: best, bd = i, d
            hit = best
        if hit is None: unassigned.append(wi)
        else: out[hit].append(wi)
    return out, unassigned

# ------------------------------------------------------------------ MAR ----
def extract_mar(master, cache_path):
    """Per-frame MAR + FaceMesh presence + YuNet presence. Cached to .npz.
    The cache is checkpointed every 500 frames (complete=False) and RESUMED
    on the next call — this VM reboots and kills long processes, so an
    all-or-nothing cache loses hours."""
    resume = 0
    mar, fmp, ynp = [], [], []
    if cache_path and os.path.exists(cache_path):
        z = np.load(cache_path)
        if "complete" not in z:  # pre-checkpoint cache format: ignore
            pass
        elif bool(z["complete"]):
            return z["mar"], z["fm_present"], z["yunet_present"], float(z["fps"])
        else:
            resume = int(z["n_done"])
            mar = list(z["mar"]); fmp = list(z["fm_present"]); ynp = list(z["yunet_present"])
            print(f"  MAR resume at frame {resume}", file=sys.stderr, flush=True)
    import cv2
    import mediapipe as mp
    from mediapipe.tasks.python import BaseOptions
    from mediapipe.tasks.python.vision import (FaceLandmarker, FaceLandmarkerOptions,
                                               RunningMode)
    cap = cv2.VideoCapture(master)
    fps = cap.get(cv2.CAP_PROP_FPS) or FPS_DEFAULT
    W0 = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)); H0 = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Landmark at reduced width: MAR is a ratio of distances (scale-free), and
    # full-720p inference is CPU-prohibitive on this VM. Presence rates are
    # therefore "at 768w" — recorded as such in the cache metadata consumers.
    SCALE = 768.0 / W0 if W0 > 768 else 1.0
    W = int(W0 * SCALE); H = int(H0 * SCALE)
    here = os.path.dirname(os.path.abspath(__file__))
    # YuNet (Tier 0 presence audit)
    yunet = None
    model = os.path.join(here, "face_detection_yunet_2023mar.onnx")
    if os.path.exists(model):
        try: yunet = cv2.FaceDetectorYN.create(model, "", (W, H), 0.6, 0.3, 50)
        except Exception: yunet = None
    # Face Mesh via the Tasks FaceLandmarker (mediapipe >= 1.x removed the
    # legacy solutions API). VIDEO mode = detection + tracking. Landmarks are
    # the same 478-point Face Mesh topology; RAW geometry only, blendshape
    # outputs are never requested (L31).
    opts = FaceLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=os.path.join(here, "face_landmarker.task")),
        running_mode=RunningMode.VIDEO, num_faces=1,
        min_face_detection_confidence=0.4, min_tracking_confidence=0.4)
    fm = FaceLandmarker.create_from_options(opts)
    if resume:
        cap.set(cv2.CAP_PROP_POS_FRAMES, resume)
    # Estimator v2 (validation fix): YuNet-guided crop fallback. The
    # landmarker's own detector misses stylised cartoon faces that YuNet
    # finds reliably; on a missed frame, crop the YuNet box (padded) and
    # run a second landmarker in IMAGE mode on the crop. Landmarks remain
    # pure Face Mesh geometry; YuNet only proposes the region.
    fm_img = None
    if yunet is not None:
        fm_img = FaceLandmarker.create_from_options(FaceLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=os.path.join(here, "face_landmarker.task")),
            running_mode=RunningMode.IMAGE, num_faces=1,
            min_face_detection_confidence=0.3, min_tracking_confidence=0.3))
    idx = resume
    def checkpoint(complete):
        if not cache_path: return
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        np.savez_compressed(cache_path, mar=np.array(mar, dtype=np.float64),
                            fm_present=np.array(fmp), yunet_present=np.array(ynp),
                            fps=fps, n_done=len(mar), complete=complete)
    while True:
        ok, frame = cap.read()
        if not ok: break
        if SCALE != 1.0:
            frame = cv2.resize(frame, (W, H), interpolation=cv2.INTER_AREA)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        res = fm.detect_for_video(img, int(round(idx / fps * 1000.0)))
        m = np.nan; present = False
        yp = False; ybox = None
        # YuNet runs on landmarker misses (fallback box) and every 6th frame
        # (presence audit series, forward-filled) — not on every frame.
        need_yunet = (yunet is not None
                      and (not res.face_landmarks or idx % 6 == 0))
        if need_yunet:
            yunet.setInputSize((W, H))
            _, faces = yunet.detect(frame)
            if faces is not None and len(faces) > 0:
                yp = True
                # largest YuNet box
                areas = faces[:, 2] * faces[:, 3]
                ybox = faces[int(np.argmax(areas))]
        elif ynp:
            yp = ynp[-1]  # forward-fill audit sample
        if res.face_landmarks:
            lm = res.face_landmarks[0]
            def px(i): return np.array([lm[i].x * W, lm[i].y * H])
            vert = np.linalg.norm(px(13) - px(14))
            horiz = np.linalg.norm(px(61) - px(291))
            if horiz > 1e-6:
                m = vert / horiz; present = True
        if not present and fm_img is not None and ybox is not None:
            bx, by, bw, bh = [float(v) for v in ybox[:4]]
            pad = 0.35
            x0 = max(0, int(bx - pad * bw)); y0 = max(0, int(by - pad * bh))
            x1 = min(W, int(bx + bw * (1 + pad))); y1 = min(H, int(by + bh * (1 + pad)))
            if x1 - x0 >= 24 and y1 - y0 >= 24:
                crop = rgb[y0:y1, x0:x1]
                if crop.shape[1] < 256:
                    crop = cv2.resize(crop, (256, int(256 * crop.shape[0] / crop.shape[1])),
                                      interpolation=cv2.INTER_CUBIC)
                cimg = mp.Image(image_format=mp.ImageFormat.SRGB, data=crop)
                cres = fm_img.detect(cimg)
                if cres.face_landmarks:
                    lm = cres.face_landmarks[0]
                    ch, cw = crop.shape[:2]
                    def px(i): return np.array([lm[i].x * cw, lm[i].y * ch])
                    vert = np.linalg.norm(px(13) - px(14))
                    horiz = np.linalg.norm(px(61) - px(291))
                    if horiz > 1e-6:
                        m = vert / horiz; present = True
        mar.append(m); fmp.append(present)
        ynp.append(yp)
        idx += 1
        if idx % 250 == 0: checkpoint(False)
        if idx % 1000 == 0: print(f"  MAR frames: {idx}", file=sys.stderr, flush=True)
    cap.release(); fm.close()
    if fm_img is not None: fm_img.close()
    checkpoint(True)
    return np.array(mar, dtype=np.float64), np.array(fmp), np.array(ynp), fps

def smooth(x, k=3):
    if k <= 1: return x.copy()
    pad = k // 2
    xp = np.pad(x, pad, mode="edge")
    return np.convolve(xp, np.ones(k) / k, mode="valid")

# --------------------------------------------------------------- anchors ----
def find_edges(mar_s, fps, t0, t1, baseline, rng, present=None):
    """Upward crossings of baseline+25% range inside [t0,t1] (seconds, master
    time). Returns list of (cross_time_s, peak_time_s).
    Estimator v3: a crossing counts only where the face was actually
    MEASURED at both the crossing frame and the peak frame (present[]).
    The MAR series is interpolated across face-missing spans for display /
    gap purposes, but edges on fabricated ramps are not measurements and
    poisoned the v2 matcher (Phase 0: scatter MAD ~9f, coverage collapse)."""
    thr = baseline + 0.25 * rng
    i0 = max(0, int(math.floor(t0 * fps))); i1 = min(len(mar_s), int(math.ceil(t1 * fps)))
    edges = []
    i = i0 + 1
    while i < i1:
        a, b = mar_s[i - 1], mar_s[i]
        if np.isfinite(a) and np.isfinite(b) and a < thr <= b:
            tc = (i - 1 + (thr - a) / max(b - a, 1e-9)) / fps
            # peak = next local max after crossing
            j = i; peak = b; peak_t = i / fps
            while j < i1 and np.isfinite(mar_s[j]):
                if mar_s[j] >= peak: peak, peak_t = mar_s[j], j / fps; j += 1
                elif mar_s[j] < thr: break
                else: j += 1
            if present is None:
                edges.append((tc, peak_t))
            else:
                pk = min(int(round(peak_t * fps)), len(present) - 1)
                def near(k):
                    lo, hi = max(0, k - 1), min(len(present), k + 2)
                    return int(present[lo:hi].sum()) >= 2
                if near(i) and near(pk):
                    edges.append((tc, peak_t))
            i = max(j, i + 1)
        else:
            i += 1
    return edges

def match_words(word_list, edges, fps):
    """Monotonic greedy sequence match. word_list: [(word,start,end)].
    Candidate edge for a word: crossing whose PEAK falls within +-0.6 s of the
    word onset. Each edge used once; edges consumed in time order.
    Returns {word_index_in_list: (edge_time_s, e_frames)}."""
    used = [False] * len(edges)
    matched = {}
    last_edge_t = -1e18
    for wi, (w, s, e) in enumerate(word_list):
        best = None
        for ei, (tc, tp) in enumerate(edges):
            if used[ei] or tc <= last_edge_t: continue
            if abs(tp - s) <= 0.6:
                if best is None or tc < edges[best][0]: best = ei
        if best is not None:
            used[best] = True
            tc = edges[best][0]
            last_edge_t = tc
            matched[wi] = (tc, (tc - s) * fps)
    return matched

# -------------------------------------------------------------- envelope ----
def envelope_offset(master, mar, fps, a, b):
    """Band-limited (2-7 Hz) cross-correlation offset between the MAR curve
    and the master-audio RMS envelope over [a,b] seconds. Returns seconds
    (positive = mouth after audio) or None. Source: mix envelope."""
    try:
        import scipy.signal as sig
        wav = "/tmp/_sg_env_%d.wav" % os.getpid()
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-to", str(b),
                        "-i", master, "-ac", "1", "-ar", "16000", wav], check=True)
        import wave, contextlib
        with contextlib.closing(wave.open(wav)) as wf:
            n = wf.getnframes(); sr = wf.getframerate()
            audio = np.frombuffer(wf.readframes(n), dtype=np.int16).astype(np.float64) / 32768.0
        os.unlink(wav)
        if len(audio) < sr * 0.5: return None
        hop = int(sr * 0.01)
        env = np.sqrt(np.convolve(audio ** 2, np.ones(hop) / hop, mode="same"))
        rate = 100.0
        t_env = np.arange(len(env)) * (hop / sr)
        i0, i1 = int(a * fps), min(len(mar), int(b * fps))
        seg = mar[i0:i1].copy()
        if np.sum(np.isfinite(seg)) < 20: return None
        idx = np.arange(len(seg)); good = np.isfinite(seg)
        seg = np.interp(idx, idx[good], seg[good])
        t_mar = np.arange(len(seg)) / fps
        grid = np.arange(0, min(t_env[-1], t_mar[-1]), 1.0 / rate)
        if len(grid) < 50: return None
        e_i = np.interp(grid, t_env, env); m_i = np.interp(grid, t_mar, seg)
        sos = sig.butter(2, [2, 7], btype="bandpass", fs=rate, output="sos")
        e_f = sig.sosfiltfilt(sos, e_i - e_i.mean()); m_f = sig.sosfiltfilt(sos, m_i - m_i.mean())
        if e_f.std() < 1e-9 or m_f.std() < 1e-9: return None
        corr = sig.correlate(m_f, e_f, mode="full") / (len(grid) * e_f.std() * m_f.std())
        lags = sig.correlation_lags(len(m_f), len(e_f), mode="full") / rate
        m_ = np.abs(lags) <= 0.6
        if not m_.any(): return None
        return float(lags[m_][np.argmax(corr[m_])])
    except Exception as ex:
        print(f"  envelope cross-check failed: {ex}", file=sys.stderr)
        return None

# ------------------------------------------------------------ statistics ----
def theil_drift(ts, es):
    """End-to-end drift (frames) from a Theil-Sen fit of e vs t."""
    if len(ts) < 4:
        return float(es[-1] - es[0]) if len(es) >= 2 else 0.0
    from scipy.stats import theilslopes
    slope, intercept, _, _ = theilslopes(es, ts, alpha=0.68)
    return float(slope * (ts[-1] - ts[0]))

def band_verdict(v, pass_max, warn_max, higher_better=False):
    if v is None: return None
    if higher_better:
        return "PASS" if v >= pass_max else ("WARN" if v >= warn_max else "FAIL")
    return "PASS" if v <= pass_max else ("WARN" if v <= warn_max else "FAIL")

def worst(a, b):
    order = {"PASS": 0, "WARN": 1, "FAIL": 2}
    if a is None: return b
    if b is None: return a
    return a if order[a] >= order[b] else b

# ------------------------------------------------------------------ main ----
def run_gate(master, words_path, segments_path, e0_frames, bands, out_path,
             text_out, mar_cache):
    words = load_words(words_path)
    inserts, ins_source = load_segments(segments_path, words)
    assign, unassigned = assign_words(inserts, words)
    mar_raw, fm_present, yunet_present, fps = extract_mar(master, mar_cache)
    finite = np.isfinite(mar_raw)
    mar_filled = mar_raw.copy()
    if finite.sum() > 0:
        idx = np.arange(len(mar_raw))
        mar_filled[~finite] = np.interp(idx[~finite], idx[finite], mar_raw[finite])
    # Estimator v2 (VALIDATED CONFIG): 3-frame moving average. A v3
    # experiment (median-3 + presence-gated edges) was tried after Phase 0
    # and REVERTED: it destroyed narrow mouth excursions and collapsed
    # coverage further (FH-A 0.45 -> 0.18). See gate_validation/VALIDATION.md.
    mar_s = smooth(mar_filled, 3)
    B = bands
    results = []
    cover_list = []
    for ii, ins in enumerate(inserts):
        widx = assign[ii]
        wlist = [words[j] for j in widx]
        f0 = max(0, int(math.floor(ins["start"] * fps)))
        f1 = min(len(mar_raw), int(math.ceil(ins["end"] * fps)))
        face_frames = int(fm_present[f0:f1].sum()) if f1 > f0 else 0
        tot_frames = max(f1 - f0, 0)
        face_rate = (face_frames / tot_frames) if tot_frames else 0.0
        rec = {"label": ins["label"], "start": ins["start"], "end": ins["end"],
               "kind": ins["kind"], "n_words": len(wlist),
               "face_presence_rate": round(face_rate, 4),
               "yunet_presence_rate": round(float(yunet_present[f0:f1].mean()), 4) if tot_frames else 0.0}
        if ins["kind"] == "cover":
            rec["verdict"] = "COVER (unscored)"
            cover_list.append(ins["label"]); results.append(rec); continue
        if not wlist:
            rec["verdict"] = "NO WORDS (unscored)"; results.append(rec); continue
        seg_mar = mar_s[f0:f1]
        finite_seg = seg_mar[np.isfinite(seg_mar)]
        if len(finite_seg) < 10:
            rec.update({"coverage": 0.0, "verdict": "INCONCLUSIVE",
                        "note": "no usable MAR signal in insert"})
            results.append(rec); continue
        baseline = float(np.percentile(finite_seg, 10))
        rng = float(np.percentile(finite_seg, 95) - baseline)
        rec["mar_baseline"] = round(baseline, 4); rec["mar_range"] = round(rng, 4)
        if rng < 0.02:
            rec.update({"coverage": 0.0, "verdict": "INCONCLUSIVE",
                        "note": "MAR range too small (mouth never opens measurably)"})
            results.append(rec); continue
        edges = find_edges(mar_s, fps, ins["start"], ins["end"], baseline, rng)
        matched = match_words(wlist, edges, fps)
        coverage = len(matched) / len(wlist)
        rec["coverage"] = round(coverage, 4)
        rec["n_anchored"] = len(matched)
        # gap score: song-silent gaps >= 0.5 s inside insert, face visible,
        # excluding 3f before next onset
        closed_thr = baseline + 0.15 * rng
        gap_frames = gap_closed = 0
        spans = []
        prev_end = ins["start"]
        for (w, s, e) in wlist:
            spans.append((prev_end, s)); prev_end = max(prev_end, e)
        spans.append((prev_end, ins["end"]))
        for (ga, gb) in spans:
            gb2 = gb - 3.0 / fps
            if gb2 - ga < 0.5: continue
            g0 = max(0, int(ga * fps)); g1 = min(len(mar_raw), int(gb2 * fps))
            vis = fm_present[g0:g1]
            if vis.sum() == 0: continue
            gap_frames += int(vis.sum())
            gap_closed += int(np.sum(mar_s[g0:g1][vis] <= closed_thr))
        gap_score = (gap_closed / gap_frames) if gap_frames >= 12 else None
        rec["gap_score"] = (round(gap_score, 4) if gap_score is not None else None)
        rec["gap_frames"] = gap_frames
        env_off = envelope_offset(master, mar_s, fps, ins["start"], ins["end"])
        rec["envelope_offset_f"] = (round(env_off * fps, 3) if env_off is not None else None)
        if coverage < B["cov_warn"]:
            rec["verdict"] = "INCONCLUSIVE"
            rec["note"] = "coverage < 60%"
            if matched:
                es = np.array([v[1] for v in matched.values()])
                rec["raw_bias_f"] = round(float(np.median(es)), 3)
            results.append(rec); continue
        es = np.array([matched[k][1] for k in sorted(matched)])
        ts = np.array([wlist[k][1] for k in sorted(matched)])
        eprime = es - e0_frames
        bias = float(np.median(eprime))
        mad = float(np.median(np.abs(eprime - np.median(eprime))))
        late = float(np.mean(eprime > 1.0)); early = float(np.mean(eprime < -3.0))
        drift = theil_drift(ts, eprime)
        # window jumps from MAR line-window medians (Tier 2 SyncNet skipped in v1)
        wins = []
        cur = [0]
        for k in range(1, len(ts)):
            if ts[k] - wlist[sorted(matched)[k - 1]][2] >= 0.9 and len(cur) >= 1:
                wins.append(cur); cur = []
            cur.append(k)
        if cur: wins.append(cur)
        merged = []
        for wn in wins:
            if merged and (ts[wn[0]] - ts[merged[-1][-1]] < 1.5):
                merged[-1] = merged[-1] + wn
            else: merged.append(list(wn))
        win_off = [float(np.median(eprime[wn])) for wn in merged if len(wn) >= 1]
        jumps = []
        for k in range(1, len(win_off)):
            if abs(win_off[k] - win_off[k - 1]) >= B["jump_f"]:
                jumps.append({"frame": int(round(ts[merged[k][0]] * fps)),
                              "step_f": round(win_off[k] - win_off[k - 1], 3)})
        stats = {"bias_f": round(bias, 3), "late_share": round(late, 4),
                 "early_share": round(early, 4), "scatter_mad_f": round(mad, 3),
                 "drift_f": round(drift, 3), "jumps": jumps,
                 "window_offsets_f": [round(x, 2) for x in win_off]}
        verdicts = {
            "bias": band_verdict(abs(bias), *B["bias_f"]),
            "late": band_verdict(late, *B["late_share"]),
            "early": band_verdict(early, *B["early_share"]),
            "scatter": band_verdict(mad, *B["scatter_f"]),
            "drift": band_verdict(abs(drift), *B["drift_f"]),
            "gap": band_verdict(gap_score, *B["gap_score"], higher_better=True),
            "jumps": ("FAIL" if jumps else "PASS"),
        }
        v = "PASS"
        for x in verdicts.values(): v = worst(v, x)
        if coverage < B["cov_full"] and v == "PASS": v = "WARN"
        if coverage < B["cov_full"]:
            verdicts["coverage_cap"] = "WARN"
        # worst words by |e'|
        order = np.argsort(-np.abs(eprime))[:5]
        stats["worst_words"] = [{"word": wlist[sorted(matched)[k]][0],
                                 "frame": int(round(ts[k] * fps)),
                                 "e_f": round(float(eprime[k]), 2)} for k in order]
        stats["per_word_e_f"] = [round(float(x), 2) for x in eprime]
        stats["word_onsets_s"] = [round(float(x), 3) for x in ts]
        rec["stats"] = stats; rec["stat_verdicts"] = verdicts; rec["verdict"] = v
        results.append(rec)
    # master composition (CineQC rule, L26)
    scored = [r for r in results if r.get("verdict") in ("PASS", "WARN", "FAIL", "INCONCLUSIVE")]
    if any(r["verdict"] == "FAIL" for r in scored): master_verdict = "FAIL"
    elif any(r["verdict"] in ("WARN", "INCONCLUSIVE") for r in scored): master_verdict = "PASS WITH FLAGS"
    elif scored: master_verdict = "PASS"
    else: master_verdict = "INCONCLUSIVE (no scored inserts)"
    out = {"gate": "G8 MEASURED SYNC (Tier B v1, MAR primary)",
           "report_only": True,
           "master": master, "fps": fps, "e0_frames": e0_frames,
           "bands": B, "insert_source": ins_source,
           "landmark_input_width": 768,
           "extractor": "facelandmarker VIDEO + YuNet-crop IMAGE fallback (v2); estimator v2",
           "syncnet_tier2": "SKIPPED in v1 (window jumps from MAR line windows)",
           "envelope_source": "mix audio (no Demucs stem cached for corpus)",
           "n_words_total": len(words), "n_words_unassigned": len(unassigned),
           "face_presence_overall": round(float(fm_present.mean()), 4),
           "yunet_presence_overall": round(float(yunet_present.mean()), 4),
           "cover_slots_unscored": cover_list,
           "master_verdict": master_verdict,
           "inserts": results}
    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w") as f: json.dump(out, f, indent=1)
    if text_out:
        lines = [f"## G8 MEASURED SYNC — {os.path.basename(master)}",
                 f"Master verdict: **{master_verdict}** (report-only; e0 = {e0_frames:+.2f} f; "
                 f"inserts from {ins_source}; cover slots unscored: {', '.join(cover_list) or 'none'})",
                 "",
                 "| Insert | Words | Anch | Cov | Bias f | Late% | Early% | MAD f | Drift f | Gap | Verdict |",
                 "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in results:
            st = r.get("stats", {})
            lines.append("| {label} | {nw} | {na} | {cov} | {b} | {l} | {e} | {m} | {d} | {g} | {v} |".format(
                label=r["label"], nw=r["n_words"], na=r.get("n_anchored", "—"),
                cov=(f"{r['coverage']:.2f}" if "coverage" in r else "—"),
                b=st.get("bias_f", "—"), l=st.get("late_share", "—"), e=st.get("early_share", "—"),
                m=st.get("scatter_mad_f", "—"), d=st.get("drift_f", "—"),
                g=(r.get("gap_score") if r.get("gap_score") is not None else "—"), v=r["verdict"]))
        lines.append("")
        with open(text_out, "w") as f: f.write("\n".join(lines))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", required=True)
    ap.add_argument("--words", required=True)
    ap.add_argument("--segments")
    ap.add_argument("--e0", type=float, default=0.0)
    ap.add_argument("--bands")
    ap.add_argument("--out")
    ap.add_argument("--text-out")
    ap.add_argument("--mar-cache")
    a = ap.parse_args()
    bands = dict(BANDS)
    if a.bands:
        bands.update(json.load(open(a.bands)))
    out = run_gate(a.master, a.words, a.segments, a.e0, bands, a.out, a.text_out, a.mar_cache)
    print(json.dumps({"master_verdict": out["master_verdict"],
                      "inserts": len(out["inserts"]),
                      "face_presence_overall": out["face_presence_overall"]}, indent=1))

if __name__ == "__main__":
    main()
