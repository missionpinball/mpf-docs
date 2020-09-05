Track player
============


The *track player* is a :doc:`config player </config_players/index>` that's used to control
audio tracks when MPF events are received. Tracks can be stopped, paused, or played with an
optional fade time. The volume of a track can also be changed with an optional fade time.
Finally, all sounds currently playing on a track can be stopped (again with an optional fade
out time). (This player is part of the MPF media controller and only available if you're
using MPF-MC for your media controller.)

Usage in config files
---------------------

In config files, the track player is used via the ``track_player:`` section.  Event names that
will trigger track actions are nested sub-headings and track names are listed as nested
sub-headings below that.  ``__all__`` can be used in place of a track name to apply the action
to all audio tracks in the sound system.

Example:

.. code-block:: mpf-config

    track_player:
      pause_music_track:
        music:
          action: pause
          fade: 1 sec
      resume_music_track:
        music:
          action: play
      stop_sounds_on_all_tracks:
        __all__:
          action: stop_all_sounds
          fade: 0.5 sec

Usage in shows
--------------

In shows, the track player is used via the ``tracks:`` section of a step.

Example:

.. code-block:: mpf-config

    shows:
      my_show_with_sound:
        - time: 0
          tracks:
            music:
              action: set_volume
              volume: 0.3
              fade: 0.25 sec
        - time: 3.5
          tracks:
            music:
              action: set_volume
              volume: 0.5
              fade: 0.25 sec

Config Options
--------------

Additional information may be found in the :doc:`track_player </config/track_player>`
configuration reference documentation.

