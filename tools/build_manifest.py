import json, os, re, hashlib
ROOT = os.path.expanduser("~/workspace/wubutv-network")
DS = "WaefreBeorn/wubutv-network-media"
BASE = f"https://huggingface.co/datasets/{DS}/resolve/main"

# Era II (CEO R1, 2026-10-21): every finished master carries MUSIC_TAG
# (bed id + sting id). Existing Era I masters backfill as "legacy-none";
# new masters must have a row in music/tags.json at ship time.
MUSIC_TAGS = {}
try:
    MUSIC_TAGS = json.load(open(f"{ROOT}/music/tags.json"))
except FileNotFoundError:
    pass

def music_tag(uid):
    row = MUSIC_TAGS.get(uid)
    if isinstance(row, dict) and row.get("bed") and row.get("sting"):
        return f"{row['bed']}+{row['sting']}"
    return "legacy-none"

def md5(p, limit=64*1024*1024):
    h = hashlib.md5()
    with open(p, "rb") as f:
        while True:
            b = f.read(4*1024*1024)
            if not b: break
            h.update(b)
    return h.hexdigest()

# Era II (CEO A3 / PROVENANCE_SPEC v1, 2026-10-21): every master carries a
# provenance block. Reference behaviour mirrors tools/provenance_stamp.py —
# never invent a generator id: unknown + needs_backfill=true. prompt_ref is
# the sha256 of whatever prompt text the record carries (episode premises),
# never a guess.
PROV_BASIS = "eu_ai_act_art50+ca_sb942"
PROV_POLICY = {
    "version": 1,
    "effective": "2026-10-21",
    "disclosure_statement": ("Every piece in this dataset is AI-generated video "
        "with native generated audio. No piece is a re-voiced or dubbed performance."),
}

def provenance_for(piece):
    txt = piece.get("prompt") or piece.get("premise") or ""
    pref = (hashlib.sha256(txt.encode("utf-8")).hexdigest()
            if isinstance(txt, str) and txt.strip() else None)
    return {
        "ai_generated": True,
        "generator": {"vendor": "unknown", "model": "unknown", "version": "unknown"},
        "prompt_ref": pref,
        "generated_at": None,
        "disclosure": {"visible": True, "latent": False},
        "basis": PROV_BASIS,
        "needs_backfill": True,
    }

manifest = {"dataset": DS, "generated": "2026-10-18", "bumpers": [], "commercials": [], "episodes": [], "extras": []}

# bumpers (slate format: | B-<n> "<title>" | <path> | <slug> | <note-or-tagline> | ...)
for line in open(f"{ROOT}/slate/BUMPERS.md"):
    s = line.strip()
    if not s.startswith("| B-"): continue
    parts = [x.strip() for x in s.split("|")]
    if len(parts) < 5: continue
    m = re.match(r'B-(\d+)\s+"([^"]+)"', parts[1])
    if not m: continue
    n, title = m.groups()
    fpath = parts[2]
    note = parts[4]
    if note.startswith('"') and note.endswith('"'): note = note[1:-1]
    full = os.path.join(ROOT, fpath)
    if fpath.endswith(".mp4") and os.path.exists(full):
        manifest["bumpers"].append({
            "number": int(n), "title": title, "tagline": note,
            "file": fpath, "bytes": os.path.getsize(full),
            "music_tag": music_tag(f"B-{n}"),
            "cdn_url": f"{BASE}/{fpath}"})

# commercials (slate format: | AD-<n> | "<title>" (<sponsor>) | <path> | ...)
for line in open(f"{ROOT}/slate/COMMERCIALS.md"):
    s = line.strip()
    if not s.startswith("| AD-"): continue
    parts = [x.strip() for x in s.split("|")]
    if len(parts) < 4: continue
    m = re.match(r'AD-(\d+)', parts[1])
    if not m: continue
    n = m.group(1)
    tm = re.match(r'"([^"]+)"(?:\s*\(([^)]+)\))?', parts[2])
    title = tm.group(1) if tm else parts[2]
    sponsor = tm.group(2) if (tm and tm.group(2)) else ""
    fpath = next((x for x in parts[2:] if x.endswith(".mp4")), "")
    full = os.path.join(ROOT, fpath)
    if fpath and os.path.exists(full):
        manifest["commercials"].append({
            "number": int(n), "title": title, "sponsor": sponsor,
            "file": fpath, "bytes": os.path.getsize(full),
            "music_tag": music_tag(f"AD-{n}"),
            "cdn_url": f"{BASE}/{fpath}"})

# episodes
for line in open(f"{ROOT}/EPISODE_LEDGER.md"):
    m = re.match(r'^\| (\d+) \| (\S+) \| (\S+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| (\S+) \|', line.strip())
    if m:
        seq, eid, channel, title, premise, seed, fpath = [x.strip() for x in m.groups()]
        if fpath.endswith(".mp4"):
            full = os.path.join(ROOT, fpath)
            if os.path.exists(full):
                manifest["episodes"].append({
                    "seq": int(seq), "id": eid, "channel": channel, "title": title,
                    "premise": premise, "file": fpath, "bytes": os.path.getsize(full),
                    "music_tag": music_tag(eid),
                    "cdn_url": f"{BASE}/{fpath}"})

# extras: media files not claimed by any ledger (outlet block, strays)
claimed = {e["file"] for k in ("bumpers","commercials","episodes") for e in manifest[k]}
for dirpath, _, files in os.walk(ROOT):
    if "/takes/" in dirpath or "/.git/" in dirpath: continue
    for fn in sorted(files):
        if not fn.endswith(".mp4"): continue
        rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
        if rel not in claimed:
            full = os.path.join(ROOT, rel)
            manifest["extras"].append({"file": rel, "bytes": os.path.getsize(full),
                                       "cdn_url": f"{BASE}/{rel}"})

# raw_takes: raw generation takes stored inside channel dirs (not finished clips)
manifest["raw_takes"] = []
claimed2 = claimed | {e["file"] for e in manifest["extras"]}
for dirpath, _, files in os.walk(ROOT):
    if "/.git/" in dirpath: continue
    for fn in sorted(files):
        if not fn.endswith(".mp4"): continue
        rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
        if rel in claimed2: continue
        full = os.path.join(ROOT, rel)
        manifest["raw_takes"].append({"file": rel, "bytes": os.path.getsize(full),
                                      "note": "raw generation take, not a finished clip",
                                      "cdn_url": f"{BASE}/{rel}"})

# audio stings: network-owned generated stings (CEO R3/R1, 2026-10-21) —
# registered by id in music/STINGS.md, dropped into the manifest here.
manifest["audio"] = []
for dirpath, _, files in os.walk(f"{ROOT}/music/stings"):
    for fn in sorted(files):
        if not fn.endswith(".wav"): continue
        rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
        full = os.path.join(ROOT, rel)
        sid = fn[:-4]
        h = hashlib.sha256()
        with open(full, "rb") as f:
            for b in iter(lambda: f.read(4*1024*1024), b""): h.update(b)
        manifest["audio"].append({"id": sid, "file": rel,
                                  "bytes": os.path.getsize(full),
                                  "sha256": h.hexdigest(),
                                  "cdn_url": f"{BASE}/{rel}"})

manifest["counts"] = {k: len(v) for k, v in manifest.items() if isinstance(v, list)}

# A3 native: stamp every media section with the provenance block, then the
# manifest-level policy with the real backfill census.
MEDIA_SECTIONS = ("bumpers", "commercials", "episodes", "extras", "raw_takes", "audio")
for _sec in MEDIA_SECTIONS:
    for _e in manifest[_sec]:
        _e["provenance"] = provenance_for(_e)
_bf_stamped = sum(len(manifest[s]) for s in MEDIA_SECTIONS)
_bf_need = sum(1 for s in MEDIA_SECTIONS for e in manifest[s]
               if e["provenance"]["needs_backfill"])
_bf_pref = sum(1 for s in MEDIA_SECTIONS for e in manifest[s]
               if e["provenance"]["prompt_ref"])
manifest["provenance_policy"] = dict(PROV_POLICY, backfill_state={
    "stamped": _bf_stamped, "needs_backfill": _bf_need,
    "prompt_ref_attached": _bf_pref})

# R1 gate: every finished master must carry a non-empty music_tag.
missing = [(k, e.get("number") or e.get("id") or e.get("seq"))
           for k in ("bumpers", "commercials", "episodes")
           for e in manifest[k] if not e.get("music_tag")]
assert not missing, f"MUSIC_TAG gate failed: {missing}"

# docs: key text documents (ledgers, slates, ideas, policy) — mirrored on GitHub
DOC_INDEX = [
    ("slate/BUMPERS.md", "Bumper ledger: number, title, file, tagline for every shipped bumper"),
    ("slate/COMMERCIALS.md", "Commercial ledger: AD number, title, sponsor, file"),
    ("EPISODE_LEDGER.md", "Episode ledger: seq, id, channel, title, premise, file"),
    ("ideas/IDEAS_BANK.md", "Idea bank: researched bumper/episode premises with hop chains"),
    ("LEARNING_LOG.md", "Recursive learning log: one line per production lesson"),
    ("tiktok/TIKTOK_POLICY.md", "TikTok channel policy: cadence, captions, settings"),
    ("tiktok/TIKTOK_POSTS.md", "TikTok post ledger with URLs"),
    ("tiktok/CAPTION_QUEUE.md", "Prepared caption queue"),
    ("notes/COMMERCIALS.md", "Commercial format notes and fictional sponsor list"),
    ("notes/CANON.md", "Canon notes"),
]
manifest["docs"] = []
for rel, desc in DOC_INDEX:
    full = os.path.join(ROOT, rel)
    if os.path.exists(full):
        manifest["docs"].append({"file": rel, "description": desc,
                                 "bytes": os.path.getsize(full),
                                 "github_url": f"https://github.com/waefrebeorn/wubutv-network/blob/main/{rel}"})
manifest["license"] = "WaefreBeorn Umbrella License v3.0 (see LICENSE in the GitHub repo)"
manifest["counts"]["docs"] = len(manifest["docs"])
manifest["total_bytes"] = sum(e.get("bytes",0) for k in ("bumpers","commercials","episodes","extras","raw_takes") for e in manifest[k])
out = os.path.expanduser("~/workspace/cdn-staging/hf-dataset/manifest.json")
json.dump(manifest, open(out, "w"), indent=1)
print(json.dumps(manifest["counts"], indent=1))
print("total GB: %.2f" % (manifest["total_bytes"]/1e9))
