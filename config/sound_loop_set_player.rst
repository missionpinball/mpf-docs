sound_loop_set_player:
======================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``sound_loop_sets:`` section
of a step.

.. overview

The ``sound_loop_set_player:`` section of your config is where you specify actions to perform
on sound loop sets when MPF events are received.  Additional information may be found in the
:doc:`sound_player </config_players/sound_loop_set_player>` documentation.

Required settings
~~~~~~~~~~~~~~~~~

The following sections are required in the ``layers:`` section of your config:

track:
^^^^^^
Single value, type: ``string``.

This is the name of the track on which to perform the specified action. This must be an existing
sound loop track. (You configure tracks and track names in the
:doc:`sound_system: </config/sound_system>` section of your machine config files.)

Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``sound_loop_set_player:`` section of your config.
(If you don't include them, the default will be used).

action:
^^^^^^^
Single value, type: one of the following options: play, stop.

The ``action:`` setting controls what action will be performed on the specified sound loop set.
Options for ``action:`` are:

+ ``play`` - The specified sound loop set will be played. Additional settings control whether the
  playback will begin immediately or after the currently playing loop set reaches the end of the
  master sound. Will cross-fade with the currently playing sound loop set if a ``fade_in`` setting
  is used.
+ ``stop`` - The currently playing sound loop set will be stopped.  Will fade out before stopping if
  a ``fade_out`` setting is used.
+ ``stop_looping`` - Looping will be cancelled for the currently playing sound loop set (the sound loop
  set will continue to play to the end of the current loop).
+ ``play_layer`` - Plays the sound on the specified layer in the currently playing loop set. Additional
  settings control whether the layer will begin immediately or will wait until after the currently
  playing loop set reaches the end of the sound. Will fade in if a ``fade_in`` setting is used.
+ ``stop_layer`` - Stops the sound on the specified layer in the currently playing loop set.  Will fade
  out before stopping if a ``fade_out`` setting is used.
+ ``stop_looping`` - Looping will be cancelled for the sound on the specified layer in the currently
  playing sound loop set (the sound on the layer will continue to play to the end of the current loop).

Other available optional settings:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several other settings may be used in the sound player to override settings specified in the
``sounds:`` section of config files.  Please refer to the :doc:`sounds: </config/sounds>`
documentation for details about each setting.

+ ``loops:``
+ ``priority:``
+ ``max_queue_time:``
+ ``volume:``
+ ``fade_in:``
+ ``fade_out:``
+ ``start_at:``
+ ``events_when_played:``
+ ``events_when_stopped:``
+ ``events_when_looping:``
+ ``mode_end_action:``

Express configuration
---------------------

The ``sound_loop_set_player`` does not support an express configuration.

