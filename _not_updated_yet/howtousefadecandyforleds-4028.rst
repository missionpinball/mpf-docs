
MPF allows you to use a FadeCandy LED controller to drive the LEDs in
your pinball machine. A FadeCandy is a small, cheap ($25) USB
controller which can drive up to 512 serially-controlled RGB LEDs. You
can read more about it on the main page of the `FadeCandy software
repository`_ in GitHub or on `Adafruit`_or `SparkFun`_, where you can
buy a FadeCandy for $25. The FadeCandy is very advanced, offering
advanced light processing capabilities (dithering, interpolation,
adjustable gamma curves and white balance) that are not available if
you just control LEDs directly. If you're not familiar with the
FadeCandy, check out thisintro from SparkFun:
https://www.youtube.com/watch?v=-4AUBjV7Y-w This How To guide will
show you how to setup and use a FadeCandy with the Mission Pinball
Framework. In MPF, you can use the FadeCandy in place of connecting
your LEDs to a Multimorphic (P-ROC / P3-ROC) controller, or you
canchoose to drive some LEDs via your primary pinball controller and
some via the FadeCandy.



(A)Understanding all the parts and pieces
-----------------------------------------

Before we dig in to setting up a FadeCandy with MPF, let's look at how
all the various components will fit together:


+ The FadeCandy is a piece of hardware that talks to your host
  computer via USB. (So if you use it in a pinball machine then you'll
  have two devices connected via USB—your pinball controller and your
  FadeCandy.
+ The FadeCandy hardware is driven a FadeCandy server process that
  you'll run on your host computer along side of the MPF core engine and
  the MPF media controller. The FadeCandy server talks to the FadeCandy
  hardware via a USB driver.
+ The FadeCandy server process receives instructions for LEDs
  connected to the FadeCandy via a protocol called `Open Pixel
  Control`_(OPC).


Putting it all together, MPF talks to the FadeCandy server via OPC,
and the FadeCandy server talks to the FadeCandy hardware via USB.



(B) Download the FadeCandy package from GitHub
----------------------------------------------

The first step is to download the `FadeCandy package`_ from GitHub.
You can unzip it to wherever you want. It doesn't have to be in your
MPF folder. (In fact it shouldn't be in your MPF folder so you can
blow away your MPF folder as new releases come out.)



(C) Install the FadeCandy drivers
---------------------------------

When I (Brian) plugged the FadeCandy hardware into my Windows
computer, the driver did not install automatically. Running the
fcserver (next step) said it was installing the drivers, but that
didn't do anything for me. (It just said "this may take awhile" but I
killed itwhen it didn't seem like it was actually doing anything.) In
my case, I googled and fount`this procedure`_ to build custom .inf
files for Windows. It seems crazy but it wasn't too bad. I had to
build two: One for the FadeCandy device and one for the FadeCandy boot
loader. Either way, you can follow the docs and the forums around the
FadeCandy and get it setup.



(D)Setup the fcserver
---------------------

The FadeCandy download package includespre-built binaries for Mac and
Windows. On Linux you can compile it. Again, the FadeCandy
documentation has details about how to do this. At this point you
should be able to run the fcserver and to talk to your FadeCandy LEDs
and get them to do things. There are a bunch of sample apps in the
FadeCandy package that are kind of cool.



(D) Setyour LEDs to use the 'fadecandy'platform
-----------------------------------------------

Next you need to configure your LEDs in MPF to use the `fadecandy`
platform. By default, all types of devices are assumed to be using the
same platform that you have set in the` `hardware:` section`_ of your
machine config file. (So if your platform is set to `fast`, MPF
assumes your LEDs are connected to a FAST controller, and if your
platform is set to `p_roc` or `p3_roc`, MPF assumes your LEDs are
connected to a PD-LED board. To configure MPF to use FadeCandy LEDs,
there are two ways you can do this. The first method is used if every
LED you have will be connected to a FadeCandy. In this case you can
add an entry to the hardware: section of your config to tell it to
override the default platform for your LEDs and to instead use the
`fadecandy` platform, like this:


::

    
    hardware:
        platform: p_roc
        driverboards: pdb
        leds: fadecandy


Or, if you'd like to mix-and-match LEDs from your base platform and
the FadeCandy platform, you can add a platform: entry to an actual LED
configuration entry to override the default. So assuming that you do
not have the leds: fadecandy entry in the hardware: section of your
machine config, you could set up LEDs like this:


::

    
    leds:
        l_some_led:
            number: 0
        l_some_other_led:
            number: 0
            platform: fadecandy


In the above example, *l_some_led* will be run from your base platform
(P-ROC or FAST), and *l_some_other_led* will be a FadeCandy. Notice
that both of these LEDs are number "0". That's ok, because the first
one is LED #0 from your base platform and the second is LED #0 from
your FadeCandy. (If you have mostly FadeCandy LEDs and only a few on
your base platform, you could flip that and add the `leds: fadecandy`
to your hardware: section and then only override the specific ones on
the base platform with `platform: p_roc` or whatever.)



(F) Understanding FadeCandy LED numbering
-----------------------------------------

The FadeCandy hardware has 8 connectorsfor LEDs, each of which can
support up to 64 RGB LEDs (for 512 RGB LEDs total). The connectorsare
numbered 0-7. The LED numbers are sequential across channels. The
first LED on Connector0is #0, the second is #1, etc., up #63 on
Connector0. Then Connector1picks up where Connector0 leaves off, with
the first LED on Connector2 being #64, and so on. The FadeCandy
doesn't actually know how many LEDs are connected to each connector,
so the first LED on Connector1 is always LED #64 even if you have less
than 64 LEDs physically connected to Connector0. ` `_ If you're
familiar with the Open Pixel Control protocol, all of the LEDs on a
single FadeCandy board are on the same OPC channel. (By default this
is OPC Channel 0. You can add additional FadeCandy controllers to
support more than 512 LEDs which will use other OPC Channels. See the
FadeCandy documentation for details.)



(G) Launch the fcserver
-----------------------

In order for MPF to communicate with the FadeCandy, the fcserver has
to be running. (On my Windows test machine, this is just
`fcserver.exe`.) There are several command line options you can use,
but we don't need any of them with MPF unless you have more than one
FadeCandy board connected. You should launch fcserver in its own
window since it will take over the console when it's running. It's
also safe to keep it running all the time, or you can add it to your
mpf.bat to run it automatically. (You'll need to figure out how to get
it to stop when MPF stops. I'm sure that's possible but I haven't
looked into it.) On my system, the fcserver puts some error message on
the screen about not being able to connect to something, but
everything still works even with that message continually being
written to the console. (I think it's something to do with the P-ROC's
FTDI driver? It only comes up when the P-ROC is on.)



(H) Test your LEDs
------------------

The easiest way to test your FadeCandy LEDs with MPF is to make a
simple attract mode light show with a few of them. We cover this in
`this step of our tutorial`_.



(I) Additional FadeCandy LEDoptions
-----------------------------------

The FadeCandy hardware supports some advanced options which are
configured in the ` `led_settings:` section`_ of your machine
configuration file. Specifically, you can set the keyframe
interpolation, dithering, gamma, white point, linear slope, and linear
cutoff. The defaults should be fine for almost everyone, though you
can go nuts if you want.

.. _FadeCandy software repository: https://github.com/scanlime/fadecandy
.. _FadeCandy package: https://github.com/scanlime/fadecandy/releases
.. _Adafruit: http://www.adafruit.com/products/1689
.. _SparkFun: https://www.sparkfun.com/products/12821
.. _this step of our tutorial: https://missionpinball.com/docs/tutorial/create-an-attract-mode-light-show/
.. _ section: https://missionpinball.com/docs/configuration-file-reference/hardware/
.. _Open Pixel Control: http://openpixelcontrol.org/
.. _this procedure: http://www.libusb.org/wiki/winusb_driver_installation
.. _ section: https://missionpinball.com/docs/configuration-file-reference/ledsettings/


