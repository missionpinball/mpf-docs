fast_coils:
===========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``fast_coils:`` section of your config is where you configure platform
specific settings for coils in the FAST platform.

.. config


Optional settings
-----------------

The following sections are optional in the ``fast_coils:`` section of your config. (If you don't include them, the default will be used).

connection:
~~~~~~~~~~~
Single value, type: one of the following options: network, local, auto. Default: ``auto``

How is your coil connected? For WPC this might be ``local`` otherwise ``network``.

recycle_ms:
~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`).

The cooldown time of a coil after each pulse. Any pulse during that time will
be ignored to prevent overheating the coil.


Related How To guides
---------------------

* :doc:`/hardware/fast/index`
