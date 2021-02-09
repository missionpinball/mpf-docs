pkone:
======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``pkone:`` section of your machine-wide config is where you
configure hardware options that are specific to the Penny K Pinball PKONE
Controller. Note that we have a how to guide which includes
:doc:`all the PKONE-specific settings </hardware/pkone/index>` throughout your entire config file,
so be sure to read that if you have Penny K Pinball PKONE hardware.

.. code-block:: mpf-config

    pkone:
      port: com3

.. config


Required settings
-----------------

The following sections are required in the ``pkone:`` section of your config:

port:
~~~~~
Single value, type: ``string``. Defaults to empty.

The serial port name your PKONE controller uses.


Optional settings
-----------------

The following sections are optional in the ``pkone:`` section of your config. (If you don't include them, the default will be used).

baud:
~~~~~
Single value, type: ``integer``. Default: ``115200``

Baud rate to use on the serial port.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this platform.

Related How To guides
---------------------

* :doc:`/hardware/pkone/index`
