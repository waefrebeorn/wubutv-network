#!/usr/bin/env python3
"""Build fire vehicles for the 2026-10-20 09:00 EDT bumper factory run.
Verbatim PREPRO_2026-10-20_0015.md extracts; Source line stripped;
0815 BUG anti-leak clause appended to NEGATIVE; zero citation tokens.
"""
import re, hashlib, json, sys

SRC = '/home/hatch/workspace/wubutv-network/slate/PREPRO_2026-10-20_0015.md'
OUTDIR = '/home/hatch/workspace/wubutv-network/slate'

JOBS = [
    ('b1275', 'B-2454', 'The Night Lock'),
    ('b1287', 'B-2455', 'The Letter Box'),
    ('b1288', 'B-2456', 'The Coat Ticket'),
]

ANTI_LEAK = ("no meta-text describing the bug's spelling, "
             "no spelling-out of the tilde instruction as words.")

def main():
    src = open(SRC).read()
    report = {}
    for num, prov, title in JOBS:
        pat = (r'## === ' + re.escape(prov) + r' \(provisional\) — "' +
               re.escape(title) + r'" : GENERATION PROMPT ===\n(.*?)\n---')
        m = re.search(pat, src, re.S)
        assert m, f'section not found: {prov} {title}'
        body = m.group(1).strip()
        lines = [l for l in body.split('\n') if not l.startswith('Source:')]
        prompt = '\n'.join(lines).strip()
        assert prompt.startswith('Hand-painted 2D cartoon'), prompt[:60]
        assert prompt.endswith('no stinger.'), prompt[-60:]
        # sanity band: prior v1 vehicles ~3.5-5.5KB
        assert 2500 < len(prompt) < 7000, len(prompt)
        prompt = prompt[:-len('no stinger.')] + 'no stinger, ' + ANTI_LEAK
        # zero citation tokens
        for tok in (prov, '0015', 'Source:', 'FRESH', 'provisional', 'Q1', 'B-245'):
            assert tok not in prompt, f'citation token leak: {tok}'
        # leak check: no swallowed neighbor section
        assert prompt.count('GENERATION PROMPT') == 0, 'neighbor section swallowed'
        path = f'{OUTDIR}/fire_{num}_20261020_0900_v1.txt'
        open(path, 'w').write(prompt)
        md5 = hashlib.md5(prompt.encode()).hexdigest()
        report[num] = {'file': path, 'md5': md5, 'bytes': len(prompt),
                       'provisional': prov, 'title': title}
        print(f'{num} {prov} "{title}": {len(prompt)} bytes, md5 {md5}')
    json.dump(report, open(f'{OUTDIR}/vehicles_20261020_0900.json', 'w'), indent=2)

if __name__ == '__main__':
    main()
