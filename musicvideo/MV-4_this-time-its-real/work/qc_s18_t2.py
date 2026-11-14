"""QC S18 t2 only: Whisper + native-fps motion gate + frame grabs."""
import json, pathlib, subprocess
import numpy as np
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-4_this-time-its-real"
work = proj / "work" / "qc_volley4"
frames_dir = work / "frames"
from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
def load_wav_np(wav_path):
    import wave
    with wave.open(str(wav_path), "rb") as w:
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
name = "mv4_s18_t2"
path = proj / "takes" / f"{name}.mp4"
wav = work / f"{name}.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(path), "-vn", "-ac", "1", "-ar", "16000", str(wav)], check=True)
segments, _ = model.transcribe(load_wav_np(wav), word_timestamps=True)
words = []
for seg in segments:
    for w in (seg.words or []):
        words.append({"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)})
print(f"{name}: words={len(words)}/12 ratio={round(len(words)/12, 2)} text={' '.join(w['word'] for w in words)!r}", flush=True)
print(f"  word times: {[(w['word'], w['start'], w['end']) for w in words]}", flush=True)
cmd = ["ffmpeg", "-v", "error", "-i", str(path), "-vf", "scale=160:90,format=gray", "-f", "rawvideo", "-pix_fmt", "gray", "-"]
raw = subprocess.run(cmd, capture_output=True, check=True).stdout
nfr = len(raw) // (160 * 90)
fr = np.frombuffer(raw, dtype=np.uint8).reshape(nfr, 160 * 90).astype(np.int16)
diffs = np.array([float(np.mean(np.abs(fr[i] - fr[i - 1]))) for i in range(1, nfr)])
vocal = diffs[max(1, int(0.0 * 24)):min(len(diffs), int(6.8 * 24))]
vocal_mean = round(float(np.mean(vocal)), 3)
run = maxrun = 0
for d in vocal:
    run = run + 1 if d < 0.5 else 0
    maxrun = max(maxrun, run)
exact = int(np.sum(diffs == 0))
print(f"  motion: frames={nfr} vocal_mean_diff={vocal_mean} longest_near_dup_run={maxrun}f exact_dup={exact}", flush=True)
for t in (2, 5, 8):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(path), "-frames:v", "1", str(frames_dir / f"{name}_{t}s.png")], check=True)
res = json.loads((work / "qc_volley4_results.json").read_text())
res[name] = {"words": len(words), "expected": 12, "ratio": round(len(words) / 12, 2),
             "text": " ".join(w["word"] for w in words), "vocal_mean_diff": vocal_mean,
             "longest_near_dup_run": maxrun, "exact_dup": exact, "word_times": words}
(work / "qc_volley4_results.json").write_text(json.dumps(res, indent=2))
wav.unlink(missing_ok=True)
print("DONE")
