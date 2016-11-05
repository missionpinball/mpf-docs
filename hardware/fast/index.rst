How to configure FAST Pinball
=============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/fast`                                                          |
+------------------------------------------------------------------------------+

This guide explains how to configure MPF to work with a FAST Pinball
controller. It applies to all three of their models—the Core, Nano, and WPC
controllers.

.. todo::
   This page needs to be updated for MPF 0.30 with the latest FAST
   changes

1. Install the FAST USB driver
------------------------------

FAST Pinball controllers use a USB chip from FTDI, so you need to download and install the FTDI driver. It's pretty
simple. Go to this `this page <http://www.ftdichip.com/Drivers/VCP.htm>`_ and scroll down to the VCP Drivers section and
download the Windows driver. The easiest one to use is the "setup executable" in the Comments section in the right-most
column.

Once this is done, when you plug in and power on your FAST controller, you should see some kind of notification that new
hardware has been detected. What exactly you see will depend on which FAST controller you’re using and what OS you have.
For example, here’s what happens when you plug a FAST WPC controller into Windows 10 for the first time (after you’ve
installed the FTDI driver):

.. image:: /hardware/images/fast-ftdi-driver.png

(This is just a progress bar which shows Windows configuring the drivers. You don’t have to click anything to get it
started, and it should only take 5-10 seconds. It will only happen the first time you plug in the hardware.)

Then if you go into your device manager, you should see four new COM ports appear. These are “virtual” COM ports that
your computer talks to via USB, and these are the ports that MPF uses to communicate with your FAST pinball controller.
These ports will disappear when you power off or unplug your FAST controller.

2. Configure your hardware platform for FAST
--------------------------------------------

To use MPF with a FAST, you need to configure your platform as ``fast`` in your machine-wide config file, like this:

::

    hardware:
        platform: fast
        driverboards: fast


You also need to configure the `driverboards:` entry for what kind of
driver boards you’re controlling: ``wpc`` for Williams WPC with the FAST WPC controller, or ``fast``
for FAST I/O boards like the 3208, 1616, or 0804 with the Core or Nano controllers.


3. Configuring the FAST-specific hardware settings
--------------------------------------------------

When you use FAST hardware with MPF, you also need to add a `fast: section </config/fast>`_
to your machine-wide config which contains some FAST-
specific hardware settings. MPF's default config file (
``mpfconfig.yaml``) contains enough default settings to get you up and
running. The only thing you absolutely have to configure is your
ports.



Understanding FAST hardware ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even though the FAST controllers are USB devices, they use "virtual"
COM ports to communicate with the host computer running MPF. On your
computer, if you look at your list of ports and then plug-in and turn
on your FAST controller, you will see 4 new ports appear. The exact
names and numbers of these ports will vary depending on your computer
and what else you've plugged in in the past. The mapping order of the
four ports is the same across all FAST controllers:


+ First (lowest numbered) port: DMD processor
+ Second: NET processor (the main processor)
+ Third: RGB LED processor
+ Fourth: Unused


Note that the FAST Nano controller does not have a DMD processor, so
on that device, both the first and fourth ports are unused. There are
transmit/receive headers on the FAST controller boards for the unused
ports, so you can develop your own hardware or plug in whatever you
want to the boards themselves and then just use the unused FAST ports
to connect to the computer. (Saves having to buy another $20 FTDI
breakout board!)



Adding the ports to your config file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're using a FAST Core or FAST WPC controller, you need to add
the first three to your MPF config. So if you plug in the Core or WPC
controller and see ports *com3*, *com4*, *com5*, and *com6* appear,
you'd set your config like this:


::


    fast:
        ports: com3, com4, com5


Note that if you're not actually using the hardware DMD, then you
don't have to enter the first port in your config. (Same is true if
you're not using the LED controller.) MPF queries each port in this
list to find out what's actually on the other end and then sets itself
up appropriately. If you're using a FAST Nano controller, you need to
add the the middle two ports that show up. So if you plug in the Nano
and see ports *com3*, *com4*, *com5*, and *com6* appear, you'd set
your config like this:


::


    fast:
        ports: com4, com5


Full details of the port options as well as the other options
available here are in the ` `fast:` section`_ of the configuration
file reference. Note that if you're using Windows and you have COM
port numbers greater than 9, you may have to enter the port names like
this: ``\\.\COM10, \\.\COM11, \\.\COM12``, etc. (It's a Windows
thing. Google it for details.) That said, it seems that Windows 10 can
just use the port names like normal: ``com10, com11, com12``, so try
that first and then try the alternate format if it doesn't work.


4. Configuring Switches
-----------------------

For switches, you can use most of the settings as outlined in the :doc:`switches: <config/switches>`
section of the config file reference. There are only a few things that are FAST-specific:



number:
~~~~~~~

FAST switches are numbered sequentially, starting with zero, from the
IO board closest to the controller and then out from there. So if you
have a 1616 (16 switches) and then a 3208 (32 switches), the switches
from the 1616 will be numbered 0-15 and then the switches from the
3208 will be numbered 16-47. You can enter your FAST switch numbers as
either integers or hex, whichever is easiest for you. Some people like
hex because that's what the serial terminal shows when you hit
switches manually. Other people like integers because they're normal
humans. (You can specify whether your numbers will be in hex or
integer format in the ``fast: config_number_format:`` section of
your config file.)



connection:
~~~~~~~~~~~

FAST switches have an optional setting called connection: which is
used to specify whether the switches are connected locally to the FAST
controller or whether they're on the I/O board network. Currently the
only FAST controller that has local switches is the FAST WPC
controller for the switches in the WPC machine that connect directly
to it. Because of that, if your driverboards: setting is wpc, then MPF
will assume your switches are "local", and if your driverboards:
setting is fast, then MPF will assume your switches are network.
However if you make a cool mod that requires adding a FAST I/O board
to a WPC machine, then you can add connection: network to those
switches to differentiate them from the local WPC switches.



Debounce options
~~~~~~~~~~~~~~~~

FAST controllers have advanced capabilities when it comes to
debouncing switches. You can specify a debounce time (in milliseconds)
from 0 to 255 ms. This can be different for each switch, and it can be
different for debounce open versus debounce closed. By default, the
debounce settings will be whatever you have configured in the fast:
section of your machine configuration file, but you can add
debounce_open: and debounce_close: values to any of your switches to
fine-tune them. For example:

::

    switches:
        some_switch:
            number: 0a
            debounce_open: 12
            debounce_close: 6

5. Configuring coils & drivers
------------------------------

Coil and driver numbering with FAST I/O boards is similar to switch
numbering. The drivers are number in order, starting with zero, and
starting with the I/O board closest to the controller. Then they count
up from there. Also like switches, you can specify whether the number
format is in hex or int. And, also again like switches, FAST
controllers differentiate between local and network drivers. Local
drivers are used for WPC drivers, and network drivers are anything
connected to FAST I/O boards. Again these defaults are set
automatically based on your driverboards: setting.

Hold power
~~~~~~~~~~

When you "hold" a driver on in MPF, you can set the power level so you
don't burn up your coils. (In WPC machines, coils that were held one
ran with lower voltage, so they could be held on at 100% no problem.
But if you're building a new machine, it's probably easier to hold a
coil on at less than 100% power rather than getting another power
supply for lower hold voltage.) FAST controllers hold coils on with a
pulse-width modulation (pwm) mask which basically lets you configure
eight ones and zeros that correspond to each millisecond of a pattern
that's repeated every 8 milliseconds. In other words, if the pwm
pattern is 11001100, then the coil will be on for 2ms, then off for
2ms, then on for 2, etc... There are two ways to configure this in MPF
with FAST hardware. The first is to use the coil's "hold_power"
setting which is a numeric value between 0 and 8 which corresponds to
a power level. 0 is 0% power (e.g. "off"), 8 is 100% power (e.g.
"solid on), 4 is 50% power, 3 is 37.5% power, etc. To configure a coil
with a hold power value of less than 8 (full power), you simply set it
up like this:

::

    coils:
        some_coil:
            number: 1b
            hold_power: 3

Pulse power
~~~~~~~~~~~

The FAST hardware also has the ability to specify the "pulse power".
Pulse power is like hold power, though it's only used during the
coil's initial pulse time. For example, consider the following
configuration:

::

    coils:
        some_coil:
            number: 1b
            pulse_ms: 30
            pulse_power: 4

When MPF sends this coil a pulse command, the coil will be fired for
30ms at 50% power. You can even combine pulse_power and hold_power,
like this:

::

    coils:
        some_coil:
            number: 1b
            pulse_ms: 30
            pulse_power: 4
            hold_power: 2


In this case, if MPF enables this coil, the coil will be fired at 50%
power for 30ms, then drop down to 25% power for the remainder of the
time that it's on.

Fine-tuning power values
~~~~~~~~~~~~~~~~~~~~~~~~

Since FAST uses an 8-bit pwm mask to control the pulse and hold power
of drivers, when you enter a pulse_power or hold_power setting, MPF
automatically converts the numeric value into an 8-bit pwm mask, like
this:


+ 0: 00000000
+ 1: 00000001
+ 2: 10001000
+ 3: 10010010
+ 4: 10101010
+ 5: 10111010
+ 6: 11101110
+ 7: 11111110
+ 8: 11111111


That should work fine for most cases, but we could envision scenarios
where you might want more fine-grained control. To enable this, you
can use pulse_pwm_mask and hold_pwm_mask settings where you actually
enter an 8-digit strings of ones and zeros for the mask. For example:


::


    coils:
        some_coil:
            number: 1b
            pulse_ms: 30
            hold_pwm_mask: 11001100


For really fine-grained scenarios, FAST also has the ability to use
32-bit pwm masks, though we haven't added that functionality to MPF
yet. If you need it, contact us and we'll get it added.



6. Configuring LEDs
-------------------

Each FAST Pinball Controllers has a built-in 4-channel RGB LED
controller which can drive up to 64 RGB LEDs per channel. This
controller uses serially-controlled LEDs (where each LED element has a
little serial protocol decoder chip in it), allowing you to drive
dozens of LEDs from a single data wire. These LEDs are generally known
as "WS2812" (or similar). You can buy them from many different
companies, and they're what's sold as the "NeoPixel" brand of
products from Adafruit. (They have all different shapes and sizes.)
There are two ways you can configure RGB LEDs for your FAST
controller: by channel & output number, or directly with the FAST
hardware number. It's more straightforward to configure them by
channel and output, like this:

::

   leds:
       l_led0:
           number: 0-0
       l_right_ramp:
           number: 2-28

In the example above, RGB LED *l_led0* is LED #0 on channel 0, and
*l_right_ramp* is LED #28 on channel 2. Note both the channel and LED
numbers start with 0, so your channel options for a FAST controller
are 0-3, and your LED number options are 0-63. Also note that when you
enter your FAST LED numbers with a dash like this, the values are
integers, even if the rest of your FAST settings are in hex.

7. Configuring matrix lamps
---------------------------

The FAST WPC controller controls the lamp matrix of WPC machines. This
means you have to configure those lights in the matrix_lights: section
of your machine configuration file. Like the other WPC-related
settings, you can enter the numbers right out of your operators
manual, so there's nothing FAST-specific you have to do.

8. Configuring a DMD
--------------------

The FAST WPC and Core controllers can control traditional mono-color
pinball DMDs via the 14-pin DMD connector cable that's been in most
pinball machines for the past 25 years. To do this, just make sure
that you have your dmd: section set to physical: yes and everything
else should just automatically work. If you want to control a color
DMD, an LCD-based DMD, or a SmartMatrix RGB LED-based DMD, then you
can do that with any FAST Pinball controller.
