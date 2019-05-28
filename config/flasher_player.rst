flasher_player:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``flashers:`` section of a step.

.. overview

The ``flasher_player:`` section of your config is where you can flash lights.
See :doc:`/config_players/flasher_player` for details.


Optional settings
-----------------

The following sections are optional in the ``flasher_player:`` section of your config. (If you don't include them, the default will be used).

ms:
~~~
Single value, type: ``integer``. Default: ``None``

Configures how long should that flasher be enabled.


.. note:: The ``flasher_player:`` section of your config may contain additional settings not mentioned here. Read the introductory text for details of what those might be.

