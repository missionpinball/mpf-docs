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

