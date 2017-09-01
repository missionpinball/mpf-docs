Tracks
======

The audio system in MPF is very similar to a sound mixing board that you control via configuration
settings and events. It is divided into tracks (similar to channels on a mixer), each of which has
its own properties such as name and volume. With the release of MPF 0.50, there are now multiple
types of audio tracks supported by the audio system, each with specialized features.

Track types
~~~~~~~~~~~

The following types of audio tracks are available in MPF:

+ ``standard`` - Standard audio tracks are the most commonly used and are virtually the same as the
audio tracks in the previous releases of MPF (since 0.30). Standard tracks have a setting to limit
the number of sounds that may be played simultaneously. If a standard track is busy playing its
limit of simultaneous sounds, pending sounds can be added to a queue where they wait to be played
until the track can play them. Several settings control a sound's behavior when a track is busy.
:doc:`Sounds </config/sounds>` are audio assets and can be played by standard tracks.
+ ``sound_loop`` - New in MPF 0.50, sound_loop tracks are optimized for live looping music control
driven by events.  This specialized track type can synchronize playback of multiple looping sounds
simultaneously in layers and supports gapless switching to a new set of loops. Sound loops are
designed to build music that dynamically changes based on events in your game.  Sound used in
sound_loop tracks must be loaded in memory (streaming sounds are not supported). Sound loop tracks
use :doc:`sound_loop_sets </config/sound_loop_sets>` which are special groups of
:doc:`sounds </config/sounds>` to control the playback and looping of audio files.

.. note::

   All tracks can be a :doc:`ducking </sound/ducking>` target regardless of the type of track.

