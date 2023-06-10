light_segment_displays:
=======================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``platform_settings:`` of your ``segment_displays`` section is where you
map segment displays to lights when using the
:doc:`light segment displays platform </hardware/light_segment_displays/index>`.

.. config


Optional settings
-----------------

The following sections are optional in the ``light_segment_displays:`` section of your config. (If you don't include them, the default will be used).

display_flash_duty:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.5``

For 7segment your segments are: a, b, c, d, e, f, g and dp (see: `7-Segment Displays in Wikipedia <https://en.wikipedia.org/wiki/Seven-segment_display_character_representations>`_ for details)
For BCD your segments are: x0, x1, x2, x3 and dp (see: `Binary Coded Decimal in Wikipedia <https://en.wikipedia.org/wiki/Binary-coded_decimal>`_ for details)
For 14segment your segments are: l, m, n, k, j, h, g2, g1, f, e, d, c, b, a and dp (see: `14 Segment Displays in Wikipedia <https://en.wikipedia.org/wiki/Fourteen-segment_display>`_ for details)
For 16segment your segments are: u, t, s, r, p, n, m, k, h, g, f, e, d, c, b, a and dp (see: `16 Segment Displays in Wikipedia <https://en.wikipedia.org/wiki/Sixteen-segment_display>`_ for details)

dp is an optional decimal point per display.

display_flash_frequency:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

How fast should the displays flash? Defaults to once per second or 1Hz.


Related How To guides
---------------------

* :doc:`/hardware/light_segment_displays/index`
* :doc:`/displays/display/alpha_numeric`
* :doc:`/hardware/segment_display_platforms`
