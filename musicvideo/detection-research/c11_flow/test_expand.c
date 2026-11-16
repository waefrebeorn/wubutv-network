/* Probe for poly_expand (LSQ form): test images with known exact
 * quadratic coefficients. Compile:
 *   gcc -std=c11 -O2 -Wall -Wextra -o test_expand test_expand.c -lm
 * Requires c11_flow.c in the same directory (renames its main). */

#define main c11_flow_main_unused
#include "c11_flow.c"
#undef main

static void check(const char *name, const img_t *f, int n, double sigma)
{
    lsq_t L = lsq_prepare(n, sigma);
    poly_t p = poly_expand(f, &L);
    int w = f->w, h = f->h;
    /* Interior: ignore the outer 2*n pixels (kernel edge effects). */
    double a11_max = 0, a22_max = 0, a12_max = 0;
    double bx_err = 0, by_err = 0;
    int cnt = 0;
    for (int y = 2 * n; y < h - 2 * n; ++y) {
        for (int x = 2 * n; x < w - 2 * n; ++x) {
            size_t i = (size_t)y * w + x;
            double ex = (double)(x - w / 2), ey = (double)(y - h / 2);
            /* f = 0.05*ex^2 + 0.03*ey^2 + 0.02*ex*ey + 0.7*ex - 0.4*ey + 128
             * exact: A11=0.05, A22=0.03, A12(xy coeff)=0.02,
             * bx = 0.1*ex + 0.02*ey + 0.7, by = 0.06*ey + 0.02*ex - 0.4 */
            double want_a11 = 0.05, want_a22 = 0.03, want_a12 = 0.02;
            double want_bx = 0.1 * ex + 0.02 * ey + 0.7;
            double want_by = 0.06 * ey + 0.02 * ex - 0.4;
            double a11 = (double)p.p[3].d[i];
            double a22 = (double)p.p[2].d[i];
            double a12 = (double)p.p[4].d[i];
            double bx = (double)p.p[1].d[i];
            double by = (double)p.p[0].d[i];
            if (fabs(a11 - want_a11) > a11_max) a11_max = fabs(a11 - want_a11);
            if (fabs(a22 - want_a22) > a22_max) a22_max = fabs(a22 - want_a22);
            if (fabs(a12 - want_a12) > a12_max) a12_max = fabs(a12 - want_a12);
            if (fabs(bx - want_bx) > bx_err) bx_err = fabs(bx - want_bx);
            if (fabs(by - want_by) > by_err) by_err = fabs(by - want_by);
            ++cnt;
        }
    }
    printf("%s: n=%d sigma=%.2f npts=%d  max|A11-0.05|=%.2e  "
           "max|A22-0.03|=%.2e  max|A12-0.02|=%.2e  max|bx-want|=%.2e  "
           "max|by-want|=%.2e\n",
           name, n, sigma, cnt, a11_max, a22_max, a12_max, bx_err, by_err);
    poly_free(&p);
    lsq_free(&L);
}

int main(void)
{
    const int w = 64, h = 64;
    img_t f = img_alloc(w, h);
    for (int y = 0; y < h; ++y)
        for (int x = 0; x < w; ++x) {
            double ex = (double)(x - w / 2), ey = (double)(y - h / 2);
            f.d[(size_t)y * w + x] =
                (float)(0.05 * ex * ex + 0.03 * ey * ey +
                        0.02 * ex * ey + 0.7 * ex - 0.4 * ey + 128.0);
        }
    check("quadratic", &f, 5, 1.1);
    check("quadratic-n3", &f, 3, 1.0);
    /* Flat image: every coefficient must be ~0. */
    for (size_t i = 0; i < (size_t)w * h; ++i)
        f.d[i] = 128.0f;
    lsq_t L = lsq_prepare(5, 1.1);
    poly_t p = poly_expand(&f, &L);
    double worst = 0.0;
    for (size_t i = 0; i < (size_t)w * h; ++i)
        for (int c = 0; c < 5; ++c) {
            double v = fabs((double)p.p[c].d[i]);
            if (v > worst) worst = v;
        }
    printf("flat-128: max |coeff| over all 5 planes = %.3e (want ~0)\n",
           worst);
    poly_free(&p);
    lsq_free(&L);
    img_free(&f);
    return 0;
}
