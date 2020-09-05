OPP Switches
============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+


For switches, you can use most of the settings as outlined in the
``switches:`` section of the config file reference. There are only a
few things that are OPP-specific:

Number:
^^^^^^^

OPP switches are numbered sequentially depending on which wing board
is the switch input.  Wing position 0 contains switch numbers 0 to 7.
Wing position 1 contains switch numbers 8 to 15.  Wing position 2
contains switch numbers 16 to 23.  Wing position 3 contains switch
numbers 24 to 31. The switch is numbered using the position of the
OPP card (starting at 0), then a '-', and finally the switch number
on the card.

Enter them as a combination of board-switch, like ``0-12``.

.. code-block:: mpf-config

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

Switch inputs for a switch matrix are number slightly differently.  To
configure an 8x8 switch matrix wing 2 is configured as the matrix input
and wing 3 is configured as a matrix output.  The OPP hardware strobes
the eight outputs while reading from the eight inputs.  This allows 64
inputs to be read using only 16 wires.  The matrix switch inputs are
numbered from 32 to 95.  Switches 32 - 39 are column 0, switches 40 -
47 are column 1, switch 48 - 55 are column 2, switches 56 - 63 are
column 3, switches 64 - 71 are column 4, switches 72 to 79 are column
5, switches 80 to 87 are column 6, and switches 88 to 95 are column 7.

What if it did not work?
------------------------

Have a look at our :doc:`OPP troubleshooting guide <troubleshooting>`.
