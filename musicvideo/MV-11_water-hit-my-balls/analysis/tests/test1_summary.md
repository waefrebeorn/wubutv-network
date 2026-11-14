# MV-11 lyrics test #1 — fixed faster-whisper config, NO VAD (vs baseline small/defaults/no-VAD)

Baseline (SONG_WORDS.json): 92 words, 102–172s: 0, 110–155s: 0
VAD RUN (test1_small.json, vad_filter=True 500ms/0.5): 3 words total, 0 in 102–172s — VAD gates out held-vowel chant singing entirely; VAD is OUT.

| model | words | 102–172s | 110–155s | max same-word run | words >2s | wall |
|---|---|---|---|---|---|---|
| small | 103 | 41 | 41 | 4 | 2 | 42.7s |
| large-v3-turbo | 132 | 33 | 30 | 5 | 6 | 249.8s |
| distil-large-v3 | 128 | 52 | 43 | 5 | 3 | 786.9s |
