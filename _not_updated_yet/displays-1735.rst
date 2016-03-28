
A "display" in MPF is a piece of physical hardwarethat shows slide.
For example, the DMD is a display, the on screen window is a display,
and (when we get to it), the segmented score displays in the backbox
are displays. MPF contains separate modules (called "display modules")
for each type of display (since the code that drives each type of a
display is very different). Even though they're all different, they
all plug-in to MPF in the same way and they all work basically the
same. (Yes, even segmented displays.) Each different type of display
has different properties, including size (length and width in pixels),
how many colors it supports, its refresh rate (in frames per second),
etc. MPF can support multiple different displays at the same time,
each with their own unique settings. (You might want to update the DMD
at 60fps but the on screen window at only 30fps.) Each display is
responsible for managing its own `slides`_and for creating new slides
when needed.

.. _slides: https://missionpinball.com/docs/displays-dmd/slides/


