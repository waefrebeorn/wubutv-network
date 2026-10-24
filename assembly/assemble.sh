#!/usr/bin/env bash
# WuBuTV episode assembly — concat 10s units into 1-min (6) or 2-min (12) episodes.
# Usage:
#   assemble.sh --units <file1> <file2> ... --out <path> --title "<title>"
# Requires: ffmpeg/ffprobe. No re-encode when all inputs are h264+aac 1280x720 (~10s).
set -euo pipefail

UNITS=()
OUT=""
TITLE=""
LIST_MODE=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --units) shift; while [[ $# -gt 0 && "$1" != --* ]]; do UNITS+=("$1"); shift; done ;;
    --out)   OUT="$2"; shift 2 ;;
    --title) TITLE="$2"; shift 2 ;;
    *) echo "ERROR: unknown arg: $1" >&2; exit 1 ;;
  esac
done

if [[ ${#UNITS[@]} -eq 0 ]]; then echo "ERROR: no --units given" >&2; exit 1; fi
if [[ -z "$OUT" ]]; then echo "ERROR: no --out given" >&2; exit 1; fi
if [[ ${#UNITS[@]} -ne 6 && ${#UNITS[@]} -ne 12 ]]; then
  echo "ERROR: episode assembly takes exactly 6 (1-min) or 12 (2-min) units, got ${#UNITS[@]}" >&2
  exit 1
fi

# --- verify every input ---
EXPECT_V="h264"; EXPECT_A="aac"; EXPECT_W=1280; EXPECT_H=720
for u in "${UNITS[@]}"; do
  if [[ ! -f "$u" ]]; then echo "ERROR: input missing: $u" >&2; exit 1; fi
  vc=$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height -of default=noprint_wrappers=1 "$u")
  ac=$(ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1 "$u")
  dur=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 "$u" | cut -d= -f2)
  vcodec=$(echo "$vc" | grep codec_name | cut -d= -f2)
  w=$(echo "$vc" | grep 'width=' | cut -d= -f2)
  h=$(echo "$vc" | grep 'height=' | cut -d= -f2)
  acodec=$(echo "$ac" | grep codec_name | cut -d= -f2)
  dur_int=${dur%.*}
  if [[ "$vcodec" != "$EXPECT_V" || "$acodec" != "$EXPECT_A" ]]; then
    echo "ERROR: codec mismatch in $u (video=$vcodec audio=$acodec, expected $EXPECT_V+$EXPECT_A)" >&2; exit 1
  fi
  if [[ "$w" != "$EXPECT_W" || "$h" != "$EXPECT_H" ]]; then
    echo "ERROR: resolution mismatch in $u (${w}x${h}, expected ${EXPECT_W}x${EXPECT_H})" >&2; exit 1
  fi
  if [[ "$dur_int" -lt 9 || "$dur_int" -gt 11 ]]; then
    echo "ERROR: duration out of range in $u (${dur}s, expected ~10s)" >&2; exit 1
  fi
  echo "OK: $u (${vcodec}+${acodec}, ${w}x${h}, ${dur}s)"
done

# --- concat ---
LISTFILE=$(mktemp /tmp/assemble_list.XXXXXX.txt)
trap 'rm -f "$LISTFILE"' EXIT
for u in "${UNITS[@]}"; do
  # escape single quotes for the concat demuxer
  printf "file '%s'\n" "$(realpath "$u" | sed "s/'/'\\\\''/g")" >> "$LISTFILE"
done

mkdir -p "$(dirname "$OUT")"
ffmpeg -hide_banner -loglevel warning -y -f concat -safe 0 -i "$LISTFILE" \
  -c copy -map 0 \
  -metadata title="$TITLE" \
  -metadata comment="WuBuTV assembled episode" \
  "$OUT"

# --- report specs ---
fdur=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 "$OUT" | cut -d= -f2)
fres=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of default=noprint_wrappers=1 "$OUT" | tr '\n' ' ')
fsize=$(stat -c%s "$OUT")
fmd5=$(md5sum "$OUT" | cut -d' ' -f1)
echo "---"
echo "OUTPUT: $OUT"
echo "DURATION: ${fdur}s | RES: $fres | SIZE: ${fsize} bytes | MD5: ${fmd5}"
echo "TITLE: $TITLE"
echo "UNITS: ${#UNITS[@]}"
