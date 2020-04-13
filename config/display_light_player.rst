display_light_player:
=====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``display_lights:`` section of a step.

.. overview

The ``display_light_player:`` section of your config is where you use your lights as a display.
See :doc:`/config_players/display_light_player` for details.

.. config


Optional settings
-----------------

The following sections are optional in the ``display_light_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: play, stop. Default: ``play``

Play or stop the display.

bcp_connection:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``local_display``

Which BCP client provides the content for your display.
You can usually leave this at the default.

lights:
~~~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Which LEDs should receive the updates.
You usually use a tag here or '*' for all of them.

max_x:
~~~~~~
Single value, type: ``integer``. Defaults to empty.

Unused.

max_y:
~~~~~~
Single value, type: ``integer``. Defaults to empty.

Unused.

min_x:
~~~~~~
Single value, type: ``integer``. Default: ``0``

Unused.

min_y:
~~~~~~
Single value, type: ``integer``. Default: ``0``

Unused.


Related How To guides
---------------------

* :doc:`/config_players/display_light_player`
