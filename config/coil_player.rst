coil_player:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``coils:`` section of a step.

.. overview

The ``coil_player:`` section of your config is where you configure coil/solenoid/driver actions (pulse, enable,
disable, etc.) based on events. It's also used in shows (via the ``coils:`` section) to perform
coil actions in that show step.

Example from a config file:

::

   coil_player:
      some_event: coil_1
      some_other_event:
         coil_2:
            action: enable
            power: .5

In the example above, when the event called ``some_event`` is posted, coil_1 will pulse.
When the event ``some_other_event`` is posted, coil_2 will enable (be held on) at power
level 4.

Note that the ``some_event: coil_1`` is entered in a different way than the ``some_other_event:``.
The first one has a simple key/value pair, whereas the second has a complete nested sub-configuration.

The first example shows the "express" config, while the second shows the
full config. (What's an "express config?" Details :doc:`here </config/instructions/express_config.rst>`.

The coil player's express config is the "pulse" action.

Example coil player from a show:

::

   - time: 0
     coils:
       coil1: pulse


Optional settings
-----------------

The following sections are optional in the ``coil_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: ``string`` (case-insensitive). Options include ``pulse``, ``enable``, ``on``, ``disable``, or ``off``. Default: ``pulse``

What action the coil should perform. Note that "on" and "enable" are the same, and that "disable" and "off" are the same.

power:
~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

A multiplier value that will be applied to this coil's pulse time (which you can use to
make this coil pulse for longer or shorter durations). Note that this power setting
only applies to pulse actions.

milliseconds:
~~~~~~~~~~~~~
The number of milliseconds you'd like this coil to pulse for. This setting
override's the coil's default pulse_ms setting. Note that this setting
only affects pulse actions.
