track_player:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``tracks:`` section of a step.

.. overview

The ``track_player:`` section of your config is where you specify actions to perform on audio
tracks when MPF events are received. Tracks can be stopped, paused, or played with an optional
fade time. The volume of a track can also be changed with an optional fade time. Finally, all
sounds currently playing on a track can be stopped (again with an optional fade
out time). (This player is part of the MPF media controller and only available if you're
using MPF-MC for your media controller.)

See the :doc:`config player </config_players/index>` for more information on config players.


Usage in config files
---------------------

In config files, the track player is used via the ``track_player:`` section.  Event names that
will trigger track actions are nested sub-headings and track names are listed as nested
sub-headings below that.  ``__all__`` can be used in place of a track name to apply the action
to all audio tracks in the sound system.

Example:

::

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

Usage in shows
--------------

In shows, the track player is used via the ``tracks:`` section of a step.

Example:

::

    shows:
        my_show_with_sound:
            - time: 0
                tracks:
                    music:
                        action: set_volume
                        volume: 0.3
                        fade: 0.25 sec
            - time: 3.5
                tracks:
                    music:
                        action: set_volume
                        volume: 0.5
                        fade: 0.25 sec

Required settings
-----------------

The following sections are required for each named sound pool in your config:

action:
~~~~~~~
Single value, type: one of the following options: play, stop, pause, set_volume, stop_all_sounds.
Default: None

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

volume:
~~~~~~~
Single value, type: ``gain setting`` (:doc:`Instructions for entering gain values </config/instructions/gain_values>`)
-inf, db, or float between 0.0 and 1.0. Default: ``0.5``

The new volume setting for the track.  As with all volume parameters in MPF, this item can be
represented as a number between 0.0 and 1.0 (1.0 is max volume, 0.0 is off, 0.9 is 90%, etc.)
It also can be represented as a decibel string from -inf to 0.0 db (ex: ``-3.0 db``). This
setting only applies to the ``set_volume`` action and will be ignored for all others.

fade:
~~~~~

Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`).
Default: ``0``

The number of seconds over which to fade the specified track action.  Applies to all track player
actions.

Express configuration
---------------------

There is no express (one line) configuration for the track player.  You must specify the ``action``
setting every time.

