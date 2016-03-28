
A "slide" in MPF's display system is essentially just a container for
one or more `display elements`_. Slides don't actually show anything
directly—they just hold display elements. For example, you don't put
text on a slide per se, rather, you create a text display element
which you then add to a slide. The size of a slide (in terms of the
number of pixels in its width and height) is controlled by the MPF
Display that it's on. So a DMD display with a resolution of 128x32
that can show 16 shades of pixels will have slides that are 128x32
with 16 shades. An on screen window that's 800x600 with 24-bit color
will have slides that are 800x600 at 24-bits. In fact the act of
creating a newa slide is actually function of the MPF display where
you say "make me a new slide" and then it generates an empty slide
that you can start putting your elements on. Keep in mind that MPF can
support multiple displays at the same time, and in those cases each
display has its own set of slides. Each `MPF Display`_ can have
multiple slides, though only one is "active" (i.e. "visible") at a
time. You can add and delete elements from a slide anytime you want.
If you add an element to the active slide then it will just appear on
the display. If you add an element to an inactive slide then it will
be there the next time you make that slide active. You can also change
and modify elements anytime you want, even when they are on an active
slide. For example, you might have a `Text element`_ on a slide
showing the player's score, and when the player gets more points then
MPF just updates the text content within that existing element. Same
slide, same element, just new text in that element.



Slide Events
------------

When a slide is removed, if that slide has a name (set via the slide:
setting in the slide_player), then an event will be posted in the form
of *removing_slide_<slide_name>*. This can be used to trigger
additional slides to be created. The technical implementation for this
is the MC sends a trigger to MPF, and MPF posts it like any event. If
*slide_player:* entries are configured for it, then MPF will send the
event to the MC.

.. _display elements: https://missionpinball.com/docs/displays/display-elements/
.. _MPF Display: https://missionpinball.com/docs/displays/displays/
.. _Text element: https://missionpinball.com/docs/displays/display-elements/text/


