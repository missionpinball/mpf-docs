How to configure mono/traditional DMD (P-ROC)
=============================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/physical_dmd`                                                  |
+------------------------------------------------------------------------------+

The P-ROC can drive a traditional single-color pinball DMD via the 14-pin DMD
connector cable that's been in most pinball machines for the past 25 years.

To do this, follow the :doc:`/displays/display/physical_mono_dmd` guide.

If you want to drive an RGB LED DMD and you're using a P-ROC, you can do that
by adding a :doc:`SmartMatrix </hardware/smartmatrix/index>` or
:doc:`RGB.DMD </hardware/eli_dmd>` board which you would then use in place of
the P-ROC's 14-pin DMD connector.

Setting the DMD update rate
---------------------------

By default, MPF will send new DMD frames to the P-ROC at about 30 frames per
second. (Technically it sends a new frame every 33ms.)

Fine tuning the DMD timing cycles
---------------------------------

The P-ROC is able to drive a traditional DMD with 16 shades of intensity,
ranging from off (0) to full on (15). Note that the P-ROC doesn't control (or
even know) what color the DMD is as that's dictated by the DMD itself.

The P-ROC creates the appearance of 16 levels of brightness by rapidly
turning individual dots on and off.

For years, DMD's have been high-voltage gas plasma displays, though more
recently they're LED-based (even the single color ones with the 14-pin
connectors).

Some people have reported less-than-optimal quality when using a P-ROC with
certain types of DMDs. To address this, the P-ROC allows you to fine-tune
the timings of the individual `bit planes <https://en.wikipedia.org/wiki/Bit_plane>`_
that make up the image.

For details on this, you can search the `P-ROC forums <http://www.pinballcontrollers.com/forum>`_
for "high_cycles" to find a few threads where people are talking about these
settings. Then you can set them in the ``p_roc: dmd_timing_cycles: section of
your machine-wide config, like this:

::

p_roc:
   dmd_timing_cycles: 90, 190, 50, 377

Note that we do not have specific recommendations for values here and based on
our experience, we haven't found a need to change this. However, if you do have
issues and you get new values by talking to the P-ROC folks, this is how you
adjust them in MPF.

Our recommendation is that you leave the ``dmd_timing_cycles:`` setting out
of your ``p_roc:`` config unless you need it and really know what you're doing.
(There's potential that bad values here could permanently damage your DMD
hardware, so again, only change these if you know what you're doing.)
