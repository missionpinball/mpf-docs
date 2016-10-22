How MPF talks to physical pinball machines
==========================================

Since MPF is ultimately about controlling real pinball machines, it's important
to understand how you "install" MPF onto a pinball machine.

MPF is software that runs on a computer. This computer can be Windows, Mac, or Linux,
and it can be a laptop, a desktop, a motherboard in your pinball machine, or a small
system like a Raspberry Pi.

(Most people develop their game on their laptop, and then when they're done, transfer
it to a smaller computer permanently installed in their pinball machine.)

The computer running MPF is connected to a modern pinball control system via USB.
That pinball control system acts as the "bridge" between the computer running MPF
and the physical pinball machine. (In other words, it receives switch notifications
from the pinball machine and sends them to MPF, and it sends LED, light, and coil
instructions from MPF to the physical pinball machine.)

This diagram shows how it all fits together:

.. image:: images/computer-controller-machine.jpg

See the :doc:`/hardware/index` page for more details on the various control systems
that MPF supports.
