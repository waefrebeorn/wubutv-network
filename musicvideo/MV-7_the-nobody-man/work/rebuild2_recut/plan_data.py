"""MV-7 REBUILD-2 re-cut — shared plan data.
Builds the per-line plan: song line spans + word anchors from SONG_WORDS.json,
take assignment + method per run-5 dispositions, take word slices."""
import json, re, os

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
FPS = 24
SONG = json.load(open(f"{BASE}/SONG_WORDS.json"))["words"]
UNITS = {u["unit"]: u for u in json.load(open(f"{BASE}/work/otaku_units.json"))}

NORM = {"spots": "sparks", "flipping": "flicking", "prayed": "made", "-made": "mad",
        "joints": "joins", "lonely": "low-lit", "same": "saved", "lessen": "lasts",
        "land": "lasts", "can't": "yeah", "cray": "grand", "ma": "man", "-": "man"}
def norm(w):
    w = w.lower().strip(",.?!")
    return NORM.get(w, w)

def song_words(a, b):
    return [w for w in SONG if a - 0.01 <= w["start"] < b]

def take_words(path):
    if not os.path.exists(path):
        return []
    d = json.load(open(path))
    return d["words"] if isinstance(d, dict) else d

OTW = f"{BASE}/work/otaku_take_words"
RTW = f"{BASE}/work/rebuild2_take_words"
OTK = f"{BASE}/takes/otaku"
RB2 = f"{BASE}/takes/rebuild2"

def U(uid, tv="t1"):
    suf = f"_{tv}" if tv != "t1" else "_t1"
    return (f"{OTK}/mv7o_{uid.lower()}{suf}.mp4",
            f"{OTW}/{uid}{'_'+tv if tv!='t1' else ''}.json")
def R(rid):
    return (f"{RB2}/mv7r2_{rid.lower()}_t1.mp4", f"{RTW}/{rid}.json")

# Non-chant line table: ref, lyric, song_start, song_end(next onset), unit
T = [
 ("V1.1","I got a profile, got a pile",19.58,22.60,"U05"),("V1.2","Got a thousand posts in a folder file",22.60,24.62,"U05"),
 ("V1.3","Old meme face and a busted grin",24.62,26.82,"U06"),("V1.4","Been here so long, I could sign back in",26.82,29.42,"U06"),
 ("V1.5","Made a joke at a quarter past eight",29.42,31.74,"U07"),("V1.6","Watched it sit there while I wait",31.74,34.02,"U07"),
 ("PC1.1","I kept clicking, kept sticking around",34.02,36.50,"U08"),("PC1.2","Little by little, I learned the sound",36.50,38.60,"U08"),
 ("PC1.3","Nobody noticing? Fine by me",38.60,42.90,"U09"),("PC1.4","I built my kingdom quietly",42.90,46.20,"U10"),
 ("C1.1","I'm The Nobody Man",47.02,49.40,"U11"),("C1.2","Still here, still stand",49.40,51.76,"U11"),
 ("C1.3","I post, I fade, I post again",51.76,53.82,"U12"),("C1.4","I'm The Nobody Man",53.82,56.18,"U12"),
 ("C1.5","I got a thousand little sparks",56.18,59.34,"U13"),("C1.6","Flicking in the dark",59.34,61.46,"U13"),
 ("C1.7","I'm The Nobody Man",61.46,63.72,"U14"),("C1.8","Nobody Man",63.72,67.80,"U15"),
 ("V2.1","I got drafts in the drawer like coins",75.84,78.50,"U18"),("V2.2","Half-mad thoughts and a stack of joins",78.50,80.58,"U18"),
 ("V2.3","Tiny wins in a low-lit room",80.58,82.94,"U19"),("V2.4","One more clip and one more zoom",82.94,85.18,"U19"),
 ("V2.5","Everybody chasing that giant shout",85.18,87.66,"U20"),("V2.6","I got a small flame I won't put out",87.66,89.92,"U20"),
 ("PC2.1","I kept clicking, kept sticking around",89.92,93.08,"U21"),("PC2.2","Little by little, I learned the sound",93.08,95.20,"U21"),
 ("PC2.3","No one crowned me, no one had to",95.20,99.82,"U22"),("PC2.4","I made this mess on purpose too",99.82,103.36,"U23"),
 ("C2.1","I'm The Nobody Man",103.36,105.50,"U24"),("C2.2","Still here, still stand",105.50,108.28,"U24"),
 ("C2.3","I post, I fade, I post again",108.28,110.36,"U25"),("C2.4","I'm The Nobody Man",110.36,112.86,"U25"),
 ("C2.5","I got a thousand little sparks",112.86,115.42,"U26"),("C2.6","Flicking in the dark",115.42,117.86,"U26"),
 ("C2.7","I'm The Nobody Man",117.86,120.32,"U27"),("C2.8","Nobody Man",120.32,123.26,"U27"),
 ("B.1","Call me lost, call me late",123.26,126.46,"U28"),("B.2","Call me anything you wanna say",126.46,128.10,"U28"),
 ("B.3","I got roots in the endless feed",128.10,130.46,"U29"),("B.4","And every scar is a saved receipt",130.46,132.58,"U29"),
 ("B.5","If fame won't call, then let it pass",132.58,137.02,"U30"),("B.6","I'm the joke that lasts and lasts",137.02,141.44,"U31"),
 ("FC.1","I'm The Nobody Man",143.40,145.52,"U32"),("FC.2","Still here, still stand",145.52,148.24,"U32"),
 ("FC.3","I post, I fade, I post again",148.24,150.38,"U33"),("FC.4","I'm The Nobody Man",150.38,152.88,"U33"),
 ("FC.5","I got a thousand little sparks",152.88,155.40,"U34"),("FC.6","Flicking in the dark",155.40,157.84,"U34"),
 ("FC.7","I'm The Nobody Man",157.84,160.02,"U35"),("FC.8","Nobody Man",160.02,164.16,"U36"),
 ("FC.9","I'm The Nobody Man",164.16,168.16,"U37"),("FC.10","Yeah, I turn the small things grand",168.16,173.30,"U38"),
]

# Assignment: ref -> (kind, take_key, extra)
# kind: KEEP | RESCUE | COND | STRUCT | MONTAGE | CHANT variants handled below
ASSIGN = {
 "V1.1": ("COND", "R05A"), "V1.2": ("STRUCT", "R05B"), "V1.3": ("STRUCT", "R06A"),
 "V1.4": ("RESCUE", "R06B"), "V1.5": ("KEEP", "U07"), "V1.6": ("KEEP", "U07"),
 "PC1.1": ("RESCUE", "R08A"), "PC1.2": ("RESCUE", "R08B"),
 "PC1.3": ("KEEP", "U09"), "PC1.4": ("KEEP", "U10"),
 "C1.1": ("KEEP", "U11"), "C1.2": ("KEEP", "U11"), "C1.3": ("KEEP", "U12"), "C1.4": ("KEEP", "U12"),
 "C1.5": ("KEEP", "R13A"), "C1.6": ("KEEP", "R13B"), "C1.7": ("RESCUE", "R14"),
 "C1.8": ("KEEP", "R15"),
 "V2.1": ("KEEP", "R18A"), "V2.2": ("RESCUE", "R18B"), "V2.3": ("KEEP", "U19t2"), "V2.4": ("KEEP", "U19t2"),
 "V2.5": ("RESCUE", "R20A"), "V2.6": ("RESCUE", "R20B"),
 "PC2.1": ("RESCUE", "R21A"), "PC2.2": ("STRUCT", "R21B"), "PC2.3": ("KEEP", "R22"), "PC2.4": ("KEEP", "U23"),
 "C2.1": ("KEEP", "U24t2"), "C2.2": ("KEEP", "U24t2"), "C2.3": ("KEEP", "U25"), "C2.4": ("KEEP", "U25"),
 "C2.5": ("KEEP", "U26"), "C2.6": ("KEEP", "U26"), "C2.7": ("KEEP", "U27"), "C2.8": ("KEEP", "U27"),
 "B.1": ("MONTAGE", "U28"), "B.2": ("MONTAGE", "U28"), "B.3": ("MONTAGE", "U29"), "B.4": ("MONTAGE", "U29"),
 "B.5": ("MONTAGE", "U30"), "B.6": ("KEEP", "U31"),
 "FC.1": ("STRUCT", "R32A"), "FC.2": ("STRUCT", "R32B"),
 "FC.3": ("KEEP", "U33"), "FC.4": ("KEEP", "U33"),
 "FC.5": ("RESCUE", "R34A"), "FC.6": ("COND", "R34B"), "FC.7": ("COND", "R35"),
 "FC.8": ("RESCUE", "U36"), "FC.9": ("RESCUE", "U37"), "FC.10": ("KEEP", "U38"),
}

def resolve(key):
    if key.startswith("R"):
        return R(key)
    uid = key[:3]; tv = key[3:] or "t1"
    return U(uid, tv)

def lyric_tokens(lyric):
    return [norm(t) for t in re.split(r"[\s/]+", lyric) if t.strip()]

def match_slice(take_ws, toks, start_idx=0):
    """Find the take-word slice performing toks, searching from start_idx.
    Returns (i0, i1) inclusive indices or None."""
    tw = [norm(w["word"]) for w in take_ws]
    if not tw or not toks:
        return None
    starts = [i for i in range(start_idx, len(tw)) if tw[i] == toks[0]]
    if not starts:
        return None
    i0 = starts[0]
    ends = [i for i in range(i0, len(tw)) if tw[i] == toks[-1]]
    if not ends:
        return None
    i1 = min(ends, key=lambda e: (abs((e - i0 + 1) - len(toks)), e))
    return (i0, i1)
