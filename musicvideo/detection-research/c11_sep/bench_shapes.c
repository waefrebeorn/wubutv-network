#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "sep_gemm.h"
static double now_s(void){struct timespec ts;clock_gettime(CLOCK_MONOTONIC,&ts);return ts.tv_sec+ts.tv_nsec*1e-9;}
static float frand(unsigned *s){*s=*s*1664525u+1013904223u;return (float)((*s>>9)&0xFFFFFF)/8388608.0f-1.0f;}
static void bench(const char *name,int M,int N,int K,int iters){
    unsigned s=999; float *A=malloc((size_t)M*K*sizeof(float)); float *B=malloc((size_t)K*N*sizeof(float)); float *C=calloc((size_t)M*N,sizeof(float));
    for(int i=0;i<M*K;i++)A[i]=frand(&s); for(int i=0;i<K*N;i++)B[i]=frand(&s);
    sgemm_acc(M,N,K,A,K,B,N,C,N);
    double t0=now_s(); for(int it=0;it<iters;it++)sgemm_acc(M,N,K,A,K,B,N,C,N);
    double dt=(now_s()-t0)/iters; double gf=2.0*(double)M*N*K/dt/1e9;
    double sum=0; for(int i=0;i<M*N;i+=997)sum+=C[i];
    printf("%-28s M=%-7d N=%-6d K=%-5d: %.2f s  %.1f GFLOPS  (chk %.1f)\n",name,M,N,K,dt,gf,sum);
    free(A);free(B);free(C);
}
int main(void){
    bench("im2col 3x3 (M huge)",786432,48,432,2);
    bench("out^T 1x1 (M huge)",786432,48,48,2);
    bench("matmul 3072->384 (ref)",12288,384,3072,2);
    bench("matmul 384->3072 (ref)",12288,3072,384,2);
    return 0;
}
