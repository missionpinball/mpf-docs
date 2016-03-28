
The `led_settings:`section of your machine configuration files lets
you configure settings for RGB LEDs in your machine. This sectioncan
be used in your machine-wide config files. This section *cannot* be
used in mode-specific config files. This section is included in the
`mpfconfig.yaml` file. You only need to add them to your own machine
config files if you want to override a default


::

    
    led_settings:
        brightness_compensation: 1.0
        default_led_fade_ms: 100
        gamma: 2.5
        whitepoint: 1.0, 1.0, 1.0
        linear_slope: 1.0
        linear_cutoff: 0.0
        keyframe_interpolation: True
        dithering: True




brightness_compensation:
~~~~~~~~~~~~~~~~~~~~~~~~

The brightness_compensation multiplier that will be used for all LEDs
in your machine. This is applied to all LEDs, even if they have their
own brightness compensation settings. (So if you have a global
brightness compensation setting of 0.85, and an individual LED has a
brightness compensation setting of 0.9, then sending that LED a "full"
brightness of 255 will actually send it a value of 195. (255 * 0.85 *
0.9) This is done on purpose so you can set machine-wide "dimming"
here at the global level while still being able to tweak relative
brightness levels of individual LEDs.



default_led_fade_ms:
~~~~~~~~~~~~~~~~~~~~

This is the default *fade_ms* that will be applied to individual RGB
LEDs that don't have fade_ms settings configured. If you configure an
individual LED's *fade_ms*, it will override this setting. Note that
this feature currently only works with LEDs connected to a
Multimorphic PD-LED board. FadeCandy and FAST controller support will
be added in the future.



gamma:
~~~~~~

Specifies the `gamma correction`_ value for the LEDs. The default is
2.5. This setting currently only affects LEDs connected to a FadeCandy
LED controller.



whitepoint:
~~~~~~~~~~~

Specifies the white point (or white balance) of your LEDs. Enter it as
a list of three floating point values that correspond to the red,
blue, and green LED segments. These values are treated as multipliers
to all incoming color commands. The default of `1.0, 1.0, 1.0` means
that no white point adjustment is used. `1.0, 1.0, 0.8` would set the
blue segment to be at 80% brightness while red and green are 100%,
etc. This setting currently only affects LEDs connected to a FadeCandy
LED controller.



linear_slope:
~~~~~~~~~~~~~

Specifies the slope (output / input) of the linear section of the
brightness curve for the LEDs. The default is 1.0. This setting
currently only affects LEDs connected to a FadeCandy LED controller.



linear_cutoff:
~~~~~~~~~~~~~~

This is best explained by quoting the FadeCandy documentation:
By default, brightness curves are entirely nonlinear. By setting
linearCutoff to a nonzero value, though, a linear area may be defined
at the bottom of the brightness curve. The linear section, near zero,
avoids creating very low output values that will cause distracting
flicker when dithered. This isn't a problem when the LEDs are viewed
indirectly such that the flicker is below the threshold of perception,
but in cases where the flicker is a problem this linear section can
eliminate it entierly at the cost of some dynamic range. To enable the
linear section, set linearCutoff to some nonzero value. A good
starting point is 1/256.0, correspnding to the lowest 8-bit PWM level.
The default value is 1.0. This setting currently only affects LEDs
connected to a FadeCandy LED controller.



keyframe_interpolation:
~~~~~~~~~~~~~~~~~~~~~~~

Boolean value that enables keyframe interpolation to smooth the color
transition of LEDs in between machine ticks. For example, if your
machine Hz rate is 30, that means the fastest MPF can update LEDs is
30 times per second. While that's really fast, some players might
perceive step "steps" between each step of the color change—especially
if LEDs are going from off to full brightness. Enabling keyframe
interpolation means the LED controller hardware will automatically in
color frames in between color updates from MPF. For example, when
keyframe interpolation is enabled, the FadeCandy LED controller will
update all the LEDs 400 times per second, generating in-between color
values which make the LEDs look smooth. The results are beautiful.
This setting is enabled by default. This setting currently only
affects LEDs connected to a FadeCandy LED controller.



dithering:
~~~~~~~~~~

Boolean value that controls whether the hardware LED controller will
use dithering to simulate richer and smoother colors than the hardware
LEDs can provide. (More details are available in the `FadeCandy
documentation`_.) This setting is enabled by default. This setting
currently only affects LEDs connected to a FadeCandy LED controller.

.. _gamma correction: http://en.wikipedia.org/wiki/Gamma_correction
.. _FadeCandy documentation: https://github.com/scanlime/fadecandy


