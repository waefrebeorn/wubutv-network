#!/usr/bin/env python3
"""MV-11 lyrics test #2: MDX-Net separation -> RMS-VAD segmentation ->
transcribe each segment with the WINNING test-#1 config (large-v3-turbo,
fixed config, NO VAD) on BOTH the original mix and the separated vocals,
keep the better per segment (judged by lyric-word coverage vs the measured
timeline anchors, NOT raw word count — test #1 proved count lies).

Separation: Demucs htdemucs via audio-separator (run separately before
this script; output analysis/tests/separation/track_44k_vocals_htdemucs.wav).
MDX-Net was the plan but its path is BROKEN in this venv: audio-separator's
MDX route uses onnx2torch -> torchvision, and torchvision 0.29.2 (built for
torch 2.9) fails to import under torch 2.15.0+cpu ("operator
torchvision::nms does not exist"); the CPU index has no torchvision 0.30.0.
The MSS-ALT paper itself used Demucs, so the test's question is intact.
RMS-VAD: 25ms window / 10ms hop on separated-vocal RMS; threshold 0.1 x
p99 RMS; min silence 1.0s to split; max segment 30s (split at quietest
point); min segment 0.5s; 0.3s pad each side for transcription context.
Resumable: per-segment checkpoint JSONs; skips segments already done.
"""
import json, os, time
import numpy as np
from scipy.io import wavfile
from scipy.signal import resample_poly

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-11_water-hit-my-balls"
TESTS = os.path.join(PROJ, "analysis", "tests")
SEP_DIR = os.path.join(TESTS, "separation")
TRACK_LEN = 172.42

# --- measured lyric anchors from LYRIC_TIMELINE.md: (onset_s, [words]) ---
ANCHORS = [
    (13.76, "water hits my balls"), (17.72, "water hits my balls"),
    (21.78, "when i poop it splashes"), (26.08, "balls balls"),
    (27.0, "balls balls"), (28.0, "balls balls"),
    (29.32, "water hits my balls"), (31.02, "water hits my balls"),
    (33.04, "water hits my balls"), (34.94, "splash back on the balls"),
    (36.94, "balls balls"), (38.0, "balls balls"),
    (45.18, "sitting on the toilet"), (47.18, "water hits"),
    (48.64, "my balls"),
    (55.26, "water hits"), (56.18, "my balls"),
    (70.66, "water hits my balls"), (76.68, "water hits my balls"),
    (85.40, "water hits my balls"), (87.36, "when i poop it splashes"),
    (89.40, "balls balls"), (90.98, "water hits my balls"),
    (93.01, "water hits my balls"), (94.88, "splash back on the balls"),
    (96.92, "balls balls"), (99.0, "balls balls"),
    (110.70, "water"), (111.5, "balls"),
    (129.98, "splashes"), (131.82, "balls balls"),
    (138.42, "water hits my balls"), (141.36, "water hits my balls"),
    (145.40, "when i poop it splashes"), (153.60, "balls balls"),
    (170.9, "balls"),
]
VOCAB = {"water", "hits", "hit", "my", "balls", "ball", "when", "i", "poop",
         "it", "splashes", "splash", "back", "on", "the", "sitting", "toilet"}


def norm(w):
    return w.lower().strip(",.!?\"'()[]")


def match(a, b):
    """plural-tolerant word equality."""
    return a == b or a + "s" == b or b + "s" == a


def expected_words(start, end, tol=0.75):
    exp = []
    for t, line in ANCHORS:
        if start - tol <= t <= end + tol:
            exp.extend(norm(w) for w in line.split())
    return exp


def score(words, start, end):
    """coverage of expected lyric words + count of non-lyric words."""
    exp = expected_words(start, end)
    got = [norm(w["word"]) for w in words]
    used = [False] * len(got)
    hit = 0
    for e in exp:
        for j, g in enumerate(got):
            if not used[j] and match(e, g):
                used[j] = True
                hit += 1
                break
    non_lyric = sum(1 for g in got if g not in VOCAB)
    cov = (hit / len(exp)) if exp else (1.0 if not got else 0.0)
    return {"expected": len(exp), "hit": hit, "coverage": round(cov, 3),
            "non_lyric_words": non_lyric, "n_words": len(got)}


def rms_vad(y, sr, win=0.025, hop=0.010, thr_frac=0.10, min_sil=1.0,
            max_len=30.0, min_len=0.5, pad=0.3):
    n_win = int(win * sr)
    n_hop = int(hop * sr)
    n_frames = 1 + max(0, (len(y) - n_win) // n_hop)
    rms = np.empty(n_frames)
    for i in range(n_frames):
        seg = y[i * n_hop: i * n_hop + n_win]
        rms[i] = np.sqrt(np.mean(seg ** 2)) if len(seg) else 0.0
    thr = thr_frac * np.percentile(rms, 99)
    active = rms > thr
    # raw active runs
    runs = []
    i = 0
    while i < n_frames:
        if active[i]:
            j = i
            while j < n_frames and active[j]:
                j += 1
            runs.append([i * hop, j * hop])
            i = j
        else:
            i += 1
    # merge runs separated by < min_sil
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] < min_sil:
            merged[-1][1] = r[1]
        else:
            merged.append(list(r))
    # drop tiny segments
    merged = [r for r in merged if r[1] - r[0] >= min_len]
    # split long segments at quietest point (Cut&Merge), recursively
    def split_long(r):
        if r[1] - r[0] <= max_len:
            return [r]
        a = int(r[0] / hop)
        b = int(r[1] / hop)
        q = a + int(np.argmin(rms[a:b]))
        mid = q * hop
        # don't split within 2s of an edge
        if mid - r[0] < 2.0 or r[1] - mid < 2.0:
            mid = (r[0] + r[1]) / 2
        return split_long([r[0], mid]) + split_long([mid, r[1]])
    out = []
    for r in merged:
        out.extend(split_long(r))
    # pad + clamp
    return [{"start": round(max(0.0, r[0] - pad), 2),
             "end": round(min(TRACK_LEN, r[1] + pad), 2)} for r in out]


def find_vocals():
    cands = [f for f in sorted(os.listdir(SEP_DIR))
             if f.lower().endswith(".wav") and "vocal" in f.lower()]
    if not cands:
        raise FileNotFoundError(f"no vocals wav in {SEP_DIR}: "
                                f"{os.listdir(SEP_DIR)}")
    return os.path.join(SEP_DIR, cands[0])


def load_16k_mono(path, target_sr=16000):
    sr, data = wavfile.read(path)
    if data.ndim > 1:
        data = data.mean(axis=1)
    y = data.astype(np.float32)
    if np.max(np.abs(y)) > 1.5:  # int16 range
        y = y / 32768.0
    if sr != target_sr:
        y = resample_poly(y, target_sr, sr).astype(np.float32)
    return y


def post_filter(words):
    filtered, run, prev = [], 0, None
    for w in words:
        k = norm(w["word"])
        run = run + 1 if k == prev else 1
        prev = k
        if run <= 5:
            filtered.append(w)
    return filtered


def main():
    voc_path = find_vocals()
    print("vocals:", voc_path, flush=True)
    sr_v, data_v = wavfile.read(voc_path)
    y_v = data_v.astype(np.float32)
    if y_v.ndim > 1:
        y_v = y_v.mean(axis=1)
    if np.max(np.abs(y_v)) > 1.5:
        y_v = y_v / 32768.0

    seg_path = os.path.join(TESTS, "test2_segments.json")
    if os.path.exists(seg_path):
        segments = json.load(open(seg_path))["segments"]
        print(f"segments loaded ({len(segments)})", flush=True)
    else:
        segments = rms_vad(y_v, sr_v)
        json.dump({"vocals_file": os.path.basename(voc_path),
                   "params": {"win": 0.025, "hop": 0.010, "thr_frac_p99": 0.10,
                              "min_silence_s": 1.0, "max_len_s": 30.0,
                              "min_len_s": 0.5, "pad_s": 0.3},
                   "n_segments": len(segments), "segments": segments},
                  open(seg_path, "w"), indent=1)
        print(f"segments: {len(segments)}", flush=True)
    for s in segments:
        print(f"  {s['start']:7.2f}–{s['end']:7.2f}  ({s['end']-s['start']:.1f}s)",
              flush=True)

    mix16 = load_16k_mono(f"{PROJ}/analysis/track_16k.wav")
    voc16 = load_16k_mono(voc_path)

    from faster_whisper import WhisperModel
    model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8",
                         cpu_threads=2)

    def transcribe(y):
        t0 = time.time()
        segments_out, _ = model.transcribe(
            y, language="en", word_timestamps=True,
            condition_on_previous_text=False, beam_size=1,
            temperature=(0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
            compression_ratio_threshold=2.4, log_prob_threshold=-1.0,
            no_speech_threshold=0.6, repetition_penalty=1.1,
            no_repeat_ngram_size=3)
        words, text = [], []
        for s in segments_out:
            text.append(s.text)
            for w in (s.words or []):
                words.append({"word": w.word.strip(),
                              "start": round(w.start, 3),
                              "end": round(w.end, 3),
                              "prob": round(w.probability, 3)})
        return post_filter(words), " ".join(text), round(time.time() - t0, 1)

    results = []
    for i, s in enumerate(segments):
        outp = os.path.join(TESTS, f"test2_seg_{i:02d}.json")
        if os.path.exists(outp):
            rec = json.load(open(outp))
            print(f"SKIP seg {i} ({s['start']:.1f}–{s['end']:.1f})", flush=True)
            results.append(rec)
            continue
        a = int(s["start"] * 16000)
        b = int(s["end"] * 16000)
        mw, mtext, mwall = transcribe(mix16[a:b])
        vw, vtext, vwall = transcribe(voc16[a:b])
        # shift word times back to track time
        for w in mw:
            w["start"] = round(w["start"] + s["start"], 3)
            w["end"] = round(w["end"] + s["start"], 3)
        for w in vw:
            w["start"] = round(w["start"] + s["start"], 3)
            w["end"] = round(w["end"] + s["start"], 3)
        ms, vs = score(mw, s["start"], s["end"]), score(vw, s["start"], s["end"])
        if ms["coverage"] != vs["coverage"]:
            winner = "mix" if ms["coverage"] > vs["coverage"] else "vocals"
        elif ms["non_lyric_words"] != vs["non_lyric_words"]:
            winner = ("mix" if ms["non_lyric_words"] < vs["non_lyric_words"]
                      else "vocals")
        else:
            winner = "mix"
        rec = {"segment": i, "start": s["start"], "end": s["end"],
               "mix": {"words": mw, "text": mtext, "wall_s": mwall,
                       "score": ms},
               "vocals": {"words": vw, "text": vtext, "wall_s": vwall,
                          "score": vs},
               "winner": winner}
        json.dump(rec, open(outp, "w"), indent=1)
        results.append(rec)
        print(f"seg {i} {s['start']:.1f}–{s['end']:.1f}: mix cov {ms['coverage']} "
              f"({ms['hit']}/{ms['expected']}, nonlyr {ms['non_lyric_words']}) | "
              f"voc cov {vs['coverage']} ({vs['hit']}/{vs['expected']}, "
              f"nonlyr {vs['non_lyric_words']}) -> {winner}", flush=True)

    # ---- summary ----
    t1 = json.load(open(os.path.join(TESTS, "test1_novad_large-v3-turbo.json")))
    t1_words = [w for w in t1["words"] if 102 <= w["start"] < 172.42]
    tot_mix = sum(len(r["mix"]["words"]) for r in results)
    tot_voc = sum(len(r["vocals"]["words"]) for r in results)
    win_mix = sum(len(r["mix"]["words"]) for r in results
                  if r["winner"] == "mix")
    win_voc = sum(len(r["vocals"]["words"]) for r in results
                  if r["winner"] == "vocals")
    mix_102 = [w for r in results for w in r["mix"]["words"]
               if 102 <= w["start"] < 172.42]
    voc_102 = [w for r in results for w in r["vocals"]["words"]
               if 102 <= w["start"] < 172.42]
    win_102 = [w for r in results
               for w in (r[r["winner"]]["words"])
               if 102 <= w["start"] < 172.42]
    lines = [
        "# MV-11 lyrics test #2 — MDX-Net separation + RMS-VAD + turbo (mix vs vocals)",
        "",
        f"Separator: Demucs htdemucs (audio-separator). "
        f"MDX-Net path broken in this venv (torchvision 0.29.2 vs torch 2.15; "
        f"see script header). "
        f"Segments: {len(segments)} (RMS-VAD on separated vocals: thr 0.1 x p99, "
        f"min silence 1.0s, max 30s, min 0.5s, pad 0.3s).",
        f"Transcriber: large-v3-turbo, fixed test-#1 config, NO VAD. "
        f"Scoring: lyric-word coverage vs LYRIC_TIMELINE.md anchors "
        f"(plural-tolerant); tie-break fewer non-lyric words, then mix.",
        "",
        "| seg | span | mix words (cov / nonlyr) | vocals words (cov / nonlyr) | winner |",
        "|---|---|---|---|---|",
    ]
    for r in results:
        ms, vs = r["mix"]["score"], r["vocals"]["score"]
        lines.append(f"| {r['segment']} | {r['start']:.1f}–{r['end']:.1f} | "
                     f"{ms['n_words']} ({ms['coverage']}, {ms['non_lyric_words']}) | "
                     f"{vs['n_words']} ({vs['coverage']}, {vs['non_lyric_words']}) | "
                     f"{r['winner']} |")
    lines += [
        "",
        f"Totals (all segments): mix {tot_mix} words, vocals {tot_voc} words. "
        f"Best-per-segment total: {win_mix + win_voc} words "
        f"(mix wins {sum(1 for r in results if r['winner'] == 'mix')} segs, "
        f"vocals wins {sum(1 for r in results if r['winner'] == 'vocals')} segs).",
        f"102–172s span: test-#1 turbo full-clip = {len(t1_words)} words; "
        f"test #2 mix-segments = {len(mix_102)}; vocals-segments = {len(voc_102)}; "
        f"best-per-segment = {len(win_102)}.",
        "",
        "## Verdict",
    ]
    # verdict: did separation recover the Drop / outro?
    drop_mix = [w for w in mix_102 if w["start"] < 122]
    drop_voc = [w for w in voc_102 if w["start"] < 122]
    out_mix = [w for w in mix_102 if w["start"] >= 155]
    out_voc = [w for w in voc_102 if w["start"] >= 155]
    lines.append(f"Drop 102–122s: mix-segments {len(drop_mix)} words, "
                 f"vocals-segments {len(drop_voc)} words "
                 f"(test-#1 turbo full-clip had "
                 f"{len([w for w in t1_words if w['start'] < 122])} here).")
    lines.append(f"Outro 155–172s: mix-segments {len(out_mix)} words, "
                 f"vocals-segments {len(out_voc)} words "
                 f"(test-#1 turbo full-clip had "
                 f"{len([w for w in t1_words if w['start'] >= 155])} here).")
    open(os.path.join(TESTS, "test2_summary.md"), "w").write("\n".join(lines) + "\n")
    print("WROTE test2_summary.md", flush=True)


if __name__ == "__main__":
    main()
