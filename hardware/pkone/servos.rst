How to configure servos (Penny K Pinball PKONE)
===============================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/servos`                                                        |
+------------------------------------------------------------------------------+

You can drive up to four servos from any PKONE Extension board.

Overview video about :doc:`servos </mechs/servos/index>`:

.. youtube:: wA6KEODwQ5w


number:
-------

When you're using PKONE Extension boards, coils plug into individual Extension boards.
Then the Extension boards are connected together in a chain to the controller.

.. image:: /hardware/images/pkone-extension.png

The ``number:`` setting for each servo is its board's Address ID number in the
PKONE chain, then the dash, then the servo output number (11-14).

.. code-block:: mpf-config

   servos:
     servo_1:
       number: 0-11    # Extension board with Address ID 0, servo 11 (the first one)
     some_other_servo:
       number: 2-14    # Extension board with Address ID 2, servo 14

Notes:

   * The PKONE Extension board Address ID switches can be set from 0 to 7.
   * Servos are numbered from 11 to 14 on the PKONE Extension board and not from 1 to 4.

All the servo config options are explained in-depth in the :doc:`servos: section </config/servos>`
of the config file reference.

What if it did not work?
------------------------

Have a look at our :doc:`PKONE troubleshooting guide <troubleshooting>`.
