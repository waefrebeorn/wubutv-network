import json, sys
from faster_whisper import WhisperModel
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
for name in ["q4_s04_t2", "q4_s25_t2"]:
    wav = f"work/qc/{name}/audio.wav"
    segments, info = model.transcribe(wav, language="en", beam_size=1,
        condition_on_previous_text=False, repetition_penalty=1.1,
        no_repeat_ngram_size=3, vad_filter=False, word_timestamps=True)
    out = []
    for seg in segments:
        for w in (seg.words or []):
            out.append({"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2), "prob": round(w.probability, 3)})
    json.dump(out, open(f"work/qc/{name}/asr_words.json", "w"), indent=1)
    print(name, json.dumps(out))
