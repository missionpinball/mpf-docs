Configuring Lights in LISY
==========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+

Lights in LISY can be configured as :doc:`lights </config/lights>`
using their number from the game manual.

This is an example:

.. code-block:: mpf-config

   lights:
     your_light:
       number: 03

There are some features in the light list like the ``game_over_relay`` which
are not real lights. Those can be configured as
:doc:`digital outputs </config/digital_outputs>`.
See :doc:`flippers_slings_popbumpers` for details about the
``game_over_relay``.

What if it did not work?
------------------------

Have a look at our :doc:`LISY troubleshooting guide <troubleshooting>`.
