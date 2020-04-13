tilt:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``tilt:`` section of your config is where you configure a tilt mode.

.. config


Optional settings
-----------------

The following sections are optional in the ``tilt:`` section of your config. (If you don't include them, the default will be used).

multiple_hit_window:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms) or template`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>` and :doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Default: ``300ms``

Window in which hits are ignored after a tilt hit.

reset_warnings_events:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Default: ``ball_will_end``

Default: ``ball_will_end``

These events, when posted, will cause the ``warnings_to_tilt:`` to be reset
to zero.

settle_time:
~~~~~~~~~~~~
Single value, type: ``time string (ms) or template`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>` and :doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Default: ``5s``

Time to wait after the machine is tilted before a new ball can be started.
This prevents that a player can tilt his ball and the first ball of the next
player.

slam_tilt_switch_tag:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``slam_tilt``

Switch tags which will cause a slam tilt.

tilt_events:
~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, cause a :doc:`/events/tilt` to occur
which will end the current ball in progress with no end of ball bonus.
You usually want to use tilt_warning_events because this one will instantly
tilt the machine on the first event.

tilt_slam_tilt_events:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, cause a :doc:`/events/slam_tilt` event to
be posted. The slam tilt typically ends the current game and also clears all
credits from the machine.

tilt_switch_tag:
~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``tilt``

Switch tag for switches which cause the machine to tilt (without prior
warnigns). You want to use the tag configured in ``tilt_warning_switch_tag``
in most cases.

tilt_warning_events:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, cause a tilt warning to occur. They will post the
:doc:`/events/tilt_warning` event, and if the ``warnings_to_tilt:`` limit is hit, will
also cause the :doc:`/events/tilt` event.

tilt_warning_switch_tag:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``tilt_warning``

Switch tags for switches which cause a tilt warning.

tilt_warnings_player_var:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``tilt_warnings``

Player var to use to store tilt warnings.

warnings_to_tilt:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer`` or ``template`` (:doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Default: ``3``

Number of warnings until the machine tilts.

.. include:: template_setting.rst


Related How To guides
---------------------

* :doc:`/game_logic/tilt/index`
