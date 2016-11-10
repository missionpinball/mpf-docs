
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







.. _blog post on getting MPF running with a Stern S.A.M. machine: https://missionpinball.com/blog/2015/04/mpf-working-on-a-stern-sam-machine/


