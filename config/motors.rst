motors:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``motors:`` section of your config is where you configure motors with position switches.

MPF supports two types of motor devices:

1. Motor can only move into one direction. The device mechanically changes the direction or moves in cycles.
2. Motor can move in two directions.

Motors devices are controlled using :doc:`digital_outputs </config/digital_outputs>` which can map to either
light or driver outputs.


Device which can only move in one direction
-------------------------------------------

This is an example for a motorized drop target bank which is mounted to a camshaft.
When the motor is running it constantly moves up and down.
Two position switches are used to detect the current position.

.. code-block:: mpf-config

   switches:
     s_motorized_drop_target_bank_position_up:
       number:
     s_motorized_drop_target_bank_position_down:
       number:
   digital_outputs:
     c_motorized_drop_target_bank_run:
       number:
       type: driver
   motors:
     motorized_drop_target_bank:
       motor_left_output: c_motorized_drop_target_bank_run
       position_switches: !!omap
         - up: s_motorized_drop_target_bank_position_up
         - down: s_motorized_drop_target_bank_position_down
       reset_position: down
       go_to_position:
         move_bank_up: up
         move_bank_down: down

Device which can move in two directions
---------------------------------------

The slimer in Stern Ghostbusters is an example for a motor which can move in two directions.
Both digital outputs are connected to light outputs.
Again two position switches are used to detect the current position.
In this setup the first and last switches are also considered as limit switches and the motor will stop
once it hit one of them.

.. code-block:: mpf-config

   switches:
     s_slimer_home:
       number: 8-1
     s_slimer_away:
       number: 8-2
   digital_outputs:
     c_slimer_motor_forward:
       number: 8-3
       type: light
     c_slimer_motor_backward:
       number: 8-4
       type: light
   motors:
     ghostbusters_slimer:
       motor_left_output: c_slimer_motor_forward
       motor_right_output: c_slimer_motor_backward
       position_switches: !!omap
         - home: s_slimer_home
         - away: s_slimer_away
       reset_position: home
       go_to_position:
         slimer_home: home
         slimer_away: away

Another example of such a device would be the claw in Stern Batman DK (or also Stern Batman 66).
It has more position switches but the mechanics are similar:

.. code-block:: mpf-config

   switches:
     s_claw_home:
       number:
     s_claw_position1:
       number:
     s_claw_position2:
       number:
     s_claw_position3:
       number:
     s_claw_position4:
       number:
     s_claw_position5:
       number:
   digital_outputs:
     c_claw_forward:
       number:
       type: driver
     c_claw_backward:
       number:
       type: driver
   motors:
     batman_claw:
       motor_left_output: c_claw_forward
       motor_right_output: c_claw_backward
       position_switches: !!omap
         - home: s_claw_home
         - pos1: s_claw_position1
         - pos2: s_claw_position2
         - pos3: s_claw_position3
         - pos4: s_claw_position4
         - pos5: s_claw_position5
       reset_position: home
       go_to_position:
         stop_claw: home
         go_pos1: pos1
         go_pos2: pos2
         go_pos3: pos3
         go_pos4: pos4
         go_pos5: pos5

.. config


Required settings
-----------------

The following sections are required in the ``motors:`` section of your config:

position_switches:
~~~~~~~~~~~~~~~~~~
Ordered list for one (or more) sub-settings. Each in the format of ``string`` : string name of a :doc:`switches <switches>` device

Ordered map of name of the position and the switch which becomes active once this position is reached.

For example:

.. code-block:: yaml

  position_switches:  !!omap
      - home: s_claw_home
      - pos1: s_claw_position1
      - pos2: s_claw_position2

``home``, ``pos1`` and ``pos2`` are the names of your positions (you can choose them freely).
``s_claw_home``, ``s_claw_position1`` and ``s_claw_position2`` are the switches to detect the position.

The order is important when the motor can move in two directions.
For instance if the device is at ``home`` and should move to ``pos1`` it will more right.
However, if it is at ``pos2`` it will move left.
If it is not at any position and also does not know its previous position it will move left until it reaches
a known position and may then change its direction again (usually this should not happen since it will move to a known
position during reset).

reset_position:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

The position the device should move to on reset (as defined in ``position_switches``).


Optional settings
-----------------

The following sections are optional in the ``motors:`` section of your config. (If you don't include them, the default will be used).

go_to_position:
~~~~~~~~~~~~~~~
One or more sub-entries. Each in the format of ``string`` : ``string``

A mapping of events to positions.
Once an event in the mapping is posted the motor will move to the corresponding position.

For instance:

.. code-block:: yaml

  go_to_position:
      stop_claw: home
      go_pos1: pos1
      go_pos2: pos2

If you post ``stop_claw`` the motor will move to the position called ``home`` (as defined in ``position_switches``).

include_in_ball_search:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Whether the motor should be included in ball search.

motor_left_output:
~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`digital_outputs <digital_outputs>` device. Defaults to empty.

:doc:`Digital output </config/digital_outputs>` to enable to move the motor left.
You need to configure at least ``motor_left_output`` or ``motor_right_output`` if you motor can only move in one
direction or both if it can move in both directions.

motor_right_output:
~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`digital_outputs <digital_outputs>` device. Defaults to empty.

:doc:`Digital output </config/digital_outputs>` to enable to move the motor right.
You need to configure at least ``motor_left_output`` or ``motor_right_output`` if you motor can only move in one
direction or both if it can move in both directions.

reset_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Default: ``machine_reset_phase_3, ball_starting``

Events on which the motor should move to its ``reset_position``.
You usually do not have to configure this.

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

* :doc:`/mechs/motors/index`
