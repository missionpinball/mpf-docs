How to update the Firmware of the P-Roc or P3-Roc
=================================================

If you experience problems around hardware rules or such consider upgrading
your P/P3-Roc firmware.
Sometimes bugs in the firmware get fixed or stuff becomes more robust.
For some known cases MPF will crash intentionally and tell you to upgrade but
there might be cases which we do not know.

Finding out the current firmware version
----------------------------------------

You can find out your current firmware version using ``mpf hardware scan``:


.. code-block:: console

   $ mpf hardware scan

   Firmware Version: 2 Firmware Revision: 6 Hardware Board ID: 1
   SW-16 boards found:
    - Board: 0 Switches: 16 Device Type: A3 Board ID: 0
    - Board: 1 Switches: 16 Device Type: A3 Board ID: 1
    - Board: 2 Switches: 16 Device Type: A4 Board ID: 2

In this example the P3-Roc is running firmware ``2.6``.

Upgrading the firmware of the P-Roc or P3-Roc
---------------------------------------------

1. Go to the `Multimorphic Customer Support Site <https://www.multimorphic.com/support/projects/customer-support/wiki/Firmware>`_.
2. If you do not yet have an account create one. Otherwise login.
3. Download the firmware upgrade tool and the newest firmware for your controller.
4. Perform the upgrade as described by Multimorphic

What if it did not work?
------------------------

In case you got troubles with the upgrade we recommend you to contact the
Multimorphic support team.
If you got a problem with MPF have a look at the :doc:`troubleshooting`
section.
