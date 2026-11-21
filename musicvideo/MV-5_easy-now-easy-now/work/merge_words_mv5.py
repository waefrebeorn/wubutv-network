"""Merge MV-5 Whisper passes into SONG_WORDS.json + line table.
Sources: work/song_transcript_noprompt.json (base, best structure),
work/song_transcript_prompted.json (chorus slots), targeted tail decodes.
Per-line boundaries/owners are the adjudicated line list below (see
LYRIC_TIMELINE.md for evidence). Word times: Whisper words matched by
order inside each line window; even-split fallback, flagged in 'source'.
"""
import json, os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(BASE, "work")

def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())

# (id, section, performed text, start, end, owner, confidence, word_source)
LINES = [
 ("I01","Intro","Easy now, easy now",1.66,3.82,"CAT","inferred","noprompt"),
 ("I02","Intro","We ride, we ride",3.82,5.98,"CAT","inferred","noprompt"),
 ("I03","Intro","Easy now, easy now",5.98,8.01,"CAT","inferred","noprompt"),
 ("I04","Intro","Till the morning comes",8.01,10.04,"CAT","inferred","noprompt"),
 ("I05","Intro","Easy now, easy now",10.04,12.72,"CAT","inferred","noprompt"),
 ("I06","Intro","We ride, we ride",12.72,15.40,"CAT","inferred","noprompt"),
 ("I07","Intro","Easy now, easy now",15.40,17.02,"CAT","inferred","noprompt"),
 ("I08","Intro","Till the morning comes",17.02,18.64,"CAT","inferred","noprompt"),
 ("I09","Intro","(ta-da vocalise)",18.64,22.00,"GIRL","confirmed","noprompt"),
 ("L01","Verse 1","Bare feet on the boardwalk",22.00,23.42,"CAT","inferred","noprompt"),
 ("L02","Verse 1","Salt on my skin",23.42,24.60,"CAT","inferred","noprompt"),
 ("L03","Verse 1","You came in laughing",24.60,26.76,"CAT","inferred","noprompt"),
 ("L04","Verse 1","Said, come on, let's begin",27.76,29.60,"CAT","inferred","noprompt"),
 ("L05","Verse 1","Blue shirt, red bicycle",29.60,31.48,"CAT","inferred","noprompt"),
 ("L06","Verse 1","Rolling past the pier",31.48,33.62,"CAT","confirmed","noprompt"),
 ("L07","Verse 1","I was posted up right here",33.62,36.14,"CAT","confirmed","noprompt"),
 ("L08","Verse 1","Now you're pulling near",36.14,38.48,"CAT","confirmed","noprompt"),
 ("L09","Verse 1","Backpack half-zipped",38.48,40.44,"CAT","confirmed","noprompt"),
 ("L10","Verse 1","Keys in your hand",40.44,42.82,"CAT","confirmed","noprompt"),
 ("L11","Verse 1","You nodded at the waves like",42.82,44.58,"CAT","confirmed","noprompt"),
 ("L12","Verse 1","Yeah, they already understand",44.58,46.86,"CAT","confirmed","noprompt"),
 ("L13","Pre-Chorus 1","Slow down, take your time",47.76,49.60,"CAT","inferred","noprompt"),
 ("L14","Pre-Chorus 1","Let the hard week fade",49.60,51.46,"CAT","inferred","noprompt"),
 ("L15","Pre-Chorus 1","One small look from you",51.46,52.80,"CAT","confirmed","noprompt"),
 ("L16","Pre-Chorus 1","And my whole head replays",52.80,56.50,"CAT","confirmed","noprompt"),
 ("L17","Chorus 1","Easy now, easy now",57.52,59.10,"GIRL","inferred","prompted"),
 ("L18","Chorus 1","We ride, we ride",59.10,60.22,"CAT","inferred","prompted"),
 ("L19","Chorus 1","Easy now, easy now",60.22,61.34,"GIRL","inferred","prompted"),
 ("L20","Chorus 1","With you by my side",61.34,62.52,"CAT","inferred","prompted"),
 ("L21","Chorus 1","Easy now, easy now",62.52,63.66,"GIRL","inferred","prompted"),
 ("L22","Chorus 1","No need to run",63.66,64.92,"CAT","inferred","prompted"),
 ("L23","Chorus 1","Easy now, easy now",64.92,65.96,"GIRL","inferred","prompted"),
 ("L24","Chorus 1","We hold the sun",65.96,67.06,"CAT","inferred","prompted"),
 ("L25","Chorus 1","Easy now, easy now",67.06,68.20,"GIRL","inferred","prompted"),
 ("L26","Chorus 1","Keep it loose, keep it low",68.20,69.40,"CAT","inferred","prompted"),
 ("L27","Chorus 1","Easy now, easy now",69.40,70.46,"GIRL","inferred","prompted"),
 ("L28","Chorus 1","Let it drift, let it go",70.46,71.66,"CAT","inferred","prompted"),
 ("L29","Chorus 1","Easy now, easy now",71.66,72.74,"GIRL","inferred","prompted"),
 ("L30","Chorus 1","We're good where we are",72.74,74.02,"CAT","inferred","prompted"),
 ("L31","Chorus 1","Easy now, easy now",74.02,75.04,"GIRL","inferred","prompted"),
 ("L32","Chorus 1","Just two small sparks",75.04,76.80,"CAT","inferred","prompted"),
 ("L33","Chorus 1 tail","I gotta go there",76.80,78.76,"CAT","inferred","tail"),
 ("L34","Chorus 1 tail","I gotta go there, just two small sparks",78.76,81.76,"CAT","inferred","tail"),
 ("L35","Chorus 1 tail","I gotta go there",81.76,83.14,"CAT","inferred","tail"),
 ("L36","Chorus 1 tail","Just two small sparks",83.14,85.16,"CAT","inferred","tail"),
 ("L37","Verse 2","Vendor at the corner",85.20,87.00,"CAT","inferred","noprompt"),
 ("L38","Verse 2","Calling mango sweet",87.00,87.60,"GIRL","inferred","noprompt"),
 ("L39","Verse 2","Socks in the sand",87.60,88.92,"GIRL","inferred","noprompt"),
 ("L40","Verse 2","And the tide tapping time with our feet",88.92,93.00,"SPLIT","inferred","noprompt"),
 ("L41","Verse 2","Your laugh hit the air",93.80,95.12,"GIRL","inferred","noprompt"),
 ("L42","Verse 2","Like a hand drum roll",95.80,96.84,"CAT","inferred","noprompt"),
 ("L43","Verse 2","I forgot the list, forgot the bills",96.84,98.44,"GIRL","inferred","noprompt"),
 ("L44","Verse 2","Forgot what I was told",98.44,102.40,"CAT","inferred","noprompt"),
 ("L45","Verse 2","Ice cup sweating",102.40,103.80,"GIRL","inferred","noprompt"),
 ("L46","Verse 2","On the rail by the steps",103.80,104.72,"GIRL","inferred","noprompt"),
 ("L47","Verse 2","You said, don't think too hard",104.72,106.42,"CAT","confirmed","noprompt"),
 ("L48","Verse 2","So I didn't, not yet",106.42,107.52,"SPLIT","confirmed","noprompt"),
 ("L49","Verse 2","Kids with a boombox",107.52,108.72,"GIRL","inferred","noprompt"),
 ("L50","Verse 2","Cutting through the crowd",108.72,109.74,"GIRL","inferred","noprompt"),
 ("L51","Verse 2","You took my sleeve and spun me once",109.74,110.70,"GIRL","inferred","noprompt"),
 ("L52","Verse 2","Like none of it was loud",110.70,111.90,"GIRL","inferred","noprompt"),
 ("L53","Pre-Chorus 2","Slow down, take your time",111.90,113.78,"CAT","inferred","noprompt"),
 ("L54","Pre-Chorus 2","Let the hard week fade",113.78,114.94,"CAT","inferred","noprompt"),
 ("L55","Pre-Chorus 2","One small look from you",114.94,116.00,"CAT","inferred","noprompt"),
 ("L56","Pre-Chorus 2","And my whole head replays",116.00,118.28,"GIRL","confirmed","noprompt"),
 ("L56b","Pre-Chorus 2","(held vocalise)",119.30,120.02,"GIRL","inferred","noprompt"),
 ("L57","Chorus 2","Easy now, easy now",121.26,122.58,"GIRL","inferred","prompted"),
 ("L58","Chorus 2","We ride, we ride",122.58,124.00,"CAT","inferred","prompted"),
 ("L59","Chorus 2","Easy now, easy now",124.00,125.06,"GIRL","inferred","prompted"),
 ("L60","Chorus 2","With you by my side",125.06,126.30,"CAT","inferred","prompted"),
 ("L61","Chorus 2","Easy now, easy now",126.30,127.38,"GIRL","inferred","prompted"),
 ("L62","Chorus 2","No need to run",127.38,128.52,"CAT","inferred","prompted"),
 ("L63","Chorus 2","Easy now, easy now",128.52,129.66,"GIRL","inferred","prompted"),
 ("L64","Chorus 2","We hold the sun",129.66,130.78,"CAT","inferred","prompted"),
 ("L65","Chorus 2","Easy now, easy now",130.78,131.88,"GIRL","inferred","prompted"),
 ("L66","Chorus 2","Keep it loose, keep it low",131.88,133.08,"CAT","inferred","prompted"),
 ("L67","Chorus 2","Easy now, easy now",133.08,134.18,"GIRL","inferred","prompted"),
 ("L68","Chorus 2","Let it drift, let it go",134.18,135.36,"CAT","inferred","prompted"),
 ("L69","Chorus 2","Easy now, easy now",135.36,136.44,"GIRL","inferred","prompted"),
 ("L70","Chorus 2","We're good where we are",136.44,137.62,"CAT","inferred","prompted"),
 ("L71","Chorus 2","Easy now, easy now",137.62,138.82,"GIRL","inferred","prompted"),
 ("L72","Chorus 2","Just two small sparks",138.82,140.52,"CAT","inferred","prompted"),
 ("L73a","Chorus 2 tail","I'm falling, I'm falling",140.52,143.14,"CAT","inferred","tail"),
 ("L73b","Chorus 2 tail","Just two small sparks",143.14,145.56,"CAT","inferred","tail"),
 ("L73c","Chorus 2 tail","I'm falling",145.56,146.62,"CAT","inferred","tail"),
 ("L73d","Chorus 2 tail","Just two small sparks",146.62,148.70,"CAT","inferred","tail"),
 ("L74","Bridge","If the rain comes down",148.70,150.00,"CAT","inferred","noprompt"),
 ("L75","Bridge","We stay out in it",150.00,151.30,"CAT","inferred","noprompt"),
 ("L76","Bridge","If the day runs long",151.30,152.36,"SPLIT","confirmed","noprompt"),
 ("L77","Bridge","We still move with it",152.36,153.58,"CAT","confirmed","noprompt"),
 ("L78","Bridge","Hand in my hand",153.58,154.42,"CAT","inferred","noprompt"),
 ("L79","Bridge","No speech, no show",154.42,155.72,"CAT","confirmed","noprompt"),
 ("L80","Bridge","Heart in the breeze",155.72,156.70,"GIRL","confirmed","noprompt"),
 ("L81","Bridge","And the bass move slow",156.70,158.06,"CAT","inferred","noprompt"),
 ("L82","Bridge","If the sky turns gray",158.06,159.10,"CAT","inferred","noprompt"),
 ("L83","Bridge","We don't fold in",159.10,160.24,"CAT","inferred","noprompt"),
 ("L84","Bridge","We lean right back",160.24,161.36,"CAT","inferred","noprompt"),
 ("L85","Bridge","Let the whole thing spin",161.36,162.46,"CAT","inferred","noprompt"),
 ("L86","Bridge","You and me, same pace",162.46,163.58,"CAT","inferred","noprompt"),
 ("L87","Bridge","Same worn-in shoes",163.58,164.90,"CAT","inferred","noprompt"),
 ("L88","Bridge","Nothing to prove",164.90,165.88,"CAT","inferred","noprompt"),
 ("L89","Bridge","Nothing to lose",165.88,167.50,"CAT","confirmed","noprompt"),
 ("L90","Bridge","(No, no, no ad-lib)",167.50,169.16,"CAT","inferred","noprompt"),
 ("L91","Final Chorus","Easy now, easy now",169.16,170.18,"GIRL","inferred","noprompt"),
 ("L92","Final Chorus","We ride, we ride",170.18,171.44,"CAT","inferred","noprompt"),
 ("L93","Final Chorus","Easy now, easy now",171.44,172.58,"GIRL","inferred","noprompt"),
 ("L94","Final Chorus","With you by my side",172.58,173.62,"CAT","inferred","noprompt"),
 ("L95","Final Chorus","Easy now, easy now",173.62,174.92,"GIRL","inferred","noprompt"),
 ("L96","Final Chorus","No need to run",174.92,176.04,"SPLIT","confirmed","noprompt"),
 ("L97","Final Chorus","Easy now, easy now",176.04,177.20,"GIRL","inferred","noprompt"),
 ("L98","Final Chorus","We hold the sun",177.20,178.24,"CAT","inferred","noprompt"),
 ("L99","Final Chorus","Easy now, easy now",178.24,179.30,"GIRL","inferred","noprompt"),
 ("L100","Final Chorus","Keep it loose, keep it low",179.30,180.50,"CAT","inferred","noprompt"),
 ("L101","Final Chorus","Easy now, easy now",180.50,181.56,"GIRL","inferred","noprompt"),
 ("L102","Final Chorus","Let it drift, let it go",181.56,182.78,"CAT","inferred","noprompt"),
 ("L103","Final Chorus","Easy now, easy now",182.78,183.80,"GIRL","inferred","noprompt"),
 ("L104","Final Chorus","We're good where we are",183.80,185.02,"CAT","inferred","noprompt"),
 ("L105","Final Chorus","Easy now, easy now",185.02,186.46,"GIRL","inferred","noprompt"),
 ("L106","Final Chorus","Just two small sparks",186.46,188.04,"CAT","inferred","noprompt"),
 ("L107","Final Chorus","Easy now, easy now",190.42,194.72,"GIRL","inferred","tail"),
 ("L108","Final Chorus","We ride, we ride",194.72,197.58,"CAT","inferred","tail"),
 ("L109","Final Chorus","Easy now, easy now",197.58,203.42,"GIRL","inferred","tail"),
 ("L110","Final Chorus","Till the morning comes",203.42,205.58,"CAT","inferred","tail"),
]

def load_words(path):
    d = json.load(open(path))
    ws = []
    for s in d["segments"]:
        ws.extend(s["words"])
    return sorted(ws, key=lambda w: w["start"])

def main():
    nop = load_words(os.path.join(WORK, "song_transcript_noprompt.json"))
    pro = load_words(os.path.join(WORK, "song_transcript_prompted.json"))
    tail_ws = []
    for f in ["transcript_c1tail_noprompt.json","transcript_c2tail_noprompt.json","transcript_tail_noprompt.json"]:
        p = os.path.join(WORK, f)
        if os.path.exists(p):
            tail_ws.extend(load_words(p))
    tail_ws = sorted(tail_ws, key=lambda w: w["start"])
    out_words = []
    for (lid, sec, text, t0, t1, owner, conf, src) in LINES:
        perf = text.replace("(","").replace(")","").split()
        perf = [w.strip(",") for w in perf]
        # the ta-da / ad-lib lines have no performed words: use placeholder words
        if lid in ("I09",):
            perf = ["ta-da","ta-da","ta-da","ta-da","ta-da","ta-da"]
        if lid in ("L56b",):
            perf = ["(held)"]
        if lid in ("L90",):
            perf = ["No,","no,","no"]
        pool = {"noprompt": nop, "prompted": pro, "tail": tail_ws}[src]
        cand = [w for w in pool if w["start"] >= t0 - 0.35 and w["end"] <= t1 + 0.35]
        n = len(perf)
        if len(cand) >= n and n > 0:
            # take the n candidates whose normalized forms best match in order;
            # simple: first n candidates in the window (Whisper order == sung order)
            use = cand[:n]
            for i, pw in enumerate(perf):
                w = use[i]
                out_words.append({"word": pw, "start": round(w["start"],3), "end": round(w["end"],3),
                                  "prob": round(w.get("prob",0),3), "line": lid, "section": sec,
                                  "owner": owner, "source": src})
        else:
            # even split across the line window
            span = (t1 - t0) / max(n,1)
            for i, pw in enumerate(perf):
                s = round(t0 + i*span, 3); e = round(t0 + (i+1)*span, 3)
                out_words.append({"word": pw, "start": s, "end": e, "prob": 0.0,
                                  "line": lid, "section": sec, "owner": owner,
                                  "source": src + "+even"})
    out = {
      "track": "track.mp3",
      "track_md5": "0c1bcafa568547e2d4fa36e133ad3626",
      "duration": 206.4,
      "method": ("faster-whisper base (~/workspace/fw-venv), word timestamps, mono 16k; "
        "no-prompt full-track pass as base (88 segments, 556 words), prompted full-track pass "
        "for chorus slots (110 segments, 506 words), targeted re-decodes for the intro, "
        "chorus tails and final tail; cross-checked against the Suno lyric video frames "
        "(track.mp4, 1fps). Per-line vocal owner from librosa pyin + aubio YIN f0 analysis "
        "(see LYRIC_TIMELINE.md vocal-ownership section); CAT = low male voice ~97-160 Hz, "
        "GIRL = high voice ~200-330 Hz. Even-split word times flagged in 'source'."),
      "lines": [{"id": lid, "section": sec, "text": text, "start": t0, "end": t1,
                 "owner": owner, "confidence": conf} for (lid, sec, text, t0, t1, owner, conf, src) in LINES],
      "words": out_words,
    }
    with open(os.path.join(BASE, "SONG_WORDS.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("lines:", len(LINES), "words:", len(out_words))
    even = sum(1 for w in out_words if "even" in w["source"])
    print("even-split words:", even)
    from collections import Counter
    print("owners:", Counter(w["owner"] for w in out_words))
    print("first word:", out_words[0], "last word:", out_words[-1])

if __name__ == "__main__":
    main()
