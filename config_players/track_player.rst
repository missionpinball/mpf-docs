Track player
============

.. versionadded:: 0.32

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
sub-headings below that.

Usage in shows
--------------

In shows, the track player is used via the ``tracks:`` section of a step.

Required settings
-----------------

Additional information may be found in the :doc:`track_player </config/track_player>`
configuration reference documentation.

