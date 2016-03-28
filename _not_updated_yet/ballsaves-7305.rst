
The *ball_saves:* section of the config file lets you create `ball
save devices`_. This sectioncan be used in your machine-wide config
files. This sectioncanbe used in mode-specific config files. Here's an
example:


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
included in the `ball save device documentation`_.)



active_time:
~~~~~~~~~~~~

How long the ball save is active (in `MPF time string format`_) once
it starts counting down. This includes the *hurry_up_time,* but does
not include the *grace_period* time. Leave this setting out (or set it
to 0) for unlimited time. Default is *0*.



hurry_up_time:
~~~~~~~~~~~~~~

The time before the ball save ends (in `MPF time string format`_) that
will cause the *ball_save_<name>_hurry_up* event to be posted. Use
this to change the script for the light or trigger other effect.
Default is *0*.



grace_period:
~~~~~~~~~~~~~

The “secret” time (in `MPF time string format`_) the ball save is
still active. This is added onto the *active_time*. Default is *0*.



timer_start_events:
~~~~~~~~~~~~~~~~~~~

An optional event (or list of events) in `MPF control event format`_
which starts this ball saver's countdown timer. Default is *None*.



auto_launch:
~~~~~~~~~~~~

True/False which controls whether the ball save should auto launch the
saved ball or wait for the player to launch it. Default is *True*.



balls_to_save:
~~~~~~~~~~~~~~

How many balls this ball saver should save before disabling itself.
Set it to -1 for unlimited. Default is *1*.



Device Control Events
---------------------

Device control events are events you can use to control devices. They
are configured in your machine-wide or mode config with settings that
end in *_events*. For example, if a device has a setting for
*enable_events:* and you add an event to that setting, then when that
event is posted, the device will enable. You can add single events or
lists of events to these settings, and you can also configure time-
delays for how much time passes between the event being posted and the
action to take place. Details are available in the `device control
event documentation`_. Ball saves make use of the following device
control events:



enable_events:
~~~~~~~~~~~~~~

Enables the ball save. If you do not have a *timer_start_events* entry
then enabling by an event here will also start the timer. Default is
*None*.



disable_events:
~~~~~~~~~~~~~~~

Disables the ball save. Default is *ball_ending*.



Settings that apply to all device types
---------------------------------------

There are some settings that apply to all types of devices that also
apply here.



tags:
~~~~~

A list of one or more tags that apply to this device. Tags allow you
to access groups of devices by tag name.



label:
~~~~~~

The plain-English name for this device that will show up in operator
menus and trouble reports.



debug:
~~~~~~

Set this to *true* to add lots of logging information about this shot
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot. Default is *False*.

.. _ball save device documentation: https://missionpinball.com/docs/mpf-core-architecture/devices/abstract-devices/ball-save/
.. _MPF time string format: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/entering-time-duration-values/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


