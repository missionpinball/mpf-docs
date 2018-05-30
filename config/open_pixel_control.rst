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


Optional settings
-----------------

The following sections are optional in the ``open_pixel_control:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set this to true to see more debug log lines.

host:
~~~~~
Single value, type: ``string``. Default: ``localhost``

Hostname of the openpixel server to connect.

port:
~~~~~
Single value, type: ``int``. Default: ``7890``

Port of the openpixel server to connect.
