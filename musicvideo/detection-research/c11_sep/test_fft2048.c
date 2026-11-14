/* Isolate fft2048_64 vs numpy float64 on a 2048-point signal. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "sep_fft64.h"
#include "sep_fft64.c"  /* pull in the statics */
static float *read_f32(const char *p, size_t n){FILE*f=fopen(p,"rb");if(!f)return NULL;float*b=malloc(n*sizeof(float));if(fread(b,sizeof(float),n,f)!=n){free(b);fclose(f);return NULL;}fclose(f);return b;}
int main(int argc,char**argv){
    float *sig=read_f32(argv[1],2048); float *rr=read_f32(argv[2],2048); float *ri=read_f32(argv[3],2048);
    if(!sig||!rr||!ri){fprintf(stderr,"read fail\n");return 1;}
    double *re=malloc(2048*sizeof(double)), *im=malloc(2048*sizeof(double));
    for(int i=0;i<2048;i++){re[i]=sig[i];im[i]=0;}
    fft2048_64(re,im,1);
    double md=0; for(int i=0;i<2048;i++){double r=re[i]*2048-rr[i],q=im[i]*2048-ri[i];double d=sqrt(r*r+q*q);if(d>md)md=d;}
    printf("fft2048_64 fwd: max|diff| %.3e\n",md);
    /* also test fft3_64 directly: X = DFT3 of (1,2,3) forward */
    double a[3]={1,2,3}, b[3]={0,0,0};
    fft3_64(a,b,1);
    printf("fft3_64(1,2,3) fwd: X0=%.4f%+.4fi X1=%.4f%+.4fi X2=%.4f%+.4fi\n",a[0],b[0],a[1],b[1],a[2],b[2]);
    printf("expected: X0=6, X1=-1.5+0.866025i, X2=-1.5-0.866025i\n");
    return 0;
}
