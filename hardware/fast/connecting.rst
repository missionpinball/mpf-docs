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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /hardware/images/fast-io-0804.png

1616 - 16 Switches, 16 Drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /hardware/images/fast-io-1616.png

3208 - 32 Switches, 08 Drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /hardware/images/fast-io-3208.png

On Linux: Add udev rules to ensure persistent device names
----------------------------------------------------------

If you have more than one ttyUSB device connected to your PC (e.g. the FAST
Nano and a FAST DMD) you can assign a name to your ports
based on the USB port they are connected to.

First identify the port of your FAST hardware. Usually it should be
``/dev/ttyUSB0`` or ``/dev/ttyUSB5``.

Then run ``udevadm info`` on your port:

.. code-block:: shell

   udevadm inf /dev/ttyUSB0

This will show you the ``DEVPATH``. Now replace the last part ``ttyUSBX`` with
an asterisk and add an udev rules like this in ``/etc/udev/rules.d/fast.rules``:

::

   SUBSYSTEM=="tty", ACTION=="add", DEVPATH=="/devices/pci0000:00/0000:00:14.0/usb1/1-4/1-4:1.1/*", SYMLINK+="ttyNET", GROUP="adm", MODE="0660"

After a reboot you should get a ``/dev/ttyNET`` device if you connect a FAST
device to that specific USB port. You can use that port in your config.
