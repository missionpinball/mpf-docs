Config Players
==============

An important concept to using the YAML-based configuration files is something we call *config players*.

*Config players* in MPF have nothing to with the actual human players of your machine, rather, they are things that
"play" based on configurations.

Config players are used in both the machine-wide and mode-specific config files, and also in show steps.

* In a config file, the config players are setup via the ``<config_player_name>_player:`` section of the file.
* In show steps, config players are accessed via the ``<config_player_name>s:`` setting.

Some examples:

* You play sounds via a config file in the ``sound_player:`` section, and you play sounds from a show step via the
  ``sounds:`` setting for that step.
* You show slides on a display via a config file in the ``slide_player:`` section, and you show slides from a show step
  via the ``slides:`` setting for that step.
* You set the color of LEDs via a config file in the ``led_player:`` section, and you set colors from a show step
  via the ``leds:`` setting for that step.
* etc.

There are several different config players in MPF and MPF-MC. Click on each below for specific details of how to use
them, with explanations of how to use them in config files and in shows.

.. toctree::
   :maxdepth: 1

   bcp_player
   coil_player
   event_player
   flasher_player
   gi_player
   led_player
   light_player
   playlist_player
   plugin_player
   queue_event_player
   queue_relay_player
   random_event_player
   show_player
   slide_player
   sound_loop_player
   sound_player
   track_player
   trigger_player
   widget_player
