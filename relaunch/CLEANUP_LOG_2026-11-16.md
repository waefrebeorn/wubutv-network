# Cleanup Log — 2026-11-16 (Telegram msg 524 authorization)

User order: "now that you have all the new masters, you can clean house on your
used up space because we back everything up to the CDN."

## Disk, before → after

| | Used | Free | Use% |
|---|---|---|---|
| Before (2026-11-17T01:35Z) | 124 G | 26 G | 83% |
| After (2026-11-17T02:06Z) | 99 G | 50 G | 67% |

**≈25 GB freed.** Filesystem: /dev/mapper/rv (150 G) on /home/hatch.

## Deleted — per class, with verification basis

| Class | Count | Measured size | Basis |
|---|---|---|---|
| `cdn-staging/.snap-worktree/` (stranded delta-sync snapshot) | 1 tree | ~11 GB | Regenerable sync scratch; removed + `git worktree prune`. No sync was running. |
| Verified media: mp4/wav under `musicvideo/`, `takes/`, `recycle/` (outside any `masters/` dir) | 2,579 files | 14.70 GB | **Hash-verified on the CDN**: local SHA-256 == HF dataset `lfs.sha256` at the identical repo path (WaefreBeorn/wubutv-network-media, tree of 13,593 files pulled live this run); non-LFS entries matched on git blob SHA-1 + size. Zero hash mismatches found anywhere. Full per-file verdicts: `~/workspace/cdn-staging/hidden_files/cleanup_media_verdicts_2026-11-16.json`. |
| Python venvs: `detection-research/finder-tests/venv`, `detection-research/venv`, `detection-research/venv_cv2`, `~/workspace/fw-venv`, `~/workspace/cv2-throwaway` | 5 venvs | ~3.2 GB | Regenerable (`pip install`); fw-venv had no script references (only mentions in memory-staging copies). |
| Scratch dirs: `lego-harvest-scratch` (re-clonable GitHub repo harvests), `slopcore-scratch-20261112` (repo clone), `tmp_hpss`, `tmpbuild` | 4 dirs | ~0.47 GB | Scratch by name and content. |
| `.thumbnails/` dirs under `takes/` + `musicvideo/` | 4,916 files / 58 dirs | 0.68 GB | Regenerable derivatives of media files. |
| `tools/blender-4.5.15-linux-x64.tar.xz` | 1 file | 361 MB | Installer tarball; Blender already extracted in `tools/blender/` (kept). Re-downloadable. |
| `~/.cache/hatch-thumbnails`, `~/.cache/bun` | 2 dirs | ~52 MB | Regenerable caches. |

Kept inside finder-tests: all `.md` reports (incl. FINDER_TEST_RESULTS), result
JSONs, `.npy` embeddings, and the SSCD/vPDQ model weights (193 MB) — the adopted
F-28/F-31 tooling. `v3_spliced_dup.mp4` was itself in the hash-verified deleted
set (matches HF, uploaded by the 17:05 EST sync run).

## HELD — not deleted, with reasons

| Item | Size | Reason |
|---|---|---|
| **Stills** (png/jpg/webp) under `takes/` + `musicvideo/` | 52,822 files / 22.45 GB | **The only copy on disk** — the delta sync only ever pushed mp4/wav/json/txt, so stills were never on the CDN. NOT deleted. A mirror to the HF dataset is RUNNING (systemd unit `wubu-cdn-mirror`, driver `cdn-staging/hidden_files/mirror_all.py`, log `cdn-staging/hidden_files/stills_mirror_20261116.log`, started 2026-11-17T02:05Z). Local deletion is deferred until a follow-up pass re-lists the dataset tree and matches each still's SHA-256 — only then may they be deleted. |
| **Held media** (mp4/wav absent from HF) | 1,484 files / 3.69 GB | Not CDN-backed (never synced or past upload failures; zero were hash mismatches — they are simply absent). Same `wubu-cdn-mirror` unit queues them after the stills. Deletion deferred to the same verified follow-up pass. Plus 11 alias symlinks in `takes/` (0 bytes, harmless). |
| `~/.cache/huggingface/hub` | 9.1 GB | Model store: faster-whisper large-v3 + turbo, HTDemucs, distil/tiny/small/medium/base. Re-downloadable in principle, but HF transfers failed repeatedly tonight (20:05 EST sync run) and transcription/separation are core pipeline — held deliberately rather than risk a blocked intake. |
| `tools/lyrics-venv` | 2.1 GB | Referenced by `separate_stems.sh` in MV-2..MV-5 `work/lyrics-redo/`; pipeline tooling, not scratch. |
| `bumpers/` 2.5 G, `assembly/` 2.4 G, `station/` 1.6 G, `new-era/` 3.1 G, every `masters/` dir | ~19 G | Shipped canon / active assembly pool / protected classes (masters, ledgers, flags never cleanup targets). Untouched. |
| `~/workspace/agents` 953 M, `user/` 251 M, `imagine_media/` 251 M, `visual_grounding/` 225 M, `wubuwizard-cpu-sep/` 156 M, `scratch_snapper/` 29 M | ~1.9 GB | Unclassified or mixed content (session data, user media, an MDX model + MV-14 stems, a sprint draft document). Not verified scratch — held. |

## Follow-up owed (one pass, when the mirror completes)

1. Re-list the HF dataset tree; SHA-256-verify every local still + held media
   file against it; delete only matches (expected recovery ≈ 26 GB more).
2. Re-check `systemctl is-active wubu-cdn-mirror` and the mirror log tail for
   "MIRROR PASS COMPLETE" (all 5 upload_folder jobs DONE, none FAILED).
