Proximity Switches
==================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

Proximity switches operate via the interaction of the ball within a magnetic
field created by the switch.
Unlike a reed switch, which also uses a magnetic field to sense the ball,
proximity switches differ in that they do not have any moving parts.
However, a voltage must be applied and they require additional circuitry
compared to a reed switch.
Alien pinball (heighway Pinball, 2017) makes signifigant use of proximity
switches in liu of the traditional thru-playfield mechanical leaf-blade style
switches.
An advantage of proximity switches (other than not needing to make
thru-playfield cuts or have mechanical parts wear out), is
that they can be designed with different levels of sensitivity, or even made
tunable.

.. todo:: Add a picture (:doc:`/about/help_us_to_write_it`).

For homebrew pinball applications, while they are not typically available
from major pinball suppliers due to their scarcity in current and past pinballs,
there are a few online sources of these switches -- including the exact ones
used in Alien Pinball.

Wiring will depend on the exact switch used.
With SW-16 switch boards, the use of pull-up resistors will likely be required
when supplying a direct input to the switch ports.
FAST boards should work similarily.


.. todo:: Describe wiring (:doc:`/about/help_us_to_write_it`).

