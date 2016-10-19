Flasher
=======

*MPF Device*

MPF includes support for flashers, which are essentially just really
bright lights that are controlled via high-power driver transistors instead
of low-power lighting circuitry.

MPF's flasher devices are only used in older machines (WPC, Stern SAM, System 11)
since modern LED-based machines typically use regular LED devices (or combinations
of them) as flashers. (So basically a "flasher" in MPF is any single-color
light that's connected to a driver output rather than a light output.


Configure your flashers in the `flashers: </config/flashers>`_
section of your machine config file.
