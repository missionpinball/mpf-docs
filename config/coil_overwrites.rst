coil_overwrites:
================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

Some devices offer one or multiple ``coil_overwrites:`` settings where you can
overwrite coil settings.

Most commonly this is used in :doc:`flippers` and :doc:`autofire_coils`.

.. config


Optional settings
-----------------

The following sections are optional in the ``coil_overwrites:`` section of your config. (If you don't include them, the default will be used).

hold_power:
~~~~~~~~~~~
Single value, type: float(0,1).

Overwrite the ``hold_power`` of the coil for this device.
See ``default_hold_power`` in :doc:`coils` for details.

pulse_ms:
~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`).

Overwrite the ``pulse_ms`` of the coil for this device.
See ``default_pulse_ms`` in :doc:`coils` for details.

pulse_power:
~~~~~~~~~~~~
Single value, type: float(0,1).

Overwrite the ``pulse_power`` of the coil for this device.
See ``default_pulse_power`` in :doc:`coils` for details.

recycle:
~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False).

Overwrite the ``recycle`` setting of the coil for this device.
See ``recycle`` in :doc:`coils` for details.


Related How To guides
---------------------

* :doc:`/config/flippers`
* :doc:`/config/kickbacks`
* :doc:`/config/autofire_coils`
