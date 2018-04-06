opp_coils:
==========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``opp_coils:`` section of your config is where you configure platform
specific settings for OPP coils.

Optional settings
-----------------

The following sections are optional in the ``opp_coils:`` section of your config. (If you don't include them, the default will be used).

recycle_factor:
~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

The recycle_factor is used in OPP to determine the cool down time of a coil
after a pulse in relation to pulse_ms. For instance, with recycle_factor of 2
and a pulse_ms of 20ms the coil will cool down for at least 40ms after each
pulse.

