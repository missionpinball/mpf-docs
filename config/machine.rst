machine:
========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``machine:`` section of your config is where you configure defails about the number of balls in your machine.

.. code-block:: mpf-config

   machine:
     balls_installed: 6
     min_balls: 3

.. config


Optional settings
-----------------

The following sections are optional in the ``machine:`` section of your config. (If you don't include them, the default will be used).

balls_installed:
~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

The (maximum) number of balls which should be installed in your machine.

min_balls:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

The minimum number of balls required to start a game.
If less than ``min_balls`` are present MPF will refuse to stat a game.

It's super annoying if you walk up to a pinball machine on location
and can't start a game because it's missing a ball. So this setting
lets you specify the minimum number of balls that need to be installed
in order for a game to start. Note that it's up to you to make sure
your game code can handle fewer balls than you might be expecting.


Related How To guides
---------------------

* :doc:`/mechs/troughs/two_coil_one_switch`
