digital_score_reels:
====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``digital_score_reels:`` section of your config is where you...

.. todo:: :doc:`/about/help_us_to_write_it`

.. config


Optional settings
-----------------

The following sections are optional in the ``digital_score_reels:`` section of your config. (If you don't include them, the default will be used).

frames:
~~~~~~~
List of one (or more) values, each is a type: :doc:`digital_score_reel_frame <digital_score_reel_frame>`. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

include_player_number:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``False``

.. todo:: :doc:`/about/help_us_to_write_it`

reel_count:
~~~~~~~~~~~
Single value, type: ``number`` (can be integer or floating point). Default: ``0``

.. todo:: :doc:`/about/help_us_to_write_it`

start_value:
~~~~~~~~~~~~
Single value, type: ``string``. Default: ``0``

.. todo:: :doc:`/about/help_us_to_write_it`

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see additional debug output. This might impact the performance of MPF.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`


Related How To guides
---------------------

.. todo:: :doc:`/about/help_us_to_write_it`
