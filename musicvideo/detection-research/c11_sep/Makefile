# c11_sep — C11 separation runner (MDX-Net, torch-free)
# Blade: 1.5 shared CPUs / 6 GB, AVX512 available (AMD EPYC 9D25).
# -march=native: binary is blade-only by design.
CC = gcc
CFLAGS = -O3 -march=native -std=c11 -Wall -Wextra -fopenmp -ffast-math
LDFLAGS = -fopenmp -lm
OMP_THREADS = 2

LEGO = wubu_fft.c wubu_audioio.c
CORE = sep_stft.c

test_stft: test_stft.c $(CORE) sep_fft.c sep_fft64.c $(LEGO) sep_stft.h wubu_fft.h wubu_audioio.h sep_fft.h sep_fft64.h
	$(CC) $(CFLAGS) -o $@ test_stft.c $(CORE) sep_fft.c sep_fft64.c $(LEGO) $(LDFLAGS)

check-stft: test_stft
	OMP_NUM_THREADS=$(OMP_THREADS) ./test_stft .

test_block1: test_block1.c sep_ops.c sep_ops.h
	$(CC) $(CFLAGS) -o $@ test_block1.c sep_ops.c $(LDFLAGS)

check-block1: test_block1
	OMP_NUM_THREADS=$(OMP_THREADS) ./test_block1 .

test_interp: test_interp.c sep_interp.c sep_interp.h sep_ops.c sep_gemm.c
	$(CC) $(CFLAGS) -o $@ test_interp.c sep_interp.c sep_ops.c sep_gemm.c $(LDFLAGS)

check-interp: test_interp
	OMP_NUM_THREADS=$(OMP_THREADS) ./test_interp .

sep_main: sep_main.c sep_interp.c sep_interp.h sep_ops.c sep_gemm.c sep_stft.c sep_fft.c sep_fft64.c $(LEGO)
	$(CC) $(CFLAGS) -o $@ sep_main.c sep_interp.c sep_ops.c sep_gemm.c sep_stft.c sep_fft.c sep_fft64.c $(LEGO) $(LDFLAGS)

# Full-track run on MV-14 (37 chunks). Writes c11_vocals.wav + c11_inst.wav.
run-mv14: sep_main
	OMP_NUM_THREADS=$(OMP_THREADS) ./sep_main /home/hatch/workspace/wubuwizard-cpu-sep/mv14_44k.wav c11_vocals.wav --out-inst c11_inst.wav

clean:
	rm -f test_stft test_block1 test_gemm test_interp sep_main

.PHONY: check-stft clean
