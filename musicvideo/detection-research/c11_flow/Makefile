# c11_flow — C11 Farneback dense optical flow (F-05's SLERM).
# libc + libm only. gcc -std=c11 -O2 -Wall -Wextra, zero warnings.

CC      = gcc
CFLAGS  = -std=c11 -O2 -Wall -Wextra
LDFLAGS = -lm

all: c11_flow test_expand

c11_flow: c11_flow.c
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

test_expand: test_expand.c c11_flow.c
	$(CC) $(CFLAGS) -o $@ test_expand.c $(LDFLAGS)

clean:
	rm -f c11_flow test_expand

check: all
	./test_expand

.PHONY: all clean check
