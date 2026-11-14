/* test_fft.c — sep_fft(6144) vs numpy float64 reference, forward + inverse. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "sep_fft.h"
static float *read_f32(const char *p, size_t n){FILE*f=fopen(p,"rb");if(!f)return NULL;float*b=malloc(n*sizeof(float));if(fread(b,sizeof(float),n,f)!=n){free(b);fclose(f);return NULL;}fclose(f);return b;}
int main(int argc,char**argv){
    float *sig=read_f32(argv[1],6144); float *ref_re=read_f32(argv[2],6144); float *ref_im=read_f32(argv[3],6144);
    if(!sig||!ref_re||!ref_im){fprintf(stderr,"read fail\n");return 1;}
    WuBuCpx *a=malloc(6144*sizeof(WuBuCpx));
    for(int i=0;i<6144;i++){a[i].re=sig[i];a[i].im=0;}
    sep_fft(a,6144,1); /* forward/6144 */
    double md=0,scale=0; for(int i=0;i<6144;i++){double r=a[i].re*6144-ref_re[i],im=a[i].im*6144-ref_im[i];double d=sqrt(r*r+im*im);if(d>md)md=d;double m=sqrt((double)ref_re[i]*ref_re[i]+(double)ref_im[i]*ref_im[i]);if(m>scale)scale=m;}
    printf("FFT6144 fwd: max|diff| %.3e  (spectrum max %.1f, rel %.2e)\n",md,scale,md/scale);
    /* inverse round-trip: sep_fft(inv=0) should give 6144*x */
    sep_fft(a,6144,0);
    double md2=0; for(int i=0;i<6144;i++){double d=fabs(a[i].re/6144.0-sig[i]);if(d>md2)md2=d;}
    printf("FFT6144 round-trip: max|diff| %.3e\n",md2);
    return 0;
}
