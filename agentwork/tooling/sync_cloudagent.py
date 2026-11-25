#!/usr/bin/env python3
"""Sync every finished media file to the cloudagent CDN, with a manifest that proves it.

Scope: /opt/data/work and /opt/data/shitpost-box/cartoons (the shipping areas), media only,
and only files that are not intermediates (frame dumps, *_raw, p_*, pic.mp4, audio beds).

Each upload is keyed by sha256 in MANIFEST.json, so a re-run uploads only what changed.
Remote layout mirrors the local path: <project>/<file>.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

from huggingface_hub import HfApi

REPO = "WaefreBeorn/cloudagent"
ROOTS = ["/opt/data/work", "/opt/data/shitpost-box/cartoons", "/opt/data/shitpost-box/brainrot"]
MANIFEST = "/opt/data/work/cloudagent_manifest.json"
EXTS = {".mp4", ".mov", ".wav", ".mp3", ".m4a", ".png", ".jpg", ".gif", ".webp"}
SKIP_PARTS = ("/frames/", "/frames_rast", "/graded/", "/denoised/", "/handoff/", "/qc/", "/segs/", "/promo_frames/",
              "/c_intro/", "/c_lockup/", "/c_end/", "/c_final/", "/k_intro/", "/k_end/",
              "/endcard/", "/card0/", "/card1/", "/card2/", "/card3/", "/card4/", "/card5/",
              "/card6/", "/thumbs/", "/.thumbnails/")
SKIP_NAMES = {"promo_raw.mp4", "pic.mp4", "one_piece_raw.mp4", "fifth_pic.mp4", "fifth_raw.mp4",
              "clean.mp4", "picture.mp4", "video_only.mp4", "THE_LAMP_v2.mp4", "p_intro.mp4",
              "p_end.mp4", "p_final.mp4", "f_intro.mp4", "f_end.mp4", "f_push.mp4",
              "ident_send.mp4", "wubutv_presents_send.mp4", "THE_ONE_PIECE_send.mp4",
              "b125_consolation.mp4", "b124_final_question.mp4", "b126_grand_prize.mp4",
              "algo_max_30s.mp4", "fifth_mark_30s.mp4", "audio.wav", "score.wav", "drone.wav",
              "fifth.wav", "promo.wav", "mix.wav", "mix_norm.wav", "chime.wav", "wind.wav"}
MIN_BYTES = 150_000


def sha256(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def probe(path):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "format=duration,size:stream=width,height,codec_name",
                              "-of", "json", path], capture_output=True, text=True, timeout=30).stdout
        d = json.loads(out or "{}")
        fmt = d.get("format") or {}
        st = (d.get("streams") or [{}])[0]
        return {"duration": float(fmt.get("duration") or 0),
                "w": st.get("width"), "h": st.get("height"), "codec": st.get("codec_name")}
    except Exception:
        return {}


def collect():
    found = []
    for root in ROOTS:
        if not os.path.isdir(root):
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            if any(p in dirpath + "/" for p in SKIP_PARTS):
                continue
            for fn in filenames:
                p = os.path.join(dirpath, fn)
                ext = os.path.splitext(fn)[1].lower()
                if ext not in EXTS or fn in SKIP_NAMES:
                    continue
                if re.fullmatch(r"f_\d{3,5}\.(png|jpg)", fn):
                    continue  # frame dump, not an asset
                try:
                    size = os.path.getsize(p)
                except OSError:
                    continue
                if size < MIN_BYTES:
                    continue
                found.append((p, size))
    return found


def main():
    dry = "--dry" in sys.argv
    api = HfApi(token=os.environ["HF_TOKEN_WRITE"])
    man = {}
    if os.path.exists(MANIFEST):
        man = json.load(open(MANIFEST))
    files = collect()
    total = sum(s for _, s in files)
    print(f"{len(files)} media files, {total/1e9:.2f} GB")
    up = 0
    for path, size in sorted(files):
        rel = os.path.relpath(path, "/opt/data")
        digest = sha256(path)
        prev = man.get(rel)
        if prev and prev.get("sha256") == digest:
            print("  skip (unchanged)", rel)
            continue
        if dry:
            print("  would upload", rel, size)
            continue
        api.upload_file(path_or_fileobj=path, path_in_repo=rel, repo_id=REPO, repo_type="dataset")
        man[rel] = {"sha256": digest, "bytes": size, **probe(path), "at": datetime.now(timezone.utc).isoformat()}
        up += 1
        print("  up", rel, f"{size/1e6:.1f} MB")
    if not dry:
        man_doc = {"dataset": REPO, "generated": datetime.now(timezone.utc).isoformat(),
                   "file_count": len(man), "total_bytes": sum(v.get("bytes", 0) for v in man.values()),
                   "files": man}
        api.upload_file(path_or_fileobj=json.dumps(man_doc, indent=1).encode(),
                        path_in_repo="MANIFEST.json", repo_id=REPO, repo_type="dataset")
        json.dump(man, open(MANIFEST, "w"), indent=1)
        remote = [f for f in api.list_repo_files(repo_id=REPO, repo_type="dataset") if f != "MANIFEST.json"]
        print(f"uploaded {up} new; remote files {len(remote)}; manifest {len(man)}")


if __name__ == "__main__":
    main()
