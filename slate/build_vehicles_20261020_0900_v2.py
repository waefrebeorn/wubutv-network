#!/usr/bin/env python3
"""Build v2 named-correction vehicles for the 2026-10-20 09:00 EDT run.
b1275: named two-axis TEXT + VOICE correction.
b1287: named single-axis TEXT correction.
b1288: named two-axis STAGING + VOICE correction.
Each asserts the v1 vehicle md5 on disk before editing.
"""
import hashlib

D = '/home/hatch/workspace/wubutv-network/slate/'

V1 = {
    'b1275': '809769ef1e3c4ddd2d2eb885a256cb74',
    'b1287': '40cd6482640a950e590f538138fa1a6f',
    'b1288': '8a5d42bf88b22284695384dfe36dea21',
}

def load(num):
    p = f'{D}fire_{num}_20261020_0900_v1.txt'
    t = open(p).read()
    assert hashlib.md5(t.encode()).hexdigest() == V1[num], f'v1 md5 mismatch {num}'
    return t

def save(num, text, label):
    assert 'no meta-text describing the bug' in text, 'anti-leak clause lost'
    assert text.endswith('no spelling-out of the tilde instruction as words.'), 'tail changed'
    for tok in ('B-245', '0015', 'Source:', 'FRESH', 'provisional'):
        assert tok not in text, f'citation leak {tok}'
    p = f'{D}fire_{num}_20261020_0900_v2.txt'
    open(p, 'w').write(text)
    print(f'{num} {label}: {len(text)} bytes, md5 {hashlib.md5(text.encode()).hexdigest()}')

# ---- B-1275 v2: named two-axis TEXT + VOICE correction ----
t = load('b1275')
old = 'TEXT: allowlist = none — no text anywhere in the frame; the door bare steel, the lock unmarked.'
new = ('TEXT: allowlist = none — no text anywhere in the frame; the door BARE STEEL — '
       'no unit number, no "S-16" sign, no door stencils, no number tokens, no lettering of any kind '
       'on the door, the hasp plate, or anywhere in the frame, in EVERY frame; the lock unmarked.')
assert old in t; t = t.replace(old, new)
old = ('[8s] ONE voice event, off-camera, no mouth on screen: "Locked for the night." — one utterance; '
       "the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance COMPLETE BY 8.75s.")
new = ('[8s] ONE voice event, off-camera, no mouth on screen: "Locked for the night." — one utterance; '
       "the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance MUST be COMPLETE "
       'BY 8.75s — no voice-grade sound after 8.75s, ever.')
assert old in t; t = t.replace(old, new)
old = 'no unit numbers, no door stencils, no second lock,'
new = 'no unit numbers, no "S-16" sign, no door stencils, no number tokens, no second lock,'
assert old in t; t = t.replace(old, new)
save('b1275', t, 'TEXT+VOICE correction')

# ---- B-1287 v2: named single-axis TEXT correction ----
t = load('b1287')
old = 'SUBJECTS: the street — one pillar box on the pavement at 0.5s, its slot open; one envelope in the hands at 0.5s.'
new = ('SUBJECTS: the street — one pillar box on the pavement at 0.5s, its slot open; one envelope in the hands '
       'at 0.5s. The street is BARE — plain pavement, plain building fronts with NO shop window, NO signage, '
       'NO "ROYAL MAIL" sign, NO awning lettering, NO posters, NO window displays, NO lettering of any kind '
       'anywhere behind the box, in EVERY frame.')
assert old in t; t = t.replace(old, new)
old = 'TEXT: allowlist = none — no text anywhere in the frame; the box unmarked (no cipher, no collection plate), the envelope blank.'
new = ('TEXT: allowlist = none — no text anywhere in the frame; the box unmarked (no cipher, no collection plate), '
       'the envelope blank, the street bare — no shop signs, no awning text, no posters, no display lettering, '
       'no lettering of any kind anywhere in the frame.')
assert old in t; t = t.replace(old, new)
old = 'no invented text, no letter-shaped noise, no box cipher, no collection plate, no address on the envelope,'
new = ('no invented text, no letter-shaped noise, no box cipher, no collection plate, no address on the envelope, '
       'no shop window, no "ROYAL MAIL" sign, no awning text, no posters, no window displays, no street lettering of any kind,')
assert old in t; t = t.replace(old, new)
save('b1287', t, 'TEXT correction')

# ---- B-1288 v2: named two-axis STAGING + VOICE correction ----
t = load('b1288')
old = 'SUBJECTS: the lobby — one counter, one pinboard, bare at 0.5s; one whole ticket in the hands at 0.5s.'
new = ('SUBJECTS: the lobby — one plain wooden counter, one pinboard, plain bare walls, BARE at 0.5s — NOTHING '
       'else in the room: no concession stand, no popcorn machine, no cash register, no display case, no shelves, '
       'no posters, no papers, no signage, no fire extinguisher. One whole ticket in the hands at 0.5s — the ticket '
       'BLANK-FACED, no text on the ticket, no "SOLD OUT", no "WuBuTV" on the ticket, ever.')
assert old in t; t = t.replace(old, new)
old = ('[4s] ONE tearing — the ticket torn down its perforation — one tearing, never two; '
       'one soft paper bed at 4s (non-speech — directed sound).')
new = ('[4s] ONE tearing — the ticket torn down its perforation — a clean parting along the perforation line, '
       'NOT a crumple, NOT a wad — one tearing, never two; one soft paper bed at 4s (non-speech — directed sound).')
assert old in t; t = t.replace(old, new)
old = ('[8s] ONE voice event, off-camera, no mouth on screen: "Half for the coat." — one utterance; '
       "the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance COMPLETE BY 8.75s.")
new = ('[8s] ONE voice event, off-camera, no mouth on screen: "Half for the coat." — one utterance; '
       "the line's FIRST SOUND lands AT 7.5s or LATER, never before 7.5s; the utterance MUST be COMPLETE "
       'BY 8.75s — no voice-grade sound after 8.75s, ever.')
assert old in t; t = t.replace(old, new)
old = 'TEXT: allowlist = none — no text anywhere in the frame; the ticket blank-faced, the board bare.'
new = ('TEXT: allowlist = none — no text anywhere in the frame; the ticket blank-faced — NO text on the ticket '
       'itself — the board bare, the lobby bare — no posters, no papers, no signage, no lettering of any kind anywhere.')
assert old in t; t = t.replace(old, new)
old = 'no invented text, no letter-shaped noise, no ticket numbers, no counter signage,'
new = ('no invented text, no letter-shaped noise, no ticket numbers, no counter signage, no concession stand, '
       'no popcorn machine, no cash register, no display case, no posters, no papers with writing, no "SOLD OUT", '
       'no "POPCORN", no text on the ticket, no crumpling the ticket,')
assert old in t; t = t.replace(old, new)
save('b1288', t, 'STAGING+VOICE correction')

print('all v2 vehicles built')
