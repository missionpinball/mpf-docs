ball_saves:
===========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``ball_saves:`` section of your config is where you create `ball save devices`.
Here's an example:

::

    ball_saves:
      default:
        active_time: 10s
        hurry_up_time: 2s
        grace_period: 2s
        enable_events: mode_base_started
        timer_start_events: balldevice_plunger_lane_ball_eject_success
        auto_launch: yes
        balls_to_save: 1
        debug: yes

<name>:
~~~~~~~

The name of this ball save device. (This is "default" in the config
snippet above.) The name is used in the events that are posted from
this ball save. (The complete list of events posted by ball saves is
included in the events reference.)

Optional settings
-----------------

The following sections are optional in the ``ball_saves:`` section of your config. (If you don't include them, the default will be used).

active_time:
~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

How long the ball save is active (in MPF time string format) once
it starts counting down. This includes the *hurry_up_time,* but does
not include the *grace_period* time. Leave this setting out (or set it
to 0) for unlimited time. Default is *0*.

auto_launch:
~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

True/False which controls whether the ball save should auto launch the
saved ball or wait for the player to launch it.

balls_to_save:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

How many balls this ball saver should save before disabling itself.
Set it to -1 for unlimited.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

disable_events:
~~~~~~~~~~~~~~~

.. versionchanged:: 0.32

List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``ball_will_end, service_mode_entered`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which disable this ball save, meaning a drained ball will no longer
be saved.

enable_events:
~~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which enable this ball save.

early_ball_save_events:
~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.33

List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Event(s) which will trigger a ball save to take place before the current ball has drained. A typical example of this might be switch
activation events from outlane switches which can be used to trigger a ball save as soon as the ball hits the outlane.

grace_period:
~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

The “secret” time (in MPF time string format) the ball save is
still active. This is added onto the *active_time*. Default is *0*.

hurry_up_time:
~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

The time before the ball save ends (in MPF time string format) that
will cause the *ball_save_<name>_hurry_up* event to be posted. Use
this to change the script for the light or trigger other effect.
Default is *0*.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

The plain-English name for this device that will show up in operator
menus and trouble reports.

source_playfield:
~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``ball_devices:`` device. Default: ``playfield``

.. todo::
   Add description.

List of one (or more) values, each is a type: ``string``. Default: ``None``

Special / reserved tags for ball saves: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.

timer_start_events:
~~~~~~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, start this ball saver's countdown timer.

eject_delay:
~~~~~~~~~~~~

.. versionadded:: 0.31

single|ms|0

TODO

only_last_ball:
~~~~~~~~~~~~~~~

.. versionadded:: 0.31

single|bool|False

TODO
