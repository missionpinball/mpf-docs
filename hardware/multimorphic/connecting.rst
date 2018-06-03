Connecting P/P3-Roc to your Computer
====================================

P-Roc
-----

If you got a P-Roc just connect it to your computer using USB.

.. image:: /hardware/images/multimorphic_p_roc.png

Then connect switches and driver according to the manual
(see :doc:`/hardware/existing_machines/index` for specific machines).
If you are using a PD-Master board see below for switches and drivers.

P3-Roc
------

If you got a P3-Roc just connect it to your computer using USB.

.. image:: /hardware/images/multimorphic_p3_roc.png

Connect all your SW-16 boards to the switch bus and all your PD-16 and PD-8x8
boards to your driver bus. Use twisted wires but connect + to + and - to - on
all nodes.

SW-16
~~~~~

.. image:: /hardware/images/multimorphic_SW-16.png

Set a unique address on every SW-16 board on your bus.
Those addresses can overlap with the driver addresses.
It does not matter on which of the two switch busses the boards are connected.
Terminate the bus at the last board.
See :doc:`switches_p3_roc` for how to configure those boards.

PD-16/PD-8x8
~~~~~~~~~~~~

.. image:: /hardware/images/multimorphic_PD-16.png

Set a unique address on every PD-16/PD-8x8 board on your bus.
Those addresses can overlap with the switch addresses.
However, they overlap with the PD-LED addresses so plan accordingly.
It does not matter on which of the two driver busses the boards are connected.
Terminate the bus at the last board.
See :doc:`drivers` and :doc:`lights` for how to configure those boards.

PD-LED
~~~~~~

.. image:: /hardware/images/multimorphic_PD-LED.png

Set a unique address on every PD-LED board on your bus.
Those addresses can overlap with the switch addresses.
However, they overlap with the PD-16 addresses so plan accordingly.
It does not matter on which of the two driver busses the boards are connected.
Terminate the bus at the last board.
See :doc:`leds` for how to configure those boards.
