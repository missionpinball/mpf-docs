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

.. code-block:: mpf-config

    sound_system:
      buffer: 1024
      channels: 1
      enabled: true
      frequency: 44100
      master_volume: 0.75
      tracks:
        music:
          type: standard
          simultaneous_sounds: 1
          volume: 0.5
        voice:
          type: standard
          simultaneous_sounds: 1
          volume: 0.7
        sfx:
          type: standard
          simultaneous_sounds: 8
          volume: 0.4

.. config


Required settings
-----------------

The following sections are required in the ``sound_system:`` section of your config:

tracks:
~~~~~~~
One or more sub-entries. Each in the format of ``string`` : :doc:`sound_system_tracks <sound_system_tracks>`

Every sound that's played in MPF is played on a track. If you are familiar with an audio mixer a
track can be thought of as a mixer channel.  Each track can have it's own settings, and you can
set volume on a per-track basis. You can have up to 8 audio tracks in your MPF machine. The example
above shows three tracks, called *music*, *voice*, and *sfx*. The idea (in case it isn't obvious)
is that you play all your music clips on the music track, voice callouts on the voice track, and
the sound effects on the sfx track. To create a track, add a sub entry to the `tracks:` section
which will be the name of that track. (So again, `music:`, `voice:` and `sfx:` in the example.)


Optional settings
-----------------

The following sections are optional in the ``sound_system:`` section of your config. (If you don't include them, the default will be used).

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
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

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
Single value, type: ``gain setting`` (-inf, db, or float between 0.0 and 1.0). Default: ``0.5``

The overall volume of the MPF sound system. As with all volume parameters in MPF, this item can be represented
as a number between 0.0 and 1.0 (1.0 is max volume, 0.0 is off, 0.9 is 90%, etc.) It also can be represented as
a decibel string from -inf to 0.0 db (ex: ``-3.0 db``). Note that this only controls the volume of the MPF app,
not the host OS'es system volume. So you still need to make sure that the host OS is not on mute and that the
volume is turned up.


Related How To guides
---------------------

* :doc:`/sound/index`
