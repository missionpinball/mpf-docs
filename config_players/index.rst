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
* You set the color of LEDs via a config file in the ``light_player:`` section, and you set colors from a show step
  via the ``lights:`` setting for that step.
* You set player and machine variables based on events in the ``variable_player:`` section (this is commonly used for
  scoring in your machine), and you set variables from a show step via the ``variables:`` setting of that step.
* etc.


Standalone Config Player
------------------------

General syntax looks like this in a standalone player:

Normal syntax
~~~~~~~~~~~~~

.. code-block:: yaml

   example_player:
     event_which_is_posted_elsewhere:
       <depends on the player>

For example (show_player; short syntax):

.. code-block:: mpf-config

   show_player:
     event_which_is_posted_elsewhere:
       your_show: play

Another example (show_player; long syntax):

.. code-block:: mpf-config

   show_player:
     event_which_is_posted_elsewhere:
       your_show:
         action: play
         sync_ms: 1000

One line syntax
~~~~~~~~~~~~~~~
This is not supported in all players. This usually performs the default action on the element:

.. code-block:: yaml

   example_player:
     event_which_is_posted_elsewhere: <depends on the player>

An example (show_player):

.. code-block:: mpf-config

   show_player:
     event_which_is_posted_elsewhere: your_show

Config Player in a Show
-----------------------

All config players also work in shows.
However, you need to skip the event which triggers the player since the action is triggered by the show.

Normal syntax
~~~~~~~~~~~~~

This supports the same syntax as above (just without the event).
Also note that instead of ``example_player:`` it becomes ``examples:``.

.. code-block:: yaml

   - duration: 2s
     examples:
       <depends on the player>

For example (show_player; short syntax):

.. code-block:: mpf-config

   ##! show: test
   - duration: 2s
     shows:
       your_show: play

Another example (show_player; long syntax):

.. code-block:: mpf-config

   ##! show: test
   - duration: 2s
     shows:
       your_show:
         action: play
         sync_ms: 1000

One line syntax
~~~~~~~~~~~~~~~
There is no one line syntax in shows.


There are several different config players in MPF and MPF-MC. Click on each below for specific details of how to use
them, with explanations of how to use them in config files and in shows.

.. toctree::
   :maxdepth: 1

   coil_player
   display_light_player
   event_player
   flasher_player
   gi_player
   hardware_sound_player
   led_player
   light_player
   playlist_player
   queue_event_player
   queue_relay_player
   random_event_player
   segment_display_player
   show_player
   slide_player
   sound_loop_player
   sound_player
   track_player
   variable_player
   widget_player
