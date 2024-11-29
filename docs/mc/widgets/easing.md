---
title: Easing Instructions
---

# Easing Instructions


MPF has the ability to use "easing" functions to adjust the
acceleration and deceleration of motions associated with
[slide transitions](../slides/transitions.md) and
[widget animations](animation.md).

An easing function is a formula that calculates a progress value based
on an input value.

Let's look at a simple (but not realistic) example of animating a
widget that moves 10 pixels in 10 seconds. With no easing function
applied, it would have moved 1 pixel after 1 second, 2 pixels after 2
seconds, etc.

At first you might think this seems fine, but to the viewer it will not
look natural because it will instantly start moving at full speed, and
then it will stop suddenly when it gets to the end. A more natural
approach would be to have it accelerate slowly at the beginning and then
to decelerate as it approaches the end.

All animation and transition functions in MPF change a value over a
certain amount of time. (Move 50 pixels in 2 seconds, change the opacity
from 100% to 50% in 500ms, etc.)

We can illustrate this with a graph, where time is the X axis, and the
value is the Y axis, like this:

![image](/docs/mc/images/easing_explained.png)

The image above shows the default formula with no easing applied. (This
is technically the "linear" easing function.) The value of the
function is directly related to the time, and the speed of change is the
same at the beginning and end.

But what if we wanted our animation to start slow and accelerate, then
slow down again towards the end? For that, we could use a formula like
this:

![image](/docs/mc/images/anim_in_out_sine.png)

Notice that at the beginning (in the lower left corner), as you move
right, the red line doesn't change too much. Then towards the middle,
the red line changes more as the transition speeds up, and then at the
end (towards the upper right), the line changes more slowly.

Here's an animated GIF which shows five different easing functions
applied to animate text moving left and right.

Don't worry about the function names. We'll cover those in a bit.

![image](/docs/mc/images/easing.gif)

!!! note

    If you're viewing the PDF version of these docs, you won't see the
    GIFs since they're animated. You can view the docs online to see them.

Note that the move to the left and the move to the right are two
separate animations, meaning the a single movement left or right is
showing the same easing function used in both directions.

If you're curious about the MPF config used to create this animated
GIF, we've posted it [here](easing_config.md).

You can also imagine how an easing formula would look if you wanted
something to start slow, but then speed up without slowing down again.
(This might be useful if you want a widget to move off screen since it
will have a gentle start and then it will shoot off and get faster and
faster.) That function might look like this:

![image](/docs/mc/images/anim_in_quart.png)

Conversely, if you have a widget coming in from off screen, you might
want it to start out fast and then slow down as it approaches its final
location. For that you could use what's essentially the opposite of the
previous formula, like this:

![image](/docs/mc/images/anim_out_quad.png)

The important thing to remember with these easing formulas is that the
red line does NOT represent the path the moving objects take, rather, it
represents how the progress of the change happens over time.

## Where can you apply easing?

In MPF, these easing functions are used in two places:

* For widget animations, to affect how the progress of an animated
    property progresses over time.
* For some (not all) slide transitions, to affect the progress of the
    transition over time.

Remember when you're animating a widget, you can animate ANY numerical
property. So this can include the x/y position on the display, but it
can also include the size, scale, and/or the opacity (transparency).

Here's an animated GIF showing the same five easing functions applied
to each text widget's opacity property (cycling them between 1 and 0):

![image](/docs/mc/images/easing_opacity.gif)

Refer to the
[slide transition](../slides/transitions.md) and
[widget animation](animation.md) documentation for details on how to actually apply these
easing functions. It's pretty straightforward---essentially you just
add `easing: <function_name>` to the animation or transition property,
like `easing: in_out_circ`.

Now lets look at the different types of easing functions MPF supports:

## Easing "start" functions

The following functions apply an easing formula at the beginning of the
time and then accelerate to the end:

`easing: in_back`

![image](/docs/mc/images/anim_in_back.png)

`easing: in_bounce`

![image](/docs/mc/images/anim_in_bounce.png)

`easing: in_circ`

![image](/docs/mc/images/anim_in_circ.png)

`easing: in_cubic`

![image](/docs/mc/images/anim_in_cubic.png)

`easing: in_elastic`

![image](/docs/mc/images/anim_in_elastic.png)

`easing: in_expo`

![image](/docs/mc/images/anim_in_expo.png)

`easing: in_quad`

![image](/docs/mc/images/anim_in_quad.png)

`easing: in_quart`

![image](/docs/mc/images/anim_in_quart.png)

`easing: in_quint`

![image](/docs/mc/images/anim_in_quint.png)

`easing: in_sine`

![image](/docs/mc/images/anim_in_sine.png)

## Easing "end" functions

The following functions apply an easing formula at the end of the time,
meaning they start fast and then slow down towards the end:

`easing: out_back`

![image](/docs/mc/images/anim_out_back.png)

`easing: out_bounce`

![image](/docs/mc/images/anim_out_bounce.png)

`easing: out_circ`

![image](/docs/mc/images/anim_out_circ.png)

`easing: out_cubic`

![image](/docs/mc/images/anim_out_cubic.png)

`easing: out_elastic`

![image](/docs/mc/images/anim_out_elastic.png)

`easing: out_expo`

![image](/docs/mc/images/anim_out_expo.png)

`easing: out_quad`

![image](/docs/mc/images/anim_out_quad.png)

`easing: out_quart`

![image](/docs/mc/images/anim_out_quart.png)

`easing: out_quint`

![image](/docs/mc/images/anim_out_quint.png)

`easing: out_sine`

![image](/docs/mc/images/anim_out_sine.png)

## Easing both "start" and "end" functions

The following functions apply the easing to both the beginning and the
end of the time, meaning they start slow, accelerate in the middle, and
then slow down again at the end.

`easing: in_out_back`

![image](/docs/mc/images/anim_in_out_back.png)

`easing: in_out_bounce`

![image](/docs/mc/images/anim_in_out_bounce.png)

`easing: in_out_circ`

![image](/docs/mc/images/anim_in_out_circ.png)

`easing: in_out_cubic`

![image](/docs/mc/images/anim_in_out_cubic.png)

`easing: in_out_elastic`

![image](/docs/mc/images/anim_in_out_elastic.png)

`easing: in_out_expo`

![image](/docs/mc/images/anim_in_out_expo.png)

`easing: in_out_quad`

![image](/docs/mc/images/anim_in_out_quad.png)

`easing: in_out_quart`

![image](/docs/mc/images/anim_in_out_quart.png)

`easing: in_out_quint`

![image](/docs/mc/images/anim_in_out_quint.png)

`easing: in_out_sine`

![image](/docs/mc/images/anim_in_out_sine.png)

We'd like to give a shout out and thanks to the creators of the Kivy
multimedia library (which is what the MPC MC uses) for [creating the
graphs](https://kivy.org/docs/api-kivy.animation.html) we used in our
easing documentation.
