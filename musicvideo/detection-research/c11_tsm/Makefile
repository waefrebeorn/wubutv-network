# c11_tsm — C11 per-gap-targeted time-stretch core (M7 + OLA256 fallback)
CC = gcc
CFLAGS = -std=c11 -O2 -Wall -Wextra
LDLIBS = -lm

all: c11_tsm

c11_tsm: c11_tsm.c
	$(CC) $(CFLAGS) -o $@ c11_tsm.c $(LDLIBS)

asan: c11_tsm.c
	$(CC) -std=c11 -O1 -g -fsanitize=address,undefined -Wall -Wextra -o c11_tsm_asan c11_tsm.c $(LDLIBS)

clean:
	rm -f c11_tsm c11_tsm_asan

.PHONY: all asan clean
