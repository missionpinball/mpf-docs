Using an RGB LED "SmartMatrix" DMD
==================================

This How To guide explains how to connect an RGB LED-based matrix
(sometimes called a "SmartMatrix") to a pinball machine running MPF.
This has been called a "real" Color DMD in the forums since the
displays are arrays of RGB LEDs rather than an LCD monitor running a
display that is made to look like a DMD. Many people like these better
than LCD-based displays because they're brighter and more vibrant, and
the blacks are actually black since the LEDs are off versus LCD
displays which have blacks are are actually dark gray.

.. image:: /displays/images/display_rgb_dmd.jpg

This video explains it all: https://www.youtube.com/watch?v=zbZQCByeXOU

We will also show you how to create an on-screen popup window which will show
the contents of the DMD, like this (with a blank DMD):

.. image:: /displays/images/on_screen_basic_dmd_window.png

If you want to use a physical RGB DMD without the on-screen equivalent, we'll show
you how to do that at the end.

If you want to only have an on-screen DMD without the physical one, like if
you want to replace the DMD with an LCD screen but still have it look like a
color DMD, then read :doc:`this guide <adding_dot_look_to_lcd>` instead.

The final version of the relevant sections of your machine config for a
physical RGB DMD with an on screen window too will look like
this:

::

    hardware:
        platform: fast  # or p_roc, p3_roc, opp, etc.
        driverboards: fast  # or whatever driverboards you have
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
      mc_ready:
        window_slide_1:
          target: window


Here's a hookup diagram which shows how all the components you need fit together:

.. image:: /displays/images/smartmatrix_architecture.png

1. Shout-out to Eli Curtz!
--------------------------

First, this project wouldn't exist without Eli Curtz.
`Eli first posted about these panels <http://www.pinballcontrollers.com/forum/index.php?topic=1396.msg12382#msg12382>`_
in the P-ROC forum in 2014. At that
time we could only find panels with 3mm spacing between pixels which
was a bit larger than traditional pinball DMDs, but that's what kicked
off the conversation about, "Whoa, maybe we could use these for 'real'
color DMDs some day." Then in September 2015, Eli posted again telling
us that we could now get panels with 2.5mm spacing which is the
perfect size we need. Eli also showed us how to connect them and what
software we needed to make everything work. So really everything here
is because of Eli. All we did is take everything he showed us and
write it down. (Well, that and we also created the interface for MPF,
but that was the easy part.) So thanks Eli!

2. Buy all the parts you need
-----------------------------

This solution is very much a "home brew" solution that will require
you to buy a lot of parts from various sources.

2a. The Panels
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

2b. The Teensy
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

.. image:: /displays/images/teensy.jpg

The software to run the Teensy is open source (more on that in Step 3)
and the Teensy has a USB port which you connect to your computer which
MPF uses to send the display data to the panels.

2c. The SmartMatrix Shield
~~~~~~~~~~~~~~~~~~~~~~~~~~

Next you need a way for the Teensy to connect to the displays. That
can be done with the SmartMatrix shield
(`$15 from the guy who made the Teensy <https://www.pjrc.com/store/smartmatrix_kit.html>`_,
though out of stock at the moment, so you might have to spend
`$20 at Adafruit <http://www.adafruit.com/products/1902>`_).

The SmartMatrix shield is a "dumb" device
that basically just connects the Teensy's GPIO pins to the 16-pin
ribbon cable that drives the displays.

.. image:: /displays/images/smartmatrix_shield.jpg


The Teensy mounts onto the
SmartMatrix shield, creating a single unit which accepts data via USB
on one end and spits out the 16-pin signal for the display panels on
the other.

.. image:: /displays/images/smartmatrix_shield_with_teensy.jpg

2d. The Power Supply
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

3. Load the SmartMatrix code onto the Teensy
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

4. Add your displays to your MPF config
---------------------------------------

The first part of the config file from the beginning of this guide is where you create
your logical displays like we covered in the :doc:`index` section.

::

    displays:
      window:
        width: 600
        height: 200
      dmd:
        width: 128
        height: 32
        default: true

We're creating two displays here. The first is called "window" and
has a size of 600x200. This will be the display that shows up on the computer
screen.

The second display, which we're calling "dmd", will be the display that provides
the content for the physical RGB DMD. This display is 128x32, which is the pixel
size of the DMD.

Notice that we set ``default: true`` for the dmd display. This is because as
we're creating display content in our game, we want it (by default) to show up
in the DMD (since that will be the primary display in our game).

Note that you don't set colors or anything here—this is just setting up the
logical displays which we'll use next.

5. Add your window configuration
--------------------------------

Next, we have a ``window:`` section which holds the settings for the actual
on screen window itself. In this case we're just configuring it to be 800x600,
with a window title of "Mission Pinball Framework".

::

    window:
      width: 600
      height: 200
      title: Mission Pinball Framework

Check out :doc:`Step 2. of the LCD guide <lcd>` for more details on this
window section, and be sure to check out all the window options in the
:doc:`/config/window` section of the config file reference.

Notice that in this case, we did not add the ``source_display: window``
setting to this section. That's because we have a logical display called
"window", and when you have that, the on-screen window will automatically use
that display as its source.

6. Configure the physical RGB DMD
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

7. Configure your RGB DMD platform to use the SmartMatrix
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

8. Configure your SmartMatrix settings
--------------------------------------

Finally, add a ``smartmatrix:`` section to your machine-wide config and
then configure the two options for your port and whether or not you'll
run the SmartMatrix communication code in a separate thread:

::

    smartmatrix:
        port: com12
        use_separate_thread: no

The port is just whatever serial port appears when you plug in
the Teensy.

8a. Mac port help
~~~~~~~~~~~~~~~~~

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

The correct setting for the thread will depend on the
specifics of your hardware and what size display you're running. For
example, on one test system (MPF running in a Windows VM on a MacBook),
it didn't matter what the thread was set to—it was the same either way.
For the user who used the 128x64 display, he had to set
``use_separate_thread: no`` to get good performance. So basically try it
with both settings and see which one works better.

.. note::
   The separate thread option will most likely be removed in MPF 0.31 as
   we're moving to a different IO model that won't need it.

9. Configure a window slide to show the on screen DMD
-----------------------------------------------------

Now we have a working on-screen window and a working physical. But if you run
``mpf both`` now, your on screen window will be blank because we haven't
built any slides to show up.

So in this step, we're going to build a slide for the on-screen window that will
be shown when MPF starts. We'll add some widgets to that slide to make it look
like the screen shot at the beginning of this guide.

First, create a ``slides:`` section in your machine config (if you don't have
one already), and then create an entry for the slide that we want to show. In
this case, we've decided to name that slide "window_slide_1". (Of course you can
call this slide whatever you want.

::

    slides:
      window_slide_1:

Next we have to add some widgets to that slide. (Refer to the
:doc:`documentation on widgets </displays/widgets/index>` if you're not familiar
with widgets yet.)

The first widget will be a :doc:`Color DMD widget </displays/widgets/widget/color_dmd>`
which is a widget which renders a logical display onto a slide in a way that
makes it look like a DMD:

::

      - type: color_dmd
        width: 512
        height: 128

Again, there are lots of options here. Note that we're adding a ``height:`` and
``width:`` of 512x128. This is the on-screen pixel size of the DMD as it will
be drawn in the window. In this case we chose an even multiple of the source
display for the DMD (which is 128x32), meaning that each pixel of the original
DMD will be rendered on screen as 4 pixels by 4 pixels. This is big enough
to get the circular "dot look" filter to look good, and being an even multiple
means that we won't have any weird moire patterns.

There are other options listed in the
:doc:`Color DMD widget </displays/widgets/widget/color_dmd>` documentation to control
settings like how big the circles are versus the space in between them, the
ability to not have the "dot" filter, and the ability to set the "glow" radius
of each dot, color tint, limiting the color palette, etc.

Note that in this case, we did not have to add the ``source_display:`` option
because we have a display called "dmd" which will automatically be used as the
source for the color DMD widget.

Next, we also added two more widgets to this slide—a text widget with the
title of the machine, and a gray rectangle that's slightly larger than the DMD
to give it a nice border.

::

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

10. Configure the slide to show when MPF starts
-----------------------------------------------

Now we have a nice slide with the virtual DMD on it, but if you run MPF, you
still won't see it because we didn't tell MPF to show that slide in the window.
So that's what we're doing here:

::

    slide_player:
      mc_ready:
        window_slide_1:
          target: window

If you don't have a slide_player: entry in your machine-wide config, go ahead
and add it now. Then create an entry for the :doc:`/config/mc_ready` event.
This is the event that the media controller posts when it's ready to be used,
so it's a good event for our use case.

Then under that event, create an entry to show the slide you just created in the
previous step. Notice that we also have to add the ``target: window`` entry to
tell the slide player that we want this slide to show on the "window" target.
We need to do this because the default display (from Step 2) is the DMD, so if
we don't specify a target, this slide will show on the default, which would be
the DMD, instead of being shown on the window. (In this case, we would show a
slide on the DMD which contains a DMD widget whose source is the DMD, and we'd
probably open up some kind of wormhole and destroy the universe. So don't do
that.)

And this point, you're all set! Of course there's no content on the DMD yet
because we haven't set up any slide_player entries to add content to it, but
that's something you can do by following the tutorial or looking at the guides
for the slides and widgets here.

11. What if you don't want the on-screen window?
-----------------------------------------------

There might be some scenarios where you just want the physical DMD with no
on-screen DMD. (For example, maybe you're using a low-power single board
computer and you don't have enough horsepower to run a graphical environment.)

This is fine. To do it, just remove the window-related components from the
config, resulting in something like this:

::

    hardware:
        platform: fast  # or p_roc, p3_roc, opp, etc.
        driverboards: fast  # or whatever driverboards you have
        rgb_dmd: smartmatrix

    displays:
      dmd:
        width: 128
        height: 32

    physical_rgb_dmd:
      brightness: .5

    smart_matrix:
      port: com5  # this will most likely be a different port for you
      use_separate_thread: no

In this case, you don't need the ``default: true`` entry for the dmd in the
displays: section because you only have one display, so it will automatically
be the default.

.. todo::

   We need more explanation of how to run with no window here.






Troubleshooting
---------------

We'll add troubleshooting tips here as we find them. So far the only
thing that came up is one user didn't have any luck with anything
appearing on the display, but that's because he was running MPF with
the ``-x`` option which is "no hardware." So if you use ``-x``, MPF will
not connect to any physical hardware and it won't work. If you want to
play with the SmartMatrix display without a FAST or P-ROC connected,
then set your platform: section like this:

::

    hardware:
        platform: virtual
        dmd: smartmatrix


Then run MPF but *do not use -x*, and it should work.
