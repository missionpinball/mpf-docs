
The *ball_locks*: section of your config files let you setup logical
ball locks which can be used to physically or virtually lock balls.
This sectioncan be used in your machine-wide config files. This
sectioncanbe used in mode-specific config files. Here’s an example:


::

    
    ball_locks:
        bunker:
            balls_to_lock: 3
            lock_devices: bd_bunker




<name>:
~~~~~~~

The logical name of this ball lock device.



balls_to_lock: (required)
~~~~~~~~~~~~~~~~~~~~~~~~~

The number of balls this ball lock should hold. If one of the
associated lock devices receives a ball and this logical ball lock is
full, then the ball device will just release the ball again.



lock_devices:
~~~~~~~~~~~~~

A list of one (or more) ball devices that will collect balls which
will count towards this lock.



source_playfield:
~~~~~~~~~~~~~~~~~

The name of the playfield that feeds balls to this lock. If you only
have one playfield (which is most games), you can leave this setting
out. Default is the playfield called *playfield*.



request_new_balls_to_pf:
~~~~~~~~~~~~~~~~~~~~~~~~

Boolean which controls whether this logical ball lock will
automatically add another ball into play after it locks a ball.
Default is *True*.



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
event documentation`_. Ball locks make use of the following device
control events:



enable_events:
~~~~~~~~~~~~~~

Enables this device. Default is *ball_started*.



disable_events:
~~~~~~~~~~~~~~~

Disables this device. Default is *ball_ending*.



reset_events:
~~~~~~~~~~~~~

Resets this device by resetting the locked ball count to 0 and
releasing all balls. Default is *machine_reset_phase_3, ball_starting,
ball_ending*.



release_one_events:
~~~~~~~~~~~~~~~~~~~

Releases a single ball. Default is *None*.



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

.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


