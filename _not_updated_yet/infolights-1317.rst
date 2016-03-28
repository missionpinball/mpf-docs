
The Info Lights plug-in is used to communicate game status information
via lights, including the number of players, the current ball, match
numbers, tilt status, and whether a game is in progress. This is
typically used in EM games since they have lights for all these things
in the backbox. It's technically possible to do this all manually via
logic blocks and light scripts, but this plug-in is dead simple. You
just map your lights to game roles and then forget about them. Done.
If you want to use this plugin, add it to your list of plug-ins in
your configuration file, like this:


::

    
    Plugins:
        info_lights.InfoLights


Details on how to configurethis plug-in are available in the
``InfoLights:` section`_ of the config file reference.

.. _`InfoLights:` section: https://missionpinball.com/docs/configuration-file-reference/infolights/


