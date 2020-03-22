config:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``config:`` section of your configuration files allows you to
specify *additional* configuration files that will be read in after
the current file is loaded. Here's an example:

.. code-block:: yaml

    config:
        - machine.yaml
        - devices.yaml
        - game.yaml
        - textstrings.yaml
        - keymap.yaml

Note that each file is on its own line, which starts with a minus,
then a space, then the file. (The space is important.) Also note that
you can (optionally) specify a path, like this:

.. code-block:: yaml

        - config\machine.yaml
        - config/my_game/machine.yaml

MPF will attempt to convert relative and absolute paths
based on your OS, and it can deal with slashes in either direction.

MPF will then open those files one-by-one and merge their
settings into the master configuration dictionary. The settings are
merged together in the order the files are listed, so if multiple
files specify the same configuration option then whichever one comes
later in the list will overwrite any options that have already been
specified.

You can also have ``config:`` sections in other config files, meaning
that one config file can call another which will call another, etc.

Whenever MPF encounters a new config file, it will add it to
the end of the list. And since files are processed in order, if there
are any conflicting settings then the last file on the list will
"win." Also note that the framework will attempt to load the file from
the current working directory (containing the config file that ``config:``
entry is from. If that fails then it will try the last
known good directory that worked for a config file.

.. config


Related How To guides
---------------------

* :doc:`/game_design/mode_layering`
