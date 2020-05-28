shot_groups:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

You can group shots together via the ``shot_groups:`` section of your config file.

For example:

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
    #! shots:
    #!   lane_l:
    #!     switch: lane_l
    #!     show_tokens:
    #!       light: lane_l
    #!   lane_a:
    #!     switch: lane_a
    #!     show_tokens:
    #!       light: lane_a
    #!   lane_n:
    #!     switch: lane_n
    #!     show_tokens:
    #!       light: lane_n
    #!   lane_e:
    #!     switch: lane_e
    #!     show_tokens:
    #!       light: lane_e
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
  same, it will post a "complete" event (in the form of *<shot_group_name>_<active_profile_name>_<profile_state_name>_complete*)
  which you can use to trigger scores based on complete, light shows,
  shot group resets, etc.
+ Any time a member shot is hit, MPF will post an event (in the form
  of *<shot_group_name>_<profile_name_of_shot_that_was_hit>_<profile_state_name_of_shot_that_was_hit>_hit*).
  You can use this to tie
  scoring, sounds, or logic blocks to any shot being hit in a group,
  which can be easier than creating entries for each individual shot.
+ Any time a member shot is hit, MPF will post an event (in the form
  of *<shot_group_name>_<profile_name_of_shot_that_was_hit>_hit*)
+ Any time a member shot is hit, MPF will post an event (in the form
  of *<shot_group_name>_hit*)


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

.. config


Optional settings
-----------------

The following sections are optional in the ``shot_groups:`` section of your config. (If you don't include them, the default will be used).

disable_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

A list of one or more events that will disable all the shots in this shot group. This
can be a simple list of events or a time-delayed list. If you do
not specify any disable_events, then MPF will automatically create
*disable_events* based on the list in the `config_validator:
shot_groups: disable_events:` section of your machine-wide config. (By
default that's *ball_ended*.)

disable_rotation_events:
~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

A list of one or more events that will disable rotation, meaning the
states of the shots in this group will not be rotated if one of the
*rotate_left_events*, *rotate_right_events*, or *rotate_events* is
posted. This can be a simple list of events or a time-delayed list.

enable_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

A list of one or more events that will enable all of the individual shots
in this shot group. (The shot group itself has no enabled/disabled state
except for rotation.) This can be a simple list of events or a
time-delayed list. If a shot in the group is not enabled, then it will not
post hit events but it *will* still rotate its profile state when the shot group
rotates.

The presence or absence of this value will not affect whether individual shots
in the group can be enabled via their own `enable_events` settings. An individual
shot can always be enabled/disabled regardless of the group state, although
a subsequent group enable/disable events will also affect that individual shot.

enable_rotation_events:
~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

A list of one or more events that will allow the states of the shots
in this group to be rotated (based on the *rotate_left_events*,
*rotate_right_events*, or *rotate_events* as described above). This
can be a simple list of events or a time-delayed list. If rotation
is not enabled, rotation events being posted will have no effect.
(Rotation is enabled by default.)

reset_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

A list of one or more events that will reset all the shots in this
shot group. This can be a simple list of events or a time-delayed list.
Resetting a shot group means that every shot in the group
jumps back to the first state in whatever shot profile is active at
that time.

restart_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

A list of one or more events that will restart all the shots in this shot group.
A restart is the same as calling reset and enable, so restarting a shot group
will jump every shot in the group to the first state of that shot's profile and
immediately enable all the shots.

rotate_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Same as ``rotate_right_events:``.

rotate_left_events:
~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

This list of events that, when posted, will rotate the current state
of each shot to the shot to its left. The state of left-most (i.e.
first entry) in your shots: list will rotate over to the right-most
shot. These states are based on whatever shot profile is active at
that time.

rotate_right_events:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

This list of events that, when posted, will rotate the current lit and
unlit shot states to the right. This can be a simple list of events or
a time-delayed list. The state of right-most (i.e. last entry) in
your `shots:` list will rotate over to the left-most shot.

shots:
~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`shots <shots>` device. Defaults to empty.

The list of shots (from the ``shots:`` section of your config file) that
make up this shot group. Order is important here if you want
to implement shot rotation events. Individual shots can belong to more
than group at the same time, which is useful in a lot of different
situations. For example, you might have three banks of three standup
targets each, and you can create shot groups for each bank with events
that will be triggered when the individual bank is complete, and then
you can create a fourth shot group with all nine targets in it which
could post different events when all nine targets have been hit.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to *true* to add lots of logging information about this shot
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot. Default is *False*.

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

* :doc:`/game_logic/shots/shot_group`
* :doc:`/game_logic/skill_shot/index`
* :doc:`/game_logic/shots/sequence_shots`
