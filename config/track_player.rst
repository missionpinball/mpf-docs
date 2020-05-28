track_player:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``tracks:`` section of a step.

.. overview

The ``track_player:`` section of your config is where you specify actions to perform on audio
tracks when MPF events are received. Tracks can be stopped, paused, or played with an optional
fade time. The volume of a track can also be changed with an optional fade time. Finally, all
sounds currently playing on a track can be stopped (again with an optional fade
out time). (This player is part of the MPF media controller and only available if you're
using MPF-MC for your media controller.)

This is an example:

.. code-block:: mpf-config

    track_player:
      pause_music_track:
        music:
          action: pause
          fade: 1 sec
      resume_music_track:
        music:
          action: play
      stop_sounds_on_all_tracks:
        __all__:
          action: stop_all_sounds
          fade: 0.5 sec

See the :doc:`config player </config_players/index>` for more information on config players.

Express configuration
---------------------

There is no express (one line) configuration for the track player.  You must specify the ``action``
setting every time.

.. config


Required settings
-----------------

The following sections are required in the ``track_player:`` section of your config:

action:
~~~~~~~
Single value, type: one of the following options: play, stop, pause, set_volume, stop_all_sounds. Defaults to empty.

The ``action:`` setting controls what action will be performed on the specified track. Options for
``action:`` are:

+ ``play`` - The specified track will be played after it has been stopped or paused.
+ ``stop`` - The track is stopped (with an optional fade out time).  All sound processing on
  the track is stopped and the track is cleared. All playing and queued sounds are canceled. All
  sound events on the track are ignored/discarded while the track is stopped.
+ ``pause`` - The track is paused (with an optional fade out time).  All sound processing on
  the track is paused. The track will pick-up where it left off when played/resumed. All sound
  events on the track are ignored/discarded while the track is paused.
+ ``set_volume`` - Set a new volume level for the track (with an optional timed fade from the
  current volume level).
+ ``stop_all_sounds`` - Stops all sounds currently playing on the track (with optional fade out
  time) and cancels any pending sounds in the track sound queue. The ``fade_out`` setting for
  any playing sounds will be ignored. The track will continue to process new sound events.


Optional settings
-----------------

The following sections are optional in the ``track_player:`` section of your config. (If you don't include them, the default will be used).

fade:
~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0.1sec``

The number of seconds over which to fade the specified track action.  Applies to all track player
actions.

volume:
~~~~~~~
Single value, type: ``gain setting`` (-inf, db, or float between 0.0 and 1.0). Defaults to empty.

The new volume setting for the track.  As with all volume parameters in MPF, this item can be
represented as a number between 0.0 and 1.0 (1.0 is max volume, 0.0 is off, 0.9 is 90%, etc.)
It also can be represented as a decibel string from -inf to 0.0 db (ex: ``-3.0 db``). This
setting only applies to the ``set_volume`` action and will be ignored for all others.


Related How To guides
---------------------

* :doc:`/config_players/track_player`
* :doc:`/sound/tips_tricks`
