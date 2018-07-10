How to use native I2C on Linux (SMBUS2)
=======================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+

MPF can control I2C devices on Linux using the Python smbus2 extension.


1. Install the smbus2 extension
-------------------------------

Install ``smbus2`` via pip:

::

   pip3 install smbus2


2. Figure out which bus to use
------------------------------

* Some boards such as the Raspberry Pi have native I2C buses. Figure out which
  bus to use and make sure MPF has sufficient permissions to use it (Alternatively,
  you can also controll the I2C on the RPi remotely using the
  :doc:`RPi </hardware/rpi/index>` platform).

* You can build an adapter to tap I2C out of a spare VGA, DVI or HDMI port:
  http://www.instructables.com/id/Worlds-Cheapest-I2C-I-Squared-C-Adapter/

* Commercial USB-I2C adapters exist but are usually very expensive

* You can `build your own USB-I2C adapter <https://github.com/harbaum/I2C-Tiny-USB>`_.
  Hardware can be bought ready-made for less than 10 bucks.


3. Connect your hardware
------------------------

Connect the hardware to the bus. This will be at least SDA, SCL and ground.
Usually, you have to power your device somehow and in a lot of cases this
power can be provided from the controller.


4. Set your I2C devices to use the "smbus2" platform
----------------------------------------------------

Next you need to configure I2C in MPF to use the ``smbus2`` platform.
By default, all types of devices are assumed to be using the same platform that
you have set in the :doc:`/config/hardware` of your machine config file. So if
your platform is set to ``fast``, MPF assumes your I2C devices are connected to a FAST
controller, and if your platform is set to ``p3_roc``, MPF assumes
your I2C devices are connected to the P3-Roc board.

To configure MPF to use native I2C, you can add an entry to the
``hardware:`` section of your machine config to tell it to override the default
platform for your I2C devices and to instead use the ``smbus2`` platform, like this:

.. code-block:: mpf-config

    hardware:
        platform: p_roc
        driverboards: pdb
        i2c: smbus2

See the :doc:`/hardware/platform` guide for more information about setting
device-specific default platforms versus overriding the platform for individual
devices.

5. Understanding I2C numbering
------------------------------

When using I2C addresses in I2C devices smbus2 will interpret those as
bus-address. If you only provide an address it will use bus 0. On Linux
bus 0 will ususally be /dev/i2c-0, 1 will be /dev/i2c-1 and so on.


