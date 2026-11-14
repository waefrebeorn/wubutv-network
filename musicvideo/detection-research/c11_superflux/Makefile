# c11_superflux — SuperFlux-family onset detection functions. Single source.
# LEGO: WAV reader / FFT / Slaney mel bank from ../c11_mir/c11_mir.c (user's
# own module, copied + n_fft parameterised); inputs from ../c11_hpss and
# ../c11_voice artifacts.
CC = gcc
CFLAGS = -std=c11 -O2 -Wall -Wextra
LDLIBS = -lm

all: c11_superflux

c11_superflux: c11_superflux.c
	$(CC) $(CFLAGS) -o $@ c11_superflux.c $(LDLIBS)

clean:
	rm -f c11_superflux

.PHONY: all clean
