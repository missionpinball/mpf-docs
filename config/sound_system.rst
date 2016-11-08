sound_system:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``sound_system:`` section of your machine config controls the general settings for the
machine's sound system. (This section is part of the MPF media controller and only available
if you're using MPF-MC for your media controller.)

Here's an example of a typical sound configuration.

::

    sound_system:
        buffer: 1024
        channels: 1
        enabled: True
        frequency: 44100
        master_volume: 0.75
        tracks:
           music:
              simultaneous_sounds: 1
              volume: 0.5
           voice:
              simultaneous_sounds: 1
              volume: 0.7
           sfx:
              simultaneous_sounds: 8
              volume: 0.4

Optional settings
-----------------

The following sections are optional in the ``sound_system:`` section of your config. (If you don't
include them, the default will be used).  If you omit the ``sound_system:`` section completely,
the sound configuration will contain nothing but the default values, which includes a single audio
track named ``default``.  It is recommended that you at least specify the ``tracks:`` section in
your machine.

buffer:
~~~~~~~
Single value, type: ``integer``. Default: ``2048``

This is the size of your sound buffer. It must be a power of 2. The exact value you should use may take
some trial-and-error. A bigger buffer means that there's less chance of skipping and dropout (lower CPU
usage), but it also means that sounds can take longer to play since the buffer has to fill first. Some
limited power platform have to run with a buffer of 4096 or 8192 or 16384, others at 512 or 256. So just
play with it and see what works for you.

channels:
~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

The number of channels the sound system will support. 1 for mono, 2 for stereo. You're probably thinking,
"aww man, I need stereo sound!"  But almost no pinball machines do this since the speakers in the backbox
are 2 feet apart and they're 4 feet away from the player's ears. (Maybe if you're going to use headphones
or put tweeters in the front of the machine?) Again, if you have a resource-constrained system, then go
for mono and make sure all your sound files are mono. If not, meh, go ahead and use stereo.

enabled:
~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

Indicates whether or not the sound system will be enabled in your machine.

frequency:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``44100``

How many sound samples per second you want. 44100 is so-called "CD quality" audio, though with the sound
systems in most pinball machines, if you cut it in half (to 22050) it still sounds virtually the same.
If you're running on a resource-constrained host computer, you should make sure all your sound files are
encoded at the same rate so MPF doesn't waste time re-encoding them on the fly. Smaller values mean
smaller sound files, less memory consumption, and less CPU processing.  So if you're on a resource
constrained host computer, think about 22050 instead of 44100. (But be sure to resample all your sound
files to match.)

master_volume:
~~~~~~~~~~~~~~
Single value, type: ``gain setting`` (:doc:`Instructions for entering gain values </config/instructions/gain_values>`)
-inf, db, or float between 0.0 and 1.0. Default: ``0.5``

The overall volume of the MPF sound system. As with all volume parameters in MPF, this item can be represented
as a number between 0.0 and 1.0 (1.0 is max volume, 0.0 is off, 0.9 is 90%, etc.) It also can be represented as
a decibel string from -inf to 0.0 db (ex: ``-3.0 db``). Note that this only controls the volume of the MPF app,
not the host OS'es system volume. So you still need to make sure that the host OS is not on mute and that the
volume is turned up.

tracks:
-------

Every sound that's played in MPF is played on a track. If you are familiar with an audio mixer a
track can be thought of as a mixer channel.  Each track can have it's own settings, and you can
set volume on a per-track basis. You can have up to 8 audio tracks in your MPF machine. The example
above shows three tracks, called *music*, *voice*, and *sfx*. The idea (in case it isn't obvious)
is that you play all your music clips on the music track, voice callouts on the voice track, and
the sound effects on the sfx track. To create a track, add a sub entry to the `tracks:` section
which will be the name of that track. (So again, `music:`, `voice:` and `sfx:` in the example.
Then create one or more of the following settings for each track:

Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``tracks:`` section of your config. (If you don't include them,
the default will be used).

simultaneous_sounds:
````````````````````
Single value, type: ``integer`` (between ``1`` and ``32``). Default: ``8``

This sets the maximum number of simultaneous sounds that can be played on this track. The example
config file above shows the *music* and *voice* tracks with a max of 1 simultaneous sound playing,
since if you have two music clips or voice callouts playing at the same time, it will sound like
gibberish. A sound effects track, on the other hand, can probably have a few sounds playing at once.
Note that MPF gives you detailed control over what happens if a new sound wants to play when the max
simultaneous sounds are already playing on that track. Should the new sound break in and stop an
existing sound? Should it wait until the existing sound is done? How long should it wait? You can
control all this on a per sound basis (see the :doc:`sounds: </config/sounds>` documentation for
more information).

volume:
```````
Single value, type: ``gain setting`` (:doc:`Instructions for entering gain values </config/instructions/gain_values>`)
-inf, db, or float between 0.0 and 1.0. Default: ``0.5``

This is the volume setting for this track (how loud will it be), as either a value between 0.0 and
1.0 or a decibel value between -inf and 0.0 db. Note that each track's volume will be combined
with the overall system volume. So if your MPF master volume is set to 0.8 (80%) and you have a
track set to 0.5 (50%), sounds on that track will play at 40% overall volume (50% of 80%).
