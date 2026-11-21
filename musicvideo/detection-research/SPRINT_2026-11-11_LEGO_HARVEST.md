# LEGO HARVEST — C modules from wubuwizard, wubuos, www for WUBUMV

Survey 2026-11-11 ~22:40–23:05 EST. User order Telegram msg 250 (22:31:59 EST):
"now continue finding c code to take from wubuwizard and wubuos and www repos
and then make the best tools for your WuBuMV repo — gather your legos."
Follow-on to the standing LEGO RULE (msg 233). SURVEY ONLY — no builds, no
commits, no Telegram. Clones at `~/workspace/lego-harvest-scratch/`
(wubuwizard b6601d4, wubuos 2bd36c1, www 3116b40; shallow, read-only).

## 0. The three repos at a glance

| repo | size | C files | C lines | what it is |
|---|---|---|---|---|
| waefrebeorn/wubuwizard | 97 MB | 1,578 | ~105,000 | "The best inference engine" — LLM inference in C/CUDA (LFM2, Gemma, GGML), plus a from-scratch multimodal ingest stack |
| waefrebeorn/wubuos | 33 MB | 2,113 | ~246,000 | WuBuOS — TempleOS/ZealOS C-port OS with Win98/XP GUI, DAW, canvas editor, RL (BearRL), JIT, VSL virtualization |
| waefrebeorn/www | 16 MB | 415 | ~13,000 | World Wide WorldSpace — C11 game/world engine (ECS, tiles, software rasterizer, Lua mods) |

Total: **4,106 C files, ~365,000 lines** of the user's own C. The honest
picture: most of it is NOT WUBUMV-shaped. wubuwizard is an LLM engine,
wubuos is an operating system, www is a game engine. The harvest is the
small set of modules that happen to be exactly what the music pipeline
needs — and that set is real and high-value.

## 1. Inventory — the modules that matter

Ranked by WUBUMV value. Deps column: what the module needs beyond libc/libm.

### Tier 1 — direct lego, near-zero porting cost

| # | module | repo / path | lines | deps | WUBUMV use |
|---|---|---|---|---|---|
| 1 | wubu_png — PNG decoder from spec | wubuwizard/src/wubu_png.c + include/wubu_png.h | 171 | zlib only | Read PNG stills/frames in C tools without stb/ffmpeg. RFC 2083: inflate + all 5 filters, RGB/RGBA/gray/palette. Feeds frame-QC, contact sheets, still analysis. |
| 2 | wubu_jpeg — JPEG baseline decoder from spec | wubuwizard/src/wubu_jpeg.c + include/wubu_jpeg.h | 397 | libc/libm | Read JPEG stills/frames in C. ITU-T T.81: Huffman + 8x8 IDCT + YCbCr→RGB. Feeds the same QC/readers as PNG. |
| 3 | wubu_video — AVI+MJPEG frame extraction | wubuwizard/src/wubu_video.c + include/wubu_video.h | 138 | own JPEG decoder | Read MJPEG/AVI takes frame-by-frame in C. H.264 frames counted, not decoded (later leg). Feeds motion/M6 analysis without ffmpeg. |
| 4 | wubu_audio — mel-spectrogram + radix-2 FFT from scratch | wubuwizard/src/wubu_audio.c + include/wubu_audio.h | 127 | libc/libm | Independent second implementation of the c11_mir STFT/mel front-end: 16 kHz, 512-frame Hann, 40 mels, 10 ms hop. Cross-check c11_mir bit-for-bit, or replace its front-end. Caveat: MAX_FRAMES 64 (~4 s) — prototype scale, needs the frame cap lifted for full tracks. |
| 5 | wubu_codec — audio↔image transform (STFT→RGB, ISTFT back) | wubuwizard/src/wubu_codec.c + include/wubu_codec.h | 229 | libc/libm | STFT → 5 perceptual bands → RGB image (mag in R, phase sin/cos in G/B); decode reconstructs audio via overlap-add ISTFT. Has its own radix-2 FFT (FFT_N 256, hop 64). The C version of dadaspec: spectrogram images without Python. |
| 6 | wubu_canvas — layered 2D pixel canvas engine | wubuos/src/apps/wubu_canvas_*.c + wubu_canvas.h | 2,005 | libc/libm | Full layered image editor engine: layers, blend modes, opacity, brush/eraser/fill/line/rect/ellipse/gradient, filters (blur, sharpen, edge, invert, threshold, grayscale), undo, PPM IO, plugin hooks, composite to RGBA. THE kinetic-type / graphic-overlay engine in C: render kinetic words, impact frames, and title cards without Python/PIL. |
| 7 | wb_render — software 3D rasterizer | www/~WuBu~/src/core/wb_render.c + wb_render.h | 162 | libc/libm | Perspective camera + heightfield mesh + z-buffered triangle fill + flat shading, rastering into a caller framebuffer (XRGB8888). Pure C11, no deps. The Blender-alternative floor: code-rendered 3D accents / stills / impact frames without Blender. |
| 8 | wubre + wubugrep — regex engine + grep | wubuos/src/tools/wubre_*.c + wubugrep.c | 3,793 | libc/libm | Complete regex: compile, DFA, SIMD matcher, literal-prefix fast path, BRE. For lyric-sheet parsing, word search, ledger/log mining in C tools. wubugrep is a working grep built on it. |

### Tier 2 — real value, needs adaptation or a model/weights

| # | module | repo / path | lines | deps | WUBUMV use |
|---|---|---|---|---|---|
| 9 | gguf_reader + quantized_matmul | wubuwizard/src/gguf_reader.c, quantized_matmul.c | 2,169 + 652 | libc/libm, mmap | GGUF model loading + IQ dequant tables + quantized matmul in C. The model-runner floor for running small models in C (Mini-GLM5.2 already proves the pattern; this is the GGUF half). Feeds future C model work (e.g. a C word-aligner), not needed today. |
| 10 | wubu_tokenizer (+ HF variant) | wubuwizard/src/wubu_tokenizer.c, wubu_tokenizer_hf.c | 807 + 526 | gguf_reader | BPE tokenizers (Qwen byte-level). Text-side lego for lyric handling in C tools. |
| 11 | wubu_audio (wubuos) — DAW mixer + Furnace tracker + SF2 + chips | wubuos/src/audio/*.c | 2,881 | pthread, libc/libm | Ardour-style track/bus mixer, Furnace chip-tracker patterns, SF2 soundfont rendering, chip synthesis. NOT a lyrics/beat tool — but the mixer + pattern engine is the seed of a C-side "song structure → stems" scratchpad, and the Furnace tracker is a step-sequencer the MV pipeline could borrow for beat-grid authoring. GUI-free core is separable; the OS bindings are not. |
| 12 | wubu_sound + wubu_waveosc — PCM synth engine | wubuos/src/gui/wubu_sound.c, wubu_waveosc.c | 171 + 100 | libc/libm | Pure PCM synthesis (sine/square/etc., note tables, no assets). Tiny; useful for generating test tones / click tracks / reference beeps in C tools. |
| 13 | thread_pool | wubuwizard/include/thread_pool.h (+ impl) | ~150 | pthread | parallel-for + matmul_nt. Speeds up batch C tools (frame loops, per-frame M6) on the 1.5-CPU blade. Drop-in. |
| 14 | wubu_tensor_store + safetensors_reader/writer | wubuwizard/src/wubu_tensor_store.c, safetensors_*.c | 932 + ~600 | libc/libm | Weight file loading (safetensors + GGUF-adjacent). Model-runner support, same family as #9. |
| 15 | wubu_vision_moondream — vision encoder | wubuwizard/src/wubu_vision_moondream.c | 534 | model weights | Moondream image understanding in C. Needs weights + a forward pass wired to the wizard's LLM core — heavy lift. Long-shot QC helper (ask a model what is in a frame); NOT a near-term build. |

### Tier 3 — checked, low or no WUBUMV value (do not re-survey)

| module | repo / path | lines | why not |
|---|---|---|---|
| wubu_4kv — INT4/INT3 KV-cache quant | wubuwizard/src/wubu_4kv.c | 300 | LLM KV-cache only. No MV use. |
| wubu_specdec — speculative decoding | wubuwizard/src/wubu_specdec.c | 89 | LLM decode only. |
| wubu_encoder (slot/vtable) | wubuwizard/src/wubu_encoder.c | 73 | Encoder registry naming "whisper"/"siglip" — a vtable, not an implementation. No Whisper code here. |
| wubu_synth — program synthesis | wubuwizard/src/wubu_synth.c | 82 | Spec→C codegen templates. Cute, not MV. |
| wubu_canvas (wizard) — latent-space VHF canvas | wubuwizard/src/wubu_canvas.c | 145 | Quaternion-field latent canvas, NOT pixels. Different canvas from wubuos's. Research toy. |
| wubuos kernel audio (dspgraph/aec/mst/pcmplugin) | wubuos/src/kernel/wubu_{dspgraph,aec,mst,pcmplugin,audio}.* | 1,150 | Hardware-detection/routing stubs (ALSA/ASoC topology, DP MST), not DSP. No real AEC, no real resampler. |
| wubuos bpm.c | wubuos/src/gui/bpm.c | 129 | "Big Picture Mode" gamepad shell. NOT beats-per-minute. False lead, recorded so nobody re-chases it. |
| wubuos music.c | wubuos/src/apps/music.c | 193 | GUI music player driving the sound engine. Player shell only. |
| wubuos bear (BearRL) | wubuos/src/bear/ | 5,499 | PPO trainer + envs. RL only. train_cartpole_gaad_video.c renders PPM frames + ffmpeg — the PPM→ffmpeg pattern is the only reusable bit, and we already do it. |
| wubuos worldsim | wubuos/src/worldsim/ | 735 | Tiny entity/physics/render sim. Toy vs Blender/www rasterizer. |
| wubuos framework (wubufx) | wubuos/src/framework/ | 560 | OS app framework bound to the HolyC daemon. Not portable. |
| wubuos JIT / runtime / VSL | wubuos/src/{jit,runtime,hosted}/ | ~66,000 | OS virtualization + JIT. Not MV. |
| wubuos apps/wubu_codec.c | wubuos/src/apps/wubu_codec.c | 497 | FFmpeg CLI wrapper (pipes to ffmpeg subprocess). We already shell out to ffmpeg; a C wrapper is a small win, not a build. |
| www engine core (ECS/tiles/avatar/camera/net/lua) | www/~WuBu~/src/core/ | ~13,000 | Game engine. Only wb_render (#7) is separable; the rest is world-space infrastructure. |
| wubuwizard LLM core (LFM2, Gemma, ggml, flash-attn, quant) | wubuwizard/src/, llama/ | ~90,000 | Inference engine. Vendored ggml is third-party (not lego). The user's own LFM2/Gemma forward passes are model code, not MV tools. |
| wubuwizard AUDIO/wubusynth | wubuwizard/AUDIO/ | Python | Python synth/compressor. Not C, not MV. |
| wubuwizard MATH / ENCODERS / DIFFUSION / OPTIMIZERS | wubuwizard/MATH, ENCODERS, DIFFUSION, OPTIMIZERS | — | Lean proofs, encoder research, diffusion/GAN, PID controllers. No MV-shaped C. |

## 2. Ranked harvest (by value for WUBUMV)

1. **wubu_png + wubu_jpeg + wubu_video** (wubuwizard) — the still/frame readers. Every C QC tool today shells to ffmpeg or Python to read a frame. These three make C tools read their own inputs. ~706 lines total, zlib only.
2. **wubu_canvas** (wubuos) — the 2D graphics engine. Kinetic type, impact frames, title cards, overlays — rendered in C, no Python/PIL, no Blender. 2,005 lines, libc/libm only.
3. **wubu_audio (mel/FFT) + wubu_codec (audio↔image)** (wubuwizard) — the audio front-ends. Second opinion on c11_mir's STFT/mel; dadaspec images in C; 356 lines combined.
4. **wb_render** (www) — the 3D floor. Code-rendered 3D accents without Blender. 162 lines.
5. **wubre** (wubuos) — regex/text engine for lyric and log tooling. 3,793 lines but self-contained.
6. **thread_pool** (wubuwizard) — parallel-for for batch C tools. ~150 lines.
7. **gguf_reader + quantized_matmul + tensor_store** (wubuwizard) — the model-runner floor for future C models. 3,700+ lines; only when a C model is actually scoped.

## 3. Top 3 first builds (queue after sprints 5/6/7 land)

1. **c11_frames — C frame reader + motion core**: lego in wubu_png + wubu_jpeg + wubu_video (read PNG/JPEG/AVI-MJPEG frames in C) and re-implement the M6/TSM motion gate on top of them, replacing the ffmpeg+Python frame pipeline in volley QC with one C binary that reads a take and prints M6 + dup runs.
2. **c11_kinetic — C kinetic-type renderer**: lego in wubu_canvas (layers, blend, filters, composite) plus wubu_png (read the still) to render kinetic words / impact frames / title cards straight onto frames in C, replacing the Python/PIL kinetic layer and the Blender impact-frame path for simple cards.
3. **c11_spec — C spectrogram + mel front-end**: lego in wubu_audio (mel/FFT) + wubu_codec (audio↔image) to emit dadaspec-style spectrogram images and mel features in C, cross-validated against c11_mir's front-end (corr ≥ 0.999) — one binary serving both intake structure maps and ASR-side features.

## 4. What was NOT useful (so nobody re-surveys it)

- No beat/onset/tempo module exists in any of the three repos. "tempo" hits (59 files) are all the word "tempo" in LLM/OS prose, not music tempo. No MFCC, no chroma, no HPSS, no onset detector, no VAD, no forced aligner, no Whisper implementation. The snapper/HPSS sprints stay from-scratch C11 — there is nothing to lego there.
- No font/glyph renderer: freetype hits are 1 file, stb_truetype 0. Kinetic type needs glyph advances from fontTools (already in the lyrics venv) or a vendored stb_truetype — not in these repos.
- No H.264/MP4 decoder: wubu_video counts H.264 frames, does not decode them. MP4 takes still need ffmpeg.
- No optical flow: Farneback stays from-scratch (sprint 7).
- The wubuos kernel "audio" files are detection stubs, not DSP. bpm.c is a gamepad shell, not BPM.

## 5. Notes for the builder

- Clones kept at `~/workspace/lego-harvest-scratch/` (wubuwizard 97M, wubuos 33M, www 16M) for the builds to lego from. Delete only after the top-3 builds land.
- /tmp note: the first clone attempt failed — /tmp is a 512 MB tmpfs and was 100% full at the time. Clones were made on home disk instead. At report time /tmp is 0% used (freed by the runtime/another process) and no /tmp/lego ever existed; nothing of this survey's was deleted from /tmp. Never clone into /tmp.
- License: all three repos are the user's own (waefrebeorn). Lego in + modify per the standing rule; keep the per-file headers when reusing.
- The wubuwizard ingest stack has a real test gate (`tools/test_ingest_all.c`, 334 lines — builds minimal real PNG/docx/PDF/AVI files in-memory and proves each decoder reads them back). Any WUBUMV build that reuses wubu_png/jpeg/video should port that gate pattern: build a tiny real file, decode it, assert the pixels.
