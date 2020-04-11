mpf:
====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``mpf:`` section of your config is where you configure global MPF settings.

.. config


Optional settings
-----------------

The following sections are optional in the ``mpf:`` section of your config. (If you don't include them, the default will be used).

allow_invalid_config_sections:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

MPF will not raise a fatal error when on invalid section when you set this to true. This might be useful when you are developing a new feature and do not want to constantly update config_spec (the file which describes allowed sections).

auto_create_switch_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

MPF will post switch_event_active and switch_event_inactive (see below) when this is enabled.

config_players:
~~~~~~~~~~~~~~~
Unknown type. See description below.

A list of config players which will be loaded.

core_modules:
~~~~~~~~~~~~~
Unknown type. See description below.

A list of core modules which will be loaded.

default_ball_search:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Default value for whether ball search is enabled or disabled on all playfields
(unless you overwrite it on that playfield).

default_light_hw_update_hz:
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``50``

Default light update hz.
Can be overwritten per platform.

default_platform_hz:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``100``

For all non-tickless platforms we poll this often.
This usually means how often we will read switches.
Reducing this setting might reduce the amounts of CPU significantly.
We recommand to keep this at least at 50Hz or you will loose switch hits.
For smooth game play aim at 100Hz.
Everything above that will mostly only reduce switch latency.

default_pulse_ms:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``10``

Default default_pulse_ms for all coils when not overwritten. This will be used when you do not specify any pulse_ms in your coil.

default_show_sync_ms:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

Default sync_mc for all shows when not specified otherwise.

device_modules:
~~~~~~~~~~~~~~~
Unknown type. See description below.

A list of device modules which will be loaded.

paths:
~~~~~~
Unknown type. See description below.

Paths for all additional files loaded in MPF.

platforms:
~~~~~~~~~~
Unknown type. See description below.

A list of platforms which will be loaded.

plugins:
~~~~~~~~
Unknown type. See description below.

A list of plugins which will be loaded.

save_machine_vars_to_disk:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

If set to true MPF will persist machine_vars to disk in a background writer.

switch_event_active:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``%_active``

If auto_create_switch_events is set to true this event will be posted after a switch turned active.

switch_event_inactive:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``%_inactive``

If auto_create_switch_events is set to true this event will be posted after a switch turned inactive.

switch_tag_event:
~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``sw_%``

This event will be posted for all tags after a switch turned active.


Related How To guides
---------------------

* :doc:`/hardware/fast/leds`
