lisy:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``lisy:`` section of your config is where your lisy platform.
See :doc:`/hardware/lisy/index` for details.

.. config


Optional settings
-----------------

The following sections are optional in the ``lisy:`` section of your config. (If you don't include them, the default will be used).

baud:
~~~~~
Single value, type: ``integer``.

Baudrate when connecting to LISY using a serial port.

connection:
~~~~~~~~~~~
Single value, type: one of the following options: network, serial. Default: ``network``

Whatever to use a network or serial connection.

display_flash_frequency:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

How fast should the displays flash? Defaults to once per second or 1Hz.

network_host:
~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Host to connect when connecting to LISY via network.

network_port:
~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

Port to connect when connecting to LISY via network.

poll_hz:
~~~~~~~~
Single value, type: ``integer``. Default: ``1000``

How fast should MPF poll LISY for switch changes? Defaults to 1000Hz

port:
~~~~~
Single value, type: ``string``. Default: ``None``

Serial port when connecting to LISY using serial.


