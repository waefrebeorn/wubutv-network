# 03 — AI video prompting

Source: https://slop.cc/wiki/ai-video-prompting (updated 2026-09-30).
Related index entries not read in full this run: camera movement prompts,
negative prompts, shot list, storyboarding.

## The rules [confirmed]

- "A useful prompt identifies what the viewer should see change. Treat the
  result as a take to evaluate: precise language improves direction, but it
  does not guarantee timing, identity, or physical accuracy."
- One readable event: "Start with the subject and a visible verb. A mechanic
  closes a toolbox is easier to assess than a mechanic realizes her whole life
  must change. Translate the larger story into posture, gaze, movement, or a
  change in the environment."
- Give setting, framing, and camera each a job: "a close view makes the latch
  readable; a locked camera keeps attention on the hands." Avoid "style
  adjectives that compete with the central action."
- "Begin with one shot and one main event. A clip that must contain an
  entrance, a conversation, a chase, and a sunset has several opportunities to
  lose the story. Plan those as separate shots first; combine actions only
  after you know the chosen workflow can handle them."
- Separate inputs: "A starting image, a character reference, and a style
  reference serve different purposes. Label those roles in your production
  notes." With an established starting frame, "concentrate the motion prompt
  on what changes from that frame."
- Audio direction separate from visible action: "Write audio direction
  separately from visible action. If the model supports generated sound,
  specify a simple sound bed or a clearly assigned line. Otherwise, use the
  same audio note during editing. A request for silent visuals cannot by itself
  guarantee that a service returns a file without audio."
- Iterate one factor at a time: "Keep a baseline prompt and compare a small
  number of deliberate variations. Change one uncertain factor, such as
  movement speed, while retaining the accepted subject and composition.
  Review the whole clip at normal speed, then inspect the failure point. Save
  useful takes before trying a more ambitious version."
- The guide's example direction (mechanic, red toolbox, both hands, palms rest
  on lid, fixed camera at bench height, soft window light left, toolbox fully
  in frame; audio note: one lid click + quiet workshop room tone) works
  because it "gives the clip one testable event, defines its endpoint, and
  assigns the camera a simple behavior."
- Common mistakes: several scenes before one shot works; emotional abstractions
  without visible behavior; changing prompt, references, and settings together
  and then guessing which change helped.

## WuBu mapping

This guide is the theoretical backing for three engine rules: one event per
scene (the timeline guide's "then more than once = two scenes" is the same rule
from the plan side), one named axis per reroll, and keep-hits (save useful
takes before trying a more ambitious version). The "audio direction separate"
rule is why our vehicles carry a SFX note distinct from the visible action —
and why a silent-visuals request is never trusted as a guarantee.
