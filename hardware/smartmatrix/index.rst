How to configure a "SmartMatrix" RGB LED DMD
============================================

This guide explains how to connect a SmartMatrix RGB LED DMD to a
pinball machine running MPF.

A `SmartMatrix <http://docs.pixelmatix.com/SmartMatrix/shieldref.html>`_ is a
cheap ($15) board that you attach to a Teensy ($20) microcontroller which lets
you connect an RGB DMD matrix display to the computer running MPF. It's a
standalone solution which you can use to add an RGB DMD to a pinball machine
that's using FAST Pinball, P-ROC/P3-ROC, or OPP controller hardware.

MPF supports several different types of RGB DMDs, and the SmartMatrix is just
one of the options. More information about this type of display and other
options that MPF supports is available in the
:doc:`/displays/display/physical_rgb_dmd` documentation.

Here's an image of the SmartMatrix RGB DMD in action:

.. image:: /hardware/images/display_rgb_dmd.jpg

And a video which explains it all: https://www.youtube.com/watch?v=zbZQCByeXOU

The following diagram shows how all the components fit together:

.. image:: /hardware/images/smartmatrix_architecture.png

1. Buy all the parts you need
-----------------------------

This solution is very much a "home brew" solution that will require
you to buy a lot of parts from various sources.

(1) The Panels
~~~~~~~~~~~~~~

We originally had to buy the panels directly from China via AliExpress,
but now `FAST Pinball sells a kit for $99 <https://squareup.com/store/fast-pinball-llc/item/rgb-dmd-panel-mounting-bracket-kit>`_.
The FAST Pinball option is nice because the price is great and
they also include a mounting bracket that fits a standard DMD cutout.

If you buy the panels yourself on AliExpress, you'll pay about
the same price for just the panels, you won't have a mounting bracket,
and you'll have to deal with customer support from China.
Also FAST tests the panels to make sure all the pixels work—a problem
people were running into when buying from AliExpress.

(2) The Teensy
~~~~~~~~~~~~~~

Once you have your panel, you need a way to talk to them via a
computer. The panels use some kind of 16-pin signalling system which
is some kind of standard in the gigantic advertising display industry.

The solution for MPF is to use a Teensy 3.2 (which is kind of like an Arduino).
The Teensy is available from multiple sources for about $20.
`Here's the link to the website <https://www.pjrc.com/store/teensy32.html>`_
of the guy who actually built it, and you can also
`get it from Adafruit <https://www.adafruit.com/products/2756>`_ which is
nice because you also need the shield (from the next step) which is also
available from them.

The Teensy runs the same software sketches as Arduinos, though it has a
slightly different processor architecture which is needed for the rapid
bit-shifting of data needed to control these panels.

Here's a Teensy:

.. image:: /hardware/images/teensy.jpg

The software to run the Teensy is open source (more on that in Step 3)
and the Teensy has a USB port which you connect to your computer which
MPF uses to send the display data to the panels.

(3) The SmartMatrix Shield
~~~~~~~~~~~~~~~~~~~~~~~~~~

Next you need a way for the Teensy to connect to the displays. That
can be done with the SmartMatrix shield
(`$15 from the guy who made the Teensy <https://www.pjrc.com/store/smartmatrix_kit.html>`_,
though out of stock at the moment, so you might have to spend
`$20 at Adafruit <http://www.adafruit.com/products/1902>`_).

The SmartMatrix shield is a "dumb" device
that basically just connects the Teensy's GPIO pins to the 16-pin
ribbon cable that drives the displays.

.. image:: /hardware/images/smartmatrix_shield.jpg

The Teensy mounts onto the
SmartMatrix shield, creating a single unit which accepts data via USB
on one end and spits out the 16-pin signal for the display panels on
the other.

.. image:: /hardware/images/smartmatrix_shield_with_teensy.jpg

(4) The Power Supply
~~~~~~~~~~~~~~~~~~~~

These RGB LED displays require 5vdc for power. At first you might
think, "Cool! I have 5v elsewhere in my machine, so I'll just tap into
that!" Not so fast. These displays require *a lot* of power. After
all, each pixel is actually three separate LEDs (one each for red,
green, and blue), and a 128x32 display means that you have 4,096
pixels. So that's 12,228 LEDs you need to power!

Since you're ordering your RGB LED display panels from FAST Pinball,
you can also order a
`5v, 10A power supply from them for $19 <https://squareup.com/store/fast-pinball-llc/item/five-volt-ten-amp-switching-power-supply>`_.

.. image:: /hardware/images/5v10a_psu.jpg

An ATX computer power supply will probably have a decent amount of amps also,
so that could be an option too, just check the specs.

One thing about these RGB LED-based displays is they are bright.
Like, really, really bright. (We're talking "burn your retinas if you
stare straight at them" kind of bright.)

So even though you can do the math and read that if every pixel
is on, full white, 100%, that might take more power than you have,
there is no way you're going to run these things at full brightness.

Even at 50% brightness, (which would draw only 50% power) most people
find these panels to be too bright. One user runs his at 25%, another
at 18%. So it's possible that you might be fine with 5-7 amps of power.

You'll need to connect the power supply up to both panels (the 128x32
display is made up of two 64x32 panels), and while you're at it you can
also use it to power your Teensy.

There's a trace you have to cut on the Teensy to control whether it's
powered externally or by USB. Don't hook it up to external power if
you haven't cut that trace!

2. Load the SmartMatrix code onto the Teensy
--------------------------------------------

Once your hardware's built, you need to load the code onto the Teensy
which receives the display data via USB and converts and sends it to the pins
connected to the SmartMatrix controller. The people who make the
SmartMatrix controller have code sample code available. We just took
their sample code, removed all the clutter we don't need, and made it
available in the tools folder in the MPF download package. (Here's a
`direct link to the code <https://raw.githubusercontent.com/missionpinball/mpf/dev/tools/smart_matrix_dmd_teensy_code/smart_matrix_dmd_teensy_code.ino>`_
which you can use since you probably installed MPF via pip and don't
have the download package available.

Also, `here's the original sample code <https://github.com/pixelmatix/SmartMatrix/blob/sm3.0/examples/FeatureDemo/FeatureDemo.ino>`_
we based our code on.

Note that the width and height of your display is set in lines 11 & 12. You can change
that if you want to use a different size display.

Mark Sunnucks was able to run a 128x64 display by setting the height there and also by changing the
DMAs from 4 to 2 in line 14.

Also note that you can set the brightness of the display in this code too. You can control
the brightness in MPF as well, but if you know for sure (maybe due to
power limitations) that you never want the brightness to go over a certain
amount, then you can set it here and it will be "hard coded" into your Teensy.
(You can change this and re-flash your Teensy at any time.)

Here's a quick overview of how to install this code onto the Teensy. Full instructions are
`here <https://github.com/pixelmatix/SmartMatrix>`_.

+ Install the Arduino IDE v1.6.5
+ Install the Teensyduino add-in which adds support for the Teensy
+ Load the smart_matrix_dmd_teensy_code.ino sketch from the mpf/tools
  folder or `this link <https://raw.githubusercontent.com/missionpinball/mpf/dev/tools/smart_matrix_dmd_teensy_code/smart_matrix_dmd_teensy_code.ino>`_
+ Push the button on the Teensy to put it into programming mode
+ Compile & load the code onto the Teensy from the Arduino IDE


3. Configure the physical RGB DMD
---------------------------------

Next, we'll make the entry that tells MPF that it should use the physical RGB DMD.

First, create an entry like this:

::

    physical_rgb_dmd:
      brightness: .5

There are several settings which can be set here (see the
:doc:`/config/physical_rgb_dmd` section of the config file reference for the full list).

The main thing we want here is to set the brightness, which is a multiplier from 0.0 to 1.0
that's applied to every pixel that's sent to the DMD. In other words, the example of
``brightness: .5`` means that each pixel will be shown at 50% brightness.

.. note::

   If you set the brightness multiplier in the sketch code .INO file you loaded onto
   the Teensy, then that will multiple the brightness after MPF sends it. In other words,
   if you set .5 in the config file and .5 in the sketch, then the final brightness will be 25%.

4. Configure your RGB DMD platform to use the SmartMatrix
---------------------------------------------------------

Next you need to make a platform setting that tells MPF that it should
use the *smartmatrix* platform interface for your DMD rather than
using the existing default platform you have set (P-ROC, FAST, OPP, etc.). To do
this, go to your *hardware:* section and add ``rgb_dmd: smartmatrix``. For
example:

::

    hardware:
        platform: fast
        driverboards: fast
        rgb_dmd: smartmatrix

5. Configure your SmartMatrix settings
--------------------------------------

Finally, add a ``smartmatrix:`` section to your machine-wide config and
then add the three settings below:

::

    smartmatrix:
        port: com12
        baud: 2500000
        old_cookie: true

The port is just whatever serial port appears when you plug in
the Teensy. (See the note in Section 8a for details of how to find the
port on Linux or Mac.)

Just enter the ``baud:`` and ``old_cookie:`` settings like they are in the
example above. These are the settings that are needed for the SmartMatrix.

5a. Finding the port on Linux or Mac
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To list the ports numbers that devices are using, open up the terminal window
and type the following command: ``ls /dev/tty.*``  The output of this command
will look something like this:

::

   /dev/tty.Bluetooth-Incoming-Port	/dev/tty.usbmodem1448891

The smartmatrix config will look something like this:

::

    smartmatrix:
        port: /dev/tty.usbmodem1448891
        use_separate_thread: no

A final config you can test
---------------------------

At this point that's all you need for the SmartMatrix DMD to work.

We've created a complete example machine config (well, at least with the
sections you can add to your machine config) which you can use to verify that
you have everything hooked up and configured properly.

Be sure to change the ``smartmatrix:port:`` setting in this example config to
match whatever port your Teensy is connected to.

To run this sample config, you can either run ``mpf both`` or (if you're on a
Mac), ``mpf`` and ``mpf mc``.

When you run it, do not use the ``-x`` or ``-X`` options, because either of
those will tell MPF to not use physical hardware which means it won't try to
connect to the Teensy.

::

    hardware:
        platform: virtual
        rgb_dmd: smartmatrix

    displays:
      window:
        width: 600
        height: 200
      dmd:
        width: 128
        height: 32
        default: true

    window:
      width: 600
      height: 200
      title: Mission Pinball Framework

    physical_rgb_dmd:
      brightness: .5

    smart_matrix:
      port: com5  # this will most likely be a different port for you
      use_separate_thread: no

    slides:
      window_slide_1:
      - type: color_dmd
        width: 512
        height: 128
      - type: text
        text: MISSION PINBALL FRAMEWORK
        anchor_y: top
        y: top-3
        font_size: 30
        color: white
      - type: rectangle
        width: 514
        height: 130
        color: 444444

    slide_player:
      init_done:
        window_slide_1:
          target: window
