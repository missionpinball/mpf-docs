---
title: How to use install drivers & configure COM ports (Penny K Pinball
  PKONE)
---

Related Config File Sections:

* [hardware:](../../config/hardware.md)
* [pkone:](../../config/pkone.md)

This guide explains how to configure MPF to work with a Penny K Pinball
controller (PKONE NANO) and add-on boards.

## 1. Install the USB driver

PKONE Pinball controllers use a USB chip from STM. On most operating
systems the driver is built-in (Windows 10, Linux, MacOS), so there is
no need to download and install the STM driver.

Once this is done, when you plug in and power on your PKONE controller,
you should see some kind of notification that new hardware has been
detected. What exactly you see will depend on what OS you have.

TODO: Finish this section

## 2. Configure your hardware platform for PKONE

To use MPF with a PKONE controller system, you need to configure your
platform as `pkone` in your machine-wide config file, like this:

``` yaml
hardware:
  platform: pkone
```

## 3. Find the PKONE COM port

Even though the PKONE controllers are USB devices, they use "virtual"
COM ports to communicate with the host computer running MPF. On your
computer, if you look at your list of ports and then connect and power
on your PKONE controller, you should see a new port appear. The exact
name and number of this port will vary depending on your computer, what
other devices you have, and which port you plug the PKONE controller
into.

You need to tell MPF which port is used for the PKONE Controller, and
the first step to doing that is to figure out what the port names are on
your system:

### Finding the COM ports on Windows

On Windows, it's easiest to use the Device Manager. Right-click on the
Start button (or whatever it's called now) and choose "Device
Manager" from the popup menu.

Then expand the "Ports (COM & LPT)" menu section to see which ports
the FAST Controller is using. The easiest way to do this is to open the
Device Manager to that section, then plug your PKONE Controller in (or
power it on) and just see which port name appears.

The port name will start with "COM" and then be a number.

### Finding the COM ports on Max or Linux

On Mac or Linux, it's easiest to find the port numbers via the terminal
window (or console window). To do that, open a new window and run the
following command:

    ls /dev/tty*

This will list all the devices whose names begin with "tty".

The PKONE port will have the name that starts with "/dev/cu.usbmodem",
then a number. (The number will be different on every system.)

For example, the PKONE port might be something like on MAC:

    /dev/cu.usbmodem (141)

On linux it would look like this:

    /dev/ttyASM0

## 4. Add the port to your config file

Next you need to add the port to your machine config file. To do this,
create a new section called `pkone:`, and then add a `port:` setting
under it.

Then if you have a PKONE Nano controller, enter the name of the port.

So an example for Windows might look like this:

    pkone:
        port: com3

And an example for Mac or Linux might look like this:

    pkone:
       port: /dev/cu.usbmodem

Note that if you're using a version of Windows before Windows 10 and
you have COM port numbers greater than 9, you will have to enter the
port names like this: `\\.\COM10, \\.\COM11, \\.\COM12`, etc. (It's a
Windows thing. Google it for details.)

There are more settings in the [pkone:](../../config/pkone.md) section of the machine config that we have not covered here,
but the port is the bare minimum you need to get up and running.

## What if it did not work?

Have a look at our
[PKONE troubleshooting guide](../../troubleshooting/index.md).
