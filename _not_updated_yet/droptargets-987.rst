
You configure individual `drop targets`_ in your machine in the
*drop_targets:*section of your machine config file. (This section is
only used for individual targets. Once you configure them here, then
you group them into banks in the ` *drop_target_banks:*section`_.)
This sectioncan be used in machine-wide config files. This
sectioncannot be used in your mode-specific config files. Here's an
example from *Judge Dredd*, with five drop targets we've given names
*J*, *U*, *D*, *G*, and *E*.


::

    
    drop_targets:
        j:
            switch: drop_target_j
            reset_coil: reset_drop_targets
        u:
            switch: drop_target_u
            reset_coil: reset_drop_targets
        d:
            switch: drop_target_d
            reset_coil: reset_drop_targets
            knockdown_coil: trip_drop_target_d
        g:
            switch: drop_target_g
            reset_coil: reset_drop_targets
        e:
            switch: drop_target_e
            reset_coil: reset_drop_targets


Important: Not all "drop targets" in your machine will be configured
as "drop targets." Some machines have drop target mechanisms that
actually act as diverters. For example, in *Attack From Mars*, the
drop target under the saucer is actually a diverter. When it's up, the
ball stays on the playfield. When it's down, the ball enters the lock.
*Star Trek: The Next Generation* has this with the drop target up
above the lanes, and *The Wizard of Oz* has this for the drop target
in front of the Winkie Guard. If a drop target in your machine is
guarding a path to somewhere the ball can go, it might be a
`diverter`_. Of course sometime a drop target can be both, like the
"D" target in *Judge Dredd*. Feel free to `post to the forum`_ with
questions.



What about drop targets with lights?
------------------------------------

Notice there are no settings to control lights associated with drop
targets, but many machines (like *Judge Dredd* used in the example)
have lights for each drop target. To control those lights, you'd
create shots based on the lights and switches for each drop target,
and then you control them just like any other shot with the ` *shot*`_
settings, ` *shot_group*`_ settings, and *`shot profiles`_*. In this
case you'd end up specifying your switch for this drop target as well
as for a shot for it. It's okay to have the same switch in both
places.



<name>:
~~~~~~~

Create one entry in your *drop_targets:* section for each drop target
in your machine. Don’t worry about grouping drop targets into banks
here. (That’s done in the *drop_target_banks:* section.) The drop
target name can be whatever you want, and it will be the name for this
drop target which is used throughout your machine.



switch:
~~~~~~~

The name of the switch that's activated when this drop target is down.
(Note that active switch = target down, so if your drop target uses
opto switches which are reversed, then you need to configure this
switch with *type: NC*in the *switches:*section of your config file.)
MPF will automatically update the state of the drop target whenever
the switch changes state.



reset_coil:
~~~~~~~~~~~

The name of the coil that is pulsed to reset this drop target. The
pulse time will be whatever you configure as the default pulse time
for this coil in the *coils:* section of your machine configuration
file. Important: Only enter a *reset_coil* name here if this coil is
only resets this drop target. For banks of drop targets where a single
coil resets the entire bank of targets, enter the *reset_coil* in the
*drop_target_banks:* configuration, not here. Why? Because if you have
three drop targets in a bank, you only want to pulse the coil once to
reset all the drop targets. If you enter the coil three times (one for
each drop target), then it will pulse three times when the bank is
reset.



knockdown_coil:
~~~~~~~~~~~~~~~

This is an optional coil that's used to knock down a drop target. Most
drop targets do not have these. (In the *Judge Dredd* example above,
you'll notice that only the *D* target has a knockdown coil.



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
event documentation`_. Drop targets make use of the following device
control events:



reset_events:
~~~~~~~~~~~~~

Resets this drop target. If this drop target is not part of a drop
target bank, then resetting this target will pulse its reset coil. If
this drop target is part of a drop target bank, then resetting this
drop target will have no effect. (Instead you would reset the bank.)
Default is *ball_starting, machine_reset_phase_3*.



knockdown_events:
~~~~~~~~~~~~~~~~~

Pulses this drop target's knockdown coil. (If this drop target doesn't
have a knockdown coil, then these events will have no effect.)



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

.. _post to the forum: https://missionpinball.com/forum/f/mpf-users/
.. _shot profiles: https://missionpinball.com/docs/configuration-file-reference/shot_profiles/
.. _shot: https://missionpinball.com/docs/configuration-file-reference/shots/
.. _shot_group: https://missionpinball.com/docs/configuration-file-reference/shot_groups/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/
.. _drop targets: https://missionpinball.com/docs/mpf-core-architecture/devices/logical-devices/drop-target/
.. _section: https://missionpinball.com/docs/configuration-file-reference/droptargetbanks/
.. _diverter: https://missionpinball.com/docs/configuration-file-reference/diverters/


