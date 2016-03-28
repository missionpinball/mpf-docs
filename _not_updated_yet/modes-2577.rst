
The `modes:` section of your machine configuration files is where you
specify which modes will be used in your game. (Read more about how
game modes work `here`_.) This sectioncan be used in your machine-wide
config files. This section *cannot* be used in mode-specific config
files. This section is just a list of modes (based on the folder names
in your machine's modes folder. This `modes:` list has nothing to do
with whether modes start or stop, or what priority they run at. (Those
settings are specified in the ` `mode:` section`_ of each mode's own
config file.) Instead this is just a list of all the modes that are
available in a game. If you have a mode that you're working on and is
not yet ready, don't include it here and it won't be processed or
loaded.


::

    
    modes:
      - skillshot
      - base
      - both_ramps_made
      - gun_fight
      - multiball
      - skillshot
      - watch_tower


Enter your list of modes (again, based on the folder names) like any
`config entry list`_.

.. _ section: https://missionpinball.com/docs/configuration-file-reference/mode/
.. _here: https://missionpinball.com/docs/game-modes/
.. _config entry list: https://missionpinball.com/docs/configuration-file-reference/adding-lists-and-lists-of-lists-to-config-files/


