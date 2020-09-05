Adjust coil strength (pulse times)
==================================

Modern pinball controller systems that MPF use have the ability to precisely
control how long (in milliseconds) the full power is applied to a coil. (Longer
time = more power.) This is called the "pulse time" of a coil, as it controls
how long the coil is pulsed MPF sends the coil a pulse command.

You can adjust this setting for all the coils in your machine, including
flippers, trough ejects, pop bumpers, etc.

This is much nicer than the old days (even the 1990s WPC era) where pulse
times were fixed, and you adjusted the strength of a mechanism by literally
swapping out the coil with a stronger or weaker one!

.. note:: If you have :doc:`"dual wound" <dual_wound_coils>`
   coils, which are common for flippers,
   diverters, and other mechs which are "held" in the on position, you can use
   the pulse settings defined in this guide to control the initial "pulse"
   portion of that coil's activation.

Adjusting the pulse time is a bit of an art. If the pulse time is too long,
you'll risk breaking something and the ball will fly off the mechanism too fast.
Times that are two low will make the machine seem sluggish.

We suggest that you start with a slow time and slowly increase it until it
feels right.

Unfortunately there's no universal pulse time setting that will work on every
machine since the "pulse time" to "actual strength" mapping varies depending on:

* What type of coils you have (wire gauge and number of windings).
* How much voltage your power supply provides.
* How much current is available.
* How clean or worn your mechanisms, return springs, and/or coil sleeves
  are.
* How warm your coils are.

Pulse values can vary widely. One of our machines using new Williams flipper
mechanisms with a 70vdc power supply has flipper pulse times of 14ms. Our
1974 Gottlieb Big Shot machine using the original flipper mechs has a pulse
time over 100ms.

You adjust the pulse time for each coil by adding a ``default_pulse_ms:`` setting to
the coil's entry in the :doc:`/config/coils` section of your machine config
file. (Notice that you make this change in the ``coils:`` section of your
config, not the section for the individual mech that coil is part of.)

If you don't specify a time for a particular coil, then MPF will a default
pulse time of 10ms. (10ms is almost certainly too low, but it's a very safe
default starting point.)

For example, for coils used in dual-wound flippers:

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

Or for single-wound flipper coils:

.. code-block:: mpf-config

    coils:
      c_flipper_left:
        number: 0
        allow_enable: true
        default_hold_power: 0.125
        default_pulse_ms: 20
      c_flipper_right:
        number: 1
        allow_enable: true
        default_hold_power: 0.125
        default_pulse_ms: 20

Again, you just need to play your game and see how it feels. Then keep on
adjusting the ``default_pulse_ms:`` values up or down until your flippers
feel right.

You might find that you have to adjust this ``default_pulse_ms:`` setting down the
road too. If you have a blank playfield then you might think that your
coils are fine where they are, but once you add some ramps you might
realize it's too hard to make a ramp shot and you have to increase the
power a bit. Later on when you have a real game, you can even expose
these pulse settings to operators via the service menu.

Advanced settings vary based on hardware
----------------------------------------

In addition to being able to specify how long a coil is pulsed for, some
pinball control systems allow you to control the power that's applied to the
coil during the initial pulse. (So instead of 100% power for 50ms, you might
be able to set a coil to 75% power for 60ms.)

See the :doc:`hardware documentation for your platform </hardware/index>` for
links to specific coil settings your hardware might allow.
