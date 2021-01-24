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

.. warning::

   DO NOT POWER DOWN THE P/P3-ROC OR YOUR PC DURING THIS PROCESS!

1. Log on to your account on Multimorphic.com (or create one) and go to the
   `Firmware page on the Multimorphic Wiki <https://www.multimorphic.com/support/projects/customer-support/wiki/Firmware>`_.
2. Read the Multimorphic upgrade instructions (they know their boards better than we do)
3. Download the firmware for your board (either P-Roc or P3-Roc)
4. Get the Upgrade tool

   * On Windows: Download the ``pinprocfw.exe`` from the Multimorphic site as well
   * On Linux: Change to ``mpf-debian-installer/libpinproc/bin``
   * On Mac: Change to ``libpinproc/bin`` (likely in ``~/proc/libpinproc/bin`` if you followed the installer)

5. Run the upgrade tool: ``./pinprocfw path/to/the/firmware/file``


What if it did not work?
------------------------

In case you got troubles with the upgrade we recommend you to contact the
Multimorphic support team.
If you got a problem with MPF have a look at the :doc:`troubleshooting`
section.
