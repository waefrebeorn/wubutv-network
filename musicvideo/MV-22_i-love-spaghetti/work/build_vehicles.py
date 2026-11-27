import json, os
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STACK = os.path.join(P, "work/stills/stack")
MARCO = "Marco, a jovial Italian chef in his early fifties, salt-and-pepper hair swept back, big dark moustache, white double-breasted chef jacket, red neckerchief, flour-dusted dark apron"
ROSA = "Rosa, a warm woman in her late forties, dark hair in a neat bun, burgundy blouse, black apron"
ELDERLY = "an elderly gentleman guest in his seventies, round glasses, grey cardigan"
COUPLE = "a woman guest in her thirties in a green dress and a tall man guest in his thirties in a blue shirt"
LOOK = ("LOOK: photorealistic live action, warm golden evening light, cozy Italian trattoria, exposed brick, "
        "hanging copper pans and garlic braids, red-and-white checkered tablecloths, shallow depth of field, real people. "
        "No text, no captions, no signs, no letters, no logos, no watermarks anywhere in the picture.")
LOOK_NIGHT = ("LOOK: photorealistic live action, warm candlelit night light, cozy Italian trattoria, exposed brick, "
        "hanging copper pans and garlic braids, red-and-white checkered tablecloths, shallow depth of field, real people. "
        "No text, no captions, no signs, no letters, no logos, no watermarks anywhere in the picture.")
def perf(joined, soft=False):
    style = "softly and warmly" if soft else "clearly"
    return (f"PERFORMANCE: Marco faces the camera, mouth clearly visible and unobstructed, and SINGS the exact lyric "
            f"\"{joined}\" — he sings \"{joined}\" {style} with clear open mouth shapes on every syllable and visible jaw movement, "
            f"no whispering, no mumbling. Every other visible person's mouth remains closed and still for the entire line. "
            f"All entrances, gestures and camera movement happen only before the first word or after the last word. "
            f"After the last word his mouth closes and stays closed in a clean held pose. His mouth movement follows the exact lyric.")
PERF_WORDLESS = ("PERFORMANCE: nobody sings in this scene; every visible person's mouth remains closed and still throughout. Motion never stops.")
PERF_HANDS = "PERFORMANCE: nobody sings in this scene; no faces are shown, only hands at work. Motion never stops."
def dur(s): return f"Exactly {s} seconds long, in exactly 16:9 aspect ratio (landscape), 1280x720."
def R(name): return os.path.join(STACK, name)

# (n, win, lines, tag, refs, dur_s, [scene_text, perf_text], look)
S = []
S.append((1,(0.00,8.10),"Spaghetti so good","SINGING",[R("REF_KITCHEN.png")],10,
 [f"at the stove of a cozy Italian trattoria kitchen, the lid of a giant steel pot of spaghetti is ALREADY lifting with steam billowing out as {MARCO} strides in mid-step toward the pot, lifts the lid fully toward the camera in a cloud of steam, grinning, and presents the steaming pot with a sweeping proud gesture. EVENT: the lid lift — the lid rises high and the steam curls around his face as he sings. The camera pushes in slowly. Motion never stops.",
  perf("Spaghetti so good")], LOOK))
S.append((2,(8.10,14.72),"","CUTAWAY",[R("REF_KITCHEN.png")],10,
 ["at a flour-dusted wooden counter in a cozy Italian trattoria kitchen, a sheet of fresh pasta dough is ALREADY rolling through a hand-crank pasta machine, golden ribbons of fettuccine cascading down in waves into a growing floury pile while hands keep cranking steadily. EVENT: the pasta machine — the dough sheet feeds in and the ribbons pour out in one continuous cascade. Close-up on the machine and ribbons. Motion never stops.",
  PERF_HANDS], LOOK))
S.append((3,(14.72,19.72),"I love spaghetti / Hell I love it","SINGING",[R("REF_MARCO.png")],10,
 [f"at the kitchen pass of a cozy Italian trattoria, {MARCO} is ALREADY plating: with long tongs he lifts a high twirl of spaghetti strands from a steaming bowl and settles the mound onto a white plate in one motion, then presents the finished plate toward the camera on the second line. EVENT: the first plate — the strands lift high, settle into a perfect mound, and the plate is presented. Motion never stops.",
  perf("I love spaghetti, Hell I love it")], LOOK))
S.append((4,(19.72,25.44),"Marinara on penne / With meatballs so big / Tomato sauce stable","SINGING",[R("REF_MARCO.png")],10,
 [f"at the stove of a cozy Italian trattoria kitchen, {MARCO} ladles bright red marinara from a saucepan in one long arc over a bowl of penne exactly on the first line, then hefts two giant meatballs with tongs and sets them on top on the second line, and pats the bowl steady on the third line. EVENT: the sauce ladle — the long red arc lands as he sings. Motion never stops.",
  perf("Marinara on penne, With meatballs so big, Tomato sauce stable")], LOOK))
S.append((5,(25.44,31.24),"Full of vitamin C / Meat and pasta / Tastes so good to me","SINGING",[R("REF_MARCO.png")],10,
 [f"at a wooden counter in a cozy Italian trattoria kitchen, {MARCO} holds up a vine cluster of ripe red tomatoes toward the camera on the first line, then wafts the steam from a platter of meat and pasta toward his face with one hand, inhaling happily, through the last lines. EVENT: the steam blessing — he breathes in the steam with a blissful expression as he sings. Steam drifts continuously. Motion never stops.",
  perf("Full of vitamin C, Meat and pasta, Tastes so good to me")], LOOK))
S.append((6,(31.24,41.68),"Not formal with lasagna / I like it forkable / Yum with some parmesan / Spoonable for all","SINGING",[R("REF_MARCO.png")],10,
 [f"at a checkered table in a cozy Italian trattoria dining room, {MARCO} sits across from {ELDERLY} and demonstrates how to twirl spaghetti: he winds a forkful into a neat twirl on the second line and lifts it high intact, then on the last line slides a spoon under the twirl to cradle it. EVENT: the forkable demo — the twirl rises intact and holds. The elderly guest watches with delight. Static medium two-shot. Motion never stops.",
  perf("Not formal with lasagna, I like it forkable, Yum with some parmesan, Spoonable for all")], LOOK))
S.append((7,(41.68,47.02),"I love spaghetti / I love spaghetti / So good so good","SINGING",[R("REF_MARCO.png")],10,
 [f"at the kitchen pass of a cozy Italian trattoria, {MARCO} belts the chorus toward the dining room, arms spreading wide on the repeated line, while behind him the seated adult guests rise to their feet in a standing ovation, applauding. EVENT: the standing ovation — the whole room rises as he sings the hook. Wide shot, slight crane up. Motion never stops.",
  perf("I love spaghetti, I love spaghetti, So good so good")], LOOK))
S.append((8,(47.02,51.76),"I love pasta / I love pasta / Fork it spoon it","SINGING",[R("REF_MARCO.png")],10,
 [f"at the long communal table of a cozy Italian trattoria, {MARCO} sings at the head of the table while the adult guests around him raise their forks and spoons high like torches in rhythm, and on the last line bring fork and spoon together overhead. EVENT: forks and spoons up — the utensils rise in unison around the singing chef. Motion never stops.",
  perf("I love pasta, I love pasta, Fork it spoon it")], LOOK))
S.append((9,(51.76,57.32),"With the sauce and meatballs / Yeah yeah yeah","SINGING",[R("REF_MARCO.png")],10,
 [f"at the long communal table of a cozy Italian trattoria, {ROSA} carries in a platter stacked absurdly high with meatballs and sets it before {MARCO} as he sings; on the last line one meatball rolls off the pile and Marco catches it neatly in a small bowl while the adult guests cheer with raised hands. EVENT: the meatball catch — the rolling meatball lands in the bowl on the final line. Motion never stops.",
  perf("With the sauce and meatballs, Yeah yeah yeah")], LOOK))
S.append((10,(57.32,61.16),"Spaghetti and pasta / Delicious every day","SINGING",[R("REF_KITCHEN.png")],5,
 [f"at the stove of a cozy Italian trattoria kitchen, {MARCO} lifts a colander of freshly cooked spaghetti out of the giant pot in a burst of steam and shakes it once, steam clouding around his face as he sings both lines. EVENT: the fresh batch — the draining steam burst frames his singing face. Motion never stops.",
  perf("Spaghetti and pasta, Delicious every day")], LOOK))
S.append((11,(61.16,67.40),"Penne for the older mouths / Easy to eat that way / Sauce is so tasty","SINGING",[R("REF_MARCO.png")],10,
 [f"at a checkered table in a cozy Italian trattoria, {MARCO} gently sets a neat small plate of penne before {ELDERLY} with both hands on the first line, then straightens and sings the praise lines to the camera while the elderly guest nods delightedly. EVENT: the gentle portion — the two-handed plate pass lands softly on the first line. Motion never stops.",
  perf("Penne for the older mouths, Easy to eat that way, Sauce is so tasty")], LOOK))
S.append((12,(67.40,73.62),"Meatballs on the side / I can't get enough / Of this yumminess wide","SINGING",[R("REF_MARCO.png")],10,
 [f"at the kitchen pass of a cozy Italian trattoria, {ROSA} leads a hand-to-hand relay of small side plates of meatballs passing steadily past {MARCO} as he sings at the pass, each plate passed on the beat, his grin widening with every plate, arms spreading wide on the last line. EVENT: the side parade — the plates travel past the singing chef in a steady relay. Motion never stops.",
  perf("Meatballs on the side, I can't get enough, Of this yumminess wide")], LOOK))
S.append((13,(73.62,83.66),"Not formal with lasagna / I like it forkable / Yum with some parmesan / Spoonable for all","SINGING",[R("REF_MARCO.png")],10,
 [f"at a checkered table in a cozy Italian trattoria dining room, {ROSA} stands at the table of {COUPLE} and performs the serving twirl: she winds spaghetti onto a fork against a spoon and lays the perfect twirl onto the woman's plate on the second line, while behind her at the kitchen pass {MARCO} sings the lines to the camera. EVENT: the service twirl — Rosa's twirl lands on the plate as Marco sings. The couple watch with delight. Motion never stops.",
  perf("Not formal with lasagna, I like it forkable, Yum with some parmesan, Spoonable for all")], LOOK))
S.append((14,(83.66,89.10),"I love spaghetti / I love spaghetti / So good so good","SINGING",[R("REF_MARCO.png")],10,
 [f"at the centre aisle of a cozy Italian trattoria dining room, {MARCO} sings the chorus walking slowly down the aisle between full tables, and on the repeated line he sweeps into a theatrical bow toward the guests, rising back up still singing on the last line. EVENT: the encore bow — the bow lands mid-hook and he rises on the last line. The adult guests applaud. The camera tracks backward ahead of him. Motion never stops.",
  perf("I love spaghetti, I love spaghetti, So good so good")], LOOK))
S.append((15,(89.10,93.78),"I love pasta / I love pasta / Fork it spoon it","SINGING",[R("REF_MARCO.png")],5,
 [f"at the long communal table of a cozy Italian trattoria, {MARCO} lifts a fork from a plate of spaghetti and one long glossy strand stretches unbroken from the plate up to the fork across the first lines; on the last line a second fork joins and twists the strand. EVENT: the pasta pull — the strand stretches and holds without breaking, Marco singing behind the fork with his mouth clearly visible. Motion never stops.",
  perf("I love pasta, I love pasta, Fork it spoon it")], LOOK))
S.append((16,(93.78,99.96),"With the sauce and meatballs / Yeah yeah yeah","SINGING",[R("REF_MARCO.png")],10,
 [f"at the long communal table of a cozy Italian trattoria, {MARCO} stands over a huge shared platter of spaghetti with sauce and meatballs and showers grated parmesan from high above it, the cheese falling like snow across the lines, while the adult guests cheer with raised hands and Marco sings up into the falling cheese. EVENT: the final garnish — the parmesan snow falls over the platter as the chorus closes. Motion never stops.",
  perf("With the sauce and meatballs, Yeah yeah yeah")], LOOK))
S.append((17,(99.96,107.86),"Spaghetti / Spaghetti / So so good / Pasta pasta / Meatballs sauce / Love it all / Love it all","CUTAWAY",[R("REF_KITCHEN.png")],10,
 ["at a cozy Italian trattoria, a fast relay of close shots in one continuous flow: a mound of spaghetti lands on a plate, a fork twirls it high, the plate passes hand to hand down the counter, fresh pasta ribbons cascade from a machine, a stack of meatballs wobbles, and two pairs of hands set the finished plate down together at the centre of a checkered table. EVENT: the chant relay — the dish travels hand to hand in quick brisk stages, every handoff rhythmic. Motion never stops.",
  PERF_WORDLESS], LOOK))
S.append((18,(107.86,116.00),"","CUTAWAY",[R("REF_KITCHEN.png")],10,
 [f"at the stove of a cozy Italian trattoria kitchen, {MARCO} and {ROSA} lift one single absurdly long strand of spaghetti out of the giant pot together and carry it slowly across the whole kitchen, the strand draping over their raised arms and never breaking, both smiling with closed mouths. EVENT: the long strand — the endless strand crosses the kitchen intact. The camera tracks alongside them. Motion never stops.",
  PERF_WORDLESS], LOOK))
S.append((19,(116.00,124.24),"","CUTAWAY",[R("REF_TRATTORIA.png")],10,
 [f"at the long communal table of a cozy Italian trattoria at dusk, {ROSA} walks slowly down the table lighting tall candles one by one from a single lit taper, each flame catching in turn as the room's light warms and dims around her. EVENT: the candle pass — the flame travels candle to candle down the whole table. The camera dollies slowly alongside. Motion never stops.",
  PERF_WORDLESS], LOOK_NIGHT))
S.append((20,(124.24,128.46),"I love spaghetti / I love spaghetti","SINGING",[R("REF_MARCO.png")],5,
 [f"at the centre aisle of a cozy Italian trattoria dining room at night, every seat at every table filled with adult guests, {MARCO} strides down the aisle singing the final chorus straight to camera while the guests applaud on both sides. EVENT: the full house — the packed room applauds the singing chef down the aisle. The camera tracks backward ahead of him. Motion never stops.",
  perf("I love spaghetti, I love spaghetti")], LOOK_NIGHT))
S.append((21,(128.46,135.74),"So good so good / I love pasta / I love pasta","SINGING",[R("REF_MARCO.png")],10,
 [f"at the kitchen pass of a cozy Italian trattoria, {MARCO} presents two plates of spaghetti at once, one in each hand, arms spread wide toward the camera on the repeated lines, both plates steaming, his grin enormous. EVENT: the double plate — both plates rise together and hold as he sings. Motion never stops.",
  perf("So good so good, I love pasta, I love pasta")], LOOK))
S.append((22,(135.74,142.96),"Fork it spoon it / With the sauce and meatballs","SINGING",[R("REF_MARCO.png")],10,
 [f"at the long communal table of a cozy Italian trattoria, {ROSA} holds a huge platter crowned with a ring of meatballs high like a trophy while {MARCO} circles it slowly singing up at it; on the last line he takes the platter from her hands and lowers it to the centre of the table with a flourish. EVENT: the meatball crown — the crowned platter circles and lands centre-table. Motion never stops.",
  perf("Fork it spoon it, With the sauce and meatballs")], LOOK))
S.append((23,(142.96,151.44),"Yeah yeah yeah / Spaghetti so good / Spaghetti so good / Spaghetti so good","SINGING",[R("REF_TRATTORIA.png")],10,
 [f"at the long communal table of a cozy Italian trattoria, the whole table of adult guests, led by {MARCO} at its head, twirls forks in unison: on each repeated line every fork winds and lifts a twirl of spaghetti together, the strands rising as one, the room glowing warm. EVENT: the great twirl — the synchronized twirl peaks on the final repeated line. Marco sings the lines to the camera. Wide shot, slow push-in. Motion never stops.",
  perf("Yeah yeah yeah, Spaghetti so good, Spaghetti so good, Spaghetti so good")], LOOK))
S.append((24,(151.44,162.54),"I love spaghetti / So good so good","SINGING",[R("REF_TRATTORIA.png")],10,
 [f"at the candlelit long table of a cozy Italian trattoria at night, {MARCO} sits beside {ROSA} among the adult guests and sings the outro softly to camera, candle flames flickering between him and the lens, the whole table leaning in warm and quiet around him. EVENT: the candlelight verse — the room settles into candle glow as he sings. Slow dolly. Motion never stops.",
  perf("I love spaghetti, So good so good", soft=True)], LOOK_NIGHT))
S.append((25,(162.54,174.40),"I love spaghetti / So good so good","SINGING",[R("REF_KITCHEN.png")],10,
 [f"at the stove of a cozy Italian trattoria kitchen at night, {MARCO} returns to the giant steel pot and lifts its lid once more, steam rising around his face as he sings the last lines softly into the steam; on the final note he lowers the lid gently and rests one hand on it, smiling, the warm dining room glowing behind him. EVENT: the last lid — the lid lifts and settles in rhyme with the opening. Slow push-in. Motion never stops until the final held smile.",
  perf("I love spaghetti, So good so good", soft=True)], LOOK_NIGHT))

scenes = []
for n, win, lines, tag, refs, d, texts, look in S:
    text = texts + [look, dur(d)]
    scenes.append({"n": n, "win": list(win), "lines": lines, "tag": tag, "refs": refs, "dur": d, "text": text})
    with open(os.path.join(P, f"mv22_s{n:02d}_vehicle.txt"), "w") as f:
        f.write("\n\n".join(text) + "\n")
json.dump(scenes, open(os.path.join(P, "work/scenes.json"), "w"), indent=1)
print("wrote", len(scenes), "scenes + vehicle files")
