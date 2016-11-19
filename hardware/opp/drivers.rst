OPP coils / drivers
===================

There are a few things to know about controlling drivers and coils
with OPP hardware.

Number
~~~~~~

OPP coils are numbered sequentially depending on which wing board
is the coil output.  Wing position 0 contains coil numbers 0 to 3.
Wing position 1 contains coil numbers 4 to 7.  Wing position 2
contains coil numbers 8 to 11.  Wing position 3 contains coil
numbers 12 to 15. The coil is numbered using the position of the
OPP card (starting at 0), then a '-', and finally the coil number
on the card.

::

    coils:
      some_coil:
        number: 0-12

The above example configures a coil output as the first OPP card, and
the third wing board, first output.  On the microprocessor card, the
output is marked as 3.4 (wing port 3, position 4).

Pulse time
~~~~~~~~~~

The OPP hardware also has the ability to specify the "pulse time".
Pulse time is the coil's initial kick time. For
example, consider the following configuration:

::

    coils:
        some_coil:
            number: 0-12
            pulse_ms: 30

When MPF sends this coil a pulse command, the coil will be fired for
30ms.

Hold Power
~~~~~~~~~~
If you want to hold a driver on at less than full power, MPF does this by using
"hold_power" parameter which works for all platforms. It can range from 0 to 8
and hold_power/8 = time share the coil is on.

The period is fixed at 16ms for OPP. To set the hold power to 25%, set
hold_power to 2 and OPP will use 4ms/16ms = 25%.

Because of firmware limitations in OPP hold_power 8 will translate to 15ms/16ms
= 93.75% on. Same happens when allow_enable is set to true and no hold_power is
provided. There is currently no way to permanently enable a hold coil in OPP.

By using the MPF hold_power parameter you can only use 8 out of 16 possible
steps. Therefore, you can also use the OPP specific parameter hold_power16
which can range from 0 to 15.

::

    coils:
      some_coil:
        number: 0-3
        pulse_ms: 32
        hold_power: 4

This will configure OPP card 0, solenoid wing 0, last solenoid to
have an initial pulse of 32 ms, and then be held on at 50% power.
