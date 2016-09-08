Easing Instructions
===================

MPF has the ability to use "easing" functions to adjust the acceleration and
deceleration of motions associated with
:doc:`slide transitions </displays/slides/transitions>` and
:doc:`widget animations </displays/widgets/animate_widgets>`.

An easing function is a formula that calculates a progress value based on an
input value.

Let's look at a simple (but not realistic) example of animating a widget that
moves 10 pixels in 10 seconds. With no easing function applied, it would
have moved 1 pixel after 1 second, 2 pixels after 2 seconds, etc.

At first you might think this seems fine, but to the viewer it will not look
natural because it will instantly start moving at full speed, and then it will
stop suddenly when it gets to the end. A more natural approach would be to have
it accelerate slowly at the beginning and then to decelerate as it approaches
the end.

All animation and transition functions in MPF change a value over a certain
amount of time. (Move 50 pixels in 2 seconds, change the opacity from 100% to
50% in 500ms, etc.)

We can illustrate this with a graph, where time is the X axis, and the value
is the Y axis, like this:

.. image:: /displays/images/easing_explained.png

The image above shows the default formula with no easing applied. (This is
technically the "linear" easing function.) The value of the function is directly
related to the time, and the speed of change is the same at the beginning and
end.

But what if we wanted our animation to start slow and accelerate, then slow down
again towards the end? For that, we could use a formula like this:

.. image:: /displays/images/anim_in_out_sine.png

Notice that at the beginning (in the lower left corner), as you move right, the
red line doesn't change too much. Then towards the middle, the red line changes
more as the transition speeds up, and then at the end (towards the upper right),
the line changes more slowly.

You can also imagine how an easing formula would look if you wanted something
to start slow, but then speed up without slowing down again. (This might be
useful if you want a widget to move off screen since it will have a gentle start
and then it will shoot off and get faster and faster.) That function might look
like this:

.. image:: /displays/images/anim_in_quart.png

Conversely, if you have a widget coming in from off screen, you might want it to
start out fast and then slow down as it approaches its final location. For that
you could use what's essentially the opposite of the previous formula, like
this:

.. image:: /displays/images/anim_out_quad.png


The important thing to remember with these easing formulas is that the red line
does NOT represent the path the moving objects take, rather, it represents how
the progress of the change happens over time.

Where can you apply easing?
---------------------------

In MPF, these easing functions are used in two places:

* For widget animations, to affect how the progress of an animated property
  progresses over time.
* For some (not all) slide transitions, to affect the progress of the transition
  over time.

Remember when you're animating a widget, you can animate ANY numerical property.
So this can include the x/y position on the display, but it can also include
the size, scale, and/or the opacity (transparency).

So if you use an easing function like this to change the opacity of a widget
over time, rather than slowly fading on and off, it will almost be like the
widget is flickering:

.. image:: /displays/images/anim_in_out_bounce.png

Refer to the :doc:`slide transition </displays/slides/transitions>` and
:doc:`widget animation </displays/widgets/animate_widgets>` documentation for
details on how to actually apply these easing functions. It's pretty
straightforward—essentially you just add ``easing: <function_name>`` to the
animation or transition property, like ``easing: in_out_circ``.

Now lets look at the different types of easing functions MPF supports:

Easing "start" functions
------------------------

The following functions apply an easing formula at the beginning of the time and
then accelerate to the end:

in_back

.. image:: /displays/images/anim_in_back.png

in_bounce

.. image:: /displays/images/anim_in_bounce.png

in_circ

.. image:: /displays/images/anim_in_circ.png

in_cubic

.. image:: /displays/images/anim_in_cubic.png

in_elastic

.. image:: /displays/images/anim_in_elastic.png

in_expo

.. image:: /displays/images/anim_in_expo.png

in_quad

.. image:: /displays/images/anim_in_quad.png

in_quart

.. image:: /displays/images/anim_in_quart.png

in_quint

.. image:: /displays/images/anim_in_quint.png

in_sine

.. image:: /displays/images/anim_in_sine.png


Easing "end" functions
----------------------

The following functions apply an easing formula at the end of the time,
meaning they start fast and then slow down towards the end:


out_back

.. image:: /displays/images/anim_out_back.png

out_bounce

.. image:: /displays/images/anim_out_bounce.png

out_circ

.. image:: /displays/images/anim_out_circ.png

out_cubic

.. image:: /displays/images/anim_out_cubic.png

out_elastic

.. image:: /displays/images/anim_out_elastic.png

out_expo

.. image:: /displays/images/anim_out_expo.png

out_quad

.. image:: /displays/images/anim_out_quad.png

out_quart

.. image:: /displays/images/anim_out_quart.png

out_quint

.. image:: /displays/images/anim_out_quint.png

out_sine

.. image:: /displays/images/anim_out_sine.png


Easing both "start" and "end" functions
---------------------------------------

The following functions apply the easing to both the beginning and the end of
the time, meaning they start slow, accelerate in the middle, and then slow down
again at the end.


in_out_back

.. image:: /displays/images/anim_in_out_back.png

in_out_bounce

.. image:: /displays/images/anim_in_out_bounce.png

in_out_circ

.. image:: /displays/images/anim_in_out_circ.png

in_out_cubic

.. image:: /displays/images/anim_in_out_cubic.png

in_out_elastic

.. image:: /displays/images/anim_in_out_elastic.png

in_out_expo

.. image:: /displays/images/anim_in_out_expo.png

in_out_quad

.. image:: /displays/images/anim_in_out_quad.png

in_out_quart

.. image:: /displays/images/anim_in_out_quart.png

in_out_quint

.. image:: /displays/images/anim_in_out_quint.png

in_out_sine

.. image:: /displays/images/anim_in_out_sine.png


We'd like to give a shout out and thanks to the creators of the Kivy multimedia
library (which is what the MPC MC uses) for
`creating the graphs <https://kivy.org/docs/api-kivy.animation.html>`_ we
used in our easing documentation.


