
The `hardware:` section of the config files lets you specify options
that relate to the specific pinball controller hardware you're using.
This sectioncan be used in your machine-wide config files. This
section *cannot* be used in mode-specific config files. Here's a
sample:


::

    
    hardware:
      platform: p_roc
      driverboards: wpc




platform:
~~~~~~~~~

Specifies which hardware platform you're using. Options include:


+ `p_roc` (Multimorphic P-ROC)
+ `p3_roc` (Multimorphic P3-ROC)
+ `fast` (FAST Core or WPC controllers)
+ `virtual`(Software-only "virtual"hardware platform that doesn't
  require any P-ROC or FAST drivers to be installed). This is the
  default option if you don't add a `platform:` section to your config
  file.
+ `openpixel` (Open Pixel Control-based LEDs)
+ `fadecandy` (LEDs connected to a FadeCandy)
+ `smartmatrix` (RGB LED color DMD)




driverboards:
~~~~~~~~~~~~~

Specifies whether you're using Williams, Stern, or other driver
boards. Typically this will match the platform of the game you're
writing for (if you're modifying an existing game), or if you're
building your own game, it will be the custom board type from your
hardware vendor.


+ `wpc95`
+ `pdb` (This is "P-ROC Driver Boards", which means you're using the
  PD-16, PD-8x8, etc.)
+ `fast`
+ `wpc`
+ `wpcAlphaNumeric` (Note that we have not yet added segmented display
  support to our media controller)
+ `sternSAM` (See our `blog post on getting MPF running with a Stern
  S.A.M. machine`_ for notes.)
+ `sternWhitestar` (Not actually tested but should work since the
  P-ROC supports it.)




Optional"per device" platform overrides
---------------------------------------

In MPF it's possible to mix-and-match your hardware platforms. For
example, you could use a P-ROC for your coils and switches while using
a FadeCandy for your LEDs. (Or, if you wanted to be crazy, you could
use a FAST controller for your switches and a P-ROC for your coils and
lamps.) You can specify a hardware platform on a device class level
(e.g. all switches are P-ROC, all LEDs are openpixel) or on a device-
by-device basis (some LEDs are from the FAST controller, others are
from the FadeCandy). To specify that a certain class of devices should
use a platform other than the default platform, add an entry for that
type of device and the platform you want to use to the hardware:
section of your config. For example, if you want to use a P-ROC for
most things but a FadeCandy for your LEDs, you would specify it like
this:


::

    
    hardware:
        platform: p_roc
        driverboards: pdb
        leds: fadecandy


You can specify the following types of hardware in this way:


+ coils
+ switches
+ matrixlights
+ leds
+ dmd
+ gis
+ flashers


Further, if you want to override the platform on an individual device
basis, you can add a platform: setting to the device itself. For
example, here are two LEDs, the first using the default hardware
platform, and the second using a FadeCandy:


::

    
    leds:
        led00:
            number: 00
        led01:
            number: 00
            platform: fadecandy


.. _blog post on getting MPF running with a Stern S.A.M. machine: https://missionpinball.com/blog/2015/04/mpf-working-on-a-stern-sam-machine/


