Slides
======

Now that you know what a display is, the next concept you need to understand is
"slides". Slides in MPF are just like slides in a PowerPoint presentation
or slides in an old-fashioned slide projector.

You create multiple slides (each with its own content), and then you tell MPF
when to activate certain slides. Every slide has a priority, so if multiple
slides are active at the same time, the one with the highest priority will be
shown. You can also set "transitions" which control what visual effect is used
to transition from the current slide to the new slide. (Transitions are things like
cross-fade, move in, push out, etc.)

.. image:: /displays/images/how_slides_work.png

.. rubric:: Slide Priorities

Every slide in MPF has a priority, which is simply a numeric value. Bigger
numbers equal higher priority.

Since only one slide is shown at a time, whenever there is more than one
active slide, whichever slide has the highest priority will be the
one that's shown.

For example, you might have a general score slide at priority 100 which shows
the current player's score, the ball, the credits, and maybe the scores of the
other players.

If the player shakes the machine too hard and a tilt warning slide is shown,
then that tilt warning slide might be activated at a priority of 10,000, meaning
that it would be shown instead of the general score slide.

Then after a few seconds, the tilt warning slide might be removed, and MPF will
then show the next-highest active slide which would most likely be the general
scoring slide that was showing before.

The slide priority system is integrated into MPF's mode system, meaning that
slides created by modes automatically inherit the priority of the mode that's
showing them. Put another way, a slide from a higher priority mode would show
in place of a slide from a lower priority mode (though every mode doesn't need
to have slides). You can also tweak the priorities of slides (higher or lower)
to make sure the slide you want to show is the one that's showing at any given
time. We'll dig into that later in the documentation.

.. rubric:: Slides with Multiple Displays

When MPF is used with :doc:`multiple displays </displays/display/index>`, each
display maintains its own stack of active slides. The priorities of the slides
in the stack and the priority of the current slide on one display has nothing
to do with the active and current slides of another display.

.. image:: /displays/images/slides_with_multiple_displays.png



.. toctree::

   Creating Slides <creating_slides>
   Showing Slides <showing_slides>
   Slide Transitions <transitions>
   multiplayer_display
   picture_in_picture
   split_screen
