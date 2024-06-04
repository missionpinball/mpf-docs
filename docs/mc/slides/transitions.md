---
title: Slide Transitions
---

!!! warning "MPF-MC is being deprecated"

    This instruction page is for the legacy MPF-MC for MPF versions 0.57 and prior. For users of MPF 0.80 and later, please refer to the [Godot Media Controller (GMC) Documentation](../../gmc/index.md)

# Slide Transitions


When MPF switches the current slide on a display with another slide, you
can set a transition effect that controls what this slide transition
looks like. You can use these transitions with the slide_player and
within shows. You can set transitions as a property of the new slide
that comes in, or as a property of the outgoing transition when the
current slide is removed. You can also control the duration (speed) of
the transition.

Here's a list of all the types of transitions that MPF supports. Note
that if you're reading the PDF or Epub version of this documentation,
if you visit the documentation website (docs.missionpinball.org) then
this page contains animated GIFs which show each of these transitions in
action.

## none

![image](/mc/images/no_transition.gif)

Setting a transition type of `none` means that no transition will be
used, and the incoming slide instantly replaces the current slide.

## push

![image](/mc/images/push_transitions.gif)

The push transition means that the incoming slide "pushes" the
outgoing slide out of the way. (e.g. the outgoing slide moves out while
the incoming slide moves in)

Options for the push transition:

* duration: MPF
    [time string](../../config/instructions/time_strings.md) Default is 1 second.
* easing: See the
    [easing instructions](../widgets/easing.md) for details.
* direction: `left`, `right`, `up` or `down`.

## move_in

![image](/mc/images/move_in_transitions.gif)

The move in transition means that the incoming slide moves in on top of
the outgoing slide. The outgoing slide is not animated.

Options for the move_in transition:

* duration: MPF
    [time string](../../config/instructions/time_strings.md) Default is 1 second.
* easing: See the
    [easing instructions](../widgets/easing.md) for details.
* direction: `left`, `right`, `top` or `bottom`.

## move_out

Not working yet.

## wipe

![image](/mc/images/wipe_transition.gif)

The wipe transition means that the display is wiped from the outgoing
slide to the incoming one. Neither slide is animated.

Options for the wipe transition:

* duration: MPF
    [time string](../../config/instructions/time_strings.md) Default is 1 second.

## swap

![image](/mc/images/swap_transition.gif)

The swap transition similates an app screen swap like on a mobile
device. The outgoing slide moves out of the way and the incoming slide
comes in on top of it.

Options for the swap transition:

* duration: MPF
    [time string](../../config/instructions/time_strings.md) Default is 1 second.

## fade

![image](/mc/images/fade_transition.gif)

The fade transition is a classic crossfade from the outgoing slide to
the incoming one.

Options for the fade transition:

* duration: MPF
    [time string](../../config/instructions/time_strings.md) Default is 1 second.

## fade_back

![image](/mc/images/fade_back_transition.gif)

The fade_back transition causes the outgoing slide to shrink and fade
away, revealing the incoming slide.

Options for the fade_back transition:

* duration: MPF
    [time string](../../config/instructions/time_strings.md) Default is 1 second.

## rise_in

![image](/mc/images/rise_in_transition.gif)

The rise in transition causes the incoming slide to fade in and rise up
from the center of the display. It's essentially the opposite of the
fade_back transition.

Options for the rise_in transition:

* duration: MPF
    [time string](../../config/instructions/time_strings.md) Default is 1 second.

## Configuring Transitions

Transitions are specified as an additional property of a `slide_player:`
config or the `slides:` section of a show config. For example:

``` mpf-mc-config
#! slides:
#!   slide1:
#!     - type: text
#!       text: "SLIDE 1"
slide_player:
  left_ramp_hit:
    slide1:
      transition:
        type: push
        duration: 2s
        direction: right
##! test
#! post left_ramp_hit
#! advance_time_and_run .1
#! assert_text_on_top_slide "SLIDE 1"
```

Hopefully the above example is obvious by now. When the event
"left_ramp_hit" happens, MPF will show the slide called "slide1:,
using the push transition, with a transition time of 2 seconds, pushing
the new slide in from the right.

Transitions can be combined with other slide settings, like this:

``` mpf-mc-config
#! slides:
#!   slide1:
#!     - type: text
#!       text: "SLIDE 1"
slide_player:
  left_ramp_hit:
    slide1:
      transition:
        type: push
        duration: 2s
        direction: right
##! test
#! post left_ramp_hit
#! advance_time_and_run .1
#! assert_text_on_top_slide "SLIDE 1"
```

You can also configure `transition_out:` settings which are transitions
that will be applied to a slide when it is removed, like this:

``` mpf-mc-config
#! slides:
#!   slide1:
#!     - type: text
#!       text: "SLIDE 1"
slide_player:
  left_ramp_hit:
    slide1:
      transition:
        type: push
        duration: 2s
        direction: right
      transition_out:
        type: fade_back
##! test
#! post left_ramp_hit
#! advance_time_and_run .1
#! assert_text_on_top_slide "SLIDE 1"
```

!!! note

    If the current slide has a `transition_out:` setting, and the new slide
    has a `transition:` setting, then the new slide's transition setting
    will take precedence.
