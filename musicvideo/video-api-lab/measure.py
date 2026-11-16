import sys, json
from PIL import Image
import collections, math
def palette(path, size=160):
    im = Image.open(path).convert('RGB')
    im.thumbnail((size,size))
    px = list(im.getdata())
    def bucket(c):
        return tuple(int(round(v/32)*32) for v in c)
    cnt = collections.Counter(bucket(p) for p in px)
    total = len(px)
    top = [(f"#{r:02x}{g:02x}{b:02x}", round(n/total*100,1)) for (r,g,b),n in cnt.most_common(8)]
    # named probes: fraction of pixels near target colours
    def frac(target, tol=60):
        tr,tg,tb = target
        return round(sum(1 for r,g,b in px if abs(r-tr)<tol and abs(g-tg)<tol and abs(b-tb)<tol)/total*100,2)
    probes = {
      "teal_cat(0,160,160)": frac((0,170,170)),
      "magenta_wall(220,0,140)": frac((225,0,140)),
      "green_floor(0,200,60)": frac((0,200,60)),
      "yellow_star(250,210,0)": frac((250,210,0)),
      "navy_night(20,30,90)": frac((20,30,90)),
      "red_lighthouse(220,40,40)": frac((220,40,40)),
      "orange_scarf(240,130,0)": frac((240,130,0)),
    }
    return {"file": path, "top": top, "probes_pct": probes}
for p in sys.argv[1:]:
    print(json.dumps(palette(p), indent=1))
