"""Prompted re-transcription for S18/S19 (cross-check method): initial_prompt = performed line.
If the prompted decode recovers the dropped/misheard words, the take sings the line and
Whisper misheard; if it still drops them, the take is missing words."""
import pathlib, subprocess, numpy as np
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-4_this-time-its-real"
work = proj / "work" / "qc_volley4"
from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
def load_wav_np(wav_path):
    import wave
    with wave.open(str(wav_path), "rb") as w:
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
for name, line in [
    ("mv4_s18_t1", "We'll rise again, he keeps on saying, but the paperwork says otherwise"),
    ("mv4_s19_t1", "You can binge the old ones on your couch, quote every line like muscle memory"),
]:
    wav = work / f"{name}_prompted.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(proj / "takes" / f"{name}.mp4"),
                    "-vn", "-ac", "1", "-ar", "16000", str(wav)], check=True)
    segments, _ = model.transcribe(load_wav_np(wav), word_timestamps=True, initial_prompt=line)
    words = []
    for seg in segments:
        for w in (seg.words or []):
            words.append({"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)})
    print(f"{name} PROMPTED: words={len(words)} text={' '.join(w['word'] for w in words)!r}", flush=True)
    print(f"  times: {[(w['word'], w['start'], w['end']) for w in words]}", flush=True)
    wav.unlink(missing_ok=True)
print("DONE")
