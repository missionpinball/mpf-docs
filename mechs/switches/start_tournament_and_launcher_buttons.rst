Start, Tournament and Launcher Buttons
======================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+

Probably all pinball machines have a start button which will start the
:doc:`game </game_design/index>` once you press it and there are enough
:doc:`credits </game_logic/credits/index>`.
Furthermore, machines have either a mechanical plunger or a launcher button
which will :doc:`shoot the ball from the launcher </mechs/plungers/coil_fired>`.
Additionally, some machines have tournament buttons to start a tournament.


Hardware
--------

:doc:`TODO: Add a picture of button </about/help_us_to_write_it>`

Those buttons usually come with a :doc:`micro switch <mechanical_switches>` and
a :doc:`#555 bulb </mechs/lights/matrix_lights>`.
You can connect the switches to any direct input on your controller or put them
into your switch matrix (with an additional diode).
The LED is rated at 6.3V which works fine at either 5V or in a lamp matrix
at 12V (the latter commonly used).

Config
------

To configure your start button you can use this config:

.. code-block:: mpf-config

   lights:     
      l_start_button:
         number: 3		   # number depends on your platform
         subtype: matrix   # depends on your platform

   switches:
      s_start:
         number: 23    	   # number depends on your platform
         tags: start


The tag ``start`` will hook the button into your game.
See :doc:`/tutorial/9_start_button` for details.
You might want to integrate the button into your attract light show.


Related How To guides
---------------------

See the documentation of your platform on how to configure GIs.

+------------------------------------------------------------------------------+
| Platform related How To                                                      |
+==============================================================================+
| :doc:`/tutorial/9_start_button`                                              |
+------------------------------------------------------------------------------+
| :doc:`mechanical_switches`                                                   |
+------------------------------------------------------------------------------+
| :doc:`/mechs/lights/matrix_lights`                                           |
+------------------------------------------------------------------------------+
