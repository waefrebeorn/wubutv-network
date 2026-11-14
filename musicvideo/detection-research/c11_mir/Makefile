# c11_mir — C11 MIR core. One source (+ LEGO'd libjson for snap), two binaries:
#   c11_mir      — the MIR core (modes: beats [default] | features | snap)
#   beat_tracker — alias for old callers (beats mode, sprint-3 behaviour)
CC = gcc
CFLAGS = -std=c11 -O2 -Wall -Wextra
LDLIBS = -lm

all: c11_mir beat_tracker

c11_mir: c11_mir.c json.c json.h
	$(CC) $(CFLAGS) -o $@ c11_mir.c json.c $(LDLIBS)

beat_tracker: c11_mir.c json.c json.h
	$(CC) $(CFLAGS) -o $@ c11_mir.c json.c $(LDLIBS)

clean:
	rm -f c11_mir beat_tracker

.PHONY: all clean
