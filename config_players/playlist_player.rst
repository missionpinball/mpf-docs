Playlist player
===============

The *playlist player* is a :doc:`config player </config_players/index>` that's used to control
playlists. (This player is part of the MPF media controller and only available if you're using MPF-MC
for your media controller.)

Usage in config files
---------------------

In config files, the playlist player is used via the ``playlist_player:`` section.  Event names that
will trigger playlist actions are nested sub-headings and playlist names are either listed as nested
sub-headings below that.

Usage in shows
--------------

In shows, the sound player is used via the ``playlists:`` section of a step.

Optional settings
-----------------

Additional information may be found in the :doc:`sound_player </config/playlist_player>`
configuration reference documentation.
