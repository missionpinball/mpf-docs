hardware_sound_systems:
=======================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``hardware_sound_systems:`` section of your config is where you configure external sound systems.
For instance, this is used in the :doc:`LISY platform </hardware/lisy/index>`.

.. config


Optional settings
-----------------

The following sections are optional in the ``hardware_sound_systems:`` section of your config. (If you don't include them, the default will be used).

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Overwrite the default platform.


