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

::

   pololu_maestro:
      port: COM5

Note that there are a few other settings you need to configure in other areas
to use a Pololu Maestro servo controller. See the How To guide for details.


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

servo_max:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``9000``

.. todo::
   Add description.

servo_min:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``3000``

.. todo::
   Add description.


