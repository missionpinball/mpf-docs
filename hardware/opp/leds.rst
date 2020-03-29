OPP LEDs
========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+

OPP hardware can directly drive LED strips.  This features is
currently being developed.  Documentation will be added as the
feature becomes more mature.

LEDs work similar to matrix lights (board 1, LED 1):

.. code-block:: mpf-config

    lights:
      some_led:
        number: 1-1
        subtype: led

