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


2. Rename physical dmd sections
-------------------------------

The ``physical_dmds:`` and ``physical_rgb_dmds:`` config sections have been renamed to ``dmds:`` and ``rgb_dmds:``.
If you use these sections, rename them as specified.


3. Event changes for game and mode lifecycle
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


4. Display refactor changes
---------------------------

The way graphics are displayed in the media controller has been changed.

TODO: Finish this document

5. Move logic blocks one level up
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

6. Renamed coil settings
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

7. Matrix_lights, leds, GIs, and flashers become lights
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

