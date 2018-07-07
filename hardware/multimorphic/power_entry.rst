Power Entry Board
=================

This board can be used to fan out your power rails.
See :doc:`/hardware/voltages_and_power/index` for details.

.. image:: /hardware/images/multimorphic_Power_Entry.png

The Multimorphic Power Filter board connects 230V/110V AC to all your PSUs
using connectors J1, J2 or J3.

Additionally, it allows to connect up to four DC rails:

* 5V
* 12V
* 15V
* High Voltage (HV)

You might use different voltages but the LEDs might operate outside the spec
in this case (consult the manual).

DC Outputs are J11 to J17. DC Inputs are J6 to J9.
J10 will turn on HV on the ouput.
You should connect it to your door switch to cut high power when the door is
opened.
Make sure that J10 is closed during development or HV will be off.
