/* test_fft64.c — sep_fft64(6144) vs numpy float64 reference. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "sep_fft64.h"
static float *read_f32(const char *p, size_t n){FILE*f=fopen(p,"rb");if(!f)return NULL;float*b=malloc(n*sizeof(float));if(fread(b,sizeof(float),n,f)!=n){free(b);fclose(f);return NULL;}fclose(f);return b;}
int main(int argc,char**argv){
    float *sig=read_f32(argv[1],6144); float *ref_re=read_f32(argv[2],6144); float *ref_im=read_f32(argv[3],6144);
    if(!sig||!ref_re||!ref_im){fprintf(stderr,"read fail\n");return 1;}
    double *re=malloc(6144*sizeof(double)), *im=malloc(6144*sizeof(double));
    for(int i=0;i<6144;i++){re[i]=sig[i];im[i]=0;}
    sep_fft64(re,im,6144,1); /* forward/6144 */
    double md=0,scale=0; for(int i=0;i<6144;i++){double r=re[i]*6144-ref_re[i],q=im[i]*6144-ref_im[i];double d=sqrt(r*r+q*q);if(d>md)md=d;double m=sqrt((double)ref_re[i]*ref_re[i]+(double)ref_im[i]*ref_im[i]);if(m>scale)scale=m;}
    printf("FFT64 fwd: max|diff| %.3e (spectrum max %.1f, rel %.2e)\n",md,scale,md/scale);
    int bad=0; for(int i=0;i<6144;i++){double r=re[i]*6144-ref_re[i],q=im[i]*6144-ref_im[i];if(sqrt(r*r+q*q)>1e-3)bad++;}
    printf("bins with err>1e-3: %d / 6144\n",bad);
    /* check the k2=1 region specifically: bins 2048..4095 */
    double md2=0; for(int i=2048;i<4096;i++){double r=re[i]*6144-ref_re[i],q=im[i]*6144-ref_im[i];double d=sqrt(r*r+q*q);if(d>md2)md2=d;}
    printf("bins 2048-4095 max|diff|: %.3e\n",md2);
    return 0;
}
