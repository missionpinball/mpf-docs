---
title: How to use native I2C on Linux (SMBUS2)
---

# How to use native I2C on Linux (SMBUS2)


Related Config File Sections:

* [hardware:](../config/hardware.md)

MPF can control I2C devices on Linux using the Python smbus2_asyncio
extension.

## 1. Install the smbus2_asyncio extension

Install `smbus2_asyncio` via pip:

    pip3 install smbus2_asyncio

## 2. Figure out which bus to use

* Some boards such as the Raspberry Pi have native I2C buses. Figure
    out which bus to use and make sure MPF has sufficient permissions to
    use it (Alternatively, you can also controll the I2C on the RPi
    remotely using the [RPi](rpi.md) platform).
* You can build an adapter to tap I2C out of a spare VGA, DVI or HDMI
    port:
    <http://www.instructables.com/id/Worlds-Cheapest-I2C-I-Squared-C-Adapter/>
* Commercial USB-I2C adapters exist but are usually very expensive
* You can [build your own USB-I2C
    adapter](https://github.com/harbaum/I2C-Tiny-USB). Hardware can be
    bought ready-made for less than 10 bucks. Atiny85 based boards can
    be bought at Adafruit as
    [Trinket](https://www.adafruit.com/product/1501) (and elsewhere just
    google it).

This is an adafruit trinket used as USB-I2C adapter for an
[MMA8451-based accelerometer](mma8451.md):

![image](/docs/hardware/images/mma8451-i2c-usb-accelerometer.jpg)

## 3. Connect your hardware

Connect the hardware to the bus. This will be at least SDA, SCL and
ground. Usually, you have to power your device somehow and in a lot of
cases this power can be provided from the controller.

## 4. Set your I2C devices to use the "smbus2" platform

Next you need to configure I2C in MPF to use the `smbus2` platform. By
default, all types of devices are assumed to be using the same platform
that you have set in the [hardware:](../config/hardware.md) of your machine config file. So if your platform is set to
`fast`, MPF assumes your I2C devices are connected to a FAST controller,
and if your platform is set to `p3_roc`, MPF assumes your I2C devices
are connected to the P3-Roc board.

To configure MPF to use native I2C, you can add an entry to the
`hardware:` section of your machine config to tell it to override the
default platform for your I2C devices and to instead use the `smbus2`
platform, like this:

``` mpf-config
hardware:
  i2c: smbus2
```

See the [Mixing-and-Matching hardware platforms](platform.md) guide for
more information about setting device-specific default platforms versus
overriding the platform for individual devices.

## 5. Understanding I2C numbering

When using I2C addresses in I2C devices smbus2 will interpret those as
bus-address. If you only provide an address it will use bus 0. On Linux
bus 0 will ususally be /dev/i2c-0, 1 will be /dev/i2c-1 and so on.

## 6. Add udev rules if you have multiple i2c devices

If you have more than one i2c device connected to your PC via USB you
can assign a name to your ports based on the USB port they are connected
to.

First identify the port of your I2C hardware. Usually it should be
`/dev/i2c0` or `/dev/i2c1`.

Then run `udevadm info` on your port:

``` shell
udevadm info /dev/i2c0
```

This will show you the `DEVPATH`. Now replace the last part `i2cX` with
an asterisk and add an udev rules like this in
`/etc/udev/rules.d/i2c.rules`:

    SUBSYSTEM=="i2c-dev", ACTION=="add", DEVPATH=="/devices/pci0000:00/0000:00:14.0/usb1/1-3/1-3.1/1-3.1:1.0/*", SYMLINK+="i2c-front", GROUP="adm", MODE="0660

After a reboot you should get a `/dev/i2c-front` device if you connect
an i2c device to that specific USB port. You can use that port in your
config.

## What if it did not work?

Have a look at our
[hardware troubleshooting guide](troubleshooting_hardware.md).
