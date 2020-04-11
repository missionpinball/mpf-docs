pin2dmd:
========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``pin2dmd:`` section of your config is where you configure your :doc:`PIN2DMD RGB DMD display </hardware/pin2dmd/index>`.

.. config


Optional settings
-----------------

The following sections are optional in the ``pin2dmd:`` section of your config. (If you don't include them, the default will be used).

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see additional debug output. This might impact the performance of MPF.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

panel:
~~~~~~
Single value, type: one of the following options: rgb, rbg. Default: ``rgb``

The order of the LEDs in your panels.
If your blue and green appear to be swapped change this.

resolution:
~~~~~~~~~~~
Single value, type: one of the following options: 128x32, 192x64. Default: ``128x32``

The resolution of your panel.
PIN2DMD XL is ``192x64`` and the standard PIN2DMD is ``128x32``.


Related How To guides
---------------------

* :doc:`/hardware/pin2dmd/index`
