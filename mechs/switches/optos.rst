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

:doc:`TODO: Add a picture of a pair of optos. </about/help_us_to_write_it>`

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

In most platforms with direct inputs you can directly connect a receiver to an
input.
You connect the collector to the input (C) and the emitter (E) to ground.
Consult the documentation of your hardware platform for details.

For the sender connect the kathode (K) to ground and the anode (A) to a
current limiting resistor. Connect the resistor to power. DO NOT omit the
resistor to power without any current limiting or it will break/burn.

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
