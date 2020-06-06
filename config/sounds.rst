sounds:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``sounds:`` section of your config is where you configure non-default parameter values for any
sound assets you want to use in your game. Note: You do *not* have to have an entry for every
single sound you want to use, rather, you only need to add individual assets to your config file
that have settings which different from other assets in that asset's folder. (This section is part
of the MPF media controller and only available if you're using MPF-MC for your media controller.)

MPF-MC currently supports 16-bit Wave (.wav), Ogg Vorbis (.ogg), and FLAC (.flac) files.

Here's an example:

.. code-block:: mpf-mc-config

    ##! asset: sounds/extra_ball_12753.wav=../sound/sounds/sound.ogg
    ##! asset: sounds/slingshot_01.ogg=../sound/sounds/sound.ogg
    #! sound_system:
    #!   buffer: 1024
    #!   channels: 1
    #!   enabled: true
    #!   frequency: 44100
    #!   master_volume: 0.75
    #!   tracks:
    #!     music:
    #!       type: standard
    #!       simultaneous_sounds: 1
    #!       volume: 0.5
    #!     voice:
    #!       type: standard
    #!       simultaneous_sounds: 1
    #!       volume: 0.7
    #!     sfx:
    #!       type: standard
    #!       simultaneous_sounds: 8
    #!       volume: 0.4
    sounds:
      extra_ball:
        file: extra_ball_12753.wav
        events_when_stopped: extra_ball_callout_finished
        streaming: false
        track: voice
        volume: 0.5
        priority: 50
        max_queue_time: None
        ducking:
          target: music
          delay: 0
          attack: 0.3 sec
          attenuation: -18db
          release_point: 2.0 sec
          release: 1.0 sec
      slingshot_01:
        volume: 0.5
        max_queue_time: 0

.. config


Optional settings
-----------------

The following sections are optional in the ``sounds:`` section of your config. (If you don't include them, the default will be used).

about_to_finish_time:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

The point relative to the end of the sound at which to post the ``events_when_about_to_finish`` event(s).
A value of 0.5 seconds means to post the event(s) prior to the end of the sound. When set to ``None``, no events will be
posted. If the value of this setting is greater than the duration of the sound, the event(s) will be posted as soon as
the sound begins playback. This value is specified as a :doc:`time string </config/instructions/time_strings>`.

ducking:
~~~~~~~~
Single value, type: :doc:`sound_ducking <sound_ducking>`. Defaults to empty.

The ``ducking:`` section controls :doc:`ducking </sound/ducking>` for the sound.

end_loop_at:
~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``None``

The position in the sound file (in seconds) at which to start looping and return to the start of the
loop as determined by the ``start_loop_at:`` setting. By default (None) the sound will loop when it
reaches the end of the sound. This setting only applies to sounds loaded in memory and played on a
standard audio track (not to any streaming sound or sound played on any other track type).

events_when_about_to_finish:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when this sound is about to finish playing.
The exact timing of this event is determined by the ``about_to_finish_time`` setting for this sound.
Enter the list in the MPF config list format. These events are posted exactly as they’re entered.

events_when_looping:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when this sound loops back to the
beginning while playing. Enter the list in the MPF config list format. These events are posted
exactly as they’re entered.

events_when_played:
~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when this sound is played. Enter the list
in the MPF config list format. These events are posted exactly as they’re entered.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when this sound stops playing. Enter the list
in the MPF config list format. These events are posted exactly as they’re entered.  These events can
be useful to trigger some action when a callout has finished playing.

fade_in:
~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

The number of seconds over which to fade in the sound when it is played.

fade_out:
~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

The number of seconds over which to fade out the sound when it is stopped. This value is not
applied when the sound stops on its own by reaching the end of the sound (will likely be added
in a future version).  At the moment it only comes into play when the sound is actively stopped
by an event.

file:
~~~~~
Single value, type: ``string``. Defaults to empty.

Sometimes you might want to name a file one thing on disk but refer to it as another thing in your
game and config files. In this case, you can create an ``file:`` setting in an asset entry. (Note
the file: `extra_ball_12753.wav` setting in the example above, and note that it includes the file
extension.) In this example, you would refer to that image asset as `extra_ball` even though the
file is `extra_ball_12753`. You might be wondering why this exists? Why not just change the file name
to be whatever you want and/or who cares what the name is? The reason this function exists is
because it allows for the separation of the actual file on disk from the way it's called in the
game. For example, you could use this to create two sets of assets—one for a traditional DMD
and one for a color DMD—and then you could refer to the asset by its generic name throughout your
configs. (In other words, you could swap out assets for different physical machine types without
having to update your display code.) That said, we expect that 99% of people won't use this
``file:`` setting, which is fine.

key:
~~~~
Single value, type: ``string``. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

loops:
~~~~~~
Single value, type: ``integer``. Default: ``0``

An integer value that controls the looping behavior of this sound.  A value of 0 indicates the
sound will not loop when reaching the end (also known as a "one-shot").  A value of -1
indicates the sound should loop infinitely until it is stopped.  A value greater than 0
specifies the number of times the sound should loop back to the beginning while playing. Note
that this value is not the total number of times the sound is played, but the number of times it
should play again after the first time through.

markers:
~~~~~~~~
List of one (or more) values, each is a type: :doc:`sound_marker <sound_marker>`. Defaults to empty.

The ``markers:`` section establishes a list of markers and their associated events at specific
times in the sound.  When a marker is reached during playback, the associated events will be
posted.  Markers are useful for synchronizing various actions with specific points in a sound.
A typical use might be to send an 'almost_finished_playing' event a short time before a sound
finishes playback or establish various checkpoints in a sound that could be used to restart
a sound at that point on the user's next turn (using mode code).

Here's a simple example utilizing markers:

.. code-block:: mpf-config

    sounds:
      long_sound_1:
        volume: 0.8
        markers:
          - time: 2.534 sec
            events: send_this_event, also_this_event
          - time: 6.712 sec
            events: almost_finished_playing

max_queue_time:
~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

Specifies the maximum time this sound can be queued before it's played. If the time between when
this sound is requested and when MPF can actually play it is longer than this queue time, then
the request is discarded and the sound doesn't play. This only comes into play if this sound is
requested but the track it's playing on is at its ``simultaneous_sounds`` limit. Then if this sound
doesn't have a high enough priority to kill any of the existing sounds, it will be queued to play
later. Some sounds (like voice callouts) might be ok to queue, but other sounds (like sound effects
for when you hit a pop bumper or slingshot) might only make sense if they're played right away, so
in those cases you might want to use a short (or no) queue time. The default setting is "None" which
means this sound will have no queue limit and will always play eventually.

mode_end_action:
~~~~~~~~~~~~~~~~
Single value, type: one of the following options: stop, stop_looping. Default: ``stop_looping``

The ``mode_end_action:`` setting determines what action to take when the mode that initiates the
playback of the sound ends. Options for ``mode_end_action:`` are:

+ ``stop`` - All currently playing and queued instances of the specified sound started by the mode
  will be stopped/canceled. If the ``fade_out`` parameter has a non-zero value, the sound will fade
  out over the specified number of seconds.
+ ``stop_looping`` - Looping will be canceled for all currently playing instances of the specified
  sound started by the mode (the sound will continue to play to the end of the current loop). In
  addition, any queued instances of the sound awaiting playback will be removed/canceled.

pan:
~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0``

Pan the audio to the left or right channel.
Currently, broken due to a bug.
Let us know if you need this.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

The numeric value indicating the priority or importance of this sound.  Sounds with higher priority
values will preempt other sounds with lower priorities that are playing when a track has reached
the maximum number of simultaneous sounds it is configured to play.  If the track is busy and the
priorities of all sounds currently playing greater than or equal to this sound, the sound will be
queued for playback and will have to wait to be played.

simultaneous_limit:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

The numeric value indicating the maximum number of instances of this sound that may be played
at the same time (up to the limit of the track).  Once the maximum number of instances has
been reached, the ``stealing_method`` setting determines the how additional requests to play
the sound will be managed.  This setting is useful for sounds that can be triggered in rapid
succession (such as spinners and pop bumpers).  Setting a limit will ensure a reasonable number
of instances will be played simultaneously and not overwhelm the audio mix.  The default value of
``None`` indicates no limits will be placed on the number of instances of the sound that may be
played at once up to the limit of the track.  The value of this setting is ignored when the
``streaming`` setting has a value of ``False``.

start_at:
~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

The position in the sound file (in seconds) to start playback of the sound when it is played. When
the sound is looped it will loop back to the beginning of the sound file.

start_loop_at:
~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

The position in the sound file (in seconds) to start playback of the sound after it is looped. By default
when the sound is looped it will loop back to the beginning of the sound file. Setting this value to
something other than zero is particularly useful when you have a music sound that has an introduction
section and want it to loop back to a verse and not the intro. This setting works in correlation with
``end_loop_at:`` and only applies to sounds loaded in memory and played on a standard audio track (not
to any streaming sound or sound played on any other track type). Be sure to use many decimal places in
your times as precision is important when it comes to loop points. If you hear pops and clicks at the
loop points, you may need to slightly adjust your start and end loop times to alleviate them.

stealing_method:
~~~~~~~~~~~~~~~~
Single value, type: one of the following options: skip, oldest, newest. Default: ``oldest``

The ``stealing_method:`` of a sound determines the behavior of additional requests to play the
sound once the number of simultaneous instances of the sound has reached its ``simultaneous_limit``
limit. This setting is ignored when ``simultaneous_limit`` is set to ``None``. Options for
``stealing_method:`` are:

+ ``oldest`` - Steal/stop the oldest playing instance of the sound and replace it with a new
  instance (essentially restarts the oldest playing instance).
+ ``newest`` - Steal/stop the newest playing instance of the sound and replace it with a new
  instance (essentially restarts the newest playing instance).
+ ``skip`` - Do not steal/stop any currently running instances of the sound. Simply skip playback
  of the newly requested instance.

streaming:
~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Indicates whether or not the sound sound will be streamed (rather than stored in memory).
Streaming sounds are limited to a single instance of the sound playing at a time.  Multiple
different streaming sounds may be played simultaneously, just not more than a single
instance of a particular sound. When ``streaming`` is set to ``True``, the ``simultaneous_limit``
setting is ignored and a value of 1 is used.

track:
~~~~~~
Single value, type: ``string``. Defaults to empty.

This is the name of the track this sound will play on. (You configure tracks and track names in the
:doc:`sound_system: </config/sound_system>` section of your machine config files.)

volume:
~~~~~~~
Single value, type: ``gain setting`` (-inf, db, or float between 0.0 and 1.0). Default: ``0.5``

The volume of this sound.  This value is factored into the track and overall MPF volumes. It's used
to "balance" your sounds if you have one particular sound that's too loud or too quiet. As with all
volume parameters in MPF, this item can be represented as a number between 0.0 and 1.0 (1.0 is max
volume, 0.0 is off, 0.9 is 90%, etc.) It also can be represented as a decibel string from -inf to
0.0 db (ex: ``-3.0 db``).


Related How To guides
---------------------

* :doc:`/sound/index`
