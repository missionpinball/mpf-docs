Migrating from config version 4 to 5 of MPF
===========================================

This topic gives step-by-step instructions to migrate from config version 4 to 5 (0.33 to 0.50) of MPF.  If you are
using a version of MPF older than 0.33, please upgrade to 0.33 (config version 4) prior to following these
instructions.

Here are the steps:

1. Update the config version number
-----------------------------------

The very first line in all your machine config files should be the following:

.. code-block:: yaml

   #config_version=4

Change it in every config file to version 5:

.. code-block:: yaml

   #config_version=5


2. Config files are now case sensitive
--------------------------------------

Setting names in config files are now case sensitive. In MPF 0.17 to 0.33 settings were case insensitive but it
caused many problems and thus has been dropped. Please carefully review your config files to ensure you use
consistent casing in your names.


3. Rename scoring section to variable_player
--------------------------------------------

The ``scoring:`` config section has been renamed to ``variable_player:`` to more accurately convey its functionality
(since it can be used to set new values of both machine and player variables and not just change the score). The
``score:`` section in show steps has been renamed to ``variables:``.  Finally, the ``score:`` setting under these
sections has been renamed ``int:`` for consistency and to avoid confusion since it is really setting an integer value
of the specified variable and may be totally unrelated to score.

Steps to update your configs:

- Rename the ``scoring:`` section in all your config files to ``variable_player:``.
- Rename the ``score:`` section in all your show steps to ``variables:``.
- Rename the ``score:`` setting in the above sections to ``int:``.

.. note::
   Be very careful when renaming any ``score:`` entry in these sections as there were three possible uses of this value
   (which has led to some confusion and is one of the reasons for making this change).  ``score:`` can be the name of a
   show step section (should be easy to recognize as it is found only in shows) and will be the highest indent level for
   a ``score:`` entry in a show file.  ``score:`` is also the name of a player variable and must not be renamed when used
   in this context.  Finally, ``score:`` sometimes refers to the new integer value to add or set the player variable.

Here is an example of scoring used in a config file in MPF 0.33 and how to modify it for 0.50:

.. code-block:: yaml

   scoring:             # Rename to 'variable_player:'
     test_event1:
       score: 100       # DO NOT RENAME, refers to player variable name
       var_a: 1
       var_c: current_player.ramps
     test_set_100:
       score:           # DO NOT RENAME, refers to player variable name
         score: 100     # Rename to 'int:' as it refers to new int value to set score variable to
         action: set
     test_set_200:
       test1:
         score: 200     # Rename to 'int:' as it refers to new int value to set test1 variable to
         action: set
     test_set_string:
       string_test:
         string: HELLO
     test_set_machine_var:
       my_var:
         score: 100     # Rename to 'int:' as it refers to new int value to set my_var variable to
         action: set_machine
     test_add_machine_var:
       my_var:
         score: 23      # Rename to 'int:' as it refers to new int value to set my_var variable to
         action: add_machine
     test_score_mode:
       score: 100       # DO NOT RENAME, refers to player variable name
     s_counter_target_active:
       score: 10        # DO NOT RENAME, refers to player variable name
     s_kills_counter_target_active:
       score: 100       # DO NOT RENAME, refers to player variable name

Here is the same config example after modification in 0.50:

.. code-block:: mpf-config

   ##! mode: my_mode
   variable_player:
     test_event1:
       score: 100
       var_a: 1
       var_c: current_player.ramps
     test_set_100:
       score:
         int: 100
         action: set
     test_set_200:
       test1:
         int: 200
         action: set
     test_set_string:
       string_test:
         string: HELLO
     test_set_machine_var:
       my_var:
         int: 100
         action: set_machine
     test_add_machine_var:
       my_var:
         int: 23
         action: add_machine
     test_score_mode:
       score: 100
     s_counter_target_active:
       score: 10
     s_kills_counter_target_active:
       score: 100

Here is an example of scoring used in a show in MPF 0.33 and how to modify it for 0.50:

.. code-block:: yaml

   shows:
     example_show_name:
       - time: 0
         score:         # Rename to 'variables:'
           score: 10    # DO NOT RENAME, refers to player variable name
       - time: 1
         score:         # Rename to 'variables:'
           score:       # DO NOT RENAME, refers to player variable name
             score: 200 # Rename to 'int:' as it refers to new int value to add to score variable
       - time: 2
         score:         # Rename to 'variables:'
           loops:       # player variable name
             score: 10  # Rename to 'int:' as it refers to new int value to add to score variable

Here is the same show example after modification in 0.50:

.. code-block:: mpf-config

   shows:
     example_show_name:
       - time: 0
         variables:
           score: 10
       - time: 1
         variables:
           score:
             int: 200
       - time: 2
         variables:
           loops:
             int: 10


4. Rename physical dmd sections
-------------------------------

The ``physical_dmds:`` and ``physical_rgb_dmds:`` config sections have been renamed to ``dmds:`` and ``rgb_dmds:``.
If you use these sections, rename them as specified.


5. Event changes for game and mode lifecycle
--------------------------------------------

Several changes were made to game and mode events to be more consistent and allow more flexibility.

- The ``player_add_success`` event has been renamed to ``player_added``. Find all occurrences in your machine
  config files and any custom code and rename them.
- The ``player_turn_start`` event has been removed and replaced with 3 events: ``player_turn_will_start``,
  ``player_turn_starting`` (a queue event), and ``player_turn_started``. It is recommended you use
  ``player_turn_started`` to replicate the existing behavior.  Be sure to find and replace all
  occurrences in both config files and custom code.
- The ``player_turn_stop`` event has been removed and replaced with 3 events: ``player_turn_will_end``,
  ``player_turn_ending`` (a queue event), and ``player_turn_ended``. It is recommended you use
  ``player_turn_ended`` to replicate the existing behavior.  Be sure to find and replace all
  occurrences in both config files and custom code.
- The ``Game.ball_ending`` method has been deprecated and replaced with the ``Game.end_ball`` method. This
  will only affect you if you have custom code that calls the deprecated method. Modify your custom code to use
  the new method.
- The ``Game.game_ending`` method has been deprecated and replaced with the ``Game.end_game`` method. This
  will only affect you if you have custom code that calls the deprecated method. Modify your custom code to use
  the new method.


6. Display refactor changes
---------------------------

Several changes were made to the various display components of the media controller. This section will
lead you through the various steps to modify your display-related configurations.

dmd and color_dmd widgets have been removed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``dmd`` and ``color_dmd`` widgets have been removed and replaced with a new ``display`` widget and
associated ``effects`` setting (``dmd`` and ``color_dmd`` have become effects that can be applied
to any ``display`` widget). The following ``dmd`` widget settings have moved to the effects section
(``type: dmd``): dot_filter, blur, pixel_size (now dot_size), pixel_color (now dot_color), dark_color
(now filter_color), bg_color (now background_color), gain, shades, and luminosity. The following ``color_dmd``
widget settings have moved to the effects section (``type: color_dmd``): dot_filter, blur, pixel_size
(now dot_size), dark_color (now filter_color), bg_color (now background_color, gain, and shades. For
detailed information see the :doc:`display </displays/widgets/display/index>` and
:doc:`display effects </displays/widgets/display/effects>` sections of the documentation.

Here is an example slide config from 0.33 using ``dmd`` and ``color_dmd`` widgets:

.. code-block:: yaml

   slides:
     dmd_slide:
       - type: dmd
         width: 640
         height: 160
         source_display: dmd
         color: ff00aa
         gain: 2
     color_dmd_slide:
       - type: color_dmd
         width: 640
         height: 160
         source_display: dmd
         shades: 4
         gain: 1.5

In 0.50 the above example becomes:

.. code-block:: mpf-config

   slides:
     dmd_slide:
       - type: display
         width: 640
         height: 160
         source_display: dmd
         effects:
           - type: dmd
             dots_x: 128
             dots_y: 32
             dot_color: ff00aa
             gain: 2
     color_dmd_slide:
       - type: display
         width: 640
         height: 160
         source_display: dmd
         effects:
           - type: color_dmd
             dots_x: 128
             dots_y: 32
             shades: 4
             gain: 1.5

Be sure to specify the ``dots_x`` and ``dots_y`` settings in your new config (the number of dots that will
be drawn in the dmd effects). These values used to be automatically set  based on the dimensions of the display
specified in the ``source_display`` setting. However, they have not been decoupled and can be set as desired.

slide_frame widgets have been removed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``slide_frame`` widgets have been removed and replaced by a combination of a ``display`` widget and a
corresponding entry in the ``displays:`` section. The changes are best illustrated using an example. This
step only applies to your project if you are using ``slide_frame`` widgets.

Example in MPF 0.33 using slide frames:

.. code-block:: yaml

   displays:
     default:
       width: 400
       height: 300

   slides:
     slide1:
     - type: slide_frame
       width: 200
       height: 100
       name: frame1
       y: 50
       x: 50
       anchor_y: bottom
       anchor_x: left
     - type: text
       text: SLIDE FRAME IN SLIDE 1
       font_size: 20
       y: bottom
       anchor_y: bottom
     slide2:
     - type: text
       text: slide2
     frame1_text:
     - type: text
       text: SLIDE 1 IN FRAME
       color: lime
       font_size: 10
     - type: rectangle
       width: 200
       height: 100
       color: 550000
     frame1_text2:
     - type: text
       text: SLIDE 2 IN FRAME
       color: black
       font_size: 10
     - type: rectangle
       width: 200
       height: 100
       color: 00ff00

   slide_player:
     show_slide1: slide1
     show_slide2: slide2
     show_frame_text:
       frame1_text:
         target: frame1
     show_frame_text2:
       frame1_text2:
         target: frame1

Now the same configuration in MPF 0.50 becomes:

.. code-block:: mpf-config

   displays:
     default:
       width: 400
       height: 300
     frame1:
       width: 200
       height: 100

   slides:
     slide1:
     - type: display
       width: 200
       height: 100
       source_display: frame1
       y: 50
       x: 50
       anchor_y: bottom
       anchor_x: left
     - type: text
       text: SLIDE FRAME IN SLIDE 1
       font_size: 20
       y: bottom
       anchor_y: bottom
     slide2:
     - type: text
       text: slide2
     frame1_text:
     - type: text
       text: SLIDE 1 IN FRAME
       color: lime
       font_size: 10
     - type: rectangle
       width: 200
       height: 100
       color: 550000
     frame1_text2:
     - type: text
       text: SLIDE 2 IN FRAME
       color: black
       font_size: 10
     - type: rectangle
       width: 200
       height: 100
       color: 00ff00

   slide_player:
     show_slide1: slide1
     show_slide2: slide2
     show_frame_text:
       frame1_text:
         target: frame1
     show_frame_text2:
       frame1_text2:
         target: frame1

To modify your configs, do the following steps for each ``slide_frame`` widget:

- Create an entry in your ``displays:`` section using the ``name:`` setting of the ``slide_frame``.
  Also set the ``width:`` and ``height:`` settings of the display using the values from the slide frame.
- Change the widget ``type:`` value from ``slide_frame`` to ``display``.
- Change the widget ``name:`` setting to ``source_display:``.

Don't forget if you have any trouble with these migration steps to post your issue in the MPF Users forum.
Other users who have already gone through the migration process will be happy to help.

image widget loops setting changed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``loops:`` setting of image widgets has been altered to be consistent with other areas of MPF (``-1`` to
loop infinitely, ``0`` no repeats/loops, ``> 0`` the number of times to repeat after the first time through).
Previously a value of ``0`` indicated infinite looping. Please review your image widget ``loops:`` settings and
subtract 1 from any existing value to maintain the same behavior as previously.

widget animations now use anchor position
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All widget animations now use the widget anchor position when animating widget position values (``x``, ``y``,
``pos``).  In MPF versions prior to 0.50 widget position animations always used the lower-left corner, even
when a different widget anchor position was set. This made it difficult to return widgets to their start
position when the animations used different coordinate offsets than the widget (animating the widget back to
the same numeric starting position put the widget in a different location than it was in originally).  Now
the position coordinates are consistent no matter the anchor position. Please review your widget position
animations and adjust any values accordingly to get the behavior you want.  Widgets that have a lower-left
corner anchor position will not need any adjustments.


7. Move logic blocks one level up
---------------------------------

Logic blocks have been moved one level. Up previously you would have this in your config:

.. code-block:: yaml

    logic_blocks:
      counters:
        your_counter:
          count_events: count_it_up

In 0.50 just use:

.. code-block:: mpf-config

    counters:
      your_counter:
        count_events: count_it_up

8. Renamed coil settings
------------------------

``pulse_ms``, ``pulse_power`` and ``hold_power`` have been split into two settings each.
Rename ``pulse_ms`` into ``default_pulse_ms`` which very much behaves the same.
This setting will be used if the coil is pulsed without any further settings.
Furthermore, you may configure ``max_pulse_ms`` to limit the pulse length to prevent damage on your coils.

``hold_power`` had a scale from 1-8 which was kind of arbitrary.
We changed that to 0.0 to 1.0 (for 0% to 100% power) in 0.50.
Therefore, if you used ``hold_power: 2`` that would become ``default_hold_power: 0.25`` (2 -> 2/8 = 0.25).
Furthermore, you can set ``max_hold_power`` to limit the maximum hold power (defaults to ``default_hold_power`` if you
do not specify it).
The same applies to ``pulse_power`` which becomes ``default_pulse_power`` and ``max_pulse_power``.

Your coil could look like this in 0.50:

.. code-block:: mpf-config

    coils:
        flipper_right_main:
            number: A0-B0-0
            default_pulse_ms: 10
            max_pulse_ms: 100
            default_pulse_power: 0.25
            max_pulse_power: 0.5

See :doc:`coils </config/coils>` for details.

9. Matrix_lights, leds, GIs, and flashers become lights
-------------------------------------------------------

All types of lights have been unified in MPF 0.50 and are configured in the ``lights`` section.
Since some platforms support differnt types of lights with the same number we added a ``subtype`` setting which can be
either ``matrix``, ``gi``, ``led`` or ``flasher``.

Lights look like this in MPF 0.50:

.. code-block:: mpf-config

    lights:
      gi_01:
         number: G01
         subtype: gi
      led_01:
         number: 7
         subtype: led
      matrix_light_01:
         number: L66
         subtype: matrix

You can use ``light_player`` for all types of lights. ``led_player`` and ``gi_player`` consequently have been removed.
Furthermore you can use ``flasher_player`` on all types lights (e.g. to flash the whole playfield with all GIs).

See :doc:`lights </config/lights>` for details.

10. Define a source device for your playfield
---------------------------------------------

Remove ``tags: ball_add_live`` from your ball devices and instead define a ``default_source_device``
to feed the playfield:

.. code-block:: mpf-config

    #! switches:
    #!     s_plunger:
    #!         number: 10
    #! ball_devices:
    #!     bd_plunger:
    #!         ball_switches: s_plunger
    #!         mechanical_eject: true
    playfields:
       playfield:
           default_source_device: bd_plunger
           tags: default

11. If you are using counters in your slides add a variable_player
------------------------------------------------------------------

Counters no longer save their state in player variables.
If you are using something like ``(YOUR_COUNTER_count)`` in a slide or widget
you can use a :doc:`variable_player </config_players/variable_player>` to restore
the old behaviour:

.. code-block:: mpf-config

   ##! mode: my_mode
   variable_player:
      logicblock_YOUR_COUNTER_updated:
          YOUR_COUNTER_count:
              int: value
              action: set

12. Sequence shots became separate devices
------------------------------------------

If you are using ``switch_sequences`` in your :doc:`shots </config/shots>`
convert them to a separate device.

Old syntax:

.. code-block:: yaml

   switches:
      switch1:
         number:
      switch2:
         number:
      switch3:
         number:

   shots:
      left_orbit:
          switch_sequence: switch1, switch2, switch3
          time: 3s

New syntax:

.. code-block:: mpf-config

   switches:
      switch1:
         number:
      switch2:
         number:
      switch3:
         number:

   sequence_shots:
      left_orbit_sequence:
         switch_sequence: switch1, switch2, switch3
         sequence_timeout: 3s

   ##! mode: test
   # in case you still want the shot (does not do much anymore in this example):
   shots:
      left_orbit:
         hit_events: left_orbit_sequence_hit

   ##! test
   start_game
   start_mode test
   mock_event left_orbit_sequence_hit
   mock_event left_orbit_hit
   hit_and_release_switch switch1
   hit_and_release_switch switch2
   hit_and_release_switch switch3
   assert_event_called left_orbit_sequence_hit
   assert_event_called left_orbit_hit
