CC = gcc
CFLAGS = -std=c11 -O2 -Wall -Wextra -I../c11_mir
LDLIBS = -lm

all: c11_voice

c11_voice: c11_voice.c ../c11_mir/json.c ../c11_mir/json.h
	$(CC) $(CFLAGS) -o $@ c11_voice.c ../c11_mir/json.c $(LDLIBS)

test: c11_voice
	./c11_voice --selftest

asan: c11_voice.c ../c11_mir/json.c
	$(CC) -std=c11 -O1 -g -fsanitize=address,undefined -fno-omit-frame-pointer \
		-I../c11_mir -o c11_voice_asan c11_voice.c ../c11_mir/json.c $(LDLIBS)
	./c11_voice_asan --selftest

clean:
	rm -f c11_voice c11_voice_asan

.PHONY: all test asan clean
