Dual-wound Coils
================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/dual_wound_coils`                                              |
+------------------------------------------------------------------------------+

A *dual-wound coil* is a coil (solenoid) with two windings--one "strong"
power (or "main") winding for moving the coil, and a second weaker / lower-power
winding for "holding" the coil in the active position.

Dual-wound coils are typically used for flippers, diverters, gates, and
other devices in pinball machines that need a strong initial movement
followed by an extended hold period.

There are many places in MPF config files where you need to specify a coil name.
Rather than adding dual-wound coil logic in many different sections of MPF, we
have a dual-wound coil config where you can specify the settings for a
particular dual-wound coil (and give it a new name), and then you can use that
dual-wound coil anywhere in MPF that a coil is configured.

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`/about/help_us_to_write_it`                                            |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| None                                                                         |
+------------------------------------------------------------------------------+

.. toctree::
   :titlesonly:

   dual_vs_single_wound


