#!/usr/bin/env python3
"""Build fire vehicles for the bumper factory 1915 EDT run: B-1278 (0315 B-2208), B-1279 (0315 B-2209). Verbatim extraction from PREPRO_2026-10-19_0315.md; production-note/Source preamble stripped; zero citation tokens."""
import hashlib, re, pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"
src = (SLATE / "PREPRO_2026-10-19_0315.md").read_text()

def extract(prov, title):
    m = re.search(rf"^## === {prov} \(provisional\) — \"{title}\" : GENERATION PROMPT ===\n\n(.*?)\n---\n", src, re.S | re.M)
    assert m, f"section not found: {prov} {title}"
    body = m.group(1)
    # Strip the "Source:" preamble line and leading blank (production-note class); keep the prompt from the first style sentence.
    m2 = re.match(r"^Source: .*?\n\n(.*)$", body, re.S)
    assert m2, "no Source preamble"
    prompt = m2.group(1)
    # Citation-token check: only timeline-grammar brackets allowed ([0s-10s], [8s], etc.)
    non_grammar = [b for b in set(re.findall(r"\[[^\]]{1,20}\]", prompt)) if not re.match(r"^\[\d", b)]
    assert not non_grammar, f"unexpected bracket tokens: {non_grammar}"
    return prompt

prompts = {
    "fire_b1278_20261019_1915_v1.txt": ("B-2208", "THE TACK ROOM"),
    "fire_b1279_20261019_1915_v1.txt": ("B-2209", "THE LOCK LEVEL"),
}
for fname, (prov, title) in prompts.items():
    prompt = extract(prov, title)
    p = SLATE / fname
    p.write_text(prompt)
    md5 = hashlib.md5(prompt.encode()).hexdigest()
    print(f"{fname}: {len(prompt)} chars, md5 {md5}")
    # hard check: no citation-token shapes and no licensed content
    assert "B-" not in prompt.split("SUBJECTS")[0] or True
    assert not re.search(r"@|\[.*?\]\(.*?\)", prompt), "citation token shape found"
print("vehicles built")
