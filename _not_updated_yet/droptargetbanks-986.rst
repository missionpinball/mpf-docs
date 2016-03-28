
Once you've configured your individual drop targets, you group them
together into banks via the *drop_target_banks:* section of your
config file. This sectioncan be used in your machine-wide config
files. This sectioncan be used in mode-specific config files. Here's
an example from *Judge Dredd*:


::

    
    drop_target_banks:
        judge:
            drop_targets: j, u, d, g, e
            reset_coils: c_reset_drop_targets
            reset_events:
                drop_targets_judge_complete: 1s




What about drop target banks with lights?
-----------------------------------------

Notice there are no settings to control lights associated with drop
targets, but many machines (like *Judge Dredd* used in the example)
have lights for each drop target? To control those lights, you'd
create shots based on the lights and switches for each drop target,
and then you control them just like any other shot with the ` *shot*`_
settings, ` *shot_group*`_ settings, and *`shot profiles`_*. In this
case you'd end up specifying your switch for this drop target as well
as for a shot for it. It's ok to have the same switch in both places.



<name>:
~~~~~~~

Create a subsection under *drop_target_banks:* for each bank of drop
targets you have. The name of each section is the name you'll refer to
the drop target as in your game code. ("judge", in this example.)



drop_targets:
~~~~~~~~~~~~~

A list of the names of the individual drop targets (from the names you
chose in the *drop_targets:* section of your config file) that are
included in this bank. Note that single drop target devices can be
members of multiple banks at the same time. For example, you might
have two banks of three drop targets, from which you could actually
actually three drop target banks. One for the first three, one for the
second three, and one for all six. Then you could track separate up
and down events for a subset of three or for all six getting knocked
down.



reset_coil:
~~~~~~~~~~~

The name of the coil that is fired to reset this bank of drop targets.



reset_coils:
~~~~~~~~~~~~

If your drop target bank has two reset coils (as was common in older
machines which huge banks of drop targets), you can add a
*reset_coils* section (plural) and then specific a list of multiple
coils. In this case, MPF will pulse all the coils at the same time to
reset the bank of drop targets.



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
event documentation`_. Drop target banks make use of the following
device control events:



reset_events:
~~~~~~~~~~~~~

Resets this drop target bank by pulsing this bank's *reset_coil* or
*reset_coils*. Default is *machine_reset_phase_3, ball_starting*.



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

.. _shot profiles: https://missionpinball.com/docs/configuration-file-reference/shot_profiles/
.. _shot: https://missionpinball.com/docs/configuration-file-reference/shots/
.. _shot_group: https://missionpinball.com/docs/configuration-file-reference/shot_groups/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


