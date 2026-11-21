# Pose vocabulary (shared language)

## Viewpoints

Front · three-quarter · side · back · top. Name one per pose card; the
viewpoint is part of the pose, not a camera move.

## Joint language (write poses in this order)

Feet → hips → torso → arms → hands → head → gaze. Each joint gets one
plain phrase: position plus tension ("feet planted shoulder-width, weight
even", "left hand on mic, fingers loose", "chin up, eyes to camera").

## Depth layering (the depth map, in words)

Every card states three layers: NEAR (closest to camera, e.g. mic stand,
ticket in hand), MID (the character), FAR (plaza, gantry, fog, headlights).
If a layer would hide the face or the motif object, restage — that is a
pose QC fail.

## Vehicle anatomy (3-slot recipe, in order)

1. Identity block (verbatim, never changes mid-project).
2. Outfit block (verbatim, never changes mid-project).
3. Pose block (one card from the project's POSE_CARDS.md).
4. Setting.
5. Camera move (one).
6. Beat (one).

## Pose-change rule

One pose change per 10-second scene at most, stated as start → end. A scene
that needs two changes is two scenes or a restage.
