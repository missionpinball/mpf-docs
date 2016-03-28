
Once you define all your `shots`_, you can group them together via the
*shot_groups:* section of your config file. This sectioncan be used in
your machine-wide config files. This sectioncan beused in mode-
specific config files. For example:


::

    
    shot_groups:
        upper_lanes:
            shots: lane_l, lane_a, lane_n, lane_e
            rotate_left_events: sw_left_flipper
            rotate_right_events: sw_right_flipper
            reset_events: upper_lanes_default_lit_complete
            enable_events: ball_started
            disable_events: ball_ending


Creating a shot group has several advantages, including:


+ You can add "rotation" events which shift the states of all the
  shots in the group to the left or right, like with flipper-controlled
  lane change or situations where the slingshots shift which lanes are
  lit.
+ Any time the state of a member shot in a group changes, MPF will
  check to see what all the other shots' states are. If they are all the
  same, it will post a "complete" event (in the form of *
  <shot_group_name>_<active_profile_name>_<profile_state_name>_complete
  *) which you can use to trigger scores based on complete, light shows,
  shot group resets, etc.
+ Any time a member shot is hit, MPF will post an event (in the form
  of * <shot_group_name>_<profile_name_of_shot_that_was_hit>_<profile_st
  ate_name_of_shot_that_was_hit>_hit *). You can use this to tie
  scoring, sounds, or logic blocks to any shot being hit in a group,
  which can be easier than creating entries for each individual shot.
+ Any time a member shot is hit, MPF will post an event (in the form
  of * <shot_group_name>_<profile_name_of_shot_that_was_hit>_hit *)
+ Any time a member shot is hit, MPF will post an event (in the form
  of * <shot_group_name>_hit *)


At first all these events might seem confusing, but really they all
exist to give you the most flexibility when looking to trigger
different things based on shots that are part of a shot group being
hit. For example, if a shot called *left_lane* is a member of a shot
group called *lanes* with a profile called *skill* and a profile state
*lit* is hit, the following six(!) events will be posted:


+ lanes_skill_lit_hit
+ lanes_skill_hit
+ lanes_hit
+ left_lane_skill_lit_hit
+ left_lane_skill_hit
+ left_lane_hit


This lets you dial-in on the amount of precision you need when you're
tying game logic to shots and shot groups.



<name>:
~~~~~~~

Create one entry in your *shot_groups:* section for each group of
shots in your machine. This name can be whatever you want, and it will
be the name for this shot group which is used throughout your machine.



shots:
~~~~~~

The list of shots (from the *shots:* section of your config file) that
make up this shot group. Note that order is important here if you want
to implement shot rotation events. Individual shots can belong to more
than group at the same time, which is useful in a lot of different
situations. For example, you might have three banks of three standup
targets each, and you can create shot groups for each bank with events
that will be triggered when the individual bank is complete, and then
you can create a fourth shot group with all nine targets in it which
could post different events when all nine targets have been hit.



profile:
~~~~~~~~

The name of the `shot profile`_ that will be applied to all the shots
in this shot group.


+ If you’re editing a machine-wide config file , then the profile name
  specified here will be the default profile for each shot in the group
  any time a mode-specific config doesn’t override it. (If you don’t
  specify a profile name, MPF will assign the shot profile called
  “default”.)
+ If you’re in a mode configuration file , then this profile entry is
  the name of the shot profile that will be applied to each shot in this
  group only when this mode is active. (i.e. it’s applied when the mode
  starts and it’s removed when the mode ends.) Like other mode-specific
  settings, shot profiles take on the priorities of the modes they’re
  in, so if you have a profile from a mode at priority 200 and another
  from priority 300, the profile from the priority 300 mode will be
  applied. If that mode stops, then the shot will get the profile from
  the priority 200 mode.




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
event documentation`_. Shot groups make use of the following device
control events:



rotate_left_events:
~~~~~~~~~~~~~~~~~~~

This list of events that, when posted, will rotate the current state
of each shot to the shot to its left. The state of left-most (i.e.
first entry) in your shots: list will rotate over to the right-most
shot. These states are based on whatever shot profile is active at
that time.



rotate_right_events:
~~~~~~~~~~~~~~~~~~~~

This list of events that, when posted, will rotate the current lit and
unlit shot states to the right. This can be a simple list of events or
a `time-delayed list`_. The state of right-most (i.e. lastentry) in
your `shots:` list will rotate over to the left-most shot.



rotate_events:
~~~~~~~~~~~~~~

This list of events that, when posted, will rotate the current shot
states in the direction specified in the profile's `custom_rotation:`
setting. This can be a simple list of events or a `time-delayed
list`_. This lets you implement custom left-right patterns (like four
left, then four right) like the moving lit shot skillshot on the bank
of five targets in T2.



enable_rotation_events:
~~~~~~~~~~~~~~~~~~~~~~~

A list of one or more events that will allow the states of the shots
in this group to be rotated (based on the *rotate_left_events*,
*rotate_right_events*, or *rotate_events* as described above). This
can be a simple list of events or a `time-delayed list`_. If rotation
is not enabled, rotation events being posted will have no effect.
(Rotation is enabled by default.)



disable_rotation_events:
~~~~~~~~~~~~~~~~~~~~~~~~

A list of one or more events that will disable rotation, meaning the
states of the shots in this group will not be rotated if one of the
*rotate_left_events*, *rotate_right_events*, or *rotate_events* is
posted. This can be a simple list of events or a `time-delayed list`_.



enable_events:
~~~~~~~~~~~~~~

A list of one or more events that will enable this shot group.
(Enabling a shot group will also enable all of the individual shots
that make up this group.) This can be a simple list of events or a
`time-delayed list`_. If a shot group is not enabled, then it will not
post hit events and shot rotation is disabled. If you do not specify
any enable_events, then MPF will automatically create enable events
based on the list in the `config_validator: shot_groups:
enable_events:` section of your machine-wide config. (By default
that's *ball_started*, meaning your shot groups are automatically
enabled when a ball starts.) If you specify any *enable_events* in
your machine-wide config, then none of the default enable events will
be added. (i.e. if you also want to include the default
*enable_events*, you will have to add them here too.) If you specify
any *enable_events* in a mode-specific config, then those events are
only active during that mode. Mode-specific *enable_events* are in
addition to machine-wide *enable_events*.



disable_events:
~~~~~~~~~~~~~~~

A list of one or more events that will disable this shot group. This
can be a simple list of events or a `time-delayed list`_. If you do
not specify any disable_events, then MPF will automatically create
*disable_events* based on the list in the `config_validator:
shot_groups: disable_events:` section of your machine-wide config. (By
default that's *ball_ended*.) If you specify any *disable_events* in
your machine-wide config, then none of the default *disable_events*
will be added. (i.e. if you also want to include the default
*disable_events*, you will have to add them here too.) If you specify
any *disable_events* in a mode-specific config, then those events are
only active during that mode. Mode-specific *disable_events* are in
addition to machine-wide *disable_events*.



reset_events:
~~~~~~~~~~~~~

A list of one or more events that will reset all the shots in this
shot group. This can be a simple list of events or a `time-delayed
list`_. Resetting a shot group means that every shot in the group
jumps back to the first state in whatever `shot profile`_ is active at
that time.



advance_events:
~~~~~~~~~~~~~~~

A list of one or more events that will advance all the shots in this
shot group one step in the active profile. This can be a simple list
of events or a `time-delayed list`_. Advancing a shot does not post
hit events and therefore does not trigger scoring or other events
related to a shot hit. They are useful if you need to move a shot to a
starting state.



remove_active_profile_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A list of one or more events that will cause the active shot profile
to be removed from every shot in the group, and the next-highest
priority profile to be applied. This can be a simple list of events or
a `time-delayed list`_.



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

.. _shot profile: https://missionpinball.com/docs/configuration-file-reference/target_profiles/
.. _shots: https://missionpinball.com/docs/configuration-file-reference/shots/
.. _time-delayed list: https://missionpinball.com/docs/configuration-file-reference/configuring-device-control-events/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


