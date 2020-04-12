sound_system_tracks:
====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``tracks:`` settings in your ``sound_system:`` section of your config is where you
configure which tracks exist in your machine.

.. config


Optional settings
-----------------

The following sections are optional in the ``sound_system_tracks:`` section of your config. (If you don't include them, the default will be used).

crossfade_time:
~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

Time to crossfade between to songs on your playlist.

The settings is specific to ``playlist`` audio tracks.
It will ignored in other track types.

ducking:
~~~~~~~~
Single value, type: :doc:`sound_ducking <sound_ducking>`.

Default ducking settings for this track.
Those can be overwritten per sound.
See :doc:`ducking </sound/ducking>` for details.

events_when_paused:
~~~~~~~~~~~~~~~~~~~
List of one (or more) events.

A list of one or more names of events that MPF will post when the track is paused. Enter the list
in the MPF config list format. These events are posted exactly as they’re entered.

events_when_played:
~~~~~~~~~~~~~~~~~~~
List of one (or more) events.

A list of one or more names of events that MPF will post when the track is played or resumed after
being stopped/paused. Enter the list in the MPF config list format. These events are posted
exactly as they’re entered.

events_when_resumed:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events.

A list of one or more names of events that MPF will post when the track is resumed.
Enter the list in the MPF config list format.
These events are posted exactly as they’re entered.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events.

A list of one or more names of events that MPF will post when the track is stopped.
Enter the list in the MPF config list format.
These events are posted exactly as they’re entered.

max_layers:
~~~~~~~~~~~
Single value, type: ``integer``. Default: ``8``

Maximum number of layers in your loop which can play in parallel.

The settings is specific to ``sound_loop`` audio tracks.
It will ignored in other track types.

simultaneous_sounds:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``8``

This sets the maximum number of simultaneous sounds that can be played on this track. The example
config file above shows the *music* and *voice* tracks with a max of 1 simultaneous sound playing,
since if you have two music clips or voice callouts playing at the same time, it will sound like
gibberish. A sound effects track, on the other hand, can probably have a few sounds playing at once.
Note that MPF gives you detailed control over what happens if a new sound wants to play when the max
simultaneous sounds are already playing on that track. Should the new sound break in and stop an
existing sound? Should it wait until the existing sound is done? How long should it wait? You can
control all this on a per sound basis (see the :doc:~sounds: </config/sounds>~ documentation for
more information).

The settings is specific to ``standard`` audio tracks.
It will ignored in other track types.

type:
~~~~~
Single value, type: one of the following options: standard, sound_loop, playlist. Default: ``standard``

The track ``type:`` setting determines what type of audio track will be used. For more detailed

volume:
~~~~~~~
Single value, type: ``gain setting`` (-inf, db, or float between 0.0 and 1.0). Default: ``0.5``

This is the volume setting for this track (how loud will it be), as either a value between 0.0 and
1.0 or a decibel value between -inf and 0.0 db. Note that each track's volume will be combined
with the overall system volume. So if your MPF master volume is set to 0.8 (80%) and you have a
track set to 0.5 (50%), sounds on that track will play at 40% overall volume (50% of 80%).


Related How To guides
---------------------

* :doc:`/sound/index`
