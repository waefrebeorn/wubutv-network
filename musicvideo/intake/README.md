# Suno MP3 intake — Era II music intake

**Owner decree (2026-10-21):** the owner will make music in Suno and send MP3s
to the Producer (Muse) and the CEO bot (WuBuCEO). This directory is where they
land.

## How to send

- Send the MP3 in chat as an attachment, or drop it in this directory if you
  have file access. Name it `MV-<N>_<title>_suno.mp3`
  (e.g. `MV-2_hallway-count_suno.mp3`).
- With each track, say which job it is for:
  - `anthem` — the network anthem / opening track
  - `serial-bed SERIAL-<n>` — the recurring bed for one serial arc
    (one bed per serial, never per clip — Chain 2)
  - `sting <CHANNEL>` — a 3–6 s channel sting
  - `pips` — THE PIPS entrance motif (three struck notes + held fourth)

## What happens on receipt

1. The track is copied here and checksummed (md5); the receipt is logged in
   `musicvideo/intake/INTAKE_LOG.md` with date, source, and job.
2. Lyrics go to `musicvideo/MV-<N>_<title>/lyrics.txt` (verbatim, owner text is
   canonical — never paraphrased).
3. Duration is measured (ffprobe) and the 48-bar/96 s-style scene grid is
   re-timed to the delivered duration — never send a track back for a timing
   miss.
4. The track is registered in the manifest flow as a MUSIC_TAG source
   (bed id + sting id); every master that rides it names it.
5. The scene grid is staged as 10 s units in order for a serial arc, and
   announced to `#wubu-mv-6a90e1`.

## Standing rules for shipped audio

- Owner-made Suno tracks are the *bed/beds*, never the dialogue. Video footage
  stays native-silent (MV-1 rule); no dub, no TTS over native speech.
- Network-native only: no licensed tracks, no real-brand references.
- Everything here is versioned and CDN-backed like any other master.
