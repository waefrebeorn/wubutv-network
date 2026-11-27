import json, os
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STACK = os.path.join(P, "work/stills/stack")
RANCH = os.path.join(STACK, "REF_RANCH.png")
TILLY = os.path.join(STACK, "REF_TILLY.png")
SHOP = os.path.join(STACK, "REF_SHOP.png")
BOARD = os.path.join(STACK, "REF_BOARDWALK.png")

R = "Ranch, a flamboyant dandy cowboy tailor in his mid-thirties, slicked dark hair with a wave, thin pencil moustache, cream fringed western suit, turquoise bolo tie, polished tan cowboy boots and a cream Stetson hat"
T = "Tilly, a seamstress in her fifties, auburn hair in a victory roll, teal blouse, yellow measuring tape draped around her neck"
H = "Hank, a burly adult man in his fifties with a grey beard and a brown work shirt"
PE = "Pearl, an adult woman in her early thirties with dark hair in a ponytail, wearing a red polka-dot dress"
C = "Cole, a lean adult man in his early forties in a denim jacket and dark jeans"
LOOK = ("LOOK: photorealistic live action, warm golden afternoon light, vintage western tailor shop, "
        "wooden floors, long red carpet runner, three-panel mirror wall, hat racks and boot shelves, "
        "shallow depth of field, real people. No text, no captions, no subtitles, no signs, no letters, "
        "no logos, no watermarks anywhere in the picture.")

def perf(who, name, lyric):
    return (f"PERFORMANCE: {name} faces the camera, mouth clearly visible and unobstructed, and SINGS the exact lyric "
            f"\"{lyric}\" — he sings \"{lyric}\" clearly with clear open mouth shapes on every syllable and visible jaw "
            f"movement, no whispering, no mumbling. Every other visible person's mouth remains closed and still for the "
            f"entire line. All entrances, gestures and camera movement happen only before the first word or after the last "
            f"word. After the last word his mouth closes and stays closed in a clean held pose. His mouth movement follows "
            f"the exact lyric.")

def scene(n, win, lines, tag, dur, refs, text0, lyric=None):
    parts = [text0]
    if tag == "CUTAWAY":
        parts.append("PERFORMANCE: nobody sings in this scene; every visible person's mouth remains closed and still throughout. Motion never stops.")
    else:
        parts.append(perf(None, "Ranch", lyric))
    parts.append(LOOK)
    parts.append(f"Exactly {dur} seconds long, in exactly 16:9 aspect ratio (landscape), 1280x720.")
    return {"n": n, "win": win, "lines": lines, "tag": tag, "refs": refs, "dur": dur, "text": parts}

SCENES = [
 scene(1, [0.00, 8.56], "Call me Ranch / I be dressin' / I be dressin' / I'm the best / Yeah", "SINGING", 10, [RANCH],
   f"at a sunlit vintage western tailor shop, {R} is ALREADY mid-stride down the long red carpet runner toward the camera at the very first frame, tipping his cream Stetson hat toward the camera with a grin as he strides and sings the opening lines, fringe swinging with every step. EVENT: the hat-tip entrance — he tips the hat on the first line and keeps striding, owning the room. The camera tracks backward ahead of him. Motion never stops.",
   "Call me Ranch, I be dressin', I be dressin', I'm the best, Yeah"),
 scene(2, [8.56, 18.70], "Call me Ranch / Cause I be dressin' / I be dressin'", "SINGING", 10, [RANCH],
   f"at the three-panel mirror wall of a vintage western tailor shop, {R} turns from the first mirror panel to the second to the third as he sings, straightening his turquoise bolo tie at the first panel, flicking a cuff at the second, and admiring the full outfit at the third, then keeps preening and turning in the mirrors after the lines end. EVENT: the triple mirror check — a new adjustment at each mirror panel on each line. The camera drifts slowly sideways. Motion never stops.",
   "Call me Ranch, Cause I be dressin', I be dressin'"),
 scene(3, [18.70, 24.98], "I'm the best at everything / Better than you, that's the thing", "SINGING", 10, [RANCH],
   f"at the fitting platform of a vintage western tailor shop, {T} stretches her yellow measuring tape across the chest of {R}, who stands tall on the platform puffing his chest out proudly as he sings, and the tape snaps taut on the last line. EVENT: the tape measure flourish — the tape stretches wider and wider until it snaps taut. Medium shot. Motion never stops.",
   "I'm the best at everything, Better than you, that's the thing"),
 scene(4, [24.98, 29.86], "I win every time I try / You can watch, but you can't fly", "SINGING", 5, [RANCH],
   f"at a wooden wall inside a vintage western tailor shop already covered with dozens of plain blue award ribbons, {R} pins one more blue ribbon onto the wall as he sings and pats it flat with satisfaction on the last line. EVENT: the ribbon pin — one more ribbon joins the wall of wins. Medium close shot. Motion never stops.",
   "I win every time I try, You can watch, but you can't fly"),
 scene(5, [29.86, 34.82], "Money, style, and the skill / I got more, you got the bill", "SINGING", 5, [RANCH],
   f"at the wooden counter of a vintage western tailor shop, the drawer of a brass vintage cash register pops open beside {R} as he sings; he lifts a thick fan of paper bills from the drawer, fans them once with a grin, and tucks them neatly away on the last line. EVENT: the register pop — the drawer springs open and the bills fan out. Medium close shot. Motion never stops.",
   "Money, style, and the skill, I got more, you got the bill"),
 scene(6, [34.82, 39.84], "I stay winning every day / You just talk, I get paid", "SINGING", 5, [RANCH],
   f"at a big plain wall calendar inside a vintage western tailor shop, every visible day marked only with a gold star sticker and no writing, {R} flips the calendar pages forward one after another as he sings, pages fluttering, landing on a fresh page on the last line. EVENT: the calendar flip — page after page of gold stars flips past. Medium shot. Motion never stops.",
   "I stay winning every day, You just talk, I get paid"),
 scene(7, [39.84, 49.58], "You can try, you can try / I stay higher, I stay high / You can try, you can try / I stay higher, that's no lie", "SINGING", 10, [RANCH],
   f"at a tall wooden hat rack inside a vintage western tailor shop, {H} and {C} take turns tossing their cowboy hats toward the rack's pegs and missing, hats bouncing off, while {R} leans against the counter singing without a care, and on the last line he tosses his own cream Stetson without looking and it lands perfectly on the top peg. EVENT: the hat-toss challenge — the others miss, Ranch lands his blind. Wide medium shot. Motion never stops.",
   "You can try, you can try, I stay higher, I stay high, You can try, you can try, I stay higher, that's no lie"),
 scene(8, [49.58, 57.04], "Call me Ranch cause I be dressin' / I'm the best, no stressin' / Better than you, no question", "SINGING", 10, [RANCH],
   f"at the long red carpet runner of a vintage western tailor shop, {R} struts the full length of the runner toward the camera as he sings the chorus, fringe swinging, shoulders rolling, while {T}, {H}, {PE} and {C} line the sides clapping along with closed smiling mouths. EVENT: the first strut — a full runway strut down the red runner on the hook. The camera tracks backward ahead of him. Motion never stops.",
   "Call me Ranch cause I be dressin', I'm the best, no stressin', Better than you, no question"),
 scene(9, [57.04, 64.60], "Call me Ranch cause I be dressin' / Call me Ranch cause I be dressin' / I'm the best, no stressin'", "SINGING", 10, [RANCH],
   f"at a boot bench inside a vintage western tailor shop, {R} sits tall like a king with one polished tan boot propped up while {C} kneels buffing the boot with a brush in fast strokes, and {R} sings the hook leaning back smugly; the brush gives a final pop and the boot gleams on the last line. EVENT: the boot-shine pop — the buffing builds until the boot shines. Medium shot. Motion never stops.",
   "Call me Ranch cause I be dressin', Call me Ranch cause I be dressin', I'm the best, no stressin'"),
 scene(10, [64.60, 70.92], "Better than you, no question / Call me Ranch cause I be dressin'", "SINGING", 10, [RANCH],
   f"at the fitting platform of a vintage western tailor shop, {R} sings while he whips his cream fringed jacket off one shoulder, spins once, and flips the jacket back on in one fluid motion on the last line, fringe flying. EVENT: the jacket flip — off the shoulder, spin, back on, all in one move. Medium shot. Motion never stops.",
   "Better than you, no question, Call me Ranch cause I be dressin'"),
 scene(11, [70.92, 77.66], "I rap better, I look better / I work harder, I get wetter / Every room I walk inside", "SINGING", 10, [BOARD],
   f"at the saloon swing doors of a vintage western tailor shop on a wooden boardwalk, {R} pushes through the swing doors mid-stride singing, doors swinging behind him, and every adult head inside the shop turns to look at him on the last line. EVENT: the doorway entrance — the doors burst open and the whole room turns. Wide shot. Motion never stops.",
   "I rap better, I look better, I work harder, I get wetter, Every room I walk inside"),
 scene(12, [77.66, 85.00], "People stop and take my side / You can hate, I don't care / I got sauce, I got flair", "SINGING", 10, [RANCH],
   f"at the sewing counter of a vintage western tailor shop, {R} sets a small glass bottle spinning flat on the wooden counter like a trick shot as he sings, the bottle whirling between spools of thread, and he catches it upright in one hand on the last line without spilling a drop. EVENT: the bottle spin — a long flat spin caught clean. Medium close shot. Motion never stops.",
   "People stop and take my side, You can hate, I don't care, I got sauce, I got flair"),
 scene(13, [85.00, 90.02], "I stay dressed, I stay ready / You stay late, I stay steady", "SINGING", 5, [RANCH],
   f"at the mirror wall of a vintage western tailor shop, a close shot of {R} snapping both of his cufflinks shut one after the other and straightening his turquoise bolo tie as he sings, chin up, checking the mirror on the last line. EVENT: the cufflink snap — both cuffs snap shut in rhythm. Close shot. Motion never stops.",
   "I stay dressed, I stay ready, You stay late, I stay steady"),
 scene(14, [90.02, 101.00], "You can try, you can try / I stay higher, I stay high / You can try, you can try / I stay higher, that's no lie", "SINGING", 10, [SHOP],
   f"at the wooden staircase of a vintage western tailor shop, {R} climbs the stairs step by step as he sings the pre-chorus, rising above the shop floor, and on the last line he reaches the mezzanine balcony and looks down over the rail with a grin, holding the look after the line ends. EVENT: the staircase rise — every line takes him higher. Low angle, camera tilting up. Motion never stops.",
   "You can try, you can try, I stay higher, I stay high, You can try, you can try, I stay higher, that's no lie"),
 scene(15, [101.00, 108.54], "Call me Ranch cause I be dressin' / I'm the best, no stressin' / Better than you, no question", "SINGING", 10, [RANCH],
   f"at the long red carpet runner of a vintage western tailor shop, {PE} and {C} strut down the runner in brand-new tailored outfits, smiling with closed mouths, while {R} sings the chorus leaning over the mezzanine balcony rail above them. EVENT: the double strut — two fresh outfits take the runway under his singing. Wide shot. Motion never stops.",
   "Call me Ranch cause I be dressin', I'm the best, no stressin', Better than you, no question"),
 scene(16, [108.54, 115.72], "Call me Ranch cause I be dressin' / Call me Ranch cause I be dressin' / I'm the best, no stressin'", "SINGING", 10, [RANCH],
   f"at the open floor of a vintage western tailor shop, {R} dances in place as he sings the hook, bouncing on the beat so the long fringe of his cream jacket shakes and shimmers, and he spins once on the repeated line. EVENT: the fringe shake — the whole jacket dances with him. Medium shot. Motion never stops.",
   "Call me Ranch cause I be dressin', Call me Ranch cause I be dressin', I'm the best, no stressin'"),
 scene(17, [115.72, 122.04], "Better than you, no question / Call me Ranch cause I be dressin'", "SINGING", 10, [RANCH],
   f"at the open floor of a vintage western tailor shop, a line of adults — {T}, {H}, {PE} and {C} — strike a proud pose one after another in sequence with closed smiling mouths, and {R} strikes the last and biggest pose as he sings the final hook line. EVENT: the pose chain — pose after pose down the line, Ranch biggest. The camera pans sideways along the line. Motion never stops.",
   "Better than you, no question, Call me Ranch cause I be dressin'"),
 scene(18, [122.04, 131.88], "", "CUTAWAY", 10, [SHOP],
   f"at a vintage western tailor shop, a fast relay of close shots in one continuous flow: a cream Stetson hat lands on a smiling man's head, a turquoise bolo tie knot slides tight, polished tan cowboy boots stomp down a red carpet runner, a man winks at his reflection in a tall mirror, a cream fringed jacket is shrugged onto shoulders, a silver belt buckle flashes in sunlight, and the man grins straight at the camera. EVENT: the dressin' relay — the outfit assembles piece by piece in quick brisk stages. Motion never stops."),
 scene(19, [131.88, 142.82], "Call me Ranch cause I be dressin'", "SINGING", 10, [RANCH],
   f"at the big front window of a vintage western tailor shop flooded with golden late-afternoon light, {R} sings the long final-chorus hook facing the camera, silhouetted fringe glowing at the edges, and after the line he slowly turns from the window to reveal the whole shop behind him dressed up and celebrating. EVENT: the golden window — the peak line sung in a flood of golden light, then the turn reveals the room. The camera pushes in slowly. Motion never stops.",
   "Call me Ranch cause I be dressin'"),
 scene(20, [142.82, 150.04], "I'm the best, no stressin' / Better than you, no question / Call me Ranch cause I be dressin'", "SINGING", 10, [RANCH],
   f"at the open floor of a vintage western tailor shop, {T}, {H}, {PE} and {C} toss their cowboy hats high into the air in celebration, hats raining down everywhere, while {R} sings the hook in the middle of it and catches his own cream Stetson out of the air on the last line. EVENT: the hat rain — a sky full of hats, and Ranch catches his. Wide shot. Motion never stops.",
   "I'm the best, no stressin', Better than you, no question, Call me Ranch cause I be dressin'"),
 scene(21, [150.04, 157.60], "Call me Ranch cause I be dressin' / I'm the best, no stressin' / Better than you, no question", "SINGING", 10, [RANCH],
   f"at the long red carpet runner of a vintage western tailor shop, the whole shop struts down the runner in a line — {R} at its head singing the hook, {T}, {PE}, {H} and {C} strutting behind him in their best outfits with closed smiling mouths, fringe and polka dots swinging. EVENT: the final strut — the entire shop takes the runway together. The camera tracks backward ahead of them. Motion never stops.",
   "Call me Ranch cause I be dressin', I'm the best, no stressin', Better than you, no question"),
 scene(22, [157.60, 163.24], "Call me Ranch cause I be dressin' / One more time / Call me Ranch", "SINGING", 5, [RANCH],
   f"at the open floor of a vintage western tailor shop, {R} sings the hook, and on the words 'one more time' he sweeps into a deep theatrical bow, hat swept low, then rises grinning straight into the last short line. EVENT: the encore bow — a full bow and a grin on the rise. Medium shot. Motion never stops.",
   "Call me Ranch cause I be dressin', One more time, Call me Ranch"),
 scene(23, [163.24, 170.74], "I be dressin' / I'm the best / Yeah", "SINGING", 10, [TILLY],
   f"at the sewing table of a vintage western tailor shop, {T} pins a final stitch into the cuff of {R}, who sits beside her singing softly, and he gives a small wink on the last word. EVENT: the last stitch — one final pin completes the outfit. Medium two-shot. Motion never stops.",
   "I be dressin', I'm the best, Yeah"),
 scene(24, [170.74, 176.80], "Call me Ranch / Cause I be dressin'", "SINGING", 10, [RANCH],
   f"at the front door of a vintage western tailor shop in warm evening light, {R} sings the last lines softly as he hangs his cream Stetson hat back on its peg beside the door, tips the brim once toward the camera, and steps back smiling; the shot ends held on the hat resting on its peg. EVENT: the hat on the peg — the hat comes home and the day is done. The camera pushes in slowly. Motion never stops.",
   "Call me Ranch, Cause I be dressin'"),
]

json.dump(SCENES, open(os.path.join(P, "work/scenes.json"), "w"), indent=1)
for s in SCENES:
    with open(os.path.join(P, f"mv23_s{s['n']:02d}_vehicle.txt"), "w") as f:
        f.write("\n\n".join(s["text"]) + "\n")
print("scenes:", len(SCENES), "vehicles written")
