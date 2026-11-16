#!/usr/bin/env python3
"""Build MV7_OTAKU_PLAN.md + vehicles + units JSON from LYRIC_TIMELINE line times."""
import json, os

BASE = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man")
IDENT = ("young adult man in his mid-20s, tousled dark hair with ONE cadmium-yellow streak at the front, "
         "round glasses, bright alert eyes, clean-shaven, clear skin, warm determined friendly smile, eager and a little shy, "
         "oversized cozy cobalt-blue hoodie with an abstract white star pattern (no text, no logo), "
         "cat-ear headphones resting around his neck, abstract graphic tee underneath (shapes only)")
BAN = ("no stubble, no beard, no thinning hair, no heavy-lidded eyes, no tired grin, no busted grin, no older man, "
       "no dark dingy room, no candle, no gothic mood, no creepy expression, no hood shadowing the face, "
       "no readable text, no logos, no licensed characters, no franchise posters, no wordmark")
ROOMS = {
    "A": "bright cozy anime-fan creator room, small start: one modest shelf of original generic anime-style figurines, one monitor with abstract colourful glow, manga volumes with plain coloured spines, abstract colourful wall art, one tiny glowing star-shaped desk lamp on the desk",
    "B": "bright cozy anime-fan creator room filling up: fuller shelves of original generic anime-style figurines, two monitors with abstract colourful glow, manga volumes with plain coloured spines, plushies, warm LED strips, one tiny glowing star-shaped desk lamp on the desk",
    "C": "bright anime-fan creator kingdom: a whole wall of glowing screens with abstract colourful glow and ONE brighter steady light among them, full shelves of original generic anime-style figurines, plushies, warm LED strips, one tiny glowing star-shaped desk lamp still burning on the desk",
}

# unit: (id, era, song_in, song_out, sung_end, [(lineref, lyric)], tag, dur_req)
U = [
 ("U01","A",0.00,4.97,4.97,[("I1a","I'm The Nobody Man"),("I1b","I'm The Nobody Man")],"SINGING",5),
 ("U02","A",4.97,9.92,9.92,[("I1c","I'm The Nobody Man"),("I1d","I'm The Nobody Man")],"SINGING",5),
 ("U03","A",9.92,14.40,14.40,[("I2a","I'm The Nobody Man"),("I2b","I'm The Nobody Man")],"SINGING",5),
 ("U04","A",14.40,19.58,18.74,[("I2c","I'm The Nobody Man")],"SINGING",5),
 ("U05","A",19.58,24.62,24.62,[("V1.1","I got a profile, got a pile"),("V1.2","Got a thousand posts in a folder file")],"SINGING",5),
 ("U06","A",24.62,29.42,29.42,[("V1.3","Old meme face and a busted grin"),("V1.4","Been here so long, I could sign back in")],"SINGING",5),
 ("U07","A",29.42,34.02,34.02,[("V1.5","Made a joke at a quarter past eight"),("V1.6","Watched it sit there while I wait")],"SINGING",5),
 ("U08","A",34.02,38.60,38.60,[("PC1.1","I kept clicking, kept sticking around"),("PC1.2","Little by little, I learned the sound")],"SINGING",5),
 ("U09","A",38.60,42.90,42.90,[("PC1.3","Nobody noticing? Fine by me")],"SINGING",5),
 ("U10","A",42.90,47.02,46.20,[("PC1.4","I built my kingdom quietly")],"SINGING",5),
 ("U11","A",47.02,51.76,51.76,[("C1.1","I'm The Nobody Man"),("C1.2","Still here, still stand")],"SINGING",5),
 ("U12","A",51.76,56.18,56.18,[("C1.3","I post, I fade, I post again"),("C1.4","I'm The Nobody Man")],"SINGING",5),
 ("U13","A",56.18,61.46,61.46,[("C1.5","I got a thousand little sparks"),("C1.6","Flicking in the dark")],"SINGING",5),
 ("U14","A",61.46,63.72,63.72,[("C1.7","I'm The Nobody Man")],"SINGING",5),
 ("U15","A",63.72,67.80,67.80,[("C1.8","Nobody Man, Nobody Man")],"SINGING",5),
 ("U16","A",67.80,71.90,71.90,[("C1.Ta","Nobody Man"),("C1.Tb","Nobody Man")],"SINGING",5),
 ("U17","A",71.90,75.84,75.84,[("C1.Tc","Nobody Man"),("C1.Td","Nobody Man")],"SINGING",5),
 ("U18","B",75.84,80.58,80.58,[("V2.1","I got drafts in the drawer like coins"),("V2.2","Half-mad thoughts and a stack of joins")],"SINGING",5),
 ("U19","B",80.58,85.18,85.18,[("V2.3","Tiny wins in a low-lit room"),("V2.4","One more clip and one more zoom")],"SINGING",5),
 ("U20","B",85.18,89.92,89.92,[("V2.5","Everybody chasing that giant shout"),("V2.6","I got a small flame I won't put out")],"SINGING",5),
 ("U21","B",89.92,95.20,95.20,[("PC2.1","I kept clicking, kept sticking around"),("PC2.2","Little by little, I learned the sound")],"SINGING",5),
 ("U22","B",95.20,99.82,99.82,[("PC2.3","No one crowned me, no one had to")],"SINGING",5),
 ("U23","B",99.82,103.36,103.36,[("PC2.4","I made this mess on purpose too")],"SINGING",5),
 ("U24","B",103.36,108.28,108.28,[("C2.1","I'm The Nobody Man"),("C2.2","Still here, still stand")],"SINGING",5),
 ("U25","B",108.28,112.86,112.86,[("C2.3","I post, I fade, I post again"),("C2.4","I'm The Nobody Man")],"SINGING",5),
 ("U26","B",112.86,117.86,117.86,[("C2.5","I got a thousand little sparks"),("C2.6","Flicking in the dark")],"SINGING",5),
 ("U27","B",117.86,123.26,123.26,[("C2.7","I'm The Nobody Man"),("C2.8","Nobody Man")],"SINGING",5),
 ("U28","B",123.26,128.10,128.10,[("B.1","Call me lost, call me late"),("B.2","Call me anything you wanna say")],"MONTAGE",5),
 ("U29","B",128.10,132.58,132.58,[("B.3","I got roots in the endless feed"),("B.4","And every scar is a saved receipt")],"MONTAGE",5),
 ("U30","B",132.58,137.02,137.02,[("B.5","If fame won't call, then let it pass")],"MONTAGE",5),
 ("U31","B",137.02,143.40,141.44,[("B.6","I'm the joke that lasts and lasts")],"SINGING",5),
 ("U32","C",143.40,148.24,148.24,[("FC.1","I'm The Nobody Man"),("FC.2","Still here, still stand")],"SINGING",5),
 ("U33","C",148.24,152.88,152.88,[("FC.3","I post, I fade, I post again"),("FC.4","I'm The Nobody Man")],"SINGING",5),
 ("U34","C",152.88,157.84,157.84,[("FC.5","I got a thousand little sparks"),("FC.6","Flicking in the dark")],"SINGING",5),
 ("U35","C",157.84,160.02,160.02,[("FC.7","I'm The Nobody Man")],"SINGING",5),
 ("U36","C",160.02,164.16,164.16,[("FC.8","Nobody Man")],"SINGING",5),
 ("U37","C",164.16,168.16,168.16,[("FC.9","I'm The Nobody Man")],"SINGING",5),
 ("U38","C",168.16,173.30,173.30,[("FC.10","Yeah, I turn the small things grand")],"SINGING",5),
 ("U39","C",173.30,178.30,178.30,[("FC.Ta","I'm The Nobody Man"),("FC.Tb","Nobody Man")],"SINGING",5),
 ("U40","C",178.30,187.20,183.24,[("FC.Tc","Nobody Man"),("FC.Td","Nobody Man")],"SINGING",10),
]

MONTAGE_BEATS = {
 "U28": "Fast beat-matched montage inside the same bright otaku room: hands posting a plushie photo at the desk, figurine shelf details, the star lamp glowing, monitor glow reflections. No face singing; any face visible keeps its mouth closed and still. Quick energetic cuts feel, one continuous 5 second clip of lively room details in motion.",
 "U29": "Fast beat-matched montage inside the same bright otaku room: hands pinning colourful abstract art cards to a corkboard, scrolling abstract glowing feed shapes on a monitor (no readable text), manga volumes with plain spines sliding into a shelf. No face singing; mouths closed and still if any face appears.",
 "U30": "Beat-matched montage inside the same bright otaku room: phone face-down on the desk ignored while the star lamp glows, figurines and plushies in warm LED light, the creator's hands drumming happily on the desk. No singing; any face visible keeps its mouth closed and still.",
}

os.makedirs(f"{BASE}/otaku_vehicles", exist_ok=True)
units = []
for uid, era, t_in, t_out, sung_end, lines, tag, dur in U:
    lyric = " / ".join(l for _, l in lines)
    still = f"refs/otaku_era{era}.webp"
    if tag == "SINGING":
        pre = (f"Wide 16:9 landscape video, exactly {dur} seconds, 24 fps. Medium close-up, facing camera, locked-off steady camera. "
               f"The singer is a {IDENT}, in a {ROOMS[era]}. His mouth is clearly visible and unobstructed; head movement restrained.")
        post = (f"From 0.0 to {min(sung_end - t_in, 4.6):.1f} seconds he sings clearly and articulately, mouth opening and closing on the words \"{lyric}\". "
                f"Clear open mouth shapes on every syllable, visible jaw drop, lips forming distinct shapes, no whispering, no mumbling. "
                f"He sings the line exactly once: \"{lyric}\" — every word, including every repeat of the hook, sung one time only, no part repeated a second time. "
                f"All gesture and movement happens before the first word or after the last word, never during the sung window. "
                f"After the final word his mouth closes and stays closed for the remainder of the clip in a warm held smile. "
                f"Repeat of the sung line for clarity: \"{lyric}\". Hard bans: {BAN}.")
    else:
        pre = (f"Wide 16:9 landscape video, exactly {dur} seconds, 24 fps. Setting: a {ROOMS[era]}. "
               f"The room's owner is the {IDENT}.")
        post = (f"{MONTAGE_BEATS[uid]} Mouth remains closed and still throughout for every visible person. "
                f"Hard bans: {BAN}.")
    veh = f"{BASE}/otaku_vehicles/mv7o_{uid.lower()}_vehicle.txt"
    with open(veh, "w") as f:
        f.write(f"PRE:\n{pre}\nIMAGE: {still}\nPOST:\n{post}\n")
    units.append({"unit": uid, "era": era, "song_in": t_in, "song_out": t_out, "sung_end": sung_end,
                  "lines": [{"ref": r, "lyric": l} for r, l in lines], "lyric": lyric, "tag": tag,
                  "dur_req": dur, "still": still, "vehicle": f"otaku_vehicles/mv7o_{uid.lower()}_vehicle.txt",
                  "volley": (int(uid[1:]) - 1) // 6 + 1})
json.dump(units, open(f"{BASE}/work/otaku_units.json", "w"), indent=1)

with open(f"{BASE}/MV7_OTAKU_PLAN.md", "w") as f:
    f.write("# MV-7 OTAKU REBUILD — line-level plan (from LYRIC_TIMELINE.md)\n\n")
    f.write("Character: THE NOBODY MAN as WEEB OTAKU (brief lock). Motif: THE SMALL SPARK LAMP (star lamp) x3+ eras. "
            "Every hook occurrence gets its OWN fresh take. Singing units: 1-2 lines, sung window <=~5s. "
            "Bridge U28-U30 = beat-matched montage (not mouth-sung); U31 settles back to his face. "
            "Kinetic HIGHLIGHT layer burned in post from SONG_WORDS.json carries visible timing.\n\n")
    f.write("| Unit | Volley | Song in-out | Lines | Lyric | Tag | Era |\n|---|---|---|---|---|---|---|\n")
    for u in units:
        refs = "+".join(l["ref"] for l in u["lines"])
        f.write(f"| {u['unit']} | V{u['volley']} | {u['song_in']:.2f}-{u['song_out']:.2f} | {refs} | {u['lyric']} | {u['tag']} | {u['era']} |\n")
print("units:", len(units), "volleys:", max(u["volley"] for u in units))
