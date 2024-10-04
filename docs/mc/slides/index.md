---
title: Slides
---

!!! warning "MPF-MC is being deprecated"

    This instruction page is for the legacy MPF-MC for MPF versions 0.57 and prior. For users of MPF 0.80 and later, please refer to the [Godot Media Controller (GMC) Documentation](../../gmc/index.md)

# Slides


Now that you know what a display is, the next concept you need to
understand is "slides". Slides in MPF are just like slides in a
PowerPoint presentation or slides in an old-fashioned slide projector.

You create multiple slides (each with its own content), and then you
tell MPF when to activate certain slides. Every slide has a priority, so
if multiple slides are active at the same time, the one with the highest
priority will be shown. You can also set "transitions" which control
what visual effect is used to transition from the current slide to the
new slide. (Transitions are things like cross-fade, move in, push out,
etc.)

![image](/docs/mc/images/how_slides_work.png)

## Slide Priorities

Every slide in MPF has a priority, which is simply a numeric value.
Bigger numbers equal higher priority.

Since only one slide is shown at a time, whenever there is more than one
active slide, whichever slide has the highest priority will be the one
that's shown.

For example, you might have a general score slide at priority 100 which
shows the current player's score, the ball, the credits, and maybe the
scores of the other players.

If the player shakes the machine too hard and a tilt warning slide is
shown, then that tilt warning slide might be activated at a priority of
10,000, meaning that it would be shown instead of the general score
slide.

Then after a few seconds, the tilt warning slide might be removed, and
MPF will then show the next-highest active slide which would most likely
be the general scoring slide that was showing before.

The slide priority system is integrated into MPF's mode system, meaning
that slides created by modes automatically inherit the priority of the
mode that's showing them. Put another way, a slide from a higher
priority mode would show in place of a slide from a lower priority mode
(though every mode doesn't need to have slides). You can also tweak the
priorities of slides (higher or lower) to make sure the slide you want
to show is the one that's showing at any given time. We'll dig into
that later in the documentation.

## Slides with Multiple Displays

When MPF is used with
[multiple displays](../displays/index.md), each display maintains its own stack of active slides. The
priorities of the slides in the stack and the priority of the current
slide on one display has nothing to do with the active and current
slides of another display.

![image](/docs/mc/images/slides_with_multiple_displays.png)

* [Creating Slides](creating_slides.md)
* [Showing Slides](showing_slides.md)
* [Slide Transitions](transitions.md)

## Slides Events

These events can be useful within players. For example, if you want to
play 3 slides as a mode begins then the
[mode_(name)_started](../../events/mode_name_started.md) event can
trigger the slide_1 - but what triggers slide_2 and slide_3?

The slide_player: can be used to sequence the playing of additional
slides using the slide_slide_1_removed event to trigger the next slide
to be played.

## Related Events

* [slide_(name)_created](../../events/slide_slide_created.md)
* [slide_(name)_removed](../../events/slide_slide_removed.md)
* [slide_(name)_active](../../events/slide_slide_active.md)
