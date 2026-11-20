import json, os
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STACK = os.path.join(P, "work/stills/stack")
HUSB = os.path.join(STACK, "REF_HUSBAND.png"); WIFE = os.path.join(STACK, "REF_WIFE.png")
DIN = os.path.join(STACK, "REF_DINING.png"); KIT = os.path.join(STACK, "REF_KITCHEN.png")
LOOK = ("LOOK: photorealistic live action, warm golden late-afternoon sunlight, cozy American home at Thanksgiving, "
        "plain autumn leaf garlands, shallow depth of field, real people. No text, no captions, no signs, no letters, "
        "no logos, no watermarks anywhere in the picture.")
HL = "the husband (a cheerful man in his early forties, short dark hair greying at the temples, round friendly face, clean-shaven, rust-red crewneck sweater)"
WL = "the wife (a woman in her late thirties, long dark wavy hair in a low ponytail, cream apron over a deep-green blouse)"
GUESTS = "adult family guests (an elderly couple, a tall brother in a plaid shirt, a young woman in a mustard cardigan)"
def sing(lyric, who="the husband"):
    return (f"PERFORMANCE: {who} faces the camera, mouth clearly visible and unobstructed, and SINGS the exact lyric "
            f"\"{lyric}\" — he sings \"{lyric}\" with clear open mouth shapes on every syllable and visible jaw movement, "
            f"no whispering, no mumbling. Every other visible person's mouth remains closed and still for the entire line. "
            f"All entrances, gestures and camera movement happen only before the first word or after the last word. "
            f"After the last word his mouth closes and stays closed in a clean held pose. His mouth movement follows the exact lyric.")
def dur(n=10):
    return f"Exactly {n} seconds long, wide 16:9 landscape, 1280x720."
S = []
def add(**kw): S.append(kw)

add(n=1, win=(0.00,8.10), lines="Thanksgiving is here / I'm proud of my wife", tag="SINGING", refs=[HUSB],
  text=[f"at the front door of a cozy house, the door is ALREADY swinging open and {HL} strides in mid-step carrying two full grocery bags, "
        f"beaming, while {WL} follows him in carrying a big platter. EVENT: the grand entrance — he enters mid-stride singing to camera, "
        f"and on the second line he turns and presents the wife with a sweeping proud open-arm gesture as she passes him with the platter. "
        f"The camera tracks backward ahead of them into the dining room. Motion never stops.",
        sing("Thanksgiving is here, I'm proud of my wife"), LOOK, dur(10)])
add(n=2, win=(8.10,15.96), lines="(wordless)", tag="CUTAWAY", refs=[DIN],
  text=[f"at a long wooden dining table in a cozy dining room, the table sets ITSELF with nobody touching it: empty plates slide in from the edges "
        f"and settle, glasses lift and float down into place, forks and knives glide across the wood and arrange themselves in neat rows in waves, "
        f"napkins fold themselves upright. EVENT: the self-setting table, objects sliding and assembling in sequence across the whole shot. "
        f"The camera dollies slowly along the table. Nobody is in the room. No people speak; the room is silent but for soft clinks.",
        LOOK, dur(10)])
add(n=3, win=(15.96,21.90), lines="Thanksgiving is a big day / Family comes to eat / We give thanks for the food", tag="SINGING", refs=[HUSB],
  text=[f"at the dining room doorway, {HL} stands in the foreground singing to camera while behind him {GUESTS} arrive one by one through the door — "
        f"first the elderly couple with a pie, then the tall brother ducking under the frame with a casserole, then the young woman with flowers — "
        f"each entrance a small event, coats off, hugs, the room filling up. EVENT: the cast assembles behind the singer, one arrival at a time.",
        sing("Thanksgiving is a big day, family comes to eat, we give thanks for the food"), LOOK, dur(10)])
add(n=4, win=(21.90,27.90), lines="And for the people we meet / Turkey on the table / Stuffing on the side", tag="SINGING", refs=[HUSB],
  text=[f"at the dining table, {WL} and the tall brother carry in a huge golden roast turkey on a platter between them and set it down at the exact "
        f"centre of the table, and a big bowl of stuffing slides in beside it, while {HL} sings to camera from the head of the table. "
        f"EVENT: the turkey lands centre-table on its lyric, the stuffing bowl slides in on its line. The camera pushes in slowly on the table.",
        sing("And for the people we meet, turkey on the table, stuffing on the side"), LOOK, dur(10)])
add(n=5, win=(27.90,31.58), lines="Mashed potatoes and gravy / Everything cooked just right", tag="CUTAWAY", refs=[KIT],
  text=[f"at a kitchen counter, an extreme close-up of a bowl of fluffy mashed potatoes as a ladle pours a long slow glossy cascade of brown gravy "
        f"over the top, the gravy pooling and spilling down the sides, steam rising through golden light. EVENT: one unbroken gravy pour. "
        f"No faces, hands only. Nobody speaks. The camera tilts slowly down following the pour.",
        LOOK, dur(5)])
add(n=6, win=(31.58,39.56), lines="My wife made the whole dinner / It tastes so very good / I'm so proud of her / She cooked like no one could", tag="SINGING", refs=[HUSB, WIFE],
  text=[f"at a busy home kitchen, {HL} sings to camera in the foreground while behind him {WL} works at the stove — and the kitchen appliances move "
        f"in rhythm around her: the oven door flaps gently, a stand mixer spins, pot lids nod and bounce on their pots, a kettle rocks. "
        f"EVENT: the appliances dance in rhythm while the wife cooks and the husband sings her praise. She smiles but her mouth stays closed.",
        sing("My wife made the whole dinner, it tastes so very good, I'm so proud of her, she cooked like no one could"), LOOK, dur(10)])
add(n=7, win=(39.56,48.12), lines="So proud of my wife / For this Thanksgiving feast", tag="SINGING", refs=[HUSB],
  text=[f"at the dining table mid-feast, the whole family of {GUESTS} plus {WL} are FROZEN completely still mid-gesture — forks halted in the air, "
        f"a glass tilted mid-pour, mouths open mid-laugh, nobody moves at all — while {HL} alone moves, weaving and stepping between the frozen "
        f"figures around the table, singing to camera. EVENT: the freeze — only the singer moves through the statue-still family.",
        sing("So proud of my wife, for this Thanksgiving feast"), LOOK, dur(10)])
add(n=8, win=(48.12,55.98), lines="The turkey is not the only thing / Being stuffed tonight", tag="SINGING", refs=[HUSB],
  text=[f"at the head of the dining table with the big roast turkey on its platter right in front of him, {HL} sings the hook straight to camera "
        f"with a huge proud grin, and on the word 'stuffed' he leans back in his chair and pats his own full round belly twice, delighted with "
        f"himself, while {WL} beside him rolls her eyes fondly with her mouth closed. EVENT: the lyric acted out — the belly pat lands exactly on 'stuffed'.",
        sing("The turkey is not the only thing being stuffed tonight"), LOOK, dur(10)])
add(n=9, win=(55.98,63.86), lines="So proud of my wife / For this Thanksgiving feast", tag="SINGING", refs=[WIFE, HUSB],
  text=[f"at the kitchen doorway, {WL} carries the big roast turkey on its platter through the room at a steady unstoppable walk — guests step aside, "
        f"a chair is whisked out of her path, a door is held — nothing slows her down, while {HL} walks backward in front of her singing to camera, "
        f"gesturing at her like a prize. EVENT: the unstoppable procession — the wife and the turkey advance through the whole room.",
        sing("So proud of my wife, for this Thanksgiving feast"), LOOK, dur(10)])
add(n=10, win=(63.86,72.90), lines="The turkey is not the only thing / Being stuffed tonight", tag="SINGING", refs=[HUSB],
  text=[f"at a long dining table loaded with the feast, serving dishes travel hand-to-hand down the whole table in a continuous wave — a bowl of "
        f"stuffing passes, a gravy boat passes, a dish of potatoes passes, hand to hand to hand — while {HL} stands at the head of the table "
        f"singing to camera, conducting the cascade with open arms. EVENT: the dish cascade passes down the table for the whole shot. "
        f"The camera tracks sideways along the table.",
        sing("The turkey is not the only thing being stuffed tonight"), LOOK, dur(10)])
add(n=11, win=(72.90,79.24), lines="Cranberry sauce is sweet / The pie is warm and nice / Everyone is happy", tag="SINGING", refs=[HUSB],
  text=[f"at a kitchen counter, a close shot of a jellied cranberry sauce standing on a plate in its perfect can shape — and it WOBBLES endlessly, "
        f"quivering and jiggling without ever settling, beside a steaming warm pie, while {HL} leans in beside the counter singing to camera, "
        f"amused by the wobble. EVENT: the impossible cranberry sauce never stops wobbling for the whole shot.",
        sing("Cranberry sauce is sweet, the pie is warm and nice, everyone is happy"), LOOK, dur(10)])
add(n=12, win=(79.24,88.74), lines="Eating more than twice / The table is so full / The food is all so good / My wife did all the work / She cooked just like she should", tag="SINGING", refs=[HUSB],
  text=[f"at the dining table crammed edge-to-edge with dishes, {HL} sings to camera from his seat while the toast travels around the table like a "
        f"wave: first the tall brother raises his glass, then the young woman raises hers, then the elderly couple, then {WL} last and highest — "
        f"one by one in sequence until every glass is up. EVENT: the join-in toast wave circles the table. Everyone's mouth stays closed but his.",
        sing("Eating more than twice, the table is so full, the food is all so good, my wife did all the work, she cooked just like she should"), LOOK, dur(10)])
add(n=13, win=(88.74,96.92), lines="My wife made the whole dinner / It tastes so very good / I'm so proud of her / She cooked like no one could", tag="SINGING", refs=[HUSB, WIFE],
  text=[f"at the dining table, the role reversal: {WL} finally sits down in the place of honour, tired and smiling, while {HL} stands beside her "
        f"carving the roast turkey and serving her the first big slice onto her plate, singing to camera as he carves. EVENT: the husband carves and "
        f"serves the wife first. The slicing motion runs through the shot; she does not speak.",
        sing("My wife made the whole dinner, it tastes so very good, I'm so proud of her, she cooked like no one could"), LOOK, dur(10)])
add(n=14, win=(97.62,105.66), lines="So proud of my wife / For this Thanksgiving feast", tag="SINGING", refs=[HUSB],
  text=[f"at the dining room, on each beat the family strikes a bold proud pose and holds it — the brother flexes, the young woman strikes a runway "
        f"pose, the elderly couple strike a ballroom pose, {WL} strikes a chef's proud arms-crossed pose at the centre — pose after pose around her, "
        f"while {HL} sings to camera from the front. EVENT: the pose-strike chain — a new frozen pose lands on every beat around the wife.",
        sing("So proud of my wife, for this Thanksgiving feast"), LOOK, dur(10)])
add(n=15, win=(105.66,113.02), lines="The turkey is not the only thing / Being stuffed tonight", tag="SINGING", refs=[HUSB],
  text=[f"at the dining table after the feast, {HL} sings the hook to camera deadpan-proud from his chair while around him the {GUESTS} slump back "
        f"in their chairs on the word 'stuffed', loosening their belts one notch and fanning themselves, laughing with full bellies. "
        f"EVENT: the belt-loosen — every guest slumps and loosens a belt exactly on 'stuffed'. Their mouths stay closed; only he sings.",
        sing("The turkey is not the only thing being stuffed tonight"), LOOK, dur(10)])
add(n=16, win=(113.02,121.40), lines="So proud of my wife / So proud of my wife / For this Thanksgiving feast", tag="SINGING", refs=[HUSB],
  text=[f"at the dining room seen from a high wide angle, the whole family suddenly scatters from the table in every direction — to the kitchen, to "
        f"the sideboard, to the counter — and streams back carrying desserts, reforming in a ring around a big pie placed at the centre of the table, "
        f"while {HL} sings to camera from the middle of the swirl. EVENT: scatter and reform — the family bursts outward and regroups around the pie.",
        sing("So proud of my wife, so proud of my wife, for this Thanksgiving feast"), LOOK, dur(10)])
add(n=17, win=(121.40,130.14), lines="The turkey is not the only thing / Being stuffed tonight", tag="SINGING", refs=[HUSB],
  text=[f"at the kitchen pass, {HL} walks slowly toward camera singing, calm and proud and unbothered in the foreground, while BEHIND him the "
        f"kitchen erupts in cheerful chaos — a tower of dirty plates wobbles higher and higher, a gravy boat tips and is caught, the brother juggles "
        f"two serving bowls, the young woman ducks a swinging pot lid. EVENT: chaos behind, calm in front — he never looks back. Only he sings.",
        sing("The turkey is not the only thing being stuffed tonight"), LOOK, dur(10)])
add(n=18, win=(130.14,137.54), lines="Thanksgiving / Family meal / Turkey good / Stuffing good", tag="CUTAWAY", refs=[DIN],
  text=[f"at a Thanksgiving table, a fast rhythmic visual roll call in one sweeping take: the camera whips across the whole laden table, dives in on "
        f"the family mid-meal laughing and eating, punches into an extreme close-up of the golden roast turkey glistening, then whips to a close-up "
        f"of a heaped bowl of stuffing with steam rising — each item hit in quick succession like a chant. Nobody sings; mouths closed or chewing. "
        f"Pure food-and-family montage energy, constant motion.",
        LOOK, dur(10)])
add(n=19, win=(137.54,143.38), lines="So proud / So proud", tag="SINGING", refs=[HUSB, WIFE],
  text=[f"at the dining room, {HL} and {WL} stand side by side at the centre singing the chant straight to camera together, arms around each other's "
        f"shoulders, while the {GUESTS} gather in behind them step by step until the frame is completely full of family, everyone smiling at camera. "
        f"EVENT: the group swell — the frame fills with family behind the singing pair. The camera pushes in slowly. Only the pair sing; the guests' mouths stay closed.",
        "PERFORMANCE: the husband and the wife face the camera side by side, mouths clearly visible, and SING the chant \"So proud, so proud\" together — they sing \"So proud, so proud\" with clear open mouth shapes and visible jaw movement. Every guest's mouth remains closed and still. After the last word their mouths close into warm smiles. Their mouth movement follows the exact chant.", LOOK, dur(10)])
add(n=20, win=(143.38,151.28), lines="So proud of my wife / For this Thanksgiving feast", tag="SINGING", refs=[HUSB, WIFE],
  text=[f"at the dining room, the whole family stands in a dense group with their backs partly to camera — then on a beat the group PARTS down the "
        f"middle like water, revealing {WL} standing alone in the cleared lane in golden light, holding a big pie up at chest height like a trophy, "
        f"while {HL} sings to camera from the front corner. EVENT: the parting — the crowd splits and the wife is revealed holding the pie.",
        sing("So proud of my wife, for this Thanksgiving feast"), LOOK, dur(10)])
add(n=21, win=(151.28,159.02), lines="The turkey is not the only thing / Being stuffed tonight", tag="SINGING", refs=[WIFE, HUSB],
  text=[f"at the dining table shot from a low angle, {WL} hoists the whole golden roast turkey on its platter high overhead with both arms like a "
        f"championship trophy while the family cheers silently around her, arms up, and {HL} below sings the hook up toward it, ecstatic. "
        f"EVENT: the trophy lift — the turkey is raised overhead and held aloft for the hook. Only the husband sings; all other mouths closed.",
        sing("The turkey is not the only thing being stuffed tonight"), LOOK, dur(10)])
add(n=22, win=(159.58,168.56), lines="So proud of my wife / For this Thanksgiving feast", tag="SINGING", refs=[HUSB],
  text=[f"at the dining room, {HL} sings to camera at the table while the whole family tosses cloth napkins high into the air around him — dozens of "
        f"napkins swarm up, flutter and rain slowly down over the table and the singer like soft snow for the rest of the shot. EVENT: the napkin "
        f"swarm — napkins fill the air and fall for the whole chorus. Only he sings.",
        sing("So proud of my wife, for this Thanksgiving feast"), LOOK, dur(10)])
add(n=23, win=(168.56,179.00), lines="The turkey is not the only thing / Being stuffed tonight / Being stuffed tonight", tag="SINGING", refs=[HUSB],
  text=[f"at the dining table at the peak of the feast, the whole table ERUPTS: every guest raises a glass at once, laughing, cheering silently, "
        f"dishes everywhere, the turkey centre-frame, while {HL} stands at the head of the table arms flung wide singing the final hook at full "
        f"blast to camera. EVENT: the feast peak — the celebration detonates around the standing singer. Only he sings; the camera pushes in slowly.",
        sing("The turkey is not the only thing being stuffed tonight, being stuffed tonight"), LOOK, dur(10)])
add(n=24, win=(179.00,188.00), lines="(settle; singing starts 181.62) So proud of my wife", tag="SINGING", refs=[HUSB, WIFE],
  text=[f"at the dining table in the evening, the light has dimmed to warm candlelight and lamplight over the conquered feast — picked-clean dishes, "
        f"the turkey bones on the platter — {HL} and {WL} slumped happily side by side among the leftovers, and he sings softly to camera, tired "
        f"and content. EVENT: the evening settles over the finished feast. The camera dollies out very slowly. Only he sings, gently.",
        sing("So proud of my wife"), LOOK, dur(10)])
add(n=25, win=(188.00,196.00), lines="Thanksgiving is good / (tail)", tag="SINGING", refs=[HUSB, WIFE],
  text=[f"at the candlelit dining table, a closer two-shot of {HL} and {WL} leaning against each other among the leftovers, completely content; he "
        f"sings the last line softly to camera, she rests her head toward his shoulder with her mouth closed, and they end in a warm held smile as "
        f"the light dims a touch more. EVENT: the quiet button — the final line lands and the feast rests. Only he sings.",
        sing("Thanksgiving is good"), LOOK, dur(10)])

for s in S:
    fn = os.path.join(P, f"mv25_s{s['n']:02d}_vehicle.txt")
    with open(fn, "w") as f:
        f.write("\n\n".join(s["text"]))
    s["vehicle"] = fn
with open(os.path.join(P, "work/scenes.json"), "w") as f:
    json.dump(S, f, indent=1)
print("vehicles:", len(S))
