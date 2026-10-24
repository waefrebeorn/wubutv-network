import re, pathlib, hashlib

repo = pathlib.Path.home() / "workspace/wubutv-network/slate"
src = (repo / "PREPRO_2026-10-19_0315.md").read_text()
run = "20261019_0430"

specs = {
    "B-2203": ("b1274", "pattern-shop", "THE PATTERN SHOP", "The pattern holds."),
    "B-2204": ("b1275", "unburned-lump", "THE UNBURNED LUMP", "The cellar keeps one."),
    "B-2205": ("b1276", "attic-window", "THE ATTIC WINDOW", "The attic has mail."),
}

for prov, (num, slug, title, line) in specs.items():
    m = re.search(rf"## === {prov} \(provisional\) — .+?===\n\n(.*?)(?=\n---\n|\Z)", src, re.S)
    assert m, f"section {prov} not found"
    body = m.group(1).strip()
    # Strip the Source: paragraph (first paragraph)
    parts = body.split("\n\n", 1)
    assert parts[0].startswith("Source:"), f"{prov}: first paragraph is not Source:"
    vehicle = parts[1].strip()
    assert vehicle.endswith("."), f"{prov}: vehicle does not end with NEGATIVE block"
    # Zero citation tokens + no stray PROD tokens
    assert not re.search(r"\[[0-9]+\]|https?://", vehicle), f"{prov}: citation token in vehicle"
    # Load-bearing payload check
    for tok in (line, "~WuBu~", "WuBuTV", "heavyset Black man"):
        assert tok in vehicle, f"{prov}: missing token {tok!r}"
    assert "PLACEHOLDER" not in vehicle
    path = repo / f"fire_{num}_{run}_v1.txt"
    path.write_text(vehicle)
    print(f"{path.name} md5={hashlib.md5(vehicle.encode()).hexdigest()} len={len(vehicle)} line_ok={'\"'+line+'\"' in vehicle}")
print("BUILD OK")
