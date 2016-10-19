Configuring flippers with single-wound coils
============================================

The example above uses dual-wound flipper coils where
MPF literally sees each flipper coil as two separate coils (with two
separate names and two separate drivers). When you push the flipper
button, MPF energizes both coils initially, but cuts the power to the
main coil after a few milliseconds so only the lower power hold coil
remains active. This prevents the flipper coil from burning up.

As an alternative, some flippers just use normal (single winding) coils and
then the hardware controller controls the flow of electricity through
it to prevent it from burning up. In that case the hardware will send
an initial constant pulse for a few milliseconds to give the flipper
its strong initial pulse, and then it will flip the current on & off
really fast (really fast, like hundreds of times per second) to keep
the flipper in the 'up' position without overheating it.

If you have single-wound flipper coils (or if you have traditional dual-wound
coils but you don't want to waste two drivers per flipper and you just
want to use a single winding), make sure you've read our
:doc:`theory` tech note for all the details about how that
works. If you'd like to use single-wound flipper coils, you need to do
two things in your config file:

+ First, you can remove the ``hold_coil:`` entries from your two
  flippers since you don't have hold coils.
+ Second, you need to add a ``hold_power:`` entry to each of your two
  coils in the ``coils:`` section of your config file. This is how you
  tell MPF what timing it should use to quickly pulse the current to
  that coil when its being held on.

Here's an example of what the ``coils:`` and ``flippers:`` sections of
your config file would look like if you're using single wound coils.
(The ``switches:`` section would be the same in both cases):

::

    # single-wound flipper coil example

    coils:
        c_flipper_left_main:
            number: 0
            pulse_ms: 20
            hold_power: 2
        c_flipper_right_main:
            number: 2
            pulse_ms: 20
            hold_power: 2

    flippers:
        left_flipper:
            main_coil: c_flipper_left_main
            activation_switch: s_left_flipper
        right_flipper:
            main_coil: c_flipper_right_main
            activation_switch: s_right_flipper

Note that we used a values of 2 for the *hold_power*. The *hold_power*
setting is a whole number from 0-8 which represent a percentage of
power that's applied when that coil is held on. (0 = 0%, 4=50%,
8=100%, etc.) At this point we have no idea if ``hold_power: 2`` is the
correct setting or not. We can fine-tune that later. (And again,
*hold_power* is only used with single-wound coils. Dual-wound coils
fire both windows at full power all the time, since the hold winding is
designed to be energized at full power.)