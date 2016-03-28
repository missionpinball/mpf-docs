
The *shots:* section of yourconfig files is where you setup
the`shots`_ in your machine. A *shot* is a switch (or a series of
switches that have to be hit in order), typically with a light or LED
that reflects the current state of the shot (unlit, lit, complete,
flashing, etc.). Shots can be things like standup targets, rollover
lanes, drop targets, ramps, loops, orbits, etc. This sectioncan be
used in your machine-wide config files. This section can beused in
mode-specific config files. Shots can have different *shot profiles*
applied to them. A shot profile controls what happens when a shot is
hit. For example the profile might specify that the shot starts unlit,
then when it's hit it becomes complete. Or a shot profile might
specify that it's flashing slowly, and each hit makes it flash faster
and faster until it's been hit enough times, etc. You can group
multiple shots together into *shot groups* for group-level
functionality like posting events when all the shots in a group in the
same state (lit, unlit, complete, etc.) and forrotatingthe states
ofshots to the left or right based on certain events happening
(slingshot hits, flipper button pushes, etc.). A shot can be a member
of multiple groups at the same time. You can add shots to your
machine-wide config file or to a mode-specific config file. Shots in
your machine-wide config will always be available, and shots in mode-
specific configs will be created and then removed as the mode is
active or inactive. (Shots can be enabled and disabled by game logic,
so just because a shot exists in your machine-wide config doesn't
necessarily mean that it's always enabled.) You can also choose to
create the shots in your machine-wide config, but then to add entries
for them in mode configs to modify their behavior while that mode is
active. (Per-mode shot profiles and control events, for example.)
Here's a sample *shots:* section from a config file:


::

    
    shots:
        lane_l:
            switch: lane_l
            light: lane_l
        lane_a:
            switch: lane_a
            light: lane_a
        lane_n:
            switch: lane_n
            light: lane_n
        lane_e:
            switch: lane_e
            light: lane_e
        upper_standup
            switch: upper_standup
            led: led_17, led_19
        right_ramp:
            switch_sequence: right_ramp_enter, right_ramp_made
            time: 2s
        left_orbit:
            switch_sequence: left_rollover, top_right_opto
            time: 3s
        weak_right_orbit:
            switch_sequence: top_right-opto, top_center_rollover
            time: 3s
        full_right_orbit:
            switch: top_right_opto, left_rollover
            time: 3s


Let's lookat each of these configuration options in detail.



<name>:
~~~~~~~

Create one entry in your `shots:` section for each shot in your
machine. Don't worrying about grouping shots here. (That's done in the
`shot_groups:` section.) The shot name can be whatever you want, and
it will be the name for this shot which is used throughout your
machine. Remember that everything with at least one switch and a
"state" is a shot, so standups, rollovers, inlane/outlines, ramps,
loops... You will have lots of shots in your game.



switch:
~~~~~~~

The name of the switch(or a list of switches) for this shot. You can
use multiple switches if the shot happens to have multiple switches,
though this is rare. (Maybe there are two standups on the sides of a
ramp that you always want to be the same so you just create them as
one logical shot?) Do *not* enter multiple switches here for different
shots, like for a bank of rollover lanes. In that case you would setup
each shot as its own shot here and then group them via `shot_groups:`.
Also do *not* enter multiple switches if you want the shot to be
complete when all the switches are hit. (That's what the
`switch_sequence:` setting is for.) Entering multiple switches here is
just in case you have a shot where you want any of the switches being
hit to count as that shot being hit.



switch_sequence:
~~~~~~~~~~~~~~~~

A *switch_sequence* is where you configure your shot so that multiple
switches have to be hit, in order, for the shot to be registered as
hit. You can optionally specify a time limit for these switches (i.e.
the sequence must be completed within the time limit) with the `time:`
setting. When the first switch in a sequence is activated, the shot
will start watching for the next one. When that one is activated, it
looks for the next, and so on. Once the last switch is activated, the
shot is considered "hit". Notice in the example above that there are
two different shots with the same switches, but the order of the
switches is inverted between the two. This is because the *left orbit*
and *right orbit* shots in this machine use the same two switches, but
the order the switches are activated in dictates which shot was just
made. Shots in MPF are able to track multiple simultaneous sequences
in situations which is nice when multiple balls are on the playfield.
If the first switch in a sequence is hit twice before the sequence
completes, MPF will start tracking two sequences. Then when the next
switch is it, it will only advance one sequence. If the next switch is
hit again, it will advance the other sequence. But if the next switch
is never hit a second time, then the second shot will not complete.



time:
~~~~~

This is the time limit these switches have to be activated in, from
start to finish, in order for the shot to be posted. You can enter
values with "s" or "ms" after the number, like `200ms` or `3s`. If you
just enter a number then the system assumes you mean seconds. If you
do not enter a time, or you enter a value of 0, then there is no
timeout (i.e. the player could literally take multiple minutes between
switch activations and the shot would count.)



cancel_switch:
~~~~~~~~~~~~~~

A switch (or list of switches) that will cause any in-progress switch
sequence tracking to be canceled. (Think of it like a cancel "abort"
switch.) If you enter more than one switch here, any of them being hit
will cause the sequence tracking to reset. If MPF is currently
tracking multiple in-process sequences, a cancel_switch hit will
cancel all of them.



delay_switch:
~~~~~~~~~~~~~

This lets you specify a switch along with a time value that will
prevent this shot from tracking from being hit. In other words, the
shot only counts if the delay_switch was *not* hit within the time
specified. If you use this with a single switch shot, then the time
must pass before the shot will count. If you use this with a
switch_sequence, then the time must pass before a new sequence will
start to be tracked. Enter this switch with a time value (in seconds
or ms), like this:


::

    
    shots:
      mode_start:
        switch: mode_start
        delay_switch:
          rear_entry: 1.5s
      rear_entry_mode_start:
        switch_sequence: rear_entry, mode_start
        time: 1.5s


The example above illustrates a typical use for this where you have a
single switch which you can hit from the front, and then also a rear
entry where a rear switch is hit then the main switch. Setting up the
switch sequence for the rear entry is easy, but without the
delay_switch on the front entry, then a ball going in the rear entry
would trigger a hit event for the front shot too.



light:
~~~~~~

The name of the lamp matrix-based light associated with this shot.
This can be a list of multiple lights if you want to have multiple
lights tied to this shot. (Note: You'll likely only use `light:` or
`led:`, but not both, depending on whether your machine uses a lamp
matrix or direct controlled LEDs.)



led:
~~~~

The name of the LEDassociated with this shot. This can be a list of
multiple LEDsif you want to have multiple LEDstied to this shot.



profile:
~~~~~~~~

The name of the `shot profile`_ that will be applied to this shot.


+ If you're editing a machine-wide config file , then the profile name
  specified here will be the default profile for that shot any time a
  mode-specific config doesn't override it. (If you don't specify a
  profile name, MPF will assign the shot profile called "default".)
+ If you're in a mode configuration file , then this profile entry is
  the name of the shot profile that will be applied only when this mode
  is active. (i.e. it's applied when the mode starts and it's removed
  when the mode ends.) Like other mode-specific settings, shot profiles
  take on the priorities of the modes they're in, so if you have a
  profile from a mode at priority 200 and another from priority 300, the
  profile from the priority 300 mode will be applied. If that mode
  stops, then the shot will get the profile from the priority 200 mode.


Only one profile can be active at a time. (Though if you're really
crazy and you need to track multiple profiles, you can configure the
same switch and same light to be part of two different shots, and each
one of them can have its own shot profile.)



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
event documentation`_. Shots make use of the following device control
events:



enable_events:
~~~~~~~~~~~~~~

A list of one or more events that will enable this shot. If a shot is
not enabled, then hits to it have no effect. (e.g. The shot will
remain in whatever state it's in.) Default is *None*.



disable_events:
~~~~~~~~~~~~~~~

A list of one or more events that will disable this shot. If a shot is
disabled, then hits to it have no effect. (e.g. The shot will remain
in whatever state it's in.) Default is *None*.



reset_events:
~~~~~~~~~~~~~

A list of one or more events that will reset this shot. Resetting a
shot means that it jumps back to the first state in whatever `shot
profile`_ is active at that time. Default is *None*.



hit_events:
~~~~~~~~~~~

A list of one or more events that will cause this shot to be "hit".
This is effectively the same thing as if the ball activated the switch
associated with this shot, (or that the entire switch sequence has
been completed), except it comes in via an event instead of from a
switch activity. Default is *None*.



advance_events:
~~~~~~~~~~~~~~~

A list of one or more events that will cause this shot to be advanced
to its next state in the active shot profile. If the shot is on the
last state, then it will roll over if the shot profile is configured
to loop, otherwise it will do nothing. *Advance_events* are similar to
*hit_events*, except *advance_events* are more "stealthy" in that they
only advance the state (and update the lights or LEDs). They do not
post hit events and therefore do not trigger scoring or other events
related to a shot hit. They are useful if you need to move a shot to a
starting state (like selecting a shot to be active for skill shot).
Default is *None*.



remove_active_profile_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A list of one or more events that will cause the active shot profile
to be removed, and the next-highest priority profile to be applied.
Default is *None*.



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

.. _shot profile: https://missionpinball.com/docs/configuration-file-reference/shot_profiles/
.. _shots: https://missionpinball.com/docs/mpf-core-architecture/devices/shot/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


