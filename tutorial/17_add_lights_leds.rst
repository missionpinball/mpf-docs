Tutorial step 17: Add lights (or LEDs)
======================================

Now that you're able to run a complete (albeit boring) game, let's get
your lights or LEDs configured. In this step, we're going to add your
machine's lights and/or LEDs to your machine config file, and then in
the next step we're going to create a basic light show that can run
during your machine's attract mode.

Note: If you're following this
tutorial with virtual hardware, you might want to skip these two steps
since you can't really see the effects of your lights working via the
console and log files. So feel free to skip to Step 19 (the one about
shots) right now and then you can come back and add lights once
you have physical hardware).

Also note that throughout the MPF
documentation, we tend to use the term "lights" to refer to any type
of playfield light, including traditional #44 or #555 incandescent
bulbs plugged into a lamp matrix, #44 and #555 LED "replacement" LEDs
used with a lamp matrix, and newer LEDs or RGB LEDs directly connected
to LED controllers. If we need to specifically refer to one type of
light versus another, we'll make that clear.

1. Understand the different between matrix lights and LEDs
----------------------------------------------------------

Before you get started building the configuration for your lights, you
have to know whether you'll be configuring matrix lights or LEDs. This
is tricky, because you can use LEDs with lamp matrices, so just
because you're using LEDs doesn't mean you configure MPF for LEDs!

Umm... what?

Ok, let's take a step back. There are two types of
lighting systems for pinball machines: lamp matrices and direct-
connected LEDs. All commercial pinball machines from about 1979
through 2012 (give or take) used lamp matrices (typically with 8 rows
and 8 columns of lights). Historically these were used with
incandescent light bulbs, (#44, #555, etc.), though in more recent
years various manufacturers have released LED "replacement" bulbs that
fit the old-style sockets but that are actually LEDs. If your machine
uses a lamp matrix, then you will add your lights (whether they're
LEDs or incandescent) via the `matrix_lights:` section of your machine
config file. This will apply to you if:

+ You're using a Multimorphic P-ROC or FAST WPC controller to write
  your own game software for an existing Williams System 11, WPC
  machine, Stern S.A.M, or Sega/Stern Whitestar machine.
+ You're using a Multimorphic P-ROC or P3-ROC with a PD-8x8 lamp
  matrix controller.

Alternately, if you have directly-controlled LEDs (i.e. no lamp
matrix), whether single color or RGB, then you'll configure them in
the ``leds:`` section of your machine config file. This will apply to
you if:

+ You're using a Multimorphic PD-LED board to control your LEDs.
+ You're using serial RGB LEDs plugged into the RGB LED ports of a
  FAST controller.
+ You're using any type of "Neopixel" RGB LED (FadeCandy, etc.)

Another way to tell which kind of lights you're using is if your lights or
LEDs have mini bayonet or mini wedge bases, they're *Matrix Lights*, and
everything else is *LEDs*. Here's a diagram that might help:

.. image:: images/lights_vs_leds.jpg

Note that it's possible that you'll have both matrix lights and direct
connected LEDs in the same machine. For example, maybe you're writing
code for an existing WPC machine and you'll use the existing matrix
lights as they are while also adding new direct connected LEDs for
some new toys.

2. Add your lights to your machine config file
----------------------------------------------

Once you figure out what kind of lights you have, you need to add the
relevant section to your machine configuration file. There's probably
not much to explain here. Adding lights is pretty similar to adding
switches and coils.

For matrix lights, follow the directions for your
specific setup as detailed in the :doc:`/config_matrix_lights` section
of the config file reference. If you have LEDs, follow the instructions
and the :doc:`/config/leds` section. (There are notes in there which
explain how to configure LEDs with different color channel order, like BRG instead of RGB.

You can apply tags to lights which you can use perform actions on a group
(such as, *turn on all the lights tagged with "red,"* or
*turn off all lights except those tagged with "mini_playfield*," though it's simple
to add tags later so you don't really have to do it now.

Also keep in mind that the specific format you use to specify which lights are
connected to which controller outputs will vary depending on whether
you have Multimorphic or FAST pinball controllers and whether you're
using OEM or Williams WPC driver boards.

Again, just follow the
directions in the config reference and post to the Google group with
questions. Here's a small part of the ``matrix_lights:`` section of our
machine configuration file for *Demolition Man*. Notice again that we
preface each light with ``l_`` (lowercase "L") to make it easier for our code editor's
autocomplete function to find light names in the future.

::

    matrix_lights:

        l_ball_save:
            number: l11
            label:
            tags:
        l_fortress_multiball:
            number: l12
            label:
            tags:
        l_museum_multiball:
            number: l13
            label:
            tags:
        l_cryoprison_multiball:
            number: l14
            label:
            tags:
        l_wasteland_multiball:
            number: l15
            label:
            tags:
        l_shoot_again:
            number: l16
            label:
            tags:
