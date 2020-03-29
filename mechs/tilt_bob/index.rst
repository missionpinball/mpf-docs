Tilt Bob
========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

:doc:`TODO: Add a picture of a tilt bob </about/help_us_to_write_it>`

The tilt bob is a plumb pop centered in a metal ring which acts as a switch.
On movement the switch closes which usually triggers a tilt warning.

You can configure it just like a
:doc:`mechanical switch </mechs/switches/mechanical_switches>`.
In addition you want to add the ``tilt_warning`` tag and add the built-in
:doc:`tilt mode </game_logic/tilt/index>` in the list of your modes.

This is an example:

.. code-block:: mpf-config

   modes:
     - tilt
   switches:
     s_tilt:
       number: 23    # number depends on your platform
       tags: tilt_warning

Part numbers:

* A-15361 or 04-10346 (Williams/Bally)
* 500-5023-00 (Stern)
* A-205-1 (Chicago Coin/early Stern)
* 95-0328-00 or PLABS (Bally/Capcom)

+------------------------------------------------------------------------------+
| Related How To guides                                                        |
+==============================================================================+
| :doc:`/game_logic/tilt/index`                                                |
+------------------------------------------------------------------------------+
