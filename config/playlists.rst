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

Here's an example:

::

    playlists:
        attract_music:
            sounds: drumbeat_7, rainbow_disco_bears, dirty_grinding_beat_loop, hippie_ahead
            shuffle: False
            repeat: False
            events_when_played: attract_music_played
            events_when_stopped: attract_music_stopped
            events_when_looping: attract_music_looping
            events_when_sound_changed: attract_music_sound_changed
            events_when_sound_stopped: attract_music_sound_stopped
        mode_1_music:
            sounds:
                - song_1
                - song_2
                - song_3

Required settings
-----------------

The following sections are required for each named sound loop set in your config:

sounds:
~~~~~~~

The ``sounds:`` section contains an indented list of existing sound assets (one per line) that will
be contained in the playlist. It is suggested you use block sequence notation for this list (begin
each line with a dash followed by a space). Alternatively, you can enter the sound asset names
in a comma-separated list. The sounds will be played in the order specfied (unless ``shuffle:`` is
set to ``True``).

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

The following sections are optional in the ``playlists:`` section of your config. (If you don't include
them, the default will be used).

crossfade_mode:
~~~~~~~~~~~~~~~
Single value, type: one of the following options: use_track_setting, override. Default: ``use_track_setting``

The ``crossfade_mode:`` of a playlist determines whether the playlist uses the track ``crossfade_time``
setting or the ``crossfade_time`` specified in the playlist.  Options for ``crossfade_mode:`` are:

+ ``use_track_settings`` - Use the ``crossfade_time`` specified in the playlist track.
+ ``override`` - Use the ``crossfade_time`` specified in the playlist.

crossfade_time:
~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`).
Default: ``0``

The number of seconds over which to crossfade between sounds in the playlist. This value is ignored when
``crossfade_mode:`` is set to ``use_track_setting``.

events_when_looping:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more names of events that MPF will post when this playlist loops back to the
beginning while playing. The playlist will only loop if ``repeat:`` is set to ``True``. Enter the
list in the MPF config list format. These events are posted exactly as they’re entered.

events_when_played:
~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more names of events that MPF will post when this playlist is played. Enter the list
in the MPF config list format. These events are posted exactly as they’re entered.

events_when_sound_changed:
~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more names of events that MPF will post when a new sound is played while the playlist
is played. Enter the list in the MPF config list format. These events are posted exactly as they’re
entered.

events_when_sound_stopped:
~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more names of events that MPF will post when a playlist sound has finished playing.
Enter the list in the MPF config list format. These events are posted exactly as they’re entered.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more names of events that MPF will post when this playlist has finished playing.
Enter the list in the MPF config list format. These events are posted exactly as they’re entered.

repeat:
~~~~~~~
Single value, type: ``bool``. Default: ``False``

Flag indicating whether or not the playlist will repeat when all sounds have been played or just
stop.

shuffle:
~~~~~~~~
Single value, type: ``bool``. Default: ``False``

Flag indicating whether or not the playlist will be played in order (``shuffle: True`` or randomized
(``shuffle: False``) for playback.
