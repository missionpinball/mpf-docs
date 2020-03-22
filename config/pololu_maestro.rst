pololu_maestro:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``pololu_maestro:`` section of your config is where you configure the serial
port that a Pololu Maestro servo controller is connected to.

When you attach a Pololu Maestro, two serial ports will appear. You want to
specific the first (lower numbered) port here. For example:

.. code-block:: mpf-config

   pololu_maestro:
     port: COM5

Note that there are a few other settings you need to configure in other areas
to use a Pololu Maestro servo controller. See the
:doc:`How To guide </hardware/pololu_maestro/index>` for details.

.. config


Required settings
-----------------

The following sections are required in the ``pololu_maestro:`` section of your config:

port:
~~~~~
Single value, type: ``string``.

The name of the serial port.

Optional settings
-----------------

The following sections are optional in the ``pololu_maestro:`` section of your config. (If you don't include them, the default will be used).

NOTE: The Pololu Maestro control center software and typical servo specifications work in units of microseconds.  The values used here are in quarter-microseconds, so to make them correspond multiply your servo specs by 4.  eg a servo with range of 600-2400 microsecods would be servo_min: 2400 and servo_max: 9600 for the full range.

servo_max:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``9000``

Quarter-microseconds to use for the max servo value.
The default (9000) translates to 2250 microseconds or 2.25ms.

servo_min:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``3000``

Quarter-microseconds to use for the max servo value.
The default (3000) translates to 750 microseconds or 0.75ms.

