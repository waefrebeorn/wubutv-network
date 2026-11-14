"""MV-4 volley 2 QC: Whisper word counts + native-fps motion gate + frame grabs.
Sequential transcription, per-take temp wavs (never shared).
Frame rule: FAIL if vocal near-dup run >= 24f during vocal OR vocal mean diff < 0.5.
Near-dup = frame-to-frame mean abs diff < 0.5 at 160x90 gray, native 24fps.
"""
import json, pathlib, subprocess
import numpy as np

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-4_this-time-its-real"
work = proj / "work" / "qc_volley3"
work.mkdir(parents=True, exist_ok=True)
frames_dir = work / "frames"
frames_dir.mkdir(exist_ok=True)

# scene, take, expected words, vocal window (s), prompted line
takes = [
    ("S05", "t1", 14, (0.8, 8.9), "Futurama's finished, Futurama's finished, for real this time, no more reruns in the dark"),
    ("S12", "t1", 17, (0.0, 8.4), "But this song's about the day they mean it, when the last new line never comes down"),
    ("S13", "t1", 14, (0.7, 8.0), "Futurama's finished, Futurama's finished, for real this time, no more reruns in the dark"),
    ("S14", "t1", 11, (0.0, 7.0), "Futurama's finished, Futurama's finished, no fresh episodes, that's the hard part"),
    ("S15", "t1", 14, (0.0, 7.6), "Good news, everyone, the ride is done, good news, everyone, the ship won't run"),
    ("S16", "t1", 14, (0.0, 8.5), "Futurama's finished, Futurama's finished, for real this time, no more reruns in the dark"),
]

from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")

def load_wav_np(wav_path):
    """Decode 16k mono wav to float32 numpy (av file-path bug workaround)."""
    import wave
    with wave.open(str(wav_path), "rb") as w:
        n = w.getnframes()
        raw = w.readframes(n)
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0

results = {}
for scene, take, expected, (v0, v1), line in takes:
    name = f"mv4_s{scene[1:]}_t{take[1:]}"
    path = proj / "takes" / f"{name}.mp4"
    wav = work / f"{name}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(path),
                    "-vn", "-ac", "1", "-ar", "16000", str(wav)], check=True)
    segments, info = model.transcribe(load_wav_np(wav), word_timestamps=True)
    words = []
    for seg in segments:
        for w in (seg.words or []):
            words.append({"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)})
    text = " ".join(w["word"] for w in words)
    n = len(words)
    ratio = round(n / expected, 2) if expected else None
    print(f"{name}: words={n}/{expected} ratio={ratio} text={text!r}", flush=True)
    print(f"  word times: {[(w['word'], w['start'], w['end']) for w in words]}", flush=True)

    # motion at native fps, 160x90 gray
    cmd = ["ffmpeg", "-v", "error", "-i", str(path), "-vf",
           "scale=160:90,format=gray", "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    nfr = len(raw) // (160 * 90)
    fr = np.frombuffer(raw, dtype=np.uint8).reshape(nfr, 160 * 90).astype(np.int16)
    diffs = np.array([float(np.mean(np.abs(fr[i] - fr[i - 1]))) for i in range(1, nfr)])
    fps = 24.0
    i0 = max(1, int(v0 * fps))
    i1 = min(len(diffs), int(v1 * fps))
    vocal = diffs[i0:i1]
    vocal_mean = round(float(np.mean(vocal)), 3) if len(vocal) else None
    # longest near-dup run (<0.5) within vocal window, in frames
    run = maxrun = 0
    for d in vocal:
        run = run + 1 if d < 0.5 else 0
        maxrun = max(maxrun, run)
    exact = int(np.sum(diffs == 0))
    print(f"  motion: frames={nfr} vocal_mean_diff={vocal_mean} longest_near_dup_run={maxrun}f exact_dup={exact}", flush=True)

    # frame grabs at 2s/5s/8s
    for t in (2, 5, 8):
        out = frames_dir / f"{name}_{t}s.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(path),
                        "-frames:v", "1", str(out)], check=True)
    results[name] = {"words": n, "expected": expected, "ratio": ratio, "text": text,
                     "vocal_mean_diff": vocal_mean, "longest_near_dup_run": maxrun,
                     "exact_dup": exact, "word_times": words}
    wav.unlink(missing_ok=True)

(work / "qc_volley3_results.json").write_text(json.dumps(results, indent=2))
print("DONE")
