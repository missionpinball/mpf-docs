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
Single value, type: ``integer``. Defaults to empty.

Baudrate when connecting to LISY using a serial port.

connection:
~~~~~~~~~~~
Single value, type: one of the following options: network, serial. Default: ``network``

Whatever to use a network or serial connection.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

disable_dtr:
~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

If set to ``True`` MPF will try to prevent your operating system from toggling
the DTR line of your serial.
This is needed for :doc:`APC </hardware/apc/index>` and some other controllers
which would reset when this happens.
If in doubt check the documentation of your controller.

display_flash_frequency:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

How fast should the displays flash? Defaults to once per second or 1Hz.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this platform.

max_led_batch_size:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``3``

How many LEDs can be batched on your controller?
This might differ on different controllers.
If in doubt check the documentation of your controller.

network_host:
~~~~~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

Host to connect when connecting to LISY via network.

network_port:
~~~~~~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

Port to connect when connecting to LISY via network.

poll_hz:
~~~~~~~~
Single value, type: ``integer``. Default: ``100``

How fast should MPF poll LISY for switch changes? Defaults to 1000Hz

port:
~~~~~
Single value, type: ``string``. Defaults to empty.

Serial port when connecting to LISY using serial.

send_length_after_command:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Some controllers require an additional length byte after the command.


Related How To guides
---------------------

* :doc:`/hardware/lisy/index`
* :doc:`/hardware/apc/index`
