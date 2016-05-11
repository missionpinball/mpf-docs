Trigger player
==============

The *trigger player* is a :doc:`config player </config_players/index>` that's used to send BCP triggers to remotely-
connected BCP devices. This isn't typically used much if you're using the MPF Media Controller (since MPF-MC can read
MPF config files), but it's used a lot if you're using a different media controller that doesn't know as much about
MPF (such as the Unity 3D backbox server).

Usage in config files
---------------------

In config files, the trigger player is used via the ``trigger_player:`` section.

Usage in shows
--------------

In shows, the trigger player is used via the ``triggers:`` section of a step.