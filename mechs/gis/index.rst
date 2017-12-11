GI (general illumination)
=========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/light_player`                                                  |
+------------------------------------------------------------------------------+

.. contents::
   :local:

MPF includes support for GI (general illumination) light strings which are
common in existing Williams and Stern machines. You can specify GI
strings which you can then enable, disable, or (if the hardware supports it)
dim.

.. note::

   In MPF 0.50 GIs became :doc:`/config/lights` with ``subtype`` gi. They behave
   like any other lights in MPF.

GI Strings are actually kind of complex. Many of them are AC (even in WPC
machines), and some Williams WPC machines include triacs (kind of like a
transistor for AC) and "zero cross" AC waveform detection circuits so they can
sync their dimming commands with the AC current wave. Later Williams WPC
machines split their GI into non-dimmable (which used still used AC) and
switched their dimmable to DC. Some machines also have "enable" relays that
must be activated first before certain GI strings will work.

MPF hides all this complexity from you. You just define your GI strings in
your machine :doc:`/config/lights` section and then you can enable, disable, and
dim the dimmable ones as you wish.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for lights is ``device.lights.<name>``.

*brightness*
   The numeric value of the brightness of this GI string, from 0-255.

Related How To guides
---------------------

:doc:`/about/help_us_to_write_it`

Related Events
--------------

None
