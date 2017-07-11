tilt:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``tilt:`` section of your config is where you...

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``tilt:`` section of your config. (If you don't include them, the default will be used).

multiple_hit_window:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``300ms``

.. todo::
   Add description.

reset_warnings_events:
~~~~~~~~~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``ball_will_end``

These events, when posted, will cause the ``warnings_to_tilt:`` to be reset
to zero.

settle_time:
~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``5s``

.. todo::
   Add description.

slam_tilt_switch_tag:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``slam_tilt``

.. todo::
   Add description.

tilt_events:
~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause a :doc:`/events/tilt` to occur
which will end the current ball in progress with no end of ball bonus.

tilt_slam_tilt_events:
~~~~~~~~~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause a :doc:`/events/slam_tilt` event to
be posted. The slam tilt typically ends the current game and also clears all
credits from the machine.

tilt_switch_tag:
~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``tilt``

.. todo::
   Add description.

tilt_warning_events:
~~~~~~~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause a tilt warning to occur. They will post the
:doc:`/events/tilt_warning` event, and if the ``warnings_to_tilt:`` limit is hit, will
also cause the :doc:`/events/tilt` event.

tilt_warning_switch_tag:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``tilt_warning``

.. todo::
   Add description.

tilt_warnings_player_var:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``tilt_warnings``

.. todo::
   Add description.

warnings_to_tilt:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``3``

.. todo::
   Add description.

