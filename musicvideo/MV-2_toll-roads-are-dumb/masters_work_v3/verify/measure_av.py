import json, subprocess, sys
import numpy as np
# 1) master audio -> 16k mono wav
subprocess.run(['ffmpeg','-v','error','-y','-i','masters/mv2_toll_roads_are_dumb_v3_16x9.mp4','-vn','-ac','1','-ar','16000','masters_work_v3/verify/master_audio.wav'], check=True)
import wave
w = wave.open('masters_work_v3/verify/master_audio.wav')
n = w.getnframes(); raw = w.readframes(n); w.close()
audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
sys.path.insert(0, '/home/hatch/workspace/fw-venv/lib/python3.12/site-packages')
from faster_whisper import WhisperModel
model = WhisperModel('base', device='cpu', compute_type='int8')
segments, _ = model.transcribe(audio, language='en', word_timestamps=True, beam_size=1)
words = []
for seg in segments:
    for wd in seg.words:
        words.append({'t0': round(wd.start, 2), 't1': round(wd.end, 2), 'word': wd.word.strip()})
json.dump(words, open('masters_work_v3/verify/master_words.json','w'), indent=1)
print('master words:', len(words))
song = json.load(open('SONG_WORDS_BASE.json'))
print('song words:', len(song))
# compare first 30 song words to nearest master word onset
import difflib
for sw in song[:40]:
    cand = min(words, key=lambda mw: abs(mw['t0']-sw['t0']))
    print(f"song {sw['t0']:7.2f} '{sw['word']}' -> master {cand['t0']:7.2f} '{cand['word']}' delta {cand['t0']-sw['t0']:+.2f}")
