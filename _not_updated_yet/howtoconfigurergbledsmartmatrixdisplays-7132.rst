
This How To guide explains how to connect an RGB LED-based matrix
(sometimes called a "SmartMatrix") to a pinball machine running MPF.
This has been called a "real" Color DMD in the forums since the
displays are arrays of RGB LEDs rather than an LCD monitor running a
display that is made to look like a DMD. Many people like these better
than LCD-based displays because they're brighter and more vibrant, and
the blacks are actually black since the LEDs are off versus LCD
displays which have blacks are are actually dark gray. This video
explains it all: https://www.youtube.com/embed/zbZQCByeXOU Note that
everything described in this How To guide is assuming that you're
controlling the content of the DMD via a USB connection from a host
computer running MPF. If you want to build an RGB LED display which
you use in an existing pinball machine connected to the existing
14-pin DMD cable, a guy named Eli Curtz is creating an alternative to
the SmartMatrix shield that can be controlled by both the computer via
USB and by an existing 14-pin DMD signal from an existing machine. See
`this Pinside thread`_ for details. Here's a hookup diagram which
shows how all the components you need fit together. (Click it to
expand it to full size.) ` `_



(A) Shout-out to Eli Curtz!
---------------------------

First, this project wouldn't exist without Eli Curtz. `Eli first
posted about these panels`_ in the P-ROC forum a year ago. At that
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



(B) Buy all the parts you need
------------------------------

This solution is very much a "home brew" solution that will require
you to buy a lot of parts from various sources.



1. The Panels
~~~~~~~~~~~~~

The main part of this project is the display panels. The panels you'll
find are sold for commercial purposes for "video walls" and "Jumbo-
trons" and stuff like that. There are many sizes of panels available
with different size spacing between the individual pixels. The ones
that are most like an existing pinball DMD have 2.5mm spacing (also
referred to as "P2.5"), which results in a 128x32 display of
320x76.8mm. This overall display will be within a 1/4" or so of the
original DMD size and will fit nicely into an existing DMD/speaker
panel from an existing machine. Currently the only place to buy these
panels is from AliExpress. They don't sell 128x32 panels, but you can
buy two 64x32 ones and connect them side-by-side. Since these things
are designed for huge video walls, they are seamless. Buying stuff
from AliExpress is somewhat of an adventure, and it's not always
possible to tell exactly what you're going to get. The exact panels we
ordered were $25 each for 64x32, though it appears that supplier
doesn't offer them anymore. Your best bet is to search for [`RGB LED
64x32 p2.5`_] and hope for the best. Prices tend to range from $50 to
$70 per panel (and remember you need two), depending on luck as far as
we can tell. (We've seen some panels as cheap as $25, but after
ordering many different models, it's clear to us that the $25 ones
were ones that had manufacturing errors that have been repaired. This
isn't necessarily a bad thing, but it does seem that availability at
the sub-$50 price point is hit-or-miss.) The key is to make sure you
get "P2.5" (the 2.5mm pitch), because if you accidentally end up with
P4 (4mm pitch) then you're going to end up with a 2-foot by 6-inch
DMD. :) Ideally you'd end up with something like this: ` `_
Unfortunately when you actually place the order for two of them, you
might end up with them mounted in a 64x64 configuration onto a single
plastic frame. In this case you will probably still have two 64x32
panels, but you'll have to remove them from the plastic frame and cut
the frame in half, or you'll have to make your own frame. ` `_



2. The Teensy
~~~~~~~~~~~~~

Once you have your panel, you need a way to talk to them via a
computer. (The panels use some kind of 16-pin signalling system which
we assume is a standard in the gigantic outdoor display industry since
it seems that all the panels have the same standards here.) We use the
Teensy 3.2 which is available from multiple sources for about $20.
(`Here's the link to the website`_ of the guy who actually built it.)
The Teensy is similar to an Arduino (in fact it runs the same software
sketches as Arduinos) though it has a slightly different processor
architecture which is needed for the rapid bit-shifting of data needed
to control these panels.

` `_

The software to run the Teensy is open source (more on that in Step C)
and the Teensy has a USB port which you connect to your computer which
MPF uses to send the display data to the panels.



3. The SmartMatrix Shield
~~~~~~~~~~~~~~~~~~~~~~~~~

Next you need a way for the Teensy to connect to the displays. That
can be done with the SmartMatrix shield (`$15 from the guy who made
the Teensy`_, though out of stock at the moment, so you might have to
spend `$25 at Adafruit`_). The SmartMatrix shield is a "dumb" device
that basically just connects the Teensy's GPIO pins to the 16-pin
ribbon cable that drives the displays. ` `_ The Teensy mounts onto the
SmartMatrix shield, creating a single unit which accepts data via USB
on one end and spits out the 16-pin signal for the display panels on
the other. ` `_ As we wrote in the introduction, this
Teensy+SmartMatrix Shield combo can only be used with source data
coming from a computer via USB. If you want a way to "colorize" an
existing 14-pin DMD signal from an existing pinball machine, you'll
need to use a different board than the Teensy. Eli Curtz is developing
a dual-purpose board which can get its signal from a computer or from
a 14-pin DMD cable, so as long as that board costs $25 or less, than
you should probably buy it instead of the SmartMatrix Shield since
that way the DMD you build here will be usable in regular pinball
machines too if you decide not to use it in your MPF-powered machine.
Here's a look at Eli's board so far. Check back in `that Pinside
thread`_ for details about its availability. ` `_



4. The Power Supply
~~~~~~~~~~~~~~~~~~~

These RGB LED displays require 5vdc for power. At first you might
think, "Cool! I have 5v elsewhere in my machine, so I'll just tap into
that!" Not so fast. These displays require *a lot* of power. After
all, each pixel is actually three separate LEDs (one each for red,
green, and blue), and a 128x32 display means that you have 4,096
pixels. So that's 12,228 LEDs you need to power! `Here's a 5v 8A power
supply`_ for $15 from Amazon. Unfortunately 8A is not enough if you
want to run these things at full brightness. I ended up buying `this
5vdc 60A power supply`_ from Amazon for $60 instead. (An ATX computer
power supply will probably have a decent amount of amps also, just
check the specs.) That said, you might be fine with a 8A supply. The
thing is, at 100% brightness, these things are bright. I mean like
"burn your retinas" bright. You can set the overall brightness level
(more on that in the next step), and when you do that, the displays
require less power. Even at 50% brightness, most people find these
panels to be too bright. One user runs his at 25%, another at 18%. So
it's possible that you might be fine with 5-7 amps of power, and that
$15 8A power supply should be fine if you don't have enough 5v power
elsewhere. You need to connect that power supply up to both panels,
and while you're at it you can also use it to power your Teensy.
(There's a trace you have to cut on the Teensy to control whether it's
powered externally or by USB. Don't hook it up to external power if
you haven't cut that trace!)



(C) Load the SmartMatrix code onto the Teensy
---------------------------------------------

Once your hardware's built, you need to load the code onto the Teensy
which receives your data via USB and converts and sends it to the pins
connected to the SmartMatrix controller. The people who make the
SmartMatrix controller have code sample code available. We just took
their sample code, removed all the clutter we don't need, and made it
available in the tools folder in the MPF download package. (Here's a
`direct link to the code`_ if you want to look at it, and `here's is
the original sample code`_ we based our code on.) Note that the width
and height of your display is set in lines 11 & 12. You can change
that if you want to a different size display. (Snux was able to run a
128x64 display by setting the height there and also by changing the
DMAs from 4 to 2 in line 14.) Also note that you can set the
brightness here too. By default it's 100%, but you can change that in
line 22 to whatever you want. Here's a quick overview of how to
install this code onto the Teensy. Full instructions are `here`_.


+ Install the Arduino IDE v1.6.5
+ Install the Teensyduino add-in which adds support for the Teensy
+ Load the smart_matrix_dmd_teensy_code.ino sketch from the mpf/tools
  folder
+ Push the button on the Teensy to put it into programming mode
+ Compile & load the code onto the Teensy from the Arduino IDE


Note that if you're using Eli's board with the 14-pin DMD input
option, then you'll install different code (from him) instead of the
code from MPF.



(D) Configure MPF to use it
---------------------------

Finally you need to update your MPF machine-wide configuration to use
the new display.



1. Configure your DMD
~~~~~~~~~~~~~~~~~~~~~

Follow the existing instructions for setting up a DMD (`Step 6(C) from
the MPF tutorial.`_) Then set *physical: yes* and *type: color*, so
your final DMD config looks like this:


::

    
    dmd:
        physical: yes
        width: 128
        height: 32
        type: color




2. Configure your DMD platform to use the SmartMatrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next you need to make a platform setting that tells MPF that it should
use the *smartmatrix* platform interface for your DMD rather than
using the existing platform you have set (P-ROC, FAST, etc.). To do
this, go to your *hardware:* section and add *dmd: smartmatrix*. For
example:


::

    
    hardware:
        platform: fast
        driverboards: fast
        dmd: smartmatrix




3. Configure your SmartMatrix settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, add a smartmatrix: section to your machine-wide config and
then configure the two options for your port and whether or not you'll
run the SmartMatrix communication code in a separate thread:


::

    
    smartmatrix:
        port: com12
        use_separate_thread: yes


The port is just whatever virtual serial port appears when you plug in
the Teensy. The correct setting for the thread will depend on the
specifics of your hardware and what size display you're running. For
example, on my test system (MPF running in a Windows VM on a MacBook),
it didn't matter what I set the thread to—it was the same either way.
For Snux who used the 128x64 display, he had to set
*use_separate_thread: no* to get good performance. So basically try it
with both settings and see which one works better.



(E) Color your slides
---------------------

At this point you should be able to run your game, though all the
content on the DMD will be white since it doesn't include any color
data. We have an existing How To guide which explains `how to
configure a color DMD`_ and walks you through setting adding colors to
the dynamic elements (text, shapes, etc.) that you add to your
display. Even though that guide is written for a "virtual" (on screen,
LCD-based) color DMD, the techniques are the same. (The only
difference is that you'll have the *physical* setting set to *yes*
which means whatever shows up on the DMD will be sent to the physical
DMD.) Essentially any images or videos you play will just sort of
automatically work in color. And then any other display elements you
add, you'll include a *color:* setting with a 6-character RGB color
value instead of the current *shade:* setting which specifies an
intensity from 0-15.



Troubleshooting
---------------

We'll add troubleshooting tips here as we find them. So far the only
thing that came up is one guy didn't have any luck with anything
appearing on the display, but that's because he was running MPF with
the `-x` option which is "no hardware." So if you use `-x`, MPF will
not connect to any physical hardware and it won't work. If you want to
play with the SmartMatrix display without a FAST or P-ROC connected,
then set your platform: section like this:


::

    
    hardware:
        platform: virtual
        dmd: smartmatrix


Then run MPF but *do not use -x*, and it should work. Also there's a
Python script called eli_test.py in the tools folder which you can run
to display some moving rainbow bars on the display. To use it, open it
up and set your port in line 4, and then change to the `/mpf/tools`
folder and run `python eli_test.py`. You should see the bars appear on
the display at that point.

.. _here's is the original sample code: https://github.com/pixelmatix/SmartMatrix/blob/sm3.0/examples/FeatureDemo/FeatureDemo.ino
.. _Step 6(C) from the MPF tutorial.: https://missionpinball.com/docs/tutorial/add-a-display/#C_Adda_DMD
.. _that Pinside thread: https://pinside.com/pinball/forum/topic/rgb-led-panels-for-dmd-replacement
.. _Here's a 5v 8A power supply: http://www.amazon.com/NEWSTYLE-Supply-Converter-Adapter-5-5x2-1mm/dp/B00MHV7576/
.. _RGB LED 64x32 p2.5: http://www.aliexpress.com/wholesale?SearchText=RGB+LED+p2.5
.. _this 5vdc 60A power supply: http://www.amazon.com/gp/product/B00IWC2RLS
.. _direct link to the code: https://github.com/missionpinball/mpf/blob/dev/tools/smart_matrix_dmd_teensy_code/smart_matrix_dmd_teensy_code.ino
.. _Eli first posted about these panels: http://www.pinballcontrollers.com/forum/index.php?topic=1396.msg12382#msg12382
.. _$25 at Adafruit: http://www.adafruit.com/products/1902
.. _how to configure a color DMD: https://missionpinball.com/docs/howto/configure-a-color-dmd/
.. _Here's the link to the website: https://www.pjrc.com/store/teensy32.html
.. _$15 from the guy who made the Teensy: https://www.pjrc.com/store/smartmatrix_kit.html
.. _here: https://github.com/pixelmatix/SmartMatrix


