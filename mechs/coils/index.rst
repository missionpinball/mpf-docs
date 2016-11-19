Coils (Solenoids)
=================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/coil_player`                                                   |
+------------------------------------------------------------------------------+

In MPF, you typically list all the coils in your machine in the
:doc:`coils: section </config/coils>` of your machine configuration file, along
with default options for them, like pulse times, PWM values, whether they can
be enabled (held on), etc.

You don't typically work with coils directly, rather, you tend to add them to
other devices once they've been defined (flippers, autofires, ball devices,
diverters, etc.)

That said, it is possible to perform actions on coils directly, such as pulsing,
enabling, or disabling them. You can do this via the :doc:`coil_player:`
section of a config file or via the ``coils:`` section of a
:doc:`show </shows/index>`.

.. toctree::

   pulse_power
   hold_power
   recycle

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
