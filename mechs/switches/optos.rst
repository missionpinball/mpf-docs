How to configure opto switches
==============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

Optical switches (short optos) are common in pinball machines.
They usually cover ranges up to 10cm and are used in places where normal
:doc:`roll over switches <mechanical_switches>` cannot be used (e.g. because a
lane is too wide or on a ramp).
Optos are also commonly used in ball troughs.


Electronical details
--------------------

Electronically they consist of a sender and a receiver.
The sender is usually connected to 5-12V power with a current limiting resistor
in line (to limit the current to about 50-70 mA). Alternatively, a constant
current driver may be used (more expensive but better for the sender).
The receiver is usually connected to a direct input on a switch board (they
cannot be used in a switch matrix without further logic PCBs).
Most direct inputs have an internal pull up which will pull the level to VCC
(usually around 10 kOhm).
The opto receiver will then pull the current to GND when it receives light from
the sender.
Once the light beam is interrupted the receiver will stop conducting and the
input will go up to VCC again.
For this reason, the input will be closed when the beam is not interrupted and
open when the opto is interrupted.
This is exactly inverse than a normal switch and you have to configure your
opto as *normally closed* (short ``NC``) for that reason.
If your opto is using an additional PCB for optos it might invert the signal
and revert this effect (just try normally closed first and change it later -
it will not break anything).

:doc:`TODO: Add electronical drawing for sender and receiver. </about/help_us_to_write_it>`


Williams/Bally optos
~~~~~~~~~~~~~~~~~~~~

.. image:: /mechs/images/williams_optos_front.jpg
.. image:: /mechs/images/williams_optos_back.jpg

In most platforms with direct inputs you can directly connect a receiver to an
input.
You connect the collector to the input (``C``) and the emitter (``E``) to ground.
Consult the documentation of your hardware platform for details.

For the transmitter connect the kathode (``K``) to ground and the anode (``A``) to a
current limiting resistor. Connect the resistor to power. DO NOT omit the
resistor to power without any current limiting or it will break/burn.

If your supply voltage is 5V you probably a 56ohm or 68ohm resistor at 1/2watt
in line with your sender (assuming a forward voltage of 1.7V and 50mA forward
current).
For 12V you need a 220ohm at 1 watt which will get very hot (do not use a
standard 1/2watt resistor).

Part numbers:

* Transmitter: A16908 or A14231
* Receiver: A16909 or A14232

Diodes used (in case you need to replace them):

* Transmitter: QED123
* Receiver: QSD124 or QSD124A4R0 (Pinball part numbers: 5163-14114-00 or 5163-12732-00)

Data East/Sega/older Stern optos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`TODO: Add a picture of those transceivers </about/help_us_to_write_it>`

Data East/Sega and later Stern used a diode which can serve as either
transmitter or receiver called "transceiver".
The advantage of this solution is that you only need one type of parts.
Electronically they work similar to Williams/Bally optos.

Part numbers:

* Transceiver: 500-6775-00/500-6775-01 or 500-6747-00

Stern Spike optos
~~~~~~~~~~~~~~~~~

Labels on Stern Spike optos looks different but they work similarly:

.. image:: /mechs/images/spike_optos_front.jpg

On the transmitter (left) connect ``+5`` to 5V and ``G`` to GND.
A current limiting resistor is not required since it is embedded on the sender.

The receiver also connects ``+5`` to 5V and ``G`` to GND.
Additionally, connect signal ``S`` to your input.

Part numbers:

* Transmitter: 520-6940-00/515-0215-00
* Receiver: 520-6940-01/515-0215-01

Multimorphic optos:
~~~~~~~~~~~~~~~~~~~

.. image:: /mechs/images/multimorphic_optos.jpg

Multimorphic produces and sells optos with a JST connector.
The transmitter contains a current limiting resistor for 12V (you only have to
connect one of the 12V and GND pins). You don't need an additional resistor
but you are also bound to 12V. They might work at 5V but the range will be much
lower.

Part numbers:

* Transmitter: PCBA-0019-EO03, PCBA-0019-EI03, PCBA-0020-CI03, PCBA-0020-CO03
* Receiver: PCBA-0021-EI03, PCBA-0021-CI03, PCBA-0021-EO03, PCBA-0021-CO03

Config
------

You can configure a normally closed opto like this:

.. code-block:: mpf-config

   switches:
      trough1:
         number: 81	# number depends on your platform
         type: 'NC'	# normally closed
      orbit_opto:
         number: 23	# number depends on your platform
         type: 'NC'	# normally closed


See :doc:`/config/switches` for details about the config options.
