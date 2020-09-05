playlists:
==========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``playlists:`` section of your config is where you configure non-default parameter values for any
playlist assets you want to use in your game. (This section is part of the MPF media controller and
only available if you're using MPF-MC for your media controller.)

Here is an example:

.. code-block:: mpf-config

   # ---------------------
   # SOUNDS::PLAYLIST
   # ---------------------
   playlists:
     playlistIntro:
       shuffle: false
       repeat: false
       sounds:
         - voiceAnnouncerNewsFlash1
         - voiceAnnouncerMessage1
         - voiceAnnouncerAliensAttack1
     playlistHighScore:
       shuffle: true
       repeat: true
       crossfade_mode: override
       crossfade_time: 5s
       sounds:
         - soundHighScore001
         - soundHighScore002
         - soundHighScore003
         - soundHighScore004
   # ---------------------
   # PLAYLIST::PLAYER
   # ---------------------
   playlist_player:
     # -------------------
     # ADDED SURPRISE VOICE DURING ATTRACT MODE
     playlistAttention:
       trackplaylist:
         playlist: playlistIntro
         action: play
     # -------------------
     # MUSIC DURING HIGH SCORE ENTRY
     high_score_enter_initials:
       trackplaylist:
         playlist: playlistHighScore
         shuffle: true
         repeat: true
         action: play
     mode_attract_started:
       trackplaylist:
         action: stop

.. config


Required settings
-----------------

The following sections are required in the ``playlists:`` section of your config:

sounds:
~~~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

.. note:: If you want to use a sound that has spaces in its name, the name of the sound must be
   in quotes:
   ::

    playlists:
       mode_music:
          sounds:
             - song_01
             - song_02
             - "song 03" # example of a sound with a space in its name using quotes
             - song_04


Optional settings
-----------------

The following sections are optional in the ``playlists:`` section of your config. (If you don't include them, the default will be used).

crossfade_mode:
~~~~~~~~~~~~~~~
Single value, type: one of the following options: use_track_setting, override. Default: ``use_track_setting``

The ``crossfade_mode:`` of a playlist determines whether the playlist uses the track ``crossfade_time``
setting or the ``crossfade_time`` specified in the playlist.  Options for ``crossfade_mode:`` are:

+ ``use_track_settings`` - Use the ``crossfade_time`` specified in the playlist track.
+ ``override`` - Use the ``crossfade_time`` specified in the playlist.

crossfade_time:
~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

The number of seconds over which to crossfade between sounds in the playlist. This value is ignored when
``crossfade_mode:`` is set to ``use_track_setting``.

events_when_looping:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when this playlist loops back to the
beginning while playing. The playlist will only loop if ``repeat:`` is set to ``True``. Enter the
list in the MPF config list format. These events are posted exactly as they’re entered.

events_when_played:
~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when this playlist is played. Enter the list
in the MPF config list format. These events are posted exactly as they’re entered.

events_when_sound_changed:
~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when a new sound is played while the playlist
is played. Enter the list in the MPF config list format. These events are posted exactly as they’re
entered.

events_when_sound_stopped:
~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when a playlist sound has finished playing.
Enter the list in the MPF config list format. These events are posted exactly as they’re entered.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when this playlist has finished playing.
Enter the list in the MPF config list format. These events are posted exactly as they’re entered.

repeat:
~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Flag indicating whether or not the playlist will repeat when all sounds have been played or just
stop.

scope:
~~~~~~
Single value, type: one of the following options: machine, player. Default: ``machine``

Whatever this playlist should be persisted per player or machine-wide.

shuffle:
~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Flag indicating whether or not the playlist will be played in order (``shuffle: True`` or randomized
(``shuffle: False``) for playback.


Related How To guides
---------------------

* :doc:`/config_players/playlist_player`
