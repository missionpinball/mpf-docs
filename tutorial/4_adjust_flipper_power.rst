Tutorial step 4: Adjust your flipper power
==========================================

We casually mentioned in the previous step that MPF uses a very low
default power setting for coils--mainly because we don't want to risk blowing
apart some 40-year-old coil mechanism with a power setting that's too high. (Ask us
how we know this! :)

So at this step in the tutorial, we're going to
look at how you can adjust and fine-tune the power of your flipper
coils. The good news is that everything you learn here will 100% apply
to all the other coils in your machine (slingshots, pop bumpers, ball
ejects, the knocker, drop target resets, etc.)

1. Adjust coil pulse times
--------------------------

Modern pinball controllers that MPF uses have
the ability to precisely control how long (in milliseconds) the full
power is applied to a coil. (Longer time = more power.) This is called
the "pulse time" of a coil, as it controls how long the coil is pulsed
when it's fired.

You can set the default pulse time for each coil in
the coil's entry in the ``coils:`` section of your config file. If you
don't specify a time for a particular coil, then MPF will use a default
pulse time of 10ms.

So in the last step, we got your flipper coils working, but as they are now,
they each use 10ms for their pulse
times. (Remember for flippers we're talking about the strong initial
pulse to move the flipper from the down to up position. Then after
that pulse is over, if you have dual-wound coils, the main winding is
shut off while the hold winding stays on, and if you have single wound
coils the pulse time specifies how long the coil is on solid for
before it goes to the on/off pwm switching.)

So right now your flippers have a pulse time of 10ms. But what if that's too strong? In
that case you risk breaking something. Or if your coil is too weak,
then your ball will be too slow or not be able to make it to the top
of the playfield or up all your ramps. So now you have to play with
different settings to see what "feels" right.

Unfortunately there's no
universal pulse time setting that will work on every machine. It
depends on how many windings your coils have, how worn out your coils
are, how clean your coil sleeves are, how tight your flipper bats are to the
playfield, how free-moving your linkages are, and how much voltage you're
using. Some machines have coil pulse times set really low, like 12 or
14ms. Others might be 60 or 70ms. Our 1974 Big Shot machine has
several coils with pulse times over 100ms. It all really depends.

You adjust the pulse time for each coil by adding a ``default_pulse_ms:`` setting to
the coil's entry in the ``coils:`` section of your config file. (Notice
that you make this change in the ``coils:`` section of your config, not
the ``flippers:`` section.) So let's try changing your flipper coils
from the default of 10ms to 20ms. Change your config file so it looks
like this:

.. code-block:: mpf-config

   coils:
     c_flipper_left_main:
       number: 00
       default_pulse_ms: 20
     c_flipper_left_hold:
       number: 01
       allow_enable: true
     c_flipper_right_main:
       number: 02
       default_pulse_ms: 20
     c_flipper_right_hold:
       number: 03
       allow_enable: true

Notice that we only added ``default_pulse_ms:`` entries to the two main coils,
since the hold coils are never pulsed so it doesn't matter what their
pulse times are. Now play your game and see how it feels. Then keep on
adjusting the ``default_pulse_ms:`` values up or down until your flippers
feel right. In the future we'll create a coil test tool that makes it
easy to dial-in your settings without having to manually change the
config file and re-run your game, but we don't have that yet. You
might find that you have to adjust this ``default_pulse_ms:`` setting down the
road too. If you have a blank playfield then you might think that your
coils are fine where they are, but once you add some ramps you might
realize it's too hard to make a ramp shot and you have to increase the
power a bit. Later on when you have a real game, you can even expose
these pulse settings to operators via the service menu.

2. Adjusting coil "hold" strength
---------------------------------

If you're using single-wound flipper coils, you should also take a
look at the ``default_hold_power:`` values. (Again, to be clear, you only have
to do this if your flippers have a single winding. If you have dual-wound
coils then the hold winding is designed to be held on for long
periods of time so you can safely keep it on full strength solid and
you can skip to the next step.)

We don't have any good guidance for
what your ``default_hold_power:`` values should be. Really you can just start
with a value of 0.125 or 0.25 and then keep increasing it (0.0 for 0% power to 1.0 for 100% power)
until your flipper holds are strong enough not to break their
hold when a ball hits them. Some hardware platform have additional
options for fine-turning the hold power if this setting
result in weird buzzing sounds or don't feel right. See the *coils:*
section of each hardware platform's How To guide for details for your
platform.

By the way there are a lot of other settings you can
configure for your flippers. (As detailed in the :doc:`/config/flippers`
section of the config file reference.) They're not too important
now, but we wanted to at least look at the power settings to make sure
you don't get too far into this tutorial with a risk of burning them
up.

3. Check out the complete config.yaml file so far
-------------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point,
it’s available in the "tutorials" folder of the mpf-examples
package that you should have downloaded in Step 1 of this tutorial.

There are config files for each step, so the config for Step 4 should
be at ``/mpf-examples/tutorial/config/step_4``.

You can run this file directly by switching to that folder and then running the following command:

.. code-block:: doscon

   C:\mpf-examples\tutorial>mpf
