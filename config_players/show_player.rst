Show player
===========

The *show player* is a :doc:`config player </config_players/index>` that's used to start, stop, pause, resume, advance,
and/or update shows.

Usage in config files
---------------------

In config files, the show player is used via the ``show_player:`` section.

Usage in shows
--------------

In shows, the show player is used via the ``shows:`` section of a step. (Yes, you can include shows in shows, meaning
you can essentially use a parent show like a playlist, or as a controller that starts and stops other shows.)