Configuring your machine for OPP
================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/opp`                                                           |
+------------------------------------------------------------------------------+

1. Configure the Hardware platform for OPP
------------------------------------------

To use MPF with OPP, you need to configure your platform as *opp*,
like this:

.. code-block:: mpf-config

    hardware:
      platform: opp


2. Configure the OPP-specific hardware settings
-----------------------------------------------

When you use OPP hardware with MPF, you also need to add an ``opp:``
section to your machine-wide config which contains some OPP-
specific hardware settings. MPF's default config file
(*mpfconfig.yaml*) contains enough default settings to get you up and
running. The only thing you absolutely have to configure is your
ports.

Understanding OPP hardware ports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Even though OPP controllers are USB devices, they use "virtual"
COM ports to communicate with the host computer running MPF. On your
computer, if you look at your list of ports and then plug-in your
OPP controller, you will see a new port appear. The exact
names and numbers of these ports will vary depending on your computer
and what else you've plugged in in the past.

Note: USB to serial converters add latency when communicating between
the host computer, and the target device.  It probably will not matter,
but if given the choice between a "real" serial port, and a USB-serial
port converter, the "real" serial port will have less latency.  The
real serial port must use 5V signal levels when talking to OPP hardware.

Adding the port to your config file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you're using an OPP controller, you need to add the serial port to
your MPF config. So if you plug in the OPP controller and see a port
such as *COM7* appear, you'd set your config like this:

.. code-block:: mpf-config

    opp:
      ports: COM7

Full details of the port options as well as the other options
available here are in the ``opp:`` section of the configuration
file reference. Note that if you're using Windows and you have COM
port numbers greater than 9, you may have to enter the port names like
this: ``\\.\COM10`` ``\\.\COM11`` ``\\.\COM12``, etc. (It's a Windows
thing. Google it for details.) That said, it seems that Windows 10 can
just use the port names like normal: ``com10, com11, com12``, so try
that first and then try the alternate format if it doesn't work.
On Linux, the port usually is ``/dev/ttyACM0`` or ``/dev/ttyACM1``.
On Mac, look for some ``/dev/cu.modemXXXX`` device.

What if it did not work?
------------------------

Have a look at our :doc:`OPP troubleshooting guide <troubleshooting>`.
