How to adjust flipper power
===========================

One of the advantages of using a modern control system is that you can fine-tune
the flipper strength in software. (In the old days you actually had to order
different coils and swap them out.)

When we talk about "adjusting flipper power" we're talking about both (1) the
strength of the flip which controls how easy it is get get balls up ramps, and
(2) the "hold" strength of single-wound flipper coils.

Adjusting coil pulse times
--------------------------

Modern pinball controllers that MPF use have
the ability to precisely control how long (in milliseconds) the full
power is applied to a coil. (Longer time = more power.) This is called
the "pulse time" of a coil, as it controls how long the coil is pulsed
when it's fired.

You can use this adjustment for both dual-wound and single-wound coils.

You can set the default pulse time for each coil in
the coil's entry in the ``coils:`` section of your config file. If you
don't specify a time for a particular coil, then MPF will a default
pulse time of 10ms.

Adjusting the pulse time is a bit of an art. If the pulse time is too long,
you'll risk breaking something and/or it will be too hard to make shots because
the ball will be flying around too fast. if the pulse time is too short, it will
be hard to make all the shots in your game because the ball won't have enough
momentum. So now you have to play with different settings to see what "feels"
right.

Unfortunately there's no universal pulse time setting that will work on every
machine since the "pulse time" to "actual strength" mapping varies depending on:

* What type of coils you have (wire guage and number of windings).
* How much voltage you're power supply provides.
* How much current is available.
* How clean or worn your flipper mechanisms, return spring, and coil sleeves
  are.
* How warm your coils are.

Pulse values can vary widely. One of our machines using new Williams flipper
mechanisms with a 70vdc power supply has flipper pulse times of 14ms. Our
1974 Gottlieb Big Shot machine using the original flipper mechs has a pulse
time over 100ms.

You adjust the pulse time for each coil by adding a ``pulse_ms:`` setting to
the coil's entry in the ``coils:`` section of your config file. (Notice
that you make this change in the ``coils:`` section of your config, not
the ``flippers:`` section.)

If this is your initial configuration (which was 10ms by default) and your
flippers don't move, maybe try changing them to 20ms instead, by adding
``pulse_ms: 20`` to your flipper coil configuration.

.. note::

   If you have dual-wound flipper coils, then you add this pulse setting to the
   main (power) coil only since the hold coils are never pulsed.

For example, for dual-wound coils:

::

    coils:
        c_flipper_left_main:
            number: 00
            pulse_ms: 20
        c_flipper_left_hold:
            number: 01
            allow_enable: true
        c_flipper_right_main:
            number: 02
            pulse_ms: 20
        c_flipper_right_hold:
            number: 03
            allow_enable: true

Or for single-wound coils:

::

    coils:
        c_flipper_left:
            number: 0
            allow_enable: true
            hold_power: 1
            pulse_ms: 20
        c_flipper_right:
            number: 1
            allow_enable: true
            hold_power: 1
            pulse_ms: 20

Now play your game and see how it feels. Then keep on
adjusting the ``pulse_ms:`` values up or down until your flippers
feel right.

You might find that you have to adjust this ``pulse_ms:`` setting down the
road too. If you have a blank playfield then you might think that your
coils are fine where they are, but once you add some ramps you might
realize it's too hard to make a ramp shot and you have to increase the
power a bit. Later on when you have a real game, you can even expose
these pulse settings to operators via the service menu.

Adjusting single-wound coil "hold" strength
-------------------------------------------

If you're using single-wound flipper coils, you should also take a
look at the ``hold_power:`` values. (Again, to be clear, you only have
to do this if your flippers have a single winding. If you have dual-wound
coils then the hold winding is designed to be held on for long
periods of time so you can safely keep it on full strength solid and
you can skip to the next step.)

We don't have any good guidance for
what your ``hold_power:`` values should be. Really you can just start
with a value of 1 or 2 and then keep increasing it (whole numbers
only) until your flipper holds are strong enough not to break their
hold when a ball hits them. Each hardware platform has additional
options for fine-turning the hold power if you find the values of 1-8
result in weird buzzing sounds or don't feel right.
