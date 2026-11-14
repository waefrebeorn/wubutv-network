# MV-5 Nemotron re-audit — run plan + findings

Date: 2026-11-05 ~10:40 EST. Author: research subagent (run 2; run 1 died in the
2026-11-05 ~10:29 EST VM reboot before writing anything — this file is the
incremental record, saved as findings landed).

## 0. Bottom line

**HF free-tier inference does NOT serve this model for this account. Nothing ran.
$0 spent. The block is account-level, not model-specific.**

The user authorized the HF key + free-tier queue. The key works (whoami-v2:
WaefreBeorn, isPro=false, canPay=false, billingMode=prepaid). Every HF
Inference Providers route demands prepaid credits or PRO:

| Route tried (2026-11-05 ~10:38–10:40 EST) | Result |
|---|---|
| Router auto-route ASR, `nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B`, 20s clip | **402 Payment Required** — `Purchase pre-paid credits to continue using Inference Providers. Alternatively, subscribe to PRO to get monthly included credits.` (routed to `router.huggingface.co/deepinfra/v1/openai/audio/transcriptions`) |
| Direct router POST (curl, same endpoint) | Same 402, same message |
| Provider `fal-ai` | `Model nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B is not supported by provider fal-ai.` |
| Provider `replicate` | `Model ... is not supported by provider replicate.` |
| Provider `hf-inference` | `Model not supported by provider hf-inference` |
| Chat completions via router | `The requested model 'nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B' is not a chat model.` (router exposes ASR only) |
| Legacy `api-inference.huggingface.co` | Dead — connection fails (HTTP 000) |
| **Control:** `openai/whisper-large-v3` ASR, same key, same clip | **402 as well** (routed to fal-ai) — proves the block is account-level: this account gets zero free inference on any model, not just Nemotron |

Model API says `inference: "warm"` (it IS served — just not for free).
This VM cannot run it locally either: no GPU (`nvidia-smi` not found), 4 CPU,
7 GB RAM, 70 GB free disk. The model needs 1x H100 80 GB (BF16 weights ~68 GB).

**Cost if unblocked (secondary sources, re-check at run time):** DeepInfra lists
Nemotron 3.5 Transcribe at **$0.002/min ($0.12/hr)**, up to 60 min per request.
The whole MV-5 re-audit is ~7.1 min of audio (206s song + 22 takes x ~10s) =
**~$0.015**. Pennies — but it still needs a paid route (see §5).

## 1. Model facts (verified from the model card, 2026-11-05)

- `nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B`, released 2026-10-28.
  34B total / ~4.3B active, hybrid Mamba-Transformer MoE, 40 languages,
  recordings up to 1 hour, 65,536-token context. License OpenMDW-1.1
  (commercial use OK).
- One model does **speaker-attributed transcription + word timestamps**:
  Parallel Expert Encoder = Transformer ASR encoder + **Sortformer speaker
  encoder (Nemotron-3-Diarization, ~99M params)** + CTC timestamp head.
- Best published multi-speaker ASR: **cpWER 15.80** (AMI / CALLHOME / Mixer 6 /
  NOTSOFAR-1 full sessions). English ASR mean WER 4.71 (Open ASR Leaderboard).
- Speaker tags are **relative within a recording** (`<spk:0>`, `<spk:1>` …);
  they do not establish real-world identity and are not stable across files.
  Anchor per file (see §4).
- **SGLang-Omni does NOT support word timestamps or speaker attribution** —
  the full-featured route is NeMo Speech + vLLM only. Transformers
  in-process also supports both (see §2).

## 2. Exact invocation (NeMo Speech + vLLM self-serve — the only full-feature route)

Server (from the model card Quick Start; vLLM 0.32.0, NeMo Speech main):

```
export VLLM_PLUGINS=nemo_speechlm
export VLLM_MAX_AUDIO_DECODE_DURATION_S=3600
export VLLM_MAX_AUDIO_CLIP_FILESIZE_MB=180
export VLLM_USE_V2_MODEL_RUNNER=0        # V1 runner REQUIRED for word timestamps
vllm serve ./NVIDIA-Nemotron-3.5-Transcribe-30B-A4B \
  --served-model-name nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B \
  --trust-remote-code --dtype bfloat16 --gpu-memory-utilization 0.94 \
  --max-model-len 65536 --max-num-batched-tokens 4096 --max-num-seqs 192 \
  --enable-chunked-prefill --no-enable-prefix-caching \
  --use-replayssm --mamba-backend flashinfer --mamba-cache-mode none \
  --mm-processor-cache-gb 0 --no-async-scheduling \
  --limit-mm-per-prompt '{"audio":{"count":6,"length":120000000}}' \
  --speculative-config '{"method":"mtp","num_speculative_tokens":8}' \
  --reasoning-parser nemotron_v3 \
  --trust-request-mm-kwargs \
  --middleware nemo.collections.speechlm2.vllm.salm.ctc_serving.ctc_timestamp_middleware
```

Request (OpenAI-compatible `/v1/chat/completions`, one audio per request,
`stream=false`, `n=1`, temperature 0, reasoning OFF):

```python
import base64
from pathlib import Path
from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="EMPTY")

SPEAKER_PROMPT = (
    "Transcribe this audio with punctuation and capitalization. "
    "Include all spoken words and verbal fillers. "
    "Write numbers in their standard written form. "
    "Put speaker tags <spk:0> <spk:1> <spk:2> <spk:3> on the transcription."
)

def ask(audio_path):
    audio = base64.b64encode(Path(audio_path).read_bytes()).decode()
    return client.chat.completions.create(
        model="nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B",
        messages=[{"role": "user", "content": [
            {"type": "text", "text": SPEAKER_PROMPT},
            {"type": "audio_url", "audio_url": {"url": f"data:audio/wav;base64,{audio}"}},
        ]}],
        temperature=0,
        extra_body={
            "chat_template_kwargs": {"enable_thinking": False},
            "skip_special_tokens": False,   # keep speaker/event tags
            "spaces_between_special_tokens": False,
            "seed": 0,
            "mm_processor_kwargs": {"capture_ctc_timestamps": True},
        },
    )

resp = ask("audio.wav")
alignment = resp.model_dump()["ctc_timestamps"]
assert alignment["error"] is None, alignment["error"]  # CHECK FIRST
for w in alignment["words"]:
    print(w["word"], w["start"], w["end"], w["speaker"])
```

Response `ctc_timestamps` object: `words` (word text, start/end seconds relative
to the input audio, transcript speaker tag); `diarization` (speaker activity
segments, audio-derived); `speaker_tag_to_diarization_speaker` (tag -> diarization
speaker map); `error` (null on success — check before using timestamps).

Transformers in-process alternative (needs the same GPU): `processor.apply_transcription_request`
with the same speaker prompt, `model.generate(..., return_word_timestamp_logits=True)`,
then `processor.align_word_timestamps(text, outputs.word_timestamp_logits,
inputs.input_features_mask, outputs.speaker_logits)`. Needs transformers from
source + torchaudio + scipy.

**What the HF router ASR endpoint can NEVER do for this job:** it returns plain
`{"text": ...}` only — no speaker tags, no word timestamps. Even paid HF
inference via the router cannot produce the ground truth this rebuild needs.

## 3. Sung-audio gotchas (why this is not a straight speech job)

- **Out-of-distribution:** the model is trained/evaluated on speech
  (meetings, calls). Sung vocals over a Suno music bed (bass ~65 Hz,
  instruments, held vocalises) are not its home turf. Expect worse-than-benchmark
  accuracy; treat every output as evidence to adjudicate, not gospel.
- **Dropped repeats:** Nemotron is a language model — like Whisper it may
  normalize or skip a repeated "Easy now" refrain. The CTC word timestamps are
  derived from the GENERATED transcript, so a dropped repeat yields no timestamp
  for it. Mitigation: compare Nemotron's word count per line against
  SONG_WORDS.json (546 words); any shortfall is a dropped repeat until proven
  otherwise. **Use the `diarization` segments (audio-derived, not
  transcript-derived) as the primary singer evidence** — the card says exactly
  this: "Use the diarization segments, rather than word timestamps, when
  evaluating diarization."
- **Speaker tags are per-file relative.** `<spk:0>` in the song is not the same
  person as `<spk:0>` in take S07. Anchor each file independently: the
  diarization speaker with the low f0 band (~97–160 Hz) is CAT; the high band
  (~200–330 Hz) is GIRL. Cross-check with the v1 per-word pyin table
  (work/pyin_f0.npy) and with known anchor lines (intro I01–I08 = CAT per v1;
  I09 ta-da vocalise = GIRL, confirmed 316 Hz).
- **Check `alignment["error"]` on every request** before using any timestamp.
- **One audio per request, `stream=false`, `n=1`.** Keep
  `skip_special_tokens=false` or the speaker tags vanish. A transcript without
  speaker tags is aligned as a single speaker — useless for this job.
- **Verbatim wording matters:** the speaker prompt asks for fillers and
  repetitions verbatim. Do NOT use the "clean written transcript" prompt —
  it drops the repeats we are trying to measure.

## 4. Re-audit pipeline (once unblocked — §5)

### 4a. Inputs (all on disk, verified 2026-11-05)
- Song: `track.mp3` (md5 `0c1bcafa568547e2d4fa36e133ad3626`, 206.400s).
- v1 ground truth to beat: `SONG_WORDS.json` (546 words), `LYRIC_TIMELINE.md`
  (line table + owner table, CAT 354 / GIRL 170 / SPLIT 22 words),
  `CUTLIST.md` (scene map + per-word fit scores).
- Takes: `takes/mv5_*.mp4` (generated clip + generated audio).

### 4b. Step 1 — song ground truth (1 request)
Convert once: `ffmpeg -y -i track.mp3 -ar 16000 -ac 1 work/nemotron/song_16k.wav`
(16k mono wav; model accepts up to 1h, so the full 206s song goes in ONE
request — no chunking, no stitching). Run §2 `ask()` with the speaker prompt.
Save raw response + parsed words to `work/nemotron_song.json` IMMEDIATELY
(incremental save before any further work), fields per word:
`{word, start, end, speaker_tag, diarization_speaker}` plus the raw
`diarization` segments and `speaker_tag_to_diarization_speaker` map.
Anchor tags -> CAT/GIRL by f0 band (see §3) and record the anchor in the file.

### 4c. Step 2 — take audit (22 requests)
For each take in §4e: extract audio only —
`ffmpeg -y -v error -i takes/<take>.mp4 -vn -ar 16000 -ac 1 work/nemotron/takes/<take>.wav`
— then one §2 request per take. Save all raw + parsed output to
`work/nemotron_takes.json` incrementally (append after EACH take, not at the
end — a reboot must not lose completed takes). Per take record: words with
times + speakers, word count vs the lines the scene is supposed to cover
(CUTLIST scene map), and the anchored CAT/GIRL owner per word.

### 4d. Step 3 — diff vs v1 (write `work/nemotron_diff.md`)
- **Song diff:** align Nemotron song words to `SONG_WORDS.json` by sequence +
  time. Per word: `offset = nemotron_start - v1_start`. Per line: owner
  (Nemotron) vs owner (`LYRIC_TIMELINE.md` table). Flag every line whose
  owner flips, and every word with |offset| > 0.50s. Count dropped repeats
  (Nemotron words < SONG_WORDS words per line).
- **Take diff:** for each take, compare its Nemotron words + speakers against
  the song lines its scene covers. Flag: (a) WRONG SINGER — take sings a line
  with the opposite speaker from the song ground truth; (b) MISSING WORDS —
  take drops words the scene needs; (c) TIMING — take word times vs song word
  times (warp needed, in/out of the 0.80–1.25 band).
- **Per-take verdict:** KEEP (right singer, words present, warp in band) /
  RE-TIME (right singer, pace off but warpable) / RE-FIRE (wrong singer or
  missing words — new volley, one named axis) / MONTAGE-COVER (structural,
  captions on song times, not a mouth-sung slot).

### 4e. Takes to audit (sung words in the v1 master, from CUTLIST)
20 sung takes + 2 cutaway controls (expect empty transcripts):

| Take file | Scene | Song lines it must sing (v1 owner) |
|---|---|---|
| mv5_s01_t1 | S01 | I01–I04 (CAT) |
| mv5_s03_t1 | S03 | I09 vocalise (GIRL) |
| mv5_s04_t1 | S04 | L03–L05 (CAT) |
| mv5_s05_t1 | S04/S05 | L05, L06–L10 (CAT) |
| mv5_s06_t1 | S06 | L10–L12 (CAT) |
| mv5_s07_t1 | S07 | L13–L16 (CAT) |
| mv5_s08_t2 | S07/S08 | L16 tail, L17–L24 refrains/responses |
| mv5_s09_t1 | S09 | L25–L32 refrains/responses |
| mv5_s11_t4 | S11 | L38–L40 (GIRL / SPLIT) |
| mv5_s12_t1 | S04/S12 | L41–L44 |
| mv5_s15_t1 | S15 | L53–L56 + vocalise (CAT / GIRL L56) |
| mv5_s17_t1 | S17 | L65–L72 refrains/responses |
| mv5_s19b_t1 | S19b | L77–L80 (CAT / GIRL L80) |
| mv5_s20_t1 | S20 | L80–L81 (GIRL / CAT) |
| mv5_s21_t3 | S21 | L82–L86 (CAT) |
| mv5_s23_t1 | S23 | L91–L96 refrains/responses + SPLIT L96 |
| mv5_s25_t1 | S25 | L99–L106 refrains/responses |
| mv5_s26_t1 | S26 | L107–L108 (GIRL / CAT) |
| mv5_s27_t1 | S27 | L109 (GIRL, held) |
| mv5_s28_t1 | S28 | L110 (CAT) |
| mv5_s10_t1 (control) | S10 cutaway | no sung words expected |
| mv5_s18_t1 (control) | S18 cutaway | no sung words expected |

Donor-only takes (silent B-roll in v1, audio dropped) need NO singer audit:
S13/S14/S16/S19a/S22/S24 structural covers use rejected takes' silent tails.
If the rebuild re-fires a structural scene, its new take gets audited then.

### 4f. What the rebuild needs from this audit
1. `LYRIC_TIMELINE.md` v2 — corrected owner table + corrected word times
   (Nemotron song ground truth replaces the f0/Whisper table wherever they
   disagree; every flip listed in `nemotron_diff.md` with evidence).
2. Per-take verdicts (§4d) — the re-fire list (wrong singer / missing words)
   and the re-time list (warpable pace misses).
3. New word-time grid for assembly: captions + placement keyed to the Nemotron
   song times (the song is the tempo gospel — the video warps to the song).

## 5. How to unblock (user decision needed — no route is free)

| Option | What it is | Cost (re-check at run time) | Notes |
|---|---|---|---|
| A. HF PRO | Subscribe to HF PRO; monthly included Inference Providers credits | PRO subscription (user pays) | Simplest: same router calls, same key. But NOTE: even paid router ASR returns text only — **no speaker tags / timestamps**. PRO does NOT unblock the real job. Only useful if DeepInfra is reached another way. |
| B. HF prepaid credits | Buy HF credits; router -> DeepInfra | ~$0.015 for the whole audit at DeepInfra's $0.002/min | Same limitation as A: router ASR = text only. Does NOT deliver speaker tags/timestamps. |
| C. DeepInfra direct API | Own DeepInfra account + key; `api.deepinfra.com/v1/inference/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B` | $0.002/min, ~$0.015 total | The real route: DeepInfra's endpoint returns word timestamps + speaker labels + language in the same call (per their docs — verify at run time). Needs a new account/key; cannot be done with the HF key alone. |
| D. Cloud H100 rental | Rent 1x H100, run §2 vLLM server, run the 23 requests, shut down | ~$2–6.50/hr depending on provider; the audit itself takes minutes of GPU time once the model loads (~10–20 min setup + load) | Full-featured, private, exact §2 invocation. Needs user go-ahead on spend. |
| E. HF ZeroGPU Space | Deploy a public Space serving the model on free ZeroGPU | $0 license; build effort large, unverified | NVFP4 weights (~17 GB) might fit a 24 GB ZeroGPU card; BF16 will not. Unverified — needs a build + test cycle, and a Space is a public deployment. Do NOT attempt without user go-ahead. |
| F. NVIDIA build.nvidia.com demo | Browser demo ("Try It" on the model card) | Reportedly free, no account | Secondary sources conflict on whether this model is even listed there (Oct 29: "doesn't appear on build.nvidia.com"). Browser-only; cannot be driven from this VM. Unverified. |

**Recommendation:** C (DeepInfra direct, ~2 cents total) is the cheapest real
route; D (rented H100) is the most faithful to the model card. A/B look like
the obvious fix but **do not work** — the HF router's ASR endpoint cannot
return speaker tags or word timestamps at any price. Do not buy HF credits or
PRO for this job.

## 6. What ran / what did not (audit trail)
- Ran: token verification (whoami-v2 OK, WaefreBeorn); model API check
  (`inference: "warm"`); 6 inference probes (auto-route ASR, direct router
  POST, fal-ai, replicate, hf-inference, chat route, legacy endpoint) — all
  failed as tabulated in §0; control probe (whisper-large-v3) also 402.
  Probe script: `/tmp/nemotron_probe.py`, log `/tmp/nemotron_probe.log`.
- Did NOT run: no audio was ever transcribed (no successful inference call);
  no video generated; the delivered v1 master was not touched; $0 spent.
- No token value appears in any file, log, or report. Token was read from
  `~/workspace/vault/hf_read.token` into process memory only.
