import sys, json
from faster_whisper import WhisperModel
# argv: wav paths...
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
for wav in sys.argv[1:]:
    segs, info = model.transcribe(wav, language="en", beam_size=1, vad_filter=False,
        condition_on_previous_text=False, repetition_penalty=1.1, no_repeat_ngram_size=3, word_timestamps=True)
    words = []
    for s in segs:
        for w in (s.words or []):
            words.append({"w": w.word.strip(), "s": round(w.start,3), "e": round(w.end,3), "p": round(w.probability,2)})
    out = wav.rsplit(".",1)[0] + "_words.json"
    json.dump(words, open(out,"w"), indent=1)
    print(out, len(words), "words")
