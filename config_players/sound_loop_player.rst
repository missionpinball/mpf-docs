Sound Loop player
=================

The *sound loop player* is a :doc:`config player </config_players/index>` that's used to control
sound loop sets (used by sound loop audio tracks). (This player is part of the MPF media controller
and only available if you're using MPF-MC for your media controller.)

Usage in config files
---------------------

In config files, the sound player is used via the ``sound_loop_player:`` section.  Event names
that will trigger sound actions are nested sub-headings and sound_loop_set names are either listed
as nested sub-headings below that.

Usage in shows
--------------

In shows, the sound player is used via the ``sounds_loop_sets:`` section of a step.

Optional settings
-----------------

Additional information may be found in the :doc:`sound_loop_player </config/sound_loop_player>`
configuration reference documentation.

