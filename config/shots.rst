shots:
======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

The *shots:* section of your config file is where you define
the shots in your machine. A *shot* is a switch, a series of
switches that have to be hit in order, or an event or series of events.

Shots are used for things like standup
targets, rollover lanes, drop targets, ramps, loops, orbits, etc.

Each shot can have a *shot profile* applied to it which defines what
happens when its hit. For example the shot profile might specify that the shot starts unlit,
then when it's hit it becomes complete. Or a shot profile might
specify that it's flashing slowly, and each hit makes it flash faster
and faster until it's been hit enough times, etc.

You can specify different shot profile on a per-mode basis, meaning a shot
can have one behavior in the base mode and then take on another behavior when
a higher-priority mode is started. The tracking of various states of the
shot profiles is maintained on a per-mode basis.

You can group multiple shots together into *shot groups* for group-level
functionality like posting events when all the shots in a group in the
same state (lit, unlit, complete, etc.) and for rotating the states
of shots to the left or right based on certain events happening
(slingshot hits, flipper button pushes, etc.). A shot can be a member of
multiple groups at the same time.

Typically you'd define your shots in your machine-wide config (since the
actual physical shots in your machine are defined by hardware and never
change), and then you apply different profiles to the shots in various
modes.

Here's a sample *shots:* section from a config file:

.. code-block:: mpf-config

    #! switches:
    #!    lane_l:
    #!       number:
    #!    lane_a:
    #!       number:
    #!    lane_n:
    #!       number:
    #!    lane_e:
    #!       number:
    #!    upper_standup:
    #!       number:
    ##! config: mode1
    shots:
        lane_l:
            switch: lane_l
            show_tokens:
                light: lane_l
        lane_a:
            switch: lane_a
            show_tokens:
                light: lane_a
        lane_n:
            switch: lane_n
            show_tokens:
                light: lane_n
        lane_e:
            switch: lane_e
            show_tokens:
                light: lane_e
        upper_standup:
            switch: upper_standup
            show_tokens:
                leds: led_17, led_19

Create one entry in your ``shots:`` section for each shot in your
machine. Don't worry about grouping shots here. (That's done in the
``shot_groups:`` section.) The shot name can be whatever you want, and
it will be the name for this shot which is used throughout your
machine. Remember that everything with at least one switch and a
"state" is a shot, so standups, rollovers, inlane/outlines, ramps,
loops... You will have lots of shots in your game.

Each shot in your ``shots:`` section can have the following config options set:

Optional settings
-----------------

The following sections are optional in the ``shots:`` section of your config. (If you don't include them, the default will be used).

advance_events:
~~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause this shot to be advanced
to its next state in the active shot profile. If the shot is on the
last state, then it will roll over if the shot profile is configured
to loop, otherwise it will do nothing. *Advance_events* are similar to
*hit_events*, except *advance_events* are more "stealthy" in that they
only advance the state (and update the lights or LEDs). They do not
post hit events and therefore do not trigger scoring or other events
related to a shot hit. They are useful if you need to move a shot to a
starting state (like selecting a shot to be active for skill shot).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set this to *true* to add lots of logging information about this shot
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot.

disable_events:
~~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, disable this shot. If a shot is
disabled, then hits to it have no effect. (e.g. The shot will remain
in whatever state it's in.)

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, enable this shot. If a shot is
not enabled, then hits to it have no effect. (e.g. The shot will
remain in whatever state it's in.)

hit_events:
~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, cause this shot to be "hit".
This is effectively the same thing as if the ball activated the switch
associated with this shot, (or that the entire switch sequence has
been completed), except it comes in via an event instead of from a
switch activity.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

The plain-English name for this device that will show up in operator
menus and trouble reports.

profile:
~~~~~~~~
Single value, type: ``string``. Default: ``profile``

The name of the *shot profile* that will be applied to this shot.

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

Shots can have (and track) multiple profiles at the same time (up to one
profile per mode). Only the show from the highest-priority profile will
play though.

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, reset this shot. Resetting a
shot means that it jumps back to the first state in whatever *shot
profile* is active at that time.

restart_events:
~~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, restart this shot. Restarting a shot is
equivalent to resetting and then enabling the shot, done with a single event.

show_tokens:
~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

A subsection containing key-value pairs that are passed to the show that's
run when this shot is in a certain state.

For example, consider the following shot config:

.. code-block:: mpf-config

   #! switches:
   #!    switch1:
   #!       number:
   ##! config: mode1
   shot_profiles:
       flash:
           states:
             - name: unlit
               show: "off"
             - name: lit
               show: "flash"

   shots:
      shot1:
         switch: switch1
         profile: flash
         show_tokens:
            leds: led1

The shot above has a show token called *leds* which is set to *led1*. This means that when
a show associated with this shot is played, if that show contains placeholder tokens for ``(leds)``,
they will be dynamically replaced with the value of ``led1`` when that show is played by this shot.

The purpose of show tokens is so you can create resuable shows that you could apply to any shot.

For example, imagine if you wanted to create a shot to flash an LED between red and off. It might look like this:

.. code-block:: mpf-config

  # show to flash an LED
  shows:
   flash_light:
    - time: 0
      lights:
        (leds): red
    - time: 1
      lights:
        (leds): off

Assuming the "flash" profile (as defined in the ``profile: flash`` in the above shot) was configured for the state
that show was in, when the shot entered that state, it would replace the ``(leds):`` section of the show with ``led1``.

More information about :doc:`show tokens </shows/tokens>`

switch:
~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

The name of the switch (or a list of switches) for this shot. You can
use multiple switches if the shot happens to have multiple switches,
though this is rare. (Maybe there are two standups on the sides of a
ramp that you always want to be the same so you just create them as
one logical shot?)

Do *not* enter multiple switches here for different
shots, like for a bank of rollover lanes. In that case you would set up
each shot as its own shot here and then group them via ``shot_groups:``.

Also do *not* enter multiple switches if you want the shot to be
complete when all the switches are hit. (That's what the
``switch_sequence:`` setting is for.) Entering multiple switches here is
just in case you have a shot where you want any of the switches being
hit to count as that shot being hit.

switches:
~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

This setting is the same as the ``switch:`` setting above. You can technically
enter a single switch or a list of switches in either the ``switch:`` setting
or the ``switches:`` setting, but we include both since it was confusing to
be able to enter multiple switches for a singlular "switch" setting and vice
versa.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more tags that apply to this device. Tags allow you
to access groups of devices by tag name.
