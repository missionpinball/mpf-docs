Tracks
======

The audio system in MPF is very similar to a sound mixing board that you control via configuration
settings and events. It is divided into tracks (similar to channels on a mixer), each of which has
its own properties such as name and volume. With the release of MPF 0.50, there are now multiple
types of audio tracks supported by the audio system, each with specialized features.

Track types
~~~~~~~~~~~

The following types of audio tracks are available in MPF:

+ ``standard`` - Standard audio tracks are the most commonly used and have a variety of playback
  features to support most pinball audio needs. Standard tracks have a setting to limit
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

+ ``playlist`` - New in MPF 0.50, playlist tracks provide a comprehensive set of music playing
  capabilities that include named playlists (lists of sound assets), playback mode (sequential or
  random/shuffled), crossfades between songs/playlists, and more.  Playlist tracks use
  :doc:`playlists </config/playlists>` which contain a list of :doc:`sounds </config/sounds>`
  (audio assets) video or audio files that can be played back sequentially or in random order and
  can be set to repeat or stop after all sounds have been played.

.. note::

   All tracks can be a :doc:`ducking </sound/ducking>` target regardless of the type of track.

Example track configuration:

.. code-block:: yaml

   sound_system:
     buffer: 2048
     frequency: 44100
     channels: 2
     master_volume: 0.9
     tracks:
       music:
         volume: 0.5
         simultaneous_sounds: 1
         events_when_stopped: music_track_stopped
         events_when_played: music_track_played
         events_when_paused: music_track_paused
       sfx:
         volume: 0.4
         simultaneous_sounds: 8
         preload: yes
       voice:
         volume: 0.6
         simultaneous_sounds: 1
         preload: yes
       loops:
         type: sound_loop
         volume: 0.6
       playlist:
         type: playlist
         volume: 0.6
         crossfade_time: 2s
