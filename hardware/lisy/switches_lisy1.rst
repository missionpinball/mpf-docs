Configuring Switches with LISY1
===============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

LISY1 supports the System 1 switch matrix which consists of a maximum of 40
switches.
The switch number in the manual of your machine can be used within MPF.
However, some of the switches in Gottlieb System 1 games are **not** part of the
switch matrix.
These are the outhole switch, the SLAM switch and the "RESET" switch on the
board itself.
The ``mpfserver`` for LISY1 is numbering these switches in the same way as
pinmame does it:

* SLAM: #76
* Outhole: #66
* Reset: #56

.. note::

   As the SLAM switch is usually closed, the logic is inverted here.
   A closed SLAM switch is interpreted as open within ``mpfserver`` and does
   not have to be configured as normally closed ``NC`` in MPF.

You can start with this config:

.. code-block:: mpf-config

   switches:
     slam:
       number: 76
     outhole:
       number: 66
     reset:
       number: 56

Then just add your switches according to the manual of your machine.
See :doc:`/config/switches` for more details about switches.

What if it did not work?
------------------------

Have a look at our :doc:`LISY troubleshooting guide <troubleshooting>`.
