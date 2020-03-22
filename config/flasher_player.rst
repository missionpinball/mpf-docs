flasher_player:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``flashers:`` section of a step.

.. overview

The ``flasher_player:`` section of your config is where you can flash lights.
See :doc:`/config_players/flasher_player` for details.

.. config


Optional settings
-----------------

The following sections are optional in the ``flasher_player:`` section of your config. (If you don't include them, the default will be used).

ms:
~~~
Single value, type: ms_or_token. Default: ``100ms``

Configures how long should that flasher be enabled.


Related How To guides
---------------------

* :doc:`/mechs/lights/flashers`
