#!/usr/bin/env python3
"""ASR-grade the C11 outputs with the same config as the validation
(tsm_m7_grade.py): faster-whisper large-v3-turbo, beam 1, word timestamps,
no VAD, 0.3 s pad. Checkpointed per clip into c11_tsm_validation.json
under "asr" — a reaped run resumes by re-running this script.

Clips: 4x C11_M7 (guard-on), 4x C11_OLA256, 1x S49MOD_C11_M7.
Residuals are vs the song grid (clip-local); identity = expected word
heard at all. Bars computed here: 2 (words-3+ onset RMS <= 100 ms),
3 (identity >= 18/23 with guard active), 4 (S49MOD 0.60-squeeze words
heard), 5 (OLA256 identity 23/23).
"""
import glob, json, os, re, sys
import numpy as np
import soundfile as sf

SR = 16000
ROOT = '/home/hatch/workspace/wubutv-network/musicvideo/detection-research/c11_tsm'
OUT = f'{ROOT}/out'
PAD = 0.3
VALIDATION = f'{ROOT}/c11_tsm_validation.json'

SONG = {
 'S47': ([106.24, 106.66, 107.10, 107.44, 107.70, 108.04, 108.30],
         ['this', 'is', 'how', 'you', 'do', 'it', 'now']),
 'S49': ([112.16, 112.68, 113.00, 113.40], ['clip', 'it', 'post', 'it']),
 'S50': ([113.72, 113.98, 114.22, 114.58], ['keep', 'the', 'work', 'alive']),
 'S52': ([117.40, 117.92, 118.06, 118.66, 118.88, 119.16, 119.38, 119.72],
         ['clip', 'it', 'post', 'it', 'help', 'me', 'stay', 'online']),
 'S49MOD': ([112.16, 112.68, 113.00, 113.284], ['clip', 'it', 'post', 'it']),
}
CLIPS = [
 ('S47', 'C11_M7'), ('S49', 'C11_M7'), ('S50', 'C11_M7'), ('S52', 'C11_M7'),
 ('S47', 'C11_OLA256'), ('S49', 'C11_OLA256'), ('S50', 'C11_OLA256'), ('S52', 'C11_OLA256'),
 ('S49MOD', 'C11_M7'),
]


def norm(w):
    return re.sub(r'[^a-z]', '', w.lower())


def align_words(asr_words, expected):
    got = [(norm(w['word']), w['start']) for w in asr_words]
    out, j = [], 0
    for exp in expected:
        found = None
        start_j = j  # a missed word must NOT consume the pointer
        while j < len(got):
            w, t = got[j]
            j += 1
            if w == norm(exp):
                found = t
                break
        if found is None:
            j = start_j
        out.append(found)
    return out


def main():
    snap = glob.glob(os.path.expanduser(
        '~/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/snapshots/*'))
    model_path = snap[0] if snap else 'mobiuslabsgmbh/faster-whisper-large-v3-turbo'
    print('model:', model_path, flush=True)
    from faster_whisper import WhisperModel
    model = WhisperModel(model_path, device='cpu', compute_type='int8',
                         cpu_threads=2, num_workers=1)
    res = json.load(open(VALIDATION)) if os.path.exists(VALIDATION) else {}
    asr = res.setdefault('asr', {})
    for name, method in CLIPS:
        key = f'{name}_{method}'
        if key in asr:
            print(f'{key}: cached res_ms={asr[key]["residual_ms"]}', flush=True)
            continue
        song_on, words = SONG[name]
        rel_song = [s - song_on[0] for s in song_on]
        p = f'{OUT}/{name}_{method}.wav'
        y, _ = sf.read(p)
        ypad = np.concatenate([np.zeros(int(PAD * SR)), y,
                               np.zeros(int(PAD * SR))]).astype(np.float32)
        segs, _ = model.transcribe(
            ypad, language='en', beam_size=1,
            word_timestamps=True, vad_filter=False,
            condition_on_previous_text=False,
            log_prob_threshold=-1.0, compression_ratio_threshold=2.4,
            no_speech_threshold=0.6, repetition_penalty=1.1)
        wlist = []
        for seg in segs:
            wlist.extend([{'word': w.word, 'start': w.start - PAD,
                           'end': w.end - PAD, 'prob': w.probability}
                          for w in (seg.words or [])])
        onsets = align_words(wlist, words)
        res_ms = [None if o is None else round((o - s) * 1000, 1)
                  for o, s in zip(onsets, rel_song)]
        asr[key] = {'asr_words': [w['word'] for w in wlist],
                    'onsets_s': onsets, 'residual_ms': res_ms}
        json.dump(res, open(VALIDATION, 'w'), indent=1)
        print(f'{key}: words={[w["word"] for w in wlist]} res_ms={res_ms}', flush=True)
    print('C11 ASR grading done', flush=True)


if __name__ == '__main__':
    main()
