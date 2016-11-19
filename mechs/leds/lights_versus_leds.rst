"Lights" versus "LEDs" (Some LEDs are lights?!?)
================================================

One thing that's important to know about LEDs in MPF is that not
all LEDs are configured as LEDs. :)

Taking a step back. There are two types of lighting systems in pinball
machines: lamp matrices and direct-connected LEDs. All commercial pinball
machines from about 1979 through 2012 (give or take) used lamp matrices
(typically with 8 rows and 8 columns of lights). Historically these were
used with incandescent light bulbs, (#44, #555, etc.).

However, in more recent years various manufacturers have released LED
"replacement" bulbs that fit the old-style sockets but that are actually
LEDs. If your machine uses a lamp matrix, then you will add your lights
(whether they're LEDs or incandescent) as :doc:`lights </mechs/lights/index>`
via the :doc:`/config/matrix_lights` section of your machine config. You'll
do this even if you have LED bulbs in your lamp matrix.

Alternately, if you have directly-controlled LEDs (i.e. no lamp
matrix), whether single color or RGB, then you'll configure them as
:doc:`LEDs <index>` in the :doc:`/config/leds` section of your config.

The following diagram shows the different types. An easy way to tell is
if your lights or LEDs have mini bayonet or mini wedge bases, they're
*Matrix Lights*, and everything else is *LEDs*:

.. image:: /mechs/images/lights_vs_leds.jpg

Note that it's possible that you'll have both matrix lights and direct
connected LEDs in the same machine. For example, maybe you're writing
code for an existing WPC machine and you'll use the existing matrix
lights as they are while also adding new direct connected LEDs for
some new toys.
