playlist_player:
================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``playlists:`` section of a step.

.. overview

The ``playlist_player:`` section of your config is where you specify actions to perform on playlists
when MPF events are received.  Additional information may be found in the
:doc:`playlist_player </config_players/playlist_player>` documentation.

Examples:

.. code-block:: yaml

   playlist_player:
     play_attract_music:
       playlist:
         playlist: attract_music
         action: play

     advance_playlist:
       playlist:
         action: advance

     stop_playlist:
       playlist:
         action: stop

Basic usage:

.. code-block:: yaml

   playlist_player:
     <triggering_event_name>:
       <playlist track name>:
         action: <action name>
         <optional settings>
     <triggering_event_name>:
       <playlist track name>:
         action: <action name>
         <optional settings>


Required settings
-----------------

The following sections are required in the ``playlist_player:`` section of your config:

track:
^^^^^^
Single value, type: ``string``.

This is the name of the track on which to perform the specified action. This must be an existing
playlist track. (You configure tracks and track names in the
:doc:`sound_system: </config/sound_system>` section of your machine config files.)

Optional settings
-----------------

The following sections are optional in the ``playlist_player:`` section of your config. (If you don't
include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: play, stop. Default: ``play``

The ``action:`` setting controls what action will be performed on the specified sound. Options for
``action:`` are:

+ ``play`` - Plays a playlist on the specified playlist track.  Will crossfade with the currently
  playing playlist if a crossfade setting is used. Any optional parameter values will override the
  playlist's settings.
+ ``stop`` - Stops the currently playing playlist.  Will fade out before stopping if a crossfade
  setting is used.
+ ``advance`` - Advances the currently playing playlist to the next sound.  Uses the crossfade time
  if one is set.
+ ``set_repeat`` - Sets the repeat flag for the currently playing playlist.  Can be used to set or
  clear the flag (turn repeat on or off).

Other available optional settings:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several other settings may be used in the playlist player to override settings specified in the
``playlists:`` section of config files.  The available settings differ depending upon the
value of ``action:``.

play action
~~~~~~~~~~~

+ ``playlist:``
+ ``crossfade_mode:``
+ ``crossfade_time:``
+ ``volume:``
+ ``shuffle:``
+ ``repeat:``
+ ``events_when_played:``
+ ``events_when_stopped:``
+ ``events_when_looping:``
+ ``events_when_sound_changed:``
+ ``events_when_sound_stopped:``

advance action
~~~~~~~~~~~~~~

No settings are available for the ``action: advance``.

stop action
~~~~~~~~~~~

No settings are available for the ``action: advance``.

set_repeat action
~~~~~~~~~~~~~~~~~

+ ``repeat:``

Express configuration
---------------------

The playlist player does not support express configuration.

Sound behavior upon mode (or show) stop
---------------------------------------

When the mode or show stops that contains a ``playlist_player``, all playlists started in that mode or
show will stop and fade out using the ``crossfade_time`` setting.

