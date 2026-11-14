#!/bin/bash
# STATION piece 573 master assembly (serial factory, 2026-11-07 1345 EST).
# P1v1 + P2v1 + P3v1 + P4v2.
# Convention (566 lesson): P1 240 frames, P2/P3/P4 239 frames each (shared-boundary
# drop off the TAILS of P2/P3/P4), total 957 frames / 39.875s. Frame-based trims
# ALWAYS use start_frame=/end_frame= (564 lesson — trim=0:240 means SECONDS).
# Audio trims match: P1 10.0s, P2-P4 9.958333s. x264 CRF 18 preset medium.
# No attenuation: hottest native TP -5.4 dBTP (P3v1), under the -1 ceiling.
set -e
D=takes/2026-11-07
ffmpeg -v error -y \
 -i $D/station_p1_lamptheprojectionboothburnsfornobody_whodoesthelampburnfor_v1_16x9.mp4 \
 -i $D/station_p2_lamptheprojectionboothburnsfornobody_thelampkeepsitshours_v1_16x9.mp4 \
 -i $D/station_p3_lamptheprojectionboothburnsfornobody_thenthreadit_v1_16x9.mp4 \
 -i $D/station_p4_lamptheprojectionboothburnsfornobody_theboothburnswithoutyou_v2_16x9.mp4 \
 -filter_complex "[0:v]trim=start_frame=0:end_frame=240,setpts=PTS-STARTPTS[v0];[1:v]trim=start_frame=0:end_frame=239,setpts=PTS-STARTPTS[v1];[2:v]trim=start_frame=0:end_frame=239,setpts=PTS-STARTPTS[v2];[3:v]trim=start_frame=0:end_frame=239,setpts=PTS-STARTPTS[v3];[v0][v1][v2][v3]concat=n=4:v=1:a=0[outv];[0:a]atrim=0:10.0,asetpts=PTS-STARTPTS[a0];[1:a]atrim=0:9.958333,asetpts=PTS-STARTPTS[a1];[2:a]atrim=0:9.958333,asetpts=PTS-STARTPTS[a2];[3:a]atrim=0:9.958333,asetpts=PTS-STARTPTS[a3];[a0][a1][a2][a3]concat=n=4:v=0:a=1[outa]" \
 -map "[outv]" -map "[outa]" -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k \
 $D/station_piece573_lamptheprojectionboothburnsfornobody_master_40s_16x9.mp4
