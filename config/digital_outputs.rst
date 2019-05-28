digital_outputs:
================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``digital_outputs:`` section of your config is where you configure digital outputs.
Those can be either mapped to a light or a driver and support only enabling and diabling.
In contrast to a light, ``digital_outputs`` do not support any fading or pwm/brightness.
Opposed to drivers, ``digital_outputs`` do not support pulsing, pattern or hardware rules.
Use them to control digital logic.
MPF uses them to control :doc:`motors </config/motors>` with additional control logic.

Some platforms such as Stern Spike, Gottlieb System 1 or Gottlieb System 80 use lights
outputs to control logic. In other platforms you usually use drivers.


Required settings
-----------------

The following sections are required in the ``digital_outputs:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``.

The number of your light or driver. The exact meaning of this number depends on your platform but is exactly
the same as if this was a light or driver (depending on the ``type`` setting).

type:
~~~~~
Single value, type: one of the following options: light, driver.

Whether this output is mapped as light or driver.


Optional settings
-----------------

The following sections are optional in the ``digital_outputs:`` section of your config. (If you don't include them, the default will be used).

disable_events:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

Those events will disable this output when posted.

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

Those events will enable this output when posted.

light_subtype:
~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

If this is mapped as light (``type: light``) you can set the ``subtype`` here
(see :doc:`lights </config/lights>` for details about ``subtype``).
The exact meaning depends on your platform.

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

In case you want to overwrite the default platform (as defined in ``hardware:``),
you can choose a platform for this output.


