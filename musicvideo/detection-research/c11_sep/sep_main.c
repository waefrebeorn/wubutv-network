/* sep_main.c — UVR driver: chunked MDX-Net separation (C11).
 *
 * Faithful C11 port of mdx_onnx_cpu.py's demix() (UVR v5 recipe) on top of
 * the compiled interpreter (sep_interp) + the parity-checked STFT/ISTFT
 * (sep_stft). Usage:
 *   sep_main <input.wav> <out_vocals.wav> [--out-inst <path>]
 *          [--prog-dir <dir>] [--threads N] [--chunks N] [--start-chunk K]
 *          [--dump-dir <dir>]
 * prog-dir holds program.bin + prog_weights.bin (default ".").
 * --chunks/--start-chunk process a subset (debugging); the full output is
 * only correct when all chunks run (OLA needs every chunk). Default: all.
 * --dump-dir: resilient/batched mode. For each chunk, write the raw ISTFT
 * output (tar, 2 x `actual` floats, with a [start, actual] int32 header) to
 * <dir>/chunk_%03d.bin and skip the in-memory OLA + final WAV writing; a
 * separate assembler (assemble_chunks.py) does the Hann OLA + divide + trim
 * + rescale from the dump files. Chunks whose dump file already exists are
 * SKIPPED (resume-friendly: a reboot/reap only loses the in-flight chunk).
 * This mode exists because the blade reboots roughly every ~2 h and a
 * 37-chunk run does not survive it (two full runs were SIGTERM'd by
 * reboots at ~70 min and ~7 min in, 2026-11-12).
 *
 * Recipe: n_fft 6144, hop 1024, dim_f 3072, dim_t 256, chunk 261120,
 * gen 254976, trim 3072, compensate 1.01, overlap 0.25, Hann OLA.
 * Peak-normalize the mix, zero bins 0-2, instrumental = mix - vocals*1.01.
 */
#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include "sep_interp.h"
#include "sep_stft.h"
#include "wubu_audioio.h"

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

#define N_FFT 6144
#define HOP 1024
#define DIM_F 3072
#define DIM_T 256
#define CHUNK_SIZE 261120
#define TRIM 3072
#define GEN_SIZE 254976
#define OVERLAP_Q 0.25
#define COMPENSATE 1.01f

static double now_s(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

/* np.hanning(M): symmetric Hann, w[n] = 0.5 - 0.5*cos(2*pi*n/(M-1)). */
static void hanning(float *w, int M) {
    if (M <= 1) { if (M == 1) w[0] = 1.0f; return; }
    for (int n = 0; n < M; n++)
        w[n] = 0.5f - 0.5f * (float)cos(2.0 * M_PI * n / (M - 1));
}

int main(int argc, char **argv) {
    if (argc < 3) {
        fprintf(stderr, "usage: %s <input.wav> <out_vocals.wav> [--out-inst <p>] "
                "[--prog-dir <d>] [--threads N] [--chunks N] [--start-chunk K]\n", argv[0]);
        return 2;
    }
    const char *in_wav = argv[1], *out_voc = argv[2];
    const char *out_inst = NULL, *prog_dir = ".", *dump_dir = NULL;
    int max_chunks = -1, start_chunk = 0;
    for (int i = 3; i < argc; i++) {
        if (!strcmp(argv[i], "--out-inst") && i + 1 < argc) out_inst = argv[++i];
        else if (!strcmp(argv[i], "--prog-dir") && i + 1 < argc) prog_dir = argv[++i];
        else if (!strcmp(argv[i], "--dump-dir") && i + 1 < argc) dump_dir = argv[++i];
        else if (!strcmp(argv[i], "--threads") && i + 1 < argc) {
            char buf[16]; snprintf(buf, sizeof buf, "%s", argv[++i]);
            setenv("OMP_NUM_THREADS", buf, 1);
        } else if (!strcmp(argv[i], "--chunks") && i + 1 < argc) max_chunks = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--start-chunk") && i + 1 < argc) start_chunk = atoi(argv[++i]);
        else { fprintf(stderr, "unknown arg: %s\n", argv[i]); return 2; }
    }

    double t_all = now_s();
    WuBuAudio *a = wubu_audio_read_stereo(in_wav);
    if (!a) { fprintf(stderr, "cannot read %s\n", in_wav); return 1; }
    if (a->sr != 44100) { fprintf(stderr, "expected 44100 Hz, got %d\n", a->sr); return 1; }
    const int T = a->n;
    printf("mix: %.2fs (%d samples), sr %d\n", (double)T / 44100, T, a->sr);

    /* De-interleave; peak-normalize (keep the original for instrumental). */
    float *mixL = (float *)malloc((size_t)T * sizeof(float));
    float *mixR = (float *)malloc((size_t)T * sizeof(float));
    if (!mixL || !mixR) return 1;
    double peak = 0;
    for (int t = 0; t < T; t++) {
        mixL[t] = a->data[2 * (size_t)t];
        mixR[t] = a->data[2 * (size_t)t + 1];
        double ap = fabs((double)mixL[t]); if (ap > peak) peak = ap;
        ap = fabs((double)mixR[t]); if (ap > peak) peak = ap;
    }
    wubu_audio_free(a);
    printf("peak %.4f\n", peak);
    const float inv_peak = peak > 0 ? (float)(1.0 / peak) : 1.0f;

    /* Mixture: [zeros TRIM, mix/peak, zeros pad]; pad = GEN+TRIM - T%GEN. */
    const int pad = GEN_SIZE + TRIM - (T % GEN_SIZE);
    const int Tmix = TRIM + T + pad;
    const int step = (int)((1.0 - OVERLAP_Q) * CHUNK_SIZE);   /* 195840 */
    const int n_chunks = (Tmix + step - 1) / step;
    printf("mixture %d samples, step %d, chunks %d\n", Tmix, step, n_chunks);
    float *mixLn = (float *)calloc((size_t)Tmix, sizeof(float));
    float *mixRn = (float *)calloc((size_t)Tmix, sizeof(float));
    float *resL = (float *)calloc((size_t)Tmix, sizeof(float));
    float *resR = (float *)calloc((size_t)Tmix, sizeof(float));
    float *divL = (float *)calloc((size_t)Tmix, sizeof(float));
    float *divR = (float *)calloc((size_t)Tmix, sizeof(float));
    if (!mixLn || !mixRn || !resL || !resR || !divL || !divR) return 1;
    for (int t = 0; t < T; t++) {
        mixLn[TRIM + t] = mixL[t] * inv_peak;
        mixRn[TRIM + t] = mixR[t] * inv_peak;
    }

    /* Interpreter + STFT. */
    char prog_path[1024], w_path[1024];
    snprintf(prog_path, sizeof prog_path, "%s/program.bin", prog_dir);
    snprintf(w_path, sizeof w_path, "%s/prog_weights.bin", prog_dir);
    SepInterp *it = sep_interp_create(prog_path, w_path);
    if (!it) { fprintf(stderr, "cannot load program from %s\n", prog_dir); return 1; }
    SepStft *st = sep_stft_create(N_FFT, HOP);
    if (!st) return 1;
    const int n_frames = sep_stft_n_frames(st, CHUNK_SIZE);
    if (n_frames != DIM_T) { fprintf(stderr, "chunk frames %d != %d\n", n_frames, DIM_T); return 1; }
    const uint32_t in_slot = sep_interp_input_slot(it);
    const uint32_t out_slot = sep_interp_output_slot(it);
    printf("input slot %u, output slot %u, %u instructions\n",
           in_slot, out_slot, sep_interp_n_instr(it));

    /* Chunk scratch. */
    float *part = (float *)malloc((size_t)CHUNK_SIZE * sizeof(float));
    float *re = (float *)malloc((size_t)(N_FFT / 2 + 1) * DIM_T * sizeof(float));
    float *im = (float *)malloc((size_t)(N_FFT / 2 + 1) * DIM_T * sizeof(float));
    float *pcm = (float *)malloc((size_t)((DIM_T - 1) * HOP + N_FFT) * sizeof(float));
    /* tar holds BOTH channels (tarL = tar, tarR = tar + CHUNK_SIZE) so dump
     * mode can write one file per chunk with L and R. */
    float *tar = (float *)malloc((size_t)2 * CHUNK_SIZE * sizeof(float));
    float *win = (float *)malloc((size_t)CHUNK_SIZE * sizeof(float));
    if (!part || !re || !im || !pcm || !tar || !win) return 1;
    const int istft_len = (DIM_T - 1) * HOP + N_FFT;   /* 267264 */

    double t_model = 0, t_stft = 0;
    int chunk_end = max_chunks < 0 ? n_chunks : start_chunk + max_chunks;
    if (chunk_end > n_chunks) chunk_end = n_chunks;
    int n_dumped = 0, n_skipped = 0;
    for (int ci = start_chunk; ci < chunk_end; ci++) {
        const int start = ci * step;
        const int end = start + CHUNK_SIZE < Tmix ? start + CHUNK_SIZE : Tmix;
        const int actual = end - start;

        /* Dump mode: skip chunks already on disk (resume after a reboot). */
        char dump_path[1024];
        if (dump_dir) {
            snprintf(dump_path, sizeof dump_path, "%s/chunk_%03d.bin", dump_dir, ci);
            FILE *probe = fopen(dump_path, "rb");
            if (probe) {
                fclose(probe);
                n_skipped++;
                if ((ci + 1) % 5 == 0 || ci + 1 == chunk_end) {
                    printf("  chunk %d/%d (dump exists, skipped)  %.1fs\n",
                           ci + 1, n_chunks, now_s() - t_all);
                    fflush(stdout);
                }
                continue;
            }
        }

        /* STFT both channels of the (zero-padded) chunk part. */
        float *slot_in = sep_interp_slot(it, in_slot);
        memset(slot_in, 0, (size_t)4 * DIM_F * DIM_T * sizeof(float));
        for (int ch = 0; ch < 2; ch++) {
            const float *mixch = ch == 0 ? mixLn : mixRn;
            memcpy(part, mixch + start, (size_t)actual * sizeof(float));
            if (actual < CHUNK_SIZE)
                memset(part + actual, 0, (size_t)(CHUNK_SIZE - actual) * sizeof(float));
            double ts = now_s();
            if (sep_stft_forward(st, part, CHUNK_SIZE, re, im) != DIM_T) {
                fprintf(stderr, "chunk %d: STFT failed\n", ci); return 1;
            }
            t_stft += now_s() - ts;
            /* Copy re then im for this channel (explicit, no aliasing tricks). */
            float *dst_re = slot_in + (size_t)(2 * ch + 0) * DIM_F * DIM_T;
            float *dst_im = slot_in + (size_t)(2 * ch + 1) * DIM_F * DIM_T;
            for (int b = 3; b < DIM_F; b++) {
                memcpy(dst_re + (size_t)b * DIM_T, re + (size_t)b * DIM_T, (size_t)DIM_T * sizeof(float));
                memcpy(dst_im + (size_t)b * DIM_T, im + (size_t)b * DIM_T, (size_t)DIM_T * sizeof(float));
            }
        }

        /* Model forward. */
        double tm = now_s();
        if (sep_interp_run(it)) { fprintf(stderr, "chunk %d: model failed\n", ci); return 1; }
        t_model += now_s() - tm;

        /* ISTFT both channels; trim TRIM each end -> CHUNK_SIZE samples. */
        float *slot_out = sep_interp_slot(it, out_slot);
        for (int ch = 0; ch < 2; ch++) {
            const float *ore = slot_out + (size_t)(2 * ch + 0) * DIM_F * DIM_T;
            const float *oim = slot_out + (size_t)(2 * ch + 1) * DIM_F * DIM_T;
            double ts = now_s();
            if (sep_istft(st, ore, oim, DIM_F, DIM_T, pcm) != istft_len) {
                fprintf(stderr, "chunk %d: ISTFT failed\n", ci); return 1;
            }
            t_stft += now_s() - ts;
            float *tarch = tar + (size_t)ch * CHUNK_SIZE;
            memcpy(tarch, pcm + TRIM, (size_t)CHUNK_SIZE * sizeof(float));
            if (dump_dir) continue; /* OLA is the assembler's job */
            /* Hann OLA: window the chunk, add to result, accumulate divider. */
            hanning(win, actual);
            float *res = ch == 0 ? resL : resR;
            float *div = ch == 0 ? divL : divR;
            for (int i = 0; i < actual; i++) {
                res[start + i] += tarch[i] * win[i];
                div[start + i] += win[i];
            }
        }
        if (dump_dir) {
            /* Write [start:int32, actual:int32, L(actual), R(actual)]. */
            FILE *f = fopen(dump_path, "wb");
            if (!f) { fprintf(stderr, "cannot write %s\n", dump_path); return 1; }
            int32_t hdr[2] = { start, actual };
            fwrite(hdr, sizeof(int32_t), 2, f);
            fwrite(tar, sizeof(float), (size_t)actual, f);
            fwrite(tar + CHUNK_SIZE, sizeof(float), (size_t)actual, f);
            fclose(f);
            n_dumped++;
        }
        if ((ci + 1) % 5 == 0 || ci + 1 == chunk_end) {
            printf("  chunk %d/%d  %.1fs (model %.1fs, stft %.1fs)\n",
                   ci + 1, n_chunks, now_s() - t_all, t_model, t_stft);
            fflush(stdout);
        }
    }

    double wall = now_s() - t_all;
    if (dump_dir) {
        printf("dump done: %d chunks written, %d skipped (already on disk), "
               "%.1fs wall; chunks %d-%d of %d\n",
               n_dumped, n_skipped, wall, start_chunk, chunk_end - 1, n_chunks);
        return 0;
    }

    /* Finalize: divide by the OLA divider, trim TRIM, truncate to T, rescale. */
    float *vocL = (float *)malloc((size_t)T * sizeof(float));
    float *vocR = (float *)malloc((size_t)T * sizeof(float));
    if (!vocL || !vocR) return 1;
    for (int t = 0; t < T; t++) {
        float d = divL[TRIM + t]; if (d < 1e-8f) d = 1e-8f;
        vocL[t] = resL[TRIM + t] / d * (float)peak;
        d = divR[TRIM + t]; if (d < 1e-8f) d = 1e-8f;
        vocR[t] = resR[TRIM + t] / d * (float)peak;
    }
    float *inter = (float *)malloc((size_t)T * 2 * sizeof(float));
    if (!inter) return 1;
    for (int t = 0; t < T; t++) {
        inter[2 * (size_t)t] = vocL[t];
        inter[2 * (size_t)t + 1] = vocR[t];
    }
    if (wubu_audio_write(out_voc, inter, T, 44100, 1)) {
        fprintf(stderr, "cannot write %s\n", out_voc); return 1;
    }
    printf("wrote %s\n", out_voc);
    if (out_inst) {
        for (int t = 0; t < T; t++) {
            inter[2 * (size_t)t] = mixL[t] - vocL[t] * COMPENSATE;
            inter[2 * (size_t)t + 1] = mixR[t] - vocR[t] * COMPENSATE;
        }
        if (wubu_audio_write(out_inst, inter, T, 44100, 1)) {
            fprintf(stderr, "cannot write %s\n", out_inst); return 1;
        }
        printf("wrote %s\n", out_inst);
    }
    wall = now_s() - t_all;
    printf("demix done: %.1fs wall for %.1fs of audio (%.2fx realtime); "
           "model %.1fs, stft %.1fs; chunks %d-%d of %d\n",
           wall, (double)T / 44100, wall / ((double)T / 44100),
           t_model, t_stft, start_chunk, chunk_end - 1, n_chunks);
    return 0;
}
