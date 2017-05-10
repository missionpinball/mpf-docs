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

If you got a newer version of Spike the CN2/DBGU connector might
be unpopulated. In this case you can also attach an FTDI USB Serial
Adapter and connect it to another USB serial adapter. This only works
with FTDI chips since Spike only supports those. However, on the other
side any chip will work.

First, connect GND between the adapters. Then connect RX to TX and TX to RX.
