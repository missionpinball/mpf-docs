extra_ball_groups:
==================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``extra_ball_groups:`` section of your config is where you...

.. todo:: :doc:`/about/help_us_to_write_it`

.. config


Optional settings
-----------------

The following sections are optional in the ``extra_ball_groups:`` section of your config. (If you don't include them, the default will be used).

award_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Immediately awards an extra ball.

This event first checks to make sure the limits of the max extra
balls have not been exceeded and that this group is enabled.

Note that this method will work even if this group does not have any
extra balls or extra balls lit.
You can use this to directly award an extra ball.

award_lit_events:
~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events to award a lit extra ball.
If the player does not have any lit extra balls, this method does nothing.

enabled:
~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Whether this ball group is enabled.

light_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Light the extra ball for possible collection by the player.
This method checks that the group is enabled and that the max lit
value has not been exceeded.
If so, this method will post the extra ball disabled events.

lit_memory:
~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

.. todo:: :doc:`/about/help_us_to_write_it`

max_lit:
~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

Max concurrent lit extra balls.

max_per_ball:
~~~~~~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

Maximum number of extra balls per ball.

max_per_game:
~~~~~~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

Maximum number of extra balls per game.

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

Not used.


Related How To guides
---------------------

* :doc:`/game_logic/extra_balls/index`
