Connecting OPP to your computer
===============================

Connect the OPP board to your computer via USB.
Make sure that your OPP chains do not get too long since the serial throughput
is limited per chain. You can connect multiple chains.

On Linux: Blacklist cytherm module
----------------------------------

If you are using OPP hardware on linux you should blacklist the cypress
thermometer because it conflicts with OPP.

In ``/etc/modprobe.d/blacklist.conf`` add:

::

  blacklist cytherm

If blacklist.conf does not exist, just create a new empty file as root.
Afterwards, reboot your PC.

On Linux: Add udev rules to ensure persistent device names
----------------------------------------------------------

If you have more than one ttyACM connected to your PC (e.g. multiple OPP
chains or other USB-serial adapters) you can assign a name to your ports
based on the USB port they are connected to.

First identify the port of your OPP hardware. Usually it should be
``/dev/ttyACM0`` or ``/dev/ttyACM1``.

Then run ``udevadm info`` on your port:

.. code-block:: shell

   udevadm inf /dev/ttyACM0

This will show you the ``DEVPATH``. Now replace the last part ``ttyACMX`` with
an asterisk and add an udev rules like this in ``/etc/udev/rules.d/opp.rules``:

::

   SUBSYSTEM=="tty", ACTION=="add", DEVPATH=="/devices/pci0000:00/0000:00:14.0/usb1/1-4/1-4:1.1/*", SYMLINK+="ttyOPP1", GROUP="adm", MODE="0660"

After a reboot you should get a ``/dev/ttyOPP1`` device if you connect an OPP
device to that specific USB port. You can use that port in your config.

On Ubuntu: Stop ModemManager
----------------------------

ModemManager tries to initialise all ``/dev/ttyACMxx`` devices as modem.
That might cause delays after attaching OPP hardware and might also leave the
hardware in a weird state with garbage on the bus.
If you do not use any modems just disable and stop ModemManager:

.. code-block:: shell

   sudo systemctl disable ModemManager
   sudo systemctl stop ModemManager
