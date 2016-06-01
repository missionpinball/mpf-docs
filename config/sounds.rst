sounds:
=======

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. overview

The ``sounds:`` section of your config is where you configure non-default parameter values for any
sound assets you want to use in your game. Note: You do *not* have to have an entry for every
single sound you want to use, rather, you only need to add individual assets to your config file
that have settings which different from other assets in that asset's folder.

Here's an example:

::


    sounds:
        extra_ball:
            file: extra_ball_12753.wav
            events_when_stopped: extra_ball_callout_finished
            track: voice
            volume: -4.5 db
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


Optional settings
-----------------

The following sections are optional in the ``sounds:`` section of your config. (If you don't include them, the default will be used).

events_when_played:
~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more names of events that MPF will post when this sound is played. Enter the list
in the MPF config list format. These events are posted exactly as they’re entered.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more names of events that MPF will post when this sound stops playing. Enter the list
in the MPF config list format. These events are posted exactly as they’re entered.  These events can
be useful to trigger some action when a callout has finished playing.

file:
~~~~~
Single value, type: ``string``. Default: ``None``

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

loops:
~~~~~~
Single value, type: ``integer``. Default: ``0``

An integer value that controls the looping behvaior of this sound.  A value of 0 indicates the
sound will not loop when reaching the end (also known as a "one-shot").  A value of -1
indicates the sound should loop infinitely until it is stopped.  A value greater than 0
specifies the number of times the sound should loop back to the beginning while playing. Note
that this value is not the total number of times the sound is played, but the number of times it
should play again after the first time through.

max_queue_time:
~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

Specifies the maximum time this sound can be queued before it's played. If the time between when
this sound is requested and when MPF can actually play it is longer than this queue time, then
the request is discarded and the sound doesn't play. This only comes into play if this sound is
requested but the track it's playing on is at its ``max_simultaneous`` limit. Then if this sound
doesn't have a high enough priority to kill any of the existing sounds, it will be queued to play
later. Some sounds (like voice callouts) might be ok to queue, but other sounds (like sound effects
for when you hit a pop bumper or slingshot) might only make sense if they're played right away, so
in those cases you might want to use a short (or no) queue time. The default setting is "None" which
means this sound will have no queue limit and will always play eventually.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

The numeric value indicating the priority or importance of this sound.  Sounds with higher priority
values will preempt other sounds with lower priorities that are playing when a track has reached
the maximum number of simultaneous sounds it is configured to play.  If the track is busy and the
priorities of all sounds currently playing greater than or equal to this sound, the sound will be
queued for playback and will have to wait to be played.

track:
~~~~~~
Single value, type: ``string``. Default: ``None``

This is the name of the track this sound will play on. (You configure tracks and track names in the
:doc:`sound_system: </config/sound_system>` section of your machine config files.)

volume:
~~~~~~~
Single value, type: ``gain setting`` (:doc:`Instructions for entering gain values) </config/instructions/gain_values>` . (-inf, db, or float between 0.0 and 1.0. Default: ``0.5``

The volume of this sound.  This value is factored into the track and overall MPF volumes. It's used
to "balance" your sounds if you have one particular sound that's too loud or too quiet. As with all
volume parameters in MPF, this item can be represented as a number between 0.0 and 1.0 (1.0 is max
volume, 0.0 is off, 0.9 is 90%, etc.) It also can be represented as a decibel string from -inf to
0.0 db (ex: ``-3.0 db``).

ducking:
--------

The ``ducking:`` section controls :doc:`ducking </sounds/ducking>` for the sound.  It contains the
following nested sub-settings

Required settings
~~~~~~~~~~~~~~~~~

The following sections are required in the ``ducking:`` section of your config:

target:
^^^^^^^
Single value, type: ``string``. 

The track name to apply the ducking to when the sound is played.  Currently, only one target track
is supported, but there are plans to support multiple target tracks in a future version. This most
commonly contains the name of the track that music is played on.

Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``ducking:`` section of your config. (If you don't include them, the default will be used).

attack:
^^^^^^^
Single value, type: ``string``. Default: ``10ms``

The duration of the period over which the ducking starts until it reaches its maximum attenuation
(attack stage).  This value may be specified as a :doc:`time string </config/instructions/time_strings>`
or a number of samples.

attenuation:
^^^^^^^^^^^^
Single value, type: ``gain setting`` (:doc:`Instructions for entering gain values) </config/instructions/gain_values>`. -inf, db, or float between 0.0 and 1.0. Default: ``1.0``

The attenuation (gain) to apply to the target track while ducking.  ``attenuation:`` controls how
quiet to make the target track while the sound is playing.

delay:
^^^^^^
Single value, type: ``string``. Default: ``0``

The duration to delay after the sound starts playing before ducking starts. This value may be
specified as a :doc:`time string </config/instructions/time_strings>` or a number of samples.

release:
^^^^^^^^
Single value, type: ``string``. Default: ``10ms``

The duration of the period over which the ducking goes from its maximum attenuation until the
ducking ends (release stage). This value may be specified as a
:doc:`time string </config/instructions/time_strings>` or a number of samples.

release_point:
^^^^^^^^^^^^^^
Single value, type: ``string``. Default: ``0``

The point relative to the end of the sound at which to start the returning the attenuation back to
normal (release stage). A value of 0.5 seconds means to begin to release the ducking 0.5 seconds
prior to the end of the sound. This value may be specified as a
:doc:`time string </config/instructions/time_strings>` or a number of samples.


