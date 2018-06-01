plugins:
========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``plugins:`` section of your config is where you list all plugin classes to load.
By default it contains:

* :doc:`info_lights`
* :doc:`switch_player`
* :doc:`auditor`
