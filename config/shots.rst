shots:
======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

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

Here's a sample *shots:* section from a config file:

.. code-block:: mpf-config

    #! switches:
    #!   lane_l:
    #!     number:
    #!   lane_a:
    #!     number:
    #!   lane_n:
    #!     number:
    #!   lane_e:
    #!     number:
    #!   upper_standup:
    #!     number:
    ##! mode: mode1
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

.. config


Optional settings
-----------------

The following sections are optional in the ``shots:`` section of your config. (If you don't include them, the default will be used).

advance_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

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

delay_switch:
~~~~~~~~~~~~~
One or more sub-entries. Each in the format of string name of a :doc:`switches <switches>` device : ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`)

A dictionary of switches and times which prevent hits for a certain time.
You can use this if you got another lane feeding into your shot and you want to
prevent it from hitting this shot.
Use this with care as it might cause issues during multiball.

This is an example:

.. code-block:: mpf-config

    #! switches:
    #!   s_my_shot:
    #!     number:
    #!   s_other_lane:
    #!     number:
    ##! mode: mode1
    shots:
      my_shot:
        switch: s_my_shot
        delay_switch:
          s_other_lane: 2s
    ##! test
    #! start_game
    #! start_mode mode1
    #! mock_event my_shot_hit
    #! hit_and_release_switch s_other_lane
    #! hit_and_release_switch s_my_shot
    #! advance_time_and_run .1
    #! assert_event_not_called my_shot_hit
    #! hit_and_release_switch s_my_shot
    #! advance_time_and_run .1
    #! assert_event_not_called my_shot_hit
    #! advance_time_and_run 2
    #! hit_and_release_switch s_my_shot
    #! advance_time_and_run .1
    #! assert_event_called my_shot_hit

In this example an activation of ``s_other_lane`` will prevent the shot from being hit for two seconds.

disable_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, disable this shot. If a shot is
disabled, then hits to it have no effect. (e.g. The shot will remain
in whatever state it's in.)

enable_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, enable this shot. If a shot is
not enabled, then hits to it have no effect. (e.g. The shot will
remain in whatever state it's in.)

hit_events:
~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, cause this shot to be "hit".
This is effectively the same thing as if the ball activated the switch
associated with this shot, (or that the entire switch sequence has
been completed), except it comes in via an event instead of from a
switch activity.

persist_enable:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Whether this shot should persist its enable state in a player variable.
If set to ``True`` this will also persist the state into the next ball
of the same player.

playfield:
~~~~~~~~~~
Single value, type: string name of a :doc:`playfields <playfields>` device. Default: ``playfield``

On which playfield is this shot?
This is only relevant when you have multiple playfields.
It is used mostly for ball search.

profile:
~~~~~~~~
Single value, type: string name of a :doc:`shot_profiles <shot_profiles>` device. Default: ``default``

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
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, reset this shot. Resetting a
shot means that it jumps back to the first state in whatever *shot
profile* is active at that time.

restart_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, restart this shot. Restarting a shot is
equivalent to resetting and then enabling the shot, done with a single event.

show_tokens:
~~~~~~~~~~~~
One or more sub-entries. Each in the format of ``string`` : template_str

A subsection containing key-value pairs that are passed to the show that's
run when this shot is in a certain state.

For example, consider the following shot config:

.. code-block:: mpf-config

   #! switches:
   #!   switch1:
   #!     number:
   ##! mode: mode1
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

start_enabled:
~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Defaults to empty.

Whether the shot starts as enabled (if you set this to ``True``) or as
disabled (if you set this to ``False``).
If you do not set this, MPF will check if there are ``enable_events``.
The shot will start disabled in that case or enabled otherwise.

switch:
~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

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
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

This setting is the same as the ``switch:`` setting above. You can technically
enter a single switch or a list of switches in either the ``switch:`` setting
or the ``switches:`` setting, but we include both since it was confusing to
be able to enter multiple switches for a singlular "switch" setting and vice
versa.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to *true* to add lots of logging information about this shot
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

The plain-English name for this device that will show up in operator
menus and trouble reports.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

A list of one or more tags that apply to this device. Tags allow you
to access groups of devices by tag name.


Related How To guides
---------------------

* :doc:`/game_logic/shots/index`
