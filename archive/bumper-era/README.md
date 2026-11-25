# The Bumper Era — archive label

**Era:** the WuBuTV single-scene bumper run, ~10-second units, one subject each,
~ WuBu ~ corner bug, deadpan house grammar.

**Closed:** by the owner's decree of 2026-10-21T01:12:09Z (2026-10-20 21:12 EDT):
"you are done with this era of the wubutv — this bumper era needs to be labeled
into a archive folder as we need to move into coherent media."
The bumper factory (wubutv-bumper-factory) was disabled on that decree.

**Final count:** 1,188 bumpers shipped (tracked goal state, goal_de7ce8f13764).
1,153 finished mp4s remain live in `bumpers/` (2.6G).

**Why the mp4s stay in `bumpers/`:** the Hugging Face CDN manifest pins them at
their current `bumpers/<file>` paths. Physically moving 1,153 files would break
1,153 public CDN URLs and force a 2.6G re-upload under new paths. The archive
is this paper trail, not a file move. (If the owner ever orders the physical
move anyway, it must be scoped with a manifest rebuild + HF re-upload.)

**What lives on:** 1-minute (E1M) and 2-minute (E2M) episode assembly continue
from catalogue units per the same decree; the era is over, the network isn't.

See `ERA_CLOSE_DECREE.md` for the decree verbatim.
