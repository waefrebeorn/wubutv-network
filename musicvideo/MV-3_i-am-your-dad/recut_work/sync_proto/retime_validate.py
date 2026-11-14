#!/usr/bin/env python3
"""Re-score the RETIMED MV-3 master with the cross-check method.

Recovery run 2026-11-05 ~02:48 EST. The re-cut baseline lives in
placement_crosscheck.json / master_motion_spotcheck.json /
master_dictation_report.json (VALIDATION_RECUT_16x9.md) -- those files
are NEVER overwritten. This driver writes the *_retimed.json siblings.

What it does, in method order (CROSSCHECK_SYNC_METHOD.md):
1. Placement cross-check for all 31 mouth scenes, using the RETIMED
   scene table (retime_build.retimed_scenes(): only S16/S18/S34 warps
   differ from the re-cut). Take dictations are re-used from
   recut_work/measure/*.json -- the warp change is placement math, not
   new dictation, so no re-transcription is needed here.
2. Picture-motion spot check on the RETIMED master file itself
   (first song-word time per scene, frame vs 0.5s earlier).
3. Master-audio dictation on the RETIMED master (full performed
   lyrics as initial_prompt), aligned to SONG_WORDS.json. The audio
   is the same untouched track.mp3, so this is expected to reproduce
   the re-cut's stability numbers -- it guards against a mux error
   (e.g. audio offset), not against a picture change.

Law One: the song never moves. Only the three take-side warps change.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys

PROJ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ)
sys.path.insert(0, HERE)
import crosscheck_sync as cc  # noqa: E402
import retime_build as rb  # noqa: E402

RETIMED = os.path.join(PROJ, "masters", "mv3_i_am_your_dad_16x9_retimed.mp4")
CACHE = os.path.join(HERE, "master_dictation_prompted.json")


def md5_of(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    # --- sanity: retimed final exists and decodes ---
    nf = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
                         "-select_streams", "v:0",
                         "-show_entries", "stream=nb_read_frames",
                         "-of", "csv=p=0", RETIMED],
                        capture_output=True, text=True, check=True).stdout.strip()
    print(f"retimed final: {nf} frames (target 8516)", flush=True)
    assert int(nf) == 8516, (RETIMED, nf)
    md5 = md5_of(RETIMED)
    print(f"retimed final md5: {md5}  size: {os.path.getsize(RETIMED)}", flush=True)

    # --- 1. placement with the retimed scene table ---
    cc.SCENES = rb.retimed_scenes()
    res = cc.do_placement()
    out1 = os.path.join(HERE, "placement_crosscheck_retimed.json")
    json.dump(res, open(out1, "w"), indent=1)
    print(f"wrote {out1}", flush=True)

    # --- 2. motion spot check on the retimed master ---
    cc.MASTER_16X9 = RETIMED
    rows = cc.picture_motion_spotcheck()
    out2 = os.path.join(HERE, "master_motion_spotcheck_retimed.json")
    json.dump(rows, open(out2, "w"), indent=1)
    print(f"wrote {out2}", flush=True)

    # --- 3. master-audio dictation on the retimed master ---
    # do_master() writes its cache to master_dictation_prompted.json;
    # park the re-cut cache aside and restore it afterwards.
    backup = CACHE + ".recut_backup"
    shutil.copy2(CACHE, backup)
    try:
        cc.MASTER_16X9 = RETIMED
        cc.MASTER_MD5 = md5
        rep = cc.do_master(transcribe=True)
    finally:
        shutil.copy2(backup, CACHE)
        os.remove(backup)
    out3 = os.path.join(HERE, "master_dictation_report_retimed.json")
    json.dump(rep, open(out3, "w"), indent=1)
    print(f"wrote {out3}", flush=True)


if __name__ == "__main__":
    os.makedirs(cc.TMP, exist_ok=True)
    main()
