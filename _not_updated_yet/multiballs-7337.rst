
The *multiballs:* section of the config file is where you can
configure `multiball devices`_. Multiball devices are "abstract"
devices in that they're more of a concept rather than a physical
device on the playfield. The multiball "device" is used to start
multiball. This sectioncan be used in your machine-wide config files.
This sectioncanbe used in mode-specific config files.


::

    
    multiballs:
        main_multiball:
            ball_count: 3
            shoot_again: 5s
            ball_locks: bunker




<name>:
~~~~~~~



ball_count: (required)
~~~~~~~~~~~~~~~~~~~~~~

Integer value of the number of balls this multiball will be.



source_playfield:
~~~~~~~~~~~~~~~~~

The name of the playfield these balls will be added to. If you only
have one playfield (which is most games), you can leave this setting
out. Default is the playfield called *playfield*.



shoot_again:
~~~~~~~~~~~~

A time period where drained balls will automatically be re-launched.
(Kind of like a multiball-specific ball save). Default is *10
seconds*.



ball_locks:
~~~~~~~~~~~

A list of one or more `ball lock devices`_ that will be used as the
source for the balls for this multiball. When multiball begins, it
will first try to eject balls from these ball locks to get the
required number of balls in play. If these devices don't have enough
balls, then it will add balls from the default device that adds balls
into play. (Typically the trough / plunger lane.)



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
event documentation`_. Multiball devices make use of the following
device control events:



enable_events:
~~~~~~~~~~~~~~

Enables this multiball device. (It must be enabled before it can be
started.) Default is *ball_started*.



disable_events:
~~~~~~~~~~~~~~~

Disables this multiball device. Default is *ball_ending*.



reset_events:
~~~~~~~~~~~~~

Resets this multiball device. Disables it, cancels *shoot_gain*, and
resets the balls ejected count to 0. Default is
*machine_reset_phase_3, ball_starting*.



start_events:
~~~~~~~~~~~~~

Starts this multiball by adding the configured number of balls into
play. Default is *None*.



stop_events:
~~~~~~~~~~~~

Stops this multiball be stopping shoot again. Note that short of
disabling the flippers, you can't really stop a multiball. Default is
*None*.



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

.. _multiball devices: https://missionpinball.com/docs/mpf-core-architecture/devices/abstract-devices/multiball/
.. _ball lock devices: https://missionpinball.com/docs/mpf-core-architecture/devices/abstract-devices/ball-lock/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


