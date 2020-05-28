open_pixel_control:
===================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``open_pixel_control:`` section of your config is where you configure a openpixel light controller.
This is usually used together with a :doc:`fadecandy </hardware/fadecandy/index>`
but can also be used standalone.
Usually, you don't have to change anything.

.. config


Optional settings
-----------------

The following sections are optional in the ``open_pixel_control:`` section of your config. (If you don't include them, the default will be used).

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see more debug log lines.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this platform.

host:
~~~~~
Single value, type: ``string``. Default: ``localhost``

Hostname of the openpixel server to connect.

port:
~~~~~
Single value, type: ``integer``. Default: ``7890``

Port of the openpixel server to connect.


Related How To guides
---------------------

* :doc:`/hardware/fadecandy/index`
