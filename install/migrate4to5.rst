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

