Connecting your computer to the Stern SPIKE CPU node
====================================================

MPF connects to the SPIKE CPU node via a serial connection. If you're running
MPF on a regular computer, you'll need to buy a USB-to-serial adapter. There
are lots of them, most for less than $10, and they're all pretty much the same.

Some examples that should work (though we don't guarantee it and we're happy to
hear feedback or recommendations):

https://www.amazon.com/FICBOX-CP2102-Serial-Downloader-Arduino/dp/B01CU12324/
https://www.amazon.com/HiLetgo-CP2102-Module-Serial-Converter/dp/B00LODGRV8
https://www.amazon.com/HiLetgo-Ft232rl-Serial-Adapter-Arduino/dp/B00IJXZQ7C
https://www.adafruit.com/products/3309
https://www.sparkfun.com/products/12731
https://www.sparkfun.com/products/13830

Make sure you have a 3.3v adapter (or that your adapter can be set for 3.3v).

.. note::  If you're using a Raspberry Pi, you can use its built-in serial pins
   and don't need a USB-to-serial adapter.


Connecting using DBGU
---------------------

Connect the USB serial adapter to the DBGU header (CN2) on the SPIKE CPU node.

Pins are marked GND, RX, TX. You do not need more than these.

TODO add a photo and more detailed pinout instructions.


Connect using two USB-Serial Adapters
-------------------------------------

Newer versions of the SPIKE CPU node do not have a connector attached to the CN2/DBGU header.
(The board is the same, but you see a blank spot instead of the plug-in connector attached.)

In this case, you can solder on your own connector, *or* you can buy two USB serial adapters and
then use the USB connection on the SPIKE CPU node.

The one you connect to the SPIKE CPU node needs to have an actual FTDI brand chip because the
FTDI drivers are included in the code on the SPIKE board. The second adapter for your computer
can be any brand since it's easy to install whatever drivers it needs on your computer. Whatever
serial port appears on your computer when you plug in this adapter is the port name you'll use
in your machine config.

These two adapters will have connectors or headers on them that you need to connect together.
Connect the "RX" (receive) from one to the "TX" (transmit) on the other and vice-versa. Also
connect the grounds (possible labeled "GND") together. It's probably a good idea to twist the
wires together to reduce interference, especially if your wires are more than a few inches long.

The following diagram illustrates how everything fits together:

.. image:: /hardware/images/spike_usb_to_usb.jpg
