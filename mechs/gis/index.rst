GI (general illumination)
=========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/gis`                                                           |
+------------------------------------------------------------------------------+
| :doc:`/config/gi_player`                                                     |
+------------------------------------------------------------------------------+

MPF includes support for GI (general illumination) light strings which are
common in existing Williams and Stern machines. You can specify GI
strings which you can then enable, disable, or (if the hardware supports it)
dim.

.. note::

   GI strings in the "gis:" config section are only for older existing machines
   that specifically have driver-powered GI strings. New custom machines will
   just use LEDs for GIs, and they are configured as LEDs, not GIs.

GI Strings are actually kind of complex. Many of them are AC (even in WPC
machines), and some Williams WPC machines include triacs (kind of like a
transistor for AC) and "zero cross" AC waveform detection circuits so they can
sync their dimming commands with the AC current wave. Later Williams WPC
machines split their GI into non-dimmable (which used still used AC) and
switched their dimmable to DC. Some machines also have "enable" relays that
must be activated first before certain GI strings will work.

MPF hides all this complexity from you. You just define your GI strings in
your machine configuration file and then you can enable, disable, and
dim the dimmable ones as you wish.

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| TODO                                                                         |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| None                                                                         |
+------------------------------------------------------------------------------+
