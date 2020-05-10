Connecting a System6 to System11c Machine to APC
================================================

1. Replace your original MPU and driver board with APC
------------------------------------------------------

See the `APC wiki <https://github.com/AmokSolderer/APC/wiki>`_ for build up
and installation instructions.


2. Configure APC to Run MPF
---------------------------

Select USB Control in APC to ensure that MPF can connect.
If you did not install an SD card (not needed for MPF if you do not want to use
the sound card of APC) this should be the default.


3. Connect your PC running MPF to APC via USB
---------------------------------------------

Connect APC to your PC via USB.
The arduino on APC will behave as a USB-serial device and your PC should show
a new serial device.
For the USB connection no special driver Software nor a special USB cable is needed,
a "normal" USB A-B cable will do the job.
APC uses the :doc:`LISY protocol </hardware/lisy/protocol>` which is why we
have to configure it similarly.

Add/update the following sections in your machine config:

.. code-block:: mpf-config

  hardware:
    platform: lisy
  lisy:
    connection: serial
    port: com1               # replace this with your com port
    baud: 115200

Once connected to the host computer, it will (hopefully) identify a new serial device.
This is usually ``COMx`` on windows or ``/dev/ttyUSBx`` on Linux.

4. Power up APC
---------------

Power up your system and enjoy.

5. Start MPF
------------

Start MPF and MPF-MC on you PC:

.. code-block:: shell

   mpf both

What if it does not work?
-------------------------

Have a look at the :doc:`LISY troubleshooting guide </hardware/lisy/troubleshooting>`.
