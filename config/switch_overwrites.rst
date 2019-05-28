switch_overwrites:
==================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

Some devices offer a ``switch_overwrites:`` setting where you can overwrite
settings of a switch used in that devices.
This is commonly used in :doc:`flippers` and :doc:`autofire_coils`.

Optional settings
-----------------

The following sections are optional in the ``switch_overwrites:`` section of your config. (If you don't include them, the default will be used).

debounce:
~~~~~~~~~
Single value, type: one of the following options: quick, normal, None. Default: ``None``

Overwrite the ``debounce`` setting on a coil.
See ``debounce`` in :doc:`switches` for details.
