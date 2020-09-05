How to use install drivers & configure COM ports (FAST Pinball)
===============================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/fast`                                                          |
+------------------------------------------------------------------------------+

This guide explains how to configure MPF to work with a FAST Pinball
controller. It applies to all three of their models—the Core, Nano, and WPC
controllers.

1. Install the FAST USB driver
------------------------------

FAST Pinball controllers use a USB chip from FTDI, so you need to download and
install the FTDI driver. It's pretty simple. Go to this
`this page <http://www.ftdichip.com/Drivers/VCP.htm>`_ and scroll down to the
VCP Drivers section and download the driver for your OS. If you're using Windows,
we think it's easier to use the "setup executable" they link to in the comments.

Once this is done, when you plug in and power on your FAST controller, you
should see some kind of notification that new hardware has been detected. What
exactly you see will depend on which FAST controller you’re using and what OS
you have. For example, here’s what happens when you plug a FAST WPC controller
into Windows 10 for the first time (after you’ve installed the FTDI driver):

.. image:: /hardware/images/fast-ftdi-driver.png

(This is just a progress bar which shows Windows configuring the drivers. You
don’t have to click anything to get it started, and it should only take 5-10
seconds. It will only happen the first time you plug in the hardware.)

2. Configure your hardware platform for FAST
--------------------------------------------

To use MPF with a FAST, you need to configure your platform as ``fast`` in your
machine-wide config file, like this:

.. code-block:: mpf-config

    hardware:
      platform: fast

    fast:
      driverboards: fast

You also need to configure the `driverboards:` entry for what kind of
driver boards you’re controlling.

Use ``driverboards: fast`` if you're using FAST I/O boards (like the 3208, 0804,
etc.), or use ``driverboards: wpc`` if you're using an existing WPC or Snux
System 11 driver board.

3. Find the FAST COM ports
--------------------------

Even though the FAST controllers are USB devices, they use "virtual" COM ports
to communicate with the host computer running MPF. On your computer, if you
look at your list of ports and then connect and power on your FAST controller,
you will see 4 new ports appear. The exact names and numbers of these ports
will vary depending on your computer, what other devices you have, and which
port you plug the FAST controller into, but the order of which ports do what
is the same everywhere:

+ First (lowest numbered) port: **DMD Processor**
+ Second: **NET processor** (the main processor)
+ Third: **RGB LED processor**
+ Fourth: **Unused** (available for your own custom use!)

Note that the FAST Nano controller does not have a DMD processor, so
on that device, both the first and fourth ports are unused.

You need to tell MPF which ports are used for the FAST Controller, and the
first step to doing that is to figure out what the port names are on your
system:

Finding the COM ports on Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On Windows, it's easiest to use the Device Manager. Right-click on the Start
button (or whatever it's called now) and choose "Device Manager" from the
popup menu.

Then expand the "Ports (COM & LPT)" menu section to see which ports the FAST
Controller is using. The easiest way to do this is to open the Device Manager
to that section, then plug your FAST Controller in (or power it on) and just
see which four port names appear.

The port names will start with "COM" and then be a number, and there will be
four consecutive numbers to represent the four FAST ports.

Finding the COM ports on Max or Linux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On Mac or Linux, it's easiest to find the port numbers via the terminal window
(or console window). To do that, open a new window and run the following
command:

::

   ls /dev/tty.*

This will list all the devices whose names begin with "tty".

The four FAST ports will have the name that starts with "tty.usbserial-", then
a number, then a letter A-D. (The number will be different on every system.)
The port ending with the "A" is the first port, the "B" is the second, etc.

For example, the four FAST ports might be something like on MAC:

::

   /dev/tty.usbserial-141A
   /dev/tty.usbserial-141B
   /dev/tty.usbserial-141C
   /dev/tty.usbserial-141D

On linux it would look like this:

::

   /dev/ttyUSB0
   /dev/ttyUSB1
   /dev/ttyUSB2
   /dev/ttyUSB3

If you have multiple FAST devices they will enumerate more or less randomly
dependent on the order they are plugged in. Unfortunately, the USB devices
do not contain any serial number. However, we can pin them based on the USB
port they are plugged into. On linux this can be achieved using a UDEV rules
such as this:

::

   SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6011", ENV{ID_PATH_TAG}=="pci-0000_00_14_0-usb-0_12_1_0", SYMLINK+="ttyDMD1"

The device will then be available as /dev/ttyDMD1. You can run the following
command while plugging in the device to get the relevand ID_PATH_TAG (and
also idVendor and idProduct in case they changed with other revisions):

::

   udevadm monitor --property


4. Add the ports to your config file
------------------------------------

Next you need to add the ports to your machine config file. To do this,
create a new section called ``fast:``, and then add a ``ports:`` setting under
it.

Then if you have a FAST Core or WPC controller, enter the names of the first
three ports. If you have a FAST Nano controller, enter the names of the middle
two ports (the second and third, since the first isn't used on a Nano).

So an example for Windows might look like this:

::

    fast:
        ports: com3, com4, com5

And an example for Mac or Linux might look like this:

::

   fast:
      ports: /dev/tty.usbserial-141B, /dev/tty.usbserial-141C

Note that if you have a FAST Core controller but you're not actually using the
hardware DMD, then you don't have to enter the first port in your config.
(Same is true if you're not using the LED controller.) MPF queries each port in
this list to find out what's actually on the other end and then sets itself
up appropriately.

Note that if you're using a version of Windows before Windows 10 and you have
COM port numbers greater than 9, you will have to enter the port names like
this: ``\\.\COM10, \\.\COM11, \\.\COM12``, etc. (It's a Windows
thing. Google it for details.)

There are more settings in the :doc:`/config/fast` section of the machine
config that we have not covered here, but the ports are the bare minimum you
need to get up and running.

5. Configure your watch dog timeout
-----------------------------------

FAST Pinball controllers have the ability to use a :term:`watch dog` timer.
This is enabled by default with a timeout of 1 second. If you would like to
disable this, or you'd like to change the timeout, you can do so in the
``fast:`` section of your machine-wide config.

::

   fast:
      ports: com3, com4, com5  # or whatever your ports are
      watchdog: 1000

The ``watchdog:`` setting is the timeout in milliseconds. Use 0 to disable it.

Note that at this time, FAST Pinball controllers only use the watch dog for
the NET processor (which controls stuff on the IO boards, like coils). The
watch dog is not used for the DMD or LEDs.

What if it did not work?
------------------------

Have a look at our :doc:`FAST troubleshooting guide <troubleshooting>`.
