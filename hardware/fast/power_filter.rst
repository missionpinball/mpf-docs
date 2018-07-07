Power Filter Board
==================

This board can be used to fan out your power rails.
See :doc:`/hardware/voltages_and_power/index` for details.

.. image:: /hardware/images/fast-power-filter-board.png

The board supports 5 power rails with one fuse per rail:

* High Voltage (HV)
* Aux V1
* Aux V2
* 5V
* 12V

There are capacitors on HV and Aux V1.
This is the theory of operations:

.. image:: /hardware/images/fast-power-filter-board-block-diagram.png

Additionally, there is a high voltage enable switch on the board on J2.
You can connect it to your door switch to cut power when the door opens.
Make sure to close this switch when you operate the machine or HV will be off.
During development you may use a jumper but be careful since HV will be always
on.

Connect all your PSUs to J3 and the playfield and controller to J4.
This is how FAST envisions the wiring of the board:

.. image:: /hardware/images/fast-power-filter-board-wiring.png
