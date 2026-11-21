#!/usr/bin/env python3
"""MV-7 assembly cutlist builder (v4 method: phrase-level smooth warps).

Each segment: take time range -> song time range, one uniform setpts
factor per phrase. Warp factor = song_span / take_span; playback speed
= take_span / song_span. Speed floor 0.5x (factor cap 2.0); speedups
unrestricted (disclosed). Frame counts forced to round(span*24).
"""
import json, hashlib, os, sys

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
TAKES = {
 "s01t2": ("takes/media-generation-mv7v2-s01-v3-intro-chant-i1-so-0-8a128f27-bc6d-41bd-8315-1f246e5adc1f.mp4", "d6ffd61f7659fbe84d2a4ea6de0ba2f9", 1152, 768),
 "s01t1": ("takes/media-generation-mv7-s01-t1-0-5ed0bfcf-e950-4418-9a9e-fb26c6f43008.mp4", "3f29a5e8670a91865af44059e14eb68f", 1152, 768),
 "s02t1": ("takes/media-generation-mv7-s02-t1-0-52866472-cc1e-4357-84d2-4210422550d4.mp4", "56838020652558bbd07c3d3ec6539e92", 1152, 768),
 "s03t1": ("takes/media-generation-mv7-s03-t1-0-a60a7857-1f80-4d05-a1b3-5dddb7c7781c.mp4", "bdbe8d744976861cc3f9c45dfe1c4e43", 1152, 768),
 "s04t1": ("takes/media-generation-mv7-s04-t1-0-6cc10eaf-bba6-4ae1-a7d6-dd76a6176e17.mp4", "23933f5a065ac2ef1e27eea4e297e941", 1152, 768),
 "s05a": ("takes/media-generation-mv7v2-s05-v3a-pre-chorus-1-pc1-0-69783a26-930b-4f00-bac2-d97001a694b3.mp4", "0181fd7e25c2de8af39314ec4cc3dc5e", 1152, 768),
 "s05b": ("takes/media-generation-mv7v2-s05-v4-pre-chorus-1-pc1-0-e4acbb70-b259-4c87-ab3f-54a3a31f8a64.mp4", "ac262c73da22068be632a47f1eabc851", 1152, 768),
 "s06t1": ("takes/media-generation-mv7v2-s06-pre-chorus-1-pc1-3-p-0-caec5eb5-e54a-4bff-b22d-a38f9f6a7e22.mp4", "b27f6c4c4a5dba8749cdbcaf322974c0", 1152, 768),
 "s07t1": ("takes/media-generation-mv7-s07-t1-0-2491c8cc-5254-4c13-9621-14a85c8da176.mp4", "9f9a41cdea6d746387de655175b8729e", 1152, 768),
 "s08t2": ("takes/media-generation-mv7v2-s08-v2-chorus-1-c1-5-c1-0-485705b7-c49a-4e4e-a84e-6026abff5048.mp4", "c04f5f46cfd67c05352289a303711c0c", 1280, 720),
 "s09t2": ("takes/media-generation-mv7v2-s09-v2-chorus-1-c1-8-son-0-9eb3da14-e138-4ab0-9112-78f8178a9838.mp4", "68a47b6e724cda3f2dfb1d61686a131d", 1280, 720),
 "s10t1": ("takes/media-generation-mv7v2-s10-chorus-1-tag-chant-c-0-64689c53-7219-49f8-b5d2-f0839acce3b3.mp4", "642211b3966a3887f4d1ea820a92d62b", 1152, 768),
 "s11t1": ("takes/media-generation-mv7v2-s11-verse-2-v2-1-v2-3-so-0-862f031f-fd6d-4d6c-8837-ea591826b343.mp4", "b90cc69e5c58f73e6cc698586de57871", 1248, 704),
 "s12t2": ("takes/media-generation-mv7v2-s12-v2-verse-2-v2-4-v2-6-0-1a61d504-11f7-48f5-a378-14e910f0385e.mp4", "383a843492b1c954c08b2c6737a65f27", 1248, 704),
 "s13t2": ("takes/media-generation-mv7v2-s13-v2-pre-chorus-2-pc2-0-7a93e8d9-7fa0-4a1d-a53a-987a4f2f0227.mp4", "81933ac4945039cbe0411099bd854103", 1248, 704),
 "s14t1": ("takes/media-generation-mv7v2-s14-pre-chorus-2-pc2-3-p-0-7b5a8b0a-affc-4a1f-97ea-91f9b5a5a630.mp4", "2043def7f8a057f53465d4aba34d1000", 1248, 704),
 "s15t2": ("takes/media-generation-mv7v2-s15-v2-chorus-2-c2-1-c2-0-44875e3c-d6eb-4b26-8713-3466eebad9ff.mp4", "43426ec08cbe01f83c5316d1ea37df09", 1248, 704),
 "s16t1": ("takes/media-generation-mv7v2-s16-chorus-2-c2-5-c2-6-s-0-2c3694f8-072a-4efa-9288-76d7e4a9494c.mp4", "9020aead4540165246264240a459c6b3", 1248, 704),
 "s17t1": ("takes/media-generation-mv7v2-s17-chorus-2-c2-7-c2-8-s-0-70773246-8933-4a21-a3b9-75bd80853392.mp4", "5440c92c4aba9d1fffd69e0f72d41568", 1248, 704),
 "s18t1": ("takes/media-generation-mv7v2-s18-bridge-montage-b1-b4-0-d8514bfa-9877-4564-9b2b-46582a9e311e.mp4", "6bcdda44b63145084136ffcac40fcfb3", 1248, 704),
 "s19t1": ("takes/media-generation-mv7v2-s19-bridge-montage-b5-b6-0-65c522dd-c352-4d26-bf5e-16784d68469f.mp4", "15aade7b9bb5933b1b0190e974ff96f3", 1248, 704),
 "s20t2": ("takes/media-generation-mv7v2-s20-t2-0-918d720a-9968-4d6a-ae48-b30351b503e5.mp4", "f80b133c10191def1508480136a40a8c", 1152, 768),
 "s21t1": ("takes/media-generation-mv7v2-s21-final-chorus-fc5-fc7-0-f901dd60-cd98-43d9-8ccb-be6c026ee373.mp4", "8ffb5f4aa5dea56951e83ddd2e54d543", 1152, 768),
 "s22t1": ("takes/media-generation-mv7v2-s22-final-chorus-fc8-fc9-0-8461ab5e-54b4-45ef-a0ba-e937660d824f.mp4", "6ed121aeb20750219f000797e9848e39", 1152, 768),
 "s23t1": ("takes/media-generation-mv7v2-s23-final-chorus-fc10-0-553c819f-bd9e-4823-ae36-e538adf3d0d7.mp4", "c07abd209f4836ed00cdef346882f615", 1152, 768),
 "s24t2": ("takes/media-generation-mv7v2-s24-t2-0-c51ead16-af8d-41e9-9a23-9395fae4ad5f.mp4", "2d9dd5ff1a6c81342925ae3f88909cd9", 1152, 768),
 "s24t1": ("takes/media-generation-mv7v2-s24-final-chorus-tag-cha-0-8a6124cb-18e1-44a4-a038-d3a768b78605.mp4", "de3d132ba3598dc8c2d336410c57a453", 1152, 768),
}

# (label, take_key, take_start, take_end, song_start, song_end, kind)
SEGMENTS = [
 ("S01a-occ1", "s01t2", 0.00, 2.46, 0.00, 2.28, "sing"),
 ("S01a-occ2", "s01t2", 2.70, 4.66, 2.28, 4.14, "sing"),
 ("S01a-occ3", "s01t2", 4.80, 6.50, 4.14, 6.90, "sing"),
 ("S01b", "s01t1", 2.50, 7.20, 6.90, 9.92, "restage"),
 ("S02-occ1", "s02t1", 0.00, 3.04, 9.92, 14.30, "sing"),
 ("S02-occ2", "s02t1", 4.28, 7.14, 14.30, 18.74, "sing"),
 ("GAP-18.74", "s02t1", 7.14, 7.98, 18.74, 19.58, "gap"),
 ("S03-V1.1", "s03t1", 0.00, 3.16, 19.58, 22.60, "sing"),
 ("S03-V1.2", "s03t1", 3.50, 6.74, 22.60, 24.62, "sing"),
 ("S03-V1.3", "s03t1", 7.24, 9.48, 24.62, 26.82, "sing"),
 ("S04-V1.4", "s04t1", 0.00, 3.70, 26.82, 29.42, "sing"),
 ("S04-V1.5", "s04t1", 4.44, 7.24, 29.42, 31.74, "sing"),
 ("S04-V1.6", "s04t1", 7.24, 9.68, 31.74, 34.02, "sing"),
 ("S05a-PC1.1", "s05a", 0.00, 4.94, 34.02, 36.50, "sing"),
 ("S05b-PC1.2", "s05b", 0.00, 5.32, 36.50, 38.60, "sing"),
 ("S06-PC1.3", "s06t1", 0.00, 5.14, 38.60, 42.90, "sing"),
 ("S06-PC1.4", "s06t1", 5.32, 8.60, 42.90, 46.20, "sing"),
 ("GAP-46.20", "s06t1", 8.60, 10.00, 46.20, 47.02, "gap"),
 ("S07-C1.1", "s07t1", 0.00, 2.00, 47.02, 49.40, "sing"),
 ("S07-C1.2", "s07t1", 2.88, 5.02, 49.40, 51.76, "sing"),
 ("S07-C1.3", "s07t1", 5.02, 7.68, 51.76, 53.82, "sing"),
 ("S07-C1.4", "s07t1", 8.06, 9.70, 53.82, 56.18, "sing"),
 ("S08-C1.5", "s08t2", 0.00, 4.18, 56.18, 59.34, "sing"),
 ("S08-C1.6", "s08t2", 4.18, 7.48, 59.34, 61.46, "sing"),
 ("S08-C1.7", "s08t2", 7.58, 8.82, 61.46, 63.72, "sing"),
 ("S09-occ1", "s09t2", 0.00, 2.22, 63.72, 66.26, "sing"),
 ("S09-occ2", "s09t2", 3.54, 6.42, 66.26, 67.80, "sing"),
 ("S10-occ1", "s10t1", 0.00, 2.74, 67.80, 70.48, "sing"),
 ("S10-occ2", "s10t1", 2.74, 5.18, 70.48, 73.16, "sing"),
 ("S10-occ3", "s10t1", 5.18, 7.38, 73.16, 75.84, "sing"),
 ("S11-V2.1", "s11t1", 0.00, 2.88, 75.84, 78.50, "sing"),
 ("S11-V2.2", "s11t1", 3.68, 6.68, 78.50, 80.58, "sing"),
 ("S11-V2.3", "s11t1", 7.06, 9.08, 80.58, 82.94, "sing"),
 ("S12-V2.4", "s12t2", 0.00, 3.24, 82.94, 85.18, "sing"),
 ("S12-V2.5", "s12t2", 4.18, 6.82, 85.18, 87.66, "sing"),
 ("S12-V2.6", "s12t2", 7.24, 9.52, 87.66, 89.92, "sing"),
 ("S13-PC2.1", "s13t2", 0.00, 4.28, 89.92, 93.08, "sing"),
 ("S13-PC2.2", "s13t2", 4.76, 8.82, 93.08, 95.20, "sing"),
 ("S14-PC2.3", "s14t1", 0.00, 4.46, 95.20, 99.82, "sing"),
 ("S14-PC2.4", "s14t1", 5.10, 8.02, 99.82, 103.36, "sing"),
 ("S15-C2.1", "s15t2", 0.00, 2.68, 103.36, 105.50, "sing"),
 ("S15-C2.2", "s15t2", 3.28, 5.34, 105.50, 108.28, "sing"),
 ("S15-C2.3", "s15t2", 5.64, 8.20, 108.28, 110.36, "sing"),
 ("C2.4-COVER", "s18t1", 7.50, 10.00, 110.36, 112.86, "montage"),
 ("S16-C2.5", "s16t1", 0.00, 4.22, 112.86, 115.42, "sing"),
 ("S16-C2.6", "s16t1", 4.22, 7.46, 115.42, 117.86, "sing"),
 ("S17-C2.7", "s17t1", 0.00, 3.52, 117.86, 120.32, "sing"),
 ("S17-C2.8", "s17t1", 4.46, 7.36, 120.32, 123.26, "sing"),
 ("S18-plate", "s18t1", 0.00, 10.00, 123.26, 132.58, "plate"),
 ("S19-plate", "s19t1", 0.00, 10.00, 132.58, 143.40, "plate"),
 ("S20-FC.1", "s20t2", 0.00, 2.18, 143.40, 145.52, "sing"),
 ("S20-FC.2", "s20t2", 2.94, 5.10, 145.52, 148.24, "sing"),
 ("S20-FC.3", "s20t2", 5.50, 8.12, 148.24, 150.38, "sing"),
 ("FC.4-COVER", "s19t1", 0.50, 3.00, 150.38, 152.88, "montage"),
 ("S21-FC.5", "s21t1", 0.00, 3.70, 152.88, 155.40, "sing"),
 ("S21-FC.6", "s21t1", 3.70, 6.68, 155.40, 157.84, "sing"),
 ("S21-FC.7", "s21t1", 6.68, 9.24, 157.84, 160.02, "sing"),
 ("S22-FC.8", "s22t1", 0.00, 2.90, 160.02, 164.16, "sing"),
 ("S22-FC.9", "s22t1", 3.98, 7.52, 164.16, 168.16, "sing"),
 ("S23-FC.10", "s23t1", 0.00, 6.60, 168.16, 173.30, "sing"),
 ("S24-P1", "s24t2", 0.00, 3.46, 173.30, 176.26, "sing"),
 ("S24-P2", "s24t2", 4.04, 7.92, 176.26, 183.24, "sing"),
 ("FADE", "s24t1", 6.62, 10.00, 183.24, 187.20, "fade"),
]

def md5_of(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    # verify take md5s
    bad = []
    for key, (rel, want, w, h) in TAKES.items():
        got = md5_of(os.path.join(PROJ, rel))
        if got != want:
            bad.append((key, want, got))
    if bad:
        print("MD5 MISMATCH:", bad)
        sys.exit(1)
    print("all take md5s verified")

    out = []
    total_frames = 0
    prev_song_end = 0.0
    problems = []
    for i, (label, key, ts, te, ss, se, kind) in enumerate(SEGMENTS):
        if abs(ss - prev_song_end) > 0.005:
            problems.append(f"{label}: song gap/overlap at {prev_song_end:.2f} -> {ss:.2f}")
        take_span = te - ts
        song_span = se - ss
        factor = song_span / take_span
        speed = take_span / song_span
        frames = round(song_span * 24)
        if speed < 0.5:
            problems.append(f"{label}: speed {speed:.3f}x BELOW 0.5 floor (factor {factor:.3f})")
        if speed > 2.6:
            problems.append(f"{label}: speed {speed:.3f}x extreme (factor {factor:.3f})")
        out.append({
            "idx": i, "label": label, "take": key, "file": TAKES[key][0],
            "w": TAKES[key][2], "h": TAKES[key][3],
            "take_start": ts, "take_end": te, "song_start": ss, "song_end": se,
            "kind": kind, "factor": round(factor, 4), "speed": round(speed, 4),
            "frames": frames,
        })
        total_frames += frames
        prev_song_end = se
        print(f"{i:2d} {label:12s} {key:7s} take {ts:5.2f}-{te:5.2f} song {ss:6.2f}-{se:6.2f} "
              f"factor {factor:5.3f} speed {speed:5.3f}x frames {frames:3d} {kind}")
    print(f"TOTAL frames {total_frames} = {total_frames/24:.3f}s (target 187.200s, 4493f = 187.208s)")
    if abs(prev_song_end - 187.20) > 0.005:
        problems.append(f"song end {prev_song_end}, expected 187.20")
    # adjust final segment to land exactly 4493 frames
    diff = 4493 - total_frames
    if diff != 0:
        print(f"adjusting FADE frames by {diff} to total 4493")
        out[-1]["frames"] += diff
        total_frames += diff
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  !", p)
    else:
        print("no problems")
    json.dump({"segments": out, "total_frames": total_frames}, open(os.path.join(PROJ, "work/assembly/cutlist.json"), "w"), indent=1)
    print("wrote work/assembly/cutlist.json")

if __name__ == "__main__":
    main()
