mypinballs:
===========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``mypinballs:`` section of your config is where your mypinballs segment display controller.
See :doc:`/hardware/mypinballs/index` for details.

.. config


Required settings
-----------------

The following sections are required in the ``mypinballs:`` section of your config:

port:
~~~~~
Single value, type: ``string``. Defaults to empty.

Serial port to use.


Optional settings
-----------------

The following sections are optional in the ``mypinballs:`` section of your config. (If you don't include them, the default will be used).

baud:
~~~~~
Single value, type: ``integer``. Default: ``115200``

Baud rate to use on the serial port.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set to true to see more debug output.


Related How To guides
---------------------

* :doc:`/hardware/mypinballs/index`
