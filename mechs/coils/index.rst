Coils (Solenoids)
=================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/coil_player`                                                   |
+------------------------------------------------------------------------------+

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

In MPF, you typically list all the coils in your machine in the
:doc:`coils: section </config/coils>` of your machine configuration file, along
with default options for them, like pulse times, PWM values, whether they can
be enabled (held on), etc.

.. image:: /mechs/images/coil.jpg

You don't typically work with coils directly, rather, you tend to add them to
other devices once they've been defined (flippers, autofires, ball devices,
diverters, etc). You can configure :doc:`dual_wound_coils` on top of coils.

That said, it is possible to perform actions on coils directly, such as pulsing,
enabling, or disabling them. You can do this via the :doc:`/config/coil_player`
section of a config file or via the ``coils:`` section of a
:doc:`show </shows/index>`.

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`/tutorial/3_get_flipping`                                              |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| None                                                                         |
+------------------------------------------------------------------------------+

.. toctree::

   pulse_power
   hold_power
   recycle
   dual_wound_coils
   dual_vs_single_wound

