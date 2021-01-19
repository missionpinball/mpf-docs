Connecting PKONE to your Computer
=================================

This page is about connecting the PKONE system to your computer.
It roughly covers connecting the bus between the boards.

PKONE Nano
----------

Connect your PKONE NANO controller to your PC using USB.

.. image:: /hardware/images/pkone-nano.png

Then connect the OUT port of your NANO to the IN port of your first board (Extension or Lightshow).
Consequently, connect the OUT port of the first board to the IN port of your second board (etc.).
Be sure each Extension board or Lightshow board has a unique Address ID set using the Address ID
switches on each board. Finally, be sure the last board in the chain has the CANBUS Protocol
Termination Jumper set to properly terminate the bus.

The ``number:`` setting for each driver/switch is its board's Address ID number in the
chain, then the dash, then the driver/switch number. Note that the addresses are numbered
starting with zero (Extension boards have addresses 0 to 7 while Lightshow boards have addresses
0 to 3).
