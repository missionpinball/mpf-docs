OPP Switches
============

For switches, you can use most of the settings as outlined in the
``switches:`` section of the config file reference. There are only a
few things that are OPP-specific:

Number:
~~~~~~~

OPP switches are numbered sequentially depending on which wing board
is the switch input.  Wing position 0 contains switch numbers 0 to 7.
Wing position 1 contains switch numbers 8 to 15.  Wing position 2
contains switch numbers 16 to 23.  Wing position 3 contains switch
numbers 24 to 31. The switch is numbered using the position of the
OPP card (starting at 0), then a '-', and finally the switch number
on the card.

Enter them as a combination of board-switch, like ``0-12``.

::

    switches:
      some_switch:
        number: 0-15

The above example configures a switch input as the first OPP card, and
the second wing board, last input.  On the microprocessor card, the
input is marked as 1.7 (wing port 1, position 7).

Switch inputs for solenoids follow the same number convention.  Since
only four inputs are available for each wing card, it uses the first
four switch numbers.  Solenoid wing 0 uses switch numbers 0 to 3.
Solenoid wing 1 uses switch numbers 8 to 11.  Solenoid wing 2 uses
switch numbers 16 to 19.  Solenoid wing 3 uses switch numbers 24 to 27.
