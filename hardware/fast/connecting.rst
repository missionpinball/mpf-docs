Connecting FAST to your Computer
================================

This page is about connecting the FAST system to your computer.
It roughly covers connecting the bus between the nodes.
For electronic details see the
`FAST section in the pinballmakers.com Wiki <http://pinballmakers.com/wiki/index.php/Fast>`_.

FAST Nano
---------

Connect your FAST NANO controller to your PC using USB.

.. image:: /hardware/images/fast-nano.png

Then connect the OUT port of your NANO to the IN port of your first node board.
Consequently, connect the OUT port of the first node to the IN port of your
second board. Connect the OUT port of the last board back to the IN port of
your NANO.

The ``number:`` setting for each driver/switch is its board's position number in the
chain, then the dash, then the driver/switch number. Note that the position
number starts with zero, so the first IO board in the chain is 0, the second
is 1, etc.

Node boards
-----------

Fast offers three different types of node boards:

0804 - 8 Switches, 4 Drivers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /hardware/images/fast-io-0804.png

1616 - 16 Switches, 16 Drivers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /hardware/images/fast-io-1616.png

3208 - 32 Switches, 08 Drivers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /hardware/images/fast-io-3208.png


Verify Connected Boards via mpf hardware scan
---------------------------------------------

You can run :doc:`mpf hardware scan </running/commands/hardware>` to see all
connected node boards:

.. code-block:: console

   $ mpf hardware scan

   NET CPU: NET FP-CPU-002-1 01.03
   RGB CPU: RGB FP-CPU-002-1 00.89
   DMD CPU: DMD FP-CPU-002-1 00.88

   Boards:
   Board 0 - Model: FP-I/O-3208-2    Firmware: 01.00 Switches: 32 Drivers: 8
   Board 1 - Model: FP-I/O-0804-1    Firmware: 01.00 Switches: 8 Drivers: 4
   Board 2 - Model: FP-I/O-1616-2    Firmware: 01.00 Switches: 16 Drivers: 16
   Board 3 - Model: FP-I/O-1616-2    Firmware: 01.00 Switches: 16 Drivers: 16

If your boards do not show up checkout our
:doc:`FAST troubleshooting guide <troubleshooting>`.


On Linux: Add udev rules to ensure persistent device names
----------------------------------------------------------

If you have more than one ttyUSB device connected to your PC (e.g. the FAST
Nano and a FAST DMD) you can assign a name to your ports
based on the USB port they are connected to.

First identify the port of your FAST hardware. Usually it should be
``/dev/ttyUSB0`` or ``/dev/ttyUSB5``.

Then run ``udevadm info`` on your port:

.. code-block:: shell

   udevadm info /dev/ttyUSB0

This will show you the ``DEVPATH``. Now replace the last part ``ttyUSBX`` with
an asterisk and add an udev rules like this in ``/etc/udev/rules.d/fast.rules``:

::

   SUBSYSTEM=="tty", ACTION=="add", DEVPATH=="/devices/pci0000:00/0000:00:14.0/usb1/1-4/1-4:1.1/*", SYMLINK+="ttyNET", GROUP="adm", MODE="0660"

After a reboot you should get a ``/dev/ttyNET`` device if you connect a FAST
device to that specific USB port. You can use that port in your config.

What if it did not work?
------------------------

Have a look at our :doc:`FAST troubleshooting guide <troubleshooting>`.
