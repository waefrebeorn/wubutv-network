import re

def extract(sheet, prov, title_tokens, lore_token):
    with open(sheet) as f:
        lines = f.readlines()
    hdr = [i for i,l in enumerate(lines) if l.startswith('## === %s ' % prov)]
    assert len(hdr) == 1, (sheet, prov, len(hdr))
    h = hdr[0]
    body_lines = []
    j = h + 1
    while j < len(lines) and not lines[j].startswith('## ==='):
        body_lines.append(lines[j])
        j += 1
    body = ''.join(body_lines).strip()
    hdr_title = lines[h].strip()
    assert hdr_title.startswith('## === %s ' % prov), hdr_title
    for tok in title_tokens:
        assert tok.lower() in body.lower(), ('body missing token', prov, tok)
    assert lore_token.lower() in body.lower(), ('body missing lore', prov, lore_token)
    return body

specs = [
    ("PREPRO_2026-10-16_0115.md", "B-1333", "B-1035", "THE HOURGLASS",
     ["hourglass", "turns the hourglass"], "THE TURNED HOUR"),
    ("PREPRO_2026-10-16_0115.md", "B-1334", "B-1036", "THE KNEADED DOUGH",
     ["dough", "kneads the dough"], "THE WORKED DOUGH"),
    ("PREPRO_2026-10-16_0115.md", "B-1335", "B-1037", "THE STROPPED RAZOR",
     ["strop", "straight razor"], "THE KEPT EDGE"),
]

for sheet, prov, claim, title, toks, lore in specs:
    body = extract(sheet, prov, toks, lore)
    header = "FIRE %s — %s (claimed from %s %s) — run 2026-10-16 02:00 EDT\nFIRE-READY draft, baked lock stack; fired verbatim. Pre-fire verification: body contains %s, LORE %s.\n\n" % (
        claim, title, sheet, prov, '/'.join(toks), lore)
    out = 'fire_%s_20261016_0200.txt' % claim.lower().replace('-', '')
    with open(out, 'w') as f:
        f.write(header + body + "\n")
    with open(out) as f:
        txt = f.read()
    assert claim in txt and prov in txt, ('round-trip fail', out)
    print(out, len(txt), 'bytes OK')
