/* test_interp.c — Stage 3b: full-graph chunk-0 validation vs ORT reference.
 *
 * Loads input_spek_f32.bin into the input slot, steps through the program
 * instruction by instruction, and after each checkpoint instruction compares
 * that instruction's output slot against the ORT stride-32 sample + stats
 * in ckpts/ (node 177 vs final_output_f32.bin, full comparison).
 * Bar per checkpoint (same as Stage 2): sample max|diff| <= max(2e-3,
 * 1e-5*range) AND corr >= 0.99999 AND full-tensor mean/std within 0.1%.
 * Prints per-instruction timing at the end (top 10 by time).
 * Exit 0 iff all checkpoints pass.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "sep_interp.h"
#include "sep_prog.h"

#define STRIDE 32

static float *read_f32(const char *path, size_t n) {
    FILE *f = fopen(path, "rb");
    if (!f) { fprintf(stderr, "cannot open %s\n", path); return NULL; }
    float *b = (float *)malloc(n * sizeof(float));
    if (!b) { fclose(f); return NULL; }
    if (fread(b, sizeof(float), n, f) != n) { fprintf(stderr, "short read %s\n", path); free(b); fclose(f); return NULL; }
    fclose(f);
    return b;
}

static double *read_f64(const char *path, size_t n) {
    FILE *f = fopen(path, "rb");
    if (!f) { fprintf(stderr, "cannot open %s\n", path); return NULL; }
    double *b = (double *)malloc(n * sizeof(double));
    if (!b) { fclose(f); return NULL; }
    if (fread(b, sizeof(double), n, f) != n) { fprintf(stderr, "short read %s\n", path); free(b); fclose(f); return NULL; }
    fclose(f);
    return b;
}

/* checkpoints.json is read by a tiny hand parser (fixed format from the
 * compiler): {"0": {"instr": 0, "slot": 1, "shape": [48, 3072, 256]}, ...} */
typedef struct { int node, instr, slot, C, H, W; } Ckpt;
static int n_ckpt = 0;
static Ckpt ckpts[32]; /* 24 checkpoints now (16 original + 8 fine);
                          MUST exceed the count in checkpoints.json —
                          a 16-slot array overflowed when the fine
                          checkpoints were added and silently dropped node 75. */

static int load_ckpts(const char *path) {
    FILE *f = fopen(path, "r");
    if (!f) return 1;
    char buf[8192];
    size_t n = fread(buf, 1, sizeof(buf) - 1, f);
    fclose(f);
    buf[n] = 0;
    /* parse "node": {"instr": I, "slot": S, "shape": [C, H, W]} */
    char *p = buf;
    while ((p = strchr(p, '"')) != NULL) {
        int node, instr, slot, C, H, W;
        /* whitespace-tolerant: a space in the format matches any whitespace
         * (the compiler writes indent=2 JSON, so fields span lines). */
        if (sscanf(p, "\"%d\" : { \"instr\" : %d , \"slot\" : %d , \"shape\" : [ %d , %d , %d ]",
                   &node, &instr, &slot, &C, &H, &W) == 6) {
            ckpts[n_ckpt].node = node;
            ckpts[n_ckpt].instr = instr;
            ckpts[n_ckpt].slot = slot;
            ckpts[n_ckpt].C = C;
            ckpts[n_ckpt].H = H;
            ckpts[n_ckpt].W = W;
            n_ckpt++;
        }
        p++;
    }
    return 0;
}

static int check_ckpt(const char *dir, const Ckpt *c, const float *data) {
    char path[1024];
    const size_t n = (size_t)c->C * c->H * c->W;
    if (c->node == 177) {
        /* full comparison vs final_output_f32.bin */
        snprintf(path, sizeof path, "%s/final_output_f32.bin", dir);
        float *ref = read_f32(path, n);
        if (!ref) return 1;
        double maxd = 0, sa = 0, sb = 0;
        for (size_t i = 0; i < n; i++) {
            double d = fabs((double)data[i] - (double)ref[i]);
            if (d > maxd) maxd = d;
            sa += data[i]; sb += ref[i];
        }
        double ma = sa / n, mb = sb / n, sab = 0, saa = 0, sbb = 0;
        for (size_t i = 0; i < n; i++) {
            double da = data[i] - ma, db = ref[i] - mb;
            sab += da * db; saa += da * da; sbb += db * db;
        }
        double corr = sab / sqrt(saa * sbb);
        printf("node 177 (final): full max|diff| %.3e  corr %.6f  -> %s\n",
               maxd, corr, (maxd <= 2e-3 && corr >= 0.99999) ? "PASS" : "FAIL");
        free(ref);
        return (maxd <= 2e-3 && corr >= 0.99999) ? 0 : 1;
    }
    const size_t sn = (n + STRIDE - 1) / STRIDE;
    snprintf(path, sizeof path, "%s/ckpts/ckpt%03d_sample.bin", dir, c->node);
    float *sample = read_f32(path, sn);
    snprintf(path, sizeof path, "%s/ckpts/ckpt%03d_stats.bin", dir, c->node);
    double *st = read_f64(path, 5);
    if (!sample || !st) return 1;
    double maxd = 0, sa = 0, sb = 0;
    for (size_t i = 0; i < sn; i++) {
        double a = data[i * STRIDE], b = sample[i];
        double d = fabs(a - b);
        if (d > maxd) maxd = d;
        sa += a; sb += b;
    }
    double ma = sa / sn, mb = sb / sn, sab = 0, saa = 0, sbb = 0;
    for (size_t i = 0; i < sn; i++) {
        double da = data[i * STRIDE] - ma, db = sample[i] - mb;
        sab += da * db; saa += da * da; sbb += db * db;
    }
    double corr = sab / sqrt(saa * sbb);
    double mn = data[0], mx = data[0], sum = 0, sum2 = 0;
#pragma omp parallel for reduction(min:mn) reduction(max:mx) reduction(+:sum,sum2) schedule(static)
    for (size_t i = 0; i < n; i++) {
        double v = data[i];
        if (v < mn) mn = v;
        if (v > mx) mx = v;
        sum += v; sum2 += v * v;
    }
    double mean = sum / n;
    double std = sqrt(sum2 / n - mean * mean);
    double range = st[3] - st[2];
    double bar = (2e-3 > 1e-5 * range) ? 2e-3 : 1e-5 * range;
    int ok = (maxd <= bar) && (corr >= 0.99999) &&
             (fabs(mean - st[0]) <= 1e-3 * fabs(st[0]) + 1e-6) &&
             (fabs(std - st[1]) <= 1e-3 * st[1]);
    printf("node %3d: sample max|diff| %.3e (bar %.1e) corr %.6f | "
           "mean %.5f vs %.5f  std %.4f vs %.4f  -> %s\n",
           c->node, maxd, bar, corr, mean, st[0], std, st[1], ok ? "PASS" : "FAIL");
    free(sample); free(st);
    return ok ? 0 : 1;
}

int main(int argc, char **argv) {
    const char *dir = argc > 1 ? argv[1] : ".";
    char path[1024];
    if (load_ckpts("checkpoints.json") != 0) { fprintf(stderr, "cannot load checkpoints.json\n"); return 1; }
    printf("checkpoints: %d\n", n_ckpt);

    SepInterp *it = sep_interp_create("program.bin", "prog_weights.bin");
    if (!it) { fprintf(stderr, "interp create failed\n"); return 1; }

    snprintf(path, sizeof path, "%s/input_spek_f32.bin", dir);
    float *spek = read_f32(path, 4 * (size_t)3072 * 256);
    if (!spek) return 1;
    memcpy(sep_interp_slot(it, sep_interp_input_slot(it)), spek,
           4 * (size_t)3072 * 256 * sizeof(float));
    free(spek);

    int fail = 0;
    uint32_t n_instr = sep_interp_n_instr(it);
    for (uint32_t i = 0; i < n_instr; i++) {
        int rc = sep_interp_step(it, i);
        if (rc) { fprintf(stderr, "instr %u failed (rc %d)\n", i, rc); return 1; }
        for (int k = 0; k < n_ckpt; k++) {
            if (ckpts[k].instr == (int)i) {
                fail |= check_ckpt(dir, &ckpts[k], sep_interp_slot(it, ckpts[k].slot));
            }
        }
    }
    printf("chunk-0 forward: %.2f s total\n", sep_interp_total_time(it));
    /* top-10 instructions by time */
    printf("top-10 instructions by time:\n");
    {
        typedef struct { uint32_t idx; double t; } TI;
        TI *arr = malloc(n_instr * sizeof(TI));
        for (uint32_t i = 0; i < n_instr; i++) {
            arr[i].idx = i;
            arr[i].t = sep_interp_time(it, i);
        }
        for (uint32_t i = 0; i < n_instr; i++)
            for (uint32_t j = i + 1; j < n_instr; j++)
                if (arr[j].t > arr[i].t) { TI tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp; }
        for (int t = 0; t < 10 && t < (int)n_instr; t++) {
            const SepInstr *ins = sep_interp_instr(it, arr[t].idx);
            printf("  instr %3u op %u: %.2f s\n", arr[t].idx, ins->op, arr[t].t);
        }
        free(arr);
    }
    printf("INTERP: %s\n", fail ? "FAIL" : "PASS");
    sep_interp_free(it);
    return fail;
}
